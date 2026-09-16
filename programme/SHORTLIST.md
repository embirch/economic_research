# Short-list — scoring and sketches

Session 1.3, Step 2. Owner: programme lead. Input: the 39 surviving candidates in
`programme/LONGLIST.md` at commit `2eff78a`, each carrying a steward feasibility line verbatim.
Nothing here changes any surviving entry's question or contribution; where scoring exposed a defect it
is named in that candidate's rationale and left for the referee (director's Step 2 instruction).

## 1. The rubric, fixed before scoring

Six dimensions, each 1–5, anchors below. **Aggregation: unweighted sum**, maximum 30. Unweighted is
chosen deliberately: any weighting would embed a judgement about what this programme is for that the
referee cannot audit from the file, whereas an unweighted sum lets a reader re-derive the ranking
from the six columns and disagree about one column at a time. Weighting was considered and rejected
for that reason.

**Stated tie-break order**, applied before any diversity consideration: (1) *What it teaches*,
(2) *Feasibility*, (3) *Foundation in usage data*. Only if all three tie may the diversity
tie-breaker be used, and only within two points of the cut line, and every use is written down in
§4.

### ORG — originality against the corpus
- **5** The question is asked nowhere in the corpus and nowhere in the external literature checked, and the measure it needs does not yet exist in either.
- **4** The corpus poses it and leaves it open; no external work does it on comparable data.
- **3** An Anthropic publication or an external work does something adjacent on different data or a different platform.
- **2** A close external analogue exists on comparable data; our version is a variation.
- **1** Substantially done somewhere already.

### FIT — fit with the threads map and the mentor's stated interests
- **5** Sits on a thread the stream is actively pursuing **and** on a quoted ⟨mentor⟩ passage in one of his own Anthropic publications.
- **4** Active thread, with a mentor passage that is adjacent rather than central.
- **3** Active thread, mentor interests "none".
- **2** A quiet corner of a thread.
- **1** Off the map.

### FOUND — foundation in usage data
- **5** Stands entirely on the Economic Index releases; no external series needed.
- **4** Index releases plus a reference file shipped **inside** a release (population, GDP, O\*NET, wages).
- **3** Index releases plus one external series, with the Index carrying the comparison.
- **2** Index plus several externals, or an external series carries the comparison.
- **1** The Index is decoration.

### FEAS — feasibility, read off the steward's line
- **5** FEASIBLE, with a generous unit count and no convention in doubt.
- **4** FEASIBLE with a modest unit count, or FEASIBLE-WITH-CAVEAT where the caveat does not touch the test.
- **3** WITH CAVEAT that constrains the design but leaves the test intact.
- **2** WITH CAVEAT that bites power, resolution or interpretability.
- **1** WITH CAVEAT that removes the test (nothing scored 1 survives; LL-34 was deleted at this point).

### TEACH — what an Institute economist learns, either way
- **5** Moves a published Anthropic number or a load-bearing construct in either direction, and changes a decision, a model input or a measurement practice.
- **4** Bounds a load-bearing construct, or supplies a measure the stream says it needs.
- **3** Adds a measurement the corpus lacks, without moving a published number.
- **2** Adds detail to something already understood.
- **1** Internal interest only.

### RISK — inverted, so lower risk scores higher
- **5** The main risk is data-shaped and the steward has already measured or bounded it.
- **4** Risk named and bounded; the post survives it intact.
- **3** Risk material; mitigation pre-registered and sufficient.
- **2** Risk could turn the post into an awkward null, or shift its object mid-flight.
- **1** Risk could invalidate the design.

## 2. Scores, all 39 survivors

Columns: ORG · FIT · FOUND · FEAS · TEACH · RISK · **Σ** (max 30). Rationale names the decisive
dimension.

| ID | question (short) | ORG | FIT | FOUND | FEAS | TEACH | RISK | Σ | decisive dimension, and why |
|---|---|---|---|---|---|---|---|---|---|
| LL-07 | Is AI delegated more on cheap or expensive work? | 5 | 5 | 4 | 5 | 5 | 4 | **28** | FEAS+RISK: the ledger says the wage × collaboration cross is published nowhere, and the steward found 99% wage coverage over three waves with the multi-holder worry bounded at ≤0.17 pp. Nothing else scores this well on both feasibility and stakes. |
| LL-11 | Do tasks growing on the API shrink on the consumer surface? | 5 | 5 | 5 | 5 | 5 | 3 | **28** | FIT: it is the mentor's own stated leading indicator, asserted in two reports and measured nowhere, and 1,241 tasks appear in all six frames. Risk is the share-versus-level accounting. |
| LL-09 | Does measured success predict what people keep bringing to AI? | 5 | 4 | 5 | 5 | 5 | 3 | **27** | TEACH: Anthropic named prediction as the validation that counts for its primitives and never ran it; a 2,427-task panel carrying 92% of mass makes it runnable. |
| LL-31 | Does what people take away from AI depend on where they are? | 5 | 4 | 5 | 5 | 4 | 4 | **27** | ORG+FEAS: no other provider publishes an artifact taxonomy, the sixth report declined its own cut, and 114 countries plus 536 subregions carry all 32 metrics in both months. |
| LL-36 | Is coding still the leading edge of AI use, or just its largest share? | 4 | 5 | 5 | 5 | 4 | 4 | **27** | FEAS: the reconstruction reproduces the published facet to 0.02 pp and both published bases come out, so the corpus's most-quoted series can be decomposed with the base named. |
| LL-01 | Do places using AI more use it more autonomously, or is that income? | 5 | 5 | 5 | 4 | 4 | 3 | **26** | ORG: the stream's only explicit "more research is needed", still open, on the one wave that ships the AUI, GDP and automation together (114 countries). |
| LL-22 | How much of a month's local AI-use pattern is real? | 5 | 4 | 5 | 3 | 5 | 4 | **26** | TEACH: it makes every geographic claim in the corpus — and in this programme — auditable, and the steward has produced both the state and country legs. |
| LL-39 | When the ruler changed, did AI use change with it? | 5 | 4 | 5 | 4 | 5 | 3 | **26** | TEACH: the appendix's own load-bearing omission, and the steward supplied a three-tier list of which metrics cross the June boundary, which is the post's spine. |
| LL-02 | Does observed use support the automation share the scenario model assumes? | 4 | 4 | 5 | 4 | 5 | 3 | **25** | TEACH: it disciplines a published parameter of the Institute's public model; the construct mismatch (conversation, not task) is the ceiling on the claim. |
| LL-18 | Where is AI doing work people could not do alone? | 5 | 4 | 4 | 5 | 4 | 3 | **25** | ORG: the corpus's one substitution primitive, measured at three grains and used in nothing; 115 countries clear the floor in both waves. |
| LL-12 | Is AI use getting broader, or is the same work recurring? | 4 | 4 | 4 | 5 | 4 | 4 | **25** | FEAS: identical privacy floors and denominators within 3.7% make the three long waves like-for-like, so the first paper's fork can be scored without the cumulative artefact. |
| LL-16 | Does AI's own description of requests match the taxonomy used to measure it? | 5 | 4 | 5 | 4 | 4 | 3 | **25** | ORG: an 18-month-old promised comparison that only Anthropic's file enables; the steward settled the flag and measured the gap (49.2% of v2 mass reached). |
| LL-20 | Does AI work less well where it is used most? | 4 | 4 | 4 | 5 | 4 | 3 | **24** | FEAS: success exists at country grain in both waves for 115 countries; the 21–27% `not_classified` share is the thing that could drive the gradient. |
| LL-24 | Do retraining programmes train people for the work AI already does? | 5 | 5 | 3 | 3 | 5 | 3 | **24** | FIT+TEACH: the mentor's own review never asks it and the $200M Fund's Priority 2 turns on it; FOUND and FEAS are held down by a hand-coded destination list against a 54%-zero distribution. |
| LL-30 | Is the work AI does for work the same work it does for study? | 5 | 4 | 4 | 3 | 5 | 3 | **24** | TEACH: every occupational claim rests on a corpus more than half of which is not work, and the work-only occupational mix is published nowhere; the cut is global-only. |
| LL-33 | What is the tenth of enterprise AI use that is neither delegated nor collaborative? | 4 | 4 | 5 | 4 | 4 | 3 | **24** | TEACH: the API residual runs 10.21 → 11.04 → 15.19, the same order as the automation fall the fifth report reports, which matters to every external user of that ratio. |
| LL-37 | What would an early-warning signal built on usage data fire on? | 5 | 5 | 4 | 3 | 5 | 2 | **24** | RISK is the binding column: the Institute's most repeated promise, but no outcome series ships, so predictive validity is unreachable and the post can only measure persistence. |
| LL-41 | Does the threshold behind the published productivity number survive being moved? | 4 | 4 | 5 | 4 | 4 | 3 | **24** | TEACH: the steward's sweep already shows near-invariance (11.93× → 11.59×), which relocates the published 1.8pp → ~5pp swing to the weighting step — a finding, but a narrower one than the entry first supposed. |
| LL-42 | Is the income gradient in AI use about intensity or about mix? | 4 | 4 | 5 | 4 | 4 | 3 | **24** | FOUND: everything sits inside one wave at N = 116 after the steward corrected the entry's premise; the two components are jointly determined, which caps TEACH. |
| LL-05 | Is the geography of Claude usage the geography of AI usage? | 4 | 4 | 3 | 4 | 5 | 3 | **23** | TEACH: it tests whether every ranking claim in the geography thread is about AI or about Claude; FOUND is 3 because the external series carries half the comparison. |
| LL-08 | Is AI used most for the work it speeds up most? | 4 | 4 | 5 | 4 | 4 | 2 | **23** | RISK: both variables come from the same estimator on the same transcripts, so a positive elasticity has an estimator reading the placebo may not separate. |
| LL-10 | How fast is AI use converging across US states, and how wide is the band? | 4 | 5 | 4 | 3 | 5 | 2 | **23** | RISK: four windows and 51 units, with the fourth an unweighted mean of two unweightable months; the band may span "no convergence" to "two years" — reportable, but an awkward headline. |
| LL-23 | Do Anthropic's own exclusion rules change its published geography? | 4 | 4 | 5 | 3 | 4 | 3 | **23** | FEAS: five of six quantities reproduce under both samples, but no AUI or Gini carries a sampling interval, so only movements above the 0.7–0.9 pp rebuild error can be read. |
| LL-29 | Do people do one thing at a time with AI, and does it change what they get? | 4 | 3 | 5 | 5 | 3 | 3 | **23** | FEAS: clean at every grain in both waves; TEACH is 3 because it bounds a unit ambiguity rather than moving a published number. |
| LL-35 | Do places that started using AI earlier get more out of it? | 4 | 5 | 4 | 4 | 4 | 2 | **23** | RISK: the early-adoption proxy is collinear with income and with the tech-worker share, so a positive result has three readings on 113 countries. |
| LL-03 | Does usage-based exposure rank occupations as workers' own reports do? | 4 | 5 | 3 | 2 | 5 | 3 | **22** | FEAS: the rank test collapses to 90 SOC minor groups with a median of 60 respondents, and the broad-group version is excluded by rule — high stakes, thin instrument. |
| LL-21 | Does enterprise AI use respond to price, or to what the model costs to run? | 5 | 4 | 5 | 2 | 4 | 2 | **22** | FEAS+RISK: the indices are re-based to mean 1.0 within each wave and only the first wave ships counts, so no level travels and the design collapses to three cross-sections. |
| LL-27 | Is AI delegated the same way everywhere inside one country? | 4 | 4 | 5 | 2 | 4 | 3 | **22** | FEAS: the decomposition's real N is 32–36 countries with five or more surviving sub-national units, not the 109–125 the grain suggests. |
| LL-38 | Which of the scenario model's parameters can usage data discipline? | 4 | 4 | 4 | 3 | 5 | 2 | **22** | RISK: the steward named two further observable dials, taking the post to six, which is exactly the sprawl lesson 5 records; the audit table is worth having, the scope is not yet safe. |
| LL-06 | Did AI use spread to new tasks, or to new countries? | 4 | 4 | 5 | 2 | 4 | 2 | **21** | FEAS: a country's named task mix covers only about 30% of its conversations, with the residual at a median 66–71%, so the within-country component may be measuring classifiability. |
| LL-13 | Do the economic primitives predict where AI use grows next? | 4 | 3 | 5 | 4 | 3 | 2 | **21** | TEACH: the only available outcome is usage growth itself, which is a weak test of the validation Anthropic asked for, on one three-month step. |
| LL-26 | Has AI use moved up or down the occupational wage ladder? | 4 | 5 | 4 | 2 | 4 | 2 | **21** | FEAS: the published $49.3 level does not reproduce under any of five wage constructions, so the post becomes a change decomposition whose first result is the non-reproduction. |
| LL-04 | Are the tasks people bring to AI the tasks workers say AI helps with? | 5 | 4 | 3 | 2 | 4 | 2 | **20** | FEAS: only 64.4% of task mass reaches an RPS-covered DWA and the median survey cell holds 13 respondents, so the comparison may reduce to a coverage statement. |
| LL-19 | Does AI bring more schooling to the work than the person asking does? | 4 | 4 | 5 | 2 | 3 | 2 | **20** | FEAS: the residual is 0.196 ± 0.209 years against CI half-widths of 0.17, i.e. about the size of its own measurement error — the null branch is the likely branch. |
| LL-28 | Does the autonomy measure capture what happens when AI can act? | 4 | 4 | 3 | 3 | 4 | 2 | **20** | RISK: two instruments with no common unit, sample or window; admissible on the never-merge rule, but the claim can only ever be about the measure. |
| LL-14 | Have official employment forecasts begun to price AI exposure? | 3 | 5 | 3 | 3 | 3 | 2 | **19** | ORG+FEAS: the neighbourhood is now crowded (NY Fed and Stanford DEL both use this file), and only one projections vintage is reachable, so a difference cannot be attributed to forecaster updating. |
| LL-17 | Does AI think longer on the work it is handed outright? | 4 | 3 | 5 | 2 | 3 | 2 | **19** | FEAS: two marginals on a release with no counts, 415 tasks with a positive thinking fraction, and 9.8 points of mass lost to `filtered`. |
| LL-15 | Is AI use broad across people or deep among a few? | 3 | 3 | 5 | 2 | 3 | 2 | **18** | ORG: the steward has already computed the answer (ρ = 0.9932, ratio range 0.978–1.087), so the post is a ±9% bound — the weakest survivor, as its own entry says. |
| LL-40 | How much of the world's AI use can the Index actually show? | 3 | 3 | 2 | 3 | 3 | 2 | **16** | FOUND: the internal half is our own atlas restated and the surviving contribution is carried by three external providers' disclosure practices, not by the Index. |

## 3. Ranking

**28** LL-07, LL-11 · **27** LL-09, LL-31, LL-36 · **26** LL-01, LL-22, LL-39 · **25** LL-02, LL-12,
LL-16, LL-18 · **24** LL-20, LL-24, LL-30, LL-33, LL-37, LL-41, LL-42 · **23** LL-05, LL-08, LL-10,
LL-23, LL-29, LL-35 · **22** LL-03, LL-21, LL-27, LL-38 · **21** LL-06, LL-13, LL-26 · **20** LL-04,
LL-19, LL-28 · **19** LL-14, LL-17 · **18** LL-15 · **16** LL-40.

## 4. The cut line, and every tie-break used

**Cut line: Σ ≥ 25, taking ten.** Eight candidates sit at 26 or above and are in on score alone:
LL-07, LL-11 (28), LL-09, LL-31, LL-36 (27), LL-01, LL-22, LL-39 (26). Four sit at 25 — LL-02,
LL-12, LL-16, LL-18 — and two of them are taken, which is where the tie-breaks apply.

**Tie-break 1, on the stated order (TEACH → FEAS → FOUND).** Among the four at 25, **LL-02** is taken
on TEACH: it alone scores 5 there, because it disciplines a published parameter of the Institute's
own public model. The other three tie at TEACH 4.

**Tie-break 2, on the stated order, is inconclusive.** LL-12 and LL-18 both score FEAS 5 and FOUND 4;
LL-16 scores FEAS 4, so it falls out at the second tie-break. LL-12 and LL-18 tie on all three.

**Tie-break 3, the diversity tie-breaker, used once and recorded here as required.** LL-12 and LL-18
are one point above the cut line, so the diversity tie-breaker is admissible. It is applied on **data
cut**, not on thread: LL-12's frames (global `onet_task` node counts and the task-share Lorenz curve)
are already represented three times in the top nine, by LL-36, LL-39 and LL-22, whereas LL-18's cut —
a categorical primitive at all three geographic grains — appears nowhere else in the short-list.
**LL-18 is taken as the tenth; LL-12 is the first reserve.** No other diversity consideration was
used anywhere in this ranking, and no candidate below 25 was promoted for any reason.

**Short-list, ten:** LL-01, LL-02, LL-07, LL-09, LL-11, LL-18, LL-22, LL-31, LL-36, LL-39.
**First reserve:** LL-12 (25), then LL-16 (25).

Thread spread of the ten, for information and not as a criterion: T1 in five, T2 in four, T3 in four,
T4 in five, T8 in three, T7 in one, T11 in one. **T5, T6, T9 and T10 are absent from the short-list.**
T9's absence is structural and was reported at Step 1; T5, T6 and T10 have survivors that scored 19–24
(LL-03, LL-24, LL-35, LL-37 are the strongest), and none reached the cut on score. The diversity
tie-breaker was **not** used to promote them, because all four sit more than two points below the cut
line — LL-24 and LL-37 at 24 are one point below, and were considered under tie-break 3: they lose to
LL-02 on TEACH only because LL-02 also scores 5, so the comparison fell to score alone, where 24 < 25.
If the director wants a labour-market or policy post in the final six regardless of score, that is a
steer for the human at Gate 1a, not a scoring adjustment, and it should name LL-24 (the retraining
targeting question) as the candidate it would promote.

## 5. Pairs among the short-listed that could not both be posts

Stated so the human can pick six coherent posts without discovering the overlap late.

1. **LL-22 and LL-39 — hard pair.** Both are measurement-integrity posts on the June 2026 wave, and
   LL-22's April-versus-May persistence *is* the within-wave replication that LL-39's admission rule
   requires. Either one would carry the other's headline ("how much of this wave can be believed").
   Pick one; if LL-39 is picked, its April–May agreement requirement absorbs LL-22's method, and if
   LL-22 is picked, the boundary list becomes one of its sections.
2. **LL-11 and LL-36 — hard pair.** The steward judged them separable, and as questions they are
   (migration between surfaces; composition inside a category). But both would headline the same
   series — coding's share on Claude.ai against the API across the three long waves — and a reader
   would receive one story twice. Pick one and let the other's frame appear inside it.
3. **LL-01 and LL-18 — soft pair.** Different measures (automation share; the could-do-alone
   primitive) on different waves, but the same shape: a primitive across places against income and
   adoption. Two posts in that shape would read as one theme. Separable if one is written on the
   2025-09-15 income axis and the other on the 2026 per-capita axis, which is how the entries stand.
4. **LL-02 depends on LL-39** rather than duplicating it. LL-02's seven-window automation series
   crosses the June boundary that LL-39 exists to characterise. If LL-02 is picked without LL-39, it
   must carry LL-39's finding for the collaboration facet — which the steward has already supplied
   (the facet is the taxonomy that never changed) — as a stated precondition.
5. **LL-31 leans on LL-22's rule.** LL-31's both-month admission rule and `pct ≥ 0.5` floor come from
   the same audit as LL-22. Not a duplication, but if LL-22 is not written, LL-31 must state the rule
   itself rather than cite it.

## 6. One-page sketches

Ten sketches follow, in short-list order, each in the fixed section order the director set. No
hypothesis appears here that is not already in the candidate's `programme/LONGLIST.md` entry, and no
assumptions sweep is attempted: that is the brief's job.

---

### LL-01 (Σ 28 rank 6) — Do places that use AI more use it more autonomously, or is that gradient just income?

**Question.** Across countries, is a higher rate of AI use associated with more collaborative and
less delegated use once income is held constant?

**Thread and ledger items.** T2 (geography), with T3. `L-2025-09-R3-25` *open* — the stream's only
explicit "more research is needed"; `L-2025-09-R3-37` *open* (whether the automation–AUI relationship
survives income is untested); `L-2025-09-R3-38` *open* (nor the `not_classified` share);
`L-2025-09-B3-06` *open* ("We're not yet sure why this is").

**Why it matters.** The automation share is the input Anthropic's own scenario model turns into the
labour share, and the policy stream reads rising delegation as the reason to prepare. If the
delegation gradient across places is an income gradient, projecting today's rich-country automation
share onto a diffusing world overstates it. The decision it informs is the Institute's choice of
which automation share to carry into a forward model; the prior it moves belongs to anyone who reads
Figure 2.11 as a cultural fact.

**Contribution.** *If it holds* (the AUI coefficient survives income): the corpus's one open "more
research is needed" gets its first test, and adoption rather than income is what travels with
collaborative use. *If it fails*: Anthropic's flagship geographic interaction is an income
relationship, and every cross-country delegation comparison needs an income control. *If null*: the
minimum detectable slope at this sample is published, showing the −3.112 cannot be separated from an
income effect on one wave.

**Design in brief.** One enriched file, one wave: regress the country automation share on the AUI and
on log GDP per working-age capita, after the published task-mix adjustment, and compare with the
published partial regression. The comparison that carries the finding is the AUI coefficient with and
without income in the same specification. Key number: the AUI coefficient after income enters,
against the published −3.112. Rough detectable effect: at 114 countries a correlation of about 0.26
is detectable at 80% power and 5%, so a halving of the published association would be visible and a
20% attenuation would not.

**Data.** Steward line, verbatim: "**LL-01. FEASIBLE.** `release_2025_09_15` enriched Claude.ai
(4–11 Aug 2025), `geography=country`: `automation_pct` (facet
`collaboration_automation_augmentation`), `usage_per_capita_index`, `gdp_per_working_age_capita`,
`working_age_pop`, plus global `onet_task::collaboration` and `onet_task_pct` — all in one file, one
wave. Of 115 thresholded countries (≥200 conversations), **114 carry AUI, GDP and automation
together**; the loss is PSE (no GDP). Published task-mix specification is N = 111.
`ATLAS §Conventions` task-mix adjustment; log (e) 12." No supplementary source and no join key: this
is the one wave shipping the index, the population and the income series in a single file.

**Overlap with existing work, stated.** `economic-index-2025-09-report` Fig 2.11 p.27 is the same
regression without income; `economic-index-2026-01-report` p.35 replicates the pattern and explains
nothing. Externally, Chatterji et al. (2025) and arXiv 2605.30685 give income gradients in *purpose*,
Bick et al. (2026) give adoption rates, and Misra et al. (2025) give adoption levels — none carries a
delegation measure. The post shares Anthropic's units and its task-mix adjustment, and differs by one
covariate.

**Risks, ranked.** (1) Collinearity: AUI and log income correlate at 0.869, so both coefficients may
lose significance — observed as standard errors roughly doubling when income enters. (2) One wave, so
nothing distinguishes a level relationship from a trend — observed as no way to test the
early-adopter reading. (3) The `not_classified` share varies with country sample size and could drive
the automation measure — observed as the residual share predicting the residualised automation share.

**What it teaches.** Whether the corpus's most striking geographic interaction is about adoption or
about money, and therefore whether a single global automation share can be carried forward.

**The imaginable close.** *Holds*: that the way people work with AI travels with how much they use
it, not with what they earn. *Fails*: that the pattern Anthropic found abroad was a pattern about
income all along. *Null*: that one week of one year cannot separate the two, and what it would take
to.

**Mentor and Institute hooks.** ⟨mentor⟩ "lower income, less educated countries paradoxically
showing more complex use in some cases. The earliest adopters often have high-value, technical use
cases." (`economic-index-2026-03-report`, OQ 13, p.17.) Institute: `ED-1`.

---

### LL-02 (Σ 25 rank 9, taken on the TEACH tie-break) — Does observed AI use support the automation share Anthropic's own scenario model assumes?

**Question.** Is the share of AI use that is delegated rather than collaborative consistent with the
automation share the Institute's scenario model sets by assumption?

**Thread and ledger items.** T11, with T3. `L-2026-09-SCPA-24` *open* (ψ anchored to the one wave
where automation exceeded augmentation, then frozen); `L-2026-09-SCPA-21` *open* (the ψ mapping
asserted); `L-2026-09-SCPA-25` *open* (the two constructs are different objects);
`L-2026-09-SCEX-25` *open* (whether the explorer and the Index agree is never asked).

**Why it matters.** The explorer is the Institute's public instrument for what AI could do to GDP,
wages and the labour share by 2030, and its defence is that its parameters are measurable. One of the
five is measured monthly by the same company, and the measurement has never been carried to the
model. It informs which scenario the Institute treats as central, and it moves the prior of anyone
reading the middle scenario as neutral.

**Contribution.** *If it holds* (the observed share brackets the least disruptive preset): the two
more disruptive presets sit far above anything the Index has recorded, and the post says what would
have to change to reach them. *If it fails* (the observed share rises past the first preset on a
defensible base): the Index is moving toward the middle scenario and the post dates it. *If null*:
the post publishes the base-choice sensitivity table the corpus lacks and states that the parameter
is not currently checkable.

**Design in brief.** Reconstruct the automation share on the five-classified-pattern base across all
seven published windows for Claude.ai and the three pre-June windows for the API, then place the
series beside the model's three presets. The comparison that carries the finding is the observed
range against the preset range. Key number: the maximum observed automation share on the base that
matches the model's conditioning. Detectable effect does not apply in the usual sense — two of the
seven windows publish no counts, so the series is reported as levels with no interval, and the
finding is the distance between a measured range and an assumed one.

**Data.** Steward line, verbatim: "**LL-02. FEASIBLE WITH CAVEAT: the API leg is three waves, not
four, and the 2025-03-27 endpoint carries no interval.** Claude.ai global five-classified-pattern
automation re-verified today across all seven windows: 42.5538 / 43.0619 / 51.0698 / 46.7394 /
45.5456 / 48.9788 / 48.6190 (June equals the published bucket metric to two decimals) — the right ψ
comparator, since that base excludes `none`. 1P API exists in Aug 2025 / Nov 2025 / Feb 2026 only
(86.17 / 83.87 / 79.75); **do not cross into June** (composition break, `ATLAS §Components`). No
counts in 2025-03-27 or June. Log (e) 14." No supplementary series: the presets come from the
published paper and explorer.

**Overlap with existing work, stated.** The paper itself glosses the mapping — chat use against a
world where agentic use is the norm — and the Index publishes the series; nobody has put the two
numbers on one page. Externally, Acemoglu (2025) offers a rival calibration with no usage measure,
and Chatterji et al. (2025) publish a different taxonomy on a different product that has never been
mapped to this parameter.

**Risks, ranked.** (1) Construct: the Index's unit is a conversation and its split is a classifier on
collaboration patterns, while the model's parameter is a share of task instances whose wage bill
moves — observed as a referee refusing the comparison as not like-for-like. (2) Base choice: the
published automation figure changes by wave and by chapter, so a critic can pick a base that moves
the answer — observed as the conclusion flipping between the classified and all-conversation bases.
(3) Claude-only traffic — observed as no way to say anything about AI beyond one provider.

**What it teaches.** Whether Anthropic's own measurement supports Anthropic's own model, and what the
gap between a measured analogue and an assumed parameter is worth.

**The imaginable close.** *Holds*: that the company's own data sits at the gentle end of its own
range of futures. *Fails*: that the data has begun to move toward the middle of that range. *Null*:
that the measure and the parameter are not yet the same kind of thing, and what would make them so.

**Mentor and Institute hooks.** Mentor: none as an author of the scenario work; the series used is
the facet he reports in three waves. Institute: `ED-4`, `ED intro ¶2`.

---

### LL-07 (Σ 28 rank 1) — Is AI delegated more on cheap work or on expensive work?

**Question.** Does the share of AI use that is delegated rather than collaborative rise or fall with
the wage of the work being done?

**Thread and ledger items.** T3, with T4. `L-2025-02-R1-16` *partially answered* (occupation and
category delivered; "the wage cross is published nowhere"); `L-2025-02-P1-22` *partially answered*
(automation share by wage or Job Zone was one join away and is never shown);
`L-2026-09-SCPA-27` *open* (whether the exposure anchor is employment- or wage-bill-weighted is not
stated).

**Why it matters.** Whether delegation rises or falls with the price of the work is the sign of the
first-order labour-share effect in Anthropic's own framework: automating expensive tasks moves a
large wage bill, automating cheap ones moves a small one. The corpus prices the work and prices the
compute, and never says whether the expensive work is the delegated work. It informs the weighting of
every automation-share input to a forward model, and it moves the prior of anyone who reads
"automation share" as if all tasks were the same size.

**Contribution.** *If it holds* (delegation rises with wage): the automation share understates the
wage bill at stake, and the post supplies the wage-weighted version. *If it fails* (delegation falls
with wage): high-wage work is the collaborative work, the observable form of the mentor's
labour-augmenting reading. *If null*: the post publishes the first wage-by-collaboration table in the
corpus with its MDE and states what a global-only intersection can resolve.

**Design in brief.** Take the task × collaboration intersection at global in three waves, attach a
wage to each task through the shipped O\*NET statements and wage file, and estimate the
usage-weighted gradient of the automation share in the task's wage, repeating it in all three waves
so persistence is shown rather than asserted. The comparison that carries the finding is the gradient
in the same wave's own task mix, not across waves. Key number: the automation-share difference
between the top and bottom wage quartile of tasks, usage-weighted. Rough detectable effect: with
2,617 / 3,169 / 3,259 tasks the sampling floor is negligible (a correlation of about 0.05 is
detectable), so the binding uncertainty is construction, not power — which is why three waves and
three allocation rules are all reported.

**Data.** Steward line, verbatim: "**LL-07. FEASIBLE.** `onet_task::collaboration` exists at
`geography=global` in all three long waves with both `_pct` and `_count` over 2,617 / 3,169 / 3,259
tasks, with global `onet_task_pct` weights in the same wave. Wage coverage is near-total, not
marginal: through the shipped O\*NET 20.1 statements to `wage_data.csv` after `MedianSalary > 100`
(1,084 of 1,090 rows), **99.4% / 99.0% / 99.3%** of *named*-task usage mass carries a wage. State the
multi-holder rule (a task's wage is an aggregate over the occupations holding it). Log (e) 7."
Supplementary: `release_2025_09_15/data/intermediate/onet_task_statements.csv` and
`release_2025_02_10/wage_data.csv`, both shipped inside releases; join key is the lower-cased,
stripped task text, then `SOCcode`. BLS Employment Projections median annual wage on `occ_code` is
the second wage source.

**Overlap with existing work, stated.** `economic-index-2026-03-report` Fig 1.4 prices the task mix
and Fig 2.2 sorts model choice by wage; `economic-index-2026-06-report` Fig 2.3 sorts tokens by wage.
The collaboration facet is never crossed with wage in any wave. Externally, Chatterji et al. (2025)
report that work usage concentrates in highly paid occupations without regressing their Asking/Doing
split on a wage, and Tomlinson et al. (2025) correlate wage with an applicability score rather than
with delegation.

**Risks, ranked.** (1) The multi-holder rule: a task held by several occupations has no single wage —
observed as the gradient moving between the three aggregation rules, bounded by the steward at
≤0.17 pp on the SOC-15 share. (2) Wage vintage: a 2019 scrape and a 2025 projections series may
disagree — observed as the two wage sources giving different quartile cuts. (3) Occupation is
inferred from the task, so a task's wage is the wage of work that *resembles* it — observed as
implausible pairings surviving into the top quartile.

**What it teaches.** Which end of the wage distribution AI is being handed outright, and therefore
how much of the wage bill an automation share implies.

**The imaginable close.** *Holds*: that the work people hand over entirely is the expensive work, and
what that implies for who feels it first. *Fails*: that the expensive work is the work people stay
inside. *Null*: that pricing a task and classifying a conversation are still too far apart to join,
and what would close the distance.

**Mentor and Institute hooks.** ⟨mentor⟩ task value as "the average hourly wage of US workers who
perform that task" (`economic-index-2026-03-report`, p.8, fn 5 p.11); ⟨mentor⟩ "more compute is
associated with more valuable artifacts" (`economic-index-2026-06-report`, pp.2–3). Institute:
`ED-7`, and the EPF's measurement ask.

---

### LL-09 (Σ 27 rank 3) — Does AI's measured success rate predict which work people keep bringing to it?

**Question.** Does a task's measured AI success rate in one window predict whether its share of use
grows by the next?

**Thread and ledger items.** T4, with T8. `L-2026-01-R4-25` *open* ("the strongest validation will
come from the primitives' ability to capture meaningful variation in labor market outcomes");
`L-2026-01-R4-37` *open* (task success has no reported validation statistic and carries three
headline results); `L-2026-03-R5-29` *open* (a model judging its own success could produce the tenure
result with no learning).

**Why it matters.** Task success is the most load-bearing and least validated primitive in the
corpus: it halves the published productivity number, reorders effective coverage and carries the
learning-curve result. Anthropic named prediction as the validation that counts and never ran it. It
informs whether chapter 4 of the fourth report and the productivity revision survive, and it moves
the prior of anyone using success as a quality measure.

**Contribution.** *If it holds* (success predicts growth): the primitive earns its first predictive
validation and the post supplies the elasticity. *If it fails*: a measure the model computes about
its own work does not predict what users do next, and three published results inherit that. *If
null*: the post reports the MDE over the matched task set and how many waves the test would need — a
direct input to the Institute's cadence promise.

**Design in brief.** On the tasks common to November 2025 and February 2026, regress the change in a
task's usage share on its November success rate, weighting by usage and instrumenting the initial
level split-sample to absorb mean reversion, with the education primitive as a placebo. The
comparison that carries the finding is high- against low-success tasks' subsequent share growth. Key
number: the share-growth difference between the top and bottom success quartile. Rough detectable
effect: with 2,427 tasks in the regression sample a correlation of about 0.06 is detectable at 80%
power, so the test is sharp enough that a null would be informative rather than merely quiet.

**Data.** Steward line, verbatim: "**LL-09. FEASIBLE.** `onet_task::task_success` at
`geography=global` (`_count`, `_pct`; `yes`/`no`) in both waves. Matching lower-cased task text:
**2,886** named tasks common to Nov 2025 and Feb 2026; **2,427** carry a Nov-2025 success rate and so
enter the regression (91.95% of Nov named mass); 2,608 carry a Feb rate. Unmatched: **282 Nov-only,
372 Feb-only** — report both. Log (e) 13." No supplementary source; the join is on lower-cased task
text within the Index.

**Overlap with existing work, stated.** The fourth report states the validation criterion at p.24 and
no publication runs it; the nearest thing in the corpus is a cross-sectional tenure–success
association. Externally, Tomlinson et al. (2025) run the closest analogue on another platform,
reporting that their scope measure correlates with the log share of user activity — which is why this
post's contribution is the Anthropic-data version and not the idea.

**Risks, ranked.** (1) Mean reversion: regressing growth on an initial level inherits a negative bias
— observed as a negative coefficient that disappears under the split-sample instrument. (2) Entry and
exit: 282 tasks appear only in the first wave and 372 only in the second, and those margins are
outcomes the regression conditions away — observed as the result changing when the entry/exit margin
is included. (3) Circularity: the same model produces the success label and the task label —
observed as the placebo moving with the outcome.

**What it teaches.** Whether the primitive that carries Anthropic's productivity revision has any
predictive content at all, on the only outcome the public data offers.

**The imaginable close.** *Holds*: that people bring back the work AI does well, which is the first
evidence that the success measure is measuring something. *Fails*: that what AI does well and what
people return with are different things. *Null*: that a single quarter cannot tell, and what cadence
would.

**Mentor and Institute hooks.** ⟨mentor⟩ interest 3, stating a design's power and publishing nulls
("differential increases in unemployment on the order of 1 percentage point would be detectable",
`labor-market-impacts-2026-03`, p.12). Institute: `ED-4`, `Share 1`.

---

### LL-11 (Σ 28 rank 2) — Do the tasks that grow on the enterprise API shrink on the consumer surface?

**Question.** When a task's share of use rises on the enterprise interface, does its share fall on
the consumer one?

**Thread and ledger items.** T3, with T1. `L-2026-03-R5-17` *open* (the migration is asserted, never
measured as a migration); `L-2026-03-R5-18` *open* ("we expect that this migration … may signal more
imminent transformation of work"); `L-2026-01-R4-23` *open* (the promised API analysis of which tasks
enter production workflows).

**Why it matters.** This is the mentor's stated leading indicator for labour-market change: work
moving to the surface where a human is not in the loop. The policy framing of the corpus rests on it
and it has never been tested. Whether the two surfaces' task series are negatively related at task
level decides whether "migration" is a flow or two independent growth stories — and therefore whether
the Index has a leading indicator at all.

**Contribution.** *If it holds* (task shares move in opposite directions across surfaces): the
corpus's central leading-indicator conjecture has its first evidence and the post publishes the
measure. *If it fails*: the surfaces are growing independently, the mechanism claim needs restating
and the policy framing loses its anchor. *If null*: the post reports the correlation with its
interval and shows that three windows of two global cross-sections cannot separate migration from
independent growth.

**Design in brief.** On the tasks present in all six frames, correlate the change in a task's
Claude.ai share with the change in its API share across the three pre-June windows, with the
accounting identity stated and non-coding tasks as a control group. The comparison that carries the
finding is the cross-surface correlation of changes, against zero and against the same statistic
computed within each surface. Key number: that correlation, with its confidence interval. Rough
detectable effect: 1,241 tasks in all six frames give a detectable correlation of about 0.08, so a
weak but real migration signal would be visible and a strong one unmistakable.

**Data.** Steward line, verbatim: "**LL-11. FEASIBLE.** Global `onet_task_pct` exists for both
surfaces in all three pre-June waves: named nodes 2,616 / 3,168 / 3,258 (Claude.ai) and 2,054 / 2,251
/ 2,297 (API); pairwise overlap 1,603 / 1,823 / 1,908; **1,241 tasks appear in all six frames**,
carrying **80.9%** of Claude.ai and **83.2%** of API Feb-2026 named mass. Shares only, and never past
2026-03-24, as your entry says. Log (e) 10." No supplementary source; the join is task text within
the Index, and the June wave is excluded because the API population changes at that boundary.

**Overlap with existing work, stated.** `economic-index-2026-03-report` p.7 states the migration and
p.6 gives the mechanism; both are statements about two independently moving share series, and the
ledger records the migration as never measured. Externally, Chatterji et al. (2025) exclude business
and enterprise plans by design and so cannot see this margin; Dillon et al. (2026) study within-firm
work patterns, not a cross-surface task flow. No provider has published it.

**Risks, ranked.** (1) Shares, not levels: a task's share can fall on one surface and rise on the
other with no conversation moving — observed as the correlation appearing even for tasks whose
absolute use rose on both. (2) The report's own mechanism, one coding job becoming many API calls,
mechanically dilutes API shares — observed as the result concentrating in coding tasks and vanishing
in the non-coding control. (3) Three windows only, so a persistent relationship cannot be
distinguished from one window's shock — observed as the pairwise correlations disagreeing in sign.

**What it teaches.** Whether the corpus's leading indicator is a measurable flow, and if so which
tasks are making the move.

**The imaginable close.** *Holds*: that work is visibly moving to the surface where people are not
watching, task by task. *Fails*: that the two surfaces are growing side by side and the migration was
a figure of speech. *Null*: that three photographs of two rooms cannot show a door, and what would.

**Mentor and Institute hooks.** ⟨mentor⟩ "As tasks migrate to the API, they may become more exposed
to automation. API workflows are far more likely to be directive, with less need for a human in the
loop." (`economic-index-2026-03-report`, OQ 17, p.9.) Institute: `ED-7`, `Share 1`.

---

### LL-18 (Σ 25 rank 10, taken on the recorded diversity tie-break) — Where is AI doing work people say they could not do alone?

**Question.** Does the share of AI use that people could not have completed unaided rise or fall with
how much a place uses AI?

**Thread and ledger items.** T4. `L-2026-01-R4-39` *open* ("human could do alone", 88% globally, is
measured and never used in an analysis — the primitive most directly about substitution);
`L-2026-02-IND-16` *open* (two readings of the same figure sit unreconciled in one spotlight);
`L-2026-02-IND-06` *open* (the "at the frontier" conjecture never holds composition constant).

**Why it matters.** Substitution against complementarity is the question the third report calls
"perhaps the most important question that we hope our data will help answer", and the corpus has a
primitive built for it and uses it nowhere. Whether the share of unaided-impossible work is higher
where adoption is lower decides whether AI is closing a capability gap or widening one — the
distributional question `ED-5` asks, and the channel the scenario model's cognitive-wage result turns
on.

**Contribution.** *If it holds* (the share is higher where adoption is lower): AI is doing work that
would otherwise not be done in the places that use it least, the capability-bypass story the survey
work reports qualitatively and nobody has measured. *If it fails*: the frontier of
unaided-impossible work sits in rich, high-adoption economies, which sharpens the convergence worry.
*If null*: the post publishes the first cross-country distribution of the primitive with intervals
and an MDE, showing the 88% global figure hides no detectable geography.

**Design in brief.** Take the primitive at country grain in both 2026 waves, rebuild per-capita usage
for those waves, and estimate the gradient of the could-not-do-alone share in adoption and in income,
with the global task intersection used to hold task mix constant at the one grain where that is
possible. The comparison that carries the finding is the top against the bottom adoption tercile of
countries, task-mix adjusted. Key number: the percentage-point difference between those terciles.
Rough detectable effect: with 115 countries in both waves a correlation of about 0.26 is detectable
at 80% power, so a gradient worth a policy sentence would be visible and a subtle one would not.

**Data.** Steward line, verbatim: "**LL-18. FEASIBLE.** `human_only_ability` exists at `global`,
`country` and `country-state` in both 2026 waves (938 / 1,082 sub-national units), plus
`onet_task::human_only_ability` at global over 3,169 / 3,259 tasks. **115** countries carry the facet
and clear 200 conversations in both waves. The residual is **`not_classified` in both waves** (never
`none`) at country and `country-state`, median **10.34% / 11.11%**; global publishes `yes`/`no` only,
summing to 100 (yes 87.9097 → 87.7599). Log (e) 5." Supplementary:
`release_2025_09_15/data/intermediate/working_age_pop_2024_country.csv` and `gdp_2024_country.csv`,
both shipped inside a release and used as static 2024 annuals; join key `iso_alpha_3` ↔ the ISO-2
`country_code` column in the same file.

**Overlap with existing work, stated.** `economic-index-2026-01-report` Fig 2.2 publishes the global
level and uses the primitive once as a control; the India brief quotes its own figure in two
directions without a comparison group. Externally, Humlum & Vestergaard (2025) report self-assessed
time savings and quality by occupation, Tomlinson et al. (2025) publish a capability "scope" rating,
and neither is a statement about what the user could have done. No geography of this construct exists
anywhere.

**Risks, ranked.** (1) Construct: the primitive is a classifier's judgement about a counterfactual,
with no validation statistic in the corpus — observed as the level being uninterpretable and only
ranks usable. (2) Language and prompt style vary by country, so the classifier may read the same work
differently — observed as the gradient tracking English-language share. (3) The country residual runs
at a median of about a tenth of conversations — observed as the gradient moving when the residual is
reported rather than renormalised away.

**What it teaches.** Where AI is doing work that would not otherwise get done, which is the only
observable form of the substitution question the corpus says matters most.

**The imaginable close.** *Holds*: that the places using AI least are the places it does the most
that could not be done without it. *Fails*: that the frontier of the impossible sits where the
technology is already thickest. *Null*: that a primitive measured once and never used may not be
ready to carry a geography.

**Mentor and Institute hooks.** ⟨mentor⟩ T4(e): lead author of the report that built the primitives
(`economic-index-2026-01-report`, p.1, ch.4) and of the first tracking of them
(`economic-index-2026-03-report`, Table 1.1 p.9). Institute: `ED-5`, `ED-1`.

---

### LL-22 (Σ 26 rank 7) — How much of a month's local AI-use pattern is real, and how much is noise?

**Question.** How much of what looks distinctive about a place's AI use in one month is still there
the next?

**Thread and ledger items.** T2, with T8. `L-2026-06-R6-29` *open* (April versus May is never
compared, though the release publishes two calendar months side by side — "the largest unexploited
cut in the wave"); `L-2025-09-B3-17` *open* (multiple comparisons in the overrepresentation stories,
with no cell sizes and no null distribution); `L-2025-09-R3-41` *open* (no sampling uncertainty on
any geographic number).

**Why it matters.** Every "overrepresented local use" claim in the corpus and all three country
spotlights are the largest ratios on a large place × use grid, published without a cell count or an
interval; the team's own lesson file records half of one month's state outliers vanishing the next.
This is the measurement Anthropic's early-warning promise needs, because a signal is early only if it
is not noise. It informs how much of a single window the Institute and any external user should
believe.

**Contribution.** *If it holds* (high persistence): single-window distinctiveness is informative, and
the post states the recurrence rate and the floor at which it holds. *If it fails* (low persistence):
a large part of the corpus's local-colour findings are noise, and the post supplies the threshold that
separates signal from it. *If null*: the post publishes recurrence under several specifications and
shows that two months without counts cannot pin the floor — which is itself the argument for the
cadence Anthropic promised.

**Design in brief.** For each geography, rank nodes by over-representation against the parent and by
raw share, take the top ten in April, and measure how many recur in May; repeat at both admission
floors and at three ladders, for US states and for countries. The comparison that carries the finding
is over-representation against raw share, and states against countries. Key number: the recurrence
rate of top-ten over-represented nodes. Rough detectable effect: with 51 states and 114 countries the
recurrence rate itself is estimated to within roughly seven and five percentage points, which is
ample for the twenty-point gap the steward has already found between the two geographies.

**Data.** Steward line, verbatim: "**LL-22. FEASIBLE WITH CAVEAT: state recurrence is the harsh case;
countries are ~20 points more persistent, and a `pct` floor of 0.5 is the honest admission rule.**
The atlas figures are **per-US-state** (51 units, benchmark the `USA` country row, top 10 by log
share ratio, nodes present in both months): 32.7 / 33.1 / 19.8 against 84.9 / 87.6 / 83.5 by raw
share. The same rule for **countries** (114 units, benchmark `GLOBAL`) gives **52.7 / 55.4 / 32.0**
and 86.7 / 90.4 / 83.8 — so yes, it can be produced for countries. With two-decimal values, relative
error is ≤1% only at `pct` ≥ **0.5** (≤2% at 0.25); cells surviving ≥0.5: 52.6 / 58.2 / 28.3%
(country), 67.4 / 75.9 / 44.3% (subregion). **6,594 `pct` cells are exactly 0.00** — drop them
explicitly. Log (f) 8." No supplementary source: the comparison is internal to one release.

**Overlap with existing work, stated.** No Anthropic publication compares the two months or reports a
persistence rate; the atlas records the state figures as a trap, which is where this post starts
rather than what it repeats. Externally, Misra et al. (2025) aggregate over many months expressly to
"mitigate short-term fluctuations" and publish volume and population floors, and Brynjolfsson et al.
(2026) publish event-study controls on a high-frequency series — both are disciplines stated without
a published persistence rate for platform usage rankings.

**Risks, ranked.** (1) No counts anywhere in the wave and values rounded to two decimals, so cells
cannot be sized — observed as recurrence falling with cell size in a way that cannot be separated
from rounding. (2) The result is specification-dependent by construction — observed as the two
admission rules giving 20–50 point differences, which is why both are reported. (3) Two months is one
comparison, so a low rate could be one month's shock — observed as the country and state legs
disagreeing in direction.

**What it teaches.** How much of one window of a place's AI use can be believed, and the rule this
programme and anyone else should apply before publishing a local claim.

**The imaginable close.** *Holds*: that the local character of AI use is stable enough to report, and
under what rule. *Fails*: that most of what looks local about AI use is the largest number on a large
grid. *Null*: that two months is not enough to say, which is an argument for the cadence rather than
against the question.

**Mentor and Institute hooks.** ⟨mentor⟩ interest 2, robustness by rank
(`labor-market-impacts-2026-03-appendix`, Fig 4 p.10). Institute: `Share 1` (early warning,
granularity and cadence), `ED-1`.

---

### LL-31 (Σ 27 rank 4) — Does what people take away from AI depend on where they are?

**Question.** Does the mix of concrete outputs people get from AI vary systematically with a place's
income or its rate of use?

**Thread and ledger items.** T2, with T1. `L-2026-06-R6-30` *open* (no per-capita geography result at
all in the sixth report, though the index is released); `L-2026-06-R6-31` *open* (no subregion result,
though the grain exists); `L-2026-06-R6A-19` *open* ("Cowork" used as a surface name without
definition and no exhibit separating chat from Cowork).

**Why it matters.** Artifacts are the closest thing in the corpus to output: a document, a
spreadsheet, a piece of code. A geography of artifacts is the first observable answer to the
value-capture half of `ED-1` — whether richer places get different things from the same technology
rather than merely more of it. It also tests the sixth report's own silence: the release made the cut
available and the report published no geography at all.

**Contribution.** *If it holds* (the artifact mix varies with income or adoption): the post supplies
the first geography of AI output and names what poorer places produce more of. *If it fails* (mixes
are flat): what people take away is invariant to place, strengthening the case that usage differences
are about volume rather than kind. *If null*: the post reports the coverage of the artifact metrics
below global and which grains support any comparison.

**Design in brief.** Pool April and May as an unweighted mean, keep only units publishing all
thirty-two metrics in both months, and relate each place's artifact mix to income and to the released
per-capita index, at country grain and again across US states. The comparison that carries the
finding is the top against the bottom income tercile's artifact mix, with the April–May agreement
shown for every claim. Key number: the largest income gradient among the thirty-two shares, with its
April–May consistency. Rough detectable effect: 114 countries give a detectable correlation of about
0.26 and 536 subregions about 0.12, so a modest income gradient is visible at subregion grain even
where the country panel would miss it.

**Data.** Steward line, verbatim: "**LL-31. FEASIBLE — the raggedness you feared is not in this
block.** At `category_name == overall` **every** published unit-month carries all 32
`artifact_*_pct` metrics: 235 of 235 country unit-months and 1,188 of 1,188 subregion unit-months.
**114 of 121** countries and **536** subregions (including all 52 US units) publish all 32 in **both**
months, and all 114 countries also carry the AUI; subregions **do** carry these metrics at `overall`
(the `pct`-only rule bites inside the ladders). No counts: pool as the unweighted April–May mean and
admit only both-month units, with a `pct` ≥ 0.5 floor wherever a ratio is formed. Log (g) 3."
Supplementary: `gdp_2024_country.csv` from `release_2025_09_15/data/intermediate/`, shipped inside a
release; join key `iso_alpha_3`, with the June wave's ISO-3 country ids and its ISO-2-prefixed
subregion ids handled per `ATLAS §Traps 4`.

**Overlap with existing work, stated.** `economic-index-2026-06-report` ch.2 publishes the taxonomy
and the global shares and no geography; the threads map records the absence as a tension — the
measure got finer and the reporting stopped. Externally, Chatterji et al. (2025) and arXiv 2605.30685
publish topic and purpose mixes by country income, neither of which is a statement about what was
produced; no other provider releases an artifact taxonomy at all.

**Risks, ranked.** (1) Compositional shares rounded to two decimals, so a distinctive small category
in a small unit can be rounding — observed as gradients concentrated in categories below the 0.5
floor. (2) No counts in the wave, so units cannot be sized and the pooling rule is unweighted by
necessity — observed as April and May disagreeing for the units that drive a result. (3) Artifact
classification has no published accuracy statistic — observed as a gradient that tracks language or
task mix rather than output type.

**What it teaches.** Whether the same technology yields different products in different economies,
measured rather than assumed.

**The imaginable close.** *Holds*: that where you are shapes not just how much AI you use but what
you walk away with. *Fails*: that people everywhere leave with the same kinds of things. *Null*: that
a wave which publishes no counts cannot yet carry a geography of output.

**Mentor and Institute hooks.** ⟨mentor⟩ first named author of the wave that introduced artifacts
(`economic-index-2026-06-report`, p.1) and of its interpretive claim that compute and human
involvement move together (pp.13–14). Institute: `ED-1`, `ED-3`.

---

### LL-36 (Σ 27 rank 5) — Is coding still the leading edge of AI use, or just its largest share?

**Question.** As coding's share of AI use falls on the consumer surface, is the coding work that
remains becoming narrower or staying the same?

**Thread and ledger items.** T7, with T1. `L-2025-04-SWE-11` *open* (which software roles change most,
and which might disappear); `L-2025-04-SWE-14` *open* (the conjecture that jobs centred on simple
applications face earlier disruption); `L-2025-03-R2-09` *open* (whether growth elsewhere is
diffusion, novel applications of coding, or capability). It also absorbs `L-2025-02-P1-28` from the
deleted LL-32, as a pre-registered robustness cut.

**Why it matters.** The Institute's headline evidence that "jobs like software engineering are
changing radically" is this thread, and the policy reading of the Index assumes coding is the leading
indicator for knowledge work. If coding's share is falling while its internal composition narrows
toward agentic work, the leading-indicator reading survives; if the share is falling because
everything else grew, coding is being diluted and the claim is about the denominator.

**Contribution.** *If it holds* (composition narrows as the share falls): the leading-edge reading
survives and the post names which coding tasks now carry it. *If it fails* (the share falls with
composition flat): coding is being diluted by diffusion elsewhere, and the agenda's sentence is not
what this series says. *If null*: the post publishes the first within-category decomposition of the
corpus's most-quoted share, with the taxonomy breaks marked.

**Design in brief.** Rebuild SOC major group 15 from global task shares in the three long waves on
both surfaces, then compute, per wave, the share of the category's own mass sitting in its ten largest
tasks. The comparison that carries the finding is within-category concentration against the
category's total share, and Claude.ai against the API. Key number: the change in within-category
concentration between August 2025 and February 2026, beside the change in the category share. Rough
detectable effect: the category holds thousands of task nodes, so sampling is not the constraint;
what matters is that both published bases reproduce, so a movement of a point or two is interpretable
rather than a reconstruction artefact.

**Data.** Steward line, verbatim: "**LL-36. FEASIBLE — and the reconstruction gap you feared is 0.02
pp.** Rebuilding SOC major group 15 from global `onet_task_pct` through the shipped O\*NET 20.1
statements gives, for August 2025, **39.03%** (classified base) and **35.86%** (all-conversation
base) against the published `soc_occupation` facet's **39.0412%** and **35.8771%**. Series: Claude.ai
39.03 → 36.02 → **32.23** (classified); 1P API 49.98 → 51.73 → 51.61, i.e. 45.67 / 46.60 on the
all-conversation base — the published '~46%' and '34–35%' both reproduce once the base is named.
Log (g) 5." Supplementary:
`release_2025_09_15/data/intermediate/onet_task_statements.csv`, shipped inside a release; join key
the lower-cased task text, then `O*NET-SOC Code` to major group.

**Overlap with existing work, stated.** The category share is the corpus's most-cited series and is
always reported as one number; the fifth report attributes its movement to call-splitting without
testing it inside the category. Externally, Chatterji et al. (2025) report programming as a small and
falling share of consumer messages — a sharply different picture that makes the within-category
question worth asking — and Tomlinson et al. (2025) note that Claude studies show more emphasis on
computer and mathematical tasks than theirs. No provider decomposes its own coding share.

**Risks, ranked.** (1) Base naming: the same series reads differently on the classified and
all-conversation bases and the corpus quotes both — observed as a reader comparing our number with a
published number computed on the other base. (2) The category is reconstructed through an external
task-to-SOC join in the waves that ship no occupation facet — observed as the reconstruction drifting
from the published facet in the waves where it cannot be checked. (3) The allocation rule for
multi-holder tasks — observed as the category share moving between rules, bounded by the steward at
≤0.17 pp.

**What it teaches.** Whether the Index's most-quoted series is about coding changing or about
everything else arriving.

**The imaginable close.** *Holds*: that the coding work left on the consumer surface is a narrower
thing than it was, which is what a leading edge looks like. *Fails*: that coding is not shrinking so
much as being surrounded. *Null*: that a share can fall for two reasons and the data cannot yet say
which.

**Mentor and Institute hooks.** ⟨mentor⟩ T3(e), the migration of coding work to the API as his stated
leading indicator (`economic-index-2026-03-report`, OQ 17–19). Institute: `ED-7`, and the agenda's own
evidence claim (`institute-agenda-2026-05`, *Lead ¶4*).

---

### LL-39 (Σ 26 rank 8) — When the ruler changed, did AI use change with it?

**Question.** How much of the change between Anthropic's fifth and sixth measurement waves is a
change in AI use, and how much is a change in how it was measured?

**Thread and ledger items.** T8, with T1 and T4. `L-2026-06-R6A-10` *open* (no old-versus-new
agreement rate, so no reader can tell how much of any change is the new classifier plus the new O\*NET
vintage — "the load-bearing omission for any cross-wave comparison");
`L-2026-03-R5A-05` *open* (the vintage change asserted and never bounded);
`L-2026-06-R6-20` *open* ("A chat transcript no longer fully captures how people are using AI, and our
methods … have had to rapidly adapt").

**Why it matters.** Every cross-wave statement anyone makes — Anthropic's, this programme's, or an
external user's — runs across this boundary, and three primitive levels break at it while the one
facet whose taxonomy did not change does not. A published account of which metrics survive the
boundary is a prerequisite for the rest of the short-list, and for anyone comparing June 2026 with
anything earlier.

**Contribution.** *If it holds* (quantities whose taxonomy changed jump while the unchanged facet does
not): the June discontinuity is a measurement artefact and the post supplies the first estimate of its
size, metric by metric. *If it fails* (everything moves together): the change is behavioural and the
sixth report's numbers can be compared with the fifth's. *If null*: the post publishes the boundary
audit — what is comparable across it and what is not — which is the bridge the appendix omitted.

**Design in brief.** Compare February 2026 with the April–May mean for every Claude.ai global quantity
published on both sides, sort them into the steward's three tiers, and use the unchanged collaboration
facet and the `onet` node counts as the control and the known-broken case respectively. The comparison
that carries the finding is the size of the move for metrics whose taxonomy changed against those
whose did not. Key number: the largest move among the comparable metrics against the smallest move
among the breaking ones. Detectable effect: no test is possible — the June wave publishes no counts —
so the design requires April and May to agree in sign and size for every metric before it is reported,
which is the substitute for a standard error.

**Data.** Steward line, verbatim: "**LL-39. FEASIBLE — here is the spine.** Claude.ai global, Feb 2026
against the April–May mean. *Comparable (moves < 1.1):* `human_only_ability_pct` −0.06,
`human_education_years_mean` −0.08, `collaboration_none_pct` −0.45, `use_case_work_pct` −0.79,
`collaboration_directive_pct` −1.09. *Comparable only with the break stated (1.8–5.7):* validation
−1.78, personal −2.95, coursework +3.78, feedback loop +4.46, task iteration +4.56, learning −5.70.
*Breaking:* `ai_autonomy_mean` −0.68, `ai_education_years_mean` +0.63, `human_only_time_mean` +1.60 h,
`human_with_ai_time_mean` +25.08 min, **`multitasking_pct` +12.72 pp**. *Absent in June:*
**`task_success`** (no such metric id), all counts, all `not_classified` nodes. *Not comparable by
construction:* `onet` node counts (3,260 vs 2,451 / 2,757) and the entire `request` ladder. June
admission rule: report magnitudes with no tests, and require April and May — the only within-wave
replication — to agree in sign and size. Log (g) 10." No supplementary source; the 1P API leg is
excluded because its population changes at the same boundary.

**Overlap with existing work, stated.** `economic-index-2026-06-appendix` validates the rebuilt
classifier with seven WildChat examples and publishes no agreement rate, no position-bias test and no
tie-break reliability figure; the fifth report's vintage recode is scoped to one figure. Externally,
Bick, Blandin, Deming & Schumacher (2026) argue that chat-log classification is conceptually fragile
and that chats are classified "without knowing the user's occupation" — an argument this post turns
into a measurement — and Tomlinson et al. (2025) validate their classifier against user feedback, the
standard this wave does not meet. No external party can run this audit, because it needs the released
files either side of the break.

**Risks, ranked.** (1) Several things changed at once — classifier, O\*NET vintage, sampling window —
so a jump cannot be attributed to any one of them; observed as the three tiers ranking metrics without
explaining them. (2) No counts in June, so nothing can be tested; observed as the post reporting
magnitudes and April–May agreement instead of intervals. (3) Two months of one wave against one week
of another, so seasonality is uncontrolled; observed as the comparable tier containing metrics with
known calendar sensitivity.

**What it teaches.** Which of Anthropic's own measures can be compared across its largest measurement
break, stated metric by metric — and therefore what any later wave can be compared to.

**The imaginable close.** *Holds*: that the sharpest movements in the newest wave belong to the
instrument rather than to the world. *Fails*: that the instrument held and the movements are real.
*Null*: that a wave which publishes no counts cannot be reconciled with its predecessor, and what the
next release would have to ship.

**Mentor and Institute hooks.** ⟨mentor⟩ he is first named author of the wave that made the break
(`economic-index-2026-06-report`, p.1) and lead author of the wave before it, so both endpoints are
his. Institute: `Share 1` (granularity and cadence), `WILD-6`.

## 7. Verification

- **Written 2026-09-16**, from `programme/LONGLIST.md` at commit `2eff78a` (39 survivors, each with a
  steward feasibility line verbatim) and `programme/THREADS.md` and `programme/LEDGER.md` at
  `0f5c1c6`. Every ledger status quoted here was read from the LEDGER, not recalled.
- **The rubric was fixed and written before any candidate was scored**, in the order the file
  presents it: anchors, then aggregation, then tie-break order, then scores. No anchor was adjusted
  after a score was assigned.
- **Aggregation is an unweighted sum of six 1–5 dimensions**, maximum 30. The tie-break order
  (TEACH → FEAS → FOUND) was fixed in §1 and used in §4. The diversity tie-breaker was used **once**,
  on data cut, to choose LL-18 over LL-12 one point above the cut line, and that use is recorded in
  §4 with its reasoning.
- **No surviving entry's question or contribution was changed while scoring.** Three candidates whose
  contribution the steward's audit had already narrowed — LL-15, LL-41, LL-26 — are scored on their
  narrowed form, with the narrowing named in the rationale, and the entries themselves were amended
  at Step 1, not here.
- **Defects found while scoring and left for the referee:** LL-37's risk column is the binding
  constraint rather than its score (no outcome series exists, so predictive validity is unreachable);
  LL-38 now carries six observable dials after the steward named two more, which is a scope defect its
  entry records; LL-14's originality fell to 3 during scoring because two external teams now use the
  same released file. None of the three is short-listed, so none of these defects affects the cut.
- **Sketch discipline.** Ten sketches, each in the director's fixed section order, each 400–600 words
  of prose plus the steward's quoted line. No sketch introduces a hypothesis absent from its LONGLIST
  entry, and none contains an assumptions sweep.
- **What this file does not do.** It does not write a brief (that is `posts/postN/BRIEF.md`), it does
  not choose the final six posts (that is the human's, at Gate 1a), and it opens nothing in
  `reference/`.
