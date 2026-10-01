"""
Phase 6 — Best-First Pairwise Segment Swap (local search).

Escapes local optima left by greedy Phase 5. Each iteration:

1. SEARCH — evaluate all (giver, receiver) pairs:
     giver   : any job with ≥ 1 optional segment currently active
     receiver: any job with < N_seg optional segments
     With giver's last segment tentatively removed:
       a) net_utility = u_recv * e_recv_next − u_give * e_give_last  > 0
       b) energy: E_freed − E_cost ≤ E_slack (global)
       c) timing: min_slack_for_job(receiver) ≥ add_time_for_receiver

2. EXECUTE the swap with the highest net utility gain.
   Full check_all_timing() for final safety.

3. FILL PASS — re-run Phase 5 (greedy) to capitalise on freed resources.

4. Repeat until no improving swap exists.

Cross-processor swaps: energy is global, so removing a low-utility segment
on P0 can fund a high-utility segment on P1.
"""

from ..models import energy_val, total_energy
from ..dbf.slack import min_slack_for_job, window_slack
from ..dbf.check import check_all_timing
from .greedy import phase_optional_segments


def _first_violation(proc_jobs, job_r, job_d, seg_k, freq_idx, freq_set,
                     cum, N_prc):
    """
    Locate the first infeasible DBF window, as (x, t1, t2, slack).

    `check_all_timing` answers only yes/no.  When the supposedly-unreachable
    revert below fires we need to know WHERE, because that is the whole
    diagnostic value — see SWAP-BREAK in ISSUES.md.
    """
    for x in range(N_prc):
        if not proc_jobs[x]:
            continue
        Ax = sorted({job_r[ij] for ij in proc_jobs[x]})
        Dx = sorted({job_d[ij] for ij in proc_jobs[x]})
        for t1 in Ax:
            for t2 in Dx:
                if t1 >= t2:
                    continue
                sl = window_slack(x, t1, t2, proc_jobs, job_r, job_d,
                                  seg_k, freq_idx, freq_set, cum)
                if sl < -1e-9:
                    return x, t1, t2, sl
    return None


def phase_swap_local_search(seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
                             N_tsk, N_job, proc_jobs, proc_jobs_map,
                             job_r, job_d, tasks, N_prc, B_BUDGET):
    """
    Returns: (n_swaps, final_E_slack, log_entries).
    """
    E_slack = B_BUDGET - total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job)
    log = []; n_swaps = 0; iteration = 0

    # Pairs whose execution failed the final DBF check.  This is NOT optional
    # bookkeeping: the search is deterministic and the revert restores the exact
    # prior state, so skipping a failed pair without remembering it would make
    # the next iteration re-select it forever.  Cleared after every successful
    # swap, because the fill pass changes seg_k and a pair that did not fit
    # before may fit afterwards.
    blacklisted = set()
    violations  = []          # diagnostics for the unreachable path (see below)

    while True:
        iteration += 1
        best = None   # (net_u, i1, j1, k1, i2, j2, k2, dE_freed, dE_cost)

        # ── SEARCH ────────────────────────────────────────────────────────
        for i1 in range(N_tsk):
            for j1 in range(N_job[i1]):
                k1 = seg_k[(i1, j1)]
                if k1 == 0:
                    continue    # giver has no optional segments to remove

                z1      = freq_idx[(i1, j1)]
                f1      = freq_set[z1]
                u_lost  = tasks[i1]['u_i'] * (cum[i1][k1] - cum[i1][k1 - 1])
                dE_freed = (energy_val(cum[i1][k1],     f1) -
                            energy_val(cum[i1][k1 - 1], f1))

                seg_k[(i1, j1)] = k1 - 1   # tentatively remove
                new_E_slack     = E_slack + dE_freed

                for i2 in range(N_tsk):
                    for j2 in range(N_job[i2]):
                        if (i2, j2) == (i1, j1):
                            continue
                        if (i1, j1, i2, j2) in blacklisted:
                            continue    # this pair already failed the DBF check
                        k2 = seg_k[(i2, j2)]
                        if k2 >= N_seg[i2]:
                            continue    # receiver already maxed

                        z2       = freq_idx[(i2, j2)]
                        x2       = proc_jobs_map[(i2, j2)]
                        u_gained = tasks[i2]['u_i'] * (cum[i2][k2 + 1] - cum[i2][k2])
                        net_u    = u_gained - u_lost
                        if net_u <= 1e-9:
                            continue

                        dE_cost = (energy_val(cum[i2][k2 + 1], freq_set[z2]) -
                                   energy_val(cum[i2][k2],     freq_set[z2]))
                        if new_E_slack < dE_cost - 1e-9:
                            continue

                        add_time = (cum[i2][k2 + 1] - cum[i2][k2]) / freq_set[z2]
                        min_sl   = min_slack_for_job(i2, j2, x2, proc_jobs,
                                                     job_r, job_d, seg_k,
                                                     freq_idx, freq_set, cum)
                        if min_sl < add_time - 1e-9:
                            continue

                        if best is None or net_u > best[0]:
                            best = (net_u, i1, j1, k1, i2, j2, k2, dE_freed, dE_cost)

                seg_k[(i1, j1)] = k1   # restore giver

        if best is None:
            break   # no improving swap found

        # ── EXECUTE ────────────────────────────────────────────────────────
        net_u, i1, j1, k1, i2, j2, k2, dE_freed, dE_cost = best
        seg_k[(i1, j1)] = k1 - 1
        seg_k[(i2, j2)] = k2 + 1

        if check_all_timing(proc_jobs, job_r, job_d, seg_k,
                            freq_idx, freq_set, cum, N_prc):
            E_slack  = E_slack + dE_freed - dE_cost
            n_swaps += 1
            blacklisted.clear()        # state moved; earlier failures may now fit
            log.append(
                f"  Swap {n_swaps} (iter {iteration}):"
                f"  remove T{tasks[i1]['id']},j{j1} k:{k1}→{k1-1}"
                f"  |  add T{tasks[i2]['id']},j{j2} k:{k2}→{k2+1}"
                f"  |  +util={net_u:.4f}  E_slack={E_slack:.3f}"
            )

            # ── FILL PASS ──────────────────────────────────────────────────
            _, E_slack, fill_log = phase_optional_segments(
                seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
                N_tsk, N_job, proc_jobs, proc_jobs_map,
                job_r, job_d, tasks, N_prc, B_BUDGET)
            if fill_log:
                log.append(f"    Fill after swap {n_swaps} ({len(fill_log)} addition(s)):")
                log.extend(fill_log)
        else:
            # ── UNREACHABLE BY CONSTRUCTION — see ISSUES.md -> SWAP-BREAK ────
            # Adding a segment to the receiver raises DBF demand in exactly the
            # windows containing its [r, d] interval, and min_slack_for_job
            # scans exactly that set — measured above at :81 with the giver
            # ALREADY tentatively removed, i.e. in the very state that holds
            # here.  The giver only removes work, which can only lower demand.
            # So the pre-check at :84 is exact, not conservative, and this
            # branch cannot be entered.  Measured: 0 firings in 19 committed
            # swaps over 54 instances.
            #
            # If it DOES fire, min_slack_for_job and check_all_timing have
            # disagreed — a state-consistency bug — and the schedule is suspect.
            # The old code logged one line and `break`, silently truncating the
            # whole local search (discarding every remaining ranked candidate
            # AND all later iterations) at the exact moment something was wrong.
            # Now: keep searching so no utility is lost to the diagnostic, and
            # raise once the search is finished so it cannot pass unnoticed —
            # a bare log would be invisible anyway, since adapters._suppress()
            # redirects stdout at the fd level during every sweep.
            seg_k[(i1, j1)] = k1
            seg_k[(i2, j2)] = k2
            where = _first_violation(proc_jobs, job_r, job_d, seg_k, freq_idx,
                                     freq_set, cum, N_prc)
            violations.append(
                f"pair T{tasks[i1]['id']},j{j1} (k {k1}->{k1-1}) -> "
                f"T{tasks[i2]['id']},j{j2} (k {k2}->{k2+1}); "
                f"post-revert first bad window = {where}"
            )
            log.append(
                f"  !! Swap {n_swaps+1} (iter {iteration}): INVARIANT VIOLATION"
                f" — pre-check passed but check_all_timing failed; "
                f"blacklisted and continuing ({violations[-1]})"
            )
            blacklisted.add((i1, j1, i2, j2))
            continue

    if violations:
        raise AssertionError(
            "phase_swap_local_search: the DBF pre-check (min_slack_for_job) and "
            "the full check (check_all_timing) disagreed, which should be "
            "impossible — see ISSUES.md -> SWAP-BREAK for why. "
            f"{len(violations)} occurrence(s): " + " | ".join(violations)
        )

    return n_swaps, E_slack, log
