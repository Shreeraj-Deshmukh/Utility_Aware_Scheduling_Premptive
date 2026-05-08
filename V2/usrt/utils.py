"""
Shared utilities: testcase loading, period arithmetic, cumulative exec-time
table construction, job generation.
"""

import importlib.util
from math import gcd as _gcd
from collections import defaultdict


def load_testcase(path):
    spec = importlib.util.spec_from_file_location("tc", path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.testcase()


def gcd_list(lst):
    r = int(lst[0])
    for x in lst[1:]:
        r = _gcd(r, int(x))
    return r


def lcm2(a, b):
    a, b = int(a), int(b)
    return a * b // _gcd(a, b)


def lcm_list(lst):
    r = int(lst[0])
    for x in lst[1:]:
        r = lcm2(r, int(x))
    return r


def build_cum(tasks):
    """
    cum[i][k] = e_{i,0} + ... + e_{i,k}  (at f_max; k=0 → mandatory only).
    N_seg[i]  = number of optional segments for task i.
    """
    cum, N_seg = [], []
    for t in tasks:
        segs = [t['e_m']] + list(t['e_o_k'])
        row, s = [], 0.0
        for e in segs:
            s += e
            row.append(s)
        cum.append(row)
        N_seg.append(len(t['e_o_k']))
    return cum, N_seg


def generate_jobs(tasks, h):
    """Returns list of (task_idx, job_idx, release, deadline)."""
    jobs = []
    for i, t in enumerate(tasks):
        p = int(t['p_i'])
        n = h // p
        for j in range(n):
            jobs.append((i, j, j * p, (j + 1) * p))
    return jobs


def build_job_times(tasks, h):
    """Returns (job_r, job_d) dicts keyed by (i, j)."""
    periods = [int(t['p_i']) for t in tasks]
    N_tsk   = len(tasks)
    N_job   = [h // periods[i] for i in range(N_tsk)]
    job_r   = {(i, j): j * periods[i]       for i in range(N_tsk) for j in range(N_job[i])}
    job_d   = {(i, j): (j + 1) * periods[i] for i in range(N_tsk) for j in range(N_job[i])}
    return job_r, job_d


def build_proc_jobs(mapping):
    """
    Returns (proc_jobs, proc_jobs_map) from a flat mapping dict.
      proc_jobs     : {proc_idx: [(i, j), ...]}
      proc_jobs_map : {(i, j): proc_idx}
    """
    proc_jobs     = defaultdict(list)
    proc_jobs_map = {}
    for (i, j), x in mapping.items():
        proc_jobs[x].append((i, j))
        proc_jobs_map[(i, j)] = x
    return proc_jobs, proc_jobs_map
