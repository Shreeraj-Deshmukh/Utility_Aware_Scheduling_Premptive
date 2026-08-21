"""
USRT test-case generator CLI  (paper Section VII.A; generation only).

Design: SYSTEM parameters are fixed for all test cases; SIMULATION parameters
are swept ONE AT A TIME with every other parameter at its default.  One value
of one parameter = one CONFIGURATION; each configuration gets --sets test cases.

Usage
-----
  python gen_testcases.py <sweep> [options]

  sweeps (simulation parameters):
    n_prc            processors                     {2,4,8,16}
    n_tsk            number of tasks
    u_mand_factor    alpha : U_M = alpha * N_prc
    u_opt_factor     beta  : U_O = beta  * (N_prc - U_M)
    rho              energy budget B = rho * E_full_fmax
    xi               per-task ACET multiplier theta ~ U(xi, 1)   [online]
  extra studies:
    util_grid        vary U_mand and U_opt together (2-D)
    schedulability   push U_mand past capacity (success-rate cliff)
    all              everything above

Options (defaults in brackets):
  --sets N         test cases per configuration [100]
  --seed S         base seed [1000]
  --out DIR        output root [testcases]
  --grid a,b,c     override the swept values for this sweep
  defaults for the NON-swept simulation parameters:
  --n-prc N [2]  --n-tsk N [8]  --alpha A [0.5]  --beta B [0.5]
  --rho R [0.7]  --xi X [0.6]
  system parameters:
  --n-frq N [5]  --max-seg N [4]  --kmax N [3]  --base-per N [10]

Examples
--------
  python gen_testcases.py n_tsk --sets 100
  python gen_testcases.py rho --sets 100 --grid 0.2,0.4,0.6,0.8,1.0
  python gen_testcases.py util_grid --sets 100
  python gen_testcases.py all --sets 100 --out testcases
"""

import sys
import os
import argparse

_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, ValueError):
    pass

from usrt.gen.spec import TestSpec
from usrt.gen import sweeps as S

SWEEPS = list(S.FACTORS) + ["util_grid", "schedulability", "all"]


def _parse_grid(text, factor):
    if not text:
        return None
    vals = [v.strip() for v in text.split(",") if v.strip()]
    if factor in ("n_prc", "n_tsk"):
        return [int(v) for v in vals]
    return [float(v) for v in vals]


def main():
    ap = argparse.ArgumentParser(prog="gen_testcases.py")
    ap.add_argument("sweep", choices=SWEEPS)
    ap.add_argument("--sets", type=int, default=100)
    ap.add_argument("--seed", type=int, default=1000)
    ap.add_argument("--out", default="testcases")
    ap.add_argument("--grid", default=None,
                    help="comma list overriding the swept values")
    # defaults for the non-swept simulation parameters
    ap.add_argument("--n-prc", type=int, default=2)
    ap.add_argument("--n-tsk", type=int, default=8)
    ap.add_argument("--alpha", type=float, default=0.5, help="u_mand_factor")
    ap.add_argument("--beta", type=float, default=0.5, help="u_opt_factor")
    ap.add_argument("--rho", type=float, default=0.7)
    ap.add_argument("--xi", type=float, default=0.6)
    # system parameters
    ap.add_argument("--n-frq", type=int, default=5)
    ap.add_argument("--max-seg", type=int, default=4)
    ap.add_argument("--kmax", type=int, default=3)
    ap.add_argument("--base-per", type=int, default=10)
    args = ap.parse_args()

    base = TestSpec(
        n_prc=args.n_prc, n_tsk=args.n_tsk,
        u_mand_factor=args.alpha, u_opt_factor=args.beta,
        rho=args.rho, xi=args.xi,
        n_frq=args.n_frq, max_optional_seg=args.max_seg,
        k_max=args.kmax, base_per_min=args.base_per, base_per_max=args.base_per,
    )
    kw = dict(n_sets=args.sets, base_seed=args.seed)

    print(f"Generating -> {args.out}")
    print(f"  defaults: n_prc={base.n_prc} n_tsk={base.n_tsk} "
          f"alpha={base.u_mand_factor} beta={base.u_opt_factor} "
          f"rho={base.rho} xi={base.xi} | n_frq={base.n_frq} "
          f"max_seg={base.max_optional_seg} periods=base{args.base_per}*2^0..{args.kmax}")

    if args.sweep == "all":
        S.generate_all(args.out, base, **kw)
    elif args.sweep == "util_grid":
        S.sweep_util_grid(args.out, base, **kw)
    elif args.sweep == "schedulability":
        S.sweep_schedulability(args.out, base,
                               mand_grid=_parse_grid(args.grid, "u_mand_factor"),
                               **kw)
    else:
        S.sweep_factor(args.out, args.sweep,
                       grid=_parse_grid(args.grid, args.sweep),
                       base_spec=base, **kw)


if __name__ == "__main__":
    main()
