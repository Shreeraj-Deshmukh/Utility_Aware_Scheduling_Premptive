"""
Exact breakpoint value function for the online slack-distribution DP.

The paper's table V[j][dt][de] is, for fixed j, a step function over the two
resource axes: piecewise-constant and non-decreasing in both dt and de, with
jumps only at the (finitely many) reachable cumulative cost vectors.  Rather
than materialise a dense grid (which would force quantisation of float costs),
we store the function exactly as its Pareto frontier of "requirement" tuples.

Representation
--------------
A value function level is a list of `Entry`:

    Entry(req_t, req_e, value, k, z, a_t, a_e, nxt)

meaning: "if at least req_t time slack and req_e energy slack are available at
this job, then `value` additional utility is achievable from here on, by giving
THIS job target segment k at frequency index z (incurring signed deltas a_t,
a_e) and continuing with downstream entry index `nxt`."

We keep only Pareto-non-dominated entries.  Entry B dominates entry A iff

    req_t_B <= req_t_A  AND  req_e_B <= req_e_A  AND  value_B >= value_A

(with a strict improvement somewhere).  The (0, 0, 0) "do nothing" entry is
always present, so a query never fails.

Recurrence (built right to left), with downstream level D = V[j+1]:

    V[j] = prune( { (max(0, a_t + d.req_t), max(0, a_e + d.req_e),
                     gain + d.value, k, z, a_t, a_e, index_of(d))
                    : action(a_t, a_e, gain, k, z) in A_j, d in D } )

Negative a_t / a_e (frequency raised / lowered) reduce the upstream
requirement — this is exactly how conversion Options 4 / 3 enter the table.
The clamp at 0 is correct because D already encodes the *minimal* requirement
for each value level, so any surplus freed by this job beyond D's need is
genuinely unusable by this sub-chain.
"""

_TOL = 1e-9


class Entry:
    """One Pareto point of a value-function level. See module docstring."""
    __slots__ = ("req_t", "req_e", "value", "k", "z", "a_t", "a_e", "nxt")

    def __init__(self, req_t, req_e, value, k=None, z=None,
                 a_t=0.0, a_e=0.0, nxt=None):
        self.req_t = req_t      # minimum time slack needed at this job
        self.req_e = req_e      # minimum energy slack needed at this job
        self.value = value      # additional utility achievable from here on
        self.k     = k          # this job's chosen target segment count
        self.z     = z          # this job's chosen target frequency index
        self.a_t   = a_t        # signed time delta of this job's action
        self.a_e   = a_e        # signed energy delta of this job's action
        self.nxt   = nxt        # index into the downstream level (or None)

    def __repr__(self):
        return (f"Entry(req_t={self.req_t:.4f}, req_e={self.req_e:.4f}, "
                f"value={self.value:.4f}, k={self.k}, z={self.z})")


def prune(entries, tol=_TOL):
    """
    Return the Pareto-non-dominated subset of `entries`.

    Sorted by (req_t asc, req_e asc, value desc) so duplicates / dominated
    points are easy to drop.  O(n^2) — fine for the small per-job frontiers
    that arise here (segments x frequencies, then Pareto-bounded).
    """
    if not entries:
        return []

    ordered = sorted(entries, key=lambda e: (e.req_t, e.req_e, -e.value))
    kept = []
    for e in ordered:
        dominated = False
        for k in kept:
            if (k.req_t <= e.req_t + tol and
                k.req_e <= e.req_e + tol and
                k.value >= e.value - tol):
                dominated = True
                break
        if not dominated:
            # Drop any previously-kept entry that THIS one now dominates
            kept = [k for k in kept
                    if not (e.req_t <= k.req_t + tol and
                            e.req_e <= k.req_e + tol and
                            e.value >= k.value - tol)]
            kept.append(e)
    return kept


def compose(actions, downstream, tol=_TOL):
    """
    Build one value-function level from this job's `actions` and the already
    -pruned `downstream` level (a list of Entry, index-stable).

    `actions` is an iterable of Action tuples (a_t, a_e, gain, k, z); see
    actions.py.  Returns a pruned list of Entry whose `nxt` indexes into
    `downstream`.
    """
    cand = []
    for (a_t, a_e, gain, k, z) in actions:
        for d_idx, d in enumerate(downstream):
            req_t = a_t + d.req_t
            req_e = a_e + d.req_e
            if req_t < 0.0:
                req_t = 0.0
            if req_e < 0.0:
                req_e = 0.0
            cand.append(Entry(req_t, req_e, gain + d.value,
                              k=k, z=z, a_t=a_t, a_e=a_e, nxt=d_idx))
    return prune(cand, tol)


def query(level, dt, de, tol=_TOL):
    """
    Best achievable entry given `dt` time slack and `de` energy slack.

    Among entries with req_t <= dt and req_e <= de, return the one with the
    greatest value (ties broken toward the smallest requirement).  `level`
    always contains the (0,0,0) entry, so the result is never None.
    """
    best = None
    for e in level:
        if e.req_t <= dt + tol and e.req_e <= de + tol:
            if (best is None or
                e.value > best.value + tol or
                (abs(e.value - best.value) <= tol and
                 (e.req_t + e.req_e) < (best.req_t + best.req_e) - tol)):
                best = e
    return best


def base_level():
    """Terminal level V[N] (no jobs left): a single zero entry."""
    return [Entry(0.0, 0.0, 0.0, k=None, z=None, a_t=0.0, a_e=0.0, nxt=None)]
