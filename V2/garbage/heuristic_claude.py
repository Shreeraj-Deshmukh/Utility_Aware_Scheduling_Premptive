"""
USRT Heuristic  —  Combined + Swap Local Search
================================================

DESIGN CHOICES (all constraints strictly enforced)
---------------------------------------------------
Phase 1 : Quantum SPS mapping (utilisation-based, DBF checked + repaired)
Phase 2 : Left shift — diagnostic only, run ONCE
Phase 3 : Energy slack check
Phase 4 : Aggressive freq scaling DOWN + energy guard (no-op in our model
           since α=1,β=0.5 minimises energy at f_max; code is generic)
Phase 5 : Greedy optional segment scheduling
           · 1 segment per j* per pass (outer while repeats to convergence)
           · Timing via DBF window slack  — min_slack_for_job()
           · No extra DBF call in Case (i)  — slack check is sufficient
           · No left-shift recomputation inside loop
           · Phase 4 direction: freq DOWN + energy guard
           · Case ii.B: dec freq of others + energy guard
           · Stable sort by (-u_i, task_id, job_id)

RADICAL IMPROVEMENT — Phase 6: Best-First Pairwise Segment Swap
----------------------------------------------------------------
The greedy Phase 5 converges to a LOCAL OPTIMUM.  It cannot undo earlier
decisions that blocked higher-utility segments from being added later.

Phase 6 escapes these local optima using a segment swap:

  For every pair (giver job, receiver job):
    • Giver removes its LAST optional segment
    • Receiver adds its NEXT optional segment
    • Net utility gain = u_recv * e_recv_next  −  u_give * e_give_last
    • Energy balance:  E_freed − E_cost  ≤  E_slack remaining
    • Timing:          min_slack_for_job(receiver, WITH giver's seg removed)
                       ≥ add_time for receiver's next segment

  Execute the BEST improving swap found (maximum net utility gain).
  After each swap, run a FILL PASS (re-run Phase 5 to convergence) to
  capitalise on newly freed energy and timing slack.
  Repeat until no improving swap exists.

WHY THIS WORKS
--------------
The greedy phase adds segments in u_i order.  If a low-utility job's segment
occupies a critical DBF window or consumes energy that a high-utility job
needed, greedy is stuck.  The swap detects this by directly computing:

  net_utility = utility_gained(receiver) − utility_lost(giver) > 0

and verifying all constraints hold after both changes.  The swap is
cross-processor: energy is a global resource, so removing a low-utility
segment on P0 can fund a high-utility segment on P1.

The fill pass after each swap propagates the improvement: freed resources
(timing slack on giver's processor, energy globally) can enable new
segments for other jobs, discovered greedily.

COMPLEXITY
----------
Phase 5: O(n_jobs²  × n_windows) per pass, O(passes) passes
Phase 6: O(n_jobs² × n_windows) per swap iteration, O(swaps) iterations
For the testcase (~100 jobs, ~100 windows, ~10 swaps): fast in practice.

Testcase : testcaase.py  →  processors, tasks, B_BUDGET
Energy   : E = α·(Σe_q/f) + β·f²·Σe_q   (α=ALPHA, β=BETA)
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
    return ALPHA * cum_k / fz + BETA * fz**2 * cum_k

def e_eff_val(cum_k, fz):
    return cum_k / fz

def total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job):
    return sum(energy_val(cum[i][seg_k[(i,j)]], freq_set[freq_idx[(i,j)]])
               for i in range(N_tsk) for j in range(N_job[i]))

def total_utility(seg_k, tasks, cum, N_tsk, N_job):
    return sum(tasks[i]['u_i'] * (cum[i][seg_k[(i,j)]] - cum[i][0])
               for i in range(N_tsk) for j in range(N_job[i]))


# ══════════════════════════════════════════════════════════════════════════════
#  SPS / DPS
# ══════════════════════════════════════════════════════════════════════════════

class PS:
    __slots__ = ('m', 'loads', 'assign', 'gap')
    def __init__(self, m):
        self.m=m; self.loads=[0.0]*m
        self.assign=[set() for _ in range(m)]; self.gap=0.0

    @classmethod
    def singleton(cls, m, key, val):
        ps=cls(m); ps.loads[0]=val; ps.assign[0].add(key); ps.gap=val; return ps

    def _resort(self):
        p=sorted(zip(self.loads,self.assign),key=lambda x:-x[0])
        self.loads=[x[0] for x in p]; self.assign=[x[1] for x in p]
        self.gap=self.loads[0]-self.loads[-1]

    def insert(self, key, val):
        self.loads[-1]+=val; self.assign[-1].add(key); self._resort()

    def combine(self, other):
        m=self.m
        raw=[(self.loads[j]+other.loads[m-1-j],
              self.assign[j]|other.assign[m-1-j]) for j in range(m)]
        raw.sort(key=lambda x:-x[0])
        ps=PS(m); ps.loads=[r[0] for r in raw]
        ps.assign=[r[1] for r in raw]; ps.gap=ps.loads[0]-ps.loads[-1]; return ps

def run_dps(jl, m):
    if not jl: return []
    k0,v0=jl[0]; active=[PS.singleton(m,k0,v0)]
    for key,val in jl[1:]:
        best=max(range(len(active)),key=lambda i:active[i].gap)
        if val<=active[best].gap: active[best].insert(key,val)
        else: active.append(PS.singleton(m,key,val))
    return active

def run_sps(ps_list):
    if not ps_list: return None
    active=list(ps_list)
    while len(active)>1:
        active.sort(key=lambda ps:-ps.gap)
        merged=active[0].combine(active[1]); active=active[2:]+[merged]
    return active[0]


# ══════════════════════════════════════════════════════════════════════════════
#  DBF HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def window_slack(x, t1, t2, proc_jobs, job_r, job_d, seg_k, freq_idx, freq_set, cum):
    """DBF slack = (t2-t1) - Σ e_eff of jobs in S(t1,t2,x)."""
    window = [(i,j) for (i,j) in proc_jobs[x]
              if job_r[(i,j)] >= t1 and job_d[(i,j)] <= t2]
    if not window: return t2 - t1
    demand = sum(e_eff_val(cum[i][seg_k[(i,j)]], freq_set[freq_idx[(i,j)]])
                 for (i,j) in window)
    return (t2 - t1) - demand


def min_slack_for_job(i_s, j_s, x, proc_jobs, job_r, job_d,
                      seg_k, freq_idx, freq_set, cum):
    """
    Min DBF slack across all windows [t1,t2] that CONTAIN job (i_s,j_s):
    t1 ≤ r_{i_s,j_s}  AND  t2 ≥ d_{i_s,j_s}.

    If ≥ add_time → adding add_time to this job keeps all windows feasible.
    No separate DBF call needed.
    """
    r_ij = job_r[(i_s,j_s)]; d_ij = job_d[(i_s,j_s)]
    Ax = sorted({job_r[ij] for ij in proc_jobs[x]})
    Dx = sorted({job_d[ij] for ij in proc_jobs[x]})
    min_sl = float('inf')
    for t1 in Ax:
        if t1 > r_ij: continue
        for t2 in Dx:
            if t2 < d_ij: continue
            if t1 >= t2: continue
            sl = window_slack(x,t1,t2,proc_jobs,job_r,job_d,seg_k,freq_idx,freq_set,cum)
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
                if window_slack(x,t1,t2,proc_jobs,job_r,job_d,
                                seg_k,freq_idx,freq_set,cum) < -1e-9:
                    return False
    return True


# ══════════════════════════════════════════════════════════════════════════════
#  QUANTUM SPS MAPPING  (Phase 1)
# ══════════════════════════════════════════════════════════════════════════════

def _check_dbf_mandatory(mapping, tasks, processors, h):
    N_tsk=len(tasks); N_prc=len(processors)
    periods=[int(t['p_i']) for t in tasks]
    N_job=[h//periods[i] for i in range(N_tsk)]
    job_r={(i,j):j*periods[i]     for i in range(N_tsk) for j in range(N_job[i])}
    job_d={(i,j):(j+1)*periods[i] for i in range(N_tsk) for j in range(N_job[i])}
    pj=defaultdict(list)
    for (i,j),x in mapping.items(): pj[x].append((i,j))
    viols={}
    for x in range(N_prc):
        if not pj[x]: continue
        Ax=sorted({job_r[ij] for ij in pj[x]}); Dx=sorted({job_d[ij] for ij in pj[x]})
        for t1 in Ax:
            for t2 in Dx:
                if t1>=t2: continue
                win=[(i,j) for (i,j) in pj[x] if job_r[(i,j)]>=t1 and job_d[(i,j)]<=t2]
                if not win: continue
                dem=sum(tasks[i]['e_m'] for (i,j) in win)
                if dem>t2-t1+1e-9: viols.setdefault(x,[]).append((t1,t2,dem,t2-t1))
    return len(viols)==0, viols

def _repair(mapping, tasks, processors, h):
    N_tsk=len(tasks); m=len(processors)
    periods=[int(t['p_i']) for t in tasks]
    N_job=[h//periods[i] for i in range(N_tsk)]
    job_r={(i,j):j*periods[i]     for i in range(N_tsk) for j in range(N_job[i])}
    job_d={(i,j):(j+1)*periods[i] for i in range(N_tsk) for j in range(N_job[i])}
    for _ in range(100):
        ok,viols=_check_dbf_mandatory(mapping,tasks,processors,h)
        if ok: return mapping, True
        worst=max(((x,t1,t2,d,c) for x,vl in viols.items() for (t1,t2,d,c) in vl),
                  key=lambda v:v[3]-v[4])
        x_bad,t1_b,t2_b=worst[0],worst[1],worst[2]
        off=[(i,j) for (i,j),px in mapping.items()
             if px==x_bad and job_r[(i,j)]>=t1_b and job_d[(i,j)]<=t2_b]
        if not off: break
        mi,mj=max(off,key=lambda ij:tasks[ij[0]]['e_m'])
        util=defaultdict(float)
        for (i,j),px in mapping.items(): util[px]+=tasks[i]['e_m']/tasks[i]['p_i']
        tgt=min((x for x in range(m) if x!=x_bad),key=lambda x:util[x])
        mapping[(mi,mj)]=tgt
    return mapping, _check_dbf_mandatory(mapping,tasks,processors,h)[0]

def quantum_sps_mapping(tasks, processors, h, quantum):
    m=len(processors); all_jobs=generate_jobs(tasks,h)
    by_arr=defaultdict(list)
    for job in all_jobs: by_arr[job[2]].append(job)
    mapping={}; proc_util=[0.0]*m; leftover=[]

    print(f"  {'Quantum':^12}  {'Mand':>5}  {'Opt':>5}  "
          f"{'Actv':>5}  {'Defr':>5}  {'MaxUtil':>9}  Status")
    print(f"  {'─'*68}")

    for q_start in range(0, h, quantum):
        q_end=q_start+quantum; newly=by_arr.get(q_start,[]); leftover_=[]
        pending=leftover+newly; leftover=[]
        if not pending: continue
        mandatory=[(i,j,r,d) for (i,j,r,d) in pending if d==q_end]
        optional=[(i,j,r,d)  for (i,j,r,d) in pending if d>q_end]
        optional.sort(key=lambda x:x[3])
        n_m=len(mandatory); n_o=len(optional)
        active=mandatory+optional; final_ps=None; deferred=0; status="OK"

        while True:
            if not active: status="EMPTY"; break
            tu=sum(tasks[i]['e_m']/tasks[i]['p_i'] for (i,j,r,d) in active)
            rc=sum(1.0-proc_util[x] for x in range(m))
            if tu>rc+1e-9:
                opt=[v for v in active if v[3]>q_end]
                if not opt: status="MAND_OVER"; break
                td=max(opt,key=lambda x:x[3]); active.remove(td)
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
            if not opt: final_ps=res; proc_util=nu; status=f"OVER({max(nu):.3f})"; break
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
#  PHASE 2 : LEFT SHIFT  (diagnostic only, run once)
# ══════════════════════════════════════════════════════════════════════════════

def left_shift(proc_jobs, job_r, job_d, seg_k, freq_idx, freq_set, cum):
    ls_slack={}
    for x,jobs in proc_jobs.items():
        jobs_edf=sorted(jobs,key=lambda ij:job_d[ij])
        pa=0.0
        for (i,j) in jobs_edf:
            ef=e_eff_val(cum[i][seg_k[(i,j)]],freq_set[freq_idx[(i,j)]])
            s=max(pa,float(job_r[(i,j)]))
            ls_slack[(i,j)]=job_d[(i,j)]-(s+ef); pa=s+ef
    return ls_slack


# ══════════════════════════════════════════════════════════════════════════════
#  PHASE 4 : AGGRESSIVE SCALING  (freq ↓, energy guard)
# ══════════════════════════════════════════════════════════════════════════════

def phase_aggressive_scaling(seg_k, freq_idx, freq_set, N_frq, cum,
                              N_tsk, N_job, proc_jobs, job_r, job_d, N_prc):
    n_sc=0; changed=True
    while changed:
        changed=False
        for i in range(N_tsk):
            for j in range(N_job[i]):
                z=freq_idx[(i,j)]
                if z==0: continue
                E_cur=energy_val(cum[i][seg_k[(i,j)]],freq_set[z])
                E_new=energy_val(cum[i][seg_k[(i,j)]],freq_set[z-1])
                if E_new>=E_cur-1e-12: continue
                freq_idx[(i,j)]=z-1
                if check_all_timing(proc_jobs,job_r,job_d,seg_k,
                                    freq_idx,freq_set,cum,N_prc):
                    changed=True; n_sc+=1
                else:
                    freq_idx[(i,j)]=z
    return n_sc


# ══════════════════════════════════════════════════════════════════════════════
#  PHASE 5 : GREEDY OPTIONAL SEGMENT SCHEDULING
# ══════════════════════════════════════════════════════════════════════════════

def phase_optional_segments(seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
                             N_tsk, N_job, proc_jobs, proc_jobs_map,
                             job_r, job_d, tasks, N_prc, B_BUDGET):
    """
    1 segment per j* per pass.
    Timing gate: min_slack_for_job (DBF window slack — no extra DBF call for case i).
    Sort: stable by (-u_i, task_id, job_id).
    Cases: (i) no impact, (ii.A) inc freq j*, (ii.B) dec freq others.
    Returns: (n_passes, final_E_slack, log_entries)
    """
    E_slack = B_BUDGET - total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job)

    sorted_jobs = sorted(
        [(i,j) for i in range(N_tsk) for j in range(N_job[i])],
        key=lambda ij: (-tasks[ij[0]]['u_i'], ij[0], ij[1])
    )

    log=[]; pass_num=0

    while True:
        pass_num+=1; improved=False

        for (i_s,j_s) in sorted_jobs:
            k_cur=seg_k[(i_s,j_s)]
            if k_cur>=N_seg[i_s]: continue

            z_cur=freq_idx[(i_s,j_s)]; f_cur=freq_set[z_cur]
            x_s=proc_jobs_map[(i_s,j_s)]

            add_time   = (cum[i_s][k_cur+1]-cum[i_s][k_cur])/f_cur
            add_energy = energy_val(cum[i_s][k_cur+1],f_cur)-energy_val(cum[i_s][k_cur],f_cur)

            min_sl=min_slack_for_job(i_s,j_s,x_s,proc_jobs,job_r,job_d,
                                     seg_k,freq_idx,freq_set,cum)

            # ── Case (i): no impact on others ────────────────────────────────
            if min_sl>=add_time-1e-9 and E_slack>=add_energy-1e-9:
                seg_k[(i_s,j_s)]=k_cur+1; E_slack-=add_energy
                improved=True
                log.append(f"    [i]  T{tasks[i_s]['id']},j{j_s}"
                           f"  k:{k_cur}→{k_cur+1}  E_slack={E_slack:.3f}")
                continue

            added=False

            # ── Case (ii.A): inc freq of j* ──────────────────────────────────
            if z_cur<N_frq-1:
                z_t=z_cur+1; f_t=freq_set[z_t]
                dt=e_eff_val(cum[i_s][k_cur+1],f_t)-e_eff_val(cum[i_s][k_cur],f_cur)
                de=energy_val(cum[i_s][k_cur+1],f_t)-energy_val(cum[i_s][k_cur],f_cur)
                if min_sl-dt>=-1e-9 and E_slack-de>=-1e-9:
                    freq_idx[(i_s,j_s)]=z_t; seg_k[(i_s,j_s)]=k_cur+1
                    if check_all_timing(proc_jobs,job_r,job_d,seg_k,
                                        freq_idx,freq_set,cum,N_prc):
                        E_slack-=de; improved=True; added=True
                        log.append(f"    [ii.A]  T{tasks[i_s]['id']},j{j_s}"
                                   f"  k:{k_cur}→{k_cur+1} z:{z_cur}→{z_t}"
                                   f"  E_slack={E_slack:.3f}")
                    else:
                        freq_idx[(i_s,j_s)]=z_cur; seg_k[(i_s,j_s)]=k_cur

            # ── Case (ii.B): dec freq of others on same proc ─────────────────
            if not added:
                others=sorted(
                    [(i2,j2) for (i2,j2) in proc_jobs[x_s]
                     if (i2,j2)!=(i_s,j_s)
                     and tasks[i2]['u_i']<=tasks[i_s]['u_i']
                     and freq_idx[(i2,j2)]>0],
                    key=lambda ij:(tasks[ij[0]]['u_i'],ij[0],ij[1])
                )
                for (i2,j2) in others:
                    z2c=freq_idx[(i2,j2)]; z2n=z2c-1
                    c2=cum[i2][seg_k[(i2,j2)]]
                    esaved=energy_val(c2,freq_set[z2c])-energy_val(c2,freq_set[z2n])
                    if esaved<=1e-12: continue
                    tcost=e_eff_val(c2,freq_set[z2n])-e_eff_val(c2,freq_set[z2c])
                    ms2=min_slack_for_job(i2,j2,x_s,proc_jobs,job_r,job_d,
                                         seg_k,freq_idx,freq_set,cum)
                    if ms2<tcost-1e-9: continue
                    new_Esl=E_slack+esaved
                    if new_Esl<add_energy-1e-9: continue
                    freq_idx[(i2,j2)]=z2n; seg_k[(i_s,j_s)]=k_cur+1
                    if check_all_timing(proc_jobs,job_r,job_d,seg_k,
                                        freq_idx,freq_set,cum,N_prc):
                        E_slack=new_Esl-add_energy; improved=True; added=True
                        log.append(f"    [ii.B]  T{tasks[i_s]['id']},j{j_s}"
                                   f"  k:{k_cur}→{k_cur+1}"
                                   f"  via T{tasks[i2]['id']},j{j2} z:{z2c}→{z2n}"
                                   f"  E_slack={E_slack:.3f}")
                        break
                    else:
                        freq_idx[(i2,j2)]=z2c; seg_k[(i_s,j_s)]=k_cur

        if not improved: break

    return pass_num, E_slack, log


# ══════════════════════════════════════════════════════════════════════════════
#  PHASE 6 : BEST-FIRST PAIRWISE SEGMENT SWAP  (radical improvement)
# ══════════════════════════════════════════════════════════════════════════════

def phase_swap_local_search(seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
                              N_tsk, N_job, proc_jobs, proc_jobs_map,
                              job_r, job_d, tasks, N_prc, B_BUDGET):
    """
    Best-first pairwise segment swap local search.

    Escapes local optima left by greedy Phase 5.  Each iteration:

    1. SEARCH — evaluate all (giver, receiver) pairs:
         giver   : any job with ≥ 1 optional segment
         receiver: any job with < N_seg optional segments
         → With giver's last segment tentatively REMOVED:
           a) net_utility = u_recv·e_recv_next − u_give·e_give_last  > 0
           b) energy: E_freed − E_cost ≤ E_slack (global)
           c) timing: min_slack_for_job(receiver) ≥ add_time_for_receiver
              (checked WITH giver's segment already removed — receiver's
               containing windows may have more slack after giver's removal
               if they are on the same processor)

    2. EXECUTE the swap with the highest net utility gain.
       Full check_all_timing() for final safety.

    3. FILL PASS — re-run Phase 5 to convergence on the updated state.
       Freed resources (energy globally, timing on giver's processor)
       may unlock new segments for other jobs.

    4. Repeat until no improving swap exists.

    Cross-processor swaps are supported: energy is global, only timing
    is per-processor, so removing a segment on P0 can fund one on P1.
    """
    E_slack = B_BUDGET - total_energy(seg_k, freq_idx, freq_set, cum, N_tsk, N_job)
    log = []; n_swaps = 0; iteration = 0

    while True:
        iteration += 1
        best = None   # (net_u, i1,j1,k1, i2,j2,k2, dE_freed,dE_cost)

        # ── SEARCH ───────────────────────────────────────────────────────────
        for i1 in range(N_tsk):
            for j1 in range(N_job[i1]):
                k1 = seg_k[(i1,j1)]
                if k1 == 0: continue          # giver has nothing to give

                z1    = freq_idx[(i1,j1)]
                f1    = freq_set[z1]
                # Utility giver LOSES by removing its last segment
                u_lost   = tasks[i1]['u_i'] * (cum[i1][k1] - cum[i1][k1-1])
                # Energy freed by removing giver's last segment
                dE_freed = (energy_val(cum[i1][k1],   f1) -
                            energy_val(cum[i1][k1-1], f1))   # always > 0

                # Tentatively remove giver's last segment
                seg_k[(i1,j1)] = k1 - 1
                new_E_slack    = E_slack + dE_freed

                for i2 in range(N_tsk):
                    for j2 in range(N_job[i2]):
                        if (i2,j2) == (i1,j1): continue
                        k2 = seg_k[(i2,j2)]
                        if k2 >= N_seg[i2]: continue   # receiver already maxed

                        z2 = freq_idx[(i2,j2)]
                        x2 = proc_jobs_map[(i2,j2)]

                        # Utility receiver GAINS from its next segment
                        u_gained = tasks[i2]['u_i'] * (cum[i2][k2+1] - cum[i2][k2])
                        net_u    = u_gained - u_lost
                        if net_u <= 1e-9: continue     # not worth swapping

                        dE_cost = (energy_val(cum[i2][k2+1], freq_set[z2]) -
                                   energy_val(cum[i2][k2],   freq_set[z2]))
                        if new_E_slack < dE_cost - 1e-9: continue

                        # Timing check for receiver WITH giver's seg already removed
                        # (if on same proc, giver's removal increased slack → receiver
                        #  has MORE room now than before; evaluated correctly here)
                        add_time = (cum[i2][k2+1] - cum[i2][k2]) / freq_set[z2]
                        min_sl   = min_slack_for_job(i2, j2, x2, proc_jobs,
                                                     job_r, job_d, seg_k,
                                                     freq_idx, freq_set, cum)
                        if min_sl < add_time - 1e-9: continue

                        if best is None or net_u > best[0]:
                            best = (net_u, i1, j1, k1, i2, j2, k2, dE_freed, dE_cost)

                # Restore giver before trying next giver
                seg_k[(i1,j1)] = k1

        if best is None:
            break   # no improving swap found → done

        # ── EXECUTE best swap ────────────────────────────────────────────────
        net_u, i1, j1, k1, i2, j2, k2, dE_freed, dE_cost = best
        seg_k[(i1,j1)] = k1 - 1
        seg_k[(i2,j2)] = k2 + 1

        # Final full timing check (safety net)
        if check_all_timing(proc_jobs, job_r, job_d, seg_k, freq_idx, freq_set, cum, N_prc):
            E_slack  = E_slack + dE_freed - dE_cost
            n_swaps += 1
            log.append(
                f"  Swap {n_swaps} (iter {iteration}):"
                f"  remove T{tasks[i1]['id']},j{j1} k:{k1}→{k1-1}"
                f"  |  add T{tasks[i2]['id']},j{j2} k:{k2}→{k2+1}"
                f"  |  +util={net_u:.4f}  E_slack={E_slack:.3f}"
            )

            # ── FILL PASS: greedily add more segments with freed resources ───
            # Freed resources:  timing on giver's proc + energy globally
            # Phase 5 discovers all newly-possible additions efficiently.
            _, E_slack, fill_log = phase_optional_segments(
                seg_k, freq_idx, freq_set, N_frq, cum, N_seg,
                N_tsk, N_job, proc_jobs, proc_jobs_map,
                job_r, job_d, tasks, N_prc, B_BUDGET)
            if fill_log:
                log.append(f"    Fill after swap {n_swaps} ({len(fill_log)} addition(s)):")
                log.extend(fill_log)
        else:
            # Full timing check failed (rare: swap was predicted safe but
            # cross-window interactions violated).  Revert.
            seg_k[(i1,j1)] = k1
            seg_k[(i2,j2)] = k2
            log.append(
                f"  Swap {n_swaps+1} (iter {iteration}): REVERTED"
                f" (cross-window timing violation)"
            )
            # Continue searching — the next-best swap might still work.
            # (Break here to be safe; could alternatively continue.)
            break

    return n_swaps, E_slack, log


# ══════════════════════════════════════════════════════════════════════════════
#  OUTPUT
# ══════════════════════════════════════════════════════════════════════════════

_S  = "=" * 76
_S2 = "-" * 76

def print_schedule(seg_k, freq_idx, freq_set, cum, tasks, N_tsk, N_job,
                   mapping, B_BUDGET, label=""):
    print(f"\n{_S}")
    print(f"  SCHEDULE{' — '+label if label else ''}")
    print(_S2)
    tot_e=tot_u=0.0
    for i in range(N_tsk):
        u_i=tasks[i]['u_i']
        procs=sorted({mapping.get((i,j),-1) for j in range(N_job[i])})
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
            print(f"  {j+1:>4}  P{mapping.get((i,j),-1):<4}  {fz:>6.3f}  {k:>3}  "
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

def run_heuristic(processors, tasks, B_BUDGET):
    N_tsk=len(tasks); N_prc=len(processors)
    freq_set=processors[0]['frequencies']; N_frq=len(freq_set)
    periods=[int(t['p_i']) for t in tasks]
    h=lcm_list(periods); quantum=gcd_list(periods)
    cum, N_seg=build_cum(tasks)
    N_job=[h//periods[i] for i in range(N_tsk)]

    job_r={(i,j):j*periods[i]     for i in range(N_tsk) for j in range(N_job[i])}
    job_d={(i,j):(j+1)*periods[i] for i in range(N_tsk) for j in range(N_job[i])}

    # ── PHASE 1 ───────────────────────────────────────────────────────────────
    print(f"\n{_S}"); print(f"  PHASE 1 : QUANTUM SPS MAPPING"); print(_S2)
    mapping = quantum_sps_mapping(tasks, processors, h, quantum)

    proc_jobs    = defaultdict(list)
    proc_jobs_map = {}
    for (i,j),x in mapping.items():
        proc_jobs[x].append((i,j)); proc_jobs_map[(i,j)]=x

    print(f"\n  Processor utilisation:")
    for x in range(N_prc):
        ul=sum(tasks[i]['e_m']/tasks[i]['p_i'] for (i,j) in proc_jobs[x])
        print(f"    P{x}: {len(proc_jobs[x])} jobs  util={ul:.4f}"
              f"{'  ← OVER 1.0' if ul>1 else ''}")

    # Initial state: f_max, k=0
    freq_idx={(i,j):N_frq-1 for i in range(N_tsk) for j in range(N_job[i])}
    seg_k   ={(i,j):0       for i in range(N_tsk) for j in range(N_job[i])}

    # ── PHASE 2 : LEFT SHIFT  (diagnostic only) ───────────────────────────────
    print(f"\n{_S}"); print(f"  PHASE 2 : LEFT SHIFT  (f_max, mandatory only)"); print(_S2)
    ls=left_shift(proc_jobs,job_r,job_d,seg_k,freq_idx,freq_set,cum)
    infeas=[k for k,v in ls.items() if v<-1e-9]
    print(f"  Jobs with negative left-shift slack: {len(infeas)}")
    print(f"  Min left-shift slack: {min(ls.values()):.4f}")

    # ── PHASE 3 : ENERGY SLACK ────────────────────────────────────────────────
    print(f"\n{_S}"); print(f"  PHASE 3 : ENERGY SLACK"); print(_S2)
    E_init=total_energy(seg_k,freq_idx,freq_set,cum,N_tsk,N_job)
    E_slk =B_BUDGET-E_init
    print(f"  E_consumed (mandatory, f_max): {E_init:.4f}")
    print(f"  E_budget                     : {B_BUDGET:.4f}")
    print(f"  E_slack                      : {E_slk:.4f}"
          f"{'  [INFEASIBLE]' if E_slk<0 else ''}")
    if E_slk<-1e-9:
        print(f"  Cannot schedule — mandatory cost exceeds budget.")
        print_schedule(seg_k,freq_idx,freq_set,cum,tasks,N_tsk,N_job,
                       mapping,B_BUDGET,label="INFEASIBLE MANDATORY")
        return seg_k,freq_idx,0.0,E_init

    # ── PHASE 4 : AGGRESSIVE SCALING ─────────────────────────────────────────
    print(f"\n{_S}"); print(f"  PHASE 4 : AGGRESSIVE SCALING  (freq ↓ + energy guard)"); print(_S2)
    n_sc=phase_aggressive_scaling(seg_k,freq_idx,freq_set,N_frq,cum,
                                   N_tsk,N_job,proc_jobs,job_r,job_d,N_prc)
    if n_sc==0:
        print(f"  No reductions (α={ALPHA},β={BETA} → min energy at f_max → no-op).")
    else:
        Ea=total_energy(seg_k,freq_idx,freq_set,cum,N_tsk,N_job)
        print(f"  {n_sc} job(s) reduced. E_consumed={Ea:.4f}  E_slack={B_BUDGET-Ea:.4f}")

    # ── PHASE 5 : GREEDY OPTIONAL SEGMENTS ───────────────────────────────────
    print(f"\n{_S}"); print(f"  PHASE 5 : GREEDY OPTIONAL SEGMENT SCHEDULING"); print(_S2)
    n_p5,E_after5,log5=phase_optional_segments(
        seg_k,freq_idx,freq_set,N_frq,cum,N_seg,
        N_tsk,N_job,proc_jobs,proc_jobs_map,
        job_r,job_d,tasks,N_prc,B_BUDGET)
    u_after5=total_utility(seg_k,tasks,cum,N_tsk,N_job)
    if log5:
        print(f"  {len(log5)} segment(s) added across {n_p5} pass(es):")
        for e in log5: print(e)
    else:
        print(f"  No optional segments added in Phase 5.")
    print(f"\n  Phase 5 result: utility={u_after5:.6f}  E_slack={E_after5:.4f}")

    # ── PHASE 6 : SWAP LOCAL SEARCH ──────────────────────────────────────────
    print(f"\n{_S}"); print(f"  PHASE 6 : BEST-FIRST PAIRWISE SEGMENT SWAP"); print(_S2)
    print(f"  Searching for improving (giver → receiver) swaps …")
    print(f"  After each swap: fill pass (Phase 5 re-run) to capitalise on freed resources.")
    print()
    n_sw,E_after6,log6=phase_swap_local_search(
        seg_k,freq_idx,freq_set,N_frq,cum,N_seg,
        N_tsk,N_job,proc_jobs,proc_jobs_map,
        job_r,job_d,tasks,N_prc,B_BUDGET)
    u_after6=total_utility(seg_k,tasks,cum,N_tsk,N_job)
    if log6:
        print(f"  {n_sw} swap(s) executed:")
        for e in log6: print(e)
    else:
        print(f"  No improving swaps found. Phase 5 solution is locally optimal.")
    print(f"\n  Phase 6 result: utility={u_after6:.6f}  E_slack={E_after6:.4f}")
    print(f"  Utility gain from swaps: {u_after6-u_after5:+.6f}")

    # ── FINAL SCHEDULE ────────────────────────────────────────────────────────
    tot_e,tot_u=print_schedule(
        seg_k,freq_idx,freq_set,cum,tasks,N_tsk,N_job,
        mapping,B_BUDGET,label="FINAL HEURISTIC SOLUTION")
    return seg_k,freq_idx,tot_u,tot_e


# ══════════════════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    tc_path=sys.argv[1] if len(sys.argv)>1 else "testcase.py"
    print(f"Loading testcase: {tc_path}")
    processors,tasks,B_BUDGET=load_testcase(tc_path)

    periods=[int(t['p_i']) for t in tasks]
    h=lcm_list(periods); quantum=gcd_list(periods)
    cum,N_seg=build_cum(tasks); N_tsk=len(tasks)
    N_job=[h//periods[i] for i in range(N_tsk)]

    print(f"\n{_S}"); print(f"  USRT Heuristic (Combined + Swap)  —  Instance"); print(_S2)
    print(f"  Processors   : {len(processors)}")
    print(f"  Frequencies  : {processors[0]['frequencies']}")
    print(f"  Energy budget: {B_BUDGET}    α={ALPHA}   β={BETA}")
    print(f"  Hyper-period : {h}    Quantum(GCD): {quantum}")
    print(_S2)
    total_util=sum(t['e_m']/t['p_i'] for t in tasks)
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
