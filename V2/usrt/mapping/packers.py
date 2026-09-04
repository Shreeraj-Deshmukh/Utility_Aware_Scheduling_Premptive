"""
Cheap bin-packing mappings — alternatives to SPS, for multi-start.

SPS is one heuristic among several.  WFD / FFD / BFD cost the same O(J log J)
but land in STRUCTURALLY DIFFERENT basins, which is exactly what a multi-start
wants: five genuinely different mappings explore more than twenty-four
single-job moves away from one mapping.

All three are job-level (paper II: "Mapping job level"), pack by mandatory
utilisation e_m/p_i, and use the standard per-processor utilisation <= 1 test,
which is sufficient for partitioned preemptive EDF with implicit deadlines.

WFD (Worst-Fit Decreasing) is additionally the mapping the paper's own
Section V.B "Heur1.0/Baseline" prescribes: "tasks in decreasing order of
utilization ... map to the first least utilized processor".

Every mapping returned here is DBF-verified before use; `pack_all` silently
drops any candidate that fails, so a caller can never receive an infeasible
mapping from this module.
"""

from collections import defaultdict

from ..utils     import generate_jobs, build_proc_jobs
from ..dbf.check import check_all_timing

_TOL = 1e-9


def _job_list(tasks, h, job_d):
    """
    Jobs in decreasing mandatory utilisation.

    e_m/p_i is a PER-TASK quantity, so every job of a task ties; the deadline
    then the index break it, giving a total order (see the 22 Aug tie-break
    work -- an unstable order here silently changes the mapping).
    """
    jobs = []
    for (i, j, r, d) in generate_jobs(tasks, h):
        jobs.append(((i, j), tasks[i]['e_m'] / tasks[i]['p_i'], d))
    jobs.sort(key=lambda t: (-t[1], t[2], t[0]))
    return [(ij, u) for (ij, u, _d) in jobs]


def wfd_mapping(tasks, processors, h, job_d):
    """Worst-Fit Decreasing: each job to the LEAST loaded processor."""
    m = len(processors)
    load = [0.0] * m
    mapping = {}
    for ij, u in _job_list(tasks, h, job_d):
        x = min(range(m), key=lambda p: (load[p], p))
        mapping[ij] = x
        load[x] += u
    return mapping


def ffd_mapping(tasks, processors, h, job_d):
    """First-Fit Decreasing: first processor that still fits under 1.0."""
    m = len(processors)
    load = [0.0] * m
    mapping = {}
    for ij, u in _job_list(tasks, h, job_d):
        placed = False
        for x in range(m):
            if load[x] + u <= 1.0 + _TOL:
                mapping[ij] = x
                load[x] += u
                placed = True
                break
        if not placed:                       # nothing fits: least loaded
            x = min(range(m), key=lambda p: (load[p], p))
            mapping[ij] = x
            load[x] += u
    return mapping


def bfd_mapping(tasks, processors, h, job_d):
    """Best-Fit Decreasing: the processor left with the LEAST slack that fits."""
    m = len(processors)
    load = [0.0] * m
    mapping = {}
    for ij, u in _job_list(tasks, h, job_d):
        fits = [x for x in range(m) if load[x] + u <= 1.0 + _TOL]
        if fits:
            x = min(fits, key=lambda p: (1.0 - load[p] - u, p))
        else:
            x = min(range(m), key=lambda p: (load[p], p))
        mapping[ij] = x
        load[x] += u
    return mapping


def donor_harvester_mapping(tasks, processors, h, job_d, cum, N_seg,
                            n_donor=None):
    """
    Deliberately CONCENTRATE utility density (the low-rho optimum).

    Measured against optimal ILP mappings, the optimum concentrates when energy
    binds and balances when it does not.  Concentration is built directly here:
    low-utility "donor" jobs are packed onto a dedicated subset of processors
    that can then run slowly without costing any optional work, while the
    high-utility "harvester" jobs keep their timing slack on the rest.

    `n_donor` defaults to one processor (the smallest meaningful split); the
    caller may size it from the energy deficit.
    """
    m = len(processors)
    if m < 2:
        return wfd_mapping(tasks, processors, h, job_d)
    n_donor = max(1, min(m - 1, n_donor or 1))

    # rank jobs by utility density: harvesters first
    jobs = []
    for (i, j, r, d) in generate_jobs(tasks, h):
        ud = tasks[i]['u_i'] * (cum[i][N_seg[i]] - cum[i][0]) / tasks[i]['p_i']
        jobs.append(((i, j), tasks[i]['e_m'] / tasks[i]['p_i'], ud, d))
    jobs.sort(key=lambda t: (-t[2], t[3], t[0]))       # high ud first

    donors   = list(range(m - n_donor, m))
    harvest  = list(range(m - n_donor))
    load     = [0.0] * m
    mapping  = {}
    n_h      = len(jobs) - max(1, len(jobs) // (m // max(1, len(harvest)) + 1))
    for idx, (ij, u, ud, d) in enumerate(jobs):
        pool = harvest if idx < len(jobs) * len(harvest) // m else donors
        x = min(pool, key=lambda p: (load[p], p))
        mapping[ij] = x
        load[x] += u
    return mapping


def pack_all(tasks, processors, h, job_r, job_d, cum, N_seg, freq_set,
             N_tsk, N_job, N_prc):
    """
    Every cheap mapping this module can build, filtered to the DBF-feasible ones.

    Returns [(name, mapping), ...].  Feasibility is the mandatory-only DBF test
    at f_max -- the same gate SPS itself must pass.
    """
    z_max = len(freq_set) - 1
    seg0  = {(i, j): 0     for i in range(N_tsk) for j in range(N_job[i])}
    frq0  = {(i, j): z_max for i in range(N_tsk) for j in range(N_job[i])}

    def ok(mp):
        pj, _ = build_proc_jobs(mp)
        return check_all_timing(pj, job_r, job_d, seg0, frq0, freq_set, cum, N_prc)

    out = []
    for name, fn in (("wfd", lambda: wfd_mapping(tasks, processors, h, job_d)),
                     ("ffd", lambda: ffd_mapping(tasks, processors, h, job_d)),
                     ("bfd", lambda: bfd_mapping(tasks, processors, h, job_d)),
                     ("donor", lambda: donor_harvester_mapping(
                         tasks, processors, h, job_d, cum, N_seg))):
        try:
            mp = fn()
        except Exception:
            continue
        if ok(mp):
            out.append((name, mp))
    return out
