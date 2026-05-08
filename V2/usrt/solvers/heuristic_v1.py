"""
Heuristic v1 — ScheduleState-based pipeline.

Mapping  : single-pass SPS (flat, no per-quantum processing)
Phase 2  : aggressive_freq_scaling_state (incremental DBF)
Phase 3  : greedy_optional_segments (ScheduleState atomic moves)

State management uses the ScheduleState class, which maintains incremental
DBF slack structures and checks timing via in-memory slack dictionaries
rather than recomputing DBF from scratch.
"""

from collections import defaultdict

from ..models   import ALPHA, BETA
from ..utils    import load_testcase, lcm_list, gcd_list, build_cum, build_job_times
from ..state    import ScheduleState
from ..mapping.single_pass import single_pass_sps_mapping
from ..output   import print_instance_summary
from ..phases.aggressive import aggressive_freq_scaling_state
from ..phases.greedy_state import greedy_optional_segments

_S  = "=" * 76
_S2 = "-" * 76


def run(processors, tasks, B_BUDGET):
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

    print_instance_summary(processors, tasks, B_BUDGET, h, quantum, N_job, N_seg,
                           ALPHA, BETA, label="USRT Heuristic v1  —  Instance")

    # ── Phase 1: Single-pass SPS mapping ─────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 1 : SINGLE-PASS SPS MAPPING")
    print(_S2)
    mapping = single_pass_sps_mapping(tasks, N_job, N_tsk, N_prc)

    proc_jobs = defaultdict(list)
    for (i, j), x in mapping.items():
        proc_jobs[x].append((i, j))

    for x in range(N_prc):
        util = sum(tasks[i]['e_m'] / tasks[i]['p_i'] for (i, j) in proc_jobs[x])
        print(f"  P{x}: {len(proc_jobs[x]):>4} jobs   utilisation={util:.4f}")

    # ── Build ScheduleState ───────────────────────────────────────────────────
    state = ScheduleState(
        tasks, processors, cum, N_seg, N_job,
        periods, freq_set, job_r, job_d, mapping, B_BUDGET
    )
    E_init = B_BUDGET - state.slack_energy
    print(f"\n  Initial energy (mandatory, f_max): {E_init:.4f}  "
          f"slack={state.slack_energy:.4f}")

    if state.slack_energy < -1e-9:
        print(f"  [!] Mandatory cost exceeds budget — infeasible.")
        _print_state_solution(state, tasks, N_tsk, N_job, N_seg, N_prc,
                               freq_set, cum, B_BUDGET)
        return state

    # ── Phase 2: Aggressive frequency scaling ─────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 2 : AGGRESSIVE FREQUENCY SCALING")
    print(_S2)
    scaled = aggressive_freq_scaling_state(state)
    print(f"  {scaled} frequency reductions applied.")
    print(f"  Energy slack after scaling: {state.slack_energy:.4f}")

    # ── Phase 3: Greedy optional segment addition ─────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 3 : GREEDY OPTIONAL SEGMENT ADDITION")
    print(_S2)
    total_added = greedy_optional_segments(state)
    print(f"  Total optional segments added: {total_added}")

    # ── Solution output ───────────────────────────────────────────────────────
    _print_state_solution(state, tasks, N_tsk, N_job, N_seg, N_prc,
                           freq_set, cum, B_BUDGET)
    return state


def _print_state_solution(state, tasks, N_tsk, N_job, N_seg, N_prc,
                           freq_set, cum, B_BUDGET):
    print(f"\n{_S}")
    print(f"  HEURISTIC v1 SOLUTION")
    print(_S2)
    total_e = total_u = 0.0
    for i in range(N_tsk):
        u_i = tasks[i]['u_i']
        print(f"\n  Task T{tasks[i]['id']}  period={tasks[i]['p_i']}  "
              f"u_i={u_i}  N_seg={N_seg[i]}  N_jobs={N_job[i]}")
        print(f"  {'Job':>5}  {'Proc':>5}  {'Freq':>6}  {'k':>4}  "
              f"{'cum_work':>9}  {'e_eff':>8}  {'Energy':>10}  {'Utility':>9}")
        print(f"  {_S2}")
        t_e = t_u = 0.0
        for j in range(N_job[i]):
            x  = state.sps_map[(i, j)]
            z  = state.freq_idx[(i, j)]
            k  = state.seg_k[(i, j)]
            fz = freq_set[z]; ck = cum[i][k]
            ef = ck / fz
            from ..models import energy_val
            en = energy_val(ck, fz)
            ut = u_i * (ck - cum[i][0])
            t_e += en; t_u += ut
            print(f"  {j+1:>5}  P{x:<4}  {fz:>6.3f}  {k:>4}  "
                  f"{ck:>9.4f}  {ef:>8.4f}  {en:>10.4f}  {ut:>9.4f}")
        total_e += t_e; total_u += t_u
        print(f"  Task totals : energy={t_e:.4f}  utility={t_u:.4f}")
    feasible = all(
        state.slack_time[x][w] >= -1e-6
        for x in range(N_prc)
        for w in state.windows[x]
    )
    print(f"\n{_S}")
    print(f"  Total energy  : {total_e:.4f}  (budget={B_BUDGET}  slack={B_BUDGET-total_e:.4f})")
    print(f"  Total utility : {total_u:.6f}")
    print(f"  DBF feasible  : {feasible}")
    print(_S)
