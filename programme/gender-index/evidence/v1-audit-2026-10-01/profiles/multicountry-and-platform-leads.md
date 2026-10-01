# Source profile: multi-country and platform leads assessed for country-by-gender cells

> Coordinator integration note, 1 October 2026: preserved specialist submission. The [reviewed disposition](../../../landscape-v1/coordination/source-audit-review.md) qualifies claims and governs v1 inclusion.

Data steward, 1 October 2026. One file for the leads whose decisive question is the same:
*do country-by-gender outcome cells actually exist, and may they be reused?* Each entry
states what was verified today, what is still unknown and the disposition for v1.

---

## 1. University of Melbourne / KPMG, *Trust, attitudes and use of AI: A global study 2025* (`MELB_KPMG_TRUST`)

**File-level check of the published report PDF** (<https://mbs.edu/-/media/PDF/Research/Trust_in_AI_Report.pdf>,
retrieved 2026-10-01; 5,498,658 bytes; 27-page PDF object containing the full report).

| Item | Verified value |
|---|---|
| Sample | **48,340 respondents across 47 countries and jurisdictions**; per-country n between **1,001 and 1,098** |
| Mode and dates | **Online survey, November 2024 – mid-January 2025**, in national languages with an English option |
| Representativeness | Samples described as nationally representative on **age, gender and regional location within a 5% margin** against official national statistics, with stated exceptions; Appendix 2 documents difficulty reaching over-65s in eight countries and over-representation of university-educated respondents in emerging economies |
| AI definition | An OECD-derived general AI definition, then respondents are **randomly allocated** to one of four framings: generative AI, healthcare AI, HR AI, or AI systems in general |
| Gender in the published report | **Composition only** (Appendix 2 prints % women / % men / % other reported genders per country) plus a global statement in the workplace section that there are **no gender differences in AI use or attitudes toward AI at work** |
| Country tables | Appendix 3 prints country-level key indicators (trust, acceptance, benefits, risks, AI knowledge, training) — **with no gender split** |
| Third-category coverage | A footnote records that other-gender and non-binary options were **not offered in some countries** “due to cultural sensitivities” (UAE and Saudi Arabia are flagged with `0*`) |
| Licence | **CC BY-NC-SA 4.0**, non-commercial only, share-alike; DOI 10.26188/28822919 |

**Disposition: no usable country-by-gender outcome cells.** Two further problems would
remain even if cells existed: the random allocation means the generative-AI framing is
seen by roughly a quarter of each country's ~1,050 respondents (≈250, so ≈125 per sex),
and the sample is an online panel, not a probability sample. The report's **global null
finding on gender at work** can be quoted as an attributed published finding, with the
design, the construct (“AI at work”, not generative AI specifically) and the missing
third category stated. Non-binary coverage varies by country by design, which must be
disclosed rather than averaged away.

---

## 2. Australian Digital Inclusion Index 2025 / Australian Internet Usage Survey (`AU_ADII_GENAI`)

**Report verified** (<https://digitalinclusionindex.org.au/wp-content/uploads/2025/10/ADII-Report-2025_V6-Remediated.pdf>,
retrieved 2026-10-01; 4,946,520 bytes). The GenAI case study publishes: 45.6% of
Australians recently used a generative-AI tool; breakdowns by **age** (69.1% of 18–34 vs
15.5% of 65–74), language spoken at home, disability, education, occupation (professionals
67.9%, managers 52.2%) and remoteness; plus types of use among recent users (text 82.6%,
images 41.5%, code 19.9%). Data year is **2024** (Australian Internet Usage Survey 2024),
report year 2025.

**No generative-AI cell by gender is published in the report.** Gender appears in the
report only in the remote-work case study (39.1% of males and 31.6% of females doing some
work from home every workday).

The provider's dashboard (<https://dashboard.digitalinclusionindex.org.au/GenerativeAI.aspx>)
does expose a gender filter, but the landing page requires clicking “agree” to a
citation/licence undertaking before the data are shown. **This audit did not click it**:
accepting terms is outside the assignment's permissions. Alternative route tried: the
report PDF (above) and the index site's own pages (`/the-index/` returned HTTP 404).

**Disposition: documentation-only.** Licence is **CC BY-NC-SA 4.0** with a prescribed
citation. A gender cell for Australia is plausibly obtainable but requires either an
authorised terms acceptance or a provider-published table; until then Australia has
**no verified sex-disaggregated generative-AI cell** in this audit.

---

## 3. OpenAI Signals (`SIGNALS_TOPIC`)

Direct requests to `openai.com/signals/`, `/signals/data-download/` and `/signals/data/`
returned **HTTP 403** to this session. Publisher page content retrieved through the search
index on 2026-10-01 establishes: suggested citation **“OpenAI Signals v2.0”**; data
dictionary **README version 1.1**; coverage described as a sample of individual ChatGPT
messages **July 2024 – June 2026** (Free, Go, Plus, Pro accounts; excludes enterprise and
Codex); **CC BY 4.0** licence; differential-privacy noise with a stated budget; and the
gender figure defined as the share of messages sent by users with **“traditionally
masculine” or “traditionally feminine” names**, excluding names that are neither.

**Disposition: documentation-only, not file-verified in this audit; version not shown to
be superseded.** Signals counts **messages, not people**, and its gender variable is a
**name-based proxy**, never self-reported sex or gender. It cannot supply an adoption rate
for a population and must be displayed in a separate, clearly labelled platform panel if
used at all.

---

## 4. ILO refined index of occupational exposure (`ILO_EXPOSURE`)

The publication page (<https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure>,
retrieved 2026-10-01) confirms **ILO Working Paper 140, 20 May 2025**, and the method:
a representative sample of the 29,753 tasks in the **Polish** occupational classification,
a survey of 1,640 workers across 1-digit ISCO-08 groups yielding 52,558 task-automation
data points, plus Delphi rounds with international experts. The page offers **PDF and EPUB
only**: no country-year data series is linked. The ILOSTAT route
(`ilostat.ilo.org/topics/artificial-intelligence/`) returned **HTTP 403** to this session.

**Disposition: documentation-only; data series still not located.** Two routes attempted
(publication page, ILOSTAT topic page). Even when located, this is **modelled potential
exposure of occupations**, with sex entering only as the **sex composition of employment**;
it is not a measure of any individual's AI use, benefit or harm, and occupational sex
shares must never be used to infer an individual's gender.

---

## 5. Research ICT Africa, After Access gender comparative report (`RIA_AFTERACCESS_CONTEXT`)

Carried from the coordinator's log as **context only**: the provider describes digital
inclusion in seven sub-Saharan countries using 2022–23 surveys. No generative-AI use table
by sex has been established, and this audit did not re-attempt the provider's PDF (the
coordinator recorded a timeout and used an indexed summary). **Disposition: contextual
digital-access evidence, not an AI indicator.** Digital-access gaps may help interpret an
AI gap; they cannot stand in for one.
