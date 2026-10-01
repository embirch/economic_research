# V1 integration and review

Codex coordinator, 1 October 2026. Internal working research edition for Emily's review. This records what the edition actually accepts; a specialist proposal is not automatic scientific approval or permission to publish a public website.

## Accepted presentation

The geographic approach is an international evidence explorer with an EU27 comparative core. National panels remain separate. Regional evidence cards include incompatible constructs and access-blocked leads with those limitations visible; they are not additional countries in a comparable index. No composite score, global rate, world-population coverage percentage or cross-source league table is produced.

| Panel | Provenance and independent check | Boundary |
|---|---|---|
| EU27 and EU aggregate, four use contexts | Fixed article commit `669b9ac0d3d6dc4c35837ee3b09df284d1442e33`; official TSV and two result CSV hashes; 112 male/female pairs checked against source cells, flags and existing differences | All individuals 16–74; PC_IND only; 2025; no gap intervals or significance claims. Non-EU extensions, age/education results and user-only denominators are outside this display. |
| UK DSIT | Pinned ODS, Table E5 B38:F41; coordinator questionnaire and technical-document checks; all four provider categories retained with bases | Broader AI definition and 16+ age scope; published weighted rates, unweighted bases. Subgroup interval locations unresolved; no CI inferred from overall design effects. |
| US Pew | Pinned HTML headline table independently parsed; methodology confirms Wave 187 and fieldwork | Ever use among adults, not recent use. Similar shares are not equality; 2024 routing/wording differs. Profile gender coding not fully audited. |
| Canada CSWC | Primary narrative, methods and Table A.1; adjusted model cells independently parsed from pinned HTML | Rounded crude rates and adjusted odds answer different questions. Male+/Female+ confidentiality grouping; provinces and survey exclusions; no new model or effect estimate. |
| Brazil Cetic.br | Hash-pinned aggregate ZIP independently downloaded and the full extractor JSON reproduced; HTML sex rows, questionnaire, collection dates, sampling frame, 95% margin method and bundle licence checked | Internet users aged 10+ in permanent private households, with specified census-sector exclusions; per-rate margins are not gap uncertainty. No direct comparison with Eurostat. |

Source copies are outside Git. The saved extracts contain permitted selected public aggregates and provenance, not respondent records or full third-party archives. Files can be rechecked locally using the commands in [README](README.md); changed source hashes require an explicit vintage review. The build validates the European, UK, US and Brazil display cells and the Canadian narrative values against reviewed inputs. It does not independently validate each provider's statistical estimation.

## Scientific review and withheld claims

The [synthesis review](coordination/synthesis-review.md) explicitly records corrections to the programme lead's submission. The reviewed [synthesis](SYNTHESIS.md) takes precedence over its preserved draft. Chief corrections concern null findings, trend comparability, sample-family identities, the Canada survey name, Eurostat purpose availability, SimilarWeb account coverage and overbroad absence claims about economic outcomes. Lead claim IDs and the proposed literature updates remain discovery records, not a whitelist of approved assertions.

The original Eurostat pilot remains preserved with its [first review](../reviews/2026-10-01-pilot-review.md). The non-use denominator reconstruction C2 is not an accepted harmonisation formula; its discrepancies cannot be explained by rounding alone. No numerical non-use panel is displayed. The programme's original manuscript is not retroactively rewritten by this integration.

Also withheld: unverified Danish encouragement/training magnitudes; an untraced GIRAI world-use percentage; HBS's illustrative aggregate productivity extrapolation as if it were an identified estimate; secondary-only adjusted counterestimates; provider-inferred demographics as self-reported gender; occupation exposure as observed harm; and inaccessible microdata as if already analysis-ready.

## Scope and remaining work

Coverage correction following Emily's review, 1 October 2026: the bounded assignment was delivered, but the broader evidence landscape remains incomplete. The 33 catalogue cards mix source, indicator and literature records; the HBS review is one card, and its 76 underlying sources have not been individually reconciled. They have not all been screened and excluded on quality or availability grounds. The [reconciliation work](coordination/COVERAGE-RECONCILIATION.md) must precede deep-dive selection.

The initial audit supplies dispositions for its assigned inventory, documented regional discovery, selected checked measures and explicit blockers. It is not a systematic worldwide review. Wider literature and national coverage, joint gender-by-age/occupation variables, usable uncertainty, publication terms and novelty comparisons still require source-specific work. No absence claim follows from an unsuccessful download or a region without a displayed panel.

The UK, US, Canada and Brazil panels are examples of source-specific published evidence. They do not establish cross-national differences in gender gaps. A statistical-significance test would need suitable design-based variance information; rounded published values and unweighted counts alone are insufficient.

Original research remains an outstanding programme deliverable. Emily's [SimilarWeb and event-response ideas](coordination/emerging-questions.md) join the unranked question log. No new paper, vendor subscription, outreach, event analysis or additional paid agent session has been commissioned. Broaden and reconcile the evidence library first, then compare feasible original questions against existing research and define a bounded study.

## Reproducibility and author preservation

The read-only adapter never imports the article's code or writes its files. The live manuscript's SHA-256 was checked as `c98f327ace493a24efae4ae12baa397dc3569e926779ae24661eb26e5f9097c5`; pre-existing untracked `output/` and `tmp/` were left alone. The paper remains available for deliberate later revision.

The presentation builder and coordinator adapters use the Python standard library and browser JavaScript. The separate Brazil workbook extractor requires `openpyxl`; the specialist Korea PDF extractor requires `pdftotext`. Those extraction dependencies are not needed to open or rebuild the explorer from its committed inputs. The HTML embeds its reviewed input data. The generated manifest records file hashes; the page offers source filters, country/context selection and CSV access. Technical checks and final delivery costs are recorded below.

## Delivery record

The programme lead delivered `97c38b0` at $8.00; the data steward delivered `78d8db2` plus correction `5082703` at $20.94. Both sessions are idle. Total additional Claude spend is **$28.94 of the $60 approved envelope** ($40 steward, $20 lead; $36/$18 service limits). The earlier $6.21 pilot is a separate tranche. No further session or resumption is authorised.

The working edition contains 33 reviewed source cards, 112 European country/context pairs (EU27 plus the EU aggregate, four contexts) and four national panels. Source cards do not represent independent studies. The steward’s original 31-row register, 72-entity coverage table and scripts remain preserved; the reviewed central atlas adds two existing literature records and coordinator qualifications.

Validation: setup consistency and session guard checks; specialist CSV/ID checks; European source-cell adapter; UK pinned-workbook and US/Canada/Brazil primary-page checks; independent Brazil aggregate extraction; presentation input validation and JavaScript syntax. Browser review covers source filters, country/context selection, CSV export and a narrow mobile viewport. The original author file hash is unchanged. This review establishes the documented technical checks and selected source verification, not comprehensive replication or external peer review.

## Foundational reading and coverage correction

Following Emily's feedback, the coordinator read the complete May 2026 HBS paper, including both appendices, and recorded [methodological and research implications](coordination/HBS-READING.md). This supersedes earlier selected-passage verification. The catalogue still needs the [full corpus reconciliation](coordination/COVERAGE-RECONCILIATION.md); full reading does not mean all primary sources have been checked. The source-register and explorer verification fields now state this boundary. No numerical panel inputs changed.

## Corpus entry accounting completed

The [HBS reconciliation](coordination/HBS-RECONCILIATION.md) supersedes the catalogue-count status above: 111 cards now include all 76 numbered HBS entries, mapped to 75 cards, plus 36 other programme records. The original 33 cards remain; 73 HBS cards and five already registered literature leads were added. New records retain review-derived or carried-forward verification labels. No numerical estimate or panel was added. The builder checks complete entry coverage, source/literature links, known shared-publication/sample relationships and exclusion of review-derived sources from numerical panels. Primary verification, exact-wave matching and wider discovery remain research work.

Reconciliation validation: all 76 citation/provider tokens were checked against their recorded Table A1 pages; the complete crosswalk, 111 atlas/card IDs and 85 literature IDs pass linkage checks. Browser filters returned 75 cards/76 entries, 57 cards/58 plotted entries, 18 narrative cards/entries and 36 other cards; the shared-publication search returned one card/two entries. Provisional RPS mapping text was visibly checked. Generated CSV files validate, and JavaScript syntax passes. The automated filtered-download event was not captured, so this turn does not claim a newly verified browser download. Original numerical arrays and the other 32 pre-existing source cards are unchanged; the author-file hash remains unchanged.
