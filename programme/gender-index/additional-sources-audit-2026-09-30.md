# Gender & AI Index: additional sources and revised feasibility

30 September 2026. Targeted follow-up to the [concept review](concept-and-feasibility.md), prompted by Emily's six-pillar table. This is a source and access audit, not a completed systematic review or a new analysis of gender differences. It leaves the first article unchanged.

## Decision

The six pillars are a useful research framework. The evidence is wider than the initial shortlist suggested, particularly for workplace conditions, attitudes and selected outcomes. However, **published findings, released variables and permission to perform a new analysis are three separate checks**.

Keep the programme ambitious, but organise it as separately documented indicators and research studies. More sources improve the evidence map; they do not automatically make a global composite valid.

## Revised pillar assessment

| Pillar | Sources and useful additions | What is defensible now | Main qualification |
|---|---|---|---|
| Participation | Eurostat/EIGE; Pew; national surveys; RPS reports; literature synthesis as a source-finding tool | Strong foundation for source-specific comparisons, especially Europe and the US | Preserve population, field dates, reference period and tool definition. Do not count a synthesis and its underlying surveys as independent evidence. |
| Patterns and intensity | Eurostat purposes; Signals; Spanish survey; potentially RPS and ECB | Survey purposes and selected platform activity can be examined separately | Eurostat measures survey respondents' sex categories; Signals infers name categories and counts messages. The proxy problem does not apply equally to both. |
| Exposure of work | ILO/ILOSTAT; Anthropic occupational exposure plus employment composition | Useful contextual indicators of potential task exposure or exposure informed by observed platform activity | Exposure does not establish individual adoption, displacement, earnings loss or benefit. Occupational sex composition does not identify the gender of platform users. |
| Conditions and opportunities at work | EWCS 2024; Eurobarometer 101.4; Cedefop AI skills survey; OECD worker survey | A credible and important pillar, with promising survey evidence on support, training and job circumstances | Registration is an access condition, not evidence of weak survey design. Some questions concern digital technologies or AI broadly; access and exact joint fields still differ by source. |
| Outcomes and returns | Public experimental packages; academic productivity study; RPS/ECB published time-savings analyses; EWCS job-quality measures | An evidence library of bounded outcome studies is feasible | A comparable population-wide gender series of realised economic returns is not established. Separate perceived savings, measured performance and causal effects. |
| Attitudes, confidence and trust | Pew; UK tracker; Eurobarometer; ISSP 2024 Digital Societies | Several credible sources support gender comparisons once files and weights are verified | Broad AI/robotics attitudes, generative-AI trust, digital confidence and demonstrated proficiency are different constructs. Greater optimism is not automatically a better outcome. |

Sources and access evidence supporting this assessment are documented below. The first three rows also draw on the [earlier file audit](../../gender_ai_audit/AUDIT_AND_SERIES.md).

## Sources worth adding or upgrading

### 1. Eurobarometer 101.4 / Special Eurobarometer 554: workplace support and attitudes

The [GESIS catalogue](https://www.gesis.org/en/eurobarometer-data-service/data-and-documentation/standard-special-eb/study-overview/eurobarometer-1014-za8844-april-may-2024) identifies ZA8844, fielded April–May 2024, and links data access and documentation. The report's 2025 publication date must not be used as its observation year.

The [source questionnaire](https://access.gesis.org/dbk/79074) was inspected. Its scripting identifiers include:

- ST0753: self-assessed ability to use digital technologies in several settings.
- ST0754: whether employers provide tools or training for digital technologies, including AI; asked of an employee subset.
- ST0755: awareness of employer use of digital technologies for managing work.
- ST0756–57: perceptions of AI/robots and their implications.

These are useful for support and attitudes. They do **not** isolate generative-AI training, and the tools-or-training item does not separate those two inputs. The scripting IDs must be mapped to released variable names before analysis. Catalogue and questionnaire verified; respondent data, gender coding, weights and country-by-gender precision not profiled here.

**Priority:** high. Ask whether women and men report different workplace support within comparable employment settings. Interpret adjusted gaps descriptively; they do not establish that support causes adoption differences.

### 2. EWCS 2024: upgrade its importance, retain an originality test

[Eurofound](https://www.eurofound.europa.eu/en/surveys-and-data/surveys/european-working-conditions-survey/ewcs-2024/) describes a probability survey of 36,644 workers in 35 countries. Its [AI topic page](https://www.eurofound.europa.eu/en/topics/artificial-intelligence) confirms questions about generative-AI use and workplace technologies. The [UK Data Service record](https://doc.ukdataservice.ac.uk/doc/9511/read9511.htm) confirms registered access under an End User Licence and a revised release adding job-quality indices.

This is a strong candidate for studying adoption alongside job circumstances. Microdata have not been acquired; the complete questionnaire and release schema still need inspection. Do not presume every training item is AI-specific or read job-quality associations as effects of AI.

[Henseke's existing paper](https://arxiv.org/abs/2604.18849) already studies exposure, adoption, workplace conditions and gender. Its overlap means we should define the incremental question before committing a second paper to these data.

**Priority:** high for the index; conditional for an original paper. Access-gated should not be used as shorthand for methodologically weaker.

### 3. Cedefop AI skills survey: a valuable new lead, not yet a ready dataset

The official [survey background note](https://www.cedefop.europa.eu/files/background_note_ai_survey-brx_seminar-2024-06-24.pdf) documents 5,342 employees aged 16–64 in 11 EU countries, surveyed February–May 2024 using probability-based panels. It excludes self-employed and family workers. The [first findings](https://www.cedefop.europa.eu/en/publications/9201) cover AI use, skills, employer support and task change.

This offers unusually relevant constructs for the workplace pillar. A reusable public respondent file was **not verified** in this pass. Public ESJS2 data from 2021 are not evidence that this separate 2024 AI survey has been released. Broad-AI measures also need to remain distinguishable from generative-AI measures.

**Priority:** high access enquiry if a documented download cannot be found. No enquiry has been sent. Do not make the programme depend on access until obtained.

### 4. ISSP 2024 Digital Societies: wider geographical coverage for attitudes

[GESIS](https://www.gesis.org/en/issp/data-and-documentation/digital-societies) lists the first integrated release, ZA10020 v1.0.0, dated 11 September 2026, with download after registration. The [questionnaire](https://access.gesis.org/dbk/82219) includes concern about job replacement and comfort with selected AI/robotics applications. Some additional AI questions are optional.

This could extend the attitudes module beyond Europe and the US. Country fieldwork dates vary substantially despite the “2024” label. Participating countries are not necessarily all present in a given release; inspect the integrated file and optional-item coverage. Respondent data and gender/background coding have not yet been profiled.

**Priority:** medium to high for contextual attitudes. It is not a direct generative-AI adoption series.

### 5. ECB Consumer Expectations Survey: relevant published results, missing public workplace fields in the inspected release

The [August 2026 ECB article](https://www.ecb.europa.eu/press/blog/date/2026/html/ecb.blog20260826~e1c1a89999.en.html) discusses workplace AI use, tasks, barriers and reported time savings across 11 euro-area countries. These are highly relevant constructs.

I downloaded the metadata archive and microdata guide linked from the [official access page](https://www.ecb.europa.eu/stats/ecb_surveys/consumer_exp_survey/html/data_methodological.en.html). The variable and category-label workbooks cover nine modules. Searches identified the background gender field `a1020_prec` and an AI response category within financial-advice question `f1003`, but did not identify the workplace AI use or time-savings fields discussed in the article. The guide search produced the financial-advice reference only.

This is a finding about the inspected public documentation, not proof that the workplace data can never be accessed. Public CES microdata in general do not establish public availability of every topical question. Save this as published evidence and an access lead; do not promise a gender-by-time-savings analysis yet. Any reported savings would remain self-reported, rather than an experimentally identified productivity effect.

**Priority:** targeted release/access clarification. Local metadata and search results are in `audit-sources/`.

### 6. RPS: a material correction to the initial recommendation

The [published paper](https://pubsonline.informs.org/doi/10.1287/mnsc.2025.02523) and [supplement](https://pubsonline.informs.org/doi/suppl/10.1287/mnsc.2025.02523) advertise replication files. Following that link reached an [INFORMS download form](https://services.informs.org/dataset/mnsc/download.php?doi=mnsc.2025.02523).

The displayed terms restrict files to verifying the original results; other use requires explicit permission from the relevant authors or data originators. I did not submit the agreement or identifying details. The retrieved response was HTML, not a data archive. These terms do not establish whether a separately licensed release exists elsewhere.

**Revised decision:** RPS remains substantively valuable, but novel reanalysis is conditional on a permitted access route, followed by a joint-variable audit. Published aggregate results can inform the evidence review. The original memo's “highest-priority acquisition” should not be read as approval to reuse the replication package for a new paper.

### 7. OECD worker and employer surveys: contextual, with scope and access checks

The [OECD's 2023 report](https://www.oecd.org/en/publications/the-impact-of-ai-on-the-workplace-main-findings-from-the-oecd-ai-surveys-of-employers-and-workers_ea0a0fe1-en.html) analyses 2022 worker and employer surveys in finance and manufacturing across seven countries. These support discussion of training, implementation and worker experiences.

They predate ChatGPT's public launch and concern AI broadly. The worker and employer surveys cannot be assumed to be matched employee–employer records. No reusable public microdata route was verified here. Include in the literature map and contextual evidence, with less acquisition priority than EWCS or Eurobarometer for this programme.

## Correcting the outcomes row

“None public at scale” is too categorical unless the intended outcome and population are specified. There are at least three evidence types:

1. **Reported benefits:** perceived time savings or usefulness, as in RPS/ECB reports. Availability of joint gender data and permission for new analysis remain separate questions.
2. **Measured task performance under experimental assignment:** [Noy and Zhang](https://shakkednoy.com/Noy%20Zhang%20NBER%20SI.pdf) study writing performance and time in a bounded professional sample. Their [OSF package](https://osf.io/xd7qw/) is public; this audit verified raw-file listings and inspected a survey header. It has not established a usable gender variable, subgroup power or reuse licence for a new analysis. An average treatment effect does not establish a gender difference in treatment effects.
3. **Observed outcomes in a specific sector:** the [PNAS Nexus academia study](https://academic.oup.com/pnasnexus/article/4/2/pgae591/7996465) links its data to OSF. Study folders were accessible using the article's public view link, but data were not profiled. Its publication analysis infers gender from names and does not directly observe individual ChatGPT use. Its design therefore requires critical causal assessment; it cannot supply a population-wide gender return to AI.

**Suggested row wording:** “Public evidence exists for selected experiments, occupations and reported benefits; comparable population-wide gender differences in realised economic returns remain poorly covered.”

Employment, income or job-quality variables in a survey are not automatically outcomes caused by AI. A public outcomes library can be useful before there is a defensible recurring outcomes indicator.

## Literature and adjacent indices

Treat the Otis synthesis as a guide to underlying sources, not another independent national survey. Working-paper versions matter: the [current HBS PDF](https://www.hbs.edu/ris/Publication%20Files/25-023_be8fb517-3dd5-40aa-97f9-4e42e1c8e6ff.pdf) is titled *Global Evidence on Gender Gaps and Generative AI Over Time* and credits Cranney, Delecourt and Koning. Record the version actually used and deduplicate its underlying datasets.

The [Global Index on Responsible AI](https://www.global-index.ai/) includes gender-equality policy and mobile-internet-gap indicators. It is useful for institutional context and index presentation. Those measures cannot substitute for women's and men's generative-AI adoption or benefits. Reusing a contextual score also requires tracing its underlying source to avoid double-counting.

## Next acquisition order and paper decisions

1. **EWCS and Eurobarometer:** acquire through their documented research routes, inspect questionnaire/routing and gender variables, reproduce one benchmark, then assess an original workplace question against existing studies.
2. **Current Pew and UK sources:** finish the already identified access and joint-field checks, rather than accumulating more report titles.
3. **Cedefop and ECB:** resolve specific release/access questions. They have high substantive relevance but are not established analysis inputs.
4. **RPS:** locate a separately permitted release or obtain author/data-originator permission before novel reanalysis.
5. **ISSP and outcome-study packages:** audit for well-defined secondary modules, including geographical coverage, gender coding, power and reuse terms.

For every candidate, record access, licence, target population, field dates, AI definition, gender measurement, question routing, weights/design, joint variables, subgroup sizes, missingness and previous use. Only after these checks should a source graduate from literature evidence to an analytical dependency.

The existing Eurostat article remains paper one. A workplace-conditions paper deserves consideration alongside the proposed Signals paper and qualitative pilot. This audit is a reason to reopen that comparison, not yet a reason to commission an additional paper or promise three independently novel results.

## Audit trail

This pass checked primary catalogues, questionnaires and reports; downloaded ECB documentation; inspected the RPS access terms; and inspected OSF file listings and a survey header. No new gender gaps or causal effects were estimated, no microdata agreements were submitted, and no external messages were sent.

Local files include `ecb_metadata.zip`, `ecb_microdata_guide.pdf`, `ecb_metadata_ai_search.json`, `rps_reuse_terms.txt`, OSF listing JSONs and `noy_survey_schema.json`. Acquisition failures were kept distinct from non-availability: Eurofound returned a size limit/rate limit through the attempted routes, and the RPS journal site restricted direct retrieval while its download form remained readable. Hashes are recorded in `audit-sources/manifest.json`.
