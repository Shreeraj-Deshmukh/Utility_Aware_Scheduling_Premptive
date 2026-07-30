"""
Online-phase demo solver.

Builds an offline schedule with the v5b pipeline (Quantum SPS + Refine 2b +
greedy/swap), then runs the online slack-distribution simulator on top of it.

  python run.py testcase.py online

This is the integration entry point for usrt.online.  It also runs the
worked-example verification first, so a single command proves both that the DP
core matches the design document and that the online phase improves a real
offline schedule while preserving all constraints.
"""

from ..models   import ALPHA, BETA
from ..utils    import (lcm_list, gcd_list, build_cum, build_job_times,
                        build_proc_jobs)
from ..mapping.quantum        import quantum_sps_mapping
from ..mapping.refine_mapping import refine_mapping_2b
from ..output   import print_instance_summary
from ..phases.aggressive   import phase_aggressive_scaling
from ..phases.greedy       import phase_optional_segments
from ..phases.swap         import phase_swap_local_search
from ..online.simulator       import OnlineSimulator, SimConfig
from ..online.worked_examples import verify as verify_worked_examples

_S  = "=" * 76
_S2 = "-" * 76


def offline_schedule(processors, tasks, B_BUDGET):
    """Run the v5b offline pipeline quietly; return (seg_k, freq_idx, mapping)."""
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

    mapping = quantum_sps_mapping(tasks, processors, h, quantum, verbose=False)
    mapping = refine_mapping_2b(mapping, tasks, N_prc, cum, N_seg,
                                job_r, job_d, verbose=False)
    proc_jobs, proc_jobs_map = build_proc_jobs(mapping)

    freq_idx = {(i, j): N_frq - 1 for i in range(N_tsk) for j in range(N_job[i])}
    seg_k    = {(i, j): 0         for i in range(N_tsk) for j in range(N_job[i])}

    phase_aggressive_scaling(seg_k, freq_idx, freq_set, N_frq, cum,
                             N_tsk, N_job, proc_jobs, job_r, job_d, N_prc,
                             B_BUDGET)
    phase_optional_segments(seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
                            N_tsk, N_job, proc_jobs, proc_jobs_map,
                            job_r, job_d, tasks, N_prc, B_BUDGET)
    phase_swap_local_search(seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
                            N_tsk, N_job, proc_jobs, proc_jobs_map,
                            job_r, job_d, tasks, N_prc, B_BUDGET)
    return seg_k, freq_idx, mapping


def run(processors, tasks, B_BUDGET):
    N_tsk   = len(tasks)
    periods = [int(t['p_i']) for t in tasks]
    h       = lcm_list(periods)
    quantum = gcd_list(periods)
    _, N_seg = build_cum(tasks)
    N_job   = [h // periods[i] for i in range(N_tsk)]

    print_instance_summary(processors, tasks, B_BUDGET, h, quantum, N_job, N_seg,
                           ALPHA, BETA, label="USRT Online Phase  —  Instance")

    # 1) DP core vs the design document.
    verify_worked_examples()

    # 2) Offline schedule (the precompute's input).
    print(f"\n{_S}")
    print("  OFFLINE SCHEDULE  (v5b pipeline)")
    print(_S2)
    seg_k, freq_idx, mapping = offline_schedule(processors, tasks, B_BUDGET)
    print("  Offline schedule built (Quantum SPS + Refine 2b + greedy + swap).")

    # 3) Online simulation over a hyper-period of early completions.
    cfg = SimConfig(acet_ratio=0.7, arbitration="proportional", verbose=True)
    sim = OnlineSimulator(processors, tasks, B_BUDGET, seg_k, freq_idx, mapping,
                          config=cfg)
    summary = sim.run()
    return summary
