"""
USRT ILP v1 — Utility-aware Energy-Constrained Real-Time Scheduling
=====================================================================
Formulation  : ILP v1  (joint job → processor + frequency + segment mapping)
Mapping level: Job-level
Environment  : Preemptive EDF, harmonic periods
Reference    : Segmented_Workload_Scheduling_Shared_v2.pdf — Section III

Testcase format  (testcaase.py)
--------------------------------
  processors : list of dicts  { 'id': int, 'frequencies': [f1..fmax] }
  tasks      : list of dicts  { 'id', 'p_i', 'e_m', 'e_o_k': [...], 'u_i' }
                  e_m     — mandatory exec time at f_max
                  e_o_k   — list of optional segment exec times at f_max
                             (cumulative: executing seg k implies segs 0..k-1 too)
  B_BUDGET   : float  — total energy budget

Notation mapping  (paper → code)
---------------------------------
  T_{i,j}             task i, job j   (j is 0-indexed)
  k = 0               mandatory only
  k in [1, N_seg_i]   up to k-th optional segment executed
  e_{i,0} = e_m       mandatory exec at f_max
  e_{i,k} = e_o_k[k-1]  k-th optional seg exec at f_max
  cum[i][k]           sum_{q=0}^{k} e_{i,q}  (total work up to seg k at f_max)

Energy model  (Eq. 1-2, v2 paper)
-----------------------------------
  e_eff(i,k,z) = cum[i][k] / f_z
  E(i,k,z)     = alpha * e_eff(i,k,z)  +  beta * f_z^2 * cum[i][k]

Decision variable
-----------------
  V[i,j,k,x,z] in {0,1}
      1  iff  job T_{i,j} runs on processor x at frequency f_z up to segment k

Auxiliary variable
------------------
  Y[i,j,k,z] = sum_x V[i,j,k,x,z]
      (1 iff job T_{i,j} runs at freq f_z up to seg k, any processor)
"""

import sys
import importlib.util
from math import gcd

import gurobipy as gp
from gurobipy import GRB

# ── energy model coefficients ─────────────────────────────────────────────────
# Imported from the single source of truth (usrt/models.py) so this solver can
# never drift from the rest of the project.  These were previously hard-coded to
# ALPHA=1.0, BETA=0.5 -- the stale pair -- which silently solved a DIFFERENT
# energy model whenever this file was run standalone: under 1.0/0.5 the energy
# optimum is f_max, whereas under the project's 0.15/1.0 it is f* ~= 0.42, so the
# two disagree about the entire DVFS trade-off.
from usrt.models import ALPHA, BETA


# ─────────────────────────── helpers ─────────────────────────────────────────

def lcm2(a: int, b: int) -> int:
    return a * b // gcd(a, b)

def hyperperiod(periods: list) -> int:
    h = periods[0]
    for p in periods[1:]:
        h = lcm2(h, p)
    return h

def load_testcase(path: str):
    """Import testcase() from an arbitrary .py file path."""
    spec   = importlib.util.spec_from_file_location("testcaase", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.testcase()


# ─────────────────────────── core solver ─────────────────────────────────────

def solve(processors, tasks, B_BUDGET):
    """
    Build and solve USRT ILP v1.

    Parameters
    ----------
    processors : list of dicts  { 'id': int, 'frequencies': list[float] }
    tasks      : list of dicts  { 'id', 'p_i', 'e_m', 'e_o_k', 'u_i' }
    B_BUDGET   : float
    """

    N_tsk = len(tasks)
    N_prc = len(processors)

    # All processors share the same frequency list (homogeneous assumption)
    freq_set = processors[0]["frequencies"]   # ascending, last = f_max
    N_frq    = len(freq_set)

    # ── cumulative exec-time table ────────────────────────────────────────────
    # cum[i][k] = e_m + sum of first k optional segments   (at f_max)
    # k=0 -> mandatory only ; k=s -> mandatory + s optional segments
    cum   = []
    N_seg = []
    for t in tasks:
        execs = [t["e_m"]] + list(t["e_o_k"])
        row, s = [], 0.0
        for e in execs:
            s += e
            row.append(s)
        cum.append(row)
        N_seg.append(len(t["e_o_k"]))

    # ── hyper-period & job counts ─────────────────────────────────────────────
    periods = [int(t["p_i"]) for t in tasks]
    h       = hyperperiod(periods)
    N_job   = [h // periods[i] for i in range(N_tsk)]

    # ── job timing ────────────────────────────────────────────────────────────
    job_r = {}
    job_d = {}
    A_set: set = set()
    D_set: set = set()
    for i in range(N_tsk):
        for j in range(N_job[i]):
            r = j * periods[i]
            d = (j + 1) * periods[i]
            job_r[(i, j)] = r
            job_d[(i, j)] = d
            A_set.add(r)
            D_set.add(d)
    A_list = sorted(A_set)
    D_list = sorted(D_set)

    def jobs_in_window(t1, t2):
        """Jobs fully contained in [t1, t2]: r >= t1 and d <= t2."""
        return [(i, j) for (i, j) in job_r
                if job_r[(i, j)] >= t1 and job_d[(i, j)] <= t2]

    # ── energy helpers ────────────────────────────────────────────────────────
    def e_eff(i, k, z):
        return cum[i][k] / freq_set[z]

    def E(i, k, z):
        c = cum[i][k]
        f = freq_set[z]
        return ALPHA * (c / f) + BETA * (f ** 2) * c

    # ── instance summary ──────────────────────────────────────────────────────
    _print_instance(tasks, processors, freq_set, B_BUDGET, h, N_job, N_seg)

    # ── Gurobi model ──────────────────────────────────────────────────────────
    mdl = gp.Model("USRT_ILP_v1")
    mdl.setParam("OutputFlag", 1)

    # V[i, j, k, x, z]
    V_keys = [
        (i, j, k, x, z)
        for i in range(N_tsk)
        for j in range(N_job[i])
        for k in range(N_seg[i] + 1)
        for x in range(N_prc)
        for z in range(N_frq)
    ]
    V = mdl.addVars(V_keys, vtype=GRB.BINARY, name="V")

    # Y[i, j, k, z] = sum_x V[i,j,k,x,z]
    Y_keys = [
        (i, j, k, z)
        for i in range(N_tsk)
        for j in range(N_job[i])
        for k in range(N_seg[i] + 1)
        for z in range(N_frq)
    ]
    Y = mdl.addVars(Y_keys, vtype=GRB.BINARY, name="Y")

    # ── linking: Y = sum_x V ─────────────────────────────────────────────────
    for i in range(N_tsk):
        for j in range(N_job[i]):
            for k in range(N_seg[i] + 1):
                for z in range(N_frq):
                    mdl.addConstr(
                        Y[i, j, k, z]
                        == gp.quicksum(V[i, j, k, x, z] for x in range(N_prc)),
                        name=f"link_{i}_{j}_{k}_{z}",
                    )

    # ── [C1] Each job assigned to exactly one (k, x, z) ──────────────────────
    for i in range(N_tsk):
        for j in range(N_job[i]):
            mdl.addConstr(
                gp.quicksum(
                    V[i, j, k, x, z]
                    for k in range(N_seg[i] + 1)
                    for x in range(N_prc)
                    for z in range(N_frq)
                ) == 1,
                name=f"C1_{i}_{j}",
            )

    # ── [C2] DBF timing per processor per (t1, t2) window ────────────────────
    n_dbf = 0
    for t1 in A_list:
        for t2 in D_list:
            if t1 >= t2:
                continue
            window = jobs_in_window(t1, t2)
            if not window:
                continue
            for x in range(N_prc):
                mdl.addConstr(
                    gp.quicksum(
                        V[i, j, k, x, z] * e_eff(i, k, z)
                        for (i, j) in window
                        for k in range(N_seg[i] + 1)
                        for z in range(N_frq)
                    ) <= t2 - t1,
                    name=f"C2_{int(t1)}_{int(t2)}_x{x}",
                )
                n_dbf += 1

    # ── [C3] Energy budget ────────────────────────────────────────────────────
    mdl.addConstr(
        gp.quicksum(
            Y[i, j, k, z] * E(i, k, z)
            for i in range(N_tsk)
            for j in range(N_job[i])
            for k in range(N_seg[i] + 1)
            for z in range(N_frq)
        ) <= B_BUDGET,
        name="C3_energy",
    )

    # ── Objective: maximise total utility ─────────────────────────────────────
    # Utility for job T_{i,j} at (k>=1, z):
    #   u_i * (cum[i][k] - cum[i][0])   (cum[i][0] = e_m = mandatory portion)
    mdl.setObjective(
        gp.quicksum(
            tasks[i]["u_i"] * (cum[i][k] - cum[i][0]) * Y[i, j, k, z]
            for i in range(N_tsk)
            for j in range(N_job[i])
            for k in range(1, N_seg[i] + 1)
            for z in range(N_frq)
        ),
        GRB.MAXIMIZE,
    )

    print(f"  Variables   : {len(V_keys) + len(Y_keys)}"
          f"  (V={len(V_keys)}  Y={len(Y_keys)})")
    print(f"  Constraints : C1={N_tsk * sum(N_job)}  "
          f"DBF={n_dbf}  Energy=1  Linking={len(Y_keys)}\n")

    mdl.optimize()

    _print_solution(
        mdl, V, Y, tasks, N_tsk, N_job, N_seg,
        N_prc, freq_set, N_frq, cum, E, e_eff, B_BUDGET,
    )
    return mdl


# ─────────────────────────── output helpers ───────────────────────────────────

_SEP  = "=" * 76
_SEP2 = "-" * 76


def _print_instance(tasks, processors, freq_set, B, h, N_job, N_seg):
    print(f"\n{_SEP}")
    print(f"  USRT ILP v1  —  Instance Summary")
    print(_SEP2)
    print(f"  Processors   : {len(processors)}")
    print(f"  Frequencies  : {freq_set}")
    print(f"  Energy budget: {B}    alpha={ALPHA}   beta={BETA}")
    print(f"  Hyper-period : {h}")
    print(_SEP2)
    hdr = (f"  {'TID':>4}  {'period':>7}  {'N_seg':>6}  {'N_jobs':>7}  "
           f"{'e_m':>9}  {'u_i':>5}  e_o_k")
    print(hdr)
    print(f"  {_SEP2}")
    for i, t in enumerate(tasks):
        print(f"  {t['id']:>4}  {t['p_i']:>7}  {N_seg[i]:>6}  {N_job[i]:>7}  "
              f"{t['e_m']:>9.4f}  {t['u_i']:>5.2f}  "
              f"{[round(x, 4) for x in t['e_o_k']]}")
    print(_SEP)
    print()


def _print_solution(mdl, V, Y, tasks, N_tsk, N_job, N_seg,
                    N_prc, freq_set, N_frq, cum, E, e_eff, B_BUDGET):

    status_map = {
        GRB.OPTIMAL    : "OPTIMAL",
        GRB.INFEASIBLE : "INFEASIBLE",
        GRB.INF_OR_UNBD: "INF_OR_UNBOUNDED",
        GRB.UNBOUNDED  : "UNBOUNDED",
        GRB.TIME_LIMIT : "TIME_LIMIT (best incumbent shown)",
    }
    status_str = status_map.get(mdl.status, f"GUROBI_CODE_{mdl.status}")

    print(f"\n{_SEP}")
    print(f"  SOLVER STATUS          : {status_str}")

    if mdl.SolCount == 0:
        print(f"  No feasible solution found.")
        if mdl.status == GRB.INFEASIBLE:
            print("  Computing IIS …")
            mdl.computeIIS()
            mdl.write("infeasible_usrt.ilp")
            print("  IIS written to  infeasible_usrt.ilp")
        print(_SEP)
        return

    print(f"  Objective (total utility): {mdl.ObjVal:.6f}")
    print(_SEP)

    total_energy  = 0.0
    total_utility = 0.0

    for i in range(N_tsk):
        u_i = tasks[i]["u_i"]
        print(f"\n  ── Task T{tasks[i]['id']}  "
              f"(period={tasks[i]['p_i']}, u_i={u_i}, "
              f"N_seg={N_seg[i]}, N_jobs={N_job[i]}) ──")
        print(f"  {'Job':>5}  {'Proc':>5}  {'Freq':>6}  {'k':>4}  "
              f"{'cum_work':>9}  {'e_eff':>8}  {'Energy':>10}  "
              f"{'Utility':>9}  Execution")
        print(f"  {_SEP2}")

        task_energy  = 0.0
        task_utility = 0.0

        for j in range(N_job[i]):
            assigned = False
            for k in range(N_seg[i] + 1):
                for x in range(N_prc):
                    for z in range(N_frq):
                        if V[i, j, k, x, z].X > 0.5:
                            assigned   = True
                            ef         = e_eff(i, k, z)
                            en         = E(i, k, z)
                            opt_work   = cum[i][k] - cum[i][0]
                            ut         = u_i * opt_work
                            task_energy  += en
                            task_utility += ut

                            if k == 0:
                                seg_desc = "mandatory only"
                            else:
                                seg_desc = f"mandatory + {k} opt seg(s)"

                            print(f"  {j+1:>5}  "
                                  f"{'P'+str(x):>5}  "
                                  f"{freq_set[z]:>6.3f}  "
                                  f"{k:>4}  "
                                  f"{cum[i][k]:>9.4f}  "
                                  f"{ef:>8.4f}  "
                                  f"{en:>10.4f}  "
                                  f"{ut:>9.4f}  "
                                  f"{seg_desc}")
            if not assigned:
                print(f"  {j+1:>5}  [WARNING: no assignment found]")

        total_energy  += task_energy
        total_utility += task_utility
        print(f"\n  {'':5} Task T{tasks[i]['id']} totals:"
              f"  energy = {task_energy:.4f}   utility = {task_utility:.4f}")

    print(f"\n{_SEP}")
    print(f"  Total energy used : {total_energy:.4f}"
          f"  /  budget {B_BUDGET}"
          f"  (slack = {B_BUDGET - total_energy:.4f})")
    print(f"  Total utility     : {total_utility:.6f}")
    print(_SEP)


# ─────────────────────────── entry point ──────────────────────────────────────

if __name__ == "__main__":
    tc_path = sys.argv[1] if len(sys.argv) > 1 else "testcase.py"
    print(f"Loading testcase from: {tc_path}")
    processors, tasks, B_BUDGET = load_testcase(tc_path)
    solve(processors, tasks, B_BUDGET)