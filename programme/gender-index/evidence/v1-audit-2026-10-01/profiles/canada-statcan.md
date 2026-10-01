# Source profile: Canada — two distinct Statistics Canada sources

Data steward, 1 October 2026. Proposed IDs `CA_CSWC_WORK` (sample family
`CA_CSWC_2024_2025`) and `CA_LFS_AI_2026` (sample family `CA_LFS_SUP_2026_03`).
Status: **published findings verified from the primary StatCan pages**; no data file or
table download was audited, and no microdata was requested.

These are **two different samples from one provider**. They must not be combined, chained
into a trend, or treated as independent confirmations of each other.

## 1. Canadian Survey on Working Conditions (`CA_CSWC_WORK`)

Primary article: *Use of artificial intelligence and automation technologies at work*,
<https://www150.statcan.gc.ca/n1/pub/75-006-x/2026001/article/00007-eng.htm>.

| Item | Verified value |
|---|---|
| Population | Workers aged **15 to 69** living in the **provinces**; excludes residents of the territories, people living on Indigenous reserves and other settlements, full-time members of the regular Armed Forces and unpaid family workers |
| Collection | Four periods: 23 Sep–18 Oct 2024; 16 Dec 2024–17 Jan 2025; 17 Mar–17 Apr 2025; 23 Jun–18 Jul 2025. Estimates are the **average of the four periods** |
| Construct | Used generative AI **as part of the main job or business in the previous 12 months** |
| Published crude rates by gender | **Women 22%, men 22%** (rounded, overall) |
| Published adjusted association | Logistic regression, Appendix Table A.1: **Male+ odds ratio 1.15 (95% CI 1.02–1.29)** versus **Female+ (reference)**, adjusting for occupation, industry, education, age, region, firm size and class of worker |
| Gender measure | Two-category **Female+ / Male+**: the article states that because the non-binary population is small, data were aggregated to a two-category gender variable to protect confidentiality, and non-binary respondents are **distributed into the other two categories**, denoted by “+” |
| Analysis caveat stated by the source | Measures capture whether a technology was used, **not intensity or frequency** |

**Interpretation rules carried into the register.** The crude rates show no gender
difference; the adjusted model shows a higher odds of use for Male+ once occupation,
industry and education are held constant. An odds ratio is **not** a percentage-point gap
and **not** a causal effect: do not convert it, do not describe it as “men use X points
more”, and always report the two results together with the confidentiality aggregation
note. The “+” categories are not a measure of non-binary experience and must never be
presented as one.

## 2. March 2026 Labour Force Survey AI supplement (`CA_LFS_AI_2026`)

Primary release: *Use of generative artificial intelligence tools among Canadian workers,
March 2026*, The Daily,
<https://www150.statcan.gc.ca/n1/daily-quotidien/260730/dq260730b-eng.htm>.

| Item | Verified value |
|---|---|
| Vehicle | **Supplement to the Labour Force Survey, March 2026** (a different survey vehicle from the CSWC) |
| Universe | Respondents aged **15 to 69** living in the **provinces**; excludes people on reserves, full-time regular Armed Forces members and institutional residents |
| Construct | Use of generative AI tools at work in the past 12 months, analysed by **potential occupational exposure to and complementarity with AI** groups |
| Published gender cells | High-exposure/high-complementarity occupations: **men 57.0%, women 50.9%**. High-exposure/low-complementarity: **men 52.9%, women 41.2%** (a difference of 11.7 pp as stated by the source). The release states there was virtually no gender difference in the remaining group |
| Gender measure | Reported as men / women in the release text; the release does not document a third category |

**This release is not a CSWC update.** It uses a different vehicle, a different reference
month and an occupational-exposure classification that is itself a modelled construct.
The exposure grouping is a property of occupations, not of respondents' AI benefit or
harm, and the sex composition of those occupational groups differs — so a within-group
gender gap is not the same quantity as an overall gender gap.

## Access and reuse

- Both pages are open, no registration. Statistics Canada content is published under the
  **Statistics Canada Open Licence**, which permits reproduction with attribution; the
  licence text was **not** re-read in this audit, so the register records the licence as
  “documented, text not verified this pass”.
- Microdata for either source (PUMF or RDC access) was **not** requested and is not
  needed for the published cells above.

## Open items

1. Locate the corresponding StatCan data tables for both sources so the published cells
   can be pinned to a table/vector identifier and a file hash, rather than to article
   prose.
2. Confirm whether any published standard error or coefficient of variation accompanies
   the gender cells (the article supplies a CI for the odds ratio only).
3. Read the open-licence text before republishing the cells.
