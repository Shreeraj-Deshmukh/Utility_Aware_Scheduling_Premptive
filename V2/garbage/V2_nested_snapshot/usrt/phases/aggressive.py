"""
Phase 4 — Aggressive frequency scaling.

Two variants:

phase_aggressive_scaling(seg_k, freq_idx, ...)
    Dict-based (proc_jobs + DBF window check).
    Iteratively decreases freq of each job if energy strictly decreases
    and full DBF timing check passes.
    Used by heuristic_claude / heuristicv4.

aggressive_freq_scaling_state(state)
    ScheduleState-based.
    Uses state.try_dec_freq() atomic move (incremental DBF update).
    Used by heuristic_v1.

With ALPHA=1, BETA=0.5 energy is minimised at f_max, so both variants are
structural no-ops in the default configuration. They fire correctly for
alternative (ALPHA, BETA) where lower frequency saves energy.
"""

from ..models import energy_val
from ..dbf.check import check_all_timing


def phase_aggressive_scaling(seg_k, freq_idx, freq_set, N_frq, cum,
                              N_tsk, N_job, proc_jobs, job_r, job_d,
                              N_prc) -> int:
    """
    Returns number of frequency reductions applied.
    """
    n_scaled = 0
    changed  = True
    while changed:
        changed = False
        for i in range(N_tsk):
            for j in range(N_job[i]):
                z_cur = freq_idx[(i, j)]
                if z_cur == 0:
                    continue
                E_cur = energy_val(cum[i][seg_k[(i, j)]], freq_set[z_cur])
                E_new = energy_val(cum[i][seg_k[(i, j)]], freq_set[z_cur - 1])
                if E_new >= E_cur - 1e-12:
                    continue    # no energy saving → skip
                freq_idx[(i, j)] = z_cur - 1
                if check_all_timing(proc_jobs, job_r, job_d, seg_k,
                                    freq_idx, freq_set, cum, N_prc):
                    changed  = True
                    n_scaled += 1
                else:
                    freq_idx[(i, j)] = z_cur    # revert
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
