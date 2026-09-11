"""
Generate every figure for the USRT results report.

Output: vector PDF into ALL_DOCS/figures/, sized for the two-column
`\documentclass[10pt,twocolumn]{article}` in heuristic_v5_report.tex.
Drop straight in with \includegraphics -- the preamble already has graphicx.

    single column  : 3.4 in wide   -> \begin{figure}
    full width     : 7.0 in wide   -> \begin{figure*}

Data sources (deliberately different per figure):
  * trend curves + runtime  -> tc_sept_small / tc_sept_paper  (100 sets per
    configuration, so the curves are smooth enough to publish)
  * distributions + scatter -> tc_unavg (5 sets, every instance kept separate,
    which is the whole point of those plots)

Style is print-safe: colour AND a distinct marker + dash pattern per model, so
the figures survive greyscale printing and photocopying.

Usage:  python make_figures.py
"""

import csv, glob, os, collections, statistics

import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

OUT = os.path.join('ALL_DOCS', 'figures')
COL, FULL = 3.4, 7.0

# ── model presentation ───────────────────────────────────────────────────────
# All nine are plotted.  Colour alone cannot separate nine series in greyscale,
# so every model also gets its own marker and dash pattern.
MODELS = [
    ('greedy_sps_baseline',     'Baseline',   '#8c8c8c', 'o', (0, (1, 1))),
    ('heuristic_v3',            'v3',         '#9467bd', 'v', (0, (4, 2))),
    ('heuristic_v4',            'v4',         '#8c564b', '^', (0, (6, 2))),
    ('heuristic_v5a',           'v5a',        '#e377c2', '<', (0, (3, 1, 1, 1))),
    ('heuristic_v5b',           'v5b',        '#1f77b4', '>', (0, (5, 1))),
    ('heuristic_claudeoptimal', 'DoubleP6',   '#ff7f0e', 's', (0, (3, 1, 1, 1, 1, 1))),
    ('ilp_v2',                  'ILP v2',     '#2ca02c', 'D', (0, (2, 2))),
    ('ilp_v3',                  'ILP v3',     '#bcbd22', 'h', (0, (4, 1, 1, 1))),
    ('heuristic_v7',            'v7',         '#17becf', 'X', (0, (7, 1, 1, 1))),
    ('heuristic_v6',            'v6',         '#d62728', 'P', (0, ())),
    # ILP v1 is the optimality reference: its own gap is 0 by construction, so in
    # the gap figures it is the zero line -- included so "distance to optimal" is
    # explicit rather than implied.  In runtime/feasibility it is a real series.
    ('ilp_v1',                  'ILP v1',     '#000000', '*', (0, ())),
]
SWEEPLAB = {'rho': r'$\rho$  (energy budget)', 'u_mand_factor': r'$\alpha$  (mandatory util.)',
            'u_opt_factor': r'$\beta$  (optional util.)', 'n_prc': r'$N_{prc}$',
            'n_tsk': r'$N_{tsk}$', 'n_frq': r'$N_{frq}$', 'xi': r'$\xi$  (ACET spread)'}
# xi is deliberately absent from the OFAT figure: the offline models never read
# the per-task theta, so that panel is a flat line by construction.
ORDER = ['rho', 'u_mand_factor', 'u_opt_factor', 'n_frq', 'n_tsk', 'n_prc']

plt.rcParams.update({
    'font.size': 8, 'axes.labelsize': 8, 'axes.titlesize': 8,
    'xtick.labelsize': 7, 'ytick.labelsize': 7, 'legend.fontsize': 6.5,
    'axes.grid': True, 'grid.alpha': 0.25, 'grid.linewidth': 0.4,
    'axes.spines.top': False, 'axes.spines.right': False,
    'figure.dpi': 200, 'savefig.bbox': 'tight', 'savefig.pad_inches': 0.02,
    'lines.linewidth': 1.1, 'lines.markersize': 3.2,
})


def load(root):
    """{(sweep, value, set): {model: row}} plus the manifest row."""
    inst = {}
    for m in sorted(glob.glob(os.path.join(root, '*', 'manifest.csv'))):
        sw = os.path.basename(os.path.dirname(m))
        man = {r['file']: r for r in csv.DictReader(open(m))}
        rf = os.path.join(os.path.dirname(m), 'results.csv')
        if not os.path.exists(rf):
            continue
        res = collections.defaultdict(dict)
        for r in csv.DictReader(open(rf)):
            res[r['file']][r['model']] = r
        for f, mr in man.items():
            inst[(sw, mr['value'], int(mr['set']), root, f)] = {'man': mr, 'res': res.get(f, {})}
    return inst


def util(rec, model):
    r = rec['res'].get(model)
    if not r or r.get('model_feasible') != '1' or not r.get('utility'):
        return None
    return float(r['utility'])


def gap(rec, model, ref='ilp_v1'):
    o, u = util(rec, ref), util(rec, model)
    if o is None or u is None or o <= 0:
        return None
    return 100 * (o - u) / o


def savefig(fig, name):
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, name)
    fig.savefig(p)
    plt.close(fig)
    print('  ', p)


# ── FIG 1: gap distribution per model (unaveraged) ───────────────────────────
def fig_distribution(unavg):
    data, labels, colours = [], [], []
    for key, lab, c, _mk, _ls in MODELS:
        g = [x for x in (gap(r, key) for r in unavg.values()) if x is not None]
        if g:
            data.append(g); labels.append(lab); colours.append(c)
    fig, ax = plt.subplots(figsize=(FULL, 2.6))
    bp = ax.boxplot(data, patch_artist=True, widths=0.6, showfliers=True,
                    flierprops=dict(marker='.', markersize=2, alpha=0.45,
                                    markerfacecolor='#333', markeredgecolor='none'),
                    medianprops=dict(color='black', linewidth=1.2),
                    whiskerprops=dict(linewidth=0.7), capprops=dict(linewidth=0.7))
    for patch, c in zip(bp['boxes'], colours):
        patch.set_facecolor(c); patch.set_alpha(0.45); patch.set_linewidth(0.7)
    ax.set_xticklabels(labels, rotation=20, ha='right')
    ax.set_ylabel(r'optimality gap vs ILP v1 (\%)' if plt.rcParams['text.usetex']
                  else 'optimality gap vs ILP v1 (%)')
    ax.set_title('Per-instance gap distribution (220 instances, no averaging)')
    ax.axhline(0, color='black', linewidth=0.6, alpha=0.5)
    savefig(fig, 'fig1_gap_distribution.pdf')


# ── FIG 2: OFAT small multiples (big campaign) ───────────────────────────────
def fig_ofat(big):
    bysweep = collections.defaultdict(lambda: collections.defaultdict(list))
    for (sw, v, s, root, f), rec in big.items():
        for key, *_ in MODELS:
            g = gap(rec, key)
            if g is not None:
                bysweep[sw][(v, key)].append(g)
    fig, axes = plt.subplots(2, 3, figsize=(FULL, 3.9), sharey=True)
    axes = axes.ravel()
    for i, sw in enumerate(ORDER):
        ax = axes[i]
        vals = sorted({v for (v, k) in bysweep[sw]}, key=float)
        for key, lab, c, mk, ls in MODELS:
            xs, ys = [], []
            for v in vals:
                g = bysweep[sw].get((v, key), [])
                if g:
                    xs.append(float(v)); ys.append(statistics.mean(g))
            if xs:
                ax.plot(xs, ys, marker=mk, color=c, linestyle=ls, label=lab,
                        markeredgewidth=0.4,
                        zorder=3 if key == 'ilp_v1' else 2,
                        linewidth=1.3 if key == 'ilp_v1' else 1.1)
        ax.set_xlabel(SWEEPLAB[sw])
        if i % 3 == 0:
            ax.set_ylabel('mean gap vs ILP v1 (%)')
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, loc='lower center', frameon=False, ncol=5,
               bbox_to_anchor=(0.5, -0.10), columnspacing=1.4, handlelength=2.6)
    fig.suptitle('Optimality gap against each swept factor (100 test cases per point)',
                 fontsize=8.5, y=1.00)
    fig.tight_layout(w_pad=0.6, h_pad=1.0, rect=(0, 0.02, 1, 0.97))
    savefig(fig, 'fig2_ofat_smallmultiples.pdf')


# ── FIG 3: v6 vs v7 per instance (unaveraged) ───────────────────────────────
def fig_v6_v7(unavg):
    xs, ys = [], []
    for rec in unavg.values():
        a, b = util(rec, 'heuristic_v6'), util(rec, 'heuristic_v7')
        if a is not None and b is not None:
            xs.append(a); ys.append(b)
    same = sum(1 for a, b in zip(xs, ys) if abs(a - b) < 1e-6)
    fig, ax = plt.subplots(figsize=(COL, 2.7))
    lim = max(max(xs), max(ys)) * 1.05
    ax.plot([0, lim], [0, lim], color='black', linewidth=0.7, alpha=0.5, zorder=1)
    ax.scatter(xs, ys, s=11, facecolor='#d62728', edgecolor='none', alpha=0.55, zorder=2)
    ax.set_xlim(0, lim); ax.set_ylim(0, lim)
    ax.set_xlabel('v6 utility'); ax.set_ylabel('v7 utility')
    ax.set_title('v6 vs v7, per instance\n%d identical, %d differ' % (same, len(xs) - same))
    ax.set_aspect('equal', adjustable='box')
    savefig(fig, 'fig3_v6_vs_v7.pdf')


# ── FIG 4: runtime vs problem size (big campaign) ───────────────────────────
def fig_runtime(big, time_limit_ms=10000):
    """
    Median runtime against problem size.

    ILP v1 is CENSORED by the solver time limit: beyond J ~ 45 most instances hit
    the 10 s cap, so its median is the cap, not the true cost.  Those buckets are
    drawn hollow and the cap is marked -- otherwise the figure would claim ILP v1
    plateaus when in reality its cost is unbounded above the line.
    """
    byJ = collections.defaultdict(lambda: collections.defaultdict(list))
    censored = collections.defaultdict(lambda: collections.defaultdict(int))
    for rec in big.values():
        J = int(rec['man']['J'])
        bucket = min(J // 10 * 10 + 5, 105)
        for key, *_ in MODELS:
            r = rec['res'].get(key)
            if r and r.get('runtime'):
                try:
                    byJ[key][bucket].append(float(r['runtime']) * 1000)
                except ValueError:
                    continue
                if r.get('status') in ('timeout', 'time_limit'):
                    censored[key][bucket] += 1

    fig, ax = plt.subplots(figsize=(COL, 2.9))
    for key, lab, c, mk, ls in MODELS:
        pts = sorted(byJ[key].items())
        if not pts:
            continue
        xs = [p for p, _ in pts]
        ys = [statistics.median(v) for _, v in pts]
        frac = [censored[key].get(p, 0) / len(v) for p, v in pts]
        solid = [i for i, f in enumerate(frac) if f < 0.5]
        ax.plot(xs, ys, color=c, linestyle=ls, label=lab, zorder=3,
                linewidth=1.3 if key == 'ilp_v1' else 1.1)
        ax.plot([xs[i] for i in solid], [ys[i] for i in solid], marker=mk,
                color=c, linestyle='none', markeredgewidth=0.4, zorder=4)
        hollow = [i for i, f in enumerate(frac) if f >= 0.5]
        if hollow:
            ax.plot([xs[i] for i in hollow], [ys[i] for i in hollow], marker=mk,
                    markerfacecolor='white', markeredgecolor=c, linestyle='none',
                    markeredgewidth=0.8, zorder=4)
    ax.axhline(time_limit_ms, color='black', linewidth=0.7, linestyle=(0, (2, 2)),
               alpha=0.55, zorder=1)
    ax.text(0.98, time_limit_ms * 1.25, 'solver time limit (10 s)', fontsize=5.6,
            ha='right', va='bottom', transform=ax.get_yaxis_transform(), alpha=0.75)
    ax.set_yscale('log')
    ax.set_xlabel('jobs per instance  $J$')
    ax.set_ylabel('median runtime (ms, log)')
    ax.set_title('Cost against problem size')
    ax.text(0.975, 0.03, 'hollow marker: >50% of instances hit the limit,\n'
                         'so the value is censored and the true cost is higher',
            transform=ax.transAxes, fontsize=5.2, va='bottom', ha='right', alpha=0.8)
    ax.legend(frameon=False, ncol=5, fontsize=5.8, loc='lower center',
              bbox_to_anchor=(0.5, -0.34), columnspacing=1.0, handlelength=2.2)
    savefig(fig, 'fig4_runtime_vs_J.pdf')


# ── FIG 5: feasibility ──────────────────────────────────────────────────────
def fig_feasibility(big):
    tot = collections.Counter(); ok = collections.Counter()
    for rec in big.values():
        for key, *_ in MODELS:
            r = rec['res'].get(key)
            if r:
                tot[key] += 1
                if r.get('model_feasible') == '1':
                    ok[key] += 1
    series = [(k, l, c) for k, l, c, _m, _s in MODELS]
    labs = [l for _k, l, _c in series if tot[_k]]
    vals = [100 * ok[k] / tot[k] for k, _l, _c in series if tot[k]]
    cols = [c for k, _l, c in series if tot[k]]
    fig, ax = plt.subplots(figsize=(FULL, 2.2))
    bars = ax.bar(range(len(vals)), vals, color=cols, alpha=0.6,
                  edgecolor='black', linewidth=0.5)
    for i, (b, v) in enumerate(zip(bars, vals)):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.4, '%.1f' % v,
                ha='center', fontsize=6)
    ax.set_xticks(range(len(labs))); ax.set_xticklabels(labs, rotation=20, ha='right')
    ax.set_ylabel('instances solved (%)')
    ax.set_ylim(min(vals) - 5, 100)
    ax.set_title('Feasibility: share of instances for which each model returned a valid schedule')
    savefig(fig, 'fig5_feasibility.pdf')


if __name__ == '__main__':
    print('loading...')
    unavg = load('tc_unavg')
    big = {}
    for t in ('tc_sept_small', 'tc_sept_paper'):
        big.update(load(t))
    print('  unaveraged %d instances, campaign %d instances' % (len(unavg), len(big)))
    print('writing figures:')
    fig_distribution(unavg)
    fig_ofat({k: v for k, v in big.items() if k[3] == 'tc_sept_small'})
    fig_v6_v7(unavg)
    fig_runtime(big)
    fig_feasibility({k: v for k, v in big.items() if k[3] == 'tc_sept_small'})
    print('done ->', OUT)
