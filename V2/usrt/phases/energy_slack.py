"""
Phase 3 — Energy slack computation.

compute_energy_slack: returns (E_consumed, E_slack).
"""

from ..models import total_energy, energy_val


def compute_energy_slack(seg_k, freq_idx, freq_set, cum,
                         N_tsk, N_job, B_BUDGET) -> tuple:
    """Returns (E_consumed, E_slack) = (E_consumed, B_BUDGET - E_consumed)."""
    E_consumed = total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job)
    return E_consumed, B_BUDGET - E_consumed


def min_possible_energy(seg_k, freq_set, cum, N_tsk, N_job) -> float:
    """
    Lower bound on total energy for the CURRENT segment selection: every job at
    its cheapest available frequency, ignoring timing.

    This is the correct terminal-infeasibility test for Phase 3.  Testing the
    budget at f_max is wrong, because Phase 4 exists precisely to lower
    frequency: in this energy model g(f) = ALPHA/f + BETA*f^2 is minimised at
    f* = (ALPHA/2BETA)^(1/3), so running slower can be far cheaper than f_max
    (e.g. 0.55 vs 1.15 per unit work at ALPHA=0.15, BETA=1.0).

    Ignoring timing only makes the bound looser, so `B < min_possible_energy`
    is a genuine *necessary* condition for infeasibility -- if it holds, no
    frequency assignment whatsoever can fit the budget.  If it does not hold,
    Phase 4 must be given the chance to scale before giving up.
    """
    return sum(
        min(energy_val(cum[i][seg_k[(i, j)]], f) for f in freq_set)
        for i in range(N_tsk)
        for j in range(N_job[i])
    )
