# Proposed v1 inclusion list

Data steward, 1 October 2026. Companion to [`permitted-cells.csv`](permitted-cells.csv),
which holds the exact cells, their definitions, provenance and display rules.
This is a **proposal for Codex review and Emily's decision**, not an approval. No ranking,
regression, model, composite or causal estimate is proposed, and none was produced.

## Tier 1 — display with full provenance (file-verified published cells)

| Module | Source IDs | What v1 can show | Cells |
|---|---|---|---|
| European core | `EU_USE`, `EU_PURPOSE`, `EU_NONUSE` | Male and female generative-AI use in the last three months, 2025, for the EU27 aggregate, the euro-area aggregate and 35 countries; purposes and single main non-use reason on the same wave | C01–C05 |
| United Kingdom | `UK_DSIT_USE` | A four-category gender breakdown of the DSIT “generative AI user” composite, with the composite's definition printed | C06 |
| Brazil | `BR_CETIC_USE`, `BR_CETIC_NONUSE` | Male and female AI-tool use among internet users **with published margins of error**, and multiple-response non-use reasons | C07–C08 |
| Republic of Korea | `KR_NIA_USE` | Male and female generative-AI service experience in the last year, **including a published sex-by-age breakdown** | C09–C10 |

These four modules are the only ones where this audit read the provider's own file, pinned
its hash and reproduced the cells with committed code.

## Tier 2 — display as attributed published findings (no file acquired)

| Module | Source IDs | What v1 can show | Cells |
|---|---|---|---|
| Canada, workplace | `CA_CSWC_WORK` | Equal crude rates (22% / 22%) **together with** the adjusted Male+ odds ratio 1.15 (1.02–1.29) and the confidentiality-aggregation note | C11 |
| Canada, occupational exposure | `CA_LFS_AI_2026` | Within-exposure-group gender differences, labelled as a separate March 2026 sample | C12 |
| United States | `PEW_GENDER` | Published US gender figures for chatbot use and attitudes, with “ever use” stated | C14 |
| Global attitudes | `PEW_GLOBAL_ATT` | The published gender finding on job-loss expectations (11 countries; France 10 pp), labelled attitudes | C13 |
| Multi-country workplace null | `MELB_KPMG_TRUST` | The published global statement of no gender difference in AI use or attitudes at work, with design caveats | C15 |

Tier 2 entries are quotations with attribution. They must not be re-tabulated as if they
were our own extraction, and the two Canadian entries and the two Pew entries must each
carry their sample-family note.

## Tier 3 — evidence cards only, not displayed as values

Each of these has an open question that blocks display. The card should state the question,
the dated attempt and the next check: `AU_ADII_GENAI` (gender cells behind a terms click),
`SIGNALS_TOPIC` (download 403; messages and name proxy, not people), `ILO_EXPOSURE`
(series not located; exposure is not adoption), `ISSP_ATTITUDES` and `EWCS_WORK` (access
blocked), `EB_SUPPORT`, `CEDEFOP_SKILLS`, `ECB_WORK`, `RPS_USE_RETURNS`,
`SPAIN_MOTIVATION`, `ANTHROPIC_CONTEXT` (carried forward unverified or reuse-restricted),
`RIA_AFTERACCESS_CONTEXT` (digital access, not AI), `UK_OFCOM_ONLINE`, `JP_MIC_GENAI`,
`MX_ENIAG_HE` (queued leads), `CRANNEY_SYNTHESIS` (source-finding tool, never an
indicator).

## Rules that must survive into the presentation

1. **One panel per source, no cross-source arithmetic.** Reference windows alone differ
   three ways across the Tier 1 modules: three months (EU, UK, Brazil), one year (Korea),
   twelve months at work (Canada).
2. **Denominators on the face of every value.** All individuals aged 16–74, recent internet
   users aged 16–74, all UK adults 16+, Brazilian internet users 10+, Korean internet users
   12+, Canadian workers 15–69 in the provinces.
3. **Definitions on the face of every value.** The UK composite includes autonomous
   workplace AI; Brazil's item says “AI tool” with generative examples including Meta AI in
   WhatsApp; Korea prompts with named services; Eurostat asks about creating content with
   named generative tools.
4. **Uncertainty shown honestly.** Brazil has published margins of error. Nobody else
   does: the UK publishes a design effect but no interval in the AI workbook, Korea
   publishes only a survey-level error, Canada publishes an interval for an odds ratio only,
   and Eurostat publishes none at all. Do not manufacture intervals from bases.
5. **Gender categories kept as the provider recorded them.** Two categories for Eurostat,
   Brazil and Korea; four for the UK, including “identify in another way” with its base of
   99; “Female+/Male+” for the Canadian CSWC, which absorbs non-binary respondents by
   design and is not a measure of their experience.
6. **No pooled or world figure, no country ranking, no coverage percentage of the world
   population.** Country counts exclude aggregates.
7. **Female-higher cells are real.** The pilot found six European geographies where the
   female rate exceeds the male rate; Brazil's non-use reasons are higher for women on all
   four substantive reasons while its use rate is lower. Both directions must be displayed
   without clipping or re-signing.
8. **Family labels visible.** `EU_ICT_2025` is one survey wave behind three Eurostat rows;
   `PEW_ATP_W187` is shared between the US report and the global study's US February data;
   the two Canadian rows are different vehicles from one provider;
   `BR_CETIC_TICDOM_2025` and `KR_NIA_INTERNET_2025` each cover three rows.

## What v1 therefore validly shows

A **source-specific international evidence map with four file-verified national modules
(Europe as a 35-country harmonised set, the UK, Brazil, Korea) and five attributed
published findings (Canada twice, the US, a 37-country attitudes study, a 47-country
workplace null)**, with coverage gaps shown explicitly and no cross-source comparison.

It does **not** show: a global adoption rate, a comparable cross-country adoption series
outside Europe, any trend (every verified source is a single period), any sex-by-occupation
cell, any non-binary estimate beyond the UK's single provider category, or any measured
economic return.
