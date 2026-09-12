"""
Heuristic v7 — multi-start mapping + guided repair.

Motivation (measured, 22 Aug):
  * The MAPPING, not the frequency/segment search, is the dominant error at
    tight budgets: at rho=0.4 the gap decomposes as 44.0% from the SPS mapping
    and only 14.2% from the search that follows it.
  * Phase 1c (v6) attacks the mapping and works, but costs ~25 full pipelines
    (30.91 ms vs Phase 1's 0.20 ms) -- and its expense is the SCORING, not the
    search: it examines only J*(P-1) single-job moves.

v7 therefore spends the same currency (full-pipeline evaluations) far more
efficiently:

  Phase 1M : MULTI-START.  Build several structurally different mappings --
             SPS, SPS+Refine2b, SPS+budget-refine, WFD, FFD, BFD,
             donor/harvester -- and score each with ONE pipeline.  Five
             different mappings explore more than twenty-five single-job moves
             away from one basin, and WFD is additionally the mapping the
             paper's Section V.B baseline prescribes.
  Phase 1R : GUIDED REPAIR.  Diagnose which processor still has TIME-blocked
             optional utility and move its least valuable job away.  Processors
             that are ENERGY-blocked are skipped: energy is global, so no
             reassignment can create any -- which is precisely where blind local
             search wastes most of its evaluations.
  Phases 2-6b : identical to v5b/v6.

Both mapping stages score on the real objective and keep a best-so-far, so
neither can return a mapping worse than the ones it was given.
"""

from ..models   import ALPHA, BETA, total_energy, total_utility
from ..utils    import lcm_list, gcd_list, build_cum, build_job_times, build_proc_jobs
from ..mapping.quantum        import quantum_sps_mapping
from ..mapping.refine_mapping import refine_mapping_2b
from ..mapping.budget_refine  import refine_mapping_budget
from ..mapping.packers        import pack_all
from ..mapping.multistart     import multi_start, guided_repair, diagnose_blocked
from ..mapping.budget_refine  import mapping_local_search
from ..output   import print_instance_summary, print_schedule
from ..phases.energy_slack import min_possible_energy
from ..phases.aggressive   import phase_aggressive_scaling
from ..phases.greedy       import phase_optional_segments
from ..phases.swap         import phase_swap_local_search
from ..phases.freq_trade   import phase_freq_utility_trade

_S  = "=" * 76
_S2 = "-" * 76

GUIDED_REPAIR_MOVES = 4
# A SHORT local search on top of the multi-start winner.  v6 spent ~25
# evaluations on this from a single SPS basin; starting from the best of
# seven structurally different mappings, far fewer are needed.
# MEASURED NEGATIVE RESULT (22 Aug): adding a 10-move local search on top of
# the multi-start winner cost 27.9 ms (vs 14.0 without) yet did NOT close the
# gap to v6 (5.10% vs 4.77%).  Starting from the best of seven structurally
# different mappings, extra single-job moves buy almost nothing -- the diversity
# has already been spent.  Disabled; set LS_ROUNDS > 0 to re-enable.
LS_ROUNDS    = 0
LS_MAX_MOVES = 10


def _pipeline(mapping, tasks, B_BUDGET, cum, N_seg, N_tsk, N_job,
              job_r, job_d, freq_set, N_frq, N_prc):
    """Phases 2-6b on a mapping. Returns (seg_k, freq_idx, u, e, feasible)."""
    proc_jobs, proc_jobs_map = build_proc_jobs(mapping)
    freq_idx = {(i, j): N_frq - 1 for i in range(N_tsk) for j in range(N_job[i])}
    seg_k    = {(i, j): 0         for i in range(N_tsk) for j in range(N_job[i])}

    if B_BUDGET < min_possible_energy(seg_k, freq_set, cum, N_tsk, N_job) - 1e-9:
        return seg_k, freq_idx, 0.0, total_energy(
            seg_k, freq_idx, freq_set, cum, N_tsk, N_job), False

    phase_aggressive_scaling(seg_k, freq_idx, freq_set, N_frq, cum,
                             N_tsk, N_job, proc_jobs, job_r, job_d, N_prc, B_BUDGET)
    phase_optional_segments(seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
                            N_tsk, N_job, proc_jobs, proc_jobs_map,
                            job_r, job_d, tasks, N_prc, B_BUDGET)
    phase_swap_local_search(seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
                            N_tsk, N_job, proc_jobs, proc_jobs_map,
                            job_r, job_d, tasks, N_prc, B_BUDGET)
    phase_freq_utility_trade(seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
                             N_tsk, N_job, proc_jobs, proc_jobs_map,
                             job_r, job_d, tasks, N_prc, B_BUDGET)
    e = total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job)
    u = total_utility(seg_k, tasks, cum, N_tsk, N_job)
    return seg_k, freq_idx, u, e, (e <= B_BUDGET + 1e-6)


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
                           ALPHA, BETA, label="USRT Heuristic v7  —  Instance")

    def _eval(m):
        _, _, u, _, ok = _pipeline(m, tasks, B_BUDGET, cum, N_seg, N_tsk, N_job,
                                   job_r, job_d, freq_set, N_frq, N_prc)
        return u, ok

    # ── Phase 1M : multi-start ───────────────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 1M : MULTI-START MAPPING")
    print(_S2)
    sps = quantum_sps_mapping(tasks, processors, h, quantum, verbose=False)
    cands = [("sps", sps)]
    try:
        cands.append(("sps+refine2b",
                      refine_mapping_2b(dict(sps), tasks, N_prc, cum, N_seg,
                                        job_r, job_d, verbose=False)))
    except Exception:
        pass
    try:
        bm, _info = refine_mapping_budget(dict(sps), tasks, N_tsk, N_prc, N_job,
                                          cum, N_seg, job_r, job_d, freq_set,
                                          B_BUDGET, h, verbose=False)
        cands.append(("sps+budget", bm))
    except Exception:
        pass
    cands.extend(pack_all(tasks, processors, h, job_r, job_d, cum, N_seg,
                          freq_set, N_tsk, N_job, N_prc))

    name, mapping, u_ms, log = multi_start(cands, _eval)
    for line in log:
        print(line)
    print(f"  -> best: {name}   utility={u_ms:.6f}   ({len(cands)} candidates)")

    # ── Phase 1R : guided repair ─────────────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 1R : GUIDED REPAIR  (move off the TIME-blocked processor)")
    print(_S2)

    def _diagnose(m):
        seg_k, freq_idx, u, e, ok = _pipeline(
            m, tasks, B_BUDGET, cum, N_seg, N_tsk, N_job,
            job_r, job_d, freq_set, N_frq, N_prc)
        if not ok:
            return {}, u, False
        pj, pjm = build_proc_jobs(m)
        info = diagnose_blocked(seg_k, freq_idx, freq_set, cum, N_seg,
                                N_tsk, N_job, pj, pjm, job_r, job_d, tasks,
                                B_BUDGET - e)
        return info, u, True

    mapping, u_rep, rlog = guided_repair(
        mapping, _eval, _diagnose, tasks, cum, N_seg, N_prc,
        max_moves=GUIDED_REPAIR_MOVES)
    for line in rlog:
        print(line)
    print(f"  -> utility after repair: {u_rep:.6f}  ({u_rep - u_ms:+.6f})")

    # ── Phase 1L : short local search from the repaired mapping ──────────────
    if LS_ROUNDS > 0:
        print(f"\n{_S}")
        print(f"  PHASE 1L : SHORT LOCAL SEARCH  ({LS_MAX_MOVES} moves x {LS_ROUNDS} round)")
        print(_S2)
        mapping, ls = mapping_local_search(mapping, _eval, N_prc,
                                           max_rounds=LS_ROUNDS,
                                           max_moves=LS_MAX_MOVES, verbose=False)
        print(f"  {ls['moves']} improving move(s)  -> utility {ls['utility']:.6f}"
              f"  ({ls['utility'] - u_rep:+.6f})")

    # ── Phases 2-6b on the chosen mapping ────────────────────────────────────
    seg_k, freq_idx, u, e, feas = _pipeline(
        mapping, tasks, B_BUDGET, cum, N_seg, N_tsk, N_job,
        job_r, job_d, freq_set, N_frq, N_prc)
    print(f"\n  final: utility={u:.6f}  energy={e:.4f}/{B_BUDGET:.4f}  feasible={feas}")

    tot_e, tot_u = print_schedule(
        seg_k, freq_idx, freq_set, cum, tasks, N_tsk, N_job,
        mapping, B_BUDGET, label="HEURISTIC v7 SOLUTION (FINAL)")
    return seg_k, freq_idx, tot_u, tot_e, mapping
