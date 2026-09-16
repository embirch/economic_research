# Post 2 · Job or place? · Research plan

Written 15 September 2026, evening, after post 1 was parked. Same rules as post 1 (PLAN → data audit → pre-registration committed → tests → write-up), with the lesson of post 1 applied first: the assumptions sweep is written before any model is run, and every construct is checked against the actual files.

## 0. The question, as the programme card states it

How much of where AI use is distinctive across US states is the jobs people hold, how much is the place itself, and which of the two explains who caught up?

Anthropic's sentences it extends: "Each 1% increase in the share of such tech workers in a state is associated with 0.36% higher usage per capita" and composition explains "nearly two-thirds of cross-state variation" (January 2026); the state Gini fell 0.37 → 0.31 → 0.29 (August 2025 to February 2026); DC's "disproportionate focus on document editing, information provision and job applications" (September 2025).

## 1. Assumptions sweep (done before any model, per the standing rule)

**(a) Value judgement.** "Distinctive" and "catching up" rank states. The post explains variation; it does not treat high adoption as good. Stated once in the write-up.

**(b) Construct mapping: two different "jobs".** *Workforce composition* is the state's labour market (Census ACS occupation shares). *User composition* is the occupation mix Anthropic infers from the conversations themselves (`soc_occupation` shares by state). They are not the same thing, and the gap between them is the selection into Claude use by occupation. The January 2026 result uses workforce composition. The decomposition of the mix must say which it uses at each stage. Design: a two-stage decomposition. Stage 1: workforce mix → user mix (who in the state uses Claude). Stage 2: user mix → what they ask for and make (the mix). "Place" is what remains after both.

**(c) Composition or selection.** Post 1's lesson. A state residual after workforce composition could be Claude's user base in that state rather than the place. Stage 1 measures exactly that selection, so it is part of the answer rather than a caveat. What cannot be removed with public data: selection *within* an occupation (which managers in Mississippi use Claude). Stated in limitations from the first draft.

**(d) Anthropic's own results that cut against or bound the framing.** (i) The January 2026 report already explains two-thirds of the level by composition; the post replicates that first and does not present it as new. (ii) Utah's August 2025 row is abuse-affected by Anthropic's own account and sits 25 points off every other state on delegation (post 1); it is excluded from every test and shown separately. (iii) The request taxonomy changes between releases and cluster suppression is heavy at fine levels (per-state L0 clusters present: 28 of 51 states in August 2025), so the mix is compared within wave at level 2 (26 clusters) and level 1 (108), never at level 0. (iv) June 2026 does not publish request shares within occupation group, which the programme card assumed. The mix decomposition therefore uses what June does publish by occupation group at the global level (artifact, use-case and collaboration mixes) and by state (the same, in `overall`), plus the request mix at levels 1 and 2 by state without an occupation cross. Stage 2 is exact for artifacts, use case and collaboration; for the request mix it is approximated through the O*NET task-to-occupation mapping and said to be.

**(e) The three-provider comparison is partly circular.** Microsoft's state estimates are a Bayesian small-area model that uses demographic covariates; a "place" residual in Microsoft's series is partly imposed by their model. OpenAI's state series is a per-capita rank (2025) plus topic shares by state, which is a direct measurement. The triangulation is therefore Anthropic against OpenAI on the mix (both measured), and all three on the level with the Microsoft caveat stated.

**(f) Sample.** 51 units. Every model has at most three predictors, and the minimum detectable effect is reported for each. No decision rule is keyed to a model whose MDE could be uninformative (post 1's mistake).

## 2. Data, confirmed against the files (15 Sep)

- Anthropic state rows exist in every wave: August 2025 (`geography = state_us`, 51 + not_classified; request L2 for 51, L1 for 45, L0 for 28; `soc_pct` for 47; AUI, usage, GDP, population in-file); November 2025 and February 2026 (`geography = country-state`, `US-XX`, 51 states; request L0–L2, onet_task, collaboration, use_case, primitives; AUI not in file, rebuilt from `usage_pct` and the state population file, convention verified in post 1); April and May 2026 (`geo_level = subregion`, `US-XX`; `overall` carries AUI, use case, collaboration, artifacts; request L0–L2, onet L0–L3 and `soc_occupation` carry `pct`).
- Census ACS 2023 one-year table C24010 (occupation of the employed by state, 25 groups mappable to SOC major groups), B15003 (education), B28002 (broadband), B19013 (income) from the table-based summary files (the API now needs a key). BLS OEWS is blocked to non-browser downloads; ACS occupation shares replace it and the difference is stated.
- Microsoft `State_Rankings_2026Q1.csv` (AI user share, 50 states + DC) and the county file, from the public GitHub repository (MIT/CC licence in repo).
- OpenAI Signals v2.0 public CSVs (CC BY 4.0): `usa_share_of_messages_by_state_2025_rank.csv` (per-capita rank, 51) and `usa_share_of_messages_by_topic_state_2025.csv` (topic shares by state).
- O*NET task statements (task → SOC code) from the February 2025 release.

## 3. Steps

| Step | Script | Done means |
|---|---|---|
| 00 | env | versions printed |
| 01 | load_states | one table per wave with AUI, usage, user occupation shares, request L1/L2 shares; June artifact/use-case/collaboration; Census, Microsoft, OpenAI merged on postal code; merge audit printed |
| 02 | replicate | the 0.36% elasticity (log AUI on log computer/math workforce share) and the Gini series 0.37 / 0.31 / 0.29, plus April and May; any discrepancy stated |
| 03 | stage1_selection | user occupation mix vs workforce mix by state: which occupations are over-represented among users, and how much that differs by state |
| 04 | stage2_mix | shift-share of each state's artifact, use-case and collaboration mix (May 2026) into user-composition and residual; request mix L2 via the O*NET mapping; variance explained; five largest residuals profiled |
| 05 | place | residual AUI (after workforce composition) on education, age, broadband, urbanisation; standardised, HC3, MDE |
| 06 | catchup | ΔAUI August 2025 → May 2026 on the change in the state's user tech share and on place covariates; Utah excluded, February influx noted |
| 07 | providers | rank correlations of Anthropic, Microsoft and OpenAI state levels raw and after workforce composition; Anthropic vs OpenAI state mix correlation raw and after composition |
| 08 | figures | observed vs expected mix; map of residuals; provider small multiples |

Pre-registration (prereg/prereg.md) is written and committed after step 03 and before steps 04–07: hypotheses, models, decision rules with MDE, robustness list, Utah rule.

## 4. Decisions fixed now

- Utah: excluded from every test; shown separately.
- Mix compared within wave only; levels 1 and 2 only.
- Workforce composition = ACS C24010 shares; user composition = Anthropic `soc_occupation` shares; both named as such in every table.
- Cross-wave key: SOC major groups and the `overall` metrics; never request clusters.
- 51 states; HC3; MDE with every coefficient; at most three predictors per model.
