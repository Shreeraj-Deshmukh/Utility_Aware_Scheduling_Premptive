"""
DBF window-slack helpers.

window_slack(x, t1, t2, ...)
    Computes (t2-t1) - Σ e_eff of jobs in S(t1,t2,x).

min_slack_for_job(i_s, j_s, x, ...)
    Minimum slack over all DBF windows that CONTAIN job (i_s, j_s).
    If ≥ add_time, adding add_time to that job keeps all containing
    windows feasible — no separate full DBF call is required (Case i proof).
"""

from ..models import e_eff_val


def window_slack(x, t1, t2, proc_jobs, job_r, job_d,
                 seg_k, freq_idx, freq_set, cum) -> float:
    window = [
        (i, j) for (i, j) in proc_jobs[x]
        if job_r[(i, j)] >= t1 and job_d[(i, j)] <= t2
    ]
    if not window:
        return t2 - t1
    demand = sum(
        e_eff_val(cum[i][seg_k[(i, j)]], freq_set[freq_idx[(i, j)]])
        for (i, j) in window
    )
    return (t2 - t1) - demand


def min_slack_for_job(i_s, j_s, x, proc_jobs, job_r, job_d,
                      seg_k, freq_idx, freq_set, cum) -> float:
    r_ij = job_r[(i_s, j_s)]
    d_ij = job_d[(i_s, j_s)]
    Ax   = sorted({job_r[ij] for ij in proc_jobs[x]})
    Dx   = sorted({job_d[ij] for ij in proc_jobs[x]})
    min_sl = float('inf')
    for t1 in Ax:
        if t1 > r_ij:
            continue
        for t2 in Dx:
            if t2 < d_ij:
                continue
            if t1 >= t2:
                continue
            sl = window_slack(x, t1, t2, proc_jobs, job_r, job_d,
                              seg_k, freq_idx, freq_set, cum)
            if sl < min_sl:
                min_sl = sl
    return min_sl if min_sl < float('inf') else (d_ij - r_ij)
