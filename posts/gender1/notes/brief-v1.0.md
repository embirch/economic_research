# Research brief

## Where is the gender gap in generative AI use widest?
### Evidence across European countries, age groups, and use contexts

**Author:** Emily Birch  
**Version:** 1.0 — 21 September 2026  
**Stage:** Research design following a completed data-feasibility audit  
**Intended output:** An empirical research blog with a paper-style methods appendix and reproducible analysis repository

This brief supersedes the scope of Piece 1 in the earlier series audit. Reasons for non-use and explanations of adoption are excluded from this study. No substantive results are being claimed in the proposed abstract below.

## 1. Research purpose

Establish where gender disparities in recent generative AI use are most pronounced, and whether the answer changes across population groups, purposes and measurement choices.

The project treats “the gender gap” as a set of measurable comparisons rather than a single universal quantity. A country can have high uptake alongside a large disparity; a small percentage-point gap can coexist with a substantial proportional difference. Differences in work-related use need not resemble differences in personal or educational use.

The European scope is a methodological choice. Harmonised Eurostat data offer a more defensible comparison than a worldwide ranking assembled from surveys with different dates, populations, tools and questions. Harmonisation improves comparability; it does not eliminate differences in national sampling, fieldwork or interpretation.

The societal and economic motivation is unequal participation in an increasingly relevant technology. The study measures participation, not whether greater use improves productivity, wellbeing or opportunity.

## 2. Provisional abstract — design, not results

Gender differences in generative AI use are often summarised as a single adoption gap, potentially obscuring variation across countries, population groups and purposes. This study will use harmonised 2025 Eurostat statistics to examine recent generative AI use among people aged 16–74 across European countries. It will compare male and female use rates overall, within age and education groups, and for private, professional and formal-education purposes. The analysis will report percentage-point differences alongside relative-use ratios, and distinguish population participation from purposes of use among existing users. Where age-specific coverage permits, direct age standardisation will assess the sensitivity of cross-country comparisons to age structure. Published reliability flags, missing cells and the absence of cell-level sampling uncertainty will be documented explicitly. The study aims to identify which patterns are robust to defensible measurement choices and where the evidence is insufficient to distinguish apparent differences. It will provide a transparent descriptive account of disparities in AI participation, without attributing them to particular mechanisms or estimating the benefits of adoption.

The final abstract will be rewritten around the results, including small, mixed or reversed differences where observed.

## 3. Specific questions

### RQ1 — Where are observed disparities largest, smallest or reversed?

1. How do male and female recent-use rates differ across countries?
2. How does the gap vary across six non-overlapping age bands?
3. How does it vary across low, medium and high educational attainment?
4. Does the pattern differ for private, professional and formal-education use?

“Largest” will primarily mean the largest **absolute percentage-point disparity**, with its direction shown. We will also identify the largest male advantage and female advantage separately. Near-zero estimates will be described as small observed differences, not proof of equality.

### RQ2 — Which comparisons depend on composition or measurement?

1. Do country comparisons change after applying a common age distribution to both groups?
2. Do absolute and relative measures identify the same disparities?
3. How do purpose-specific comparisons change when the denominator is all individuals versus existing AI users?
4. Are conclusions sensitive to reliability exclusions, common-country coverage and restricting the sample to the EU27?

RQ2 tests the stability and interpretation of RQ1. It is not a causal explanation of adoption. Education is a stratification dimension; joint adjustment for age, education and employment is outside the available data and outside the main design.

## 4. Scope and exclusions

**Primary geographic sample:** EU27, using the official EU aggregate as a reference.  
**Geographic extension:** Other country/territory codes in the audited Eurostat extract, clearly labelled and analysed separately where helpful. Do not imply that the extract covers every European country.  
**Population:** Individuals aged 16–74 within the survey's household population. Exclude optional 75–89 groups.  
**Reference period:** Generative AI use in the three months preceding the 2025 survey. This is not a common calendar-quarter experiment.  
**Technology:** Generative AI tools as defined in the questionnaire; not all AI, all automation or one provider.  
**Design:** Descriptive secondary analysis of published survey estimates.

The study will not analyse reasons for non-use, first-use motivations, trust, confidence, causal mechanisms, occupational exposure, productivity, earnings or welfare. It will not require Anthropic, OpenAI, Pew or Spanish microdata. Relevant literature may briefly contextualise implications, without adding another empirical question.

Use “gender gap” as the research framing, but explain that the source supplies male/female statistical categories. These data do not capture the full range of gender identities; we will retain the source's category definitions rather than imply a richer measure.

## 5. Data and variables

### Core dataset

**Eurostat `isoc_ai_iaiu`: Individuals — use of generative AI tools.**

- [Eurostat table](https://ec.europa.eu/eurostat/databrowser/view/isoc_ai_iaiu/default/table?lang=en)
- [Official EIGE mirror and metadata](https://dgs-p.eige.europa.eu/data/information/ta_resdig_dig_intuse__isoc_ai_iaiu)
- [Questionnaire, especially B1 and B5–B6](https://www.cso.ie/en/media/csoie/releasespublications/documents/ep/isshinternetaccessandict/2025/Information_Society_Statistics_2025_Model_Questionnaire.pdf)

The audit downloaded the EIGE full extract because Eurostat's API returned a service-unavailable page. The mirror was updated on 20 July 2026 and extracted on 21 September 2026. Before analysis, check for a newer official revision; retain both versions and document any change.

The audited file contains 37,885 rows and seven columns: `Time`, `geo`, `Value`, `indic_is`, `ind_type`, `unit`, `Flags`. It covers 2025, 35 countries/territories plus the EU aggregate, and 104 population-group codes. These are **published cells, not 37,885 respondents**.

| Concept | Source code | Interpretation |
|---|---|---|
| Any recent use | `I_IUAI` | Used generative AI during the preceding three months |
| Private use | `I_IUAIPR` | Used it for private purposes |
| Work use | `I_IUAIWP` | Used it for professional/work purposes |
| Education use | `I_IUAIFE` | Used it for formal education |
| Population denominator | `PC_IND` | Percentage of individuals in the specified group |
| Internet-user denominator | `PC_IND_IU3` | Percentage of recent internet users in the group |
| AI-user denominator | `PC_IND_IUAI` | Percentage of recent AI users in the group |
| Overall comparison | `F_Y16_74`, `M_Y16_74` | Female/male individuals aged 16–74 |
| Education groups | `F_`/`M_` + `I0_2`, `I3_4`, `I5_8` | Low, medium, high education, following source labels |

Primary age bands: **16–24, 25–34, 35–44, 45–54, 55–64, 65–74**. Source codes use `F_Y...` and `M_Y...`. Overlapping groups such as 16–29 or 25–54 will not be combined with these bands.

Purpose responses are multi-select: their rates do not sum to overall use. “Work use among all adults” is not “work use among employed adults”; the latter denominator is not verified for gender comparisons in this extract. Likewise education use is not a rate among enrolled students.

The AI module is routed through recent internet use. This matters when comparing the all-individual and internet-user denominators. The primary outcome remains the published all-individual percentage.

### Supplementary data for age standardisation

Obtain official 2025 EU27 population counts by age to construct a single, sex-pooled EU27 age distribution for ages 16–74. Use the same six-band weights for every country and for both male and female estimates. Record the exact source, reference date, population universe and aggregation code before calculation; this supplementary file is not yet secured by the audit.

The resulting estimates describe rates under a common hypothetical age distribution. They need not reproduce national survey totals. Differences between resident-population weights and the survey's household population will be disclosed. If compatible population weights cannot be obtained, retain age-stratified results and mark standardisation unavailable; do not silently substitute equal weights.

## 6. Quantities to estimate

Let `p_M` and `p_F` be the published male and female percentages for the same country, group, outcome and denominator.

**Primary measure:** `gap_pp = p_M − p_F`. Positive means higher male use; negative means higher female use. Preserve the sign in every plot and table.

**Magnitude:** `absolute_gap_pp = |gap_pp|`, used when answering where disparities are widest.

**Secondary measure:** `female_to_male_ratio = p_F / p_M`. One denotes equal observed rates. A zero male rate makes the ratio undefined; mark it missing. Ratios with very small denominators will not drive headline rankings.

**Age-standardised rate:** `p_s_standardised = Σ_a w_a × p_s,a`, for sex category `s` and common age weights `w_a` summing to one. Compute the standardised gap as the male rate minus the female rate. Compare crude and standardised gaps on the **same complete-country sample**.

Report the change in the gap in percentage points. Do not label it a causal “percentage explained”, especially where the crude gap is close to zero or changes sign.

For purpose comparisons, analyse two distinct quantities:

- **Population participation:** percentage of all individuals who used AI for each purpose — primary.
- **Purpose among users:** percentage of AI users who used it for that purpose — secondary, conditional on a selected group.

## 7. Analysis sequence

### A. Freeze and validate the analytical extract

Record source version and checksum; retain flags; validate unique keys and valid percentage ranges; generate a coverage table before looking at rankings. Reproduce official rounded EU headline estimates as an ingestion check. Confirm the allowed combinations of indicator and denominator.

### B. Overall country comparisons

Show female and male rates together, alongside signed pp gaps. Present EU27 first and the wider covered geography as an extension. Distinguish high adoption from small disparities. Use ratios as a companion sensitivity view, not a substitute for actual rates.

Sorting can aid reading, but will not establish that adjacent countries differ statistically. Report observed extremes cautiously and preserve ties introduced by presentation rounding.

### C. Age and education

Present the official EU aggregate's age-specific and education-specific rates and gaps, followed by country variation. Use a manageable country-by-age heatmap and appendix tables. Treat education and age comparisons separately; do not manufacture jointly adjusted estimates from marginal tables.

### D. Purposes

Compare private, work and education participation using `PC_IND`. Then show how conclusions change using `PC_IND_IUAI`. Interpret the education comparison in light of enrolment composition without claiming adjustment for enrolment. Do not subtract overlapping purpose rates to infer exclusive use categories.

### E. Age standardisation

Standardise overall recent use where all six male/female age-band estimates are available and pass reliability rules. Do not impute missing bands or renormalise weights over surviving bands. Purpose-specific standardisation is an optional appendix extension only if coverage remains adequate; it is not necessary for the core paper.

### F. Sensitivity and synthesis

Compare signed pp differences with ratios, crude with standardised gaps, EU27 with the wider sample, and unflagged estimates with a clearly marked flagged-cell appendix. For cross-purpose comparisons, repeat on a common geography set. Use `PC_IND_IU3` as a secondary check of how internet participation changes interpretation.

Summarise which conclusions persist, which depend on definitions, and which cannot be resolved with these data. Do not select the preferred measure after observing which produces the strongest story.

## 8. Reliability, missingness and uncertainty

The audit found paired unflagged overall male/female estimates for all 36 geography codes. Finer groups are less complete. Across the full extract, 3,196 values are missing and 6,699 rows carry a low-reliability flag; these sets overlap. These totals are not missingness rates for the final restricted sample.

Main analyses require both comparison cells to be non-missing and unflagged. `u` means low reliability. Preserve any new flags introduced by a refreshed extract and inspect their definitions before inclusion. Missing/suppressed values are not zero. Retain all exclusions in a machine-readable log.

No cell-level standard errors, respondent counts or survey-design variables are included in the downloaded table. Therefore:

- Do not invent confidence intervals or treat percentage denominators as respondent counts.
- Do not bootstrap published cells and present the output as survey sampling uncertainty.
- Do not describe small gaps as statistically absent or adjacent ranks as meaningfully different.
- Do not treat age standardisation as reducing sampling error.

Review official metadata for usable uncertainty information during setup. If none is obtainable, publish a clearly descriptive analysis with reliability flags and measurement sensitivity. That limitation belongs in the main text as well as the appendix.

Cross-country correlations with income, equality indices or digitalisation are outside scope. They would add ecological interpretation problems without answering the agreed question more directly.

## 9. Planned figures and tables

| Output | Purpose |
|---|---|
| Figure 1: Country rates and signed gaps | Show absolute uptake and disparity together; avoid a ranking without context |
| Figure 2: Country-by-age gaps, with EU age profile | Locate heterogeneity while displaying missing cells |
| Figure 3: Purpose-specific rates/gaps, population versus users | Make denominator-sensitive conclusions visible |
| Figure 4: Crude versus age-standardised gaps | Assess the stability of country comparisons |
| Table 1: Definitions, populations and coverage | Make the empirical scope auditable |
| Table 2: Education-specific comparisons | Retain education as a substantive dimension without overloading the figures |
| Appendix tables | Full estimates, ratios, flags, exclusions, common-sample results and standardisation weights |

Each figure will state year, age range, denominator, direction of the gap and reliability treatment. Use consistent colours and scales. Missing estimates must be visually distinct from zero gaps. No artificial confidence bars.

## 10. Literature and contribution

The existence of gender differences in AI adoption is already documented. The contribution sought here is a systematic, reproducible account of **where those differences concentrate and how measurement changes the answer**. It must add analysis beyond Eurostat's existing descriptive release.

Initial references:

- [Eurostat's 2025 release](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20251216-3): establishes the official population measure and benchmark.
- [Eurostat's analytical overview](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Use_of_artificial_intelligence_by_individuals): important prior descriptive coverage; assess overlap before claiming novelty.
- [Humlum and Vestergaard, The Adoption of ChatGPT](https://www.iza.org/publications/dp/16992/the-adoption-of-chatgpt): relevant workplace-adoption literature, with a different population and tool definition.
- [Henseke, From Exposure to Adoption](https://arxiv.org/abs/2604.18849): European workplace evidence; distinguish our household-population and use-context question from occupational exposure analysis.
- [Pew's gender report](https://www.pewresearch.org/internet/2026/06/17/the-gender-gap-in-ai/): context for the distinction between ever-use and other use measures; do not pool its estimates into the European ranking.

A focused literature check should cover studies through the analysis start date, including work already using the 2025 Eurostat release. Record population, outcome, denominator and contribution for each close comparator. Do not promise to be the first without verifying it.

## 11. Interpretation and claim boundaries

Permissible: “The observed gap is larger in this use context”; “country comparisons change under a common age distribution”; “absolute and proportional measures give different orderings”.

Not supported: “women are less confident”; “training would close the gap”; “this country is significantly the worst”; “equal uptake implies equal benefits”; “education causes the difference”; “AI is widening the wage gap”.

The discussion can explain why participation disparities matter and identify hypotheses for subsequent work. It should also recognise that use is not automatically beneficial and that differing purposes need not reflect deficits. No empirical analysis of non-use reasons will be added to this paper.

## 12. Transparency and implementation

This is a **dated analysis plan after exploratory data inspection**, not an untouched preregistration. The audit has already exposed EU headline/purpose estimates and coverage. Declare those inspections and log changes to this brief. New analyses prompted by results should be labelled exploratory.

Implementation in Python:

1. Create a dedicated project folder for this piece, referencing the immutable audit snapshot.
2. Write download/version, cleaning and validation scripts; preserve original files and metadata.
3. Produce a tidy analytical table with keys, rates, flags and paired-cell eligibility.
4. Implement gap and ratio calculations; separately implement age weights and standardisation.
5. Generate figures, appendix tables and exclusions directly from code.
6. Rebuild outputs from a clean environment and review arithmetic, source definitions and claims.

Meaningful checks include sign conventions, expected unique keys, purpose rates bounded by overall rates within rounding tolerance, denominator-conversion consistency where comparable, weights summing to one, and complete age-band coverage. These checks should detect errors rather than merely repeat implementation logic.

Required resources: the secured Eurostat/EIGE extract and questionnaire; an official age-population file; Python plotting and data libraries; a reference library; methodological review before publication. No paid data, participant recruitment, model API calls or new survey collection are required for the core study.

Final deliverables: readable research blog; methods and limitations appendix; source/variable dictionary; archived data version or permitted retrieval instructions; executable scripts and environment lock; generated tables/figures; a decision log. Disclose AI assistance and retain human responsibility for analytical choices and interpretation.

## 13. Milestones and completion criteria

| Milestone | Output | Completion criterion |
|---|---|---|
| Data and literature lock | Versioned extract, coverage matrix, source register | Definitions and close-study overlap documented |
| Descriptive analysis | Country, age, education and purpose tables | Official benchmarks reproduce and exclusions are explicit |
| Robustness | Ratios, denominator checks, age standardisation where feasible | Comparisons use compatible samples and assumptions |
| Writing | Blog and appendix | Every headline is traceable to a generated output |
| Review and release preparation | Rebuilt package and revised text | Arithmetic, interpretation and reproducibility checks pass |

The study is complete when it answers the two research questions within these limits—even if no simple country ranking survives scrutiny, some gaps are small, or results differ across contexts. Additional mechanisms or datasets are not required to make the paper feel more substantial.

## Audit provenance

See [the completed audit](AUDIT_AND_SERIES.md), [source profiles](outputs/source_profiles.json), [subgroup coverage](outputs/eurostat_subgroup_coverage.csv) and [paired estimates](outputs/isoc_ai_iaiu_gender_pairs.csv). The audit's earlier inclusion of non-use reasons is superseded by this brief; its underlying files remain available for separate future research.
