"""
USRT Heuristic  —  Segmented Deterministic
===========================================

ALGORITHM OVERVIEW
------------------
Phase 1 : SPS Mapping
          Quantum-based SPS at f_max, mandatory only.
          Produces P*_{i,j} for every job.

Phase 2 : Left Shift
          On each processor, schedule jobs in EDF order starting as early
          as possible: start = max(proc_avail_time, release_time).
          Compute per-job time slack  and  per-window DBF slack.
          Left-shift invariant: time slack exists only in the FUTURE
          (a job cannot start earlier than its release time).

Phase 3 : Energy Slack
          E_slack = B_BUDGET − Σ E(i, k=0, z=f_max)
          This is the budget available for optional segments / freq changes.

Phase 4 : Aggressive Scaling
          Iteratively try to decrease frequency of each job by ONE level.
          Commit if:
            (a) timing still feasible (all DBF windows ≥ 0), AND
            (b) energy actually decreases (E_slack improves).
          Repeat until no job can be reduced further.
          Note: with the default α=1, β=0.5 energy model, minimum energy
          is at f_max, so this phase may be a no-op. The code handles it
          generically — if different α,β are used where lower freq saves
          energy, this phase kicks in correctly.

Phase 5 : Optional Segment Scheduling  (deterministic, highest u_i first)
          Sort all jobs by u_i descending.
          While any improvement in a full pass:
            For each j* in sorted order:
              While can still add optional segments to j*:
                Case (i)  — Without impacting others:
                  additional_time   = e_{i*,k+1} / f_{z*}
                  additional_energy = E(i*,k+1,z*) − E(i*,k,z*)
                  Check: min_window_slack(j*) ≥ additional_time
                      AND E_slack ≥ additional_energy
                  → If OK: add segment, update E_slack

                Case (ii.A) — Increase freq of j* (saves time, check energy):
                  Try z* → z*+1 (faster execution for both k and k+1)
                  Recompute time change and energy change.
                  Check timing globally, check E_slack.
                  → If OK: commit freq change + add segment.

                Case (ii.B) — Decrease freq of other jobs on same processor
                              (saves energy if model supports, check their timing):
                  Candidates: jobs on same proc with u_i ≤ u_i*, freq > f_min.
                  Sorted: lowest u_i first (sacrifice least valuable).
                  For each candidate: try z → z−1.
                    Energy saved  = E(old) − E(new)   [only proceed if > 0]
                    Time cost     = e_eff(new) − e_eff(old)
                    Check candidate's timing still OK.
                    Check E_slack + energy_saved ≥ additional_energy for j*.
                    → If all OK: commit both changes, add segment.

              If no case worked: move to next job.

Testcase format : testcaase.py  →  processors, tasks, B_BUDGET
Energy model    : E = α·(Σe_q/f_z) + β·f_z²·Σe_q        (Eq.2, paper)
"""

import sys
import importlib.util
from math import gcd as _gcd
from collections import defaultdict

ALPHA = 1.0
BETA  = 0.5


# ══════════════════════════════════════════════════════════════════════════════
#  UTILITIES
# ══════════════════════════════════════════════════════════════════════════════

def load_testcase(path):
    spec = importlib.util.spec_from_file_location("tc", path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.testcase()

def gcd_list(lst):
    r = int(lst[0])
    for x in lst[1:]:
        r = _gcd(r, int(x))
    return r

def lcm2(a, b):
    a, b = int(a), int(b)
    return a * b // _gcd(a, b)

def lcm_list(lst):
    r = int(lst[0])
    for x in lst[1:]:
        r = lcm2(r, int(x))
    return r

def build_cum(tasks):
    """
    cum[i][k] = e_{i,0} + … + e_{i,k}  (at f_max; k=0 → mandatory only).
    N_seg[i]  = number of optional segments.
    """
    cum, N_seg = [], []
    for t in tasks:
        segs = [t['e_m']] + list(t['e_o_k'])
        row, s = [], 0.0
        for e in segs:
            s += e; row.append(s)
        cum.append(row)
        N_seg.append(len(t['e_o_k']))
    return cum, N_seg

def generate_jobs(tasks, h):
    jobs = []
    for i, t in enumerate(tasks):
        p = int(t['p_i']); n = h // p
        for j in range(n):
            jobs.append((i, j, j * p, (j + 1) * p))
    return jobs

def energy_val(cum_k, fz):
    """E(i,k,z) = α·cum_k/fz + β·fz²·cum_k"""
    return ALPHA * cum_k / fz + BETA * fz**2 * cum_k

def e_eff_val(cum_k, fz):
    """e_eff = cum_k / fz"""
    return cum_k / fz


# ══════════════════════════════════════════════════════════════════════════════
#  SPS / DPS
# ══════════════════════════════════════════════════════════════════════════════

class PS:
    __slots__ = ('m', 'loads', 'assign', 'gap')

    def __init__(self, m):
        self.m      = m
        self.loads  = [0.0] * m
        self.assign = [set() for _ in range(m)]
        self.gap    = 0.0

    @classmethod
    def singleton(cls, m, key, val):
        ps = cls(m)
        ps.loads[0] = val
        ps.assign[0].add(key)
        ps.gap = val
        return ps

    def _resort(self):
        p = sorted(zip(self.loads, self.assign), key=lambda x: -x[0])
        self.loads  = [x[0] for x in p]
        self.assign = [x[1] for x in p]
        self.gap    = self.loads[0] - self.loads[-1]

    def insert(self, key, val):
        self.loads[-1] += val
        self.assign[-1].add(key)
        self._resort()

    def combine(self, other):
        m   = self.m
        raw = [(self.loads[j] + other.loads[m-1-j],
                self.assign[j] | other.assign[m-1-j])
               for j in range(m)]
        raw.sort(key=lambda x: -x[0])
        ps        = PS(m)
        ps.loads  = [r[0] for r in raw]
        ps.assign = [r[1] for r in raw]
        ps.gap    = ps.loads[0] - ps.loads[-1]
        return ps


def run_dps(jobs_and_loads, m):
    if not jobs_and_loads:
        return []
    key0, val0 = jobs_and_loads[0]
    active = [PS.singleton(m, key0, val0)]
    for key, val in jobs_and_loads[1:]:
        best = max(range(len(active)), key=lambda idx: active[idx].gap)
        if val <= active[best].gap:
            active[best].insert(key, val)
        else:
            active.append(PS.singleton(m, key, val))
    return active


def run_sps(ps_list):
    if not ps_list:
        return None
    active = list(ps_list)
    while len(active) > 1:
        active.sort(key=lambda ps: -ps.gap)
        merged = active[0].combine(active[1])
        active = active[2:] + [merged]
    return active[0]


# ══════════════════════════════════════════════════════════════════════════════
#  QUANTUM SPS MAPPING  (Phase 1)
# ══════════════════════════════════════════════════════════════════════════════

def check_dbf(mapping, tasks, processors, h):
    N_tsk = len(tasks); N_prc = len(processors)
    periods = [int(t['p_i']) for t in tasks]
    N_job   = [h // periods[i] for i in range(N_tsk)]
    job_r   = {(i,j): j*periods[i]      for i in range(N_tsk) for j in range(N_job[i])}
    job_d   = {(i,j): (j+1)*periods[i]  for i in range(N_tsk) for j in range(N_job[i])}
    proc_jobs = defaultdict(list)
    for (i,j), x in mapping.items():
        proc_jobs[x].append((i,j))
    violations = {}
    for x in range(N_prc):
        jobs_x = proc_jobs[x]
        if not jobs_x: continue
        Ax = sorted({job_r[ij] for ij in jobs_x})
        Dx = sorted({job_d[ij] for ij in jobs_x})
        for t1 in Ax:
            for t2 in Dx:
                if t1 >= t2: continue
                window = [(i,j) for (i,j) in jobs_x
                          if job_r[(i,j)] >= t1 and job_d[(i,j)] <= t2]
                if not window: continue
                demand = sum(tasks[i]['e_m'] for (i,j) in window)
                if demand > t2 - t1 + 1e-9:
                    violations.setdefault(x, []).append((t1,t2,demand,t2-t1))
    return len(violations) == 0, violations


def repair_mapping(mapping, tasks, processors, h):
    N_tsk = len(tasks); m = len(processors)
    periods = [int(t['p_i']) for t in tasks]
    N_job   = [h // periods[i] for i in range(N_tsk)]
    job_r   = {(i,j): j*periods[i]      for i in range(N_tsk) for j in range(N_job[i])}
    job_d   = {(i,j): (j+1)*periods[i]  for i in range(N_tsk) for j in range(N_job[i])}
    for _ in range(100):
        ok, viols = check_dbf(mapping, tasks, processors, h)
        if ok: return mapping, True
        worst = max(((x,t1,t2,d,c) for x,vl in viols.items() for (t1,t2,d,c) in vl),
                    key=lambda v: v[3]-v[4])
        x_bad, t1_bad, t2_bad = worst[0], worst[1], worst[2]
        offenders = [(i,j) for (i,j),px in mapping.items()
                     if px==x_bad and job_r[(i,j)]>=t1_bad and job_d[(i,j)]<=t2_bad]
        if not offenders: break
        mi,mj = max(offenders, key=lambda ij: tasks[ij[0]]['e_m'])
        util = defaultdict(float)
        for (i,j),px in mapping.items():
            util[px] += tasks[i]['e_m'] / tasks[i]['p_i']
        target = min((x for x in range(m) if x != x_bad), key=lambda x: util[x])
        mapping[(mi,mj)] = target
    ok, _ = check_dbf(mapping, tasks, processors, h)
    return mapping, ok


def quantum_sps_mapping(tasks, processors, h, quantum):
    m        = len(processors)
    all_jobs = generate_jobs(tasks, h)
    by_arr   = defaultdict(list)
    for job in all_jobs:
        by_arr[job[2]].append(job)

    mapping   = {}
    proc_util = [0.0] * m
    leftover  = []

    for q_start in range(0, h, quantum):
        q_end   = q_start + quantum
        newly   = by_arr.get(q_start, [])
        pending = leftover + newly
        leftover = []
        if not pending: continue

        mandatory = [(i,j,r,d) for (i,j,r,d) in pending if d == q_end]
        optional  = [(i,j,r,d) for (i,j,r,d) in pending if d >  q_end]
        optional.sort(key=lambda x: x[3])
        active   = mandatory + optional
        final_ps = None

        while True:
            if not active: break
            util_vals        = [tasks[i]['e_m'] / tasks[i]['p_i'] for (i,j,r,d) in active]
            total_util_actv  = sum(util_vals)
            remaining_cap    = sum(1.0 - proc_util[x] for x in range(m))

            if total_util_actv > remaining_cap + 1e-9:
                opt_now = [(i,j,r,d) for (i,j,r,d) in active if d > q_end]
                if not opt_now: break
                to_defer = max(opt_now, key=lambda x: x[3])
                active.remove(to_defer); leftover.append(to_defer)
                continue

            jl      = sorted([((i,j), tasks[i]['e_m']/tasks[i]['p_i'])
                               for (i,j,r,d) in active], key=lambda x: -x[1])
            ps_list = run_dps(jl, m)
            result  = run_sps(ps_list)
            if result is None: break

            new_util = list(proc_util)
            for px, job_set in enumerate(result.assign):
                for (i,j) in job_set:
                    new_util[px] += tasks[i]['e_m'] / tasks[i]['p_i']

            if max(new_util) <= 1.0 + 1e-9:
                final_ps  = result
                proc_util = new_util
                break

            opt_now = [(i,j,r,d) for (i,j,r,d) in active if d > q_end]
            if not opt_now:
                final_ps = result; proc_util = new_util; break
            to_defer = max(opt_now, key=lambda x: x[3])
            active.remove(to_defer); leftover.append(to_defer)

        if final_ps:
            for px, job_set in enumerate(final_ps.assign):
                for (i,j) in job_set:
                    mapping[(i,j)] = px

    # Handle remaining leftover
    for (i,j,r,d) in leftover:
        px = min(range(m), key=lambda x: proc_util[x])
        mapping[(i,j)] = px
        proc_util[px] += tasks[i]['e_m'] / tasks[i]['p_i']

    # Ensure all jobs mapped
    expected = {(i,j) for (i,j,r,d) in generate_jobs(tasks, h)}
    for (i,j) in sorted(expected - set(mapping.keys())):
        px = min(range(m), key=lambda x: proc_util[x])
        mapping[(i,j)] = px
        proc_util[px] += tasks[i]['e_m'] / tasks[i]['p_i']

    ok, viols = check_dbf(mapping, tasks, processors, h)
    if not ok:
        mapping, _ = repair_mapping(mapping, tasks, processors, h)

    return mapping


# ══════════════════════════════════════════════════════════════════════════════
#  TIMING HELPERS  (used in Phases 4 and 5)
# ══════════════════════════════════════════════════════════════════════════════

def window_slack(x, t1, t2, proc_jobs, job_r, job_d, seg_k, freq_idx, freq_set, cum):
    """DBF slack in window [t1,t2] on processor x given current seg_k, freq_idx."""
    jobs_x = proc_jobs[x]
    window = [(i,j) for (i,j) in jobs_x
              if job_r[(i,j)] >= t1 and job_d[(i,j)] <= t2]
    if not window:
        return t2 - t1
    demand = sum(e_eff_val(cum[i][seg_k[(i,j)]], freq_set[freq_idx[(i,j)]])
                for (i,j) in window)
    return (t2 - t1) - demand


def min_slack_containing_job(i_s, j_s, x, proc_jobs, job_r, job_d,
                              seg_k, freq_idx, freq_set, cum):
    """
    Minimum DBF slack across all windows that CONTAIN job (i_s,j_s).
    A window [t1,t2] contains the job if t1 ≤ r_{i_s,j_s} and t2 ≥ d_{i_s,j_s}.
    This is the bottleneck slack for adding extra execution to this job.
    """
    r_ij = job_r[(i_s, j_s)]
    d_ij = job_d[(i_s, j_s)]
    jobs_x = proc_jobs[x]

    Ax = sorted({job_r[ij] for ij in jobs_x})
    Dx = sorted({job_d[ij] for ij in jobs_x})

    min_sl = float('inf')
    for t1 in Ax:
        if t1 > r_ij: continue          # window must start ≤ r
        for t2 in Dx:
            if t2 < d_ij: continue      # window must end   ≥ d
            if t1 >= t2: continue
            sl = window_slack(x, t1, t2, proc_jobs, job_r, job_d,
                              seg_k, freq_idx, freq_set, cum)
            min_sl = min(min_sl, sl)
    return min_sl


def check_all_timing(proc_jobs, job_r, job_d, seg_k, freq_idx, freq_set, cum, N_prc):
    """Full DBF feasibility check across all processors and windows."""
    for x in range(N_prc):
        jobs_x = proc_jobs[x]
        if not jobs_x: continue
        Ax = sorted({job_r[ij] for ij in jobs_x})
        Dx = sorted({job_d[ij] for ij in jobs_x})
        for t1 in Ax:
            for t2 in Dx:
                if t1 >= t2: continue
                sl = window_slack(x, t1, t2, proc_jobs, job_r, job_d,
                                  seg_k, freq_idx, freq_set, cum)
                if sl < -1e-9:
                    return False
    return True


def total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job):
    return sum(energy_val(cum[i][seg_k[(i,j)]], freq_set[freq_idx[(i,j)]])
               for i in range(N_tsk) for j in range(N_job[i]))


def total_utility(seg_k, tasks, cum, N_tsk, N_job):
    return sum(tasks[i]['u_i'] * (cum[i][seg_k[(i,j)]] - cum[i][0])
               for i in range(N_tsk) for j in range(N_job[i]))


# ══════════════════════════════════════════════════════════════════════════════
#  PHASE 2 : LEFT SHIFT
# ══════════════════════════════════════════════════════════════════════════════

def left_shift(proc_jobs, job_r, job_d, seg_k, freq_idx, freq_set, cum):
    """
    For each processor, schedule jobs in EDF order starting as early as possible.
      start[i,j] = max(proc_avail, r_{i,j})
      finish[i,j] = start[i,j] + e_eff(i,k,z)
      slack[i,j]  = d_{i,j} − finish[i,j]   (per-job leftover before deadline)

    Left-shift invariant: slack exists ONLY in the future.
    The per-job slack is a quick proxy; exact slack uses the DBF windows above.
    """
    start_t  = {}
    finish_t = {}
    ls_slack = {}   # per-job left-shift slack

    for x, jobs in proc_jobs.items():
        # EDF order within each processor
        jobs_edf  = sorted(jobs, key=lambda ij: job_d[ij])
        proc_avail = 0.0
        for (i, j) in jobs_edf:
            s = max(proc_avail, float(job_r[(i,j)]))
            e = e_eff_val(cum[i][seg_k[(i,j)]], freq_set[freq_idx[(i,j)]])
            f = s + e
            start_t[(i,j)]  = s
            finish_t[(i,j)] = f
            ls_slack[(i,j)] = job_d[(i,j)] - f
            proc_avail = f

    return start_t, finish_t, ls_slack


# ══════════════════════════════════════════════════════════════════════════════
#  PHASE 4 : AGGRESSIVE SCALING
# ══════════════════════════════════════════════════════════════════════════════

def phase_aggressive_scaling(seg_k, freq_idx, freq_set, N_frq, cum,
                              N_tsk, N_job, proc_jobs, job_r, job_d, N_prc):
    """
    Iteratively try to decrease frequency of each job by one level.
    Commit only if:
      (a) timing still feasible across all DBF windows, AND
      (b) energy actually decreases (E_slack improves).
    Repeat until no job can be further reduced.

    With α=1, β=0.5 the minimum energy is at f_max, so this phase may be
    a no-op. With smaller α or larger β (dynamic-power-dominated), it fires.
    """
    n_scaled = 0
    changed  = True
    while changed:
        changed = False
        for i in range(N_tsk):
            for j in range(N_job[i]):
                z_cur = freq_idx[(i,j)]
                if z_cur == 0:
                    continue   # already at f_min
                z_new  = z_cur - 1
                E_cur  = energy_val(cum[i][seg_k[(i,j)]], freq_set[z_cur])
                E_new  = energy_val(cum[i][seg_k[(i,j)]], freq_set[z_new])
                if E_new >= E_cur - 1e-12:
                    continue   # doesn't save energy

                # Tentatively apply
                freq_idx[(i,j)] = z_new
                if check_all_timing(proc_jobs, job_r, job_d, seg_k,
                                    freq_idx, freq_set, cum, N_prc):
                    changed  = True
                    n_scaled += 1
                else:
                    freq_idx[(i,j)] = z_cur   # revert

    return n_scaled


# ══════════════════════════════════════════════════════════════════════════════
#  PHASE 5 : OPTIONAL SEGMENT SCHEDULING
# ══════════════════════════════════════════════════════════════════════════════

def phase_optional_segments(seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
                             N_tsk, N_job, proc_jobs, job_r, job_d,
                             tasks, N_prc, mapping, B_BUDGET):
    """
    Greedy optional segment addition, highest u_i first.

    Returns: (total_passes, log entries)
    """
    # Current energy slack
    E_slack = B_BUDGET - total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job)

    # Sort jobs: descending u_i, then task id, then job id (stable)
    sorted_jobs = sorted(
        [(i,j) for i in range(N_tsk) for j in range(N_job[i])],
        key=lambda ij: (-tasks[ij[0]]['u_i'], ij[0], ij[1])
    )

    log      = []
    pass_num = 0

    while True:
        pass_num += 1
        improved = False

        for (i_s, j_s) in sorted_jobs:
            x_s = mapping[(i_s, j_s)]

            while seg_k[(i_s, j_s)] < N_seg[i_s]:
                k_cur  = seg_k[(i_s, j_s)]
                k_new  = k_cur + 1
                z_cur  = freq_idx[(i_s, j_s)]
                f_cur  = freq_set[z_cur]

                # Incremental time and energy for one more optional segment
                add_time   = (cum[i_s][k_new] - cum[i_s][k_cur]) / f_cur
                add_energy = (energy_val(cum[i_s][k_new], f_cur) -
                              energy_val(cum[i_s][k_cur], f_cur))

                min_sl = min_slack_containing_job(i_s, j_s, x_s, proc_jobs,
                                                  job_r, job_d, seg_k,
                                                  freq_idx, freq_set, cum)

                # ── Case (i): add without impacting others ─────────────────
                if min_sl >= add_time - 1e-9 and E_slack >= add_energy - 1e-9:
                    seg_k[(i_s, j_s)]  = k_new
                    E_slack           -= add_energy
                    improved           = True
                    log.append(f"  Pass {pass_num}: T{tasks[i_s]['id']},j{j_s}"
                               f" k:{k_cur}→{k_new}  [case i]"
                               f"  E_slack={E_slack:.3f}")
                    continue   # try next segment for this job

                added = False

                # ── Case (ii.A): increase freq of j* ──────────────────────
                # Higher freq → faster execution → less time needed per segment
                if z_cur < N_frq - 1:
                    z_try  = z_cur + 1
                    f_try  = freq_set[z_try]
                    # New effective time for k_new segments at higher freq
                    new_e_eff_knew = e_eff_val(cum[i_s][k_new], f_try)
                    # Old effective time for k_cur segments at old freq
                    old_e_eff_kcur = e_eff_val(cum[i_s][k_cur], f_cur)
                    # Net time change on this job (negative = time saved)
                    dt = new_e_eff_knew - old_e_eff_kcur
                    # Net energy change (new - old)
                    de = (energy_val(cum[i_s][k_new], f_try) -
                          energy_val(cum[i_s][k_cur], f_cur))

                    if (min_sl - dt >= -1e-9 and    # timing OK (dt may be negative)
                        E_slack - de >= -1e-9):      # energy OK
                        # Full feasibility check
                        freq_idx[(i_s, j_s)] = z_try
                        seg_k[(i_s, j_s)]    = k_new
                        if check_all_timing(proc_jobs, job_r, job_d, seg_k,
                                            freq_idx, freq_set, cum, N_prc):
                            E_slack -= de
                            improved = True
                            added    = True
                            log.append(f"  Pass {pass_num}: T{tasks[i_s]['id']},j{j_s}"
                                       f" k:{k_cur}→{k_new} z:{z_cur}→{z_try}"
                                       f"  [case ii.A]  E_slack={E_slack:.3f}")
                        else:
                            # Revert
                            freq_idx[(i_s, j_s)] = z_cur
                            seg_k[(i_s, j_s)]    = k_cur

                # ── Case (ii.B): decrease freq of other jobs (save energy) ─
                if not added:
                    # Candidates: same processor, lower or equal u_i, freq > f_min
                    others = [
                        (i2, j2)
                        for (i2, j2) in proc_jobs[x_s]
                        if (i2, j2) != (i_s, j_s)
                        and tasks[i2]['u_i'] <= tasks[i_s]['u_i']
                        and freq_idx[(i2, j2)] > 0
                    ]
                    # Sacrifice lowest u_i first
                    others.sort(key=lambda ij: (tasks[ij[0]]['u_i'], ij[0], ij[1]))

                    for (i2, j2) in others:
                        z2_cur   = freq_idx[(i2, j2)]
                        z2_new   = z2_cur - 1
                        f2_cur   = freq_set[z2_cur]
                        f2_new   = freq_set[z2_new]
                        cum_k2   = cum[i2][seg_k[(i2, j2)]]

                        E2_cur       = energy_val(cum_k2, f2_cur)
                        E2_new       = energy_val(cum_k2, f2_new)
                        energy_saved = E2_cur - E2_new   # positive = savings

                        if energy_saved <= 1e-12:
                            continue   # doesn't save energy

                        time_cost_j2 = (e_eff_val(cum_k2, f2_new) -
                                        e_eff_val(cum_k2, f2_cur))

                        # Check timing for j2 after freq reduction
                        min_sl_j2 = min_slack_containing_job(
                            i2, j2, x_s, proc_jobs, job_r, job_d,
                            seg_k, freq_idx, freq_set, cum)

                        if min_sl_j2 < time_cost_j2 - 1e-9:
                            continue   # j2's timing would be violated

                        # Check if combined energy allows j*'s new segment
                        new_E_slack = E_slack + energy_saved
                        if new_E_slack < add_energy - 1e-9:
                            continue   # still not enough even after savings

                        # Try combined change
                        freq_idx[(i2, j2)]   = z2_new
                        seg_k[(i_s, j_s)]    = k_new

                        if check_all_timing(proc_jobs, job_r, job_d, seg_k,
                                            freq_idx, freq_set, cum, N_prc):
                            E_slack  = new_E_slack - add_energy
                            improved = True
                            added    = True
                            log.append(
                                f"  Pass {pass_num}: T{tasks[i_s]['id']},j{j_s}"
                                f" k:{k_cur}→{k_new}"
                                f"  [case ii.B: T{tasks[i2]['id']},j{j2}"
                                f" z:{z2_cur}→{z2_new}]"
                                f"  E_slack={E_slack:.3f}")
                            break
                        else:
                            # Revert both
                            freq_idx[(i2, j2)] = z2_cur
                            seg_k[(i_s, j_s)]  = k_cur

                if added:
                    continue   # got a segment, try another for j*
                else:
                    break      # can't add any more to j*, move on

        if not improved:
            break   # full pass with no improvement → done

    return pass_num, E_slack, log


# ══════════════════════════════════════════════════════════════════════════════
#  OUTPUT
# ══════════════════════════════════════════════════════════════════════════════

_S  = "=" * 76
_S2 = "-" * 76


def print_schedule(seg_k, freq_idx, freq_set, cum, tasks, N_tsk, N_job,
                   mapping, start_t, finish_t, ls_slack, B_BUDGET, label=""):
    print(f"\n{_S}")
    print(f"  SCHEDULE STATE{' — ' + label if label else ''}")
    print(_S2)
    total_e = total_utility_val = 0.0
    for i in range(N_tsk):
        u_i = tasks[i]['u_i']
        print(f"\n  Task T{tasks[i]['id']}  u_i={u_i}  period={tasks[i]['p_i']}"
              f"  N_seg={len(tasks[i]['e_o_k'])}")
        print(f"  {'job':>4}  {'proc':>5}  {'freq':>6}  {'k':>3}  "
              f"{'cum_work':>9}  {'e_eff':>8}  {'energy':>9}  "
              f"{'utility':>8}  {'ls_slack':>9}")
        print(f"  {'─'*72}")
        t_e = t_u = 0.0
        for j in range(N_job[i]):
            k  = seg_k[(i,j)]
            z  = freq_idx[(i,j)]
            fz = freq_set[z]
            cw = cum[i][k]
            ee = e_eff_val(cw, fz)
            en = energy_val(cw, fz)
            ut = u_i * (cw - cum[i][0])
            sl = ls_slack.get((i,j), float('nan'))
            t_e += en; t_u += ut
            px = mapping.get((i,j), -1)
            print(f"  {j+1:>4}  {'P'+str(px):>5}  {fz:>6.3f}  {k:>3}  "
                  f"{cw:>9.4f}  {ee:>8.4f}  {en:>9.4f}  "
                  f"{ut:>8.4f}  {sl:>9.3f}")
        total_e += t_e; total_utility_val += t_u
        print(f"  {'':4}  Task totals: energy={t_e:.4f}  utility={t_u:.4f}")
    print(f"\n{_S}")
    print(f"  Total energy  : {total_e:.4f}  "
          f"(budget={B_BUDGET}  E_slack={B_BUDGET-total_e:.4f})")
    print(f"  Total utility : {total_utility_val:.6f}")
    print(_S)
    return total_e, total_utility_val


# ══════════════════════════════════════════════════════════════════════════════
#  MAIN HEURISTIC
# ══════════════════════════════════════════════════════════════════════════════

def run_heuristic(processors, tasks, B_BUDGET):
    N_tsk    = len(tasks)
    N_prc    = len(processors)
    freq_set = processors[0]['frequencies']
    N_frq    = len(freq_set)
    periods  = [int(t['p_i']) for t in tasks]
    h        = lcm_list(periods)
    quantum  = gcd_list(periods)
    cum, N_seg = build_cum(tasks)
    N_job    = [h // periods[i] for i in range(N_tsk)]

    # Job timing tables
    all_j  = generate_jobs(tasks, h)
    job_r  = {(i,j): j*periods[i]      for (i,j,r,d) in all_j for _ in [None]}
    job_d  = {(i,j): (j+1)*periods[i]  for (i,j,r,d) in all_j for _ in [None]}
    # Simpler rebuild:
    job_r = {}; job_d = {}
    for i in range(N_tsk):
        for j in range(N_job[i]):
            job_r[(i,j)] = j * periods[i]
            job_d[(i,j)] = (j+1) * periods[i]

    # ── PHASE 1: SPS MAPPING ─────────────────────────────────────────────────
    print(f"\n{_S}")
    print(f"  HEURISTIC PHASE 1 : SPS MAPPING")
    print(_S2)
    mapping   = quantum_sps_mapping(tasks, processors, h, quantum)
    proc_jobs = defaultdict(list)
    for (i,j), x in mapping.items():
        proc_jobs[x].append((i,j))

    print(f"  Mapping complete. Proc utilisation:")
    for x in range(N_prc):
        ul = sum(tasks[i]['e_m']/tasks[i]['p_i'] for (i,j) in proc_jobs[x])
        print(f"    P{x}: {len(proc_jobs[x])} jobs  util={ul:.4f}")

    # ── INITIAL STATE: f_max, k=0 ────────────────────────────────────────────
    freq_idx = {(i,j): N_frq - 1 for i in range(N_tsk) for j in range(N_job[i])}
    seg_k    = {(i,j): 0         for i in range(N_tsk) for j in range(N_job[i])}

    # ── PHASE 2: LEFT SHIFT ──────────────────────────────────────────────────
    print(f"\n{_S}")
    print(f"  HEURISTIC PHASE 2 : LEFT SHIFT  (EDF order, f_max, mandatory only)")
    print(_S2)
    start_t, finish_t, ls_slack = left_shift(
        proc_jobs, job_r, job_d, seg_k, freq_idx, freq_set, cum)

    infeasible_jobs = [(i,j) for (i,j) in ls_slack if ls_slack[(i,j)] < -1e-9]
    if infeasible_jobs:
        print(f"  [!] {len(infeasible_jobs)} job(s) miss deadline in left-shift"
              f" (non-preemptive proxy). Preemptive EDF may still be feasible.")
    else:
        print(f"  All jobs schedulable (left-shift slack ≥ 0).")

    min_slack_overall = min(ls_slack.values()) if ls_slack else 0
    print(f"  Minimum per-job left-shift slack : {min_slack_overall:.4f}")

    # ── PHASE 3: ENERGY SLACK ────────────────────────────────────────────────
    print(f"\n{_S}")
    print(f"  HEURISTIC PHASE 3 : ENERGY SLACK")
    print(_S2)
    E_consumed_init = total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job)
    E_slack_init    = B_BUDGET - E_consumed_init
    print(f"  E_consumed (mandatory, f_max) : {E_consumed_init:.4f}")
    print(f"  E_budget                      : {B_BUDGET:.4f}")
    print(f"  E_slack                       : {E_slack_init:.4f}"
          f"{'  [INFEASIBLE: budget exceeded]' if E_slack_init < 0 else ''}")

    if E_slack_init < -1e-9:
        print(f"\n  [ERROR] Mandatory-only execution at f_max already exceeds budget.")
        print(f"  Cannot produce a feasible schedule. Reporting mandatory-only solution.")
        _, total_u = print_schedule(seg_k, freq_idx, freq_set, cum, tasks,
                                    N_tsk, N_job, mapping, start_t, finish_t,
                                    ls_slack, B_BUDGET, label="INFEASIBLE MANDATORY")
        return seg_k, freq_idx, 0.0, E_consumed_init

    # ── PHASE 4: AGGRESSIVE SCALING ──────────────────────────────────────────
    print(f"\n{_S}")
    print(f"  HEURISTIC PHASE 4 : AGGRESSIVE SCALING  (freq ↓ to save energy)")
    print(_S2)
    n_scaled = phase_aggressive_scaling(
        seg_k, freq_idx, freq_set, N_frq, cum,
        N_tsk, N_job, proc_jobs, job_r, job_d, N_prc)

    E_after_scaling = total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job)
    E_slack_after   = B_BUDGET - E_after_scaling

    if n_scaled == 0:
        print(f"  No frequency reductions made.")
        print(f"  (Energy model with α={ALPHA}, β={BETA} has minimum at f_max;")
        print(f"   freq reduction would increase energy. Phase 4 is a no-op.)")
    else:
        print(f"  {n_scaled} frequency reduction(s) applied.")
        print(f"  E_consumed after scaling : {E_after_scaling:.4f}")
        print(f"  E_slack after scaling    : {E_slack_after:.4f}")

    # Recompute left shift after scaling
    start_t, finish_t, ls_slack = left_shift(
        proc_jobs, job_r, job_d, seg_k, freq_idx, freq_set, cum)

    # ── PHASE 5: OPTIONAL SEGMENT SCHEDULING ─────────────────────────────────
    print(f"\n{_S}")
    print(f"  HEURISTIC PHASE 5 : OPTIONAL SEGMENT SCHEDULING")
    print(f"  Strategy: highest u_i first, case (i) then (ii.A) then (ii.B)")
    print(_S2)

    n_passes, E_slack_final, opt_log = phase_optional_segments(
        seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
        N_tsk, N_job, proc_jobs, job_r, job_d,
        tasks, N_prc, mapping, B_BUDGET)

    if opt_log:
        print(f"  Segment additions ({len(opt_log)} total across {n_passes} passes):")
        for entry in opt_log:
            print(entry)
    else:
        print(f"  No optional segments could be added.")

    # Final left shift for output
    start_t, finish_t, ls_slack = left_shift(
        proc_jobs, job_r, job_d, seg_k, freq_idx, freq_set, cum)

    # ── FINAL SCHEDULE ────────────────────────────────────────────────────────
    total_e, total_u = print_schedule(
        seg_k, freq_idx, freq_set, cum, tasks,
        N_tsk, N_job, mapping, start_t, finish_t,
        ls_slack, B_BUDGET, label="FINAL HEURISTIC SOLUTION")

    return seg_k, freq_idx, total_u, total_e


# ══════════════════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    tc_path = sys.argv[1] if len(sys.argv) > 1 else "testcase.py"
    print(f"Loading testcase: {tc_path}")
    processors, tasks, B_BUDGET = load_testcase(tc_path)

    periods = [int(t['p_i']) for t in tasks]
    h       = lcm_list(periods)
    quantum = gcd_list(periods)
    cum, N_seg = build_cum(tasks)
    N_tsk   = len(tasks)
    N_job   = [h // periods[i] for i in range(N_tsk)]

    # Instance summary
    print(f"\n{_S}")
    print(f"  USRT Heuristic  —  Instance")
    print(_S2)
    print(f"  Processors   : {len(processors)}")
    print(f"  Frequencies  : {processors[0]['frequencies']}")
    print(f"  Energy budget: {B_BUDGET}    α={ALPHA}   β={BETA}")
    print(f"  Hyper-period : {h}    Quantum(GCD): {quantum}")
    print(_S2)
    total_util = sum(t['e_m']/t['p_i'] for t in tasks)
    print(f"  {'TID':>4}  {'period':>7}  {'Nseg':>5}  {'Njobs':>6}  "
          f"{'e_m':>9}  {'util':>7}  e_o_k")
    print(f"  {_S2}")
    for i, t in enumerate(tasks):
        u = t['e_m'] / t['p_i']
        print(f"  {t['id']:>4}  {t['p_i']:>7}  {N_seg[i]:>5}  {N_job[i]:>6}  "
              f"{t['e_m']:>9.4f}  {u:>7.4f}  "
              f"{[round(x,4) for x in t['e_o_k']]}")
    print(f"\n  Total utilisation: {total_util:.4f} / {len(processors)}"
          f"  [{'FEASIBLE' if total_util <= len(processors) else 'OVERLOADED'}]")
    print(_S)

    run_heuristic(processors, tasks, B_BUDGET)