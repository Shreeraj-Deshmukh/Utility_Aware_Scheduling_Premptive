"""
Per-processor online DP precompute.

Builds, once per processor, the exact breakpoint value functions for every EDF
suffix of that processor's job chain.  Because V_levels[s] is the value
function over jobs[s:], a single precompute answers *every* future completion
point: when the job at position c completes early, its windfall is distributed
over jobs[c+1:] using V_levels[c+1] — a pure lookup + reconstruction.

Time slack is processor-local, so each processor owns an independent time-DP
(doc Section 5, Approach A).  The energy axis is threaded through the same
table; the *global* coupling between processors is resolved separately by the
controller via utility-density arbitration (Approach C).

Construction is right-to-left:
    V_levels[N] = base (no jobs, zero utility)
    V_levels[s] = compose(actions(jobs[s]), V_levels[s+1])

Job execution order is EDF: (deadline, release, task, job).
"""

from collections import namedtuple

from ..dbf.slack  import min_slack_for_job
from .actions     import build_job_actions
from .value_function import base_level, compose, query

# Static per-slot metadata for one job in a processor's EDF chain.
JobSlot = namedtuple("JobSlot", ["pos", "i", "j", "k_off", "z_off", "time_cap"])

# One reconstructed online decision.
PlannedAction = namedtuple(
    "PlannedAction",
    ["pos", "i", "j", "k_off", "z_off", "k", "z", "a_t", "a_e", "gain"],
)


class ProcessorDP:
    """
    Precomputed online DP for a single processor.

    Attributes
    ----------
    x         : processor index
    slots     : list[JobSlot] in EDF order
    V_levels  : list of value-function levels; V_levels[s] covers jobs[s:]
    """

    def __init__(self, x, slots, V_levels, cum, freq_set, tasks):
        self.x        = x
        self.slots    = slots
        self.V_levels = V_levels
        self._cum     = cum
        self._freq    = freq_set
        self._tasks   = tasks

    # ── queries ────────────────────────────────────────────────────────────
    def best_value(self, start_pos, dt, de):
        """Max additional utility obtainable for jobs[start_pos:] from (dt, de)."""
        if start_pos >= len(self.slots):
            return 0.0
        e = query(self.V_levels[start_pos], dt, de)
        return e.value if e is not None else 0.0

    def distribute(self, start_pos, dt, de):
        """
        Reconstruct the optimal per-job decisions for jobs[start_pos:] given a
        windfall of (dt, de).

        Returns (total_value, [PlannedAction, ...]).  Only jobs that change
        from their baseline (k != k_off or z != z_off) are returned.
        """
        decisions = []
        s = start_pos
        N = len(self.slots)
        if s >= N:
            return 0.0, decisions

        e = query(self.V_levels[s], dt, de)
        total = e.value if e is not None else 0.0

        while e is not None and e.nxt is not None and s < N:
            slot = self.slots[s]
            if e.k is not None and (e.k != slot.k_off or e.z != slot.z_off):
                gain = self._tasks[slot.i]['u_i'] * (
                    self._cum[slot.i][e.k] - self._cum[slot.i][slot.k_off])
                decisions.append(PlannedAction(
                    pos=slot.pos, i=slot.i, j=slot.j,
                    k_off=slot.k_off, z_off=slot.z_off,
                    k=e.k, z=e.z, a_t=e.a_t, a_e=e.a_e, gain=gain))
            nxt = self.V_levels[s + 1][e.nxt]
            e = nxt
            s += 1

        # Last consumed level (e.nxt is None) — handle its own job decision.
        if e is not None and s < N and e.k is not None:
            slot = self.slots[s]
            if e.k != slot.k_off or e.z != slot.z_off:
                gain = self._tasks[slot.i]['u_i'] * (
                    self._cum[slot.i][e.k] - self._cum[slot.i][slot.k_off])
                decisions.append(PlannedAction(
                    pos=slot.pos, i=slot.i, j=slot.j,
                    k_off=slot.k_off, z_off=slot.z_off,
                    k=e.k, z=e.z, a_t=e.a_t, a_e=e.a_e, gain=gain))

        return total, decisions


def _edf_order(jobs_x, job_r, job_d):
    """Sort a processor's jobs into EDF execution order."""
    return sorted(jobs_x, key=lambda ij: (job_d[ij], job_r[ij], ij[0], ij[1]))


def build_processor_dp(x, proc_jobs, seg_k, freq_idx, job_r, job_d,
                       cum, N_seg, freq_set, tasks, time_caps=None,
                       max_frontier=None):
    """
    Construct the ProcessorDP for processor x from an offline schedule.

    Parameters mirror the heuristic solvers' state.  `time_caps` optionally
    overrides the per-job DBF window-slack cap (keyed by (i, j)); when omitted
    it is computed with min_slack_for_job at the offline-committed state.
    `max_frontier` optionally caps each level's Pareto frontier (aggregate
    states) — required when DVFS is active or the exact frontier can explode.

    Returns a ProcessorDP (with V_levels precomputed for every suffix).
    """
    jobs_x = _edf_order(list(proc_jobs[x]), job_r, job_d)

    slots = []
    for pos, (i, j) in enumerate(jobs_x):
        k_off = seg_k[(i, j)]
        z_off = freq_idx[(i, j)]
        if time_caps is not None and (i, j) in time_caps:
            cap = time_caps[(i, j)]
        else:
            cap = min_slack_for_job(i, j, x, proc_jobs, job_r, job_d,
                                    seg_k, freq_idx, freq_set, cum)
        slots.append(JobSlot(pos, i, j, k_off, z_off, cap))

    # Right-to-left DP.
    N = len(slots)
    V_levels = [None] * (N + 1)
    V_levels[N] = base_level()
    for s in range(N - 1, -1, -1):
        slot = slots[s]
        acts = build_job_actions(
            slot.i, slot.k_off, slot.z_off, cum, N_seg[slot.i],
            freq_set, tasks[slot.i]['u_i'], slot.time_cap)
        V_levels[s] = compose(acts, V_levels[s + 1], max_frontier=max_frontier)

    return ProcessorDP(x, slots, V_levels, cum, freq_set, tasks)
