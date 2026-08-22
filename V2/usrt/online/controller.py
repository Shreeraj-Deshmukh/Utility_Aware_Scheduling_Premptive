"""
Online controller — drives the precomputed DP at runtime with hard guarantees.

Holds the live (mutable) committed schedule, one ProcessorDP per processor, and
the single global energy pool.  On every early completion it:

  1. records the completing job's ACTUAL (reduced) execution and returns its
     energy windfall to the global pool;
  2. arbitrates how much of the pool this processor may spend, reserving for
     other processors by future utility density (doc Approach C);
  3. looks up the precomputed DP for the downstream chain and reconstructs the
     optimal (k, z) decisions for the observed (time, energy) windfall;
  4. HARD-VERIFIES the result against a DYNAMIC DBF (which credits the freed
     time of every already-completed job) and the global energy pool before
     committing — trimming to a feasible subset if necessary;
  5. lazily rebuilds the affected processor's DP so later completions stay
     exact after baselines change.

Why a *dynamic* DBF (not the offline worst-case test): the online phase exists
precisely because early completion frees slack the static WCET schedule cannot
see.  Feasibility must therefore be judged against what actually executed — job
J* contributing ACET, not WCET.  Adding work to downstream jobs in J*'s windows
is then provably safe (the window demand never rises above its original,
already-feasible value).  This is the honest "feasible under the observed
execution" guarantee, and it never permits a real deadline miss or B overrun.

Nothing here is probabilistic: decisions are the DP optimum, and a decision is
committed only if it provably satisfies every constraint.
"""

from collections import namedtuple

from ..models     import total_energy, total_utility, energy_val, e_eff_val
from ..utils      import lcm_list, build_cum, build_job_times, build_proc_jobs
from .dp          import build_processor_dp
from .density     import future_utility_density, arbitrate_energy
from .energy_pool import SharedEnergyPool

_TOL = 1e-9

# An applied online decision (committed).
JobDecision = namedtuple(
    "JobDecision",
    ["x", "i", "j", "k_off", "z_off", "k", "z", "a_t", "a_e", "gain"],
)


class OnlineController:
    """Runtime owner of the committed schedule + per-processor DPs + energy pool."""

    def __init__(self, processors, tasks, B, seg_k, freq_idx, mapping,
                 arbitration="proportional", max_frontier=256):
        self.processors = processors
        self.tasks      = tasks
        self.B          = B
        self.max_frontier = max_frontier
        self.N_tsk      = len(tasks)
        self.N_prc      = len(processors)
        self.freq_set   = processors[0]['frequencies']
        self.periods    = [int(t['p_i']) for t in tasks]
        self.h          = lcm_list(self.periods)
        self.N_job      = [self.h // self.periods[i] for i in range(self.N_tsk)]
        self.cum, self.N_seg = build_cum(tasks)
        self.job_r, self.job_d = build_job_times(tasks, self.h)
        self.arbitration = arbitration

        # Live committed decision (mutated as the schedule runs).
        self.seg_k    = dict(seg_k)
        self.freq_idx = dict(freq_idx)
        self.mapping  = dict(mapping)
        self.proc_jobs, self.proc_jobs_map = build_proc_jobs(self.mapping)

        # Effective-time overrides for jobs that have ALREADY completed early.
        # (i, j) -> actual effective time < its committed WCET effective time.
        self.eff_override = {}

        # Global energy pool = remaining budget after the committed schedule.
        # Shared by ALL per-processor DPs, guarded by a binary semaphore.  Grows
        # (refund) as jobs complete under budget; shrinks (try_spend) as any
        # processor commits optional segments.  This is the ONLY cross-processor
        # shared variable — timing is per-processor and lock-free.
        self.pool = SharedEnergyPool(B - self.total_energy())

        # Per-processor DP precompute (one per processor; covers all suffixes).
        self.dps = {}
        for x in range(self.N_prc):
            self.dps[x] = self._build_dp(x)

        # Position of each job in its processor's EDF chain.
        self.pos_of = {}
        for x, dp in self.dps.items():
            for slot in dp.slots:
                self.pos_of[(slot.i, slot.j)] = slot.pos

        # ── Δt-scalar approximation instrumentation ──────────────────────────
        # Measures how much utility the scalar-Δt DP over-promises that the exact
        # commit-time DBF then trims (the Issue-4 gap).  If trim_loss stays ~0,
        # the per-window vector state would buy nothing here.
        self.promised_total  = 0.0   # Σ DP table value at each event
        self.committed_total = 0.0   # Σ utility actually kept after the DBF trim
        self.trim_events     = 0     # events where the trim removed some utility
        self.trim_loss       = 0.0   # Σ (promised − committed) over those events
        self.trims           = []    # (event_job, #planned, #committed, gap)

        self.applied = []   # history of JobDecision

    # ── construction helpers ────────────────────────────────────────────────
    def _build_dp(self, x):
        # Structural per-job time cap = deadline interval (a job cannot occupy
        # more than its own window).  The real limiter on additions is the
        # observed time windfall (the DP's dt budget) plus the dynamic-DBF
        # gate at commit time — NOT the offline-exhausted static slack.
        time_caps = {(i, j): float(self.job_d[(i, j)] - self.job_r[(i, j)])
                     for (i, j) in self.proc_jobs[x]}
        return build_processor_dp(
            x, self.proc_jobs, self.seg_k, self.freq_idx,
            self.job_r, self.job_d, self.cum, self.N_seg,
            self.freq_set, self.tasks, time_caps=time_caps,
            max_frontier=self.max_frontier)

    # ── metrics ──────────────────────────────────────────────────────────────
    def _eff(self, i, j):
        """Effective time of (i, j): actual if already completed, else committed."""
        if (i, j) in self.eff_override:
            return self.eff_override[(i, j)]
        return self.cum[i][self.seg_k[(i, j)]] / self.freq_set[self.freq_idx[(i, j)]]

    def total_energy(self):
        return total_energy(self.seg_k, self.freq_idx, self.freq_set,
                            self.cum, self.N_tsk, self.N_job)

    def total_utility(self):
        return total_utility(self.seg_k, self.tasks, self.cum,
                            self.N_tsk, self.N_job)

    def is_feasible(self):
        """Honest verdict: dynamic DBF (credits completed jobs) + energy pool >= 0."""
        return self._timing_ok_dynamic() and self.pool.level() >= -1e-6

    # ── dynamic DBF feasibility ───────────────────────────────────────────────
    def _timing_ok_dynamic(self, only_x=None):
        """
        Preemptive-EDF DBF using each job's ACTUAL effective time (reduced for
        already-completed jobs).  Adding work to a downstream job in a window
        where an earlier job finished early keeps the window demand at or below
        its original, already-feasible value.

        Timing is per-processor once the mapping is fixed (paper II), so when
        committing on processor `only_x` we check ONLY that processor — this is
        both cheaper and lock-free: it never reads another processor's live
        state, so it is safe to run while other processors commit concurrently.
        `only_x=None` checks all processors (used by is_feasible()).
        """
        xs = (only_x,) if only_x is not None else range(self.N_prc)
        for x in xs:
            jobs = self.proc_jobs[x]
            if not jobs:
                continue
            Ax = sorted({self.job_r[ij] for ij in jobs})
            Dx = sorted({self.job_d[ij] for ij in jobs})
            for t1 in Ax:
                for t2 in Dx:
                    if t1 >= t2:
                        continue
                    demand = 0.0
                    for (i, j) in jobs:
                        if self.job_r[(i, j)] >= t1 and self.job_d[(i, j)] <= t2:
                            demand += self._eff(i, j)
                    if demand > (t2 - t1) + 1e-9:
                        return False
        return True

    # ── densities / arbitration ──────────────────────────────────────────────
    def _densities(self, t):
        return {
            x: future_utility_density(
                x, t, self.proc_jobs, self.tasks, self.cum, self.N_seg,
                self.seg_k, self.job_r, self.periods)
            for x in range(self.N_prc)
        }

    # ── the online event ──────────────────────────────────────────────────────
    def on_completion(self, i, j, observed_dt, observed_de):
        """
        Handle early completion of job (i, j): time windfall `observed_dt`
        (processor-local) and energy windfall `observed_de` (to the global pool).

        Returns (added_utility, [JobDecision, ...]) actually committed.
        """
        x = self.proc_jobs_map[(i, j)]
        c = self.pos_of[(i, j)]

        # 1) record the completed job's ACTUAL (reduced) execution + free energy.
        #    refund() is atomic under the semaphore: the freed energy is visible
        #    to every other processor's next pool read.
        committed_eff = self.cum[i][self.seg_k[(i, j)]] / self.freq_set[self.freq_idx[(i, j)]]
        self.eff_override[(i, j)] = max(0.0, committed_eff - observed_dt)
        self.pool.refund(observed_de)

        # 2) arbitrate this processor's claim on the shared pool by future
        #    utility density.  We read a LIVE snapshot of the pool level under
        #    the lock; the value is advisory (another processor may spend before
        #    we commit) — the hard guarantee is the atomic try_spend in step 4.
        t = self.job_r[(i, j)]
        pool_now  = self.pool.level()
        densities = self._densities(t)
        caps      = arbitrate_energy(pool_now, densities, self.arbitration)
        de_budget = min(pool_now, max(0.0, caps.get(x, 0.0)))

        # 3) DP lookup + reconstruction for the downstream chain jobs[c+1:].
        dp_value, planned = self.dps[x].distribute(c + 1, observed_dt, de_budget)

        # 4) hard-verify (per-processor dynamic DBF + atomic pool spend), trimming
        #    if necessary.  All energy is deducted through pool.try_spend inside.
        committed = self._commit_with_guarantee(x, planned)

        # ── instrument the scalar-Δt approximation cost ──────────────────────
        # In the deterministic single-thread run the energy batch always fits
        # (the DP already respected de_budget ≤ pool), so any shortfall here is
        # the DBF trim removing utility the scalar-Δt DP over-promised.
        committed_gain = sum(d.gain for d in committed)
        gap = dp_value - committed_gain
        self.promised_total  += dp_value
        self.committed_total += committed_gain
        if gap > 1e-9:
            self.trim_events += 1
            self.trim_loss   += gap
            self.trims.append(((i, j), len(planned), len(committed), gap))

        # 5) rebuild this processor's DP so later completions stay exact.
        self.dps[x] = self._build_dp(x)
        for slot in self.dps[x].slots:
            self.pos_of[(slot.i, slot.j)] = slot.pos

        out = [JobDecision(x=x, i=d.i, j=d.j, k_off=d.k_off, z_off=d.z_off,
                           k=d.k, z=d.z, a_t=d.a_t, a_e=d.a_e, gain=d.gain)
               for d in committed]
        self.applied.extend(out)
        return sum(d.gain for d in committed), out

    def _commit_with_guarantee(self, x, planned):
        """
        Apply `planned` on processor `x`, verifying the per-processor dynamic DBF
        (lock-free) and deducting energy through the shared pool's ATOMIC
        try_spend (semaphore-guarded).  If the whole set is feasible it is kept;
        otherwise it is reverted and re-applied greedily (highest gain first),
        keeping only decisions that preserve both constraints.  The committed
        schedule always satisfies timing and the global energy budget.

        Ordering per decision: timing is checked FIRST (cheap, lock-free); only
        if timing passes do we touch the pool — so a rejected decision never
        needs an energy refund.  The fast path spends the batch atomically and
        refunds it if the batch fails the timing check.

        GRACEFUL DEGRADATION: when a planned segment addition (k > k_off) does
        not fit at its target k, we do NOT drop the job to baseline — we retry
        k-1, k-2, … down to k_off+1, DBF-checking every level, and keep the
        largest that satisfies timing + energy.  This recovers utility the
        all-or-nothing trim used to discard (a job that could take *some* extra
        segments no longer takes *none*).  It is a partial, cheap remedy for the
        scalar-Δt over-planning; the exact per-window DP would avoid planning the
        infeasible k in the first place.
        """
        if not planned:
            return []

        backup_seg  = {(d.i, d.j): self.seg_k[(d.i, d.j)]    for d in planned}
        backup_freq = {(d.i, d.j): self.freq_idx[(d.i, d.j)] for d in planned}

        # ── Fast path: the whole set at once. ────────────────────────────────
        for d in planned:
            self.seg_k[(d.i, d.j)]    = d.k
            self.freq_idx[(d.i, d.j)] = d.z
        if self._timing_ok_dynamic(only_x=x):
            # Timing holds; try to claim the batch energy atomically.
            if self.pool.try_spend_batch([d.a_e for d in planned]):
                return list(planned)
            # Not enough shared energy for the whole batch → fall through.

        # ── Revert and try greedily. ─────────────────────────────────────────
        for ij, kv in backup_seg.items():
            self.seg_k[ij] = kv
        for ij, zv in backup_freq.items():
            self.freq_idx[ij] = zv

        committed = []
        # Highest gain first.  Among EQUAL gains commit the CHEAPER decision
        # first (least time + energy): the trim below drops whatever no longer
        # fits, so spending the scarce resources on the cheapest of two equally
        # valuable options leaves room for more of them.
        for d in sorted(planned,
                        key=lambda p: (-p.gain, p.a_t + p.a_e, p.i, p.j)):
            i, j = d.i, d.j

            # Pure frequency change (no segment gain): single-shot, nothing to
            # degrade — apply the exact (k_off, z) or drop to baseline.
            if d.k <= d.k_off:
                self.seg_k[(i, j)]    = d.k
                self.freq_idx[(i, j)] = d.z
                if self._timing_ok_dynamic(only_x=x) and self.pool.try_spend(d.a_e):
                    committed.append(d)
                else:
                    self.seg_k[(i, j)]    = d.k_off
                    self.freq_idx[(i, j)] = d.z_off
                continue

            # Segment addition: try the DP's target k, then degrade k-1, k-2, …
            # down to k_off+1.  DBF-check EVERY level; keep the largest that fits.
            base_en  = energy_val(self.cum[i][d.k_off], self.freq_set[d.z_off])
            base_eff = e_eff_val(self.cum[i][d.k_off], self.freq_set[d.z_off])
            fz       = self.freq_set[d.z]
            for kp in range(d.k, d.k_off, -1):
                self.seg_k[(i, j)]    = kp
                self.freq_idx[(i, j)] = d.z
                a_e_kp = energy_val(self.cum[i][kp], fz) - base_en
                # Timing first (lock-free); only then claim energy atomically.
                if self._timing_ok_dynamic(only_x=x) and self.pool.try_spend(a_e_kp):
                    committed.append(d._replace(
                        k=kp,
                        a_t=e_eff_val(self.cum[i][kp], fz) - base_eff,
                        a_e=a_e_kp,
                        gain=self.tasks[i]['u_i'] * (self.cum[i][kp] - self.cum[i][d.k_off]),
                    ))
                    break
                # level kp infeasible → back to baseline, try a smaller k
                self.seg_k[(i, j)]    = d.k_off
                self.freq_idx[(i, j)] = d.z_off
        return committed
