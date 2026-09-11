"""
Refine Mapping — post-SPS utility-density balancing (Section V.A).

Two approaches:
  refine_mapping_2a : linear doublet scan
  refine_mapping_2b : one-swap-one-scan (like SPS)

Utility density of job T_{i,j}:
    ud(i) = u_i * (cum[i][N_seg[i]] - cum[i][0]) / p_i
    (identical for every job of task i)

Processor utility density:
    UD(x) = sum of ud(task_i)  for all jobs (i,j) mapped to processor x.

A swap is accepted only when ALL THREE conditions hold:
  1. UD imbalance strictly decreases (pair-level for 2a; max-UD level for 2b).
  2. Mandatory utilisation imbalance between the two processors does NOT worsen.
     (SPS produces a balanced mandatory-util mapping; swaps that disturb this
     leave less timing slack for optional segments on the overloaded processor,
     hurting Phase 5 even when DBF is still technically satisfied.)
  3. Mandatory-only DBF at f_max remains feasible for both affected processors.
"""

from itertools import combinations
from collections import defaultdict


# ── internal helpers ──────────────────────────────────────────────────────────

def _task_ud(tasks, cum, N_seg):
    """ud(i) = u_i * e_opt_total_i / p_i  for each task index i."""
    return [
        tasks[i]['u_i'] * (cum[i][N_seg[i]] - cum[i][0]) / tasks[i]['p_i']
        for i in range(len(tasks))
    ]


def _task_mutil(tasks):
    """Mandatory utilisation per task index: e_m_i / p_i."""
    return [tasks[i]['e_m'] / tasks[i]['p_i'] for i in range(len(tasks))]


def _init_proc_ud(mapping, task_ud, N_prc):
    pud = [0.0] * N_prc
    for (i, j), x in mapping.items():
        pud[x] += task_ud[i]
    return pud


def _init_proc_mutil(mapping, task_mutil, N_prc):
    pm = [0.0] * N_prc
    for (i, j), x in mapping.items():
        pm[x] += task_mutil[i]
    return pm


def _build_doublets(mapping, task_ud):
    """All job pairs sorted by ascending |ud(a) - ud(b)|."""
    jobs  = list(mapping.keys())
    pairs = list(combinations(jobs, 2))
    pairs.sort(key=lambda p: abs(task_ud[p[0][0]] - task_ud[p[1][0]]))
    return pairs


def _dbf_ok(jobs_on_proc, tasks, job_r, job_d):
    """Mandatory-only DBF check at f_max for a given job list on one processor."""
    if not jobs_on_proc:
        return True
    Ax = sorted({job_r[ij] for ij in jobs_on_proc})
    Dx = sorted({job_d[ij] for ij in jobs_on_proc})
    for t1 in Ax:
        for t2 in Dx:
            if t1 >= t2:
                continue
            demand = sum(tasks[i]['e_m'] for (i, j) in jobs_on_proc
                         if job_r[(i, j)] >= t1 and job_d[(i, j)] <= t2)
            if demand > (t2 - t1) + 1e-9:
                return False
    return True


def _swap_feasible(proc_jobs, job_a, job_b, pa, pb, tasks, job_r, job_d):
    """Return True if swapping job_a (on pa) with job_b (on pb) keeps DBF feasible."""
    new_pa = [ij for ij in proc_jobs[pa] if ij != job_a] + [job_b]
    new_pb = [ij for ij in proc_jobs[pb] if ij != job_b] + [job_a]
    return (_dbf_ok(new_pa, tasks, job_r, job_d) and
            _dbf_ok(new_pb, tasks, job_r, job_d))


def _do_swap(mapping, proc_jobs, proc_ud, proc_mutil,
             task_ud, task_mutil, job_a, job_b, pa, pb):
    """Commit swap: update mapping, proc_jobs, proc_ud, proc_mutil in-place."""
    mapping[job_a] = pb
    mapping[job_b] = pa
    proc_jobs[pa].remove(job_a)
    proc_jobs[pa].append(job_b)
    proc_jobs[pb].remove(job_b)
    proc_jobs[pb].append(job_a)
    delta_ud = task_ud[job_a[0]] - task_ud[job_b[0]]
    proc_ud[pa] -= delta_ud
    proc_ud[pb] += delta_ud
    delta_mu = task_mutil[job_a[0]] - task_mutil[job_b[0]]
    proc_mutil[pa] -= delta_mu
    proc_mutil[pb] += delta_mu


def _ud_summary(proc_ud, proc_mutil):
    return (f"UD [{min(proc_ud):.4f}, {max(proc_ud):.4f}]  "
            f"spread={max(proc_ud) - min(proc_ud):.4f}  |  "
            f"mutil [{min(proc_mutil):.4f}, {max(proc_mutil):.4f}]")


# ── public API ────────────────────────────────────────────────────────────────

def refine_mapping_2a(mapping, tasks, N_prc, cum, N_seg, job_r, job_d, verbose=True):
    """
    Step 2a — Linear doublet scan.

    Form all job pairs (doublets) sorted by ascending |ud_a - ud_b|.
    For each pair:
      - skip if both jobs are on the same processor
      - swap if UD pair-imbalance decreases
               AND mandatory-util pair-imbalance does not worsen
               AND DBF stays feasible
    Every pair is considered exactly once (single linear pass).
    """
    task_ud    = _task_ud(tasks, cum, N_seg)
    task_mutil = _task_mutil(tasks)
    proc_ud    = _init_proc_ud(mapping, task_ud, N_prc)
    proc_mutil = _init_proc_mutil(mapping, task_mutil, N_prc)
    doublets   = _build_doublets(mapping, task_ud)

    proc_jobs = defaultdict(list)
    for (i, j), x in mapping.items():
        proc_jobs[x].append((i, j))

    if verbose:
        print(f"  Before: {_ud_summary(proc_ud, proc_mutil)}")
        for x in range(N_prc):
            print(f"    P{x}: UD={proc_ud[x]:.4f}  mutil={proc_mutil[x]:.4f}")

    n_swaps = 0
    for (job_a, job_b) in doublets:
        pa = mapping[job_a]
        pb = mapping[job_b]
        if pa == pb:
            continue

        ud_a      = task_ud[job_a[0]]
        ud_b      = task_ud[job_b[0]]
        cur_diff  = abs(proc_ud[pa] - proc_ud[pb])
        new_UD_pa = proc_ud[pa] - ud_a + ud_b
        new_UD_pb = proc_ud[pb] - ud_b + ud_a
        new_diff  = abs(new_UD_pa - new_UD_pb)

        if new_diff >= cur_diff - 1e-9:
            continue

        # Guard: mandatory utilisation imbalance must not worsen
        mu_a         = task_mutil[job_a[0]]
        mu_b         = task_mutil[job_b[0]]
        cur_mu_diff  = abs(proc_mutil[pa] - proc_mutil[pb])
        new_mu_diff  = abs((proc_mutil[pa] - mu_a + mu_b) -
                           (proc_mutil[pb] - mu_b + mu_a))
        if new_mu_diff > cur_mu_diff + 1e-9:
            continue

        if _swap_feasible(proc_jobs, job_a, job_b, pa, pb, tasks, job_r, job_d):
            _do_swap(mapping, proc_jobs, proc_ud, proc_mutil,
                     task_ud, task_mutil, job_a, job_b, pa, pb)
            n_swaps += 1

    if verbose:
        print(f"  After:  {_ud_summary(proc_ud, proc_mutil)}  ({n_swaps} swap(s))")
        for x in range(N_prc):
            print(f"    P{x}: UD={proc_ud[x]:.4f}  mutil={proc_mutil[x]:.4f}")

    return mapping


def refine_mapping_2b(mapping, tasks, N_prc, cum, N_seg, job_r, job_d, verbose=True):
    """
    Step 2b — One-swap-one-scan (like SPS).

    Repeat until no improving swap is found:
      1. Identify P1 = highest-UD processor, P2 = lowest-UD processor.
      2. Scan doublets for the first pair where the higher-UD job is on P1,
         the swap would strictly reduce max UD,
         AND mandatory-util imbalance between the two processors does not worsen.
      3. Execute that swap if DBF stays feasible on both affected processors.
    The max-UD-must-decrease condition prevents cycling.
    """
    task_ud    = _task_ud(tasks, cum, N_seg)
    task_mutil = _task_mutil(tasks)
    proc_ud    = _init_proc_ud(mapping, task_ud, N_prc)
    proc_mutil = _init_proc_mutil(mapping, task_mutil, N_prc)
    doublets   = _build_doublets(mapping, task_ud)

    proc_jobs = defaultdict(list)
    for (i, j), x in mapping.items():
        proc_jobs[x].append((i, j))

    if verbose:
        print(f"  Before: {_ud_summary(proc_ud, proc_mutil)}")
        for x in range(N_prc):
            print(f"    P{x}: UD={proc_ud[x]:.4f}  mutil={proc_mutil[x]:.4f}")

    n_swaps = 0
    while True:
        P1 = max(range(N_prc), key=lambda x: proc_ud[x])
        P2 = min(range(N_prc), key=lambda x: proc_ud[x])
        if proc_ud[P1] - proc_ud[P2] < 1e-9:
            break

        swapped = False
        for (job_a, job_b) in doublets:
            hi_job, lo_job = ((job_a, job_b) if task_ud[job_a[0]] >= task_ud[job_b[0]]
                              else (job_b, job_a))

            if mapping[hi_job] != P1:
                continue

            pb = mapping[lo_job]
            if pb == P1:
                continue

            new_UD_P1 = proc_ud[P1] - task_ud[hi_job[0]] + task_ud[lo_job[0]]
            new_UD_pb = proc_ud[pb]  - task_ud[lo_job[0]] + task_ud[hi_job[0]]
            if max(new_UD_P1, new_UD_pb) >= proc_ud[P1] - 1e-9:
                continue

            # Guard: mandatory utilisation imbalance between P1 and pb must not worsen
            mu_hi        = task_mutil[hi_job[0]]
            mu_lo        = task_mutil[lo_job[0]]
            cur_mu_diff  = abs(proc_mutil[P1] - proc_mutil[pb])
            new_mu_diff  = abs((proc_mutil[P1] - mu_hi + mu_lo) -
                               (proc_mutil[pb]  - mu_lo + mu_hi))
            if new_mu_diff > cur_mu_diff + 1e-9:
                continue

            if _swap_feasible(proc_jobs, hi_job, lo_job, P1, pb, tasks, job_r, job_d):
                _do_swap(mapping, proc_jobs, proc_ud, proc_mutil,
                         task_ud, task_mutil, hi_job, lo_job, P1, pb)
                n_swaps += 1
                swapped = True
                break

        if not swapped:
            break

    if verbose:
        print(f"  After:  {_ud_summary(proc_ud, proc_mutil)}  ({n_swaps} swap(s))")
        for x in range(N_prc):
            print(f"    P{x}: UD={proc_ud[x]:.4f}  mutil={proc_mutil[x]:.4f}")

    return mapping
