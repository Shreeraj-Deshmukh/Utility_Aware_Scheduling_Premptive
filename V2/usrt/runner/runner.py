"""
Walk a sweep manifest, run the selected models on every instance, and write a
long-format results.csv (one row per instance x model) next to the manifest.

Resume: if results.csv already exists, previously-completed (file, model) pairs
are skipped, so a long run can be interrupted and restarted safely.
"""

import os
import csv
import glob
import time

from ..utils    import load_testcase
from .adapters  import run_model

# NB: the model's feasibility is `model_feasible`, NOT `feasible` — the manifest
# already has an instance-level `feasible` column and merging would clobber it.
_METRIC_COLS = ["model", "status", "model_feasible", "utility", "energy",
                "util_per_energy", "runtime", "gap", "error"]


def find_manifests(path):
    """Accept a manifest.csv, a sweep dir, or a tree of sweeps."""
    if path.endswith(".csv"):
        return [path]
    if os.path.isdir(path):
        return sorted(glob.glob(os.path.join(path, "**", "manifest.csv"),
                                recursive=True))
    raise FileNotFoundError(path)


def _resolve(manifest_path, file_field):
    base = os.path.dirname(os.path.dirname(os.path.abspath(manifest_path)))
    return os.path.join(base, file_field.replace("\\", os.sep).replace("/", os.sep))


def _load_done(results_path):
    done = set()
    if os.path.exists(results_path):
        with open(results_path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                done.add((row.get("file"), row.get("model")))
    return done


def run_manifest(manifest_path, models=("ilp_v2", "heuristic"), time_limit=30,
                 heur_variant="v5b", mip_gap=0.0, resume=True, verbose=True,
                 progress_every=25):
    """Run `models` over every instance in one manifest; append to results.csv."""
    with open(manifest_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        man_cols = list(rows[0].keys()) if rows else []

    results_path = os.path.join(os.path.dirname(manifest_path), "results.csv")
    done = _load_done(results_path) if resume else set()
    cols = man_cols + [c for c in _METRIC_COLS if c not in man_cols]

    # Guard: appending under a header with different/reordered columns would
    # silently misalign every new row (DictWriter writes in `cols` order).
    new_file = not os.path.exists(results_path)
    if not new_file:
        with open(results_path, newline="", encoding="utf-8") as f:
            existing = next(csv.reader(f), [])
        if existing and existing != cols:
            raise SystemExit(
                f"results.csv schema mismatch at {results_path}\n"
                f"  on disk : {existing}\n"
                f"  expected: {cols}\n"
                f"Delete the file (or pass --no-resume after removing it) to rebuild.")

    fout = open(results_path, "a", newline="", encoding="utf-8")
    w = csv.DictWriter(fout, fieldnames=cols, extrasaction="ignore")
    if new_file:
        w.writeheader()

    todo = [(r, m) for r in rows for m in models
            if (r["file"], _model_key(m, heur_variant)) not in done]
    if verbose:
        print(f"[{os.path.relpath(manifest_path)}] {len(rows)} instances x "
              f"{len(models)} models  ->  {len(todo)} runs to do "
              f"({len(rows)*len(models)-len(todo)} already done)")

    t_start = time.perf_counter()
    n = 0
    for (row, model) in todo:
        tc_path = _resolve(manifest_path, row["file"])
        try:
            processors, tasks, B = load_testcase(tc_path)
            metrics = run_model(model, processors, tasks, B,
                                time_limit=time_limit, heur_variant=heur_variant,
                                mip_gap=mip_gap)
        except Exception as e:
            metrics = dict(model=model, status="error", model_feasible=0, utility="",
                           energy="", util_per_energy="", runtime="", gap="",
                           error=repr(e)[:200])
        w.writerow({**row, **metrics})
        fout.flush()
        n += 1
        if verbose and n % progress_every == 0:
            rate = n / (time.perf_counter() - t_start)
            print(f"    {n}/{len(todo)}  ({rate:.1f} runs/s)")

    fout.close()
    if verbose:
        dt = time.perf_counter() - t_start
        print(f"    done: {n} runs in {dt:.1f}s  ->  {os.path.relpath(results_path)}")
    return results_path


def _model_key(model, heur_variant):
    """Match the 'model' string the adapter will stamp (for resume de-dup)."""
    if model == "heuristic":
        return f"heuristic_{heur_variant}"
    return model


def run_all(path, models=("ilp_v2", "heuristic"), **kw):
    """Run every manifest under `path`."""
    mans = find_manifests(path)
    print(f"found {len(mans)} manifest(s) under {path}")
    for m in mans:
        run_manifest(m, models=models, **kw)
