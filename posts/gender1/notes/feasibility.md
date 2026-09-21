# Feasibility · gender1 · 21 September 2026

Written by the human's assistant in the steward's form; the steward confirms or corrects at the start of the next session. Data profile: `data/releases/eurostat_isoc_ai_iaiu.md`.

## 1. The extract

- Official Eurostat TSV fetched 21 September 2026 by `data/fetch/eurostat_isoc_ai_iaiu.py`; 39,006 cells (37,885 plus the euro-area aggregate). The EIGE mirror export of the same date agrees on all 37,885 common cells, values and flags.
- Flags: `u` on 6,699 cells; no other flag. Missing 3,196 (`:`).

## 2. Coverage for the pre-registered tests (counts inspected; no gap values below the overall 16–74 level read)

- Overall usable pairs, `I_IUAI` `PC_IND`: 36 of 36 geographies.
- All twelve usable sex-by-age cells, `I_IUAI` `PC_IND`: 33 of 36; IE, MK, RS incomplete. EU27 subset: 26 of 27 (IE out).
- Education pairs and purpose pairs: see `outputs/audit/eurostat_subgroup_coverage.csv`; the low-education purpose cells are the thinnest (27 of 36 geographies).

## 3. National sample sizes (the steward task in the profile, done)

Source: Eurostat national reference metadata pages `isoc_i_simsih2_<cc>.htm`, fetched 21 September 2026 for 36 geographies (MK and XK pages not served). Each page reports, for a reference indicator, the number of "yes" respondents, the estimated proportion, and often its standard error; achieved sample counts are printed explicitly by CZ (7,705) and IT (31,536). Elsewhere the achieved n is implied as yes-count ÷ proportion. Table: `data/processed/national_sample_sizes_2025.csv`. Range: about 1,750 (MT) to 31,536 (IT); DE 12,235; FR 10,781; ES 13,577; PL 10,295; RO 13,668. NL reports a net sample of about 5,000 but no yes-count in the form parsed. Response rates range from 11% (RO) to 92% (FR) where stated.

Check of the simple-random-sampling assumption: the published standard error of the reference indicator divided by the SRS value has median 1.11 across 30 countries (IT 0.89, DE 1.09, MT 0.99); Romania is 2.8, a design effect the bound understates there. So the bound is a lower bound that is close for most countries, and it is labelled as a bound.

## 4. The bound (script 01, `data/processed/power_rules.json`)

- Overall gap, 95% half-width: median 2.75 points across 32 countries; IT 0.88, DE 1.66, DK 3.14, MT 4.67.
- By sex-by-age band: median half-width 6.3 to 7.6 points; MT 25–34 is 11.7.
- Reading: country rankings of the overall gap are distinguishable only between countries several points apart; within age bands, almost nothing is. The pre-registration's class rule and its "distinguishable majority" counts follow from this.

## 5. Age weights

`demo_pjan` EU27_2020, 1 January 2025, provisional (`ep`): band weights 0.131, 0.158, 0.179, 0.189, 0.188, 0.155 for the six bands 16–24 to 65–74; sum one (checked).

## 6. What the data cannot show, for the notebook

No sex within employment, occupation or urbanisation; no trend; no intensity; no confidence intervals; no gender beyond female and male; no age-by-education by sex; the household population differs from the resident population used for weights.

## 7. Triangulation inputs

- OpenAI Signals gender by country by month: cached bundle `data/cache/openai_signals/signals.zip`; all EU27 present; 26 with June 2025 (Greece is `GR` there and `EL` in Eurostat). Licence in the bundle's `README.pdf`, to be read before use.
- Henseke (2026) country table of work-adoption gaps: to be transcribed from the paper's appendix before script 07; if not published by country, leg (ii) is dropped and logged.
