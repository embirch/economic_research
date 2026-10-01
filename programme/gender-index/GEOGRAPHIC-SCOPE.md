# Geographic scope: decision framework and initial leads

## V1 integration update, 1 October 2026

The [working v1](landscape-v1/README.md) implements option B below for review: an international evidence explorer with option A as its European comparison core. It includes EU27 plus a separately labelled EU aggregate, four source-specific national panels (UK, US, Canada and Brazil), and wider source cards. Korea remains a source card while reuse terms are unresolved. The finite audit has not established option C, a comparable global series. This is an edition architecture, not a final public-release decision.

The [reviewed atlas](evidence/source-register.csv), [coverage matrix](evidence/v1-audit-2026-10-01/coverage.csv) and [integration review](landscape-v1/REVIEW.md) supersede the pending-check status of the initial leads below. Regional search coverage is not representative population coverage. The initial scoping record is retained for provenance.

Codex coordinator note, 1 October 2026. Emily prefers global scope, conditional on data. This note supplements the bounded Claude steward pilot; it is a targeted scoping pass, not a systematic world inventory or a final release decision.

The completed pilot and reproduced file diagnostics are assessed in the [coordinator review](reviews/2026-10-01-pilot-review.md). Its required corrections take precedence over stronger readiness/representation claims in the draft steward report.

## Decision to make

Keep global ambition in the programme design. Determine separately the geography of each measure and the geography covered by the evidence library. The existing European paper does not set the outer boundary of the index.

| Option | What a reader could validly compare | Evidence required | Provisional assessment |
|---|---|---|---|
| A. European comparative core | Harmonised survey measures within eligible European countries and years | Verified common instruments, denominators, coverage and limitations | Strong existing foundation; does not exhaust the broader programme |
| B. International resource with source-specific modules | Within-source comparisons; related national findings shown separately | Additional national sources with interpretable sex/gender measures, accessible evidence and permitted reuse | Worth pursuing now: targeted checks found relevant Brazil and Canada evidence |
| C. Comparable global survey indicators | Countries with sufficiently aligned constructs, populations, reference periods and methods | Verified joint country-by-gender data across diverse regions, measurement equivalence and usable uncertainty | Not established by this pass; multi-country research is a lead, not proof |

Recommendation for investigation: design for B, use A as its first reproducible component, and test C explicitly. Do not brand a world population estimate or worldwide ranking from a collection of selected-country sources. A global research remit can coexist with incomplete, clearly marked indicator coverage.

## New primary-source checks

Retrieved 1 October 2026 through public provider pages. No respondent data downloaded; no new gap estimates calculated. These are proposed additions to the source queue, separate from the existing 14-row inventory until reviewed.

| Candidate | What was actually verified | What remains unresolved | Implication |
|---|---|---|---|
| Brazil, Cetic.br TIC Domicílios 2025 | The provider's [M1 HTML table](https://www.cetic.br/pt/tics/domicilios/2025/individuos/M1/) publishes generative-AI use by male/female sex categories among internet users, with age bands beginning at 10–15. The [indicator index](https://www.cetic.br/pt/tics/domicilios/2025/individuos/) lists M2 purposes and M3 non-use reasons. | Exact reference window, survey methods, joint age-by-sex cells, downloadable precision tables and reuse conditions need a bounded file audit. Separate age/sex margins cannot create joint cells. | Concrete Latin American national-module candidate. The displayed internet-user denominator and age coverage differ from the paper's all-individuals EU16–74 measures. |
| Canada, Statistics Canada CSWC | The [June 2026 article](https://www150.statcan.gc.ca/n1/pub/75-006-x/2026001/article/00007-eng.htm) reports workplace generative-AI use and gender comparisons. Its methods identify workers aged 15–69 in the provinces, four collection periods during September 2024–July 2025, and past-12-month use in the main job/business. A confidentiality note describes redistribution of nonbinary respondents into two categories denoted with a plus sign. | Need exact reusable gender tables, gender-gap precision, access/terms and harmonisation checks; no microdata acquired. Preserve geographic and population exclusions. | Concrete North American workplace-module candidate; cannot append to Eurostat household-use rankings. |
| University of Melbourne/KPMG 2025 survey | The [provider report](https://mbs.edu/-/media/PDF/Research/Trust_in_AI_Report.pdf?rev=0ee82285b2b0439bba524dbddc58214a) documents 47 countries/jurisdictions, online fieldwork November 2024–January 2025, and gender demographics. Country coverage includes Africa, Asia, Latin America, North America, Europe and Oceania. Methods mix general-AI questions with randomly allocated application-specific questions, including generative AI. Appendix 2 acknowledges overrepresentation of university-educated respondents in emerging economies. | Usable country-by-gender outcome tables, respondent-data access and reuse permission are unverified. Broad-AI indicators cannot silently become generative-AI measures. Check country sampling exceptions and whether every intended joint cell exists. | Priority cross-region feasibility lead. Geographic breadth alone does not establish a representative global adoption series. |

This limited search also encountered an [ITU AI for Good community survey](https://aiforgood.itu.int/your-voice-matters/?topic=1): recruitment through an AI-interest mailing list/social media does not support national population prevalence. [GSMA mobile gender-gap evidence](https://www.gsma.com/gender-gap/) measures digital access and use; it must not substitute for direct generative-AI adoption. These are useful scope boundaries, not rejections of their original purposes.

## Regional coverage audit to complete

- Europe: distinguish EU27, non-EU European countries and aggregates; do not count an aggregate as another country.
- Latin America/Caribbean: investigate Brazil first; record other countries and the Caribbean as unchecked unless primary evidence is inspected.
- North America: inspect Canada and the existing US leads separately; no North-American regional average from these national sources.
- Africa: multi-country survey leads include Egypt, Nigeria and South Africa, but this pass has not verified usable country-by-gender generative-AI cells. Search national and regional sources before concluding coverage is absent.
- Asia: distinguish East, South, Southeast and West/Central Asian coverage rather than treating one country as representative of the region. The multi-country lead contains several Asian jurisdictions; exact eligible joint cells remain unverified.
- Oceania: Australia and New Zealand appear in the multi-country lead; other Pacific coverage remains unchecked.

For each regional entry, record: source identified; primary documentation checked; joint gender measure confirmed; file acquired; reuse permitted; uncertainty assessed; comparable group assigned. Keep not searched, no suitable source found in a specified search, inaccessible, incompatible and missing distinct.

## What would support a broader release decision

1. A country-by-construct coverage matrix backed by dated evidence, not simply a count of publications or countries mentioned in reports.
2. At least one feasible module outside Europe with meaningful sex/gender comparisons. This is a minimum test for expanding the first edition, not a definition of global coverage.
3. A comparison dictionary stating where age bounds, denominators, question wording, tool scope and reference periods differ. Harmonisation must follow actual joint data; do not reconstruct unobserved cells from margins.
4. A separately reported assessment of geographic breadth, population coverage, representation and statistical comparability. Do not report a global coverage percentage until eligible country data and matching population denominators have been verified.
5. A reasoned release label: European core, international evidence explorer, or a specific comparable cross-country series. The decision does not automatically alter the first paper's geography; deliberate paper revisions remain possible under the [research agenda](RESEARCH-AGENDA.md).

No final geography has been selected. A bounded next audit of Brazil, Canada and the multi-country survey is more informative than either assuming a worldwide dataset exists or ruling out global scope from the Europe-heavy starter register.

## Local foundation check

On 1 October 2026, Codex recomputed the four SHA-256 values listed in the article repository’s `data/sources.csv`; all match. A read-only parse of the frozen official use TSV found 39,006 series, one year column (2025), 35 country/territory codes plus EU27 and euro-area aggregates, and the units `PC_IND`, `PC_IND_IU3`, `PC_IND_IUAI`. This verifies file integrity and table dimensions, not complete eligible sex-by-age coverage for every geography or statistical comparability. No article file or generated output was changed.
