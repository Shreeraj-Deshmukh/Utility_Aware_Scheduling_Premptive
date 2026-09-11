# garbage/ — retired files

Moved here 2026-09-11. Nothing in this folder is imported, invoked, or read by
any live code path. Kept rather than deleted because several are the provenance
of the current `usrt/` package.

**Do not run anything in here.** See the warning on the heuristics below.

---

## Why each file is here

### Pre-modularization heuristic monoliths — BROKEN, DO NOT RUN

    heuristicv1.py  heuristicv2.py  heuristicv3.py  heuristicv4.py
    heuristic_claude.py

The self-contained originals from which `usrt/` was extracted. Git calls the
2026-05-02 commit that froze them *"last edit b4 modularization"*.

They now return badly wrong answers. On `testcase.py` (B=400):

| | v1 | v2 | v3 | v4 | claude |
|---|---|---|---|---|---|
| these files | 117.46 | **4.83** | 168.27 | **4.83** | **4.83** |
| `usrt/` equivalent | 129.33 | 167.01 | 220.67 | 239.80 | 243.24 |

**Mechanism.** On 2026-08-22 (commit `fd7103b0`) their hard-coded
`ALPHA = 1.0 / BETA = 0.5` was replaced by `from usrt.models import ALPHA, BETA`
— 8 insertions, 2 deletions, no algorithmic change. But their
`phase_aggressive_scaling` takes no `B_BUDGET` argument: it scales down while
energy strictly decreases. That was harmless at `α=1.0, β=0.5`, where f_max is
energy-optimal and the phase is a genuine no-op (as their docstrings still
claim). Under the project's `α=0.15, β=1.0` the optimum moves to `f* ≈ 0.42`, so
the loop drives every job downward, inflates `e_eff = work/f`, saturates the DBF
windows with mandatory work, and leaves Phase 5 nothing to add.

The fix — stop the instant the budget fits — landed only in
`usrt/phases/aggressive.py`, whose docstring documents this exact failure.
These files were correct for four months and were broken by a consistency
change that reached their constants but not the code depending on them.

So: correct as historical artefacts, invalid as solvers. If you ever need to run
one, first pin it back to `ALPHA = 1.0, BETA = 0.5` — its own energy model.

### Superseded ILP drafts

* `Untitled-1.py` — earlier ILP v1 draft, superseded by root `ILP.py`.
  Different API (`solve_usrt_ilp_v1(instance: dict)`), reads `testcase.json`.
  Untouched since 2026-03-29.
* `ilp2.py` — pre-package ILP v2 monolith, superseded by `usrt/solvers/ilp_v2.py`.
* `ilp2gemini.py` — PuLP sketch with `alpha, beta = 1.0, 1.0`, a third energy
  model agreeing with neither the old pair nor the current one. 2026-04-21.

### Orphaned data and debug byproducts

* `testcase.json` — read only by `Untitled-1.py`. Schema
  (`period` / `exec_times` / `utility`) predates the current
  `p_i` / `e_m` / `e_o_k` / `u_i` format.
* `infeasible_v2.ilp`, `infeasible_usrt_v2.ilp` — Gurobi IIS dumps from
  2026-04-18. `usrt/solvers/ilp_v2.py:179` still *writes* `infeasible_v2.ilp` on
  an infeasible standalone solve, so a fresh one may reappear in the root; the
  runner monkeypatches `Model.write` to a no-op, so sweeps never produce them.

### `V2_nested_snapshot/`

Was `V2/V2/` — a snapshot of the tree inside itself, circa 2026-06-14.
Three reasons it is dead:

1. **Unreachable.** Entry points put only the V2 root on `sys.path`, so
   `import usrt` can never resolve into it.
2. **Incomplete.** Its `usrt/` has no `solvers/`, `gen/` or `runner/`, yet its
   own `run.py` dispatches to `usrt.solvers.*` — every solver key would raise
   `ModuleNotFoundError`.
3. **Stale.** Its `usrt/models.py` still carries `ALPHA = 1.0, BETA = 0.5`.

Its `commands.txt` is superseded by `ALL_DOCS/V2_Commands_Reference.html`.

---

## What was verified before moving (2026-09-11)

* No live module imports any of these. `usrt/runner/adapters.py:155`
  imports root `ILP` only — that file stays.
* No name collisions: root `heuristicv4` vs packaged `usrt.solvers.heuristic_v4`
  are different module names, so no import could ever have been shadowed.
  `load_testcase` uses an explicit path, never `sys.path`.
* Every `model` value in every `results.csv` / `results_timed.csv` names a
  packaged solver (`heuristic_v3..v7`, `heuristic_claudeoptimal`, `ilp_v1..v4`,
  `greedy_sps_baseline`). No row here could have produced one.
* No file in `ALL_DOCS/` references any of these names.
