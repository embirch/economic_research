# Source profile: Pew Research Center — global attitudes study and US gender report

Data steward, 1 October 2026. IDs `PEW_GENDER` (existing register row) and
`PEW_GLOBAL_ATT` (new, from the pilot's `LEAD_PEW_GLOBAL_AI_2026`).
Status: **documentation-verified from the publisher's own report, methodology and topline
pages**. No respondent-level file was obtained; Pew's dataset downloads require an
account, and no registration was made.

## Spring 2026 Global Attitudes Survey — AI module (`PEW_GLOBAL_ATT`)

| Item | Verified value |
|---|---|
| Report | *Globally, More People Expect AI to Cause Job Loss Than Growth*, published 17 September 2026 |
| Non-US samples | **42,151 respondents across 36 countries**, fieldwork **8 February – 13 May 2026**, each sample designed to represent that country's adult population |
| US samples | **two separate American Trends Panel surveys**: 5,119 adults 17–23 Feb 2026 (**W187**) and 3,488 adults 22–28 Jun 2026 (**W195**) |
| Construct | Expectations about AI's effect on jobs and on inequality, concern/excitement, AI awareness, trust in regulators. **Attitudes, not adoption or use** |
| Gender measure | Reported as men / women; no third category documented in the inspected pages |
| Country-by-gender availability | **Not published for every item.** The appendix detailed tables are by **age, education and household income**. Gender appears in narrative text and in a chart whose note reads “Only statistically significant differences are shown”; the gender finding is summarised as women being more likely than men to expect fewer jobs in **11 mostly high-income countries**, with France cited at 10 percentage points |
| Precision | The topline lists a margin of error at 95% per country; the gender subgroup cells that would be needed for a gender matrix are not themselves published with errors |
| Access / reuse | Report, topline and methodology are open PDFs/pages. Respondent-level data require a Pew account and acceptance of terms — **not attempted** |

**Consequence for v1.** This source can support a *global attitudes* module only, as
quoted published findings (for example “women are more likely than men to expect AI to
reduce jobs in 11 of the 37 countries surveyed, including a 10-point difference in
France”). It cannot populate a country-by-gender attitudes matrix, and it must never be
placed beside Eurostat, Brazilian, Korean, UK or Canadian **use** rates as if they
measured the same thing.

## Americans and AI 2026 (`PEW_GENDER`)

| Item | Verified value |
|---|---|
| Report | *Americans and AI 2026: Chatbots, Smart Devices and Views on Impact*, published 17 June 2026, with a dedicated “gender gap in AI” section |
| Sample | **American Trends Panel Wave 187**, fieldwork **17–23 February 2026**, **5,119** panellists responding out of 5,854 sampled; online (n=4,930) and live telephone (n=189) by SSRS; English and Spanish; oversample of non-Hispanic Asian adults weighted back |
| Population | US adults |
| Construct | Ever-use and frequency of chatbot use (for example ever use ChatGPT), purposes, perceived helpfulness, confidence, awareness and attitudes |
| Register correction | The register's “confirm wave/sample” is now resolved: the wave number is **187**, stated on the methodology page |
| Sample-family note | W187 is the **same wave** that supplies the US February data in the global report. The two Pew records share that sample and are not independent evidence |

**Estimand incompatibility.** “Ever use ChatGPT” (US) and “used generative AI in the last
three months” (Eurostat) are different estimands with different reference windows; the
pilot's warning stands and is reinforced by the wave overlap above.

## Retrieval record

Pages and files retrieved 2026-10-01: the two report pages, both methodology pages, both
topline PDFs, the global appendix page, and the global report PDF
(`pg_2026.09.17_global-views-of-ai_report.pdf`, 1,329,590 bytes). Downloads are in
ignored scratch and are not committed.

## Open items

1. If a US gender indicator is wanted with uncertainty, read the W187 topline's
   per-question bases and the stated margin of error rather than inferring precision.
2. Treat any ATP microdata route as a separate decision: it needs an account and terms
   acceptance, which this assignment does not authorise.
