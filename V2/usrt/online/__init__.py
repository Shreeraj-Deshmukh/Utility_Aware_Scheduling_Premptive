"""
USRT Online Phase — joint (time, energy) slack distribution via precomputed DP.

Implements Section VI of the USRT paper and the design document
``usrt_online_dp_doc.pdf``.

Pipeline
--------
Offline (precompute, once per processor):
    build_processor_dp(...)         -> ProcessorDP  (exact breakpoint value fn)
Online (at every early completion, microseconds):
    OnlineController.on_completion(...) -> per-job (k, z) decisions

Design decisions (locked with the user, 2026-06):
  * Per-processor time DP (time slack is processor-local) + a single global
    energy pool arbitrated across processors by future utility density
    (doc Section 5, Approach A + C).
  * Full 4-option action set: each downstream job may re-pick BOTH its segment
    count k' >= k_off and its frequency z'.  Frequency changes implement the
    time<->energy conversion Options 3 and 4 via signed (a_t, a_e) deltas.
  * Exact breakpoint DP: states are the finite set of reachable cumulative
    (time, energy) cost vectors — no quantisation error (doc Issue 5 / 7.2).
  * Deterministic and constraint-respecting: every action is gated on DBF
    window slack + energy; the controller additionally re-verifies the full
    preemptive-EDF DBF and the global energy budget before committing.

Key modelling assumptions (see module docstrings for detail):
  A1  Online may only ADD optional segments (k' >= k_off); offline-committed
      segments are never dropped.
  A2  Time feasibility uses the binding DBF window slack of a job
      (min_slack_for_job) as the scalar a_t cap — the doc Issue-4 fix.
  A3  Global energy contention between processors is resolved by proportional
      future-utility-density share (parameter-free); a strict-priority rule is
      also provided.  The controller never lets total energy exceed B.
"""

from .value_function import Entry, prune, compose, query
from .actions        import Action, build_job_actions
from .dp             import ProcessorDP, build_processor_dp
from .density        import future_utility_density, arbitrate_energy
from .controller     import OnlineController, JobDecision
from .simulator      import OnlineSimulator, SimConfig

__all__ = [
    "Entry", "prune", "compose", "query",
    "Action", "build_job_actions",
    "ProcessorDP", "build_processor_dp",
    "future_utility_density", "arbitrate_energy",
    "OnlineController", "JobDecision",
    "OnlineSimulator", "SimConfig",
]
