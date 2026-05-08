"""
Full DBF feasibility checks.

check_all_timing  — global check across all processors and all windows.
check_dbf_proc    — check a single processor (used inside tight loops).
"""

from .slack import window_slack


def check_all_timing(proc_jobs, job_r, job_d,
                     seg_k, freq_idx, freq_set, cum, N_prc) -> bool:
    """Returns True iff DBF slack ≥ 0 for every (processor, window) pair."""
    for x in range(N_prc):
        if not proc_jobs[x]:
            continue
        Ax = sorted({job_r[ij] for ij in proc_jobs[x]})
        Dx = sorted({job_d[ij] for ij in proc_jobs[x]})
        for t1 in Ax:
            for t2 in Dx:
                if t1 >= t2:
                    continue
                if window_slack(x, t1, t2, proc_jobs, job_r, job_d,
                                seg_k, freq_idx, freq_set, cum) < -1e-9:
                    return False
    return True


def check_dbf_proc(x, mapping, tasks, h, seg_state, freq_state,
                   cum, freq_set) -> bool:
    """
    Check DBF feasibility for a single processor x.

    Accepts the flat mapping dict and separate seg_state / freq_state dicts
    (heuristicv3-style). Returns True if feasible.
    """
    from collections import defaultdict
    N_tsk   = len(tasks)
    periods = [int(t['p_i']) for t in tasks]
    N_job   = [h // periods[i] for i in range(N_tsk)]
    job_r   = {(i, j): j * periods[i]       for i in range(N_tsk) for j in range(N_job[i])}
    job_d   = {(i, j): (j + 1) * periods[i] for i in range(N_tsk) for j in range(N_job[i])}

    jobs_x = [(i, j) for (i, j), px in mapping.items() if px == x]
    Ax = sorted({job_r[ij] for ij in jobs_x})
    Dx = sorted({job_d[ij] for ij in jobs_x})

    for t1 in Ax:
        for t2 in Dx:
            if t1 >= t2:
                continue
            window = [(i, j) for (i, j) in jobs_x
                      if job_r[(i, j)] >= t1 and job_d[(i, j)] <= t2]
            if not window:
                continue
            demand = sum(cum[i][seg_state[(i, j)]] / freq_set[freq_state[(i, j)]]
                         for (i, j) in window)
            if demand > (t2 - t1) + 1e-9:
                return False
    return True
