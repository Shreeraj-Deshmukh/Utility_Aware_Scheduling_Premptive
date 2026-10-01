"""
USRT model-runner CLI — run the offline models over generated test-cases.

Runs each instance in a sweep's manifest through the selected models and writes
a long-format results.csv (one row per instance x model) beside each manifest.

--online additionally runs the online phase on top of each solver's committed
schedule.  It is a MODIFIER, not a model: the online phase does not compete with
the solvers, it tops up whatever schedule one of them produced, so its numbers
are extra COLUMNS on that solver's row.  Every online result therefore stays
paired with the offline schedule it came from, with no join.  ACETs come from
the per-task `theta` the generator bakes into each instance (theta ~ U(xi, 1)),
so runs are reproducible and `xi` is the OFAT factor that drives them.

Usage
-----
  python run_models.py <manifest.csv | sweep_dir | testcases_root> [options]

Options (defaults in brackets):
  --models M      comma list of ilp_v1,ilp_v2,ilp_v3,heuristic,
                  heuristic_v3..v7, greedy_sps_baseline   [ilp_v2,heuristic]
  --heur V        heuristic variant (v5b,v5a,v4,...)       [v5b]
  --time-limit S  Gurobi TimeLimit seconds per ILP solve  [30]
  --mip-gap G     stop ILP at this relative gap (0=exact)  [0]
  --online        also run the online phase on each schedule [off]
  --no-resume     recompute rows already in results.csv   [resume on]

Examples
--------
  python run_models.py testcases/energy_rho/manifest.csv --models ilp_v1,ilp_v2,heuristic
  python run_models.py testcases/ --models ilp_v2,heuristic        # whole tree
  python run_models.py testcases/x/manifest.csv --models ilp_v2,ilp_v3  # mapping A/B
  python run_models.py testcases/util_success --models heuristic   # one sweep
  python run_models.py tc_x --models ilp_v1,ilp_v4 --online        # + online phase
  python run_models.py tc_x/xi --models heuristic --heur v5b --online

Notes
-----
  * ilp_v1's energy constants are auto-aligned to usrt.models (0.15/1.0); the
    ILP.py file itself still hard-codes 1.0/0.5 -- fix it there for standalone use.
  * results.csv = manifest columns + {model,status,feasible,utility,energy,
    util_per_energy,runtime,gap,error}.  Join back on 'file' to plot vs any knob.
  * --online appends {online_utility,online_added,online_feasible,
    online_wcet_energy,online_realised_energy,online_trim_loss,
    online_trim_events,online_mean_theta,online_runtime}.  online_wcet_energy
    MAY exceed B and that is not a violation -- it is the worst-case commitment,
    over-counted by exactly what the early finishers saved; online_realised_energy
    is the one C3 binds on.  --online widens the schema, so its results.csv
    cannot be shared with a plain run's (the header guard will refuse).
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
    ap.add_argument("--online", action="store_true",
                    help="also run the online phase on each committed schedule")
    ap.add_argument("--acet-ratio", type=float, default=None,
                    help="fixed theta for EVERY job, overriding the test case's "
                         "per-task theta; makes theta an experiment axis")
    ap.add_argument("--out", default="results.csv",
                    help="results filename written next to each manifest; give a "
                         "distinct name per --acet-ratio so a theta grid does not "
                         "collide (e.g. results_t0.7.csv)")
    ap.add_argument("--no-resume", action="store_true")
    args = ap.parse_args()

    models = tuple(m.strip() for m in args.models.split(",") if m.strip())
    mans = find_manifests(args.target)
    print(f"models={models}  heur={args.heur}  time_limit={args.time_limit}s"
          f"  online={'on' if args.online else 'off'}")
    print(f"found {len(mans)} manifest(s)\n")
    for m in mans:
        run_manifest(m, models=models, time_limit=args.time_limit,
                     heur_variant=args.heur, mip_gap=args.mip_gap,
                     resume=not args.no_resume, online=args.online,
                     acet_ratio=args.acet_ratio, out_name=args.out)


if __name__ == "__main__":
    main()
