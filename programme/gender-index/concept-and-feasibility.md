# Gender & AI Index: concept and feasibility review

Prepared for Emily Birch, 30 September 2026. Working proposal, not a completed systematic review or a published index. This memo leaves the existing Eurostat article unchanged.

**Follow-up source audit:** see [additional sources and revised feasibility](additional-sources-audit-2026-09-30.md). It strengthens the case for a workplace-conditions module, adds Eurobarometer, Cedefop, ISSP and ECB leads, and identifies a restriction on novel use of the RPS replication files. Public outcome-study data exist in bounded settings; a population-wide gender series of economic returns is not established.

## Recommendation

Build a continuing, public research resource on gender differences in **participation, patterns of use and experience of generative AI**, with economic consequences as the longer-term research agenda. Use “Gender & AI Index” as a working name, with an explicit generative-AI scope statement. Publish separately identified indicators, source-specific comparisons, a searchable evidence map and original research papers.

Public data support a credible first version. They do not yet support a comprehensive global score of gender equality in AI, nor a global measure of the benefits women and men receive. A single number should be a possible later research output, conditional on a defensible construct and adequate coverage. It should not be a prerequisite for launching the programme.

The strongest contribution would be a resource that tells readers **what we know, for whom, in which setting, with what uncertainty, and how the evidence changes**. Its novelty would need to come from methodological discipline, maintenance and original analyses. The existence of a gender gap is already well established in several research traditions.

## What the Anthropic model offers

The [Economic Index](https://www.anthropic.com/economic-index#us-usage) combines a public explorer, defined measures, downloadable releases and a sequence of research reports. The live page was inspected, including state/country comparisons, usage relative to population, task groupings, use contexts and the data explorer. Its usage index measures activity relative to population share; it is not a comprehensive measure of economic welfare. Task mappings describe the work represented in conversations, not necessarily the jobs of their users.

Its reusable design is: a clear organising question; repeatable measurement; geography/task exploration; visible methods; and papers that deepen the interpretation. Its distinctive advantage is access to proprietary platform telemetry and linked surveys. Our project would instead depend on a carefully curated combination of public sources. The [release repository](https://huggingface.co/datasets/Anthropic/EconomicIndex) provides useful documentation and versioning examples.

The [June 2026 report](https://www.anthropic.com/research/economic-index-june-2026-report) already examines gender in a linked survey and usage sample. Women are 12% of that selected sample, not 12% of the population or necessarily of all Claude users. The report finds differences in product and interaction patterns after occupational adjustment. Those are valuable related results, but we have not verified a public release of the linked respondent-level data needed to reproduce or extend that gender analysis. Public aggregate data and access to the authors' underlying analysis sample are different things.

Our local Economic Index audit checked 27 CSV headers and the earlier release/facet documentation. Those checks did not establish a usable gender dimension. The current June release documentation also does not document gender breakdowns. Adding the female employment share of an occupation would produce an occupational-composition analysis, not reveal the gender of Claude users.

## Proposed organising question

> How does participation in generative AI differ by gender, how does that participation develop into different patterns of use, and what evidence exists about the resulting opportunities and outcomes?

This is a research agenda, not a claim that every transition is observable in current data. Distinguish six concepts:

1. **Access and opportunity:** access to relevant tools, training, workplace permission and useful applications.
2. **Participation:** whether a person uses generative AI within a specified period.
3. **Patterns and intensity:** purposes, tasks, frequency and ways of interacting.
4. **Experience:** perceived usefulness, confidence, barriers, concerns and self-reported gains.
5. **Economic exposure:** how occupational tasks might change with AI. This is context, not demonstrated use or harm.
6. **Realised outcomes:** measured time savings, learning, job quality, earnings or employment effects.

Do not combine these into a causal sequence using unrelated samples. The first release should concentrate on concepts 2–4, with a clearly separated exposure module if its data pass the audit. The follow-up audit also makes access and workplace opportunity a serious candidate module, conditional on joint-variable checks. Realised outcomes can initially appear as an evidence library of bounded studies and explicit gaps, without implying comparable population-wide returns.

AI governance, model-output bias, AI-industry leadership and AI-related harms are important neighbouring subjects. Adding all of them would change the scope from how people adopt and experience AI to gender and AI in its entirety. Record them in the literature map; require an explicit scope decision before adding them as index pillars.

## Data feasibility

“File verified” below refers to the archived September 21 audit and selected checks repeated September 30. “Documentation verified” is not a claim that we downloaded microdata. This review updates the evidence behind the concept; it is not a fresh census of every available release.

| Source | What it can measure | Verification and intended role | Main constraint |
|---|---|---|---|
| Eurostat/EIGE `isoc_ai_iaiu` | Recent use, age and education differences, private/work/formal-education purposes | File verified; core comparable European module; existing article already uses it | Audited data cover 2025 only. Aggregate tables do not provide full joint demographic records or gap standard errors. National fieldwork timing varies. |
| Eurostat/EIGE `isoc_ai_iaiuxr` | Reported reasons for non-use | File verified; separate descriptive module | Eligible non-users are recent internet users without recent generative-AI use. Reasons cannot be interpreted as causal explanations of the adoption gap. |
| OpenAI Signals v2.0 | Name-associated gender representation in consumer ChatGPT messages, by topic and month | File verified; core platform-pattern module | Messages, not unique people. Name classification, not self-identified gender. Privacy noise, suppression and selected coverage. |
| Spanish ChatGPT survey, Ochoa/Fernández Melero/Revilla release | Recalled starting motivations, current/former/never use, reported repetition | File verified; promising dedicated paper and case study | Opt-in quota sample; very short answers; no verified survey weights. Coding quality and survey-specific reuse terms remain gates. |
| Anthropic Economic Index and linked survey findings | Task context; published gender comparisons in selected users | Public documentation/report verified; supplementary research | Audited public aggregate releases do not supply the gender-linked records required for our own equivalent analysis. |
| Anthropic Interviewer public transcripts | Rich accounts of work and AI | File verified; conceptual background | Audited 1,250 transcripts have ID and text only, without structured gender. Not a gender-comparative interview sample. |
| Pew US surveys | Adoption, frequency, confidence and attitudes | Published June 2026 gender report verified; older dataset access route previously verified | Wave 187 microdata access remains unverified. A public report is not an acquired respondent dataset. |
| RPS / Bick, Blandin and Deming | US use intensity, work use and reported time savings | Replication route verified; access/reuse clarification required before novel analysis | The linked INFORMS form restricts use to replication unless permission is obtained. No agreement submitted or data acquired. Joint fields and subgroup precision remain unaudited. |
| ILO exposure index / ILOSTAT | Occupational exposure by sex, using employment composition | Primary publications and data-catalogue listings verified; possible context module | Specific downloadable series, country-year coverage and occupational detail still need file-level checks. Exposure is not job loss or realised benefit. |
| UK DSIT / ONS | National use and attitudes comparisons | Published reports/table access routes verified; potential independent national module | Exact gender crossings and instrument equivalence must be checked in files. Do not append UK rates to Eurostat rankings automatically. |
| EWCS 2024 | Workplace adoption and employment circumstances | Registered researcher access route verified previously | Microdata not acquired; existing research already addresses European workplace gender gaps. A new analysis needs a distinct contribution. |
| Eurobarometer 101.4 / Special 554 | Digital workplace support and broad AI attitudes | Catalogue and source questionnaire verified; strong next acquisition candidate | Broad digital/AI wording does not isolate generative-AI support. Gender coding, routing, design and joint-field precision need verification. |
| Cedefop AI skills survey 2024 | AI skills, training, workplace support and task change | Official design/results verified | Reusable respondent data not located in this pass; not interchangeable with the separate ESJS2 release. |
| ISSP 2024 Digital Societies | AI/robotics attitudes across countries | September 2026 release and questionnaire verified; registered download route | Country field dates and optional-item coverage vary. Not a generative-AI adoption series. |
| ECB Consumer Expectations Survey | Published workplace AI use, barriers and reported savings | Public metadata downloaded and searched | Workplace AI variables were not found in the inspected public guide/metadata. Access to general CES microdata does not establish access to those questions. |

Supporting links: [Eurostat use](https://ec.europa.eu/eurostat/databrowser/view/isoc_ai_iaiu/default/table?lang=en), [EIGE non-use reasons](https://dgs-p.eige.europa.eu/data/information/ta_resdig_dig_intuse__isoc_ai_iaiuxr), [Signals release and dictionary](https://openai.com/signals/data-download/), [Spanish OSF release](https://osf.io/gpc5u/), [Interviewer release](https://huggingface.co/datasets/Anthropic/AnthropicInterviewer), [Pew report](https://www.pewresearch.org/internet/2026/06/17/the-gender-gap-in-ai/), [RPS author data link](https://sites.google.com/view/blandin/research), [GenAI Adoption Tracker](https://www.genaiadoptiontracker.com/), [ILO index](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure), [ILOSTAT catalogue](https://ilostat.ilo.org/data/?cat_mode=database), [DSIT survey](https://www.gov.uk/government/statistics/dsit-public-engagement-survey-20252026/dsit-public-engagement-survey-20252026), [EWCS access documentation](https://doc.ukdataservice.ac.uk/doc/9511/read9511.htm).

### Concrete feasibility checks

- The archived Eurostat use table has 35 country/territory codes plus the EU aggregate. Our existing paper uses the EU27 core; extensions remain separate. There is no verified multi-year Eurostat AI trend in this snapshot.
- Signals has a complete global 24-month × seven-topic panel, July 2024–June 2026. The country-topic file contains some observations for 86 countries, but only eight countries have every month/topic cell in that full period: Brazil, Canada, Germany, France, Great Britain, India, Mexico and the US. Coverage is an analytical choice, not a reason to silently interpret suppressed cells as zero. Shorter-period and unbalanced analyses are possible if prespecified and labelled.
- The Spanish survey has 2,102 completed responses. Among ever-users, 1,014 provided starting-motivation text. The median response is only 18 characters. This supports testing a limited motivation taxonomy; it does not justify promising a rich qualitative paper before the coding pilot.
- Public Interviewer files contain `transcript_id` and `text`. Inferring gender from names, occupation, writing or selected self-disclosures would not repair the missing comparison variable.

These checks establish feasible units of analysis, not results for a new index.

## What to measure first

For a fixed survey population and period, retain women's and men's use rates and the source categories verbatim. Show:

- **Absolute gap:** male rate minus female rate, in percentage points, matching the existing paper. Negative values mean higher female use.
- **Relative gap:** 100 × (male rate minus female rate) / male rate, matching the existing paper. Undefined if the male rate is zero; do not replace it with a fabricated value.
- **Optional parity ratio:** female rate / male rate, with 1 indicating parity. Keep this secondary to avoid unnecessary terminology. Ratios above 1 should remain visible.

Always show the underlying rates. Equal use rates of 5% and equal use rates of 80% have the same parity but very different levels of participation. A closing gap could also arise because men's use falls. Neither equality nor increasing use alone proves improved welfare.

For Signals, use different labels: feminine-name message share and its difference from the same month's overall feminine-name message share. The released topic table measures the name-category composition **within a topic**, not the share of women's activity devoted to that topic. Do not turn it into preferences, population uptake or within-person changes. The overall and topic comparison is meaningful only within the documented compatible release and name-classifiable population.

Avoid a single composite in version 1. Its weights would impose a value judgment about how adoption, confidence, exposure and outcomes substitute for each other. More automation, more confidence or less occupational exposure is not unambiguously better. Before any later composite, define the construct and direction of each indicator; assess missingness, dependence, normalisation and weights; and publish ranking sensitivity. The [OECD/JRC handbook](https://www.oecd.org/en/publications/handbook-on-constructing-composite-indicators-methodology-and-user-guide_9789264043466-en.html) provides the relevant methodological framework.

## Triangulation: what it should mean

Start with a common conceptual dictionary, then preserve source-specific estimands. Each observation should retain its original question, population, geography, field dates, reference period, tool scope, numerator, denominator, gender/sex measurement, sampling design, weighting and uncertainty information. Record release version, access conditions and licence as well.

Classify comparisons as:

1. **Directly comparable:** sufficiently aligned measurement and population to support a stated comparison.
2. **Informative alongside one another:** related constructs, but different denominators, instruments or selected samples. Show separately.
3. **Unsuitable for the intended claim:** no gender variable, no relevant outcome, uninterpretable selection, or insufficient detail.

Agreement between different sources can strengthen a qualitative interpretation, but does not make their percentages interchangeable. Disagreement is often informative about selection, reference windows or task definitions. For example, a majority feminine-name message share within one platform can coexist with lower population adoption among women because participation, platform choice and messages per user differ. The available sources cannot automatically separate those contributions.

Do not average survey participation, message shares, workforce representation and exposure scores. Do not multiply separate demographic and task margins to invent joint observations. Do not fill countries without evidence by inferring use from income or general gender equality. Literature reports that reuse the same survey are not independent corroboration.

A meta-analysis may eventually be appropriate within a carefully defined family of compatible studies. It requires explicit inclusion rules, overlap checks, usable uncertainty and a defensible target population. A random-effects model does not itself solve incompatible measures or generate a representative world estimate.

## Existing work and differentiation

- [Cranney, Delecourt and Koning](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6880085) synthesise 76 sources from over 100 countries. This is a central overlap check. An undifferentiated literature compilation would add little. Our proposed distinction is maintained, inspectable indicator series, explicit comparability and original analyses of heterogeneity.
- [Pew's gender report](https://www.pewresearch.org/internet/2026/06/17/the-gender-gap-in-ai/) already addresses use and experience in the US. It should guide measurement design and identify what our own studies must add.
- [Henseke's European workplace paper](https://arxiv.org/abs/2604.18849) already links occupational exposure and workplace adoption across countries. Repeating “women's adoption is lower” would be insufficient.
- The [ILO's 2026 gender brief](https://www.ilo.org/publications/gen-ai-occupational-segregation-and-gender-equality-world-work) directly addresses occupational segregation and exposure. Any exposure module should attribute this work, and any exposure paper needs a more specific incremental question.
- The [Global Index on Responsible AI](https://www.global-index.ai/) includes gender-equality policy and inclusion indicators. It is an adjacent governance project, not interchangeable with measures of people's use and benefits.
- Search also located an existing [Women in AI Index quarterly report](https://empressa.ai/wp-content/uploads/2025/11/Women-in-AI-Index-Quarterly-Report-Q4-2025.pdf). Its existence and title were verified in search; full document retrieval exceeded the tool's size limit. Its methodology has not been assessed here. This is enough to rule out an unqualified claim to the first gender/AI index, and it should be reviewed before deciding on branding.
- [Bick, Blandin, Deming and Schumacher's “What Work Does Generative AI Do?”](https://sites.google.com/view/blandin/research) is a newly identified task-level survey lead. Its distinction between worker-reported adoption and platform task classification is directly relevant to our measurement design; the linked data still need auditing.

The next literature pass should cover adoption/diffusion, gender and digital inequality, workplace practices, unpaid work, experience and trust, causal benefits, and measurement/index construction. Record searches, screening decisions, study versions and dataset families. Include null findings and female advantages, and distinguish probability surveys, opt-in surveys, behavioural records, qualitative work, experiments and modelled exposure. This review has not yet done that systematic screening.

## Three research papers within the programme

### 1. Where is the gender gap in generative AI use widest?

Keep the existing article focused: European household participation across countries, age groups and contexts, with sensitivity to gap definition and age composition. Its contribution is careful comparison within one harmonised source. It supplies the first reproducible index module. It should not be expanded into an umbrella manifesto or have a causal “why” section added back in.

### 2. Does convergence in overall representation conceal differences across AI tasks?

Use Signals to examine how topic-specific feminine-name message shares evolve relative to the platform-wide baseline. Begin with the complete global panel and prespecify any country extension. Report coverage and privacy limitations. Assess whether task differences narrow, persist or change as overall representation changes; do not frame this as a claim about inherent preferences.

The novelty gate is whether a carefully defined longitudinal comparison adds materially to the provider's existing dashboard and research. A static reproduction of its topic chart is insufficient. Uncertainty cannot be invented from the overall message sample count; absent subgroup counts and the relevant noise information, descriptive trends and sensitivity checks must be labelled accordingly.

### 3. What brings people to ChatGPT, and who keeps using it?

The Spanish survey gives this a concrete public-data foundation. Pilot 100–150 responses, code in Spanish, hide gender from coders, allow ambiguity and multiple codes, and assess agreement with independent human coding. Estimate sample-specific differences in reported motivations and associations with current versus former use or repetition, respecting routing and missingness. Any adjustment should use a small prespecified set of available covariates.

Recalled motivation is not an observed first task; current status is not longitudinal retention; associations are not causal pathway effects. The opt-in sample cannot support unqualified national prevalence claims. Verify survey-specific terms before quoting or redistributing text.

This paper remains conditional on sufficient codable material and a distinct contribution beyond the original authors' work. If the pilot is weak, publish a bounded methods note or do not proceed. A null gender difference is a valid result; insufficient measurement is a different problem.

**Alternatives to compare before fixing slots 2–3:** an EWCS/Eurobarometer workplace-conditions paper, or a participation/intensity/reported-savings paper using RPS if a permitted access route is established. These could connect more directly to economic opportunity. They should replace, rather than automatically add to, a proposed paper if the data and novelty are stronger. RPS replication terms currently prevent treating novel reuse as assured; the ECB's inspected public metadata also did not establish access to its workplace AI questions. Necessary joint fields and sample precision remain unverified. A causal-benefits paper would require an appropriate experiment or credible quasi-experimental design.

These are three distinct contributions under one programme. They do not follow the same people from discovery through use to benefit, and they should not be presented as proving that sequence. Scope alone cannot guarantee three publication-quality papers.

## What the first public release would contain

1. A short landing page explaining scope and the questions the evidence can answer.
2. A participation explorer using the existing EU study, with absolute/relative options and both underlying rates.
3. A separate platform-pattern explorer that visibly identifies message units and name-associated categories.
4. Source-specific case studies of experience and reported barriers; no unsupported worldwide league table.
5. A coverage matrix showing missing countries, periods, identities and outcomes.
6. A methods/code/data-download section, with source attribution and redistribution conditions.
7. Standalone research articles linked to the exact data release behind each figure.

Each indicator needs an “evidence card”: question answered, population, measure, dates, gender variable, source, uncertainty, exclusions, comparability and next-update status. Public access should distinguish open downloads, free-registration access, requests and restricted access. Dataset availability is not the same as an unrestricted redistribution licence.

A static, versioned first edition is enough. Update when eligible source releases arrive, retain previous editions, and label field dates separately from publication dates. Do not promise a quarterly refresh when the foundational survey currently provides one audited year. Changes in questionnaires, platform coverage and classifications must create explicit series breaks where needed.

## Scientific quality and decision gates

**Gate 1 — Scope and contribution.** Finalise the construct map; identify the specific improvement over existing syntheses, dashboards and gender reports. Select useful questions for researchers and policymakers, not simply visually appealing rankings.

**Gate 2 — Actual data and permitted reuse.** Follow the [revised acquisition order](additional-sources-audit-2026-09-30.md): prioritise EWCS/Eurobarometer, finish current Pew/UK checks, and clarify Cedefop/ECB releases and RPS reuse permissions. Retain ILO's precise series and Spanish survey documentation on the existing audit queue. Inspect codebooks, routing, design and weights; profile joint variables, subgroup sizes, missingness and longitudinal structure; reproduce a published benchmark. Refresh metadata without silently replacing the first paper's frozen inputs.

**Gate 3 — Minimal measurement prototype.** Build a small indicator registry and coverage matrix from already secured files. Demonstrate one comparable survey series and one clearly separated platform series. Test denominator and sign conventions, failure handling and traceability before building a polished website.

**Gate 4 — Analysis plans.** Specify estimands, primary comparisons, inclusion rules, sensitivity checks and uncertainty methods before the substantive new analyses. Disclose earlier exploration. Decide how multiple comparisons, selective reporting, overlapping samples and classification error will be handled. An index itself is descriptive infrastructure; stronger causal language requires stronger designs.

**Gate 5 — Independent review and release.** Have a methods reviewer audit claims and reproducibility; have a gender-measurement reviewer assess construct validity and omissions. Preserve binary-category limitations rather than calling them full gender coverage. Separate human review from AI-assisted checking. Publish null findings, coverage failures and corrections alongside substantive results.

Do not launch a composite if rankings are highly sensitive to arbitrary weights, missing-data choices or inconsistent denominators. Do not promise a paper whose essential variables or permissions are unresolved. Do not delay the completed first paper merely to complete the larger platform.

## What has actually been completed in this review

Reviewed the live Anthropic explorer, current release documentation and June gender results; consulted the repository's original-report and release audits; revisited the gender-data audit; rechecked the Signals file schema and coverage; and conducted targeted primary-source searches on existing projects, literature and candidate data. Produced this design and decision framework. No new gender effects, global ranks or composite scores were estimated. No external contacts were made, and no new repository or website was published.

Local evidence: [prior full data audit](../../gender_ai_audit/AUDIT_AND_SERIES.md), [source profiles](../../gender_ai_audit/outputs/source_profiles.json), [Signals profiles](../../gender_ai_audit/outputs/signals_profile.json), [country-topic coverage](../../gender_ai_audit/outputs/signals_complete_country_topic_panel.csv), [existing study's literature notes](../../gender-gap-generative-ai/notes/literature-and-definitions.md), [Economic Index release audit](../../economic_research/reference/sources/data-audit.md).
