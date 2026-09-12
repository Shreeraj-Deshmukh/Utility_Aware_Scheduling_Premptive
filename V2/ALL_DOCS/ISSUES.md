# USRT — Issue Register

Working file. We **append** findings here as they are confirmed; we do **not** fix them one at a
time. Once the register is populated we read it whole and derive a single sequenced plan, because
several issues share a root and fixing them separately produces layered patches that fight.

- Discussion happens in chat. This file holds only what survived scrutiny.
- Either of us edits it.
- **Readable snapshot:** `ALL_DOCS/usrt_code_review_report.html` renders this register whole.
  Regenerate it when this file drifts. `audit_issues_22Aug.html` and `15Aug_Online_Audit.html`
  are **retired** — folded in here and banner-marked at source.
- `Confidence` is not decoration — an entry marked *re-verify* must be reconfirmed before it is
  allowed to influence the plan.

---

## Entry template
```
### <ID> — <one-line claim>
| field | value |
|---|---|
| Status      | open / needs-decision / ready / fixed |
| Confidence  | verified live <date> / from audit, re-verify / suspected |
| Layer       | A invariant · B behaviour · C contract · — none |
| Costs us    | what it actually breaks |
| Location    | file:line |
| Shares root | <IDs> — same fix, must land together |
| Blocks      | <IDs> — must land before those |
| Blocked by  | <IDs> |

**Mechanism.** What actually happens, in terms of the model. Not "this looks wrong."

**Blast radius.** Every module that reads the state this touches.

**Evidence.** The measurement.

**Fix options.** 1) … 2) … with the trade-off stated.

**Open question.** What needs a decision rather than a keystroke.
```

**Layer** decides how we verify a fix, so it is not optional:
**A** = violates a rule of the problem (a runtime assertion catches it) ·
**B** = valid output, wrong quality (only a before/after diff catches it) ·
**C** = two parts of the codebase disagree (a contract test catches it) ·
**—** = feature/environment/docs, no test applies.

---

# Register

### B2 — Quantum SPS capacity is never released, so most jobs bypass SPS
| field | value |
|---|---|
| Status      | **fixed 2026-09-05** |
| Confidence  | verified live 2026-09-04; fix measured 2026-09-05 over 900 instances |
| Layer       | **B** — output stays legal, quality is wrong |
| Cost us     | every SPS-vs-alternative result published before 2026-09-05 |
| Location    | `usrt/mapping/quantum.py:81, 117, 151, 164` (was `:39, 79, 84, 117, 124, 156`) |
| Landed with | UTIL-METRIC — same change, as the register required |

**What it was.** `proc_util` was initialised once and only accumulated into, adding `e_m_i/p_i`
once per **job**. Utilisation is a *rate* — a task using 24.5% of a core uses it at every instant,
permanently — so charging that rate again on every job release compares a quantity that grows with
time against a capacity that does not. The comparison was therefore guaranteed to fail eventually;
processor count only changed *when*. Once it passed `m`, every later quantum took the
`MAND_OVERUTIL` break, committed nothing, and its jobs fell through to the min-util round-robin
without ever reaching DPS/SPS.

**The fix — JOB-SHARE metric.** One job of task `i` occupies `e_m_i / h` of a processor over the
hyper-period. Summed over that task's `h/p_i` jobs this is exactly `e_m_i/p_i`, and summed over
everything exactly `U_M`. So `proc_util[x]` becomes literally *(mandatory work placed on x) / h* —
a true per-processor utilisation, computed incrementally, correct however a task's jobs are split
across cores. Four lines, no new state.

**Why not the other candidates.** A *task-set* variant (charge each distinct task once per
processor) was built and measured first. It is bounded, unlike the original, but **~50% of tasks
are split across processors** and it charges the whole task to each, so `sum(proc_util) ≈ 1.5·U_M`.
That inflation trips the gate at roughly two-thirds of real capacity. Measured: fallback only fell
to 23%, and `heuristic_v5b` **regressed −0.54% overall, −18.5% at α=0.8**. Rejected. Options (1)
event-based release and (3) gate-on-DBF were never needed — job-share is exact, so the proxy
question the old entry posed ("what should `proc_util` *mean*?") is answered rather than traded off.

**Blast radius — two more copies of the same bug, both fixed in the same change.**
* `repair.py:92` — repair-target choice ranked processors by the same inflated metric.
* `packers.py:40,116` — **`ffd_mapping` and `bfd_mapping` test `load[x] + u <= 1.0` while
  accumulating `e_m/p_i` per job.** This is B2 verbatim, inside v7's own multi-start candidates —
  the ones previously described as "immune to B2 because they bypass SPS". They bypass
  `quantum.py`, not the defect. Fixing them is where most of v7's gain came from (+0.36% → +0.79%).
* 9 display sites across `heuristic_v1/v2/v3/v4/v5a/v5b/claudeoptimal` — see UTIL-METRIC.
* `ilp_v2.py` consumes the mapping and improved with it; no code change needed.

**Evidence — OFAT on `u_mand_factor` (paper α), 9 points × 100 seeds = 900 instances, `n_prc=2,
n_tsk=8, n_frq=5, u_opt=0.5, rho=0.7, xi=0.6, H=80` all held fixed. Identical instances before and
after; results in `tc_b2/u_mand_factor/results_{before,after_taskset,after_jobshare,after_full}.csv`.**

Fallback-mapped jobs (never reach SPS), 25 seeds per α:

| α | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | total |
|---|---|---|---|---|---|---|---|---|---|---|
| before | 0% | 1.5% | 11.5% | 26.2% | 39.2% | 49.7% | 59.4% | 64.6% | 69.7% | **35.8%** |
| task-set | 0% | 0% | 0% | 0.4% | 12.1% | 24.0% | 45.0% | 56.1% | 69.0% | 23.0% |
| **job-share** | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | **0.0%** |

Final change set vs original:

| model | Δ utility (paired) | feasible /900 | mean runtime |
|---|---|---|---|
| `ilp_v2` | **+0.20%** | 731 → **741** | 0.472 → **0.345** s (−27%) |
| `heuristic_v5b` | **+0.38%** | 727 → **737** | 0.027 → **0.022** s (−17%) |
| `heuristic_v7` | **+0.79%** (204 better / 120 worse) | 753 → **765** | 0.266 → 0.285 s |

α ≤ 0.6 is 100/100 feasible in every run; α = 0.9 is 0/100 in every run; the feasibility gains are
all at α = 0.7–0.8. `sum(proc_util) == U_M` exactly at every α, and `maxUtil` never exceeds 1.0.

**Still open, deliberately.** The DPS/SPS *balance* metric at `quantum.py:101` and the deferral
sort keys at `:63, :89` remain on `e_m/p_i`. Those **rank** jobs; they do not gate capacity, so
they are a separate question with its own experiment. The file now carries two metrics side by
side — a deliberate choice, not an oversight.

---

### UTIL-METRIC — "utilisation" is summed over jobs, not tasks
| field | value |
|---|---|
| Status      | **fixed 2026-09-05** |
| Confidence  | verified live 2026-09-04; fixed and measured 2026-09-05 |
| Layer       | **B** (+ display) |
| Cost us     | every `← OVER 1.0` warning in the logs was spurious |
| Location    | 9 display sites in `heuristic_v1/v2/v3/v4/v5a/v5b/claudeoptimal` · `repair.py:92` |
| Landed with | B2 — same change, as this entry required |

**Mechanism.** `Σ_jobs e_m_i/p_i = Σ_i (H/p_i)·(e_m_i/p_i)` — inflated by `H/p_i`. Utilisation is
a per-*task* quantity being summed per *job*.

**Evidence.** `testcase.py` printed `P0: util=3.2434 ← OVER 1.0` for a mapping whose true
utilisation is ~0.67 and which DBF confirms feasible.

**Fix.** All sites now use the job-share metric `e_m_i / h`, identical to B2's, so the diagnostic
and the mapper agree by construction. The display sites are pure printout — no decision reads them
— so they carried zero behavioural risk; `repair.py:92` does steer the repair target and was
validated in the same 900-instance run (byte-identical results for `ilp_v2` and `heuristic_v5b`,
since repair almost never fires once fallback is 0%).

**Note.** The original entry proposed `Σ over distinct tasks`. That is the *task-set* variant, and
measuring it showed it double-counts tasks split across processors — see B2. `e_m/h` is used
instead, and is exact.

---

### REPAIR-PARTIAL — a PARTIAL mapping is never surfaced to unguarded callers
| field | value |
|---|---|
| Status      | **fixed 2026-09-13.** Three parts, all closed: the repair algorithm itself (2026-09-12), the stdout path via `output.verify_schedule` (2026-09-13), and the programmatic path via the widened `run()` contract + `adapters._schedule_feasible` (2026-09-13) |
| Confidence  | verified live 2026-09-04; algorithm root-caused and fixed 2026-09-12, validated against brute force; severity re-examined 2026-09-12 after an initial (wrong) downgrade to Medium |
| Layer       | **A** — a returned schedule could violate C2, unconditionally, on any unguarded call |
| Costs us    | *(historical)* a deadline-missing schedule could print as `SOLUTION (FINAL)` on a **direct, unguarded** solver call -- `python run.py`, or any direct `mod.run(...)` -- which is the primary single-instance workflow, not an obscure path. Residual rate is uneven, not uniformly rare: **0% at u_mand_factor 0.70-0.85, but 12.3% at 0.95** (28/227) -- the aggregate 3.8% hides this. |
| Location    | `usrt/mapping/repair.py` (rewritten) · consumed at `quantum.py:187-192` · guards in `usrt/output.py` and `usrt/runner/adapters.py` |
| Blocked by  | ~~B2~~ — landed 2026-09-05 |

**What was actually wrong — deeper than "nobody checks."** Investigating this to plan a fix
uncovered that `repair_mapping`'s own algorithm was far more broken than "can return PARTIAL": it
**oscillates**. It always moved the single biggest offender in the single worst-violated window to
whichever processor had the lowest *global* utilisation, unconditionally, with no memory of past
moves. Traced live: moving a job to fix window A can make it the single biggest job in window B
(e.g. one spanning the whole hyper-period); the next iteration moves it straight back, recreating
A — a 2-cycle that burns all 100 iterations and returns the **original, unmodified, still-
infeasible** mapping. Brute force confirmed a feasible mapping existed in **100% of a 26-instance
sample** (u_mand_factor 0.6–0.9, n_prc=2) that the old algorithm never found.

**Fix — two-tier best-improvement search against a monotone objective.**
Track `total_excess` = Σ(demand − cap) over every violated window (0 iff feasible).
- **Tier 1** — try single-job moves (worst windows → biggest offenders → every other
  processor as target); commit only if it **strictly decreases** total_excess. Since this
  quantity is bounded, non-negative, and only ever strictly decreases on an accepted move, no
  mapping can repeat — the oscillation is now structurally impossible.
- **Tier 2** — pairwise swaps, tried only when tier 1 finds nothing. Needed because a genuine
  fix can require two coordinated moves where the first, evaluated alone, makes total_excess
  *worse* (traced case: 2.09 → 14.83 → 0 across two single moves) — tier 1 can never take that
  first step since it isn't monotone. The identical reassignment applied as one **simultaneous**
  swap takes total_excess straight from 2.09 to 0. Found and closed the only regression this
  produced against the old algorithm (see Evidence).

If neither tier improves, that's a genuine local optimum for this move set — stop immediately
(rather than burning `max_iters` on moves that can't help) and report PARTIAL honestly.

**Evidence.** OFAT-style sweep, `n_tsk=8`, `n_prc ∈ {2,3,4}`, 80 seeds/point, brute-force
existence check on every case where the new algorithm still fails (task-level partition search,
`n_prc^n_tsk ≤ 2^18` — always satisfied here, so every residual case was actually checked, not
skipped):

| u_mand_factor | needed repair | OLD fixed | NEW fixed |
|---|---|---|---|
| 0.70 | 76 | 71 (93.4%) | **76 (100.0%)** |
| 0.80 | 141 | 87 (61.7%) | **141 (100.0%)** |
| 0.85 | 168 | 70 (41.7%) | **168 (100.0%)** |
| 0.90 | 208 | 29 (13.9%) | **205 (98.6%)** |
| 0.95 | 227 | 9 (4.0%) | **199 (87.7%)** |
| **total** | **820** | **266 (32.4%)** | **789 (96.2%)** |

Per-instance comparison (not just aggregate counts): **0 regressions** — every instance OLD fixed,
NEW also fixes (one regression was found mid-development, root-caused to the tier-1-only version,
and closed by adding tier 2). Of the 31 instances still PARTIAL under NEW, brute force confirms
**all 31 have a feasible mapping the two-tier search still doesn't find** (0 confirmed truly
infeasible) — a real limit of a 2-move local search, concentrated entirely at u_mand_factor ≥ 0.9.
Cost: 2.70 ms/call average, 49.7 ms worst case over the 820 repair invocations — negligible next to
a single ILP solve (≈300–600 ms).

**End-to-end confirmed**, not just at the mapping level: an instance whose raw SPS mapping needed
repair, run through `run_model('heuristic_v5b', ...)` with a generous budget — before the fix this
would report `status=infeasible, model_feasible=0` (the guard correctly catching the old
algorithm's failure); after the fix, `_mandatory_feasible` returns `True` and the run reports
`status=solved, model_feasible=1, utility=21.36`.

**Severity re-examined 2026-09-12.** This entry was initially downgraded to Medium on the strength
of the algorithm fix. That was wrong, and worth recording why: the fix improved a *different*
sub-issue (repair's own success rate) from the one this entry is actually about (whether a failure
is ever surfaced to the caller). Layer is still **A**, the exposure path (`python run.py`, direct
`mod.run(...)`) is still the primary documented single-instance workflow, and the residual rate
concentrates exactly where researchers probe the schedulability boundary (12.3% at
u_mand_factor=0.95) rather than being uniformly rare. Averaging that against the 0% at moderate
utilisation to get "3.8% overall" is the same kind of aggregate-hides-the-tail framing this project
has been burned by before (B2 sitting unnoticed for two weeks). Reverted to **High**.

**What this does and does not close.** The algorithm bug (repair oscillating, 32.4% success) is
fixed and validated -- that part is closed. What's still open, unchanged in kind, is the
*detection* gap: `quantum.py` still returns the mapping unconditionally on PARTIAL, and only
`adapters._mandatory_feasible` (runner-driven paths) gates on it.

**Detection gap — half closed 2026-09-13.** `usrt/output.py` now has `verify_schedule()`, called
from both `print_schedule` and `print_schedule_with_ls`. Every solver routes its final schedule
through those, so this is the one choke point that covers all of them, with **zero call-site
changes** — the 15-signature change floated earlier turned out to be unnecessary. It re-checks the
*final* schedule (strictly stronger than checking the initial mapping: it also catches any phase
that commits an infeasible move) against C2 and C3, and prints an unmissable
`*** INFEASIBLE SCHEDULE - DO NOT USE THESE NUMBERS ***` banner naming which constraint broke.

*Verified 2026-09-13.* True positive: a deliberately unschedulable instance (4 tasks × 0.8 util on
2 cores) still prints `SOLUTION (FINAL)` — and now the banner fires immediately after it. No false
alarms: 160 runs across v5b/v7 × u_mand 0.5–0.95 × n_prc 2/4, **0 cases** where the banner fired on
a schedule the adapter accepted, full agreement with the adapter verdict on all 160.

**Published results were never affected — confirmed, not assumed.** The concern was that
`_mandatory_feasible` guards the *raw* SPS mapping while solvers actually run on a *refined* one
(v5b adds `refine_mapping_2b`, v6 adds 1b'+1c, v7 adds 1M+1R), so a refinement that broke
feasibility would slip through. Tested directly by capturing the mapping each solver actually
commits (intercepting `print_schedule`) and re-checking the committed schedule: **480 runs across
v5a/v5b/v6/v7, 191 reported feasible, 0 false positives**, plus an earlier 200-run v5b pass
(100 reported feasible, 0 false positives). The refinement stages do preserve DBF feasibility —
each guards its own swaps. So every number in `tc_b2/` and the sweep CSVs stands.

**Programmatic half — closed 2026-09-13 by widening the `run()` contract.** The stdout banner does
nothing for the runner, because `adapters.run_heuristic` wraps `mod.run(...)` in `_suppress()` and
throws the output away. And the adapter could not do the check itself: it had the schedule but not
the **mapping**, and a schedule is only meaningful relative to the assignment it was built on. So
the blocker was a missing return value, not a missing check.

Every heuristic `run()` now returns `(seg_k, freq_idx, utility, energy, mapping)` — 15 return
statements across 9 solvers, 2 unpack sites in `adapters`. `adapters._schedule_feasible` then
DBF-checks the schedule the solver actually **committed**, and a failure produces
`status=infeasible, model_feasible=0, error="C2: committed schedule misses a deadline"`.

This is strictly stronger than what was there. `_mandatory_feasible` (still kept, as a cheap
pre-filter that short-circuits before the solver runs) is blind twice over: it re-derives the *raw*
SPS mapping, which v5a/v5b/v6/v7 then refine or replace, and it never sees the seg_k/freq_idx that
phases 2-6b commit on top. The new check sees the end state.

*Verified 2026-09-13, both directions.*

- **It does not change any result.** 6300 runs — v3, v4, v5a, v5b, v6, v7 and
  `greedy_sps_baseline`, each over all 900 instances of `tc_b2/u_mand_factor` — and the new guard
  **fired 0 times**. Since unpacking `mapping` changes no arithmetic and the guard is the only new
  branch, every number already published is unchanged by this commit. (v5a/v5b were run twice, in
  separate processes, and agreed exactly: 739 and 740 solved.)
- **It is not vacuous.** Positive control: sabotage `refine_mapping_2b` to return a
  pile-everything-onto-P0 mapping — exactly the failure mode the guard exists for, a refinement
  committing something the pre-filter never saw — restricted to the 440 instances where
  `U_M > 1.0` makes P0-only *provably* miss deadlines. **0 of 440 scored as a success.** 400 were
  already caught by the pre-existing energy check (a crowded P0 blocks frequency scaling, so it
  busts C3 too); the remaining **40 were caught only by the new C2 guard** and would have been
  scored as successes before this change.

**Residual, by design.** `quantum_sps_mapping` still returns the mapping unconditionally on
PARTIAL and discards repair's flag; `run()` hands back the mapping but not a boolean verdict. A
*new* consumer therefore still has to call `verify_schedule` or `_schedule_feasible` itself rather
than being forced to. That is now a one-line opt-in with the data in hand, not the impossible
position it was before, and both consumers that exist (stdout, runner) are guarded. Left as-is
rather than threading a flag through as well: two verdict channels that can disagree is worse than
one piece of data both callers check.

---

### RUN-FEAS — runner error path clobbers the manifest's `feasible` column
| field | value |
|---|---|
| Status      | **fixed 2026-09-12** |
| Confidence  | verified live 2026-09-04; fix verified by reproducer 2026-09-12 |
| Layer       | **C** — contract |
| Costs us    | corrupts the generator's instance-level flag in `results.csv` |
| Location    | `usrt/runner/runner.py:94` |
| Blocks      | — |
| Blocked by  | — |

**Mechanism.** The outer `except` writes `feasible=0`; the schema is `model_feasible`
(`runner.py:19`, `adapters.py:8-12`). The row is merged as `{**row, **metrics}` and the manifest
owns `feasible` (`emit.py:19`), so a `load_testcase` failure overwrites it. Exactly what the
module docstring two lines above warns against. `run_model`'s own handler is correct.

**Note.** `audit_issues_22Aug.html` lists this collision as *fixed and deliberately omitted* — the
fix landed in `adapters.py` and this path was missed. Isolated; no coupling.

**Fix (2026-09-12).** One line at `runner.py:94`: `feasible=0` → `model_feasible=0`.

**Verification.** Built a two-row manifest — one loadable instance, one file that raises on import —
and ran it through `run_manifest`:

| file | `feasible` (manifest) | `model_feasible` | status |
|---|---|---|---|
| good.py | 1 | 1 | solved |
| bad.py | **1** (preserved) | **0** | error |

Before the fix the `bad.py` row would have carried `feasible=0` (the generator's flag clobbered)
and a blank `model_feasible`.

**No stored data was corrupted.** Scanned all 44 `results*.csv` in the tree — 115,750 rows,
**0 with `status=error`** — so the path never actually fired in any saved sweep. Nothing to
regenerate.

---

### SWAP-BREAK — Phase 6 aborts the whole search on one failed candidate
| field | value |
|---|---|
| Status      | open |
| Confidence  | verified live 2026-09-04 (present; did not fire in 13 runs) |
| Layer       | **A** *and* **B** — see below |
| Costs us    | silently truncates Phase 6; magnitude unmeasured |
| Location    | `usrt/phases/swap.py:126` |
| Blocked by  | — |

**Mechanism.** When the best candidate fails `check_all_timing`, the else-branch executes
`break`, ending the local search and discarding every remaining improving candidate from the same
scan.

**The deeper point** (June review B5): `min_slack_for_job` evaluates exactly the windows affected
by adding time to the receiver, so **the revert path should be unreachable**. If it ever fires,
that signals a state-consistency bug elsewhere — which makes silently breaking doubly wrong.

**Fix options.** Blacklist the pair and `continue` — *and* assert/log loudly on the "unreachable"
revert rather than swallowing it. Fixing only the `break` hides a real bug.

---

### FREQ-SET — `processors[0]['frequencies']` assumed for all processors, in 18 places
| field | value |
|---|---|
| Status      | open (latent) |
| Confidence  | verified live 2026-09-04 |
| Layer       | **C** |
| Costs us    | nothing today; blocks paper §VII.A fidelity |
| Location    | 18 sites (re-counted 2026-09-12; grew with `ilp_v3`/`ilp_v4`) incl. `heuristic_v{1..7}.py`, `ilp_v2/v3/v4.py`, `adapters.py`, `online/controller.py:59`, `ILP.py:96` |

**Mechanism.** Paper §VII.A(i) generates a **distinct** frequency set per processor and forces
f_max=1.0 on only *some*. The code reads `processors[0]` everywhere. Latent only because
`generate.py:55` currently gives every processor the same list.

**Related.** `repair.py:44` and `refine_mapping.py:75` use raw `e_m` as demand — i.e. they assume
`max(frequencies) == 1.0`. A set topping out at 0.9 makes both DBF checks optimistic.

---

### ONLINE-DEMO — the online entry point does not run the pipeline it claims
| field | value |
|---|---|
| Status      | open |
| Confidence  | verified live 2026-09-04 |
| Layer       | **C** |
| Costs us    | latent divergence at tight budgets, exactly where online should be reported |
| Location    | `usrt/solvers/online_demo.py:31-61` |

**Mechanism.** `offline_schedule()` calls `quantum_sps_mapping → refine_mapping_2b → aggressive →
greedy → swap` **directly** instead of `heuristic_v5b.run()`, so it has neither the Phase 3
`min_possible_energy` gate nor Phase 6b. Harmless at B=400 where both are no-ops; divergent at
tight ρ.

---

### IXB-ROUTING — paper §IX.B opportunity-cost energy routing not implemented
| field | value |
|---|---|
| Status      | open (feature) |
| Confidence  | verified absent 2026-09-04 |
| Layer       | — |
| Location    | would replace/extend `usrt/online/density.py:45` |

**Mechanism.** Implemented instead: Approach C proportional density split. It **always** splits,
so with two equal-density processors each is capped at half the pool *even in surplus*
(`controller.py:208` `de_budget = min(pool_now, caps[x])`). §IX.B's surplus branch
(`opp-cost = 0` when `E_rem ≥ D`) degenerates to plain greedy and fixes exactly this.

**Evidence.** Already recorded as a weakness in `15Aug_Online_Audit.html` §5, "proportional
density arbitration can under-serve immediate high-value work".

**Note.** The DP tables already contain the Δ values §IX.B needs — this is a change to
`density.py` plus one call site, not a redesign.

---

### NO-TESTS — no test suite exists
| field | value |
|---|---|
| Status      | needs-decision |
| Confidence  | verified live 2026-09-04 |
| Layer       | — |
| Costs us    | no way to know a fix broke something; blocks safe work on B2 |

**Mechanism.** Zero test files, no `conftest.py`, no pytest config. The only executable
self-check in the project is `worked_examples.verify()` (online DP core). `pytest` is not
installed; `unittest` is. Measured loop cost: **39 ms/instance → 3.5 s per solver over
`dry_run_tc`'s 90 instances.**

**Open question.** Golden baseline only (~20 min, what B2 actually needs), or golden + invariant
suite (~1 h, pays off across every later fix)?

---

### ONLINE-FREQ — online revises the frequency of a job that has already started
| field | value |
|---|---|
| Status      | open |
| Confidence  | verified live 2026-09-12 — repro, violation in 3 of 4 configurations |
| Layer       | **A** — violates a rule of the problem |
| Costs us    | every online result where a preempted job's frequency was revised: the schedule is inadmissible under §II, and both its reported energy and its DBF check are computed at the wrong frequency |
| Location    | `usrt/online/controller.py:273, 299, 314` (the writes); root cause `usrt/online/dp.py:111` with `controller.py:191, 211` |
| Shares root | — (see **Note** on the simulator's event order) |

**Mechanism.** Paper §II: *"once a job starts executing it cannot execute with a different
frequency"*. The online DP chain is ordered by EDF — `(deadline, release, task, job)` at
`dp.py:111` — and `on_completion` re-plans every job at chain position `> c`
(`controller.py:191, 211`), writing a new `freq_idx` at `:273` (batch fast path), `:299` (pure
frequency change) and `:314` (segment addition).

Under **non**-preemptive execution "later in the chain" implies "not yet started", and those
writes would be safe. Under preemptive EDF it does not: a long-period job can start, be preempted
by a shorter-period release, and still sit *downstream* of that job in deadline order — so it is
eligible for revision while already in flight.

Raising `k` on such a job is sound: the added optional work is appended at the tail and provably
has not run. **Only the frequency write is unsound.**

**Blast radius.** Everything that reads `freq_idx` after an online event:
- `models.total_energy` (`models.py:22-27`) charges `energy_val(cum[i][k], f_new)` for the *whole*
  job, but a prefix already executed at `f_old` — so reported online energy is wrong even setting
  admissibility aside, and C3 is being checked against a number that never happened.
- `controller._eff` (`:124-126`) returns `cum/f_new` for the whole job — `eff_override` is only
  set on *completion*, never on *start*. With `f_new > f_old` the already-executed prefix is
  credited as faster than it really was, making `_timing_ok_dynamic` (`:147`) **optimistic**.
- the per-processor DP rebuild after each event, and every metric in `simulator.run()`.

**Evidence.** `ALL_DOCS/repro_online_freq_inflight.py`. One processor; T0 `p=40`, T1 `p=10`.
Under preemptive EDF, T0,j0 starts once T1,j0 finishes and is preempted at `t=10` by T1,j1, yet
sits at chain position 3 while T1,j1 is at position 1. Firing T1,j1's early completion:

| `Z_OFF` | T0,j0 starts | freq revised | verdict |
|---|---|---|---|
| 0 | t=3.75 | z 0 → 1 | VIOLATION |
| 1 | t=2.50 | z 1 → 3 | VIOLATION |
| 2 | t=1.88 | z 2 → 3 | VIOLATION |
| 3 | t=1.50 | — | clean (no headroom above `f_max`) |

The bug needs frequency headroom to fire, so it is invisible in any run committed at `f_max` —
which is why `dry_run_tc` at B=400 never surfaced it.

**Depends on the preemption model being fully preemptive** — which it is, and this is now settled:
the blocking term implied by segment-atomic execution reaches **245% of the shortest period** in
`dry_run_tc` (largest segment 8.580 at `f_min=0.35` → 24.514 against `min p = 10`), so the
segment-atomic reading would make nearly every generated instance infeasible. June's `C7` posed
this as undecided; it is decided, and `usrt_code_review_report.html` now records it as resolved
under *Examined, not defects* — with this 245% figure as the deciding evidence, which is stronger
than the paper-wording argument it previously rested on.

**Fix options.**
1) **Track started jobs.** Maintain a `started` set; for any job in it, restrict the action set to
   `z' = z_off` while leaving `k'` free (`actions.build_job_actions` already takes the baseline, so
   this is a filter at one call site). Needs a notion of "now", which the controller currently
   lacks — `on_completion` knows `t = job_r[(i,j)]` (`:206`) but never compares it to job starts.
2) **Restrict the chain.** Re-plan only jobs with `r >= t_event`, not all of `jobs[c+1:]`. Cheaper
   and needs no new state, but it is strictly more conservative: it also drops jobs that are
   downstream *and* unstarted, losing utility the DP could legitimately have banked.
3) **Relax the paper.** Permit frequency change at preemption points. Contradicts ref [1]'s
   motivation (switch overhead/reliability) and would need the energy model to account for the
   switch. Not recommended.

**Open question.** Option 1 is correct but needs a start-time notion the online phase does not
currently carry; option 2 is a two-line change that costs utility. Which, and is the utility cost
worth measuring first?

**Note — adjacent, same root.** `simulator.py:88` iterates events in **release** order while the DP
chain is in **deadline** order, so `jobs[c+1:]` can include jobs the simulator has *already
processed as complete*. Whatever fix lands should reconcile the two orderings, not just one.

---

### HEUR-V1-RET — `heuristic_v1` is unrunnable through the runner
| field | value |
|---|---|
| Status      | **closed by decision 2026-09-12 — v1/v2 descoped** |
| Confidence  | verified live 2026-09-12; resolved by owner decision, not by a code change |
| Layer       | **C** — contract |
| Costs us    | nothing — the solvers are out of scope |
| Location    | `usrt/solvers/heuristic_v1.py` (return type) · `usrt/runner/adapters.py` dispatch list |

**Mechanism.** Two defects, one symptom.

1. `heuristic_v1.run()` returns a `ScheduleState`, not the `(seg_k, freq_idx, utility, energy)`
   4-tuple that `adapters.run_heuristic` unpacks.
2. `heuristic_v1` and `heuristic_v2` are **absent from the adapter dispatch list** entirely — it
   names only `heuristic`, `heuristic_v7/v6/v5b/v5a/v4/v3`, `heuristic_claudeoptimal`.

So (2) masks (1): the call fails before the return type can matter.

**Evidence.** 2026-09-12: `run_model('heuristic_v1', ...)` → `ValueError('unknown model
heuristic_v1')`. Called directly, `run()` returns a `ScheduleState` (confirmed by `type()`), and on
`testcase.py` at B=400 produces energy 234.71/400 — a valid schedule the runner simply cannot read.

**Decision (owner, 2026-09-12).** *"We are not really gonna consider heuristic v1 and v2 — they
are too basic."* The contract will **not** be fixed; the solvers are retired from scope. They were
already invisible to every sweep, so no published result changes.

**What this closes.** Six register items resolve off this one decision: HEUR-V1-RET itself,
STATE-ENERGY-GUARD (`ScheduleState` has no other caller), and V1-STRIP, V2-CH23, FP-DRIFT,
V1-WINDOW-BLIND — all four are internal to v1/v2.

**Code still present, pending a separate call.** Descoped is not deleted. If the files are removed,
this set goes with them and nothing else references it:
`solvers/heuristic_v1.py`, `solvers/heuristic_v2.py`, `phases/greedy_state.py`,
`phases/greedy_leftshift.py`, `state.py`, `mapping/single_pass.py`,
`aggressive.aggressive_freq_scaling_state`, plus 4 lines in `run.py`. They appear in no figure
registry and no adapter.

---

### V5AB-COMPARE — the variant ladder is not a controlled comparison
| field | value |
|---|---|
| Status      | open |
| Confidence  | **verified live 2026-09-12** (was: carried from 22Aug B1/B2, unverified) |
| Layer       | — (experiment validity) |
| Costs us    | any "Refine 2a vs 2b" claim read off the v5a/v5b pair |
| Location    | `heuristic_v3/v4/v5a` (absent) vs `heuristic_v5b/v6/v7/claudeoptimal` (present) |
| Shares root | 6B-INERT — see below |

**Mechanism.** Phase 6b (`phase_freq_utility_trade`) is applied to **4 of 7** heuristic variants.
`v5a` vs `v5b` therefore reads as "Refine 2a vs Refine 2b" when it is actually "2a without 6b vs
2b with 6b". The "one capability per step" reading of the ladder does not hold.

**Evidence.** 2026-09-12, grep of `phase_freq_utility_trade` across all seven solvers:
present in v5b, v6, v7, claudeoptimal; absent from v3, v4, v5a. (The 22 Aug figure was "3 of 6" —
the count moved with v7, the defect did not.)

**Note — the confound may be nominal.** Given 6B-INERT below, Phase 6b currently contributes
**nothing measurable**, so v5a-vs-v5b may in practice still be a clean 2a-vs-2b comparison. That is
luck, not design: fix 6b and the confound becomes real. Make the ladder honest either way.

---

### 6B-INERT — Phase 6b never fires
| field | value |
|---|---|
| Status      | open |
| Confidence  | verified live 2026-09-04 (0/72) and re-verified 2026-09-12 (0/20) |
| Layer       | **B** — valid output, the phase simply does no work |
| Costs us    | a documented 40–58% gap is recorded as closed when it is not |
| Location    | `usrt/phases/freq_trade.py` |
| Shares root | V5AB-COMPARE |

**Mechanism.** Phase 6b prices the two scarce resources off the current solution —
`λ = max u_i/g(f)` over energy-blocked segments, `μ = max u_i·f` over time-blocked ones — and
downshifts a job when `λ·ΔE > μ·ΔT`. Three things stop it:

1. **μ is a global price for a per-processor resource.** Time is per-core; the score function has
   no notion of *which* processor pays the `ΔT`. Traced on a live instance (ρ=0.6, λ=3.113,
   **μ=0.000**): donor T6,j3 frees `ΔE=0.2959`, enough for target T4,j0's 0.2394 shortfall — but
   both sit on **P1**, and the downshift spends exactly the window slack the target needed.
   `E_slack` 0.0373→0.3332 (now OK), `min_slack` 0.9258→0.4898 (need 0.6516, now SHORT). Net zero.
2. **Atomicity.** `λ·ΔE > μ·ΔT` is a marginal, continuous criterion; segments are indivisible. One
   downshift must free an entire shortfall or it yields nothing. Phase 5's case ii.B gets this right
   by stacking donors until `gained >= need`; 6b makes exactly one downshift per round.
3. **It gives up immediately** — `break` on the first non-improving round rather than trying the
   next-best candidate.

**Evidence.** 0 moves in 72 instances (2026-09-04, ρ=0.4–1.0, 8/12 tasks, 2/4 procs) and 0 in 20
instances (2026-09-12 re-check). In the 72-instance run `λ > 0` — something *was* energy-blocked —
in 26 cases, and still no move was made.

**Not a regression risk.** 6b keeps a best-so-far and restores it, so it provably cannot return a
worse schedule; inert is its designed worst case.

**Open question.** The 40–58% figure in `freq_trade.py`'s own docstring predates the `spec.py`
rewrite and has never been re-measured against the current generator. Re-measure the gap first —
if it has closed by other means, 6b may not be worth fixing at all.

---

### NO-ONLINE-ADAPTER — the online phase cannot be swept
| field | value |
|---|---|
| Status      | open (feature) |
| Confidence  | **verified live 2026-09-12** (was: carried from 22Aug D1, unverified) |
| Layer       | — |
| Costs us    | online has no OFAT curves and no head-to-head against the offline models |
| Location    | `usrt/runner/adapters.py` — `MODELS` and the dispatch chain |

**Mechanism.** `MODELS = ("ilp_v1", "ilp_v2", "ilp_v3", "ilp_v4", "heuristic",
"greedy_sps_baseline")`. The string `online` does not appear anywhere in `adapters.py`, so
`run_models.py` cannot dispatch it. `usrt/solvers/online_demo.py` is reachable only through
`run.py`, one instance at a time.

**Note.** Wiring it up is blocked in practice by **ONLINE-FREQ** — sweeping the online phase before
that is fixed would mass-produce inadmissible schedules. Fix the admissibility bug first, then the
adapter.

---

### STATE-ENERGY-GUARD — `try_dec_freq` has no energy guard
| field | value |
|---|---|
| Status      | **closed as moot 2026-09-12** |
| Confidence  | verified live 2026-09-12 — absent, and not reachable in 6 configurations tested |
| Layer       | **A** in principle; no violation ever observed |
| Costs us    | nothing — the only caller is descoped |
| Location    | `usrt/state.py` `try_dec_freq` |
| Closed by   | HEUR-V1-RET — `ScheduleState` is reached only from `heuristic_v1`, now out of scope |

**Mechanism.** The method checks timing windows only, then executes `self.slack_energy -= delta_e`
unconditionally — unlike `try_inc_seg` and `try_inc_freq`, which both guard. The guard is genuinely
missing.

**Why this is Low and not Critical.** The June review (B1) rated it Critical on the premise
`α=1.0, β=0.5`, where *every* downshift costs energy, so `aggressive_freq_scaling_state`'s
`while state.try_dec_freq(...)` loop silently blew the budget. Under today's `α=0.15, β=1.0`,
downshifting **saves** energy above `f*≈0.42` and only costs it below.

**Evidence — 2026-09-12, six configurations, no violation in any:**

| frequency set | B | final energy | over budget? | jobs below f* |
|---|---|---|---|---|
| default `[0.3 … 1.0]` | 187.48 | 186.98 | no (−0.50) | 1/30 |
| default | 220.56 | 218.84 | no (−1.72) | 1/30 |
| default | 400.00 | 234.71 | no (−165.29) | 1/30 |
| `[0.3,0.4,0.5,0.6,0.8,1.0]` | 192.99 | 191.47 | no (−1.52) | 1/30 |
| `[0.15,0.2,0.25,0.3,0.35,0.4,0.7,1.0]` | 192.99 | 191.34 | no (−1.65) | 4/30 |
| `[0.15,…,1.0]` | 275.71 | 212.44 | no (−63.27) | 3/30 |

The timing check stops the loop before it descends far enough below `f*` to matter — even with
frequency sets deliberately dense below `f*`.

**Fix.** Two-line budget guard mirroring `try_inc_freq`. Worth doing for robustness; not worth a
re-measurement, and not worth sequencing ahead of anything else.

---

### C8-HARMONIC — the hand-written testcase is not harmonic
| field | value |
|---|---|
| Status      | ready |
| Confidence  | verified live 2026-09-12 |
| Layer       | — (instance is off-model) |
| Costs us    | every single-instance figure quoted from `testcase.py` is outside the paper's model |
| Location    | `testcase.py` — periods `10, 20, 20, 40, 60, 120` |

**Mechanism.** The paper assumes a harmonic period chain. `40 ∤ 60`, so this instance violates it.
Carried from June C8 and still true.

**Why it still matters.** The *generator* is correct — `usrt/gen/spec.py` builds periods as
`base × 2^m`, so every generated set is harmonic. Only the legacy hand-written `testcase.py`
breaks it — and that file is `run.py`'s default and appears throughout `ALL_DOCS/`.

**Fix.** Change the period 60 → 80. One character, but it moves every number ever quoted from
`testcase.py`, so it should land with a doc re-baseline rather than on its own.

---

### INT-PERIOD — `int(t['p_i'])` silently truncates non-integer periods
| field | value |
|---|---|
| Status      | open (latent) |
| Confidence  | verified live 2026-09-12 — 25 sites |
| Layer       | **C** |
| Costs us    | nothing today; a silent corruption if any generator ever emits a float period |
| Location    | 25 sites across `usrt/**` |

**Mechanism.** Periods are coerced with `int()` in 25 places. A period of `10.7` becomes `10` with
no warning, changing the hyper-period, the job count and every deadline — quietly, and differently
in each of the 25 places depending on evaluation order.

**Fix.** Validate once at load time in `utils.load_testcase` and raise, instead of truncating in 25
places. Carried from June D12.

---

### HEUR1.0 — the paper's §V.B baseline is still not assembled
| field | value |
|---|---|
| Status      | open (feature) |
| Confidence  | **verified live 2026-09-12** (was: carried from 22Aug E1, unverified) |
| Layer       | — |
| Costs us    | no comparison against the baseline the paper itself prescribes |
| Location    | `usrt/solvers/greedy_sps_baseline.py` · `usrt/mapping/packers.py:wfd_mapping` |

**Mechanism.** Paper §V.B prescribes *"tasks in decreasing order of utilization … map to the first
least utilized processor"* — i.e. **WFD**. Two halves exist, and they are not joined:

* `packers.wfd_mapping` **is** the §V.B mapping — but it lives only as one candidate inside v7's
  Phase 1M multi-start, never as a standalone model.
* `greedy_sps_baseline.py` **is** a naive floor (f_max pinned, no refine, no swap) — but its
  Phase 1 is **Quantum SPS**, not WFD. Its docstring says so explicitly.

So the runnable baseline uses the wrong mapping, and the right mapping is not runnable as a
baseline. The 22 Aug note ("WFD half now exists via `packers.py`") was right about the half and
wrong to imply the item was closing.

**Fix.** A `heur1_0.py` that calls `wfd_mapping` then the same greedy body as
`greedy_sps_baseline` — a handful of lines, since both pieces already exist and are DBF-verified.

---

### DEAD-CODE — unused imports in `heuristic_v6`
| field | value |
|---|---|
| Status      | ready |
| Confidence  | **verified live 2026-09-12 by AST scan** |
| Layer       | — (hygiene) |
| Costs us    | nothing; noise only |
| Location    | `usrt/solvers/heuristic_v6.py` |

**Mechanism.** Three names are imported and never used: `compute_energy_slack`,
`estimate_operating_freq`, `is_energy_bound`.

**Half of the original claim was false, and is now becoming true.** 22Aug F2 also said
`greedy_leftshift.py` and `greedy_state.py` were "possibly orphaned". At the time they were **not**
— both are imported by `heuristic_v1` / `heuristic_v2`. With those two solvers **descoped on
2026-09-12** (see HEUR-V1-RET) the modules are orphaned in scope terms, and genuinely orphaned the
moment the solvers are deleted. Until then, deleting them still breaks `run.py`.

---

# Closed — examined, not defects

| ID | Claim | Why it was closed |
|---|---|---|
| GREEDY-ORDER | Phase 5 sorts by `u_i`, paper §V.5 says "utility density" | **Not a defect — `u_i` is the correct key.** Phase 5 decides one marginal segment; gain is `u_i·w`, cost is `w·g(f)` energy or `w/f` time, so utility-per-energy = `u_i/g(f)` and utility-per-time = `u_i·f` — **`w` cancels in both**. At uniform frequency, ordering by `u_i` *is* the correct ordering by either. Utility density (`u_i·e_opt_total/p_i`) answers Phase 1b's mapping question instead. Measured over 16 instances at ρ=0.5/0.65/0.8/1.0: mean utility `u_i` 91.271, density 91.278, `u_i/g(f)` 90.957, `u_i·f` 91.271 — a 0.35% spread, and `u_i` ≡ `u_i·f` in all 16 runs. Closed by owner 2026-09-04. |
| C7-PREEMPT | "DBF over-certifies feasibility if optional segments are atomic" (June C7, rated Critical) | **Decided: execution is fully preemptive, so DBF is the correct test and the code is right.** Two independent arguments. (1) Paper §II says *Preemptive*. (2) Quantitatively, the blocking term implied by segment-atomic execution reaches **245% of the shortest period** in `dry_run_tc` (largest segment 8.580 at `f_min=0.35` → 24.514 against `min p = 10`), so the atomic reading would make nearly every generated instance infeasible. **Action: `Key_Notes&Deductions.txt` is the stale artefact** — it still says "Preemption is NOT allowed mid-segment". Fix the note, not the code. |
| FREQ-INERT | "DVFS looks unimplemented online" (15 Aug) | **A regime effect, not a bug.** At B=400 energy is nowhere near binding, so there is no headroom up (already at `f_max`) and no incentive down. At tight budgets the DP demonstrably fires the paper's Option 3/4 conversions, including a textbook pure Option 4. |
| UTIL-FREQ-INDEP | "Utility does not depend on frequency" | **By design** — paper Eq. 8 has no `f` term. Frequency is purely a time↔energy exchange rate. This is exactly what makes donating energy cost a donor **zero** utility, which is why Phase 5's case ii.B was widened to global multi-donor. |
| NPRC-COVARY | "`n_prc` sweep co-varies `n_tsk`" (22Aug C2) | **Deliberate and documented** in `sweeps._tasks_for_cores`: `U_M = α·N_prc` grows with the core count, so the task set must grow with the system or every task is pinned at the per-task cap `γ`. |
| A-ENERGY-CONST | "α=1.0, β=0.5 make `f_max` energy-optimal, so DVFS is dead code" (June §A, rated Critical) | **Resolved by changing the constants on 22 Aug**, not the code. `models.py:19-20` now has `α=0.15, β=1.0`, so `f*≈0.42` sits inside the frequency range and Phase 4 / case ii.B / the online Options 3–4 are all live. |

---

# Fixed elsewhere — closed ledger

Items from the retired documents that are fixed in the tree, kept as one-liners so they are not
re-filed. Re-opening any of these needs fresh evidence, not the original write-up.

| Origin | Issue | How it closed |
|---|---|---|
| June B6 | Every solver crashed on a cp1252 Windows console | CLIs force UTF-8 |
| June C9 | Paper §VI online phase entirely unimplemented | `usrt/online/` implemented; worked examples reproduce the design doc |
| June C10 | Infeasible-mandatory early exit gave up too early | Phase 3 now uses `min_possible_energy()` — cheapest frequency, timing ignored — the correct necessary condition |
| June (unnumbered) | Phase 4 scaled in arbitrary task-index order | Now ranks by energy saved per unit time cost, descending |
| June (unnumbered) | Left-shift deadline ties broken by dict insertion order (2.0 vs 12.0 on one instance) | Now sorts by `(deadline, release, job-id)` |
| 22Aug A1 | `ILP.py` hard-coded the wrong energy constants | Imports from `usrt.models` |
| 22Aug A2 | `testcases/` tree (18,500 files) from the superseded generator | Deleted |
| 22Aug A3 | Gurobi licence expiring 2026-08-19 | Renewed to 2027-08-16 (LICENSEID 2853854) |
| owner decision | v1/v2 descoped — heuristic_v1/v2 too basic to keep considering | 2026-09-12, and V1-STRIP, V2-CH23, FP-DRIFT, V1-WINDOW-BLIND close as moot with them (code untouched, still importable, just out of scope) |
| 22Aug F1 | `summary-1-Aug` §4 described superseded Phase 3/4/5 logic | §4 rewritten 4 Sep against the code; Phases 1, 1M, 1R, 1L, 2–6b all match, DPS/SPS explained rather than assumed. *Partial:* §5's version matrix still stops at v6 |

---

# Not yet re-verified — do not plan against these

Each needs confirming before it earns a full entry. The 22 Aug carry-overs that *have* since been
verified were promoted above and removed from this table.

| ID | Claim | Source |
|---|---|---|
| DELTA-CAP | δ cap arithmetically impossible when β > 2α/(1−α) | 22Aug C1 |
| DBF-COMPILE | DBF hot spot is compilable — 56× available, bit-identical | 22Aug C4 |
| SCALAR-DT | scalar Δt over-plans; commit DBF trims (4.55 utility, one event, B=400) | 22Aug D2 / 15Aug |
| AGG-STATES | aggregate-state quantisation clips the exact frontier | 22Aug D3 / 15Aug |
| DP-REBUILD | per-event DP rebuild dominates online runtime (performance only) | 22Aug D4 / 15Aug |
| LEFTSHIFT-ALARM | the left-shift diagnostic raises false alarms | June D14 |
| PAPER-TYPO | paper §VII.A.2(d)(i) says "mandatory" where "optional" is meant | 22Aug E3 |

**V1-STRIP, V2-CH23, FP-DRIFT and V1-WINDOW-BLIND were removed from this table on 2026-09-12** —
all four are internal to `heuristic_v1`/`v2`, which the owner has descoped. They are recorded as
moot under *Closed* rather than carried as debt.

---

# Sequencing notes

```
ONLINE-FREQ ──blocks── NO-ONLINE-ADAPTER   sweeping online before the
                                            admissibility bug is fixed would
                                            mass-produce invalid schedules

HEUR-V1-RET DESCOPED 2026-09-12 (owner decision) -- closed V1-STRIP, V2-CH23,
FP-DRIFT, V1-WINDOW-BLIND and STATE-ENERGY-GUARD as moot in the same stroke

6B-INERT ──shares root── V5AB-COMPARE        6b contributes nothing today, so
                                             the ladder confound is currently
                                             nominal; fixing 6b makes it real

B2 ──shares root── UTIL-METRIC               LANDED TOGETHER 2026-09-05
REPAIR-PARTIAL                               FIXED 2026-09-12/13 -- algorithm
                                             (0 regressions, 32.4%->96.2% fix
                                             rate on the same needs-repair
                                             set), stdout guard, and the
                                             run() contract that let the
                                             runner check the committed
                                             schedule

RUN-FEAS                                     LANDED 2026-09-12
FREQ-SET, ONLINE-DEMO,                       isolated, land any time
INT-PERIOD, DEAD-CODE
SWAP-BREAK                                   isolated; fix the `break` AND
                                             assert on the unreachable revert
C8-HARMONIC                                  isolated, but moves every number
                                             quoted from testcase.py — land it
                                             with a doc re-baseline
```

**Highest value: ONLINE-FREQ.** It is the only Layer-A item with a confirmed violation, it
*invalidates* results rather than degrading them, and it is the only open item that changes what
can be claimed in the paper.

**Sequencing question — answered.** B2 moved every published number, and the plan taken was to
re-measure at the point B2 landed rather than batch it: `tc_b2/u_mand_factor/` holds the
900-instance before/after for all three models, and `ALL_DOCS/` has **not** yet been re-baselined
against it. Anything in `ALL_DOCS/` quoting mapping quality, SPS-vs-alternative, or per-model
utility predates 2026-09-05 and is stale — `22Aug_better_mapping_SPS.html` most of all, since its
`sps`, `sps+refine2b` and `sps+budget` candidates all ran through the broken metric **and** its
`wfd`/`ffd`/`bfd` candidates ran through the `packers.py` copy of the same bug.
