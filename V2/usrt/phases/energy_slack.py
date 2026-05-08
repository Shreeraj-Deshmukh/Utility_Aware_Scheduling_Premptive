"""
Phase 3 — Energy slack computation.

compute_energy_slack: returns (E_consumed, E_slack).
"""

from ..models import total_energy


def compute_energy_slack(seg_k, freq_idx, freq_set, cum,
                         N_tsk, N_job, B_BUDGET) -> tuple:
    """Returns (E_consumed, E_slack) = (E_consumed, B_BUDGET - E_consumed)."""
    E_consumed = total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job)
    return E_consumed, B_BUDGET - E_consumed
