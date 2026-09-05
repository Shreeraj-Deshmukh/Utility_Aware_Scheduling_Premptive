"""
ILP v3 Solver - Predicted-work SPS mapping (Phase 1) + Gurobi ILP (Phase 2).

Phase 2 is byte-for-byte ILP v2: same Y(i,j,k,z) variables, same C1/C2/C3, same
objective.  ONLY the mapping changes.

Why the mapping changes
-----------------------
ILP v2's Phase 1 packs jobs by MANDATORY work.  Phase 2 then spends the budget
on OPTIONAL work.  So the packer balances a quantity the final schedule does
not carry: a processor handed several high-utility tasks saturates its DBF
windows and the ILP cannot buy their optional segments, however much budget is
left.  That mismatch is what Phase 1b/1b'/1c/1M/1R all patch downstream in the
heuristics.  ILP v3 fixes it in the packer instead:

    f_hat  = fastest frequency whose mandatory cost fits B
    S      = B - E(W_mand, f_hat)                        (energy surplus)
    k_hat  = greedily raise segments by descending u_i/g(f_hat) while S allows
    weight = cum[i][k_hat_i] / h                         (predicted TOTAL work)

DPS/SPS criss-cross is untouched - only the item sizes change.  u_i/g(f) is
Phase 6b's lambda; with a common f_hat it reduces to descending u_i, Phase 5's
key.  No tuned constants: everything derives from B and the energy model.

Safety: the mapping is DBF-verified (mandatory-only, at f_hat).  On failure the
surplus is scaled back 1.0 -> 0.5 -> 0.25, and finally the plain ILP v2 mapping
is used - so ILP v3 can never be less feasible than ILP v2.
"""

from collections import defaultdict

import gurobipy as gp
from gurobipy import GRB

from ..models  import ALPHA, BETA
from ..utils   import lcm_list, gcd_list, build_cum, generate_jobs, build_job_times, build_proc_jobs
from ..mapping.quantum import quantum_sps_mapping
from ..mapping.predictive import predict_segment_levels, predicted_weights
from ..dbf.check import check_all_timing
from ..output  import print_instance_summary, print_mapping_summary


_S  = "=" * 76
_S2 = "-" * 76


def _e_eff(cum, i, k, z, freq_set):
    return cum[i][k] / freq_set[z]


def _energy(cum, i, k, z, freq_set):
    c = cum[i][k]; f = freq_set[z]
    return ALPHA * (c / f) + BETA * (f ** 2) * c


def solve_ilp_v3(processors, tasks, B_BUDGET):
    """
    Full ILP v2 solver.
    Phase 1 : quantum_sps_mapping
    Phase 2 : Gurobi ILP

    Returns the Gurobi model (solved).
    """
    N_tsk    = len(tasks)
    N_prc    = len(processors)
    freq_set = processors[0]['frequencies']
    N_frq    = len(freq_set)
    periods  = [int(t['p_i']) for t in tasks]
    h        = lcm_list(periods)
    quantum  = gcd_list(periods)
    cum, N_seg = build_cum(tasks)
    N_job    = [h // periods[i] for i in range(N_tsk)]
    job_r, job_d = build_job_times(tasks, h)

    # ── Instance summary ──────────────────────────────────────────────────────
    print_instance_summary(processors, tasks, B_BUDGET, h, quantum, N_job, N_seg,
                           ALPHA, BETA, label="USRT ILP v3  —  Instance")

    # -- Phase 1: Predicted-work Quantum SPS mapping -------------------------
    print(f"\n{_S}")
    print(f"  PHASE 1 : QUANTUM SPS MAPPING  (predicted-work item sizes)")
    print(_S2)

    def _dbf_ok(mp, z_hat):
        pj, _ = build_proc_jobs(mp)
        sk = {(i, j): 0 for i in range(N_tsk) for j in range(N_job[i])}
        fz = {(i, j): z_hat for i in range(N_tsk) for j in range(N_job[i])}
        return check_all_timing(pj, job_r, job_d, sk, fz, freq_set, cum, N_prc)

    mapping, chosen = None, None
    for scale in (1.0, 0.5, 0.25):
        k_hat, f_hat, spent = predict_segment_levels(
            tasks, N_tsk, N_job, cum, N_seg, freq_set, B_BUDGET,
            surplus_scale=scale)
        z_hat = min(range(N_frq), key=lambda z: abs(freq_set[z] - f_hat))
        if all(k == 0 for k in k_hat):
            break                       # no surplus to spend -> plain SPS below
        w  = predicted_weights(tasks, N_tsk, N_job, cum, k_hat, h)
        mp = quantum_sps_mapping(tasks, processors, h, quantum, verbose=False,
                                 job_weight=w)
        if _dbf_ok(mp, z_hat):
            mapping = mp
            chosen  = (scale, k_hat, f_hat, spent)
            break
        print(f"  surplus x{scale}: DBF infeasible at f_hat={f_hat:.2f}, backing off")

    if mapping is None:
        print(f"  falling back to the plain ILP v2 mapping (mandatory-work sizes)")
        mapping = quantum_sps_mapping(tasks, processors, h, quantum, verbose=True)
    else:
        scale, k_hat, f_hat, spent = chosen
        print(f"  f_hat={f_hat:.3f}  surplus x{scale}  spent={spent:.3f}")
        print(f"  predicted k_hat={k_hat}")

    proc_jobs, _ = build_proc_jobs(mapping)
    print_mapping_summary(mapping, tasks, processors, h, job_r, job_d)

    # ── Phase 2: ILP v2 ──────────────────────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 2 : ILP v2  (frequency + segment optimisation)")
    print(_S2)

    mdl = gp.Model("USRT_ILP_v3")
    mdl.setParam("OutputFlag", 1)

    Y_keys = [
        (i, j, k, z)
        for i in range(N_tsk)
        for j in range(N_job[i])
        for k in range(N_seg[i] + 1)
        for z in range(N_frq)
    ]
    Y = mdl.addVars(Y_keys, vtype=GRB.BINARY, name="Y")

    # C1: each job exactly one (k, z)
    for i in range(N_tsk):
        for j in range(N_job[i]):
            mdl.addConstr(
                gp.quicksum(Y[i, j, k, z]
                            for k in range(N_seg[i] + 1)
                            for z in range(N_frq)) == 1,
                name=f"C1_{i}_{j}"
            )

    # C2: DBF per processor
    n_dbf = 0
    for x in range(N_prc):
        jobs_x = proc_jobs[x]
        if not jobs_x:
            continue
        Ax = sorted({job_r[ij] for ij in jobs_x})
        Dx = sorted({job_d[ij] for ij in jobs_x})
        for t1 in Ax:
            for t2 in Dx:
                if t1 >= t2:
                    continue
                window = [(i, j) for (i, j) in jobs_x
                          if job_r[(i, j)] >= t1 and job_d[(i, j)] <= t2]
                if not window:
                    continue
                mdl.addConstr(
                    gp.quicksum(
                        Y[i, j, k, z] * _e_eff(cum, i, k, z, freq_set)
                        for (i, j) in window
                        for k in range(N_seg[i] + 1)
                        for z in range(N_frq)
                    ) <= t2 - t1,
                    name=f"C2_x{x}_{int(t1)}_{int(t2)}"
                )
                n_dbf += 1

    # C3: energy budget
    mdl.addConstr(
        gp.quicksum(
            Y[i, j, k, z] * _energy(cum, i, k, z, freq_set)
            for i in range(N_tsk)
            for j in range(N_job[i])
            for k in range(N_seg[i] + 1)
            for z in range(N_frq)
        ) <= B_BUDGET,
        name="C3_energy"
    )

    # Objective
    mdl.setObjective(
        gp.quicksum(
            tasks[i]['u_i'] * (cum[i][k] - cum[i][0]) * Y[i, j, k, z]
            for i in range(N_tsk)
            for j in range(N_job[i])
            for k in range(1, N_seg[i] + 1)
            for z in range(N_frq)
        ),
        GRB.MAXIMIZE
    )

    print(f"\n  Y variables  : {len(Y_keys)}")
    print(f"  Constraints  : C1={sum(N_job)}   DBF={n_dbf}   Energy=1\n")

    mdl.optimize()

    _print_ilp_solution(mdl, Y, tasks, N_tsk, N_job, N_seg, freq_set, N_frq,
                        cum, B_BUDGET, mapping, job_r, job_d)
    return mdl


def run(processors, tasks, B_BUDGET):
    return solve_ilp_v3(processors, tasks, B_BUDGET)


def _print_ilp_solution(mdl, Y, tasks, N_tsk, N_job, N_seg,
                         freq_set, N_frq, cum, B_BUDGET, mapping, job_r, job_d):
    smap = {
        GRB.OPTIMAL:     "OPTIMAL",
        GRB.INFEASIBLE:  "INFEASIBLE",
        GRB.INF_OR_UNBD: "INF_OR_UNBOUNDED",
        GRB.TIME_LIMIT:  "TIME_LIMIT (best shown)",
    }
    print(f"\n{_S}")
    print(f"  SOLVER STATUS : {smap.get(mdl.status, str(mdl.status))}")

    if mdl.SolCount == 0:
        if mdl.status == GRB.INFEASIBLE:
            print("  Computing IIS …")
            mdl.computeIIS()
            mdl.write("infeasible_v3.ilp")
            print("  IIS → infeasible_v3.ilp")
        print(_S); return

    print(f"  Objective (total utility) : {mdl.ObjVal:.6f}")
    print(_S)

    total_e = total_u = 0.0
    for i in range(N_tsk):
        u_i   = tasks[i]['u_i']
        procs = sorted({mapping.get((i, j), -1) for j in range(N_job[i])})
        print(f"\n  Task T{tasks[i]['id']}  period={tasks[i]['p_i']}  "
              f"u_i={u_i}  N_seg={N_seg[i]}  N_jobs={N_job[i]}  proc(s)={procs}")
        print(f"  {'Job':>5}  {'Proc':>5}  {'Freq':>6}  {'k':>4}  "
              f"{'cum_work':>9}  {'e_eff':>8}  {'Energy':>10}  {'Utility':>9}")
        print(f"  {_S2}")
        t_e = t_u = 0.0
        for j in range(N_job[i]):
            px = mapping.get((i, j), -1)
            for k in range(N_seg[i] + 1):
                for z in range(N_frq):
                    if Y[i, j, k, z].X > 0.5:
                        ef  = _e_eff(cum, i, k, z, freq_set)
                        en  = _energy(cum, i, k, z, freq_set)
                        opt = cum[i][k] - cum[i][0]
                        ut  = u_i * opt
                        t_e += en; t_u += ut
                        print(f"  {j+1:>5}  P{px:<4}  {freq_set[z]:>6.3f}  {k:>4}  "
                              f"{cum[i][k]:>9.4f}  {ef:>8.4f}  {en:>10.4f}  {ut:>9.4f}")
        total_e += t_e; total_u += t_u
        print(f"\n  Task T{tasks[i]['id']} totals : energy={t_e:.4f}   utility={t_u:.4f}")

    print(f"\n{_S}")
    print(f"  Total energy  : {total_e:.4f}  (budget={B_BUDGET}  slack={B_BUDGET-total_e:.4f})")
    print(f"  Total utility : {total_u:.6f}")
    print(_S)
