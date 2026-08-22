"""
Model adapters — normalise each solver to one metrics schema, quietly and safely.

Each adapter returns:
    {model, status, model_feasible, utility, energy, util_per_energy, runtime,
     gap, error}
  status         : optimal | solved | time_limit | timeout | infeasible | error
  model_feasible : 1 if THIS MODEL produced a valid schedule, else 0.
                   Deliberately NOT named `feasible`: the generator's manifest
                   already carries an instance-level `feasible` column (does the
                   mandatory part pack at all), and merging the two dicts would
                   silently overwrite it, destroying the generator's flag.
  utility  : total optional utility (model-consistent; ILP ObjVal == models util)
  energy   : total energy of the chosen schedule, recomputed via usrt.models so
             every model is measured on the SAME energy model
  runtime  : wall-clock seconds
  gap      : MIP optimality gap (ILP only)

Design choices that keep this non-invasive (no edits to the solver files):
  * Gurobi's per-model verbose log + the solvers' own print()s are silenced at
    the file-descriptor level (captures the C-level Gurobi log too).
  * Gurobi's computeIIS()/write() (called by both ILPs on infeasible instances)
    are monkeypatched to no-ops — they are slow and spew .ilp files, and we only
    need the infeasible verdict (SolCount == 0).
  * ILP v1's module-global ALPHA/BETA are re-pointed to usrt.models so it solves
    the project's energy model, not the stale 1.0/0.5 baked into ILP.py.
    (Recommend making that fix permanent in ILP.py.)
"""

import os
import re
import sys
import time
import importlib
import contextlib

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))          # ...\V2
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from usrt.models      import ALPHA, BETA, energy_val, total_energy, total_utility
from usrt.utils       import (lcm_list, gcd_list, build_cum, build_job_times,
                              build_proc_jobs)
from usrt.mapping.quantum import quantum_sps_mapping
from usrt.dbf.check   import check_all_timing

MODELS = ("ilp_v1", "ilp_v2", "heuristic", "greedy_sps_baseline")

_YRE = re.compile(r"^Y\[(\d+),(\d+),(\d+),(\d+)\]$")


class _Null:
    """A sink that never encodes — immune to cp1252 console crashes."""
    def write(self, *a):  return 0
    def flush(self):      pass


# ── output suppression ───────────────────────────────────────────────────────
# Two layers, because the solvers emit output two ways on Windows:
#   * fd level (os.dup2 -> devnull) swallows Gurobi's C log.
#   * sys.stdout/stderr -> _Null swallows the solvers' Python print()s AND makes
#     them encoding-proof (box-drawing / >= glyphs would otherwise raise
#     UnicodeEncodeError on a cp1252 console, mislabelling the run as "error").
@contextlib.contextmanager
def _suppress():
    try:
        sys.stdout.flush(); sys.stderr.flush()
    except Exception:
        pass
    devnull = os.open(os.devnull, os.O_WRONLY)
    old1, old2 = os.dup(1), os.dup(2)
    old_out, old_err = sys.stdout, sys.stderr
    try:
        os.dup2(devnull, 1); os.dup2(devnull, 2)
        sys.stdout = _Null(); sys.stderr = _Null()
        yield
    finally:
        sys.stdout = old_out; sys.stderr = old_err
        os.dup2(old1, 1); os.dup2(old2, 2)
        os.close(devnull); os.close(old1); os.close(old2)


_gurobi_patched = False


def _prep_gurobi(time_limit, mip_gap=0.0):
    """Silence IIS/file-writes and set global TimeLimit/MIPGap/OutputFlag.

    TimeLimit is the ILP timeout exit: Gurobi self-terminates the solve after
    `time_limit`s and returns the best incumbent (status TIME_LIMIT) — or no
    solution, handled distinctly in _ilp_metrics.  It bounds optimize(), which
    for the ILP-tractable tier (small H, few tasks) is the whole cost; model
    building there is milliseconds.  mip_gap>0 lets v1 stop early at a proven
    relative gap (faster, still a bounded-quality optimum)."""
    global _gurobi_patched
    import gurobipy as gp
    if not _gurobi_patched:
        gp.Model.computeIIS = lambda self, *a, **k: None
        gp.Model.write      = lambda self, *a, **k: None
        _gurobi_patched = True
    gp.setParam("OutputFlag", 0)
    if time_limit:
        gp.setParam("TimeLimit", float(time_limit))
    if mip_gap:
        gp.setParam("MIPGap", float(mip_gap))


_STATUS = {2: "optimal", 3: "infeasible", 4: "infeasible", 5: "unbounded",
           9: "time_limit"}


def _ilp_metrics(mdl, cum, freq_set, model_name, runtime):
    """Extract the normalised metrics from a solved Gurobi model."""
    status = _STATUS.get(mdl.status, f"code_{mdl.status}")
    if mdl.SolCount == 0:
        # No incumbent: distinguish a genuine INFEASIBLE from a TIME_LIMIT hit
        # before any solution was found (feasibility unknown -> NOT infeasible,
        # or the success-rate metric would be corrupted).
        if mdl.status == 9:            # GRB.TIME_LIMIT, no incumbent
            st, feas = "timeout", ""
        elif mdl.status in (3, 4):     # GRB.INFEASIBLE / INF_OR_UNBD
            st, feas = "infeasible", 0
        else:
            st, feas = status, ""
        return dict(model=model_name, status=st, model_feasible=feas,
                    utility="", energy="", util_per_energy="",
                    runtime=round(runtime, 4), gap="", error="")
    utility = mdl.ObjVal
    energy = 0.0
    for v in mdl.getVars():
        if v.X > 0.5:
            m = _YRE.match(v.VarName)
            if m:
                i, j, k, z = map(int, m.groups())
                energy += energy_val(cum[i][k], freq_set[z])
    try:
        gap = round(mdl.MIPGap, 6)
    except Exception:
        gap = ""
    upe = utility / energy if energy > 1e-12 else ""
    return dict(model=model_name, status=status, model_feasible=1,
                utility=round(utility, 6), energy=round(energy, 6),
                util_per_energy=(round(upe, 6) if upe != "" else ""),
                runtime=round(runtime, 4), gap=gap, error="")


def _cum_freq(processors, tasks):
    cum, _ = build_cum(tasks)
    return cum, processors[0]['frequencies']


# ── ILP v1 ────────────────────────────────────────────────────────────────
def run_ilp_v1(processors, tasks, B, time_limit=30, mip_gap=0.0):
    import ILP                                   # root-level ILP.py
    ILP.ALPHA, ILP.BETA = ALPHA, BETA            # align energy model to models.py
    _prep_gurobi(time_limit, mip_gap)
    cum, freq_set = _cum_freq(processors, tasks)
    t0 = time.perf_counter()
    with _suppress():
        mdl = ILP.solve(processors, tasks, B)
    return _ilp_metrics(mdl, cum, freq_set, "ilp_v1", time.perf_counter() - t0)


# ── ILP v2 ────────────────────────────────────────────────────────────────
def run_ilp_v2(processors, tasks, B, time_limit=30, mip_gap=0.0):
    from usrt.solvers import ilp_v2
    _prep_gurobi(time_limit, mip_gap)
    cum, freq_set = _cum_freq(processors, tasks)
    t0 = time.perf_counter()
    with _suppress():
        mdl = ilp_v2.solve_ilp_v2(processors, tasks, B)
    return _ilp_metrics(mdl, cum, freq_set, "ilp_v2", time.perf_counter() - t0)


# ── Heuristic ───────────────────────────────────────────────────────────────
def _mandatory_feasible(processors, tasks):
    """Does the heuristic's SPS mapping yield a DBF-feasible mandatory schedule?"""
    N_tsk = len(tasks)
    periods = [int(t['p_i']) for t in tasks]
    h = lcm_list(periods); quantum = gcd_list(periods)
    cum, _ = build_cum(tasks)
    N_job = [h // periods[i] for i in range(N_tsk)]
    job_r, job_d = build_job_times(tasks, h)
    freq_set = processors[0]['frequencies']
    with _suppress():
        mapping = quantum_sps_mapping(tasks, processors, h, quantum, verbose=False)
    proc_jobs, _ = build_proc_jobs(mapping)
    seg_k    = {(i, j): 0 for i in range(N_tsk) for j in range(N_job[i])}
    freq_idx = {(i, j): len(freq_set) - 1 for i in range(N_tsk) for j in range(N_job[i])}
    return check_all_timing(proc_jobs, job_r, job_d, seg_k, freq_idx,
                            freq_set, cum, len(processors))


def run_baseline(processors, tasks, B, time_limit=None):
    """greedy_SPS_Baseline: SPS mapping, f_max fixed, greedy segments."""
    if not _mandatory_feasible(processors, tasks):
        return dict(model="greedy_sps_baseline", status="infeasible",
                    model_feasible=0, utility="", energy="", util_per_energy="",
                    runtime=0.0, gap="", error="")
    from usrt.solvers import greedy_sps_baseline as _gsb
    t0 = time.perf_counter()
    with _suppress():
        seg_k, freq_idx, tot_u, tot_e = _gsb.run(processors, tasks, B)
    rt = time.perf_counter() - t0
    if tot_e > B + 1e-6:
        return dict(model="greedy_sps_baseline", status="infeasible",
                    model_feasible=0, utility="", energy=round(tot_e, 6),
                    util_per_energy="", runtime=round(rt, 4), gap="",
                    error=f"over budget: E={tot_e:.4f} > B={B:.4f}")
    upe = tot_u / tot_e if tot_e > 1e-12 else ""
    return dict(model="greedy_sps_baseline", status="solved", model_feasible=1,
                utility=round(tot_u, 6), energy=round(tot_e, 6),
                util_per_energy=(round(upe, 6) if upe != "" else ""),
                runtime=round(rt, 4), gap="", error="")


def run_heuristic(processors, tasks, B, variant="v5b", time_limit=None):
    feasible = _mandatory_feasible(processors, tasks)
    if not feasible:
        return dict(model=f"heuristic_{variant}", status="infeasible", model_feasible=0,
                    utility="", energy="", util_per_energy="", runtime=0.0,
                    gap="", error="")
    mod = importlib.import_module(f"usrt.solvers.heuristic_{variant}")
    t0 = time.perf_counter()
    with _suppress():
        seg_k, freq_idx, tot_u, tot_e = mod.run(processors, tasks, B)
    rt = time.perf_counter() - t0

    # VALIDATE the returned schedule against the energy budget.  The heuristics
    # bail out early when the mandatory part alone busts the budget, returning
    # (utility 0, energy = mandatory-at-f_max) — which is NOT a feasible
    # schedule.  Without this check the runner would score that as a success and
    # corrupt both the success-rate and the utility curves.
    if tot_e > B + 1e-6:
        return dict(model=f"heuristic_{variant}", status="infeasible",
                    model_feasible=0, utility="", energy=round(tot_e, 6),
                    util_per_energy="", runtime=round(rt, 4), gap="",
                    error=f"over budget: E={tot_e:.4f} > B={B:.4f}")

    upe = tot_u / tot_e if tot_e > 1e-12 else ""
    return dict(model=f"heuristic_{variant}", status="solved", model_feasible=1,
                utility=round(tot_u, 6), energy=round(tot_e, 6),
                util_per_energy=(round(upe, 6) if upe != "" else ""),
                runtime=round(rt, 4), gap="", error="")


def run_model(name, processors, tasks, B, time_limit=30, heur_variant="v5b",
              mip_gap=0.0):
    """Dispatch to the right adapter; never raise — errors become a status row."""
    try:
        if name == "ilp_v1":
            return run_ilp_v1(processors, tasks, B, time_limit, mip_gap)
        if name == "ilp_v2":
            return run_ilp_v2(processors, tasks, B, time_limit, mip_gap)
        if name == "greedy_sps_baseline":
            return run_baseline(processors, tasks, B)
        if name in ("heuristic", "heuristic_v6", "heuristic_v5b", "heuristic_v5a", "heuristic_v4",
                    "heuristic_v3", "heuristic_claudeoptimal"):
            variant = heur_variant if name == "heuristic" else name.split("_", 1)[1]
            return run_heuristic(processors, tasks, B, variant=variant)
        raise ValueError(f"unknown model {name}")
    except Exception as e:                        # keep the sweep going
        return dict(model=name, status="error", model_feasible=0, utility="", energy="",
                    util_per_energy="", runtime="", gap="", error=repr(e)[:200])
