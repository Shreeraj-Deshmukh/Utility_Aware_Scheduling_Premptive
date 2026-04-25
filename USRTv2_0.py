"""
ilp_usrt.py
===========
Gurobi ILP for the USRT problem.
Faithful to the paper:
  "Utility-aware Energy Constrained Real-Time Scheduling"
  Section II (System Model) and Section III (ILP Formulation).

NO pre-partitioning step.  The task-to-processor mapping is a
decision variable V(ix) optimised jointly with everything else.

Assumptions
-----------
A1. Variables follow the paper exactly:
      V(ix)    : binary, 1 iff task Ti is mapped to processor Px  [Eq.3]
      X(ijkz)  : binary, 1 iff job Ti,j runs at fz up to k opt segs  [Eq.4]
      A(ijkzx) : auxiliary binary = V(ix) AND X(ijkz)  [Eq.5a-5c]

A2. Energy model is paper Eq.(2):
      E = α·e_eff + β·fz²·e_nom
    where e_eff = e_nom/fz,  e_nom = e_i + sum_{q=1}^{k} e^O_{i,q}
    All energy coefficients are pre-computed constants.

A3. Timing feasibility uses the DBF condition for preemptive EDF,
    paper Eq.(6)-(7):
      dbf(t1,t2,Px) <= t2 - t1
    for all t1 in set of release times, t2 in set of deadlines,
    t1 < t2, per processor Px.

    A job Ti,j belongs to interval [t1,t2] iff:
      r_ij >= t1  AND  d_ij <= t2
    i.e. its full [release, deadline] window fits inside [t1,t2].
    This is the standard DBF membership condition for
    preemptive EDF with implicit deadlines.

A4. Homogeneous processors: all share the same frequency set F.

A5. No migration: C1 enforces one processor per task.
    A(ijkzx) propagates this to every job via the linearisation.

A6. Schedule horizon = one hyper-period H = lcm{p_i}.

A7. k=0 is always a valid choice (mandatory only, zero utility).
    k ranges over 0 .. N_seg_i.

A8. Utility is linear per paper:
      U_ij(k) = u_i * sum_{q=1}^{k} e^O_{i,q}
    same weight for all jobs of a task.

A9. Paper index convention: j-th job of Ti released at
      r_ij = (j-1)*p_i,  deadline d_ij = j*p_i,  j in [1..Nj].
    In code we use 0-based j, so:
      r_ij = j*p_i,  d_ij = (j+1)*p_i,  j in [0..Nj-1].
"""

import math
import sys
import gurobipy as gp
from gurobipy import GRB
from testcase import testcase

ALPHA = 1.0
BETA  = 1.0


# ══════════════════════════════════════════════════════════════════════════════
#  Helpers
# ══════════════════════════════════════════════════════════════════════════════

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b) if a and b else 0

def hyperperiod(tasks):
    h = 1
    for t in tasks:
        h = lcm(h, t['p_i'])
    return h

def e_nom(task, k):
    """Nominal exec time (at f_max=1) for mandatory + first k optional segs."""
    return task['e_m'] + sum(task['e_o_k'][:k])

def e_eff(task, k, f):
    """Effective (actual wall-clock) exec time — paper Eq.(1)."""
    return e_nom(task, k) / f

def energy(task, k, f):
    """Energy — paper Eq.(2):  E = α·e_eff + β·f²·e_nom."""
    nom  = e_nom(task, k)
    eff  = nom / f
    return ALPHA * eff + BETA * (f ** 2) * nom

def utility(task, k):
    """Utility for k optional segments — paper Eq.(10): u_i * sum(e_o[:k])."""
    if k == 0:
        return 0.0
    return task['u_i'] * sum(task['e_o_k'][:k])


# ══════════════════════════════════════════════════════════════════════════════
#  ILP
# ══════════════════════════════════════════════════════════════════════════════

def solve_usrt():
    processors, tasks, B = testcase()

    H  = hyperperiod(tasks)
    F  = processors[0]['frequencies']     # homogeneous (A4)
    Nf = len(F)
    Np = len(processors)
    Nt = len(tasks)

    # Number of jobs per task in H
    for t in tasks:
        t['Nj'] = H // t['p_i']

    print("=" * 60)
    print("  USRT ILP  (paper Section III, no pre-partitioning)")
    print("=" * 60)
    print(f"  Tasks        : {Nt}")
    print(f"  Processors   : {Np}")
    print(f"  Frequencies  : {F}")
    print(f"  Hyper-period : {H}")
    print(f"  Budget B     : {B}")

    # ── DBF check-point sets ──────────────────────────────────────────────────
    # t1: all release times {r_ij = j*p_i} in [0, H)
    # t2: all deadline times {d_ij = (j+1)*p_i} in (0, H]
    # paper: t1 in {r_i,j}, t2 in {r_i,j} — but since deadlines = next
    # release we use deadlines for t2 (standard DBF practice).
    t1_set = sorted(set(
        j * t['p_i']
        for t in tasks for j in range(t['Nj'])
    ))
    t2_set = sorted(set(
        (j + 1) * t['p_i']
        for t in tasks for j in range(t['Nj'])
    ))

    # ── Model ─────────────────────────────────────────────────────────────────
    m = gp.Model("USRT")
    m.Params.OutputFlag = 1
    m.Params.TimeLimit  = 3600

    # ── V(ix): task-to-processor mapping  [paper Eq.3] ───────────────────────
    V = m.addVars(Nt, Np, vtype=GRB.BINARY, name="V")

    # ── X(ijkz): job execution choice  [paper Eq.4] ──────────────────────────
    X = {}
    for i, t in enumerate(tasks):
        Nk = len(t['e_o_k'])
        for j in range(t['Nj']):
            for k in range(Nk + 1):
                for z in range(Nf):
                    X[i, j, k, z] = m.addVar(
                        vtype=GRB.BINARY,
                        name=f"X_{i}_{j}_{k}_{z}"
                    )

    # ── A(ijkzx): auxiliary linearisation of V*X  [paper Eq.5a-5c] ──────────
    A = {}
    for i, t in enumerate(tasks):
        Nk = len(t['e_o_k'])
        for j in range(t['Nj']):
            for k in range(Nk + 1):
                for z in range(Nf):
                    for x in range(Np):
                        A[i, j, k, z, x] = m.addVar(
                            vtype=GRB.BINARY,
                            name=f"A_{i}_{j}_{k}_{z}_{x}"
                        )

    m.update()

    # ── Objective: maximise total utility  [paper Eq.10-12] ───────────────────
    obj = gp.LinExpr()
    for i, t in enumerate(tasks):
        Nk = len(t['e_o_k'])
        for j in range(t['Nj']):
            for k in range(1, Nk + 1):      # k=0 → zero utility
                u_val = utility(t, k)
                for z in range(Nf):
                    obj += u_val * X[i, j, k, z]
    m.setObjective(obj, GRB.MAXIMIZE)

    # ── C1: each task mapped to exactly one processor  [paper Eq.3] ───────────
    for i in range(Nt):
        m.addConstr(
            gp.quicksum(V[i, x] for x in range(Np)) == 1,
            name=f"C1_T{i}"
        )

    # ── C2: each job has exactly one (k,z) choice  [paper Eq.4] ───────────────
    for i, t in enumerate(tasks):
        Nk = len(t['e_o_k'])
        for j in range(t['Nj']):
            m.addConstr(
                gp.quicksum(
                    X[i, j, k, z]
                    for k in range(Nk + 1)
                    for z in range(Nf)
                ) == 1,
                name=f"C2_T{i}_J{j}"
            )

    # ── C3 linearisation: A = V AND X  [paper Eq.5a-5c] ──────────────────────
    for i, t in enumerate(tasks):
        Nk = len(t['e_o_k'])
        for j in range(t['Nj']):
            for k in range(Nk + 1):
                for z in range(Nf):
                    for x in range(Np):
                        a = A[i, j, k, z, x]
                        m.addConstr(a <= V[i, x])
                        m.addConstr(a <= X[i, j, k, z])
                        m.addConstr(a >= V[i, x] + X[i, j, k, z] - 1)

    # ── C3 DBF: timing feasibility per processor  [paper Eq.6-7] ─────────────
    # For each Px, each interval [t1,t2]:
    #   sum_{Ti,j in S(t1,t2)} sum_{k,z} A(ijkzx) * e_eff(i,k,z) <= t2-t1
    # S(t1,t2): jobs with r_ij >= t1 AND d_ij <= t2
    for x in range(Np):
        for t1 in t1_set:
            for t2 in t2_set:
                if t2 <= t1:
                    continue
                terms = []
                for i, t in enumerate(tasks):
                    Nk = len(t['e_o_k'])
                    p  = t['p_i']
                    for j in range(t['Nj']):
                        r_ij = j * p
                        d_ij = (j + 1) * p
                        # job belongs to S(t1,t2) iff r_ij>=t1 and d_ij<=t2
                        if r_ij >= t1 and d_ij <= t2:
                            for k in range(Nk + 1):
                                for z, f in enumerate(F):
                                    eff = e_eff(t, k, f)
                                    terms.append(eff * A[i, j, k, z, x])
                if terms:
                    m.addConstr(
                        gp.quicksum(terms) <= t2 - t1,
                        name=f"C3_P{x}_{t1}_{t2}"
                    )

    # ── C4: total energy <= B  [paper Eq.8-9] ─────────────────────────────────
    E_total = gp.LinExpr()
    for i, t in enumerate(tasks):
        Nk = len(t['e_o_k'])
        for j in range(t['Nj']):
            for k in range(Nk + 1):
                for z, f in enumerate(F):
                    E_total += energy(t, k, f) * X[i, j, k, z]
    m.addConstr(E_total <= B, name="C4_energy")

    # ── Solve ─────────────────────────────────────────────────────────────────
    print(f"\n  Variables   : {m.NumVars}")
    print(f"  Constraints : {m.NumConstrs}")
    print(f"\nSolving ...\n")
    m.optimize()

    # ── Output ────────────────────────────────────────────────────────────────
    if m.status not in (GRB.OPTIMAL, GRB.TIME_LIMIT) or m.SolCount == 0:
        if m.status == GRB.INFEASIBLE:
            print("INFEASIBLE. Computing IIS ...")
            m.computeIIS()
            m.write("infeasible.ilp")
            print("IIS written to 'infeasible.ilp'")
        else:
            print(f"No solution found. Status: {m.status}")
        return

    total_util   = m.objVal
    total_energy = E_total.getValue()

    # Collect all jobs from the solution into one flat list
    all_jobs = []
    for i, t in enumerate(tasks):
        # which processor did this task get mapped to
        proc = next(x for x in range(Np) if V[i, x].X > 0.5)
        Nk   = len(t['e_o_k'])
        for j in range(t['Nj']):
            for k in range(Nk + 1):
                for z, f in enumerate(F):
                    if X[i, j, k, z].X > 0.5:
                        all_jobs.append({
                            'label':    f"T{i}.J{j}",
                            'task_id':  i,
                            'proc':     proc,
                            'k':        k,
                            'max_k':    Nk,
                            'f':        f,
                            'exec_t':   e_eff(t, k, f),
                            'energy':   energy(t, k, f),
                            'utility':  utility(t, k),
                            'release':  j * t['p_i'],
                            'deadline': (j + 1) * t['p_i'],
                        })

    # Sort combined schedule by deadline then release (EDF order)
    all_jobs.sort(key=lambda r: (r['deadline'], r['release']))

    W   = 95
    HDR = (f"  {'Job':<12} {'Proc':<6} {'k':<4} {'f':<6} "
           f"{'ExecTime':<10} {'Energy':<12} {'Utility':<10} "
           f"{'Release':<9} {'Deadline':<9}\n")
    SEP = "  " + "-" * (len(HDR) - 3) + "\n"

    def write_block(out):
        out("=" * W + "\n")
        out("  USRT ILP SOLUTION  (paper Section III)\n")
        if m.status == GRB.TIME_LIMIT:
            out(f"  TIME LIMIT – best incumbent  |  "
                f"MIP gap = {100.0 * m.MIPGap:.2f}%\n")
        out("=" * W + "\n\n")
        out(f"  Total Utility    : {total_util:.4f}\n")
        out(f"  Total Energy     : {total_energy:.4f} / {B}  "
            f"({100.0 * total_energy / B:.1f}% used)\n")
        out(f"  Hyper-period     : {H}\n")
        out(f"  Total jobs       : {len(all_jobs)}\n")
        out(f"  Processors used  : {Np}\n")
        out("\n")

        out(HDR)
        out(SEP)
        for r in all_jobs:
            out(
                f"  {r['label']:<12}"
                f"P{r['proc']:<5}"
                f"{r['k']}/{r['max_k']:<3} "
                f"{r['f']:<6.2f}"
                f"{r['exec_t']:<10.4f}"
                f"{r['energy']:<12.4f}"
                f"{r['utility']:<10.4f}"
                f"{r['release']:<9} "
                f"{r['deadline']:<9}\n"
            )

        out(f"\n{'='*W}\n")

        # Per-task summary
        out(f"\n  Per-task summary\n")
        out(f"  {'Task':<8} {'Proc':<6} {'Jobs':<6} "
            f"{'k range':<12} {'f range':<12} "
            f"{'Energy':<12} {'Utility':<10}\n")
        out("  " + "-" * 68 + "\n")
        for i, t in enumerate(tasks):
            jobs_i = [r for r in all_jobs if r['task_id'] == i]
            k_vals = [r['k'] for r in jobs_i]
            f_vals = [r['f'] for r in jobs_i]
            t_e    = sum(r['energy']  for r in jobs_i)
            t_u    = sum(r['utility'] for r in jobs_i)
            proc   = jobs_i[0]['proc'] if jobs_i else '-'
            out(
                f"  T{i:<7} P{proc:<5} {len(jobs_i):<6} "
                f"[{min(k_vals)},{max(k_vals)}]/{jobs_i[0]['max_k']:<7} "
                f"[{min(f_vals):.2f},{max(f_vals):.2f}]   "
                f"{t_e:<12.4f} {t_u:.4f}\n"
            )
        out(f"\n{'='*W}\n")

    print()
    write_block(sys.stdout.write)
    with open("output_ilp.txt", "w", encoding="utf-8") as fh:
        write_block(fh.write)
    print(f"\nFull output saved to 'output_ilp.txt'")


if __name__ == "__main__":
    solve_usrt()