"""
heuristic_v2.py
===============
Utility-Aware Energy-Constrained Real-Time Scheduling – Heuristic v2

Pipeline
--------
  Partition  – Worst-Fit Decreasing Utilisation (WFDU)
               Sort tasks by descending mandatory utilisation u = e_m/p.
               Assign each to the valid processor (u_total < 1.0) with the
               LOWEST current utilisation (most headroom = worst fit).
               No cap beyond the hard u < 1.0 per-processor constraint.

  Phase 1    – Feasibility-first mandatory baseline (fastest frequency)
               Schedule mandatory segments (k=0) at the FASTEST frequency.
               Rationale: the non-preemptive EDF simulation advances a clock
               per job. Slow frequencies make early jobs finish late, pushing
               subsequent jobs' start times until some job cannot meet its
               deadline even at f_max (FAILURE_TIME). Using the fastest
               frequency minimises cascading delays and always produces a
               feasible baseline when utilisation < 1.0.

  Phase 2a   – Frequency-reclaim sweep
               For each job, try to lower its frequency one step at a time.
               A reduction is accepted only when BOTH:
                 (i)  every job on that processor still meets its deadline, AND
                 (ii) the job's energy actually decreases at the lower frequency.
               Condition (ii) is critical because the paper's energy model
               E = α(e/f)(βf²+e) has minimum at f_opt = √(e/β).  Any task
               with e_m > β has f_opt > 1.0, so within the normalised
               frequency range [0,1] energy is monotonically DECREASING in f
               — lower frequency = more energy, not less.  The sweep therefore
               only helps tasks whose e_m < β (i.e. very short tasks relative
               to the energy constant), which is uncommon but possible.

  Phase 2b   – Multi-move greedy optional-segment upgrade
               Three move types per job per iteration:
                 INC_K        – add one optional segment, keep frequency
                 INC_F_INC_K  – raise frequency one step + add one segment
                 DEC_F_INC_K  – lower frequency one step + add one segment
               Scored by marginal_utility / marginal_energy (+inf if free).
               Best feasible move applied each iteration until no improvement.
"""

import math
import sys
from testcase import testcase

# ── Terminal colours ───────────────────────────────────────────────────────────
GREEN  = '\033[92m'
RED    = '\033[91m'
YELLOW = '\033[93m'
RESET  = '\033[0m'

# ── Energy-model constants (α, β from the paper) ──────────────────────────────
ALPHA_PARAM = 1.0
BETA_PARAM  = 1.0


# ══════════════════════════════════════════════════════════════════════════════
#  Maths / model helpers
# ══════════════════════════════════════════════════════════════════════════════

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b) if a and b else 0


def hyperperiod(tasks):
    h = 1
    for t in tasks:
        h = lcm(h, t['p_i'])
    return h


def nominal_exec(job, k):
    """Nominal (f_max-normalised) time: mandatory + first k optional segments."""
    return job.e_m_nominal + sum(job.e_o_list_nominal[:k])


def actual_exec(nominal, f):
    """Wall-clock execution time at frequency f."""
    return nominal / f


def energy_cost(nominal, f):
    """
    E = α·(e/f)·(β·f² + e)   per the paper's energy model.

    Note: dE/df = α·e·(β - e/f²), so E is minimised at f_opt = √(e/β).
    For tasks with e > β (common when β=1 and e_m>1), f_opt > 1 = f_max,
    meaning lower frequency always increases energy within the valid range.
    """
    if f <= 0:
        return float('inf')
    return ALPHA_PARAM * (nominal / f) + BETA_PARAM * (f ** 2) * nominal



def utility(job, k):
    """Weighted utility for executing the first k optional segments."""
    if k == 0:
        return 0.0
    return job.u_i * sum(job.e_o_list_nominal[:k])


# ══════════════════════════════════════════════════════════════════════════════
#  Data structures
# ══════════════════════════════════════════════════════════════════════════════

class Job:
    def __init__(self, task_id, task_index, release, deadline,
                 e_m, e_o_list, u_i, p_i):
        self.task_id          = task_id
        self.task_index       = task_index
        self.release          = release
        self.deadline         = deadline
        self.e_m_nominal      = e_m
        self.e_o_list_nominal = e_o_list
        self.u_i              = u_i
        self.p_i              = p_i

    def __repr__(self):
        return f"Job(T{self.task_id}, R:{self.release}, D:{self.deadline})"


def generate_jobs(task, task_index, H):
    """All jobs for one task over the full hyper-period."""
    jobs, p = [], task['p_i']
    for j in range(H // p):
        jobs.append(Job(
            task_id    = task['id'],
            task_index = task_index,
            release    = j * p,
            deadline   = (j + 1) * p,
            e_m        = task['e_m'],
            e_o_list   = task['e_o_k'],
            u_i        = task['u_i'],
            p_i        = p,
        ))
    return jobs


# ══════════════════════════════════════════════════════════════════════════════
#  Partitioning – Worst-Fit Decreasing Utilisation (WFDU)
# ══════════════════════════════════════════════════════════════════════════════

def partition_WFDU(tasks, num_processors):
    """
    Worst-Fit Decreasing Utilisation (WFDU).

    1. Sort tasks by mandatory utilisation u = e_m/p  (decreasing).
    2. For each task assign it to the processor with the LOWEST current
       utilisation whose resulting utilisation stays strictly below 1.0.
       (Lowest current load = most headroom = worst fit.)

    Hard rejection cases:
      (a) u_i >= 1.0  →  unschedulable on any single processor.
      (b) No processor can absorb the task without hitting u >= 1.0.

    No other utilisation cap is applied.

    Returns (tasks_by_proc, True) on success, (None, False) on failure.
    """
    tasks_by_proc = [[] for _ in range(num_processors)]
    proc_util     = [0.0] * num_processors

    annotated = sorted(
        [{'idx': i, 'util': t['e_m'] / t['p_i'], 'task': t}
         for i, t in enumerate(tasks)],
        key=lambda x: x['util'], reverse=True
    )

    print("Partitioning tasks (WFDU, no util cap) ...")

    for td in annotated:
        u    = td['util']
        task = td['task']

        # (a) Task alone exceeds a single processor
        if u >= 1.0 - 1e-9:
            print(f"{RED}  WFDU failed: Task {task['id']} has u={u:.4f} >= 1.0 "
                  f"– unschedulable on any single processor.{RESET}")
            return None, False

        # Worst-fit: pick the valid processor with the LOWEST current util
        best_pid   = -1
        best_u_now = float('inf')

        for pid in range(num_processors):
            new_u = proc_util[pid] + u
            if new_u < 1.0 - 1e-9:               # resulting util stays < 1.0
                if proc_util[pid] < best_u_now:   # least loaded = worst fit
                    best_u_now = proc_util[pid]
                    best_pid   = pid

        # (b) No processor can fit this task
        if best_pid == -1:
            print(f"{RED}  WFDU failed: Task {task['id']} (u={u:.4f}) "
                  f"cannot be placed – all processors too loaded.{RESET}")
            for pid in range(num_processors):
                print(f"    P{pid}  current={proc_util[pid]:.4f}  "
                      f"would-be={proc_util[pid]+u:.4f}")
            return None, False

        proc_util[best_pid] += u
        tasks_by_proc[best_pid].append({
            'task': task, 'original_index': td['idx']
        })

    for pid in range(num_processors):
        ids = [t['task']['id'] for t in tasks_by_proc[pid]]
        print(f"  P{pid}  util={proc_util[pid]:.4f}  tasks={ids}")

    return tasks_by_proc, True


# ══════════════════════════════════════════════════════════════════════════════
#  Schedule-timeline helpers
# ══════════════════════════════════════════════════════════════════════════════

def rebuild_timeline(proc_list):
    """
    Recompute start_time, finish_time, laxity for every job-context.
    proc_list must be in EDF (earliest-deadline) order.
    """
    clock = 0.0
    for jc in proc_list:
        job = jc['job']
        nom = nominal_exec(job, jc['opt_k'])
        jc['start_time']  = max(job.release, clock)
        jc['finish_time'] = jc['start_time'] + actual_exec(nom, jc['frequency'])
        jc['laxity']      = job.deadline - jc['finish_time']
        clock             = jc['finish_time']


def is_feasible(proc_list, from_idx=0):
    """True iff every job at positions >= from_idx has non-negative laxity."""
    return all(jc['laxity'] >= -1e-9 for jc in proc_list[from_idx:])


# ══════════════════════════════════════════════════════════════════════════════
#  Phase 1 – Fastest-frequency mandatory baseline
# ══════════════════════════════════════════════════════════════════════════════

def phase1_fastest_freq(tasks_by_proc, processors, H, B):
    """
    Schedule mandatory segments (k=0) per processor using EDF.

    Each job runs at the FASTEST feasible frequency.

    Why fastest?  The non-preemptive simulation advances a shared clock.
    Choosing the slowest frequency per job greedily looks energy-efficient
    in isolation, but jobs finish much later, cascading delays onto
    subsequent jobs until some job requires a frequency above f_max →
    FAILURE_TIME.  Fastest frequency minimises clock advancement and always
    produces a feasible schedule when per-processor utilisation < 1.0.
    """
    print("\nPhase 1 – fastest-frequency mandatory baseline ...")
    schedule     = []
    total_energy = 0.0

    for pid, proc_tasks in enumerate(tasks_by_proc):
        if not proc_tasks:
            continue

        # Descending order → fastest first
        freqs_desc = sorted(processors[pid]['frequencies'], reverse=True)

        all_jobs = []
        for ti in proc_tasks:
            all_jobs.extend(generate_jobs(ti['task'], ti['original_index'], H))
        all_jobs.sort(key=lambda j: (j.deadline, j.release))

        clock = 0.0

        for job in all_jobs:
            chosen        = None
            time_feasible = False

            for f in freqs_desc:
                start  = max(job.release, clock)
                nom    = nominal_exec(job, 0)
                finish = start + actual_exec(nom, f)

                if finish > job.deadline + 1e-9:
                    continue
                time_feasible = True

                e = energy_cost(nom, f)
                if total_energy + e > B + 1e-9:
                    continue

                chosen = {
                    'job':          job,
                    'processor_id': pid,
                    'frequency':    f,
                    'opt_k':        0,
                    'start_time':   start,
                    'finish_time':  finish,
                    'utility':      0.0,
                    'energy':       e,
                    'laxity':       job.deadline - finish,
                }
                break

            if chosen is None:
                reason = "FAILURE_TIME" if not time_feasible else "FAILURE_ENERGY"
                return None, 0.0, reason

            schedule.append(chosen)
            clock        = chosen['finish_time']
            total_energy += chosen['energy']

    print(f"{GREEN}  Phase 1 OK  –  energy used: {total_energy:.4f} / {B:.4f}{RESET}")
    return schedule, total_energy, "SUCCESS"


# ══════════════════════════════════════════════════════════════════════════════
#  Phase 2a – Frequency-reclaim sweep
# ══════════════════════════════════════════════════════════════════════════════

def phase2a_reclaim(schedule, processors, B, total_energy):
    """
    Attempt to lower each job's frequency to reclaim energy budget.

    A reduction from f_current to f_lower is accepted only when:
      (i)  every job on that processor still meets its deadline, AND
      (ii) the energy at f_lower is strictly less than at f_current.

    Condition (ii) guards against the energy model's non-monotonicity:
    E = α(e/f)(βf²+e) is minimised at f_opt = √(e/β).  For tasks with
    e_m > β (typical when β=1), f_opt > f_max so energy INCREASES as
    frequency drops within the valid range — lowering frequency wastes
    budget instead of saving it.  We only lower when it genuinely helps.
    """
    print("\nPhase 2a – frequency-reclaim sweep ...")

    by_proc = [[] for _ in range(len(processors))]
    for jc in schedule:
        by_proc[jc['processor_id']].append(jc)
    for lst in by_proc:
        lst.sort(key=lambda x: x['start_time'])

    reclaimed = 0.0

    for pid, proc_list in enumerate(by_proc):
        freqs_asc = sorted(processors[pid]['frequencies'])  # ascending

        for jidx, jc in enumerate(proc_list):
            nom = nominal_exec(jc['job'], jc['opt_k'])

            for f_try in freqs_asc:
                if f_try >= jc['frequency']:
                    break   # can't go lower than current – stop

                new_e = energy_cost(nom, f_try)

                # Skip if lowering this frequency would increase energy
                if new_e >= jc['energy'] - 1e-9:
                    continue

                old_f = jc['frequency']
                old_e = jc['energy']

                # Tentative apply
                jc['frequency'] = f_try
                jc['energy']    = new_e
                rebuild_timeline(proc_list)

                if is_feasible(proc_list, jidx):
                    # Accept – energy decreases AND deadlines still met
                    delta         = old_e - new_e
                    reclaimed    += delta
                    total_energy -= delta
                    # Continue trying even lower frequencies
                else:
                    # Revert
                    jc['frequency'] = old_f
                    jc['energy']    = old_e
                    rebuild_timeline(proc_list)
                    break

    if reclaimed > 1e-9:
        print(f"  Energy reclaimed : {reclaimed:.4f}")
        print(f"  Remaining budget : {B - total_energy:.4f}")
    else:
        print(f"  No energy reclaimed (energy model favours f_max for all jobs)")

    return [jc for lst in by_proc for jc in lst], total_energy


# ══════════════════════════════════════════════════════════════════════════════
#  Phase 2b – Multi-move greedy optional-segment upgrade
# ══════════════════════════════════════════════════════════════════════════════

def phase2b_upgrade(schedule, processors, B, total_energy):
    """
    Iteratively apply the highest-scoring feasible upgrade move.

    Move catalogue (each adds exactly one optional segment):
      INC_K        Keep frequency; add one optional segment.
      INC_F_INC_K  Raise frequency one step; add one optional segment.
                   Useful when deadline is tight at current frequency.
      DEC_F_INC_K  Lower frequency one step; add one optional segment.
                   Can be energy-neutral or cheaper when running slower
                   saves more energy than the extra segment costs.

    Score = marginal_utility / marginal_energy.
    Moves with marginal_energy <= 0 score +inf (free utility — always take).

    A move is accepted only when:
      (1) global energy budget is not exceeded, and
      (2) every job on that processor still meets its deadline.
    """
    print("\nPhase 2b – multi-move greedy upgrade ...")

    by_proc = [[] for _ in range(len(processors))]
    for jc in schedule:
        by_proc[jc['processor_id']].append(jc)
    for lst in by_proc:
        lst.sort(key=lambda x: x['start_time'])

    max_k_global = max(
        (len(jc['job'].e_o_list_nominal) for jc in schedule), default=0
    )
    MAX_ITER = len(schedule) * (max_k_global + 1) * 3 + 1

    applied = 0
    for _ in range(MAX_ITER):
        best_move  = None
        best_score = -1.0

        for pid, proc_list in enumerate(by_proc):
            freqs = sorted(processors[pid]['frequencies'])

            for jidx, jc in enumerate(proc_list):
                job   = jc['job']
                cur_k = jc['opt_k']
                max_k = len(job.e_o_list_nominal)

                if cur_k >= max_k:
                    continue

                new_k     = cur_k + 1
                marg_util = utility(job, new_k) - utility(job, cur_k)
                if marg_util <= 1e-9:
                    continue

                f_idx    = freqs.index(jc['frequency'])
                f_higher = freqs[f_idx + 1] if f_idx + 1 < len(freqs) else None
                f_lower  = freqs[f_idx - 1] if f_idx - 1 >= 0          else None

                candidates = [('INC_K', jc['frequency'])]
                if f_higher is not None:
                    candidates.append(('INC_F_INC_K', f_higher))
                if f_lower is not None:
                    candidates.append(('DEC_F_INC_K', f_lower))

                for move_label, f_new in candidates:
                    nom_new = nominal_exec(job, new_k)
                    e_new   = energy_cost(nom_new, f_new)
                    marg_e  = e_new - jc['energy']

                    if total_energy + marg_e > B + 1e-9:
                        continue

                    # Tentative apply → feasibility check → always revert
                    old_f, old_k, old_e = jc['frequency'], jc['opt_k'], jc['energy']
                    jc['frequency'] = f_new
                    jc['opt_k']     = new_k
                    jc['energy']    = e_new
                    rebuild_timeline(proc_list)
                    feasible = is_feasible(proc_list, jidx)
                    jc['frequency'] = old_f
                    jc['opt_k']     = old_k
                    jc['energy']    = old_e
                    rebuild_timeline(proc_list)

                    if not feasible:
                        continue

                    score = float('inf') if marg_e <= 1e-9 else marg_util / marg_e

                    if score > best_score:
                        best_score = score
                        best_move  = {
                            'pid':        pid,
                            'jidx':       jidx,
                            'move_label': move_label,
                            'f_new':      f_new,
                            'k_new':      new_k,
                            'marg_e':     marg_e,
                            'marg_util':  marg_util,
                        }

        if best_move is None:
            break  # converged – no improving move exists

        # Commit winning move
        pid, jidx = best_move['pid'], best_move['jidx']
        jc = by_proc[pid][jidx]
        jc['frequency'] = best_move['f_new']
        jc['opt_k']     = best_move['k_new']
        jc['utility']   = utility(jc['job'], best_move['k_new'])
        jc['energy']    = energy_cost(
            nominal_exec(jc['job'], best_move['k_new']), best_move['f_new']
        )
        total_energy += best_move['marg_e']
        rebuild_timeline(by_proc[pid])
        applied += 1

    print(f"  Applied {applied} upgrade(s).")
    return [jc for lst in by_proc for jc in lst], total_energy


# ══════════════════════════════════════════════════════════════════════════════
#  Output
# ══════════════════════════════════════════════════════════════════════════════

def print_schedule(schedule, total_energy, total_utility, B, processors):
    by_proc = {}
    for jc in schedule:
        by_proc.setdefault(jc['processor_id'], []).append(jc)
    for lst in by_proc.values():
        lst.sort(key=lambda x: x['start_time'])

    with open("output_heuristic.txt", "w") as fh:
        fh.write("=" * 65 + "\n")
        fh.write("  USRT HEURISTIC v2\n")
        fh.write("  WFDU | Fastest-Freq Baseline | "
                 "Freq Reclaim | Multi-Move Upgrade\n")
        fh.write("=" * 65 + "\n\n")
        fh.write(f"Total Utility : {total_utility:.4f}\n")
        fh.write(f"Total Energy  : {total_energy:.4f} / {B:.4f}  "
                 f"({100.0 * total_energy / B:.1f}% used)\n\n")

        for pid in sorted(by_proc):
            lst = by_proc[pid]
            fh.write(f"Processor {pid}  ({len(lst)} jobs):\n")
            hdr = (f"{'Job':<12} {'k':<3} {'f':<6} "
                   f"{'Start':<10} {'Finish':<10} "
                   f"{'Util':<10} {'Energy':<10} {'Laxity':<8}\n")
            fh.write(hdr)
            fh.write("-" * len(hdr) + "\n")
            for jc in lst:
                j = jc['job']
                fh.write(
                    f"T{j.task_id}.J{j.release // j.p_i:<6}"
                    f"{jc['opt_k']:<3} {jc['frequency']:<6.2f}"
                    f"{jc['start_time']:<10.2f}{jc['finish_time']:<10.2f}"
                    f"{jc['utility']:<10.4f}{jc['energy']:<10.4f}"
                    f"{jc['laxity']:<8.4f}\n"
                )
            fh.write("\n")

    print(f"\n{GREEN}Total Utility : {total_utility:.4f}{RESET}")
    print(f"Total Energy  : {total_energy:.4f} / {B:.4f}  "
          f"({100.0 * total_energy / B:.1f}% used)")
    print(f"{GREEN}All {len(schedule)} jobs scheduled successfully.{RESET}")
    print(f"\n{GREEN}Full schedule saved to 'output_heuristic.txt'{RESET}")


# ══════════════════════════════════════════════════════════════════════════════
#  Entry point
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    try:
        processors, TASKS, B_BUDGET = testcase()
        H = hyperperiod(TASKS)

        if H > 2000:
            print(f"{YELLOW}Warning: hyperperiod H={H} is large – "
                  f"runtime may be significant.{RESET}")

        # ── Partitioning ───────────────────────────────────────────────────────
        tasks_by_proc, ok = partition_WFDU(TASKS, len(processors))
        if not ok:
            print(f"\n{RED}WFDU partitioning failed – see diagnostics above.{RESET}")
            sys.exit(1)

        # ── Phase 1 ────────────────────────────────────────────────────────────
        schedule, base_e, status = phase1_fastest_freq(
            tasks_by_proc, processors, H, B_BUDGET
        )
        if status != "SUCCESS":
            msg = {
                "FAILURE_TIME":   "tasks not schedulable (time).",
                "FAILURE_ENERGY": "energy budget too tight for mandatory segments.",
            }.get(status, status)
            print(f"\n{RED}Phase 1 failed – {msg}{RESET}")
            sys.exit(1)

        # ── Phase 2a ───────────────────────────────────────────────────────────
        schedule, base_e = phase2a_reclaim(
            schedule, processors, B_BUDGET, base_e
        )

        # ── Phase 2b ───────────────────────────────────────────────────────────
        schedule, final_e = phase2b_upgrade(
            schedule, processors, B_BUDGET, base_e
        )

        total_util = sum(jc['utility'] for jc in schedule)
        print_schedule(schedule, final_e, total_util, B_BUDGET, processors)

    except Exception as exc:
        print(f"{RED}Error: {exc}{RESET}")
        import traceback; traceback.print_exc()