"""
Predicted-work weights for the SPS packer (used by ILP v3).

Why
---
`quantum_sps_mapping` packs jobs by MANDATORY work (`e_m/p_i`, now `e_m/h`).
Whatever runs after it -- the greedy phases, or an exact ILP -- then tries to
add OPTIONAL work on top.  So the packer balances a quantity that is not what
the schedule ends up carrying, and every later mapping stage (Phase 1b, 1b',
1c, 1M, 1R) is downstream compensation for that single mismatch.

This module predicts, parameter-free, how much optional work the budget can
actually afford, and hands SPS an item weight that includes it.  The DPS/SPS
criss-cross itself is untouched -- only the item sizes change.

Method
------
    f_hat = fastest frequency whose mandatory cost fits B      (budget_refine)
    S     = B - E(W_mand, f_hat)                               (energy surplus)
    greedily raise segment levels in descending u_i / g(f_hat) while S allows
    weight(i, j) = cum[i][k_hat_i] / h

`u_i / g(f)` is Phase 6b's lambda -- utility per unit energy -- and with a
common f_hat the ranking reduces to descending u_i, the same key Phase 5 uses.
No tuned constants: everything derives from B and the energy model.

Degrades gracefully: a tight budget gives k_hat = 0 and reproduces the
mandatory-only weights exactly, so this can only differ where there is surplus
to spend.
"""

from ..models import energy_val
from .budget_refine import estimate_operating_freq

_TOL = 1e-9


def predict_segment_levels(tasks, N_tsk, N_job, cum, N_seg, freq_set,
                           B_BUDGET, surplus_scale=1.0):
    """
    Returns (k_hat, f_hat, spent).

    k_hat[i] = predicted segment level for every job of task i.
    `surplus_scale` in [0,1] shrinks the surplus -- the back-off knob used when
    the resulting mapping fails its DBF check (scale 0 => mandatory-only).
    """
    f_hat = estimate_operating_freq(tasks, N_tsk, N_job, freq_set, B_BUDGET)
    g_f   = energy_val(1.0, f_hat)                 # energy per unit work at f_hat
    W_m   = sum(N_job[i] * cum[i][0] for i in range(N_tsk))
    S     = max(0.0, B_BUDGET - energy_val(W_m, f_hat)) * surplus_scale

    k_hat = [0] * N_tsk
    if S <= _TOL or g_f <= _TOL:
        return k_hat, f_hat, 0.0

    # Every next-segment step, ranked by utility per unit ENERGY (Phase 6b's
    # lambda).  Raising task i by one level costs ALL its jobs.
    steps = []
    for i in range(N_tsk):
        for k in range(N_seg[i]):
            w = cum[i][k + 1] - cum[i][k]
            if w <= _TOL:
                continue
            cost = N_job[i] * w * g_f
            steps.append((-(tasks[i]['u_i'] / g_f), i, k, cost))
    steps.sort()                                    # best utility-per-energy first

    spent = 0.0
    for _, i, k, cost in steps:
        if k_hat[i] != k:                           # segments are cumulative
            continue
        if spent + cost <= S + _TOL:
            k_hat[i] = k + 1
            spent += cost
    return k_hat, f_hat, spent


def predicted_weights(tasks, N_tsk, N_job, cum, k_hat, h):
    """Item weight per job: predicted TOTAL work share of the hyper-period."""
    return {(i, j): cum[i][k_hat[i]] / h
            for i in range(N_tsk) for j in range(N_job[i])}
