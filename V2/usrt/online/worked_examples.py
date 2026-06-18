"""
Exact reproduction of the design document's two worked examples.

The DP core (value_function.compose / query / prune) is model-agnostic: it
consumes Action tuples (a_t, a_e, gain, k, z).  Here we feed it the document's
own per-job actions — single processor, single frequency, energy simplified to
equal execution time — and assert that every cell of every published table
V[j][dt][de] is reproduced exactly.  This pins the DP machinery to the paper.

Run directly:  python -m usrt.online.worked_examples
or via:        OnlineSimulator / run.py online  (see verify()).
"""

from .actions        import Action
from .value_function import base_level, compose, query

_S  = "=" * 76
_S2 = "-" * 76


# ── generic helpers ─────────────────────────────────────────────────────────

def build_levels(actions_per_job):
    """
    actions_per_job[p] = list of Action for the job at execution position p
    (position 0 runs first).  Returns V_levels with V_levels[p] covering
    jobs[p:]; V_levels[0] is the entry point (the doc's V[1]).
    """
    N = len(actions_per_job)
    V = [None] * (N + 1)
    V[N] = base_level()
    for p in range(N - 1, -1, -1):
        V[p] = compose(actions_per_job[p], V[p + 1])
    return V


def table(level, dt_max, de_max):
    """Materialise a dense table from a step-function level, for comparison."""
    return [[round(query(level, dt, de).value, 6) for de in range(de_max + 1)]
            for dt in range(dt_max + 1)]


def _cmp(name, got, want):
    ok = (len(got) == len(want) and
          all(len(g) == len(w) for g, w in zip(got, want)) and
          all(abs(a - b) <= 1e-6 for g, w in zip(got, want) for a, b in zip(g, w)))
    print(f"    {name:<10} {'PASS' if ok else 'FAIL'}")
    if not ok:
        for r, (g, w) in enumerate(zip(got, want)):
            if g != w:
                print(f"      dt={r}: got ={g}")
                print(f"             want={w}")
    return ok


def reconstruct(V, dt, de):
    """Follow nxt pointers from V[0] at (dt,de): returns [(pos,k,value), ...]."""
    out = []
    s, e = 0, query(V[0], dt, de)
    while e is not None and s < len(V) - 1:
        out.append((s, e.k, e.value))
        if e.nxt is None:
            break
        e = V[s + 1][e.nxt]
        s += 1
    return out


# ── Example 1 — 3 jobs, non-uniform segments ─────────────────────────────────

def example1():
    # Action(a_t, a_e, gain, k, z); single freq z=0; energy == time == cost.
    J1 = [Action(0, 0, 0.0, 0, 0), Action(2, 2, 6.0, 1, 0), Action(3, 3, 9.0, 2, 0)]
    J2 = [Action(0, 0, 0.0, 0, 0), Action(3, 3, 3.0, 1, 0)]
    J3 = [Action(0, 0, 0.0, 0, 0), Action(1, 1, 2.0, 1, 0), Action(4, 4, 8.0, 2, 0)]
    V = build_levels([J1, J2, J3])

    want_V3 = [[0,0,0,0,0,0,0,0,0],
               [0,2,2,2,2,2,2,2,2],
               [0,2,2,2,2,2,2,2,2],
               [0,2,2,2,2,2,2,2,2],
               [0,2,2,2,8,8,8,8,8],
               [0,2,2,2,8,8,8,8,8]]
    want_V2 = [[0,0,0,0,0,0,0,0,0],
               [0,2,2,2,2,2,2,2,2],
               [0,2,2,2,2,2,2,2,2],
               [0,2,2,3,3,3,3,3,3],
               [0,2,2,3,8,8,8,8,8],
               [0,2,2,3,8,8,8,8,8]]
    want_V1 = [[0,0,0,0,0,0,0,0,0],
               [0,2,2,2,2,2,2,2,2],
               [0,2,6,6,6,6,6,6,6],
               [0,2,6,9,9,9,9,9,9],
               [0,2,6,9,11,11,11,11,11],
               [0,2,6,9,11,11,11,11,11]]

    print("  Example 1 (3 jobs):")
    ok  = _cmp("V[3]", table(V[2], 5, 8), want_V3)
    ok &= _cmp("V[2]", table(V[1], 5, 8), want_V2)
    ok &= _cmp("V[1]", table(V[0], 5, 8), want_V1)
    # Spot-check the doc's headline trace: (dt=4, de=5) -> 11.0
    ok &= abs(query(V[0], 4, 5).value - 11.0) <= 1e-6
    return ok


# ── Example 2 — 4 jobs, verified ─────────────────────────────────────────────

def example2():
    J1 = [Action(0,0,0.0,0,0), Action(1,1,2.0,1,0), Action(3,3,6.0,2,0)]
    J2 = [Action(0,0,0.0,0,0), Action(2,2,8.0,1,0)]
    J3 = [Action(0,0,0.0,0,0), Action(1,1,1.0,1,0), Action(2,2,2.0,2,0), Action(3,3,3.0,3,0)]
    J4 = [Action(0,0,0.0,0,0), Action(3,3,9.0,1,0)]
    V = build_levels([J1, J2, J3, J4])

    want_V4 = [[0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,9,9,9,9,9],
               [0,0,0,9,9,9,9,9],
               [0,0,0,9,9,9,9,9],
               [0,0,0,9,9,9,9,9]]
    want_V3 = [[0,0,0,0,0,0,0,0],
               [0,1,1,1,1,1,1,1],
               [0,1,2,2,2,2,2,2],
               [0,1,2,9,9,9,9,9],
               [0,1,2,9,10,10,10,10],
               [0,1,2,9,10,11,11,11],
               [0,1,2,9,10,11,12,12]]
    want_V2 = [[0,0,0,0,0,0,0,0],
               [0,1,1,1,1,1,1,1],
               [0,1,8,8,8,8,8,8],
               [0,1,8,9,9,9,9,9],
               [0,1,8,9,10,10,10,10],
               [0,1,8,9,10,17,17,17],
               [0,1,8,9,10,17,18,18]]
    want_V1 = [[0,0,0,0,0,0,0,0],
               [0,2,2,2,2,2,2,2],
               [0,2,8,8,8,8,8,8],
               [0,2,8,10,10,10,10,10],
               [0,2,8,10,11,11,11,11],
               [0,2,8,10,11,17,17,17],
               [0,2,8,10,11,17,19,19]]

    print("  Example 2 (4 jobs):")
    ok  = _cmp("V[4]", table(V[3], 6, 7), want_V4)
    ok &= _cmp("V[3]", table(V[2], 6, 7), want_V3)
    ok &= _cmp("V[2]", table(V[1], 6, 7), want_V2)
    ok &= _cmp("V[1]", table(V[0], 6, 7), want_V1)
    # The doc's three verified traces (total utilities).
    for (dt, de, exp) in [(6, 7, 19.0), (5, 5, 17.0), (3, 7, 10.0)]:
        v = query(V[0], dt, de).value
        ok &= abs(v - exp) <= 1e-6
        print(f"    trace (dt={dt}, de={de}) -> {v:.1f}  (doc {exp:.1f})  "
              f"{'OK' if abs(v-exp)<=1e-6 else 'MISMATCH'}")
    return ok


def verify():
    print(f"\n{_S}")
    print("  WORKED-EXAMPLE VERIFICATION  (DP core vs design document)")
    print(_S2)
    ok = example1()
    ok &= example2()
    print(_S2)
    print(f"  RESULT: {'ALL TABLES MATCH THE DOCUMENT' if ok else 'MISMATCH FOUND'}")
    print(_S)
    return ok


if __name__ == "__main__":
    import sys
    sys.exit(0 if verify() else 1)
