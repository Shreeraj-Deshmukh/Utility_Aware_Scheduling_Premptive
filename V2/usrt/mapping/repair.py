"""
Mandatory-only DBF feasibility check and greedy repair for the SPS mapping.

check_dbf_mandatory: verifies DBF(t1,t2,x) ≤ t2-t1 using e_m at f_max.
repair_mapping: best-improvement single-job moves, then pairwise swaps,
                against a monotone total-excess objective (see
                repair_mapping's docstring for why this replaced the earlier
                always-move-the-biggest-job rule).
"""

from collections import defaultdict

# Caps on the per-iteration search so a stuck repair can't blow up on a large
# instance: try only the few worst windows, and only the few biggest offenders
# in each, before giving up on that iteration.  Targets are never capped (m is
# small in practice) since trying every processor is what fixed the oscillation.
_MAX_WINDOWS_TRIED      = 5
_MAX_OFFENDERS_TRIED    = 5
_MAX_SWAP_PARTNERS_TRIED = 10


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


def _total_excess(mapping, tasks, processors, h):
    """Sum of (demand - cap) over every currently-violated window.  0 iff feasible."""
    _, viols = check_dbf_mandatory(mapping, tasks, processors, h)
    return sum(dem - cap for vlist in viols.values() for (_, _, dem, cap) in vlist)


def repair_mapping(mapping, tasks, processors, h, max_iters=100):
    """
    Greedy DBF repair via best-improvement single-job moves.

    History. The original version always moved the single biggest offender in
    the single worst-violated window to whichever processor had the lowest
    GLOBAL utilisation, unconditionally, with no memory of earlier moves.
    Measured live (2026-09-12): this OSCILLATES. Moving the offending job to
    fix window A can make it the single biggest job in some other window B
    (e.g. one spanning the whole hyper-period); the next iteration then moves
    it straight back to fix B, recreating A -- a 2-cycle that burns every one
    of the 100 iterations and returns the ORIGINAL, unmodified, still-
    infeasible mapping. Brute force confirmed the fix existed in 100% of a
    26-instance sample (u_mand_factor in [0.6,0.9], n_prc=2) -- the old
    algorithm simply never found it.

    Fix, tier 1 (single-job moves). Track a single scalar objective, total DBF
    excess (sum of demand-cap over every violated window; 0 iff feasible).
    Only ever commit a candidate move if it STRICTLY decreases this total --
    trying, in order, the `_MAX_WINDOWS_TRIED` worst windows, the
    `_MAX_OFFENDERS_TRIED` biggest jobs in each, and every other processor as
    a target. Since total excess is a bounded, non-negative quantity that
    only ever strictly decreases on an accepted move, no mapping can repeat
    and the oscillation above is structurally impossible.

    Fix, tier 2 (pairwise swaps). Tier 1 alone still has a real limit, found
    live on the same date: a genuine fix can require moving offender A to
    processor X *while simultaneously* moving some job B the other way, where
    the A-move ALONE, evaluated on its own, makes total excess WORSE (it just
    relocates the violation rather than removing it) -- so tier 1 can never
    take that first step, even though the fix is one atomic move away.
    Measured case: window excess 2.09 -> (single move alone) 14.83 -> (second
    single move) 0 -- non-monotonic, so tier 1 stops after the first move
    looks like a regression. The SAME two reassignments applied as one
    simultaneous swap take total excess directly 2.09 -> 0. So when tier 1
    finds no improving single move, tier 2 tries swapping each offender with
    each of the `_MAX_SWAP_PARTNERS_TRIED` biggest jobs on a different
    processor, evaluating the swap as one atomic unit against the same
    strict-improvement criterion.

    If neither tier improves, that is a genuine local optimum for this move
    set -- stop immediately (rather than exhausting max_iters on moves that
    cannot help) and report PARTIAL.

    Returns (mapping, is_feasible).
    """
    m = len(processors)
    cur_excess = _total_excess(mapping, tasks, processors, h)

    for _ in range(max_iters):
        if cur_excess <= 1e-9:
            return mapping, True

        ok, viols = check_dbf_mandatory(mapping, tasks, processors, h)
        if ok:
            return mapping, True

        periods = [int(t['p_i']) for t in tasks]
        N_tsk   = len(tasks)
        N_job   = [h // periods[i] for i in range(N_tsk)]
        job_r   = {(i, j): j * periods[i]       for i in range(N_tsk) for j in range(N_job[i])}
        job_d   = {(i, j): (j + 1) * periods[i] for i in range(N_tsk) for j in range(N_job[i])}

        windows_by_excess = sorted(
            ((x, t1, t2, dem, cap)
             for x, vlist in viols.items()
             for (t1, t2, dem, cap) in vlist),
            key=lambda v: -(v[3] - v[4])
        )[:_MAX_WINDOWS_TRIED]

        moved = False

        # ── tier 1: single-job moves ─────────────────────────────────────
        for (x_bad, t1_bad, t2_bad, _dem, _cap) in windows_by_excess:
            offenders = sorted(
                [(i, j) for (i, j), px in mapping.items()
                 if px == x_bad
                 and job_r[(i, j)] >= t1_bad
                 and job_d[(i, j)] <= t2_bad],
                key=lambda ij: -tasks[ij[0]]['e_m']
            )[:_MAX_OFFENDERS_TRIED]
            if not offenders:
                continue

            # JOB-SHARE: one job of task i occupies e_m_i/h of a processor over
            # the hyper-period, so this sums to the processor's true
            # utilisation however the task's jobs are split across cores.
            util = defaultdict(float)
            for (i, j), px in mapping.items():
                util[px] += tasks[i]['e_m'] / h
            targets = sorted((x for x in range(m) if x != x_bad), key=lambda x: util[x])

            for (mi, mj) in offenders:
                old_px = mapping[(mi, mj)]
                for target in targets:
                    mapping[(mi, mj)] = target
                    new_excess = _total_excess(mapping, tasks, processors, h)
                    if new_excess < cur_excess - 1e-9:
                        cur_excess = new_excess
                        moved = True
                        break
                    mapping[(mi, mj)] = old_px      # no improvement -- revert
                if moved:
                    break
            if moved:
                break

        # ── tier 2: pairwise swaps (only if tier 1 found nothing) ─────────
        if not moved:
            for (x_bad, t1_bad, t2_bad, _dem, _cap) in windows_by_excess:
                offenders = sorted(
                    [(i, j) for (i, j), px in mapping.items()
                     if px == x_bad
                     and job_r[(i, j)] >= t1_bad
                     and job_d[(i, j)] <= t2_bad],
                    key=lambda ij: -tasks[ij[0]]['e_m']
                )[:_MAX_OFFENDERS_TRIED]
                if not offenders:
                    continue

                partners = sorted(
                    [(i, j) for (i, j), px in mapping.items() if px != x_bad],
                    key=lambda ij: -tasks[ij[0]]['e_m']
                )[:_MAX_SWAP_PARTNERS_TRIED]

                for (mi, mj) in offenders:
                    old_a = mapping[(mi, mj)]
                    for (pi, pj) in partners:
                        if (pi, pj) == (mi, mj):
                            continue
                        old_b = mapping[(pi, pj)]
                        mapping[(mi, mj)] = old_b
                        mapping[(pi, pj)] = old_a
                        new_excess = _total_excess(mapping, tasks, processors, h)
                        if new_excess < cur_excess - 1e-9:
                            cur_excess = new_excess
                            moved = True
                            break
                        mapping[(mi, mj)] = old_a       # no improvement -- revert both
                        mapping[(pi, pj)] = old_b
                    if moved:
                        break
                if moved:
                    break

        if not moved:
            break   # local optimum for single-move + swap -- report PARTIAL

    ok, _ = check_dbf_mandatory(mapping, tasks, processors, h)
    return mapping, ok
