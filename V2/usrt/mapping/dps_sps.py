"""
DPS (Determining Partial Solutions) and SPS (Sum Partial Solutions) algorithms.

DPS: greedy job insertion into the partial solution with the largest gap.
SPS: iteratively combine the two partial solutions with the largest gaps.

Together they produce a near-balanced job-to-processor assignment.
"""

from .ps import PS


def run_dps(jobs_and_loads: list, m: int) -> list:
    """
    DPS procedure.

    jobs_and_loads: list of ((i, j), load_val) sorted descending by load.
    Returns: list of PS objects (partial solutions).
    """
    if not jobs_and_loads:
        return []
    key0, val0 = jobs_and_loads[0]
    active = [PS.singleton(m, key0, val0)]
    for key, val in jobs_and_loads[1:]:
        best = max(range(len(active)), key=lambda idx: active[idx].gap)
        if val <= active[best].gap:
            active[best].insert(key, val)
        else:
            active.append(PS.singleton(m, key, val))
    return active


def run_sps(ps_list: list):
    """
    SPS algorithm: iteratively combine the two PS with the biggest gaps.
    Returns a single merged PS, or None if ps_list is empty.
    """
    if not ps_list:
        return None
    active = list(ps_list)
    while len(active) > 1:
        # Largest gap first (the SPS rule).  No principled preference exists
        # among equal gaps, so the secondary key is the honest one: total load,
        # resolving the heaviest partial solution earlier; position closes the
        # order.  ps_list itself is deterministic once DPS's input is.
        active = [ps for _, ps in
                  sorted(enumerate(active),
                         key=lambda t: (-t[1].gap, -sum(t[1].loads), t[0]))]
        merged = active[0].combine(active[1])
        active = active[2:] + [merged]
    return active[0]
