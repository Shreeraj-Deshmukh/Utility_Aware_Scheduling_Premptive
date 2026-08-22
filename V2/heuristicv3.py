"""
USRT Heuristic  —  Segmented Deterministic Heuristic
=====================================================
Reference: Heuristic_15_04_2026.pdf (handwritten notes)

ALGORITHM OVERVIEW
------------------
Phase 1 : SPS Mapping
          Quantum-based SPS (same as ILP v2 Phase 1).
          All jobs mapped at f_max, mandatory segments only.
          Output: mapping[(i,j)] → processor x.

Phase 2 : Left Shift  (executed ONCE)
          Simulated non-preemptive left-shift per processor.
          Each job starts at max(proc_avail_time, job_release_time).
          Gives time_slack[(i,j)] = deadline − (start + e_eff).
          Purpose: estimate idle time in each job's activation window.
          NOTE: This is an ANALYSIS TOOL only. Actual execution is
          preemptive EDF. DBF is still used for feasibility checking.

Phase 3 : Compute Energy Slack
          E_slack = B_BUDGET − Σ E(i, k=0, z=f_max)

Phase 4 : Aggressive Scaling  (freq UP)
          In our energy model  E = α*(cum/f) + β*f²*cum  with α=1,β=0.5,
          energy is minimised at f_max. All jobs start at f_max, so
          aggressive scaling is a structural no-op in this model.
          We still implement the scan and document why no changes occur.
          After any changes: recompute time_slack and E_slack.

Phase 5 : Greedy Optional Segment Scheduling
          Sort all jobs by u_i descending (j* = highest utility job first).
          For each j*:
            Try to increment its segment count k by 1.

            Case (i)  — Without impacting others:
              Check time_slack[(i*,j*)] ≥ extra_exec_time_needed  (from left-shift)
              Check E_slack ≥ delta_energy
              Check DBF(proc(j*)) still feasible after change
              If all pass → add segment, update slacks, continue to next j*.

            Case (ii) — Impacting others (if case (i) fails):
              Step 1: Inc freq of j* by one level
                      In our model this saves time AND energy.
                      Try: does (k+1) fit with new freq?
                      If DBF ok and energy ok → apply, continue.

              Step 2: Inc freq of other jobs on same processor
                      For each other job on same proc (sorted by u_i asc,
                      least important first):
                        Inc their freq by one level → saves time on their slot
                        → creates time slack for j*.
                        Check DBF + energy → apply if feasible.

              Step 3: Dec freq of other jobs  (LAST RESORT, only if E_slack < threshold)
                      Only try when energy slack is nearly exhausted.
                      Dec freq of lowest-u_i jobs on same proc by one level.
                      In our model dec freq → MORE energy → only worthwhile if
                      combined with reducing their segment count, freeing energy
                      budget for j*'s optional segment.
                      Check DBF + energy after combined change.

          Outer loop: repeat until a full pass through all j* yields no improvement.

INVARIANTS (from notes)
-----------------------
  Energy invariant : inc/dec freq by same value → energy stays same   ← not exactly
                     true in our model but guides intuition.
  Performance invariant : same optional execution length ≠ same utility
                          (utility depends on u_i and which segments run).
  Left-shift invariant : no time slack in the past, only in future.

Testcase: testcaase.py  →  processors, tasks, B_BUDGET
"""

import sys
import importlib.util
from math import gcd as _gcd
from collections import defaultdict

# ── energy model coefficients ─────────────────────────────────────────────────
# Imported from the single source of truth (usrt/models.py) so this legacy
# monolith can never drift from the rest of the project.  Previously hard-coded
# to ALPHA=1.0, BETA=0.5 -- the stale pair -- under which the energy optimum is
# f_max, whereas under the project's 0.15/1.0 it is f* ~= 0.42.  The two
# disagree about the entire DVFS trade-off, so a standalone run of this file was
# silently solving a different problem.
from usrt.models import ALPHA, BETA

# ─────────────────────────────────────────────────────────────────────────────
#  SHARED UTILITIES  (mirrors ILP v2 code for consistency)
# ─────────────────────────────────────────────────────────────────────────────

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


# ─────────────────────────────────────────────────────────────────────────────
#  SPS / DPS  (identical to ILP v2)
# ─────────────────────────────────────────────────────────────────────────────

class PS:
    __slots__ = ('m', 'loads', 'assign', 'gap')
    def __init__(self, m):
        self.m = m; self.loads = [0.0]*m
        self.assign = [set() for _ in range(m)]; self.gap = 0.0

    @classmethod
    def singleton(cls, m, key, val):
        ps = cls(m); ps.loads[0] = val; ps.assign[0].add(key); ps.gap = val
        return ps

    def _resort(self):
        p = sorted(zip(self.loads, self.assign), key=lambda x: -x[0])
        self.loads = [x[0] for x in p]; self.assign = [x[1] for x in p]
        self.gap = self.loads[0] - self.loads[-1]

    def insert(self, key, val):
        self.loads[-1] += val; self.assign[-1].add(key); self._resort()

    def combine(self, other):
        m = self.m
        raw = [(self.loads[j] + other.loads[m-1-j],
                self.assign[j] | other.assign[m-1-j]) for j in range(m)]
        raw.sort(key=lambda x: -x[0])
        ps = PS(m); ps.loads = [r[0] for r in raw]
        ps.assign = [r[1] for r in raw]; ps.gap = ps.loads[0] - ps.loads[-1]
        return ps

def run_dps(jobs_and_loads, m):
    if not jobs_and_loads: return []
    key0, val0 = jobs_and_loads[0]
    active = [PS.singleton(m, key0, val0)]
    for key, val in jobs_and_loads[1:]:
        best = max(range(len(active)), key=lambda idx: active[idx].gap)
        if val <= active[best].gap: active[best].insert(key, val)
        else: active.append(PS.singleton(m, key, val))
    return active

def run_sps(ps_list):
    if not ps_list: return None
    active = list(ps_list)
    while len(active) > 1:
        active.sort(key=lambda ps: -ps.gap)
        merged = active[0].combine(active[1]); active = active[2:] + [merged]
    return active[0]

def check_dbf_global(mapping, tasks, processors, h, seg_state=None, freq_state=None, cum=None, freq_set=None):
    """
    DBF feasibility check.
    If seg_state/freq_state provided → use those e_eff values.
    Otherwise uses e_m at f_max (mandatory only baseline).
    """
    N_tsk = len(tasks); N_prc = len(processors)
    periods = [int(t['p_i']) for t in tasks]
    N_job = [h // periods[i] for i in range(N_tsk)]
    job_r = {(i,j): j*periods[i]      for i in range(N_tsk) for j in range(N_job[i])}
    job_d = {(i,j): (j+1)*periods[i]  for i in range(N_tsk) for j in range(N_job[i])}

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
                if seg_state is not None:
                    demand = sum(cum[i][seg_state[(i,j)]] / freq_set[freq_state[(i,j)]]
                                 for (i,j) in window)
                else:
                    demand = sum(tasks[i]['e_m'] for (i,j) in window)
                cap = t2 - t1
                if demand > cap + 1e-9:
                    violations.setdefault(x, []).append((t1, t2, demand, cap))
    return len(violations) == 0, violations

def repair_mapping(mapping, tasks, processors, h):
    periods = [int(t['p_i']) for t in tasks]
    N_tsk = len(tasks); m = len(processors)
    N_job = [h // periods[i] for i in range(N_tsk)]
    job_r = {(i,j): j*periods[i]      for i in range(N_tsk) for j in range(N_job[i])}
    job_d = {(i,j): (j+1)*periods[i]  for i in range(N_tsk) for j in range(N_job[i])}

    for _ in range(100):
        ok, viols = check_dbf_global(mapping, tasks, processors, h)
        if ok: return mapping, True
        worst = max(((x, t1, t2, dem, cap)
                     for x, vlist in viols.items()
                     for (t1, t2, dem, cap) in vlist),
                    key=lambda v: v[3] - v[4])
        x_bad, t1_b, t2_b = worst[0], worst[1], worst[2]
        offenders = [(i,j) for (i,j), px in mapping.items()
                     if px == x_bad and job_r[(i,j)] >= t1_b and job_d[(i,j)] <= t2_b]
        if not offenders: break
        mi, mj = max(offenders, key=lambda ij: tasks[ij[0]]['e_m'])
        util = defaultdict(float)
        for (i,j), px in mapping.items():
            util[px] += tasks[i]['e_m'] / tasks[i]['p_i']
        target = min((x for x in range(m) if x != x_bad), key=lambda x: util[x])
        mapping[(mi, mj)] = target
    ok, _ = check_dbf_global(mapping, tasks, processors, h)
    return mapping, ok

def quantum_sps_mapping(tasks, processors, h, quantum):
    m = len(processors)
    all_jobs = generate_jobs(tasks, h)
    by_arr = defaultdict(list)
    for job in all_jobs: by_arr[job[2]].append(job)

    mapping = {}; proc_util = [0.0]*m; leftover = []

    print(f"\n  {'Quantum':^12}  {'Mand':>5}  {'Opt':>5}  "
          f"{'Actv':>5}  {'Defr':>5}  {'MaxUtil':>9}  Status")
    print(f"  {'─'*68}")

    for q_start in range(0, h, quantum):
        q_end = q_start + quantum
        newly = by_arr.get(q_start, []); pending = leftover + newly; leftover = []
        if not pending: continue

        mandatory = [(i,j,r,d) for (i,j,r,d) in pending if d == q_end]
        optional  = [(i,j,r,d) for (i,j,r,d) in pending if d >  q_end]
        optional.sort(key=lambda x: x[3])
        n_mand = len(mandatory); n_opt = len(optional)
        active = mandatory + optional; final_ps = None; deferred = 0; status = "OK"

        while True:
            if not active: status = "EMPTY"; break
            util_vals = [tasks[i]['e_m']/tasks[i]['p_i'] for (i,j,r,d) in active]
            total_util = sum(util_vals)
            remaining_cap = [1.0 - proc_util[x] for x in range(m)]
            if total_util > sum(remaining_cap) + 1e-9:
                opt_now = [(i,j,r,d) for (i,j,r,d) in active if d > q_end]
                if not opt_now: status = "MAND_OVERUTIL"; break
                to_defer = max(opt_now, key=lambda x: x[3])
                active.remove(to_defer); leftover.append(to_defer); deferred += 1; continue

            jl = sorted([((i,j), tasks[i]['e_m']/tasks[i]['p_i'])
                          for (i,j,r,d) in active], key=lambda x: -x[1])
            result = run_sps(run_dps(jl, m))
            if result is None: status = "SPS_NONE"; break

            new_util = list(proc_util)
            for px, job_set in enumerate(result.assign):
                for (i,j) in job_set: new_util[px] += tasks[i]['e_m']/tasks[i]['p_i']

            if max(new_util) <= 1.0 + 1e-9:
                final_ps = result; proc_util = new_util
                status = f"util={max(new_util):.3f}"; break

            opt_now = [(i,j,r,d) for (i,j,r,d) in active if d > q_end]
            if not opt_now:
                final_ps = result; proc_util = new_util
                status = f"OVER(util={max(new_util):.3f})"; break
            to_defer = max(opt_now, key=lambda x: x[3])
            active.remove(to_defer); leftover.append(to_defer); deferred += 1

        print(f"  [{q_start:>4},{q_end:>4}]  {n_mand:>5}  {n_opt:>5}  "
              f"{len(active):>5}  {deferred:>5}  {max(proc_util):>9.4f}  {status}")

        if final_ps:
            for px, job_set in enumerate(final_ps.assign):
                for (i,j) in job_set: mapping[(i,j)] = px

    if leftover:
        print(f"\n  [!] {len(leftover)} leftover job(s) → least-util proc.")
        for (i,j,r,d) in leftover:
            px = min(range(m), key=lambda x: proc_util[x])
            mapping[(i,j)] = px; proc_util[px] += tasks[i]['e_m']/tasks[i]['p_i']

    expected = {(i,j) for (i,j,r,d) in generate_jobs(tasks,h)}
    missing = expected - set(mapping.keys())
    if missing:
        for (i,j) in sorted(missing):
            px = min(range(m), key=lambda x: proc_util[x])
            mapping[(i,j)] = px; proc_util[px] += tasks[i]['e_m']/tasks[i]['p_i']

    ok, viols = check_dbf_global(mapping, tasks, processors, h)
    if not ok:
        n_v = sum(len(v) for v in viols.values())
        print(f"\n  DBF: {n_v} violation(s) → running repair …")
        mapping, repaired = repair_mapping(mapping, tasks, processors, h)
        print(f"  Repair: {'SUCCESS ✓' if repaired else 'PARTIAL'}")
    else:
        print(f"\n  DBF: FEASIBLE ✓")

    return mapping


# ─────────────────────────────────────────────────────────────────────────────
#  PHASE 2 : LEFT SHIFT  (one-time slack estimator)
# ─────────────────────────────────────────────────────────────────────────────

def left_shift(mapping, tasks, processors, h, seg_state, freq_state, cum, freq_set):
    """
    Non-preemptive left-shift simulation per processor.

    For each processor, sort jobs by deadline (EDF order).
    Each job's simulated start = max(proc_avail, release_time).
    time_slack[(i,j)] = deadline − (start + e_eff(i, k, z))

    This is an APPROXIMATION of idle time in each job's activation window.
    Actual scheduling is preemptive EDF; DBF is used for hard feasibility.

    Returns: dict (i,j) → float time_slack
    """
    N_tsk   = len(tasks)
    periods = [int(t['p_i']) for t in tasks]
    N_job   = [h // periods[i] for i in range(N_tsk)]

    proc_jobs = defaultdict(list)
    for i in range(N_tsk):
        for j in range(N_job[i]):
            x = mapping[(i,j)]
            r = j * periods[i]; d = (j+1) * periods[i]
            proc_jobs[x].append((i, j, r, d))

    time_slack = {}
    for x in range(len(processors)):
        jobs_x = sorted(proc_jobs[x], key=lambda ijrd: ijrd[3])   # EDF order
        proc_avail = 0.0
        for (i, j, r, d) in jobs_x:
            k  = seg_state[(i,j)]; z = freq_state[(i,j)]
            ef = cum[i][k] / freq_set[z]
            start  = max(proc_avail, float(r))
            finish = start + ef
            time_slack[(i,j)] = d - finish
            proc_avail = finish   # non-preemptive: proc busy until finish

    return time_slack


# ─────────────────────────────────────────────────────────────────────────────
#  ENERGY HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def energy_val(cum_ik, fz):
    """E(i,k,z) = α*(cum/f) + β*f²*cum"""
    return ALPHA * (cum_ik / fz) + BETA * (fz ** 2) * cum_ik

def total_energy_consumed(tasks, h, seg_state, freq_state, cum, freq_set):
    N_tsk = len(tasks)
    periods = [int(t['p_i']) for t in tasks]
    N_job = [h // periods[i] for i in range(N_tsk)]
    return sum(energy_val(cum[i][seg_state[(i,j)]], freq_set[freq_state[(i,j)]])
               for i in range(N_tsk) for j in range(N_job[i]))


# ─────────────────────────────────────────────────────────────────────────────
#  DBF CHECK FOR A SINGLE PROCESSOR  (used inside heuristic loop)
# ─────────────────────────────────────────────────────────────────────────────

def dbf_feasible_proc(x, mapping, tasks, h, seg_state, freq_state, cum, freq_set):
    """
    Check DBF feasibility for processor x under current seg_state/freq_state.
    Returns True if feasible.
    """
    N_tsk   = len(tasks)
    periods = [int(t['p_i']) for t in tasks]
    N_job   = [h // periods[i] for i in range(N_tsk)]
    job_r   = {(i,j): j*periods[i]      for i in range(N_tsk) for j in range(N_job[i])}
    job_d   = {(i,j): (j+1)*periods[i]  for i in range(N_tsk) for j in range(N_job[i])}

    jobs_x = [(i,j) for (i,j), px in mapping.items() if px == x]
    Ax = sorted({job_r[ij] for ij in jobs_x})
    Dx = sorted({job_d[ij] for ij in jobs_x})

    for t1 in Ax:
        for t2 in Dx:
            if t1 >= t2: continue
            window = [(i,j) for (i,j) in jobs_x
                      if job_r[(i,j)] >= t1 and job_d[(i,j)] <= t2]
            if not window: continue
            demand = sum(cum[i][seg_state[(i,j)]] / freq_set[freq_state[(i,j)]]
                         for (i,j) in window)
            if demand > (t2 - t1) + 1e-9:
                return False
    return True


# ─────────────────────────────────────────────────────────────────────────────
#  PHASE 3-5 : HEURISTIC CORE
# ─────────────────────────────────────────────────────────────────────────────

def run_heuristic_core(processors, tasks, B_BUDGET, mapping):
    """
    Phases 2–5 of the heuristic.

    State per job:
      seg_state[(i,j)]  : current segment level k  (0 = mandatory only)
      freq_state[(i,j)] : current frequency index z (N_frq-1 = f_max)

    Returns:
      seg_state, freq_state, total_utility achieved
    """
    N_tsk    = len(tasks)
    freq_set = processors[0]['frequencies']
    N_frq    = len(freq_set)
    f_max_idx = N_frq - 1
    periods   = [int(t['p_i']) for t in tasks]
    h         = lcm_list(periods)
    N_job     = [h // periods[i] for i in range(N_tsk)]
    cum, N_seg = build_cum(tasks)

    _S2 = "─" * 70

    # ── INITIALISE: f_max, k=0 for all jobs ──────────────────────────────────
    seg_state  = {(i,j): 0          for i in range(N_tsk) for j in range(N_job[i])}
    freq_state = {(i,j): f_max_idx  for i in range(N_tsk) for j in range(N_job[i])}

    # ── PHASE 2: LEFT SHIFT (once) ────────────────────────────────────────────
    print(f"\n  Phase 2 : Left Shift")
    time_slack = left_shift(mapping, tasks, processors, h,
                            seg_state, freq_state, cum, freq_set)
    min_slack = min(time_slack.values()) if time_slack else 0.0
    print(f"  Min time slack across all jobs: {min_slack:.4f}")

    # ── PHASE 3: ENERGY SLACK ─────────────────────────────────────────────────
    E_consumed = total_energy_consumed(tasks, h, seg_state, freq_state, cum, freq_set)
    E_slack    = B_BUDGET - E_consumed
    print(f"\n  Phase 3 : Energy Slack")
    print(f"  E_consumed (mandatory, f_max) = {E_consumed:.4f}")
    print(f"  E_slack                       = {E_slack:.4f}")
    if E_slack < 0:
        print(f"  [!] E_slack < 0: mandatory execution already exceeds budget!")
        return seg_state, freq_state, 0.0

    # ── PHASE 4: AGGRESSIVE SCALING (freq UP toward f_max) ───────────────────
    # In our energy model E=α*(c/f)+β*f²*c with α=1,β=0.5, energy is minimised
    # at f_max. All jobs start at f_max, so no frequency increase is possible.
    # This phase is structural; if an alternative initialisation used lower
    # frequencies, this scan would push them up.
    print(f"\n  Phase 4 : Aggressive Scaling (freq UP)")
    scaled = 0
    for i in range(N_tsk):
        for j in range(N_job[i]):
            z_cur = freq_state[(i,j)]
            if z_cur >= f_max_idx:
                continue   # already at max
            # Try incrementing frequency one level
            z_new  = z_cur + 1
            k      = seg_state[(i,j)]
            dE     = energy_val(cum[i][k], freq_set[z_new]) \
                   - energy_val(cum[i][k], freq_set[z_cur])
            if E_slack + dE >= -1e-9:    # dE < 0 in our model → always helps
                freq_state[(i,j)] = z_new
                x = mapping[(i,j)]
                if dbf_feasible_proc(x, mapping, tasks, h,
                                     seg_state, freq_state, cum, freq_set):
                    E_slack  -= dE   # dE<0 → E_slack increases
                    scaled   += 1
                else:
                    freq_state[(i,j)] = z_cur   # revert
    print(f"  Jobs frequency-scaled up: {scaled}")

    # Recompute time slack after scaling
    time_slack = left_shift(mapping, tasks, processors, h,
                            seg_state, freq_state, cum, freq_set)
    print(f"  E_slack after scaling: {E_slack:.4f}")

    # ── PHASE 5: GREEDY OPTIONAL SEGMENT SCHEDULING ───────────────────────────
    print(f"\n  Phase 5 : Greedy Optional Segment Scheduling")
    print(f"  {'─'*70}")

    # All jobs sorted by u_i descending (j* ordering)
    all_jobs_sorted = sorted(
        [(i,j) for i in range(N_tsk) for j in range(N_job[i])],
        key=lambda ij: tasks[ij[0]]['u_i'],
        reverse=True
    )

    # Energy threshold for "nearly exhausted" (step 3 trigger)
    E_SLACK_THRESHOLD = 1.0

    iteration  = 0
    total_pass_improvements = 0

    while True:
        improved_this_pass = 0
        iteration += 1

        for (i_star, j_star) in all_jobs_sorted:
            k_cur = seg_state[(i_star, j_star)]
            z_cur = freq_state[(i_star, j_star)]

            if k_cur >= N_seg[i_star]:
                continue   # already at max segments for this task

            x_star = mapping[(i_star, j_star)]
            u_star = tasks[i_star]['u_i']

            # Extra execution time for one more segment at current freq
            extra_exec = tasks[i_star]['e_o_k'][k_cur] / freq_set[z_cur]

            # Energy cost of adding one more segment (freq unchanged)
            dE_seg = (energy_val(cum[i_star][k_cur + 1], freq_set[z_cur])
                    - energy_val(cum[i_star][k_cur],     freq_set[z_cur]))

            added = False

            # ══ CASE (i): add segment without impacting others ════════════════
            slack_ok  = time_slack.get((i_star, j_star), 0.0) >= extra_exec - 1e-9
            energy_ok = E_slack >= dE_seg - 1e-9

            if slack_ok and energy_ok:
                seg_state[(i_star, j_star)] = k_cur + 1
                if dbf_feasible_proc(x_star, mapping, tasks, h,
                                     seg_state, freq_state, cum, freq_set):
                    E_slack   -= dE_seg
                    time_slack = left_shift(mapping, tasks, processors, h,
                                            seg_state, freq_state, cum, freq_set)
                    improved_this_pass += 1
                    added = True
                else:
                    seg_state[(i_star, j_star)] = k_cur   # revert

            if added:
                continue

            # ══ CASE (ii) Step 1: inc freq of j* ════════════════════════════
            if not added and z_cur < f_max_idx:
                z_new   = z_cur + 1
                # Energy with new freq AND new segment vs current state
                dE_step1 = (energy_val(cum[i_star][k_cur + 1], freq_set[z_new])
                          - energy_val(cum[i_star][k_cur],     freq_set[z_cur]))

                if E_slack >= dE_step1 - 1e-9:
                    freq_state[(i_star, j_star)] = z_new
                    seg_state[(i_star, j_star)]  = k_cur + 1
                    if dbf_feasible_proc(x_star, mapping, tasks, h,
                                         seg_state, freq_state, cum, freq_set):
                        E_slack   -= dE_step1
                        time_slack = left_shift(mapping, tasks, processors, h,
                                                seg_state, freq_state, cum, freq_set)
                        improved_this_pass += 1
                        added = True
                    else:
                        freq_state[(i_star, j_star)] = z_cur   # revert
                        seg_state[(i_star, j_star)]  = k_cur

            if added:
                continue

            # ══ CASE (ii) Step 2: inc freq of others on same proc ═══════════
            if not added:
                # Other jobs on same proc, sorted least-important first
                others = sorted(
                    [(i,j) for (i,j), px in mapping.items()
                     if px == x_star and (i,j) != (i_star, j_star)
                     and freq_state[(i,j)] < f_max_idx],
                    key=lambda ij: tasks[ij[0]]['u_i']   # least u_i first
                )
                for (i_o, j_o) in others:
                    z_o_cur = freq_state[(i_o, j_o)]
                    z_o_new = z_o_cur + 1
                    k_o     = seg_state[(i_o, j_o)]

                    # Energy: inc freq of other + add seg to j*
                    dE_other = (energy_val(cum[i_o][k_o], freq_set[z_o_new])
                              - energy_val(cum[i_o][k_o], freq_set[z_o_cur]))
                    total_dE = dE_seg + dE_other

                    if E_slack >= total_dE - 1e-9:
                        freq_state[(i_o, j_o)]       = z_o_new
                        seg_state[(i_star, j_star)]  = k_cur + 1
                        if dbf_feasible_proc(x_star, mapping, tasks, h,
                                             seg_state, freq_state, cum, freq_set):
                            E_slack   -= total_dE
                            time_slack = left_shift(mapping, tasks, processors, h,
                                                    seg_state, freq_state, cum, freq_set)
                            improved_this_pass += 1
                            added = True
                            break
                        else:
                            freq_state[(i_o, j_o)]      = z_o_cur   # revert
                            seg_state[(i_star, j_star)] = k_cur

            if added:
                continue

            # ══ CASE (ii) Step 3: dec freq of others  (LAST RESORT) ══════════
            # Only triggered when E_slack is nearly exhausted.
            # In our model, dec freq INCREASES energy → we combine it with
            # reducing that job's segment count so the net effect saves energy.
            if not added and E_slack < E_SLACK_THRESHOLD:
                candidates = sorted(
                    [(i,j) for (i,j), px in mapping.items()
                     if px == x_star and (i,j) != (i_star, j_star)
                     and tasks[i]['u_i'] < u_star           # lower priority only
                     and freq_state[(i,j)] > 0              # can dec freq
                     and seg_state[(i,j)] > 0],             # has optional segs to drop
                    key=lambda ij: tasks[ij[0]]['u_i']      # least u_i first
                )
                for (i_o, j_o) in candidates:
                    z_o_cur = freq_state[(i_o, j_o)]
                    z_o_new = z_o_cur - 1
                    k_o_cur = seg_state[(i_o, j_o)]
                    k_o_new = k_o_cur - 1    # drop one optional seg to save energy

                    # Energy change: (dec freq + dec seg) for other, (+seg) for j*
                    dE_other = (energy_val(cum[i_o][k_o_new], freq_set[z_o_new])
                              - energy_val(cum[i_o][k_o_cur], freq_set[z_o_cur]))
                    total_dE = dE_seg + dE_other    # dE_other is negative → saves energy

                    if E_slack >= total_dE - 1e-9:
                        freq_state[(i_o, j_o)]      = z_o_new
                        seg_state[(i_o, j_o)]       = k_o_new
                        seg_state[(i_star, j_star)] = k_cur + 1
                        if dbf_feasible_proc(x_star, mapping, tasks, h,
                                             seg_state, freq_state, cum, freq_set):
                            E_slack   -= total_dE
                            time_slack = left_shift(mapping, tasks, processors, h,
                                                    seg_state, freq_state, cum, freq_set)
                            improved_this_pass += 1
                            added = True
                            break
                        else:
                            freq_state[(i_o, j_o)]      = z_o_cur   # revert all
                            seg_state[(i_o, j_o)]       = k_o_cur
                            seg_state[(i_star, j_star)] = k_cur

        total_pass_improvements += improved_this_pass
        print(f"  Iteration {iteration:>3} : {improved_this_pass:>4} segment(s) added  "
              f"| E_slack={E_slack:.4f}")

        if improved_this_pass == 0:
            break   # no improvement in full pass → terminate

    # ── Compute final utility ─────────────────────────────────────────────────
    total_utility = sum(
        tasks[i]['u_i'] * (cum[i][seg_state[(i,j)]] - cum[i][0])
        for i in range(N_tsk) for j in range(N_job[i])
    )

    print(f"\n  Total iterations   : {iteration}")
    print(f"  Total segs added   : {total_pass_improvements}")
    print(f"  Final E_slack      : {E_slack:.4f}")
    print(f"  Final utility      : {total_utility:.6f}")

    return seg_state, freq_state, total_utility


# ─────────────────────────────────────────────────────────────────────────────
#  OUTPUT
# ─────────────────────────────────────────────────────────────────────────────

_S  = "=" * 76
_S2 = "-" * 76


def print_heuristic_solution(seg_state, freq_state, mapping,
                              tasks, processors, h, cum, N_seg, B_BUDGET):
    freq_set = processors[0]['frequencies']
    N_tsk    = len(tasks)
    periods  = [int(t['p_i']) for t in tasks]
    N_job    = [h // periods[i] for i in range(N_tsk)]

    def ef(i, k, z): return cum[i][k] / freq_set[z]
    def en(i, k, z):
        c = cum[i][k]; f = freq_set[z]
        return ALPHA*(c/f) + BETA*(f**2)*c

    print(f"\n{_S}")
    print(f"  HEURISTIC SOLUTION")
    print(_S2)

    total_e = total_u = 0.0
    for i in range(N_tsk):
        u_i   = tasks[i]['u_i']
        procs = sorted({mapping.get((i,j),-1) for j in range(N_job[i])})
        print(f"\n  Task T{tasks[i]['id']}  period={tasks[i]['p_i']}  "
              f"u_i={u_i}  N_seg={N_seg[i]}  N_jobs={N_job[i]}  procs={procs}")
        print(f"  {'Job':>5}  {'Proc':>5}  {'Freq':>6}  {'k':>4}  "
              f"{'cum_work':>9}  {'e_eff':>8}  {'Energy':>10}  "
              f"{'Utility':>9}  Execution")
        print(f"  {_S2}")

        t_e = t_u = 0.0
        for j in range(N_job[i]):
            k  = seg_state[(i,j)]; z = freq_state[(i,j)]
            px = mapping.get((i,j), -1)
            e  = ef(i, k, z); en_val = en(i, k, z)
            opt = cum[i][k] - cum[i][0]; ut = u_i * opt
            t_e += en_val; t_u += ut
            seg_desc = "mandatory only" if k == 0 else f"mandatory + {k} opt seg(s)"
            print(f"  {j+1:>5}  P{px:<4}  {freq_set[z]:>6.3f}  {k:>4}  "
                  f"{cum[i][k]:>9.4f}  {e:>8.4f}  {en_val:>10.4f}  "
                  f"{ut:>9.4f}  {seg_desc}")
        total_e += t_e; total_u += t_u
        print(f"\n  {'':5}  Task T{tasks[i]['id']} totals : "
              f"energy={t_e:.4f}   utility={t_u:.4f}")

    print(f"\n{_S}")
    print(f"  Total energy  : {total_e:.4f}  "
          f"(budget={B_BUDGET}  slack={B_BUDGET-total_e:.4f})")
    print(f"  Total utility : {total_u:.6f}")
    print(_S)


# ─────────────────────────────────────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    tc_path = sys.argv[1] if len(sys.argv) > 1 else "testcase.py"
    print(f"Loading testcase: {tc_path}")
    processors, tasks, B_BUDGET = load_testcase(tc_path)

    periods  = [int(t['p_i']) for t in tasks]
    h        = lcm_list(periods)
    quantum  = gcd_list(periods)
    cum, N_seg = build_cum(tasks)
    N_tsk    = len(tasks)
    N_job    = [h // periods[i] for i in range(N_tsk)]

    # ── Instance summary ──────────────────────────────────────────────────────
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
          f"{'e_m':>9}  {'util':>7}  u_i")
    print(f"  {_S2}")
    for i, t in enumerate(tasks):
        u = t['e_m']/t['p_i']
        print(f"  {t['id']:>4}  {t['p_i']:>7}  {N_seg[i]:>5}  {N_job[i]:>6}  "
              f"{t['e_m']:>9.4f}  {u:>7.4f}  {t['u_i']}")
    feas = "FEASIBLE" if total_util <= len(processors) else "OVERLOADED"
    print(f"\n  Total utilisation : {total_util:.4f} / {len(processors)}  [{feas}]")
    print(_S)

    # ══ PHASE 1: SPS MAPPING ═════════════════════════════════════════════════
    print(f"\n{_S}")
    print(f"  PHASE 1 : QUANTUM SPS MAPPING")
    print(_S2)
    mapping = quantum_sps_mapping(tasks, processors, h, quantum)

    # ══ PHASES 2-5: HEURISTIC CORE ═══════════════════════════════════════════
    print(f"\n{_S}")
    print(f"  PHASES 2-5 : HEURISTIC CORE")
    print(_S2)
    seg_state, freq_state, utility = run_heuristic_core(
        processors, tasks, B_BUDGET, mapping)

    # ══ PRINT SOLUTION ════════════════════════════════════════════════════════
    print_heuristic_solution(seg_state, freq_state, mapping,
                             tasks, processors, h, cum, N_seg, B_BUDGET)