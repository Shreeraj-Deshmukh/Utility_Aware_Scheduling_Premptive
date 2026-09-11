"""
Timing-grade runner: best-of-N repeats, explicit censoring, no silent caps.

Why this exists
---------------
`run_models.py` times each (instance, model) ONCE.  A single measurement was
shown to be wrong by 97x: heuristic_v7 on tc_sept_paper/n_frq/set39/n_frq_2.py
recorded 90.695 s and replays in 0.27 s with byte-identical output -- the OS had
descheduled the process.  Any runtime conclusion drawn from single runs is
therefore unsafe.

What this does differently
--------------------------
  * BEST-OF-N (default 3).  Keeps the MINIMUM wall time across repeats, which is
    the standard estimator for "how long does this actually take" -- the minimum
    is the run least polluted by unrelated system activity.
  * VERIFIES DETERMINISM.  Every repeat must return the same utility; a mismatch
    is recorded in `nondeterministic`, because a solver whose output varies run
    to run invalidates any single-number comparison.
  * RECORDS CENSORING EXPLICITLY.  A run that hits the solver time limit is
    marked censored=1 and its runtime is a LOWER BOUND, never a measurement.
    Censored runs must be excluded from runtime statistics, not averaged in --
    a solver that times out otherwise appears artificially fast.
  * SKIPS REPEATS ON SLOW RUNS.  If the first repeat exceeds --repeat-cutoff
    seconds, no further repeats are taken (the OS-artifact risk is proportionally
    tiny there, and the cost is not).  `repeats` records how many were actually
    run, so the estimator is never misreported.

Output columns added over run_models.py:
    runtime_best, runtime_worst, repeats, censored, nondeterministic

Usage:
    python run_timed.py <dir> --models a,b,c --heur v6 --time-limit 300
"""

import argparse, csv, os, sys, time, glob, importlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from usrt.utils import load_testcase
from usrt.runner.adapters import run_model

EXTRA = ["runtime_best", "runtime_worst", "repeats", "censored", "nondeterministic"]


def timed_run(model, procs, tasks, B, heur, time_limit, repeats, cutoff):
    """Run `model` up to `repeats` times; return the merged metric dict."""
    best = None
    times, utils = [], []
    n = 0
    for i in range(repeats):
        kw = {}
        if model.startswith("heuristic"):
            kw["heur_variant"] = heur          # run_model's parameter name
        t0 = time.perf_counter()
        m = run_model(model, procs, tasks, B, time_limit=time_limit, **kw)
        el = time.perf_counter() - t0
        n += 1
        times.append(el)
        utils.append(m.get("utility", ""))
        if best is None or el < float(best["runtime"] or el):
            best = dict(m)
            best["runtime"] = round(el, 6)
        # a genuinely slow solve is not worth repeating
        if el > cutoff:
            break
    censored = 1 if best.get("status") in ("timeout", "time_limit") else 0
    nd = 0
    seen = {u for u in utils if u not in ("", None)}
    if len(seen) > 1:
        nd = 1
    best["runtime_best"] = round(min(times), 6)
    best["runtime_worst"] = round(max(times), 6)
    best["repeats"] = n
    best["censored"] = censored
    best["nondeterministic"] = nd
    best["runtime"] = round(min(times), 6)
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--models", default="ilp_v1,ilp_v2,ilp_v3,ilp_v4,heuristic,greedy_sps_baseline")
    ap.add_argument("--heur", default="v6")
    ap.add_argument("--time-limit", type=float, default=300.0)
    ap.add_argument("--repeats", type=int, default=3)
    ap.add_argument("--repeat-cutoff", type=float, default=20.0,
                    help="seconds; skip further repeats once a run exceeds this")
    ap.add_argument("--out", default="results_timed.csv")
    a = ap.parse_args()

    manifests = sorted(glob.glob(os.path.join(a.path, "**", "manifest.csv"), recursive=True))
    models = [m.strip() for m in a.models.split(",") if m.strip()]

    for man_path in manifests:
        base = os.path.dirname(man_path)
        rows = list(csv.DictReader(open(man_path)))
        if not rows:
            continue
        out_path = os.path.join(base, a.out)
        done = set()
        cols = list(rows[0].keys()) + ["model", "status", "model_feasible", "utility",
                                       "energy", "util_per_energy", "runtime", "gap",
                                       "error"] + EXTRA
        if os.path.exists(out_path):
            prev = list(csv.DictReader(open(out_path)))
            if prev and list(prev[0].keys()) != cols:
                raise SystemExit(f"schema mismatch in {out_path}; delete it and re-run")
            done = {(r["file"], r["model"]) for r in prev}
        fh = open(out_path, "a", newline="")
        w = csv.DictWriter(fh, fieldnames=cols)
        if not done:
            w.writeheader()

        t0 = time.time()
        n = 0
        for r in rows:
            path = os.path.join(base, *r["file"].split(os.sep)[1:])
            if not os.path.exists(path):
                path = os.path.join(a.path, r["file"])
            if not os.path.exists(path):
                continue
            procs, tasks, B = load_testcase(path)
            for model in models:
                key = model if model != "heuristic" else f"heuristic_{a.heur}"
                if (r["file"], key) in done:
                    continue
                m = timed_run(model, procs, tasks, B, a.heur, a.time_limit,
                              a.repeats, a.repeat_cutoff)
                row = dict(r)
                row.update(m)
                w.writerow({c: row.get(c, "") for c in cols})
                n += 1
            fh.flush()
        fh.close()
        print(f"    done: {n} runs in {time.time()-t0:.1f}s  ->  {out_path}")


if __name__ == "__main__":
    main()
