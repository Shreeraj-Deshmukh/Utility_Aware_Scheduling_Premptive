"""
Mandatory-only DBF feasibility check and greedy repair for the SPS mapping.

check_dbf_mandatory: verifies DBF(t1,t2,x) ≤ t2-t1 using e_m at f_max.
repair_mapping: iteratively moves the biggest-demand job from the worst-
                violated window to the least-loaded processor.
"""

from collections import defaultdict


def check_dbf_mandatory(mapping, tasks, processors, h):
    """
    Global DBF check at f_max with mandatory segments only (k=0, z=max).

    Returns (is_feasible: bool, violations: {proc: [(t1, t2, demand, cap)]}).
    """
    N_tsk   = len(tasks)
    N_prc   = len(processors)
    periods = [int(t['p_i']) for t in tasks]
    N_job   = [h // periods[i] for i in range(N_tsk)]
    job_r   = {(i, j): j * periods[i]       for i in range(N_tsk) for j in range(N_job[i])}
    job_d   = {(i, j): (j + 1) * periods[i] for i in range(N_tsk) for j in range(N_job[i])}

    proc_jobs = defaultdict(list)
    for (i, j), x in mapping.items():
        proc_jobs[x].append((i, j))

    violations = {}
    for x in range(N_prc):
        jobs_x = proc_jobs[x]
        if not jobs_x:
            continue
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
                demand = sum(tasks[i]['e_m'] for (i, j) in window)
                cap    = t2 - t1
                if demand > cap + 1e-9:
                    violations.setdefault(x, []).append((t1, t2, demand, cap))

    return len(violations) == 0, violations


def repair_mapping(mapping, tasks, processors, h):
    """
    Greedy DBF repair: move the job with the largest e_m in the worst-violated
    window to the processor with the most remaining utilisation capacity.

    Returns (mapping, is_feasible).
    """
    m = len(processors)
    for _ in range(100):
        ok, viols = check_dbf_mandatory(mapping, tasks, processors, h)
        if ok:
            return mapping, True

        worst = max(
            ((x, t1, t2, dem, cap)
             for x, vlist in viols.items()
             for (t1, t2, dem, cap) in vlist),
            key=lambda v: v[3] - v[4]
        )
        x_bad, t1_bad, t2_bad = worst[0], worst[1], worst[2]

        periods = [int(t['p_i']) for t in tasks]
        N_tsk   = len(tasks)
        N_job   = [h // periods[i] for i in range(N_tsk)]
        job_r   = {(i, j): j * periods[i]       for i in range(N_tsk) for j in range(N_job[i])}
        job_d   = {(i, j): (j + 1) * periods[i] for i in range(N_tsk) for j in range(N_job[i])}

        offenders = [
            (i, j) for (i, j), px in mapping.items()
            if px == x_bad
            and job_r[(i, j)] >= t1_bad
            and job_d[(i, j)] <= t2_bad
        ]
        if not offenders:
            break

        mi, mj = max(offenders, key=lambda ij: tasks[ij[0]]['e_m'])

        # JOB-SHARE: one job of task i occupies e_m_i/h of a processor over the
        # hyper-period, so this sums to the processor's true utilisation however
        # the task's jobs are split across cores (see quantum.py).
        util = defaultdict(float)
        for (i, j), px in mapping.items():
            util[px] += tasks[i]['e_m'] / h
        target = min((x for x in range(m) if x != x_bad), key=lambda x: util[x])
        mapping[(mi, mj)] = target

    ok, _ = check_dbf_mandatory(mapping, tasks, processors, h)
    return mapping, ok
