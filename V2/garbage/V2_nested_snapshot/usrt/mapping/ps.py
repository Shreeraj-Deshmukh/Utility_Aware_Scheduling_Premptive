"""
PartialSolution (PS) — the data structure for SPS/DPS load-balancing.

A PS holds m processor loads (sorted descending) and the corresponding
job-sets. The 'gap' = loads[0] - loads[-1] drives the SPS combination step.
"""


class PS:
    __slots__ = ('m', 'loads', 'assign', 'gap')

    def __init__(self, m: int):
        self.m      = m
        self.loads  = [0.0] * m
        self.assign = [set() for _ in range(m)]
        self.gap    = 0.0

    @classmethod
    def singleton(cls, m: int, key, val: float) -> 'PS':
        ps = cls(m)
        ps.loads[0] = val
        ps.assign[0].add(key)
        ps.gap = val
        return ps

    def _resort(self):
        p           = sorted(zip(self.loads, self.assign), key=lambda x: -x[0])
        self.loads  = [x[0] for x in p]
        self.assign = [x[1] for x in p]
        self.gap    = self.loads[0] - self.loads[-1]

    def insert(self, key, val: float):
        self.loads[-1] += val
        self.assign[-1].add(key)
        self._resort()

    def combine(self, other: 'PS') -> 'PS':
        m   = self.m
        raw = [
            (self.loads[j] + other.loads[m - 1 - j],
             self.assign[j] | other.assign[m - 1 - j])
            for j in range(m)
        ]
        raw.sort(key=lambda x: -x[0])
        ps        = PS(m)
        ps.loads  = [r[0] for r in raw]
        ps.assign = [r[1] for r in raw]
        ps.gap    = ps.loads[0] - ps.loads[-1]
        return ps
