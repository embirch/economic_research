# Source profile: Brazil, Cetic.br TIC Domicílios 2025 (generative-AI module)

Data steward, 1 October 2026. Proposed IDs `BR_CETIC_USE`, `BR_CETIC_PURPOSE`,
`BR_CETIC_NONUSE`; sample family **`BR_CETIC_TICDOM_2025`**.
Status: **file-verified published aggregates** (proportions, population totals and
sampling margins of error), provider documentation read. No respondent microdata was
downloaded; the provider's microdata CSV was deliberately not retrieved.

This replaces the coordinator-supplied lead status in the pilot coverage CSV
(`LEAD_CETIC_TIC_DOMICILIOS`, “not audited by me”).

## Provider, survey and design

| Item | Verified value | Evidence |
|---|---|---|
| Provider | Centro Regional de Estudos para o Desenvolvimento da Sociedade da Informação (Cetic.br), a department of NIC.br; UNESCO Category 2 centre | provider pages; methodological report |
| Survey | *Pesquisa sobre o uso das tecnologias de informação e comunicação nos domicílios brasileiros — TIC Domicílios 2025* | methodological report v1.0 |
| Target population | Permanent private households in Brazil and residents **aged 10 and over** | methodological report, “População-alvo” |
| Sampling | Stratified, clustered probability sample in 3–4 stages; frame built from IBGE register-based census sector listings; calibrated weights | methodological report, “Plano amostral” |
| Mode | CAPI, face-to-face, in-home | data-collection report, “Método de coleta” |
| Fieldwork | **March to September 2025**, whole national territory | data-collection report, “Data de coleta” |
| Achieved sample | 27,177 households approached in 720 municipalities; **24,535 households with TIC Domicílios individual interviews** (persons aged 10+); planned 41,145, adjusted count 40,408 | data-collection report, “Resultado da coleta” |
| Internet-user definition | used the internet at least once in the **three months** before interview (ITU 2020 definition) | methodological report, “Usuário de Internet” |
| Precision | Provider publishes a **margin of error (%) table** alongside proportions and population totals for every indicator and breakdown | sampling-error workbook |

## The generative-AI items

Indicator tables M1–M3 in the individuals volume:

| Table | Published construct | Base (denominator) | Response type |
|---|---|---|---|
| M1 | Internet users by use of generative-AI tools (Yes / No / Does not know / Did not answer) | internet users aged 10+ | single response |
| M2 | Purpose of use | internet users **who used** generative AI | **multiple response** |
| M3 | Declared reason for not using | internet users **who did not use** generative AI | **multiple response** |

**Questionnaire wording matters here.** The variable dictionary (v1.0) records the item
as `C13A`: *“Nos últimos 3 meses, o(a) sr.(a) usou ferramenta de inteligência artificial,
como chatGPT, Copilot, Gemini ou a Meta IA do WhatsApp?”* — that is, **“AI tool”** with
generative-AI examples (including Meta AI inside WhatsApp), asked of internet users with
a **three-month** reference period. The published tables are labelled “generative
artificial intelligence (AI) tools”. The label and the stimulus are therefore not
identical, and the Meta-AI-in-WhatsApp example has no counterpart in the Eurostat item.
Record the question wording next to any displayed value.

**M3 is not Eurostat's B7.** Brazil's reasons are multiple response: the male row sums to
about 239% of its base (73.96 + 50.41 + 55.00 + 58.65 + 0.95). Eurostat's B7 collects the
**single main reason**. These two tables must never be aligned or differenced.

## Verified published cells (sex rows)

From [`../checks/cetic-published-cells.json`](../checks/cetic-published-cells.json),
produced by [`../checks/check_cetic.py`](../checks/check_cetic.py):

| Table | Measure | Male | Female |
|---|---|---|---|
| M1 “Yes” | proportion (%) | 34.7902 | 30.4901 |
| M1 “Yes” | margin of error (pp, 95%) | ±3.2872 | ±2.7759 |
| M1 “Yes” | estimated population | 25,591,924 | 25,579,362 |
| M2 professional/work use | proportion (%) | 52.2303 | 48.6824 |
| M2 school/college work | proportion (%) | 47.6790 | 58.4770 |
| M2 personal use | proportion (%) | 88.1700 | 80.3000 |
| M3 lack of interest or need | proportion (%) | 73.9557 | 77.5159 |
| M3 lack of awareness of such tools | proportion (%) | 50.4143 | 53.2201 |
| M3 lack of skills to use them | proportion (%) | 55.0028 | 60.4712 |
| M3 security or privacy concerns | proportion (%) | 58.6516 | 67.5019 |

The provider's own HTML indicator pages display the same cells rounded to whole
percentages (M1 Male 35, Female 30; total 32). The unrounded workbook values reproduce
those displays, which is the only consistency check performed; **no new gap estimate is
computed here.**

Sex categories are the provider's `SEXO` rows **Masculino / Feminino**. The published
tables contain no third category and no gender-identity item; there is also a separate
“Did not answer” column for the AI item itself, which is not a gender category.

## Joint fields and what cannot be built

- The published tables give **marginal breakdowns only** (area, region, sex, race/colour,
  education, age band, household income, social class, labour-force status, occupation
  type). There is **no published sex × age or sex × education cell**. Do not construct one
  from the margins.
- Age bands start at **10–15**, so the published base is wider than Eurostat's 16–74 and
  wider than the UK's 16+.
- Respondent-level microdata exist (`…_base_de_microdados_v1.0.csv`) and were **not
  downloaded**; any future individual-level analysis needs its own scope, terms check and
  authorisation.

## Access and reuse

- Open download, no registration, no account: tables, questionnaire, variable dictionary,
  methodological report and data-collection report are all public.
- The download page's dataset entry records **Licença: Atribuição 4.0 Internacional
  (CC BY 4.0)** for version 1.0 of the individuals tables. The provider's indicator pages
  also carry a CC BY-SA 4.0 site link. **Two different licence statements appear on the
  provider's own pages**; before publishing the derived cells, pin the licence that
  accompanies the exact file version used (the CC BY 4.0 statement attached to the table
  bundle) and attribute as the provider requires.
- Required attribution, as printed under each table: Núcleo de Informação e Coordenação do
  Ponto BR. (2025). *Pesquisa sobre o uso das tecnologias de informação e comunicação nos
  domicílios brasileiros: TIC Domicílios 2025* [Tabelas].

## Provenance of retrieved files (ignored scratch, not committed)

| File | Bytes | SHA-256 |
|---|---:|---|
| `ict_households_2025_individuals_tables_xlsx_v1.0.zip` | 1,027,291 | `9ca6638cc6a965d7d90de789cdc7f0e67de08918d4f4067c56575e9b621dd930` |
| `tic_domicilios_2025_relatorio_metodologico_v1.0.pdf` | 1,569,812 | `ba623fad92c9e7c7d0015186dd3df4e255992ab93e6716f9b2b5be824383f3a2` |
| `tic_domicilios_2025_relatorio_coleta_de_dados_v1.0.pdf` | 1,444,385 | `f18a69305f7ed2f95512ee65b49774cf3be812720c5c2b27cac3fe35c2bd9237` |

Source pages: <https://www.cetic.br/pt/tics/domicilios/2025/individuos/M1/> (and M2, M3)
and <https://cetic.br/pt/arquivos/domicilios/2025/individuos/>, retrieved
2026-10-01.

## Comparability verdict

A genuine, probability-based national module with **published uncertainty** — the only
candidate so far that supplies a margin of error for a sex-specific generative-AI rate.
It is **not** comparable with Eurostat: different age floor (10 vs 16), different
denominator (internet users vs all individuals or recent internet users), a different
stimulus (“AI tool” with examples incl. Meta AI), multiple-response non-use reasons, and
fieldwork spread over seven months rather than referenced to one quarter. Present it as
its own module with its definitions attached; do not rank it against European countries.

## Open items

1. Pin the licence version in writing with the provider's own file-level statement
   (done above) and decide whether a derived table is published non-commercially.
2. Check whether the Portuguese tables volume carries table-level notes on the C13A item
   not present in the English volume.
3. If joint sex × age cells are ever needed, they require the microdata route, a separate
   authorisation and a terms review.
