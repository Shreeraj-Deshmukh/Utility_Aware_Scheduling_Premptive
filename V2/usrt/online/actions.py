"""
Per-job online action set (the full 4-option DVFS model).

For a downstream job whose offline-committed decision is (k_off, z_off), an
online action re-selects a target (k', z') with k' in [k_off, N_seg_i] and
z' in [0, N_frq-1].  Relative to the offline baseline each action has:

    a_t  = e_eff(cum[i][k'], f_z')  - e_eff(cum[i][k_off], f_z_off)   (time)
    a_e  = E   (cum[i][k'], f_z')  - E   (cum[i][k_off], f_z_off)     (energy)
    gain = u_i * (cum[i][k'] - cum[i][k_off])                          (>= 0)

Signs encode the paper's four options (doc Section 2.4):
    k'>k_off, z'=z_off    -> Option 2  (spend: a_t>0, a_e>0, gain>0)
    k'=k_off, z'=z_off    -> Option 1  (save : a_t=0, a_e=0, gain=0)
    k'=k_off, z'<z_off    -> Option 3  (T->E: a_t>0, a_e<0, gain=0)   slower
    k'=k_off, z'>z_off    -> Option 4  (E->T: a_t<0, a_e>0, gain=0)   faster
    plus all (k'>k_off, z'!=z_off) combinations the DP may want.

Timing gate (assumption A2, doc Issue 4): an action is admissible only if its
added effective time fits the job's binding DBF window slack, i.e.
    a_t <= time_cap            (time_cap = min_slack_for_job at the baseline)
A negative a_t (frequency raised) always passes the timing gate — it frees
time rather than consuming it.

Energy is NOT gated here: it is a global, shared, possibly-replenished pool,
handled by the DP state (req_e) and the controller's pool accounting.  gain
depends only on k' (utility is earned at f_max-normalised work, paper Eq. 8),
so several (k', z') share a gain and Pareto pruning keeps the efficient ones.
"""

from collections import namedtuple

from ..models import energy_val, e_eff_val

# a_t, a_e: signed deltas vs offline baseline.  gain >= 0.  k, z: target.
Action = namedtuple("Action", ["a_t", "a_e", "gain", "k", "z"])

_TOL = 1e-9


def build_job_actions(i, k_off, z_off, cum, N_seg_i, freq_set, u_i,
                      time_cap, tol=_TOL):
    """
    Enumerate admissible online actions for one job of task i.

    Parameters
    ----------
    i         : task index (for documentation only; cum already indexed by i)
    k_off     : offline-committed segment count (online may only add: k' >= k_off)
    z_off     : offline-committed frequency index
    cum       : cum[i][k] cumulative WCET work table (at f_max)
    N_seg_i   : number of optional segments of task i (max k')
    freq_set  : list of normalised frequencies (ascending; freq_set[-1] = 1.0)
    u_i       : per-unit utility rate of task i
    time_cap  : max admissible added effective-time (binding DBF window slack);
                use float('inf') to disable the timing gate.

    Returns
    -------
    list[Action] sorted with the baseline (k_off, z_off) action first.  Always
    contains the (0, 0, 0) "save" action so the DP has a feasible no-op.
    """
    base_eff = e_eff_val(cum[i][k_off], freq_set[z_off])
    base_en  = energy_val(cum[i][k_off], freq_set[z_off])

    actions = []
    for k in range(k_off, N_seg_i + 1):
        gain = u_i * (cum[i][k] - cum[i][k_off])
        for z in range(len(freq_set)):
            fz   = freq_set[z]
            a_t  = e_eff_val(cum[i][k], fz) - base_eff
            if a_t > time_cap + tol:
                continue                     # violates this job's window slack
            a_e  = energy_val(cum[i][k], fz) - base_en
            actions.append(Action(a_t, a_e, gain, k, z))

    # Keep baseline action first for stable, readable reconstruction.
    actions.sort(key=lambda a: (a.k != k_off or a.z != z_off, a.k, a.z))
    return actions
