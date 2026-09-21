# Research brief

## Where is the gender gap in generative AI use widest, and how much of that is measurement?
### Evidence across European countries, age groups and use contexts

**Author:** Emily Birch
**Version:** 1.1 — 21 September 2026 (v1.0 reviewed in `BRIEF_REVIEW.md`; changes are marked ▲)
**Stage:** Research design following a completed data-feasibility audit; pre-registration next
**Intended output:** An empirical research post with a methods appendix and a reproducible analysis repository

This brief supersedes the scope of Piece 1 in the earlier series audit. Reasons for non-use and explanations of adoption are excluded from this study. No substantive results are claimed; the figures marked ⟨inspected⟩ in §12 were seen during the audit and this review and are declared.

## 0. Why this matters ▲

This post opens a series on one question: how gender differences in AI exposure, adoption and workplace conditions translate into differences in economic opportunity. Participation is the first link in that chain. Whatever the returns to using AI turn out to be, a group that uses it less collects less of them, and the returns are already being priced: employers report paying a premium for demonstrable AI skills, and the exposure and productivity measures that Anthropic and others publish are sex-blind by construction. Nobody can yet measure the returns by sex in Europe. Everybody can measure participation, and nobody has done it properly below the EU average.

Two readers need the answer in different forms.

1. **A person asking whether AI is arriving unequally in women's lives and work.** For them the question is where the gap is, and where it is not. A gap concentrated in work use among 25-to-54-year-olds is a labour-market gap, and the opportunity story follows directly. A gap that is absent at 16 to 24 and appears from 25 is a life-cycle or workplace pattern, not a cohort difference that will age out. A gap in private use only is a consumption gap. A reversed gap in education use is a schooling channel running the other way. These are different stories and the same headline number hides them.
2. **An analyst choosing a number to put into an exposure or opportunity model.** For them the question is whether "the gender gap in AI use" is a single stable quantity. If country rankings change when a common age structure is applied, when the denominator changes from all adults to internet users, or when the measure changes from points to ratios, then the published gap is not a parameter and a model that treats it as one is wrong in a knowable direction.

Both are answered by the same design: measure the gap in every cell the data allow, then test how much of the map survives composition and measurement.

## 1. Research purpose

Establish where gender disparities in recent generative AI use are most pronounced across European countries, age groups, education levels and purposes, and whether the answer changes with population composition and measurement choices.

The project treats "the gender gap" as a set of measurable comparisons rather than a single universal quantity. A country can have high uptake alongside a large disparity; a small percentage-point gap can coexist with a substantial proportional difference; differences in work-related use need not resemble differences in private or educational use.

The European scope is a methodological choice. Harmonised Eurostat data offer a more defensible comparison than a worldwide ranking assembled from surveys with different dates, populations, tools and questions. Harmonisation improves comparability; it does not eliminate differences in national sampling, fieldwork or interpretation.

The study measures participation, not whether greater use improves productivity, wellbeing or opportunity.

## 2. What is already known, and the gap ▲

- **Eurostat's own release and article** (December 2025) report generative AI use in the previous three months by 33% of EU residents aged 16 to 74, with men at 35% and women at 30%. Gender is published at the EU aggregate only; the article gives no gender breakdown by country, age or purpose. The table behind it carries all of those cells.
- **Henseke (2026), From Exposure to Adoption**, EWCS 2024, 35 European countries: among workers, men are 4.1 points more likely to use generative AI at work (13.8% against 9.7%), the gap is positive in most countries and concentrated in the most exposed occupations. A workplace population and a work-only measure; no household population, no age bands, no purposes.
- **Di Pietro (2026), gender disparities in AI use among European youth**, Flash Eurobarometer 2024, 27 countries: young men are more likely to have used AI applications; young women are more likely for schoolwork and research; the gap is largely due to unobserved characteristics (Fairlie decomposition). Youth only, a different survey, no country-by-gender map.
- **Otis and co-authors (Harvard Business School working paper)**, meta-analysis across 143,000 people worldwide: a gap of about 25% of the male rate, persisting over time. Global, pooled across instruments.
- **Pew (June 2026), US adults**: ever-use has converged (50% of men, 47% of women) while daily use (27% against 20%) and work use among the employed (40% against 35%) have not. A single country, an ever-use measure.
- **Stephany and Duszynski (2026), UK**: women's uptake tracks perceived societal risk more than men's. An explanation, out of this post's scope.

The gap this post fills: no publication reports the 2025 harmonised European gender gap by country, by age band or by purpose, and none tests whether those comparisons survive age standardisation, a change of denominator or a change of measure. The contribution is the map and the sensitivity of the map, together.

## 3. Provisional abstract, design not results

Gender differences in generative AI use are often summarised as a single adoption gap, obscuring variation across countries, population groups and purposes. This study uses harmonised 2025 Eurostat statistics to examine recent generative AI use among people aged 16 to 74 across European countries. It compares male and female use rates overall, within age and education groups, and for private, professional and formal-education purposes; reports percentage-point differences alongside relative-use ratios; distinguishes population participation from purposes of use among existing users; and, where age-specific coverage permits, applies direct age standardisation to test the sensitivity of cross-country comparisons to age structure. Published reliability flags, missing cells and the absence of cell-level sampling uncertainty are documented, and an approximate sampling bound is derived from published national sample sizes and labelled as such. Country orderings are reported as classes that persist across measures rather than as ranks. The study identifies which patterns are robust to defensible measurement choices and where the evidence cannot distinguish apparent differences, without attributing them to mechanisms or estimating the benefits of adoption. The final abstract will be rewritten around the results, including small, mixed or reversed differences.

## 4. Questions, hypotheses and decision rules ▲

### RQ1: where are observed disparities largest, smallest or reversed?

1. How do male and female recent-use rates differ across countries?
2. How does the gap vary across six non-overlapping age bands?
3. How does it vary across low, medium and high educational attainment?
4. Does the pattern differ for private, professional and formal-education use?

### RQ2: which comparisons depend on composition or measurement?

1. Do country comparisons change after applying a common age distribution to both sexes?
2. Do absolute and relative measures identify the same disparities?
3. How do purpose-specific comparisons change when the denominator is all individuals rather than existing AI users, and all individuals rather than internet users?
4. Are conclusions sensitive to reliability exclusions, common-country coverage and restricting the sample to the EU27?

RQ2 tests the stability and interpretation of RQ1. It is not a causal explanation of adoption. Joint adjustment for age, education and employment is outside the available data.

### Hypotheses, each with the pattern that would count against it ▲

The EU-aggregate values of each quantity have been seen (§12) and are excluded from the tests; the hypotheses are judged on the country-level and purpose-by-age results, which have not.

- **H-work: the gap is larger in work use than in private use, in most countries.** *Against it:* the private-use gap exceeds the work-use gap in more than half of the countries with unflagged cells for both, on the all-individual denominator.
- **H-age: the gap is smallest, or reversed, at 16 to 24 and largest between 25 and 44, in most countries.** *Against it:* the 16-to-24 gap is the largest band in a majority of countries with complete age cells, or the 25-to-44 bands are not the largest in a majority.
- **H-education: the gap widens with educational attainment.** *Against it:* the high-education gap is not the largest of the three in a majority of countries with unflagged cells.
- **H-composition: applying a common age structure changes the class of few countries.** *Against it:* more than a third of countries change class (rule below) between the crude and standardised gap.

"Most" and "majority" are counts over countries, reported as counts with the number of countries in the comparison, never as shares of a base under thirty.

### Decision rule for "largest", "smallest" and "reversed" ▲

No cell-level standard errors are published, so a ranking is not a finding. A country is classed as **large-gap** only if it sits in the top tercile of the signed percentage-point gap, in the top tercile of the male-to-female ratio, and in the top tercile after age standardisation, all on unflagged cells; **small-gap** by the same rule at the bottom; **reversed** only if the female rate exceeds the male rate on the all-individual denominator and on the internet-user denominator; every other country is **not distinguishable**. The number of countries that change class between any two measures is RQ2's headline quantity. Ties within presentation rounding are reported as bands.

## 5. Scope and exclusions

**Primary geographic sample:** EU27, with the official EU aggregate as a reference.
**Geographic extension:** the other country and territory codes in the audited extract, labelled and analysed separately; the extract does not cover every European country.
**Population:** individuals aged 16 to 74 within the survey's household population; optional 75-to-89 groups excluded.
**Reference period:** generative AI use in the three months preceding the survey interview; fieldwork is by convention in the first quarter of 2025, so the window is roughly December 2024 to March 2025 for most countries, and this is not a common calendar quarter. ▲
**Technology:** generative AI tools as the questionnaire defines them; not all AI, all automation or one provider.
**Design:** descriptive secondary analysis of published survey estimates, pre-registered.

Excluded: reasons for non-use (the next post), first-use motivations, trust, confidence, causal mechanisms, occupational exposure, productivity, earnings and welfare. No Anthropic, OpenAI, Pew or Spanish microdata is required for the core analysis; one OpenAI aggregate file is used only as a triangulation leg (§9). Literature may contextualise implications without adding another empirical question.

"Gender gap" is the research framing; the source supplies male and female statistical categories, which do not capture the full range of gender identities. The source's categories are retained.

## 6. Data and variables

### Core dataset

**Eurostat `isoc_ai_iaiu`: Individuals — use of generative AI tools.** Eurostat table; official EIGE mirror and metadata; model questionnaire (B1, B5 to B6). The audit downloaded the EIGE full extract because Eurostat's API returned a service-unavailable page; mirror updated 20 July 2026, extracted 21 September 2026. Before analysis, check for a newer official revision; retain both versions and document any change.

The audited file contains 37,885 rows and seven columns (`Time`, `geo`, `Value`, `indic_is`, `ind_type`, `unit`, `Flags`), covers 2025 only (the questions were first asked in 2025, so no earlier wave exists ▲), 35 countries and territories plus the EU aggregate, and 104 population-group codes. These are published cells, not respondents.

| Concept | Source code | Interpretation |
|---|---|---|
| Any recent use | `I_IUAI` | Used generative AI during the preceding three months |
| Private use | `I_IUAIPR` | For private purposes |
| Work use | `I_IUAIWP` | For professional purposes |
| Education use | `I_IUAIFE` | For formal education |
| Population denominator | `PC_IND` | Percentage of individuals in the group |
| Internet-user denominator | `PC_IND_IU3` | Percentage of recent internet users in the group |
| AI-user denominator | `PC_IND_IUAI` | Percentage of recent AI users in the group |
| Overall comparison | `F_Y16_74`, `M_Y16_74` | Female and male individuals aged 16 to 74 |
| Education groups | `F_`/`M_` + `I0_2`, `I3_4`, `I5_8` | Low, medium, high education, source labels |

Primary age bands: 16–24, 25–34, 35–44, 45–54, 55–64, 65–74, coded `F_Y…` and `M_Y…`. Overlapping groups (16–29, 25–54) are not combined with these bands.

**Sex crosses that exist:** sex by age, sex by education. **Sex crosses that do not exist** ▲: employment status, occupation (ISCO), income and urbanisation carry no sex prefix in the extract, so no gender comparison is possible within the employed, within occupations or within any of those groups. "Work use among all adults" is therefore the only work measure, and it is not work use among the employed.

Purpose responses are multi-select and do not sum to overall use. The AI module is routed through recent internet use, which is why the all-individual and internet-user denominators differ, and why their difference is itself informative (§8). The primary outcome is the published all-individual percentage.

### Age weights ▲

Secured: Eurostat `demo_pjan` (population on 1 January by single age and sex) is served by the Eurostat API for EU27_2020, 2025, with status flag `ep` (estimated, provisional). The common distribution is the sex-pooled EU27 population aged 16 to 74 in the six bands, weights summing to one, applied to every country and both sexes. The survey's household population differs from the resident population; the difference is disclosed, not corrected. If the provisional file is revised before publication, both versions are kept and the change logged.

### Approximate sampling bound ▲

Eurostat's metadata states that about 330,000 individuals aged 16 to 74 were surveyed in the EU in 2025 and that national sample characteristics are in national metadata files. Those national sample sizes will be fetched and recorded. With a national sample by sex and a simple-random-sampling assumption, a binomial standard error is a lower bound on the true one, since design effects only widen it. It is published as a bound with the assumption named, never as a survey interval. Order of magnitude for the reader to judge: 2,000 respondents per sex at a 33% rate gives about 1.1 points on each rate and 1.5 on the gap, so gaps below about 3 points are inside noise; 350 respondents per sex in an age band gives a gap standard error near 4 points, so most country-by-age gaps are. If national sample sizes cannot be obtained, the analysis is descriptive with flags only, and the main text says so.

## 7. Quantities to estimate

Let `p_M` and `p_F` be the published male and female percentages for the same country, group, outcome and denominator.

**Primary:** `gap_pp = p_M − p_F`; positive means higher male use. The sign is preserved in every plot and table.
**Magnitude:** `|gap_pp|`, for "where widest".
**Secondary:** `ratio = p_F / p_M`; one is equality; undefined when `p_M` is zero, marked missing; ratios with small denominators do not drive classes.
**Age-standardised rate:** `Σ_a w_a p_{s,a}` for sex `s` with common weights `w_a`; the standardised gap is the male minus the female standardised rate, compared with the crude gap on the same complete-country sample. The change is reported in points, never as a "percentage explained".
**Purpose comparisons:** population participation (all individuals) is primary; purpose among users (AI users) is secondary and conditional on a selected group.
**Internet-composition share** ▲: the difference between the all-individual gap and the internet-user gap, by age band, as the part of the AI gap that is an internet-use gap.

## 8. Analysis sequence

**A. Freeze and validate.** Record source version and checksum; retain flags; validate unique keys and ranges; produce a coverage table before any ranking; reproduce the official EU headline (33%; 35% men, 30% women) as an ingestion check; confirm allowed indicator-by-denominator combinations.

**B. Country comparisons.** Female and male rates together with signed gaps; EU27 first, extension second; classes by the §4 rule, not ranks; ties as bands.

**C. Age and education.** EU profiles first, then country variation; a country-by-age heatmap with missing cells visibly distinct from zero; education reported crude, with the statement that age standardisation within education is impossible because no sex-by-age-by-education cells exist ▲.

**D. Purposes.** Participation on the all-individual denominator; then among users; no subtraction of overlapping purposes; enrolment composition named, not adjusted.

**E. Age standardisation.** Where all twelve sex-by-age cells are unflagged (33 of 36 geographies ⟨inspected⟩; Ireland, North Macedonia and Serbia are incomplete); no imputation, no renormalisation over surviving bands; purpose-specific standardisation only as an appendix if coverage allows.

**F. Internet composition** ▲. The all-individual and internet-user gaps by age band, and their difference, as a named sensitivity with an interpretation.

**G. Triangulation** ▲ (§9): the country ordering against OpenAI's feminine share of messages by country (26 of the EU27 in June 2025), and the work-use gaps against Henseke's EWCS work-adoption gaps; agreement measured by rank correlation and by class agreement, reported either way.

**H. Sensitivity and synthesis.** Points against ratios; crude against standardised; EU27 against the wider sample; unflagged against a flagged-cell appendix; common geography for cross-purpose comparisons; the count of class changes. The preferred measure was fixed here, before results.

## 9. Triangulation legs ▲

Two independent sources measure a related quantity with a different construct, which is why agreement or disagreement is informative rather than circular.

- **OpenAI Signals, feminine share of ChatGPT messages by country and month** (public, name-inferred gender, consumer accounts, messages not people). Coverage: all EU27, 26 with June 2025. Used for one question only: does the ordering of EU countries by the Eurostat gap agree with the ordering by feminine message share? Reported as a rank correlation with its country count, and as class agreement.
- **Henseke (2026), work-adoption gap by country** among workers, EWCS 2024. Used for one question only: does the ordering of the Eurostat work-use gap agree with it?

Neither enters a headline, a class, or a hypothesis test.

## 10. Reliability, missingness and uncertainty

Paired unflagged overall male and female estimates exist for all 36 geographies; finer groups lose coverage. Across the full extract 3,196 values are missing and 6,699 rows carry the low-reliability flag `u`, overlapping sets. Main analyses require both cells non-missing and unflagged. New flags in a refreshed extract are inspected before inclusion. Missing is not zero. All exclusions are logged machine-readably.

No cell-level standard errors, counts or design variables are published. Therefore: no invented confidence intervals; no bootstrap of published cells presented as sampling uncertainty; no "statistically absent" or "significantly different"; age standardisation does not reduce sampling error. The approximate bound of §6 is the only uncertainty statement, labelled as a bound.

Cross-country correlations with income, equality indices or digitalisation are outside scope.

## 11. Assumptions sweep ▲

- **Value judgement.** A gap is a difference in participation, not a deficit; differing purposes need not reflect deficits; the post explains and does not rank countries as better or worse.
- **Construct.** "Use" is any use in three months as the respondent understood generative AI; not intensity, skill or benefit. Pew's convergence in ever-use alongside persisting gaps in daily use is the reminder that participation is the weakest of the measures.
- **Composition.** Age (standardised), internet use (the internet-composition share), education (stratified, not standardised); employment and occupation cannot be held fixed and are named as the composition this design cannot remove.
- **Results in the literature that cut against the framing.** Di Pietro's reversed gap for schoolwork and Eurostat's near-zero education-purpose gap at EU level say the gap is not one-signed; Henseke's concentration in exposed occupations says the work gap may be an occupation-mix gap, which this design cannot test.

## 12. Declared inspections ▲

Seen during the audit and the review, and excluded from hypothesis tests: the EU purpose gaps on the all-individual denominator (private 5.5, work 3.0, education 0.05 points; overall 4.5); the EU education-purpose share among users (30.5% female, 26.8% male); the EU age profile of the overall gap (−1.7 at 16–24, then 4.7, 4.8, 2.8, 4.2, 4.1 points); the EU education profile (3.8, 4.6, 7.0 points); the distribution of the overall country gap (median 4.0 points, range −3.8 to +9.3, six of 36 geographies reversed: North Macedonia, Malta, Estonia, Slovenia, Lithuania, Croatia); and age-cell completeness (33 of 36). Not seen: any country-by-age, country-by-education or country-by-purpose gap, any ratio, any standardised value, either triangulation leg.

## 13. Contribution per outcome ▲

- **If the hypotheses hold and composition changes few classes:** the first harmonised map of the European gender gap by country, age and purpose, with a demonstration that it is a stable quantity at the country level, and a named set of countries where it is absent or reversed.
- **If the hypotheses fail:** the map still stands, and the finding is that the gap is not where the literature expects (in work, in mid-life, at high education), which redirects the series' next question.
- **If most comparisons are not distinguishable:** the finding is that a country ranking of the gender gap in AI use cannot be supported from published cells at this precision, and the post says what Eurostat would need to publish (cell counts or standard errors) for it to be. That is a measurement contribution, and it is the outcome the sampling bound makes likely for the age-band comparisons.

## 14. What the close will say, per outcome ▲

- **Holds:** the gap in AI use across Europe is concentrated in work and in mid-life, is smallest or reversed among the young, and survives age structure; the next post asks what non-users say.
- **Fails:** the gap is real at the EU level and unstable below it; where it sits depends on which purpose and which age band is asked about, and no single number should be carried into an opportunity model.
- **Not distinguishable:** the European gender gap in AI use is one number at the EU level and a cloud below it; the honest map has classes, not ranks, and the sampling bound says why.

In every outcome the close carries no number the body has not carried, states the internet-composition result, and names the returns question this series will reach.

## 15. Planned figures and tables

| Output | Purpose |
|---|---|
| Figure 1: country rates and signed gaps, with classes | Uptake and disparity together; classes, not ranks |
| Figure 2: country-by-age gaps with the EU profile | Heterogeneity with missing cells visible |
| Figure 3: purpose-specific rates and gaps, population against users | Denominator sensitivity made visible |
| Figure 4: crude against age-standardised gaps, with class changes counted | Stability of country comparisons |
| Figure 5 ▲: all-individual against internet-user gaps by age | The internet-composition share |
| Table 1: definitions, populations, coverage | Auditable scope |
| Table 2: education-specific comparisons | Education as a substantive dimension |
| Table 3 ▲: triangulation | Rank and class agreement with the two external orderings |
| Appendix: full estimates, ratios, flags, exclusions, common-sample results, weights, sampling bound | Reproducibility |

Each figure states year, age range, denominator, direction of the gap and reliability treatment. Missing estimates are visually distinct from zero. No artificial confidence bars; the bound, where shown, is labelled as a bound.

## 16. Interpretation and claim boundaries

Permissible: "the observed gap is larger in this use context"; "country comparisons change under a common age distribution"; "absolute and proportional measures give different orderings"; "this country's class does not change under any measure".

Not supported: "women are less confident"; "training would close the gap"; "this country is significantly the worst"; "equal uptake implies equal benefits"; "education causes the difference"; "AI is widening the wage gap"; any rank of adjacent countries.

## 17. Transparency and implementation

This is a dated analysis plan after exploratory data inspection, with the inspections declared in §12; the pre-registration that follows is committed before any country-level, purpose-by-age, ratio or standardised value is computed. New analyses prompted by results are labelled exploratory.

Implementation in Python, in the team's structure: a `posts/gender1/` folder (or a new repository) with `BRIEF.md` (this document), `prereg/prereg.md`, numbered scripts with check blocks, `data/processed/results.json`, figures with captions, a lab notebook, a claims list written after verification, and the page built and verified with `site/tools/`. Checks: sign conventions, unique keys, purpose rates bounded by overall rates within rounding, denominator consistency, weights summing to one, complete age-band coverage before standardisation, and the EU headline reproduced.

Required resources: the secured Eurostat/EIGE extract and questionnaire; the `demo_pjan` file; national sample sizes from national metadata; the OpenAI Signals bundle (already held); Henseke's country table; Python data and plotting libraries; a referee review of the pre-registration and of the draft. No paid data, recruitment, model calls or new survey collection.

Deliverables: the post; methods and limitations appendix; source and variable dictionary; archived data version or retrieval instructions; executable scripts and environment lock; generated tables and figures; the decision log; an assistance disclosure.

## 18. Milestones and completion criteria

| Milestone | Output | Completion criterion |
|---|---|---|
| Data and literature lock | Versioned extract, coverage matrix, source register, national sample sizes, age weights | Definitions, close-study overlap and the sampling bound documented |
| Pre-registration | `prereg/prereg.md` committed | Hypotheses, classes rule and sequence fixed; referee review passed |
| Descriptive analysis | Country, age, education, purpose tables | EU headline reproduces; exclusions explicit |
| Robustness | Ratios, denominators, standardisation, internet composition, triangulation | Compatible samples; class changes counted |
| Writing | Post and appendix | Every headline traceable to a generated output; claims list respected |
| Review and release | Rebuilt package and revised text | Arithmetic, interpretation and reproducibility checks pass |

The study is complete when it answers the two research questions within these limits, including the outcome in which no country ranking survives.

## Audit provenance

See `AUDIT_AND_SERIES.md`, `outputs/source_profiles.json`, `outputs/eurostat_subgroup_coverage.csv`, `outputs/isoc_ai_iaiu_gender_pairs.csv`, and `BRIEF_REVIEW.md` for the review that produced this version.
