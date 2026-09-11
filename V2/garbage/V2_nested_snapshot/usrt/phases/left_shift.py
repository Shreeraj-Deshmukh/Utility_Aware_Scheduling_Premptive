"""
Phase 2 — Left-Shift simulation.

Two variants:

left_shift(proc_jobs, job_r, job_d, seg_k, freq_idx, freq_set, cum)
    Takes the proc_jobs dict (already built from mapping).
    Returns ls_slack dict: {(i,j): float}.
    Used by heuristic_claude / heuristicv4 (diagnostic, run once after Phase 1).

left_shift_mapping(mapping, tasks, processors, h, seg_state, freq_state, cum, freq_set)
    Takes raw mapping dict and rebuilds proc_jobs internally.
    Returns time_slack dict: {(i,j): float}.
    Used by heuristicv3-style solvers that recompute left-shift after each change.

Both simulate non-preemptive EDF-order scheduling per processor and compute:
    start     = max(proc_avail, release_time)
    finish    = start + e_eff(i, k, z)
    slack     = deadline - finish

This is an approximation of idle time. Actual scheduling is preemptive EDF;
DBF is used for hard feasibility checking.
"""

from ..models import e_eff_val


def left_shift(proc_jobs, job_r, job_d, seg_k, freq_idx, freq_set, cum) -> dict:
    """
    Returns {(i,j): slack} for all jobs.
    """
    ls_slack = {}
    for x, jobs in proc_jobs.items():
        jobs_edf   = sorted(jobs, key=lambda ij: job_d[ij])
        proc_avail = 0.0
        for (i, j) in jobs_edf:
            ef         = e_eff_val(cum[i][seg_k[(i, j)]], freq_set[freq_idx[(i, j)]])
            start      = max(proc_avail, float(job_r[(i, j)]))
            ls_slack[(i, j)] = job_d[(i, j)] - (start + ef)
            proc_avail = start + ef
    return ls_slack


def left_shift_mapping(mapping, tasks, processors, h,
                       seg_state, freq_state, cum, freq_set) -> dict:
    """
    Rebuilds proc_jobs from mapping, then runs left-shift.
    Returns {(i,j): slack}.
    """
    from collections import defaultdict
    N_tsk   = len(tasks)
    periods = [int(t['p_i']) for t in tasks]
    N_job   = [h // periods[i] for i in range(N_tsk)]

    proc_jobs = defaultdict(list)
    for i in range(N_tsk):
        for j in range(N_job[i]):
            x = mapping[(i, j)]
            r = j * periods[i]
            d = (j + 1) * periods[i]
            proc_jobs[x].append((i, j, r, d))

    time_slack = {}
    for x in range(len(processors)):
        jobs_x     = sorted(proc_jobs[x], key=lambda ijrd: ijrd[3])
        proc_avail = 0.0
        for (i, j, r, d) in jobs_x:
            k      = seg_state[(i, j)]
            z      = freq_state[(i, j)]
            ef     = cum[i][k] / freq_set[z]
            start  = max(proc_avail, float(r))
            time_slack[(i, j)] = d - (start + ef)
            proc_avail         = start + ef

    return time_slack
