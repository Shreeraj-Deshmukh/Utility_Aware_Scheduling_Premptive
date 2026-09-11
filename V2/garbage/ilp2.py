"""
USRT ILP v2  —  Corrected Implementation
=========================================

ROOT CAUSES OF PREVIOUS BUGS (and their fixes)
------------------------------------------------
BUG 1 — CRITICAL: C_max ≤ quantum check is WRONG for preemptive scheduling.
    e.g. task3 has e_m=20.63 with GCD=15. C_max check always fails for this
    task, so it gets deferred every quantum, ends up force-mapped via
    round-robin → terrible mapping → ILP infeasible.

    FIX: Use PER-PROCESSOR UTILISATION (Σ e_m_i/p_i ≤ 1.0) as the
    feasibility criterion. For preemptive EDF, utilisation ≤ 1 per processor
    is the correct feasibility condition (necessary + sufficient for harmonic
    periods by Liu & Layland). A job with e_m=20.63, p=90 has utilisation
    0.229 and is perfectly schedulable; it just spreads its execution across
    the whole period [0,90], not just one quantum.

BUG 2 — Ratio bound used tn in denominator (1 + (m-1)*t1/(n*tn)).
    When any job has tiny e_m (tasks 4,5 have e_o_k ≈ 0.12), tn→0 and
    bound→∞, removing all optional jobs unnecessarily.

    FIX: Use only the simple C* lower bound:
        C*_lb = max(max_util, total_util / m)
    as a CHEAP PRE-FILTER before running SPS. This never blows up.

BUG 3 — Missing jobs silently dropped if leftover pool never clears.
    FIX: Track proc_util across quanta. Final leftover jobs are assigned
    to the processor with most remaining capacity (not round-robin).

BUG 4 — Global DBF check passed even when ILP was infeasible because
    check used e_m (f_max) but ILP uses lower frequencies (e_eff > e_m).
    FIX: DBF check is correct (e_m at f_max). If DBF passes at f_max,
    the ILP with (k=0, z=max_freq) is always a valid solution (k=0 means
    mandatory only, z=max gives shortest execution time). ILP infeasibility
    can only come from a bad mapping; repair_mapping handles this.

PHASE 1 ALGORITHM (per quantum [q, q+GCD])
------------------------------------------
  Load metric : utilisation  util_i = e_m_i / p_i
  Feasibility : cumulative per-processor utilisation ≤ 1.0

  1. Collect arrived + leftover jobs.f
  2. Classify: mandatory (d == q+GCD), optional (d > q+GCD).
  3. Quick pre-filter (O(n)):
       remaining_cap = 1.0 - current proc util
       If total_util_active > sum(remaining_cap):
           some jobs MUST be deferred → remove latest-deadline optionals first.
  4. Run DPS + SPS.
  5. Check if resulting per-processor utilisation stays ≤ 1.0.
  6. If not → remove one optional (latest deadline) → goto 4.
  7. Commit mapping; update running proc_util.

  After all quanta: global DBF check + greedy repair.

PHASE 2 (ILP v2, exactly per paper Section IV)
-----------------------------------------------
  Variable Y(i,j,k,z): 1 iff job T_{i,j} runs at freq f_z up to segment k.
  C1  : Σ_{k,z} Y(i,j,k,z) = 1   ∀i,j
  C2  : DBF(t1,t2,x) ≤ t2-t1      ∀x, t1∈Ax, t2∈Dx  (only jobs on Px)
  C3  : Σ_{i,j,k,z} Y·E ≤ B
  Obj : max Σ u_i·(cum[i][k]-cum[i][0])·Y(i,j,k,z)  for k≥1

Testcase : testcase.py  →  processors, tasks, B_BUDGET
"""

import sys
import importlib.util
from math import gcd as _gcd
from collections import defaultdict

import gurobipy as gp
from gurobipy import GRB

# ── energy model coefficients ─────────────────────────────────────────────────
# Imported from the single source of truth (usrt/models.py) so this solver can
# never drift from the rest of the project.  These were previously hard-coded to
# ALPHA=1.0, BETA=0.5 -- the stale pair -- which silently solved a DIFFERENT
# energy model whenever this file was run standalone: under 1.0/0.5 the energy
# optimum is f_max, whereas under the project's 0.15/1.0 it is f* ~= 0.42, so the
# two disagree about the entire DVFS trade-off.
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
    cum[i][k] = e_{i,0} + … + e_{i,k}   (at f_max; k=0 → mandatory only)
    N_seg[i]  = number of optional segments
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
    """-> list of (i, j, r_{i,j}, d_{i,j})"""
    jobs = []
    for i, t in enumerate(tasks):
        p = int(t['p_i']); n = h // p
        for j in range(n):
            jobs.append((i, j, j * p, (j + 1) * p))
    return jobs


# ══════════════════════════════════════════════════════════════════════════════
#  SPS / DPS
# ══════════════════════════════════════════════════════════════════════════════

class PS:
    """
    Partial solution for m machines.
    loads[j]  = total load on machine j  (sorted descending)
    assign[j] = set of (i,j_job) on machine j
    gap       = loads[0] - loads[-1]
    """
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
    """
    DPS procedure.  jobs_and_loads : [((i,j), util_val)] sorted descending.
    """
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
    """SPS algorithm: iteratively combine the two PS with the biggest gaps."""
    if not ps_list:
        return None
    active = list(ps_list)
    while len(active) > 1:
        active.sort(key=lambda ps: -ps.gap)
        merged = active[0].combine(active[1])
        active = active[2:] + [merged]
    return active[0]


# ══════════════════════════════════════════════════════════════════════════════
#  DBF FEASIBILITY CHECK  (mandatory only, f_max)
# ══════════════════════════════════════════════════════════════════════════════

def check_dbf(mapping, tasks, processors, h):
    """
    Global DBF check at f_max with mandatory segments only (k=0, z=max).
    If this passes, the ILP is guaranteed to have a feasible solution
    (set k=0, z=N_frq-1 for all jobs).

    Returns (is_feasible: bool,
             violations: {proc_idx: [(t1, t2, demand, capacity)]})
    """
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
        if not jobs_x:
            continue
        Ax = sorted({job_r[ij] for ij in jobs_x})
        Dx = sorted({job_d[ij] for ij in jobs_x})
        for t1 in Ax:
            for t2 in Dx:
                if t1 >= t2:
                    continue
                # S(t1,t2,x): jobs on x with r>=t1 and d<=t2
                window = [(i,j) for (i,j) in jobs_x
                          if job_r[(i,j)] >= t1 and job_d[(i,j)] <= t2]
                if not window:
                    continue
                demand = sum(tasks[i]['e_m'] for (i,j) in window)
                cap    = t2 - t1
                if demand > cap + 1e-9:
                    violations.setdefault(x, []).append((t1, t2, demand, cap))
    return len(violations) == 0, violations


def repair_mapping(mapping, tasks, processors, h):
    """
    Greedy DBF repair: find worst-violated (proc, window), move the job
    contributing most demand in that window to the processor with most
    remaining capacity.  Repeat until feasible or 100 iterations.
    """
    N_tsk   = len(tasks); m = len(processors)
    periods = [int(t['p_i']) for t in tasks]
    N_job   = [h // periods[i] for i in range(N_tsk)]
    job_r   = {(i,j): j*periods[i]      for i in range(N_tsk) for j in range(N_job[i])}
    job_d   = {(i,j): (j+1)*periods[i]  for i in range(N_tsk) for j in range(N_job[i])}

    for iteration in range(100):
        ok, viols = check_dbf(mapping, tasks, processors, h)
        if ok:
            return mapping, True

        # Worst violated window
        worst = max(
            ((x, t1, t2, dem, cap)
             for x, vlist in viols.items()
             for (t1, t2, dem, cap) in vlist),
            key=lambda v: v[3] - v[4]
        )
        x_bad, t1_bad, t2_bad = worst[0], worst[1], worst[2]

        # Offending jobs: on x_bad, in the violated window
        offenders = [(i,j) for (i,j), px in mapping.items()
                     if px == x_bad
                     and job_r[(i,j)] >= t1_bad
                     and job_d[(i,j)] <= t2_bad]
        if not offenders:
            break

        # Move the job with largest e_m (biggest demand contribution)
        mi, mj = max(offenders, key=lambda ij: tasks[ij[0]]['e_m'])

        # Target: processor with most remaining utilisation capacity
        util = defaultdict(float)
        for (i,j), px in mapping.items():
            util[px] += tasks[i]['e_m'] / tasks[i]['p_i']
        target = min((x for x in range(m) if x != x_bad),
                     key=lambda x: util[x])
        mapping[(mi, mj)] = target

    ok, _ = check_dbf(mapping, tasks, processors, h)
    return mapping, ok


# ══════════════════════════════════════════════════════════════════════════════
#  PHASE 1 : QUANTUM SPS MAPPING
# ══════════════════════════════════════════════════════════════════════════════

def quantum_sps_mapping(tasks, processors, h, quantum):
    """
    Per-quantum SPS mapping with utilisation-based feasibility.

    Load metric   : util_i = e_m_i / p_i  per job
    Feasibility   : cumulative per-processor utilisation ≤ 1.0
    Pre-filter    : O(n) check before running SPS
    Mandatory     : d_{i,j} == q+GCD  (must assign this quantum)
    Optional      : d_{i,j} >  q+GCD  (assign if capacity allows, else defer)

    WHY utilisation and NOT C_max ≤ quantum
    ----------------------------------------
    For PREEMPTIVE scheduling, a job can execute across multiple quanta.
    e.g. task3 has e_m=20.63, period=90 → utilisation=0.229 → perfectly
    feasible. But e_m > GCD=15, so C_max check would always fail,
    causing ALL task3 jobs to be force-mapped via round-robin → infeasible ILP.
    Utilisation ≤ 1 is the correct EDF feasibility condition.
    """
    m         = len(processors)
    all_jobs  = generate_jobs(tasks, h)

    by_arr = defaultdict(list)
    for job in all_jobs:
        by_arr[job[2]].append(job)   # key = arrival time

    mapping   = {}                        # (i,j) → proc_idx
    proc_util = [0.0] * m                 # running utilisation per processor
    leftover  = []                        # jobs deferred from earlier quanta

    print(f"\n  {'Quantum':^12}  {'Mand':>5}  {'Opt':>5}  "
          f"{'Actv':>5}  {'Defr':>5}  {'MaxUtil':>9}  Status")
    print(f"  {'─'*68}")

    for q_start in range(0, h, quantum):
        q_end    = q_start + quantum
        newly    = by_arr.get(q_start, [])
        pending  = leftover + newly
        leftover = []

        if not pending:
            continue

        mandatory = [(i,j,r,d) for (i,j,r,d) in pending if d == q_end]
        optional  = [(i,j,r,d) for (i,j,r,d) in pending if d >  q_end]
        # Keep most-urgent optional first (earliest deadline)
        optional.sort(key=lambda x: x[3])

        n_mand = len(mandatory)
        n_opt  = len(optional)
        active = mandatory + optional

        final_ps  = None
        deferred  = 0
        status    = "OK"

        while True:
            if not active:
                status = "EMPTY"; break

            util_vals = [(i,j, tasks[i]['e_m'] / tasks[i]['p_i'])
                         for (i,j,r,d) in active]
            total_util_active = sum(u for _,_,u in util_vals)
            max_util_active   = max(u for _,_,u in util_vals)

            # ── PRE-FILTER (O(n), no SPS) ─────────────────────────────────
            # Best-case: load balanced perfectly → each processor gets
            #   proc_util[x] + total_util_active / m
            # If even best-case exceeds 1.0, remove optional jobs immediately.
            remaining_cap  = [1.0 - proc_util[x] for x in range(m)]
            total_cap      = sum(remaining_cap)

            if total_util_active > total_cap + 1e-9:
                # Even perfect balance won't fit everything
                opt_now = [(i,j,r,d) for (i,j,r,d) in active if d > q_end]
                if not opt_now:
                    status = "MAND_OVERUTIL"; break
                to_defer = max(opt_now, key=lambda x: x[3])
                active.remove(to_defer); leftover.append(to_defer)
                deferred += 1
                continue

            # ── RUN DPS + SPS ─────────────────────────────────────────────
            jl = sorted([((i,j), tasks[i]['e_m'] / tasks[i]['p_i'])
                          for (i,j,r,d) in active],
                        key=lambda x: -x[1])
            ps_list = run_dps(jl, m)
            result  = run_sps(ps_list)

            if result is None:
                status = "SPS_NONE"; break

            # ── CHECK: will this keep per-proc utilisation ≤ 1.0? ─────────
            new_util = list(proc_util)   # tentative copy
            for px, job_set in enumerate(result.assign):
                for (i,j) in job_set:
                    new_util[px] += tasks[i]['e_m'] / tasks[i]['p_i']

            if max(new_util) <= 1.0 + 1e-9:
                # Feasible → commit
                final_ps  = result
                proc_util = new_util
                status    = f"util={max(new_util):.3f}"
                break

            # Not feasible → remove one optional
            opt_now = [(i,j,r,d) for (i,j,r,d) in active if d > q_end]
            if not opt_now:
                # Only mandatory remain and still > 1.0 → overloaded
                # Commit anyway; global DBF + repair will handle it
                final_ps  = result
                proc_util = new_util
                status    = f"OVER(util={max(new_util):.3f})"
                break
            to_defer = max(opt_now, key=lambda x: x[3])
            active.remove(to_defer); leftover.append(to_defer)
            deferred += 1

        print(f"  [{q_start:>4},{q_end:>4}]  "
              f"{n_mand:>5}  {n_opt:>5}  "
              f"{len(active):>5}  {deferred:>5}  "
              f"{max(proc_util):>9.4f}  {status}")

        if final_ps:
            for px, job_set in enumerate(final_ps.assign):
                for (i,j) in job_set:
                    mapping[(i,j)] = px

    # ── Handle remaining leftover: assign to processor with most capacity ──
    if leftover:
        print(f"\n  [!] {len(leftover)} leftover job(s). "
              f"Assigning to most-available processor.")
        for (i,j,r,d) in leftover:
            # least-loaded processor by utilisation
            px = min(range(m), key=lambda x: proc_util[x])
            mapping[(i,j)] = px
            proc_util[px] += tasks[i]['e_m'] / tasks[i]['p_i']
            print(f"      T{tasks[i]['id']},job{j}  r={r}  d={d}  → P{px}")

    # ── Ensure ALL jobs are mapped ─────────────────────────────────────────
    expected = {(i,j) for (i,j,r,d) in generate_jobs(tasks, h)}
    missing  = expected - set(mapping.keys())
    if missing:
        print(f"\n  [!] {len(missing)} job(s) still missing. Assigning to min-util proc.")
        for (i,j) in sorted(missing):
            px = min(range(m), key=lambda x: proc_util[x])
            mapping[(i,j)] = px
            proc_util[px] += tasks[i]['e_m'] / tasks[i]['p_i']

    # ── Global DBF check + repair ──────────────────────────────────────────
    print(f"\n  Proc utilisation after mapping: "
          f"{[round(u,4) for u in proc_util]}")
    print(f"  Running global DBF check (mandatory only, f_max) …")
    ok, viols = check_dbf(mapping, tasks, processors, h)
    if ok:
        print(f"  DBF: FEASIBLE ✓")
    else:
        n_v = sum(len(v) for v in viols.values())
        print(f"  DBF: {n_v} violation(s). Running greedy repair …")
        mapping, repaired = repair_mapping(mapping, tasks, processors, h)
        print(f"  Repair: {'SUCCESS ✓' if repaired else 'PARTIAL — ILP will enforce remaining'}")

    return mapping


# ══════════════════════════════════════════════════════════════════════════════
#  PHASE 2 : ILP v2  (exactly per paper, Section IV)
# ══════════════════════════════════════════════════════════════════════════════

def solve_ilp_v2(processors, tasks, B_BUDGET, mapping):
    """
    ILP v2 — Section IV of the paper.

    Variable Y(i,j,k,z) ∈ {0,1}
      = 1  iff  job T_{i,j} executes with frequency f_z up to segment k
               on processor P*_{i,j}  (fixed by SPS Phase 1)

    C1  : Σ_{k,z} Y(i,j,k,z) = 1          ∀i,j               (Eq.11)
    C2  : DBF(t1,t2,x) ≤ t2-t1             ∀x, t1∈Ax, t2∈Dx  (Eq.12-13)
    C3  : Σ_{i,j,k,z} Y·E(i,k,z) ≤ B                         (C3 from v1)
    Obj : max Σ_{i,j,k≥1,z} u_i·(cum[i][k]-cum[i][0])·Y      (Eq.8-10)
    """
    N_tsk    = len(tasks)
    N_prc    = len(processors)
    freq_set = processors[0]['frequencies']   # ascending; last entry = f_max = 1.0
    N_frq    = len(freq_set)
    periods  = [int(t['p_i']) for t in tasks]
    h        = lcm_list(periods)
    N_job    = [h // periods[i] for i in range(N_tsk)]
    cum, N_seg = build_cum(tasks)

    job_r = {(i,j): j*periods[i]      for i in range(N_tsk) for j in range(N_job[i])}
    job_d = {(i,j): (j+1)*periods[i]  for i in range(N_tsk) for j in range(N_job[i])}

    # Jobs per processor from Phase 1 SPS mapping
    proc_jobs = defaultdict(list)
    for (i,j), x in mapping.items():
        proc_jobs[x].append((i,j))

    def e_eff(i, k, z):
        return cum[i][k] / freq_set[z]

    def E(i, k, z):
        c = cum[i][k]; f = freq_set[z]
        return ALPHA * (c / f) + BETA * (f ** 2) * c

    # ── Build model ────────────────────────────────────────────────────────
    mdl = gp.Model("USRT_ILP_v2")
    mdl.setParam("OutputFlag", 1)

    # Y(i,j,k,z)  — no processor dimension (fixed by Phase 1)
    Y_keys = [(i,j,k,z)
              for i in range(N_tsk)
              for j in range(N_job[i])
              for k in range(N_seg[i]+1)
              for z in range(N_frq)]
    Y = mdl.addVars(Y_keys, vtype=GRB.BINARY, name="Y")

    # ── C1: each job exactly one (k, z) ───────────────────────────────────
    for i in range(N_tsk):
        for j in range(N_job[i]):
            mdl.addConstr(
                gp.quicksum(Y[i,j,k,z]
                            for k in range(N_seg[i]+1)
                            for z in range(N_frq)) == 1,
                name=f"C1_{i}_{j}"
            )

    # ── C2: DBF per processor (only jobs mapped to that processor) ─────────
    n_dbf = 0
    for x in range(N_prc):
        jobs_x = proc_jobs[x]
        if not jobs_x:
            continue
        # Ax, Dx: only from jobs mapped to x  (per paper Eq.12-13)
        Ax = sorted({job_r[ij] for ij in jobs_x})
        Dx = sorted({job_d[ij] for ij in jobs_x})
        for t1 in Ax:
            for t2 in Dx:
                if t1 >= t2:
                    continue
                # S(t1,t2,x): jobs on x with r_{i,j}>=t1 and d_{i,j}<=t2
                window = [(i,j) for (i,j) in jobs_x
                          if job_r[(i,j)] >= t1 and job_d[(i,j)] <= t2]
                if not window:
                    continue
                mdl.addConstr(
                    gp.quicksum(Y[i,j,k,z] * e_eff(i,k,z)
                                for (i,j) in window
                                for k in range(N_seg[i]+1)
                                for z in range(N_frq)) <= t2 - t1,
                    name=f"C2_x{x}_{int(t1)}_{int(t2)}"
                )
                n_dbf += 1

    # ── C3: energy budget ──────────────────────────────────────────────────
    mdl.addConstr(
        gp.quicksum(Y[i,j,k,z] * E(i,k,z)
                    for i in range(N_tsk)
                    for j in range(N_job[i])
                    for k in range(N_seg[i]+1)
                    for z in range(N_frq)) <= B_BUDGET,
        name="C3_energy"
    )

    # ── Objective: maximise total utility ─────────────────────────────────
    # U^job_{i,j} = u_i × Σ_{k≥1,z} Y(i,j,k,z) × (cum[i][k] − cum[i][0])
    # cum[i][0] = e_m_i  (mandatory only); cum[i][k]-cum[i][0] = optional work
    mdl.setObjective(
        gp.quicksum(
            tasks[i]['u_i'] * (cum[i][k] - cum[i][0]) * Y[i,j,k,z]
            for i in range(N_tsk)
            for j in range(N_job[i])
            for k in range(1, N_seg[i]+1)   # k=0 → no optional exec → 0 utility
            for z in range(N_frq)
        ),
        GRB.MAXIMIZE
    )

    print(f"\n  Y variables  : {len(Y_keys)}")
    print(f"  Constraints  : C1={sum(N_job)}   DBF={n_dbf}   Energy=1\n")

    mdl.optimize()
    _print_solution(mdl, Y, tasks, N_tsk, N_job, N_seg,
                    freq_set, N_frq, cum, E, e_eff, B_BUDGET, mapping)
    return mdl


# ══════════════════════════════════════════════════════════════════════════════
#  OUTPUT
# ══════════════════════════════════════════════════════════════════════════════

_S  = "=" * 76
_S2 = "-" * 76


def print_mapping_summary(mapping, tasks, processors, h):
    m       = len(processors)
    periods = [int(t['p_i']) for t in tasks]
    N_tsk   = len(tasks)
    N_job   = [h // periods[i] for i in range(N_tsk)]
    job_r   = {(i,j): j*periods[i]      for i in range(N_tsk) for j in range(N_job[i])}
    job_d   = {(i,j): (j+1)*periods[i]  for i in range(N_tsk) for j in range(N_job[i])}

    print(f"\n{_S}")
    print(f"  SPS MAPPING SUMMARY")
    print(_S2)
    for x in range(m):
        jobs_x = sorted((i,j) for (i,j), px in mapping.items() if px == x)
        em_tot = sum(tasks[i]['e_m'] for (i,j) in jobs_x)
        ul_tot = sum(tasks[i]['e_m'] / tasks[i]['p_i'] for (i,j) in jobs_x)
        flag   = '  ← OVERLOADED' if ul_tot > 1.0 else ''
        print(f"\n  Processor P{x}  |  {len(jobs_x)} jobs  "
              f"Σe_m={em_tot:.3f}  utilisation={ul_tot:.4f}{flag}")
        print(f"  {'Task':>5}  {'job':>4}  {'arrival':>8}  "
              f"{'deadline':>9}  {'e_m':>9}  {'util':>7}")
        print(f"  {'─'*50}")
        for (i,j) in jobs_x:
            u = tasks[i]['e_m'] / tasks[i]['p_i']
            print(f"  T{tasks[i]['id']:>4}  {j:>4}  "
                  f"{job_r[(i,j)]:>8}  {job_d[(i,j)]:>9}  "
                  f"{tasks[i]['e_m']:>9.4f}  {u:>7.4f}")
    print(_S)


def _print_solution(mdl, Y, tasks, N_tsk, N_job, N_seg,
                    freq_set, N_frq, cum, E, e_eff, B_BUDGET, mapping):
    smap = {GRB.OPTIMAL    : "OPTIMAL",
            GRB.INFEASIBLE : "INFEASIBLE",
            GRB.INF_OR_UNBD: "INF_OR_UNBOUNDED",
            GRB.TIME_LIMIT : "TIME_LIMIT (best shown)"}
    print(f"\n{_S}")
    print(f"  SOLVER STATUS : {smap.get(mdl.status, str(mdl.status))}")

    if mdl.SolCount == 0:
        if mdl.status == GRB.INFEASIBLE:
            print("  Computing IIS …")
            mdl.computeIIS()
            mdl.write("infeasible_v2.ilp")
            print("  IIS → infeasible_v2.ilp")
            print("\n  NOTE: If IIS points to a C2 (DBF) constraint, the SPS")
            print("  mapping has a processor that is overloaded in some time")
            print("  window. Check the mapping summary above for utilisation > 1.")
        print(_S); return

    print(f"  Objective (total utility) : {mdl.ObjVal:.6f}")
    print(_S)

    total_e = total_u = 0.0
    for i in range(N_tsk):
        u_i   = tasks[i]['u_i']
        procs = sorted({mapping.get((i,j),-1) for j in range(N_job[i])})
        print(f"\n  Task T{tasks[i]['id']}  period={tasks[i]['p_i']}  "
              f"u_i={u_i}  N_seg={N_seg[i]}  N_jobs={N_job[i]}  "
              f"proc(s)={procs}")
        print(f"  {'Job':>5}  {'Proc':>5}  {'Freq':>6}  {'k':>4}  "
              f"{'cum_work':>9}  {'e_eff':>8}  {'Energy':>10}  "
              f"{'Utility':>9}  Execution")
        print(f"  {_S2}")

        t_e = t_u = 0.0
        for j in range(N_job[i]):
            px = mapping.get((i,j), -1)
            for k in range(N_seg[i]+1):
                for z in range(N_frq):
                    if Y[i,j,k,z].X > 0.5:
                        ef  = e_eff(i, k, z)
                        en  = E(i, k, z)
                        opt = cum[i][k] - cum[i][0]
                        ut  = u_i * opt
                        t_e += en; t_u += ut
                        seg = ("mandatory only" if k == 0
                               else f"mandatory + {k} opt seg(s)")
                        print(f"  {j+1:>5}  P{px:<4}  "
                              f"{freq_set[z]:>6.3f}  {k:>4}  "
                              f"{cum[i][k]:>9.4f}  {ef:>8.4f}  "
                              f"{en:>10.4f}  {ut:>9.4f}  {seg}")
        total_e += t_e; total_u += t_u
        print(f"\n  {'':5}  Task T{tasks[i]['id']} totals : "
              f"energy={t_e:.4f}   utility={t_u:.4f}")

    print(f"\n{_S}")
    print(f"  Total energy  : {total_e:.4f}  "
          f"(budget={B_BUDGET}  slack={B_BUDGET-total_e:.4f})")
    print(f"  Total utility : {total_u:.6f}")
    print(_S)


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

    # ── Instance summary ──────────────────────────────────────────────────
    print(f"\n{_S}")
    print(f"  USRT ILP v2  —  Instance")
    print(_S2)
    print(f"  Processors   : {len(processors)}")
    print(f"  Frequencies  : {processors[0]['frequencies']}")
    print(f"  Energy budget: {B_BUDGET}    α={ALPHA}   β={BETA}")
    print(f"  Hyper-period : {h}    Quantum(GCD): {quantum}    "
          f"Quanta: {h//quantum}")
    print(_S2)
    total_util = sum(t['e_m'] / t['p_i'] for t in tasks)
    print(f"  {'TID':>4}  {'period':>7}  {'Nseg':>5}  {'Njobs':>6}  "
          f"{'e_m':>9}  {'util':>7}  e_o_k")
    print(f"  {_S2}")
    for i, t in enumerate(tasks):
        u = t['e_m'] / t['p_i']
        print(f"  {t['id']:>4}  {t['p_i']:>7}  {N_seg[i]:>5}  {N_job[i]:>6}  "
              f"{t['e_m']:>9.4f}  {u:>7.4f}  "
              f"{[round(x,4) for x in t['e_o_k']]}")
    feas = "FEASIBLE" if total_util <= len(processors) else "OVERLOADED"
    print(f"\n  Total utilisation : {total_util:.4f} / {len(processors)}"
          f"  [{feas}]")
    print(_S)

    # ══ PHASE 1: SPS MAPPING ═════════════════════════════════════════════
    print(f"\n{_S}")
    print(f"  PHASE 1 : QUANTUM SPS MAPPING")
    print(f"  Load metric  : utilisation  e_m / p_i")
    print(f"  Feasibility  : per-processor utilisation ≤ 1.0")
    print(_S2)
    mapping = quantum_sps_mapping(tasks, processors, h, quantum)
    print_mapping_summary(mapping, tasks, processors, h)

    # ══ PHASE 2: ILP v2 ══════════════════════════════════════════════════
    print(f"\n{_S}")
    print(f"  PHASE 2 : ILP v2  (frequency + segment optimisation)")
    print(_S2)
    solve_ilp_v2(processors, tasks, B_BUDGET, mapping)
