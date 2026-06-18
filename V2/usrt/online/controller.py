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

from ..models   import total_energy, total_utility
from ..utils    import lcm_list, build_cum, build_job_times, build_proc_jobs
from .dp        import build_processor_dp
from .density   import future_utility_density, arbitrate_energy

_TOL = 1e-9

# An applied online decision (committed).
JobDecision = namedtuple(
    "JobDecision",
    ["x", "i", "j", "k_off", "z_off", "k", "z", "a_t", "a_e", "gain"],
)


class OnlineController:
    """Runtime owner of the committed schedule + per-processor DPs + energy pool."""

    def __init__(self, processors, tasks, B, seg_k, freq_idx, mapping,
                 arbitration="proportional"):
        self.processors = processors
        self.tasks      = tasks
        self.B          = B
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
        # Grows as jobs complete using less than budgeted; shrinks as we spend.
        self.energy_pool = B - self.total_energy()

        # Per-processor DP precompute (one per processor; covers all suffixes).
        self.dps = {}
        for x in range(self.N_prc):
            self.dps[x] = self._build_dp(x)

        # Position of each job in its processor's EDF chain.
        self.pos_of = {}
        for x, dp in self.dps.items():
            for slot in dp.slots:
                self.pos_of[(slot.i, slot.j)] = slot.pos

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
            self.freq_set, self.tasks, time_caps=time_caps)

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
        return self._timing_ok_dynamic() and self.energy_pool >= -1e-6

    # ── dynamic DBF feasibility ───────────────────────────────────────────────
    def _timing_ok_dynamic(self):
        """
        Preemptive-EDF DBF across all processors, using each job's ACTUAL
        effective time (reduced for already-completed jobs).  Adding work to a
        downstream job in a window where an earlier job finished early keeps the
        window demand at or below its original, already-feasible value.
        """
        for x in range(self.N_prc):
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
        committed_eff = self.cum[i][self.seg_k[(i, j)]] / self.freq_set[self.freq_idx[(i, j)]]
        self.eff_override[(i, j)] = max(0.0, committed_eff - observed_dt)
        self.energy_pool += observed_de

        # 2) arbitrate the global pool across processors by future density.
        t = self.job_r[(i, j)]
        densities = self._densities(t)
        caps = arbitrate_energy(self.energy_pool, densities, self.arbitration)
        de_budget = min(self.energy_pool, max(0.0, caps.get(x, 0.0)))

        # 3) DP lookup + reconstruction for the downstream chain jobs[c+1:].
        _, planned = self.dps[x].distribute(c + 1, observed_dt, de_budget)

        # 4) hard-verify (dynamic DBF + energy pool), trimming if necessary.
        committed = self._commit_with_guarantee(planned)

        # 5) update energy pool by net energy actually spent, rebuild DP for x.
        spent = sum(d.a_e for d in committed)
        self.energy_pool -= spent
        self.dps[x] = self._build_dp(x)
        for slot in self.dps[x].slots:
            self.pos_of[(slot.i, slot.j)] = slot.pos

        out = [JobDecision(x=x, i=d.i, j=d.j, k_off=d.k_off, z_off=d.z_off,
                           k=d.k, z=d.z, a_t=d.a_t, a_e=d.a_e, gain=d.gain)
               for d in committed]
        self.applied.extend(out)
        return sum(d.gain for d in committed), out

    def _commit_with_guarantee(self, planned):
        """
        Apply `planned`, verify dynamic DBF + energy pool.  If the full set is
        feasible, keep it; else revert and re-apply greedily (highest gain
        first), keeping only decisions that preserve feasibility.  The committed
        schedule always satisfies every constraint.
        """
        if not planned:
            return []

        backup_seg  = {(d.i, d.j): self.seg_k[(d.i, d.j)]    for d in planned}
        backup_freq = {(d.i, d.j): self.freq_idx[(d.i, d.j)] for d in planned}

        # Fast path: the whole set.
        spent = 0.0
        for d in planned:
            self.seg_k[(d.i, d.j)]    = d.k
            self.freq_idx[(d.i, d.j)] = d.z
            spent += d.a_e
        if self._timing_ok_dynamic() and (self.energy_pool - spent) >= -1e-6:
            return list(planned)

        # Revert.
        for ij, kv in backup_seg.items():
            self.seg_k[ij] = kv
        for ij, zv in backup_freq.items():
            self.freq_idx[ij] = zv

        # Greedy re-apply with per-step verification.
        committed, run_spent = [], 0.0
        for d in sorted(planned, key=lambda p: -p.gain):
            prev_k = self.seg_k[(d.i, d.j)]
            prev_z = self.freq_idx[(d.i, d.j)]
            self.seg_k[(d.i, d.j)]    = d.k
            self.freq_idx[(d.i, d.j)] = d.z
            if (self._timing_ok_dynamic() and
                    (self.energy_pool - (run_spent + d.a_e)) >= -1e-6):
                committed.append(d)
                run_spent += d.a_e
            else:
                self.seg_k[(d.i, d.j)]    = prev_k
                self.freq_idx[(d.i, d.j)] = prev_z
        return committed
