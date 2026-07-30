"""
SharedEnergyPool — the single global energy slack, shared by every processor.

Design context (paper Section VI "Two DP with shared Energy"; user decision
2026-06):
  * Time slack is processor-LOCAL — each processor's DP reasons about its own
    windows with no cross-processor coupling, so timing needs no lock.
  * Energy slack is a single GLOBAL pool that all per-processor DPs draw from
    and refund to, frequently.  It is the one variable shared across processors,
    so it — and only it — is guarded by a semaphore.

Concurrency model (user decision):
  * Execution is DETERMINISTIC and single-threaded (a fixed event order gives
    reproducible research numbers), but EVERY access to the pool goes through
    this lock-guarded object.  The code is therefore already thread-safe: flip
    the driver to one thread per processor and the same guarantees hold, because
    the read-modify-write below is atomic under the lock.
  * FINE-GRAINED locking: the critical section is only the pool's
    check-and-deduct (`try_spend`) and `refund`.  Arbitration, DP lookup, the
    per-processor timing check, and commit stay OUTSIDE the lock.

The guard is a binary semaphore (threading.Lock == a Semaphore(1) / mutex).
`try_spend` is the hard correctness gate: even if the pool changed between a
processor's arbitration snapshot and its commit (as it could under real
threads), the atomic check-and-deduct never lets the global consumption exceed
the budget, so C3 (total energy <= B) can never be violated by a race.
"""

import threading

_TOL = 1e-6


class SharedEnergyPool:
    """
    Atomic, semaphore-guarded global energy slack.

    Level semantics: `level` is the current global energy slack (budget minus
    realised consumption plus freed energy).  Feasibility requires level >= 0
    (within _TOL).  All mutation is atomic under `_sem`.
    """

    __slots__ = ("_level", "_sem", "_spent_total", "_refunded_total",
                 "_acquisitions", "_denied")

    def __init__(self, initial):
        self._level          = float(initial)
        self._sem            = threading.Lock()   # binary semaphore (mutex)
        # ── instrumentation (proves the guard is exercised) ──────────────────
        self._spent_total    = 0.0    # cumulative energy successfully spent
        self._refunded_total = 0.0    # cumulative energy returned by early finish
        self._acquisitions   = 0      # number of critical-section entries
        self._denied         = 0      # try_spend calls rejected for lack of slack

    # ── reads (still guarded: a consistent snapshot) ─────────────────────────
    def level(self):
        """Atomic snapshot of the current global energy slack."""
        with self._sem:
            self._acquisitions += 1
            return self._level

    # ── atomic mutations ─────────────────────────────────────────────────────
    def refund(self, amount):
        """
        Atomically return `amount` of freed energy to the global pool (a job
        finished using less than budgeted).  Returns the new level.  A negative
        `amount` is treated as 0 (refunds never reduce the pool).
        """
        if amount is None:
            amount = 0.0
        with self._sem:
            self._acquisitions += 1
            if amount > 0.0:
                self._level          += amount
                self._refunded_total += amount
            return self._level

    def try_spend(self, amount, tol=_TOL):
        """
        Atomically deduct `amount` IFF it keeps the pool >= -tol.  Returns True
        on success (deducted), False on failure (pool untouched).

        `amount <= 0` (a conversion action that frees energy) always succeeds and
        increases the pool.  This is the single hard energy gate: no interleaving
        of concurrent processors can push global consumption past the budget,
        because the check and the deduction happen together under the lock.
        """
        with self._sem:
            self._acquisitions += 1
            if self._level - amount >= -tol:
                self._level -= amount
                if amount > 0.0:
                    self._spent_total += amount
                elif amount < 0.0:
                    self._refunded_total += -amount
                return True
            self._denied += 1
            return False

    def try_spend_batch(self, amounts, tol=_TOL):
        """
        All-or-nothing atomic spend of `sum(amounts)`.  Either the whole batch is
        deducted (returns True) or nothing is (returns False).  Used by the
        commit fast-path; the per-decision `try_spend` is used by the greedy
        fallback.
        """
        total = sum(amounts)
        return self.try_spend(total, tol)

    # ── diagnostics ──────────────────────────────────────────────────────────
    def stats(self):
        """Snapshot of the instrumentation counters (for reporting)."""
        with self._sem:
            self._acquisitions += 1
            return {
                "level":          self._level,
                "spent_total":    self._spent_total,
                "refunded_total": self._refunded_total,
                "acquisitions":   self._acquisitions,
                "denied":         self._denied,
            }

    def __repr__(self):
        return (f"SharedEnergyPool(level={self._level:.4f}, "
                f"spent={self._spent_total:.4f}, refunded={self._refunded_total:.4f}, "
                f"acquisitions={self._acquisitions}, denied={self._denied})")
