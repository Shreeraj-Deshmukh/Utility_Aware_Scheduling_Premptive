"""
Phase 5 (left-shift variant) — Greedy optional segment scheduling using
left-shift time proxy for timing estimates.

Unlike greedy.py (DBF window slack), this variant:
  • Uses time_slack[(i,j)] from left_shift() as the timing gate.
  • Recomputes left_shift after every accepted segment addition.
  • Case (ii) steps 1-3 follow heuristicv3 structure.
  • Runs a full dbf_feasible_proc check for safety after each change.

Used by heuristic_v2 (quantum SPS + left-shift greedy).
"""

from collections import defaultdict
from ..models import energy_val
from ..dbf.check import check_dbf_proc
from .left_shift import left_shift_mapping


def phase_optional_segments_leftshift(mapping, tasks, processors, h, B_BUDGET,
                                      seg_state, freq_state, cum, N_seg,
                                      freq_set, N_frq, N_tsk, N_job,
                                      time_slack, E_slack):
    """
    Greedy optional segment scheduling using left-shift time proxy.

    Parameters
    ----------
    mapping      : {(i,j): proc_idx}
    tasks, processors, h : problem parameters
    seg_state    : mutable {(i,j): k}
    freq_state   : mutable {(i,j): z}
    cum, N_seg, freq_set, N_frq, N_tsk, N_job : problem tables
    time_slack   : initial left-shift slack (will be updated in-place on each change)
    E_slack      : initial energy slack (float, updated locally)

    Returns
    -------
    (seg_state, freq_state, E_slack, total_utility, iteration_count)
    """
    f_max_idx = N_frq - 1
    E_SLACK_THRESHOLD = 1.0

    all_jobs_sorted = sorted(
        [(i, j) for i in range(N_tsk) for j in range(N_job[i])],
        key=lambda ij: tasks[ij[0]]['u_i'],
        reverse=True
    )

    iteration           = 0
    total_improvements  = 0

    while True:
        improved_this_pass = 0
        iteration += 1

        for (i_star, j_star) in all_jobs_sorted:
            k_cur = seg_state[(i_star, j_star)]
            z_cur = freq_state[(i_star, j_star)]

            if k_cur >= N_seg[i_star]:
                continue

            x_star    = mapping[(i_star, j_star)]
            extra_exec = tasks[i_star]['e_o_k'][k_cur] / freq_set[z_cur]
            dE_seg     = (energy_val(cum[i_star][k_cur + 1], freq_set[z_cur]) -
                          energy_val(cum[i_star][k_cur],     freq_set[z_cur]))
            added = False

            # ── Case (i) ───────────────────────────────────────────────────
            slack_ok  = time_slack.get((i_star, j_star), 0.0) >= extra_exec - 1e-9
            energy_ok = E_slack >= dE_seg - 1e-9
            if slack_ok and energy_ok:
                seg_state[(i_star, j_star)] = k_cur + 1
                if check_dbf_proc(x_star, mapping, tasks, h,
                                   seg_state, freq_state, cum, freq_set):
                    E_slack    -= dE_seg
                    time_slack  = left_shift_mapping(mapping, tasks, processors, h,
                                                     seg_state, freq_state, cum, freq_set)
                    improved_this_pass += 1
                    added = True
                else:
                    seg_state[(i_star, j_star)] = k_cur

            if added:
                continue

            # ── Case (ii) Step 1: inc freq of j* ──────────────────────────
            if z_cur < f_max_idx:
                z_new    = z_cur + 1
                dE_step1 = (energy_val(cum[i_star][k_cur + 1], freq_set[z_new]) -
                            energy_val(cum[i_star][k_cur],     freq_set[z_cur]))
                if E_slack >= dE_step1 - 1e-9:
                    freq_state[(i_star, j_star)] = z_new
                    seg_state[(i_star, j_star)]  = k_cur + 1
                    if check_dbf_proc(x_star, mapping, tasks, h,
                                      seg_state, freq_state, cum, freq_set):
                        E_slack    -= dE_step1
                        time_slack  = left_shift_mapping(mapping, tasks, processors, h,
                                                         seg_state, freq_state, cum, freq_set)
                        improved_this_pass += 1
                        added = True
                    else:
                        freq_state[(i_star, j_star)] = z_cur
                        seg_state[(i_star, j_star)]  = k_cur

            if added:
                continue

            # ── Case (ii) Step 2: inc freq of other jobs on same proc ─────
            others = sorted(
                [(i, j) for (i, j), px in mapping.items()
                 if px == x_star and (i, j) != (i_star, j_star)
                 and freq_state[(i, j)] < f_max_idx],
                key=lambda ij: tasks[ij[0]]['u_i']
            )
            for (i_o, j_o) in others:
                z_o_cur  = freq_state[(i_o, j_o)]; z_o_new = z_o_cur + 1
                k_o      = seg_state[(i_o, j_o)]
                dE_other = (energy_val(cum[i_o][k_o], freq_set[z_o_new]) -
                            energy_val(cum[i_o][k_o], freq_set[z_o_cur]))
                total_dE = dE_seg + dE_other
                if E_slack >= total_dE - 1e-9:
                    freq_state[(i_o, j_o)]       = z_o_new
                    seg_state[(i_star, j_star)]   = k_cur + 1
                    if check_dbf_proc(x_star, mapping, tasks, h,
                                      seg_state, freq_state, cum, freq_set):
                        E_slack    -= total_dE
                        time_slack  = left_shift_mapping(mapping, tasks, processors, h,
                                                         seg_state, freq_state, cum, freq_set)
                        improved_this_pass += 1
                        added = True
                        break
                    else:
                        freq_state[(i_o, j_o)]      = z_o_cur
                        seg_state[(i_star, j_star)]  = k_cur

            if added:
                continue

            # ── Case (ii) Step 3: dec freq of others (last resort) ─────────
            if E_slack < E_SLACK_THRESHOLD:
                u_star = tasks[i_star]['u_i']
                candidates = sorted(
                    [(i, j) for (i, j), px in mapping.items()
                     if px == x_star and (i, j) != (i_star, j_star)
                     and tasks[i]['u_i'] < u_star
                     and freq_state[(i, j)] > 0
                     and seg_state[(i, j)] > 0],
                    key=lambda ij: tasks[ij[0]]['u_i']
                )
                for (i_o, j_o) in candidates:
                    z_o_cur = freq_state[(i_o, j_o)]; z_o_new = z_o_cur - 1
                    k_o_cur = seg_state[(i_o, j_o)];  k_o_new = k_o_cur - 1
                    dE_other = (energy_val(cum[i_o][k_o_new], freq_set[z_o_new]) -
                                energy_val(cum[i_o][k_o_cur], freq_set[z_o_cur]))
                    total_dE = dE_seg + dE_other
                    if E_slack >= total_dE - 1e-9:
                        freq_state[(i_o, j_o)]      = z_o_new
                        seg_state[(i_o, j_o)]        = k_o_new
                        seg_state[(i_star, j_star)]  = k_cur + 1
                        if check_dbf_proc(x_star, mapping, tasks, h,
                                          seg_state, freq_state, cum, freq_set):
                            E_slack    -= total_dE
                            time_slack  = left_shift_mapping(mapping, tasks, processors, h,
                                                             seg_state, freq_state, cum, freq_set)
                            improved_this_pass += 1
                            added = True
                            break
                        else:
                            freq_state[(i_o, j_o)]      = z_o_cur
                            seg_state[(i_o, j_o)]        = k_o_cur
                            seg_state[(i_star, j_star)]  = k_cur

        total_improvements += improved_this_pass
        if improved_this_pass == 0:
            break

    total_utility = sum(
        tasks[i]['u_i'] * (cum[i][seg_state[(i, j)]] - cum[i][0])
        for i in range(N_tsk) for j in range(N_job[i])
    )
    return seg_state, freq_state, E_slack, total_utility, iteration
