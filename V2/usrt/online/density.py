"""
Future utility density + global-energy arbitration (doc Section 5, Approach C).

Time slack is processor-local, so each processor's time-DP is independent.  The
energy slack is a single global pool that all processors draw from, which is
the one thing coupling them.  When several processors could spend the same
energy, we resolve contention with a precomputed priority — the paper's own
suggestion: "consider the job which has more higher density in the future."

Future utility density of processor x:

    rho_x = sum over jobs (i, j) on x that are NOT yet resolved of
                   u_i * (remaining addable optional work of (i,j)) / p_i

"remaining addable optional work" = cum[i][N_seg_i] - cum[i][k_committed],
i.e. the optional work that online execution could still add.  A processor with
more valuable upcoming work has the stronger claim on shared energy.

"Not yet resolved" means the job's own completion event has not fired, i.e. it
is absent from the controller's `eff_override`.  This used to be approximated
by "released at or after the arbitration instant t" (ISSUES.md -> I2), which
excluded a job that was released earlier but still pending — understating its
processor's claim in precisely the contended case the arbitration exists to
handle.  The question was never *when* a job arrives but whether its fate is
already decided: a job still pending can gain optional segments (an already-
started job may still grow k — see ONLINE-FREQ), so it still has a live claim;
a completed one cannot, whatever its release time.  Asking `eff_override`
directly is both exact and removes the need for any notion of "now" here.

Assumption A3: contention is resolved by *proportional* density share
(parameter-free) by default; a strict-priority rule is also provided.  Either
way the controller guarantees total energy never exceeds the budget B.
"""

_TOL = 1e-9


def future_utility_density(x, proc_jobs, tasks, cum, N_seg, seg_k, periods,
                           completed=None):
    """
    rho_x: density of still-addable optional utility on processor x.  Uses the
    *current committed* seg_k so it reflects what is still available to
    schedule online.

    `completed` is the set/mapping of jobs whose own completion has already
    fired (the controller's `eff_override`); those are resolved history and
    contribute nothing.  Pass None to count every job on the processor.
    """
    rho = 0.0
    for (i, j) in proc_jobs[x]:
        if completed is not None and (i, j) in completed:
            continue
        remaining = cum[i][N_seg[i]] - cum[i][seg_k[(i, j)]]
        if remaining <= _TOL:
            continue
        rho += tasks[i]['u_i'] * remaining / periods[i]
    return rho


def arbitrate_energy(pool, densities, mode="proportional", demand=None):
    """
    Decide how much of the global energy `pool` each processor may claim.

    Parameters
    ----------
    pool      : current global energy slack (>= 0)
    densities : {proc_idx: rho_x} at the arbitration instant
    mode      : "proportional"  -> cap_x = pool * rho_x / sum(rho)
                "strict"        -> the single highest-rho processor gets the
                                   whole pool, the rest get 0
    demand    : D from `OnlineController._addable_demand`, or None to always
                ration (the pre-§IX.B behaviour)
                (the pre-§IX.B behaviour)

    Returns {proc_idx: energy_cap}.  If every density is ~0, the pool is shared
    equally (nothing has a stronger claim).

    Surplus branch (paper §IX.B, ISSUES.md -> IXB-ROUTING): when `pool >= D`
    every live claim can be met at once, so rationing can only strand energy.
    Approach C as originally coded *always* split, capping a processor at a
    fraction of a pool nobody else wanted — measured on testcase.py, that cost
    5.55 utility (27.87 vs 33.42) while leaving 8 more energy units unspent.
    Nothing here is tuned: both `pool` and `demand` are observed.
    """
    procs = list(densities.keys())
    if pool <= _TOL or not procs:
        return {x: 0.0 for x in procs}

    if demand is not None and pool >= demand - _TOL:
        return {x: pool for x in procs}          # surplus: do not ration

    total = sum(max(0.0, densities[x]) for x in procs)

    if total <= _TOL:
        share = pool / len(procs)
        return {x: share for x in procs}

    if mode == "strict":
        top = max(procs, key=lambda x: densities[x])
        return {x: (pool if x == top else 0.0) for x in procs}

    # proportional (default)
    return {x: pool * max(0.0, densities[x]) / total for x in procs}
