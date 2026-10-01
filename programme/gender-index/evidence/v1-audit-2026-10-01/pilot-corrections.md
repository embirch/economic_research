# Pilot corrections: disposition of the coordinator review

> Coordinator integration note, 1 October 2026: preserved specialist submission. The [reviewed disposition](../../landscape-v1/coordination/source-audit-review.md) qualifies claims and governs v1 inclusion.

Data steward, 1 October 2026. Branch `work/index-v1-source-audit-2026-10-01`.
Assignment: `team/assignments/2026-10-01-v1-steward.md`.
Reviewed document: [`../../reviews/2026-10-01-pilot-review.md`](../../reviews/2026-10-01-pilot-review.md)
(coordinator review of steward commit `4b3b8a9`).

This file gives each of the eight review items one of three dispositions:
**resolved with source evidence**, **claim qualified or withdrawn**, or **unresolved
blocker**. Nothing in the pilot directory is edited or deleted: the pilot report and
profile stay as submitted, and the corrections below are what should be carried into the
register and into any v1 presentation. No article file was read or changed.

Retrieval dates are 1 October 2026 unless stated. Downloads went to ignored local
scratch (`/tmp/v1audit/`); only hashes, code and written evidence are committed.

---

## 1. Worldwide representation — **claim withdrawn and replaced**

The pilot report's phrase “one genuinely global, population-representative,
gender-disaggregated source” (§1 headline, §2.1, §3C) must not be used. Replacement
wording, supported by the publisher's own methods page:

> Pew Research Center's Spring 2026 Global Attitudes Survey covers 36 countries plus
> the United States, each with a sample designed to represent that country's adult
> population. It is a 37-country study of **AI attitudes and expectations**, not a
> measure of generative-AI adoption, and it is not a sample of the world population.

Country-by-gender availability is now audited (item 2 and
[`profiles/pew-global-and-us.md`](profiles/pew-global-and-us.md)): per-country gender
cells are **not** published for every item. The appendix detailed tables are by age,
education and income; gender appears in the narrative and in a chart that shows only
statistically significant differences (11 countries for the “fewer jobs” item). Any v1
use of Pew gender material is therefore a quotation of selected published differences,
not a country-by-gender matrix.

## 2. Pew sample and fieldwork — **resolved with source evidence**

Verified from the primary report page
<https://www.pewresearch.org/global/2026/09/17/globally-more-people-expect-ai-to-cause-job-loss-than-growth/>
and its methodology page `.../methodology-global-ai-2026/`:

- 42,151 respondents across **36 countries**, fieldwork **8 February – 13 May 2026**.
- US results come from **two separate American Trends Panel surveys**: 5,119 adults
  17–23 February 2026 (W187) and 3,488 adults 22–28 June 2026 (W195).
- The non-US sample total and the February–May window must not be attached to the whole
  37-country report, and the US figures must carry their own wave and dates.
- The report measures expectations and concern about AI, awareness of AI and trust in
  regulators. It contains no generative-AI adoption rate.

The separate US gender report (`PEW_GENDER`) is confirmed as **ATP Wave 187**, fieldwork
17–23 February 2026, 5,119 respondents, published 17 June 2026 — the wave number the
pilot could not confirm is now evidenced on the methodology page. The two Pew records
share family `PEW_ATP_W187` for the February wave and must not be counted twice.

## 3. European country count, readiness and world-population share — **corrected**

- Counts re-read from the files downloaded today (hashes identical to the pilot's, §7):
  `isoc_ai_iaiu` has **37 `geo` codes = 2 aggregates (EU27_2020, EA) + 35
  countries/territories**; `isoc_ai_iaiuxr` has **38 = 2 aggregates + 36
  countries/territories** (adds ME). Write it that way; never “EU27 + 35–36 countries”,
  which double-counts the EU27 members inside the country list.
- “Instrument-identical” is withdrawn. Correct description: a **harmonised EU model
  questionnaire** (2025 edition, item B5/B6/B7) implemented by national statistical
  institutes, whose national questionnaires, survey vehicles, fieldwork timing and
  routing may differ. Eurostat's own metadata (ESMS §15.1) warns that results for some
  countries may be of reduced comparability for exactly these reasons.
- “Roughly 6% of world population” is **removed**. No world-population denominator was
  verified, and none should be published until eligible country data and matching
  population denominators are both checked.
- Blanket “ready for release” is replaced by the conditional verdicts in
  [`v1-inclusion.md`](v1-inclusion.md).

## 4. Survey-wave documentation — **resolved; the inconsistency is in the source**

The pilot cited Commission Implementing Regulation (EU) 2025/1322 as the 2025-wave
basis. The coordinator was right to challenge it:

- EUR-Lex's own title for that act (ELI `reg_impl/2025/1322`, OJ L, 2025/1322,
  9 July 2025) specifies the data set **for reference year 2026**, with reference period
  Q1 2026 and fieldwork in Q2 2026.
- The Eurostat ESMS page `isoc_i_esms` cites the same act number but with the words
  “for reference year **2025**”, and separately says “the new legal basis for the 2025 EU
  survey … as implemented by Commission Implementing Regulation (EU) 2025/1322 of 4 July
  2025”. The corresponding 2025-reference-year act is a distinct, earlier implementing
  regulation whose draft is on EUR-Lex as `PI_COM:Ares(2024)3093436` (reference period
  Q1 2025, fieldwork Q2 2025, quality report due 5 January 2026).
- **Disposition:** the ESMS citation conflates two annual acts. Do not cite 2025/1322 as
  the legal basis of the 2025 wave. Cite the instrument actually verified for the 2025
  wave — the **ICT Survey Model Questionnaire 2025** annex — and record the legal-basis
  reference as unresolved in the source documentation.

**Routing and denominator claims are nevertheless safe to accept**, because they rest on
the questionnaire, not on the regulation. The annex PDF re-downloaded today is
byte-identical to the pilot's (SHA-256
`2f556a1c7a96d8dfc9a310937f3b18927fd6a4b1e50d25c996fe84a0b45643ac`), its front matter
reads “EU survey on the use of ICT in households and by individuals **2025** — Model
questionnaire … Coverage 2025 … ICT-HH_IND 2025 Model Questionnaire_v.1.3_final”, and it
contains B5 (tick one), B6 (tick all that apply) and B7 (“main reason”, tick one) with
the routing the pilot described. Item **H2 Sex** offers Male and Female only.

National notes were sought and **not obtained** (item 5), so country-level routing
deviations remain undocumented here.

## 5. Uncertainty, residuals and C2 — **narrowed; cause not claimed; blocker recorded**

- Narrowed wording, verified in the ESMS text today: “ESMS §13.2 states that national
  institutes supply Eurostat with estimated standard errors for the e-commerce indicator
  (ordering goods or services online in the last 12 months) only. **No sampling error is
  available in the inspected Eurostat tables or reference metadata for any
  generative-AI rate or for a male−female difference.**” National precision publications
  were not audited and may exist; that is now stated as unknown, not as absence.
- The ~1% shortfall in the non-use reason totals is described as a **residual consistent
  with** a single-response item plus item non-response. Item non-response is no longer
  asserted as the explanation.
- **C2 remains an unresolved blocker, with no cause claimed.** The published
  `PC_IND_IUAIX` base cannot be reconstructed from the use table (up to 6.52 pp, confined
  to BE, SE, NO, LU). Two routes to the documentation that would explain it were tried
  and failed: the ESMS “Country specific notes” CIRCABC library
  (`circabc.europa.eu/ui/group/4f80b004-…/library/0581a1a1-…`, HTTP 404 to the UI URL and
  to the node API) and the European compilers' manual, which is published only for the
  **2024 survey** (KS-01-25-011, 24 April 2025) and therefore predates the generative-AI
  module. Consequence for v1: use the published non-user base cells, do not reconstruct
  them, and do not offer a routing explanation.
- ESMS §16 (Cost and Burden) additionally documents the 2025 EU sample size — about 172,000 households and
  330,000 individuals aged 16–74 — which is a scale statement, not a per-country sample
  size and not a basis for deriving standard errors.

## 6. Reuse scope — **qualified**

The Eurostat copyright notice (retrieved today) authorises commercial and non-commercial
re-use with source acknowledgement, no written licence, and requires disclosure of
modification. The exclusion that matters here applies to data for countries other than
EU Member States, EFTA members and official EU acceding/candidate countries, for
**commercial** re-use. “Clear for re-use” is therefore replaced by:

> Non-commercial re-use of the full tables is unrestricted with attribution, DOI and
> access date. For any commercial product, the status of individual non-EU/EFTA
> geographies in the tables (including BA and XK) must be checked against the notice
> first; they do not share one status and were not resolved here.

## 7. Signals version — **resolved as “still v2.0 by the publisher's own label”, with a retrieval limit**

Direct HTTP requests to `openai.com/signals/`, `/signals/data-download/` and
`/signals/data/` returned **HTTP 403** to this session (user-agent set; three distinct
URLs). The publisher page text was obtained instead through the search index on
1 October 2026, and it still carries the suggested citation **“OpenAI Signals v2.0”**
with a data dictionary labelled README version 1.1, data described as a sample of
messages **July 2024 – June 2026**, and a **CC BY 4.0** licence. The May 2026 hub entry
is a data update within that release, not evidence of a superseded bundle.

Disposition: the prior bundle is **not shown to be superseded**; the pilot's inference in
either direction is withdrawn. Status for v1 is **documentation-only, not file-verified
in this audit**, because no file could be downloaded. Signals remains message-level with
**name-associated** gender categories (“traditionally masculine / traditionally feminine
names”, other names excluded) and differential-privacy noise; it is not a population
survey and cannot carry a sex/gender rate for people.

## 8. Exploratory work, code limits and discovery counts — **corrected**

- The pilot report's absolute claim that no gap arithmetic was produced is replaced by
  the disclosure the review asked for: exploratory gap arithmetic was performed during
  verification and **none of it is an approved index result**.
- `pilot-2026-10-01/checks.py` stays what it is: a diagnostic for one single-year
  snapshot that skips the header, prints residuals and enforces no acceptance threshold.
  It is **not a maintained pipeline**. Before it becomes one it needs explicit schema,
  period and duplicate-key validation. This audit did not re-run it (the review already
  reproduced C1–C3) and did not modify it.
- Counting is restated so the categories cannot be mixed:
  **14 original indicator rows** = 3 file-verified (the Eurostat family, one sample
  family `EU_ICT_2025`) + 4 given fresh documentation checks + 7 carried forward in the
  pilot. The pilot's coverage CSV additionally contains one synthesis row
  (`CRANNEY_SYNTHESIS`, a source-finding tool, not an indicator) and four discovery
  leads. Unique **source families** are counted separately in
  [`coverage.csv`](coverage.csv).
- Regional “nothing” is written as **“no verified sex-disaggregated generative-AI
  adoption indicator was found in this bounded, dated search”**, never as an absence of
  data in that region. `coverage.csv` separates *no source found in a dated search* from
  *not searched*.

---

## Status summary

| Review item | Disposition |
|---|---|
| 1 Worldwide representation | Claim withdrawn; replacement wording supplied; Pew gender-cell availability audited |
| 2 Pew sample/fieldwork | Resolved with source evidence; ATP W187/W195 confirmed |
| 3 Country count, readiness, 6% figure | Corrected; counts re-verified from the files; figure removed |
| 4 Survey-wave documentation | Resolved: source inconsistency identified; 2025 questionnaire verified; legal-basis citation withdrawn |
| 5 Uncertainty, residual, C2 | Narrowed; no cause claimed; **unresolved blocker** on national/country-specific notes |
| 6 Reuse scope | Qualified; commercial exclusion carried into the register |
| 7 Signals version | Resolved as publisher-labelled v2.0; **direct download blocked (403)**, documentation-only |
| 8 Exploratory work, code, counts | Corrected and disclosed |
