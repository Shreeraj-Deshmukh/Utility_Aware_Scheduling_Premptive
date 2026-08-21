"""
USRT model-runner CLI — run the offline models over generated test-cases.

Runs each instance in a sweep's manifest through the selected models and writes
a long-format results.csv (one row per instance x model) beside each manifest.
Online is intentionally excluded (it needs actual execution times).

Usage
-----
  python run_models.py <manifest.csv | sweep_dir | testcases_root> [options]

Options (defaults in brackets):
  --models M      comma list of ilp_v1,ilp_v2,heuristic   [ilp_v2,heuristic]
  --heur V        heuristic variant (v5b,v5a,v4,...)       [v5b]
  --time-limit S  Gurobi TimeLimit seconds per ILP solve  [30]
  --mip-gap G     stop ILP at this relative gap (0=exact)  [0]
  --no-resume     recompute rows already in results.csv   [resume on]

Examples
--------
  python run_models.py testcases/energy_rho/manifest.csv --models ilp_v1,ilp_v2,heuristic
  python run_models.py testcases/ --models ilp_v2,heuristic        # whole tree
  python run_models.py testcases/util_success --models heuristic   # one sweep

Notes
-----
  * ilp_v1's energy constants are auto-aligned to usrt.models (0.15/1.0); the
    ILP.py file itself still hard-codes 1.0/0.5 -- fix it there for standalone use.
  * results.csv = manifest columns + {model,status,feasible,utility,energy,
    util_per_energy,runtime,gap,error}.  Join back on 'file' to plot vs any knob.
"""

import sys
import os
import argparse

_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, ValueError):
    pass

from usrt.runner.runner import find_manifests, run_manifest


def main():
    ap = argparse.ArgumentParser(prog="run_models.py")
    ap.add_argument("target", help="manifest.csv, a sweep dir, or a testcases root")
    ap.add_argument("--models", default="ilp_v2,heuristic")
    ap.add_argument("--heur", default="v5b")
    ap.add_argument("--time-limit", type=float, default=30)
    ap.add_argument("--mip-gap", type=float, default=0.0)
    ap.add_argument("--no-resume", action="store_true")
    args = ap.parse_args()

    models = tuple(m.strip() for m in args.models.split(",") if m.strip())
    mans = find_manifests(args.target)
    print(f"models={models}  heur={args.heur}  time_limit={args.time_limit}s")
    print(f"found {len(mans)} manifest(s)\n")
    for m in mans:
        run_manifest(m, models=models, time_limit=args.time_limit,
                     heur_variant=args.heur, mip_gap=args.mip_gap,
                     resume=not args.no_resume)


if __name__ == "__main__":
    main()
