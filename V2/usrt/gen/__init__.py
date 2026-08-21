"""
USRT synthetic test-case generation (paper Section VII.A).

Controlled OFAT design: SYSTEM parameters are fixed across all test cases;
SIMULATION parameters are swept one at a time, every other parameter holding
its default.  One value of one parameter = one *configuration*; each
configuration gets `n_sets` (default 100) test cases.

Modules
-------
spec        : TestSpec — system + simulation parameters, with validation.
primitives  : UUniFast, 0.01-unit donation, harmonic period construction,
              random frequency sets, normal segment split, rho energy budget.
generate    : TestSpec + seed -> TaskSet (incl. per-task ACET multiplier theta).
emit        : write one instance as a runnable .py + a manifest row.
sweeps      : OFAT drivers + the (U_mand x U_opt) grid + schedulability cliff.

Symbol map (paper -> code), avoiding the energy-model alpha/beta collision:
    alpha -> u_mand_factor,  beta -> u_opt_factor,  gamma -> gamma,
    delta -> delta,          rho  -> rho,           xi    -> xi
"""

from .spec       import TestSpec, HARMONIC_CHAIN
from .primitives import (uunifast, donate_excess, assign_periods,
                         random_freq_set, split_segments_normal,
                         budget_for_rho, energies_fmax, min_mandatory_energy,
                         worst_fit_feasible)
from .generate   import draw_taskset, TaskSet
from .emit       import emit_testcase, ManifestWriter
from .sweeps     import (sweep_factor, sweep_util_grid, sweep_schedulability,
                         generate_all, FACTORS)

__all__ = [
    "TestSpec", "HARMONIC_CHAIN",
    "uunifast", "donate_excess", "assign_periods", "random_freq_set",
    "split_segments_normal", "budget_for_rho", "energies_fmax",
    "min_mandatory_energy", "worst_fit_feasible",
    "draw_taskset", "TaskSet",
    "emit_testcase", "ManifestWriter",
    "sweep_factor", "sweep_util_grid", "sweep_schedulability",
    "generate_all", "FACTORS",
]
