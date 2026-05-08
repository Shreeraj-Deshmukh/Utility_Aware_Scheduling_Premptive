"""
Heuristic v2 — Quantum SPS + left-shift greedy pipeline.

Mapping  : quantum_sps_mapping (Phase 1)
Phase 2  : left_shift (diagnostic, run once)
Phase 3  : energy slack check
Phase 4  : aggressive scaling (structural no-op at α=1, β=0.5)
Phase 5  : greedy_optional_segments_leftshift
           (uses left-shift time proxy; recomputes after each change;
            3-step case structure: case i, ii-step1, ii-step2, ii-step3)

Equivalent to the heuristicv3.py monolith.
"""

from collections import defaultdict

from ..models   import ALPHA, BETA, total_energy, total_utility
from ..utils    import load_testcase, lcm_list, gcd_list, build_cum, build_job_times, build_proc_jobs
from ..mapping.quantum import quantum_sps_mapping
from ..output   import print_instance_summary, print_mapping_summary
from ..phases.left_shift  import left_shift_mapping
from ..phases.energy_slack import compute_energy_slack
from ..phases.greedy_leftshift import phase_optional_segments_leftshift

_S  = "=" * 76
_S2 = "-" * 76


def run(processors, tasks, B_BUDGET):
    N_tsk    = len(tasks)
    N_prc    = len(processors)
    freq_set = processors[0]['frequencies']
    N_frq    = len(freq_set)
    f_max_idx = N_frq - 1
    periods  = [int(t['p_i']) for t in tasks]
    h        = lcm_list(periods)
    quantum  = gcd_list(periods)
    cum, N_seg = build_cum(tasks)
    N_job    = [h // periods[i] for i in range(N_tsk)]
    job_r, job_d = build_job_times(tasks, h)

    print_instance_summary(processors, tasks, B_BUDGET, h, quantum, N_job, N_seg,
                           ALPHA, BETA, label="USRT Heuristic v2  —  Instance")

    # ── Phase 1: Quantum SPS mapping ─────────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 1 : QUANTUM SPS MAPPING")
    print(_S2)
    mapping = quantum_sps_mapping(tasks, processors, h, quantum, verbose=True)
    proc_jobs, _ = build_proc_jobs(mapping)

    print(f"\n  Processor utilisation:")
    for x in range(N_prc):
        ul = sum(tasks[i]['e_m'] / tasks[i]['p_i'] for (i, j) in proc_jobs[x])
        print(f"    P{x}: {len(proc_jobs[x])} jobs  util={ul:.4f}"
              f"{'  ← OVER 1.0' if ul > 1 else ''}")

    print_mapping_summary(mapping, tasks, processors, h, job_r, job_d)

    # Initialise state: f_max, k=0
    seg_state  = {(i, j): 0         for i in range(N_tsk) for j in range(N_job[i])}
    freq_state = {(i, j): f_max_idx for i in range(N_tsk) for j in range(N_job[i])}

    # ── Phase 2: Left shift ───────────────────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 2 : LEFT SHIFT  (f_max, mandatory only)")
    print(_S2)
    time_slack = left_shift_mapping(mapping, tasks, processors, h,
                                    seg_state, freq_state, cum, freq_set)
    min_slack  = min(time_slack.values()) if time_slack else 0.0
    print(f"  Min time slack: {min_slack:.4f}")

    # ── Phase 3: Energy slack ─────────────────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 3 : ENERGY SLACK")
    print(_S2)
    E_consumed, E_slack = compute_energy_slack(seg_state, freq_state, freq_set,
                                               cum, N_tsk, N_job, B_BUDGET)
    print(f"  E_consumed (mandatory, f_max): {E_consumed:.4f}")
    print(f"  E_budget                     : {B_BUDGET:.4f}")
    print(f"  E_slack                      : {E_slack:.4f}"
          f"{'  [INFEASIBLE]' if E_slack < 0 else ''}")
    if E_slack < -1e-9:
        print(f"  Mandatory cost exceeds budget — no feasible schedule.")
        return seg_state, freq_state, 0.0, E_consumed

    # ── Phase 4: Aggressive scaling (structural no-op at α=1, β=0.5) ─────────
    print(f"\n{_S}")
    print(f"  PHASE 4 : AGGRESSIVE SCALING  (freq UP toward f_max)")
    print(_S2)
    scaled = 0
    from ..dbf.check import check_dbf_proc
    from ..models import energy_val
    for i in range(N_tsk):
        for j in range(N_job[i]):
            z_cur = freq_state[(i, j)]
            if z_cur >= f_max_idx:
                continue
            z_new = z_cur + 1
            k     = seg_state[(i, j)]
            dE    = (energy_val(cum[i][k], freq_set[z_new]) -
                     energy_val(cum[i][k], freq_set[z_cur]))
            if E_slack + dE >= -1e-9:
                freq_state[(i, j)] = z_new
                x = mapping[(i, j)]
                if check_dbf_proc(x, mapping, tasks, h,
                                   seg_state, freq_state, cum, freq_set):
                    E_slack -= dE; scaled += 1
                else:
                    freq_state[(i, j)] = z_cur
    print(f"  Jobs frequency-scaled: {scaled}")
    time_slack = left_shift_mapping(mapping, tasks, processors, h,
                                    seg_state, freq_state, cum, freq_set)
    print(f"  E_slack after scaling: {E_slack:.4f}")

    # ── Phase 5: Greedy optional segment scheduling (left-shift variant) ──────
    print(f"\n{_S}")
    print(f"  PHASE 5 : GREEDY OPTIONAL SEGMENT SCHEDULING  (left-shift proxy)")
    print(_S2)
    seg_state, freq_state, E_slack, total_util_val, iterations = \
        phase_optional_segments_leftshift(
            mapping, tasks, processors, h, B_BUDGET,
            seg_state, freq_state, cum, N_seg,
            freq_set, N_frq, N_tsk, N_job,
            time_slack, E_slack
        )
    print(f"  Iterations: {iterations}  Final E_slack: {E_slack:.4f}  "
          f"Utility: {total_util_val:.6f}")

    # ── Final schedule ────────────────────────────────────────────────────────
    from ..output import print_schedule
    tot_e, tot_u = print_schedule(
        seg_state, freq_state, freq_set, cum, tasks, N_tsk, N_job,
        mapping, B_BUDGET, label="HEURISTIC v2 SOLUTION")

    return seg_state, freq_state, tot_u, tot_e
