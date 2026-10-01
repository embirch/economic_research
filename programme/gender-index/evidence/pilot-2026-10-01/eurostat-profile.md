# Eurostat source profile: EU_USE, EU_PURPOSE, EU_NONUSE

Data-steward pilot, 1 October 2026. Branch `work/index-steward-pilot-2026-10-01`.
Assignment: `team/assignments/2026-10-01-steward-pilot.md`. Register: [`../indicators.csv`](../indicators.csv).

This profile is a **new, dated verification** performed on 1 October 2026 against Eurostat's
primary dissemination API and primary provider documentation. It supersedes nothing in the
existing audits; it adds a dated check beside them. Earlier statements carried in
`concept-and-feasibility.md` (30 September 2026) are labelled *prior* below where they differ.

It does **not** rely on `posts/gender1/`, and it does not touch, rewrite or re-scope the
authoritative manuscript in `gender-gap-generative-ai`.

---

## 1. Scope of what was verified

| Verified by me, 2026-10-01 | Not verified by me |
|---|---|
| Both Eurostat tables downloaded from the primary API; SHA-256 recorded | The article's frozen `data/raw/*.tsv` files and `outputs/validation/report.json` (repository not mounted; token has no access) |
| Full dimension/code structure and labels from the primary JSON-stat endpoint | The article's four-hash validation result (coordinator re-ran it locally on 2026-10-01 and reports all four match; **supplied provenance, not my check**) |
| 2025 model questionnaire wording and routing (Eurostat ESMS annex) | National questionnaire translations and country-specific deviations |
| ESMS reference metadata (population, reference period, accuracy, release policy) | National quality reports / execution reports |
| Eurostat copyright and re-use notice | Microdata (scientific-use files); not requested, not needed for aggregates |
| Denominator arithmetic, flags and missingness, by reproducible script | Any sampling variance for a gender gap (none is published — see §6) |

---

## 2. Table and measure identifiers

### 2.1 `isoc_ai_iaiu` — EU_USE and EU_PURPOSE

- Title: **Individuals - use of generative AI tools**
- DOI: `10.2908/ISOC_AI_IAIU` · dataset issued 2025-12-16 · data structure `ESTAT:ISOC_AI_IAIU v5.0`
- Last data dissemination timestamp: **2026-06-05T11:00:00+02:00**
- Databrowser: <https://ec.europa.eu/eurostat/databrowser/view/isoc_ai_iaiu/default/table?lang=en>
- Bulk TSV: <https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/isoc_ai_iaiu/?format=TSV&compressed=false>

### 2.2 `isoc_ai_iaiuxr` — EU_NONUSE

- Title: **Individuals - reasons for not using generative AI tools**
- DOI: `10.2908/ISOC_AI_IAIUXR` · created 2025-12-16 · data structure `ESTAT:ISOC_AI_IAIUXR v4.0`
- Last data dissemination timestamp: **2026-04-17T11:00:00+02:00**
- Bulk TSV: <https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/isoc_ai_iaiuxr/?format=TSV&compressed=false>

**Register correction.** The register's `source_url` for EU_NONUSE pointed at EIGE's gender
statistics mirror. EIGE's own page (retrieved 2026-10-01) states: source organisation *Eurostat*,
"Downloaded from Eurostat's online database as dataset isoc_ai_iaiuxr", imported **20.07.2026**,
"Number of values: 53280". The Eurostat table I downloaded on 2026-10-01 contains **54,825**
value cells. The 1,545-cell difference is unexplained and I did not resolve it. EIGE is therefore
a **secondary mirror of a possibly different extract**; the primary Eurostat table should be the
cited and used source. I have changed the EU_NONUSE `source_url` accordingly and kept the EIGE
link as a documented mirror.

### 2.3 Measure codes (`indic_is`)

`isoc_ai_iaiu`:

| Code | Label |
|---|---|
| `I_IUAI` | Use of generative AI tools: in the last 3 months |
| `I_IUAIPR` | Use of generative AI tools: for private purposes |
| `I_IUAIWP` | Use of generative AI tools: for professional (work) purposes |
| `I_IUAIFE` | Use of generative AI tools: for formal education |

`isoc_ai_iaiuxr`:

| Code | Label |
|---|---|
| `I_IUAIX_NUNN` | Reason for not using generative AI tools: No need |
| `I_IUAIX_NUUNK` | Reason for not using generative AI tools: Did not know they existed |
| `I_IUAIX_NUUSE` | Reason for not using generative AI tools: Did not know how to use |
| `I_IUAIX_NUSEC` | Reason for not using generative AI tools: Concerns about privacy, security, or safety |
| `I_IUAIX_NUOTH` | Reason for not using generative AI tools: Other |

### 2.4 Unit codes = denominators

| Code | Denominator | Present in |
|---|---|---|
| `PC_IND` | Percentage of individuals (all individuals in the survey population) | both tables, all measures |
| `PC_IND_IU3` | Percentage of individuals who used the internet in the last 3 months | both tables, all measures |
| `PC_IND_IUAI` | Percentage of individuals who have used any generative AI tools in the last 3 months | `isoc_ai_iaiu`, **purposes only** (not `I_IUAI`) |
| `PC_IND_IUAIX` | Percentage of individuals who have **not** used any generative AI tools in the last 3 months | `isoc_ai_iaiuxr` only |

The unit code *is* the denominator. Any indicator built from these tables must carry it.

---

## 3. Population, instrument, routing and the sex variable

Source: Eurostat ESMS reference metadata `isoc_i_esms` (metadata last updated 11 December 2025)
and the 2025 **Model Questionnaire** published as ESMS annex
`isoc_i_esms_an_ICT_Survey_Model_Questionnaire.pdf`
(SHA-256 `2f556a1c7a96d8dfc9a310937f3b18927fd6a4b1e50d25c996fe84a0b45643ac`, retrieved 2026-10-01).

- **Survey:** EU survey on the use of ICT in households and by individuals, annual since 2002.
- **Statistical population (individuals):** all individuals **aged 16 to 74**. Some countries
  optionally collect ages ≤15 and ≥75; the table's `Y0_15`, `Y75_89` and `*_75_89` codes are
  those optional extensions, **not** part of the standard population.
- **Reference period:** "In general, data refer to the **first quarter of the reference year**."
  National fieldwork timing varies; Eurostat flags this as a source of reduced geographical
  comparability.
- **Legal basis (2025 wave):** Regulation (EU) 2019/1700, implemented by Commission Implementing
  Regulation (EU) 2025/1322 of 4 July 2025.

### 3.1 Routing — verified from the model questionnaire

```
Module B (Use of the internet)
  B1  When did you last use the internet?   [filter]
      a) Within the last 3 months  -> B2 ... (continues to B5)
      b) 3 months–1 year ago       -> B10
      c) More than 1 year ago      -> B10
      d) Never used it             -> B10

  B5  Have you used any generative AI tools (e.g. ChatGPT, Copilot, Gemini, LLaMA,
      Midjourney, DALL-E) to create content like text, images, programming code,
      or videos in the last 3 months?          [tick one: Yes -> B6 / No -> B7]

  B6  (only if B5 = Yes)  What was the purpose ... ?   [TICK ALL THAT APPLY]
      a) private purposes   b) professional (work) purposes   c) formal education

  B7  (only if B5 = No)   What is the MAIN reason for not using ... ?   [TICK ONE]
      a) no need  b) didn't know they existed  c) didn't know how to use
      d) concerns about privacy, security, or safety  e) other
```

Three consequences that the register did not previously state:

1. **B5 is asked only of recent internet users.** `PC_IND` therefore counts every
   non-recent-internet-user in the denominator as a non-user of generative AI. That is a
   defensible population rate, but it mixes internet access with AI adoption. `PC_IND_IU3`
   isolates behaviour among recent internet users. Both must be shown or the choice stated.
2. **Purposes are multiple response** — they do not sum to 100%, and a person can appear in
   more than one purpose. The work-purpose cell is *not* restricted to workers: its denominator
   is all individuals (or all AI users), not the employed.
3. **Non-use reasons are single response: the one MAIN reason.** The register described
   "reasons … (plural)". This is a material correction. The five reasons are mutually exclusive
   and nearly exhaust the base: over the EU27 non-user base they sum to 99.10% (all individuals),
   99.14% (men 16–74) and 99.06% (women 16–74); the residual is non-response. Falling share of
   one reason mechanically raises another.

### 3.2 The sex/gender variable

- **There is no `sex` dimension.** Sex is encoded inside the `ind_type` ("Individual type")
  dimension as a prefix: 21 `M_*` codes and 21 `F_*` codes out of 104 total codes.
- The headline sex totals are **`M_Y16_74` ("Males, 16 to 74 years old")** and
  **`F_Y16_74` ("Females, 16 to 74 years old")**. There is no bare `M`/`F` code; code
  `IND_TOTAL` ("All individuals") is the overall total, not a sex category.
- Sex is crossed with age bands (16–19, 16–24, 16–29, 20–24, 25–29, 25–34, 25–54, 25–64, 35–44,
  45–54, 55–64, 55–74, 65–74, 75–89) and with education (low `I0_2`, medium `I3_4`, high `I5_8`,
  plus 75–89 education variants). **Sex is not crossed with occupation, activity status,
  degree of urbanisation or country of birth** in these tables — those `ind_type` codes
  (`ISCO*`, `EMPL_UNE`, `IND_DEG*`, `CB_*`, `CC_*`) are sex-neutral. Any
  sex × occupation or sex × employment-status analysis is **not** available from these aggregates.
- **Source measurement:** model questionnaire item **H2 "Sex"**, response options **Male** and
  **Female** only, collected in the socio-demographic module. There is no non-binary, "other" or
  self-described category, and no separate gender-identity item. These are *sex categories as
  recorded by the survey*, not a full gender measure; the absence of non-binary data is a
  coverage gap of the instrument, to be stated and not silently relabelled "gender".

*Note on the questionnaire annex:* the PDF's internal document properties read
`Status: Draft` and `Rights: Restricted access to members of the ISS WG`. It is nevertheless
published openly by Eurostat as a reference-metadata annex and is linked from `isoc_i_esms`.
I treat it as the public primary instrument document and quote only item identifiers and
question wording.

---

## 4. Countries and periods actually present

Verified from the downloaded files, 2026-10-01.

- **Time: 2025 only, in both tables.** One annual period. `freq = A`. **There is no time series,
  so no trend, convergence or change statement is available from these tables.**
- `isoc_ai_iaiu` — **37 `geo` codes**: 2 aggregates (`EU27_2020`, `EA`) + **35 countries/territories**:
  AL, AT, BA, BE, BG, CH, CY, CZ, DE, DK, EE, EL, ES, FI, FR, HR, HU, IE, IT, LT, LU, LV, MK, MT,
  NL, NO, PL, PT, RO, RS, SE, SI, SK, TR, XK.
- `isoc_ai_iaiuxr` — **38 `geo` codes**: the same plus **ME (Montenegro)**.
- **Iceland (IS) is absent from both**, although the ESMS reference area names Iceland. **Ireland
  (IE) is present.** The EU27 is complete in both tables.
- The register's EU_NONUSE geography field ("European coverage to verify") is now resolved:
  EU27_2020 + EA + 36 countries.
- Prior audit (September) recorded "35 country/territory codes plus the EU aggregate" for the use
  table. That is consistent; the `EA` aggregate is the second aggregate.

**Cell-availability result for the headline measure** (`I_IUAI`, `PC_IND`, `M_Y16_74` and
`F_Y16_74`): all 37 male and all 37 female cells are **present and unflagged**. Published EU27
values are 34.91% (men 16–74) and 30.45% (women 16–74), quoted here only to evidence that the
cells read correctly.

A coverage fact that any later measurement plan must handle: reading the published male and
female cells across the 37 geographies, **six geographies have a higher female than male rate**
(HR, LT, SI, EE, MT, MK). Negative gaps are real cells, not errors, and must not be clipped,
hidden or re-signed.

*No gap ranking, league table or effect estimate is produced or approved by this pilot.* Per the
coordinator's 1 October 2026 scope check, any gap arithmetic performed during verification is
exploratory and is **not** an approved index output; the estimand, inclusion rules and
uncertainty treatment belong to a later analysis plan. The article's own results, whose scope is
the 2025 EU27 core, are unaffected by anything here.

---

## 5. Reproducible checks performed

Script: [`checks.py`](checks.py). Run against the two TSVs downloaded as in §7.
Results, 2026-10-01:

| Check | What it tests | Result |
|---|---|---|
| **C1** | `PC_IND_IUAI` purpose cell = 100 × purpose `PC_IND` ÷ use `PC_IND`, same `ind_type`/`geo` | 9,486 comparisons; **max abs. difference 0.96 pp**; only 1 case >0.6 pp (TR, `Y55_74LO`, `I_IUAIPR`, where the underlying values are 0.57/0.61 — rounding on tiny numbers). **Denominator semantics confirmed.** |
| **C2** | Non-use `PC_IND_IUAIX` base = (recent internet users) − (AI users), reconstructed from the use table | 6,510 comparisons over sex `ind_type`s; **max abs. difference 6.52 pp**; at headline `M_Y16_74`/`F_Y16_74` max **1.60 pp**. Only 42 cells exceed 1 pp, confined to **BE (20), SE (18), NO (2), LU (2)**. Within any single cell the base implied by all five reasons is consistent to ~0.1 pp, so the xr table is internally coherent; the gap is *between* tables. **Do not reconstruct the non-user base from the use table — use the published `PC_IND_IUAIX` cells.** Cause not established in this pilot. |
| **C3** | `PC_IND_IU3` cells consistent with the internet-user share implied by `I_IUAI` | 12,920 comparisons; **max abs. difference 0.019 pp**. Confirmed. |
| **C4** | The five non-use reasons are mutually exclusive and sum to ≈100% of the non-user base | EU27: 99.10% (all), 99.14% (M), 99.06% (F). Consistent with a single-response "main reason" item plus item non-response. |
| **C5** | Hash of the current `isoc_ai_iaiu.tsv` against the manuscript snapshot | **Identical** — see §7. |

Nothing was tuned to produce a match; C2's residual is reported as a discrepancy, not resolved.

---

## 6. Flags, missingness and uncertainty

Parsed from the TSV value/flag fields.

| | numeric, unflagged | numeric, flag `u` | `:` (not available) with `u` | total |
|---|---:|---:|---:|---:|
| `isoc_ai_iaiu` | 32,307 | 3,503 | 3,196 | 39,006 |
| `isoc_ai_iaiuxr` | 45,210 | 5,385 | 4,230 | 54,825 |

- **`u` is the only flag present in either table** (Eurostat: *low reliability*). There are no
  `p` (provisional), `e` (estimated), `b` (break), `d` (definition differs) or `c` (confidential)
  flags in these 2025 extracts.
- Roughly **8–9% of cells are unavailable and a further 9–10% are flagged low reliability.** This
  is concentrated in small `ind_type` cells (narrow age × education bands, small countries).
  Missing is **not zero**. Suppressed cells must stay missing in any derived table.
- For the headline comparison (`I_IUAI`, `PC_IND`, `M_Y16_74`/`F_Y16_74`) every one of the
  37 × 2 cells is present and unflagged. Precision degrades sharply for finer crossings.
- **No sampling errors are published for these indicators.** ESMS §13.2 states that national
  institutes supply estimated standard errors to Eurostat only for the e-commerce indicator
  ("individuals having ordered goods or services … over the internet in the last 12 months").
  Therefore:
  - there is **no published standard error, confidence interval or design effect** for a
    generative-AI rate, and none at all for a male−female difference;
  - a gap's sampling variance **cannot** be derived from the published aggregates, because the
    male and female estimates come from the same complex sample and their covariance is unknown;
  - **resident-population counts are not sample sizes** and must not be used to manufacture
    standard errors;
  - the honest statement for a first release is a descriptive gap with the `u` flag surfaced and
    an explicit "sampling uncertainty not quantifiable from published cells" note.
- **EU aggregate rule (ESMS §17.2):** EU aggregates are compiled when the available countries
  represent 60% of the population and 55% of the number of countries defining the aggregate.
  For 2025 the EU27 is in fact complete for the headline cells, but the rule means an aggregate
  is not automatically a full-coverage figure and must be rechecked per cell.
- **Revision policy:** revisions are not expected but unscheduled revisions occur; data may be
  published while some countries are missing or flagged, and are replaced when validated. A
  dated snapshot and hash are therefore necessary, not optional.

---

## 7. Provenance of the files I retrieved

Downloaded to ignored local scratch (`/tmp`), **not committed**. No respondent-level data exist
in these products; they are published aggregate cells.

| File | Retrieved (UTC) | Bytes | SHA-256 |
|---|---|---:|---|
| `isoc_ai_iaiu.tsv` | 2026-10-01T08:30:35Z | 1,560,775 | `7f668f7be9aaefaa5662ab2ab059875de8ccbe050c5c38a8de4b2c33a96896ab` |
| `isoc_ai_iaiuxr.tsv` | 2026-10-01T08:31:44Z | 2,483,018 | `8901c5c90b8661e23f609f406d59889efcbc740b09b8639ca9cea48b5eda8ef4` |
| `isoc_i_esms_an_ICT_Survey_Model_Questionnaire.pdf` | 2026-10-01T08:34Z | 999,470 | `2f556a1c7a96d8dfc9a310937f3b18927fd6a4b1e50d25c996fe84a0b45643ac` |
| `isoc_i_esms_an_Aggregated_variables_and_break.pdf` | 2026-10-01T08:34Z | 640,922 | `19c759b969102e50cda2ffd66cc11b4c9c5a8acfd8b30d2394f8e39099673ec0` |

### The key provenance result

The coordinator supplied the manuscript's frozen use-table hash:
`7f668f7be9aaefaa5662ab2ab059875de8ccbe050c5c38a8de4b2c33a96896ab`, retrieved
2026-09-21T15:13:28Z. **My independent download on 2026-10-01T08:30:35Z from the same URL is
byte-identical.** Eurostat's own dissemination timestamp for the table (2026-06-05) predates both
retrievals, which is consistent.

What this does and does not establish:

- It **does** establish that the manuscript's European foundation is currently reproducible from
  the live primary source, that no silent revision has occurred between 21 September and
  1 October 2026, and that the index can reuse the same vintage without re-freezing anything.
- It **does not** reproduce the article's four-hash source-validation report. I cannot read
  `data/raw/` or `outputs/validation/report.json`: the repository is not mounted in this session
  and the available token cannot reach it. I did not attempt to circumvent that boundary. The
  coordinator states (1 October 2026) that a local re-run matched all four hashes; that is
  **coordinator-supplied provenance**, recorded as such.
- It **does not** make the aggregate cells into joint respondent records. Published cells give
  marginal and some two-way crossings only; they do not support any analysis requiring the joint
  distribution of sex with occupation, employment status or country of birth.

---

## 8. Re-use and redistribution terms

Source: Eurostat *Copyright notice and free re-use of data*,
<https://ec.europa.eu/eurostat/web/main/help/copyright-notice>, retrieved 2026-10-01.

- **Editorial content** of the Eurostat website: Creative Commons **Attribution 4.0 International**.
- **Statistical data, metadata and publications:** re-use "for commercial or non-commercial
  purposes is authorised provided the source is acknowledged". **No written licence or special
  procedure is required.**
- **Modification must be disclosed:** where re-use involves modifications to the data or text,
  that must be stated clearly to the end user, together with a disclaimer that Eurostat is not
  responsible. A derived indicator table must therefore say it is derived.
- **Commercial-use exception that touches these tables:** data for countries other than EU Member
  States, EFTA Member States and official EU acceding and candidate countries may not be re-used
  commercially. Both tables include **BA** and **XK**, whose status against that wording should be
  confirmed before any *commercial* re-use; **non-commercial re-use is unrestricted**. The simple
  mitigation is to publish the full table non-commercially, or to exclude the affected rows from
  any commercial product.
- **Required citation form:** `Source: [DOI of the Eurostat dataset], [access date]`, with
  customised versions cited as customised. For us: `Source: 10.2908/ISOC_AI_IAIU, accessed
  1 October 2026` and `Source: 10.2908/ISOC_AI_IAIUXR, accessed 1 October 2026`.
- **Access status:** open bulk download, no registration. This is distinct from Eurostat
  **microdata** (scientific-use files), which run through a separate accredited-researcher route
  (ESMS §10.4) and were neither needed nor requested here.

**Verdict on terms:** the three Eurostat indicators are **clear for inclusion and for publishing
derived aggregates**, with attribution, a DOI + access date, and a statement of modification.
This is the strongest access position of any candidate in the register.

---

## 9. Verdicts

| Indicator | Verdict | Conditions |
|---|---|---|
| **EU_USE** | **Ready for bounded calculation.** | Use `I_IUAI`; state `PC_IND` vs `PC_IND_IU3`; sex via `M_Y16_74`/`F_Y16_74`; single year 2025; no trend claims; preserve six negative gaps; surface `u`; no gap standard errors. |
| **EU_PURPOSE** | **Ready for bounded calculation.** | Multiple-response; denominator must be stated (`PC_IND` or `PC_IND_IUAI`); work purpose is **not** restricted to workers; same sample family as EU_USE — never counted as independent evidence. |
| **EU_NONUSE** | **Ready for bounded calculation, with a corrected definition.** | It is the **single main reason**, not multiple reasons; base = recent internet users who did not use generative AI in the last 3 months; use published `PC_IND_IUAIX`, do not reconstruct it; reasons are not causal explanations of the adoption gap; geography includes ME, so it differs from EU_USE by one country. |

All three share sample family `EU_ICT_2025`. They are three views of one survey wave.

**Register rows updated** (EU_USE, EU_PURPOSE, EU_NONUSE only; `new_check_this_setup` kept
`false`, which continues to mean "the 30 September migration performed no check"):
geography resolved, denominators and routing corrected, gender measure specified, uncertainty
statement sharpened, EU_NONUSE primary URL repointed to Eurostat, `audit_record` extended to this
profile, `verification_status` set to file-verified on this date, and `next_check` rewritten.

---

## 10. Open items for a later assignment

1. **C2 residual.** Explain the up-to-6.5 pp difference between the published non-user base and
   the base reconstructed from the use table, confined to BE, SE, NO and LU. Likely candidates: a
   different national routing of B5/B7, or a different treatment of item non-response in the
   base. Check the ESMS "Variable specific notes" and country-specific notes annexes.
2. **EIGE cell-count difference** (53,280 vs 54,825). Resolve or drop the mirror.
3. **Aggregated-variables annex** (`isoc_i_esms_an_Aggregated_variables_and_break.pdf`, hash in
   §7) was downloaded but not yet parsed; it should confirm the official definition of each
   `ind_type` breakdown.
4. **2026 wave.** Eurostat's release target is December of the survey year. If a 2026 wave
   appears, it becomes a *new index edition*, never a silent refresh of the manuscript's inputs,
   and a break check (questionnaire, population, classification) is required before any series.
5. **Country-specific comparability notes** have not been read. ESMS §15.1 warns of translation,
   reference-period, survey-vehicle and routing differences. Needed before ranking countries.
