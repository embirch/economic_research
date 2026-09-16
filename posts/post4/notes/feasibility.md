# post4 (LL-09) · feasibility — data steward, 2026-09-16

Against `posts/post4/BRIEF.md` (commit 008d762, question frozen: *Does AI's self-assessed success
rate predict which work people keep bringing to it?*) and the lead's request in
`room/lead-2026-09-16-brief-post4-status.md`.

Everything below was re-derived today from the cache, in this sandbox, at Hugging Face revision
`2ea58ff`. Nothing is asserted from `data/ATLAS.md` alone. The single script that produces every
number is **`data/replication/post4_feasibility_checks.py`**; its full output is
**`data/replication/results/post4_feasibility_checks.txt`**. Reproduce with

```bash
python data/fetch/release_2025_09_15.py && python data/fetch/release_2026_01_15.py \
  && python data/fetch/release_2026_03_24.py           # ~2 min, idempotent, checksummed
python data/replication/post4_feasibility_checks.py     # 7 s
```

Cache state when this note was written: `sha256sum -c CHECKSUMS.txt` inside each of the three
release folders — 38 / 4 / 3 files, **0 failed**. Every file is read with
`keep_default_na=False, na_values=[]` (traps 1, 2) and `level` cast to `str` after each Parquet
read (trap 7). Raw files were not modified.

**Headline.** The design is feasible and the published number reproduces exactly. Three rows of §8
(rows 2, 3 and 5) are wrong or under-specified and must be amended once: the `task_success` intersection has **three**
categories, not two; its `not_classified` cell is the **folded privacy residual**, so the brief's
fallback `yes/(yes+no)` is the wrong fallback; and §8 row 2's "`_count` ≥ 15" rule is inert as
written. Two numbers change: the instrument is available for **2,140** tasks, not the ~2,284
implied, and the usage-weighted (Kish) minimum detectable correlation is **≈ 0.31**, not the
nominal 0.057.

---

## 1. Cuts confirmed at column level

Grain vocabulary: "global" = `geography == 'global'` (`geo_id == 'GLOBAL'`); the long-family key is
`(geo_id, geography, date_start, date_end, platform_and_product, facet, level, variable,
cluster_name)`. `onet_task` and every intersection carry `level == '0'` only. The brief's metric
labels `_pct` / `_count` correspond to file `variable` values with underscores, not colons:
`onet_task_task_success_pct`, not `onet_task::task_success_pct`.

### Row 1 — `onet_task` global share, November and February (Claude.ai) · **CONFIRMED**

| | |
|---|---|
| release / file | `release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv`; `release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv` (Parquet siblings used) |
| grain | `geography == 'global'`, `facet == 'onet_task'`, `level == '0'` |
| facet / category | `cluster_name` = the lower-cased O\*NET task statement, plus the two pseudo-nodes `none` and `not_classified` |
| metric columns | `variable ∈ {onet_task_pct, onet_task_count}` — exactly two, both present in both waves |
| threshold / suppression | privacy floor **15** confirmed as binding and exact: `min(onet_task_count) == 15` in both waves. No suppression flag; absent ≠ zero |

```python
g = df[(df.geography=='global') & (df.facet=='onet_task') & (df.level=='0')]
w = g.pivot_table(index='cluster_name', columns='variable', values='value', aggfunc='first')
```

- November: 6,340 rows → **3,170 nodes** (3,168 named + `none` + `not_classified`);
  `onet_task_pct` sums to **100.000000**; `onet_task_count` sums to **999,875**; named mass
  **93.5144**; `none` 37,119 (3.7124 pp), `not_classified` 27,729 (2.7732 pp).
- February: 6,520 rows → **3,260 nodes** (3,258 named); pct sum **100.000000**; count sum
  **1,000,000**; named mass **92.9714**; `none` 42,922 (4.2922 pp), `not_classified` 27,364
  (2.7364 pp).
- Second implementation (§10) verified now: `max |count/N*100 − pct| = 4.4e-16` in both waves, with
  N = 999,875 (Nov) and 1,000,000 (Feb). **The February denominator is a per-million sample base,
  not conversations** (skill correction 11): shares are comparable across the waves, raw count
  differences are not.

### Row 2 — `onet_task::task_success` global · **CONFIRMED WITH CAVEAT** (three corrections)

| | |
|---|---|
| release / file | the same two Claude.ai files |
| grain | `geography == 'global'`, `facet == 'onet_task::task_success'`, `level == '0'`. Global only — the intersection exists at no other geography (cut 10) |
| facet / category | `cluster_name == '<task>::<category>'` with category ∈ {`yes`, `no`, **`not_classified`**} |
| metric columns | `onet_task_task_success_pct`, `onet_task_task_success_count` — two, as the brief says |
| threshold / suppression | **every published `yes` or `no` cell has count ≥ 15** (min exactly 15; 0 of 2,506 `yes` cells and 0 of 1,650 `no` cells below it). Sub-floor cells are **folded into `not_classified`**, whose counts run 1–27 (Nov) and 1–28 (Feb) and never reach 30 |

```python
g  = df[(df.geography=='global') & (df.facet=='onet_task::task_success')]
sp = g.cluster_name.str.rsplit('::', n=1, expand=True)
g  = g.assign(task=sp[0].str.strip().str.lower(), cat=sp[1])
pct = g[g.variable.str.endswith('_pct')].pivot_table(index='task', columns='cat', values='value')
cnt = g[g.variable.str.endswith('_count')].pivot_table(index='task', columns='cat', values='value')
g.groupby('task').cat.apply(lambda s: tuple(sorted(set(s)))).value_counts()
```

Row counts and coverage: November 11,540 rows over **3,169 task keys** (3,168 named + `none`);
February 12,060 rows over **3,259**. The `not_classified` *task* node — 27,729 November
conversations, 2.77 pp — has **zero** rows in this intersection in either wave.

**(a) Three categories, not two, and `not_classified` is not a classifier output.** The publication
pattern over the 3,169 November task keys is `{no,yes}` 1,545 · `{not_classified,yes}` 951 ·
`{not_classified}` 558 · `{no,not_classified}` 105 · `{yes}` 10 — i.e. **no node publishes all
three**, and the published cells' *counts* partition `onet_task_count` **exactly for 3,169 of 3,169
nodes** (3,259 of 3,259 in February). Together with the floors above, that identifies the mechanism:
the classifier prompt is binary (brief §3), every substantive cell is published at ≥ 15, and any
cell below 15 is relabelled `not_classified`. Where both cells clear the floor there is nothing to
fold, so `not_classified` is absent; where one is folded, `not_classified` ≤ 14; where both are,
`not_classified` is the whole node (counts 15–27). The same rule holds in
`onet_task::use_case`, where up to three cells can fold and the maximum `not_classified` count is
**39** (≈ 3 × 13). *This is a new data fact; it is in `data/ATLAS.md` dated log 2026-09-16 (h).*

**(b) The brief's fallback is the wrong fallback.** `yes + no == 100` for only **1,555 of 3,169**
November nodes (1,568 of 3,259 in February) — the 1,545 `{no,yes}` nodes plus the 10 `{yes}` nodes.
Renormalising over published cells (`yes/(yes+no)`) would set **961** November nodes to exactly
100% success, because their `no` cell is folded rather than zero, and is undefined for the 558 with
no label at all. The construction that is defensible on these files is **success = `yes` `_pct` as
published**: because the cells partition the node exactly, `yes_pct` *is* the share of that task's
own conversations Claude judged successful, with no renormalisation. Its measurement error is the
folded mass, which is published: `not_classified` `_pct`. That bound is not small — **1,056**
November nodes carry a label *and* a folded cell, with bound width median **22.22 pp** and maximum
**48.28 pp** — and it is mechanically larger for small nodes, i.e. correlated with the November
share that the design instruments. Hence the three nested samples in §4.

**(c) The stated threshold rule is inert.** "Nov `_count` ≥ 15 … because intersections go down to 1
in this wave" removes **nothing**: 0 of 2,506 published `yes` cells and 0 of 1,650 `no` cells are
below 15, and the only cells that go to 1 are `not_classified`. The near-floor sensitivity the brief
wants should be written on `onet_task_count` (the node's own size, min 15) and/or on the folded
`not_classified` cell.

### Row 3 — August 2025 `onet_task` share as the instrument · **CONFIRMED WITH CAVEAT**

| | |
|---|---|
| release / file | `release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv` (raw); cross-checked against `data/output/aei_enriched_claude_ai_…parquet` |
| grain | `geography == 'global'`, `facet == 'onet_task'`, `level == '0'` |
| metric column | `onet_task_pct` (and `onet_task_count`) |
| threshold | privacy floor 15 (`min(onet_task_count) == 15`) |

5,236 rows → **2,618 nodes** (2,616 named); pct sum **100.000000**; count sum **964,494**; named
mass **91.8727**. The raw and enriched files give **identical** `onet_task_pct` on all 2,618 nodes,
so either may be used; the raw file is ISO-2 and the enriched ISO-3, which does not matter at global
grain.

**Caveat — the instrument is thinner than §8 assumes.** The brief asks how many of the 2,427 carry
an August share and offers "2,284 nodes appear in all three long waves (ATLAS (e) 9)". That 2,284 is
the *all-node* figure; the named three-wave intersection is **2,282** (2,282 + `none` +
`not_classified` = 2,284, the same arithmetic as 2,886/2,888). Intersected with a November success
label the instrument set is:

| regression sample | N | with an August 2025 share |
|---|---|---|
| any November `yes` or `no` cell | 2,524 | **2,140** (84.79%) |
| published November `yes` cell (the long-list 2,427) | 2,427 | **2,065** (85.09%) |
| exactly identified (no folded cell) | 1,553 | **1,493** |

The 2,140 carry 90.9914 pp of the 92.2879 pp sample mass (98.60%), so the loss is in the tail, not
the mass. First stage on the 2,140: `corr(Aug pct, Nov pct)` = **0.9167** in levels (R² 0.8404) and
**0.8753** in logs (R² 0.7662) — strong, as the design needs. **The August wave has no
`task_success` facet at all** (`facets matching "success" at global: []`), which is why the
exclusion logic is untestable (§4, H1).

### Row 4 — August → November change as the placebo · **CONFIRMED**

Same two files as rows 1 and 3; the placebo is defined on the **2,140** tasks of row 3, not on
2,427. Sizes, computed now: Aug→Nov change mean **+0.00024 pp**, sd **0.08373**, max |·| **2.1578
pp**; Nov→Feb outcome over 2,524 tasks mean **−0.00039 pp**, sd **0.05297**, p5 −0.0079, p95
+0.0178, max |·| **1.8160 pp**. `corr(outcome, placebo) = −0.4251`, the mechanical sign the brief
anticipates (§10) — the November level enters the two changes with opposite signs.

### Row 5 — November controls: `onet_task::use_case`, `onet_task::human_education_years` · **CONFIRMED WITH CAVEAT**

`onet_task::use_case` (global, 3,169 task keys; variables `onet_task_use_case_pct`,
`onet_task_use_case_count`; categories `work`, `personal`, `coursework`, `not_classified`; `_pct`
sums to 100 for 3,169 of 3,169 nodes). Coverage over the 2,524-task sample: `work` **1,782**,
`personal` 1,556, `coursework` 873, `not_classified` 1,917. Same folding rule: `work`, `personal`
and `coursework` cells are all ≥ 15; `not_classified` runs 1–39.
**Caveat:** for **742** of the 2,524 tasks the `work` cell is folded, so the November work share is
not published but bounded in [0, 15/`onet_task_count`). H2's median split is therefore defined on
1,782 tasks (median published work share **59.91**) or on all 2,524 with folded set to zero (median
**41.37**) — two different splits, and the brief must pre-register which.

`onet_task::human_education_years` (global): **`cluster_name` is the task alone, with no
`::category` suffix** — the intersection is a numeric one and carries **nine** variables
(`_count`, `_mean`, `_mean_ci_lower/_upper`, `_median`, `_median_ci_lower/_upper`, `_pct`, `_stdev`),
so §8's "`_mean` (+ `_count`)" is correct but incomplete. `_mean` is published for **3,169 of 3,169**
keys, hence **2,524 of 2,524** regression tasks and 2,140 of 2,140 instrumented tasks; range
1.009–17.512 years; `_count` equals `onet_task_count` for 3,169 of 3,169 nodes, and `_pct` is 100
everywhere. H3's collinearity pre-check, run now: `corr(Nov yes_pct, education mean)` = **−0.0703**
unweighted and **−0.1752** usage-weighted over the 2,524 — the expected sign, far too weak to
carry H1 on its own.

### Row 6 — the 1P API exploratory leg · **CONFIRMED WITH CAVEAT**

`release_2026_01_15/…/aei_raw_1p_api_2025-11-13_to_2025-11-20.csv` and
`release_2026_03_24/data/aei_raw_1p_api_2026-02-05_to_2026-02-12.csv`. `geography` is **`global`
only** in all three waves and there is **no `usage_count` variable** in any of them — both as §8
says.

| wave | `onet_task` nodes (named) | count sum | `onet_task::task_success` task keys |
|---|---|---|---|
| Aug 2025 | 2,056 (2,054) | 944,638 | **absent** |
| Nov 2025 | 2,253 (2,251) | 971,525 | 2,252 |
| Feb 2026 | 2,299 (2,297) | 1,000,000 | 2,298 |

Matched named API panel Nov ∩ Feb = **1,930**; with a November success label **1,686**; also
carrying an August API share (so instrumentable) **1,428**. Same three categories and same folding
rule (Nov `yes` cells min 15, `not_classified` 1–28); February has **one** node publishing all
three, the only such node found in any frame. So the exploratory replication (§9 (ii)) is available
on 1,686 tasks, or 1,428 with the instrument — state which.

**No cut named in §8 does not exist.** Every row resolves to a real column at the stated grain; the
corrections above are to the category list, the fallback rule, the threshold rule and two Ns.

---

## 2. Replication target

**The number.** Fourth report (`economic-index-2026-01-report`, 2026-01-15): global Claude.ai task
success **67%**, Figure 2.2, p.25, N = 999,875; and the platform pair **67% vs 49%**, p.26.

**Specification expected** (`data/ATLAS.md` §Conventions, §Other bases worth stating): `facet ==
'task_success'`, `geography == 'global'`, `variable == 'task_success_pct'`, `cluster_name == 'yes'`,
on the **all-conversation base**. No renormalisation and no exclusion is needed: the global
`task_success` facet publishes `yes` and `no` only, its `_pct` sums to exactly 100, and its `_count`
sums to the wave's sample N.

**Anthropic's released code does not cover it.** Reports 4, 5 and 6 ship none; the 2025-09-15
`code/` library is the specification of record for later waves, and its relevant entry point
(`filter_df`) is a filter, not a statistic. The number is a single published cell, so the
re-implementation is the filter above and nothing else. Stated as such.

**Run now** (under ten minutes; §6 of the checks script):

```python
t = df[(df.geography=='global') & (df.facet=='task_success')]
w = t.pivot_table(index='cluster_name', columns='variable', values='value', aggfunc='first')
```

| frame | `yes` `_pct` | `no` `_pct` | `_count` sum | published | match |
|---|---|---|---|---|---|
| Nov 2025 Claude.ai | **66.9060** | 33.0940 | **999,875** | 67%, N = 999,875 (p.25) | **exact** — 66.9060 → 67%; N identical to the digit |
| Nov 2025 1P API | **49.3638** | 50.6362 | 971,525 | 49% (p.26) | **exact** — 49.3638 → 49% |
| Feb 2026 Claude.ai | 69.9385 | 30.0615 | 1,000,000 | not published | data fact (ATLAS §Cuts 26b), reported as such |
| Feb 2026 1P API | 50.5476 | 49.4523 | 1,000,000 | not published | data fact; note a `not_classified` cell of count 1 |

The count route agrees with the `_pct` route to four decimals in every frame (66.9060 / 49.3638 /
69.9385 / 50.5476), so the second implementation of §10 already passes for the replication target.

**One further check that ties the column to the published measure** (assumptions sweep §7.2): the
usage-weighted mean of the *per-task* `yes_pct` over the 2,611 labelled November task nodes is
**66.9141%** on 962,000 conversations, against the published global **66.9060%** — a 0.0081 pp
difference, entirely accounted for by the 558 unlabelled nodes and the two pseudo-nodes. February:
**69.9215%** against 69.9385%. The intersection column is demonstrably the same measure as the
headline.

A replication note is not required for this post beyond the above; when the analysis starts I will
copy this table into `posts/post4/notes/replication.md` with the commit that produced it.

---

## 3. Supplementary joins tested

**The brief names none, and none is needed.** §8 states "No supplementary data and no external
join", which is correct: every quantity in §§6–10 lives inside `release_2025_09_15`,
`release_2026_01_15` and `release_2026_03_24`. The post needs no O\*NET→SOC crosswalk, no wage file,
no population and no GDP (and §4 correctly declines post1's multi-holder rule).

The only join in the design is the **within-corpus task-text name match**, which is audited here
rather than under §1:

| join | rows in | matched | unmatched |
|---|---|---|---|
| Nov ↔ Feb `onet_task` (lower-cased, stripped) | 3,170 / 3,260 | **2,888** incl. both pseudo-nodes → **2,886** named | 282 Nov-only, 372 Feb-only |
| (Nov ∩ Feb) ↔ Aug `onet_task` | 2,886 / 2,618 | **2,282** named | 604 of the matched pair absent in August |
| matched pair ↔ Nov `onet_task::task_success` | 2,886 | 2,524 with a label (2,427 with a `yes` cell) | 362 with no label |
| matched pair ↔ Nov `onet_task::human_education_years` | 2,886 | 2,886 | 0 |

**The 2,886 / 2,888 reconciliation the lead asked for is exactly as §8 expects**: the difference is
the two pseudo-nodes `none` and `not_classified`, both of which match across the waves.
Lower-casing is safe here — trap 21 (case-variant duplicates) was checked and there are **0**
collisions in all three waves (3,170 / 3,260 / 2,618 nodes → the same number of distinct
lower-cased stripped keys).

Licence, for the record: data **CC-BY** (no version given in the card body), code MIT; attribute
Anthropic. No external source, so no external licence.

---

## 4. Hypothesis by hypothesis

Three nested samples, all on the matched named panel of 2,886:

| label | rule | N | Nov mass | with instrument |
|---|---|---|---|---|
| **A** | any published November `yes` or `no` cell | 2,524 | 92.2879 pp | 2,140 |
| **B** | published November `yes` cell (the long-list 2,427) | 2,427 | 91.9470 pp | 2,065 |
| **C** | exactly identified: no folded `not_classified` cell | 1,553 | 88.6094 pp | 1,493 |

B is the brief's sample and it reproduces to the node: **2,427**, mass **91.9470** of 100 (98.32% of
the November named mass — note the brief's "91.95% of Nov named mass" is 91.95 *of 100*, i.e. of all
conversations, not of the named mass; the wording needs one word changed). A adds the 97 nodes whose
only label is `no`. C is the sample on which the regressor is measured without folding error.

**Power, which is where this design is fragile.** The nominal MDE in §9 is right; the weighted one is
five times larger:

| sample | N | Kish N_eff (Nov weights) | Kish N_eff (Feb weights) | MDE \|r\| nominal | MDE \|r\| weighted |
|---|---|---|---|---|---|
| A | 2,524 | **87.1** | 129.6 | 0.0558 | **0.3052** / 0.2489 |
| B | 2,427 | **86.5** | 128.2 | 0.0569 | **0.3064** / 0.2503 |
| C | 1,553 | 80.4 | 118.2 | 0.0711 | 0.3184 / 0.2608 |

(MDE = 2.8 × SE with SE = 1/√(N−3), as §9 specifies.) The cause is the concentration §9 already
names: the ten largest matched tasks are **19.4410 pp** of all February conversations — which is
**19.4% of the all-conversation base and 20.9% of named-task mass**; §9's phrase "19.4% of the
February named mass" mixes the two bases and should say the former. A usage-weighted null must be
declared against ≈ 0.31, not 0.057, exactly as §9 requires — the numbers are now available to write
into the pre-registration.

**H1 (predictive content).** Exists at the grain assumed. Outcome, regressor, level control,
instrument and education control are all present at global grain for 2,140 tasks (2,524 without the
instrument). Caveats: (i) the regressor carries folding error on **971** of the 2,524
sample nodes (1,056 of all 3,169 published nodes), median bound width **22.73 pp** on the sample,
and that error is larger for small nodes, i.e. **correlated with the
instrumented level** — run A and C and report both; (ii) **the exclusion restriction is not testable
with these aggregates.** There is no unit-level identifier (cut 27b), no success measure in the
August wave at all, and no second instrument, so "the August share affects the Nov→Feb change only
through the November level" can be argued but not tested; the nearest available checks are the
first-stage strength (R² 0.84 in levels) and the placebo, and the brief should say so rather than
imply an over-identification test; (iii) the outcome is small relative to the wave-to-wave noise —
sd 0.053 pp against a placebo sd of 0.084 pp.

**H2 (composition, not return behaviour).** Partly feasible. The `use_case` shares and
education-years controls exist for the whole sample, but the work-share split is defined on 1,782 of
2,524 tasks (above), so the interaction test loses 29% of the sample or needs the folded-to-zero
convention. The *mechanism* — the February first-time-user inflow — is **not observable in any
released file**: there is no tenure, user, account, plan or first-time-user column anywhere (cuts
26, 26a), so H2 tests the interaction pattern the inflow would produce, never the inflow itself.
State that plainly.

**H3 (inverse index of difficulty).** Fully feasible: education `_mean` for 2,524 of 2,524, with
CIs, and the collinearity is mild (−0.0703 unweighted, −0.1752 usage-weighted). The benchmark
coefficient §7.4 wants is estimable.

**H4 (movement at the margin).** Feasible but weak, and the brief's framing of it needs a caveat.
Of the 282 November-only exits only **86** carry a November success label, and of the 372
February-only entrants only **140** carry a February one — the rest publish `not_classified` alone,
because they sit at the floor: **213 of 282** exits and **264 of 372** entrants have ≤ 20
conversations. So these nodes are **floor-crossers, not new work** (absent ≠ zero, trap 25): a
February-only task was very likely present in November below 15 conversations. Sizes: exits 0.5438
pp of November, entrants 0.7552 pp of February. Raw comparisons and their power, computed now —
exits mean November `yes_pct` **73.44** (sd 25.25, n 86) against survivors' **66.60** (sd 19.11,
n 2,524), MDE **7.70 pp**; entrants mean February `yes_pct` **75.45** (sd 24.81, n 140) against
survivors' February **69.25**, MDE **5.98 pp**. Both raw gaps sit near the MDE, so H4 will be
reported as suggestive-or-null whichever way it lands, and the "three groups' distributions"
comparison should be pre-registered as unweighted (usage weights are meaningless for nodes of 15–20
conversations).

---

## 5. Traps that apply

| trap (`data/ATLAS.md`) | what it does here | brief section |
|---|---|---|
| **1, 2 — `NA` is Namibia; `NONE` is a real geography in 2026-03-24** | irrelevant at global grain but fatal if any country cut is ever added; the loader in §8 is already correct | §8 closing paragraph |
| **7 — Parquet `level` dtype differs between waves** | `level == '0'` silently returns zero rows on one wave without the cast; the checks script casts | §8 closing paragraph |
| **24 — `none` ≠ `not_classified`** | both pseudo-nodes must be dropped from `onet_task` (6.49 pp Nov, 7.03 pp Feb combined); and inside the intersection `not_classified` means something different again (§1 row 2) | §8 rows 1–2, §10 |
| **NEW (h) — the intersection's `not_classified` is the folded sub-15 residual** | determines the success construction, the effective N and the near-floor rule | §8 row 2, §9 test 1, §10 |
| **25 — absent ≠ zero** | the 282/372 "entrants and exits" are floor-crossers, not appearances and disappearances | §6 H4, §12 |
| **21 — lower-casing can create many-to-many matches** | checked: 0 collisions in all three waves, so the §8 match rule is safe as written | §8 closing paragraph |
| **40 / §Taxonomies — never diff cluster sets across waves without a name match and the unmatched names** | complied with; `onet_task` is the ladder that survives (2,888 of 3,170/3,260), `request` would not | §8 |
| **14 + ATLAS (e) 3 — Seychelles** | 24,715 November conversations (2.47% of the base), **0 rows in February**. Partly removable — see below | §7.3(c), §10 |
| **42 / §Other bases — say which base** | `onet_task_pct` is a share of all conversations including `not_classified`; the intersection `_pct` is a share of the task's own conversations (verified exactly) | §8 rows 1–2, §7.2 |
| **skill correction 11 — February counts are per million** | the count route to shares must divide by 1e6 (Feb) and 999,875 (Nov) | §10 second implementation |
| **cut 10 — intersections are global only** | no geographic control, no country fixed effect, no way to net any geography out of the regressor | §7.3(c), §9 |
| **cut 7 / 27a — no time dimension inside a release** | the panel is three cross-sections with 2–3 month gaps; "next window" is February, and there is no fourth | §6, §12 |
| **`task_success` has no June 2026 counterpart** (`## Components`) | a third window does not exist and cannot be added; §12's ask is correctly framed | §12 |
| **36 — occupation is inferred from the task** | not used here (no SOC join), but the unit remains a conversation, not a worker | §7.3 |

**Correction to §7.3(c), with numbers.** The brief says the Seychelles asymmetry "cannot be removed
at global grain because every intersection is global-only". Half of that is right. Seychelles
publishes **67 `onet_task` nodes (65 named) whose counts sum to 24,715 — its `usage_count` exactly**
(6.2% of it in its own `none`/`not_classified` nodes), and 65 of those named nodes are inside the
regression sample, carrying 23,173 conversations = 2.3176 pp of the November base. So the
**outcome** *can* be netted, task by task, on the November side: doing it moves the November share
of 47 tasks by more than 0.01 pp, median +0.0002, **minimum −0.5449 pp**. That minimum matters,
because it is the largest task in the panel: "modify existing software to correct errors…" has
59,739 November conversations of which **6,790 (11.37%) are Seychelles**, and its raw Nov→Feb change
of **−1.8160 pp** — the largest movement in the whole panel, and the heaviest weight under a
usage-weighted estimator — becomes **−1.2712 pp** once Seychelles is netted out. Thirty per cent of
the headline mover is one departed geography. What *cannot* be corrected is the **regressor**: SC has
0 rows at `onet_task::task_success` (intersections are global only). Recommended amendment: keep the
statement, add the SC-netted outcome as a required robustness run in §10, and name the 11.37% figure
in the post.

---

## 6. Verdict

**FEASIBLE WITH CAVEAT.**

The caveat the referee and the lead must carry: the cuts all exist and the published anchor
reproduces exactly (66.9060% → 67%, N = 999,875; API 49.3638% → 49%), but three things in §8 are
mis-specified and one power statement is five times too optimistic. `onet_task::task_success`
publishes **three** categories, and its `not_classified` cell is the **folded sub-15 privacy
residual**, not a classifier verdict — so the brief's fallback `success = yes/(yes+no)` must be
replaced by `success = yes _pct` as published (the cells partition the node's conversations exactly),
with the folded mass carried as a bound that is median 22.73 pp wide on 971 of the 2,524 sample
nodes and mechanically wider for smaller nodes, i.e. correlated with the instrumented level; §8 row 2's
"`_count` ≥ 15" rule removes nothing, because every published `yes`/`no` cell is already ≥ 15, and
the near-floor sensitivity belongs on `onet_task_count`; the instrument exists for **2,140** of the
2,524 (2,065 of the 2,427), not the ~2,284 implied by §8 row 3, and the August wave has no success
measure at all, so the exclusion restriction can be argued but **not tested** on these aggregates;
the H4 margin is 86 labelled exits and 140 labelled entrants, four-fifths of them within five
conversations of the publication floor, so H4 tests floor-crossing, not entry; H2's work-share split
is defined on 1,782 of 2,524 tasks and its mechanism — the February first-time-user inflow — is
unobservable in every released file; and the usage-weighted minimum detectable correlation is
**≈ 0.31** (Kish N_eff 87 on November weights), not the nominal 0.057, so a null must be declared
against the weighted figure and the post must not read a small weighted coefficient as evidence
either way. Finally, the largest task in the panel owes 11.37% of its November conversations to
Seychelles, which is absent in February: the outcome can and should be netted for that (it moves the
biggest mover from −1.8160 to −1.2712 pp), the regressor cannot.

*Amendments requested of the lead, once, in `room/steward-2026-09-16-feasibility-post4.md`: §8 row 2
(categories, construction, threshold), §8 row 3 (2,140/2,065), §7.3(c) and §10 (Seychelles is
partly removable), §9 (Kish MDE ≈ 0.31; "19.4% of all conversations, 20.9% of named mass"), §8's
"91.95% of Nov named mass" → "91.95 of 100".*

---

### Dated log

- **2026-09-16 — written.** Against BRIEF.md at 008d762. Cache verified (38/4/3 files, 0 failed);
  all numbers from `data/replication/post4_feasibility_checks.py`, output in
  `data/replication/results/post4_feasibility_checks.txt`. New data fact recorded in
  `data/ATLAS.md` dated log 2026-09-16 (h): the folded `not_classified` cell in the 2026 long-wave
  `onet_task::<categorical>` intersections.
