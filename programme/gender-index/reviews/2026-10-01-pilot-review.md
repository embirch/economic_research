# Coordinator review of the first steward pilot

1 October 2026. Reviewed steward commit `4b3b8a9` on `work/index-steward-pilot-2026-10-01`. This is a limited coordinator verification, not an independent referee report. Read this before adopting the [steward report](../evidence/pilot-2026-10-01/PILOT-REPORT.md) or its three updated register rows.

**Disposition: pilot delivered; revisions required before scientific integration.** The file checks reproduce, but parts of the report overstate release readiness and geographic representativeness. Preserve the specialist's submitted work and request the corrections below; do not silently treat it as approved evidence. No live indicator, release geography or new analysis has been approved.

## What the pilot establishes

- Two public Eurostat aggregate downloads were independently retrieved by Codex at 08:47:52–54 UTC on 1 October. Both SHA-256 hashes match the steward's profile. The use file also matches the article's frozen official file. This establishes the identity of this input, not reproduction of the entire manuscript or proof that no intermediate revision ever occurred.
- Headers inspected before executing the steward script contain a single 2025 period. The script reproduces 39,006 use/purpose cells across 35 countries/territories plus two aggregates, and 54,825 non-use cells across 36 countries/territories plus two aggregates. The EU27 countries are included in these country counts, not added to them.
- Re-running `checks.py` reproduces C1: 9,486 comparisons, maximum difference 0.963 percentage points; C3: 12,920 comparisons, maximum 0.019; C2: 6,510 comparisons, maximum 6.523, with headline male/female maximum 1.598. C2 remains an unresolved cross-table denominator discrepancy. These diagnostics are not pass/fail acceptance tests or evidence that all differences have been explained.
- The file structure, flags and available male/female codes reproduce. Missing cells and low-reliability flags must remain visible. No uncertainty estimate can be recovered from these TSV cells alone.
- Locally, all four article source hashes match their manifest. The author-edited manuscript remains unchanged, SHA-256 `c98f327ace493a24efae4ae12baa397dc3569e926779ae24661eb26e5f9097c5`.

## Required corrections and unresolved checks

| Item | Correction or evidence needed |
|---|---|
| Worldwide representation | Replace “genuinely global, population-representative” with a description of the countries actually surveyed. Pew's national samples do not establish representation of the world population. Joint country-by-gender cells, item coverage and reuse remain to be audited. |
| Pew sample/fieldwork | The [primary report](https://www.pewresearch.org/global/2026/09/17/globally-more-people-expect-ai-to-cause-job-loss-than-growth/) says 42,151 respondents across **36 non-US countries**, February–May 2026. US results come from **two separate surveys**, February and June. Do not attach the non-US sample total and dates to the entire 37-country report. It measures AI attitudes, not generative-AI adoption. |
| European country count and readiness | Correct the report's “EU27 + 35–36 countries” wording. Replace “instrument-identical” and blanket readiness with a harmonised framework whose national implementation still needs review. Remove the unsupported “roughly 6% of world population” figure. No world-coverage denominator was verified. |
| Survey-wave documentation | The profile names Regulation 2025/1322 as the 2025-wave basis. [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ%3AL_202501322) identifies it as the **2026** reference-year instrument; the [Eurostat metadata](https://ec.europa.eu/eurostat/cache/metadata/en/isoc_i_esms.htm) appears inconsistent on this point. Resolve the wave/version mismatch against the 2025 instrument before adopting routing and questionnaire claims as definitive. This is a source-document inconsistency, not a reason to change the paper. |
| Uncertainty and residuals | Narrow “no sampling errors are published for any generative-AI rate” to “none available in the inspected tables.” National precision publications were not audited. An approximately 1% shortfall in reason totals does not alone prove item non-response. Check documentation before assigning that explanation or explaining C2 by national routing. |
| Reuse scope | The [Eurostat notice](https://ec.europa.eu/eurostat/web/main/help/copyright-notice) contains exclusions for particular material and commercial reuse of certain countries' data. Carry relevant conditions into summaries and the register; “clear for reuse” is not blanket clearance. Check the applicable country status rather than suggesting BA/XK share the same status. |
| Signals version | A 2026Q1 hub entry does not establish that the prior bundle, inspected through June 2026, is superseded. Current version remains unverified. |
| Exploratory work and code limits | The session performed exploratory gap arithmetic before a scope correction, so replace the report's absolute claim that none was produced with a disclosure that none is an approved index result. The script is a diagnostic for the inspected single-year snapshot: it skips the header, prints residuals, and does not enforce acceptance thresholds. Add explicit schema/year/duplicate validation before making it a maintained pipeline. |
| Discovery counts and status | Keep “3 file + 4 documentation + 7 carried” explicitly tied to the 14 original indicator rows; the coverage CSV also includes a synthesis and four additional source leads. Count unique source families separately. Regional “nothing” must mean no verified adoption indicator in this bounded pass, not no relevant data anywhere. |

These requests are recorded for the next authorised correction/inventory assignment. No paid session was resumed to address them. The original specialist files and three register rows remain draft submissions on this branch; this review limits their use pending correction.

## Geographic recommendation and next work

Proceed with the design of an international evidence resource with source-specific modules, using the European material as the first candidate foundation. [The coordinator scope note](../GEOGRAPHIC-SCOPE.md) records Brazil, Canada and a multi-country survey as concrete leads. None establishes an aligned global adoption series. Unknown coverage in Africa, Asia and Oceania remains an open search question.

The next proposed assignment should first close the consequential Eurostat documentation issues, then audit Brazil and Canada files/terms and the multi-country sources' actual joint gender cells. Report comparable groups and exclusions before choosing a release label or building calculations. Further paid work requires its own scope and cap under the accepted proposal.

## Session and spend

Existing data steward v3, session `sesn_01Nd6UQtbow3FztwfczxvAcY`, launch commit `b04508a`. User envelope **$20**, configured service limit **$18**, final API list cost **$6.21** (621 USD cents), status `idle`; local runner exited successfully. The remaining envelope is not automatically reallocated. No further paid agents launched. Durable outputs and cost are linked in `team/RUNS.csv`.
