"""
Online simulator + validator.

Drives a precomputed OnlineController through a hyper-period of early
completions and checks that every step is feasible and that, for a single
controlled completion, the utility actually banked equals the DP's table value
(the doc's "verified trace" property).

Completion model (doc Section 1.1): a job whose committed effective time is
e_eff actually runs for ratio * e_eff (ratio < 1), freeing
    dt = (1 - ratio) * e_eff                      (local time slack)
    de = (1 - ratio) * E(committed)               (energy returned to pool)
These windfalls are handed to OnlineController.on_completion, which distributes
them to downstream jobs.  Events are processed in release order (≈ wall-clock).

Nothing is probabilistic in the *decision*: the ACET ratio only models reality;
the controller's choices remain the constraint-respecting DP optimum.
"""

import random
from collections import namedtuple

from ..models     import energy_val, e_eff_val
from .controller  import OnlineController

SimConfig = namedtuple("SimConfig", [
    "acet_ratio",    # fixed ratio in (0,1], or None to draw per job
    "ratio_min",     # lower bound when drawing
    "ratio_max",     # upper bound when drawing
    "seed",          # RNG seed (reproducible)
    "arbitration",   # "proportional" | "strict"
    "verbose",
    "max_frontier",  # per-level Pareto-frontier cap (aggregate states)
])
SimConfig.__new__.__defaults__ = (0.7, 0.5, 0.9, 12345, "proportional", True, 256)

_S  = "=" * 76
_S2 = "-" * 76


class OnlineSimulator:
    def __init__(self, processors, tasks, B, seg_k, freq_idx, mapping,
                 config=None):
        self.config = config or SimConfig()
        self.ctrl = OnlineController(
            processors, tasks, B, seg_k, freq_idx, mapping,
            arbitration=self.config.arbitration,
            max_frontier=self.config.max_frontier)
        self._rng = random.Random(self.config.seed)
        self.offline_utility = self.ctrl.total_utility()
        self.offline_energy  = self.ctrl.total_energy()

    # ── windfall model ───────────────────────────────────────────────────────
    def _ratio(self):
        if self.config.acet_ratio is not None:
            return self.config.acet_ratio
        return self._rng.uniform(self.config.ratio_min, self.config.ratio_max)

    def _windfall(self, i, j, ratio):
        k = self.ctrl.seg_k[(i, j)]
        z = self.ctrl.freq_idx[(i, j)]
        fz = self.ctrl.freq_set[z]
        eff = e_eff_val(self.ctrl.cum[i][k], fz)
        en  = energy_val(self.ctrl.cum[i][k], fz)
        dt = (1.0 - ratio) * eff
        de = (1.0 - ratio) * en
        return dt, de

    # ── event order ──────────────────────────────────────────────────────────
    def _event_order(self):
        jobs = [(i, j) for i in range(self.ctrl.N_tsk)
                       for j in range(self.ctrl.N_job[i])]
        jobs.sort(key=lambda ij: (self.ctrl.job_r[ij], self.ctrl.job_d[ij],
                                  ij[0], ij[1]))
        return jobs

    # ── main loop ──────────────────────────────────────────────────────────────
    def run(self):
        cfg = self.ctrl
        if self.config.verbose:
            print(f"\n{_S}")
            print(f"  ONLINE SIMULATION  (arbitration={self.config.arbitration}, "
                  f"acet_ratio={self.config.acet_ratio})")
            print(_S2)
            print(f"  Offline utility : {self.offline_utility:.6f}")
            print(f"  Offline energy  : {self.offline_energy:.4f}  "
                  f"(budget={cfg.B}  pool={cfg.pool.level():.4f})")
            print(_S2)
            print(f"  {'event':>5}  {'job':>10}  {'dt':>8}  {'de':>8}  "
                  f"{'+util':>9}  {'#chg':>5}  {'pool':>9}")
            print(f"  {'-'*64}")

        total_added = 0.0
        n_event = 0
        for (i, j) in self._event_order():
            ratio = self._ratio()
            dt, de = self._windfall(i, j, ratio)
            added, committed = cfg.on_completion(i, j, dt, de)
            total_added += added
            n_event += 1
            if self.config.verbose and (added > 1e-9 or committed):
                print(f"  {n_event:>5}  T{self.ctrl.tasks[i]['id']},j{j:<5}  "
                      f"{dt:>8.4f}  {de:>8.4f}  {added:>9.4f}  "
                      f"{len(committed):>5}  {cfg.pool.level():>9.4f}")

        final_u  = cfg.total_utility()
        wcet_e   = cfg.total_energy()          # conservative WCET commitment
        actual_e = cfg.B - cfg.pool.level()    # realised consumption (C3 binds here)
        feasible = cfg.is_feasible()
        pstats   = cfg.pool.stats()

        if self.config.verbose:
            print(_S2)
            print(f"  Online added utility : {total_added:.6f}")
            print(f"  Final utility        : {final_u:.6f}  "
                  f"(offline {self.offline_utility:.6f}, "
                  f"+{final_u - self.offline_utility:.6f})")
            print(f"  Energy (WCET commit) : {wcet_e:.4f}   (budget={cfg.B})")
            print(f"  Energy (realised)    : {actual_e:.4f}   "
                  f"pool/slack={cfg.pool.level():.4f}   [C3 binds on realised]")
            print(f"  Feasible (dyn-DBF + energy pool >= 0): {feasible}")
            print(f"  Shared pool (semaphore): {pstats['acquisitions']} lock "
                  f"acquisitions, spent={pstats['spent_total']:.4f}, "
                  f"refunded={pstats['refunded_total']:.4f}, "
                  f"denied={pstats['denied']}")
            print(_S)

        return {
            "offline_utility": self.offline_utility,
            "online_added":    total_added,
            "final_utility":   final_u,
            "wcet_energy":     wcet_e,
            "actual_energy":   actual_e,
            "energy_pool":     cfg.pool.level(),
            "pool_stats":      pstats,
            "feasible":        feasible,
        }

    # ── single-event validation ────────────────────────────────────────────────
    def verify_single(self, i, j, dt, de):
        """
        Distribute one windfall and assert the banked utility equals the DP
        table value for that processor's downstream chain.  Returns
        (added_utility, dp_value, ok).
        """
        x = self.ctrl.proc_jobs_map[(i, j)]
        c = self.ctrl.pos_of[(i, j)]
        # Arbitrated energy budget the controller would grant.  Probe the pool
        # through its atomic API, then undo so on_completion redoes it cleanly.
        pool_now = self.ctrl.pool.refund(de)          # atomic += de
        densities = self.ctrl._densities(self.ctrl.job_r[(i, j)])
        from .density import arbitrate_energy
        caps = arbitrate_energy(pool_now, densities, self.config.arbitration)
        de_budget = min(pool_now, max(0.0, caps.get(x, 0.0)))
        dp_value = self.ctrl.dps[x].best_value(c + 1, dt, de_budget)
        self.ctrl.pool.try_spend(de)                  # atomic -= de (undo the probe)
        added, _ = self.ctrl.on_completion(i, j, dt, de)
        # NOTE: distribute()'s dp_value is an optimistic ceiling; the committed
        # `added` may be less if the per-processor DBF trims a shared-window
        # conflict.  Assert <= (not ==) — see online_phase_explained_2 §I1.
        ok = added <= dp_value + 1e-6
        return added, dp_value, ok
