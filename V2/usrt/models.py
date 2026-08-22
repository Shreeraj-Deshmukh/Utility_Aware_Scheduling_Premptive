"""
Energy model constants and per-job energy/utility functions.

Energy model:  E(i,k,z) = ALPHA * cum[i][k] / fz  +  BETA * fz^2 * cum[i][k]
Effective exec time:  e_eff(i,k,z) = cum[i][k] / fz

Energy per unit work is  g(f) = ALPHA/f + BETA*f^2,  minimised at
    f* = (ALPHA / 2*BETA)^(1/3)
With the current ALPHA=0.15, BETA=1.0 that is f* ~= 0.42, so running BELOW
f_max is cheaper per unit of work (g(0.4)=0.535 vs g(1.0)=1.150, a 2.15x
difference) -- which is what makes DVFS worth anything here.
(Under the older ALPHA=1.0, BETA=0.5 the minimum sat at f_max and DVFS was
degenerate; several files still hard-coded that stale pair until 22 Aug.)

This module is the SINGLE SOURCE OF TRUTH for ALPHA/BETA -- every solver,
the generator and the runner import them from here.  Do not re-declare them.
"""

ALPHA = 0.15
BETA  = 1.0


def energy_val(cum_k: float, fz: float) -> float:
    return ALPHA * cum_k / fz + BETA * fz ** 2 * cum_k


def e_eff_val(cum_k: float, fz: float) -> float:
    return cum_k / fz


def total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job) -> float:
    return sum(
        energy_val(cum[i][seg_k[(i, j)]], freq_set[freq_idx[(i, j)]])
        for i in range(N_tsk)
        for j in range(N_job[i])
    )


def total_utility(seg_k, tasks, cum, N_tsk, N_job) -> float:
    return sum(
        tasks[i]['u_i'] * (cum[i][seg_k[(i, j)]] - cum[i][0])
        for i in range(N_tsk)
        for j in range(N_job[i])
    )
