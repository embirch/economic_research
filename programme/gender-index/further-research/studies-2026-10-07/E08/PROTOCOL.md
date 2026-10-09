# E08 execution and writing protocol

**Integrated protocol v1, 7 October 2026.** This version incorporates the [separate reader review and coordinator decisions](REVIEW.md). The [contributor draft](contributions/E08-plan.md) is preserved. This is a specification after prior pilot inspection, not a completed study or an untouched preregistration.

Emily selected E08, E03 and E10 on 7 October 2026. This contribution specifies E08 only and does not reopen that selection. It is a plan for executing and writing a descriptive empirical study, not a completed manuscript or an estimate of AI’s causal economic effects. Existing feasibility analyses and independent checks are reused rather than restarted.

The working question is: **Among reference-job employees aged 15–69 in Canada’s ten provinces, how does the reported frequency of unpaid job work during personal time differ between workplace GenAI users and nonusers, and how does that association differ between Men+ and Women+?**

The purpose is to test whether descriptions of workplace AI participation also reveal differences in an observed work burden. The practical use is to improve the outcomes and recruitment strata of subsequent workplace evaluations: adoption and paid work hours alone may miss work performed without pay during personal time. This survey cannot tell an employer whether adopting AI will reduce that burden, whether an employee’s burden changed after adoption, or who captures productivity gains.

The assignment uses branch `work/index-steward-pilot-2026-10-01`, with this contribution owned at `selected-studies-2026-10-07/contributions/E08-plan.md`. Current external spending cap is $0. This planning step makes no new primary estimates, transfers no respondent files, launches no paid calls and changes no historical analysis or live page. Implementation outputs listed below are proposed next-stage deliverables, not files claimed already produced.

## 1. Population, time and measurements

Use the public Canadian Survey on Working Conditions (CSWC) 2024–2025, collected in four waves from 23 September 2024 to 18 July 2025. The target is the pooled survey reference-job population, not a single-date workforce or a worker panel. Restrict to public/private employees, `COWMAIN3` in character codes `1` and `2`; exclude code `3`, self-employed. Retain all five released age categories, covering 15–69. The inspected file contains 23,314 people overall and 20,538 employees.

The frame covers the ten provinces and excludes the territories, institutionalized people, full-time Canadian Armed Forces members, people living on reserves and other Indigenous settlements in the provinces, and extremely remote low-density areas. Unpaid family workers are outside the survey employment frame. Respondents come from Labour Force Survey (LFS) households, and CSWC does not accept proxy answers. Report these limits in Methodology rather than calling the sample all Canadian workers.

**Reference-job timing is a substantive qualification.** The guide reports that 4.9% of the whole CSWC sample answered about a job or business they had already left. That is not an independently estimated percentage for this employee subset. The identifying variable `CHG_05` is unavailable in the public file, so this group cannot be removed. For these respondents, 12-month items concern the last 12 months they worked at that reference job, with past-tense routing; for other respondents they concern the preceding 12 months. LFS-derived characteristics refer to its earlier reference week. These observations cannot establish which came first, GenAI use or unpaid work.

There is no usable public wave field. Do not infer a trend from the four collection waves, split a trend by file order, or treat a 12-month recall question as a before/after observation. A published aggregate adoption trend cannot identify the proposed joint use/gender/work-burden trend.

| Role | Public field and frozen coding | Interpretation |
|---|---|---|
| Join | `PUMFID`, one-to-one between analytical and bootstrap files | Key only; never publish it or other respondent records. |
| Employee denominator | `COWMAIN3`: `1` public, `2` private | Reference main-job employee status. Keep both sectors in the primary population. |
| Gender | `GENDER`: `1` Men+, `2` Women+ | CSWC-reported gender, aggregated for confidentiality. Some nonbinary respondents are redistributed into these categories. Preserve plus signs; no independent nonbinary estimate or biological-sex interpretation. |
| Workplace use | `G_AI_05A`: `1` yes, `2` no | Any reported use of GenAI tools for the reference main job over the relevant 12-month period. No use intensity, adoption date, employer introduction or productivity measure. |
| Primary burden | `WTQ_45`: `1` daily, `2` several times a week, `3` several times a month, `4` once a month or less, `5` never | Unpaid work during free time to meet reference-job demands. It is job work, not unpaid domestic or care work, and frequency is not a number of hours. |
| Primary binary outcome | `Y = 1[WTQ_45 ∈ {1,2}]` | Frequent unpaid job work, defined as daily or several times a week. This threshold was already inspected and will not be retuned to a preferred result. |
| Secondary flexibility | `WTQ_60`: `1` very easy, `2` easy, `3` difficult, `4` very difficult; `D = 1[WTQ_60 ∈ {3,4}]` | Difficulty taking one or two hours off during work for personal/family matters. A separate assessment without an explicit 12-month recall, subject to reference-job wording; not another measure of unpaid-work hours. |
| Adjustment | `AGECAT`, `EDUC_G`, `NOC7`, `NAICS8`, `COWMAIN3`, all categorical | Five age groups; three education groups; released broad occupation, industry and sector. `NOC7` actually has eight released codes `00`–`07`; do not infer seven categories from its name. |
| Point weights | `CSWCWT` | Producer’s public-use survey weight. Never substitute unweighted rates or normalize weights into pseudo sample sizes. |
| Uncertainty | `BSW1`–`BSW1000` joined by `PUMFID` | Producer-supplied generalized bootstrap weights for the PUMF, distinct from the confidential master-file Rao–Wu–Yue replicates. |

Audit code values before deriving binaries. A missing, invalid or skipped value must not become a “no.” The inspected core fields are complete, but the guide describes nearest-neighbour donor imputation and does not release imputation flags. Consequently, no observed-only or multiple-imputation sensitivity can be claimed from this file. Do not create one by guessing which rows were imputed. If the pinned inputs reproduce the inspected completeness, retain all 20,538 employees; if a file/version difference creates exclusions, stop and document the discrepancy before changing the analysis target.

## 2. Estimands and their order

Let `g` be Men+ (`M`) or Women+ (`W`), `a` be reported GenAI use (`1`) or nonuse (`0`), and `w` be `CSWCWT`. Define `p_ga` as the survey-weighted proportion with `Y=1` in that group.

**Primary descriptive contrast:**

`Δ_raw = (p_W1 − p_W0) − (p_M1 − p_M0)`.

Report percentage points, all four group proportions, both within-gender user/nonuser differences and their intervals alongside the interaction. A positive interaction means the user/nonuser difference in frequent unpaid work is larger for Women+; it does not mean AI increased their work, and the interaction alone does not state which group has the highest burden. The four proportions supply that context.

**Full distribution:** For each of the same four groups, estimate the five `WTQ_45` category shares, summing to one before rounding. This is a planned description, not a search across five alternative primary thresholds. Show whether the binary comparison describes a broader frequency pattern or mainly one part of the distribution. Do not average the numeric category codes, assign hours to them, or declare ordinal dominance from one threshold. Category contrasts are secondary and their intervals are pointwise unless explicitly upgraded in a documented prospective analysis.

**Secondary outcome:** Repeat the four-rate, two within-gender differences and gender interaction for `D`, with the four-category `WTQ_60` distribution in the supplement. Keep this separate from the primary outcome. More unpaid work can coexist with greater ability to take personal time; do not average the two into a new burden index or select whichever gives the preferred gender narrative.

**Adjustment has two distinct, explicitly secondary targets.** Publish the following in fixed order, not as a competition to find the “correct” sign.

1. **Additive projection in the whole eligible employee sample.** Fit survey-weighted least squares to `Y` with intercept, Women+ indicator, user indicator, their interaction and categorical main effects for age, education, broad occupation, broad industry and public/private sector. The existing design has 25 columns and full rank. The coefficient on Women+ × use is `Δ_add`: the interaction in this prespecified weighted linear projection, with common additive covariate slopes. It uses all eligible records and can borrow model structure across sparse covariate combinations. It is neither a causal adjustment nor a nonparametric comparison of otherwise identical jobs. It need not equal the contrast standardized below. Audit fitted ranges and leverage; do not interpret out-of-range linear predictions as individual probabilities, silently switch links, or call the coefficient an explained/unexplained causal decomposition. Apply the same model to `D` as a secondary analysis.

2. **Direct common-composition description.** For the first target, form `NOC7 × COWMAIN3` strata. For the second, form `NOC7 × COWMAIN3 × EDUC_G` strata. For each definition, let `C` contain only strata observed in all four gender/use groups. Let `q_s` be the pooled survey-weighted share of stratum `s` among all four groups restricted to `C`, and `p_ga,s` the within-stratum group proportion. Estimate `p_std,ga = Σ(s∈C) q_s p_ga,s`, then `Δ_std = (p_std,W1 − p_std,W0) − (p_std,M1 − p_std,M0)`. Every group is evaluated at the same empirically pooled covariate mix. This is nonparametric across the stated strata, but does not make members identical within broad occupations or measure individual task suitability.

The first common-composition target retained all employees in the pilot. The education extension retained 20,413 records, 99.44% of employee weight, across 44 common strata. It is a restricted overlap population, not automatically the entire employee population. For each version publish retained record count, retained weight by each of the four groups, overall loss and the covariate definition.

**Prospectively freeze a same-support raw comparison:** compute the unstandardized four rates and interaction on exactly each target’s `C` before standardizing. This separates changes caused by restricting the population from changes caused by applying a common mix. It is a new planned diagnostic, not a claim that this decomposition has already been executed. Do not change `C` according to outcomes. Fix its observed-support membership across bootstrap replicates and recompute its pooled weighted mix within each replicate. Inference is conditional on that observed-support choice. Report `Delta_raw,C - Delta_raw,full` and `Delta_std,C - Delta_raw,C` as descriptive restriction and composition changes. If their intervals are shown, construct each change inside the same replicate before estimating variance; do not subtract marginal interval endpoints or ignore covariance.

Adding age to the nonparametric education target already lost 15.24% of weight and produced two zero replicate-cell denominators. Preserve this failed support result as an appendix diagnostic. It is not a cleared national estimate. Do not remove the offending replicates, insert pseudo counts, extrapolate into the empty cells or rebrand the additive regression as having solved nonparametric support. No richer stratum search is planned.

## 3. What has already been seen, and what can still be frozen

This is retrospective planning after substantial feasibility inspection. The sample, outcome threshold, full frequency distribution, raw contrasts, additive adjustment, common-support targets and secondary time-off outcome have already been inspected. The title, selection and framing must disclose that history; this is not an untouched confirmatory preregistration.

The following are existing diagnostics, rounded here for planning, not final findings:

| Existing target | Frequent unpaid-work user/nonuser interaction, Women+ minus Men+ | Approximate 95% half-width |
|---|---:|---:|
| Raw employee description | +3.4 percentage points | 2.9 points |
| Additive age/education/occupation/industry/sector projection | +2.7 points | 2.9 points |
| Common occupation/sector composition | −1.7 points | 3.4 points |
| Common occupation/sector/education composition | −1.0 points | 3.5 points |

These are not contradictory estimates of a single causal effect. They differ in composition target, retained population and model restrictions. Their sensitivity is central to the study’s explanation: the release does not establish a unique adjusted gender ordering. The raw comparison remains primary because it describes the selected population; the adjustments expose how much the description depends on who holds which broad jobs, without proving why that happens.

Freeze before further primary analysis: the estimator hierarchy above, same-support raw diagnostic, chart set, source quality rules, rounding, final table schema and deviation process. Mark every genuinely new analysis as prospective from that freeze; keep earlier outputs in an immutable pilot ledger. Any later subgroup, threshold, covariate, transformation, model, endpoint or source-version change gets a dated reason and both versions retained. No new geography, wave, training-route or self-employment study is added implicitly. E07 is separate and is not smuggled into E08 as an outcome-dependent extension.

## 4. Survey uncertainty and support

For any statistic `T`, compute `T_hat` using `CSWCWT`, recompute the entire statistic under each `BSWb`, and use the public guide’s formula:

`Var_hat(T_hat) = (1/1000) Σ_b (T_b − T_hat)^2`.

Center on the full-weight estimate, not the replicate mean; divide by 1,000, not 999. For a vector of estimates use the analogous outer-product covariance around the full vector. Construct contrasts within each common replicate so their covariance is retained. No independently bootstrapped group margins, ordinary row bootstrap or independent-binomial standard errors replace this procedure.

Each adjusted model must be refitted under all 1,000 weights with the same design coding. Each common-composition replicate must recompute group-cell denominators, means and the pooled target mix. Check positivity of every required denominator, finite estimates, rank/estimability, weight alignment and normal-equation residuals. If a declared statistic is undefined in a replicate, retain and explain the failure; do not calculate a standard error after dropping failed replicates.

Use the already established normal-approximation interval `T_hat ± 1.96 SE` for the main contrasts, labelled as public-bootstrap sampling uncertainty. The guide’s illustrative 95% multiplier is rounded to 2.0; the analysis uses the more precise normal multiplier consistently. The original guide §10.2 explicitly permits percentile intervals from the public bootstrap replicates. As a fixed pointwise sensitivity, compute the 2.5th and 97.5th percentiles for all four primary Y proportions and all four secondary D proportions using `np.quantile(replicate_estimates, [0.025, 0.975], method="linear")`. State that interpolation convention. This eight-proportion sensitivity is not triggered by a boundary, sign or p-value and does not replace the primary normal contrast intervals. Inspect interval adequacy near zero or one and apply the same source-quality rules to both methods. A degenerate all-zero/all-one sample and bootstrap is not proof of a known population probability. Do not silently clip an interval and pretend coverage is unchanged.

The core four groups have 7,993 Men+ nonusers, 2,224 Men+ users, 8,080 Women+ nonusers and 2,241 Women+ users. These are respondents, not weighted population totals or effective independent sample sizes. The bootstrap reflects the producer’s public variance approximation. It does not remove recall error, reverse selection, task differences, donor-imputation uncertainty or public-file disclosure treatment. Do not claim equality with confidential master-data variance.

Precision is an output, not a success criterion. Present interval-compatible contrasts in natural percentage points. No p-value threshold determines whether the study is written, whether a contrast is shown or which sex is highlighted. Failure to reject zero does not establish no association, practical equivalence or an effect smaller than a minimum detectable effect. No MDE is an upper bound on a realised or causal effect. A wide interval should change the specificity of the conclusion, not cause a search for a different endpoint.

The source benchmark and independent validation are already available. Whole-file use is 22.1%, with interval [21.4%, 22.9%], matching the published master-file table to rounding. This benchmark uses all 23,314 records, including self-employed people; it must not be relabelled an employee use rate. The independent reviewer reconstructed the full one-to-one weight join, this benchmark and both E08 raw interactions without calling the author’s estimator, within numerical tolerance. Reuse that record. The new implementation needs a regression test against it; independent review should focus next on the adjusted/common-support estimators and new same-support diagnostic rather than redundantly rediscovering the source margin.

## 5. Publication quality, small cells and safe outputs

Apply the CSWC guide §9.5, not a generic coefficient-of-variation rule borrowed from another survey. Its national-and-below categorical rules classify contributing sample sizes of at least 150 as A, 75–149 as E (warning), and below 75 as F (unacceptable quality); under five contributing respondents is expressly unacceptable. The guide discourages releasing unacceptable estimates and requires warnings for marginal/unacceptable releases. These are source quality rules, not arbitrary significance or study-eligibility thresholds and not a mathematical privacy guarantee.

For this study, do not publish F-quality cell estimates. E-quality estimates, if substantively necessary, must carry the source warning and uncertainty. Record the denominator/domain count and outcome count separately, and have the reviewer confirm the rule’s application to each table. In particular, a large denominator does not make a very rare numerator’s normal interval reliable. Do not publish fine occupation/sector/education cell estimates merely because they were used internally for standardization; pilot internal group-cell minima are three for occupation/sector and one after education. Publish pooled target estimates and support-loss summaries, with an explicit sparse-component caveat, rather than identifiable or unstable component tables. Aggregation or omission must follow the frozen release rule and never the estimated sign.

Compute from unrounded components. Follow the guide §9.1 in public outputs: weighted counts to the nearest hundred; percentages, rates and percentage-point differences to one decimal; totals from unrounded components, not sums of displayed rounded numbers. Retain full precision only in the internal verification layer. Published chart data and downloadable tables receive the same quality flags and rounding; suppression must not be defeated by complementary tables or exports. Do not expose bootstrap-weight files, respondent-level fitted values, small-cell raw records or joins. Public PUMF availability does not authorize redistributing our raw extracts.

Use the existing source hashes and retrieval receipts, preserve the analytical/weight/key integrity checks, and cite Statistics Canada with its required acknowledgement/use terms. Review source release conditions against the exact pinned guide before the first public artifact. The current internal diagnostic JSON contains precision and fine support intended for review, so it is not automatically a publication-ready data download.

## 6. Contribution and answer-to-action branches

The official [Statistics Canada analysis by Hahmann and Lovei](https://www150.statcan.gc.ca/n1/pub/75-006-x/2026001/article/00007-eng.htm) already describes GenAI adoption, occupation/gender differences and the perceived pace of technological change. We do not claim to discover a Canadian gender adoption gap. The additional question joins reported workplace use to unpaid personal-time job work and examines explicitly different composition targets.

[Jiang, Park, Xiao and Zhang’s *AI and the Extended Workday*](https://faculty.marshall.usc.edu/Gerard-Hoberg/CETAFE/papers/paper7.pdf) already studies occupational AI exposure and work/leisure time, including gender and spouse hours. The August 2025 full draft was read. A newer February 2026 SSRN revision was located and its abstract read, but its full text was inaccessible through the attempted public routes. Therefore, claim a distinct measure and setting, not first-ever research on AI and longer workdays or absence of every possible overlapping appendix. Before fixing the final novelty paragraph, make one documented public-source update of this and closely adjacent work. If the latest text remains unavailable, preserve that limit; no paid access, account creation or contact is assumed.

The useful contrast is between participation and work burden, not whether AI is inherently good or bad. The manuscript should spell out what different findings change:

- **Use coexists with more frequent unpaid work in one or both groups:** workplace evaluations should measure unpaid work as an outcome and inspect whether their recruitment covers the job types carrying that burden. This does not justify saying AI caused intensification or that banning use would reduce it.
- **Use coexists with less frequent unpaid work:** time relief remains a plausible hypothesis for a longitudinal or randomized evaluation. Selection into jobs/use prevents treating the difference as a benefit delivered by AI.
- **Gender interactions are small with suitably narrow intervals:** future recruitment need not presume different associations for Men+ and Women+ at the stated target. Any practical-equivalence claim needs a separately justified margin; none is authorized retrospectively here.
- **Interactions remain wide or differ across declared composition targets:** report the unresolved gender distinction and explain which population/model changes matter. Prefer evaluating gender and job composition jointly in future work over choosing a single gender-priority headline.
- **Unpaid-work and time-off patterns differ:** preserve both observations. They may describe different dimensions of work organisation, so subsequent evaluations should not treat a single flexibility question as a substitute for unpaid-work measurement.

No branch licenses a training, scheduling or AI-rollout policy effect estimate. The paper can improve an evaluation’s measurement and competing hypotheses; it cannot choose the effective intervention from this cross-section.

## 7. Figures, tables and manuscript arc

Produce all charts from the same approved aggregate files used by the manuscript and downloads.

1. **Four group rates:** a dot-and-interval figure for frequent unpaid job work, grouped by Men+/Women+ and user/nonuser status, with the eligible population, recall qualification and respondent counts stated. Show within-gender differences without turning them into causal arrows.
2. **Full frequency profile:** four ordered 100% stacked bars for the five `WTQ_45` categories, plus a pointwise interval table. This reveals information lost by the frequent/not-frequent split. Do not treat unequal category steps as hours.
3. **Composition sensitivity:** an interval plot in frozen order for raw, additive projection, occupation/sector standardization and occupation/sector/education standardization. Label different estimands and populations directly; display retained weight and the new same-support raw diagnostic. The unsupported age-saturated version belongs in a clearly labelled support table, not as a valid comparable interval.
4. **Secondary flexibility:** a compact figure or supplement for difficulty taking personal/family time, using the same four-group layout and separate outcome label.

The main text should first define the population and the distinction between use and unpaid job work. It should then present the four group profiles and full frequency pattern, show what changes under the declared composition comparisons, and conclude with what these measurements add to workplace evaluation. The secondary time-off outcome follows as a separate dimension. The Methodology explains sample construction, timing, weights, bootstrap, adjustment targets, quality rules and prior inspection. The discussion compares the exact measures with Statistics Canada and Jiang et al., considers selection and unobserved tasks, and closes on bounded answer-to-action implications.

Write final finding/chart headings only after verified tables are locked, as complete statements naming the outcome and comparison. Do not precommit the headline to “AI saves time,” “AI intensifies work” or a gender ordering. Keep technical audit logs and task status outside the public reader’s path, while retaining consequential limitations beside the claims they govern. Emily’s wording and paragraph structure remain the manuscript master once she supplies or edits prose.

## 8. End-to-end execution and review handoffs

| Stage | Work and proposed outputs | Completion criterion / reviewer duty |
|---|---|---|
| 1. Freeze the selected design | `protocol.md`, `prior-inspection.md`, `deviations.csv`, exact field/estimand table and output specification | Coordinator incorporates this contribution and a methods reader checks timing, targets, binary threshold and adjustment hierarchy before new primary runs. Record that substantial pilot results were already seen; no further study-selection approval is requested. |
| 2. Reuse source and sample validation | Source manifest, schema checks and sample-flow aggregate | Analyst verifies pinned analytical and bootstrap files, unique complete join, value domains and the 20,538-employee sample. Reuse existing source benchmark and independent raw-contrast record. Any discrepancy is resolved and logged before estimates are refreshed. |
| 3. Execute the frozen analysis once | Runnable study code; internal four-group ratios, full distributions, raw/adjusted/standardized contrasts, covariance, support and replicate diagnostics | All 1,000 replicates are used correctly; outputs have explicit target identifiers. Failed fine-target diagnostics remain visible. The new same-support raw comparison is clearly labelled as prospective from this plan. |
| 4. Independent numerical review | Separate reviewer script and a concise resolved-objection log | A reviewer who did not implement the estimator reconstructs at least the primary contrast and one full adjustment path, checks every common-support target and replicate target-mix recomputation, verifies full-rank models and denominator failures, and distinguishes model/population changes from mathematical errors. Existing independently matched raw results are baselines, not a reason to re-run all prior work. |
| 5. Literature and claim lock | Updated primary-source reading log, novelty paragraph, claim-to-table/source map and release-quality table | Reviewer checks the accessible latest Jiang version or records its limit, the exact official StatCan overlap, the 4.9% full-sample qualifier, Men+/Women+ wording and noncausal interpretation. Final tables satisfy quality/rounding rules. A new overlap may narrow the claim; it does not trigger a fresh ranking. |
| 6. Draft and figures | Manuscript draft, Methods appendix, four planned figure assets and safe rounded downloads from one data layer | Writer separates findings from explanations, reports every frozen target regardless of sign, and uses no mechanism or policy effect absent from the design. Coordinator checks prose/figure/table consistency and gives Emily the draft. |
| 7. Author revision and release preparation | Versioned author edits, reproduction instructions, AI-assistance disclosure, final claim checks and publication package | Preserve Emily’s master. A new draft-review agent is commissioned only after Emily has seen the draft, following team SETUP. Scope technical review to changed material. Publication, public deployment and additional spending require the appropriate later instruction; none is performed by this planning contribution. |

A substantive issue is escalated when it changes the estimand, reveals a denominator/coding error, invalidates a declared uncertainty calculation, changes source terms or establishes material novelty overlap. Ordinary contrary or imprecise findings are not failure conditions. The analyst should complete unaffected outputs while the coordinator resolves the affected claim, preserving old and corrected versions.

## 9. Existing evidence to carry forward

Paths below are relative to this contribution and point to preserved work rather than new analysis claims.

- [Final integrated E08 assessment](../stabilisation-2026-10-07/assessment.json), candidate E08, and [households scientific review](../stabilisation-2026-10-07/reviews/households-challenge.md).
- [Raw ratios, full distributions and common-support code](../stabilisation-2026-10-07/strands/work-households/analyse.py) and [Canada safe internal diagnostics](../stabilisation-2026-10-07/strands/work-households/canada-diagnostics.json).
- [Exact additive bootstrap refits](../stabilisation-2026-10-07/strands/work-households/canada_models.py) and [adjusted results](../stabilisation-2026-10-07/strands/work-households/canada-adjusted.json).
- [Independent reconstruction code](../stabilisation-2026-10-07/reviews/check_households_independent.py) and [independent results](../stabilisation-2026-10-07/reviews/households-independent-results.json).
- [Source hashes](../stabilisation-2026-10-07/strands/work-households/data-source-pins.json), [search/reading log](../stabilisation-2026-10-07/strands/work-households/search-reading-log.json), and [existing consistency verification](../stabilisation-2026-10-07/strands/work-households/verification.json).
- [Statistics Canada PUMF publication](https://www150.statcan.gc.ca/n1/pub/14-25-0001/142500012026001-eng.htm). Its pinned local guide supplies §5.5 reference-period alignment, §6.4 imputation, §6.8/§9.4 generalized public bootstrap, §9.1 rounding, §9.5 quality rules and §10.1 full-estimate-centred MSE. The categorical release table on printed page 43 was visually checked during preparation of this plan.

Raw sources remain in the existing external cache, `/private/tmp/gender-longlist-households-20261007/canada/PUMF/`, with no copy in the selected-studies package. Native review is not external human peer review. External spend for this contribution: $0.
