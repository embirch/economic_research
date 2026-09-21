# Gender and AI: data audit and revised research series

Audit date: 21 September 2026. Prepared for Emily Birch.

## Decision

There is a defensible path to **three empirical pieces using existing public data**:

1. **Where is the gender gap in generative AI use, and what do non-users report?** Eurostat household ICT statistics.
2. **What gets people started with ChatGPT—and who continues?** The Spanish survey accompanying the Ochoa, Fernández Melero and Revilla research release.
3. **Does convergence in overall usage conceal differences across tasks?** OpenAI Signals, explicitly measuring message shares by name-associated gender.

These are feasible data foundations, not guarantees of novel findings or journal acceptance. The second piece requires a short coding feasibility exercise and confirmation of survey-specific reuse/documentation. None of the three identifies a causal gender effect or economic returns to adoption.

The audit materially changes the earlier advice: **there IS public individual-level first-use-motivation data in the Spanish release.** The field was not apparent from the published metered-data article alone. The qualitative component can therefore use linked self-reported gender, rather than trying to infer it from Anthropic interviews. However, responses are brief survey answers, not in-depth interviews.

## Scope and evidence standard

This is an audit of the candidates developed in our conversation, the local copy of the GitHub repository, relevant existing workspace datasets, and targeted primary-source follow-up. It is not a claim to have exhausted every global dataset. Distinguish:

- **File verified:** downloaded/opened and profiled actual records.
- **Documentation verified:** questionnaire, catalogue or publication inspected; microdata not obtained.
- **Unresolved:** access, reuse, sample construction or essential variables remain uncertain.
- **Unsuitable:** available data cannot answer the proposed gender/adoption question.

Repository material reviewed: `economic_research/reference/sources/{datasets,data-audit,external-data-check}.md`; relevant prior research summaries; 27 local Economic Index CSV headers in `bible/data/ei`; existing OpenAI Signals files in `research/post2/data/raw/openai_signals`. Repository claims were treated as leads, not automatically as verified facts. Existing projects were not edited.

## Source-by-source findings

### 1. Eurostat use of generative AI — FILE VERIFIED / core

Source: [Eurostat](https://ec.europa.eu/eurostat/databrowser/view/isoc_ai_iaiu/default/table?lang=en); obtained through the [official EIGE mirror](https://dgs-p.eige.europa.eu/data/information/ta_resdig_dig_intuse__isoc_ai_iaiu). Eurostat's API returned an HTML service-unavailable page even with HTTP 200. EIGE's full CSV export succeeded. Mirror last-updated date: 20 July 2026; extraction: 21 September 2026. This may lag subsequent Eurostat revisions.

Actual file: 37,885 rows, 7 columns, 2025 only; 35 country/territory codes plus the EU aggregate; 104 population-group codes. Unit: published survey estimate for a geography × population group × indicator × denominator × year. Not respondent-level data. The primary age range is 16–74; optional 75–89 cells exist but have limited coverage.

Indicators: `I_IUAI` recent use; `I_IUAIFE` formal education; `I_IUAIPR` private use; `I_IUAIWP` work use. Denominators: `PC_IND` all individuals; `PC_IND_IU3` recent internet users; `PC_IND_IUAI` recent AI users. Purposes overlap.

Available gender crossings include sex × age and sex × education. They do **not** form a full sex × age × education × occupation microdataset. Do not combine marginal tables to pretend they do. No gender-specific employed denominator is verified in these extracts.

All 36 geography codes have both unflagged male and female 16–74 estimates for each available indicator/denominator. Finer subgroups lose coverage. Complete unflagged six-age-band male/female adoption estimates exist for 32 countries/territories plus the EU aggregate. Missing values: 3,196; low-reliability flags: 6,699 across the full table. These counts overlap: flags can accompany missing or numeric estimates. No duplicate analytical keys or out-of-range numeric values were found. No respondent sample sizes, standard errors or survey-design variables are in this CSV.

Preliminary validation, EU 2025, percentages of all individuals aged 16–74:

| Measure | Female | Male | Male minus female, pp |
|---|---:|---:|---:|
| Any recent use | 30.45 | 34.91 | 4.46 |
| Private use | 22.76 | 28.27 | 5.51 |
| Work use | 13.87 | 16.87 | 3.00 |
| Formal education | 9.30 | 9.35 | 0.05 |

These establish that different purposes are observable. They are not significance tests. Among AI users, the education shares are 30.53% female and 26.77% male: changing denominators can change the interpretation without either statistic being wrong.

**Use for:** descriptive disparities, subgroup comparisons, purpose contrasts, age standardisation with explicit common weights. **Not for:** first-use motives, intensity, productivity, individual transitions, or causal explanations.

### 2. Eurostat reasons for non-use — FILE VERIFIED / integrate into piece 1

[Official EIGE source](https://dgs-p.eige.europa.eu/data/information/ta_resdig_dig_intuse__isoc_ai_iaiuxr). Actual file: 53,280 rows, 7 columns, 2025; 36 countries/territories plus EU aggregate; same 104 group codes. All 37 geography codes have unflagged paired overall male/female estimates for the five reasons and three denominators. Missing values: 4,230; low-reliability flags: 9,615. No duplicate analytical keys or out-of-range numeric values found.

Reasons: no need (`I_IUAIX_NUNN`), other (`NUOTH`), privacy/security/safety (`NUSEC`), unaware (`NUUNK`), did not know how (`NUUSE`). This is a **single main reason**, not a checklist of all barriers.

Critical denominator correction: [the actual model questionnaire, B1 and B5–B7](https://www.cso.ie/en/media/csoie/releasespublications/documents/ep/isshinternetaccessandict/2025/Information_Society_Statistics_2025_Model_Questionnaire.pdf) routes the AI module through recent internet use. Consequently the reason distribution concerns **recent internet users who did not recently use generative AI**, even though the short unit label `PC_IND_IUAIX` says AI non-users. It does not explain the behaviour of adults who do not use the internet. The all-individual shares of reasons sum to less than 100 minus AI adoption for this reason.

Example: no need is 62.20% among female eligible non-users and 66.49% among male eligible non-users, but its all-individual prevalence is 39.33% and 39.17%. Report both denominators where informative. Do not call the conditional difference a causal explanation of the adoption gap.

**Use for:** the descriptive “why” component of piece 1. **Not for:** estimating the effects of training, trust or interventions. Combine with piece 1 unless a distinct contribution warrants separation.

### 3. Spanish ChatGPT survey — FILE VERIFIED / core first-use study

Public repository: [OSF project](https://osf.io/gpc5u/), [survey workbook](https://osf.io/download/68f00236ee9b765838497770/). The release accompanies [Ochoa, Fernández Melero and Revilla (2026)](https://doi.org/10.1155/hbe2/9703008). Author conference materials describe two separate opt-in samples and survey quotas for gender/age and education; see [author slides](https://www.upf.edu/documents/244683118/246905697/ESRA25-MelanieRevilla.pdf/9ffda9fb-58c6-e6fc-e7dd-07238384d353?t=1753298493520).

Discovery: the workbook initially downloaded under the audit filename `osf_panel_history.xlsx` is actually the **survey**, with sheets `Datos`, `Labels`, `variables`, `codes`. Its original source name is `UPFBES_277388_20250520_V1.xlsx`. The audit scripts explicitly document this naming correction.

2,714 rows and 197 columns in the raw workbook; **2,102 completed interviews** after `TYPE == complete`, with unique respondent identifiers. Complete interviews span 3–14 April 2025. Gender is self-reported: 1,060 female and 1,042 male. The instrument supplies two gender options. Non-completes, consent refusals and quality exclusions must be excluded; raw row count is not the analytical sample.

Directly verified variables:

| Field | Meaning | Audit finding |
|---|---|---|
| `GENDER` | Self-reported gender | Complete for 2,102 valid respondents |
| `USER` | Never used / formerly used / still using | 1,081 never; 268 former; 753 current |
| `START_USE_MES`, `START_USE_ANO` | Recalled first-use month/year | Available for 1,021 ever-users |
| `REASON_USER` | What motivated you to start using ChatGPT? | 1,014 non-empty free-text responses: 490 female, 524 male |
| `USE#1`, `USE#2` | Subsequent academic/professional and personal use | Subsequent purposes, **not** first tasks |
| `USERNB` | Used ChatGPT more than ten times | 668 yes; 353 no among ever-users |
| `NOMORE#...` | Reasons for not using it more | Routed to low-repeat users; not a clean former-user-only measure |
| `NOTUSER#...` | Reasons for never using | Separate routed module |
| `RECOMMEND` | People you know recommended ChatGPT | Does not establish recommendation preceded first use |
| Other fields | Age, education, employment, children, emotions, comfort | Available; exact routing and missingness must be respected |

The motivation responses have median **18 characters**, mean 27.8 and maximum 250. There are 747 distinct strings; repeated short responses are not duplicate respondents. Seven ever-users have missing motivation text. A fixed-seed 35-answer inspection found codable mentions of curiosity, work, education, practical tasks, and recommendations alongside ambiguous answers. This was a feasibility read, not a finished codebook or prevalence estimate.

No weight column was found. Treat this as an opt-in, quota-based survey, not a probability sample of Spain. The file contains 70 valid survey respondents with a metered-sample ID; only 39 appear in the downloaded visit file. **Do not join the two samples and claim a large longitudinal test of motivations.**

Reuse/documentation: files are publicly downloadable and the article explicitly announces open data. No machine-readable licence was found on the OSF node. Before publishing respondent text or redistributing files, verify the survey-specific reuse terms and recruitment/routing documentation. This is a limited documentation task, not a missing-data problem. Do not republish personal fields or identifiable free text.

**Use for:** a full study of reported motivations, adoption status and cautious associations with subsequent self-reported use. **Not for:** a rich interview ethnography, the exact first task for everyone, or causal effects of entry routes. No gaming premise is needed.

### 4. Spanish metered panel — FILE VERIFIED / reserve, discrepancy unresolved

[Metered file](https://osf.io/download/82ug6/), [profiling workbook](https://osf.io/download/bnt8m/), [meter documentation](https://osf.io/download/u2cxb/), [profiling documentation](https://osf.io/download/mt468/).

699,468 event rows, six columns; February 2023–April 2025; **1,188 distinct IDs in the downloaded visit file**. Profiling supplies 2,100 distinct metered IDs (1,171 male, 929 female); all visit IDs match profiling. Three duplicate event rows; no missing event fields or negative time intervals; unusually long duration tail (maximum 1,990.67 minutes), requiring session-definition checks. Desktop records dominate.

**Material discrepancy:** SOM1 describes 1,607 users and 493 non-users, but the downloaded file contains 1,188 observed users. Do not silently treat the remaining 912 profiled people as validated non-users or replicate the published prevalence with this file. The original and revised profiling workbooks are available; this does not itself explain missing visit IDs.

A preliminary strict-domain screen retains 984 people, demonstrating sensitivity to counting general `openai.com` visits as ChatGPT use. That screen is provisional, not a validated classifier. General documentation/account visits do not establish chatbot interaction.

The original paper already studies weekly adoption, session counts, duration and gender trends. A new event-time return-use study may be possible, but needs the discrepancy resolved, proper observation/censoring rules and a novelty check. No first-task content or social referral data appear in the event file. **Do not make this a required dependency of the series.**

### 5. OpenAI Signals — FILE VERIFIED / core use-pattern study

[Official source](https://openai.com/signals/data/), [methodology](https://openai.com/signals/data-download/). Existing workspace contains 25 CSVs, a ZIP and version-2.0 documentation. Profiled all 25 CSVs; full details in `outputs/signals_profile.json`.

Relevant actual files:

| Table | Rows | Coverage |
|---|---:|---|
| Global name-gender × month | 48 | 24 months × 2 labels |
| Country × name-gender × month | 5,194 | 119 countries with some data; 95 with all 24 months |
| Global topic × name-gender × month | 336 | Complete 24 × 7 × 2 |
| Country × topic × name-gender × month | 14,164 | 86 countries with some data; only 8 complete 24 × 7 × 2 panels |

Dates: July 2024–June 2026. Complete topic-country panels: BR, CA, DE, FR, GB, IN, MX, US. A country appearing in all months does **not** mean all its topics appear in every month. All released gender pairs sum to one; no duplicate keys or out-of-range shares found in these four tables.

The field is `typical_name_gender`, with feminine/masculine categories inferred by the provider from first names, not self-identified gender. Unmatched names are excluded. Unit is **message**, not unique person; heavy users count more. The release samples 300,000 messages per month, applies day weights, differential privacy noise, rounding and suppression below an effective cell count threshold. Counts and standard errors for the released cells are absent. Consumer accounts only; excludes Enterprise, Codex, under-18/nonreported ages, deleted accounts and training opt-outs under the documented sampling rules.

Crucial conditional direction: the topic-gender file is **P(name category | topic, month)**, not P(topic | gender). We can directly compare female-name representation within topics, and compare it with overall representation. Do not multiply unrelated margins to manufacture gender × work × age outcomes. A Bayes inversion with overall topic shares would require matching the name-classifiable denominator, which has not been established.

Preliminary endpoints: feminine-name share in Technical help is .264 in July 2024 and .394 in June 2026; Writing .492 and .573; Self-expression .438 and .625. These are feasibility checks, not claims of statistical significance or inherent preferences. Self-expression combines games/roleplay with other activities; there is no separate public gaming series in these files.

**Use for:** changes in representation across topics over time, globally and in a prespecified supported country set. **Not for:** population adoption rates, first-use pathways, individual transitions, gender-specific work use, confidence or productivity. These limitations should be visible in the main article.

### 6. Anthropic Interviewer — FILE VERIFIED / supplementary only

[Dataset](https://huggingface.co/datasets/Anthropic/AnthropicInterviewer), pinned at `c9e1ec1e6b093712b9c42235c7303ece647490e9` for this audit. All three CSVs downloaded: 1,000 workforce, 125 creatives, 125 scientists. Exactly two columns: `transcript_id`, `text`; no null text or duplicate IDs within files. No structured gender, age, occupation, weights or adoption-history variables.

Useful for developing concepts about work experience. Not a valid male/female comparison without new linked metadata. Gender inference from prose is not an acceptable workaround. A subset mentioning gender would be disclosure-selected and would answer a different question. Richness of prose does not supply the missing comparison variable.

### 7. Other Anthropic releases — repository audit plus local schema checks

The prior repository audit reviews all 14 Anthropic releases it found on 2 September 2026. For this audit, 27 locally available Economic Index CSV headers were checked; none has a gender field. This is a local subset check, not a fresh full crawl of every release. The earlier full facet audit also reports no user demographic cross-tabs.

- Economic Index: supplementary task/exposure context, not gender uptake data. An occupation's female workforce share is not the gender of its Claude users.
- Enabling-independent-research: prior audit finds experience/productivity facets but no linked participant gender. Not a gender-outcomes foundation.
- Values-in-the-wild: model values taxonomy, not respondent gender experiences.
- Persuasion: experimental outcome data but no participant demographics in the audited release.
- Discrim-eval / model-written evaluations: synthetic demographic prompts can study model bias; they do not measure gender differences in adoption. Pursuing them would change the programme.
- Training, safety and science benchmarks: outside the present research questions.

### 8. Pew — documentation verified; no microdata acquired

[Wave 164](https://www.pewresearch.org/dataset/american-trends-panel-wave-164/) is listed for download behind free-account login. It includes 2025 ChatGPT use questions and could provide an independent survey comparison once acquired. Do not treat an account gate as unavailable forever, but do not claim that the file has been inspected.

The rich June 2026 [gender report](https://www.pewresearch.org/internet/2026/06/17/the-gender-gap-in-ai/) uses **Wave 187**, 5,119 respondents. Questionnaire verified: `CHATUSEMOD`, `CHATFREQ`, `CHATCONF`, `CHATENJ`, brand-specific use and additional use/attitude measures. The expected Wave 187 dataset URL returned 404; the report offers questionnaire/topline materials, not a verified microdata download. Thus **not a secured foundation today**. Published gender tables are useful context but reproducing them would offer little novelty. Wording/routing differs between some waves, so do not assume a clean longitudinal adoption measure.

### 9. EWCS 2024 — access route verified; microdata not acquired

[UKDS study 9511 access conditions](https://doc.ukdataservice.ac.uk/doc/9511/read9511.htm): available to registered users under an End User Licence. Dataset-specific questionnaire and microdata were not obtained in this audit; attempted generic questionnaire/directory paths failed. Henseke's [existing paper](https://arxiv.org/abs/2604.18849) already studies exposure, adoption and gender across European workplaces. Keep as a reserve for a specific workplace mechanism, not a prerequisite. A generic repetition of its central analysis is not a contribution.

### 10. Other first-use and outcomes leads — literature, not secured datasets

The previously identified MIPRO student first-use study and elite-college survey are useful question-design references, but no public respondent-level files were secured for either. UK qualitative search-behaviour material is a report rather than a verified gender-linked interview corpus. No suitable public causal-outcomes dataset was secured for a gender-benefits paper. These leads do not need to block the three verified alternatives above.

## Revised series and implementation

### Piece 1 — Where is the gender gap, and what do non-users report?

Scope: European 2025 population statistics, purposes and reported non-use reasons. Primary analysis: prespecified sex/age range, pp gaps and ratios, country comparisons with reliability flags preserved, common-age standardisation where supported. Combine reasons with participation descriptively; distinguish all-adult and eligible-non-user denominators. A decomposition may be arithmetically useful but must not be described as causal mediation.

Scientific safeguards: no invented survey confidence intervals; no rankings presented as statistically resolved; no full individual-level regression from marginal tables; separate EU aggregate from countries; exclude low-reliability cells in the main analysis and show sensitivity. Obtain common age weights from an explicitly documented population series before standardisation. A small number of prespecified figures is preferable to all possible slices.

Novelty test: the basic gender gap is known. The contribution must be the measurement-sensitive pattern across purposes, groups and non-use reasons. Preliminary values suggest genuine scope, but do not promise the direction of results.

### Piece 2 — What gets people started with ChatGPT—and who continues?

Scope: Spanish April 2025 opt-in survey. Main question: how reported first-use motivations differ by gender, and how motivations are associated with current versus former use and repetition among ever-users. Distinguish entry motivation, first task, referral and subsequent purpose; only claim what the item measures.

Implementation: code a random pilot of 100–150 responses before committing to a taxonomy; mark vague/uncodable responses explicitly. Use Spanish-language coding with gender hidden from coders, allow multi-label categories where justified, and use two independent human coders on a substantial subset. Record agreement and adjudication. If AI assists coding, retain prompts/model versions and validate against held-out human coding; never let it invent unstated motivations. Preserve short answers as short evidence.

Analysis: report motivation prevalence among ever-users with valid answers and missingness by gender. Estimate modest prespecified adjusted associations (e.g. age, education), with sample-conditional uncertainty and sensitivity to coding ambiguity. Do not treat opt-in quotas as probability weights. Current-use associations are retrospective and selected on ever-use; they are not effects of motivations. `RECOMMEND` has ambiguous temporal ordering; `NOMORE` concerns low repetition, not necessarily discontinuation.

Pre-publication checks: verify survey-specific recruitment and redistribution terms; review authors' related work for overlap; confirm sufficient codable content. If motivation categories are too vague, pivot within the same file to continued use/non-use and reported reasons, rather than force a narrative.

### Piece 3 — Does convergence in overall use conceal differences across tasks?

Scope: OpenAI consumer message shares, July 2024–June 2026. Main question: whether representation becomes more similar across topics as overall feminine-name message share changes.

Implementation: start with the complete global 24 × 7 series; compare topic-specific name shares against the same month's overall name share (pp difference and, if useful, log-odds contrast). Describe it as representation, not within-gender preferences. Use the eight complete country-topic panels for a predefined comparative extension; report their selection and unbalanced-panel sensitivity.

Scientific safeguards: no manufactured demographic/work cross-tabs; no pooled monthly totals without message-count weights; no simple binomial confidence intervals from the global 300,000 count; distinguish rounding/noise sensitivity from sampling confidence intervals. Serial monthly observations are not independent people. Consider this a descriptive measurement paper; any trend modelling must state what uncertainty it does and does not capture.

Novelty test: OpenAI already displays demographic topic shares. The added contribution must be an explicit longitudinal convergence measure, supported country comparisons and transparent denominator/coverage analysis, rather than relabelling the dashboard.

### Programme interpretation

The three pieces examine **participation, reported entry/continuation, and patterns of use**. They do not trace the same people across all three sources. They can motivate hypotheses about opportunity, support, unpaid work and economic benefits, but do not directly establish wage, productivity or welfare effects. The original causal experiment remains a future proposal, not an obligatory third empirical piece.

## What is complete and what remains

Completed: repository review; actual downloads and schema checks for Eurostat/EIGE, Spanish survey/meter/profiling and Anthropic interviews; profiling of existing Signals files; primary questionnaire checks; preliminary feasibility tables; identified missingness, suppression, denominator and sample-linkage problems; revised executable series.

Remaining before substantive analysis: coding pilot; survey-specific documentation/reuse clarification; fuller literature-overlap review; dated analysis plans after acknowledging this exploratory audit; age-weight source selection; final uncertainty strategy. No interviews, surveys or experiments have been commissioned. No messages have been sent to dataset authors.

## Reproducibility and files

- `scripts/fetch.py`: initial public downloads with status/content-type/hash logging.
- `scripts/replay_downloads.py`: replays the complete recorded download manifest, including the EIGE export POSTs.
- `scripts/profile.py`: Signals and Interviewer structural checks and illustrative endpoints.
- `scripts/profile_sources.py`: Eurostat/EIGE and Spanish survey/meter profiles and preliminary tables.
- `outputs/fetch_log*.json`, `eige_export_log.json`: URLs, access results and checksums. HTTP success is not treated as proof of valid data; the Eurostat outage responses are recorded.
- `outputs/source_profiles.json`, `signals_profile.json`, `interviewer_profile.json`: machine-readable audit results.
- `outputs/*coverage.csv`, `*gender_pairs.csv`, `spanish_preliminary_user_status.csv`: feasibility tables, not finished research results.
- `raw/`: archived source data/docs. Keep raw individual-level material local; public dissemination should use code, citations and approved aggregate outputs.

Run from this workspace: `python3 gender_ai_audit/scripts/profile.py` and `python3 gender_ai_audit/scripts/profile_sources.py`. The Signals script uses the already-existing sibling workspace directory documented above. Package versions are recorded in `outputs/environment.json`; no original author R scripts were executed.
