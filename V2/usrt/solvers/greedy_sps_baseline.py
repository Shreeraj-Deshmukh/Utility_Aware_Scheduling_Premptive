"""
greedy_SPS_Baseline — the naive reference point.

Deliberately minimal, so it can serve as the floor that the staged heuristics
must beat:

  * Phase 1 ONLY  : Quantum SPS mapping.  No Refine Mapping (1b), no left-shift,
                    no aggressive scaling, no swap, no iterated greedy.
  * Frequency     : every job pinned at f_max, permanently.  No DVFS in either
                    direction -- this is the whole point of the baseline.
  * Segments      : greedily add optional segments in decreasing utility
                    density, gated by DBF window slack and the remaining energy
                    budget.  One segment per step, highest density first, until
                    nothing else fits.

Utility density here is marginal utility per unit of execution time,
    dens = u_i * w / (w / f_max) = u_i * f_max,
so at a fixed frequency the ranking reduces to the per-unit utility rate u_i --
exactly the "take the most valuable work first" rule a naive implementer would
write.  Ties break on (task, job) index, so the result is deterministic.

Because frequency never moves, this baseline is infeasible whenever the
mandatory workload alone exceeds the budget at f_max.  That is precisely the
regime where the DVFS-capable heuristics earn their keep, and it is the
comparison this baseline exists to make.

Returns (seg_k, freq_idx, total_utility, total_energy) like every other solver.
The returned energy is the TRUE energy even when it exceeds the budget, so the
runner can mark such runs infeasible.
"""

from ..models   import ALPHA, BETA, energy_val, total_energy, total_utility
from ..utils    import (lcm_list, gcd_list, build_cum, build_job_times,
                        build_proc_jobs)
from ..mapping.quantum import quantum_sps_mapping
from ..dbf.slack import min_slack_for_job
from ..output   import print_instance_summary, print_schedule

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
                           ALPHA, BETA, label="greedy_SPS_Baseline  —  Instance")

    # ── Phase 1 only: Quantum SPS mapping ────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 1 : QUANTUM SPS MAPPING  (no refine)")
    print(_S2)
    mapping = quantum_sps_mapping(tasks, processors, h, quantum, verbose=True)
    proc_jobs, proc_jobs_map = build_proc_jobs(mapping)

    # ── Fixed f_max, mandatory only ──────────────────────────────────────────
    z_max    = N_frq - 1
    freq_idx = {(i, j): z_max for i in range(N_tsk) for j in range(N_job[i])}
    seg_k    = {(i, j): 0     for i in range(N_tsk) for j in range(N_job[i])}
    f_max    = freq_set[z_max]

    E_used  = total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job)
    E_slack = B_BUDGET - E_used

    print(f"\n{_S}")
    print(f"  BASELINE GREEDY  (all jobs at f_max={f_max}, no DVFS)")
    print(_S2)
    print(f"  E_mandatory(f_max) = {E_used:.4f}   budget = {B_BUDGET:.4f}   "
          f"slack = {E_slack:.4f}")
    if E_slack < -1e-9:
        print(f"  Mandatory workload exceeds the budget at f_max and this "
              f"baseline cannot scale frequency → infeasible.")
        tot_u = total_utility(seg_k, tasks, cum, N_tsk, N_job)
        return seg_k, freq_idx, tot_u, E_used

    # ── Greedy: highest utility density first ────────────────────────────────
    n_added = 0
    while True:
        cands = []
        for i in range(N_tsk):
            for j in range(N_job[i]):
                k = seg_k[(i, j)]
                if k >= N_seg[i]:
                    continue
                w = cum[i][k + 1] - cum[i][k]
                if w <= 1e-12:
                    continue
                add_t = w / f_max
                add_e = (energy_val(cum[i][k + 1], f_max) -
                         energy_val(cum[i][k], f_max))
                if add_e > E_slack + 1e-9:
                    continue                       # energy blocked
                x  = proc_jobs_map[(i, j)]
                ms = min_slack_for_job(i, j, x, proc_jobs, job_r, job_d,
                                       seg_k, freq_idx, freq_set, cum)
                if ms < add_t - 1e-9:
                    continue                       # timing blocked
                dens = tasks[i]['u_i'] * w / (add_t + 1e-12)
                cands.append((-dens, i, j, add_e))
        if not cands:
            break
        cands.sort()                               # highest density, then index
        _, i, j, add_e = cands[0]
        seg_k[(i, j)] += 1
        E_slack -= add_e
        n_added += 1

    print(f"  {n_added} optional segment(s) added.  E_slack = {E_slack:.4f}")

    tot_e, tot_u = print_schedule(
        seg_k, freq_idx, freq_set, cum, tasks, N_tsk, N_job,
        mapping, B_BUDGET, label="greedy_SPS_Baseline SOLUTION (FINAL)")
    return seg_k, freq_idx, tot_u, tot_e
