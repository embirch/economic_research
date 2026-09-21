# Eurostat `isoc_ai_iaiu` and `isoc_ai_iaiuxr` · Individuals: use of generative AI tools, and reasons for non-use · 2025

Profiled 21 September 2026 (audit by the human's assistant; steward to confirm the national sample sizes). First non-Anthropic data profile in the programme; it serves `posts/gender1/`.

## Source and provenance

- Eurostat tables: `isoc_ai_iaiu` (use) and `isoc_ai_iaiuxr` (reasons for non-use), from the EU survey on ICT usage in households and by individuals, 2025 module on generative AI. Questions first asked in 2025; no earlier wave exists.
- Primary web pages: https://ec.europa.eu/eurostat/databrowser/view/isoc_ai_iaiu/default/table?lang=en and `…/isoc_ai_iaiuxr/…`. Statistics Explained article: https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Use_of_artificial_intelligence_by_individuals (gender at EU level only). News release 16 December 2025: https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20251216-3. Metadata (ESMS): https://ec.europa.eu/eurostat/cache/metadata/en/isoc_i_esms.htm. Model questionnaire 2025 (B1, B5–B7): https://www.cso.ie/en/media/csoie/releasespublications/documents/ep/isshinternetaccessandict/2025/Information_Society_Statistics_2025_Model_Questionnaire.pdf.
- Extract used: the EIGE full CSV export (official mirror, https://dgs-p.eige.europa.eu/data/information/ta_resdig_dig_intuse__isoc_ai_iaiu), mirror updated 20 July 2026, extracted 21 September 2026, because the Eurostat API returned a service-unavailable page on that date. Export logs: `posts/gender1/outputs/audit/eige_export_log.json`, `raw_manifest.json`.
- Cache (gitignored): `data/cache/eurostat/isoc_ai_iaiu_Data.csv` (sha256 `c1bd2a16…`), `isoc_ai_iaiu_Label.csv` (`35b96efe…`), `isoc_ai_iaiuxr_Data.csv` (`6911d623…`), `isoc_ai_iaiuxr_Label.csv` (`08118a83…`). Refetch with `data/fetch/eurostat_isoc_ai_iaiu.py`; keep both versions if a newer revision appears.

## Grain and shape

- `isoc_ai_iaiu`: 37,885 published cells; columns `Time, geo, Value, indic_is, ind_type, unit, Flags`; 2025 only; 35 countries and territories plus `EU27_2020` (AL AT BA BE BG CH CY CZ DE DK EE EL ES FI FR HR HU IE IT LT LU LV MK MT NL NO PL PT RO RS SE SI SK TR XK); 104 population-group codes. Cells, not respondents.
- `isoc_ai_iaiuxr`: 53,280 cells; 36 geographies plus EU; same group codes; five single-main-reason indicators (`I_IUAIX_NUNN` no need, `NUOTH` other, `NUSEC` privacy/security, `NUUNK` unaware, `NUUSE` did not know how).
- Indicators (use): `I_IUAI` any use in the previous three months; `I_IUAIPR` private; `I_IUAIWP` professional; `I_IUAIFE` formal education. Purposes are multi-select; they do not sum to `I_IUAI`.
- Units: `PC_IND` percentage of individuals; `PC_IND_IU3` percentage of recent internet users; `PC_IND_IUAI` percentage of recent AI users. The AI module is routed through recent internet use (questionnaire B1 → B5), so the reason distribution in `isoc_ai_iaiuxr` concerns recent internet users who did not use generative AI.
- Population: individuals aged 16–74 in private households; optional 75–89 cells exist with poor coverage.
- Reference period: use in the three months before the interview; fieldwork by convention in the first quarter of the survey year.

## Population-group codes

- Sex by age: `F_`/`M_` + `Y16_74, Y16_24, Y25_34, Y35_44, Y45_54, Y55_64, Y65_74` (non-overlapping bands) plus overlapping `Y16_19, Y16_29, Y20_24, Y25_29, Y25_54, Y25_64, Y55_74` and `Y75_89`.
- Sex by education: `F_`/`M_` + `I0_2` (low), `I3_4` (medium), `I5_8` (high), plus `_75_89` variants.
- **No sex prefix** on employment (`EMPL_UNE, SAL_SELF_FAM, UNE, RETIR_OTHER, STUD`), occupation (`ISCO0_5, ISCO6_9, ISCO_ICT, ISCO_ICTX`), income (`IND_DEG1..3` are degree of urbanisation? — verify label), birth/citizenship (`CB_*`, `CC_*`), age-by-education (`Y16_24HI` etc.). So no gender comparison exists within the employed, within occupations, or within age-by-education.

## Flags, missingness, precision

- Flags: `u` low reliability on 6,699 cells (use) and 9,615 (reasons); no other flag in the extract. Eurostat's rule: results with a denominator under 20 respondents are not published; 20–49 are published and flagged `u`.
- Missing values: 3,196 (use), 4,230 (reasons); overlap with flags.
- No cell-level standard errors, counts or design variables. The ESMS states about 172,000 households and 330,000 individuals aged 16–74 were surveyed in the EU in 2025 and that national sample characteristics are in the national metadata files. **Steward task:** fetch the national sample sizes (by sex if published) and record them here; they support an approximate binomial bound, labelled as a bound.

## Coverage facts (inspected 21 September 2026)

- Paired unflagged overall male/female `I_IUAI` `PC_IND` cells: all 36 geographies.
- All twelve unflagged sex-by-age cells for `I_IUAI` `PC_IND`: 33 of 36; incomplete: IE, MK, RS.
- Subgroup coverage table: `posts/gender1/outputs/audit/eurostat_subgroup_coverage.csv`.

## Age weights

- `demo_pjan` (population on 1 January by single age and sex) is served by the Eurostat API: `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/demo_pjan?format=JSON&lang=EN&geo=EU27_2020&time=2025&sex=T&age=Y16…Y74`; status `ep` (estimated, provisional) on 21 September 2026. Sample pull cached at `data/cache/eurostat/demo_pjan_EU27_2025_sample.json`. Full six-band pull is in the fetch script.

## Traps

1. `Value` is a string with two decimals; missing is empty; flags are in a separate column.
2. `EU27_2020` is population-weighted; the four largest members dominate it.
3. `EL` is Greece (Eurostat code), `GR` in OpenAI Signals; `XK` Kosovo; `UK` absent.
4. Purposes overlap; never subtract them.
5. The internet-user and AI-user denominators condition on routed subgroups; a gap can change sign between denominators without either being wrong.
6. No 2024 comparison exists; any "trend" claim is impossible.

## Companion source: OpenAI Signals gender files

The bundle `https://cdn.openai.com/signals/data-download-csv.zip` (cached at `data/cache/openai_signals/signals.zip`, sha256 `83b49feb…`, fetched 21 September 2026) carries, beyond the files the atlas profiled: `share_of_messages_by_gender_country_month.csv` (month × country × `typical_name_gender` feminine/masculine, 5,194 rows, 119 countries; all EU27 present, 26 with June 2025), `share_of_messages_by_gender_topic_country_month.csv` (86 countries, 7 topics), `share_of_messages_by_gender_topic_month.csv` and `global_share_of_messages_by_gender_month.csv` (July 2024 to June 2026), plus age-group equivalents. Shares are within topic (the feminine share of a topic's messages), gender is inferred from first names, the unit is a message, and the licence is stated only in the bundle's `README.pdf`, to be read before use.
