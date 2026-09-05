"""
Quantum SPS Mapping  (Phase 1, canonical implementation).

Per quantum [q_start, q_end]:
  1. Collect newly-arrived + leftover jobs.
  2. Classify: mandatory (d == q_end), optional (d > q_end).
  3. Pre-filter: if total utilisation > remaining capacity, defer latest-
     deadline optional jobs until it fits.
  4. Run DPS + SPS to get a balanced assignment.
  5. Check per-processor utilisation ≤ 1.0; if not, defer more optionals.
  6. Commit assignment; update running proc_util.

After all quanta: DBF check (mandatory only, f_max) + greedy repair.

Load metric  : util_i = e_m_i / p_i  (correct for preemptive EDF).
Feasibility  : cumulative per-processor utilisation ≤ 1.0.
"""

from collections import defaultdict
from .dps_sps import run_dps, run_sps
from .repair  import check_dbf_mandatory, repair_mapping
from ..utils  import generate_jobs


def quantum_sps_mapping(tasks, processors, h, quantum, verbose=True,
                        job_weight=None):
    """
    Map all jobs to processors using per-quantum SPS.

    job_weight : optional {(i, j): float} giving the item size DPS/SPS balances
                 on.  Defaults to mandatory work share e_m_i/h.  ILP v3 passes
                 PREDICTED total work (mandatory + affordable optional) so the
                 packer balances what the schedule will actually carry -- see
                 mapping/predictive.py.  Only the item sizes change; the
                 criss-cross algorithm and the capacity gate are untouched.

    Returns: mapping dict  {(i, j): proc_idx}.
    """
    def _w(i, j):
        """Item size DPS/SPS balances on.  The default is the historical
        e_m/p_i -- deliberately NOT the e_m/h capacity metric, so the validated
        default path is bit-identical.  (e_m/h as a BALANCE metric looks
        promising but is a separate change needing its own measurement.)"""
        if job_weight is None:
            return tasks[i]['e_m'] / tasks[i]['p_i']
        return job_weight[(i, j)]

    def _dw(i, j):
        """Deferral ranking key.  Historically e_m/p_i; left EXACTLY as it was
        on the default path so the validated behaviour is bit-identical, and
        follows the supplied weight when one is given."""
        if job_weight is None:
            return tasks[i]['e_m'] / tasks[i]['p_i']
        return job_weight[(i, j)]
    m        = len(processors)
    all_jobs = generate_jobs(tasks, h)

    by_arr = defaultdict(list)
    for job in all_jobs:
        by_arr[job[2]].append(job)

    mapping   = {}
    proc_util = [0.0] * m
    leftover  = []

    if verbose:
        print(f"\n  {'Quantum':^12}  {'Mand':>5}  {'Opt':>5}  "
              f"{'Actv':>5}  {'Defr':>5}  {'MaxUtil':>9}  Status")
        print(f"  {'─'*68}")

    for q_start in range(0, h, quantum):
        q_end   = q_start + quantum
        newly   = by_arr.get(q_start, [])
        pending = leftover + newly
        leftover = []

        if not pending:
            continue

        mandatory = [(i, j, r, d) for (i, j, r, d) in pending if d == q_end]
        optional  = [(i, j, r, d) for (i, j, r, d) in pending if d >  q_end]
        # Deadline first.  Among jobs sharing a deadline the key ties, and the
        # tie decided placement order purely by list construction; prefer the
        # HEAVIER job (larger e_m/p_i) so that when capacity forces a deferral
        # the most capacity is freed per job deferred.
        optional.sort(key=lambda x: (x[3], -_dw(x[0], x[1]), x[0], x[1]))

        n_mand   = len(mandatory)
        n_opt    = len(optional)
        active   = mandatory + optional
        final_ps = None
        deferred = 0
        status   = "OK"

        while True:
            if not active:
                status = "EMPTY"; break

            # JOB-SHARE metric: one job of task i occupies e_m_i/h of a
            # processor over the hyper-period.  Summing this over a task's
            # h/p_i jobs recovers e_m_i/p_i exactly, so proc_util below stays a
            # true utilisation however the task's jobs are split across cores.
            total_util_active = sum(tasks[i]['e_m'] / h
                                    for (i, j, r, d) in active)
            remaining_cap     = sum(1.0 - proc_util[x] for x in range(m))

            if total_util_active > remaining_cap + 1e-9:
                opt_now = [(i, j, r, d) for (i, j, r, d) in active if d > q_end]
                if not opt_now:
                    status = "MAND_OVERUTIL"; break
                # latest deadline (least urgent) defers first; among equal
                # deadlines defer the HEAVIEST, which frees the most capacity
                to_defer = max(opt_now,
                               key=lambda x: (x[3], _dw(x[0], x[1]), x[0], x[1]))
                active.remove(to_defer); leftover.append(to_defer)
                deferred += 1; continue

            # Heaviest-first (DPS wants that).  The key e_m/p_i is a PER-TASK
            # quantity, so EVERY job of a task ties -- previously resolved by
            # list order.  Among equal load, place the EARLIER-DEADLINE job
            # first: it is the more constrained one, and DPS fills the largest
            # gap, so the tighter job gets the better choice of processor.
            # deterministic, but WITHOUT the deadline preference (that variant
            # measured slightly worse: ilp_v2 4.79% -> 4.99%)
            jl      = sorted([((i, j), _w(i, j))
                              for (i, j, r, d) in active],
                             key=lambda x: (-x[1], x[0]))
            ps_list = run_dps(jl, m)
            result  = run_sps(ps_list)

            if result is None:
                status = "SPS_NONE"; break

            new_util = list(proc_util)
            for px, job_set in enumerate(result.assign):
                for (i, j) in job_set:
                    new_util[px] += tasks[i]['e_m'] / h

            if max(new_util) <= 1.0 + 1e-9:
                final_ps  = result
                proc_util = new_util
                status    = f"util={max(new_util):.3f}"
                break

            opt_now = [(i, j, r, d) for (i, j, r, d) in active if d > q_end]
            if not opt_now:
                final_ps  = result
                proc_util = new_util
                status    = f"OVER(util={max(new_util):.3f})"
                break
            to_defer = max(opt_now, key=lambda x: x[3])
            active.remove(to_defer); leftover.append(to_defer)
            deferred += 1

        if verbose:
            print(f"  [{q_start:>4},{q_end:>4}]  {n_mand:>5}  {n_opt:>5}  "
                  f"{len(active):>5}  {deferred:>5}  {max(proc_util):>9.4f}  {status}")

        if final_ps:
            for px, job_set in enumerate(final_ps.assign):
                for (i, j) in job_set:
                    mapping[(i, j)] = px

    # Handle remaining leftover
    if leftover:
        if verbose:
            print(f"\n  [!] {len(leftover)} leftover job(s). Assigning to min-util processor.")
        for (i, j, r, d) in leftover:
            px = min(range(m), key=lambda x: proc_util[x])
            mapping[(i, j)] = px
            proc_util[px]  += tasks[i]['e_m'] / h
            if verbose:
                print(f"      T{tasks[i]['id']},job{j}  r={r}  d={d}  → P{px}")

    # Ensure all jobs are mapped
    expected = {(i, j) for (i, j, r, d) in generate_jobs(tasks, h)}
    missing  = expected - set(mapping.keys())
    if missing:
        if verbose:
            print(f"\n  [!] {len(missing)} job(s) unmapped. Assigning to min-util proc.")
        for (i, j) in sorted(missing):
            px = min(range(m), key=lambda x: proc_util[x])
            mapping[(i, j)] = px
            proc_util[px]  += tasks[i]['e_m'] / h

    # DBF check + repair
    ok, viols = check_dbf_mandatory(mapping, tasks, processors, h)
    if not ok:
        n_v = sum(len(v) for v in viols.values())
        if verbose:
            print(f"\n  DBF: {n_v} violation(s) → repair…")
        mapping, rep = repair_mapping(mapping, tasks, processors, h)
        if verbose:
            print(f"  Repair: {'OK ✓' if rep else 'PARTIAL'}")
    else:
        if verbose:
            print(f"\n  DBF: FEASIBLE ✓")

    return mapping
