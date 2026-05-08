"""
Heuristic v4 — Quantum SPS + DBF window-slack greedy + Swap local search
               (all 6 phases).

Mapping  : quantum_sps_mapping (Phase 1)
Phase 2  : left_shift (diagnostic)
Phase 3  : energy slack check
Phase 4  : aggressive_scaling (freq ↓ + energy guard)
Phase 5  : phase_optional_segments (DBF window slack, 1-seg-per-j*-per-pass)
Phase 6  : phase_swap_local_search (best-first pairwise swap + fill pass)

Equivalent to heuristic_claude.py monolith.
"""

from collections import defaultdict

from ..models   import ALPHA, BETA, total_energy, total_utility
from ..utils    import lcm_list, gcd_list, build_cum, build_job_times, build_proc_jobs
from ..mapping.quantum import quantum_sps_mapping
from ..output   import print_instance_summary, print_schedule
from ..phases.left_shift   import left_shift
from ..phases.energy_slack import compute_energy_slack
from ..phases.aggressive   import phase_aggressive_scaling
from ..phases.greedy       import phase_optional_segments
from ..phases.swap         import phase_swap_local_search

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
                           ALPHA, BETA, label="USRT Heuristic v4  —  Instance")

    # ── Phase 1: Quantum SPS mapping ─────────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 1 : QUANTUM SPS MAPPING")
    print(_S2)
    mapping = quantum_sps_mapping(tasks, processors, h, quantum, verbose=True)
    proc_jobs, proc_jobs_map = build_proc_jobs(mapping)

    print(f"\n  Processor utilisation:")
    for x in range(N_prc):
        ul = sum(tasks[i]['e_m'] / tasks[i]['p_i'] for (i, j) in proc_jobs[x])
        print(f"    P{x}: {len(proc_jobs[x])} jobs  util={ul:.4f}"
              f"{'  ← OVER 1.0' if ul > 1 else ''}")

    # Initialise: f_max, k=0
    freq_idx = {(i, j): N_frq - 1 for i in range(N_tsk) for j in range(N_job[i])}
    seg_k    = {(i, j): 0         for i in range(N_tsk) for j in range(N_job[i])}

    # ── Phase 2: Left shift (diagnostic) ─────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 2 : LEFT SHIFT  (f_max, mandatory only)")
    print(_S2)
    ls    = left_shift(proc_jobs, job_r, job_d, seg_k, freq_idx, freq_set, cum)
    infeas = [k for k, v in ls.items() if v < -1e-9]
    print(f"  Jobs with negative left-shift slack: {len(infeas)}")
    print(f"  Min left-shift slack: {min(ls.values()):.4f}")

    # ── Phase 3: Energy slack ─────────────────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 3 : ENERGY SLACK")
    print(_S2)
    E_init, E_slk = compute_energy_slack(seg_k, freq_idx, freq_set,
                                          cum, N_tsk, N_job, B_BUDGET)
    print(f"  E_consumed (mandatory, f_max): {E_init:.4f}")
    print(f"  E_budget                     : {B_BUDGET:.4f}")
    print(f"  E_slack                      : {E_slk:.4f}"
          f"{'  [INFEASIBLE]' if E_slk < 0 else ''}")
    if E_slk < -1e-9:
        print(f"  Mandatory cost exceeds budget — no feasible schedule.")
        print_schedule(seg_k, freq_idx, freq_set, cum, tasks, N_tsk, N_job,
                       mapping, B_BUDGET, label="INFEASIBLE MANDATORY")
        return seg_k, freq_idx, 0.0, E_init

    # ── Phase 4: Aggressive scaling ───────────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 4 : AGGRESSIVE SCALING  (freq ↓ + energy guard)")
    print(_S2)
    n_sc = phase_aggressive_scaling(seg_k, freq_idx, freq_set, N_frq, cum,
                                     N_tsk, N_job, proc_jobs, job_r, job_d, N_prc)
    if n_sc == 0:
        print(f"  No reductions (α={ALPHA}, β={BETA} → min energy at f_max → no-op).")
    else:
        Ea = total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job)
        print(f"  {n_sc} job(s) reduced.  E_consumed={Ea:.4f}  E_slack={B_BUDGET-Ea:.4f}")

    # ── Phase 5: Greedy optional segments ────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 5 : GREEDY OPTIONAL SEGMENT SCHEDULING")
    print(_S2)
    n_p5, E_after5, log5 = phase_optional_segments(
        seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
        N_tsk, N_job, proc_jobs, proc_jobs_map,
        job_r, job_d, tasks, N_prc, B_BUDGET)

    u_after5 = total_utility(seg_k, tasks, cum, N_tsk, N_job)
    if log5:
        print(f"  {len(log5)} segment(s) added across {n_p5} pass(es):")
        for e in log5: print(e)
    else:
        print(f"  No optional segments added in Phase 5.")
    print(f"\n  Phase 5 result: utility={u_after5:.6f}  E_slack={E_after5:.4f}")

    # ── Phase 6: Best-first pairwise segment swap ─────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 6 : BEST-FIRST PAIRWISE SEGMENT SWAP")
    print(_S2)
    print(f"  Searching for improving (giver → receiver) swaps …")
    print(f"  After each swap: fill pass (Phase 5 re-run) to capitalise on freed resources.")
    print()
    n_sw, E_after6, log6 = phase_swap_local_search(
        seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
        N_tsk, N_job, proc_jobs, proc_jobs_map,
        job_r, job_d, tasks, N_prc, B_BUDGET)

    u_after6 = total_utility(seg_k, tasks, cum, N_tsk, N_job)
    if log6:
        print(f"  {n_sw} swap(s) executed:")
        for e in log6: print(e)
    else:
        print(f"  No improving swaps found. Phase 5 solution is locally optimal.")
    print(f"\n  Phase 6 result: utility={u_after6:.6f}  E_slack={E_after6:.4f}")
    print(f"  Utility gain from swaps: {u_after6 - u_after5:+.6f}")

    # ── Final schedule ────────────────────────────────────────────────────────
    tot_e, tot_u = print_schedule(
        seg_k, freq_idx, freq_set, cum, tasks, N_tsk, N_job,
        mapping, B_BUDGET, label="HEURISTIC v4 SOLUTION (FINAL)")

    return seg_k, freq_idx, tot_u, tot_e
