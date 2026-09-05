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

### REPAIR-PARTIAL — `repair_mapping` can return PARTIAL and no solver checks
| field | value |
|---|---|
| Status      | open |
| Confidence  | verified live 2026-09-04 |
| Layer       | **A** — a returned schedule can violate C2 |
| Costs us    | a deadline-missing schedule can print as `SOLUTION (FINAL)` |
| Location    | `usrt/mapping/repair.py:60, 96` · consumed at `quantum.py:150-152` |
| Blocks      | — |
| Blocked by  | ~~B2~~ — landed 2026-09-05. Repair now fires far less often (fallback is 0%), so this is rarer but **not** fixed: a PARTIAL return is still unchecked. |

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
B2 ──shares root── UTIL-METRIC        LANDED TOGETHER 2026-09-05, as required

B2 ──blocked── REPAIR-PARTIAL          B2 has landed; repair now fires far less
                                       often, so REPAIR-PARTIAL is rarer but
                                       still unfixed and now unblocked

RUN-FEAS, FREQ-SET, ONLINE-DEMO        isolated, land any time
SWAP-BREAK                             isolated; fix the `break` AND assert on
                                       the supposedly-unreachable revert
```

**Sequencing question — now answered.** B2 moved every published number, and the plan taken was
to re-measure at the point B2 landed rather than batch it: `tc_b2/u_mand_factor/` holds the
900-instance before/after for all three models, and `ALL_DOCS/` has **not** yet been re-baselined
against it. Anything in `ALL_DOCS/` quoting mapping quality, SPS-vs-alternative, or per-model
utility predates 2026-09-05 and is stale — `22Aug_better_mapping_SPS.html` most of all, since its
`sps`, `sps+refine2b` and `sps+budget` candidates all ran through the broken metric **and** its
`wfd`/`ffd`/`bfd` candidates ran through the `packers.py` copy of the same bug.

**Next.** With B2 and UTIL-METRIC closed, the remaining open entries are independent of each
other: REPAIR-PARTIAL and SWAP-BREAK (both need a decision, not just a keystroke), RUN-FEAS
(`ready`, one line), FREQ-SET and ONLINE-DEMO (latent), IXB-ROUTING (feature), NO-TESTS (blocks
safe work on any of them).
