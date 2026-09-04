"""
Multi-start mapping selection + guided repair.

The measured cost breakdown for Phase 1c was:
    Phase 1        0.20 ms
    one pipeline   1.11 ms
    Phase 1c      30.91 ms   (~25 pipelines)
and Phase 1c examines only J*(P-1) single-job moves -- FEWER candidates than
Phase 1b considers.  So its expense is the SCORING, not the search.  Two
consequences drive this module:

  1. MULTI-START beats local search per unit cost.  Five structurally different
     mappings (SPS, SPS+refine, budget-refine, WFD, FFD, BFD, donor/harvester)
     cost five pipelines and explore far more than twenty-five single-job moves
     away from one basin.

  2. GUIDED REPAIR beats blind moves.  After Phase 5 converges we can ask WHY a
     processor still has unscheduled optional work.  If it is TIME-bound, moving
     a low-value job off it may help.  If it is ENERGY-bound, no mapping change
     can help at all, because energy is a global budget -- and blind local
     search wastes most of its evaluations on exactly those processors.

Both are scored on the REAL objective (the utility the full pipeline achieves),
and both keep a best-so-far, so neither can return something worse than its
input.
"""

from ..models    import energy_val
from ..dbf.slack import min_slack_for_job

_TOL = 1e-9


def multi_start(candidates, evaluate, verbose=False):
    """
    Score each (name, mapping) with one full pipeline; return the best.

    `evaluate(mapping) -> (utility, feasible)`.  Infeasible candidates are
    discarded.  Returns (best_name, best_mapping, utility, log_lines).
    """
    best_name, best_map, best_u = None, None, float('-inf')
    log = []
    for name, mp in candidates:
        u, ok = evaluate(mp)
        log.append(f"    {name:<14} utility={u:10.4f}  {'' if ok else '(infeasible)'}")
        if ok and u > best_u + _TOL:
            best_name, best_map, best_u = name, mp, u
    if best_map is None:                      # nothing feasible: keep the first
        best_name, best_map = candidates[0]
        best_u = float('-inf')
    return best_name, dict(best_map), best_u, log


def diagnose_blocked(seg_k, freq_idx, freq_set, cum, N_seg, N_tsk, N_job,
                     proc_jobs, proc_jobs_map, job_r, job_d, tasks, E_slack):
    """
    For each processor, how much optional utility is still unscheduled, and WHY.

    Returns {proc: dict(blocked_utility, time_blocked, energy_blocked)} where the
    two counters are the utility blocked by each cause.  A candidate segment is
    attributed to TIME when its window slack is short, to ENERGY when the global
    pool cannot pay for it.
    """
    info = {x: dict(blocked=0.0, time=0.0, energy=0.0) for x in proc_jobs}
    for i in range(N_tsk):
        for j in range(N_job[i]):
            k = seg_k[(i, j)]
            if k >= N_seg[i]:
                continue
            x = proc_jobs_map[(i, j)]
            f = freq_set[freq_idx[(i, j)]]
            w = cum[i][k + 1] - cum[i][k]
            if w <= _TOL:
                continue
            gain  = tasks[i]['u_i'] * w
            add_t = w / f
            add_e = energy_val(cum[i][k + 1], f) - energy_val(cum[i][k], f)
            ms = min_slack_for_job(i, j, x, proc_jobs, job_r, job_d,
                                   seg_k, freq_idx, freq_set, cum)
            time_short   = ms < add_t - _TOL
            energy_short = E_slack < add_e - _TOL
            if not (time_short or energy_short):
                continue
            info[x]['blocked'] += gain
            if time_short:
                info[x]['time'] += gain
            if energy_short:
                info[x]['energy'] += gain
    return info


def guided_repair(mapping, evaluate, diagnose, tasks, cum, N_seg, N_prc,
                  max_moves=4, verbose=False):
    """
    Diagnose, then make ONE informed move at a time.

    `diagnose(mapping) -> (info, utility, feasible)` where `info` is the dict
    from diagnose_blocked.  The processor with the most TIME-blocked utility is
    the target; its lowest-utility-density job is moved to the processor with
    the least time-blocked utility.  Energy-blocked processors are skipped
    outright -- no reassignment can create global energy.

    Keeps the incumbent unless a move strictly improves, so it cannot regress.
    """
    best_map = dict(mapping)
    info, best_u, ok = diagnose(best_map)
    if not ok:
        return best_map, best_u, []
    log, moves = [], 0

    for _ in range(max_moves):
        # target: most TIME-blocked processor (energy-blocked ones are hopeless)
        cand = [(v['time'], x) for x, v in info.items() if v['time'] > _TOL]
        if not cand:
            log.append("    nothing time-blocked -- mapping cannot help further")
            break
        cand.sort(key=lambda t: (-t[0], t[1]))
        src = cand[0][1]
        dst_pool = sorted(info.keys(), key=lambda x: (info[x]['time'], x))
        dst = next((x for x in dst_pool if x != src), None)
        if dst is None:
            break

        # move the LOWEST utility-density job off the congested processor
        jobs_here = [ij for ij, x in best_map.items() if x == src]
        if not jobs_here:
            break
        def ud(ij):
            i = ij[0]
            return tasks[i]['u_i'] * (cum[i][N_seg[i]] - cum[i][0]) / tasks[i]['p_i']
        jobs_here.sort(key=lambda ij: (ud(ij), ij))
        moved = False
        for ij in jobs_here[:3]:              # try the 3 least valuable
            trial = dict(best_map)
            trial[ij] = dst
            t_info, u, feas = diagnose(trial)
            if feas and u > best_u + _TOL:
                best_map, best_u, info = trial, u, t_info
                moves += 1
                moved = True
                log.append(f"    moved T{tasks[ij[0]]['id']},j{ij[1]}  "
                           f"P{src} -> P{dst}   utility={u:.4f}")
                break
        if not moved:
            log.append("    no improving move from the congested processor")
            break
    return best_map, best_u, log
