"""
Phase 3 (ScheduleState variant) — Greedy optional segment addition.

Visits jobs in decreasing u_i order. For each j*:
  - Directly tries try_inc_seg (atomic move on state).
  - On failure, tries freeing moves on overlapping jobs:
      (A) try_inc_freq on each overlapping job (frees time, costs energy)
      (B) try_dec_seg  on each overlapping job (frees time and energy)
  - After a freeing move, retries try_inc_seg once.

Used by heuristic_v1 (ScheduleState-based pipeline).
"""

from ..state import ScheduleState


def greedy_optional_segments(state: ScheduleState) -> int:
    """
    Add optional segments greedily. Returns total segments added.
    """
    job_order = [
        (i, j)
        for i in range(state.N_tsk)
        for j in range(state.N_job[i])
    ]
    job_order.sort(key=lambda ij: -state.tasks[ij[0]]['u_i'])

    total_added = 0

    for (i, j) in job_order:
        while True:
            if state.seg_k[(i, j)] >= state.N_seg[i]:
                break
            if state.slack_energy <= 1e-9:
                break

            if state.try_inc_seg(i, j):
                total_added += 1
                continue

            freed       = False
            overlapping = state.overlapping_jobs(i, j)

            # (A) increment frequency of an overlapping job
            for (ii, jj) in overlapping:
                if state.try_inc_freq(ii, jj):
                    freed = True
                    break

            # (B) decrement segment of an overlapping job
            if not freed:
                for (ii, jj) in overlapping:
                    if state.seg_k[(ii, jj)] > 0:
                        if state.try_dec_seg(ii, jj):
                            freed = True
                            break

            if not freed:
                break

            if not state.try_inc_seg(i, j):
                break

            total_added += 1

    return total_added
