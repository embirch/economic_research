# Broad source audit for landscape/index v1

> Coordinator integration note, 1 October 2026: preserved specialist submission. The [reviewed disposition](../../landscape-v1/coordination/source-audit-review.md) qualifies claims and governs v1 inclusion.

Data steward, 1 October 2026. Branch `work/index-v1-source-audit-2026-10-01`.
Assignment: [`team/assignments/2026-10-01-v1-steward.md`](../../../../team/assignments/2026-10-01-v1-steward.md)
(user authorisation: Emily's “ok go” to the explicit $60 additional Claude envelope,
1 October 2026; $40 user ceiling and $36 service limit for this assignment).

**What this is.** A source-verification and feasibility audit answering one question:
*what can landscape/index v1 validly show, across which populations and geographies, and
with what limitations?* It is not a deep-dive selection, an effect estimate, a ranking or a
model. No new gender-gap estimate was produced and none is proposed.

**Deliverables in this directory**

| File | Content |
|---|---|
| [`pilot-corrections.md`](pilot-corrections.md) | Disposition of all eight coordinator review items |
| [`source-register.csv`](source-register.csv) | 31 proposed register rows: the 14 original IDs preserved, plus coordinator-proposed and new IDs marked distinctly |
| [`coverage.csv`](coverage.csv) | 72 entity rows; countries separated from aggregates; *no source found in a dated search* separated from *not searched* |
| [`search-log.csv`](search-log.csv) | This audit's 19 dated searches and provider checks, with exact queries, URLs, routes and limits |
| [`permitted-cells.csv`](permitted-cells.csv) | The 15 exact published cells proposed for display, with definitions, denominators, provenance, reuse conditions and display rules |
| [`v1-inclusion.md`](v1-inclusion.md) | Proposed inclusion tiers and the rules that must survive into the presentation |
| `profiles/` | Source profiles: Brazil, Korea, Canada, Pew, UK DSIT outstanding checks, multi-country and platform leads |
| `checks/` | `check_cetic.py`, `check_korea.py` and their JSON outputs; `build_tables.py`; `check_outputs.py` |

The historical pilot directory and the coordinator's files were **read only**. No article
file, `literature.csv`, shared `indicators.csv`, coordinator record or run ledger was
touched. `posts/gender1/` was not used.

---

## 1. Headline findings

1. **The register's Europe-heavy shape was an artefact, and it can now be fixed with
   verified files.** Two national modules outside Europe were taken from “coordinator-supplied
   lead” to **file-verified published cells with committed extraction code**: Brazil
   (Cetic.br TIC Domicílios 2025) and the Republic of Korea (MSIT/NIA 2025 Survey on the
   Internet Usage). Both are probability-sample official or official-standard statistics
   with sex rows on a generative-AI item.
2. **Brazil is the only audited source whose published tables carry uncertainty for a
   sex-specific generative-AI rate** (male 34.79% ± 3.29 pp, female 30.49% ± 2.78 pp at
   95%). Eurostat publishes none; Korea publishes only a survey-level error; Canada
   publishes an interval for an odds ratio only. For the UK the position is different and
   should not be stated as an absence: the DSIT technical report (sections 7.5–8.2)
   documents 95% logit intervals computed in R `survey` for the published tables and a
   design effect of 1.67, but no interval column appears in the AI workbook or in a second
   inspected PES workbook, so **the published location of the gender-cell intervals is
   unresolved** and is recorded as a question, not as “no CIs published”.
3. **Korea is the only audited source that publishes a sex × age generative-AI
   crossing.** No audited source publishes a sex × occupation cell.
4. **No comparable multi-country adoption series exists outside the European core.** Every
   verified non-European module differs in reference window, age floor, denominator and
   stimulus. The two genuinely multi-country studies audited (Pew 37 countries, Melbourne/KPMG
   47 countries) measure attitudes or broad AI and **do not publish country-by-gender outcome
   cells**; Pew publishes only selected statistically significant gender differences, and the
   Melbourne/KPMG country tables have no gender split at all.
5. **Every verified source is a single period.** No trend, convergence or “gap is closing”
   statement is available anywhere in the audited material.
6. **Canada shows why the denominator and the estimand matter more than the headline.**
   Crude workplace use is 22% for both women and men; the adjusted odds of use are higher for
   Male+ (1.15, 95% CI 1.02–1.29) once occupation, industry and education are held constant.
   Both must be shown, and the odds ratio must not be converted into a gap.
7. **All eight pilot-review items are now dispositioned**, including the Eurostat wave
   documentation (a genuine inconsistency in Eurostat's own metadata) and the Signals version
   question (publisher still labels it v2.0; direct download blocked).

## 2. Exact files and versions verified

Downloads went to ignored scratch (`/tmp/v1audit/`). Only hashes, code and written evidence
are committed. No respondent-level file was downloaded; Brazil's microdata CSV was
deliberately left alone.

| File / object | Bytes | SHA-256 | Status |
|---|---:|---|---|
| Eurostat `isoc_ai_iaiu.tsv` | 1,560,775 | `7f668f7be9aaefaa5662ab2ab059875de8ccbe050c5c38a8de4b2c33a96896ab` | identical to the pilot and to the manuscript snapshot |
| Eurostat `isoc_ai_iaiuxr.tsv` | 2,483,018 | `8901c5c90b8661e23f609f406d59889efcbc740b09b8639ca9cea48b5eda8ef4` | identical to the pilot |
| `isoc_i_esms_an_ICT_Survey_Model_Questionnaire.pdf` (2025) | 999,470 | `2f556a1c7a96d8dfc9a310937f3b18927fd6a4b1e50d25c996fe84a0b45643ac` | identical to the pilot; front matter confirms 2025 coverage |
| `isoc_i_esms_an_Aggregated_variables_and_break.pdf` | 640,922 | `19c759b969102e50cda2ffd66cc11b4c9c5a8acfd8b30d2394f8e39099673ec0` | identical to the pilot; not parsed |
| DSIT AI tables `.ods` | 325,288 | `a34ed705b6f8c2966d82586917befaae975fee8f61206ef3a2d679cc95c4610a` | identical to the coordinator vintage; extractor reproduces |
| DSIT digital inclusion and skills tables `.ods` | 279,706 | `bc449398970cd1c0053443c2c63acc9e946a46db7b4cd1579785c7c9cd9b42e5` | new; checked only for the presence of confidence-interval columns (none) |
| Cetic.br individuals tables bundle v1.0 (`.zip`) | 1,027,291 | `9ca6638cc6a965d7d90de789cdc7f0e67de08918d4f4067c56575e9b621dd930` | new; parsed by `check_cetic.py` |
| Cetic.br methodological report v1.0 | 1,569,812 | `ba623fad92c9e7c7d0015186dd3df4e255992ab93e6716f9b2b5be824383f3a2` | new |
| Cetic.br data-collection report v1.0 | 1,444,385 | `f18a69305f7ed2f95512ee65b49774cf3be812720c5c2b27cac3fe35c2bd9237` | new |
| NIA 2025 statistical tables (English) | 4,815,170 | `12ec5ffec2596bed3162f671231ca3b166f2137031b76095f720d763a988bc00` | new; parsed by `check_korea.py` |
| NIA 2025 final report (English) | 46,515,597 | `70ecc9022000fdebced4fc626289688cbf8c3a4a67326fb0e015a812fa98a1d3` | new; design documentation |
| Pew global report PDF | 1,329,590 | — | read for appendix structure |
| Melbourne/KPMG report PDF | 5,498,658 | — | read for design, country tables, licence |
| ADII 2025 report PDF | 4,946,520 | — | read; no gender cell for generative AI |

Documents read without a committed hash: Eurostat ESMS metadata and copyright notice; the
EU compilers' manual landing page; DSIT technical report, online and paper questionnaires;
Statistics Canada CSWC article and the March 2026 Daily release; Pew methodology, topline
and appendix pages; Cetic.br variable dictionary and questionnaire; ILO Working Paper 140
landing page.

**Checks run.** `check_cetic.py` and `check_korea.py` both exit non-zero if the file hash,
sheet names, page captions or expected labels change; both pass against the audited
vintages and their outputs are committed as JSON. `build_tables.py` regenerates the four
CSVs. `check_outputs.py` validates them: no ragged rows, unique non-empty IDs, every
`source_id` cross-reference resolvable, URL syntax, aggregates flagged, *not searched*
distinguished from *no source found*, the eight-lead cap respected, and all 14 original
indicator IDs still present. It reports **all checks passed**. The coordinator's
`check_dsit.py` was re-run unchanged against an independent download.

A live reachability check of all 31 register URLs returned HTTP 200 for 24. Seven are
documented non-200s: the NIA notice page rejects `HEAD` (503/403) although `GET` works and
was used; `openai.com/signals/data-download/`, the GESIS Eurobarometer page and the Ofcom
PDF return 403 to automated requests; Eurofound returns 429.

## 3. Task-by-task completion

| Required work | Status |
|---|---|
| 1. Address every pilot-review issue | **Complete.** Eight items, each resolved / qualified / recorded as a blocker in `pilot-corrections.md`. The 2025 questionnaire version is verified; the legal-basis citation is withdrawn; no cause is claimed for C2. |
| 2. Assess 14 existing candidates plus the four named additional sources | **Complete at the depth the evidence allowed.** All 14 original IDs carry a dated disposition; the four named additions (Brazil Cetic, Canada CSWC, Melbourne/KPMG, Pew global) are audited, two of them to file level. File checks, documentation checks and published findings are kept in separate `evidence_level` values. |
| 3. Bounded regional search with exact queries and routes | **Complete.** 19 dated rows in `search-log.csv` covering Europe, North America, Latin America, Africa, Asia (East/Southeast), Oceania and West Asia/North Africa explicitly, plus the platform and modelled-exposure sources. Eight lead slots used in total: six carried from the coordinator's `SCOUT.md`, two new (Japan MIC, Mexico ENIAG). |
| 4. Prioritise usable non-European adoption evidence, Brazil and Canada first; assess multi-country country-by-gender availability | **Complete.** Brazil file-verified; Canada verified as two distinct published sources; Korea added as a third non-European module; both multi-country studies assessed and found to lack usable country-by-gender outcome cells. |
| 5. Proposed inclusion list and exact permitted cells | **Complete.** `v1-inclusion.md` and 15 rows in `permitted-cells.csv`, with evidence cards (Tier 3) for everything unresolved. |

## 4. Key limitations

1. **Four sources remain access-blocked or reuse-restricted after one documented route
   plus an alternative:** ISSP release ZA10020 (GESIS 403, fourth consecutive failure),
   EWCS 2024 (Eurofound 429 twice; UK Data Service catalogue is a script shell), OpenAI
   Signals (three URLs, all 403), RPS (replication-only terms; no owner contact made or
   authorised).
2. **Korea's reuse position is unresolved.** NIA asserts report copyright and no open
   licence was found in the English volumes. Published numbers may be quoted with
   attribution; republishing the tables needs a terms check.
3. **Brazil has two licence statements** on the provider's own pages (CC BY 4.0 at file
   level, CC BY-SA 4.0 on the indicator pages). The file-level statement should govern, but
   this needs a human decision before publication.
4. **Australia is still without a verified gender cell.** The dashboard would supply one
   but requires accepting provider terms, which this assignment forbids.
5. **The Eurostat C2 residual is unexplained**, because the country-specific notes are on
   CIRCABC (404 to two routes) and the compilers' manual exists only for the 2024 survey.
   No national routing explanation may be offered.
6. **No usable uncertainty accompanies most displayed cells**, and none at all for any
   male−female *difference* except through Brazil's published margins — which are per-cell,
   not difference-level. For the UK this is an unresolved location question rather than an
   absence (see finding 2).
7. **Mexico's ENIAG lead rests on secondary coverage only.** The primary publication was
   not located; it is recorded as a queued lead, not evidence.
8. **Language coverage is partial.** Japanese and Portuguese provider documents were read;
   Korean was read only in the provider's own English volumes; Arabic was not searched at
   all. The West Asia and North Africa entries are therefore *searched in English (and
   French for Morocco) without result*, which is not an absence of data.
9. **Not searched remains large and is labelled as such:** the Caribbean, Pacific islands,
   Central Asia, South Asia, most of Southeast Asia, China, most of sub-Saharan Africa, most
   of North Africa and the non-EU European east.
10. **Memory stores are mounted read-only in this session**, so the durable findings live in
    these files rather than in the research journal. A session with write access may wish to
    record: the Korea file-download route (notice page as referer), the Brazil
    margin-of-error workbook, the Brazil multiple-response non-use contrast with Eurostat's
    single main reason, and the Eurostat ESMS legal-basis inconsistency.

## 5. Recommended v1 scope

Adopt the pilot's option (B) in a sharper form, now backed by files rather than leads:

> **An international evidence map of source-specific modules.** Four file-verified modules —
> the European harmonised core (35 countries plus two aggregates, clearly labelled), the
> United Kingdom, Brazil and the Republic of Korea — displayed one panel per source with
> denominator, definition, period, gender categories and uncertainty attached. Five
> attributed published findings alongside (Canada twice, the United States, the 37-country
> attitudes study, the 47-country workplace null). Coverage gaps shown as three distinct
> states: verified, searched without result, not searched.

Explicitly **not** recommended: any pooled or world rate, any cross-country ranking, any
trend, any composite, any world-population coverage percentage, and any presentation that
places attitudes, platform messages or modelled occupational exposure beside measured use.

## 6. Remaining work, in priority order

1. Resolve the Korean reuse terms and the Brazilian licence choice — both are decisions, not
   research. In the same pass, find where the DSIT 95% logit intervals are published
   (remaining PES workbooks or an accompanying product), or record the question for the
   producer.
2. Extract Korean printed table 134 (and 113+ if purposes are wanted) to complete those
   indicators.
3. Pin the Canadian cells to StatCan table identifiers instead of article prose.
4. Retry Eurofound and GESIS outside rate-limit windows; decide whether access-gated
   European worker sources are worth a separate authorised acquisition.
5. Download the Japanese white-paper figure data and the e-Stat Communications Usage Trend
   Survey tables to settle whether Japan has a sex-disaggregated generative-AI item.
6. Locate the primary Mexican ENIAG publication.
7. Decide whether to seek an authorised route to the ADII dashboard gender cells.
8. Arabic-language searching for West Asia and North Africa, and national-statistics
   searching for the large *not searched* blocks, if coverage breadth matters more than
   depth.

## 7. Boundaries observed

No source owner was contacted; no registration, account creation, terms acceptance or
purchase was made; the ADII dashboard's agreement click was deliberately not performed. No
access control was bypassed; blocked routes are reported as blocked. No respondent-level or
restricted data were downloaded, and none exist in the aggregates used. No credentials
appear in any file. No model or agent configuration was changed and no subagent was
spawned. Nothing outside
`programme/gender-index/evidence/v1-audit-2026-10-01/` was created or modified.

## 8. Session and spend

Existing data steward v3, launched from the coordinator's confirmed launch commit on
branch `work/index-v1-source-audit-2026-10-01`; configured model unchanged. The user
envelope is $40 with a $36 service limit; the authoritative spend figure is the service
ledger's, which this session cannot read, and the coordinator records it in
`team/RUNS.csv`. Work was stopped at task completion, not at the cap, and no additional
session, delegation or budget increase was requested or used.
