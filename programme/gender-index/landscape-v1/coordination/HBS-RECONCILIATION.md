# HBS corpus reconciliation

Codex, 1 October 2026. All 76 numbered entries in Table A1 of the May 2026 foundational paper now have a dated, source-level disposition in [hbs-corpus.csv](../../evidence/hbs-corpus.csv). They are linked into the existing [source atlas](../../evidence/source-register.csv), [literature register](../../evidence/literature.csv) and [explorer](../index.html#sources). This completes the initial entry accounting, not the primary-source audit or the resolution of every sample overlap.

## What the counts now mean

| Count | Unit and boundary |
|---|---|
| 76 | Numbered HBS source/outcome entries: 58 plotted and 18 narrative. No entry omitted. |
| 75 | Citation records for those entries, and 75 linked source cards. Entries 8 and 56 share a publication and card but retain separate entry links. This is not a count of independent samples. |
| 111 | Explorer/source-atlas cards: the original 33, 73 cards added from the HBS reconciliation, and five previously registered literature leads newly made visible. |
| 36 | Cards outside the 75 mapped HBS cards. Includes datasets, additional measures, interpretation, comparators and the HBS synthesis itself. Does not mean 36 independent additional studies. |
| 85 | Literature-register records: 75 HBS citations plus 10 existing records outside the numbered corpus. This register and the dataset/indicator atlas count different things. |

The source-card total is deliberately not described as a dataset count. Nor does it count sources ready for our original analysis: that requires file access, suitable variables, permission and design checks. No new adoption estimate, effect size, country panel or composite score was added by this reconciliation.

## Matching and overlap decisions

- **Entry 21:** matched to the existing `HUM_VEST` literature record and made visible as a source card. Its prior primary-access limitation remains.
- **Entry 48:** linked to `EU_USE` at dataset/outcome level. The official narrative companion proposed by the literature specialist is the Eurostat publication cited by HBS. `EU_PURPOSE` and `EU_NONUSE` remain related measures; they do not become extra HBS entries. Our checked primary-vintage metadata takes precedence over different fieldwork wording in the review.
- **Entry 53:** linked to `RPS_USE_RETURNS` at family level. The precise 2024 paper version and survey waves remain to be checked. Entry 49 is retained separately as the later seven-country publication; possible sample relationships are not assumed resolved.
- **Entries 8/56:** one publication/card, two outcomes. Neither is silently substituted for the existing June 2026 Anthropic lead.
- **Entries 63/75:** distinct publications with the same Nature AI-and-science sample-family identifier. Analytic exclusions and sample-count differences still require primary checks. The Nature postdoc survey, entry 68, remains separate.
- **Entries 31/43 and 41/43:** possible survey overlap or related source lineage is explicitly flagged. No claim of independent replication follows from different citations.
- **Pew, Australian, Korean, UK, Spanish and European worker sources:** a shared provider, country or broad population is insufficient for a match. The crosswalk records the relevant existing IDs and the reason for retaining separate records or checking identity. In particular, the 2023/2025 Pew entries do not inherit our verification of the 2026 wave; AIM-WORK is not EWCS.

For the other citations, no matching citation was identified in the current programme registers. Their disposition is “Added review-derived citation”, with sample overlap still unreviewed. `UNRESOLVED_HBS_*` identifiers are placeholders for unresolved family identity, not evidence of independent datasets. No HBS entry was excluded on quality, access or comparability grounds.

## Existing specialist leads also accounted for

The specialist's 25 `literature-updates.csv` rows are field-level suggestions, not 25 distinct studies. Its six `proposed_new` identifiers now have these dispositions:

| Proposed identifier | Disposition |
|---|---|
| `NEW_EUROSTAT_SE` | HBS entry 48 / `HBS_048` literature record / `EU_USE` card; the official narrative is a companion to the checked dataset. |
| `NEW_CETIC_BR` | Existing `BR_CETIC_USE`, `BR_CETIC_PURPOSE`, `BR_CETIC_NONUSE`; retain the coordinator's primary checks. |
| `NEW_STEPHANY_DUSZYNSKI` | HBS entry 57 / `HBS_057`; the specialist inspected a later arXiv revision's abstract. The review's earlier metadata and later revision must be distinguished. |
| `NEW_STATCAN_WORKER` | Existing `CA_CSWC_WORK`; distinct from `CA_LFS_AI_2026`. |
| `NEW_AIM_WORK` | HBS entry 65 / `HBS_065`; primary verification remains pending. |
| `NEW_PLATFORM_PROXY` | A construct grouping, not a new dataset: entry 61 / `HBS_061`, entry 67 / `HBS_067`, and the SimilarWeb analysis in `CRANNEY_SYNTHESIS`. |

The five pre-existing literature records newly surfaced as cards are `ILO_GENDER`, `NOY_ZHANG`, `WOMEN_AI_INDEX`, `GIRAI` and `OPENAI_JOB_TRANSITION`. Their recorded verification limitations are carried forward. `PEW_REPORT` already corresponds to `PEW_GENDER`, and `ILO_EXPOSURE_METHOD` to `ILO_EXPOSURE`; these were not added as duplicate cards. Being outside the numbered corpus does not establish that a source is absent from the HBS paper's references or discussion.

## Provenance and verification boundary

Bibliographic identifiers and concise factual sample-scope metadata were read from Table A1, with measurement/relationship checks informed by Tables A2/A3 and the references. Each crosswalk row links to its PDF page and states its evidence basis. Original source descriptions, table prose and numerical findings were not copied into the new catalogue. The [full-reading record](HBS-READING.md) identifies the exact PDF version and hash.

New HBS cards are labelled **Review-derived; primary check pending**. They generally link back to the relevant HBS page as a discovery source; that link is not represented as a checked primary publication. The existing Humlum primary link and the later Stephany abstract lead are identified separately. An open review does not establish open microdata or redistribution rights. Source-specific definition, precision, gender coding and data access remain explicit unknowns where unchecked.

## Next research work

The omission of the numbered corpus is corrected. The next stage is substantive primary-source verification and synthesis: resolve exact citations and versions, check measurement and selection, confirm overlap, record access and feasible variables, and assess what findings should enter the narrative or a numerical panel. Prioritise sources that resolve an important disagreement, fill geographic/construct gaps or establish an original-analysis opportunity; also retain contrary, null and female-advantage evidence. Do not choose a deep dive merely because it is easiest to download.

The global coverage question remains evidence-led. The additional countries appearing in review-derived cards expand the discovery map, not the set of comparable countries in the index. Updated search and screening outside this foundation are still needed before calling the wider landscape complete or systematic.

No new paid session, subscription or manuscript revision was undertaken. The builder checks entry coverage, cross-register links and known overlap relationships, while retaining the existing numerical-panel checks.
