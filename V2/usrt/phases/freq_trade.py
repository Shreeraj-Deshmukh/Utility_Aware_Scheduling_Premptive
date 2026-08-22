"""
Phase 4b — Frequency/segment trade governed by shadow prices.

The heuristic's structural weakness (measured: 40-58% below the exact optimum
once energy binds) is that it never trades FREQUENCY for OPTIONAL SEGMENTS
globally.  Phase 4 lowers frequency only far enough to reach energy
feasibility, and Phase 5 spends whatever energy happens to be left.  Neither
asks the real question: *is the energy freed by slowing a job down worth more
than the time it costs?*

Economics
---------
There are two scarce resources -- energy (a global budget) and time (per-
processor DBF window slack) -- and frequency is the exchange rate between them.
For a candidate segment of work w on task i at frequency f:

    utility            = u_i * w
    energy cost        = w * g(f),   g(f) = ALPHA/f + BETA*f^2
    time cost          = w / f

so the two marginal rates are conveniently independent of w:

    utility per ENERGY = u_i / g(f)
    utility per TIME   = u_i * f

Shadow prices read off the CURRENT solution (no tuned constants anywhere):

    lambda = max u_i/g(f) over segments blocked ONLY by energy
             ("what one more unit of energy would buy")
    mu     = max u_i*f    over segments blocked ONLY by time
             ("what one more unit of time would buy")

Lowering job j one frequency level frees dE and costs dT, at ZERO direct
utility cost (frequency does not appear in the utility function, paper Eq. 8).
So the move is worth making exactly when

    lambda * dE  >  mu * dT

Safety
------
  * Never crosses f*: candidates require dE > 0, i.e. g strictly decreases.
    Below f* = (ALPHA/2BETA)^(1/3) a downshift costs BOTH energy and time.
  * Every move is DBF-verified (donor window slack first, then a full
    check_all_timing before it is kept).
  * Strict-improvement acceptance with best-so-far restore: the phase can never
    return a worse schedule than it was given.  Worst case is a no-op.
  * Deterministic: fixed tie-breaking, no randomness.
"""

from ..models     import energy_val, e_eff_val, total_energy, total_utility
from ..dbf.slack  import min_slack_for_job
from ..dbf.check  import check_all_timing
from .greedy      import phase_optional_segments

_TOL = 1e-9


def _shadow_prices(seg_k, freq_idx, freq_set, cum, N_seg, N_tsk, N_job,
                   proc_jobs, proc_jobs_map, job_r, job_d, tasks, E_slack):
    """
    (lambda, mu) from the current solution.

    A candidate is the NEXT optional segment of each job.  It contributes to
    lambda only if energy alone blocks it, and to mu only if time alone blocks
    it -- a candidate blocked by both would not be unlocked by either resource
    on its own, so it prices neither.
    """
    lam = mu = 0.0
    for i in range(N_tsk):
        for j in range(N_job[i]):
            k = seg_k[(i, j)]
            if k >= N_seg[i]:
                continue
            f = freq_set[freq_idx[(i, j)]]
            w = cum[i][k + 1] - cum[i][k]
            if w <= _TOL:
                continue
            add_t = w / f
            add_e = (energy_val(cum[i][k + 1], f) - energy_val(cum[i][k], f))
            x     = proc_jobs_map[(i, j)]
            ms    = min_slack_for_job(i, j, x, proc_jobs, job_r, job_d,
                                      seg_k, freq_idx, freq_set, cum)
            time_ok   = ms >= add_t - _TOL
            energy_ok = E_slack >= add_e - _TOL
            if time_ok and not energy_ok:
                lam = max(lam, tasks[i]['u_i'] * w / (add_e + 1e-12))
            elif energy_ok and not time_ok:
                mu = max(mu, tasks[i]['u_i'] * w / (add_t + 1e-12))
    return lam, mu


def phase_freq_utility_trade(seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
                             N_tsk, N_job, proc_jobs, proc_jobs_map,
                             job_r, job_d, tasks, N_prc, B_BUDGET,
                             max_rounds=40):
    """
    Repeatedly: price the two resources, make the single best profitable
    downshift, then re-run Phase 5 to spend the energy it freed.  Stop as soon
    as a round fails to improve total utility.

    Returns (n_moves, final_E_slack, log_entries).
    """
    best_seg  = dict(seg_k)
    best_freq = dict(freq_idx)
    best_u    = total_utility(seg_k, tasks, cum, N_tsk, N_job)
    log, n_moves = [], 0

    for _ in range(max_rounds):
        E_slack = B_BUDGET - total_energy(seg_k, freq_idx, freq_set, cum,
                                          N_tsk, N_job)
        lam, mu = _shadow_prices(seg_k, freq_idx, freq_set, cum, N_seg,
                                 N_tsk, N_job, proc_jobs, proc_jobs_map,
                                 job_r, job_d, tasks, E_slack)
        if lam <= _TOL:
            break                      # nothing is energy-blocked: no trade pays

        # Best downshift by  lambda*dE - mu*dT  (ties broken by index order).
        best_score, cand = _TOL, None
        for i2 in range(N_tsk):
            for j2 in range(N_job[i2]):
                z = freq_idx[(i2, j2)]
                if z == 0:
                    continue
                c2 = cum[i2][seg_k[(i2, j2)]]
                dE = energy_val(c2, freq_set[z]) - energy_val(c2, freq_set[z - 1])
                if dE <= 1e-12:
                    continue           # at/below f*: slowing down costs energy too
                dT = e_eff_val(c2, freq_set[z - 1]) - e_eff_val(c2, freq_set[z])
                score = lam * dE - mu * dT
                if score > best_score:
                    x2 = proc_jobs_map[(i2, j2)]
                    ms = min_slack_for_job(i2, j2, x2, proc_jobs, job_r, job_d,
                                           seg_k, freq_idx, freq_set, cum)
                    if ms >= dT - _TOL:
                        best_score, cand = score, (i2, j2, z)
        if cand is None:
            break

        i2, j2, z = cand
        freq_idx[(i2, j2)] = z - 1
        if not check_all_timing(proc_jobs, job_r, job_d, seg_k, freq_idx,
                                freq_set, cum, N_prc):
            freq_idx[(i2, j2)] = z     # revert; no further move will be safer
            break

        # Spend the energy the downshift just freed.
        phase_optional_segments(seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
                                N_tsk, N_job, proc_jobs, proc_jobs_map,
                                job_r, job_d, tasks, N_prc, B_BUDGET)

        u = total_utility(seg_k, tasks, cum, N_tsk, N_job)
        if u > best_u + _TOL:
            best_u    = u
            best_seg  = dict(seg_k)
            best_freq = dict(freq_idx)
            n_moves  += 1
            log.append(f"    [trade] T{tasks[i2]['id']},j{j2} "
                       f"f:{freq_set[z]:.2f}→{freq_set[z-1]:.2f}  "
                       f"λ={lam:.3f} μ={mu:.3f}  utility={u:.4f}")
        else:
            break                      # no gain: stop and restore below

    # Always finish at the best schedule seen (never worse than the input).
    seg_k.clear();    seg_k.update(best_seg)
    freq_idx.clear(); freq_idx.update(best_freq)
    E_final = B_BUDGET - total_energy(seg_k, freq_idx, freq_set, cum,
                                      N_tsk, N_job)
    return n_moves, E_final, log
