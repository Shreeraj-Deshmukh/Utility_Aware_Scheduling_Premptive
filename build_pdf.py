"""Generate heuristic_v5_report.pdf using fpdf2 (ASCII-safe)."""

from fpdf import FPDF

L_MARGIN = 18
R_MARGIN = 18
PAGE_W   = 210
BODY_W   = PAGE_W - L_MARGIN - R_MARGIN


class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 5,
            "Heuristic v5 - Utility-Density Aware Mapping Refinement | USRT Scheduling",
            align="C")
        self.ln(1)
        self.set_draw_color(150, 150, 150)
        self.line(L_MARGIN, self.get_y(), PAGE_W - R_MARGIN, self.get_y())
        self.ln(4)
        self.set_text_color(0, 0, 0)
        self.set_draw_color(0, 0, 0)

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 5, f"Page {self.page_no()}", align="C")
        self.set_text_color(0, 0, 0)


def new_pdf():
    pdf = PDF(format="A4")
    pdf.set_margins(L_MARGIN, 22, R_MARGIN)
    pdf.set_auto_page_break(True, margin=15)
    pdf.add_page()
    return pdf


# ── helpers ───────────────────────────────────────────────────────────────────

def title_block(pdf):
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(20, 40, 80)
    pdf.cell(0, 8,
        "Heuristic v5: Utility-Density Aware Mapping Refinement",
        align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "I", 11)
    pdf.set_text_color(60, 60, 80)
    pdf.cell(0, 6,
        "Post-SPS Balancing of Optional-Segment Utility Potential",
        align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 5, "Technical Report  |  USRT Scheduling System",
        align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(20, 40, 80)
    pdf.set_line_width(0.6)
    pdf.line(L_MARGIN, pdf.get_y() + 2, PAGE_W - R_MARGIN, pdf.get_y() + 2)
    pdf.ln(6)
    pdf.set_text_color(0, 0, 0)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_line_width(0.2)


def section(pdf, title):
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(20, 40, 80)
    pdf.set_fill_color(225, 235, 255)
    pdf.set_draw_color(100, 130, 200)
    pdf.set_line_width(0.3)
    pdf.cell(BODY_W, 6.5, "  " + title, border="LB", fill=True,
             new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_line_width(0.2)
    pdf.ln(2)


def subsec(pdf, title):
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(30, 60, 120)
    pdf.cell(BODY_W, 5.5, title, new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0)
    pdf.ln(0.5)


def body(pdf, text, size=9):
    pdf.set_font("Helvetica", "", size)
    pdf.multi_cell(BODY_W, 4.8, text, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)


def formula(pdf, text):
    pdf.set_font("Courier", "B", 9.5)
    pdf.set_fill_color(248, 248, 248)
    pdf.set_draw_color(180, 180, 180)
    pdf.multi_cell(BODY_W, 5.5, "  " + text,
                   border=1, fill=True, align="C",
                   new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(0, 0, 0)
    pdf.ln(1.5)


def callout(pdf, text, color=(255, 245, 210), border_color=(200, 150, 30)):
    pdf.set_font("Helvetica", "", 8.8)
    pdf.set_fill_color(*color)
    pdf.set_draw_color(*border_color)
    pdf.set_line_width(0.5)
    pdf.multi_cell(BODY_W, 4.6, text,
                   border=1, fill=True, new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(0, 0, 0)
    pdf.set_line_width(0.2)
    pdf.ln(2)


def bullets(pdf, items):
    pdf.set_font("Helvetica", "", 9)
    for item in items:
        pdf.set_x(L_MARGIN + 3)
        pdf.cell(5, 4.8, "-", new_x="RIGHT", new_y="TOP")
        pdf.multi_cell(BODY_W - 8, 4.8, item, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)


def algo(pdf, title, lines):
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_fill_color(215, 228, 255)
    pdf.set_draw_color(100, 130, 200)
    pdf.set_line_width(0.4)
    pdf.cell(BODY_W, 6, "  Algorithm: " + title,
             border="LTR", fill=True, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Courier", "", 7.8)
    pdf.set_fill_color(245, 248, 255)
    for ln in lines:
        pdf.set_x(L_MARGIN)
        pdf.cell(BODY_W, 4.5, "  " + ln,
                 border="LR", fill=True, new_x="LMARGIN", new_y="NEXT")
    pdf.set_x(L_MARGIN)
    pdf.cell(BODY_W, 2, "", border="LBR", fill=True,
             new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(0, 0, 0)
    pdf.set_line_width(0.2)
    pdf.ln(2)


def tbl(pdf, headers, rows, col_widths):
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_fill_color(200, 215, 245)
    pdf.set_draw_color(100, 130, 200)
    pdf.set_line_width(0.3)
    pdf.set_x(L_MARGIN)
    for h, cw in zip(headers, col_widths):
        pdf.cell(cw, 6, " " + h, border=1, fill=True)
    pdf.ln()
    pdf.set_font("Helvetica", "", 8.2)
    for ri, row in enumerate(rows):
        pdf.set_x(L_MARGIN)
        fill = ri % 2 == 0
        pdf.set_fill_color(248, 250, 255) if fill else pdf.set_fill_color(255, 255, 255)
        row_h = 5
        for cell, cw in zip(row, col_widths):
            pdf.multi_cell(cw, row_h, " " + cell, border=1,
                           fill=fill, new_x="RIGHT", new_y="TOP")
        pdf.ln(row_h)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_line_width(0.2)
    pdf.ln(2)


# ─────────────────────────────────────────────────────────────────────────────
pdf = new_pdf()
title_block(pdf)

# ── 1. Motivation ─────────────────────────────────────────────────────────────
section(pdf, "1.  Motivation and Problem")

subsec(pdf, "1.1  The USRT Problem")
body(pdf,
    "The Utility-Aware Scheduling with Real-Time constraints (USRT) problem maps "
    "periodic real-time tasks to processors. Each task Ti has:\n"
    "  - A mandatory segment (execution time e_m) that must complete before the deadline.\n"
    "  - N_seg optional segments with incremental execution times. Running them yields utility.\n"
    "  - A utility rate u_i: reward per unit of optional execution time.\n\n"
    "The objective is to maximise total utility subject to EDF timing feasibility "
    "and a global energy budget B.")

subsec(pdf, "1.2  What SPS Does and Misses")
body(pdf,
    "Phase 1 uses SPS (Sum Partial Solutions) to map jobs to processors. "
    "Its load metric is mandatory utilisation: l_i = e_m / p_i. "
    "SPS minimises the gap between the most- and least-loaded processor, producing "
    "a mapping where every processor carries approximately equal mandatory load. "
    "This is correct for EDF feasibility (Liu & Layland: EDF schedules a task set "
    "on one processor if and only if total utilisation <= 1.0).")

callout(pdf,
    "THE SPS INADEQUACY:  SPS knows nothing about optional segments or utility. "
    "It can accidentally map all high-utility tasks onto one processor. Even if "
    "the energy budget allows their optional segments to run, the timing constraint "
    "on that congested processor prevents it. The other processor has free time but "
    "nothing valuable to fill it with.",
    color=(255, 238, 200), border_color=(200, 140, 20))

subsec(pdf, "1.3  Heuristic v5 - the Fix")
body(pdf,
    "Heuristic v5 inserts a new Phase 1b (Refine Mapping) immediately after Phase 1 "
    "(SPS). It adjusts which jobs sit on which processor to spread utility potential "
    "evenly, without breaking the feasible mandatory mapping that SPS produced.\n\n"
    "Two algorithms are provided:\n"
    "  - v5a (Step 2a): single linear scan over all doublets.\n"
    "  - v5b (Step 2b): iterative one-swap-one-scan, always targeting the globally "
    "most overloaded processor.\n\n"
    "Phases 2-6 (left-shift diagnostic, energy check, frequency scaling, greedy "
    "optional segments, pairwise swap) are identical to Heuristic v4.")

# ── 2. Key Definitions ────────────────────────────────────────────────────────
section(pdf, "2.  Key Definitions")

subsec(pdf, "2.1  Cumulative Execution Time")
body(pdf,
    "Let c[i][k] = e_{i,0} + e_{i,1} + ... + e_{i,k}  (at f_max, k = 0..N_seg).\n"
    "So c[i][0] = e_m (mandatory only)  and  c[i][N_seg] = full execution if all segments run.")

subsec(pdf, "2.2  Utility Density of a Task")
formula(pdf, "ud(i)  =  u_i  x  ( c[i][N_seg] - c[i][0] )  /  p_i")
body(pdf,
    "Plain English: if this task always ran all its optional segments, "
    "how much utility would it generate per unit of clock time?\n\n"
    "  u_i                        reward per unit of optional execution time\n"
    "  c[i][N_seg] - c[i][0]     total optional execution time available per job\n"
    "  1 / p_i                    how many times per unit clock time this task recurs\n\n"
    "Every job of task Ti has the same ud(i). A task with ud=5.0 is 5x more "
    "valuable per clock-second than one with ud=1.0.")

subsec(pdf, "2.3  Processor Utility Density")
formula(pdf, "UD(x)  =  sum of ud(i)  for all jobs (i,j) mapped to processor x")
body(pdf,
    "The total utility potential concentrated on processor x. "
    "The refinement goal is to make UD(x) approximately equal across all processors.")

subsec(pdf, "2.4  Mandatory Utilisation")
formula(pdf, "mu(i) = e_m(i) / p_i          MU(x) = sum of mu(i) over all jobs on x")
body(pdf,
    "SPS balances MU(x). The refinement must preserve this balance "
    "(see Condition 2 in Section 4).")

# ── 3. Doublets ───────────────────────────────────────────────────────────────
section(pdf, "3.  Doublets")

body(pdf,
    "A doublet is any pair of two jobs drawn from the full job set. "
    "All C(N_jobs, 2) pairs are formed and sorted by ASCENDING |ud(a) - ud(b)|. "
    "Pairs with similar utility density come first; pairs with very different "
    "utility density come last.")

callout(pdf,
    "WHY THIS ORDER?  Jobs with similar ud are the most interchangeable - swapping "
    "them between processors barely shifts the UD distribution. Jobs with very "
    "different ud are the big moves. Sorted ascending, the list moves from safe, "
    "small adjustments up to large disruptive ones. "
    "Both 2a and 2b scan this list from the front.",
    color=(228, 248, 228), border_color=(50, 150, 50))

body(pdf,
    "Doublets are built once before any swaps and reused throughout. "
    "Each pair is visited at most a bounded number of times.")

# ── 4. Acceptance Conditions ──────────────────────────────────────────────────
section(pdf, "4.  Swap Acceptance Conditions")

body(pdf,
    "Any proposed swap of job a (on Pa) with job b (on Pb) must pass ALL THREE "
    "of the following conditions before being committed. "
    "Conditions 1 and 2 are O(1) checks. Condition 3 (DBF) is only reached if "
    "both pass, so the expensive window check is rarely invoked.")

subsec(pdf, "Condition 1 -- UD Imbalance Decreases")
body(pdf, "Simulate the swap on temporary values (real data is NOT modified):")
formula(pdf,
    "UD'(Pa) = UD(Pa) - ud(a) + ud(b)\n"
    "UD'(Pb) = UD(Pb) - ud(b) + ud(a)")
body(pdf,
    "For Step 2a (pair-level check):\n"
    "  |UD'(Pa) - UD'(Pb)|  <  |UD(Pa) - UD(Pb)| - epsilon\n"
    "  The UD imbalance between these two specific processors must strictly decrease.\n\n"
    "For Step 2b (global max-UD check):\n"
    "  max( UD'(P1), UD'(Pb) )  <  UD(P1) - epsilon\n"
    "  where P1 is the globally highest-UD processor. The new maximum across both "
    "affected processors must be strictly less than P1's current UD. "
    "This also prevents cycling: every accepted swap strictly reduces the global max.")

subsec(pdf, "Condition 2 -- Mandatory Utilisation Balance Does Not Worsen")
callout(pdf,
    "WHY THIS GUARD IS NEEDED.  Without it, a swap that improves UD balance might "
    "move a high-e_m job onto an already-loaded processor. That processor then has "
    "little timing slack left for optional segments, even though UD is balanced on "
    "paper. Phase 5 finds fewer optional segments can fit, and total utility drops. "
    "This was the root cause of the low-utility failure before this guard was added.",
    color=(255, 238, 200), border_color=(200, 140, 20))
formula(pdf,
    "delta_cur = |MU(Pa) - MU(Pb)|\n"
    "delta_new = |(MU(Pa)-mu(a)+mu(b)) - (MU(Pb)-mu(b)+mu(a))|\n"
    "Accept only if:  delta_new  <=  delta_cur + epsilon")

subsec(pdf, "Condition 3 -- DBF Timing Feasibility")
body(pdf,
    "Build hypothetical job lists for both processors after the swap (temporary "
    "copies only). Run a mandatory-only DBF check at f_max on both:\n\n"
    "  For every window [t1, t2] on processor x:\n"
    "  sum of e_m for all jobs with release >= t1 and deadline <= t2  <=  (t2 - t1)\n\n"
    "If either processor violates this, the swap is rejected. This is the hard "
    "correctness guarantee: no committed swap ever makes the mandatory schedule "
    "infeasible under EDF. Only if all three conditions pass does _do_swap() get "
    "called to permanently update the six tracked data structures.")

# ── 5. Algorithm 2a ───────────────────────────────────────────────────────────
section(pdf, "5.  Algorithm Step 2a - Linear Doublet Scan (v5a)")

algo(pdf, "Refine Mapping - Step 2a", [
    "Compute ud(i), mu(i) for all tasks",
    "Initialise UD(x), MU(x) for all processors from current mapping",
    "Build doublets = all job pairs, sorted by ascending |ud(a)-ud(b)|",
    "",
    "FOR EACH (a, b) IN doublets:              # visits every pair exactly once",
    "  Pa = mapping[a];  Pb = mapping[b]",
    "  IF Pa == Pb: CONTINUE                   # same processor, skip",
    "",
    "  Compute UD'(Pa), UD'(Pb)               # Condition 1 check",
    "  IF |UD'(Pa)-UD'(Pb)| >= |UD(Pa)-UD(Pb)| - eps: CONTINUE",
    "",
    "  Compute delta_new                        # Condition 2 check",
    "  IF delta_new > delta_cur + eps: CONTINUE",
    "",
    "  IF SwapFeasible(a, b, Pa, Pb):          # Condition 3 (DBF check)",
    "    DoSwap(a, b, Pa, Pb)                  # commit swap",
    "    # NO break -- continue to next pair in list",
    "",
    "END FOR",
])

body(pdf,
    "Key property of 2a: the loop NEVER breaks early. Every doublet pair is "
    "visited exactly once. When a swap is committed, UD and MU are updated "
    "immediately so subsequent pairs see the current state. This is a "
    "DISTRIBUTED approach: it fixes many local imbalances in a single "
    "left-to-right pass without ever re-identifying the globally worst processor.")

# ── 6. Algorithm 2b ───────────────────────────────────────────────────────────
section(pdf, "6.  Algorithm Step 2b - One-Swap-One-Scan (v5b)")

algo(pdf, "Refine Mapping - Step 2b", [
    "Compute ud(i), mu(i);  initialise UD(x), MU(x)",
    "Build doublets as in Step 2a",
    "",
    "OUTER LOOP:",
    "  P1 = processor with max UD(x)           # re-identified every iteration",
    "  P2 = processor with min UD(x)",
    "  IF UD(P1) - UD(P2) < eps: BREAK         # already balanced",
    "",
    "  swapped = False",
    "  FOR EACH (a, b) IN doublets:            # inner scan from the beginning",
    "    hi = job with higher ud in pair",
    "    lo = the other job",
    "    IF mapping[hi] != P1: CONTINUE        # hi-ud job must be on P1",
    "    Pb = mapping[lo]",
    "    IF Pb == P1: CONTINUE",
    "",
    "    IF max(UD'(P1),UD'(Pb)) >= UD(P1)-eps: CONTINUE  # Condition 1",
    "    IF delta_new > delta_cur + eps: CONTINUE           # Condition 2",
    "    IF SwapFeasible(hi, lo, P1, Pb):                  # Condition 3",
    "      DoSwap(hi, lo, P1, Pb)",
    "      swapped = True",
    "      BREAK                              # exit inner, go back to outer",
    "  END FOR",
    "",
    "  IF NOT swapped: BREAK                  # no valid swap found: done",
    "END LOOP",
])

body(pdf,
    "Key properties of 2b:\n\n"
    "  BREAK after first valid swap: the inner loop is abandoned immediately. "
    "The outer loop goes back to the top and re-identifies P1 from the updated "
    "UD values. The next inner scan restarts from the beginning of the doublet list.\n\n"
    "  Always targets P1: the swap always moves a job off the globally most "
    "overloaded processor. This is the GREEDY approach.\n\n"
    "  Termination guarantee: Condition 1 for 2b requires "
    "max(UD'(P1), UD'(Pb)) < UD(P1). Every accepted swap strictly reduces "
    "the global maximum UD. Since UD >= 0, the outer loop must terminate.")

# ── 7. DoSwap ─────────────────────────────────────────────────────────────────
section(pdf, "7.  DoSwap - Data Structures Updated")

body(pdf,
    "When a swap of job a (on Pa) with job b (on Pb) is committed, "
    "six quantities are updated atomically:")

tbl(pdf,
    ["Data Structure", "Update after swap  a(Pa) <-> b(Pb)"],
    [
        ["mapping[a]",    "Pa  ->  Pb"],
        ["mapping[b]",    "Pb  ->  Pa"],
        ["proc_jobs[Pa]", "remove a,  add b"],
        ["proc_jobs[Pb]", "remove b,  add a"],
        ["UD(Pa)",        "UD(Pa) - ud(a) + ud(b)"],
        ["UD(Pb)",        "UD(Pb) - ud(b) + ud(a)"],
        ["MU(Pa)",        "MU(Pa) - mu(a) + mu(b)"],
        ["MU(Pb)",        "MU(Pb) - mu(b) + mu(a)"],
    ],
    [60, BODY_W - 60])

body(pdf,
    "UD and MU are running totals updated incrementally after each swap. "
    "Conditions 1 and 2 are therefore O(1) per candidate pair. "
    "Condition 3 (DBF) is only computed after 1 and 2 pass.")

# ── 8. 2a vs 2b ──────────────────────────────────────────────────────────────
section(pdf, "8.  Comparison: Step 2a vs Step 2b")

tbl(pdf,
    ["Property", "Step 2a  (v5a)", "Step 2b  (v5b)"],
    [
        ["Structure",
         "Single linear pass over all doublets",
         "Outer loop + inner scan, repeated"],
        ["Target processor",
         "Whichever processors the current pair happens to be on",
         "Always the globally highest-UD processor P1"],
        ["After a swap",
         "Continue to next pair (no break)",
         "Break inner; re-identify P1; restart scan"],
        ["Doublet scans",
         "Exactly one",
         "One per accepted swap"],
        ["UD condition",
         "Pair-level |UD(Pa)-UD(Pb)| decreases",
         "Global max UD strictly decreases"],
        ["Approach",
         "Distributed: fixes many local imbalances simultaneously",
         "Greedy: always attacks the single biggest problem"],
        ["Worst-case cost",
         "O(N^2 * W^2)  once",
         "O(k * N^2 * W^2),  k = accepted swaps"],
    ],
    [38, (BODY_W - 38) // 2, (BODY_W - 38) // 2])

# ── 9. Why UD is the right metric ────────────────────────────────────────────
section(pdf, "9.  Why SPS Uses Utilisation and Why UD is the Right Metric")

subsec(pdf, "9.1  Why SPS uses e_m/p_i and not raw e_m")
body(pdf,
    "Raw execution time e_m alone is meaningless for scheduling balance. "
    "A job with e_m=10 and p=10 occupies the processor 100% of the time; "
    "one with e_m=10 and p=100 occupies only 10%. "
    "Utilisation e_m/p_i normalises for period and measures the fraction of "
    "processor time consumed per unit clock time. "
    "Balancing utilisation gives equal mandatory load, which is exactly the "
    "condition for EDF feasibility. All SPS feasibility checks and gap "
    "computations work in utilisation units, not raw execution time.")

subsec(pdf, "9.2  Comparing refinement metric candidates")

tbl(pdf,
    ["Metric", "Reward?", "Amount?", "Key Problem"],
    [
        ["e_m/p_i  (mand. util.)",
         "No", "No",
         "SPS already balances this. Refinement is a no-op."],
        ["u_i only",
         "Yes (rate)", "No",
         "Ignores how much optional work exists and how often the task repeats."],
        ["e_opt/p_i  (opt. exec.)",
         "No", "Yes",
         "Treats all optional work equally. Misleads when u_i varies."],
        ["u_i x e_opt/p_i  (UD)",
         "Yes", "Yes",
         "Best available proxy. Overestimates achievable; needs mutil guard."],
    ],
    [44, 20, 20, BODY_W - 84])

body(pdf,
    "UD = 'if all optional segments ran, how much utility per unit clock time?' "
    "It correctly weights tasks that are frequent (small p_i), valuable (large u_i), "
    "and have large optional work (large e_opt).\n\n"
    "Known limitation: UD uses the theoretical maximum (all segments). "
    "The actual achievable utility per processor cannot be computed without "
    "running Phase 5 first (chicken-and-egg problem). UD is therefore the "
    "best available proxy computable before scheduling begins.")

# ── 10. Full Pipeline ─────────────────────────────────────────────────────────
section(pdf, "10.  Full Pipeline - Heuristic v5")

tbl(pdf,
    ["Phase", "Name", "What it does"],
    [
        ["1",   "Quantum SPS",
         "Maps jobs balancing e_m/p_i. Knows nothing about utility."],
        ["1b",  "Refine Mapping  (NEW)",
         "Rebalances UD(x) via doublet swaps. Preserves MU(x) and DBF."],
        ["2",   "Left Shift",
         "Diagnostic: confirms timing slack at f_max."],
        ["3",   "Energy Slack",
         "Checks if mandatory segments at f_max fit within budget B."],
        ["4",   "Freq. Scaling",
         "Attempts to lower frequency to save energy."],
        ["5",   "Greedy Optional",
         "Adds optional segments by utility density; checks DBF + energy."],
        ["6",   "Pairwise Swap",
         "Swaps low-value optional segs for high-value; fill pass after each."],
    ],
    [14, 42, BODY_W - 56])

callout(pdf,
    "WHY PHASE 1b HELPS PHASE 5.  Phase 5 can only schedule optional segments where "
    "timing slack exists. Slack on processor x is proportional to 1 - MU(x). "
    "If Phase 1b has spread high-UD jobs across processors while keeping MU(x) "
    "balanced, then (a) every processor has similar timing slack available, and "
    "(b) every processor has high-utility jobs ready to fill that slack. "
    "Phase 5 can exploit capacity on all processors instead of being blocked on "
    "the congested one and idle on the empty one.",
    color=(228, 248, 228), border_color=(50, 150, 50))

# ── 11. Worked Example ────────────────────────────────────────────────────────
section(pdf, "11.  Concrete Worked Example")

body(pdf, "2 processors, 4 tasks. All tasks have period p = 1, hyper-period h = 10.")

tbl(pdf,
    ["Task", "e_m", "p", "u_i", "e_opt", "mu(i)=e_m/p", "ud(i)=u*e_opt/p"],
    [
        ["T_A", "0.40", "1", "8", "0.50", "0.40", "4.00"],
        ["T_B", "0.30", "1", "7", "0.40", "0.30", "2.80"],
        ["T_C", "0.10", "1", "1", "0.30", "0.10", "0.30"],
        ["T_D", "0.10", "1", "1", "0.20", "0.10", "0.20"],
    ],
    [16, 13, 10, 12, 14, 30, 35])

subsec(pdf, "State after SPS (worst-case imbalanced outcome):")
body(pdf,
    "  P0 = {T_A, T_B}     MU(P0) = 0.70     UD(P0) = 6.80\n"
    "  P1 = {T_C, T_D}     MU(P1) = 0.20     UD(P1) = 0.50\n\n"
    "MU is imbalanced; SPS had limited choice in this small example. "
    "More critically, UD is catastrophically skewed: all valuable optional work "
    "is on P0, which has only 30% of its time free for optional segments.")

subsec(pdf, "Doublet pairs sorted by |ud(a) - ud(b)|:")
tbl(pdf,
    ["Pair", "|ud_a - ud_b|", "Same processor?", "Action in 2b"],
    [
        ["(T_C, T_D)", "0.10", "Yes (P1)", "Skip (same proc)"],
        ["(T_A, T_B)", "1.20", "Yes (P0)", "Skip (same proc)"],
        ["(T_B, T_C)", "2.50", "No",       "Candidate (T_B is hi_job on P0=P1)"],
        ["(T_B, T_D)", "2.60", "No",       "Candidate"],
        ["(T_A, T_C)", "3.70", "No",       "Candidate"],
        ["(T_A, T_D)", "3.80", "No",       "Candidate"],
    ],
    [28, 28, 35, BODY_W - 91])

subsec(pdf, "Step 2b trace:")
body(pdf,
    "Outer: P1 = P0 (UD=6.80). Scan doublets for first pair with hi_job on P0.\n\n"
    "Pair (T_B, T_C): T_B is hi_job (ud=2.8, on P0). T_C is lo_job (ud=0.3, on P1).\n\n"
    "Condition 1:\n"
    "  UD'(P0) = 6.80 - 2.80 + 0.30 = 4.30\n"
    "  UD'(P1) = 0.50 - 0.30 + 2.80 = 3.00\n"
    "  max(4.30, 3.00) = 4.30  <  6.80  -->  PASS\n\n"
    "Condition 2:\n"
    "  mu(T_B)=0.30, mu(T_C)=0.10\n"
    "  MU'(P0) = 0.70 - 0.30 + 0.10 = 0.50\n"
    "  MU'(P1) = 0.20 - 0.10 + 0.30 = 0.40\n"
    "  delta_new = |0.50 - 0.40| = 0.10  <  delta_cur = |0.70 - 0.20| = 0.50  -->  PASS\n\n"
    "Condition 3 (DBF): both processors feasible at mandatory load.  -->  PASS\n\n"
    "SWAP COMMITTED: T_B goes to P1, T_C goes to P0.\n\n"
    "New state:\n"
    "  P0 = {T_A, T_C}     MU(P0) = 0.50     UD(P0) = 4.30\n"
    "  P1 = {T_B, T_D}     MU(P1) = 0.40     UD(P1) = 3.00\n\n"
    "Re-identify P1 = P0 (UD=4.30). Next candidate: (T_A, T_D), T_A on P0.\n"
    "  UD'(P0) = 4.30-4.0+0.2 = 0.50     UD'(P1) = 3.0-0.2+4.0 = 6.80\n"
    "  max(0.50, 6.80) = 6.80  >=  4.30  -->  FAIL Condition 1. Rejected.\n\n"
    "No further valid swaps found. Algorithm terminates.\n"
    "Result: UD spread reduced from 6.30 to 1.30. MU spread reduced from 0.50 to 0.10. "
    "Phase 5 now sees balanced mandatory load AND balanced utility potential on both processors.")

# ── 12. Summary ───────────────────────────────────────────────────────────────
section(pdf, "12.  Summary")

bullets(pdf, [
    "SPS balances mandatory utilisation e_m/p_i (utilisation units, not raw "
    "execution time) because utilisation directly measures processor time fraction.",
    "Phase 1b (Refine Mapping) fixes SPS's blindness to utility by rebalancing "
    "ud(i) = u_i * (c[i][N_seg] - c[i][0]) / p_i across processors.",
    "Doublets (all job pairs sorted by ascending |ud_a - ud_b|) are the candidates "
    "for swapping. Each is considered a bounded number of times.",
    "Every swap must pass three conditions: UD improves (Condition 1), mandatory "
    "utilisation balance does not worsen (Condition 2), DBF remains feasible (Condition 3).",
    "v5a makes a single linear pass over all doublets (distributed, one scan). "
    "v5b iterates and always targets the globally most overloaded processor (greedy).",
    "The mandatory utilisation guard (Condition 2) was essential: without it, "
    "UD-focused swaps disrupted timing slack and reduced the utility Phase 5 could achieve.",
    "UD is the best cheap proxy for utility potential before scheduling, "
    "correctly combining reward rate u_i, optional volume e_opt, "
    "and task frequency 1/p_i in one number.",
])

pdf.output("c:/homogenous/heuristic_v5_report.pdf")
print("Done: c:/homogenous/heuristic_v5_report.pdf")
