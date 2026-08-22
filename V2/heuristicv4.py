"""
USRT Heuristic  —  Combined Deterministic
==========================================
Design choices (hybrid of two versions):

  ✓  1 segment per j* per outer pass      (old approach)
  ✓  Timing via DBF window slack           (new: min_slack_containing_job)
  ✓  No extra DBF call in Case (i)         (new: min_slack check is sufficient)
  ✓  No left-shift recompute inside loop   (new: min_slack queries fresh state)
  ✓  Phase 4: decrease freq + energy guard (new: correct DVFS direction)
  ✓  Case (ii.B): dec freq others + guard  (new: energy-saving direction)
  ✓  Stable sort                           (new: deterministic tie-breaking)

WHY 1 SEGMENT PER PASS
-----------------------
Allowing unlimited segments per j* in one pass (inner while) greedily saturates
the highest-utility job before others get a chance. With 1 segment per pass,
every job gets one opportunity per iteration, and the outer while loop repeats
until no further improvement. This is fairer and may allow lower-priority jobs
to unlock timing slack that benefits higher-priority jobs in the next pass.

TIMING CHECK
------------
min_slack_containing_job(i,j,x) = min over all DBF windows [t1,t2] that
contain job (i,j) (i.e. t1 ≤ r_{i,j} and t2 ≥ d_{i,j}) of:
    (t2 - t1) - Σ_{jobs in window} e_eff(i',k',z')

If this ≥ add_time, adding add_time more execution to (i,j) keeps all
containing windows feasible. No separate DBF call needed for Case (i).

ALGORITHM (per outer pass)
--------------------------
  For each j* in stable descending u_i order:
    Try to add ONE optional segment.

    Case (i)   — No impact on others:
                 min_slack_containing(j*) ≥ add_time  AND  E_slack ≥ add_energy
                 → add segment (no extra DBF call needed)

    Case (ii.A)— Inc freq of j* (shorter exec, saves energy in our model):
                 Try z* → z*+1. Net time change dt, net energy change de.
                 Pre-check: min_slack - dt ≥ 0  AND  E_slack ≥ de
                 Full DBF check for safety. Commit if OK.

    Case (ii.B)— Dec freq of others on same proc (to save energy):
                 Only if energy_saved > 0 for that other job.
                 Check other job's own timing after freq reduction.
                 Check combined energy allows j*'s new segment.
                 Full DBF check. Commit if OK.

  Outer while: repeat until a full pass adds nothing.

Testcase : testcaase.py  →  processors, tasks, B_BUDGET
Energy   : E = α·(Σe_q/f) + β·f²·Σe_q   with α=ALPHA, β=BETA
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
    for x in lst[1:]: r = _gcd(r, int(x))
    return r

def lcm2(a, b):
    a, b = int(a), int(b); return a * b // _gcd(a, b)

def lcm_list(lst):
    r = int(lst[0])
    for x in lst[1:]: r = lcm2(r, int(x))
    return r

def build_cum(tasks):
    """cum[i][k] = e_{i,0}+…+e_{i,k}  (f_max; k=0 → mandatory only)."""
    cum, N_seg = [], []
    for t in tasks:
        segs = [t['e_m']] + list(t['e_o_k'])
        row, s = [], 0.0
        for e in segs: s += e; row.append(s)
        cum.append(row); N_seg.append(len(t['e_o_k']))
    return cum, N_seg

def generate_jobs(tasks, h):
    jobs = []
    for i, t in enumerate(tasks):
        p = int(t['p_i']); n = h // p
        for j in range(n): jobs.append((i, j, j*p, (j+1)*p))
    return jobs

def energy_val(cum_k, fz):
    """E = α·cum_k/fz + β·fz²·cum_k"""
    return ALPHA * cum_k / fz + BETA * fz**2 * cum_k

def e_eff_val(cum_k, fz):
    return cum_k / fz


# ══════════════════════════════════════════════════════════════════════════════
#  SPS / DPS
# ══════════════════════════════════════════════════════════════════════════════

class PS:
    __slots__ = ('m', 'loads', 'assign', 'gap')

    def __init__(self, m):
        self.m = m; self.loads = [0.0]*m
        self.assign = [set() for _ in range(m)]; self.gap = 0.0

    @classmethod
    def singleton(cls, m, key, val):
        ps = cls(m); ps.loads[0] = val
        ps.assign[0].add(key); ps.gap = val; return ps

    def _resort(self):
        p = sorted(zip(self.loads, self.assign), key=lambda x: -x[0])
        self.loads  = [x[0] for x in p]
        self.assign = [x[1] for x in p]
        self.gap    = self.loads[0] - self.loads[-1]

    def insert(self, key, val):
        self.loads[-1] += val; self.assign[-1].add(key); self._resort()

    def combine(self, other):
        m = self.m
        raw = [(self.loads[j] + other.loads[m-1-j],
                self.assign[j] | other.assign[m-1-j]) for j in range(m)]
        raw.sort(key=lambda x: -x[0])
        ps = PS(m); ps.loads = [r[0] for r in raw]
        ps.assign = [r[1] for r in raw]
        ps.gap = ps.loads[0] - ps.loads[-1]; return ps


def run_dps(jl, m):
    if not jl: return []
    k0, v0 = jl[0]; active = [PS.singleton(m, k0, v0)]
    for key, val in jl[1:]:
        best = max(range(len(active)), key=lambda i: active[i].gap)
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


# ══════════════════════════════════════════════════════════════════════════════
#  DBF HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def window_slack(x, t1, t2, proc_jobs, job_r, job_d, seg_k, freq_idx, freq_set, cum):
    """
    DBF slack in window [t1,t2] on processor x.
    = (t2-t1) - demand,  where demand = Σ e_eff of jobs in S(t1,t2,x).
    """
    window = [(i,j) for (i,j) in proc_jobs[x]
              if job_r[(i,j)] >= t1 and job_d[(i,j)] <= t2]
    if not window: return t2 - t1
    demand = sum(e_eff_val(cum[i][seg_k[(i,j)]], freq_set[freq_idx[(i,j)]])
                 for (i,j) in window)
    return (t2 - t1) - demand


def min_slack_for_job(i_s, j_s, x, proc_jobs, job_r, job_d,
                      seg_k, freq_idx, freq_set, cum):
    """
    Minimum DBF slack across all windows that CONTAIN job (i_s,j_s).
    A window [t1,t2] contains (i_s,j_s) iff t1 ≤ r_{i_s,j_s} AND t2 ≥ d_{i_s,j_s}.

    If this value ≥ add_time, adding add_time to (i_s,j_s) keeps all
    containing windows feasible — no separate DBF call required.
    """
    r_ij = job_r[(i_s, j_s)]; d_ij = job_d[(i_s, j_s)]
    Ax = sorted({job_r[ij] for ij in proc_jobs[x]})
    Dx = sorted({job_d[ij] for ij in proc_jobs[x]})
    min_sl = float('inf')
    for t1 in Ax:
        if t1 > r_ij: continue          # need t1 ≤ r so job is in window
        for t2 in Dx:
            if t2 < d_ij: continue      # need t2 ≥ d so job is in window
            if t1 >= t2: continue
            sl = window_slack(x, t1, t2, proc_jobs, job_r, job_d,
                              seg_k, freq_idx, freq_set, cum)
            if sl < min_sl: min_sl = sl
    return min_sl if min_sl < float('inf') else (d_ij - r_ij)


def check_all_timing(proc_jobs, job_r, job_d, seg_k, freq_idx, freq_set, cum, N_prc):
    """Full DBF check across all processors and windows."""
    for x in range(N_prc):
        if not proc_jobs[x]: continue
        Ax = sorted({job_r[ij] for ij in proc_jobs[x]})
        Dx = sorted({job_d[ij] for ij in proc_jobs[x]})
        for t1 in Ax:
            for t2 in Dx:
                if t1 >= t2: continue
                if window_slack(x, t1, t2, proc_jobs, job_r, job_d,
                                seg_k, freq_idx, freq_set, cum) < -1e-9:
                    return False
    return True


def total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job):
    return sum(energy_val(cum[i][seg_k[(i,j)]], freq_set[freq_idx[(i,j)]])
               for i in range(N_tsk) for j in range(N_job[i]))


def total_utility(seg_k, tasks, cum, N_tsk, N_job):
    return sum(tasks[i]['u_i'] * (cum[i][seg_k[(i,j)]] - cum[i][0])
               for i in range(N_tsk) for j in range(N_job[i]))


# ══════════════════════════════════════════════════════════════════════════════
#  QUANTUM SPS MAPPING  (Phase 1, identical to ILP v2)
# ══════════════════════════════════════════════════════════════════════════════

def _check_dbf_mandatory(mapping, tasks, processors, h):
    N_tsk = len(tasks); N_prc = len(processors)
    periods = [int(t['p_i']) for t in tasks]
    N_job   = [h//periods[i] for i in range(N_tsk)]
    job_r   = {(i,j): j*periods[i]     for i in range(N_tsk) for j in range(N_job[i])}
    job_d   = {(i,j): (j+1)*periods[i] for i in range(N_tsk) for j in range(N_job[i])}
    pj = defaultdict(list)
    for (i,j),x in mapping.items(): pj[x].append((i,j))
    viols = {}
    for x in range(N_prc):
        if not pj[x]: continue
        Ax = sorted({job_r[ij] for ij in pj[x]})
        Dx = sorted({job_d[ij] for ij in pj[x]})
        for t1 in Ax:
            for t2 in Dx:
                if t1 >= t2: continue
                win = [(i,j) for (i,j) in pj[x]
                       if job_r[(i,j)] >= t1 and job_d[(i,j)] <= t2]
                if not win: continue
                dem = sum(tasks[i]['e_m'] for (i,j) in win)
                if dem > t2-t1+1e-9: viols.setdefault(x,[]).append((t1,t2,dem,t2-t1))
    return len(viols)==0, viols


def _repair(mapping, tasks, processors, h):
    N_tsk = len(tasks); m = len(processors)
    periods = [int(t['p_i']) for t in tasks]
    N_job   = [h//periods[i] for i in range(N_tsk)]
    job_r   = {(i,j): j*periods[i]     for i in range(N_tsk) for j in range(N_job[i])}
    job_d   = {(i,j): (j+1)*periods[i] for i in range(N_tsk) for j in range(N_job[i])}
    for _ in range(100):
        ok, viols = _check_dbf_mandatory(mapping, tasks, processors, h)
        if ok: return mapping, True
        worst = max(((x,t1,t2,d,c) for x,vl in viols.items()
                     for (t1,t2,d,c) in vl), key=lambda v: v[3]-v[4])
        x_bad,t1_b,t2_b = worst[0],worst[1],worst[2]
        off = [(i,j) for (i,j),px in mapping.items()
               if px==x_bad and job_r[(i,j)]>=t1_b and job_d[(i,j)]<=t2_b]
        if not off: break
        mi,mj = max(off, key=lambda ij: tasks[ij[0]]['e_m'])
        util = defaultdict(float)
        for (i,j),px in mapping.items(): util[px]+=tasks[i]['e_m']/tasks[i]['p_i']
        tgt = min((x for x in range(m) if x!=x_bad), key=lambda x: util[x])
        mapping[(mi,mj)] = tgt
    return mapping, _check_dbf_mandatory(mapping,tasks,processors,h)[0]


def quantum_sps_mapping(tasks, processors, h, quantum):
    m = len(processors); all_jobs = generate_jobs(tasks,h)
    by_arr = defaultdict(list)
    for job in all_jobs: by_arr[job[2]].append(job)
    mapping = {}; proc_util = [0.0]*m; leftover = []

    print(f"  {'Quantum':^12}  {'Mand':>5}  {'Opt':>5}  "
          f"{'Actv':>5}  {'Defr':>5}  {'MaxUtil':>9}  Status")
    print(f"  {'─'*68}")

    for q_start in range(0, h, quantum):
        q_end = q_start+quantum; newly = by_arr.get(q_start,[]); leftover_ = []
        pending = leftover+newly; leftover = []
        if not pending: continue

        mandatory = [(i,j,r,d) for (i,j,r,d) in pending if d==q_end]
        optional  = [(i,j,r,d) for (i,j,r,d) in pending if d>q_end]
        optional.sort(key=lambda x: x[3])
        n_m=len(mandatory); n_o=len(optional)
        active=mandatory+optional; final_ps=None; deferred=0; status="OK"

        while True:
            if not active: status="EMPTY"; break
            total_u=sum(tasks[i]['e_m']/tasks[i]['p_i'] for (i,j,r,d) in active)
            rem_cap=sum(1.0-proc_util[x] for x in range(m))
            if total_u > rem_cap+1e-9:
                opt=[v for v in active if v[3]>q_end]
                if not opt: status="MAND_OVER"; break
                td=max(opt,key=lambda x: x[3]); active.remove(td)
                leftover.append(td); deferred+=1; continue

            jl=sorted([((i,j),tasks[i]['e_m']/tasks[i]['p_i'])
                        for (i,j,r,d) in active],key=lambda x:-x[1])
            res=run_sps(run_dps(jl,m))
            if res is None: status="SPS_NONE"; break

            nu=list(proc_util)
            for px,js in enumerate(res.assign):
                for (i,j) in js: nu[px]+=tasks[i]['e_m']/tasks[i]['p_i']
            if max(nu)<=1.0+1e-9:
                final_ps=res; proc_util=nu; status=f"util={max(nu):.3f}"; break
            opt=[v for v in active if v[3]>q_end]
            if not opt:
                final_ps=res; proc_util=nu; status=f"OVER({max(nu):.3f})"; break
            td=max(opt,key=lambda x:x[3]); active.remove(td)
            leftover.append(td); deferred+=1

        print(f"  [{q_start:>4},{q_end:>4}]  {n_m:>5}  {n_o:>5}  "
              f"{len(active):>5}  {deferred:>5}  {max(proc_util):>9.4f}  {status}")
        if final_ps:
            for px,js in enumerate(final_ps.assign):
                for (i,j) in js: mapping[(i,j)]=px

    for (i,j,r,d) in leftover:
        px=min(range(m),key=lambda x:proc_util[x])
        mapping[(i,j)]=px; proc_util[px]+=tasks[i]['e_m']/tasks[i]['p_i']
    exp={(i,j) for (i,j,r,d) in generate_jobs(tasks,h)}
    for (i,j) in sorted(exp-set(mapping.keys())):
        px=min(range(m),key=lambda x:proc_util[x])
        mapping[(i,j)]=px; proc_util[px]+=tasks[i]['e_m']/tasks[i]['p_i']
    ok,viols=_check_dbf_mandatory(mapping,tasks,processors,h)
    if not ok:
        n_v=sum(len(v) for v in viols.values())
        print(f"\n  DBF: {n_v} violation(s) → repair…")
        mapping,rep=_repair(mapping,tasks,processors,h)
        print(f"  Repair: {'OK ✓' if rep else 'PARTIAL'}")
    else:
        print(f"\n  DBF: FEASIBLE ✓")
    return mapping


# ══════════════════════════════════════════════════════════════════════════════
#  PHASE 2 : LEFT SHIFT  (one-time; for initial slack reporting only)
# ══════════════════════════════════════════════════════════════════════════════

def left_shift(proc_jobs, job_r, job_d, seg_k, freq_idx, freq_set, cum):
    """
    Non-preemptive EDF-order simulation per processor.
    Used ONCE after Phase 1 for diagnostic reporting.
    NOT recomputed inside the optimisation loop.
    """
    ls_slack = {}
    for x, jobs in proc_jobs.items():
        jobs_edf   = sorted(jobs, key=lambda ij: job_d[ij])
        proc_avail = 0.0
        for (i,j) in jobs_edf:
            ef    = e_eff_val(cum[i][seg_k[(i,j)]], freq_set[freq_idx[(i,j)]])
            start = max(proc_avail, float(job_r[(i,j)]))
            ls_slack[(i,j)] = job_d[(i,j)] - (start + ef)
            proc_avail      = start + ef
    return ls_slack


# ══════════════════════════════════════════════════════════════════════════════
#  PHASE 4 : AGGRESSIVE SCALING  (freq ↓, energy guard)
# ══════════════════════════════════════════════════════════════════════════════

def phase_aggressive_scaling(seg_k, freq_idx, freq_set, N_frq, cum,
                              N_tsk, N_job, proc_jobs, job_r, job_d, N_prc):
    """
    Iteratively decrease frequency of each job by one level.
    Commits only if:
      (a) energy strictly decreases  (E_new < E_cur)
      (b) timing still feasible across all DBF windows

    With α=1, β=0.5 the energy minimum is at f_max, so this phase is a
    no-op for the default testcase. With different α,β (e.g. dynamic-power-
    dominated systems where lower freq saves energy), it actively fires.
    """
    n_scaled = 0; changed = True
    while changed:
        changed = False
        for i in range(N_tsk):
            for j in range(N_job[i]):
                z_cur = freq_idx[(i,j)]
                if z_cur == 0: continue
                z_new = z_cur - 1
                E_cur = energy_val(cum[i][seg_k[(i,j)]], freq_set[z_cur])
                E_new = energy_val(cum[i][seg_k[(i,j)]], freq_set[z_new])
                if E_new >= E_cur - 1e-12: continue     # no energy saving → skip
                freq_idx[(i,j)] = z_new
                if check_all_timing(proc_jobs, job_r, job_d, seg_k,
                                    freq_idx, freq_set, cum, N_prc):
                    changed = True; n_scaled += 1
                else:
                    freq_idx[(i,j)] = z_cur              # revert
    return n_scaled


# ══════════════════════════════════════════════════════════════════════════════
#  PHASE 5 : OPTIONAL SEGMENT SCHEDULING
# ══════════════════════════════════════════════════════════════════════════════

def phase_optional_segments(seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
                             N_tsk, N_job, proc_jobs, job_r, job_d,
                             tasks, N_prc, B_BUDGET):
    """
    ONE segment per j* per outer pass.  Outer loop repeats until no improvement.

    Timing gate : min_slack_for_job  (DBF window slack — no extra DBF call)
    Case (i)    : no impact on others
    Case (ii.A) : inc freq of j* (saves time and energy in our model)
    Case (ii.B) : dec freq of others (only if saves their energy + timing OK)
    """
    E_slack = B_BUDGET - total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job)

    # Stable sort: descending u_i, then task index, then job index
    sorted_jobs = sorted(
        [(i,j) for i in range(N_tsk) for j in range(N_job[i])],
        key=lambda ij: (-tasks[ij[0]]['u_i'], ij[0], ij[1])
    )

    log = []; pass_num = 0

    while True:
        pass_num += 1; improved = False

        for (i_s, j_s) in sorted_jobs:

            k_cur = seg_k[(i_s, j_s)]
            if k_cur >= N_seg[i_s]: continue      # already maxed out

            z_cur  = freq_idx[(i_s, j_s)]
            f_cur  = freq_set[z_cur]
            x_s    = proc_jobs_map[(i_s, j_s)]    # processor

            # Incremental cost of one more optional segment at current freq
            add_time   = (cum[i_s][k_cur+1] - cum[i_s][k_cur]) / f_cur
            add_energy = (energy_val(cum[i_s][k_cur+1], f_cur) -
                          energy_val(cum[i_s][k_cur],   f_cur))

            # Minimum DBF slack across all windows containing this job
            min_sl = min_slack_for_job(i_s, j_s, x_s, proc_jobs, job_r, job_d,
                                       seg_k, freq_idx, freq_set, cum)

            # ── CASE (i): no impact on others ────────────────────────────────
            # min_sl ≥ add_time is provably sufficient; no extra DBF call needed.
            if min_sl >= add_time - 1e-9 and E_slack >= add_energy - 1e-9:
                seg_k[(i_s, j_s)] = k_cur + 1
                E_slack           -= add_energy
                improved           = True
                log.append(f"  Pass {pass_num}: T{tasks[i_s]['id']},j{j_s}"
                           f"  k:{k_cur}→{k_cur+1}  [i]  E_slack={E_slack:.3f}")
                continue   # ONE segment added → move to next j*

            added = False

            # ── CASE (ii.A): increase freq of j* ─────────────────────────────
            # Inc freq → shorter execution, LESS energy (in our α=1,β=0.5 model)
            if z_cur < N_frq - 1:
                z_try  = z_cur + 1
                f_try  = freq_set[z_try]
                # Net time change: running k+1 segs at f_try vs k segs at f_cur
                dt = e_eff_val(cum[i_s][k_cur+1], f_try) \
                   - e_eff_val(cum[i_s][k_cur],   f_cur)
                # Net energy change
                de = energy_val(cum[i_s][k_cur+1], f_try) \
                   - energy_val(cum[i_s][k_cur],   f_cur)
                # Quick pre-check before full DBF
                if min_sl - dt >= -1e-9 and E_slack - de >= -1e-9:
                    freq_idx[(i_s, j_s)] = z_try
                    seg_k[(i_s, j_s)]    = k_cur + 1
                    if check_all_timing(proc_jobs, job_r, job_d, seg_k,
                                        freq_idx, freq_set, cum, N_prc):
                        E_slack -= de; improved = True; added = True
                        log.append(f"  Pass {pass_num}: T{tasks[i_s]['id']},j{j_s}"
                                   f"  k:{k_cur}→{k_cur+1} z:{z_cur}→{z_try}"
                                   f"  [ii.A]  E_slack={E_slack:.3f}")
                    else:
                        freq_idx[(i_s, j_s)] = z_cur   # revert
                        seg_k[(i_s, j_s)]    = k_cur

            # ── CASE (ii.B): dec freq of others to save energy ───────────────
            # Only proceeds if decrementing OTHER job's freq actually saves energy.
            # In our model (min E at f_max), this fires only if Phase 4 reduced
            # some jobs below f_max and there is still room to go lower.
            # Guarded by: energy_saved > 0 AND other job's timing still OK.
            if not added:
                others = sorted(
                    [(i2,j2) for (i2,j2) in proc_jobs[x_s]
                     if (i2,j2) != (i_s,j_s)
                     and tasks[i2]['u_i'] <= tasks[i_s]['u_i']
                     and freq_idx[(i2,j2)] > 0],
                    key=lambda ij: (tasks[ij[0]]['u_i'], ij[0], ij[1])  # lowest u_i first
                )
                for (i2,j2) in others:
                    z2_cur = freq_idx[(i2,j2)]; z2_new = z2_cur - 1
                    f2_cur = freq_set[z2_cur];  f2_new = freq_set[z2_new]
                    cum_k2 = cum[i2][seg_k[(i2,j2)]]

                    energy_saved = energy_val(cum_k2, f2_cur) - energy_val(cum_k2, f2_new)
                    if energy_saved <= 1e-12: continue     # dec freq doesn't save energy

                    time_cost_j2 = e_eff_val(cum_k2, f2_new) - e_eff_val(cum_k2, f2_cur)

                    # Check other job's timing after freq reduction
                    min_sl_j2 = min_slack_for_job(i2, j2, x_s, proc_jobs,
                                                   job_r, job_d, seg_k,
                                                   freq_idx, freq_set, cum)
                    if min_sl_j2 < time_cost_j2 - 1e-9: continue

                    # Check combined energy budget
                    new_E_slack = E_slack + energy_saved
                    if new_E_slack < add_energy - 1e-9: continue

                    # Full timing check after both changes
                    freq_idx[(i2,j2)]   = z2_new
                    seg_k[(i_s,j_s)]    = k_cur + 1
                    if check_all_timing(proc_jobs, job_r, job_d, seg_k,
                                        freq_idx, freq_set, cum, N_prc):
                        E_slack = new_E_slack - add_energy
                        improved = True; added = True
                        log.append(f"  Pass {pass_num}: T{tasks[i_s]['id']},j{j_s}"
                                   f"  k:{k_cur}→{k_cur+1}"
                                   f"  [ii.B T{tasks[i2]['id']},j{j2}"
                                   f" z:{z2_cur}→{z2_new}]"
                                   f"  E_slack={E_slack:.3f}")
                        break
                    else:
                        freq_idx[(i2,j2)] = z2_cur    # revert both
                        seg_k[(i_s,j_s)]  = k_cur

            # ONE segment per j* per pass: if added, move on. If not, skip.
            # (No inner while — outer loop will revisit j* in the next pass.)

        if not improved: break

    return pass_num, E_slack, log


# ══════════════════════════════════════════════════════════════════════════════
#  OUTPUT
# ══════════════════════════════════════════════════════════════════════════════

_S  = "=" * 76
_S2 = "-" * 76

def print_schedule(seg_k, freq_idx, freq_set, cum, tasks, N_tsk, N_job,
                   mapping, B_BUDGET, label=""):
    print(f"\n{_S}")
    print(f"  SCHEDULE{' — ' + label if label else ''}")
    print(_S2)
    tot_e = tot_u = 0.0
    for i in range(N_tsk):
        u_i = tasks[i]['u_i']
        procs = sorted({mapping.get((i,j),-1) for j in range(N_job[i])})
        print(f"\n  Task T{tasks[i]['id']}  period={tasks[i]['p_i']}"
              f"  u_i={u_i}  N_seg={len(tasks[i]['e_o_k'])}"
              f"  N_jobs={N_job[i]}  procs={procs}")
        print(f"  {'job':>4}  {'proc':>5}  {'freq':>6}  {'k':>3}  "
              f"{'cum_work':>9}  {'e_eff':>8}  {'energy':>9}  {'utility':>8}")
        print(f"  {'─'*65}")
        t_e=t_u=0.0
        for j in range(N_job[i]):
            k=seg_k[(i,j)]; z=freq_idx[(i,j)]; fz=freq_set[z]; cw=cum[i][k]
            ee=e_eff_val(cw,fz); en=energy_val(cw,fz)
            ut=u_i*(cw-cum[i][0]); t_e+=en; t_u+=ut
            px=mapping.get((i,j),-1)
            print(f"  {j+1:>4}  P{px:<4}  {fz:>6.3f}  {k:>3}  "
                  f"{cw:>9.4f}  {ee:>8.4f}  {en:>9.4f}  {ut:>8.4f}")
        tot_e+=t_e; tot_u+=t_u
        print(f"  Task totals : energy={t_e:.4f}  utility={t_u:.4f}")
    print(f"\n{_S}")
    print(f"  Total energy  : {tot_e:.4f}  "
          f"(budget={B_BUDGET}  slack={B_BUDGET-tot_e:.4f})")
    print(f"  Total utility : {tot_u:.6f}")
    print(_S)
    return tot_e, tot_u


# ══════════════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════════════

# Module-level alias so phase_optional_segments can look up processor per job
proc_jobs_map: dict = {}


def run_heuristic(processors, tasks, B_BUDGET):
    global proc_jobs_map

    N_tsk    = len(tasks); N_prc = len(processors)
    freq_set = processors[0]['frequencies']
    N_frq    = len(freq_set)
    periods  = [int(t['p_i']) for t in tasks]
    h        = lcm_list(periods); quantum = gcd_list(periods)
    cum, N_seg = build_cum(tasks)
    N_job    = [h//periods[i] for i in range(N_tsk)]

    job_r = {(i,j): j*periods[i]     for i in range(N_tsk) for j in range(N_job[i])}
    job_d = {(i,j): (j+1)*periods[i] for i in range(N_tsk) for j in range(N_job[i])}

    # ── PHASE 1 ───────────────────────────────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 1 : QUANTUM SPS MAPPING")
    print(_S2)
    mapping = quantum_sps_mapping(tasks, processors, h, quantum)

    proc_jobs = defaultdict(list)
    for (i,j),x in mapping.items():
        proc_jobs[x].append((i,j))
    proc_jobs_map = {(i,j): x for (i,j),x in mapping.items()}

    print(f"\n  Processor utilisation:")
    for x in range(N_prc):
        ul = sum(tasks[i]['e_m']/tasks[i]['p_i'] for (i,j) in proc_jobs[x])
        print(f"    P{x}: {len(proc_jobs[x])} jobs  util={ul:.4f}"
              f"{'  ← OVER 1.0' if ul>1 else ''}")

    # Initial state: f_max, k=0
    freq_idx = {(i,j): N_frq-1 for i in range(N_tsk) for j in range(N_job[i])}
    seg_k    = {(i,j): 0       for i in range(N_tsk) for j in range(N_job[i])}

    # ── PHASE 2 : LEFT SHIFT  (diagnostic only, run once) ────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 2 : LEFT SHIFT  (diagnostic, f_max, mandatory only)")
    print(_S2)
    ls_slack = left_shift(proc_jobs, job_r, job_d, seg_k, freq_idx, freq_set, cum)
    infeas   = [k for k,v in ls_slack.items() if v < -1e-9]
    print(f"  Jobs with negative left-shift slack: {len(infeas)}"
          f"  (preemptive EDF may still be feasible)")
    print(f"  Min per-job left-shift slack: {min(ls_slack.values()):.4f}")

    # ── PHASE 3 : ENERGY SLACK ────────────────────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 3 : ENERGY SLACK")
    print(_S2)
    E_init = total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job)
    E_slk  = B_BUDGET - E_init
    print(f"  E_consumed (mandatory, f_max) : {E_init:.4f}")
    print(f"  E_budget                      : {B_BUDGET:.4f}")
    print(f"  E_slack                       : {E_slk:.4f}"
          f"{'  [INFEASIBLE]' if E_slk < 0 else ''}")
    if E_slk < -1e-9:
        print(f"  Mandatory-only at f_max already exceeds budget. Reporting as-is.")
        print_schedule(seg_k, freq_idx, freq_set, cum, tasks, N_tsk, N_job,
                       mapping, B_BUDGET, label="INFEASIBLE MANDATORY")
        return seg_k, freq_idx, 0.0, E_init

    # ── PHASE 4 : AGGRESSIVE SCALING  (freq ↓ + energy guard) ────────────────
    print(f"\n{_S}")
    print(f"  PHASE 4 : AGGRESSIVE SCALING  (freq ↓, only if saves energy)")
    print(_S2)
    n_sc = phase_aggressive_scaling(seg_k, freq_idx, freq_set, N_frq, cum,
                                     N_tsk, N_job, proc_jobs, job_r, job_d, N_prc)
    E_after = total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job)
    if n_sc == 0:
        print(f"  No reductions made  (energy model minimum is at f_max;")
        print(f"  α={ALPHA}, β={BETA} → dec freq increases energy → no-op).")
    else:
        print(f"  {n_sc} job(s) frequency-reduced.")
        print(f"  E after scaling : {E_after:.4f}  E_slack={B_BUDGET-E_after:.4f}")

    # ── PHASE 5 : OPTIONAL SEGMENT SCHEDULING ────────────────────────────────
    print(f"\n{_S}")
    print(f"  PHASE 5 : OPTIONAL SEGMENT SCHEDULING")
    print(f"  1 segment per j* per pass  |  DBF window slack  |  stable u_i sort")
    print(_S2)

    n_passes, E_final_slack, opt_log = phase_optional_segments(
        seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
        N_tsk, N_job, proc_jobs, job_r, job_d,
        tasks, N_prc, B_BUDGET)

    if opt_log:
        print(f"  {len(opt_log)} segment addition(s) across {n_passes} pass(es):")
        for entry in opt_log: print(entry)
    else:
        print(f"  No optional segments added.")

    # ── FINAL SCHEDULE ────────────────────────────────────────────────────────
    tot_e, tot_u = print_schedule(
        seg_k, freq_idx, freq_set, cum, tasks, N_tsk, N_job,
        mapping, B_BUDGET, label="FINAL HEURISTIC SOLUTION")

    return seg_k, freq_idx, tot_u, tot_e


# ══════════════════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    tc_path = sys.argv[1] if len(sys.argv) > 1 else "testcase.py"
    print(f"Loading testcase: {tc_path}")
    processors, tasks, B_BUDGET = load_testcase(tc_path)

    periods = [int(t['p_i']) for t in tasks]
    h       = lcm_list(periods); quantum = gcd_list(periods)
    cum, N_seg = build_cum(tasks)
    N_tsk   = len(tasks)
    N_job   = [h//periods[i] for i in range(N_tsk)]

    print(f"\n{_S}")
    print(f"  USRT Heuristic (Combined)  —  Instance")
    print(_S2)
    print(f"  Processors   : {len(processors)}")
    print(f"  Frequencies  : {processors[0]['frequencies']}")
    print(f"  Energy budget: {B_BUDGET}    α={ALPHA}   β={BETA}")
    print(f"  Hyper-period : {h}    Quantum(GCD): {quantum}")
    print(_S2)
    total_util = sum(t['e_m']/t['p_i'] for t in tasks)
    print(f"  {'TID':>4}  {'period':>7}  {'Nseg':>5}  {'Njobs':>6}  "
          f"{'e_m':>9}  {'util':>7}  {'u_i':>6}  e_o_k")
    print(f"  {_S2}")
    for i,t in enumerate(tasks):
        u=t['e_m']/t['p_i']
        print(f"  {t['id']:>4}  {t['p_i']:>7}  {N_seg[i]:>5}  {N_job[i]:>6}  "
              f"{t['e_m']:>9.4f}  {u:>7.4f}  {t['u_i']:>6}  "
              f"{[round(x,4) for x in t['e_o_k']]}")
    print(f"\n  Total utilisation: {total_util:.4f}/{len(processors)}"
          f"  [{'FEASIBLE' if total_util<=len(processors) else 'OVERLOADED'}]")
    print(_S)

    run_heuristic(processors, tasks, B_BUDGET)
