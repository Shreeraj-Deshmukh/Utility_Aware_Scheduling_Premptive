"""
Single-pass (flat) SPS mapping — used by heuristic_v1.

Unlike quantum_sps_mapping, this processes all jobs in a single SPS call
using utilisation as load metric. No per-quantum processing, no leftover pool.
"""

from .dps_sps import run_dps, run_sps


def single_pass_sps_mapping(tasks, N_job, N_tsk, m):
    """
    Map all jobs to m processors in a single SPS pass.

    Load metric: util_i = e_m_i / p_i  (same as quantum version).

    Returns: mapping dict {(i, j): proc_idx}.
    """
    job_loads = [
        ((i, j), tasks[i]['e_m'] / tasks[i]['p_i'])
        for i in range(N_tsk)
        for j in range(N_job[i])
    ]
    job_loads_sorted = sorted(job_loads, key=lambda x: -x[1])

    ps_list = run_dps(job_loads_sorted, m)
    result  = run_sps(ps_list)

    if result is None:
        return {}

    mapping = {}
    for px, job_set in enumerate(result.assign):
        for (i, j) in job_set:
            mapping[(i, j)] = px
    return mapping
