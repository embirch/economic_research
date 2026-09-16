# post5 · Where is AI doing work users could not have completed without it?

*Candidate LL-18. Brief of record; question, title and contribution freeze at Gate 1b.*
**Title as frozen**, settling the editor's title-form point
(`room/editor-2026-09-16-sketch-LL-18.md`): "say" is gone, because the sketch's "work people say
they could not do alone" attributed speech to a classifier and the corpus reserves speech verbs for
self-reports. The replacement negates Anthropic's own construction of the measure — "We measure
whether users could have completed tasks without Claude" (`economic-index-2026-01-report`, 15 Jan
2026, p.21) — and names no speaker; "users" is the classifier prompt's own subject. The question
says AI; every finding will say Claude (criterion 6).

## 1. The question

Does the share of AI use that users could not have completed without it rise or fall with how much a
place uses AI?

## 2. Why it matters, and to whom

Whether AI substitutes for work people would otherwise have done, or does work that would not have
been done at all, is the economic question that decides what adoption means for wages and for the
distribution of the gains. The corpus names it as the question it most hopes its data will settle —
"Whether AI compliments or substitutes work is perhaps the most important question that we hope our
data will help answer" (`economic-index-2025-09-report`, 15 Sep 2025, p.47, concluding endnote 1) —
and it built a measure for exactly this: "We measure whether users could have completed tasks without
Claude" (`economic-index-2026-01-report`, 15 Jan 2026, p.21). That measure is a classifier's
judgement of a counterfactual, read off a transcript, and the report that built it grades it in the
same breath as it reports it: the primitives are "somewhat noisy and not perfectly accurate by
themselves", were "mainly tested for directional accuracy", and "none of the measures should be
taken as exact or definitive" (ibid., pp.22–23). No validation statistic for this facet is published
anywhere in the corpus. So the strongest thing this evidence can carry is a comparison of places,
not a level.

Who decides something differently. The Institute asks "What pre- or re-distributive mechanisms could
effectively spread the gains from AI development and deployment more broadly?" (`ED-5`,
`institute-agenda-2026-05`) and, on adoption, "AI development is concentrated in a small number of
companies in a small number of countries, but deployment is global … If it can access it, how does
it capture economic value from AI?" (`ED-1`, ibid.). Those questions answer differently depending on
whether the work Claude does in low-adoption countries is work its users could have done anyway,
more slowly, or work that would not otherwise have been produced; a development ministry weighing
access against complementary investment needs the sign of that gradient, not its global average.

What this data can say that nothing else can. The Economic Index publishes this counterfactual
judgement for every conversation in a one-million-conversation sample, aggregated to 173 and 176
countries in two waves. No survey asks a respondent whether the task just finished was one they
could not have finished alone; the nearest external measures are self-reported time savings and
capability ratings of activities. What the corpus has never published is any geography of this
measure — the global figure and one country, read two ways.

## 3. The thread of Anthropic's inquiry this builds on

Thread **T4** (task-level primitives and productivity; `programme/THREADS.md` §T4), with the ledger
items `L-2026-01-R4-39`, `L-2026-02-IND-16` and `L-2026-02-IND-06`, all open.

The construct, verbatim, as the classifier is asked it (`economic-index-2026-01-report`, 15 Jan
2026, Table 2.1, p.20; the identical prompt is reprinted for the February wave at
`economic-index-2026-03-appendix`, Table A.1, p.4):

> "Could the User have completed this task by themselves? Choose from these options:
> • Yes: the User would have been able to complete the task without the Assistant, even if it would
> have taken more time
> • No: the User would not have been able to complete the task without the Assistant, even with more
> time"

Its place in the programme (ibid., p.21):

> "**Human and AI skills** address how automation interacts with skill levels. If AI
> disproportionately substitutes for tasks requiring less expertise while complementing
> higher-skilled work, it could be another form of skill-biased technical change… We measure whether
> users could have completed tasks without Claude, and the years of education needed to understand
> both user prompts and Claude's responses."

What the thread has established. The global level, twice: "Human could do alone **88%**"
(`economic-index-2026-01-report`, Figure 2.2, p.25, N = 999,875), and its complement tracked over
one interval — "Human can't do alone (%) 12.09 → 12.24, ▲ +0.15", with the caption "All differences
are statistically significant with p<0.001, except Human-only time with p<0.05"
(`economic-index-2026-03-report`, 24 Mar 2026, Table 1.1, p.9), glossed as "One change goes
ostensibly in the opposite direction: the tasks performed by Claude were judged to be slightly less
possible for a human without access to AI" (ibid., pp.8–9). One decomposition exists, by request
type at global grain: "Claude estimates that users would be able to complete personal life
management requests by themselves 96% of the time, versus 82% for software development
requests—indicating that Claude provides more essential support for technical work"
(`economic-index-2026-01-report`, p.25). Where the thread is open: the measure has never been
compared across places. The fourth report's country-level chapter plots five primitives against the
AI Usage Index — human-only time, human education, AI autonomy, work use case, task success (Fig
3.3, p.31) — and human-only ability is not one of the five, although it sits in the same file and is
used as a control in the Figure 3.5 partial regression (p.34). ⟨mentor⟩ The measure is one the
intended mentor built and then tracked: lead authorship of the primitives report and of the first
over-time table carrying this row (`economic-index-2026-01-report`, p.1, ch.4;
`economic-index-2026-03-report`, Table 1.1, p.9; `programme/THREADS.md` T4(e)).

## 4. Overlap, stated

- **Anthropic, the global level.** Figure 2.2 publishes 88% for November 2025 and Table 1.1 of the
  next report publishes the complement for both waves (12.09 → 12.24). *New here:* the same measure
  at country grain, which no Anthropic publication reports for any country but one.
- **Anthropic, the one country.** The India spotlight reports "We find that 84.6% of tasks could be
  completed by a human alone (vs. 87.9% globally)" (`country-brief-india-2026-02`, §Economic
  primitives) with no comparison group and no interval, and reads the same figure in two directions:
  as evidence that "Higher shares of complex tasks that humans could not complete alone suggest that
  Indian users are using the technology at the frontier" (§Executive summary) and, among the
  evidence for a different claim, as "frequent use for tasks humans could do alone" (§Implications).
  *New here:* the comparison group, the interval, and a stated choice of which reading is tested —
  the first, `L-2026-02-IND-06`, tested with composition held as constant as the public files allow.
- **Anthropic, as a covariate.** "human ability" is one of nine controls in the Figure 3.5 partial
  regression of task success on human education (`economic-index-2026-01-report`, p.34). *New here:*
  it is the outcome, and its own gradient in adoption and income is estimated.
- **The earlier programme, as a bound, cited and not inherited.** `reference/posts/post1` found that
  the user bases behind low-AUI countries are professional rather than general-population. That
  finding is not re-derived here; it is the reason every holds-branch sentence in this post is about
  who Claude's users are in low-adoption countries rather than about those countries' economies
  (referee correction 5). That post also already ran the adoption-and-income regression on the
  task-mix residual of the automation share, so no "first test of geography" claim is made here
  beyond this specific primitive.
- **Outside Anthropic.** Humlum & Vestergaard (2025) measure self-assessed time savings and quality
  by occupation; Bick, Blandin, Deming & Schumacher (2026) measure aggregate adoption and time
  savings; Tomlinson et al. (2025) rate how much of an activity AI can do. None asks whether the user
  could have done the work, and none has a geography of such a measure.
- **Separation from post6 (LL-31), per the director's pairs ruling.** This post is on the primitive
  `human_only_ability` at country grain in the two 2026 long waves. post6 is on artifact shares at
  country and state grain in the June 2026 release. Neither uses the other's outcome variable; the
  shared element is the adoption and income axis, which post6 must state for its own grain.

## 5. Contribution

If the share of work users could not have completed without Claude is higher where Claude is used
less, the post shows that Claude's users in low-adoption countries bring it work that would not
otherwise have been produced; if it is higher where Claude is used most, that work is concentrated in
the economies already using the technology most densely; either way it is the first cross-country
distribution of the corpus's only counterfactual-capability measure, with intervals, with its
residual, and with its task mix held as constant as the public files permit.

## 6. Hypotheses

The outcome throughout is a country's `no` share — conversations the classifier judges the user could
not have completed without the Assistant — on the renormalised base `no / (yes + no)`, the base the
global rows publish. Adoption is the rebuilt AI Usage Index; income is GDP per working-age capita.

**H1 — Substitution where adoption is thin.** The `no` share falls with adoption: countries in the
bottom adoption tercile show a higher `no` share than those in the top, in both waves.
*Signature only H1 predicts:* a negative gradient in the AUI that survives conditioning on log GDP
per working-age capita and on human-only time, keeps its sign in both waves, and survives the
partial task-mix adjustment with the covered share printed.
*What would count against it:* a gradient of zero or positive sign in either wave; a gradient that
loses its sign once income is conditioned; a gradient that is an artefact of the `not_classified`
residual (i.e. reverses on the all-conversation base); or a tercile gap inside the permutation null.

**H2 — The frontier reading (rival, from `L-2026-02-IND-06`).** The `no` share rises with adoption
and with income: the work users could not have done alone is concentrated where the technology is
densest, which is the spotlight's "at the frontier" conjecture stated as a cross-country
prediction.
*Signature only H2 predicts:* a positive gradient in both adoption and income, with the income
gradient surviving conditioning on adoption — the two axes agreeing, which H1 does not require.
*What would count against it:* a negative or zero gradient; or a positive raw gradient that
disappears in the task-mix-adjusted residual, which would make it H3.

**H3 — Composition, not capability.** Whatever gradient exists in the raw share is the task mix of
what Claude is asked to do in each country, not a difference in what its users could have done.
*Signature only H3 predicts:* a raw gradient distinguishable from zero together with an adjusted
gradient that is not, with the ordering of terciles preserved in the predicted (shift-share) series
and absent in the residual series.
*What would count against it:* an adjusted gradient of the same sign and comparable magnitude to the
raw one; or a predicted series with no gradient of its own.

**H4 — The classifier is reading places differently.** The cross-country variation is variation in
how the classifier reads prompts, not in the work.
*Signature only H4 predicts:* the `not_classified` share has its own gradient in adoption, so that
renormalising is not neutral and the raw and renormalised gradients disagree in sign; and the
country ranking is no more stable between the two waves than its own sampling precision allows.
*What would count against it:* a flat `not_classified` gradient, raw and renormalised gradients that
agree, and a November-to-February rank correlation materially above what count-based resampling
produces.

## 7. Assumptions sweep

**(1) Value judgement in the framing — newly flagged; design change made.** "Closing a capability
gap" and "widening one" are the sketch's words and they order the two outcomes morally before the
number is seen. The change: "gap", "deficit", "bypass" and "leapfrog" appear in no finding sentence;
findings state a share, a difference in shares and its sign. The second half of the judgement is the
choice of reading: the India spotlight reads its own 84.6% in two directions (`L-2026-02-IND-16`), so
this brief fixes the reading under test — a higher `no` share is read as work the user could not have
completed without Claude, and not as skill, sophistication or frontier status.

**(2) Construct mapping — handled, with the level ruled out of use.** The measure is Claude's answer
to one question about one transcript: "Could the User have completed this task by themselves? … No:
the User would not have been able to complete the task without the Assistant, even with more time"
(`economic-index-2026-01-report`, Table 2.1, p.20). Three properties follow and are designed around.
It is a judgement, not a report: no user is asked, so the post attributes it to Claude in every
sentence. It is unvalidated in the corpus for this facet: validation was against "a human researcher
on a small set of transcripts in which users gave feedback to Claude.ai", of which the report says
"Neither data sources are fully representative of Claude.ai or 1P API traffic" (ibid., p.22), and the
grade given is "directionally accurate even if they may deviate somewhat from human ratings" (p.22) —
so the level is not interpreted and every claim is a difference between places on one instrument. And
the unit is a conversation: "The unit of observation is a conversation with Claude on Claude.ai, not
a user" (ibid., fn2, p.36), so the outcome is a share of conversations, never of work or hours.

**(3) Composition and selection — newly flagged; three design changes.** Who Claude's users are in
each country is not observed. No release carries a user, account, plan, industry or language column,
and the country aggregate is a share of conversations sampled from whoever in that country was using
Claude.ai in one week. Two facts bound how much of any gradient this could produce. First,
Anthropic's own category spread on this very measure is four times the largest published country
difference: 96% for personal life management requests against 82% for software development requests
(`economic-index-2026-01-report`, p.25), a 14-point spread, against India's 3.3-point difference from
global (84.6 vs 87.9). Shifting about a quarter of a country's conversations between those two
request categories reproduces the whole country gap, which is why H3 is a pre-registered rival and
not a robustness check. Second, the India
spotlight's own composition — the highest software share in the world — is never held constant, which
is `L-2026-02-IND-06`. The changes: (a) every holds-branch sentence is about **who Claude's users are
in low-adoption countries**, not about those countries' populations or economies, with
`reference/posts/post1`'s professional-user-base finding cited as the bound that licenses that
wording and nothing stronger (referee correction 5); (b) the task-mix adjustment is run and reported
beside the unadjusted gradient, with the covered share printed next to both, because it is partial by
construction — a country's published `onet_task` mix reaches a median 34.1% (November) and 29.0%
(February) of that country's own conversations, the rest sitting in the `none`/`not_classified` node
(`data/ATLAS.md` §Dated log (e) 2), so about 30% of a country's conversations carry the mix that the
adjustment uses; (c) the post states that the adjustment holds constant the mix of *named tasks*
only, and cannot hold constant which users brought them.

**(4) Anthropic's own results that cut against or bound the framing — newly flagged; covariate added.**
Three. First, the fourth report already finds that low-adoption countries bring Claude *longer* and
*more autonomous* work: at country level, ln AUI against human-only time gives r = −0.561, β = −0.97
and against AI autonomy r = −0.801, β = −8.10 (Fig 3.3, p.31). A negative `no`-share gradient would
therefore sit inside an existing pattern rather than be news about capability, so human-only time
enters as a pre-registered covariate and the conditional gradient is reported beside the
unconditional one. Second, the same report warns off the causal reading: "Importantly, the primitives
themselves are not necessarily causal factors—we don't know if income or education are truly driving
adoption, or if they're proxies for other underlying conditions" (pp.32–33), and the post makes no
adoption-causes-anything claim. Third, the global level barely moves across four windows — 87.91,
87.76, 87.79, 87.62 (`data/ATLAS.md` §Components, boundary list) — which bounds the plausible size of
any geography in it and is why the MDE is stated beside the null branch rather than after it.

## 8. Data, confirmed at column level

The data steward's feasibility line for this candidate, verbatim and in full, from
`programme/LONGLIST.md` (originally `room/steward-2026-09-16-longlist-feasibility-batch-2-answers.md`):

> "**LL-18. FEASIBLE.** `human_only_ability` exists at `global`, `country` and `country-state` in both
> 2026 waves (938 / 1,082 sub-national units), plus `onet_task::human_only_ability` at global over
> 3,169 / 3,259 tasks. **115** countries carry the facet and clear 200 conversations in both waves. The
> residual is **`not_classified` in both waves** (never `none`) at country and `country-state`, median
> **10.34% / 11.11%**; global publishes `yes`/`no` only, summing to 100 (yes 87.9097 → 87.7599).
> Log (f) 5."

The steward's confirming note is `posts/post5/notes/feasibility.md`, written after this brief; it
confirms or contradicts each cut below at column level, with a command.

**Cuts, at column level.** Long schema (Family B), `platform_and_product = Claude AI (Free and Pro)`,
read with `keep_default_na=False` (and `na_values=[]` for the February file, where `NONE` is a real
`geo_id`); `NA` is Namibia in both.

| # | release | grain (`geography`) | `facet` | `level` | `cluster_name` | `variable` | threshold / rule |
|---|---|---|---|---|---|---|---|
| C1 | `release_2026_01_15`, `release_2026_03_24` | `global` | `human_only_ability` | 0 | `yes`, `no` | `human_only_ability_pct` | none; publishes yes/no only, sums to 100 |
| C2 | both | `country` | `human_only_ability` | 0 | `no`, `yes`, `not_classified` | `human_only_ability_pct`, `human_only_ability_count` | `usage_count ≥ 200` applied by this post, both waves; 115 countries clear it in both |
| C3 | both | `country` | `country` | 0 | empty string | `usage_count`, `usage_pct` | same 200 rule; `usage_pct` at country is a share of the **global** sample |
| C4 | both | `global` | `onet_task::human_only_ability` | 0 | `<task>::no` / `::yes` | `onet_task_human_only_ability_pct`, `_count` | global only; 3,169 / 3,259 tasks; each `_pct` is a share of its **base cluster** |
| C5 | both | `country` | `onet_task` | 0 | named task nodes + `none`/`not_classified` | `onet_task_pct` | median 21 / 18 published nodes per country; named nodes are a median 34.1% / 29.0% of a country's mass |
| C6 (robustness only) | `release_2026_06_26` | `country`, `geo_level` = `country`, `category_name` = `overall` | — | — | — | `human_only_ability_pct`, `usage_per_capita_index` | 121 country ids; **no count metric of any kind**, so the 200 rule cannot be applied or checked |

Primary outcome: `no` share on the renormalised base `no_pct / (yes_pct + no_pct)`, which is the base
the global rows use and therefore the base on which the published number reproduces. The raw
`no_pct` (a share of the geography's total **including** `not_classified`) and the
`not_classified_pct` itself are reported beside every rate and never renormalised away silently; the
gradient is re-estimated on the raw base as a pre-registered robustness, and the `not_classified`
gradient is H4's confirmatory test. Counts in `release_2026_03_24` are on a 1,000,000 sample base,
not conversations — every global `{facet}_count` sums to exactly 1e6, so "200 per country" means 200
per million (`data/ATLAS.md` §Other bases; referee correction 5); November's sample is the same order
(Figure 2.2's N = 999,875). At 200 per million and p ≈ 0.12 the binomial standard error of a country's
`no` share is about 2.3 percentage points, larger than the largest published country difference, so
the gradient is count-weighted and the MDE uses the Kish effective N, not the nominal 115. Seychelles
is excluded by the report's own rule — "we exclude the Seychelles from all geographic analyses because
a large fraction of usage we saw during the sampling dates was abusive traffic"
(`economic-index-2026-01-report`, fn5, p.37): it is 2.5% of the November global sample and absent from
the February file altogether, so the rule bites in one wave and is inert in the other. The 23
`EXCLUDED_COUNTRIES` are already absent from both.

**Supplementary data.** Both files ship inside an Economic Index release and are used as static 2024
annuals, because the 2026 waves ship no population, GDP, AUI or usage-tier column
(`data/ATLAS.md` §Cuts 22, 29).

- `release_2025_09_15/data/intermediate/working_age_pop_2024_country.csv` (194 × 5:
  `iso_alpha_3, year, working_age_pop, country_code, country_name`; World Bank SP.POP.1564.TO 2024
  plus Taiwan). **Why needed:** the adoption axis; no 2026 wave publishes the AUI, so it is rebuilt.
  **Join key:** the file's own ISO-2 `country_code` against the waves' ISO-2 `geo_id`, with
  `iso_country_codes.csv` as the check on the `iso_alpha_3` bridge. **Coverage:** the atlas records
  the February merge audit as 178 country rows in, 170 matched, 8 unmatched (`not_classified`,
  `NONE`, GF, GG, GP, JE, MQ, RE).
- `release_2025_09_15/data/intermediate/gdp_2024_country.csv` (174 × 3:
  `iso_alpha_3, gdp_total, year`; IMF NGDPD 2024, USD). **Why needed:** the income axis, and the
  covariate that separates H1 from H2; income enters as log `gdp_total / working_age_pop`, the same
  construction as the August 2025 enriched column `gdp_per_working_age_capita`. **Join key:**
  `iso_alpha_3`, via the same bridge. **Coverage:** 113 of the 115 balanced-panel countries carry
  IMF GDP (`data/ATLAS.md` §Dated log (e) 4).

**The published numbers this reproduces first** (criterion 3), in this order:

1. "Human can't do alone (%) 12.09 → 12.24" (`economic-index-2026-03-report`, Table 1.1, p.9), as
   `100 − human_only_ability_pct[yes]` at `global` in the two waves: 100 − 87.9097 = 12.0903 and
   100 − 87.7599 = 12.2401, Seychelles included as published. This also fixes the polarity: the
   published series is the complement of the file's `yes`, and it is the outcome of this post.
2. Figure 2.2's "Human could do alone 88%" (`economic-index-2026-01-report`, p.25), the same row.
3. The rebuilt AUI, against a published level: Canada's "Anthropic AI Usage Index (AUI) is 4.4"
   (`country-report-canada-2026-07`, §"Canada is at the forefront of Claude adoption", Figure 1 right
   panel) reproduces as 4.4430 from `release_2026_03_24` with the usage denominator over thresholded
   countries only, and as 3.6219 under the August-2025 `+ not_classified` rule; the symmetric rule is
   therefore the one used for every 2026 AUI level here (`data/ATLAS.md` §The AI Usage Index).
4. As the positive control on the rebuilt AUI, Figure 3.3's country regression of ln AUI on human
   education, r = 0.359, R² = 0.129, p < 0.001, β = 0.75 (`economic-index-2026-01-report`, p.31),
   which uses an AUI the wave does not ship and so tests the rebuild end to end.

## 9. Confirmatory tests and the exploratory allowance

Four confirmatory tests, one per hypothesis, both waves, count-weighted, Seychelles excluded.

- **T1 (H1/H2 direction).** Regress the country `no` share on the rebuilt ln AUI, then on ln AUI with
  log GDP per working-age capita and human-only time added; report the top-against-bottom adoption
  tercile difference in percentage points as the key number, with its interval, in each wave. H1 is
  a negative gradient in both waves; H2 is a positive gradient in both axes.
- **T2 (H2's income axis).** Regress the same outcome on log GDP per working-age capita with ln AUI
  conditioned, which separates "where it is used most" from "where income is highest".
- **T3 (H3).** Build the shift-share prediction from the global `onet_task::human_only_ability`
  task-level `no` shares applied to each country's published `onet_task` mix, and re-run T1 on the
  residual (actual − predicted) and on the prediction separately, printing the covered share beside
  each estimate.
- **T4 (H4).** Regress the country `not_classified` share on ln AUI; and compare the
  November-to-February rank correlation of the `no` share against the distribution produced by
  count-based resampling of both waves.

**Exploratory allowance: two tests, after the four above are run and reported.** (E1) The association
between the `no`-share gradient and a static indicator of English as an official or administrative
language, coded from a fixed published list before the values are inspected — to characterise H4's
mechanism if H4's in-release signature fires; no confirmatory claim rests on it, because no release
carries a language column (`data/ATLAS.md` §Cuts 26) and the join is untested. (E2) A description of
which task nodes carry the global `no` mass, from `onet_task::human_only_ability` over 3,169 / 3,259
tasks — to tell the reader what kind of work the measure picks out, in the interpretation section
only. Any further test is a deviation and is logged as one.

## 10. Noise and robustness required

- **Persistence across windows.** Both 2026 long waves reported side by side, never averaged; the
  sign of the gradient must hold in each. The two June 2026 calendar months are a third and fourth
  window for ranks only (cut C6): the June file carries no count metric of any kind, so the 200 rule
  cannot be applied, and it carries no `not_classified` node at all — the global level is comparable
  (the boundary move in `human_only_ability_pct` is −0.06, `data/ATLAS.md` §Dated log (f) 10) but no
  June number enters a confirmatory test.
- **Leave-one-out.** Over the 115 countries, and over the top and bottom adoption tercile
  separately; the key number must not depend on any single country.
- **Flagged units excluded.** Seychelles under the report's own rule, stated in both waves and shown
  to be inert in February (the report's Wyoming exclusion does not bind at country grain). Any
  country whose `not_classified` share exceeds twice the median is shown separately.
- **Placebo and permutation.** A permutation null for the tercile difference, reassigning adoption
  ranks across countries; and the positive control of §8 item 4, which must reproduce a published
  gradient before any new gradient is reported.
- **Second implementation.** The country panel and the gradient built twice, independently, including
  the AUI rebuild; the two must agree to the printed precision before any number leaves the post.
- **MDE beside the null.** With 115 countries a correlation of about 0.26 is detectable at 80% power
  and α = 0.05; the percentage-point MDE for the tercile difference is computed from the
  cross-country standard deviation of the `no` share and the Kish effective N under count weights,
  both of which the steward is asked to report in `posts/post5/notes/feasibility.md`.

## 11. Literature check

Searches run: `wiki/reports/` for every appearance of this primitive (`human_only_ability`, "could
do alone", "without the Assistant"), which returns the four uses named in §3 and §4 and nothing else;
and a web search for cross-country work on counterfactual capability and AI use (2026), which returns
adoption and exposure measures, the International AI Safety Report's capability assessment and
macro-distributional commentary, and no measure of whether a user could have completed the work.
Closest prior work, checked at long-list stage and re-fetched by the referee: Humlum & Vestergaard
(2025), self-assessed time savings and quality by occupation from a worker survey — complementarity
with no counterfactual-capability item; Bick, Blandin, Deming & Schumacher (2026), adoption and
aggregate time savings; Tomlinson et al. (2025), a "scope" rating of how much of an activity AI can
do, a statement about the technology rather than the user. METR's task-horizon work measures model
capability on fixed benchmark tasks, which the fourth report distinguishes from its own setting on
selection grounds (`economic-index-2026-01-report`, p.42). Where this sits: the first geography of a
counterfactual-capability construct, and a description of Claude's users by place rather than an
estimate of any country's capability.

## 12. What the closing section will be able to say

**If H1 holds (the `no` share is higher where adoption is lower).** Where Claude is used least, the
people using it bring it a larger share of work that Claude judges they could not have completed
without it — a difference of X percentage points between the top and bottom adoption terciles, in both
waves, on a measure whose level should not be read but whose ranking is stable. The claim is about
who Claude's users are in those countries, professional users on the evidence of the earlier
programme's finding, and not about those countries' workforces; the substitution question the corpus
calls its most important now has a geography, and it points away from the places with the most use.

**If H2 holds (the share is higher where adoption is higher).** The work users could not have
completed alone is concentrated in the economies where Claude is already densest, by X percentage
points between terciles, and the spotlight's frontier reading generalises beyond the one country that
prompted it. Convergence in usage per capita would then not imply convergence in what the technology
is doing, because the places adopting later are bringing work their users could have done anyway.

**If the result is null (no gradient the design can detect).** The first cross-country distribution of
this primitive is flat: across 115 countries in two waves the top and bottom adoption terciles differ
by less than the design's minimum detectable difference of X percentage points at 80% power, against a
residual that runs at a median of a tenth of a country's conversations, so the 88% global figure hides
no geography this instrument can resolve. That is a result about the measure as much as about the
world, and it is the sentence the corpus could have written when it published the global figure and
did not.
