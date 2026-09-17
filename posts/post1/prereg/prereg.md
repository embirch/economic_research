# Pre-registration · post1 (LL-07) · "Is AI delegated more on low-wage work or on high-wage work?"

**Date written.** 2026-09-17, before any primary test: before D, Δ_W, any quartile automation share,
the continuous slope, any H3 leg, any robustness re-estimate and any exploratory test.
**Committed as** `<git hash, filled by the director>`.

**Authority and scope.** `posts/post1/BRIEF.md` at `8fbffbd` (question, title, contribution and
hypotheses frozen at Gate 1b), `posts/post1/notes/feasibility.md` at `3ef51e9` including §7,
`posts/post1/notes/replication.md`, `posts/post1/notes/referee-brief-2.md` (its §(c) items P1–P9
are the list this document closes, and each is labelled below), `team/templates/PREREG.md` for the
section headings, and the `empirical-standards`, `economic-index-data` and `room-protocol` skills.
The brief's §9 rules are the confirmatory set; they are reproduced here, not redesigned. Where the
brief is silent, this document completes it, marks the completion, and reports the literal reading
beside the completed one. Three such completions exist and are named in place: the persistence of
the H3 leg rule (P4), the identified set for the within-group leg (P3(b)), and the declaration
probability of step (4) as against step (4)'s clause taken alone (P2). Nothing here alters a frozen
rule, a hypothesis, the question or the title.

**One script has been run before this commit,** and it loads no data:
`posts/post1/scripts/01_power_rules.py` (power of the decision rules from the standard errors the
steward has already published; check block passed). No other script exists yet.

---

## Disclosure: what has already been seen

### P8 · Exactly what has been seen, and by whom

Taken from `posts/post1/notes/replication.md` §5 and `posts/post1/notes/referee-brief-2.md` P8, plus
everything the analyst has seen while drafting this document.

**Seen by the data steward** (`feasibility.md` §1–§4, §7; `replication.md` §1–§3; outputs in
`data/replication/results/`):

- every C1–C10 row count, node set, threshold, floor, residual mass and merge audit; the analysis
  set (1,802 / 2,075 / 2,188 tasks; 97.15 / 96.23 / 96.52% of named mass; 818,673 / 854,432 /
  848,716 classified conversations) and its two audited losses (5 / 12 / 12 and 805 / 1,079 / 1,056
  tasks);
- the wage distribution: usage-weighted mean hourly wage per wave on both wage sources, the
  matched-window changes, the common-set uplift, four alternative aggregations, the **usage-weighted
  wage-quartile boundaries** ($25.78 / $35.79 / $43.40 Aug; $25.78 / $34.56 / $43.40 Nov; $24.00 /
  $34.40 / $43.40 Feb), and each quartile's task count, usage mass, **Kish effective N** and
  **classified conversation count**;
- automation shares **at wave or global level only**: 49.0980 / 51.0698, 45.3554 / 46.7394,
  44.1569 / 45.5456; the SC-netted November value 46.7394 → 45.4868; the §8(iii) internal check
  51.2001 / 47.0325 / 45.8966 (51.7424 with the `none` node); the March-2025 window's
  **43.2902** against its published 43.0619; and Figure 2.11's country regression (−3.111834,
  partial R² 0.393687, N 111);
- variance only, not level: the SEs and MDEs of the top-minus-bottom difference under the three
  variance models, the task-level standard deviation of the automation share by quartile (27–31 pp),
  and the Q1 / Q4 Kish N;
- the **use-case mix by wage quartile** (C9): work share Q1→Q4 32.60 / 48.69 / 42.05 / 61.91% (Nov)
  and 28.97 / 51.21 / 42.85 / 61.65% (Feb), with `personal` falling 44.67 → 23.91 and 56.40 → 29.17;
  the work-dominant set sizes (943 / 1,071 tasks) and the 29 / 21 `not_classified`-only tasks;
- the C8 Seychelles figures (24,715 conversations, 2.47181%; 23 tasks above 10% of their global
  count holding 11.594 pp of the wave of which **9.039 pp in Q4**; 14 tasks above 20% holding
  1.966 pp) and the top-10 concentration on both denominators.

The steward's scratch working tables `/tmp/p1/tk_{aug2025,nov2025,feb2026}.csv` carry **each task's
automation share beside its wage**. They were not aggregated by quartile in that session, they sit
outside the repository, and no output file in `data/replication/results/` contains a quartile
automation share or a value of D (`replication.md` §5).

**Seen by the referee** (`posts/post1/notes/rederivation/referee_brief_post1.py`,
`referee_brief2_post1_reverdict.py` and their outputs): the analysis set and the wage quartiles
rebuilt independently on an equal-split holder wage (boundaries agreeing with the steward's within
$0.31); the Q4 Kish N (13.8 / 11.7 / 19.0) and SE 0.151 / 0.149 / 0.151 pp; **the use-case mix by
wage quartile, computed twice** (32.77 / 48.38 / 41.81 / 61.95 Nov; 28.45 / 51.45 / 41.57 / 61.32
Feb) with the work-dominant set, its substantive-cell rival and the 35 flips per wave; every C9 and
C10 figure; SOC-15 at 77.1 / 75.7 / 69.9% of top-quartile mass and 39.86 / 37.12 / 33.11% of
analysis mass; the wage-weighted-minus-unweighted arithmetic (0.11–0.12 pp of Δ_W per point of gap;
8–9 pp of gap for a full point); the $24–26/hr bottom-quartile ceiling against ≈$22.9/hr and the
54–58% wage-mass figure; the 41³ grid partition of §9(1) and the three-wave power figures. The
referee states: "**No quartile automation share was computed**; the headline statistic remains
unseen by the referee" (`referee-brief-2.md`, opening).

**Seen by the programme lead:** everything quoted in the brief, which is the union of the two lists
above plus the published corpus.

**Seen by the analyst, drafting this document** (added here as the rule requires): the whole of
`BRIEF.md`, `feasibility.md`, `replication.md`, `referee-brief-2.md` and
`room/steward-2026-09-17-replication-post1.md` — hence every number listed above; and, from
`data/replication/results/post1_feasibility_checks.txt`, the printed SE and MDE lines
(lines 139, 160, 181, 183, 191–192, 204–205, 217–218) together with the C1–C4 and published-split
lines that surround them. Computed by the analyst: nothing from data. Script
`01_power_rules.py` takes the three published SEs as its only input and produces rule power,
80%-power thresholds, the 41³ partition counts and the MDE arithmetic.

**Nobody has computed, and nobody has seen:** D in any wave, on any wage rule, under any leg; Δ_W;
**any quartile's automation share**; the continuous wage slope; any H3 leg, including the SOC-15,
within-group, leave-one-group-out and work-dominant re-estimates; the permutation null; and any
exploratory test.

---

## Definitions, fixed

### 1 · Outcome

The **per-task automation share** p_i: for task *i* in a wave, (`directive` + `feedback loop`)
counts divided by the sum of the **five classified pattern** counts (`directive`, `feedback loop`,
`learning`, `task iteration`, `validation`) in `onet_task::collaboration` at `geography = 'global'`.
The `none` and `not_classified` **patterns** are excluded from the denominator, as Anthropic's
released `collaboration_task_regression` does, and the `none` share is printed beside every
automation share so the base is never implicit (BRIEF §9(1)). Units: percentage points.
n_i = the task's classified conversation count (the same denominator).

### 2 · The headline quantities

**D, per wave.** With usage weights w_i = `onet_task_pct` from the same wave's base `onet_task`
facet, and Q1 / Q4 the bottom and top usage-weighted wage quartile of the analysis set:

    D = Σ_{i∈Q4} (w_i / W_4) p_i  −  Σ_{i∈Q1} (w_i / W_1) p_i,      W_q = Σ_{i∈q} w_i

**Δ_W, per wave** (P1), on the whole analysis set, with wage_i in $/hr:

    Δ_W = Σ_i w_i·wage_i·p_i / Σ_i w_i·wage_i  −  Σ_i w_i·p_i / Σ_i w_i
        = Cov_w(wage, p) / E_w[wage]

the wage-weighted minus the unweighted usage-weighted automation share. The second form is the
second implementation (below). Δ_W is published with its own interval beside D. Its materiality
line is separate and higher than δ: 0.11–0.12 pp of Δ_W per point of gap, so a full point of Δ_W
needs a gap of roughly 8–9 pp (BRIEF §9(1)).

**The continuous companion.** The usage-weighted slope of p_i in the task's hourly wage, per
+$10/hr, in the form of Anthropic's own Opus gradient (2026-03, Fig. 2.2, p. 14); **sign and
significance only** (BRIEF §9(2)).

### 3 · Predictors and quartiles

The task's hourly wage: `MedianSalary` from `release_2025_02_10/wage_data.csv` (C6), joined on the
**full 10-character `O*NET-SOC Code` → `SOCcode`** (the key Anthropic's `plots.ipynb` cell 26 uses;
the `[:7]` prefix matches 0 of 775), filtered `MedianSalary > 100` **before** the join (this post's
choice, labelled as such, as is the ÷ 2080 hourly conversion), top-coded at $208,000 = $100.00/hr.
Task → O\*NET-SOC through C5 on the **lower-cased, stripped** task text, de-duplicated on that key
before the merge.

**Quartile boundaries** are drawn on **usage-weighted** wage over the analysis set of that wave, on
the primary wage rule, and are **kept fixed** from the full analysis set wherever a leg or a
robustness cut removes tasks (P3). Expected boundaries, from `feasibility.md` §4: $25.78 / $35.79 /
$43.40 (Aug), $25.78 / $34.56 / $43.40 (Nov), $24.00 / $34.40 / $43.40 (Feb).

**Standardisation: none.** Shares and differences are in percentage points, wages in dollars per
hour, the slope per +$10/hr. No variable is z-scored, residualised or rank-transformed except where
a rank statistic is named (Spearman for C6-versus-C7 agreement).

### 4 · Sample rule and exclusions, with the error type

#### P9 · Every sample and exclusion rule, listed once

| # | rule | status | reason | error type |
|---|---|---|---|---|
| S1 | **Analysis set** = named global task nodes with a C6 wage **and** at least one classified-pattern cell: 1,802 / 2,075 / 2,188 tasks, 97.15 / 96.23 / 96.52% of named mass | primary | the two things the estimator needs: a price and a rate | (a) below |
| S2 | Wave restricted to `geography == 'global'`, `level == '0'`, `platform_and_product` as in C1–C3; the three waves are **estimated separately and never pooled or spliced** | primary | intersections are global only (`ATLAS` §Cuts 10); no time dimension inside a release (§Cuts 7) | (a) |
| S3 | The **2,616 / 3,168 / 3,258 named** task nodes are the universe; the `none` and `not_classified` **base** nodes are dropped (8.13 / 6.49 / 7.03 pp of usage mass, not one node's worth) | primary | C4: the base facet has two residual nodes, the intersection one | (a) |
| X1 | **805 / 1,079 / 1,056** tasks with a wage and no classified cell — **dropped explicitly, never zeroed** (2.03 / 2.57 / 2.58 pp) | primary | absent ≠ zero (`ATLAS` §Traps 25); their rows are entirely `none`/`not_classified` | reported as dropped mass |
| X2 | **5 / 12 / 12** tasks with a classified cell and no wage — dropped, never zeroed (0.58 / 0.95 / 0.65 pp) | primary | no price, so no quartile | reported as dropped mass |
| X3 | Tasks with **fewer than 100 classified conversations** dropped and D re-estimated | sensitivity, threshold fixed here | small-cell noise; the figure is fixed so the pre-registration carries no free parameter (BRIEF §10) | (a) |
| X4 | **`SC` (Seychelles) netted out of the November task weights** (mean \|shift\| 0.0012 pp, max 0.5823 pp) | sensitivity | flagged unit, in the file and not in the report (`ATLAS` §Traps 14) | (a) |
| X5 | **Tasks where `SC` exceeds 10% of the global count dropped** (23 tasks, 11.594 pp of the wave, 9.039 pp of it in Q4), with the **>20% variant** beside it (14 tasks, 1.966 pp) | sensitivity, both pre-registered | the rates cannot be cleaned: `SC` has 0 intersection rows | (a) |
| X6 | November treated as **corroborated by August and February**, never as independent confirmation | primary reporting rule | X4–X5 cannot reach the rates | — |
| X7 | **The `none`-node variant**: the released spec keeps the `none` task node; D re-estimated with it kept | sensitivity | Anthropic's released code keeps it (`replication.md` §2(a)) | (a) |
| X8 | Leave-one-group-out: 22 major groups plus the **23rd group-spanning bucket**; and a leave-out of the **ten largest tasks** by usage mass (20.91% of Feb named mass; Aug 24.97%, Nov 25.93%) | robustness, descriptive | small effective N (Kish 89.5–134.3 against a nominal 2,616–3,258) | (a) and (b) |
| W1 | **Wage of a multi-holder task**: **employment-weighted mean over holder occupations** (BLS-EP `Employment 2025` on `occ_code`) — **primary**; **equal-split mean** and **modal holder** beside it in every table | three rules, primary named | Anthropic's rule is employment-and-time weighted and no time weight is public (2026-03, footnote 5 p. 11); exposure is 74 / 93 / 86 tasks, 4.44 / 5.98 / 4.87% of named mass, the two wages correlating 0.9998 | (a) |
| A1 | **Allocating usage mass to a group**: **equal split over distinct holder 2019 codes** — **primary**; modal-holder and employment-weighted beside it. Governs every *share* statistic | three rules, primary named | the released convention (`soc15_figA1_2026_03.py`); BRIEF §8 rule (iv) | (a) |
| A2 | **Each task in exactly one group** (for the SOC-15 exclusion, the within-group leg and the leave-one-group-out series): the **6 / 10 / 9** group-spanning tasks go to the holder with the largest BLS-EP employment, ties to the lexicographically smallest 10-character code; also reported as a 23rd bucket | primary | BRIEF §8 rule (iii), scope sentence of referee item 17 | (a) |
| V1 | **Vintage**: the wage is attached on the shipped **2010** O\*NET-SOC codes (the only taxonomy `wage_data.csv` joins to); **any occupational grouping** is reported on the **2019 recode** as primary with the 2010 grouping beside it (55 / 71 / 70 tasks change their major-group set) | primary | BRIEF §8; `posts/post2/notes/feasibility.md` §2 | (a) |
| E1 | Every load uses `keep_default_na=False, na_values=[]`; `cluster_name` split on the **last** `::`; `geography` filtered before any `geo_id` use | primary | `NA` is Namibia, `NONE` a real pseudo-geography (`ATLAS` §Traps 1, 2, 6) | — |

Exclusions are **drops, never zeros**, in every case; each script prints rows in, matched,
unmatched by name, and the dropped mass.

#### P1 · Error type, the interval formulas, and why

**(a) Primary — conversation-level binomial on the classified counts, task mix held fixed.** The
statement the post makes is about the conversations in these three windows, so the conversation is
the sampling unit and the task mix is fixed by construction. Each task contributes its own
p_i(1−p_i)/n_i, so the variance is **heteroskedastic by construction** across tasks — the
cross-section analogue the standards require. **No clustering is applied, and none is available:**
no release carries a user, account, session or any unit identifier, and the waves are never pooled,
so there is no cluster dimension and no panel (`ATLAS` §Traps 27b, §Cuts 7); the task enters as a
weight, not as a cluster of repeated observations. Conversations within a task are not known to be
independent — one user or one session may contribute several — and no identifier exists to correct
for it, so model (a)'s SE is a lower bound on the sampling variance of D under within-task
dependence and is stated as such wherever it appears. Intervals are **two-sided 95%**
(z = 1.959964); tests are **two-sided at 5%**; δ = 1 pp; MDE(80%) = 2.8 × SE.

Because Q1 and Q4 are **disjoint task sets** with disjoint conversation sets, their terms are
independent (P1) and

    Var(D) = Σ_{i∈Q4} (w_i/W_4)² p_i(1−p_i)/n_i  +  Σ_{i∈Q1} (w_i/W_1)² p_i(1−p_i)/n_i
    95% interval: D ± 1.959964 · √Var(D)

    Δ_W = Σ_i (a_i − b_i) p_i,   a_i = w_i·wage_i / Σ_j w_j·wage_j,   b_i = w_i / Σ_j w_j
    Var(Δ_W) = Σ_i (a_i − b_i)² p_i(1−p_i)/n_i
    95% interval: Δ_W ± 1.959964 · √Var(Δ_W)

with p_i on the 0–1 scale inside the variance and the result scaled to percentage points. Every
statistic in the confirmatory set (D, Δ_W, each leg, each retained fraction) is **linear in the
same vector of per-task shares**, so covariances are available in closed form:

    for L = Σ_i c_i p_i and M = Σ_i e_i p_i:   Cov(L, M) = Σ_i c_i e_i p_i(1−p_i)/n_i

which is how the retained-fraction intervals of P3 and P4 are formed.

**Per-wave SE of D** (P1), the steward's model (a) on the analysis set, `feasibility.md` §4 and
`replication.md` §3, produced by `data/replication/post1_variance_mde.py`:
**0.151 / 0.148 / 0.154 pp** (Aug / Nov / Feb), MDE(80%) **0.42 / 0.42 / 0.43 pp**. `BRIEF.md`
§9(4)'s parenthetical quotes the referee's independent 0.151 / 0.149 / 0.151 pp; the MDEs agree to
two decimals, so no rule moves. On the SEs printed to three decimals, 2.8 × 0.148 = 0.4144, which
rounds to 0.41 rather than to the steward's printed 0.42 — a printed-precision artefact, not a
discrepancy (any unrounded SE in [0.1482, 0.1518] prints 0.42). Script 03 recomputes SE to four
decimals and asserts MDE = 2.8 × SE.

**(b) Reported beside (a) as the generalisation bound, in no decision rule** — design-based:
resample **tasks** equal-probability and recompute the usage-weighted mean. SE 4.46 / 6.22 / 5.75 pp,
MDE **12.5 / 17.4 / 16.1 pp**. It resolves nothing below about twelve points *as a statement about
tasks*, because the Kish effective N on the `onet_task_pct` weights is **99.7 / 89.5 / 134.3**
against a nominal 2,616 / 3,168 / 3,258 and **11.5–16.5 tasks in Q4** on the primary wage rule
(13.8 / 11.7 / 19.0 on the referee's equal-split rule). The Kish N is printed beside the nominal
count throughout. Nothing is reported as "underpowered" for the within-window statement; the
generalisation to other task mixes is, and that sentence appears in every close (BRIEF §9(4), §12).

**(c) Not used.** The first brief's literal spec (resample tasks with p ∝ usage weight, unweighted
mean; MDE 3.26 / 3.44 / 3.68 pp) is recorded in `feasibility.md` §4 and is neither primary nor
reported, because its estimand is not the one §9(1) names.

### 5 · Frames, fixed

C1 `release_2025_09_15` (4–11 Aug 2025) · C2 `release_2026_01_15` (13–20 Nov 2025) · C3
`release_2026_03_24` (5–12 Feb 2026), each `onet_task::collaboration` at global with same-wave
`onet_task_pct` weights; C5 the O\*NET 20.1 statements; C6 the wage; C7 BLS-EP as the second wage
source (55.66 / 58.52 / 62.22% of named mass; Spearman with C6 0.9869 / 0.9859 / 0.9870 — **rank and
sign only, never a level**); C8 Seychelles; C9 `onet_task::use_case` (Nov and Feb only; 100%
coverage of the analysis set; **August is an absent facet, not an empty cut**, and `request::use_case`
is keyed to requests, not tasks, so there is no substitute); C10 the Feb–Mar 2025 per-task file
(P7 below).

**Replication first, and it is already done** (`replication.md` §2): the three published wave splits
on both bases (49.0980 / 51.0698, 45.3554 / 46.7394, 44.1569 / 45.5456); Figure 2.11 from
Anthropic's released library (−3.111834 / 0.393687 / N 111); the §8(iii) internal check returning
+0.1303 / +0.2931 / +0.3510 pp, positive in all three waves and inside 0.36 pp; and the **known
non-reproduction** of the task-value *level*, stated not attempted, with its four causes. Script 02
re-asserts all of these in its check block before any estimate is formed.

---

## Hypotheses and decision rules

The five owners of §9(1) are **H1, H2, O-A, H4, O-B**; H3 is a rival *explanation* of a declared
gradient, not a rival value of D. One size criterion serves all: **δ = 1 pp** on two-sided 95%
intervals. The ordered rule, **first match winning**, reproduced from BRIEF §9(1):

1. lower bound > **+1 pp** in all three waves → **H1**
2. upper bound < **−1 pp** in all three waves → **H2**
3. otherwise, every interval excluding zero with the same sign in all three → **O-A**
4. otherwise, every interval inside **±1 pp** in all three → **H4**
5. otherwise → **O-B**

Under H4 or O-B the legs are still computed and reported — the H4 close carries leg (a)'s number —
but **no H3 declaration is made**, and the post says so.

### P2 · The power of each rule, per rule and not per wave

`posts/post1/scripts/01_power_rules.py`, exact normal calculation and an independent Monte Carlo
(400,000 triples per point, seed 20260917; the two agree to 0.0007 on every owner). Assumptions,
stated: **independent waves, a constant true D across waves, the normal approximation at the stated
SE, two-sided 95% intervals**; because the per-wave SE varies 0.148–0.154 pp and the true D need not
be constant, every threshold is reported to **±0.05 pp**.

| rule | 80% power at a true \|D\| of | at true D = 1.0 pp | notes |
|---|---|---|---|
| **H1** (step 1), and **H2** by symmetry | **≈ 1.5 pp** (1.517 at the steward's SEs; 1.515 at the referee's; 1.514 at a flat 0.15) | **0.000** | 0.501 at 1.42 pp = δ + MDE |
| **O-A or stronger** (all three intervals signed and excluding zero) | **≈ 0.5 pp** (0.517 / 0.515 / 0.514) | 1.000 | 0.51 at the per-wave MDE of 0.42 pp |
| **H4**, step (4)'s clause alone (all three intervals inside ±1 pp) (the figure BRIEF §9(4) quotes) | **up to ≈ 0.5 pp** (0.483 / 0.485 / 0.486) | 0.000 | 0.133 at 0.70 pp |
| **H4 as declared** under the ordered rule (the clause *and* step 3 failing) | **up to ≈ 0.32 pp** (0.324 / 0.323 / 0.322) | 0.000 | 0.228 at 0.49 pp |

**The completion, marked.** Item 23 of `referee-brief-2.md` and BRIEF §9(4) state H4's power as
"up to about 0.5 pp"; that is the probability of step (4)'s **clause**, computed without the
precedence of step (3). Because step (3) fires first whenever all three intervals exclude zero with
one sign, the probability that H4 is **declared** is lower: 0.810 at a true D of 0.32 pp and 0.228
at 0.49 pp. Both figures are pre-registered and both are reported; the brief's figure is not
changed, and the post's H4 close carries the declared-power figure as well as the per-wave MDE.
Between roughly 0.3 and 1.5 pp the owner depends on the draw, and the post reports the three
intervals whatever the owner (BRIEF §9(4)).

The partition of §9(1) is re-checked mechanically in the same script: 68,921 point-estimate triples
on a 41³ grid at SE 0.15 pp, **each with exactly one owner**, all five reachable (H1 512, H2 512,
O-A 10,640, H4 3,125, O-B 54,132 — the O-A count matching the referee's), and the named problem
triples resolving as §9(1) says (+0.8 / +0.8 / −0.2 → O-B; +0.6 / +0.6 / −0.2 → H4; +0.6 / +0.6 /
+0.6 → O-A; +1.2 / +1.15 / +1.5 → O-A; +1.5 / +1.5 / +0.9 → O-A).

### H1 · Price gradient

- **Test.** D in each of the three waves, with its 95% interval under model (a).
- **Rule for support.** Step (1): the lower bound of D exceeds **+1 pp in all three waves**; **and**
  D keeps more than half its size, with the same sign, on **every composition leg testable in that
  wave** — legs (a) and (b) in all three waves, leg (e) in November and February only.
- **Rule against.** Any wave whose lower bound does not clear +1 pp (the outcome passes to H2, O-A,
  H4 or O-B by the same rule); losing more than half the size, or the sign, on a leg in every wave in
  which that leg is testable (H3 qualifies the declaration, P4); a leg firing in some waves only is
  reported with both readings' verdicts; a sign that disagrees between the two wage sources (P6).
- **Expected MDE.** Per wave 0.42 / 0.42 / 0.43 pp; the rule itself reaches 80% power at a true D of
  ≈ 1.5 pp and 0.000 at 1.0 pp (P2). A true D of exactly δ is therefore **not** detected by this
  rule at 80%, which the post states.
- **P6 · The second wage source under H1 / H2.** The C7 rebuild's point estimate carries the declared
  sign in all three waves, and its intervals are reported. If it does not, the owner is unchanged —
  the ordered rule runs on C6 — and the §12 H1 (H2) paragraph carries, in its first sentence, that
  the gradient is not corroborated on the second wage source in the wave(s) named, with C7's coverage
  (55.66 / 58.52 / 62.22% of named mass) stated as the reason it is not decisive; H3 is still
  evaluated.
- **Specification risks.** SOC-15 is 77.1 / 75.7 / 69.9% of top-quartile mass, so leg (a) removes
  most of Q4 by construction and its SE rises accordingly (the leave-one-group-out series is
  dominated by that one leave-out, which the post states); Q4's Kish effective N is 11.5–16.5 tasks,
  which is why no task-level statement is made; November's rates carry unremovable Seychelles
  contamination behind 9.039 pp of Q4 (X4–X6).

### H2 · Inverse gradient

- **Test.** As H1, and in addition the three augmentation shares (`learning`, `task iteration`,
  `validation`) by quartile, with the `none` and `not_classified` shares by quartile beside them.
- **Rule for support.** Step (2): the upper bound of D is below **−1 pp in all three waves**. The
  declaration rests on the interval alone.
- **Rule against.** Any wave whose upper bound does not fall below −1 pp; losing more than half the
  size, or the sign, on a leg in every wave in which it is testable (H3, P4).
- **Expected MDE.** As H1 by symmetry: 80% power at a true D of ≈ −1.5 pp.
- **P5 · What is written when step (2) fires and the augmentation clause fails.** The augmentation
  clause is not part of the declaration. If fewer than two of `learning`, `task iteration` and
  `validation` are weakly increasing across the four quartiles in a wave, H2 is still declared on
  the interval, and the §12 H2 sentence is written **without** the augmentation clause; the close
  then states, in the same paragraph, how many of the three patterns rose (0, 1 or 2 of 3, by wave),
  and reports the quartile `none` and `not_classified` shares, so that a negative D whose movement
  sits in the classified base rather than in the augmentation patterns is visible as such (BRIEF §6
  H2, "reported as such"). The count of rising patterns per wave and the quartile residual shares go
  into `results.json` whether or not H2 is declared.
- **Specification risks.** "Weakly increasing across quartiles" is a monotonicity statement on four
  points with no interval attached; it is therefore reported as description with each quartile
  share's own interval beside it and is in no decision rule.

### H3 · Composition, not price

Evaluated only when H1, H2 or O-A has been declared. Declared on legs **(a)**, **(b)** and **(e)**
alone (BRIEF §9(3)); leg (c) is descriptive under §10 and leg (d) is a reported mix.

**Estimand of each leg, and the retained fraction.** For a leg L with estimate D_L in a wave, the
retained fraction is r_L = D_L / D on the same wave's headline D. Because D and every D_L are linear
in the same per-task shares, Var(D_L), Cov(D_L, D) and hence a 95% interval for r_L (delta method)
and for the contrast **D_L − ½D** are available in closed form from the covariance formula above.
**The declaration is made on the point estimates, as §9(3) writes it** (a leg fires in a wave if
sign(D_L) ≠ sign(D) **or** \|D_L\| < ½\|D\|); the interval for D_L − ½D and the interval for r_L are
reported beside every leg so that a leg firing on a point estimate whose interval straddles ½D is
visible as such.

#### P3 · Leg mechanics

**(a) SOC-15 excluded.** Computer and Mathematical (`soc_major_group` 15) tasks are removed from the
analysis set; **the quartile boundaries are kept from the full analysis set and are not re-drawn**;
a **group-spanning task is excluded if and only if rule A2 assigns it to SOC-15**. Removes 39.86 /
37.12 / 33.11% of analysis mass and 77.1 / 75.7 / 69.9% of top-quartile mass. Grouping is on the
2019 recode as primary with the 2010 grouping beside it (V1). Testable in all three waves.

**(b) Within SOC major group.** For each major group g that contains at least one analysis-set task
in the **global** Q1 **and** at least one in the **global** Q4 (boundaries kept, not re-drawn;
each task in exactly one group by A2), the within-group difference is

    D_g = Σ_{i∈g∩Q4} (w_i/W_{g,4}) p_i − Σ_{i∈g∩Q1} (w_i/W_{g,1}) p_i

and the leg estimate is the **usage-weighted average over those groups**, each group weighted by its
analysis-set usage mass in the two extreme quartiles, W_{g,1} + W_{g,4}:

    D_(b) = Σ_g (W_{g,1}+W_{g,4}) D_g / Σ_g (W_{g,1}+W_{g,4})

Groups that do not contain both are **reported as not identified, never as zeros**.
*The completion, marked:* `feasibility.md` §4 gives **10 / 10 / 8** groups containing tasks in both
the global bottom and top quartile and **7 / 8 / 6** spanning all four, and BRIEF §9(3)(b) names the
first condition in words and the second count in its parenthesis. The estimand needs only Q1 and Q4,
so the **primary identified set is the 10 / 10 / 8 groups**, with the **7 / 8 / 6 all-four subset
reported beside it** in every table; both go into `results.json`. If the two readings disagree on
whether the leg fires, both are reported and the notebook records it.
*How "half of D" is judged against a differently defined estimand:* D_(b) and D are different
estimands — D_(b) holds the group mix fixed and averages within-group contrasts, D does not — so the
comparison is made on the **ratio r_(b) = D_(b)/D** against ½ exactly as §9(3) writes it, and
**three things are reported beside it**: the interval for r_(b), the interval for D_(b) − ½D, and
the share of analysis-set Q1+Q4 mass the identified groups carry (so that a small r_(b) driven by
non-identification rather than by composition is visible). Testable in all three waves.

**(e) Work-dominant tasks.** A task's **work share** = its `work` count ÷ **the sum of all published
`use_case` cells for that task, including `not_classified` (and `none` in February)** — the cells
partition `onet_task_count` exactly, so this is a share of the node and is **not** renormalised over
substantive cells (`ATLAS` log (j) 2; `feasibility.md` §7). The work-dominant set is
**work share ≥ 0.50**, fixed here: **943 tasks, 48.9382 pp of the wave = 54.38% of analysis-set mass**
(Nov) and **1,071 tasks, 47.4364 pp = 52.86%** (Feb). **Quartile boundaries are kept from the full
analysis set, not re-drawn.** The **29 (Nov) / 21 (Feb)** analysis-set tasks whose only published
cell is `not_classified` (0.0779 / 0.0527 pp) have an undefined work share and are **dropped by this
rule, never scored 0**; the dropped count and mass are printed. The substantive-cell denominator
(978 / 1,106 tasks; **35 tasks flip in each wave**) is reported as the pre-registered sensitivity.
Leg (e) also enters the continuous companion as the task's **work share as a covariate**.
**August is untestable on legs (d) and (e)**: no facet name in the August file contains `use_case`,
and there is no substitute; for August the work-mix rival is asserted, not tested, and H1's
signature there is judged on legs **(a) and (b) only** (P5).

**(d) Use-case mix beside each quartile's share.** Each wage quartile's work / personal / coursework
mix reported beside its automation share, November and February; description, in no decision rule.
The mix has a real gradient in this data (work share Q1→Q4 32.60 → 61.91% Nov, 28.97 → 61.65% Feb),
which is the reason to run leg (e).

**(c) Leave-one-group-out.** 22 re-estimates plus the 23rd group-spanning bucket, reported under
§10 as description; the SOC-15 leave-out dominates by construction and the post says so.

#### P4 · Persistence of the H3 legs, and how the leg tests are counted

**Eight leg tests are run:** leg (a) in three waves, leg (b) in three waves, leg (e) in two
(November and February) — 3 + 3 + 2 = 8.

*The completion, marked.* §9(3) says H3 is declared if D loses more than half its size, or its sign,
"on at least one of (a), (b) and (e)" and does not say in how many waves. BRIEF §6 does not settle
it: §6 H3's "against it" (D keeping half its size on all three legs in all three waves) and §6 H1's
"against it" (losing on any composition leg) are both complements of the any-wave reading. The
persistent-leg rule is nevertheless primary, for a reason of specification rather than of text: on
point estimates at these SEs the any-wave reading declares H3 with no composition present in roughly
60 / 50 / 27 / 12% of declared gradients at a true D of 0.5 / 0.6 / 0.8 / 1.0 pp, whereas the
persistent-leg rule does so in at most 1–2% at any D
(`posts/post1/notes/rederivation/referee_prereg_post1.py` §C, covariance model stated there). A rule
that fires under the null in a quarter to two-thirds of cases in the O-A range is not a test, so the
literal reading is reported beside the primary rather than used as it. Mirroring §9(1)'s
all-three-waves persistence for D:

- **Primary (the persistent-leg rule).** H3 is declared if **at least one leg fires in every wave in
  which that leg is testable** — legs (a) and (b) in all three waves, leg (e) in both waves in which
  it exists. A leg that fires in one wave and not another does not declare H3.
- **Reported beside it (the literal reading).** The any-wave rule: at least one leg firing in at
  least one wave. Both verdicts are reported, in the same table, whether or not they agree; where
  they disagree, the post reports the persistent-leg verdict as the pre-registered one and states
  the literal reading's verdict in the same sentence, and the notebook records the disagreement.

**How the leg-test count is reported.** One table, in the post and in `results.json`, with one row
per leg-wave (eight rows): leg, wave, D, D_L, r_L = D_L/D, the 95% interval for D_L, the interval
for r_L, the interval for D_L − ½D, the MDE for D_L, N (tasks and classified conversations), the
retained mass, and a **fired / did not fire** flag. The headline count is reported as
**"k of 8 leg tests fired"** with its denominators named (legs (a) and (b) out of 3 waves each, leg
(e) out of 2), together with the per-leg persistence counts ("leg (a) fired in j of 3 waves"), so the
count is never read as a single test.

- **Rule for support (H3).** As above, when H1, H2 or O-A has been declared (a declaration spans the
  three waves).
- **Rule against (H3).** No leg fires in every wave in which it is testable — the complement of the
  support rule, so every declared gradient is either H3-qualified or not. The strongest form, D
  keeping more than half its size and its sign on all three legs in every wave and across all 22
  leave-one-group-out re-estimates, is BRIEF §6 H3's "against it" and is reported as such when it
  obtains; a leg firing in some waves but not all is "not declared" and is reported with the literal
  reading's verdict in the same sentence (above).
- **Expected MDE.** Each leg's MDE is 2.8 × SE(D_L) computed by the same formula on the leg's own
  sub-sample and **printed beside every leg estimate**, together with the MDE for the contrast
  D_L − ½D. A pre-commit expectation, from the mass each leg removes: leg (a) removes 70–77% of
  top-quartile mass, so SE(D_(a)) is expected to be roughly 1.3–2.0 × SE(D) (MDE ≈ 0.55–0.85 pp);
  leg (e) retains 53–54% of analysis mass (MDE expected ≈ 0.55–0.65 pp); leg (b)'s SE depends on the
  identified groups' mass and is expected to be the widest of the three. These are expectations, not
  results: the pre-registered commitment is that the MDE is computed on the same variance model and
  printed beside every leg, and that a leg which does not fire is reported as "nothing bigger than
  the MDE" rather than as a confirmation.
- **Power of the H3 rule, per rule and not per leg** (referee's re-derivation,
  `posts/post1/notes/rederivation/referee_prereg_post1.py` §C; covariance model: Var(A1) = Var(A4) =
  ½Var(D); a leg's quartile mean has variance Var(A_q)/f_q for retained mass fraction f_q and
  covariance Var(A_q) with the full mean; leg (a) f4 = 0.229 / 0.243 / 0.301, f1 = 1; leg (e)
  f1 = 0.35, f4 = 0.65; leg (b) SE ratio 2.0; constant true D; conditional on a declared positive
  gradient; thresholds approximate to about ±0.05). Expected SE(D_(a)) ≈ 0.23–0.25 pp,
  corr(D, D_(a)) ≈ 0.6–0.7, SE(D_(a) − ½D) ≈ 0.18–0.21 pp. Under the persistent-leg rule, false
  declaration of H3 with no composition present ≤ 0.01–0.02 at every true D; power to declare H3
  when one leg truly loses three-quarters of D — leg (a): 0.37 / 0.46 / 0.60 / 0.72 / 0.92 at a true
  D of 0.5 / 0.6 / 0.8 / 1.0 / 1.5 pp; leg (e), two waves: 0.54 / 0.63 / 0.75 / 0.84 / 0.96;
  leg (b): 0.29 / 0.35 / 0.45 / 0.55 / 0.77. At the boundary (a leg truly retaining exactly half)
  each wave fires with probability ½ and the persistent rule with ⅛. Under the literal any-wave
  reading the false-declaration rate is 0.60 / 0.49 / 0.27 / 0.12 / 0.01 at the same true D.
  Consequence, fixed now: in the O-A range an H3 non-declaration is "nothing shown", not composition
  excluded; the post's sentence for that case is in the Interpretation table. Script 04 or 01 may
  reproduce these figures on the same model with a ±0.03 tolerance; the pre-registered commitment is
  the realised SE, MDE and D_L − ½D interval printed beside every leg.
- **Specification risks.** Leg (a) and the leave-one-group-out series are not independent evidence
  (SOC-15 dominates both); r_L is a ratio of two correlated estimates, which is why its interval is
  formed from the exact covariance rather than by treating D and D_L as independent; leg (b)'s
  estimand differs from D's, which is why the identified mass is reported beside it.

### H4 · No relation at the stated margin

- **Test.** D and its interval in each of the three waves.
- **Rule for support.** Step (4): every interval **inside ±1 pp** in all three waves, **and** the
  three intervals not all excluding zero with one sign (that second clause is step (3)'s precedence
  and is what separates H4 from O-A).
- **Rule against.** Three same-signed intervals excluding zero (O-A, or H1/H2 if they clear the
  margin); any wave whose interval leaves ±1 pp (O-B, or H1/H2).
- **Expected MDE.** Per wave 0.42 / 0.42 / 0.43 pp — "nothing bigger than about four tenths of a
  point" is the null's content **for these windows' conversations**. The rule is declared with 80%
  probability at a true \|D\| up to ≈ 0.32 pp (step (4)'s clause alone: ≈ 0.49 pp). As a statement
  about tasks in general the design-based MDE is 12.5 / 17.4 / 16.1 pp and nothing below about twelve
  points is resolved; that sentence appears in the close.
- **P6 · The second wage source under H4.** The C7 rebuild's interval must **also lie inside ±1 pp
  in all three waves**. If it does not, the null is reported as not corroborated on the second
  source, with C7's coverage (55.66 / 58.52 / 62.22% of named mass) stated as the reason it is not
  decisive.
- **Specification risks.** A null on a quantity whose design-based bound is 12–17 pp must not be read
  as a null about tasks; the Kish N is printed beside every count for that reason.

### O-A · A persistent gradient not shown to clear the margin in every window

- **Test.** As H1.
- **Rule for support.** Step (3): every interval excludes zero with the same sign in all three waves,
  and step (1) and step (2) have failed. Some or all point estimates may exceed ±1 pp (referee item
  14): O-A means "not shown to clear the margin in every window", never "smaller than a point".
- **Rule against.** Any wave whose interval contains zero, or a sign that disagrees across waves
  (O-B); all three lower bounds clearing +1 pp or all three upper bounds below −1 pp (H1 / H2).
- **Expected MDE.** O-A or stronger reaches 80% from ≈ 0.5 pp; O-A as declared is ≈ 1.00 near 1.0 pp
  and yields to H1 above ≈ 1.4 pp. Per-wave MDE 0.42 / 0.42 / 0.43 pp.
- **P6 · The second wage source under O-A.** Sign agreement: the C7 rebuild's point estimate carries
  the declared sign in **all three waves**, and its intervals are reported. If C7's point estimate
  carries the opposite sign in any wave, the owner is unchanged and the O-A paragraph carries, in its
  first sentence, that the direction is not corroborated on the second wage source in that wave, with
  C7's coverage stated.

### O-B · No persistent gradient

- **Test.** As H1.
- **Rule for support.** Step (5): none of steps (1)–(4) holds — signs disagreeing across waves, or
  one wave past the margin while another does not resolve (the +0.8 / +0.8 / −0.2 pp case).
- **Rule against.** Any of steps (1)–(4).
- **Expected MDE.** O-B is the residual of the ordered rule and carries no MDE of its own; the three
  per-wave MDEs (0.42 / 0.42 / 0.43 pp) and the three intervals are what the post reports, plus the
  probability that the ordered rule lands on O-B at the relevant true values (0.043 at 0.5 pp, 0.008
  at 0.7 pp, 0.000 at 1.0 pp — `01_power_rules.py`).
- **P6 · The second wage source under O-B.** The C7 rebuild is **reported** — three estimates with
  intervals — and no sign agreement is required, because the claim being made is the absence of a
  stable sign. Where C6 and C7 disagree on the sign in a wave, the disagreement is itself reported as
  part of the O-B finding.

### The confirmatory set, named and counted

| # | quantity | per wave | waves | estimates |
|---|---|---|---|---|
| 1 | **D** | 1 | 3 | 3 |
| 2 | **Δ_W** | 1 | 3 | 3 |
| 3 | The continuous slope per +$10/hr (sign and significance only; in no decision rule) | 1 | 3 | 3 |
| 4 | **Leg (a)** D with SOC-15 excluded | 1 | 3 | 3 |
| 5 | **Leg (b)** within-group D | 1 | 3 | 3 |
| 6 | **Leg (e)** D on work-dominant tasks | 1 | 2 | 2 |
| | **total confirmatory estimates** | | | **17**, of which **8** are the leg tests of P4 |

Reported beside them, in no decision rule: each quartile's automation share with its `none` and
`not_classified` shares (4 per wave), leg (c)'s 22 + 1 leave-one-group-out re-estimates, leg (d)'s
quartile use-case mixes (Nov, Feb), the continuous slope with the task's work share as a covariate
(§9(3)(e); Nov and Feb), with the usage-weighted pairwise correlation and VIF of wage and work share
printed beside it, since the two predictors compete, and every robustness cut listed below.

### P6 · Two implementations of every confirmatory quantity

Every number in the table above is produced twice, by two named code paths in two scripts, and the
check block of the second fails if they disagree beyond the stated tolerance. The C7 rebuild is a
**second data source**, not a second implementation, and is reported separately as above.

| quantity | primary implementation (script 03 / 05) | second, independent implementation (script 04) | agreement required |
|---|---|---|---|
| p_i, per-task share | from `onet_task_collaboration_count` rows, five classified patterns | from `onet_task_collaboration_pct` rows renormalised over the same five patterns | 1e-6 pp, or the published `_pct` rounding stated as the cause and 0.01 pp enforced |
| weights w_i | `onet_task_pct` | `onet_task_count` renormalised over the analysis set | 1e-9 |
| the wage join | task side: task text → C5 → 10-char code → C6 | SOC side: C6 → C5 pivoted to holder sets → task text | identical task→wage map, 0 differences; merge audits printed both ways |
| **D** | weighted-difference form, quartile masks | pooled form Σ_i c_i p_i with c_i assembled independently from the masks | 1e-9 pp |
| **Δ_W** | Σ w·wage·p / Σ w·wage − Σ w·p / Σ w | Cov_w(wage, p) / E_w[wage] | 1e-9 pp |
| **slope** | weighted least squares of p on wage/10 | weighted covariance ÷ weighted variance, and `statsmodels` WLS as a third read | 1e-8 |
| **legs (a), (b), (e)** | as defined above | the same estimands rebuilt on the second code path for p_i, w_i and the wage join | 1e-6 pp |
| **Var, intervals, MDE** | closed form above | numerical: parametric bootstrap drawing n_i·p_i ~ Binomial(n_i, p_i) per task, 10,000 draws, seeded | SE agreement to 2%; interval coverage 95% ± 0.5 pp |
| the retained fractions r_L | delta method on the closed-form covariance | the same parametric bootstrap | SE agreement to 2% |

### Synthetic-data recovery, one per estimator the post relies on (script 04)

Each test builds a synthetic task table with known p_i, n_i, w_i and wage_i, runs the estimator
unchanged, and asserts recovery; each also runs the zero-effect case and asserts that zero is
returned and covered.

1. **D** — a known quartile gap implanted (0, 0.5, 1, 3 pp): recovered within 3 × the analytic SE,
   and the zero case's interval covers zero; coverage over 2,000 replications 95% ± 1 pp.
2. **Δ_W** — a wage-linear p implanted so Δ_W is known in closed form: recovered to 1e-9.
3. **The continuous slope** — a known slope per +$10/hr: recovered to 1e-8 under exact weights; sign
   correct in 95%+ of noisy replications at the implanted size.
4. **The within-group average (leg (b))** — groups with known within-group gaps and a
   between-group wage gradient: the estimator returns the implanted within-group average and **not**
   the total gap, which is the property the leg is run for; non-identified groups are reported as
   such and never as zeros.
5. **The work-dominant restriction (leg (e))** — synthetic `use_case` cells including
   `not_classified`-only tasks: the threshold selects the implanted set, the `not_classified`-only
   tasks are dropped rather than scored 0, and the substantive-cell denominator reproduces the
   implanted flips.
6. **The design-based task bootstrap** — a known task-level dispersion: SE recovered to 5%, and the
   MDE reproducing 2.8 × SE.
7. **The permutation null** — under a zero gradient the permutation test rejects at 5.0% ± 1 pp
   (size), and at an implanted gradient of the order of the design-based MDE it rejects more often
   than 5%.
8. **The Kish effective N** — an analytic case (two weight values) recovered exactly.

**Outcome rubric, structural.** Every script ends in a check block that asserts known facts and
raises; nothing downstream runs on a failed check. Script 02 asserts the published wave splits, the
Figure 2.11 triple, the merge audits, the analysis-set counts and masses, the quartile boundaries and
the Kish N; script 03 asserts the SE and MDE against `feasibility.md` §4 and the second
implementation's agreement; script 04 asserts every recovery above; script 05 asserts the leg
coverage counts (943 / 1,071 work-dominant tasks; 29 / 21 dropped; SOC-15 mass shares; the identified
group counts); script 06 the Seychelles and concentration figures; script 07 the C10 figures of P7;
script 09 that every number in the post appears in `results.json` with its script.

**Plot before modelling** (script 02): per-task histograms of p_i, n_i and w_i; a scatter of p_i
against wage with the usage weight as the point size; the wage distribution with the quartile
boundaries drawn — so that a coding error shows as a shape before any estimate is formed.

---

## Robustness, fixed now

Nothing is added later without a dated deviation in `posts/post1/notes/lab-notebook.md`.

1. **Persistence across windows, inside the confirmatory rule.** Three waves, estimated and reported
   separately, never pooled or spliced. November is corroborated by August and February rather than
   treated as independent confirmation (X6).
2. **P7 · The fourth window (C10), design-based only and outside the confirmatory set.**
   `release_2025_03_27/automation_vs_augmentation_by_task.csv` (Feb–Mar 2025), 3,364 × 7, flat and
   global. The per-task automation share is **(`directive` + `feedback_loop`) renormalised over the
   five classified ratios, i.e. over 1 − `filtered`**; weights are `task_pct_v2` (3,365 rows in,
   3,364 matched, the one unmatched being `none`; 98.2183 of 100 `pct` carried, 90.1561 after the
   (1 − `filtered`) weighting). There are **no counts**, so **no conversation-level interval exists**
   in this window and only the design-based (task-resampling) interval is reported. The
   **1,066 rows at `filtered` = 1.0** — **179 / 251 / 286 of the matched analysis-set tasks** — are
   **dropped, never zeroed**, and the dropped count and mass are printed. There is **no task-level
   `none` share**: `filtered` is 8.0623 pp of the task base against a global `none` of 3.2389, so it
   is `none` plus about 4.8 pp of unpublished exclusions and cannot be decomposed; §9(1)'s
   `none`-beside-every-share rule therefore holds **at the global level only** in this window, and
   that is stated wherever the window appears. On this base the usage-weighted global automation
   share is **43.2902%** against the release's published **43.0619%** — a **0.23 pp gap**, the same
   "not a strict decomposition" gap recorded in `data/releases/release_2025_03_27.md` §Metrics and
   the analogue of §8(iii)'s +0.13 / +0.29 / +0.35 pp; it is reported wherever a C10 number is.
   The window reaches **1,635 / 1,843 / 1,904** of the 1,802 / 2,075 / 2,188 analysis-set tasks
   (98.78 / 98.49 / 98.08% of their mass) and the task list is **not a panel**, so entry and exit are
   not random. No column in the release is named `collaboration`; the five underscored pattern
   columns are the split. **This window is in no decision rule and cannot declare or refute an
   owner**; it is a design-based bound on whether the gradient's sign predates the three long waves.
3. **Leave-one-out.** 22 leave-one-group-out re-estimates plus the 23rd group-spanning bucket
   (confirmatory under H3 as leg (c), reported as description), and a leave-out of the ten largest
   tasks by usage mass (19.4410 pp of the February wave = 20.9107% of named mass; Aug 22.9409 /
   24.9703%, Nov 24.2471 / 25.9288%) — the denominator stated each time. Movers named.
4. **Flagged units.** X4, X5 and X6 above: the weight-netted November re-estimate; the `SC` > 10%
   drop (23 tasks, 11.594 pp, of which 9.039 pp in Q4) with the > 20% variant (14 tasks, 1.966 pp)
   beside it. Utah's August anomaly is a `state_us` row and cannot move a global intersection.
5. **Low-count sensitivity.** X3: drop tasks with fewer than 100 classified conversations. A per-cell
   floor rule would be inert (the intersection's minimum published count is 1 and the 1–59 values are
   the folded residual), and the post says so.
6. **The `none`-node variant.** X7: D re-estimated with the `none` task node kept, as Anthropic's
   released code does (which raises the August global figure to 51.7424).
7. **Wage rules and allocation rules.** D, Δ_W and every leg re-estimated under the three wage rules
   (W1) and the three allocation rules (A1), with the primary named; the ≤ 0.17–0.18 pp bound from
   the shortlist work is a bound on a **share** and is **not** a bound on this gradient, which is why
   the gradient is re-estimated under each rule rather than bounded.
8. **Second wage source.** The C7 rebuild of D, Δ_W and every leg, with sign agreement defined per
   owner (P6) and the wage join re-run from the task side and the SOC side as two builds.
9. **Placebo.** A permutation null: the wage vector permuted across tasks **within** SOC major group
   and the estimator re-run, 10,000 permutations, seeded. Reported here as **the task-level bound it
   is** — its band is of the order of the design-based MDE, 12.5–17.4 pp, because Q4 holds 11.5–16.5
   effective tasks. **It is in no decision rule.**
10. **Country mix inside a task — named and not testable.** Intersections are global only, so a
    per-task rate cannot be cleaned of its country blend and no reverse construction is identified
    (only ≈71.43% of a wave's SOC-15 mass is recoverable from country rows, `ATLAS` log (k) 4). It is
    raised first in the post's limitations, not claimed as closed.
11. **The generalisation sentence.** Model (b)'s bound (MDE 12.5 / 17.4 / 16.1 pp) is reported beside
    every headline number, and the sentence that a claim about work in general is not licensed appears
    in every close.

**Exploratory allowance — three tests, after the confirmatory set, none in the headline, each
labelled exploratory** (BRIEF §9): (a) the same gradient on the **1P API** global intersection
(11,660 rows at global in the February file; the API is automation-dominant and its February sample
includes Claude Code, so it is context, not a replication); (b) the **pattern-level split** — which
of `directive` and `feedback loop` carries a positive gradient and whether `learning`,
`task iteration` and `validation` move the other way; (c) the gradient against **`JobZone`** (99.22 /
98.83 / 99.06% of named mass with the 119 `-1` sentinel occupations dropped). **No further tests; any
additional cut is a logged deviation.**

**Named as not run** (BRIEF §7(2), §10): the wage × human-time version of the outcome
(`onet_task::human_only_time` exists at global in two of three waves and not in August, is a bucketed
estimate rather than hours worked, and would import an unconfirmed construct mapping); any wage
**level** reported as Anthropic's; any geographic version of this post; any task-level claim below the
design-based bound.

---

## Interpretation, fixed now

Each owner's reading is fixed before it is known, and is the corresponding paragraph of `BRIEF.md`
§12. No new claim is introduced here; the mapping is the whole of the commitment.

| declared owner (§9(1)) | §12 paragraph that is written | what it may say | what it may not say |
|---|---|---|---|
| **H1** (step 1) | "If H1 holds (a gradient above the margin, upward)" | in each of the three windows, conversations on top-quartile tasks were delegated at a rate more than a point above those on bottom-quartile tasks; the leg (a) number in the headline sentence; Δ_W beside it as the nearer of the two published numbers to what a model of labour payments weights by — **an hourly rate, not a bill** | that the difference is a bill; that it generalises to work in general (the design-based bound is stated in the same paragraph) |
| **H2** (step 2) | "If H2 holds (a gradient above the margin, downward)" | the same, downward, with the augmentation clause **only if** at least two of the three augmentation shares rose (P5); Anthropic's own conditional reading named as Anthropic's and tested here | that the augmentation pattern holds when it did not; generality beyond these windows |
| **O-A** (step 3) | "If O-A holds (a persistent gradient not shown to clear the margin in every window)" | that delegation does track the wage of the work, in the direction stated and in all three windows, D of X, Y and Z points, without the interval clearing a full point in every window; that the correction is roughly a tenth of a point per point of gap, so the direction is the finding and the correction is not a repair | that the gradient is smaller than a point (it may exceed it); "by the wage bill" |
| **H4** (step 4) | "If H4 holds (the null, at the stated margin)" | that the two quartiles differed by less than one percentage point, and by X with Computer & Mathematical tasks excluded, at an MDE of 0.42–0.43 pp **on these windows' conversations**; a second null beside Anthropic's null for the education level of the prompt; that for weighting purposes an unweighted automation share is, in these windows, the right number after all | that the SOC-15-excluded difference is smaller (it is not constrained to be); a null about tasks in general (nothing below about twelve points is resolved) |
| **O-B** (step 5) | "If O-B holds (no persistent gradient)" | that the gradient is not a stable feature of these three windows; what a longer released series would settle | a sign; a magnitude claim for any single wave read as the finding |
| **H3 declared** (legs, after H1, H2 or O-A) | "If H3 holds (composition, not price)" — **qualifying** the declared owner's paragraph, not replacing it | that the relation is carried by a mix travelling with wage — coding, or use case, with the leg that fired named and its retained fraction given; that anyone weighting an automation share by wage must know which | that the price mechanism is refuted; a use-case claim for August, where the leg is untestable |
| **H3 not declared, or not evaluated (H4 / O-B)** | the owner's paragraph, plus one sentence | that the legs were computed and reported and that no H3 declaration is made; where the owner is O-A, that the pre-registered rule detects a three-quarters loss on a single leg with a probability of roughly 0.4–0.7 at a true D of 0.5–1.0 pp, so non-declaration is nothing shown, not composition excluded | an H3 declaration under H4 or O-B; that composition has been ruled out |

The post's body says **"the wage of the work"**, never "cheap" or "expensive"; low-wage and high-wage
mean the bottom and top usage-weighted wage quartile of the tasks brought to Claude, defined in the
first paragraph, and low-wage is relative to that mix and not to the economy. "Delegated" is
Anthropic's automation share — directive and feedback-loop conversations; "outright" describes
directive alone and belongs to the exploratory pattern-level split. Every finding sentence says
Claude or Claude.ai; the question says AI.

**What no outcome may be read as.** A count of tasks automated; a measure of AI autonomy; a
measurement of displaced labour; a statement about the wage **bill**; a statement about work in
general; a statement about any country, since the per-task rate is a usage-weighted blend over
countries that cannot be cleaned at this grain.

---

## Deviations

Every deviation from this document is logged in `posts/post1/notes/lab-notebook.md` with its date and
reason, and the **pre-registered rule and the corrected one are both run and both reported** if a
rule proves mis-specified. The three places where this document completes a rule the brief leaves
open — the H3 persistence rule (P4), the within-group identified set (P3(b)) and the declared-power
figure for step (4) (P2) — are marked in place, and in each the literal reading is reported beside
the completed one, so that a referee can see both. Any additional cut beyond the confirmatory set and
the three named exploratory tests is a logged deviation.

**Scripts, in order** (each numbered, each with a docstring that says what and why, each ending in a
check block): `01_power_rules.py` (run before this commit; loads no data) · `02_build.py` (frames,
joins, merge audits, analysis set, quartiles, plots, replication assertions) · `03_headline.py` (D,
Δ_W, the slope, intervals, MDEs) · `04_second_implementation.py` (the second code path for every
confirmatory quantity, the parametric bootstrap, and the synthetic recovery tests) ·
`05_legs.py` (H3 legs (a)–(e), retained fractions with covariances, the eight-row leg table) ·
`06_robustness.py` (X3–X8, W1, A1, the permutation null, C7) · `07_fourth_window.py` (C10) ·
`08_exploratory.py` (the three named exploratory tests) · `09_results_and_figures.py`
(`data/processed/results.json`, `outputs/figures/*.png`, `figures.json`, and the verification that
nothing may appear in the post that is not in `results.json`).
