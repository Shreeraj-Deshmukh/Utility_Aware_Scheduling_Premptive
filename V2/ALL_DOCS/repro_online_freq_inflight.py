"""
Repro for ISSUES.md / ONLINE-FREQ.

Shows that OnlineController.on_completion revises the frequency of a job that
has ALREADY STARTED executing under preemptive EDF, violating paper II:
"once a job starts executing it cannot execute with a different frequency".

Construction
------------
One processor, two tasks:
  T0  p=40  (long period)  -- starts early, then gets preempted
  T1  p=10  (short period) -- preempts T0 at t=10

Under preemptive EDF, T0,j0 starts as soon as T1,j0 finishes, and is preempted
at t=10 when T1,j1 is released.  But the online DP chain is ordered by EDF
(deadline, release, task, job), so T0,j0 (d=40) sits at a chain position AFTER
T1,j1 (d=20).  When T1,j1 completes early, on_completion re-plans every job at
a later chain position -- which includes the already-running T0,j0.

Run
---
    python ALL_DOCS/repro_online_freq_inflight.py          # Z_OFF=1
    Z_OFF=0 python ALL_DOCS/repro_online_freq_inflight.py  # other commitments
    Z_OFF=2 python ALL_DOCS/repro_online_freq_inflight.py

Z_OFF is the offline-committed frequency index.  The violation reproduces for
Z_OFF in {0, 1, 2}; at Z_OFF=3 (= f_max) the DP has no headroom to raise
frequency and no change fires, so the trace is clean.
"""

import io
import os
import sys
import contextlib

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from usrt.online.controller import OnlineController
from usrt.utils  import build_cum
from usrt.models import e_eff_val

Z_OFF = int(os.environ.get("Z_OFF", "1"))

processors = [{'id': 0, 'frequencies': [0.4, 0.6, 0.8, 1.0]}]
tasks = [
    {'id': 0, 'e_m': 6.0, 'e_o_k': [2.0, 2.0], 'p_i': 40, 'u_i': 1.0, 'theta': 1.0},
    {'id': 1, 'e_m': 1.5, 'e_o_k': [1.0],      'p_i': 10, 'u_i': 5.0, 'theta': 0.5},
]
B = 200.0
h = 40

cum, N_seg = build_cum(tasks)
freq_set   = sorted(processors[0]['frequencies'])
periods    = [t['p_i'] for t in tasks]

# Offline commitment: mandatory only, everything on processor 0 at f = Z_OFF.
mapping, seg_k, freq_idx = {}, {}, {}
for i, t in enumerate(tasks):
    for j in range(h // t['p_i']):
        mapping[(i, j)]  = 0
        seg_k[(i, j)]    = 0
        freq_idx[(i, j)] = Z_OFF

# ── preemptive EDF simulation: when does each job actually START? ────────────
jobs = [(i, j, j * periods[i], (j + 1) * periods[i],
         e_eff_val(cum[i][seg_k[(i, j)]], freq_set[freq_idx[(i, j)]]))
        for i in range(len(tasks)) for j in range(h // periods[i])]
rem   = {(i, j): e for (i, j, r, d, e) in jobs}
start = {}
t, step = 0.0, 0.01
while t < h and any(v > 1e-9 for v in rem.values()):
    ready = [(d, (i, j)) for (i, j, r, d, e) in jobs
             if r <= t and rem[(i, j)] > 1e-9]
    if ready:
        _, ij = min(ready)
        start.setdefault(ij, t)
        rem[ij] -= step
    t += step

print(f"Z_OFF = {Z_OFF}  (f = {freq_set[Z_OFF]})\n")
print("job     release  deadline   start(EDF)")
for (i, j, r, d, e) in sorted(jobs, key=lambda x: x[3]):
    print(f"T{i},j{j}   {r:>7.1f} {d:>9.1f} {start.get((i, j), float('nan')):>12.2f}")

# ── fire the online event: T1,j1 completes early ────────────────────────────
ctrl = OnlineController(processors, tasks, B, seg_k, freq_idx, mapping)
print("\nEDF chain order (dp.py:111 -- sorted by deadline, release, task, job):")
for slot in ctrl.dps[0].slots:
    print(f"  pos {slot.pos}: T{slot.i},j{slot.j}  d={ctrl.job_d[(slot.i, slot.j)]}")

event    = (1, 1)
evt_time = start[event]
before   = dict(ctrl.freq_idx)
eff      = e_eff_val(cum[1][0], freq_set[Z_OFF])
with contextlib.redirect_stdout(io.StringIO()):
    ctrl.on_completion(*event, 0.5 * eff, 20.0)   # (dt, de) windfall
after = dict(ctrl.freq_idx)

print(f"\nEvent: T1,j1 completes early at t={evt_time:.2f}")
viol = []
for ij in before:
    if before[ij] != after[ij]:
        started = ij in start and start[ij] < evt_time
        print(f"  freq changed: T{ij[0]},j{ij[1]}  z {before[ij]} -> {after[ij]}"
              f"   started_at={start.get(ij, float('nan')):.2f}"
              f"   ALREADY RUNNING: {started}")
        if started:
            viol.append(ij)

print(f"\nRESULT: {len(viol)} already-started job(s) had frequency revised -> "
      f"{'VIOLATION CONFIRMED' if viol else 'no violation in this trace'}")
sys.exit(1 if viol else 0)
