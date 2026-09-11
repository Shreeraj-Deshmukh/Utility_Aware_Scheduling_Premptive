"""
Future utility density + global-energy arbitration (doc Section 5, Approach C).

Time slack is processor-local, so each processor's time-DP is independent.  The
energy slack is a single global pool that all processors draw from, which is
the one thing coupling them.  When several processors could spend the same
energy, we resolve contention with a precomputed priority — the paper's own
suggestion: "consider the job which has more higher density in the future."

Future utility density of processor x at time t:

    rho_x(t) = sum over jobs (i, j) on x with release r_{i,j} >= t of
                   u_i * (remaining addable optional work of (i,j)) / p_i

"remaining addable optional work" = cum[i][N_seg_i] - cum[i][k_committed],
i.e. the optional work that online execution could still add.  A processor with
more valuable upcoming work has the stronger claim on shared energy.

Assumption A3: contention is resolved by *proportional* density share
(parameter-free) by default; a strict-priority rule is also provided.  Either
way the controller guarantees total energy never exceeds the budget B.
"""

_TOL = 1e-9


def future_utility_density(x, t, proc_jobs, tasks, cum, N_seg, seg_k,
                           job_r, periods):
    """
    rho_x(t): density of still-addable optional utility on processor x from
    time t onward.  Uses the *current committed* seg_k so it reflects what is
    still available to schedule online.
    """
    rho = 0.0
    for (i, j) in proc_jobs[x]:
        if job_r[(i, j)] < t - _TOL:
            continue
        remaining = cum[i][N_seg[i]] - cum[i][seg_k[(i, j)]]
        if remaining <= _TOL:
            continue
        rho += tasks[i]['u_i'] * remaining / periods[i]
    return rho


def arbitrate_energy(pool, densities, mode="proportional"):
    """
    Decide how much of the global energy `pool` each processor may claim.

    Parameters
    ----------
    pool      : current global energy slack (>= 0)
    densities : {proc_idx: rho_x(t)} at the arbitration instant
    mode      : "proportional"  -> cap_x = pool * rho_x / sum(rho)
                "strict"        -> the single highest-rho processor gets the
                                   whole pool, the rest get 0

    Returns {proc_idx: energy_cap}.  If every density is ~0, the pool is shared
    equally (nothing has a stronger claim).
    """
    procs = list(densities.keys())
    if pool <= _TOL or not procs:
        return {x: 0.0 for x in procs}

    total = sum(max(0.0, densities[x]) for x in procs)

    if total <= _TOL:
        share = pool / len(procs)
        return {x: share for x in procs}

    if mode == "strict":
        top = max(procs, key=lambda x: densities[x])
        return {x: (pool if x == top else 0.0) for x in procs}

    # proportional (default)
    return {x: pool * max(0.0, densities[x]) / total for x in procs}
