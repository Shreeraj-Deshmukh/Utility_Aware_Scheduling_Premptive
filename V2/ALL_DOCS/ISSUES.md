# USRT — Issue Register

Working file. We **append** findings here as they are confirmed; we do **not** fix them one at a
time. Once the register is populated we read it whole and derive a single sequenced plan, because
several issues share a root and fixing them separately produces layered patches that fight.

- Discussion happens in chat. This file holds only what survived scrutiny.
- Either of us edits it.
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
| Status      | open |
| Confidence  | verified live 2026-09-04 |
| Layer       | **B** — output stays legal, quality is wrong |
| Costs us    | every SPS-vs-alternative result we have published |
| Location    | `usrt/mapping/quantum.py:39, 79, 84, 117, 124, 156` |
| Shares root | UTIL-METRIC |
| Blocks      | — |
| Blocked by  | — |

**Intent — what the gate is actually for.** `quantum_sps_mapping` walks the hyper-period one
quantum `[q_start, q_end]` at a time (quantum = `gcd(periods)`, so every release and deadline falls
on a boundary). Inside a quantum it splits pending jobs into *mandatory-now* (`d == q_end`, must be
placed) and *deferrable* (`d > q_end`), hands them to DPS+SPS for criss-cross load balancing, then
needs an admission test: **"can the processors still absorb this quantum's jobs, or must some be
pushed later?"** That test is `proc_util` against capacity `m` (`:79`, `:117`). It matters because
DPS and SPS see only scalar loads — they know nothing about releases or deadlines — so this gate is
the *only* thing inside the per-quantum loop preventing a core from being overfilled. All remaining
timing correctness is deferred to the mandatory-only DBF check + repair after the loop ends.

**Mechanism.** `proc_util` is initialised once (`:39`) and only ever accumulated into (`:117`,
`:124`). It is therefore a running sum of `e_m/p_i` over the whole hyper-period — one term per
**job** — not a utilisation, and unbounded. Utilisation is a *rate*: a task consuming 24.5% of a
core consumes 24.5% at every instant, permanently. The gate adds that rate once per job release and
never releases it, so it compares a quantity that grows with time against a capacity that does not.
The comparison is therefore guaranteed to fail eventually; processor count only changes *when*.
Once it passes `m`, `remaining_cap` at `:79` goes negative, the pre-filter at `:81` tries to defer
its way back under capacity but never can, every later quantum takes the `MAND_OVERUTIL` break at
`:84` and commits nothing, and those `active` jobs are not even appended to `leftover` — they fall
through to the min-util round-robin at `:156`.

**Blast radius.** `repair.py` (same metric drives its target choice) · `multistart.py`
(3 of 7 candidates route through SPS) · `ilp_v2.py` (consumes the same mapping) ·
v5a/v5b/v6/v7 (all print the metric) · **every number in `ALL_DOCS/`**.

**Evidence.**
- 22 of 30 jobs on `testcase.py` (73%) placed by fallback. The workload is not the problem: real
  utilisation there is **1.33 against capacity 2.0** — mandatory-only at f_max is the lightest load
  the system ever sees and it fits comfortably. The counter nonetheless reaches **6.50**, because
  T0 (p=10, u=0.245, 12 jobs) contributes 0.245 × 12 = **2.94 by itself** — more than both cores
  combined, for a task that never needs more than a quarter of one core.
- **Adding processors does not help.** N_tsk=12, `u_mand_factor`=0.4, sweeping N_prc 2→8:
  fallback 16 / 18 / 17 / 17 / 19%. `A = Σ_i (H/p_i)·(e_m_i/p_i)` grows ×4.17 as m grows ×4, so the
  capacity added is cancelled exactly by the load that comes with it.
- Fallback fraction is predicted by `1 − m/A`; substituting `A ≈ n̄ · u_mand_factor · m` (n̄ = mean
  jobs per task) gives **`1 − 1/(n̄ · u_mand_factor)` — N_prc cancels out entirely**. The gate
  survives the whole hyper-period only when `n̄ · u_mand_factor ≤ 1`.
- Measured drivers at N_prc=4, n̄=4.17 — `u_mand_factor` 0.2/0.3/0.4/0.5/0.6 → fallback
  0/18/38/49/60%; period spread `k_max` 2→3 (n̄ 1.75→4.17) → 19%→49%. Both track the formula.
  **This is the normal operating point, not a corner case** — it vanishes only in the
  low-utilisation, short-hyper-period corner.
- First documented 2026-06-12 as `usrt_code_review_report.html` **B2** (High); dropped from
  `audit_issues_22Aug.html`, so it has been invisible since.

**Fix options.** All four must answer the same question — what should `proc_util` *mean*?

1. **Event-based release** (the June review's proposal). Keep the running load, but subtract a
   job's `e_m/p_i` at the quantum where its deadline passes. Smallest diff; restores the intended
   "current occupancy" reading. Still a utilisation proxy, so still not the quantity that decides
   feasibility.
2. **Per-quantum interval load.** Replace the metric: measure work against window length
   (`Σ e_m / quantum`) over jobs whose windows overlap the quantum, rather than `e_m/p_i`.
   Dimensionally correct for the question being asked *inside* a quantum, and matches what the
   mandatory-now classification already implies (those jobs share deadline `q_end`). Needs care for
   work carried in from earlier quanta.
3. **Drop the proxy — gate on DBF itself.** `check_dbf_mandatory` already exists and already runs
   after the loop; use it (per affected processor) as the admission test and defer only on real
   infeasibility. Most correct and removes UTIL-METRIC as a separate issue. Cost is
   O(|A|·|D|·n) per quantum — but `state.py` already implements incremental DBF with identical
   semantics and is currently used by nothing but `heuristic_v1`, so the machinery exists.
4. ~~Per-quantum reset~~ — diagnostic probe only, **not a fix**. See the scoring note below.

**Scoring note — this is the trap.** The fallback path is `min(range(m), key=proc_util)`, i.e.
worst-fit on cumulative load, which is a respectable partitioning heuristic in its own right. The
pipeline does not degrade to garbage when SPS drops out; it degrades to *worst-fit*. Probe (4)
removed the fallback completely and moved final utility **−14%..+11%, mean −2%** across 12
instances. So a fix must be scored on **downstream utility**, never on "fallback count = 0" — and
criss-cross SPS is not automatically the winner on the real objective.

**Open question.** (1), (2) and (3) are three different semantics, not three spellings of one.
Decide what `proc_util` is *meant* to be before writing any of them. Note that (3) makes
UTIL-METRIC moot rather than merely consistent, which is worth weighing against its cost.

---

### UTIL-METRIC — "utilisation" is summed over jobs, not tasks
| field | value |
|---|---|
| Status      | open |
| Confidence  | verified live 2026-09-04 |
| Layer       | **B** (+ display) |
| Costs us    | every `← OVER 1.0` warning in the logs is spurious |
| Location    | `quantum.py:77-78, 113, 147, 160` · `heuristic_v5b.py:58, 73` (and v5a/v6/v7) · `repair.py:92` |
| Shares root | B2 — **must land in the same change** |
| Blocks      | — |
| Blocked by  | — |

**Mechanism.** `Σ_jobs e_m_i/p_i = Σ_i (H/p_i)·(e_m_i/p_i)` — inflated by `H/p_i`. Utilisation is
a per-*task* quantity being summed per *job*.

**Evidence.** `testcase.py` prints `P0: util=3.2434 ← OVER 1.0` for a mapping whose true
utilisation is ~0.67 and which DBF confirms feasible.

**Fix options.** Print `Σ over distinct tasks`. Trivial once B2's semantics are settled — but if
fixed *separately* the diagnostic and the mapper would disagree, which is worse than both being
wrong consistently.

---

### REPAIR-PARTIAL — `repair_mapping` can return PARTIAL and no solver checks
| field | value |
|---|---|
| Status      | open |
| Confidence  | verified live 2026-09-04 |
| Layer       | **A** — a returned schedule can violate C2 |
| Costs us    | a deadline-missing schedule can print as `SOLUTION (FINAL)` |
| Location    | `usrt/mapping/repair.py:60, 96` · consumed at `quantum.py:150-152` |
| Blocks      | — |
| Blocked by  | B2 (changing the mapper changes how often repair is even reached) |

**Mechanism.** `repair_mapping` retries 100 times then returns `(mapping, ok)`. `quantum.py`
prints `PARTIAL` when `ok` is false **and returns the mapping anyway**. The v5+ solvers never
inspect it; only `adapters._mandatory_feasible` gates, and only for runner-driven runs — a direct
`python run.py` has no guard at all.

**Open question.** On PARTIAL: abort, or fall back to a different mapping strategy? v7's
multi-start makes the second genuinely available now.

---

### RUN-FEAS — runner error path clobbers the manifest's `feasible` column
| field | value |
|---|---|
| Status      | ready |
| Confidence  | verified live 2026-09-04 |
| Layer       | **C** — contract |
| Costs us    | corrupts the generator's instance-level flag in `results.csv` |
| Location    | `usrt/runner/runner.py:95` |
| Blocks      | — |
| Blocked by  | — |

**Mechanism.** The outer `except` writes `feasible=0`; the schema is `model_feasible`
(`runner.py:19`, `adapters.py:8-12`). The row is merged as `{**row, **metrics}` and the manifest
owns `feasible` (`emit.py:19`), so a `load_testcase` failure overwrites it. Exactly what the
module docstring two lines above warns against. `run_model`'s own handler is correct.

**Note.** `audit_issues_22Aug.html` lists this collision as *fixed and deliberately omitted* — the
fix landed in `adapters.py` and this path was missed. Isolated; no coupling.

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

### FREQ-SET — `processors[0]['frequencies']` assumed for all processors, in 17 places
| field | value |
|---|---|
| Status      | open (latent) |
| Confidence  | verified live 2026-09-04 |
| Layer       | **C** |
| Costs us    | nothing today; blocks paper §VII.A fidelity |
| Location    | 17 sites incl. `heuristic_v{1..7}.py`, `ilp_v2.py`, `adapters.py:150,185`, `online/controller.py:59`, `ILP.py:96` |

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

# Closed — examined, not defects

| ID | Claim | Why it was closed |
|---|---|---|
| GREEDY-ORDER | Phase 5 sorts by `u_i`, paper §V.5 says "utility density" | **Not a defect — `u_i` is the correct key.** Phase 5 decides one marginal segment; gain is `u_i·w`, cost is `w·g(f)` energy or `w/f` time, so utility-per-energy = `u_i/g(f)` and utility-per-time = `u_i·f` — **`w` cancels in both**. At uniform frequency, ordering by `u_i` *is* the correct ordering by either. Utility density (`u_i·e_opt_total/p_i`) answers Phase 1b's mapping question instead. Measured over 16 instances at ρ=0.5/0.65/0.8/1.0: mean utility `u_i` 91.271, density 91.278, `u_i/g(f)` 90.957, `u_i·f` 91.271 — a 0.35% spread, and `u_i` ≡ `u_i·f` in all 16 runs. Closed by owner 2026-09-04. |

---

# Not yet re-verified — do not plan against these

Carried from `audit_issues_22Aug.html`; each needs confirming before it earns a full entry.

| ID | Claim | Source |
|---|---|---|
| HEUR-V1-RET | `heuristic_v1` returns a `ScheduleState`, not the runner's 4-tuple | B4 |
| DELTA-CAP | δ cap arithmetically impossible when β > 2α/(1−α) | C1 |
| SCALAR-DT | scalar Δt over-plans; commit DBF trims (4.55 utility, one event, B=400) | D2 |
| NO-ONLINE-ADAPTER | online phase absent from `run_models.py` | D1 |
| HEUR1.0 | paper §V.B baseline unimplemented (WFD half now exists via `packers.py`) | E1 |
| V5AB-COMPARE | v5a/v5b no longer a controlled comparison (6b in one, not the other) | B1/B2 |
| DEAD-CODE | unused imports in v6; `greedy_leftshift.py` / `greedy_state.py` possibly orphaned | F2 |

---

# Sequencing notes (fill in as the register grows)

Edges known so far:

```
B2 ──shares root── UTIL-METRIC        one change, or the mapper and its
                                       diagnostic disagree

B2 ──blocks── REPAIR-PARTIAL           changing the mapper changes how often
                                       repair is reached at all

RUN-FEAS, FREQ-SET, ONLINE-DEMO        isolated, land any time
```

**Open sequencing question.** B2 moves every published number. Decide whether the plan
re-baselines `ALL_DOCS/` after it lands, or whether B2 waits until the rest of the offline fixes
are ready so we re-measure **once**.
