# post3 (LL-36) — data feasibility

**Owner:** data steward. **Date:** 2026-09-16. **Brief of record:** `posts/post3/BRIEF.md` (commit
4768455). **Lead's status note:** `room/lead-2026-09-16-brief-post3-status.md`.

Everything below was re-derived today against the cached raw files, not from the atlas. The script
of record is **`data/checks/post3_feasibility.py`** (run: `python data/checks/post3_feasibility.py`,
45 s; writes `data/checks/results/post3_S_series.csv`, `…/post3_C_series.csv` and
`/tmp/post3_feasibility.json`); its numbered sections are cited below as *(script §n)*. The cache
was present and verified (`python data/fetch/supplementary_onet.py` → "0 fetched, 2 skipped, all
sha256 match"). Raw files were read, never written.

Headline: **the "+14% API" leg does reproduce** — at **+14.380%** with Anthropic's own released
function, and at +14.389% with an independent re-implementation — but only on the **2019
O\*NET-SOC recode**, which is not the construction the brief's §8 specifies. Both answers to the
lead's §8 questions are in §2 below.

---

## 1. Cuts confirmed at column level

Read convention applied to every frame: `keep_default_na=False`, and `na_values=[]` for
`release_2026_03_24`; `level` cast to `str` after any parquet read; residual nodes `none` **and**
`not_classified` treated as different things (script §0, `load()` / `global_onet()`).

### Cut 1 — `release_2025_09_15` (4–11 Aug 2025), global `onet_task` L0, both surfaces

| field | value |
|---|---|
| files | `data/cache/release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv` and `…aei_raw_1p_api_2025-08-04_to_2025-08-11.csv` |
| grain | `geography == "global"` (the API file has **no other geography**); `level == "0"` — the only level the facet carries |
| facet | `onet_task` |
| metric columns | `onet_task_pct`, `onet_task_count` (both present, keyed 1:1 on `cluster_name`) |
| threshold | privacy floor **confirmed at exactly 15 conversations**: `min(onet_task_count) == 15` in this and all five other frames. No suppression flag; absent ≠ zero |
| platform labels | `Claude AI (Free and Pro)` / `1P API` |

Command and result *(script §1)*:

```python
g = d[(d.geography=="global") & (d.facet=="onet_task") & (d.level=="0")]
# Claude.ai: 2,618 nodes (2,616 named + none + not_classified), pct sums to 100.0000,
#            residual 8.1273 pct, counts sum 964,494, min 15, max 55,132
# 1P API:    2,056 nodes (2,054 named), pct 100.0000, residual 12.1617,
#            counts sum 944,638, min 15, max 76,618
```

**Verdict: CONFIRMED.**

### Cut 2 — `release_2026_01_15` (13–20 Nov 2025), same cut

Files `…/release_2026_01_15/data/intermediate/aei_raw_{claude_ai,1p_api}_2025-11-13_to_2025-11-20.parquet`
(Parquet siblings written by the fetch script; `level` cast to `str`).
Claude.ai **3,170** nodes (3,168 named), residual **6.4856**, counts **999,875**, min 15;
1P API **2,253** nodes (2,251 named), residual **11.7210**, counts **971,525**, min 15. `pct` sums
to exactly 100 in both. Platform label is still `Claude AI (Free and Pro)` in this wave.
**Verdict: CONFIRMED.**

### Cut 3 — `release_2026_03_24` (5–12 Feb 2026), same cut

Files `…/release_2026_03_24/data/aei_raw_{claude_ai,1p_api}_2026-02-05_to_2026-02-12.parquet`.
Claude.ai **3,260** nodes (3,258 named), residual **7.0286**, counts **1,000,000 exactly**, min 15;
1P API **2,299** nodes (2,297 named), residual **9.7124**, counts **1,000,000 exactly**, min 15.
Platform label `Claude AI (Free, Pro, and Max)`.
**Verdict: CONFIRMED WITH CAVEAT** — the brief's note is right that counts are on a 1,000,000
sample base, and the consequence for this post is that the three waves' count bases are **not
equal** (964,494 / 999,875 / 1,000,000 counted conversations on Claude.ai; 944,638 / 971,525 /
1,000,000 on the API). Any statement about **node counts rising** (H4's signature, §10's node-count
check) is therefore partly a statement about more cells clearing the fixed 15-conversation floor in
a larger counted base. Node counts must be reported beside the counted base, or normalised.

### Cut 4 — `release_2025_09_15` published `soc_occupation` facet (reproduction target)

File `data/cache/release_2025_09_15/data/output/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.parquet`
(the facet exists in the **enriched** file only, Claude.ai only). Facet `soc_occupation`, single
variable `soc_pct`, 23 cluster names = 22 SOC major groups + **`not_classified` only** (there is no
`none` row here, and its 8.1047 differs from the `onet_task` residual's 8.1273 — the two residuals
are not the same object). Published `Computer and Mathematical` = **35.877057** on the
all-conversation base and **39.0412** on the classified base *(script §4)*.
**Verdict: CONFIRMED.**

### Cut 5 — the task → SOC join (brief §8 "Supplementary data")

`release_2025_09_15/data/intermediate/onet_task_statements.csv`, 19,530 × **9** columns, carries
`soc_major_group`; 974 O\*NET-SOC 2010 codes; join key the lower-cased, stripped task text
(18,428 distinct keys after collapsing case variants). Merge audit, every wave and surface
*(script §2)*: rows in **2,616 / 2,054 / 3,168 / 2,251 / 3,258 / 2,297**, matched the same,
**0 unmatched, 0.0000% of named mass unmatched** in all six frames. The brief asked for the
February coverage: it is **3,258/3,258 (Claude.ai) and 2,297/2,297 (1P API)**.
**Verdict: CONFIRMED** (the brief's statement of the November coverage, 3,168/3,168 and
2,251/2,251, is also confirmed).

### Cut 6 — the derived metrics S and C

*S* (category share) behaves as the brief describes, on both bases, and is reported below. **C is
base-invariant**: it is a ratio of SOC-15 mass to SOC-15 mass, so the classified and
all-conversation bases give the *identical* number to every decimal. **Verdict: CONFIRMED WITH
CAVEAT** — §9's instruction to "compute C … on both bases" and §10's "classified and
all-conversation series are reported side by side throughout" are satisfiable only for **S**; for
**C** there is one series, and the base sentence in the caption should say so rather than print the
same number twice. C *is* sensitive to two other choices (allocation rule, O\*NET vintage): see §4.

### Cut 7 — §10's node-set and name-match check

*(script §6)*, on the **named** node sets: Claude.ai Nov↔Feb **2,886** of 3,168 / 3,258 names match,
carrying **99.42% / 99.19%** of each wave's named mass; Aug↔Feb 2,364 of 2,616 / 3,258 (99.27% /
97.31%). 1P API Nov↔Feb 1,930 of 2,251 / 2,297 (98.50% / 97.75%); Aug↔Feb 1,702 of 2,054 / 2,297
(98.13% / 96.37%). **Verdict: CONFIRMED WITH CAVEAT** — the brief's "2,888 of 3,170 / 3,260 …
99.46% / 99.24%" is the same fact counted **with** the two residual nodes on each side; the
named-node version above is the one to quote in a post that drops them. Note also the much weaker
API match (1,702 of 2,054 Aug↔Feb): the cross-wave node set on the developer surface is markedly
less stable than on the consumer surface, which bears on H4.

### Cut 8 — §10's allocation-rule robustness (the LL-32 bound), inputs confirmed

*(script §2 and §5)*. In the shipped 20.1 statements a task text has more than one **holder
occupation** for **74 / 93 / 86** Claude.ai task nodes (Aug / Nov / Feb) carrying **4.44% / 5.98% /
4.87%** of named mass, and **51 / 55 / 57** API nodes carrying 2.11% / 2.07% / 1.80%. More than one
**SOC major group** is far rarer: 6 / 10 / 9 nodes, **0.30% / 0.31% / 0.28%** of named mass
(Claude.ai). Measured movement across four allocation rules (equal split over distinct SOC codes,
over distinct major groups, over distinct occupation Titles, and Anthropic's own full-duplication
rule): **S moves by ≤ 0.18 pp** (max 0.183 pp, API Feb, 2019 vintage; ≤ 0.12 pp on the 2010
vintage) and **C moves by ≤ 0.39 pp** (max 0.387 pp, API Aug, 2010 vintage; ≤ 0.21 pp on Claude.ai).
**Verdict: CONFIRMED WITH CAVEAT** — the ≤ **0.17 pp** bound the brief carries from LL-32 is a bound
on **S**, it is confirmed at that order (≤ 0.18 pp on the exact rule set used here, and the tiny
difference is the fourth rule LL-32 did not test), but it is **not** a bound on **C**, which moves
up to 0.39 pp on the API. §9's arithmetic for δ = 1.0 pp should cite the C figure, not the S figure.
The counts differ slightly from LL-32's "72 / 91 / 84 tasks, 4.05% / 5.57% / 4.50%" because those
were computed after dropping the tasks whose holders are all in one group under a slightly
different key set; the order of magnitude and the conclusion are unchanged.

### Cut 9 — §10's Seychelles handling

**Verdict: DOES NOT EXIST as stated — the brief's premise is wrong in the post's favour.** §8(b)
and §10 assert that Seychelles "cannot be removed at global grain". It can, almost exactly: see §2
below. Nearest (and better) substitute: net Seychelles' published country rows out of the global
task counts and report the corrected November point beside the published one.

### Cuts named in §9's exploratory allowance

Exploratory test 2 (the two next-largest SOC groups): `25` Educational Instruction and Library and
`43` Office and Administrative Support both exist in the rebuild at every wave and surface — but on
the 2010 vintage the API's group 43 is 11.08 / 15.14 / 17.56 and on the 2019 recode 6.66 / 7.21 /
7.17, because `43-9011 Computer Operators` moves **into** group 15 in the 2019 taxonomy
(`data/ATLAS.md` §Conventions, "SOC major groups from `onet_task`, and the 2019 recode"). The
comparison-group test is therefore vintage-defined too. **CONFIRMED WITH CAVEAT.**
Exploratory test 1 (tasks entering/leaving the top ten): names are published, so it is computable;
all ten of Claude.ai's SOC-15 top-ten tasks are also published on the API in every wave, and the
cross-surface SOC-15 node overlap is 270 / 282 / 284 nodes — H2's signature is measurable.

---

## 2. Replication target

**Report and page.** `economic-index-2026-03-report` p.7: "Since August 2025, the share of tasks in
this category has increased by 14% in the API and decreased by 18% in Claude.ai"; with
`economic-index-2026-03-appendix` Figure A.1 (p.5, "Task usage share trends by occupation group
(V1-V5, 2019 O\*NET-SOC)") and its footnote 1 (p.6): "This figure uses 2019 O\*NET-SOC codes, while
previous reports use the 2010 vintage."

**Does Anthropic's released code cover it? Yes — and I ran it.** The August-2025 library ships
`map_to_occupational_categories(df, task_statements, soc_structure)` in
`release_2025_09_15/code/aei_analysis_functions_1p_api.py`. Its rule, in its own comments: map the
lower-cased stripped task text to major groups, "Assign full value to each group (creates
duplicates)", label `none`/`not_classified` as "Not Classified", then "Renormalize percentages to
sum to 100". That is **full duplication on an all-conversation base**, not an equal split, and it
is the specification of the published facet: run on the August Claude.ai frame with the shipped
statements it returns **35.8771** against the published `soc_occupation` value **35.877057**, and a
**0.0000 pp** mean absolute error across all 22 major groups *(script §4b; needs `pip install
plotly`, an import-time dependency of the module)*.

**The reproduction, to the decimal** *(script §4 and §4b; two implementations)*:

| construction (classified base) | Claude.ai Aug → Nov → Feb | Aug→Feb | 1P API Aug → Nov → Feb | Aug→Feb |
|---|---|---|---|---|
| **2019 recode, Anthropic's released function** | 41.9294 → 38.4599 → **34.5867** | **−17.512%** | 53.7272 → 59.0386 → **61.4530** | **+14.380%** |
| 2019 recode, my re-implementation (equal split over 2019 codes) | 41.9682 → 38.5001 → 34.6150 | −17.521% | 53.8833 → 59.2074 → 61.6363 | +14.389% |
| 2010 vintage (the brief's §8 construction), released function | 39.0412 → 36.0309 → 32.2469 | −17.403% | 49.9661 → 51.7242 → 51.5975 | **+3.265%** |
| Figure A.1 axis readings (wiki, ±0.2 pp) | 42.3 → 38.8 → 34.5 | −18.4% | 53.7 → 59.6 → 61.6 | +14.7% |

Published −18% ⇢ reproduced **−17.51%**; published +14% ⇢ reproduced **+14.38%**; published "35% of
conversations on Claude.ai" (p.5) ⇢ reproduced **34.59** (34.62 on the second implementation). The
two implementations agree to **0.01 pp of relative change**. All six Figure A.1 Computer and
Mathematical points land within **0.4 pp** of the published axis readings, and the other seven
panels land too.

**Why the brief's series does not reproduce the API leg.** The brief holds the shipped O\*NET DB
20.1 statements fixed across all three waves (§7(iv)), which is the **2010** O\*NET-SOC taxonomy.
The published figure is on the **2019** taxonomy, under which `43-9011 Computer Operators` and its
tasks move into major group 15; on the API that single move carries 3.83 / 6.92 / **9.32 pp** of
matched mass across the three waves (`data/ATLAS.md`, added 2026-09-16 (i), which also names the
one fast-growing task inside it). So the +14% is a real, reproducible number **about the 2019
taxonomy**, and the brief's +3.3% is a real number about the 2010 one. Both are correct; neither is
quotable without the vintage. A third check, run independently today: re-joining the task text to a
later O\*NET **database** instead of applying the crosswalk (DB 27.3 → 30.2) reproduces the
*direction* but not the level (+12.6% API, −16.0% Claude.ai), because a text join to a newer
database loses ~18–19% of named mass; use the crosswalk, not a later database.

**Consequence for §8 of the brief.** The sentence "and **the API leg does not** [reproduce]" is now
superseded, as is the pre-registered rule built on it ("if no named base reproduces the API leg to
within ±3 pp of relative change…"): a named specification does reproduce it, to 0.4 pp. What
replaces it is a **vintage decision that must be pre-registered before any C is looked at**, because
the vintage is not neutral for this post's own statistic (see §4).

### Answer to the lead's question (a) — the February all-conversation API level, and the base that reproduces +14%

- **February 2026, 1P API, SOC-15, all-conversation base: 46.6134** on the brief's own 2010
  construction with Anthropic's released rule (46.61–46.69 across allocation rules), against
  43.9245 in August and 45.6920 in November — i.e. **+6.12%** Aug→Feb, not +14%.
- On the 2019 recode the same all-conversation series is **47.2322 → 52.1557 → 55.5180** (+17.54%).
- **No base reproduces +14% on the 2010 vintage** (classified +3.27%, all-conversation +6.12%,
  count-weighted identical to the pct version, node-share −5.20%). The base is not the free
  parameter; the **taxonomy vintage** is. On the 2019 recode the **classified** base gives +14.38%
  and the all-conversation base +17.58%, so the published sentence is *2019 vintage, classified
  base* — the same base the published "35%" is on.

### Answer to the lead's question (b) — how much of the November global SOC-15 mass is recoverable from country rows, and the Seychelles bound

*(script §7; the country-grain `onet_task` facet in `release_2026_01_15`.)*

- Global November Claude.ai SOC-15 mass = **337,154 conversations**. Recoverable from country rows:
  **240,822 = 71.43%** of it, across **113 countries** and 205 distinct task names (country rows are
  thin: median 21 of 3,170 task nodes per country).
- **Seychelles does not need bounding — it can be netted out almost exactly.** Its country task rows
  are **complete**: 67 rows summing to **24,715** conversations = its published `usage_count` to the
  unit. (This is general in the November wave: for **all 117** countries that publish task rows, the
  task counts sum **exactly** to the country's `usage_count`, because sub-floor cells are folded
  into that country's own residual rows.) Of Seychelles' 23,173 *named* conversations, **19,487
  (84.1%) are SOC-15** — the anomaly is a coding anomaly. It is **5.78% of the entire global SOC-15
  mass** while the country is 2.47% of the sample.
- Netting Seychelles out of the November global mix moves the November point by:
  **S (classified) 36.0583 → 34.8375 (−1.22 pp)**; S (all-conversation) 33.7197 → 32.5759 (−1.14 pp);
  **C 61.1859 → 59.8982 (−1.29 pp)** on the 2010 vintage, and −1.20 pp / −1.28 pp on the 2019 recode.
  The only residual uncertainty is Seychelles' 1,542 unnamed conversations: if every one of them
  were a sub-floor SOC-15 task, S would fall to 34.7272, so the correction is bounded in
  **[−1.33, −1.22] pp**. **Both the size of the Seychelles effect and the correction exceed the
  post's δ = 1.0 pp band**, so the November leg — the placebo leg — must be reported netted, not
  bounded.

---

## 3. Supplementary joins tested

| source | vintage / how obtained | join key | merge audit | coverage against Index units | licence |
|---|---|---|---|---|---|
| O\*NET DB **20.1** task statements | shipped inside `release_2025_09_15/data/intermediate/onet_task_statements.csv` (19,530 × 9, 974 O\*NET-SOC 2010 codes); already in the cache via `python data/fetch/release_2025_09_15.py` | lower-cased, stripped task text (18,428 distinct keys) | rows in 2,616 / 2,054 / 3,168 / 2,251 / 3,258 / 2,297 → **all matched, 0 unmatched, 0.0000% of mass** | 100% of named `onet_task` nodes in all six frames | O\*NET CC BY 4.0, redistributed under Anthropic's dataset card ("CC-BY", no version) |
| O\*NET-SOC **2010 → 2019 crosswalk** | `https://www.onetcenter.org/taxonomy/2019/walk/2010_to_2019.csv?fmt=csv` via `python data/fetch/supplementary_onet.py`; sha256 `8f026a33…`, 108,052 B, 1,164 rows | 2010 O\*NET-SOC code | 19,530 (key, 2010-code) pairs in → **20,081 out, 0 unmatched**, all 974 codes matched, 917 distinct 2019 codes; 337 pairs change major group | needed for the published figure, not for the post's own series | O\*NET Center, CC BY 4.0 |
| O\*NET DB **30.2** text zip (corroboration only) | `https://www.onetcenter.org/dl_files/database/db_30_2_text.zip`, 200, 13,444,123 B, sha256 `b547927193…`; also checked 27.3 / 28.2 / 29.2 / 30.0 | task text | 2,173 / 1,722 / 2,635 / 1,887 / 2,703 / 1,931 of the named nodes match, **81.5% / 80.8% of named mass** (i.e. ~18–19% lost) | **not usable as the primary join** — use the crosswalk | O\*NET Center, CC BY 4.0 |

No other supplementary source is named in the brief, and none is needed: there is no population,
GDP, wage or employment join in this design. (The employment-weighted allocation rule cited from
`posts/post1/BRIEF.md` §8 would need BLS Employment Projections; `data.bls.gov/projections` is
reachable, `www.bls.gov`/`download.bls.gov` are 403 from this sandbox. For this post the rule
matters at ≤0.39 pp on C, so it is robustness, not construction.)

---

## 4. Hypothesis by hypothesis

**Unblinding notice, for the referee and the director.** Computing effective N and checking that
the top-ten construction is well defined required computing C itself. The three-wave C series for
both surfaces, both vintages, four allocation rules, the fixed-August-basket variant and the SOC-15
TVDs are in **`data/checks/results/post3_C_series.csv`** and `/tmp/post3_feasibility.json`. I have
deliberately not printed ΔC in this note. Three **structural** facts about it bear on the design and
must be settled in the pre-registration, before the values are read:
(i) C is base-invariant (§1, cut 6);
(ii) **ΔC on the API changes sign between the 2010 vintage and the 2019 recode** — so H4's
confirmatory test is decided by a construction choice the brief has not yet pre-registered;
(iii) **the Aug→Nov and Aug→Feb legs of ΔC on Claude.ai do not agree in sign**, which under §10's own
persistence rule downgrades the T1 finding to descriptive. The lead and the referee should decide
whether the confirmatory test survives as confirmatory now that a steward thread has seen it, or
whether the design changes (my recommendation: pre-register the vintage and the Seychelles-netted
November point, and treat T1's headline as the Aug→Feb leg with the placebo reported beside it,
exactly as §10 already says — the design is unchanged, only its reporting rule is now load-bearing).

**Effective N and power** *(script §5)*. SOC-15 conversations per wave (equal-split allocation,
2010 vintage): Claude.ai **346,207 / 337,154 / 299,950**; 1P API **415,574 / 444,509 / 466,863**
(2019 recode: 371,883 / 359,986 / 321,821 and 447,098 / 507,794 / 556,499). Binomial SE on C:
**0.083 / 0.084 / 0.091 pp** (Claude.ai) and 0.073–0.076 pp (API) ⇒ SE(ΔC) ≈ **0.12 pp**, MDE
(2.8 × SE) ≈ **0.35 pp**, an order of magnitude inside δ = 1.0 pp. §9's "if it implies a standard
error above 0.33 pp, δ is raised" is therefore **not triggered** on sampling error. SOC-15 **node**
counts per wave: Claude.ai 330 / 342 / 352, API 299 / 323 / 317 (2019: 331 / 344 / 348 and
298 / 318 / 313).

Three caveats on that power statement, all of which the post must carry:
1. the counted bases differ (964,494 / 999,875 / 1,000,000 on Claude.ai), and the February file's
   counts are a scaled 1,000,000 base, so these are sample SEs, not population SEs;
2. conversations are not independent draws and **no unit identifier exists in any release**, so no
   clustered or design-effect-corrected error can be computed — the true interval is wider by an
   unknown factor, and an equivalence claim must say so;
3. the binding uncertainty is **construction, not sampling**: the allocation rule moves C by up to
   **0.39 pp** and the O\*NET vintage by several points. A 1.0 pp equivalence interval that covers
   only sampling error would be a false precision.

**H1 / H2 / H3 (Claude.ai, T1).** Data exist at the grain the design assumes: three waves of global
`onet_task` L0 `onet_task_pct` with a complete SOC join, 330–352 SOC-15 nodes per wave, ~300–346k
conversations behind the category. *Caveats:* the November point is contaminated by Seychelles at
−1.22 pp on S and −1.29 pp on C and must be netted (§2b); C is one series, not two (base
invariance); H3's equivalence test is powered against sampling error only (above); and the
"equivalence interval excluding ±1.0 pp" must be built from an interval the design can defend —
I recommend the interval carry the allocation-rule spread and the Seychelles correction as an
explicit construction term, not a clustered SE that cannot be computed.

**H1's signature** (C rises while the published whole-universe concentration falls) is available:
the published whole-universe series is reproducible from the same files (`data/ATLAS.md`
§Conventions: Feb Claude.ai 19.4410 → "19%", API 32.5729 → "33%", un-renormalised, `none` and
`not_classified` dropped) — but note the denominators differ, as §7(ii) already says.

**H2's signature** (the tasks that leave the Claude.ai top ten are large on the API) is computable:
cross-surface SOC-15 node overlap is **270 / 282 / 284** nodes and all ten Claude.ai SOC-15 top-ten
tasks are published on the API in every wave. *Caveat:* task names are shared only where both
surfaces clear the 15-conversation floor; the overall cross-surface node overlap is 1,603 / 1,823 /
1,908, so absence from the API list is a floor statement, not a zero.

**H3's signature** (SOC-15 TVD no larger than the rest of the universe) is computable on the
name-matched node sets — 312 common SOC-15 nodes Aug↔Feb on Claude.ai (99.9% / 99.6% of each wave's
SOC-15 mass) against 2,054 common nodes outside it (98.9% / 96.2%). *Caveat:* a TVD on unequal node
counts is not scale-free; report both TVDs on their common sets and state the node counts.

**H4 (1P API, T2).** The statistic exists and the API's SOC-15 category is larger than Claude.ai's
(415–467k conversations). Three caveats, all material:
1. **the vintage decides the sign** of the API's ΔC (above), and the published mechanism sentence
   this hypothesis tests is itself from the 2019-vintage figure;
2. the API's **node count** is the weakest part of the signature: the counted base grows 944,638 →
   1,000,000 across the window, so more cells clear the fixed floor mechanically, and the API's
   cross-wave name match is the worst of the four (1,702 of 2,054 Aug↔Feb);
3. **Claude Code cannot be separated.** The February API file includes it ("This includes data from
   Claude Code.", R5 fn 1, p.11) and no column names a product; the June-2026 boundary, where the
   API series jumps 58.22 → 80.88 on directive share as Claude Code leaves the documented
   population, is the evidence that the composition of "1P API" is not constant. H4's mechanism
   ("Claude Code's agentic architecture splits coding work…") is therefore **not identifiable** from
   these files; the test can show the signature's *shape*, never attribute it to Claude Code. The
   brief says as much in §3; §9's T2 should say it too.

---

## 5. Traps that apply

| trap (`data/ATLAS.md` §Traps unless stated) | where it bites this brief |
|---|---|
| 1–2. `NA` is Namibia; `NONE` is a real pseudo-geography in 2026-03-24 — read with `keep_default_na=False`, `na_values=[]` | §8 conventions (already stated) and every script |
| 7. `level` is a string documented as int; Parquet siblings differ | §8 conventions (already stated) |
| 23–24. `none` ≠ `not_classified`, and the `soc_occupation` facet's residual (8.1047) is not the `onet_task` residual (8.1273) | §8 cut 4; any statement that the rebuild "matches the facet" |
| 25. cluster suppression at the 15-conversation floor, with unequal counted bases across waves | §10's node-count check and H4's node-count signature (cut 3 above) |
| 14. Seychelles, November | §8(b), §10 — and it is **correctable**, not merely boundable (§2b) |
| 36. occupation is inferred from the task, never from the user | §7(ii) (already handled: the post never says "software engineers") |
| Taxonomies: O\*NET vintages differ by folder (20.1 shipped, 27.x, 30.2) and the published occupational figures use the **2019** O\*NET-SOC recode | §7(iv), §8's reproduction target, and — newly — H4's sign (§4) |
| Request clusters are not comparable across waves; `onet_task` names are | §10's name-match check; the post uses task names only |
| June 2026 rebuilt on O\*NET 30.2 with a new classifier and a changed API population | §10's boundary rule (already stated); do not splice |
| 2026-03-24 counts are per million | §8 cut 3; effective N and SE |
| Absent ≠ zero, no suppression flag | H2's "present and large on the API" signature |
| Bases: every `{facet}_pct` includes `not_classified`; the published p.5 "35%" is on the **classified** base despite the words "of conversations" | §8's two-base rule, and §2 above |

---

## 6. Verdict

**FEASIBLE WITH CAVEAT.**

The three cuts the brief names exist exactly as specified, at column level, on both surfaces, in all
three waves, with a complete task → SOC join (0 unmatched in 13,644 node-rows) and an effective N of
300–467 thousand conversations per category-wave — enough that sampling error is an order of
magnitude inside the pre-registered 1.0 pp band. Four things must change in §8 before the
pre-registration is written, and the referee should carry all four. **First**, the published "+14%
API" *does* reproduce — at **+14.380%** with Anthropic's own released
`map_to_occupational_categories` and **+14.389%** with an independent implementation — but only on
the **2019 O\*NET-SOC recode**, which is *not* the construction §7(iv) and §8 fix for the post's own
series; the −18% leg reproduces on either vintage (−17.51% / −17.40%), and the p.5 "35%" reproduces
at 34.59. §8's "the API leg does not [reproduce]" and the ±3 pp stop rule built on it are
superseded, and the post's first published arithmetic should be the vintage pair, not a
non-reproduction. **Second**, the vintage is not neutral for the post's own statistic: it changes
the sign of the API's ΔC, so H4 is decided by a construction choice that must be pre-registered
before the values are read (and a steward thread has now seen them — see the unblinding notice in
§4). **Third**, Seychelles *can* be removed from the November global mix, near-exactly: the
correction is −1.22 pp on S and −1.29 pp on C, larger than δ, so §10's "state the bound" becomes
"report the netted point". **Fourth**, C is base-invariant, so the two-base rule applies to S alone,
and the ≤0.17 pp allocation bound is a bound on S (confirmed at ≤0.18 pp here); the corresponding
bound on C is **≤0.39 pp**, which is what §9's δ arithmetic should cite.

Room note to the lead: `room/steward-2026-09-16-feasibility-post3.md`.
