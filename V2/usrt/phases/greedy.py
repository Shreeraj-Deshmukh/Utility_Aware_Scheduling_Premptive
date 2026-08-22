"""
Phase 5 — Greedy optional segment scheduling (DBF window-slack variant).

One segment per j* per outer pass; outer loop repeats to convergence.

Timing gate : min_slack_for_job (DBF window slack — sufficient for Case i,
              no extra DBF call needed).
Sort        : stable by (-u_i, task_id, job_id).

Cases:
  (i)   — add segment without impacting others
           min_slack ≥ add_time  AND  E_slack ≥ add_energy  → commit
  (ii.A)— increase freq of j* (saves exec time + energy in default model)
           pre-check + full check_all_timing for safety
  (ii.B)— decrease freq of other jobs on same proc (to save their energy)
           only if energy_saved > 0; check their timing; full check_all_timing

Used by heuristic_v3 (phases 1-5) and heuristic_v4 (phases 1-6).
"""

from ..models import energy_val, e_eff_val, total_energy
from ..dbf.slack import min_slack_for_job
from ..dbf.check import check_all_timing


def phase_optional_segments(seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
                             N_tsk, N_job, proc_jobs, proc_jobs_map,
                             job_r, job_d, tasks, N_prc, B_BUDGET):
    """
    Returns: (n_passes, final_E_slack, log_entries).
    """
    E_slack = B_BUDGET - total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job)

    sorted_jobs = sorted(
        [(i, j) for i in range(N_tsk) for j in range(N_job[i])],
        key=lambda ij: (-tasks[ij[0]]['u_i'], ij[0], ij[1])
    )

    log = []; pass_num = 0

    while True:
        pass_num += 1; improved = False

        for (i_s, j_s) in sorted_jobs:
            k_cur = seg_k[(i_s, j_s)]
            if k_cur >= N_seg[i_s]:
                continue

            z_cur = freq_idx[(i_s, j_s)]
            f_cur = freq_set[z_cur]
            x_s   = proc_jobs_map[(i_s, j_s)]

            add_time   = (cum[i_s][k_cur + 1] - cum[i_s][k_cur]) / f_cur
            add_energy = (energy_val(cum[i_s][k_cur + 1], f_cur) -
                          energy_val(cum[i_s][k_cur], f_cur))

            min_sl = min_slack_for_job(i_s, j_s, x_s, proc_jobs, job_r, job_d,
                                       seg_k, freq_idx, freq_set, cum)

            # ── Case (i) ────────────────────────────────────────────────────
            if min_sl >= add_time - 1e-9 and E_slack >= add_energy - 1e-9:
                seg_k[(i_s, j_s)] = k_cur + 1
                E_slack -= add_energy
                improved = True
                log.append(f"    [i]  T{tasks[i_s]['id']},j{j_s}"
                            f"  k:{k_cur}→{k_cur+1}  E_slack={E_slack:.3f}")
                continue

            added = False

            # ── Case (ii.A) ─────────────────────────────────────────────────
            if z_cur < N_frq - 1:
                z_t = z_cur + 1; f_t = freq_set[z_t]
                dt  = e_eff_val(cum[i_s][k_cur + 1], f_t) - e_eff_val(cum[i_s][k_cur], f_cur)
                de  = energy_val(cum[i_s][k_cur + 1], f_t) - energy_val(cum[i_s][k_cur], f_cur)
                if min_sl - dt >= -1e-9 and E_slack - de >= -1e-9:
                    freq_idx[(i_s, j_s)] = z_t
                    seg_k[(i_s, j_s)]    = k_cur + 1
                    if check_all_timing(proc_jobs, job_r, job_d, seg_k,
                                        freq_idx, freq_set, cum, N_prc):
                        E_slack -= de; improved = True; added = True
                        log.append(f"    [ii.A]  T{tasks[i_s]['id']},j{j_s}"
                                   f"  k:{k_cur}→{k_cur+1} z:{z_cur}→{z_t}"
                                   f"  E_slack={E_slack:.3f}")
                    else:
                        freq_idx[(i_s, j_s)] = z_cur
                        seg_k[(i_s, j_s)]    = k_cur

            # ── Case (ii.B) — GLOBAL energy donation ────────────────────────
            # Energy is a GLOBAL budget, so a donor on ANY processor can fund
            # this segment; restricting donors to x_s was an artificial limit.
            # Lowering a donor's frequency also costs it ZERO utility (frequency
            # does not appear in the utility function, paper Eq. 8), so the old
            # "donor must have u_i <= u_j*" rule guarded against a cost that does
            # not exist.  Donors are therefore ranked purely by how cheaply they
            # yield energy (time paid per unit energy freed), and SEVERAL may
            # contribute until the segment becomes affordable.
            #
            # ii.B only helps when ENERGY is the blocker: donating energy cannot
            # fix a timing shortfall for j* (and donors on j*'s own processor
            # make its timing worse, which the final DBF check catches).
            if not added and min_sl >= add_time - 1e-9 and E_slack < add_energy - 1e-9:
                need  = add_energy - E_slack
                cands = []
                for i2 in range(N_tsk):
                    for j2 in range(N_job[i2]):
                        if (i2, j2) == (i_s, j_s):
                            continue
                        z2c = freq_idx[(i2, j2)]
                        if z2c == 0:
                            continue
                        c2 = cum[i2][seg_k[(i2, j2)]]
                        es = (energy_val(c2, freq_set[z2c]) -
                              energy_val(c2, freq_set[z2c - 1]))
                        if es <= 1e-12:
                            continue          # at/below f*: slowing costs energy too
                        tc = (e_eff_val(c2, freq_set[z2c - 1]) -
                              e_eff_val(c2, freq_set[z2c]))
                        cands.append((tc / (es + 1e-12), i2, j2))
                cands.sort()                  # cheapest time-per-energy first

                applied, gained = [], 0.0
                for (_, i2, j2) in cands:
                    if gained >= need - 1e-9:
                        break
                    z2c = freq_idx[(i2, j2)]
                    if z2c == 0:
                        continue
                    c2 = cum[i2][seg_k[(i2, j2)]]
                    es = (energy_val(c2, freq_set[z2c]) -
                          energy_val(c2, freq_set[z2c - 1]))
                    if es <= 1e-12:
                        continue
                    tc = (e_eff_val(c2, freq_set[z2c - 1]) -
                          e_eff_val(c2, freq_set[z2c]))
                    x2  = proc_jobs_map[(i2, j2)]
                    ms2 = min_slack_for_job(i2, j2, x2, proc_jobs, job_r, job_d,
                                            seg_k, freq_idx, freq_set, cum)
                    if ms2 < tc - 1e-9:
                        continue
                    freq_idx[(i2, j2)] = z2c - 1
                    applied.append((i2, j2))
                    gained += es

                if applied and gained >= need - 1e-9:
                    seg_k[(i_s, j_s)] = k_cur + 1
                    if check_all_timing(proc_jobs, job_r, job_d, seg_k,
                                        freq_idx, freq_set, cum, N_prc):
                        E_slack = E_slack + gained - add_energy
                        improved = True; added = True
                        log.append(f"    [ii.B]  T{tasks[i_s]['id']},j{j_s}"
                                   f"  k:{k_cur}\u2192{k_cur+1}"
                                   f"  via {len(applied)} donor(s)"
                                   f"  E_slack={E_slack:.3f}")
                    else:
                        seg_k[(i_s, j_s)] = k_cur
                        for (i2, j2) in applied:
                            freq_idx[(i2, j2)] += 1
                else:
                    for (i2, j2) in applied:
                        freq_idx[(i2, j2)] += 1

        if not improved:
            break

    return pass_num, E_slack, log
