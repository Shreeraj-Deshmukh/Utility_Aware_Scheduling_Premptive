"""
OFAT sweep drivers (paper Section VII.A structure).

Experiment design
-----------------
  * SYSTEM parameters are fixed across every test case (N_frq, frequency-set
    construction, N_seg range, period construction, utility range).
  * SIMULATION parameters are swept ONE AT A TIME.  A *configuration* is one
    value of one simulation parameter with every other parameter at its
    default; for each configuration we generate `n_sets` (default 100) test
    cases and later aggregate model performance over them.

Simulation parameters (paper VII.A.2):
    n_prc          number of homogeneous processors        {2,4,8,16}
    n_tsk          number of tasks
    u_mand_factor  alpha : U_M = alpha * N_prc
    u_opt_factor   beta  : U_O = beta  * (N_prc - U_M)
    rho            B = rho * E_full_fmax
    xi             per-task ACET multiplier theta ~ U(xi, 1)  [online]

`util_grid` additionally sweeps (u_mand_factor, u_opt_factor) as a 2-D grid,
for the "vary U_mand and U_opt together" study.

Layout:  <out>/<sweep>/set00/<factor>_<value>.py   +  <out>/<sweep>/manifest.csv
"""

import os
from math import ceil
from dataclasses import replace

from .spec       import TestSpec
from .generate   import draw_taskset
from .primitives import budget_for_rho
from .emit       import emit_testcase, ManifestWriter


# ── grids for the simulation parameters ──────────────────────────────────────
GRID_N_PRC   = [2, 4, 8, 16]                        # paper VII.A.2(a)
GRID_N_TSK   = [4, 6, 8, 10, 12]                    # ILP-tractable tier
GRID_N_TSK_BIG = [5, 10, 15, 20, 25, 30, 35, 40, 45]  # heuristic-only tier
GRID_U_MAND  = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
GRID_U_OPT   = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
GRID_RHO     = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
GRID_XI      = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

FACTORS = {
    "n_prc":         GRID_N_PRC,
    "n_tsk":         GRID_N_TSK,
    "u_mand_factor": GRID_U_MAND,
    "u_opt_factor":  GRID_U_OPT,
    "rho":           GRID_RHO,
    "xi":            GRID_XI,
}


def _vlabel(v):
    if isinstance(v, tuple):
        return "-".join(f"{x:g}" for x in v)
    if isinstance(v, float):
        return f"{v:g}"
    return str(v)


def _emit_one(man, out_dir, root, sweep, s, seed, spec_v, ts, factor, value):
    path = os.path.join(root, f"set{s:02d}", f"{factor}_{_vlabel(value)}.py")
    B = budget_for_rho(ts.e_full_fmax, spec_v.rho)
    prov = {
        "sweep": sweep, "set": s, "seed": seed,
        "factor": factor, "value": _vlabel(value),
        "n_prc": spec_v.n_prc, "n_tsk": spec_v.n_tsk, "n_frq": spec_v.n_frq,
        "u_mand_factor": spec_v.u_mand_factor,
        "u_opt_factor": spec_v.u_opt_factor,
        "rho": spec_v.rho, "xi": spec_v.xi,
        "H": ts.H, "J": ts.J, "B": round(B, 6),
    }
    emit_testcase(path, ts, B, prov)
    _ = None
    man.row(
        file=os.path.relpath(path, out_dir), sweep=sweep, set=s,
        factor=factor, value=_vlabel(value),
        n_prc=spec_v.n_prc, n_tsk=spec_v.n_tsk, n_frq=spec_v.n_frq,
        u_mand_factor=spec_v.u_mand_factor, u_opt_factor=spec_v.u_opt_factor,
        rho=spec_v.rho, xi=spec_v.xi,
        U_M=round(ts.U_M, 6), U_O=round(ts.U_O, 6), B=round(B, 6),
        H=ts.H, J=ts.J,
        e_mand_fmax=round(ts.e_mand_fmax, 6),
        e_full_fmax=round(ts.e_full_fmax, 6),
        e_mand_min=round(ts.e_mand_min, 6),
        feasible=int(ts.feasible), donate_ok=int(ts.donate_ok),
        seed=seed, redraws=ts.redraws,
    )
    return ts.donate_ok


def _tasks_for_cores(spec, n_prc):
    """
    Fewest tasks that can carry U_M = alpha * n_prc without every task being
    pinned at the per-task cap gamma.  A task set must grow with the system it
    runs on: with alpha=0.5 and gamma=0.5, a 16-core system needs U_M=8.0,
    which 8 tasks simply cannot hold (8 * 0.5 = 4.0).

    NOTE this is a deliberate, documented co-variation in the n_prc sweep only:
    n_tsk rises with n_prc so each configuration is generatable at all.  The
    realised n_tsk is recorded in the manifest, so the co-variation is visible
    rather than hidden.
    """
    need = ceil(spec.u_mand_factor * n_prc / (0.7 * spec.gamma))
    return max(spec.n_tsk, need)


def sweep_factor(out_dir, factor, grid=None, base_spec=None, n_sets=100,
                 base_seed=1000, verbose=True):
    """
    Sweep ONE simulation parameter; every other parameter keeps its default.
    Generates `n_sets` test cases per configuration (grid value).

    Exception: in the n_prc sweep n_tsk is scaled up as needed (see
    _tasks_for_cores) because U_M grows with the core count.
    """
    base_spec = base_spec or TestSpec()
    grid = grid if grid is not None else FACTORS[factor]
    root = os.path.join(out_dir, factor)
    man = ManifestWriter(os.path.join(root, "manifest.csv"))
    n = 0
    skipped = {}
    dfail = {}
    for s in range(n_sets):
        seed = base_seed + s
        for value in grid:
            spec_v = replace(base_spec, **{factor: value})
            if factor == "n_prc":
                spec_v = replace(spec_v, n_tsk=_tasks_for_cores(base_spec, value))
            try:
                ts = draw_taskset(spec_v, seed)
            except ValueError as e:
                skipped.setdefault(_vlabel(value), str(e))
                continue
            if not _emit_one(man, out_dir, root, factor, s, seed, spec_v, ts,
                             factor, value):
                dfail[_vlabel(value)] = dfail.get(_vlabel(value), 0) + 1
            n += 1
    man.close()
    if verbose:
        print(f"  {factor}: {n_sets} sets x {len(grid)} configs -> {n} testcases")
        for v, why in skipped.items():
            print(f"      SKIPPED {factor}={v}: {why}")
        for v, c in sorted(dfail.items()):
            print(f"      delta-cap UNMET at {factor}={v}: {c} instance(s) "
                  f"(U_O > delta*U_M is arithmetically impossible here)")
    return os.path.join(root, "manifest.csv")


def sweep_util_grid(out_dir, base_spec=None, mand_grid=None, opt_grid=None,
                    n_sets=100, base_seed=1000, verbose=True):
    """
    2-D study: vary U_mand and U_opt together.  Each (alpha, beta) pair is one
    configuration with `n_sets` test cases.
    """
    base_spec = base_spec or TestSpec()
    mand_grid = mand_grid or [0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    opt_grid  = opt_grid  or [0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    root = os.path.join(out_dir, "util_grid")
    man = ManifestWriter(os.path.join(root, "manifest.csv"))
    n = 0
    for s in range(n_sets):
        seed = base_seed + s
        for a in mand_grid:
            for b in opt_grid:
                spec_v = replace(base_spec, u_mand_factor=a, u_opt_factor=b)
                try:
                    ts = draw_taskset(spec_v, seed)
                except ValueError:
                    continue
                _emit_one(man, out_dir, root, "util_grid", s, seed, spec_v, ts,
                          "u_mand_u_opt", (a, b))
                n += 1
    man.close()
    if verbose:
        print(f"  util_grid: {n_sets} sets x {len(mand_grid)*len(opt_grid)} "
              f"configs -> {n} testcases")
    return os.path.join(root, "manifest.csv")


def sweep_schedulability(out_dir, base_spec=None, mand_grid=None, n_sets=100,
                         base_seed=1000, verbose=True):
    """
    Schedulability-cliff study: push U_mand past what the cores can hold and
    keep the instance regardless (guarantee_feasible=False), so success rate
    can be measured as it collapses.
    """
    base_spec = base_spec or TestSpec()
    mand_grid = mand_grid or [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
    root = os.path.join(out_dir, "schedulability")
    man = ManifestWriter(os.path.join(root, "manifest.csv"))
    n = 0
    for s in range(n_sets):
        seed = base_seed + s
        for a in mand_grid:
            spec_v = replace(base_spec, u_mand_factor=a,
                             guarantee_feasible=False)
            try:
                ts = draw_taskset(spec_v, seed)
            except ValueError:
                continue
            _emit_one(man, out_dir, root, "schedulability", s, seed, spec_v, ts,
                      "u_mand_factor", a)
            n += 1
    man.close()
    if verbose:
        print(f"  schedulability: {n_sets} sets x {len(mand_grid)} configs "
              f"-> {n} testcases")
    return os.path.join(root, "manifest.csv")


def generate_all(out_dir, base_spec=None, n_sets=100, base_seed=1000,
                 verbose=True):
    """Generate the full OFAT suite: every simulation parameter + the 2-D grid."""
    base_spec = base_spec or TestSpec()
    if verbose:
        print(f"Generating OFAT suite -> {out_dir}  (n_sets={n_sets})")
        print(f"  defaults: n_prc={base_spec.n_prc} n_tsk={base_spec.n_tsk} "
              f"alpha={base_spec.u_mand_factor} beta={base_spec.u_opt_factor} "
              f"rho={base_spec.rho} xi={base_spec.xi} n_frq={base_spec.n_frq}")
    for factor in FACTORS:
        sweep_factor(out_dir, factor, base_spec=base_spec, n_sets=n_sets,
                     base_seed=base_seed, verbose=verbose)
    sweep_util_grid(out_dir, base_spec, n_sets=n_sets, base_seed=base_seed,
                    verbose=verbose)
    sweep_schedulability(out_dir, base_spec, n_sets=n_sets, base_seed=base_seed,
                         verbose=verbose)
    if verbose:
        print("Done.")
