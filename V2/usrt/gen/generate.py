"""
draw_taskset(spec, seed) -> TaskSet   (paper Section VII.A)

Pipeline for one instance:
  1. frequency set   : N_frq distinct levels from the 0.05 grid, f_max present
  2. periods         : base * 2^m  (harmonic; H = max period used)
  3. mandatory util  : U_M = u_mand_factor * N_prc, UUniFast + donation to gamma
  4. optional util   : U_O = u_opt_factor * (N_prc - U_M), UUniFast + donation
                       to the per-task cap delta * u_mand_i
  5. exec times      : e = period * utilisation; optional split across segments
                       with a normal distribution (sd = 20% of mean)
  6. utility         : u_i ~ U(u_lo, u_hi)
  7. theta           : per-task ACET multiplier ~ U(xi, 1)   [paper VII.A.2(f)]

theta is stored PER TASK and emitted into the test-case file, so an online
run's early-completion behaviour is reproducible DATA rather than a simulator
setting.
"""

import random
from dataclasses import dataclass
from typing import List

from ..utils      import lcm_list
from .spec        import TestSpec
from .primitives  import (uunifast, donate_excess, assign_periods,
                          random_freq_set, split_segments_normal,
                          energies_fmax, min_mandatory_energy,
                          worst_fit_feasible)


@dataclass
class TaskSet:
    processors: List[dict]
    tasks: List[dict]
    seed: int
    H: int
    J: int
    U_M: float
    U_O: float
    e_mand_fmax: float
    e_full_fmax: float
    e_mand_min: float
    feasible: bool
    bins: List[float]
    redraws: int
    donate_ok: bool


def _one_draw(spec: TestSpec, seed: int):
    rng = random.Random(seed)

    # 1) frequency set (homogeneous: shared by all processors)
    freqs = random_freq_set(spec.n_frq, spec.f_min, spec.f_max, spec.f_step, rng)
    processors = [{'id': x, 'frequencies': list(freqs)}
                  for x in range(spec.n_prc)]

    # 2) periods
    periods = assign_periods(spec.n_tsk, spec.base_per_min, spec.base_per_max,
                             spec.per_step, spec.k_max, rng,
                             spec.min_distinct_periods)

    # 3) mandatory utilisation: UUniFast then donate down to gamma
    u_mand = uunifast(spec.n_tsk, spec.U_M, rng)
    u_mand, ok_m = donate_excess(u_mand, spec.gamma, spec.donate_unit)

    # 4) optional utilisation: UUniFast over U_O, then donate down to the
    #    per-task cap delta * u_mand_i (paper's per-task mandatory:optional
    #    ratio limit).
    u_opt = uunifast(spec.n_tsk, spec.U_O, rng)
    caps_o = [spec.delta * um for um in u_mand]
    u_opt, ok_o = donate_excess(u_opt, caps_o, spec.donate_unit)

    # 5-7) build the tasks
    tasks = []
    for i in range(spec.n_tsk):
        p = periods[i]
        e_m = u_mand[i] * p
        n_seg = rng.randint(1, spec.max_optional_seg)
        e_o_k = split_segments_normal(u_opt[i] * p, n_seg, rng, spec.seg_var_frac)
        tasks.append({
            'id':    i,
            'e_m':   round(e_m, 6),
            'e_o_k': [round(e, 6) for e in e_o_k],
            'p_i':   int(p),
            'u_i':   round(rng.uniform(spec.u_lo, spec.u_hi), 4),
            'theta': round(rng.uniform(spec.xi, 1.0), 4),   # per-task ACET mult.
        })

    H = lcm_list(periods)
    J = sum(H // p for p in periods)
    n_job = [H // int(t['p_i']) for t in tasks]
    e_mand_fmax, e_full_fmax = energies_fmax(tasks, n_job)
    e_mand_min = min_mandatory_energy(tasks, n_job, freqs)
    feasible, bins = worst_fit_feasible(u_mand, spec.n_prc)

    return TaskSet(
        processors=processors, tasks=tasks, seed=seed, H=H, J=J,
        U_M=sum(u_mand), U_O=sum(u_opt),
        e_mand_fmax=e_mand_fmax, e_full_fmax=e_full_fmax, e_mand_min=e_mand_min,
        feasible=feasible, bins=bins, redraws=0, donate_ok=(ok_m and ok_o),
    )


def draw_taskset(spec: TestSpec, seed: int) -> TaskSet:
    """
    Draw one instance.  With spec.guarantee_feasible, redraw under perturbed
    seeds until the mandatory part packs onto n_prc cores (or max_redraws is
    exhausted, in which case the last draw is returned with feasible=False).
    With guarantee_feasible=False (schedulability-cliff studies) the first draw
    is kept regardless.
    """
    spec.validate()
    ts = _one_draw(spec, seed)
    if not spec.guarantee_feasible:
        return ts
    tries = 0
    while not ts.feasible and tries < spec.max_redraws:
        tries += 1
        ts = _one_draw(spec, seed + 7919 * tries)
    ts.redraws = tries
    return ts
