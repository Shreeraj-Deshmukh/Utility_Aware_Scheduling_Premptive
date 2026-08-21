"""
Generation primitives implementing the paper's Section VII.A.

  uunifast            : Bini & Buttazzo UUniFast (uniform over the simplex).
  donate_excess       : the paper's cap enforcement — excess utilisation above a
                        per-task cap is iteratively DONATED to other tasks in
                        units of 0.01 (NOT discard-and-redraw, which biases the
                        distribution).
  assign_periods      : base period from {basePerMin, +step, ..., basePerMax};
                        period = base * 2^m, m in {0..k_max}.  Harmonic by
                        construction, H = max(period used).
  random_freq_set     : N_frq distinct levels drawn from
                        {f_min, f_min+0.05, ..., f_max}, with f_max guaranteed
                        present (paper VII.A.1 step ii).
  split_segments_normal: optional utilisation split across segments with a
                        normal distribution, mean = U_opt_i / N_seg_i and
                        sd = seg_var_frac * mean, renormalised to preserve the
                        task's total optional utilisation exactly.
  budget_for_rho      : B = rho * (energy to run ALL jobs at f_max) — the
                        paper's definition (a pure scaling, not an offset).
  worst_fit_feasible  : mandatory-timing guard (per-core utilisation <= 1).
"""

import random
from ..models import energy_val


# ── utilisations ─────────────────────────────────────────────────────────────

def uunifast(n, U, rng):
    """n utilisations, uniform over the simplex summing to U."""
    if n <= 0:
        return []
    if U <= 0:
        return [0.0] * n
    utils, s = [], U
    for i in range(1, n):
        nxt = s * (rng.random() ** (1.0 / (n - i)))
        utils.append(s - nxt)
        s = nxt
    utils.append(s)
    return utils


def donate_excess(utils, caps, unit=0.01, max_iter=1000000):
    """
    Paper VII.A.2(c)/(d): any utilisation above its cap is iteratively donated
    to other tasks in units of `unit`, preserving the total.

    `caps` is either a scalar cap or a per-task list of caps.  Returns
    (utils, ok); ok is False when the excess cannot be placed anywhere (the
    paper's "report error" case).
    """
    u = list(utils)
    n = len(u)
    if n == 0:
        return u, True
    if not isinstance(caps, (list, tuple)):
        caps = [caps] * n

    it = 0
    while it < max_iter:
        it += 1
        # the most over-cap task
        over = max(range(n), key=lambda i: u[i] - caps[i])
        if u[over] - caps[over] <= 1e-12:
            return u, True                      # everyone within cap
        step = min(unit, u[over] - caps[over])
        # the task with the most room
        recv = max(range(n), key=lambda i: (caps[i] - u[i]) if i != over else -1e18)
        if recv == over or caps[recv] - u[recv] < step - 1e-12:
            return u, False                     # nowhere to donate
        u[over] -= step
        u[recv] += step
    return u, False


# ── periods ──────────────────────────────────────────────────────────────────

def assign_periods(n_tsk, base_per_min, base_per_max, per_step, k_max, rng,
                   min_distinct=3):
    """
    Paper VII.A.1: choose a base period, then period_i = base * 2^m_i with
    m_i drawn from {0..k_max}.  The first min(n_tsk, k_max+1) tasks receive
    distinct multipliers so at least `min_distinct` distinct periods appear.
    """
    bases = list(range(int(base_per_min), int(base_per_max) + 1, int(per_step)))
    base = bases[rng.randrange(len(bases))] if bases else int(base_per_min)

    mults = []
    forced = min(n_tsk, k_max + 1)
    for i in range(n_tsk):
        mults.append(i if i < forced else rng.randint(0, k_max))
    return [int(base * (2 ** m)) for m in mults]


# ── frequencies ──────────────────────────────────────────────────────────────

def random_freq_set(n_frq, f_min, f_max, f_step, rng):
    """
    N_frq distinct normalised levels from {f_min, f_min+f_step, ..., f_max},
    ascending, with f_max guaranteed present.

    The processors are homogeneous (paper Section II), so one set is drawn and
    shared by every processor; the paper's step (ii) — "if no processor has
    f_max, assign it" — is enforced directly by pinning the top level to f_max.
    """
    n_grid = int(round((f_max - f_min) / f_step)) + 1
    grid = [round(f_min + i * f_step, 6) for i in range(n_grid)]
    sel = sorted(rng.sample(grid, min(n_frq, n_grid)))
    if abs(sel[-1] - f_max) > 1e-9:
        sel[-1] = f_max                          # guarantee f_max is available
    return tuple(sel)


# ── optional-segment split ───────────────────────────────────────────────────

def split_segments_normal(total_opt_exec, n_seg, rng, var_frac=0.20):
    """
    Paper VII.A.2(d)(iii): split a task's optional execution time across its
    segments with a normal distribution — mean = total/n_seg, sd = var_frac *
    mean — then renormalise so the segments sum EXACTLY to total_opt_exec.
    Draws are floored at a small positive value so no segment is degenerate.
    """
    if n_seg <= 0 or total_opt_exec <= 0:
        return []
    mean = total_opt_exec / n_seg
    sd = var_frac * mean
    vals = []
    for _ in range(n_seg):
        v = rng.gauss(mean, sd)
        vals.append(max(v, 0.05 * mean))         # keep strictly positive
    s = sum(vals)
    return [total_opt_exec * v / s for v in vals]


# ── energy budget ────────────────────────────────────────────────────────────

def budget_for_rho(e_full_fmax, rho):
    """Paper VII.A.2(e): B = rho * (energy for ALL jobs of ALL tasks at f_max)."""
    return rho * e_full_fmax


def energies_fmax(tasks, n_job):
    """(E_mand_fmax, E_full_fmax, E_mand_min) over the hyper-period.

    E_mand_min uses each job's cheapest available frequency and is only a
    diagnostic: it is the least energy any schedule could possibly spend on the
    mandatory segments, so B < E_mand_min is provably infeasible.
    """
    e_mand = e_full = 0.0
    for i, t in enumerate(tasks):
        cum_mand = t['e_m']
        cum_full = t['e_m'] + sum(t['e_o_k'])
        e_mand += n_job[i] * energy_val(cum_mand, 1.0)
        e_full += n_job[i] * energy_val(cum_full, 1.0)
    return e_mand, e_full


def min_mandatory_energy(tasks, n_job, freq_set):
    """Least possible mandatory energy: each job at its cheapest frequency."""
    tot = 0.0
    for i, t in enumerate(tasks):
        best = min(energy_val(t['e_m'], f) for f in freq_set)
        tot += n_job[i] * best
    return tot


# ── feasibility guard ────────────────────────────────────────────────────────

def worst_fit_feasible(u_mand, n_prc, tol=1e-9):
    """
    Worst-Fit-Decreasing packing of mandatory utilisations onto n_prc cores.
    Under partitioned preemptive EDF with implicit deadlines a core is feasible
    iff its utilisation <= 1, so this is a sufficient existence check for a
    feasible mandatory partition.  Returns (feasible, bins).
    """
    bins = [0.0] * n_prc
    for u in sorted(u_mand, reverse=True):
        j = min(range(n_prc), key=lambda b: bins[b])
        bins[j] += u
    return (max(bins) <= 1.0 + tol), bins
