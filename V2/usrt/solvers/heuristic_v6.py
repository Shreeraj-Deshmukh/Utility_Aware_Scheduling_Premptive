"""
Heuristic v6 — v5b with a BUDGET-AWARE mapping stage.

Identical to v5b except for how the job->processor mapping is chosen:

  Phase 1   : Quantum SPS mapping                        (same as v5b)
  Phase 1b' : BUDGET-AWARE refine                        (proposals 1 + 2)
              - objective flips on the regime test E_mand_fmax <= B:
                  time-bound   -> balance      utility density
                  energy-bound -> concentrate  utility density
              - DBF + load balance judged at the operating frequency f_hat,
                not at f_max
  Phase 1c  : MAPPING-LEVEL LOCAL SEARCH                 (proposal 3, optional)
              single-job reassignments scored by the utility the FULL pipeline
              actually achieves; incumbent replaced only on strict improvement
  Phases 2-6b: exactly v5b's pipeline

Every stage is non-regressive by construction: 1b' only accepts swaps that keep
mandatory DBF feasible at f_hat, and 1c only accepts a mapping that the whole
pipeline scores strictly higher.  With MAP_LOCAL_SEARCH = False and a
time-bound instance, v6 reduces to v5b's behaviour.
"""

from ..models   import ALPHA, BETA, total_energy, total_utility
from ..utils    import lcm_list, gcd_list, build_cum, build_job_times, build_proc_jobs
from ..mapping.quantum        import quantum_sps_mapping
from ..mapping.budget_refine  import (refine_mapping_budget, mapping_local_search,
                                      estimate_operating_freq, is_energy_bound)
from ..output   import print_instance_summary, print_schedule
from ..phases.energy_slack import compute_energy_slack, min_possible_energy
from ..phases.aggressive   import phase_aggressive_scaling
from ..phases.greedy       import phase_optional_segments
from ..phases.swap         import phase_swap_local_search
from ..phases.freq_trade   import phase_freq_utility_trade

_S  = "=" * 76
_S2 = "-" * 76

MAP_LOCAL_SEARCH = True      # proposal 3
MAP_LS_ROUNDS    = 2
MAP_LS_MAX_MOVES = 24        # candidate reassignments evaluated per round


def _pipeline(mapping, tasks, processors, B_BUDGET, cum, N_seg, N_tsk, N_job,
              job_r, job_d, freq_set, N_frq, N_prc):
    """
    Run phases 2-6b on a given mapping.  Returns (seg_k, freq_idx, utility,
    energy, feasible).  Pure: it does not mutate anything the caller owns.
    """
    proc_jobs, proc_jobs_map = build_proc_jobs(mapping)
    freq_idx = {(i, j): N_frq - 1 for i in range(N_tsk) for j in range(N_job[i])}
    seg_k    = {(i, j): 0         for i in range(N_tsk) for j in range(N_job[i])}

    E_floor = min_possible_energy(seg_k, freq_set, cum, N_tsk, N_job)
    if B_BUDGET < E_floor - 1e-9:
        return seg_k, freq_idx, 0.0, total_energy(
            seg_k, freq_idx, freq_set, cum, N_tsk, N_job), False

    phase_aggressive_scaling(seg_k, freq_idx, freq_set, N_frq, cum,
                             N_tsk, N_job, proc_jobs, job_r, job_d, N_prc,
                             B_BUDGET)
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
                           ALPHA, BETA, label="USRT Heuristic v6  —  Instance")

    # ── Phase 1 ──────────────────────────────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 1 : QUANTUM SPS MAPPING")
    print(_S2)
    mapping = quantum_sps_mapping(tasks, processors, h, quantum, verbose=True)

    # ── Phase 1b': budget-aware refine ───────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 1b': BUDGET-AWARE REFINE MAPPING")
    print(_S2)
    sps_mapping = dict(mapping)
    refined, info = refine_mapping_budget(
        mapping, tasks, N_tsk, N_prc, N_job, cum, N_seg,
        job_r, job_d, freq_set, B_BUDGET, h, verbose=True)

    # The refinement optimises a PROXY (utility density), so it can land on a
    # mapping the full pipeline scores lower than plain SPS.  Score both on the
    # real objective and keep the better one -- this makes Phase 1b' unable to
    # hurt, and gives the local search below the stronger starting point.
    def _score(m):
        _, _, u, _, ok = _pipeline(m, tasks, processors, B_BUDGET, cum, N_seg,
                                   N_tsk, N_job, job_r, job_d, freq_set,
                                   N_frq, N_prc)
        return (u if ok else -1.0)
    u_sps, u_ref = _score(sps_mapping), _score(refined)
    if u_ref >= u_sps:
        mapping = refined
        print(f"  refined mapping kept   (utility {u_ref:.4f} >= SPS {u_sps:.4f})")
    else:
        mapping = sps_mapping
        print(f"  refined mapping REJECTED (utility {u_ref:.4f} < SPS {u_sps:.4f})"
              f" -- falling back to plain SPS")

    # ── Phase 1c: mapping-level local search ─────────────────────────────────
    if MAP_LOCAL_SEARCH:
        print(f"\n{_S}")
        print(f"  PHASE 1c: MAPPING-LEVEL LOCAL SEARCH")
        print(_S2)

        def _eval(m):
            _, _, u, e, ok = _pipeline(m, tasks, processors, B_BUDGET, cum,
                                       N_seg, N_tsk, N_job, job_r, job_d,
                                       freq_set, N_frq, N_prc)
            return u, ok

        mapping, ls = mapping_local_search(
            mapping, _eval, N_prc, max_rounds=MAP_LS_ROUNDS,
            max_moves=MAP_LS_MAX_MOVES, verbose=True)
        print(f"  {ls['moves']} improving reassignment(s) over {ls['rounds']} round(s)"
              f"  -> utility {ls['utility']:.6f}")

    # ── Phases 2-6b on the final mapping ─────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASES 2-6b  (aggressive scaling -> greedy -> swap -> freq trade)")
    print(_S2)
    seg_k, freq_idx, u, e, feas = _pipeline(
        mapping, tasks, processors, B_BUDGET, cum, N_seg, N_tsk, N_job,
        job_r, job_d, freq_set, N_frq, N_prc)
    print(f"  utility={u:.6f}  energy={e:.4f}/{B_BUDGET:.4f}  feasible={feas}")

    tot_e, tot_u = print_schedule(
        seg_k, freq_idx, freq_set, cum, tasks, N_tsk, N_job,
        mapping, B_BUDGET, label="HEURISTIC v6 SOLUTION (FINAL)")
    return seg_k, freq_idx, tot_u, tot_e, mapping
