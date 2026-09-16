# post3 · When AI's coding share falls on one surface, does the coding that remains narrow?

## 1. The question

As the share of AI use classified to coding tasks falls on the consumer surface and rises on the
developer surface, is the coding work that remains on the consumer surface becoming more
concentrated, less concentrated, or unchanged in composition?

*Title form, settled here (editor's note, `room/editor-2026-09-16-sketch-LL-36.md`).* The sketch's
"leading edge" is dropped: the corpus's term is leading **indicator**, applied to the migration of
coding work to the API — "we expect that this migration from Claude.ai to the API may signal more
imminent transformation of work for the associated jobs" (`economic-index-2026-03-report`,
2026-03-24, p.7) — not to a frontier of capability. "Or just its largest share" is also dropped: it
presupposes that a series cannot be both the largest share and an indicator. The question says AI;
every finding and every measurement in the post says Claude.

## 2. Why it matters, and to whom

The Institute's most load-bearing labour-market assertion is a sentence with no number attached:
"At Anthropic, we can see early evidence that jobs like software engineering are changing radically."
(`institute-agenda-2026-05`, 2026-05, *Lead ¶4*). The corpus's coding series is what a reader reaches
for as its evidence, and that series is falling on Claude.ai: "the share of conversations on
Claude.ai assigned to such (mostly) coding-related tasks is down from a peak of 40% in March 2025 to
34% in November 2025" (`economic-index-2026-01-report`, 2026-01-15, p.7), then "Since August 2025,
the share of tasks in this category has increased by 14% in the API and decreased by 18% in
Claude.ai" (`economic-index-2026-03-report`, p.7).

A falling share admits two readings and the corpus has never separated them. If the share falls
while the work inside the category concentrates into fewer tasks, the series is saying something
about the work itself; if the composition inside the category is unchanged, the claim is about the
denominator — everything else arrived, and coding did not change. The two readings imply different
actions for the people who use this series: the Institute, which has committed to "updating the
Economic Index to share more high-frequency, granular data" (`institute-agenda-2026-05`, *ED-7*) and
to using it as "an early warning signal for significant change and disruption" (ibid., *Share 1*);
and the labour-market researchers who now build exposure measures on provider logs.

Only the Economic Index can settle it: it is the one public series that publishes task-level usage
shares on two surfaces of the same provider, in three windows built on a comparable task taxonomy,
with enough detail to look **inside** an occupational category rather than at its total. No
`soc_occupation` facet exists after August 2025 (`data/ATLAS.md` §Cuts 13), so the category must be
rebuilt — and the rebuild reproduces Anthropic's own published facet to 0.02 pp (steward, §8), which
is what makes the within-category question answerable at all.

## 3. The thread of Anthropic's inquiry this builds on

**Thread T7 (agentic coding and the agentic surfaces), with T1 (adoption and diffusion).** The gap
this post occupies is `L-2025-03-R2-09`, *open*: "the increase in these other categories could
reflect either ongoing diffusion of AI throughout the economy, novel applications of coding to those
domains, or unexpected capability improvements in the model" (`economic-index-2025-03-report`,
2025-03-27, § "What's changed since the launch of Claude 3.7 Sonnet?"). Three explanations were
offered for movement in the category shares and none was tested; the same three-way fork recurs in
the September 2025 report.

Two further ledger items are **touched, not addressed** by this design (referee correction 7):
`L-2025-04-SWE-11`, "Which software development roles will change the most, and which might
disappear entirely?" and `L-2025-04-SWE-14`, "jobs that center on making simple applications and
user interfaces might face earlier disruption from AI systems"
(`economic-index-2025-04-software-development`, 2025-04, § "Looking ahead" and key pattern 2). A
concentration statistic over task shares says nothing about which roles disappear and nothing about
front-end work specifically; the post says so in its limitations rather than imply otherwise.
`L-2025-02-P1-28` (the allocation of a task's conversations across the occupations that share it) is
rehoused here from the deleted LL-32 and enters as a pre-registered robustness cut, not a question.

The measure this post extends is Anthropic's own, and it is defined for the whole task universe:
"Figure 1.1: Usage shares among top 10 tasks over time by platform, Claude.ai and 1P API / Share of
conversations assigned to the 10 most prevalent O\*NET tasks, by platform and report version."
(`economic-index-2026-03-report`, p.5). What the thread has established is a set of totals — the
category share by wave and surface, and a whole-universe concentration series (Claude.ai 21 / 24 /
23 / 24 / 19; API 28 / 32 / 33, ibid., Fig. 1.1). What is open is everything inside the category.
The one mechanism the corpus offers for the divergence is asserted without a number: "Claude Code's
agentic architecture splits coding work into smaller API calls, which are labeled as distinct tasks.
So while coding's overall share of API traffic has grown, it is spread across many task categories
rather than concentrated in a few" (ibid., p.6). ⟨mentor⟩ The migration is the mentor's stated
leading indicator: "As tasks migrate to the API, they may become more exposed to automation. API
workflows are far more likely to be directive, with less need for a human in the loop." (ibid.,
p.9).

## 4. Overlap, stated

**What Anthropic has shown and has not.** The Computer and Mathematical share is the corpus's
most-cited series — 37.2% in the first paper (`economic-index-2025-02-paper`, 2025-02-10, p.6,
Fig. 2), 37.2 → 39.6 → 36.9 across the first three waves (`economic-index-2025-09-report`,
2025-09-15, Fig. 1.1, p.8), 34% in November with the API "edged higher from 44% in August to 46% in
November 2025" (`economic-index-2026-01-report`, p.7), 35% in February
(`economic-index-2026-03-report`, p.5) — and it is always published as one number per wave per
surface. Concentration is published for the whole task universe only (§3 above), never within a
category, and the call-splitting mechanism offered for the API's behaviour (p.6) carries no
measurement. New here, in one sentence: the same category decomposed from the inside as a
concentration series on both surfaces, which is also the first test of that mechanism's own
signature — a category share rising while concentration inside the category falls.

**What others have shown.** On a different consumer product, coding is a small share: "Computer
programming and self-expression both represent relatively small shares of use" (Chatterji,
Cunningham, Deming, Hitzig, Ong, Shan and Wadman, *How People Use ChatGPT*, NBER WP 34255, 2025,
abstract; fetched 2026-09-16). New here: the comparison is made inside one provider's own category
rather than across providers' taxonomies.

**Separation from the other posts of this programme** (director's pairs ruling, `programme/SHORTLIST.md` §5):
- **post2 (LL-11)** headlines cross-surface task **migration** and may not headline coding's share.
  This post headlines **composition inside coding** on one surface at a time and cites post2 for the
  migration frame; the two share no key number.
- **post7 (LL-12)** works concentration over the **whole** task universe within a window. This post
  works concentration **inside SOC major group 15 only**, and says so in its first figure caption.
- **post1 (LL-07)** is written first in the construction triple and states the task → SOC join and
  the multi-holder allocation rule in its §8. This post **cites `posts/post1/BRIEF.md` §8 for the
  construction** rather than re-deriving it, and carries the ≤0.17 pp allocation bound as its own
  pre-registered robustness cut.

## 5. Contribution

If concentration inside the category moves, the post supplies the first within-category decomposition
of the corpus's most-quoted share and states which of the two readings a concentration statistic
licenses — a narrowing frontier, or a surface left with the routine — without choosing between them on
this evidence alone; if it does not move, the post establishes, with a stated equivalence bound, that
the fall in coding's share on Claude.ai is a fact about the denominator and not about coding.

## 6. Hypotheses

The confirmatory statistic is **C**, the share of a surface's Computer and Mathematical (SOC major
group 15) usage mass sitting in that category's ten largest O\*NET tasks, renormalised inside the
category, computed per wave per surface; **ΔC** is its August 2025 → February 2026 change. The
pre-registered band is **δ = 1.0 pp** (§9 gives the arithmetic behind it). H1–H3 are the three
regions of one test and are mutually exclusive by construction; H4 is a second test on the other
surface.

**H1 · Concentration (ΔC ≥ +1.0 pp on Claude.ai).** The category's share falls while the work inside
it concentrates into fewer tasks.
*Signature only H1 predicts:* C rises **while** the published whole-universe concentration on the
same surface falls over the same window (24% → 19%, `economic-index-2026-03-report`, Fig. 1.1, p.5),
so the movement is specific to the category and is not the general diversification.
*Counter-evidence:* C flat or falling; or C's rise reproduced in the whole-universe series or in the
two next-largest SOC groups, which would make it a property of the sample rather than of coding; or
C's rise accounted for by a fall in the category's published node count (a top-ten share rises
mechanically when the category loses tail nodes), which the node-count and name-match checks in §10
would show.

**H2 · Internal broadening (ΔC ≤ −1.0 pp on Claude.ai).** The category's share falls **and** what
remains is spread more thinly, consistent with the largest coding tasks being the ones that left.
*Signature only H2 predicts:* C falls on Claude.ai while the same tasks that leave the Claude.ai top
ten are present and large in the API's SOC-15 top ten in the same wave.
*Counter-evidence:* C falls without any correspondence between the Claude.ai tasks that shrink and
the API tasks that grow; or C falls on both surfaces at once, which points at the classifier or the
taxonomy rather than at migration.

**H3 · Flat composition (|ΔC| < 1.0 pp on Claude.ai, with the equivalence interval excluding ±1.0
pp).** The category's share falls with its internal composition unchanged: dilution from outside.
*Signature only H3 predicts:* C within band **and** a total-variation distance between the August and
February SOC-15 mixes no larger than that of the rest of the task universe over the same window.
*Counter-evidence:* the equivalence interval fails to exclude ±1.0 pp (then the result is
indeterminate, not flat, and is reported as such); or the TVD inside SOC-15 is materially larger
than outside it, which would mean the mix changed without the top-ten statistic registering it.

**H4 · The call-splitting signature on the API (share up, C down).** Anthropic's stated mechanism —
"Claude Code's agentic architecture splits coding work into smaller API calls, which are labeled as
distinct tasks" (`economic-index-2026-03-report`, p.6) — predicts the API's category share rising
while concentration inside the category falls.
*Signature only H4 predicts:* opposite signs on the same statistic across the two surfaces in the
same waves, with the API's SOC-15 node count rising.
*Counter-evidence:* the API's C rises with its share; or both surfaces move the same way; or the
API's SOC-15 node count is flat while C falls, which would make the fall a re-weighting rather than
a splitting.

## 7. Assumptions sweep

**(i) Value judgement in the framing — *needs a design change; the change is made here.*** "Leading
edge", "narrowing" and "frontier" all rank the work that remains as better or worse than the work
that left. Anthropic's own term is about location, not quality: "we expect that this migration from
Claude.ai to the API may signal more imminent transformation of work for the associated jobs"
(`economic-index-2026-03-report`, p.7). *Change:* the title and question drop "leading edge" (§1);
the post's finding sentence is about **concentration**, and both readings a concentration statistic
licenses — a narrowing frontier, or a surface left with the routine after the professional work moved
— are stated side by side and neither is chosen on this evidence (referee correction 7).

**(ii) Construct mapping — *newly flagged; two design changes.*** The published statistic is "Share
of conversations assigned to the 10 most prevalent O\*NET tasks, by platform and report version"
(`economic-index-2026-03-report`, Fig. 1.1, p.5), computed over the **whole** universe and, per
`data/ATLAS.md` §Conventions, **not renormalised**. C is the same shape on a different denominator —
the category's own mass — so C is not comparable in level to the published 19% or 24%. Second, the
category is a task taxonomy wearing occupation labels: "a task involving software debugging would
fall into the Computer and Mathematical occupation group" (`economic-index-2025-09-report`, p.20),
occupation being inferred from the task, not the user (`data/ATLAS.md` §Traps 36). *Changes:* every
table prints C beside the published whole-universe series and states the denominator in the caption;
and the post never calls SOC-15 "software engineers" — it says "tasks Claude was used for that
O\*NET assigns to Computer and Mathematical occupations".

**(iii) Composition or selection — *needs a design change; the change is made here.*** The February
window carries a named user-composition shock: "Our sampling period overlapped with the release of
our Super Bowl advertisements, which brought many first-time users" (`economic-index-2026-03-report`,
chapter 2 endnote 3, p.18). An inflow of new consumer users changes the denominator and can move the
within-category mix with no change in anyone's coding behaviour. Externally, the same problem is
formalised: "platform-derived exposure scores combine task-level AI applicability with the
occupational composition of the platform's user base … consumer and enterprise channels within the
same vendor disagree in sign" (Yin and Ogut, arXiv:2605.21743v2, 2026-05-27, abstract; fetched
2026-09-16). *Change:* the August → November leg, which contains no advertising inflow, is a
pre-registered placebo; ΔC over August → February is reported only alongside it, and a finding
requires the two legs to agree in sign. The post states that the design cannot separate "who is
using Claude" from "what coding is brought to Claude", because no release publishes a user column.

**(iv) Anthropic's own results that cut against or bound the framing — *handled.*** Three bite.
First, the aggregate runs the other way on the same surface and window — whole-universe
concentration on Claude.ai fell, "the top 10 most common O\*NET tasks went from 24% of conversations
to just 19%" (`economic-index-2026-03-report`, p.5) — so an H1 result is a claim about a category
moving against its own sample; the post prints the published whole-universe series beside C in every
table and reports the two comparison categories (§9, exploratory test 2). Second, a "new
coding work" reading is bounded by the report's own statement that "In this data pull, that
cumulative estimate barely changed (Appendix Figure A.2). Our data from this report showed many
fewer novel O\*NET tasks than in our previous report" (ibid., p.7). Third, the published category
series is not internally consistent across vintages: "This number uses 2019 O\*NET-SOC codes, while
previous reports use the 2010 vintage" (ibid., footnote 2, p.11). *Handling:* the reconstruction
holds one crosswalk fixed — the O\*NET DB 20.1 statements shipped inside `release_2025_09_15` — across
all three waves, so the series is internally consistent by construction, and the post states that
this is why its levels may differ from a published level computed on another vintage.

## 8. Data, confirmed at column level

**The data steward's feasibility line, verbatim** (`room/steward-2026-09-16-longlist-feasibility-batch-3-answers.md`,
2026-09-16; quotation marks as in the original):

> "**LL-36. FEASIBLE — and the reconstruction gap you feared is 0.02 pp.** Rebuilding SOC major group
> 15 from global `onet_task_pct` through the shipped O\*NET 20.1 statements gives, for August 2025,
> **39.03%** (classified base) and **35.86%** (all-conversation base) against the published
> `soc_occupation` facet's **39.0412%** and **35.8771%**. Series: Claude.ai 39.03 → 36.02 → **32.23**
> (classified); 1P API 49.98 → 51.73 → 51.61, i.e. 45.67 / 46.60 on the all-conversation base — the
> published "~46%" and "34–35%" both reproduce once the base is named. Log (g) 5."

**The caveat that travels with it**, in the steward's words on the allocation rule this candidate
absorbs from the deleted LL-32 (same note): "**LL-32. FEASIBLE WITH CAVEAT: the answer is almost
certainly 'the rule barely matters', and the effect size is the finding.** In the O\*NET 20.1
statements a task text has one holder occupation for all but **72 / 91 / 84** tasks — **4.05% /
5.57% / 4.50%** of named usage mass (the flat family: 84 tasks, 2.56%). Equal-split,
employment-weighted and modal-holder allocation move the SOC-15 share by **≤0.17 pp** and the
22-group ranking by at most **one** position (Aug 2025) or **none** (Nov, Feb). Publishable as a
bound on a construction choice, not as a correction. Log (g) 4."

The steward's confirming note for this post is **`posts/post3/notes/feasibility.md`**; he writes it
after this brief and confirms or contradicts each cut below at column level.

**Cuts, at column level.** Long schema (Family B), columns `geo_id, geography, date_start, date_end,
platform_and_product, facet, level, variable, cluster_name, value`.

| # | release (window) | grain | facet / level | variable | filter and threshold |
|---|---|---|---|---|---|
| 1 | `release_2025_09_15` (Aug 2025) | `geography == global` | `onet_task`, `level` 0 | `onet_task_pct` | `platform_and_product` ∈ {Claude.ai, 1P API}; privacy floor `onet_task_count ≥ 15` already applied upstream |
| 2 | `release_2026_01_15` (Nov 2025) | same | same | same | same |
| 3 | `release_2026_03_24` (Feb 2026) | same | same | same | same; counts are on a 1,000,000 sample base, not conversations |
| 4 | `release_2025_09_15` | — | `soc_occupation` (enriched, global) | `soc_pct` | reproduction target only: the published 39.0412% / 35.8771% |

Conventions applied, each from `data/ATLAS.md`: read with `keep_default_na=False` and, for
`release_2026_03_24`, `na_values=[]` (§Traps 1–2); cast `level` to `str` after any parquet read
(§Traps 7); drop the pseudo-task `none` **and** `not_classified`, which are different things
(§Traps 23–24); the 200 / 100 geography thresholds do not apply, this being a global cut.

**Two bases, both reported, every time.** The classified base (named tasks only) and the
all-conversation base (including the unnamed residual) are both quoted in the corpus and give
different levels for the same series (`data/ATLAS.md` §Conventions: "2025-09-15 occupation shares:
Chapter 1 quotes an all-conversation base and Chapter 2 a classified base; both reproduce"). Every
sentence in the post that carries a number names its base, and every table carries both.

**Derived metrics.** *Category share* `S` = Σ `onet_task_pct` over SOC-15 tasks, on each base.
*Within-category concentration* `C` = (Σ of the ten largest SOC-15 `onet_task_pct`) ÷ `S`,
renormalised inside the category; the top ten is recomputed within each wave, matching Anthropic's
within-window convention, with a fixed-August-basket variant as the second implementation.
*Secondary:* SOC-15 Herfindahl index; SOC-15 node count per wave; total-variation distance between
waves on the name-matched SOC-15 node set.

**Supplementary data, and why it is needed.**
`release_2025_09_15/data/intermediate/onet_task_statements.csv` — O\*NET DB 20.1, 19,530 × 9, carries
`soc_major_group` — shipped inside an Economic Index release. It is needed because no
`soc_occupation` facet exists at any grain in the 2026 waves (`data/ATLAS.md` §Cuts 13), so the
category must be rebuilt. Join key: the **lower-cased, stripped** task text; case-variant duplicates
must be collapsed before the join or it silently becomes many-to-many (§Traps 21). Coverage recorded
in the atlas: the 2026-01-15 join to this file is clean, 3,168/3,168 (API 2,251/2,251); the
2026-03-24 coverage is for the steward to state. The multi-holder allocation rule is **cited from
`posts/post1/BRIEF.md` §8**, not re-derived here.

**The published number this reproduces first** (criterion 3; referee correction 7). The target is
the relative change at `economic-index-2026-03-report`, p.7: "Since August 2025, the share of tasks
in this category has increased by 14% in the API and decreased by 18% in Claude.ai". On the
steward's own reconstructed classified series the Claude.ai leg reproduces — 32.23 / 39.03 − 1 =
**−17.4%**, against a published −18% — and **the API leg does not**: 51.61 / 49.98 − 1 = **+3.3%**,
against a published +14%. This arithmetic is the first thing the post publishes, with the three
candidate explanations named and not chosen between: the 2019-vintage recode disclosed at footnote 2
(p.11), Claude Code entering the API sample ("This includes data from Claude Code.", ibid.,
footnote 1, p.11), or a third base not yet identified. **Pre-registered rule:** if no named base
reproduces the API leg to within ±3 pp of relative change, H4 is reported as descriptive, the
discrepancy is reported as a finding in its own right, and the headline stays on Claude.ai, where
the reproduction holds.

**Two questions for the steward, to be answered in `posts/post3/notes/feasibility.md`.**
(a) The February all-conversation API level is absent from the line above; state it, and state
whether any base reproduces +14%. (b) The November 2025 global mix cannot have Seychelles removed —
24,715 conversations, 2.5% of the whole global sample, excluded by the report and not excluded in
the file (`data/ATLAS.md` §Traps 14) — and the `onet_task` facet exists at country grain but with
median 21 of 3,170 nodes per country (§Coverage). State the largest share of the November global
SOC-15 mass recoverable from country rows, so the post can bound the contamination instead of
ignoring it.

## 9. Confirmatory tests and the exploratory allowance

**T1 (H1 / H2 / H3), Claude.ai.** Compute C for August 2025, November 2025 and February 2026 on both
bases; the confirmatory quantity is ΔC over August → February, assigned to one of the three
pre-registered regions: ≥ +1.0 pp (H1), ≤ −1.0 pp (H2), or inside the band with an equivalence
interval excluding ±1.0 pp (H3). ΔC is reported beside ΔS, the change in the category share, in the
same sentence.

**Why δ = 1.0 pp, and the power behind the null.** The construction error is bounded and small: the
reconstruction matches the published facet to **0.02 pp**, and the allocation rule moves the category
share by **≤0.17 pp** (steward, §8). Sampling is not the constraint: the February file is a 1,000,000
sample base, SOC-15 carries roughly a third of it, and the binomial standard error on a share of
about 0.3 within a category of that size is of order **0.1 pp** — an order of magnitude below δ. A
true |ΔC| of 1.0 pp is therefore detected with power near one, and the H3 region is a statement the
design can make rather than a failure to tell. The steward confirms the effective N per wave and
surface; if it implies a standard error above 0.33 pp, δ is raised to three standard errors before
any number is looked at, and the change is logged.

**T2 (H4), 1P API.** The same statistic and the same three waves on the API, plus the cross-surface
sign test: H4 requires ΔS > 0 with ΔC < 0 on the API in the window where ΔS < 0 on Claude.ai, and the
API's SOC-15 node count rising.

**Exploratory allowance: three tests, after the confirmatory set, each labelled exploratory in the
post, none in a headline and none carrying a p-value.** (1) Which tasks enter and leave the SOC-15
top ten between waves, named and tabulated — for interpretation of H1 versus H2 only. (2) The same C
statistic for the two next-largest SOC groups (Educational Instruction and Library; Office and
Administrative Support) — to show whether a Claude.ai movement is specific to coding. (3) C plotted
against the published whole-universe concentration series — to show the reader how the two
denominators differ.

## 10. Noise and robustness required

- **Persistence across windows.** The August → November leg must agree in sign with August → February;
  a disagreement is reported and downgrades the finding to descriptive.
- **Placebo.** August → November is the pre-advertising window (assumption (iii)); a movement of the
  same size in the placebo window means the February result is not about the February window.
- **Leave-one-out.** Recompute C dropping the single largest SOC-15 task in each wave, and dropping
  the largest task of the August wave from all three.
- **Flagged units excluded, or bounded when they cannot be.** Utah (August 2025) and Wyoming
  (November 2025) are geographic flags and do not bite a global cut; Seychelles does bite November's
  global mix and **cannot be removed at global grain**, so the post states the bound the steward
  supplies rather than treating the November point as clean.
- **Second implementation.** The fixed-August-basket variant of C, and an independent re-derivation
  of the task → SOC join written from the O\*NET file without reusing the first script's loader.
- **Allocation-rule robustness (the LL-32 cut, pre-registered).** C and S recomputed under
  equal-split, employment-weighted and modal-holder allocation; the published bound is ≤0.17 pp on S
  and the post reports the realised movement on C.
- **Node-count and taxonomy checks.** SOC-15 node counts per wave and surface, and the name match
  across waves (globally, 2,888 of 3,170 / 3,260 `onet_task` names match between the November and
  February waves, carrying 99.46% / 99.24% of each wave's mass, `data/ATLAS.md` §Taxonomies), so that
  a concentration movement cannot be read off a changing node set.
- **Base robustness, and boundaries not crossed.** Classified and all-conversation series are
  reported side by side throughout, and a finding that appears on one base only is not a finding; the
  February 2025 and March 2025 flat releases use `pct_occ_scaled` and are reported separately on
  their own base; the June 2026 release rebuilt on O\*NET 30.2 with a new classifier and is not
  spliced to this series.

## 11. Literature check

**Searches run (2026-09-16):** "Chatterji Cunningham Deming how people use ChatGPT programming share
of messages"; "within-occupation concentration of AI task usage decomposition coding tasks 2026"; a
direct fetch of arXiv 2605.21743; and a search of `programme/LEDGER.md` for every item attached to
the coding thread (`R2-09`, `SWE-11`, `SWE-14`, `P1-28`).

**Closest prior work.** (1) Chatterji et al., *How People Use ChatGPT* (NBER WP 34255, 2025): the
nearest thing to a rival series on a consumer product, reporting that "Computer programming and
self-expression both represent relatively small shares of use" (abstract). It reports a level, not a
decomposition, and its taxonomy is its own. (2) Yin and Ogut, *Who Uses AI? Platform Selection and
the Measurement of Occupational AI Exposure* (arXiv:2605.21743v2, 2026-05-27): "Holding the empirical
design fixed, changing only the platform input changes the post-ChatGPT employment coefficient by a
factor of 1.9, and consumer and enterprise channels within the same vendor disagree in sign"
(abstract) — the formal statement of this post's selection problem, and the reason the two surfaces
are reported separately and never pooled. (3) Anthropic's own reports, above.

**Where this sits.** Between a literature that compares providers' totals and a corpus that publishes
one number per category per wave, nobody — Anthropic included — has decomposed a provider's own
coding share from the inside; this post does that on the release data alone, and takes its
interpretive discipline from the selection literature: a composition statistic on a self-selected
user base bounds a reading, it does not identify a mechanism.

## 12. What the closing section will be able to say

**If H1 holds (concentration).** The coding work left on Claude.ai is a more concentrated thing than
it was a year ago: as the category's share fell by roughly a fifth, the ten largest coding tasks took
a larger share of what remained, and did so while the surface as a whole was diversifying. Two
readings survive this evidence — a narrowing frontier, where the coding that stays is the coding
worth doing in a chat window, and a surface left with the routine after the professional work moved
to the API — and which one the next wave supports is what this leaves open.

**If H2 holds (internal broadening).** Coding on Claude.ai is not shrinking so much as being
hollowed out: its share fell and what remained was spread more thinly across its own tasks, with the
tasks that thinned on the consumer surface sitting among the largest on the developer surface in the
same weeks. The corpus's most-quoted series is then a statement about where coding is done rather
than about how much of it there is, which is a weaker claim than the one the agenda's sentence
invites.

**If H3 holds (flat composition, the null the design can deliver).** The composition of coding on
Claude.ai did not move: the ten largest coding tasks held the same share of the category across a
window in which the category itself lost roughly a fifth of its share, with an equivalence interval
that excludes a movement of one percentage point. The fall in coding's share is then a fact about the
denominator — everything else arrived — and a reader who takes the series as evidence that software
work is changing is reading the arrival of other work as the departure of this one.
