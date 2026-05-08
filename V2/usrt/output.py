"""
Output / pretty-printing utilities.
"""

from .models import e_eff_val, energy_val, total_energy, total_utility

_S  = "=" * 76
_S2 = "-" * 76


def print_instance_summary(processors, tasks, B_BUDGET, h, quantum, N_job, N_seg,
                            alpha, beta, label="USRT Instance"):
    print(f"\n{_S}")
    print(f"  {label}")
    print(_S2)
    print(f"  Processors   : {len(processors)}")
    print(f"  Frequencies  : {processors[0]['frequencies']}")
    print(f"  Energy budget: {B_BUDGET}    α={alpha}   β={beta}")
    print(f"  Hyper-period : {h}    Quantum(GCD): {quantum}")
    print(_S2)
    total_util = sum(t['e_m'] / t['p_i'] for t in tasks)
    print(f"  {'TID':>4}  {'period':>7}  {'Nseg':>5}  {'Njobs':>6}  "
          f"{'e_m':>9}  {'util':>7}  {'u_i':>6}  e_o_k")
    print(f"  {_S2}")
    for i, t in enumerate(tasks):
        u = t['e_m'] / t['p_i']
        print(f"  {t['id']:>4}  {t['p_i']:>7}  {N_seg[i]:>5}  {N_job[i]:>6}  "
              f"{t['e_m']:>9.4f}  {u:>7.4f}  {t['u_i']:>6}  "
              f"{[round(x, 4) for x in t['e_o_k']]}")
    feas = "FEASIBLE" if total_util <= len(processors) else "OVERLOADED"
    print(f"\n  Total utilisation: {total_util:.4f}/{len(processors)}  [{feas}]")
    print(_S)


def print_mapping_summary(mapping, tasks, processors, h, job_r, job_d):
    m      = len(processors)
    N_tsk  = len(tasks)
    print(f"\n{_S}")
    print(f"  SPS MAPPING SUMMARY")
    print(_S2)
    for x in range(m):
        jobs_x = sorted((i, j) for (i, j), px in mapping.items() if px == x)
        ul_tot = sum(tasks[i]['e_m'] / tasks[i]['p_i'] for (i, j) in jobs_x)
        flag   = '  ← OVERLOADED' if ul_tot > 1.0 else ''
        print(f"\n  Processor P{x}  |  {len(jobs_x)} jobs  util={ul_tot:.4f}{flag}")
        print(f"  {'Task':>5}  {'job':>4}  {'arrival':>8}  {'deadline':>9}  {'e_m':>9}  {'util':>7}")
        print(f"  {'─'*50}")
        for (i, j) in jobs_x:
            u = tasks[i]['e_m'] / tasks[i]['p_i']
            print(f"  T{tasks[i]['id']:>4}  {j:>4}  "
                  f"{job_r[(i,j)]:>8}  {job_d[(i,j)]:>9}  "
                  f"{tasks[i]['e_m']:>9.4f}  {u:>7.4f}")
    print(_S)


def print_schedule(seg_k, freq_idx, freq_set, cum, tasks, N_tsk, N_job,
                   mapping, B_BUDGET, label=""):
    """Standard heuristic schedule printout (no left-shift columns)."""
    print(f"\n{_S}")
    print(f"  SCHEDULE{' — ' + label if label else ''}")
    print(_S2)
    tot_e = tot_u = 0.0
    for i in range(N_tsk):
        u_i   = tasks[i]['u_i']
        procs = sorted({mapping.get((i, j), -1) for j in range(N_job[i])})
        print(f"\n  Task T{tasks[i]['id']}  period={tasks[i]['p_i']}"
              f"  u_i={u_i}  N_seg={len(tasks[i]['e_o_k'])}"
              f"  N_jobs={N_job[i]}  procs={procs}")
        print(f"  {'job':>4}  {'proc':>5}  {'freq':>6}  {'k':>3}  "
              f"{'cum_work':>9}  {'e_eff':>8}  {'energy':>9}  {'utility':>8}")
        print(f"  {'─'*65}")
        t_e = t_u = 0.0
        for j in range(N_job[i]):
            k  = seg_k[(i, j)]; z = freq_idx[(i, j)]
            fz = freq_set[z];   cw = cum[i][k]
            ee = e_eff_val(cw, fz)
            en = energy_val(cw, fz)
            ut = u_i * (cw - cum[i][0])
            t_e += en; t_u += ut
            px = mapping.get((i, j), -1)
            print(f"  {j+1:>4}  P{px:<4}  {fz:>6.3f}  {k:>3}  "
                  f"{cw:>9.4f}  {ee:>8.4f}  {en:>9.4f}  {ut:>8.4f}")
        tot_e += t_e; tot_u += t_u
        print(f"  Task totals : energy={t_e:.4f}  utility={t_u:.4f}")
    print(f"\n{_S}")
    print(f"  Total energy  : {tot_e:.4f}  "
          f"(budget={B_BUDGET}  slack={B_BUDGET - tot_e:.4f})")
    print(f"  Total utility : {tot_u:.6f}")
    print(_S)
    return tot_e, tot_u


def print_schedule_with_ls(seg_k, freq_idx, freq_set, cum, tasks, N_tsk, N_job,
                            mapping, ls_slack, B_BUDGET, label=""):
    """Schedule printout including left-shift slack column."""
    print(f"\n{_S}")
    print(f"  SCHEDULE{' — ' + label if label else ''}")
    print(_S2)
    tot_e = tot_u = 0.0
    for i in range(N_tsk):
        u_i = tasks[i]['u_i']
        print(f"\n  Task T{tasks[i]['id']}  u_i={u_i}  period={tasks[i]['p_i']}"
              f"  N_seg={len(tasks[i]['e_o_k'])}")
        print(f"  {'job':>4}  {'proc':>5}  {'freq':>6}  {'k':>3}  "
              f"{'cum_work':>9}  {'e_eff':>8}  {'energy':>9}  "
              f"{'utility':>8}  {'ls_slack':>9}")
        print(f"  {'─'*72}")
        t_e = t_u = 0.0
        for j in range(N_job[i]):
            k  = seg_k[(i, j)]; z = freq_idx[(i, j)]
            fz = freq_set[z];   cw = cum[i][k]
            ee = e_eff_val(cw, fz)
            en = energy_val(cw, fz)
            ut = u_i * (cw - cum[i][0])
            sl = ls_slack.get((i, j), float('nan'))
            t_e += en; t_u += ut
            px = mapping.get((i, j), -1)
            print(f"  {j+1:>4}  P{px:<4}  {fz:>6.3f}  {k:>3}  "
                  f"{cw:>9.4f}  {ee:>8.4f}  {en:>9.4f}  "
                  f"{ut:>8.4f}  {sl:>9.3f}")
        tot_e += t_e; tot_u += t_u
        print(f"  Task totals : energy={t_e:.4f}  utility={t_u:.4f}")
    print(f"\n{_S}")
    print(f"  Total energy  : {tot_e:.4f}  "
          f"(budget={B_BUDGET}  slack={B_BUDGET - tot_e:.4f})")
    print(f"  Total utility : {tot_u:.6f}")
    print(_S)
    return tot_e, tot_u
