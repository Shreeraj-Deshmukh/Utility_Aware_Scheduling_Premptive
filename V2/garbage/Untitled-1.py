"""
USRT ILP v1 — Utility-aware Energy-Constrained Real-Time Scheduling
====================================================================
Formulation  : ILP v1 (joint job-to-processor, frequency, segment mapping)
Mapping level: Job-level  (each job of a task may land on a different processor)
Environment  : Preemptive, EDF
Periods      : Harmonic
Reference    : Segmented_Workload_Scheduling_Shared_v2.pdf — Section III

Decision variable
-----------------
V(i, j, k, x, z) ∈ {0,1}
    = 1  iff  job T_{i,j}  executes on processor P_x
              with frequency  f_z
              up to (and including) the k-th segment

Auxiliary variable
------------------
Y(i, j, k, z) = Σ_x  V(i, j, k, x, z)
    (1 iff job T_{i,j} is executed up to k-th segment at frequency f_z,
     regardless of processor)

Energy model  (Eq. 1–2 in v2 paper)
--------------------------------------
  e_eff(i, k, z)   = (1 / f_z)  ·  Σ_{q=0}^{k}  e_{i,q}
  E(i, k, z)       = α · e_eff(i, k, z)  +  β · f_z²  ·  Σ_{q=0}^{k}  e_{i,q}

Testcase JSON format (testcase.json)
--------------------------------------
{
  "tasks": [
    {
      "period"     : <int>,          // p_i  (must form harmonic set)
      "exec_times" : [e_i0, e_i1, ...],  // e_{i,0}=mandatory at f_max,
                                          // e_{i,k} k≥1 = k-th optional seg at f_max
      "utility"    : <float>         // u_i  (utility per unit optional execution)
    },
    ...
  ],
  "processors"    : <int>,           // N_prc
  "frequencies"   : [f1, f2, ..., 1.0],  // ascending; last entry MUST be 1.0 (f_max)
  "energy_budget" : <float>,         // B
  "alpha"         : <float>,         // static power coefficient
  "beta"          : <float>          // dynamic power coefficient
}
"""

import json
import sys
from math import gcd

import gurobipy as gp
from gurobipy import GRB


# ── helpers ───────────────────────────────────────────────────────────────────

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def compute_hyperperiod(periods: list[int]) -> int:
    h = periods[0]
    for p in periods[1:]:
        h = lcm(h, p)
    return h


# ── model ─────────────────────────────────────────────────────────────────────

def solve_usrt_ilp_v1(instance: dict) -> gp.Model:
    """
    Build and solve USRT ILP v1.

    Parameters
    ----------
    instance : dict  (see module docstring for JSON schema)

    Returns
    -------
    gurobipy.Model  (solved)
    """

    # ── unpack instance ──────────────────────────────────────────────────────
    tasks  = instance["tasks"]
    N_prc  = instance["processors"]
    F      = instance["frequencies"]   # ascending, F[-1] == 1.0
    B      = instance["energy_budget"]
    alpha  = instance["alpha"]
    beta   = instance["beta"]

    N_tsk  = len(tasks)
    N_frq  = len(F)

    # ── hyper-period ─────────────────────────────────────────────────────────
    periods = [int(t["period"]) for t in tasks]
    h       = compute_hyperperiod(periods)

    # number of jobs of task i in the hyper-period
    N_job = [h // periods[i] for i in range(N_tsk)]

    # number of optional segments per task
    N_seg = [len(tasks[i]["exec_times"]) - 1 for i in range(N_tsk)]

    # cumulative exec time up to segment k at f_max
    # cum[i][k] = Σ_{q=0}^{k}  e_{i,q}
    cum: list[list[float]] = []
    for i in range(N_tsk):
        row, s = [], 0.0
        for e in tasks[i]["exec_times"]:
            s += e
            row.append(s)
        cum.append(row)

    # ── derived quantities ───────────────────────────────────────────────────
    def e_eff(i: int, k: int, z: int) -> float:
        """Effective execution time for task i, up to seg k, at freq F[z]."""
        return cum[i][k] / F[z]

    def energy(i: int, k: int, z: int) -> float:
        """Energy consumed by one job of task i executing up to seg k at F[z]."""
        c = cum[i][k]
        return alpha * (c / F[z]) + beta * (F[z] ** 2) * c

    # ── job timing ───────────────────────────────────────────────────────────
    # 0-indexed j: job j of task i arrives at j·p_i, deadline (j+1)·p_i
    job_rd: dict[tuple[int, int], tuple[float, float]] = {}
    A_set: set[float] = set()
    D_set: set[float] = set()

    for i in range(N_tsk):
        for j in range(N_job[i]):
            r = j * periods[i]
            d = (j + 1) * periods[i]
            job_rd[(i, j)] = (r, d)
            A_set.add(r)
            D_set.add(d)

    A_list = sorted(A_set)
    D_list = sorted(D_set)

    def demand_window(t1: float, t2: float) -> list[tuple[int, int]]:
        """Jobs fully within [t1, t2]: r_{i,j} ≥ t1  and  d_{i,j} ≤ t2."""
        return [(i, j) for (i, j), (r, d) in job_rd.items()
                if r >= t1 and d <= t2]

    # ── Gurobi model ─────────────────────────────────────────────────────────
    mdl = gp.Model("USRT_ILP_v1")
    mdl.setParam("OutputFlag", 1)

    # V(i, j, k, x, z)
    V_keys = [
        (i, j, k, x, z)
        for i in range(N_tsk)
        for j in range(N_job[i])
        for k in range(N_seg[i] + 1)
        for x in range(N_prc)
        for z in range(N_frq)
    ]
    V = mdl.addVars(V_keys, vtype=GRB.BINARY, name="V")

    # Y(i, j, k, z)  auxiliary — equals Σ_x V(i,j,k,x,z)
    Y_keys = [
        (i, j, k, z)
        for i in range(N_tsk)
        for j in range(N_job[i])
        for k in range(N_seg[i] + 1)
        for z in range(N_frq)
    ]
    Y = mdl.addVars(Y_keys, vtype=GRB.BINARY, name="Y")

    # ── linking constraints: Y = Σ_x V ───────────────────────────────────────
    for i in range(N_tsk):
        for j in range(N_job[i]):
            for k in range(N_seg[i] + 1):
                for z in range(N_frq):
                    mdl.addConstr(
                        Y[i, j, k, z]
                        == gp.quicksum(V[i, j, k, x, z] for x in range(N_prc)),
                        name=f"link_Y_{i}_{j}_{k}_{z}",
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

    # ── [C2] DBF timing constraints (per processor, per [t1,t2] window) ──────
    for t1 in A_list:
        for t2 in D_list:
            if t1 >= t2:
                continue
            window = demand_window(t1, t2)
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
                    name=f"C2_t{int(t1)}_t{int(t2)}_x{x}",
                )

    # ── [C3] Energy budget ────────────────────────────────────────────────────
    mdl.addConstr(
        gp.quicksum(
            Y[i, j, k, z] * energy(i, k, z)
            for i in range(N_tsk)
            for j in range(N_job[i])
            for k in range(N_seg[i] + 1)
            for z in range(N_frq)
        ) <= B,
        name="C3_energy",
    )

    # ── Objective: maximise total utility ────────────────────────────────────
    # U^job_{i,j} = u_i · Σ_{k=1}^{N_seg_i} Σ_z  Y(i,j,k,z) · (cum[i][k] - cum[i][0])
    # (k=0 → only mandatory → no optional execution → zero utility contribution)
    mdl.setObjective(
        gp.quicksum(
            tasks[i]["utility"] * (cum[i][k] - cum[i][0]) * Y[i, j, k, z]
            for i in range(N_tsk)
            for j in range(N_job[i])
            for k in range(1, N_seg[i] + 1)   # k ≥ 1 for utility
            for z in range(N_frq)
        ),
        GRB.MAXIMIZE,
    )

    mdl.optimize()

    # ── print results ─────────────────────────────────────────────────────────
    _print_solution(
        mdl, V, Y, tasks, N_tsk, N_job, N_seg,
        N_prc, F, N_frq, cum, h, energy, e_eff,
    )
    return mdl


# ── output ────────────────────────────────────────────────────────────────────

def _print_solution(
    mdl, V, Y, tasks, N_tsk, N_job, N_seg,
    N_prc, F, N_frq, cum, h, energy, e_eff,
):
    SEP  = "=" * 72
    SEP2 = "-" * 72

    if mdl.status == GRB.OPTIMAL:
        print(f"\n{SEP}")
        print(f"  STATUS            : OPTIMAL")
        print(f"  Objective (Utility): {mdl.ObjVal:.6f}")
        print(f"  Hyper-period       : {h}")
        print(SEP)

        total_energy  = 0.0
        total_utility = 0.0

        for i in range(N_tsk):
            u_i = tasks[i]["utility"]
            print(f"\nTask T{i+1}  |  period={tasks[i]['period']}  "
                  f"u_i={u_i}  N_seg={N_seg[i]}  N_jobs={N_job[i]}")
            hdr = (f"  {'Job':>5}  {'Proc':>5}  {'Freq':>6}  {'k':>4}  "
                   f"{'Σe(0..k)':>9}  {'e_eff':>8}  {'Energy':>10}  {'Utility':>9}")
            print(hdr)
            print(f"  {SEP2}")

            task_energy  = 0.0
            task_utility = 0.0

            for j in range(N_job[i]):
                for k in range(N_seg[i] + 1):
                    for x in range(N_prc):
                        for z in range(N_frq):
                            if V[i, j, k, x, z].X > 0.5:
                                ef  = e_eff(i, k, z)
                                en  = energy(i, k, z)
                                opt = cum[i][k] - cum[i][0]   # optional exec portion
                                ut  = u_i * opt
                                task_energy  += en
                                task_utility += ut
                                print(
                                    f"  {j+1:>5}  {'P'+str(x+1):>5}  "
                                    f"{F[z]:>6.3f}  {k:>4}  "
                                    f"{cum[i][k]:>9.4f}  {ef:>8.4f}  "
                                    f"{en:>10.4f}  {ut:>9.4f}"
                                )

            total_energy  += task_energy
            total_utility += task_utility
            print(f"  {'':5}  Task totals →  energy={task_energy:.4f}   utility={task_utility:.4f}")

        print(f"\n{SEP}")
        print(f"  Total Energy Used   : {total_energy:.6f}")
        print(f"  Total Utility       : {total_utility:.6f}   (= objective)")
        print(SEP)

    elif mdl.status == GRB.INFEASIBLE:
        print("\n[!] Model is INFEASIBLE.")
        print("    Computing IIS and writing to  infeasible_usrt.ilp  …")
        mdl.computeIIS()
        mdl.write("infeasible_usrt.ilp")

    elif mdl.status == GRB.INF_OR_UNBD:
        print("\n[!] Model is INFEASIBLE or UNBOUNDED.")

    else:
        print(f"\n[!] Gurobi status code: {mdl.status}")


# ── entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    testcase_file = sys.argv[1] if len(sys.argv) > 1 else "testcase.json"

    print(f"Loading testcase: {testcase_file}")
    with open(testcase_file) as f:
        instance = json.load(f)

    # Print a quick summary of the instance
    print(f"\n{'─'*50}")
    print(f"  Tasks        : {len(instance['tasks'])}")
    for idx, t in enumerate(instance["tasks"]):
        print(f"    T{idx+1}: period={t['period']}  exec_times={t['exec_times']}  u={t['utility']}")
    print(f"  Processors   : {instance['processors']}")
    print(f"  Frequencies  : {instance['frequencies']}")
    print(f"  Energy budget: {instance['energy_budget']}")
    print(f"  α={instance['alpha']}   β={instance['beta']}")
    print(f"{'─'*50}\n")

    solve_usrt_ilp_v1(instance)