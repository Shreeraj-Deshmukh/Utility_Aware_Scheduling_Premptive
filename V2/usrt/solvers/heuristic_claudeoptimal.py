"""
Heuristic claudeoptimal — Quantum SPS + greedy + multi-level local search.

Phases 1-6 : identical to heuristic_v4 (baseline)
Phase 7     : Double-giver swap — remove TWO low-utility segments to unlock
              ONE blocked high-utility segment; fill pass after each execute.
Phase 8     : Iterated greedy (IG) — destroy/reconstruct loop that escapes
              local optima via principled destruction + Phase 5+6 rebuild.

Key insight: with α=1, β=0.5 energy is minimised at f_max, so Phase 4 is a
structural no-op and all cases except (i) in Phase 5 are dead code.  The
entire problem reduces to binary segment selection under timing (DBF per
processor) and a global energy cap.  Phases 7-8 attack that combinatorial
problem with richer neighbourhood moves.
"""

import copy

from ..models import energy_val, total_energy, total_utility, ALPHA, BETA
from ..utils  import lcm_list, gcd_list, build_cum, build_job_times, build_proc_jobs
from ..mapping.quantum  import quantum_sps_mapping
from ..output            import print_instance_summary, print_schedule
from ..dbf.slack         import min_slack_for_job
from ..dbf.check         import check_all_timing
from ..phases.left_shift  import left_shift
from ..phases.energy_slack import compute_energy_slack, min_possible_energy
from ..phases.aggressive   import phase_aggressive_scaling
from ..phases.greedy       import phase_optional_segments
from ..phases.swap         import phase_swap_local_search
from ..phases.freq_trade   import phase_freq_utility_trade

_S  = "=" * 76
_S2 = "-" * 76

# ── Tuning knobs ──────────────────────────────────────────────────────────────
_MAX_DG_CANDIDATES = 20   # Phase 7: giver pool size (avoids O(n³) blowup)
_IG_ITERATIONS     = 8    # Phase 8: number of destroy/reconstruct rounds
_IG_DESTROY_FRAC   = 0.33 # Phase 8: fraction of active segments to destroy


# ─────────────────────────────────────────────────────────────────────────────
# Phase 7 — Double-giver swap
# ─────────────────────────────────────────────────────────────────────────────

def _phase_double_giver_swap(seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
                              N_tsk, N_job, proc_jobs, proc_jobs_map,
                              job_r, job_d, tasks, N_prc, B_BUDGET,
                              max_candidates=_MAX_DG_CANDIDATES):
    """
    Remove the last optional segment of TWO givers simultaneously to open
    timing + energy room for ONE receiver that could not be served by any
    single-giver swap.

    Returns: (n_swaps, final_E_slack, log_entries).
    """
    E_slack = B_BUDGET - total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job)
    log = []; n_swaps = 0

    while True:
        # Build giver pool — jobs with ≥1 optional segment, sorted by
        # marginal utility ASC (lowest-value segs destroyed first).
        giver_pool = []
        for i in range(N_tsk):
            for j in range(N_job[i]):
                k = seg_k[(i, j)]
                if k == 0:
                    continue
                marginal = tasks[i]['u_i'] * (cum[i][k] - cum[i][k - 1])
                giver_pool.append((marginal, i, j))
        giver_pool.sort()
        giver_pool = giver_pool[:max_candidates]

        if len(giver_pool) < 2:
            break

        best = None  # (net_u, i1,j1,k1, i2,j2,k2, i_r,j_r,k_r, dE1,dE2,dE_cost)

        for gi1 in range(len(giver_pool)):
            mu1, i1, j1 = giver_pool[gi1]
            k1 = seg_k[(i1, j1)]
            z1 = freq_idx[(i1, j1)]
            dE1 = (energy_val(cum[i1][k1], freq_set[z1]) -
                   energy_val(cum[i1][k1 - 1], freq_set[z1]))

            for gi2 in range(gi1 + 1, len(giver_pool)):
                mu2, i2, j2 = giver_pool[gi2]
                k2 = seg_k[(i2, j2)]
                z2 = freq_idx[(i2, j2)]
                dE2 = (energy_val(cum[i2][k2], freq_set[z2]) -
                       energy_val(cum[i2][k2 - 1], freq_set[z2]))

                u_lost     = mu1 + mu2
                new_E_slack = E_slack + dE1 + dE2

                # Tentatively remove both givers so receiver sees updated slack
                seg_k[(i1, j1)] = k1 - 1
                seg_k[(i2, j2)] = k2 - 1

                for i_r in range(N_tsk):
                    for j_r in range(N_job[i_r]):
                        if (i_r, j_r) == (i1, j1) or (i_r, j_r) == (i2, j2):
                            continue
                        k_r = seg_k[(i_r, j_r)]
                        if k_r >= N_seg[i_r]:
                            continue

                        z_r     = freq_idx[(i_r, j_r)]
                        x_r     = proc_jobs_map[(i_r, j_r)]
                        u_gain  = tasks[i_r]['u_i'] * (cum[i_r][k_r + 1] - cum[i_r][k_r])
                        net_u   = u_gain - u_lost
                        if net_u <= 1e-9:
                            continue

                        dE_cost = (energy_val(cum[i_r][k_r + 1], freq_set[z_r]) -
                                   energy_val(cum[i_r][k_r],     freq_set[z_r]))
                        if new_E_slack < dE_cost - 1e-9:
                            continue

                        add_time = (cum[i_r][k_r + 1] - cum[i_r][k_r]) / freq_set[z_r]
                        min_sl   = min_slack_for_job(i_r, j_r, x_r, proc_jobs,
                                                     job_r, job_d, seg_k,
                                                     freq_idx, freq_set, cum)
                        if min_sl < add_time - 1e-9:
                            continue

                        if best is None or net_u > best[0]:
                            best = (net_u, i1, j1, k1, i2, j2, k2,
                                    i_r, j_r, k_r, dE1, dE2, dE_cost)

                # Restore givers
                seg_k[(i1, j1)] = k1
                seg_k[(i2, j2)] = k2

        if best is None:
            break

        net_u, i1, j1, k1, i2, j2, k2, i_r, j_r, k_r, dE1, dE2, dE_cost = best

        seg_k[(i1, j1)]  = k1 - 1
        seg_k[(i2, j2)]  = k2 - 1
        seg_k[(i_r, j_r)] = k_r + 1

        if check_all_timing(proc_jobs, job_r, job_d, seg_k,
                            freq_idx, freq_set, cum, N_prc):
            E_slack  = E_slack + dE1 + dE2 - dE_cost
            n_swaps += 1
            log.append(
                f"  DGSwap {n_swaps}:"
                f"  remove T{tasks[i1]['id']},j{j1} k:{k1}→{k1-1}"
                f"  + T{tasks[i2]['id']},j{j2} k:{k2}→{k2-1}"
                f"  |  add T{tasks[i_r]['id']},j{j_r} k:{k_r}→{k_r+1}"
                f"  |  +util={net_u:.4f}  E_slack={E_slack:.3f}"
            )
            # Fill pass
            _, E_slack, fill_log = phase_optional_segments(
                seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
                N_tsk, N_job, proc_jobs, proc_jobs_map,
                job_r, job_d, tasks, N_prc, B_BUDGET)
            if fill_log:
                log.append(f"    Fill after DGSwap {n_swaps} ({len(fill_log)} addition(s)):")
                log.extend(fill_log)
        else:
            seg_k[(i1, j1)]  = k1
            seg_k[(i2, j2)]  = k2
            seg_k[(i_r, j_r)] = k_r
            log.append(f"  DGSwap {n_swaps + 1}: REVERTED (timing violation)")
            break

    return n_swaps, E_slack, log


# ─────────────────────────────────────────────────────────────────────────────
# Phase 8 — Iterated greedy
# ─────────────────────────────────────────────────────────────────────────────

def _phase_iterated_greedy(seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
                            N_tsk, N_job, proc_jobs, proc_jobs_map,
                            job_r, job_d, tasks, N_prc, B_BUDGET,
                            n_iter=_IG_ITERATIONS,
                            destroy_fraction=_IG_DESTROY_FRAC):
    """
    Destroy/reconstruct meta-heuristic.

    Destruction score = u_i * (cum[k]-cum[k-1]) / add_time
        → "utility per unit exec time" — low score = cheap to remove,
           freeing timing density for higher-value segments.

    After destruction, rebuild with Phase 5 greedy + Phase 6 pairwise swap.
    Accept new solution if it strictly improves; otherwise restore best.
    At end, best solution is always restored into seg_k (in-place).

    Returns: (iterations_run, final_E_slack, log_entries).
    """
    best_seg_k  = dict(seg_k)
    # Phase 5 (case ii.A/ii.B) and Phase 6 both MUTATE freq_idx during the
    # reconstruct step, so the frequency assignment must be snapshotted and
    # rolled back together with seg_k.  Restoring seg_k alone leaves an
    # inconsistent (seg_k, freq_idx) pair whose energy can exceed the budget.
    best_freq_idx = dict(freq_idx)
    best_utility = total_utility(seg_k, tasks, cum, N_tsk, N_job)
    log = []

    for it in range(n_iter):
        # Score each active optional segment
        scored = []
        for i in range(N_tsk):
            for j in range(N_job[i]):
                k = seg_k[(i, j)]
                if k == 0:
                    continue
                z        = freq_idx[(i, j)]
                marginal = tasks[i]['u_i'] * (cum[i][k] - cum[i][k - 1])
                add_time = (cum[i][k] - cum[i][k - 1]) / freq_set[z]
                density  = marginal / (add_time + 1e-9)
                scored.append((density, i, j))

        if not scored:
            log.append(f"  IG iter {it + 1}: no active segments — stopping early.")
            break

        scored.sort()  # ascending density: cheapest first
        n_destroy = max(1, int(len(scored) * destroy_fraction))
        to_destroy = scored[:n_destroy]

        # Destroy: reset selected jobs to mandatory-only (k=0)
        destroyed = []
        for _, i, j in to_destroy:
            if seg_k[(i, j)] > 0:
                destroyed.append((i, j, seg_k[(i, j)]))
                seg_k[(i, j)] = 0

        # Reconstruct: greedy + pairwise swap
        phase_optional_segments(seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
                                N_tsk, N_job, proc_jobs, proc_jobs_map,
                                job_r, job_d, tasks, N_prc, B_BUDGET)
        phase_swap_local_search(seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
                                N_tsk, N_job, proc_jobs, proc_jobs_map,
                                job_r, job_d, tasks, N_prc, B_BUDGET)

        new_utility = total_utility(seg_k, tasks, cum, N_tsk, N_job)
        accepted    = new_utility > best_utility + 1e-9
        log.append(
            f"  IG iter {it + 1}:"
            f"  destroyed={len(destroyed)}"
            f"  utility={new_utility:.6f}"
            f"  best={best_utility:.6f}"
            f"  {'ACCEPT' if accepted else 'REJECT'}"
        )

        if accepted:
            best_seg_k    = dict(seg_k)
            best_freq_idx = dict(freq_idx)
            best_utility  = new_utility
        else:
            for key in seg_k:
                seg_k[key] = best_seg_k[key]
            for key in freq_idx:
                freq_idx[key] = best_freq_idx[key]

    # Guarantee best solution is active (segments AND frequencies)
    for key in seg_k:
        seg_k[key] = best_seg_k[key]
    for key in freq_idx:
        freq_idx[key] = best_freq_idx[key]

    E_final = B_BUDGET - total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job)
    return n_iter, E_final, log


# ─────────────────────────────────────────────────────────────────────────────
# Main entry point
# ─────────────────────────────────────────────────────────────────────────────

def run(processors, tasks, B_BUDGET):
    """
    Returns (seg_k, freq_idx, utility, energy, mapping).

    `mapping` is part of the contract, not a convenience: a schedule is only
    meaningful relative to the job->processor assignment it was built on, so
    without it a caller cannot DBF-check what it was handed.  See
    usrt/runner/adapters._schedule_feasible and ISSUES.md -> REPAIR-PARTIAL.
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

    print_instance_summary(processors, tasks, B_BUDGET, h, quantum, N_job, N_seg,
                           ALPHA, BETA, label="USRT Heuristic claudeoptimal  —  Instance")

    # ── Phase 1: Quantum SPS mapping ─────────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 1 : QUANTUM SPS MAPPING")
    print(_S2)
    mapping = quantum_sps_mapping(tasks, processors, h, quantum, verbose=True)
    proc_jobs, proc_jobs_map = build_proc_jobs(mapping)

    print(f"\n  Processor utilisation:")
    for x in range(N_prc):
        ul = sum(tasks[i]['e_m'] / h for (i, j) in proc_jobs[x])
        print(f"    P{x}: {len(proc_jobs[x])} jobs  util={ul:.4f}"
              f"{'  ← OVER 1.0' if ul > 1 else ''}")

    # Initialise: f_max, k=0
    freq_idx = {(i, j): N_frq - 1 for i in range(N_tsk) for j in range(N_job[i])}
    seg_k    = {(i, j): 0         for i in range(N_tsk) for j in range(N_job[i])}

    # ── Phase 2: Left shift (diagnostic) ─────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 2 : LEFT SHIFT  (f_max, mandatory only)")
    print(_S2)
    ls     = left_shift(proc_jobs, job_r, job_d, seg_k, freq_idx, freq_set, cum)
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
    E_floor = min_possible_energy(seg_k, freq_set, cum, N_tsk, N_job)
    # Phase 3 must NOT declare infeasible merely because f_max busts the
    # budget -- Phase 4 lowers frequency and is the fix for exactly that.
    # Only a budget below the cheapest-possible assignment is terminal.
    if B_BUDGET < E_floor - 1e-9:
        print(f"  Budget below cheapest-possible mandatory cost — infeasible at any frequency.")
        print_schedule(seg_k, freq_idx, freq_set, cum, tasks, N_tsk, N_job,
                       mapping, B_BUDGET, label="INFEASIBLE MANDATORY")
        return seg_k, freq_idx, 0.0, E_init, mapping

    # ── Phase 4: Aggressive scaling (structural no-op at α=1, β=0.5) ─────────
    print(f"\n{_S}")
    print(f"  PHASE 4 : AGGRESSIVE SCALING  (freq ↓ + energy guard)")
    print(_S2)
    n_sc = phase_aggressive_scaling(seg_k, freq_idx, freq_set, N_frq, cum,
                                     N_tsk, N_job, proc_jobs, job_r, job_d, N_prc,
                                     B_BUDGET)
    if n_sc == 0:
        print(f"  No reductions (α={ALPHA}, β={BETA}): already energy-feasible at f_max → no-op.")
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
    n_sw6, E_after6, log6 = phase_swap_local_search(
        seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
        N_tsk, N_job, proc_jobs, proc_jobs_map,
        job_r, job_d, tasks, N_prc, B_BUDGET)

    u_after6 = total_utility(seg_k, tasks, cum, N_tsk, N_job)
    if log6:
        print(f"  {n_sw6} swap(s) executed:")
        for e in log6: print(e)
    else:
        print(f"  No improving swaps found.")
    print(f"\n  Phase 6 result: utility={u_after6:.6f}  E_slack={E_after6:.4f}")
    print(f"  Utility gain from Phase 6: {u_after6 - u_after5:+.6f}")

    # Phase 6b: frequency<->segment trade (shadow-price governed)
    print(f"\n{_S}")
    print(f"  PHASE 6b: FREQUENCY <-> SEGMENT TRADE  (lambda*dE > mu*dT)")
    print(_S2)
    n_tr, E_after6b, log6b = phase_freq_utility_trade(
        seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
        N_tsk, N_job, proc_jobs, proc_jobs_map,
        job_r, job_d, tasks, N_prc, B_BUDGET)
    if log6b:
        print(f"  {n_tr} profitable trade(s):")
        for e in log6b: print(e)
    else:
        print(f"  No profitable frequency/segment trade found.")
    print(f"  Phase 6b utility={total_utility(seg_k, tasks, cum, N_tsk, N_job):.6f}")

    # ── Phase 7: Double-giver swap ────────────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 7 : DOUBLE-GIVER SWAP  (2 givers → 1 receiver)")
    print(f"  Giver pool size: {_MAX_DG_CANDIDATES}  |  Fill pass after each swap.")
    print(_S2)
    n_sw7, E_after7, log7 = _phase_double_giver_swap(
        seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
        N_tsk, N_job, proc_jobs, proc_jobs_map,
        job_r, job_d, tasks, N_prc, B_BUDGET)

    u_after7 = total_utility(seg_k, tasks, cum, N_tsk, N_job)
    if log7:
        print(f"  {n_sw7} double-giver swap(s) executed:")
        for e in log7: print(e)
    else:
        print(f"  No improving double-giver swaps found.")
    print(f"\n  Phase 7 result: utility={u_after7:.6f}  E_slack={E_after7:.4f}")
    print(f"  Utility gain from Phase 7: {u_after7 - u_after6:+.6f}")

    # ── Phase 8: Iterated greedy ──────────────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 8 : ITERATED GREEDY")
    print(f"  Iterations: {_IG_ITERATIONS}  |  Destroy fraction: {_IG_DESTROY_FRAC:.0%}")
    print(f"  Destruction score: utility-density (u*Δcum / exec_time) ASC")
    print(f"  Rebuild: Phase 5 greedy + Phase 6 pairwise swap.")
    print(_S2)
    n_it8, E_after8, log8 = _phase_iterated_greedy(
        seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
        N_tsk, N_job, proc_jobs, proc_jobs_map,
        job_r, job_d, tasks, N_prc, B_BUDGET)

    u_after8 = total_utility(seg_k, tasks, cum, N_tsk, N_job)
    for e in log8: print(e)
    print(f"\n  Phase 8 result: utility={u_after8:.6f}  E_slack={E_after8:.4f}")
    print(f"  Utility gain from Phase 8: {u_after8 - u_after7:+.6f}")

    # ── Final schedule ────────────────────────────────────────────────────────
    tot_e, tot_u = print_schedule(
        seg_k, freq_idx, freq_set, cum, tasks, N_tsk, N_job,
        mapping, B_BUDGET, label="HEURISTIC claudeoptimal SOLUTION (FINAL)")

    print(f"\n  Summary of gains:")
    print(f"    Phase 5 (greedy)        : {u_after5:.6f}")
    print(f"    Phase 6 (+pairwise swap): {u_after6:.6f}  ({u_after6 - u_after5:+.6f})")
    print(f"    Phase 7 (+double-giver) : {u_after7:.6f}  ({u_after7 - u_after6:+.6f})")
    print(f"    Phase 8 (+iter greedy)  : {u_after8:.6f}  ({u_after8 - u_after7:+.6f})")
    print(_S)

    return seg_k, freq_idx, tot_u, tot_e, mapping
