"""
USRT top-level runner — select and execute any solver.

Usage
-----
  python run.py <testcase.py> [solver]

  solver (optional, default: heuristic_v4):
    ilp_v2        — Quantum SPS + Gurobi ILP optimisation
    ilp_v3        — Predicted-work SPS mapping + the SAME Gurobi ILP as v2
    heuristic_v1  — Single-pass SPS + ScheduleState + freq scaling + greedy
    heuristic_v2  — Quantum SPS + left-shift greedy (3-step cases)
    heuristic_v3  — Quantum SPS + DBF window-slack greedy, Phases 1-5
    heuristic_v4  — Quantum SPS + DBF window-slack greedy + swap, Phases 1-6
    heuristic_v5a — Quantum SPS + Refine Mapping 2a (linear doublet scan) + Phases 2-6
    heuristic_v5b — Quantum SPS + Refine Mapping 2b (one-swap-one-scan)  + Phases 2-6
    heuristic_claudeoptimal — Phases 1-6 + double-giver swap + iterated greedy
    greedy_sps_baseline — SPS mapping only, f_max fixed, greedy segments (naive floor)
    online        — Offline v5b schedule + online slack-distribution DP (Section VI)

Examples
--------
  python run.py testcase.py
  python run.py testcase.py heuristic_v5a
  python run.py testcase.py heuristic_v5b
  python run.py testcase.py ilp_v2
  python run.py testcase.py ilp_v3
  python run.py testcase.py online
"""

import sys
import os

# Force UTF-8 console output (Windows cp1252 cannot encode the α/β/box glyphs).
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, ValueError):
    pass

# Make sure the V2 directory is on the path when running as a script
_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)

from usrt.utils import load_testcase

SOLVERS = {
    "ilp_v2":                 "usrt.solvers.ilp_v2",
    "ilp_v3":                 "usrt.solvers.ilp_v3",
    "heuristic_v1":           "usrt.solvers.heuristic_v1",
    "heuristic_v2":           "usrt.solvers.heuristic_v2",
    "heuristic_v3":           "usrt.solvers.heuristic_v3",
    "heuristic_v4":           "usrt.solvers.heuristic_v4",
    "heuristic_v5a":          "usrt.solvers.heuristic_v5a",
    "heuristic_v5b":          "usrt.solvers.heuristic_v5b",
    "heuristic_v6":           "usrt.solvers.heuristic_v6",
    "heuristic_v7":           "usrt.solvers.heuristic_v7",
    "heuristic_claudeoptimal":"usrt.solvers.heuristic_claudeoptimal",
    "greedy_sps_baseline":    "usrt.solvers.greedy_sps_baseline",
    "online":                 "usrt.solvers.online_demo",
}

DEFAULT_SOLVER = "heuristic_v4"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print(f"Available solvers: {', '.join(SOLVERS)}")
        sys.exit(1)

    tc_path     = sys.argv[1]
    solver_name = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_SOLVER

    if solver_name not in SOLVERS:
        print(f"Unknown solver '{solver_name}'. Choose from: {', '.join(SOLVERS)}")
        sys.exit(1)

    print(f"Loading testcase: {tc_path}")
    processors, tasks, B_BUDGET = load_testcase(tc_path)

    import importlib
    solver_module = importlib.import_module(SOLVERS[solver_name])

    print(f"\nRunning solver: {solver_name}")
    solver_module.run(processors, tasks, B_BUDGET)


if __name__ == "__main__":
    main()
