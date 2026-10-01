# Source profile: Korea, 2025 Survey on the Internet Usage (NIA)

> Coordinator integration note, 1 October 2026: preserved specialist submission. The [reviewed disposition](../../../landscape-v1/coordination/source-audit-review.md) qualifies claims and governs v1 inclusion.

Data steward, 1 October 2026. Proposed IDs `KR_NIA_USE`, `KR_NIA_SERVICE`,
`KR_NIA_NONUSE`; sample family **`KR_NIA_INTERNET_2025`**.
Status: **file-verified published aggregates** (English statistical-table volume) plus
the English final report's design documentation. No respondent microdata exists in these
products and none was sought.

This resolves the coordinator's queued lead (`SCOUT.md`, “English-table web download
failed … catalogue access is not data verification”). The English table volume **was**
retrieved in this audit by requesting the board's file-download endpoint with the notice
page as referer.

## Provider, design and dates

| Item | Verified value |
|---|---|
| Survey | 2025 Survey on the Internet Usage (인터넷이용실태조사) |
| Host / specialised agency / fieldwork | Ministry of Science and ICT / National Information Society Agency (NIA) / Gallup Korea |
| Legal basis | Article 18 of the Statistics Act (approval for production of statistics); Framework Act on Intelligent Informatization Arts. 12 and 66 — i.e. **approved national statistics** |
| Target population | Households nationwide and the resident population **aged 3 and over** as of 1 July 2025; military personnel, long-term overseas residents, dormitory residents and inmates excluded |
| Sample | 22,500 households targeted; **valid 22,691 households and 50,750 household members aged 3+**; all members aged 3+ in a selected household are enumerated |
| Sampling | Stratified multi-stage cluster sampling; PSU = enumeration districts stratified by region, administrative division and housing type; frame = 2023 Register-based Census microdata (MDIS) |
| Mode | In-home face-to-face interview (tablet-assisted) |
| Fieldwork | **17 October – 12 December 2025**; **reference date 1 July 2025** |
| Estimation | Post-stratification against 2025 household and population projections |
| Published precision | Survey-level only: internet access rate ±0.01 pp and internet usage rate ±0.19 pp at 95%. **No table-level or subgroup standard error is published**, including none for the generative-AI tables |

## The generative-AI tables

Module Q26 in the household-member questionnaire. Reference period for all of them is
**“within the last 1 year”** — not three months.

| Printed table | Construct | Base (denominator) | Response type |
|---|---|---|---|
| 105 | Generative-AI service experience status (experience rate) | internet users aged 12+ (used internet within the last year) | single response |
| 106 | Which services were experienced (ChatGPT, Gemini, Copilot, CLOVA X, other, not experienced) | internet users aged 12+ | **multiple response** |
| 107–112 | Paid-subscription conversion, overall and by service | experienced users | single response |
| 113–122 | Purpose of use, per service | experienced users of that service | **multiple response** |
| 123–132 | Satisfaction, per service | experienced users of that service | scale |
| 133–134 | Reasons for not using | internet users aged 12+ **not** experienced | multi-column, continues in table 134 |

## Verified published cells (sex rows)

From [`../checks/korea-published-cells.json`](../checks/korea-published-cells.json),
produced by [`../checks/check_korea.py`](../checks/check_korea.py):

| Table | Cell | Male | Female |
|---|---|---|---|
| 105 | experienced a generative-AI service in the last year (%) | 48.7 | 40.3 |
| 105 | not experienced (%) | 51.3 | 59.7 |
| 106 | ChatGPT (%) | 45.5 | 38.0 |
| 106 | Gemini (%) | 11.5 | 8.1 |
| 106 | Copilot (%) | 2.5 | 1.8 |
| 106 | CLOVA X (%) | 2.3 | 1.7 |
| 133 | no interest / not needed (%) | 50.6 | 48.4 |
| 133 | do not know how to use it (%) | 16.8 | 19.9 |
| 133 | did not know such a service exists (%) | 15.7 | 16.4 |

Published all-internet-user totals for table 105 are 44.5% experienced / 55.5% not.

**This is the only audited source that publishes a sex × age crossing of a
generative-AI rate.** Table 105 prints a `Gender*Age` block (Male and Female × 12–19,
20s, 30s, 40s, 50s, 60s, 70+), for example male 20s 76.5% and female 20s 73.9%, male 50s
38.8% and female 50s 28.4%. The same volume also prints occupation rows, but those are
**not** crossed with sex, so no sex × occupation cell exists here either.

Table 133's three columns do not exhaust the base (49.5 + 18.5 + 16.1 = 84.1 for the
total row); further reason columns continue in printed table 134, which this audit did
not extract. Do not treat the three extracted columns as a complete reason distribution.

## Sex/gender measurement

The volume reports a two-category **Gender: Male / Female** breakdown. The English report
does not document a third category or a separate gender-identity item. Treat these as the
survey's recorded sex categories, as with Eurostat, and do not relabel them as a full
gender measure.

## Access and reuse

- The notice page and both PDFs are public and need no registration. Direct automated
  retrieval of the file links works when the notice page is sent as referer; a plain
  request to the English-table link had previously failed for the coordinator.
- The English report states that **copyright in the report is owned by NIA** and that
  unauthorised reproduction is restricted. No open-licence statement (for example KOGL)
  was found in the inspected English volumes.
- **Disposition:** published numbers may be quoted with attribution as published
  statistics; bulk re-publication of the tables, or a derived table presented as a
  reusable dataset, needs a licence check first. That check requires reading the Korean
  portal's terms page and is **not done** here, so the register records redistribution
  as unresolved.

## Provenance of retrieved files (ignored scratch, not committed)

| File | Bytes | SHA-256 |
|---|---:|---|
| `2025_인터넷이용실태조사_통계표(영문).pdf` (statistical tables) | 4,815,170 | `12ec5ffec2596bed3162f671231ca3b166f2137031b76095f720d763a988bc00` |
| `2025_인터넷이용실태조사_보고서(영문).pdf` (final report) | 46,515,597 | `70ecc9022000fdebced4fc626289688cbf8c3a4a67326fb0e015a812fa98a1d3` |

Notice page: <https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?bcIdx=29580&cbIdx=99870>
(posted 25 June 2026), file endpoints `…/common/board/Download.do?bcIdx=29580&cbIdx=99870&fileNo=1|2`,
retrieved 2026-10-01.

## Comparability verdict

Strong national module: probability sample, official statistics, face-to-face mode, large
achieved sample, and sex × age cells. **Not comparable with Eurostat**: a one-year
reference window instead of three months, a base of internet users aged 12+ instead of
all individuals or recent internet users aged 16–74, service-named prompts (ChatGPT,
Gemini, Copilot, CLOVA X) instead of a generic generative-AI definition, and a July 2025
reference date with autumn fieldwork. Present separately with its definitions attached.

## Open items

1. Resolve the reuse/licence position for republishing table cells.
2. Extract printed table 134 to complete the non-use reason set, and tables 113+ if
   purposes are wanted (they are per-service, not a single purpose question).
3. Confirm whether KOSIS/e-나라지표 publishes the same cells in a machine-readable form
   with an explicit open licence.
