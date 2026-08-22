"""
Phase 4 — Frequency scaling for energy FEASIBILITY.

Two variants:

phase_aggressive_scaling(seg_k, freq_idx, ..., B_BUDGET)
    Dict-based (proc_jobs + DBF window check).
    Reduces frequencies ONLY as far as needed to fit the energy budget.

aggressive_freq_scaling_state(state)
    ScheduleState-based.
    Uses state.try_dec_freq() atomic move (incremental DBF update).
    Used by heuristic_v1.

Phase 4 exists to make the schedule ENERGY-FEASIBLE, not to minimise energy.
Lowering a job's frequency inflates its effective execution time
(e_eff = work / f), which eats the timing slack Phase 5 needs to add optional
segments.  So when the schedule is already within budget at the current (f_max)
assignment, Phase 4 must do NOTHING — otherwise, whenever lower frequency saves
energy (e.g. ALPHA=0.15, BETA=1.0, where f* < f_max), it would greedily drive
every job toward f*, saturate the DBF windows with mandatory work, and starve
the objective (observed: 98 jobs scaled → Phase 5 adds 0 segments → utility 0).

With B_BUDGET given, jobs are scaled down (only while energy is over budget) and
the loop stops the instant it fits.  With B_BUDGET=None the legacy behaviour
(scale while energy strictly decreases) is kept for backward compatibility.
Under ALPHA=1, BETA=0.5 (f_max is energy-optimal) this is a no-op either way.
"""

from ..models import energy_val, e_eff_val, total_energy
from ..dbf.check import check_all_timing


def phase_aggressive_scaling(seg_k, freq_idx, freq_set, N_frq, cum,
                              N_tsk, N_job, proc_jobs, job_r, job_d,
                              N_prc, B_BUDGET=None) -> int:
    """
    Reduce frequencies only as needed for energy feasibility.

    Returns number of frequency reductions applied (0 when already feasible at
    the current assignment and B_BUDGET is given).
    """
    # Feasibility gate: if a budget is given and we already fit, do nothing.
    E_tot = None
    if B_BUDGET is not None:
        E_tot = total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job)
        if E_tot <= B_BUDGET + 1e-9:
            return 0

    n_scaled = 0
    changed  = True
    while changed:
        changed = False
        # Visit candidates in order of ENERGY SAVED PER UNIT TIME COST
        # (descending) rather than task-index order.  Feasibility is reached by
        # spending the least DBF slack per unit of energy recovered; index order
        # can burn timing slack on poor trades and then fail to reach the budget
        # on instances that are in fact schedulable.
        cands = []
        for i in range(N_tsk):
            for j in range(N_job[i]):
                z_cur = freq_idx[(i, j)]
                if z_cur == 0:
                    continue
                c     = cum[i][seg_k[(i, j)]]
                E_cur = energy_val(c, freq_set[z_cur])
                E_new = energy_val(c, freq_set[z_cur - 1])
                if E_new >= E_cur - 1e-12:
                    continue                 # no energy saving (at/below f*)
                saved = E_cur - E_new
                tcost = (e_eff_val(c, freq_set[z_cur - 1]) -
                         e_eff_val(c, freq_set[z_cur]))
                cands.append((-(saved / (tcost + 1e-12)), i, j))
        cands.sort()

        for (_, i, j) in cands:
            z_cur = freq_idx[(i, j)]
            if z_cur == 0:
                continue
            c     = cum[i][seg_k[(i, j)]]
            E_cur = energy_val(c, freq_set[z_cur])
            E_new = energy_val(c, freq_set[z_cur - 1])
            if E_new >= E_cur - 1e-12:
                continue
            freq_idx[(i, j)] = z_cur - 1
            if check_all_timing(proc_jobs, job_r, job_d, seg_k,
                                freq_idx, freq_set, cum, N_prc):
                changed   = True
                n_scaled += 1
                if E_tot is not None:
                    E_tot -= (E_cur - E_new)
                    if E_tot <= B_BUDGET + 1e-9:
                        return n_scaled
            else:
                freq_idx[(i, j)] = z_cur     # revert
    return n_scaled


def aggressive_freq_scaling_state(state) -> int:
    """
    ScheduleState-based aggressive scaling.
    Visits jobs in decreasing e_m order (heaviest first → most energy saved).
    Returns total number of frequency reductions applied.
    """
    all_jobs = [
        (i, j)
        for i in range(state.N_tsk)
        for j in range(state.N_job[i])
    ]
    all_jobs.sort(key=lambda ij: -state.tasks[ij[0]]['e_m'])

    scaled = 0
    for (i, j) in all_jobs:
        while state.try_dec_freq(i, j):
            scaled += 1
    return scaled
