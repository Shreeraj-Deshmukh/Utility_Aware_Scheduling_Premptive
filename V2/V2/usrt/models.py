"""
Energy model constants and per-job energy/utility functions.

Energy model:  E(i,k,z) = ALPHA * cum[i][k] / fz  +  BETA * fz^2 * cum[i][k]
Effective exec time:  e_eff(i,k,z) = cum[i][k] / fz

With ALPHA=1.0, BETA=0.5 the minimum energy is achieved at f_max.
"""

ALPHA = 1.0
BETA  = 0.5


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
