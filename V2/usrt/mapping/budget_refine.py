"""
Budget-aware Refine Mapping (Phase 1b') + mapping-level local search.

Why the existing Refine Mapping is not enough
---------------------------------------------
`refine_mapping_2a/2b` always MINIMISES max utility density, i.e. it always
balances.  Measured against optimal ILP mappings, that is the right objective
only when energy is plentiful:

    rho     SPS UD-spread   OPT UD-spread   optimum ...
    0.4         0.504           0.730       CONCENTRATES  (3/4 instances)
    0.7         0.472           0.511       neutral
    1.0         0.472           0.295       BALANCES

The inversion has a mechanism.  With energy plentiful everything runs at f_max
and the binding resource is per-processor TIME, so spreading optional work keeps
any one core from saturating -> balance.  With energy tight, utility per energy
is u_i/g(f), so the budget should be spent on high-u_i work while low-u_i work
runs slowly to shrink its energy footprint.  Running slowly costs TIME on its
own processor, so scattering low-value jobs makes every core pay the slowdown --
including the cores hosting the valuable optional work.  Segregating them onto
dedicated "donor" cores localises that penalty where nothing is lost -> concentrate.

Two changes are therefore applied here:

  1. OBJECTIVE, switched on a parameter-free regime test (E_mand_fmax <= B):
       time-bound   -> minimise sum UD(x)^2   (balance,     as before)
       energy-bound -> maximise sum UD(x)^2   (concentrate, the inversion)
     Sum-of-squares is used in both directions because, for a fixed total, it
     falls exactly when mass spreads and rises exactly when it concentrates.

  2. FEASIBILITY AT THE OPERATING POINT.  SPS checks per-processor utilisation
     <= 1 at f_max, but a tight budget forces execution at some f_hat < 1 where
     effective times inflate by 1/f_hat -- so a mapping "feasible" at f_max can
     leave a core with almost no slack where it matters.  Both the DBF check and
     the load-balance guard are evaluated at f_hat.

Safety: a swap is accepted only if the objective strictly improves, the
mandatory-utilisation imbalance does not worsen, AND mandatory DBF at f_hat
stays feasible.  So feasibility can never regress relative to the input mapping.
"""

from collections import defaultdict

from ..models    import energy_val, e_eff_val
from ..dbf.check import check_all_timing
from ..utils     import build_proc_jobs

_TOL = 1e-9


# ── operating point ──────────────────────────────────────────────────────────

def estimate_operating_freq(tasks, N_tsk, N_job, freq_set, B_BUDGET):
    """
    The fastest frequency whose MANDATORY-only cost fits the budget.

    g(f) = ALPHA/f + BETA*f^2 is U-shaped, so the affordable set is an interval
    around f*, not a suffix -- we take its maximum (fastest affordable, hence
    the most timing slack left for optional work).  If nothing fits, fall back
    to the cheapest frequency available.
    """
    W = sum(N_job[i] * tasks[i]['e_m'] for i in range(N_tsk))
    if W <= _TOL:
        return max(freq_set)
    ok = [f for f in freq_set if energy_val(W, f) <= B_BUDGET + _TOL]
    if ok:
        return max(ok)
    return min(freq_set, key=lambda f: energy_val(W, f))


def is_energy_bound(tasks, N_tsk, N_job, freq_set, B_BUDGET):
    """True when the mandatory workload does not fit the budget at f_max."""
    W = sum(N_job[i] * tasks[i]['e_m'] for i in range(N_tsk))
    return energy_val(W, max(freq_set)) > B_BUDGET + _TOL


# ── per-processor quantities ─────────────────────────────────────────────────

def _job_ud(tasks, cum, N_seg, i, H):
    """Optional-utility density contributed by ONE job of task i."""
    return tasks[i]['u_i'] * (cum[i][N_seg[i]] - cum[i][0]) / H


def _proc_stats(mapping, tasks, cum, N_seg, N_prc, H):
    """(UD per processor, mandatory utilisation per processor)."""
    ud = [0.0] * N_prc
    mu = [0.0] * N_prc
    for (i, j), x in mapping.items():
        ud[x] += _job_ud(tasks, cum, N_seg, i, H)
        mu[x] += tasks[i]['e_m'] / H
    return ud, mu


def _sumsq(v):
    return sum(a * a for a in v)


def _spread(v):
    return max(v) - min(v) if v else 0.0


# ── the refinement ───────────────────────────────────────────────────────────

def refine_mapping_budget(mapping, tasks, N_tsk, N_prc, N_job, cum, N_seg,
                          job_r, job_d, freq_set, B_BUDGET, H,
                          max_swaps=200, verbose=False):
    """
    Budget-aware Phase 1b'.  Returns (new_mapping, info_dict).

    Objective is sum UD(x)^2 -- minimised when time-bound, maximised when
    energy-bound.  Every accepted swap keeps mandatory-utilisation imbalance
    from worsening and keeps mandatory DBF feasible at f_hat.
    """
    mapping = dict(mapping)
    e_bound = is_energy_bound(tasks, N_tsk, N_job, freq_set, B_BUDGET)
    f_hat   = estimate_operating_freq(tasks, N_tsk, N_job, freq_set, B_BUDGET)
    z_hat   = min(range(len(freq_set)), key=lambda z: abs(freq_set[z] - f_hat))

    # sorted(): iteration order over a dict must not leak into which swap is
    # chosen among equally-scoring candidates.
    jobs = sorted(mapping.keys())
    seg0 = {ij: 0 for ij in jobs}
    frq  = {ij: z_hat for ij in jobs}          # judge timing AT THE OPERATING POINT

    def dbf_ok(m):
        pj, _ = build_proc_jobs(m)
        return check_all_timing(pj, job_r, job_d, seg0, frq, freq_set, cum, N_prc)

    if not dbf_ok(mapping):
        # The incoming mapping is already infeasible at f_hat; refining it under
        # a guard it cannot satisfy would reject every swap.  Leave it alone.
        return mapping, dict(energy_bound=e_bound, f_hat=f_hat, swaps=0,
                             skipped="infeasible at f_hat")

    ud, mu = _proc_stats(mapping, tasks, cum, N_seg, N_prc, H)
    obj0   = _sumsq(ud)
    n_swaps = 0

    for _ in range(max_swaps):
        best = None
        best_gain = _TOL
        for a in range(len(jobs)):
            ija = jobs[a]
            xa  = mapping[ija]
            for b in range(a + 1, len(jobs)):
                ijb = jobs[b]
                xb  = mapping[ijb]
                if xa == xb:
                    continue
                da = _job_ud(tasks, cum, N_seg, ija[0], H)
                db = _job_ud(tasks, cum, N_seg, ijb[0], H)
                ma = tasks[ija[0]]['e_m'] / H
                mb = tasks[ijb[0]]['e_m'] / H

                nud = list(ud)
                nud[xa] += db - da
                nud[xb] += da - db
                nmu = list(mu)
                nmu[xa] += mb - ma
                nmu[xb] += ma - mb

                # load balance must not get worse (measured at the operating point)
                if _spread(nmu) > _spread(mu) + _TOL:
                    continue

                gain = (_sumsq(nud) - _sumsq(ud)) if e_bound else \
                       (_sumsq(ud) - _sumsq(nud))
                if gain > best_gain:
                    best_gain = gain
                    best = (ija, ijb, xa, xb, nud, nmu)

        if best is None:
            break
        ija, ijb, xa, xb, nud, nmu = best
        mapping[ija], mapping[ijb] = xb, xa
        if not dbf_ok(mapping):
            mapping[ija], mapping[ijb] = xa, xb      # revert
            break
        ud, mu = nud, nmu
        n_swaps += 1

    info = dict(energy_bound=e_bound, f_hat=f_hat, swaps=n_swaps,
                ud_spread=_spread(ud), mu_spread=_spread(mu),
                obj_before=obj0, obj_after=_sumsq(ud))
    if verbose:
        mode = "CONCENTRATE (energy-bound)" if e_bound else "BALANCE (time-bound)"
        print(f"  regime: {mode}   f_hat={f_hat:.2f}   swaps={n_swaps}")
        print(f"  UD sum-of-squares {obj0:.4f} -> {_sumsq(ud):.4f}   "
              f"UD spread={_spread(ud):.4f}  mand-util spread={_spread(mu):.4f}")
    return mapping, info


# ── proposal 3: mapping-level local search ───────────────────────────────────

def mapping_local_search(mapping, evaluate, N_prc, max_rounds=3,
                         max_moves=None, verbose=False):
    """
    Best-improvement search over single-job reassignments, scoring each
    candidate by the utility the FULL pipeline actually achieves.

    `evaluate(mapping) -> (utility, feasible)`; infeasible candidates are
    discarded.  The incumbent is only replaced on strict improvement, so the
    result is never worse than the mapping handed in.
    """
    best_map = dict(mapping)
    best_u, ok = evaluate(best_map)
    if not ok:
        return best_map, dict(rounds=0, moves=0, utility=best_u)

    jobs = sorted(best_map.keys())
    moves = 0
    for rnd in range(max_rounds):
        cand_best, cand_u = None, best_u
        tried = 0
        for ij in jobs:
            for x in range(N_prc):
                if x == best_map[ij]:
                    continue
                if max_moves is not None and tried >= max_moves:
                    break
                trial = dict(best_map)
                trial[ij] = x
                u, feas = evaluate(trial)
                tried += 1
                if feas and u > cand_u + 1e-9:
                    cand_u, cand_best = u, trial
            if max_moves is not None and tried >= max_moves:
                break
        if cand_best is None:
            break
        best_map, best_u = cand_best, cand_u
        moves += 1
        if verbose:
            print(f"    [map-LS] round {rnd+1}: utility -> {best_u:.4f}")
    return best_map, dict(rounds=rnd + 1, moves=moves, utility=best_u)
