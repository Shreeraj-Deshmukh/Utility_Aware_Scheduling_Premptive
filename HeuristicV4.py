import math
import sys
from testcase import testcase

# ── colours ───────────────────────────────────────────────────────────────────
GREEN  = '\033[92m'
RED    = '\033[91m'
YELLOW = '\033[93m'
RESET  = '\033[0m'

# ── energy model constants ────────────────────────────────────────────────────
ALPHA = 1.0
BETA  = 1.0

# ── DBF safety margin ─────────────────────────────────────────────────────────
EPSILON = 1e-4


# ══════════════════════════════════════════════════════════════════════════════
#  Model helper functions
# ══════════════════════════════════════════════════════════════════════════════

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b) if a and b else 0

def hyperperiod(tasks):
    h = 1
    for t in tasks:
        h = lcm(h, t['p_i'])
    return h

def nominal(e_m, e_o_list, k):
    """Nominal execution time (at f_max) for mandatory + first k optional segs."""
    return e_m + sum(e_o_list[:k])

def energy(nom, f):
    return ALPHA * (nom / f) + BETA * (f**2) * nom

def exec_time(nom, f):
    return nom / f


# ══════════════════════════════════════════════════════════════════════════════
#  Job data structure
# ══════════════════════════════════════════════════════════════════════════════

class Job:
    __slots__ = ('task_id', 'task_idx', 'job_idx',
                 'release', 'deadline', 'period',
                 'e_m', 'e_o_list', 'u_i',
                 'f', 'k')

    def __init__(self, task_id, task_idx, job_idx,
                 release, deadline, period,
                 e_m, e_o_list, u_i, f_init):
        self.task_id   = task_id
        self.task_idx  = task_idx
        self.job_idx   = job_idx
        self.release   = release
        self.deadline  = deadline
        self.period    = period
        self.e_m       = e_m
        self.e_o_list  = e_o_list
        self.u_i       = u_i
        self.f         = f_init
        self.k         = 0

    # ── derived quantities ────────────────────────────────────────────────────
    def nom(self):
        return nominal(self.e_m, self.e_o_list, self.k)

    def exec_t(self):
        return exec_time(self.nom(), self.f)

    def energy(self):
        return energy(self.nom(), self.f)

    def utility(self):
        if self.k == 0:
            return 0.0
        return self.u_i * sum(self.e_o_list[:self.k])

    def __repr__(self):
        return (f"Job(T{self.task_id}.J{self.job_idx} "
                f"r={self.release} d={self.deadline} "
                f"f={self.f:.2f} k={self.k})")


def make_jobs(task, task_idx, H, f_init):
    jobs, p = [], task['p_i']
    for j in range(H // p):
        jobs.append(Job(
            task_id  = task['id'],
            task_idx = task_idx,
            job_idx  = j,
            release  = j * p,
            deadline = (j + 1) * p,
            period   = p,
            e_m      = task['e_m'],
            e_o_list = task['e_o_k'],
            u_i      = task['u_i'],
            f_init   = f_init,
        ))
    return jobs

# ══════════════════════════════════════════════════════════════════════════════
#  DBF helpers
# ══════════════════════════════════════════════════════════════════════════════

def make_checkpoints(jobs_on_proc, H):
    pts = sorted(set(j.deadline for j in jobs_on_proc if 0 < j.deadline <= H))
    return pts


def dbf_at(t, jobs_on_proc):

    return sum(j.exec_t() for j in jobs_on_proc if j.deadline <= t)


def dbf_feasible(jobs_on_proc, checkpoints, from_deadline=0.0):
    for t in checkpoints:
        if t < from_deadline - 1e-9:
            continue
        if dbf_at(t, jobs_on_proc) > (1.0 - EPSILON) * t:
            return False
    return True


# ══════════════════════════════════════════════════════════════════════════════
#  WFDU Partition  PHASE 1 — f_max baseline 
# ══════════════════════════════════════════════════════════════════════════════

def partition_WFDU(tasks, processors, H):

    num_proc      = len(processors)
    tasks_by_proc = [[] for _ in range(num_proc)]
    proc_util     = [0.0] * num_proc

    annotated = sorted(
        [{'idx': i, 'u': t['e_m'] / t['p_i'], 'task': t}
         for i, t in enumerate(tasks)],
        key=lambda x: x['u'], reverse=True
    )

    print("WFDU partitioning ...")
    for td in annotated:
        u, task = td['u'], td['task']

        if u >= 1.0 - 1e-9:
            print(f"{RED}  Task {task['id']} u={u:.4f} >= 1.0 – unschedulable.{RESET}")
            return None, None, False

        # worst fit: pick least-loaded valid processor
        best_pid, best_u = -1, float('inf')
        for pid in range(num_proc):
            new_u = proc_util[pid] + u
            if new_u < 1.0 - 1e-9 and proc_util[pid] < best_u:
                best_u   = proc_util[pid]
                best_pid = pid

        if best_pid == -1:
            print(f"{RED}  Task {task['id']} (u={u:.4f}) cannot be placed.{RESET}")
            return None, None, False

        proc_util[best_pid] += u
        tasks_by_proc[best_pid].append({'task': task, 'idx': td['idx']})

    # Build jobs at f_max for DBF verification
    f_max_by_proc = [max(p['frequencies']) for p in processors]
    jobs_by_proc  = []

    for pid in range(num_proc):
        jobs = []
        for ti in tasks_by_proc[pid]:
            jobs.extend(make_jobs(ti['task'], ti['idx'], H,
                                  f_init=f_max_by_proc[pid]))
        jobs_by_proc.append(jobs)

    # DBF check at f_max, k=0
    for pid in range(num_proc):
        cps = make_checkpoints(jobs_by_proc[pid], H)
        if not dbf_feasible(jobs_by_proc[pid], cps):
            print(f"{RED}  DBF check failed at f_max on P{pid} – "
                  f"partition infeasible.{RESET}")
            return None, None, False

    for pid in range(num_proc):
        ids = [t['task']['id'] for t in tasks_by_proc[pid]]
        print(f"  P{pid}  u_mand={proc_util[pid]:.4f}  tasks={ids}")
    print(f"{GREEN}  Partition + DBF OK{RESET}")

    return tasks_by_proc, jobs_by_proc, True


# ══════════════════════════════════════════════════════════════════════════════
#  Phase 1 — Assign f_max to all jobs
# ══════════════════════════════════════════════════════════════════════════════

def phase1(jobs_by_proc, processors, H):

    print("\nPhase 1 – assigning f_max to all jobs ...")
    total_energy = 0.0

    for pid, jobs in enumerate(jobs_by_proc):
        f_max = max(processors[pid]['frequencies'])
        for job in jobs:
            job.f = f_max
            job.k = 0
            total_energy += job.energy()

    print(f"{GREEN}  Phase 1 OK  –  energy used: {total_energy:.4f}{RESET}")
    return total_energy


# ══════════════════════════════════════════════════════════════════════════════
#  Phase 2 — greedy upgrade
# ══════════════════════════════════════════════════════════════════════════════

def compute_score(d_util, d_e, d_t, lam):

    if d_util <= 1e-8:
        return -1.0          # no utility gain at all — skip

    cost_e = lam * d_e
    cost_t = (1.0 - lam) * d_t
    denom  = cost_e + cost_t

    if denom <= 1e-12:
        return float('inf')  # free or net-saving move

    return d_util/denom


def phase2(jobs_by_proc, processors, H, B, total_energy):

    print("\nPhase 2 – bang-for-buck greedy upgrade ...")

    # Pre-compute checkpoints per processor
    cps_by_proc = [make_checkpoints(jobs, H) for jobs in jobs_by_proc]

    # Frequency lists per processor
    freqs_by_proc = [sorted(p['frequencies']) for p in processors]

    applied = 0
    MAX_ITER = sum(
        len(j.e_o_list) * 3
        for jobs in jobs_by_proc for j in jobs
    ) + 1

    for iteration in range(MAX_ITER):
        lam        = total_energy / B
        best_move  = None
        best_score = -1.0

        for pid, jobs in enumerate(jobs_by_proc):
            freqs = freqs_by_proc[pid]
            cps   = cps_by_proc[pid]

            for job in jobs:
                cur_k  = job.k
                max_k  = len(job.e_o_list)

                if cur_k >= max_k:
                    continue   # no optional segments left

                # ── build candidate moves ─────────────────────────────────
                f_idx    = freqs.index(job.f)
                f_same   = job.f
                f_higher = freqs[f_idx + 1] if f_idx + 1 < len(freqs) else None
                f_lower  = freqs[f_idx - 1] if f_idx - 1 >= 0          else None

                candidates = [('INC_K', f_same)]
                if f_higher is not None:
                    candidates.append(('INC_F_INC_K', f_higher))
                if f_lower is not None:
                    candidates.append(('DEC_F_INC_K', f_lower))

                nom_old  = nominal(job.e_m, job.e_o_list, cur_k)
                nom_new  = nominal(job.e_m, job.e_o_list, cur_k + 1)
                e_old    = energy(nom_old, job.f)
                d_util   = job.u_i * job.e_o_list[cur_k]  # marginal utility

                for move_label, f_new in candidates:
                    e_new = energy(nom_new, f_new)
                    d_e   = e_new - e_old          # energy delta for this job
                    d_t   = exec_time(nom_new, f_new) - exec_time(nom_old, job.f)

                    # ── Gate 1: global energy budget ──────────────────────
                    if total_energy + d_e > B + 1e-9:
                        continue

                    # ── Gate 2: incremental DBF ───────────────────────────
                    old_f, old_k = job.f, job.k
                    job.f = f_new
                    job.k = cur_k + 1
                    feasible = dbf_feasible(jobs, cps,
                                            from_deadline=job.deadline)
                    job.f = old_f
                    job.k = old_k

                    if not feasible:
                        continue

                    # ── Score ─────────────────────────────────────────────
                    score = compute_score(d_util, d_e, d_t, lam)
                    if score < 0:
                        continue

                    # Tie-break: higher ΔUtility first, then lower ΔE
                    if (score > best_score or
                        (abs(score - best_score) < 1e-12 and
                         (best_move is None or
                          d_util > best_move['d_util'] or
                          (abs(d_util - best_move['d_util']) < 1e-12
                           and d_e < best_move['d_e'])))):
                        best_score = score
                        best_move  = {
                            'pid':   pid,
                            'job':   job,
                            'f_new': f_new,
                            'k_new': cur_k + 1,
                            'd_e':   d_e,
                            'd_util': d_util,
                            'label': move_label,
                        }

        if best_move is None:
            print(f"  Converged after {applied} upgrade(s).")
            break

        # ── Commit winning move ───────────────────────────────────────────
        bm          = best_move
        bm['job'].f = bm['f_new']
        bm['job'].k = bm['k_new']
        total_energy += bm['d_e']
        applied      += 1

    else:
        print(f"  Reached MAX_ITER ({MAX_ITER}). Applied {applied} upgrade(s).")

    return total_energy


# ══════════════════════════════════════════════════════════════════════════════
#  Output
# ══════════════════════════════════════════════════════════════════════════════

def print_schedule(jobs_by_proc, total_energy, B, H):
    total_utility = sum(j.utility() for jobs in jobs_by_proc for j in jobs)

    W   = 85
    HDR = (f"  {'Job':<14} {'k':<4} {'f':<6} "
           f"{'ExecTime':<10} {'Energy':<12} {'Utility':<10} "
           f"{'Release':<9} {'Deadline':<9}\n")
    SEP = "  " + "-" * (len(HDR) - 3) + "\n"

    def write_block(out):
        out("=" * W + "\n")
        out("  USRT HEURISTIC v4  -  Preemptive EDF | Per-job f & k\n")
        out("  WFDU | Phase1: f_max baseline | Phase2: bang-for-buck\n")
        out("=" * W + "\n\n")
        out(f"  Total Utility : {total_utility:.4f}\n")
        out(f"  Total Energy  : {total_energy:.4f} / {B:.4f}  "
            f"({100.0 * total_energy / B:.1f}% used)\n")
        out(f"  Hyper-period  : {H}\n")

        # ── per-processor utilisation summary ─────────────────────────────
        # jobs list already contains every job instance across H, so:
        #   U = sum(exec_t per instance) / H
        out(f"\n  Processor Utilisation Summary\n")
        out(f"  {'Proc':<8} {'U_mand':<12} {'U_total':<12} {'U_used%':<10} "
            f"{'Energy':<12} {'Utility':<10}\n")
        out("  " + "-" * 60 + "\n")
        for pid, jobs in enumerate(jobs_by_proc):
            u_mand  = sum(j.e_m      / j.f for j in jobs) / H
            u_total = sum(j.exec_t()       for j in jobs) / H
            p_e     = sum(j.energy()  for j in jobs)
            p_u     = sum(j.utility() for j in jobs)
            out(f"  P{pid:<7} {u_mand:<12.4f} {u_total:<12.4f} "
                f"{100.0*u_total:<10.2f} {p_e:<12.4f} {p_u:.4f}\n")

        # ── per-processor job detail ───────────────────────────────────────
        for pid, jobs in enumerate(jobs_by_proc):
            proc_energy  = sum(j.energy()  for j in jobs)
            proc_utility = sum(j.utility() for j in jobs)
            u_total      = sum(j.exec_t() for j in jobs) / H

            out(f"\n{'-'*W}\n")
            out(f"  Processor {pid}   jobs={len(jobs)}   "
                f"U_total={u_total:.4f}   "
                f"energy={proc_energy:.4f}   "
                f"utility={proc_utility:.4f}\n")
            out(f"{'-'*W}\n")
            out(HDR)
            out(SEP)

            for j in sorted(jobs, key=lambda x: (x.deadline, x.release)):
                out(
                    f"  T{j.task_id}.J{j.job_idx:<9}"
                    f"{j.k:<4} {j.f:<6.2f}"
                    f"{j.exec_t():<10.4f}{j.energy():<12.4f}"
                    f"{j.utility():<10.4f}"
                    f"{j.release:<9} {j.deadline:<9}\n"
                )

            # per-task summary
            out(f"\n  Task summary\n")
            for tid in sorted(set(j.task_id for j in jobs)):
                task_jobs = [j for j in jobs if j.task_id == tid]
                k_vals    = [j.k for j in task_jobs]
                f_vals    = [j.f for j in task_jobs]
                t_e       = sum(j.energy()  for j in task_jobs)
                t_u       = sum(j.utility() for j in task_jobs)
                t_util    = sum(j.exec_t() for j in task_jobs) / H
                out(f"    T{tid}  jobs={len(task_jobs)}"
                    f"  k=[{min(k_vals)},{max(k_vals)}]"
                    f"  f=[{min(f_vals):.2f},{max(f_vals):.2f}]"
                    f"  U={t_util:.4f}"
                    f"  energy={t_e:.4f}"
                    f"  utility={t_u:.4f}\n")

        out(f"\n{'='*W}\n")

    # write to file
    with open("output_heuristic.txt", "w", encoding="utf-8") as fh:
        write_block(fh.write)

    # print to console
    print()
    write_block(sys.stdout.write)
    print(f"{GREEN}Schedule also saved to 'output_heuristic.txt'{RESET}")


# ══════════════════════════════════════════════════════════════════════════════
#  Sanity checks
# ══════════════════════════════════════════════════════════════════════════════

def verify(jobs_by_proc, processors, H, B):
    """Post-hoc verification: DBF per processor + energy budget."""
    ok = True
    total_energy = 0.0

    for pid, jobs in enumerate(jobs_by_proc):
        cps = make_checkpoints(jobs, H)
        for t in cps:
            d = dbf_at(t, jobs)
            if d > t + 1e-6:
                print(f"{RED}  VERIFY FAIL: P{pid} DBF({t})={d:.4f} > {t}{RESET}")
                ok = False
        total_energy += sum(j.energy() for j in jobs)

    if total_energy > B + 1e-6:
        print(f"{RED}  VERIFY FAIL: energy {total_energy:.4f} > B={B}{RESET}")
        ok = False

    if ok:
        print(f"{GREEN}  Verification passed.{RESET}")
    return ok


# ══════════════════════════════════════════════════════════════════════════════
#  Entry point
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    try:
        processors, TASKS, B = testcase()
        H = hyperperiod(TASKS)

        if H > 10_000:
            print(f"{YELLOW}Warning: H={H} is large – may be slow.{RESET}")
        print(f"Hyper-period H = {H}\n")

        # ── Partition ─────────────────────────────────────────────────────────
        tasks_by_proc, jobs_by_proc, ok = partition_WFDU(TASKS, processors, H)
        if not ok:
            print(f"{RED}Partitioning failed.{RESET}")
            sys.exit(1)

        # ── Phase 1 ───────────────────────────────────────────────────────────
        E = phase1(jobs_by_proc, processors, H)

        # ── Phase 2 ───────────────────────────────────────────────────────────
        E = phase2(jobs_by_proc, processors, H, B, E)

        # ── Verify + print ────────────────────────────────────────────────────
        print("\nVerifying schedule ...")
        verify(jobs_by_proc, processors, H, B)
        print_schedule(jobs_by_proc, E, B, H)

    except Exception as exc:
        print(f"{RED}Error: {exc}{RESET}")
        import traceback; traceback.print_exc()
        
        
        

"""
heuristic_v4.py
===============
Utility-Aware Energy-Constrained Real-Time Scheduling
Preemptive EDF | Per-job f_max baseline | Per-job optional segments

Pipeline
--------
  WFDU Partition
      Worst-Fit Decreasing Utilisation on mandatory util proxy e_m/p.
      Accepts a partition only after verifying DBF at f_max, k=0.

  Phase 1 — Per-job lowest feasible frequency
      Every job starts at f_max, k=0 (guaranteed feasible from WFDU).
      Jobs processed in EDF order. For each job, sweep frequencies
      slowest→fastest and accept the first f where the incremental
      DBF check passes with safety margin ε.

  Phase 2 — Bang-for-buck greedy upgrade
      Move types per job: INC_K, INC_F_INC_K, DEC_F_INC_K.
      Each move scored by:
          score = ΔUtility / (λ·ΔE + (1-λ)·Δt)
      where λ = E_total/B is the current energy pressure.
      Hard gates: energy budget and incremental DBF (+ ε margin).
      Best-scoring feasible move applied each iteration.
"""