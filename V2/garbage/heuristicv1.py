"""
USRT Deterministic Heuristic
=============================
Type     : SPS + Search  <J, P, F, O>
Approach : Deterministic (no random moves)
Reference: Heuristic_15_04_2026.pdf + Segmented_Workload_Scheduling_Shared_v2.pdf §V

Pipeline
--------
  Phase 1 — SPS mapping
      Single-pass SPS, mandatory only at f_max.
      Load metric: utilisation e_m / p_i.
      Produces: job → processor mapping.

  Phase 2 — Aggressive frequency scaling (preprocessing)
      For each job in decreasing e_m order:
          While next-lower frequency exists:
              Tentatively scale down one level.
              If DBF still holds on that processor AND time slack ≥ 0:
                  Accept (saves energy).
              Else:
                  Revert, stop scaling this job.
      After this step energy slack = B - E_consumed is maximised
      with no utility change (obj = 0 at this point).

  Phase 3 — Greedy optional segment addition
      Sort all jobs by u_i descending (task weight, fixed order).
      For each job J* in that order:
          While J* has remaining optional segments AND energy slack > 0:
              Try adding next optional segment to J* at current frequency:
                  Check DBF on J*'s processor for all windows containing J*.
                  Check energy slack ≥ ΔE.
                  If both pass → accept, update slacks.
                  Else → try freeing moves (see below), then retry once.
                  If still blocked → move to next job.

      Freeing moves for J* (in preference order):
        (A) Inc frequency of overlapping jobs on same processor
            (reduces their e_eff → frees time slack, costs more energy)
            Try each overlapping job, increase freq by one level if:
                DBF still holds AND energy slack ≥ ΔE_freq_inc
        (B) Dec optional segments of overlapping jobs on same processor
            (reduces their e_eff → frees time slack, returns energy)
            Try each overlapping job, remove one optional segment if:
                DBF still holds (always true — less work)

Slack definitions
-----------------
  Time slack (per processor per window):
      slack_time[x][(t1,t2)] = (t2 - t1) - DBF(t1, t2, x)
      Maintained incrementally after every move.

  Energy slack (global):
      slack_energy = B - sum of E(i, k, z) for all jobs

Assumptions
-----------
  - Aggressive scaling done once at start, not re-run after each J*.
  - Greedy visits each job once; no re-visiting after moving on.
  - Freeing moves scoped to same processor, overlapping [r_{i,j}, d_{i,j}].
  - Mapping is single-pass SPS (not quantum), consistent with ILP v2 Phase 1.
"""

import sys
import importlib.util
from math import gcd as math_gcd

# ── energy model coefficients ─────────────────────────────────────────────────
# Imported from the single source of truth (usrt/models.py) so this legacy
# monolith can never drift from the rest of the project.  Previously hard-coded
# to ALPHA=1.0, BETA=0.5 -- the stale pair -- under which the energy optimum is
# f_max, whereas under the project's 0.15/1.0 it is f* ~= 0.42.  The two
# disagree about the entire DVFS trade-off, so a standalone run of this file was
# silently solving a different problem.
from usrt.models import ALPHA, BETA

# ═══════════════════════════════════════════════════════════════
#  Helpers shared with v1/v2
# ═══════════════════════════════════════════════════════════════

def lcm2(a, b):
    return a * b // math_gcd(a, b)

def hyperperiod(periods):
    h = periods[0]
    for p in periods[1:]:
        h = lcm2(h, p)
    return h

def load_testcase(path):
    spec   = importlib.util.spec_from_file_location("tc", path)
    mod    = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.testcase()

def e_eff(cum_ik, fz):
    return cum_ik / fz

def energy(cum_ik, fz):
    return ALPHA * (cum_ik / fz) + BETA * (fz ** 2) * cum_ik

# ═══════════════════════════════════════════════════════════════
#  SPS core  (same DPS + SPS as usrt_ilp_v2.py)
# ═══════════════════════════════════════════════════════════════

class _PS:
    def __init__(self, m):
        self.m     = m
        self.loads = [0.0] * m
        self.jobs  = [[] for _ in range(m)]

    @property
    def gap(self):
        return self.loads[0] - self.loads[-1]

    def _resort(self):
        paired     = sorted(zip(self.loads, self.jobs), key=lambda x: -x[0])
        self.loads = [p[0]       for p in paired]
        self.jobs  = [list(p[1]) for p in paired]

    def insert(self, jk, load):
        idx = self.loads.index(self.loads[-1])
        self.loads[idx] += load
        self.jobs[idx].append(jk)
        self._resort()


def _combine(a, b):
    m  = a.m
    ps = _PS(m)
    for j in range(m):
        ps.loads[j] = a.loads[j] + b.loads[m - 1 - j]
        ps.jobs[j]  = list(a.jobs[j]) + list(b.jobs[m - 1 - j])
    ps._resort()
    return ps


def _dps(sorted_jobs, m):
    pss = []
    for jk, load in sorted_jobs:
        if not pss:
            ps = _PS(m); ps.insert(jk, load); pss.append(ps); continue
        best = max(pss, key=lambda p: p.gap)
        if load <= best.gap:
            best.insert(jk, load)
        else:
            ps = _PS(m); ps.insert(jk, load); pss.append(ps)
    return pss


def run_sps(jobs_with_loads, m):
    if not jobs_with_loads:
        return {}
    sj  = sorted(jobs_with_loads, key=lambda x: -x[1])
    pss = _dps(sj, m)
    while len(pss) > 1:
        pss.sort(key=lambda p: -p.gap)
        pss = [_combine(pss[0], pss[1])] + pss[2:]
    final = pss[0]
    return {jk: idx for idx, jlist in enumerate(final.jobs) for jk in jlist}


# ═══════════════════════════════════════════════════════════════
#  Schedule state
# ═══════════════════════════════════════════════════════════════

class ScheduleState:
    """
    Holds the complete mutable state of the heuristic solution.

    Per-job decisions:
        freq_idx[i,j]  — index into freq_set  (current frequency level)
        seg_k[i,j]     — current segment level (0 = mandatory only)

    Slack structures (maintained incrementally):
        dbf[x][(t1,t2)]        — current demand in window on processor x
        slack_time[x][(t1,t2)] — (t2-t1) - dbf[x][(t1,t2)]
        slack_energy           — B - total energy consumed
    """

    def __init__(self, tasks, processors, cum, N_seg, N_job,
                 periods, freq_set, job_r, job_d, sps_map, B):

        self.tasks     = tasks
        self.N_tsk     = len(tasks)
        self.N_prc     = len(processors)
        self.freq_set  = freq_set
        self.N_frq     = len(freq_set)
        self.cum       = cum
        self.N_seg     = N_seg
        self.N_job     = N_job
        self.periods   = periods
        self.job_r     = job_r
        self.job_d     = job_d
        self.sps_map   = sps_map          # (i,j) → proc_idx
        self.B         = B

        # per-processor job sets
        self.proc_jobs = {x: [] for x in range(self.N_prc)}
        for (i, j), x in sps_map.items():
            self.proc_jobs[x].append((i, j))

        # initial decisions: f_max (last index), mandatory only (k=0)
        self.freq_idx = {(i, j): self.N_frq - 1
                         for i in range(self.N_tsk)
                         for j in range(N_job[i])}
        self.seg_k    = {(i, j): 0
                         for i in range(self.N_tsk)
                         for j in range(N_job[i])}

        # build DBF window set per processor and initialise demands
        self.windows   = {}    # x → list of (t1,t2)
        self.dbf       = {}    # x → {(t1,t2): demand}
        self.slack_time= {}    # x → {(t1,t2): slack}
        self._build_windows()
        self._init_dbf()

        # global energy slack
        self.slack_energy = B - self._total_energy()

    # ── window construction ──────────────────────────────────────────────────

    def _build_windows(self):
        for x in range(self.N_prc):
            jobs = self.proc_jobs[x]
            Ax   = sorted({self.job_r[(i,j)] for (i,j) in jobs})
            Dx   = sorted({self.job_d[(i,j)] for (i,j) in jobs})
            wins = [(t1, t2) for t1 in Ax for t2 in Dx if t1 < t2]
            self.windows[x]    = wins
            self.dbf[x]        = {w: 0.0 for w in wins}
            self.slack_time[x] = {}

    def _init_dbf(self):
        for x in range(self.N_prc):
            for (t1, t2) in self.windows[x]:
                d = sum(
                    e_eff(self.cum[i][self.seg_k[(i,j)]],
                          self.freq_set[self.freq_idx[(i,j)]])
                    for (i,j) in self.proc_jobs[x]
                    if self.job_r[(i,j)] >= t1 and self.job_d[(i,j)] <= t2
                )
                self.dbf[x][(t1,t2)]         = d
                self.slack_time[x][(t1,t2)]  = (t2 - t1) - d

    # ── energy helpers ───────────────────────────────────────────────────────

    def _job_energy(self, i, j):
        return energy(self.cum[i][self.seg_k[(i,j)]],
                      self.freq_set[self.freq_idx[(i,j)]])

    def _total_energy(self):
        return sum(self._job_energy(i, j)
                   for i in range(self.N_tsk)
                   for j in range(self.N_job[i]))

    # ── windows that contain a given job ────────────────────────────────────

    def windows_of(self, i, j):
        x = self.sps_map[(i, j)]
        r, d = self.job_r[(i,j)], self.job_d[(i,j)]
        return [(t1, t2) for (t1, t2) in self.windows[x]
                if t1 <= r and t2 >= d]

    # ── overlapping jobs on same processor ──────────────────────────────────

    def overlapping_jobs(self, i, j):
        """
        All jobs on same processor as (i,j) whose [r,d] overlaps [r_{i,j}, d_{i,j}].
        Excludes (i,j) itself.
        """
        x  = self.sps_map[(i, j)]
        r0 = self.job_r[(i, j)]
        d0 = self.job_d[(i, j)]
        return [
            (ii, jj) for (ii, jj) in self.proc_jobs[x]
            if (ii, jj) != (i, j)
            and self.job_r[(ii,jj)] < d0
            and self.job_d[(ii,jj)] > r0
        ]

    # ── slack check ─────────────────────────────────────────────────────────

    def min_slack_in_windows(self, i, j):
        """Minimum time slack across all windows containing job (i,j)."""
        wins = self.windows_of(i, j)
        if not wins:
            return float('inf')
        x = self.sps_map[(i, j)]
        return min(self.slack_time[x][w] for w in wins)

    # ── incremental DBF update after a job's e_eff changes ──────────────────

    def _update_dbf_for_job(self, i, j, old_eeff, new_eeff):
        x     = self.sps_map[(i, j)]
        delta = new_eeff - old_eeff
        for (t1, t2) in self.windows_of(i, j):
            self.dbf[x][(t1,t2)]        += delta
            self.slack_time[x][(t1,t2)] -= delta

    # ── atomic moves (return True if applied, False if rejected) ────────────

    def try_inc_seg(self, i, j):
        """
        Try adding one optional segment to job (i,j) at current frequency.
        Checks: all containing windows have enough time slack + energy slack.
        """
        k_cur = self.seg_k[(i, j)]
        if k_cur >= self.N_seg[i]:
            return False                        # already at max segments

        z_cur    = self.freq_idx[(i, j)]
        fz       = self.freq_set[z_cur]
        old_cum  = self.cum[i][k_cur]
        new_cum  = self.cum[i][k_cur + 1]
        old_eeff = e_eff(old_cum, fz)
        new_eeff = e_eff(new_cum, fz)
        delta_e  = energy(new_cum, fz) - energy(old_cum, fz)

        # energy check
        if delta_e > self.slack_energy + 1e-9:
            return False

        # time slack check — must remain ≥ 0 in every containing window
        x = self.sps_map[(i, j)]
        for (t1, t2) in self.windows_of(i, j):
            if self.slack_time[x][(t1,t2)] - (new_eeff - old_eeff) < -1e-9:
                return False

        # apply
        self.seg_k[(i, j)]  = k_cur + 1
        self._update_dbf_for_job(i, j, old_eeff, new_eeff)
        self.slack_energy   -= delta_e
        return True

    def try_dec_seg(self, i, j):
        """Remove one optional segment from job (i,j). Always succeeds if k>0."""
        k_cur = self.seg_k[(i, j)]
        if k_cur == 0:
            return False

        z_cur    = self.freq_idx[(i, j)]
        fz       = self.freq_set[z_cur]
        old_cum  = self.cum[i][k_cur]
        new_cum  = self.cum[i][k_cur - 1]
        old_eeff = e_eff(old_cum, fz)
        new_eeff = e_eff(new_cum, fz)
        delta_e  = energy(new_cum, fz) - energy(old_cum, fz)   # negative

        self.seg_k[(i, j)]  = k_cur - 1
        self._update_dbf_for_job(i, j, old_eeff, new_eeff)
        self.slack_energy   -= delta_e      # slack increases
        return True

    def try_dec_freq(self, i, j):
        """
        Scale frequency of job (i,j) down by one level.
        Checks: all containing windows still have time slack ≥ 0.
        """
        z_cur = self.freq_idx[(i, j)]
        if z_cur == 0:
            return False                        # already at minimum frequency

        k_cur    = self.seg_k[(i, j)]
        old_fz   = self.freq_set[z_cur]
        new_fz   = self.freq_set[z_cur - 1]
        cum_ik   = self.cum[i][k_cur]
        old_eeff = e_eff(cum_ik, old_fz)
        new_eeff = e_eff(cum_ik, new_fz)
        delta_e  = energy(cum_ik, new_fz) - energy(cum_ik, old_fz)  # negative

        # time slack check
        x = self.sps_map[(i, j)]
        for (t1, t2) in self.windows_of(i, j):
            if self.slack_time[x][(t1,t2)] - (new_eeff - old_eeff) < -1e-9:
                return False

        # apply
        self.freq_idx[(i, j)] = z_cur - 1
        self._update_dbf_for_job(i, j, old_eeff, new_eeff)
        self.slack_energy    -= delta_e     # slack increases (delta_e < 0)
        return True

    def try_inc_freq(self, i, j):
        """
        Increase frequency of job (i,j) by one level (frees time, costs energy).
        """
        z_cur = self.freq_idx[(i, j)]
        if z_cur >= self.N_frq - 1:
            return False

        k_cur    = self.seg_k[(i, j)]
        old_fz   = self.freq_set[z_cur]
        new_fz   = self.freq_set[z_cur + 1]
        cum_ik   = self.cum[i][k_cur]
        old_eeff = e_eff(cum_ik, old_fz)
        new_eeff = e_eff(cum_ik, new_fz)
        delta_e  = energy(cum_ik, new_fz) - energy(cum_ik, old_fz)  # positive

        if delta_e > self.slack_energy + 1e-9:
            return False

        self.freq_idx[(i, j)] = z_cur + 1
        self._update_dbf_for_job(i, j, old_eeff, new_eeff)
        self.slack_energy    -= delta_e
        return True


# ═══════════════════════════════════════════════════════════════
#  Phase 2 — Aggressive frequency scaling
# ═══════════════════════════════════════════════════════════════

def aggressive_freq_scaling(state: ScheduleState):
    """
    Scale down frequency of every job as far as possible.
    Order: decreasing e_m (heaviest jobs first — they save most energy).
    Stopping condition per job: revert if next scale-down would violate DBF.
    """
    all_jobs = [
        (i, j)
        for i in range(state.N_tsk)
        for j in range(state.N_job[i])
    ]
    # sort by e_m descending
    all_jobs.sort(key=lambda ij: -state.tasks[ij[0]]["e_m"])

    scaled = 0
    for (i, j) in all_jobs:
        while state.try_dec_freq(i, j):
            scaled += 1

    print(f"  Aggressive scaling: {scaled} frequency reductions applied")
    print(f"  Energy slack after scaling: {state.slack_energy:.4f}")


# ═══════════════════════════════════════════════════════════════
#  Phase 3 — Greedy optional segment addition
# ═══════════════════════════════════════════════════════════════

def greedy_optional_segments(state: ScheduleState):
    """
    Visit jobs in decreasing u_i order.
    For each J*: keep adding optional segments until maxed or blocked.
    On block: try freeing moves on overlapping jobs (inc freq first, then dec seg).
    """
    # build job list sorted by u_i descending (fixed order, no re-sorting)
    job_order = [
        (i, j)
        for i in range(state.N_tsk)
        for j in range(state.N_job[i])
    ]
    job_order.sort(key=lambda ij: -state.tasks[ij[0]]["u_i"])

    total_segs_added = 0

    for (i, j) in job_order:
        added_this_job = 0

        while True:
            # check if J* can still gain segments
            if state.seg_k[(i, j)] >= state.N_seg[i]:
                break   # maxed out
            if state.slack_energy <= 1e-9:
                break   # global energy exhausted

            # attempt direct addition
            if state.try_inc_seg(i, j):
                added_this_job  += 1
                total_segs_added += 1
                continue

            # direct addition failed — try freeing moves
            freed = False
            overlapping = state.overlapping_jobs(i, j)

            # (A) try inc freq on each overlapping job (frees time, costs energy)
            for (ii, jj) in overlapping:
                if state.try_inc_freq(ii, jj):
                    freed = True
                    break

            # (B) if still not freed, try dec seg on each overlapping job
            if not freed:
                for (ii, jj) in overlapping:
                    if state.seg_k[(ii, jj)] > 0:
                        if state.try_dec_seg(ii, jj):
                            freed = True
                            break

            if not freed:
                break   # cannot free any room for J* — move to next job

            # retry J* addition after freeing
            if not state.try_inc_seg(i, j):
                break   # freeing helped slacks but still not enough

            added_this_job  += 1
            total_segs_added += 1

        if added_this_job > 0:
            print(f"  J*=T{state.tasks[i]['id']},job{j+1}: "
                  f"+{added_this_job} seg(s) → k={state.seg_k[(i,j)]}  "
                  f"f={state.freq_set[state.freq_idx[(i,j)]]:.2f}  "
                  f"E_slack={state.slack_energy:.3f}")

    print(f"\n  Total optional segments added: {total_segs_added}")


# ═══════════════════════════════════════════════════════════════
#  Main solver
# ═══════════════════════════════════════════════════════════════

def solve(processors, tasks, B_BUDGET):
    N_tsk    = len(tasks)
    N_prc    = len(processors)
    freq_set = processors[0]["frequencies"]
    N_frq    = len(freq_set)

    # cumulative exec time table
    cum, N_seg = [], []
    for t in tasks:
        execs = [t["e_m"]] + list(t["e_o_k"])
        row, s = [], 0.0
        for e in execs:
            s += e; row.append(s)
        cum.append(row)
        N_seg.append(len(t["e_o_k"]))

    periods = [int(t["p_i"]) for t in tasks]
    h       = hyperperiod(periods)
    N_job   = [h // periods[i] for i in range(N_tsk)]
    job_r   = {(i,j): j*periods[i]     for i in range(N_tsk) for j in range(N_job[i])}
    job_d   = {(i,j): (j+1)*periods[i] for i in range(N_tsk) for j in range(N_job[i])}

    _print_header(tasks, processors, freq_set, B_BUDGET, h, N_job, N_seg)

    # ── Phase 1: SPS mapping ─────────────────────────────────────────────────
    print(f"\n{'─'*60}")
    print("  PHASE 1 — SPS Mapping (mandatory only, f_max)")
    print(f"{'─'*60}")
    job_loads = [(( i, j), tasks[i]["e_m"] / periods[i])
                 for i in range(N_tsk) for j in range(N_job[i])]
    sps_map   = run_sps(job_loads, N_prc)

    # print mapping summary
    proc_jobs = {x: [] for x in range(N_prc)}
    for (i,j), x in sps_map.items():
        proc_jobs[x].append((i, j))
    for x in range(N_prc):
        util = sum(tasks[i]["e_m"]/periods[i] for (i,j) in proc_jobs[x])
        print(f"  P{x}: {len(proc_jobs[x]):>4} jobs   utilisation={util:.4f}")

    # ── build schedule state ─────────────────────────────────────────────────
    state = ScheduleState(
        tasks, processors, cum, N_seg, N_job,
        periods, freq_set, job_r, job_d, sps_map, B_BUDGET
    )
    print(f"\n  Initial energy consumed : "
          f"{B_BUDGET - state.slack_energy:.4f}  "
          f"(slack={state.slack_energy:.4f})")

    # ── Phase 2: aggressive frequency scaling ────────────────────────────────
    print(f"\n{'─'*60}")
    print("  PHASE 2 — Aggressive Frequency Scaling")
    print(f"{'─'*60}")
    aggressive_freq_scaling(state)

    # ── Phase 3: greedy optional segment addition ────────────────────────────
    print(f"\n{'─'*60}")
    print("  PHASE 3 — Greedy Optional Segment Addition")
    print(f"{'─'*60}")
    greedy_optional_segments(state)

    # ── print solution ───────────────────────────────────────────────────────
    _print_solution(state, tasks, N_tsk, N_job, N_seg,
                    N_prc, freq_set, cum, B_BUDGET, periods)
    return state


# ═══════════════════════════════════════════════════════════════
#  Output
# ═══════════════════════════════════════════════════════════════

_SEP  = "=" * 76
_SEP2 = "-" * 76

def _print_header(tasks, processors, freq_set, B, h, N_job, N_seg):
    print(f"\n{_SEP}")
    print("  USRT Deterministic Heuristic — Instance Summary")
    print(_SEP2)
    print(f"  Processors   : {len(processors)}")
    print(f"  Frequencies  : {freq_set}")
    print(f"  Energy budget: {B}    alpha={ALPHA}   beta={BETA}")
    print(f"  Hyper-period : {h}")
    print(_SEP2)
    print(f"  {'TID':>4}  {'period':>7}  {'N_seg':>6}  {'N_jobs':>7}  "
          f"{'e_m':>9}  {'u_i':>5}  e_o_k")
    print(f"  {_SEP2}")
    for i, t in enumerate(tasks):
        print(f"  {t['id']:>4}  {t['p_i']:>7}  {N_seg[i]:>6}  {N_job[i]:>7}  "
              f"{t['e_m']:>9.4f}  {t['u_i']:>5.2f}  "
              f"{[round(x,4) for x in t['e_o_k']]}")
    print(_SEP)


def _print_solution(state, tasks, N_tsk, N_job, N_seg,
                    N_prc, freq_set, cum, B_BUDGET, periods):
    print(f"\n{_SEP}")
    print("  HEURISTIC SOLUTION")
    print(_SEP2)

    total_energy = total_utility = 0.0

    for i in range(N_tsk):
        u_i = tasks[i]["u_i"]
        print(f"\n  ── Task T{tasks[i]['id']}  "
              f"(period={tasks[i]['p_i']}, u_i={u_i}, "
              f"N_seg={N_seg[i]}, N_jobs={N_job[i]}) ──")
        print(f"  {'Job':>5}  {'Proc':>5}  {'Freq':>6}  {'k':>4}  "
              f"{'cum_work':>9}  {'e_eff':>8}  {'Energy':>10}  "
              f"{'Utility':>9}  Segments")
        print(f"  {_SEP2}")

        task_e = task_u = 0.0
        for j in range(N_job[i]):
            x    = state.sps_map[(i, j)]
            z    = state.freq_idx[(i, j)]
            k    = state.seg_k[(i, j)]
            fz   = freq_set[z]
            ck   = cum[i][k]
            ef   = e_eff(ck, fz)
            en   = energy(ck, fz)
            opt  = ck - cum[i][0]
            ut   = u_i * opt
            task_e += en; task_u += ut
            seg_desc = "mandatory only" if k == 0 else f"mand + {k} opt"
            print(f"  {j+1:>5}  {'P'+str(x):>5}  {fz:>6.3f}  {k:>4}  "
                  f"{ck:>9.4f}  {ef:>8.4f}  {en:>10.4f}  "
                  f"{ut:>9.4f}  {seg_desc}")

        total_energy += task_e; total_utility += task_u
        print(f"\n  Task T{tasks[i]['id']} totals:"
              f"  energy={task_e:.4f}   utility={task_u:.4f}")

    # verify DBF feasibility
    feasible = all(
        state.slack_time[x][w] >= -1e-6
        for x in range(N_prc)
        for w in state.windows[x]
    )

    print(f"\n{_SEP}")
    print(f"  Total energy used : {total_energy:.4f} / {B_BUDGET}"
          f"  (slack={B_BUDGET-total_energy:.4f})")
    print(f"  Total utility     : {total_utility:.6f}")
    print(f"  DBF feasible      : {feasible}")
    print(_SEP)


# ═══════════════════════════════════════════════════════════════
#  Entry point
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    tc_path = sys.argv[1] if len(sys.argv) > 1 else "testcase.py"
    print(f"Loading testcase from: {tc_path}")
    processors, tasks, B_BUDGET = load_testcase(tc_path)
    solve(processors, tasks, B_BUDGET)