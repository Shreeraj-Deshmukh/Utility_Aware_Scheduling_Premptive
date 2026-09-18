"""
Online-phase demo solver.

Builds an offline schedule with the v5b pipeline (Quantum SPS + Refine 2b +
greedy/swap), then runs the online slack-distribution simulator on top of it.

  python run.py testcase.py online

This is the integration entry point for usrt.online.  It also runs the
worked-example verification first, so a single command proves both that the DP
core matches the design document and that the online phase improves a real
offline schedule while preserving all constraints.
"""

import contextlib
import io

from ..models   import ALPHA, BETA
from ..utils    import lcm_list, gcd_list, build_cum
from ..output   import print_instance_summary
from ..phases.energy_slack    import min_possible_energy
from ..online.simulator       import OnlineSimulator, SimConfig
from ..online.worked_examples import verify as verify_worked_examples
from .          import heuristic_v5b

_S  = "=" * 76
_S2 = "-" * 76


def offline_schedule(processors, tasks, B_BUDGET):
    """
    Build the online phase's input with the REAL v5b pipeline, quietly.
    Returns (seg_k, freq_idx, mapping).

    This calls `heuristic_v5b.run()` rather than re-deriving its phase list.
    The hand-rolled version it replaces ran Quantum SPS + Refine 2b + phases
    4/5/6 only, so it silently skipped Phase 3's `min_possible_energy`
    infeasibility gate and Phase 6b's frequency<->segment trade — the online
    phase was therefore topping up a schedule no other solver would have
    produced (ISSUES.md -> ONLINE-DEMO).  Invisible at slack budgets where both
    are no-ops; divergent at tight rho, which is exactly where online matters.

    `run()` prints a full phase-by-phase report unconditionally and takes no
    verbosity flag, so its stdout is captured here; the caller prints its own
    one-line summary instead.
    """
    with contextlib.redirect_stdout(io.StringIO()):
        seg_k, freq_idx, _utility, _energy, mapping = heuristic_v5b.run(
            processors, tasks, B_BUDGET)
    return seg_k, freq_idx, mapping


def _mandatory_affordable(tasks, processors, B_BUDGET, N_tsk, N_job):
    """
    Phase 3's terminal test, applied before we bother building anything.

    Mirrors `heuristic_v5b.run()`'s own gate so this entry point can say so
    plainly: below this bound no frequency assignment whatsoever fits the
    budget, and v5b would return a mandatory-only schedule that is not a
    solution.  Running the online simulator on top of that would report an
    infeasible pool from its first line, which reads like a bug rather than an
    infeasible instance.
    """
    cum, _N_seg = build_cum(tasks)
    freq_set    = processors[0]['frequencies']
    seg_k       = {(i, j): 0 for i in range(N_tsk) for j in range(N_job[i])}
    floor       = min_possible_energy(seg_k, freq_set, cum, N_tsk, N_job)
    return floor <= B_BUDGET + 1e-9, floor


def run(processors, tasks, B_BUDGET):
    N_tsk   = len(tasks)
    periods = [int(t['p_i']) for t in tasks]
    h       = lcm_list(periods)
    quantum = gcd_list(periods)
    _, N_seg = build_cum(tasks)
    N_job   = [h // periods[i] for i in range(N_tsk)]

    print_instance_summary(processors, tasks, B_BUDGET, h, quantum, N_job, N_seg,
                           ALPHA, BETA, label="USRT Online Phase  —  Instance")

    # 1) DP core vs the design document.
    verify_worked_examples()

    # 2) Offline schedule (the precompute's input).
    print(f"\n{_S}")
    print("  OFFLINE SCHEDULE  (v5b pipeline)")
    print(_S2)
    ok, floor = _mandatory_affordable(tasks, processors, B_BUDGET, N_tsk, N_job)
    if not ok:
        print(f"  Budget {B_BUDGET:.4f} is below the cheapest possible mandatory cost "
              f"{floor:.4f}")
        print("  — infeasible at any frequency, so there is no schedule to top up.")
        print("  Skipping the online simulation.")
        print(_S)
        return None
    seg_k, freq_idx, mapping = offline_schedule(processors, tasks, B_BUDGET)
    print("  Offline schedule built via heuristic_v5b.run() "
          "(full pipeline: Phases 1-6b).")

    # 3) Online simulation over a hyper-period of early completions.
    cfg = SimConfig(acet_ratio=0.7, arbitration="proportional", verbose=True)
    sim = OnlineSimulator(processors, tasks, B_BUDGET, seg_k, freq_idx, mapping,
                          config=cfg)
    summary = sim.run()
    return summary
