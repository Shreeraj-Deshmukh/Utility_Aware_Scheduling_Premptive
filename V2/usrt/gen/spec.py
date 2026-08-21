"""
TestSpec — the complete, reproducible description of a synthetic instance,
following the paper's Section VII.A "Test Case Generation".

Naming note.  The paper reuses the symbols alpha/beta for BOTH the energy model
(Section II) and the utilisation parameters (Section VII.A).  To keep the code
unambiguous, the utilisation parameters are named explicitly here:

    paper symbol   code name          meaning
    ------------   ----------------   ----------------------------------------
    alpha          u_mand_factor      U_M   = u_mand_factor * N_prc
    beta           u_opt_factor       U_O   = u_opt_factor  * (N_prc - U_M)
    gamma          gamma              max per-task MANDATORY utilisation
    delta          delta              max per-task optional:mandatory ratio
    rho            rho                B     = rho * E_full_fmax
    xi             xi                 per-task ACET multiplier theta in [xi, 1]

ALPHA/BETA in usrt.models remain the ENERGY constants and are never swept.

Parameter classes (paper VII.A):
  * System parameters  — fixed across all test cases (N_frq, frequency-set
    construction, N_seg range, period construction, utility range).
  * Simulation parameters — varied one at a time (N_prc, N_tsk, u_mand_factor,
    u_opt_factor, rho, xi); every other one holds its default.
"""

from dataclasses import dataclass, asdict, field
from typing import Tuple

# Periods are built as base * 2^m, so any draw is harmonic and
# H = max(period used).  With base_per_min = base_per_max = 10 and k_max = 3
# the reachable set is {10, 20, 40, 80} — the locked harmonic chain.
HARMONIC_CHAIN: Tuple[int, ...] = (10, 20, 40, 80, 160, 320, 640)


@dataclass
class TestSpec:
    # ── SYSTEM PARAMETERS (fixed for all test cases) ─────────────────────────
    n_frq: int = 5                 # paper: fixed to 5
    f_min: float = 0.3
    f_max: float = 1.0             # normalised; must appear in every freq set
    f_step: float = 0.05           # grid {f_min, f_min+0.05, ..., f_max}
    max_optional_seg: int = 4      # N_seg drawn from {1..max_optional_seg}
    base_per_min: int = 10         # base period drawn from
    base_per_max: int = 10         #   {base_per_min, +per_step, ..., base_per_max}
    per_step: int = 5
    k_max: int = 3                 # period = base * 2^m, m in {0..k_max}
    min_distinct_periods: int = 3
    u_lo: float = 1.0              # task utility ~ U(u_lo, u_hi)
    u_hi: float = 5.0
    seg_var_frac: float = 0.20     # segment split: normal, sd = 20% of mean

    # ── SIMULATION PARAMETERS (swept one at a time) ──────────────────────────
    n_prc: int = 2                 # paper sweeps 2/4/8/16
    n_tsk: int = 8
    u_mand_factor: float = 0.5     # paper alpha
    u_opt_factor: float = 0.5      # paper beta
    rho: float = 0.7               # paper rho  (B = rho * E_full_fmax)
    xi: float = 0.6                # paper xi   (theta ~ U(xi, 1) per task)

    # ── CONSTRAINT PARAMETERS ────────────────────────────────────────────────
    gamma: float = 0.5             # max per-task mandatory utilisation
    delta: float = 2.0             # max per-task optional:mandatory ratio
    donate_unit: float = 0.01      # donation granularity (paper: 0.01)

    # ── generation control ───────────────────────────────────────────────────
    guarantee_feasible: bool = True
    max_redraws: int = 200
    seed: int = 0

    # ── derived ──────────────────────────────────────────────────────────────
    @property
    def U_M(self) -> float:
        """Total mandatory utilisation = u_mand_factor * N_prc."""
        return self.u_mand_factor * self.n_prc

    @property
    def U_O(self) -> float:
        """Total optional utilisation = u_opt_factor * (N_prc - U_M).

        This is the paper's definition and it is self-limiting: for
        u_opt_factor <= 1 the TOTAL utilisation U_M + U_O never exceeds N_prc,
        so the 'total <= N_prc' cap holds by construction — no extra guard and
        no hand-picked parameter bands are needed."""
        return self.u_opt_factor * (self.n_prc - self.U_M)

    def validate(self):
        """Raise ValueError if the spec cannot produce a legal instance."""
        if self.n_tsk < self.min_distinct_periods:
            raise ValueError(f"n_tsk={self.n_tsk} < min_distinct_periods="
                             f"{self.min_distinct_periods}")
        if self.k_max + 1 < self.min_distinct_periods:
            raise ValueError(f"k_max={self.k_max} gives only {self.k_max+1} "
                             f"period values; need {self.min_distinct_periods}")
        if not (0.0 < self.u_mand_factor < 1.0):
            raise ValueError(f"u_mand_factor must be in (0,1), got {self.u_mand_factor}")
        if self.u_opt_factor < 0.0:
            raise ValueError(f"u_opt_factor must be >= 0, got {self.u_opt_factor}")
        if self.U_M > self.n_tsk * self.gamma + 1e-9:
            raise ValueError(f"U_M={self.U_M:.3f} cannot be split over {self.n_tsk} "
                             f"tasks with per-task cap gamma={self.gamma}")
        if not (0.0 < self.xi <= 1.0):
            raise ValueError(f"xi must be in (0,1], got {self.xi}")
        n_grid = int(round((self.f_max - self.f_min) / self.f_step)) + 1
        if self.n_frq > n_grid:
            raise ValueError(f"n_frq={self.n_frq} exceeds the {n_grid}-level "
                             f"frequency grid")
        return self

    def to_dict(self) -> dict:
        return asdict(self)
