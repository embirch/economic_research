# post1 (LL-07) — feasibility, confirmed at column level

*Data steward. Written against `posts/post1/BRIEF.md` (commit 9541d92) and
`room/lead-2026-09-16-brief-post1-status.md`. Authority for conventions and traps:
`data/ATLAS.md`. Cache rebuilt from scratch in this sandbox before anything was confirmed —
`for r in release_2025_02_10 release_2025_09_15 release_2026_01_15 release_2026_03_24; do python
data/fetch/$r.py; done` → 59 files, 355,158,908 B, every byte size and sha256 equal to
`data/releases/INDEX.md`, and `sha256sum -c CHECKSUMS.txt` re-run inside each of the four folders
(14 / 38 / 4 / 3 OK, 0 failed). Nothing below is confirmed from the atlas alone.*

Every long-wave read in this note is
`pd.read_csv(..., keep_default_na=False, na_values=[])` or the Parquet sibling with every
non-`value` column cast to `str` (`ATLAS` §Traps 1, 2, 6). Working scripts, committed so any
session can re-run them: `data/replication/post1_{cuts_c1_c8,joins_c5_c7,variance_mde,replicate_fig211}.py`;
pooled output `data/replication/results/post1_feasibility_checks.txt`.

---

## 1. Cuts confirmed at column level

### C1 · `release_2025_09_15`, Aug 2025 global `onet_task::collaboration` — **CONFIRMED**

- File `data/cache/release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv`
  (100,062 rows). `platform_and_product` = **`Claude AI (Free and Pro)`** (single value);
  `date_start` 2025-08-04, `date_end` 2025-08-11.
- Grain `geography == 'global'` (29,656 rows); `facet == 'onet_task::collaboration'` → **14,454
  rows**, `level` = `'0'` throughout, variables **`onet_task_collaboration_count`** and
  **`onet_task_collaboration_pct`** (7,227 rows each). **0 rows at any geography other than
  `global`** — the grain rule in the brief holds.
- `cluster_name` is `task::pattern`; split on the **last** `::` (`str.rsplit('::', n=1)`).
  **2,617** distinct base tasks, **2,616** named. Patterns present: all **seven** —
  `directive`, `feedback loop`, `learning`, `task iteration`, `validation`, `none`,
  `not_classified`.
- Threshold: privacy floor only, and it is **1**, not 15 — `min(_count) = 1.0`,
  `max = 25,852`. Within a task the seven `_pct` values sum to exactly 100.0000 at the median,
  min and max (the intersection `_pct` is a share of its **base cluster**, `ATLAS` §Other bases).
- **Refinement the brief should carry:** the intersection publishes **100.00%** of the base
  named-task `onet_task_count` (886,107 of 886,107), so there is *no* cell suppression inside it;
  what the brief calls the residual is explicit — over named tasks the intersection counts split
  **92.90% classified / 2.46% `none` / 4.64% `not_classified`**.

```python
g = df[df.geography=='global']; ix = g[g.facet=='onet_task::collaboration']
p = ix.cluster_name.str.rsplit('::', n=1); ix['task'], ix['pattern'] = p.str[0], p.str[1]
len(ix), ix.task.nunique(), sorted(ix.pattern.unique()), ix[ix.variable.str.endswith('_count')].value.min()
# -> 14454, 2617, ['directive','feedback loop','learning','none','not_classified','task iteration','validation'], 1.0
```

### C2 · `release_2026_01_15`, Nov 2025 — **CONFIRMED**

Parquet sibling of `data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv`
(458,778 rows), `platform_and_product` = `Claude AI (Free and Pro)` — the label the brief
correctly flags as wrong for the sample (`ATLAS` Components / `[R4 §Traps 10]`).
`onet_task::collaboration` at global: **16,778 rows**, 8,389 per variable, level `'0'`,
**3,169** base tasks / **3,168** named, seven patterns, `min(_count) = 1.0`, per-task `_pct`
sums exactly 100. Intersection publishes 100.00% of the base named counts (935,027);
classified **92.34%**, `none` 2.02%, `not_classified` 5.64%. No non-global intersection rows.

### C3 · `release_2026_03_24`, Feb 2026 — **CONFIRMED**

`data/aei_raw_claude_ai_2026-02-05_to_2026-02-12` (477,717 rows),
`platform_and_product` = **`Claude AI (Free, Pro, and Max)`**. `onet_task::collaboration` at
global: **17,530 rows**, 8,765 per variable, **3,259** base tasks / **3,258** named, seven
patterns, `min(_count) = 1.0`. Counts are on the **1,000,000 sample base** as the brief says
(global `onet_task_count` sums to exactly 1,000,000; named tasks carry 929,714). Classified
**91.94%**, `none` 2.16%, `not_classified` 5.90%. No non-global intersection rows.

**New fact, and it bears on §8(ii) and §9(1).** The base `collaboration` facet at global carries
**essentially no `not_classified`** (1 conversation in Aug, **0** in Nov and Feb —
`ATLAS` log (g) 6), while the `onet_task::collaboration` intersection carries
**41,134 / 52,693 / 54,893** `not_classified` conversations (4.64 / 5.64 / 5.90% of named-task
counts) on 2,476 / 3,029 / 3,110 tasks. The two frames do not agree on the residual, so the
five-pattern base is *not* the same population in the marginal facet and in the intersection.

### C4 · same-wave `onet_task` weights — **CONFIRMED WITH CAVEAT (the brief names the wrong pair)**

Global `onet_task`: 5,236 / 6,340 / 6,520 rows, variables `onet_task_count`, `onet_task_pct`;
`onet_task_pct` sums to **exactly 100.000000** in each wave; `min(onet_task_count) = 15` in all
three (the base-cell floor).

| wave | task nodes | named | `none` mass | `not_classified` mass | named mass | conversations (named) |
|---|---|---|---|---|---|---|
| Aug 2025 | 2,618 | 2,616 | 5.7162 | 2.4111 | **91.8727** | 886,107 |
| Nov 2025 | 3,170 | 3,168 | 3.7124 | 2.7732 | **93.5144** | 935,027 |
| Feb 2026 | 3,260 | 3,258 | 4.2922 | 2.7364 | **92.9714** | 929,714 |

The caveat: the **base facet has two residual nodes** (2,618 / 3,170 / 3,260 = named + `none` +
`not_classified`), the **intersection has one** — `none` is present in the intersection,
`not_classified` is **absent from it entirely** (set difference computed both ways: 0 intersection
tasks missing from the base facet, exactly 1 base task missing from the intersection, and it is
`not_classified`). So the brief's "one-node difference between 2,617/3,169/3,259 and
2,616/3,168/3,258" is arithmetically right but the node it is dropping is `none`, and dropping
"`none` and `not_classified` task nodes" from the **base facet** removes 8.13 / 6.49 / 7.03 pp of
usage mass, not one node's worth. §8 should say: intersection = named + `none`; base = named +
`none` + `not_classified`; the analysis universe is the 2,616 / 3,168 / 3,258 named nodes.

### C5 · `onet_task_statements.csv` (O\*NET DB 20.1) task → SOC — **CONFIRMED**

`data/cache/release_2025_09_15/data/intermediate/onet_task_statements.csv`, **19,530 × 9**:
`O*NET-SOC Code, Title, Task ID, Task, Task Type, Incumbents Responding, Date, Domain Source,
soc_major_group`. 974 distinct `O*NET-SOC Code`, 775 distinct 7-char prefixes, 22
`soc_major_group` values, 19,530 distinct `Task ID`, **18,429** distinct `Task` texts →
**18,428** lower-cased-stripped keys (the case-variant collapse is exactly **one** pair here) and
up to **34 rows per key**, so the de-duplication the brief requires is necessary and sufficient.

Merge audit, named global task nodes → 20.1 key, per wave:

| wave | rows in | matched | unmatched | unmatched mass | nodes colliding on one key |
|---|---|---|---|---|---|
| Aug 2025 | 2,616 | **2,616** | 0 | 0.0000 pp | 0 |
| Nov 2025 | 3,168 | **3,168** | 0 | 0.0000 pp | 0 |
| Feb 2026 | 3,258 | **3,258** | 0 | 0.0000 pp | 0 |

Multi-holder exposure (the construction triple's rule): tasks whose key has more than one holder
— **74 / 93 / 86** at the 10-char `O*NET-SOC Code`, **72 / 91 / 84** at the 7-char SOC
(= `ATLAS` log (g) 4), **6 / 10 / 9** spanning more than one SOC **major group**
(0.28 / 0.29 / 0.26 pp of the wave). The multi-holder mass is **4.05 / 5.57 / 4.50 pp of the
wave** = **4.44 / 5.98 / 4.87% of named mass**: the brief quotes the first pair but calls it "of
named usage mass" — it is of the wave total. The ≤0.17 pp bound the brief cites for the three
allocation rules is confirmed as reported in `room/steward-…-batch-3-answers.md` (LL-32) and is a
bound on the **SOC-15 occupational share**, not on this post's gradient; on *wage* the three
rules differ on only 74 / 93 / 86 tasks, with equal-split vs employment-weighted correlated at
**0.9998** and a maximum single-task gap of **$6.38/hr**.

### C6 · `release_2025_02_10/wage_data.csv` — **CONFIRMED WITH CAVEAT: the stated join key does not join**

- File 1,090 × 10: `SOCcode, JobName, JobFamily, isBright, isGreen, JobZone, MedianSalary,
  JobForecast, ChanceAuto, WageGroup`. `SOCcode` is unique and is a **10-character O\*NET-SOC
  code** (`13-2011.01`), every row 10 chars.
- **The brief's key is wrong.** `O*NET-SOC Code[:7]` → `SOCcode` matches **0 of 775** codes.
  Three repairs, in order of preference:
  1. **the full 10-char `O*NET-SOC Code` → `SOCcode`** — **970 of 974** occupations, and this is
     what Anthropic's own released code does
     (`plots.ipynb` cell 26: `merge(wage_df, left_on="O*NET-SOC Code", right_on="SOCcode")`);
  2. truncate **both** sides to 7 chars — 772 of 775, but up to **13** wage rows share one 7-char
     code, so it imports a second, unstated aggregation choice;
  3. nothing else joins.
- `MedianSalary > 100` keeps **1,084 of 1,090**; the six removed are the hourly rows
  (15.94, 16.31, 17.54, 28.15 ×3 — `ATLAS` §Traps 10). In the released notebook the filter is
  applied **after** the join and after an `agg('first')` aggregation to occupation `Title`, not as
  a pre-filter. `MedianSalary` is **annual** and Anthropic plots it as dollars per year; the
  ÷2080 hourly conversion is this post's, not Anthropic's, and must be labelled as such. It is
  **top-coded at $208,000** (6 occupations, $100.00/hr), which touches 9 / 6 / 6 tasks and
  0.05–0.06% of analysis mass — immaterial. `JobZone == -1` for 121 occupations and
  `ChanceAuto == -1` for 424 (missing-value sentinels).
- Coverage on the corrected key, tasks priced / named tasks and priced mass:
  **2,607 of 2,616 = 99.35%**, **3,154 of 3,168 = 98.98%**, **3,244 of 3,258 = 99.30%** of named
  mass — the 99.4 / 99.0 / 99.3 in the brief's verbatim line is confirmed, on the 10-char join.
  `JobZone` (exploratory test c) covers 99.86 / 99.85 / 99.77% of named mass.

### C7 · BLS Employment Projections — **CONFIRMED WITH CAVEAT**

`curl -sL https://data.bls.gov/projections/occupationProj` → **HTTP 200**, 1,397,448 B, one HTML
table, **831 detailed-SOC rows**, 831 unique `Occupation Code`; `Median Annual Wage 2025`
non-null on **825**, `Employment 2025` (thousands) on 831. Merge audit `soc7` → `occ_code`:
775 in, **670 matched**, 105 unmatched (`11-1031` Legislators, `11-2031`, `11-3011`, `11-9061`,
`13-1021`, …). Priced named-task mass: **51.14 / 54.73 / 57.85 pp of the wave** =
**55.66 / 58.52 / 62.22% of named mass**. The brief's "54.7% / 57.8%" are the *wave-total*
figures for Nov and Feb; say which denominator. Rank agreement with C6 over tasks priced by both
is high (Spearman **0.9869 / 0.9859 / 0.9870**, N 2,042 / 2,534 / 2,593), so C7 is fit for the
sign-agreement role the brief gives it and unfit for a level (usage-weighted mean hourly wage
$37.64 / $37.69 / $37.55 on EP against $35.34 / $35.08 / $34.36 on C6 — both far from Anthropic's
$49.3/$47.9). **Employment weights are 7-char only**, so the employment-weighted multi-holder
rule is identified only across distinct 7-char SOCs; of the 74 / 93 / 86 multi-priced-holder
tasks, **2** have all holders inside one 7-char SOC and there the rule degenerates to the
equal-split mean. US Government work, public domain. (`www.bls.gov` and `download.bls.gov` still
return **403** here, so OEWS is unobtainable — `ATLAS` §Supplementary sources.)

### C8 · Seychelles netting — **CONFIRMED WITH CAVEAT: wrong `geo_id`, and the netting cannot reach the rates**

- **`geo_id == 'SYC'` returns 0 rows.** In `release_2026_01_15` country ids are **ISO-2**: the id
  is **`SC`** (410 rows), `usage_count` **24,715**, `usage_pct` 2.47181. §8 must be amended.
- SC's `onet_task` rows: 134 (67 nodes), `onet_task_count` summing to 24,715 (= its whole usage),
  of which 65 named nodes carry 93.76% of SC's mass; all 65 are in the global named set. Netting
  the **weights** is therefore exact and small in aggregate — mean |shift| 0.0012 pp — but reaches
  **0.58 pp** on one task ("modify existing software to correct errors…").
- **`geo_id == 'SC'` has 0 rows of `onet_task::collaboration`** — intersections are global only
  (`ATLAS` §Cuts 10). So the November re-estimate can net Seychelles out of the task **weights**
  and **cannot** net it out of the per-task **automation rates**, which are the dependent
  variable. That matters here more than the 1.17 pp headline suggests: SC's own collaboration mix
  is 60.0% `feedback loop` against a global 13.6%, and SC is up to **64.3%** of the *global*
  conversation count of individual tasks (median 4.8% over its 67 nodes). In the analysis set,
  **23 tasks** have SC above 10% of their global count and hold **11.59 pp** of wave mass, of
  which **9.04 pp sits in the top wage quartile** (a third of that quartile's 25.76 pp).
- The 1.17 pp figure reproduces: netting SC from the global `collaboration_count` moves the mix by
  **1.1748 pp** (`feedback loop`) and the five-pattern automation share from 46.7394 to **45.4868**.
- Nearest substitute for the un-nettable part, at low cost: a pre-registered sensitivity that drops
  the tasks where SC exceeds a stated share of the global count (14 tasks at >20%, 1.97 pp; 23 at
  >10%, 11.59 pp) and re-estimates; and treating November as the wave that must be corroborated by
  Aug 2025 and Feb 2026 rather than as an independent confirmation.

---

## 2. Replication target

**What the brief names (§8).** (i) each wave's global collaboration split on the base its report
used; (ii) an internal check that the usage-weighted mean of per-task automation returns that
wave's global value "within rounding"; (iii) the task-value non-reproduction, stated not attempted.

**(i) Reproduced, to four decimals, from the wave files (`/tmp/p1/a_out.txt`).**

| wave | published | all-conversation base | five-classified base | brief's figure |
|---|---|---|---|---|
| Aug 2025 | "49%" | **49.0980** | **51.0698** | 49.0980 / 0.5107 ✓ |
| Nov 2025 | "45%" | **45.3554** | **46.7394** | 45.3554 / 0.4674 ✓ |
| Feb 2026 | "44%" | **44.1569** | **45.5456** | 44.1569 / 0.4555 ✓ |

The Aug 2025 enriched file's own `automation_pct` variable at global is **51.0698**, identical to
the five-pattern recomputation — the base-by-wave rule of `ATLAS` §Conventions holds exactly.

**Anthropic's released code covers this, and it was run.** `release_2025_09_15/code/` is the only
library in the dataset. Imported in place (`geopandas` is imported at module scope, is not
installed here and is not used by these functions, so a stub module was injected;
`chdir` into `code/` is required — `ATLAS` §Traps 31):

```
collaboration_task_regression(df, geography="country")
 -> partial_slope -3.111834   partial_r2 0.393687   p 1.721e-13   n_countries 111   n_tasks 1808
    published (report Fig 2.11): -3.112 / 0.394 / 111     ->  exact match
```

This is the strongest replication available for this post, because Figure 2.11 is built from
**exactly** the machinery post1 extends: per-task automation rates from
`onet_task::collaboration` at global on the five-classified-pattern base, weighted by
`onet_task_pct`. The released spec, verbatim from the function: drop the `not_classified` **task**
node, keep the `none` task node ("they have automation/augmentation patterns in the data"), drop
`none`/`not_classified` **patterns** from each task's base, renormalise the weights over tasks
that have a rate. Its parser is `cluster_name.str.split("::").str[0]` — safe here (0 cluster names
contain more than one `::`), but `rsplit` is the durable form.

**(ii) The internal check is not an identity, and §8 should say so.** Running the released rule at
global:

| wave | usage-weighted mean of per-task automation (named tasks) | wave five-pattern value | gap |
|---|---|---|---|
| Aug 2025 | **51.2001** | 51.0698 | **+0.1303** |
| Nov 2025 | **47.0325** | 46.7394 | **+0.2931** |
| Feb 2026 | **45.8966** | 45.5456 | **+0.3510** |

Keeping the `none` task node as the released code does gives 51.7424 in Aug (+0.67). Cause,
decomposed: the intersection publishes 100.00% of base named counts, so this is **not**
suppression — it is (a) the named-task restriction, which drops 8.13 / 6.49 / 7.03 pp of mass
whose automation mix differs, and (b) the intersection's own `not_classified` pattern
(4.64 / 5.64 / 5.90% of named counts) which the marginal facet does not have. Recommended
wording for §8(ii): the check must return the wave value **within 0.36 pp**, with the direction
positive in all three waves, and the two causes named. A tolerance of "rounding" would fail a
check that is in fact passing.

**(iii) The task-value non-reproduction re-derived today, on the corrected C6 key:** usage-weighted
mean hourly wage **$35.34 (Aug) → $35.08 (Nov) → $34.36 (Feb)** on `wage_data.csv` and
**$37.64 → $37.69 → $37.55** on BLS-EP, against Anthropic's published $49.3 → $47.9. The Nov→Feb
pair reproduces `ATLAS` log (f) 13 exactly, which confirms that the atlas's figures were computed
on the 10-char join and that the `[:7]` shorthand in that log entry (and in the brief) is a
transcription error. Direction preserved (−$0.72 against the published −$1.40). Nothing further is
needed in Stage 2 for the replication; the rank-based design stands.

---

## 3. Supplementary joins tested

| source | vintage | join key | audit | coverage against Index units | licence |
|---|---|---|---|---|---|
| O\*NET task statements (C5) | **DB 20.1**, shipped in `release_2025_09_15/data/intermediate/` | lower-cased stripped task text, de-duplicated (19,530 rows → 18,428 keys) | 2,616 / 3,168 / 3,258 in, **all matched**, 0 unmatched, 0 collisions | 100% of named task nodes in all three waves | O\*NET CC-BY (via the dataset card's CC-BY, no version) |
| `wage_data.csv` (C6) | O\*NET website scrape, **Kilbourne-Quirk 2019** — not a BLS series | **full 10-char `O*NET-SOC Code` → `SOCcode`** (not `[:7]`) | 974 occupation codes in, **970 matched**; 1,084 of 1,090 wage rows after `>100` | 2,607 / 3,154 / 3,244 tasks = **99.35 / 98.98 / 99.30%** of named mass | see `release_2025_02_10/README.md` |
| BLS Employment Projections (C7) | 2025–2035 table, fetched today, HTTP 200 | `soc7` → `occ_code` | 775 in, **670 matched**, 105 unmatched | **55.66 / 58.52 / 62.22%** of named mass; employment for the multi-holder rule at 7-char only | US Gov, public domain |
| `JobZone` from C6 (exploratory c) | same file | same 10-char key | 121 occupations carry the `-1` sentinel and must be dropped | 99.86 / 99.85 / 99.77% of named mass | as C6 |

No other supplementary source is named in §8, and none is needed: the whole design lives inside
the released files plus these. OEWS (Anthropic's own wage source) is **unobtainable from this
sandbox** — `www.bls.gov` and `download.bls.gov` 403 — which is why the level does not reproduce
and the design is rank-based.

---

## 4. Hypothesis by hypothesis

**The analysis set** (task has a C6 wage **and** at least one classified-pattern cell):
**1,802 / 2,075 / 2,188 tasks**, carrying **89.25 / 89.99 / 89.73 pp** of the wave =
**97.15 / 96.23 / 96.52% of named mass**, on **818,673 / 854,432 / 848,716** classified
conversations. Losses are small and audited: 5 / 12 / 12 tasks have a classified cell but no wage
(0.58 / 0.95 / 0.65 pp), and 805 / 1,079 / 1,056 tasks have a wage but **no** classified cell
(2.03 / 2.57 / 2.58 pp) — those are tasks whose intersection rows are entirely
`none`/`not_classified`, and they must be dropped explicitly, never `fillna(0)`.

**Kish effective N, checked as the brief asks.** `n/(1+cv²)` on `onet_task_pct`:

| wave | nominal named | Kish (all named) | nominal analysis set | Kish (analysis set) | Kish by wage quartile Q1→Q4 |
|---|---|---|---|---|---|
| Aug 2025 | 2,616 | **99.7** | 1,802 | **94.4** | 62.3 / 43.3 / 22.2 / **13.7** |
| Nov 2025 | 3,168 | **89.5** | 2,075 | **83.4** | 55.6 / 37.7 / 22.0 / **11.5** |
| Feb 2026 | 3,258 | **134.3** | 2,188 | **125.7** | 51.0 / 50.6 / 36.8 / **16.5** |

The brief's expectation ("well below the nominal 2,617 / 3,169 / 3,259") is confirmed and then
some: the effective N is **3–4% of nominal**, and the top wage quartile — the quartile the
headline difference depends on — has an effective N of **11.5 to 16.5 tasks**. Quartile
boundaries on usage-weighted wage are $25.78 / $34.6–35.8 / $43.40 in every wave (Q4 = $43.40 to
$100.00/hr), and each quartile holds 199k–248k classified conversations.

**H1 / H2 (price gradient, either sign) — data exists at the grain and coverage assumed.** The
three global frames, the same-wave weights, the wage and the five-pattern base are all in place
and the estimator is the one Anthropic's own released code implements. Caveats: the wage is an
occupational aggregate for work that *resembles* the task (`ATLAS` §Traps 36), the Nov wave's
top-quartile rates carry unremovable Seychelles contamination (C8), and the augmentation-component
test H2 requires the three augmentation patterns separately — they are present as distinct
patterns in every task's intersection row set, so that test is feasible as written.

**H3 (composition, not price) — feasible, but two of its three legs need restating.**
`soc_major_group` gives all **22** major groups plus a 23rd bucket for the 6 / 10 / 9 tasks whose
holders span groups (assign or drop them by a stated rule — they are 0.26–0.29 pp).
SOC-15 is **39.86 / 37.12 / 33.11%** of analysis mass, so "exclude SOC-15" removes a third of the
sample: the leave-one-group-out series is dominated by that one leave-out by construction, which
is what H3 predicts and also what makes it weakly diagnostic. The **22 leave-one-group-out
re-estimates** are feasible (all 22 groups present; 17 / 18 / 20 have ≥20 tasks; 12 / 11 / 11 hold
≥1 pp of mass), but the **within-major-group estimator is not identified in 22 groups**: only
**10 / 10 / 8** groups contain tasks in both the global bottom and top wage quartile, and only
**7 / 8 / 6** span all four. §9(3)(b) should say "averaged over the groups that span the quartiles
(7 / 8 / 6 of 22)" or define quartiles within group.

**H4 (the null) — feasible only under a named variance model, and under the brief's own bootstrap
it is not.** This is the one place the design does not deliver what §9(4) promises. Three
defensible variance models for the top-minus-bottom difference, all computed on the analysis set:

| variance model | SE, Aug / Nov / Feb | MDE(80%, two-sided 5%) = 2.8×SE | resolves ±3 pp? |
|---|---|---|---|
| (a) conversation-level binomial on the classified counts | 0.151 / 0.148 / 0.154 pp | **0.42 / 0.42 / 0.43 pp** | yes |
| (b) design-based: resample **tasks** equal-probability, recompute the usage-weighted mean | 4.46 / 6.22 / 5.75 pp | **12.5 / 17.4 / 16.1 pp** | **no** |
| (c) the brief's literal §9(4) spec: resample tasks with **p ∝ usage weight**, unweighted mean | 1.164 / 1.228 / 1.313 pp | **3.26 / 3.44 / 3.68 pp** | **no** |

The spread is not a detail: (a) treats the task mix as fixed and the conversation as the sampling
unit; (b) treats the task as the sampling unit, and then the effective N of 11.5–16.5 tasks in Q4
dominates everything (task-level sd of the automation share is 27–31 pp, so sd/√Kish is
7.1–7.9 pp in Q4 alone); (c) is the hybrid the brief writes and sits just above the ±3 pp band.
So: H1/H2 are testable against a 3 pp signature under (a) and (c) but not (b); **H4's null is
reportable only under (a)**, and under the brief's own wording the result would have to be
reported as "underpowered", which §9(4) foresees but the brief's §12 null paragraph does not.
Recommendation for the pre-registration: name (a) as primary with the task mix explicitly held
fixed (it is the right model for a statement about *this* window's conversations), report (b) as
the generalisation-to-other-task-mixes bound, and set the indifference band or the null claim
accordingly.

---

## 5. Traps that apply

| trap (`data/ATLAS.md`) | where it bites this brief |
|---|---|
| §Traps 1, 2, 6 — `NA` is Namibia; `NONE` is a real `geo_id` in 2026-03-24; `level` dtype differs between Parquet siblings | every load in §8; irrelevant to a global-only cut only if `geography` is filtered first, which the C1–C4 commands do |
| §Traps 24 — `none` ≠ `not_classified` | C1–C4 and §8(ii): three different residuals (task node, pattern in the marginal facet, pattern in the intersection) and they do not agree |
| §Other bases — intersection `_pct` is a share of its **base cluster** | §9(1): per-task shares may never be summed across tasks; weight them |
| §Conventions — the automation base changes by wave *and* chapter | §8's replication list and every table in §9: the five-pattern base is the analysis base, the all-conversation base is the published one |
| §Traps 10 — `MedianSalary` mixes hourly and annual; `-1` sentinels | C6, and the JobZone leg of the exploratory allowance |
| §Traps 21 — case-variant task duplicates create a silent many-to-many | C5; de-duplicate on the key **before** the merge (one collapsing pair in this file, 34 rows on one key) |
| §Traps 14 — Seychelles is in the file and not in the report | C8 and §10; and see §1 above: the rates cannot be cleaned |
| §Traps 13 — Utah, Aug 2025 | §10's claim that it cannot move a global intersection materially is right (it is a `state_us` row and the intersection is global), so the sentence stands as written |
| §Traps 25 / §Thresholds — absent ≠ zero, no suppression flag | §9(4) and §10's count floor: the 805 / 1,079 / 1,056 wage-but-no-classified-cell tasks must be dropped, not zeroed |
| §Traps 36 — occupation is inferred from the task, not the user | §7(3) — already handled, and the wage inherits it |
| §Traps 27b / §Cuts 7 — no time dimension inside a release | §10's "never pooled, never spliced" is the only available reading of "three waves" |
| §Cuts 10 — intersections are global only | C8's netting limit, and the reason there is no geographic version of this post |
| §Traps 31 — the released library needs `chdir` into `code/` and imports `geopandas` at module scope | §2's replication; stub the import |
| §Conventions — top-10 concentration is **not** renormalised | §10 quotes "19.4% of Feb-2026 named usage": 19.4410 is of the wave total; of *named* mass it is **20.9107%** (Aug 22.9409 / 24.97%, Nov 24.2471 / 25.93%) |

---

## 6. Verdict

**FEASIBLE WITH CAVEAT.**

Every frame the brief needs exists at the grain it assumes: `onet_task::collaboration` at
`geography == 'global'` with both `_count` and `_pct` over 2,617 / 3,169 / 3,259 base tasks in the
three long waves, same-wave `onet_task_pct` weights summing to exactly 100, a wage on
99.35 / 98.98 / 99.30% of named-task mass, and an estimator that Anthropic's own released code
implements and that reproduces Figure 2.11 exactly (−3.111834 / 0.393687 / N 111). Four things in
§8 need amending, and one of them changes a decision rule. **(1) C6's join key is wrong**:
`wage_data.SOCcode` is a 10-character O\*NET-SOC code, so `O*NET-SOC Code[:7]` matches nothing;
the key is the full 10-character code, as in Anthropic's `plots.ipynb`, and the coverage figures
in the brief's verbatim line are the ones that key produces. **(2) C8's `geo_id` is wrong** —
Seychelles is `SC`, not `SYC`, in this ISO-2 wave — and the netting can only reach the task
weights: intersections are global only, so the November per-task automation rates cannot be
cleaned of a geography that is up to 64% of an individual task's global count and holds 9.04 pp of
the top wage quartile. **(3) C4's residual nodes are `none` *and* `not_classified` in the base
facet but only `none` in the intersection**, and the intersection carries a `not_classified`
*pattern* worth 4.6–5.9% of named counts that the marginal facet does not — which is why §8(ii)'s
internal check returns the wave value to **+0.13 / +0.29 / +0.35 pp** rather than "within
rounding"; the check passes, the stated tolerance does not. **(4) the ±3 pp null in §9(4) is not
deliverable under the bootstrap §9(4) itself specifies**: MDE(80%) is 3.26 / 3.44 / 3.68 pp under
the brief's "resample tasks with probability proportional to usage weight", 12.5–17.4 pp under a
plain design-based task bootstrap, and only 0.42 pp under a conversation-level model — the Kish
effective N is 99.7 / 89.5 / 134.3 against a nominal 2,616 / 3,168 / 3,258, and 11.5–16.5 in the
top quartile. The pre-registration must name one variance model, state its MDE, and either hold
the task mix fixed by construction or widen the indifference band; otherwise the H4 branch can
only be reported as underpowered.

---

## Verification — commands run, 2026-09-16

```bash
cd /workspace/economic_research
for r in release_2025_02_10 release_2025_09_15 release_2026_01_15 release_2026_03_24; do
  python data/fetch/$r.py; done          # 59 files, 355,158,908 B, all sha256 = INDEX.md
for r in release_2025_02_10 release_2025_09_15 release_2026_01_15 release_2026_03_24; do
  (cd data/cache/$r && sha256sum -c CHECKSUMS.txt); done   # 14/38/4/3 OK, 0 failed
python data/replication/post1_cuts_c1_c8.py        # C1-C4, C8, published splits, internal check
python data/replication/post1_joins_c5_c7.py       # C5-C7 audits, wage coverage, multi-holder, Kish N
python data/replication/post1_variance_mde.py      # three variance models, SOC groups, API cut
python data/replication/post1_replicate_fig211.py  # Anthropic's released library: Fig 2.11
curl -sL https://data.bls.gov/projections/occupationProj    # 200, 1,397,448 B, 831 SOC rows
```

Per-cut one-liners are inline in §1. Full output:
`data/replication/results/post1_feasibility_checks.txt`; the per-task working tables written for
the analyst are `/tmp/p1/tk_{aug2025,nov2025,feb2026}.csv`
(task, key, weight, count, holders, four wage variants, JobZone, automation share, classified
base) — these are scratch, not deliverables, and rebuild in ~3 minutes from the scripts above.
