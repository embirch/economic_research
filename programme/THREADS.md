# Threads of inquiry in Anthropic's economics stream

Corpus snapshot: **2026-09-16**. Written from the 38 files in `wiki/reports/` (covering the 49 entries in
`wiki/INDEX.md`), plus `data/ATLAS.md` for the reach-of-data lines and
`room/steward-2026-09-16-question-batch-answers.md` for the steward's answers to ten standing questions.

## How to read this map

**What a thread is.** A thread is a line of inquiry the economics stream has pursued across more than one
publication, with (i) its own construct or measure, (ii) at least two publications that build on each other,
and (iii) a question it has not closed. A single paper with no successor is not a thread; it is recorded
inside the thread whose measure it uses. Threads are not the same as Anthropic's own four Institute focus
areas: the whole of this map sits inside one of those areas, "Economic diffusion" (`institute-agenda-2026-05`,
*Lead ¶2*, *ED intro ¶1–¶2*).

**How "established" and "open" are judged.** *Established* means a finding stated with a number in a
publication, by that publication's own words, with the source's page or figure reference. Firmness is graded
in three bands, and the band is stated for every established finding:

- **repeated** — the same quantity measured in three or more waves or reproduced by a second publication;
- **single-wave** — measured once, with no replication inside the corpus;
- **asserted** — stated in prose without a published number, or carried only by a hyperlink to another
  publication.

*Open* means the corpus itself says the question is unanswered: a "more research is needed", a named
limitation, an untested conjecture, a promised follow-up not yet delivered, or a cut the publication had the
data to make and did not. Items sourced from a publication's own words are quoted; items that are the wiki
author's inference are marked **[inference]** and taken from the "What it did not test" section of the wiki
file named, which is itself marked as inference there.

**Citation convention.** `slug` + the page, figure, footnote or section reference **as recorded in that
slug's `wiki/reports/` file**. No number appears in this map without such a reference. Where a wiki file
records that a number exists in two forms, both are given. No data file was opened for this map; every
statement about what the released data can and cannot do is cited to `data/ATLAS.md` or to the steward's
answer note, and where the atlas is silent the line is flagged `steward?`.

**Departures from the candidate list in `team/SETUP.md` §5 row 0.4, and why.**

| Candidate | What this map does | Why |
|---|---|---|
| adoption and diffusion | kept as T1 | the task-concentration and enterprise/consumer series are its own object |
| geography | kept as T2, separate from T1 | it has its own measure (the AUI), its own model (state convergence), three dedicated spotlights, and a result that runs opposite to T1's |
| automation versus augmentation | kept as T3 | the collaboration facet is the one taxonomy unchanged across all six waves (`data/ATLAS.md` §Conventions, "A like-for-like automation comparison twelve months apart does exist") |
| task-level primitives and productivity | **split** into T4 (primitives and productivity) and T8 (measurement and methods) | the pipeline itself became a subject of publication — a two-step O\*NET classifier, an artifact classifier, a taxonomy-vintage change and an external-access pilot — with its own promises and its own unmeasured validation |
| labour-market exposure and observed impacts | kept as T5 | one measure, one paper, one appendix, and a growing set of downstream uses |
| learning curves and skill | kept as T6 | tenure, expertise, fluency and the skill-formation trial share a construct |
| the survey and self-reported effects | kept as T9 | four publications and a standing monthly instrument |
| — | **added** T7 agentic coding and the agentic surfaces | ~400k-session and ~200k-transcript studies, two surface-comparison reports and a social-science survey; the largest body of economics work outside the Index, and the one the Institute cites as its evidence that "jobs like software engineering are changing radically" (`institute-agenda-2026-05`, *Lead ¶4*) |
| — | **added** T10 retraining, adjustment and policy | a 124-page evidence review, a tiered policy framework, a nine-category policy post and a $200M research agenda |
| — | **added** T11 scenarios and macro aggregation | two publications in September 2026 plus the Hulten aggregation of November 2025; it is where the stream states what its usage measures imply for GDP |
| — | nothing dropped | every candidate had at least two publications behind it |

Eleven threads. Publications appear in more than one thread where they carry more than one measure; the
count of distinct `wiki/reports/` files mapped is in `## Verification`.

---

## The threads

### T1 · Adoption and diffusion: what AI is used for, and by whom

**(a) Publications, in date order.** `economic-index-2025-02-report`; `economic-index-2025-02-paper`;
`economic-index-2025-03-report`; `economic-index-2025-04-software-development`;
`economic-index-2025-09-report`; `economic-index-2025-09-blog`; `economic-index-2026-01-report`;
`economic-index-2026-01-blog`; `country-brief-india-2026-02`; `economic-index-2026-03-report`;
`economic-index-2026-03-appendix`; `economic-index-2026-06-report`; `economic-index-2026-06-appendix`;
`programme-and-product-pages` (`economic-index-connector-2026-07`, `economic-index-hub-page`).

**(b) What is established.**

- **Usage is concentrated in a small number of tasks, and the concentration series is now five waves long
  — repeated.** Share of conversations in the ten most prevalent O\*NET tasks, Claude.ai: 21% (Jan 2025),
  24% (Mar 2025), 23% (Aug 2025), 24% (Nov 2025), 19% (Feb 2026) (`economic-index-2026-03-report`, Fig 1.1
  p.5). First-party API: 28% (Aug 2025), 32% (Nov 2025), 33% (Feb 2026) (same figure; the Discussion states
  it as "up from 28%", p.19).
- **Coding is the largest single domain on both surfaces, and the two surfaces have diverged — repeated.**
  Computer and Mathematical tasks were 37.2% of queries in the first paper (`economic-index-2025-02-paper`,
  p.6, Fig 2 p.5); on Claude.ai the share is "down from a peak of 40% in March 2025 to 34% in November
  2025" while the API "edged higher from 44% in August to 46% in November 2025"
  (`economic-index-2026-01-report`, p.7); by February 2026 the Claude.ai figure is 35% on 2019 O\*NET-SOC
  codes (`economic-index-2026-03-report`, claim 3, p.5, evidenced in the appendix) and "Since August 2025,
  the share of tasks in this category has increased by 14% in the API and decreased by 18% in Claude.ai"
  (p.7).
- **Depth of use inside occupations is rising but shallow — repeated, on a cumulative measure.** "∼36% of
  occupations using AI for at least a quarter of their associated tasks" and "Only ∼4% of occupations show
  usage for at least 75%" (`economic-index-2025-02-paper`, abstract p.1 and p.7, Fig 4 p.7); "Combining
  across reports, 49% of jobs have seen AI usage for at least a quarter of their tasks"
  (`economic-index-2026-01-report`, p.43); at February 2026 the three thresholds read 49% / 24% / 7%
  (`economic-index-2026-03-appendix`, Fig A.2 p.5, printed data labels).
- **Consumer and enterprise surfaces differ in what they are used for — repeated.** API usage is 74% work
  against 46% on Claude.ai, and Computer & Mathematical 52% against 36% (`economic-index-2026-01-report`,
  pp.26–27); Office and Administrative Support tasks on the API "rose 3pp in August to 13% in November 2025"
  (p.8).
- **The Claude.ai use-case mix has moved away from coursework — single-wave comparison.** "Coursework fell
  from 19% to 12% of conversations, while personal use rose from 35% to 42%"
  (`economic-index-2026-03-report`, Fig 1.2 p.6), with part of the coursework fall attributed to academic
  calendars: 5pp where term was active against 12pp where students were on break (fn 3, p.11).
- **Firm-level adoption, measured by others, is low and rising — single-wave, external data.** Census BTOS
  AI adoption "rising from 3.7% in fall 2023 to 9.7% in early August 2025"
  (`economic-index-2025-09-report`, p.31, Fig 3.1); the scenario paper's own anchor is "In late 2025, 18
  percent of firms used AI (32 percent employment-weighted)" (`econ-scenarios-paper-2026-09`, p.27).
- **The Index's own statement of what it does and does not represent — asserted, and repeated in the
  product voice.** "the Index reflects patterns in Claude usage rather than the labor market as a whole"
  (`programme-and-product-pages`, `economic-index-connector-2026-07`, final paragraph).

**(c) Where it is open.**

- **Why adoption differs at all.** Five candidate factors are listed and none tested: digital
  infrastructure, economic structure, regulatory environment, awareness and access, trust and comfort
  (`economic-index-2025-09-report`, pp.17–18).
- **The 2025-03 fork, never resolved.** The rise in non-coding categories "could reflect either ongoing
  diffusion of AI throughout the economy, novel applications of coding to those domains, or unexpected
  capability improvements in the model" (`economic-index-2025-03-report`, §"What's changed…", also OQ 1).
- **Composition against behaviour.** No wave decomposes a share change into new users arriving and existing
  users changing (**[inference]**, `economic-index-2025-09-blog` item 1; `economic-index-2026-01-report`
  item 10). The February 2026 window is the sharpest case: the report names two shocks, winter school breaks
  (fn 3, p.11) and "the release of our Super Bowl advertisements, which brought many first-time users"
  (fn 3, p.18), and reweights for neither outside the coursework figure.
- **Firm-level adoption inside Anthropic's own data.** The corpus has no firm unit of observation; the
  January 2026 blog file records the constraint in the report's own terms — the unit is a conversation, so
  concentration claims "cannot be decomposed into adoption breadth versus intensity"
  (`economic-index-2026-01-blog`, What it did not test 3).
- **Emergent tasks.** Named as a limitation from the first paper — O\*NET "cannot capture emerging tasks and
  occupations that AI systems such as Claude may create or transform" (`economic-index-2025-02-paper`,
  p.12) — and as an Institute question (`institute-agenda-2026-05`, `ED-7`). No publication attempts a
  measure.
- **The bottom-up taxonomy's stated purpose is unfulfilled.** The 630-cluster release "enables comparisons
  between top-down and bottom-up approaches" and the comparison "is not performed in the report"
  (`economic-index-2025-03-report`, OQ 4; What it did not test 9).

**(d) What the Institute says it wants next.**

- `ED-1` "Who adopts AI?": "What determines whether a country, region, or city can access AI? If it can
  access it, how does it capture economic value from AI? … How do free or open weight models contribute to
  this dynamic?" (`institute-agenda-2026-05`, Definitions 15).
- `ED-2` "Adoption in firms:" — "What causes AI adoption at the firm level, and what are the consequences?
  … How concentrated is AI usage across firms? How do changes in concentration of AI adoption translate into
  markups and labor share?" (ibid., Definitions 16).
- `ED-3` "Is AI a general purpose technology?" — "adoption is fastest in high-margin commercial
  applications, and slowest where social returns exceed private returns?" (ibid., Definitions 17).
- `ED-7`: "What new tasks and jobs could emerge as AI automates existing parts of the economy?" (ibid.,
  Definitions 21).
- `Share 1`: "More granular information from The Anthropic Economic Index, at a higher cadence … We'll try
  to be an early warning signal for significant change and disruption." (ibid., Definitions 6).
- Economic Futures programme page, Group 1: "Labor market transitions", "Productivity effects",
  "Democratization of capabilities" — "How is AI lowering barriers to entrepreneurship and creative work?"
  (`programme-and-product-pages`, Open questions, the twelve research questions).
- Research Fund priority 1, "Shaping AI's impact on workers at the firm and workplace level": "The existing
  evidence on AI's integration in the workplace is observational and short-term." (ibid.,
  `economic-futures-research-fund-2026-07`, priority 1 rationale).

**(e) The mentor's interests ⟨mentor⟩.** Massenkoff is a lead author of the report that introduced the
five-wave concentration series and the wage-based task-value series (`economic-index-2026-03-report`, p.1,
Figs 1.1 and 1.4) and of the wave that split usage across surfaces by cadence
(`economic-index-2026-06-report`, p.1). ⟨mentor⟩ His stated reading of the diffusion pattern is an
adoption-curve one: "The pattern is consistent with a standard 'adoption curve' story, in which early
adopters favor specific high-value uses like coding, and later adopters take on a much wider range of
tasks." (`economic-index-2026-03-report`, OQ 20, p.3). ⟨mentor⟩ He is also the author who priced the task
mix: task value on Claude.ai "dropped slightly from $49.3 to $47.9" against a US average hourly wage of
$37.3 (ibid., claim 11, Fig 1.4 p.8).

**(f) Reach of the public data** (one line per open item; `[R*]`/`§` references are `data/ATLAS.md`'s).

| Open item | Reach |
|---|---|
| Determinants of adoption | Usage exists at country and subregion grain, but no release ships population, GDP, O\*NET or SOC reference files after 2025-09-15 — "every population, GDP, O\*NET or SOC join for the 2026 waves is an external join" (§Components, Reference files; §Cuts 29). Feasible with an external join; no determinant is in the files. |
| Composition vs behaviour | **Blocked.** "No unit-level longitudinality anywhere": no user, account, organisation, session or conversation identifier in any release (§Cuts 27b). |
| Firm-level adoption, concentration, markups, labour share | **Blocked.** No firm, industry (NAICS), plan or tier column in any release (§Cuts 26). |
| Emergent tasks | **Blocked.** "No emergent-task cut and no research-field cut"; the `onet` ladder is a closed universe and the bottom-up residual is `Other / Unclear` at 0.39% / 0.36% of global `pct` in 2026-06-26 (§Cuts 15a; steward answer 5). |
| Top-down against bottom-up | Both ladders exist in the long and wide families; 2025-03-27 ships the 630-cluster TSV with an O\*NET task field (§Cuts, Family A row). But "No request-hierarchy file after 2025-09-15, so the parent of a level-0 cluster is not recoverable" (§Cuts 25), and cluster ids "do not survive a wave" (§Cuts 15a). |
| Task concentration series | Reproducible at the Feb 2026 endpoint: top-10 `onet_task_pct` with `none` and `not_classified` dropped and no renormalisation gives 19.4410 (§Conventions, "Top-10 task concentration (Feb 2026)"). Earlier endpoints need the same rule re-checked per wave (§Conventions, "Say which base you are on"). |
| Occupational shares by wave | `soc_occupation` is absent at every grain in 2026-01-15 and 2026-03-24; shares must be rebuilt through an external O\*NET→SOC join (§Cuts 13). The 2019-vintage recode of `economic-index-2026-03-report` fn 2 is not reproducible from the files — `steward?` (atlas records the O\*NET 30.2 switch for 2026-06-26 only). |
| Free against paid, and model choice | **Blocked.** No plan, tier or model column in any release (§Cuts 26). |
| Super Bowl / term-break reweighting | **Blocked.** No date grain inside a wave; one seven-day window per long release (§Cuts 7), and no day or hour grain in 2026-06-26 (§Cuts 8). |

---

### T2 · Geography: unevenness, income and convergence

**(a) Publications, in date order.** `economic-index-2025-09-report`; `economic-index-2025-09-blog`;
`country-brief-india-2026-02`; `economic-index-2026-01-report`; `economic-index-2026-01-blog`;
`country-report-australia-2026-03`; `economic-index-2026-03-report`; `country-report-canada-2026-07`;
`economic-index-2026-06-report` (geography largely absent — see below);
`programme-and-product-pages` (`economic-futures-uk-europe-2025-11`, `economic-index-hub-page`).

**(b) What is established.**

- **The AI Usage Index, and the size of the spread — repeated across three waves.** Israel 7.00, Singapore
  4.57, Australia 4.10, United States 3.62, India 0.27, Nigeria 0.2
  (`economic-index-2025-09-report`, Fig 2.2 p.14 and p.16); Denmark 2.1 in November 2025
  (`economic-index-2026-01-report`, p.12); Canada 4.4 in February 2026
  (`country-report-canada-2026-07`, claim 2, Fig 1).
- **Adoption rises with income across countries, and more steeply within the US — repeated.** "A 1%
  increase in GDP per capita is associated with a 0.7% increase in Claude usage per capita at the country
  level" (`economic-index-2026-01-report`, pp.28, 31, Fig 3.3 r = 0.869, R² = 0.755, β = 0.70); the
  September 2025 report gives β = 0.690, p < 0.001, R² = 0.709 (`economic-index-2025-09-report`, Fig 2.4
  p.17); the US-state slope is 1.77 (`economic-index-2026-01-report`, Fig 3.4 p.32) and 1.8
  (`economic-index-2025-09-report`, p.19).
- **Within a country, workforce composition beats income — repeated in three countries.** "each 1% increase
  in the share of such tech workers in a state is associated with 0.36% higher usage per capita … This alone
  accounts for nearly two-thirds of the cross-state variation in AUI" (`economic-index-2026-01-report`,
  p.13, Fig 1.7 `R² = 0.61`); "income does not appear to predict adoption across Australian states and
  territories" (`country-report-australia-2026-03`, claim 7, Fig 3); "provincial usage per capita is mostly
  uncorrelated with income" while the employment share of professional, scientific and technical services is
  positively related (`country-report-canada-2026-07`, claim 7, Fig 4).
- **US states are converging; countries are not — repeated, and revised.** State AUI Gini 0.37 (Aug 2025) →
  0.31 (Nov 2025) → 0.29 (Feb 2026); country AUI Gini 0.48 → 0.46 → 0.50
  (`economic-index-2026-03-report`, Fig 1.5 p.10). The convergence model gave β̂ ≈ 0.77 (OLS), 0.76 (WLS),
  0.89 / 0.86 (2SLS) and "usage per capita would be equalized across the country in 2-5 years, a pace of
  diffusion roughly 10x faster than the spread of previous economically consequential technologies in the
  20th century" (`economic-index-2026-01-report`, pp.6, 15–17); three months later the same model on new
  data gives "5-9 years, rather than 2-5" (`economic-index-2026-03-report`, claim 15, p.10, fn 7 p.11).
- **Use case shifts with national income — repeated.** Coursework share against log GDP per working-age
  capita: r = −0.542, R² = 0.293, p < 0.001, β = −4.24; personal r = 0.681, R² = 0.463, β = 3.49; work
  r = 0.142, p = 0.131 — i.e. the work relationship is not significant
  (`economic-index-2026-01-report`, Fig 3.2 p.30). India's own figures: 51.3% work against 46% globally,
  coursework 20.9% against 19.3%, personal 27.8% against 34.7% (`country-brief-india-2026-02`, claim 13).
- **Local specialisation exists and is reported as ratios — single-wave.** Brazil translation and language
  learning 6.4×, India UI/layout 2.4×, DC job-application help 1.84×
  (`economic-index-2025-09-report`, Figs 2.8 p.23, 2.9 p.25, 2.10 p.26, and p.25). India ranks 1st globally
  on software-task share at 45.2% of O\*NET-mapped tasks (`country-brief-india-2026-02`, claim 9).
- **Higher-adoption countries collaborate more, conditional on task mix — single-wave, twice replicated
  qualitatively.** Partial regression of automation-% residuals on AUI residuals: β = −3.112, R² = 0.394,
  p < 0.001, N = 111 (`economic-index-2025-09-report`, Fig 2.11 p.27); "This mirrors a finding from our 3rd
  Economic Index report" (`economic-index-2026-01-report`, p.35).
- **Geography goes quiet in the sixth wave — recorded as an absence.** "The report publishes no AI Usage
  Index / Anthropic Usage Index figure, no country ranking and no US-state or subregion cut"
  (`economic-index-2026-06-report`, §Notes on the cuts), even though the release ships
  `usage_per_capita_index` for countries and US states (ibid., Definitions 47).

**(c) Where it is open.**

- **The stream's one explicit "more research is needed" is here.** "This is somewhat counter-intuitive,
  since we are controlling for the more diverse task composition across different countries. We speculate
  that cultural and economic factors might affect the automation share, or perhaps that early adopters in
  each country tend to use AI in a more automotive way—but more research is needed here."
  (`economic-index-2025-09-report`, pp.26–27.)
- **Convergence or divergence, as a question.** "The uneven geography of early AI adoption raises important
  questions about economic convergence… If the productivity gains are larger for high-adoption economies,
  current usage patterns suggest that the benefits of AI may concentrate in already-rich regions" (ibid.,
  p.4); "we see no evidence that low-use countries are catching up or that high-use countries are pulling
  away" (`economic-index-2026-01-report`, p.6).
- **The convergence estimate's own precision.** "This estimate comes with a high degree of uncertainty as
  the precision of our estimates cannot rule out much slower rates of diffusion" and "our estimates are
  based on just three months of data" (`economic-index-2026-01-report`, pp.15, 17).
- **Why the country Gini is non-monotonic (0.48 → 0.46 → 0.50) is not addressed** (**[inference]**,
  `economic-index-2026-03-report` item 10).
- **Whether the automation–AUI gradient is an income gradient.** Figure 2.11 residualises on task mix only;
  GDP per working-age capita is in the same release (**[inference]**, `economic-index-2025-09-report`
  item "Whether the automation–AUI relationship survives income").
- **Whether the AUI's denominator is the right one.** "The AUI therefore cannot distinguish 'few people here
  use Claude' from 'few people here could'" (**[inference]**, ibid., Constructs used without validation).
- **No sampling uncertainty on any geographic number**, although Ns are printed down to N = 283 for Malta
  and N = 430 for Vermont (**[inference]**, ibid.).
- **Europe-specific granular releases, promised and not delivered.** "We're expanding the Anthropic Economic
  Index to provide more granular, Europe-specific information, with regular public data releases tracking AI
  adoption across European industries and regions" (`programme-and-product-pages`,
  `economic-futures-uk-europe-2025-11`, Open questions). No such release is in the corpus; and the five
  European usage claims on that page are recorded as not reproducing as worded from the only release
  predating them (steward answer 7(b)).

**(d) What the Institute says it wants next.**

- `ED-1`, quoted at T1(d) — access, value capture and open-weight models, all geographic in framing.
- Economic Futures programme page, Group 2: "International impacts: How can we ensure that people around
  the world benefit from the AI-enabled economy? How might AI improve the growth and outcomes of developing
  economies?" (`programme-and-product-pages`, Open questions).
- The September 2025 report's own four questions to outside researchers, two of which are geographic: "What
  are the local labor market consequences for workers and firms of AI usage & adoption?" and "What
  determines AI adoption across countries and within the US? What can be done to ensure that the benefits of
  AI do not only accrue to already-rich economies?" (`economic-index-2025-09-report`, pp.5–6).
- `becker-friedman-partnership-2025-07`: "Distributional impacts: Studying how AI benefits and challenges
  affect different segments of society" (`programme-and-product-pages`, Open questions).

**(e) The mentor's interests ⟨mentor⟩.** ⟨mentor⟩ Massenkoff is a lead author of the report that built the
state convergence model (`economic-index-2026-01-report`, p.1, §Chapter 1 geography) and of the report that
revised its horizon to 5–9 years and reported the country-Gini reversal
(`economic-index-2026-03-report`, p.1, claim 15–16). ⟨mentor⟩ His own reading of the cross-country primitive
pattern is that early adopters dominate poorer countries' user bases: "lower income, less educated countries
paradoxically showing more complex use in some cases. The earliest adopters often have high-value, technical
use cases." (ibid., OQ 13, p.17).

**(f) Reach of the public data.**

| Open item | Reach |
|---|---|
| Automation and AUI across countries, controlling for income | Feasible on 2025-09-15, which is the only wave shipping AUI, `working_age_pop` and `gdp_per_working_age_capita` in one enriched file (§Cuts, Family B geography row; §Cuts 22 for the later waves' absence). The published partial regression reproduces exactly: slope −3.111834, R² 0.393687, N = 111 (§Conventions, "Task-mix adjustment"). |
| Country and state Ginis | Reproducible: state AUI Gini 0.366510 / 0.3184 / 0.2859 against published 0.37 / 0.32 / 0.29, unweighted over 51 values; country 0.478117 (Aug) and 0.5049 (Feb 2026) against 0.48 and 0.50 (§Conventions, Gini). Concentration *shares* land 0.7–0.9 pp below published because the population denominator is unpublished (same section). |
| Convergence model, re-estimated | Two AUI vintages are needed. 2026-01-15 and 2026-03-24 ship no AUI (§Cuts 22), so AUI must be rebuilt with the 2025-09-15 population files; use the symmetric denominator for 2026 levels (Canada 4.4430 against 3.6219 asymmetric) (§Conventions, "February 2026 has a level test"). |
| Country AUI *levels* in June 2026 | **Partly blocked.** "Country AUI ranks, ratios and month-to-month changes reproduce exactly; absolute country levels do not" — ~1% uniform level error from a later population vintage (§Conventions, AUI, June 2026). |
| Sub-national AUI outside the US | **Blocked.** No AUI for non-US subregions in 2026-06-26 (601 of 652) and none for `US-PR` (§Cuts 4); the Australia and Canada provincial AUIs "need ABS / StatCan population that no release ships" (steward answer, Open for the record). |
| Uncertainty on geographic numbers | Counts exist in the long family (`usage_count`) but 2026-06-26 has **no count metric of any kind** (§Cuts 17), and 2026-03-24 counts are on a 1,000,000 sample base, not conversations (§Conventions, Other bases). Cell fill is the binding constraint: median 18 of 3,260 `onet_task` L0 cells per country in Feb 2026 (§Cuts, Family B fill table) — "Compare mixes at level 1 or 2, never at level 0 below global." |
| The five European claims | Do not reproduce as worded on `release_2025_09_15`; GB (15.81) and FR (17.97) coding shares are below the global 18.53, no "equipment" category exists, and nothing reaches 4× for hospitality (steward answer 7(b)). |
| Non-monotonic country Gini | Reproducible at the three endpoints (as above); whether the November dip is within sampling noise needs counts, which 2026-01-15 has and 2026-06-26 does not — `steward?` for a bootstrap convention. |

---

### T3 · Automation versus augmentation, delegation and autonomy

**(a) Publications, in date order.** `economic-index-2025-02-report`; `economic-index-2025-02-paper`;
`economic-index-2025-03-report`; `economic-index-2025-04-software-development`;
`economic-index-2025-09-report`; `economic-index-2025-09-blog`; `economic-index-2026-01-report`;
`economic-index-2026-01-blog`; `economic-index-2026-03-report`; `economic-index-2026-03-appendix`;
`economic-index-2026-06-report`; `claude-code-expertise-2026-06`; `programme-and-product-pages`
(`economic-policy-responses-2025-10`, `economic-index-hub-page` metadata).

**(b) What is established.**

- **The five-pattern taxonomy has not changed since the first paper — repeated across six waves.**
  "Directive … Feedback Loop … Task Iteration … Learning … Validation"
  (`economic-index-2025-02-paper`, Table 1 p.10), with automation = Directive + Feedback Loop and
  augmentation = Validation + Task Iteration + Learning (`economic-index-2026-01-report`, Fig 1.3 note
  p.10).
- **The Claude.ai series, five waves, with one crossing and one reversal — repeated.** Augmentation 55%
  (Jan 2025), 55% (Mar 2025), 47% (Aug 2025), 52% (Nov 2025), 53% (Feb 2026) and automation 41%, 42%, 49%,
  45%, 44% (`economic-index-2026-03-report`, Fig 1.3 p.7). August 2025 is "the first report where automation
  usage exceeds augmentation usage" (`economic-index-2025-09-report`, p.9); November 2025 is "a reversal of
  what we saw in our August sample" (`economic-index-2026-01-blog`, claim 21).
- **The directive share is the moving part — repeated.** 27% (Jan 2025) → 39% (Aug 2025)
  (`economic-index-2025-09-report`, p.9), then "fallen 7pp to 32% in November 2025"
  (`economic-index-2026-01-report`, p.9).
- **The API is automation-dominant, and is becoming less so — repeated.** 77% automation against 12%
  augmentation in August 2025 (`economic-index-2025-09-report`, p.36); 75% / 14% in November 2025 (Fig 1.3
  labels, `economic-index-2026-01-report`, p.10); 68% / 17% in February 2026
  (`economic-index-2026-03-appendix`, Fig A.3 p.6, printed labels). Note that the published pair never sums
  to 100 (89%, 89%, 85%) and the residual is unexplained (ibid., claim 6).
- **Agentic surfaces automate more — repeated across two publications three years apart in measurement
  design.** Claude Code 79% automation against 49% on Claude.ai coding conversations, with Feedback Loop
  35.8% against 21.3% and Directive 43.8% against 27.5%
  (`economic-index-2025-04-software-development`, claims 4–6); and, on the autonomy primitive, "Across all
  conversations the average difference in autonomy is 0.37 points", of which "Approximately two thirds …
  is explained by the same tasks being executed with more delegation on Claude Code"
  (`economic-index-2026-06-report`, pp.14, 15), surviving within model: "among conversations using Sonnet,
  Claude Code sessions still show 0.26 points more autonomy" (p.16).
- **Autonomy is a separate construct from automation, and Anthropic says so — single-wave definition,
  repeated in use.** "'Translate this paragraph into French' is high automation (directive, minimal
  back-and-forth) but low AI autonomy" (`economic-index-2026-01-report`, p.19). Global Claude.ai mean 3.4 on
  1–5 (Fig 2.2 p.25); 3.38 → 3.41 between November 2025 and February 2026
  (`economic-index-2026-03-report`, Table 1.1 p.9).
- **Autonomy rises with the work's compute and falls with its specifiability — single-wave.** "the
  lowest-autonomy outputs are math or calculations, translations, and Q&As. High-autonomy tasks are those
  that require selection among many possible choices" (`economic-index-2026-06-report`, p.14); "across
  artifacts, mean autonomy and median token use rise together (r = 0.68 on chat and Cowork)" (p.16).
- **Who decides what, inside an agentic session — single-wave.** "On average, people make about 70% of the
  planning decisions but only 20% of the execution decisions"
  (`claude-code-expertise-2026-06`, p.6, Fig 2 p.5).

**(c) Where it is open.**

- **The capability-versus-learning fork, stated and never resolved.** "Whether the growth in directive usage
  is attributable to improving model capabilities or learning-by-doing could signal very different labor
  market implications… This will be an important area of inquiry for future research."
  (`economic-index-2025-09-report`, p.10.)
- **Whether the reversal is measurement.** The classifier model changed from Sonnet 4 to Sonnet 4.5 between
  the two waves either side of the reversal (`economic-index-2026-01-report`, fn 7 p.18), and no re-run of
  either wave through the other's classifier is reported (**[inference]**, ibid., item 11) — the report's own
  precedent for such a check is the August 2025 re-run, which moved automation from 49% to 45%
  (`economic-index-2025-09-report`, fn 4 p.11).
- **Whether the category framework still separates cleanly on agentic surfaces.** "The boundary between
  automation and augmentation becomes increasingly blurred with agentic tools like Claude Code… We will
  likely need to extend the automation/augmentation framework to account for new agentic capabilities"
  (`economic-index-2025-04-software-development`, Limitations).
- **Automation share does not vary with the education of the prompt — a published null with no statistic.**
  "the automation share is essentially unrelated to the human levels of education required to write the
  prompt (Appendix Figure A.1)" (`economic-index-2026-01-report`, pp.39–40); no fit statistic is printed in
  either document (ibid., claim 102).
- **Task success is never crossed with collaboration mode**, although both facets run on the same
  conversations (**[inference]**, `economic-index-2026-01-report` item 17).
- **The 1P API's falling automation is not decomposed** into behaviour and Claude Code's call-splitting
  (**[inference]**, `economic-index-2026-03-report` item 17, against the report's own mechanism claim at
  p.6).
- **Out-of-chat editing bounds the construct in one direction only.** "the true proportion of augmentative
  conversations may be even higher" (`economic-index-2025-02-paper`, p.9).

**(d) What the Institute says it wants next.** `ED-8` "Can AI diffusion be modulated?" is the agenda's
automation-adjacent question: "Are there analogous dials that AI companies … might turn to control the rate
of AI diffusion on a sector-by-sector basis?" (`institute-agenda-2026-05`, Definitions 22). `WILD-10` asks
"What are areas of AI oversight where humans either have a comparative advantage or a legal or normative
requirement to be 'in the loop'?" (ibid., Open questions 37). The policy stream's framing rests on this
thread: "Users are becoming increasingly likely to delegate full tasks to Claude, 'collaborating' with Claude
less" (`programme-and-product-pages`, `economic-policy-responses-2025-10`, claim 1) — asserted by hyperlink,
with no number on that page.

**(e) The mentor's interests ⟨mentor⟩.** ⟨mentor⟩ The migration of work toward the automated surface is
Massenkoff's stated mechanism for imminent labour-market change: "As tasks migrate to the API, they may
become more exposed to automation. API workflows are far more likely to be directive, with less need for a
human in the loop." (`economic-index-2026-03-report`, OQ 17, p.9), and "we expect that this migration from
Claude.ai to the API may signal more imminent transformation of work for the associated jobs" (ibid., OQ 19,
p.7). ⟨mentor⟩ In the labour-market measure he co-authored, automation is given twice the weight of
augmentation by construction: α = 1/2 + 1/2 × automation share, so "A task that sees only augmentative uses
and does not appear in the API transcripts would have α_t equal to 0.5 … A task with only automative uses
would have α_t = 1" (`labor-market-impacts-2026-03-appendix`, Definitions 10–11, p.3).

**(f) Reach of the public data.**

| Open item | Reach |
|---|---|
| The automation series, wave to wave | **Feasible, and the longest pair is twelve months.** The collaboration facet is the one taxonomy that never changed; 2025-03-27 → 2026-03-24 gives 43.0619 → 45.5456 on the five-pattern base (+2.48 pp), with five caveats that must travel with it (§Conventions, "A like-for-like automation comparison twelve months apart does exist"; steward answer 7(c)). |
| The published headline, reproduced | The base changes by wave *and* by chapter: 43% (2025-02-10) on five classified patterns; 49% (2025-09-15 headline) on **all seven** patterns; 45% (2026-01-15) and 44% (2026-03-24) on **all conversations**; 2026-06-26 on five classified patterns (§Conventions, automation table). "Say which base you are on, every time." |
| Classifier-version re-run | **Blocked.** Released files are aggregates; no transcript, no classifier output at conversation level, no model column (§Cuts 26). |
| Automation × education of prompt | **Blocked below global.** All intersections are global only in 2025-09-15, 2026-01-15 and 2026-03-24 (§Cuts 10), and 2026-06-26 has no cross of any two categories or metrics (§Cuts 11). The primitive means exist, but not crossed with collaboration. |
| Success × collaboration mode | **Blocked.** Same two cuts as above; no crossed category anywhere (§Cuts 10, 11). |
| Autonomy by surface | **Blocked for Claude Code.** "there is no Claude Code data anywhere in this dataset" (§Components). The nearest public file is `Anthropic/enabling-independent-research`, which carries METR Claude Code clusters with `cc_session_turn_count`, `model_version` and `session_duration_seconds` on an April–May 2026 window — a separate instrument with no denominator in common with the Index (§Supplementary sources). |
| Autonomy against tokens | Autonomy means exist at all three grains from 2026-01-15; token and cost measures exist **only** for the 1P API and **only** as indices re-based to mean 1.0 (§Components, First-party API; §Cuts 27). The report's r = 0.68 is on chat and Cowork tokens, which are not released — `steward?` |
| The API's unexplained 11–15% residual | Partly recoverable: `collaboration_pct` sums to 100 including `not_classified` and `none` in the long family, so the residual is decomposable there (§Conventions, Other bases); but 2026-06-26 has "No `not_classified` residual node at all" and the gap "mixes unclassified and suppressed and is not decomposable" (§Cuts 24). |

---

### T4 · Task-level primitives and productivity

**(a) Publications, in date order.** `productivity-gains-2025-11`; `economic-index-2026-01-report`;
`economic-index-2026-01-blog`; `country-brief-india-2026-02`; `economic-index-2026-03-report`;
`economic-index-2026-03-appendix`; `economic-index-2026-06-report`; `econ-scenarios-paper-2026-09`.

**(b) What is established.**

- **Claude-as-estimator time savings, and the aggregate they imply — single-wave, then replicated on a
  larger sample.** 100,000 transcripts; tasks "take people 1.4 hours to complete"; "Claude estimates that AI
  reduces task completion time by 80%"; average task cost $55
  (`productivity-gains-2025-11`, pp.2–3). Aggregated by Hulten's theorem: "Claude's estimates imply a 1.8%
  annualized increase in US labor productivity" and an implied TFP increase of 1.08%
  (ibid., Fig 7 caption p.15). Replicated on 1M conversations and on the API: "the API sample likewise
  implies a 1.8 percentage point increase" (`economic-index-2026-01-report`, p.48).
- **Reliability cuts the estimate by a third to a half — single-wave.** "implied productivity growth falls
  from 1.8 to 1.2 percentage points per year … based on Claude.ai usage, and to 1.0 percentage points for
  API traffic" (`economic-index-2026-01-report`, p.48). The chapter summary states the same revision as
  "roughly halves the implied gains, from 1.8 to about 1.0" (p.38) — the wiki file flags the two as
  irreconcilable without naming the platform (claim 85).
- **Complementarity across tasks moves the number more than reliability does — single-wave.** At σ = 0.5 the
  effect is "0.7–0.9 percentage points per year", falling to 0.8pp (Claude.ai) and 0.6pp (API) with the
  success adjustment; at σ = 1.5 it "rises to 2.2–2.6 percentage points"
  (`economic-index-2026-01-report`, pp.50–51).
- **The headline is threshold-dependent, and the report says so.** "We choose a threshold of 0.02% because
  it replicates our previous results … If we do not impose a restriction on our 1M sample … the implied
  aggregate labor productivity growth over the next decade would be roughly 5% percentage points per year"
  (ibid., fn 6 pp.52–53).
- **Gains rise with task complexity — single-wave, both directions measured.** Prompts requiring 12 years of
  schooling get a 9× speedup and those requiring 16 years a 12× speedup, while success falls from 70% to 66%
  (`economic-index-2026-01-report`, pp.38–39, Fig 4.1).
- **Effective coverage reorders which occupations are exposed — single-wave.** "data entry workers have one
  of the highest effective AI coverage… For radiologists, their top two tasks … have high success rates"
  (ibid., pp.44–45, Fig 4.4).
- **Removing Claude-covered tasks would deskill jobs on average — single-wave.** Mean predicted education of
  all tasks 13.2 years against 14.4 years for tasks seen in Claude.ai data, both employment-weighted
  (ibid., p.46, Fig 4.5 n = 18,429 / 3,169); "Overall, the net first-order impact is to deskill jobs" (p.46).
- **Effective task horizons far exceed benchmark horizons — single-wave.** API 3.5 hours; Claude.ai "about
  19 hours" by extrapolation; METR's comparator "2 hours for Sonnet 4.5 and about 5 hours for Opus 4.5"
  (ibid., pp.41–42, Fig 4.3).
- **Primitive levels have started to move — single-wave comparison.** Human education 12.21 → 11.92 years,
  AI autonomy 3.38 → 3.41, human time 185.53 → 183.77 min, human-and-AI time 15.35 → 14.30 min, all
  significant at p<0.001 except human-only time at p<0.05 (`economic-index-2026-03-report`, Table 1.1 p.9).
- **Compute tracks the value of the work — single-wave.** Marketing managers earn about twice what editors
  do ($80 against $37 an hour) and their mapped conversations use "approximately 2.5 times as many tokens",
  with "About 44% of the wage gradient in token consumption … explained by output mix"; the paper also
  publishes its own counter-example, pharmacists against statistical assistants
  (`economic-index-2026-06-report`, pp.12–13).

**(c) Where it is open.**

- **The with-AI estimate is never validated.** Both validation exercises test the human-alone estimate only
  (**[inference]**, `productivity-gains-2025-11` item 1); and the note states "we lack real-world data to
  validate the estimates that Claude provides" (p.19).
- **Task success has no reported validation statistic at all**, and it carries the success-adjusted
  productivity revision, effective coverage and the task-horizon result (**[inference]**,
  `economic-index-2026-01-report` item 1). Claude grades its own work (ibid., item 3).
- **No uncertainty is propagated to the 1.8%** — no interval, no bootstrap, no sensitivity to the labour
  share, the aggregation rule or the documented compression bias (**[inference]**,
  `productivity-gains-2025-11` item 3).
- **The bottleneck claim is illustrated, not quantified.** "Where AI makes less of a difference, these tasks
  might become bottlenecks, potentially acting as a constraint on growth" (ibid., Overview bullet), with four
  occupations shown by hand (Fig 9 p.18) and no wage-bill share computed (**[inference]**, item 9).
- **Effective coverage is never linked to an observable outcome**, although the report says "the strongest
  validation will come from the primitives' ability to capture meaningful variation in labor market
  outcomes" (`economic-index-2026-01-report`, p.24; **[inference]** item 15).
- **The deskilling result is construct-dependent and the report says so.** "our education-based measure
  differs from Autor and Thompson's expertise concept" (ibid., p.47); it is also reported as anecdotes rather
  than a distribution over workers (**[inference]**, item 16).
- **The 19-hour horizon is an unbounded extrapolation** from a plot whose x-axis ends at 8 hours
  (**[inference]**, ibid., item 14).
- **Two primitives are measured and then set aside**: "human could do alone" (88% globally) and
  multitasking (9%) appear in Figure 2.2 and in a control set and nowhere else (**[inference]**, ibid.,
  items 4–5). AI education is correlated with human education (r = 0.925 / 0.928, p.34) and then dropped
  (item 22).
- **Speedup is never reported by use case**, though 54% of Claude.ai conversations are not work
  (**[inference]**, ibid., item 18).

**(d) What the Institute says it wants next.** `ED-4` "Productivity growth: What impact will AI have on the
rate of innovation and productivity growth across the economy?" (`institute-agenda-2026-05`, Definitions 18).
Economic Futures Group 1: "Productivity effects: Why might AI's capabilities not immediately translate to
measured productivity growth?" and "Value creation and new industries: … How can we measure economic gains
beyond traditional productivity metrics?" (`programme-and-product-pages`, Open questions). The Economic
Policy Framework asks for exactly these measures from government: "Instruments should focus on directly
observable metrics like AI usage rates and intensity of use, and worker productivity indicators by level of
AI adoption" (ibid., `economic-policy-framework-2026-06`, PDF p.5). `becker-friedman-partnership-2025-07`:
"Productivity measurement: Investigating how AI adoption affects traditional measures of productivity across
different sectors" (ibid.).

**(e) The mentor's interests ⟨mentor⟩.** ⟨mentor⟩ Massenkoff is a lead author of the report that built the
success adjustment, effective coverage, the task-education model and the deskilling exercise
(`economic-index-2026-01-report`, p.1, Chapter 4) and of the report that first tracked the primitives over
time (`economic-index-2026-03-report`, Table 1.1 p.9). ⟨mentor⟩ In the sixth report he moves the productivity
question onto compute: "We measure each conversation's computational costs in tokens … and compare across
occupations by mapping each conversation's classified task to the occupation that typically performs it"
(`economic-index-2026-06-report`, p.12), with the interpretive claim "Crucially, these move together: more
production from Claude does not mean less from the user. If the human remains involved in the highest-value
tasks, the pattern looks more labor-augmenting than labor-displacing" (pp.13–14).

**(f) Reach of the public data.**

| Open item | Reach |
|---|---|
| The primitive means, by geography | **Feasible.** `human_only_time`, `human_with_ai_time`, `ai_autonomy`, `human_education_years`, `ai_education_years` are numeric facets with eight statistics each at global, country and country-state grain in 2026-01-15 and 2026-03-24; histograms are global only (§Cuts, Family B primitives row; §Cuts 20). |
| Units, before any speedup is computed | **Trap.** 2026-01-15: `human_only_time` in hours, `human_with_ai_time` in minutes; 2026-03-24: both in hours and the report prints minutes (3.0629 h × 60 = 183.77); 2026-06-26: hours and minutes again (§Traps 8). |
| Confidence intervals on the primitives | **Mostly blocked.** "No confidence intervals on four of the five global numeric facets in 2026-03-24 (only `human_education_years` has them)", and `*_median_ci_lower` can be negative and must never be plotted as error bars (§Cuts 20; §Traps 11). |
| Re-aggregating the 1.8% | **Blocked as published.** No wage, employment, population or O\*NET reference file ships in 2026-01-15, 2026-03-24 or 2026-06-26 (§Cuts 29), so the Hulten weights are an external join; and the aggregation needs conversation-level speedups, which are not released. Task-level primitive means are available as the substitute — `steward?` on whether task-level `human_only_time`/`human_with_ai_time` intersections exist below global (§Cuts 10 suggests not). |
| Success × anything | Task success exists as a categorical facet at all three grains in 2026-01-15 and 2026-03-24 and as a metric in 2026-06-26, but never crossed with another category (§Cuts 10, 11). |
| Bottleneck share of the wage bill | Needs task-level time fractions, which are not in any release; `labor_market_impacts/` has "No task → occupation link and no time-on-task weights", so `observed_exposure` "is not decomposable" (§Cuts 15). |
| Speedup by use case | `use_case` is a categorical facet at all three grains from 2026-01-15, but the crossing with the time primitives is an intersection, and intersections are global only (§Cuts 10). |
| Token gradient against wages | **Blocked.** Token measures exist only for the 1P API, as indices, and only at global grain (§Components; §Cuts 27); the chat-and-Cowork tokens behind the sixth report's Figure 2.3 are not released. |
| The 19-hour horizon | **Blocked.** No conversation-level data and no task-level success × duration cross (§Cuts 10, 11). |

---

### T5 · Labour-market exposure and observed impacts

**(a) Publications, in date order.** `economic-index-2025-02-paper` (the exposure-versus-usage framing);
`labor-market-impacts-2026-03`; `labor-market-impacts-2026-03-appendix`;
`survey-81k-economics-2026-04`; `economic-index-2026-03-report` (one restated exposure result);
`economic-index-2026-06-report` (reported against observed exposure); `worker-retraining-2026-08` (who is at
risk); `programme-and-product-pages` (`economic-policy-framework-2026-06`);
`econ-scenarios-paper-2026-09` (exposure as a calibration anchor).

**(b) What is established.**

- **Observed exposure, the measure — single-wave, with a formal definition in the appendix.** "a new measure
  of AI displacement risk, observed exposure, that combines theoretical LLM capability and real-world usage
  data, weighting automated (rather than augmentative) and work-related uses more heavily"
  (`labor-market-impacts-2026-03`, p.2); formally `r̃_t = 1{WorkUsage_t ≥ 100} × 1{β_t ≥ 0.5} × α_t`, with
  the usage gate "must be 100 or 0.0025% of traffic" and `R_o` the time-fraction-weighted average over a
  job's tasks (`labor-market-impacts-2026-03-appendix`, Definitions 4, 8, 13).
- **Realised coverage is a fraction of theoretical capability — single-wave.** "the β measure shows scope
  for LLM penetration in the majority of tasks in Computer & Math (94%) and Office & Admin (90%)" against
  "Claude currently covers just 33% of all tasks in the Computer & Math category"
  (`labor-market-impacts-2026-03`, p.7, Fig 2).
- **Usage is concentrated on theoretically feasible tasks — single-wave.** "Tasks rated β=1 … account for
  68% of observed Claude usage, while tasks rated β=0 … account for just 3%" (ibid., Fig 1 caption p.4);
  "97% of the tasks observed across the previous four Economic Index reports fall into categories rated as
  theoretically feasible" (p.5).
- **The exposure ranking, and the control group it creates — single-wave.** "Computer Programmers are at the
  top, with 75% coverage, followed by Customer Service Representatives"; "Data Entry Keyers … are 67%
  covered"; "At the bottom end, 30% of workers have zero coverage" (ibid., pp.7–8, Fig 3).
- **Exposure predicts official forecasts weakly, and the composite beats its capability input — single-wave.**
  "For every 10 percentage point increase in coverage, the BLS's growth projection drops by 0.6 percentage
  points"; "Interestingly, there is no such correlation using the Eloundou et al. measure alone" (ibid.,
  pp.8–9, Fig 4).
- **No detectable differential rise in unemployment, with a stated MDE — single-wave, twice checked.** "The
  average change in the gap since the release of ChatGPT is small and insignificant"; "differential increases
  in unemployment on the order of 1 percentage point would be detectable" (ibid., pp.11–12). The appendix
  adds the pooled estimates: −0.0023 (SE 0.0058) in the CPS and +0.001 (SE 0.002) on unemployment-insurance
  claims (`labor-market-impacts-2026-03-appendix`, Figs 1 and 3, read from the figures).
- **Youth hiring into exposed occupations has slowed, barely significantly — single-wave.** "entry into the
  most exposed jobs decreases by about half a percentage point. The averaged estimate in the post-ChatGPT
  era is a 14% drop in the job finding rate … although this is just barely statistically significant. (There
  is no such decrease for workers older than 25.)" (`labor-market-impacts-2026-03`, pp.12–13, Fig 7).
- **Exposed workers were already advantaged before ChatGPT — single-wave.** "16 percentage points more
  likely to be female, 11 percentage points more likely to be white… They earn 47% more" (ibid., p.9, Fig 5).
- **The measure's ranking is robust to most construction choices — single-wave, ten variants.** Spearman
  correlations against the baseline: Claude.ai usage 0.81, Eloundou β 0.70, baseline × success 1.00, Ridge
  imputation 0.73, DWA 0.71, IWA 0.66, core-weight 0.99
  (`labor-market-impacts-2026-03-appendix`, Fig 4 p.10, read from the figure).
- **Perceived threat tracks observed exposure — single-wave.** "For every 10-percentage-point increase in
  exposure, perceived job threat increased by 1.3 percentage points"; "People in the top 25% of exposure
  mentioned the worry three times as often as those in the bottom 25%"
  (`survey-81k-economics-2026-04`, p.3, Fig 1).
- **Self-reported exposure exceeds observed exposure, and is positively correlated with it — single-wave.**
  "reported exposure (grey dots) is positively correlated with both observed and theoretical exposure"
  (`economic-index-2026-06-report`, p.22, Fig 3.3); "reported exposure systematically exceeds observed
  exposure" (p.23).

**(c) Where it is open.**

- **The closing-gap conjecture.** "As capabilities advance, adoption spreads, and deployment deepens, the red
  area will grow to cover the blue" (`labor-market-impacts-2026-03`, p.7) — stated in the future tense, with
  no trend estimate even across the two waves the measure uses (**[inference]**, item 1).
- **Which ingredient does the work.** No result is reported with one of the four adjustments switched off
  (**[inference]**, ibid., item 3); the gate-invariance claim, "The exact cutoff has little impact on the job
  rankings", is asserted and never shown (`labor-market-impacts-2026-03-appendix`, p.2; **[inference]**,
  item 1).
- **Who counts as treated.** "A key question in interpreting our coverage measure is which workers should be
  considered treated? Should changes in employment be expected from just 10% task coverage?" with three
  competing theoretical answers named — Gans and Goldfarb, Hampole et al., Autor and Thompson
  (`labor-market-impacts-2026-03`, p.10).
- **Whether the zero-exposure group is a valid control**, given the pre-treatment differences in Figure 5 and
  the opposite-signed COVID divergence (**[inference]**, ibid., item 6).
- **Where the un-hired young workers went.** "remaining at their existing jobs, taking different jobs, or
  returning to school" (ibid., p.13) — named and not distinguished.
- **The recent-graduate question the paper proposes for itself.** "a key next step might be to look at how
  recent graduates with educational credentials in exposed areas are navigating the labor market" (ibid.,
  p.14).
- **Non-Claude usage, and non-US labour markets.** "Our task- and occupation-level exposure measures can
  readily incorporate other usage data, and be extended to different countries. We intend to apply this
  methodology to new settings over time." (ibid., fn 3 p.15) — an intention, not a test.
- **Whether fear is warranted.** The same measure produced no detectable unemployment effect and a 3× fear
  ratio, and the two are never confronted (**[inference]**, `survey-81k-economics-2026-04` item 1 — see
  §Cross-thread tensions, pair 5).

**(d) What the Institute says it wants next.** `ED-7` "AI and jobs: How will AI change jobs and employment
in different parts of the economy?" (`institute-agenda-2026-05`, Definitions 21). `Share 1`'s early-warning
promise (ibid., Definitions 6) is the specific commitment this thread is the candidate instrument for; the
wiki file records that no publication in the corpus defines a trigger, threshold or lead time (ibid., Open
questions 3). The Economic Policy Framework names the trigger variable and the watch list: unemployment
primary, with "labor force participation, underemployment, wages, and labor's share of national income"
alongside (`programme-and-product-pages`, `economic-policy-framework-2026-06`, PDF p.6).

**(e) The mentor's interests ⟨mentor⟩.** ⟨mentor⟩ This thread is the mentor's own: observed exposure is
Massenkoff and McCrory's measure (`labor-market-impacts-2026-03`, p.1), and its formal construction, its
robustness matrix and its administrative-data replication are his appendix
(`labor-market-impacts-2026-03-appendix`, pp.2–4, 6, 8–9). ⟨mentor⟩ The paper's opening argument is a
scepticism about exposure measures and official forecasts: "a prominent attempt to measure job offshorability
identified roughly a quarter of US jobs as vulnerable, but a decade on, most of those jobs maintained healthy
employment growth. The government's own occupational growth forecasts, while directionally correct, have
added little predictive value beyond linear extrapolation of past trends"
(`labor-market-impacts-2026-03`, p.3, fn 1 sourcing the forecast claim to his own non-Anthropic Occupational
Outlook working paper, which `wiki/INDEX.md` places out of scope and permits only as a statement of
interest). ⟨mentor⟩ He states the design's purpose as separating signal from noise before the effect is
visible: "This framework is most useful when the effects are ambiguous—and could help identify the most
vulnerable jobs before displacement is visible" (ibid., p.3), and "An established approach may help future
observers separate signal from noise" (p.14). ⟨mentor⟩ He then linked the measure to perceptions in his own
first-authored survey paper (`survey-81k-economics-2026-04`, p.3, Fig 1).

**(f) Reach of the public data.**

| Open item | Reach |
|---|---|
| Job-level exposure, as released | **Exists, in exactly one place.** `labor_market_impacts/job_exposure.csv`, 756 rows, `occ_code` a 7-character 2018 SOC detailed code, unique, no aggregates, no SOC 55 Military; the only join key is `occ_code` (steward answer 8; §Components, Labour-market files). |
| Task-level penetration | `task_penetration.csv`, 17,998 rows over **17,992 distinct** task strings — "not unique on its only key; de-duplicate before joining and never lower-case first"; `penetration` is not a share, support `{0} ∪ [0.5, 1]`, 92.48% exactly zero (steward answer 10; §Traps 9). |
| Decomposing the measure | **Blocked.** No β column, no α column, no time-fraction weights, no crosswalks, no alternative measures in the folder (§Cuts 30); "the two files share no key" (§Cuts, Family A row). |
| Varying the usage gate | **Blocked.** The ≥100 gate is already applied upstream — 16,644 of 17,998 rows are exactly 0 — and "do not apply another" (§Thresholds, `labor_market_impacts/`). |
| Trend in coverage across waves | Needs the measure rebuilt per wave from usage; feasible in principle from the long-family `onet_task` and `collaboration` facets plus an external Eloundou β, but the automation weight needs `onet_task::collaboration`, which is **global only** (§Cuts 10) — so a per-occupation α cannot be rebuilt below global. `steward?` on whether the 2025-09-15 enriched `collaboration_automation_augmentation` facet supports it at task level. |
| Linking exposure to CPS or UI outcomes | External: no demographics anywhere (§Cuts 28), no geography in `labor_market_impacts/` (§Cuts 1). The BLS Employment Projections table merges on `occ_code` with 755 of 756 matched, the one miss being 11-1031 Legislators (§Supplementary sources). |
| Non-US extension | **Blocked as released.** `labor_market_impacts/` is US-implicit with no geography (§Cuts 1); the country-grain usage data has no O\*NET→SOC reference file after 2025-09-15 (§Cuts 29). |
| Reproducing the tech-worker slope | Partly: "each 1% increase" means one percentage point of share, not a log-log elasticity; 0.369 with R² 0.62 on the August 2025 file reproduces the published 0.36, but the November 2025 version reaches only 0.3124 with an ACS substitute because "BLS OEWS … returns 403 to this sandbox" (§Conventions, "Each 1% increase"; steward answer, Open for the record). |

---

### T6 · Learning curves, skill and expertise

**(a) Publications, in date order.** `skill-formation-rct-2026-01`; `ai-fluency-index-2026-02`;
`economic-index-2026-03-report`; `claude-code-expertise-2026-06`;
`claude-code-expertise-2026-06-appendix`; `economic-index-2026-06-report` (ch.3 learning items);
`worker-retraining-2026-08` (the training side).

**(b) What is established.**

- **Experienced users differ across every characteristic measured, and in the collaborative direction —
  single-wave.** High tenure (≥6 months) against low: directive 38.1% → 29.4%, task iteration 24.5% →
  28.2%, learning 21.3% → 24.7%, work use 41.6% → 48.9%, coursework 14.1% → 10.8%, task success 66.7% →
  73.1%, human education 11.5 → 12.3 years (`economic-index-2026-03-report`, Table 2.1 p.15).
- **The tenure–success association survives narrow controls — single-wave, three specifications.** "long
  tenure users are about 5 percentage points more likely to have a successful conversation"; "bringing it
  closer to 3 percentage points" with O\*NET task and request-cluster fixed effects; "a 4 percentage point
  higher success rate accounting for the full controls" of model, use case and country
  (ibid., pp.17–18, Fig 2.4).
- **Returns to task-specific expertise in agentic sessions are large and concave — single-wave.** "A
  novice-rated session reaches our strictest measure, verified success, 15% of the time and at least partial
  success 77% of the time. A session rated intermediate or up reaches verified success 28-33% of the time and
  partial success 91-92%"; "most of the gain comes from moving between novice to intermediate"
  (`claude-code-expertise-2026-06`, pp.11–12, Fig 5). Expert sessions also draw more out of the agent: 4.9
  actions and 607 words at level 1 against 11.7 actions and 3.2k words at level 5, "+9% actions and +13%
  output per expertise level" in a regression with clustered standard errors (ibid., p.8, Fig 3 caption p.9).
- **Occupation matters less than expertise — single-wave.** "Software engineers and users in other 'computer
  and mathematical occupations' reach verified success in about 30% of their sessions overall, where users
  from other professions reach verified success about 26%"; "In code-producing sessions, every one of the ten
  largest occupations in our dataset lands within seven points of software engineers"
  (ibid., pp.14, Fig 6 p.15).
- **In a randomised trial, AI assistance lowered comprehension without a measured speed gain — single trial,
  n = 52.** "There is a 4.15 point difference between the means … For a 27-point quiz, this translates into a
  17% score difference or 2 grade points", Cohen's d = 0.738, p = 0.010; task time p = 0.391
  (`skill-formation-rct-2026-01`, p.9, Fig 6 p.10). The largest gap was on debugging questions (p.11,
  Fig 8), and the treatment was **GPT-4o**, not Claude (p.6).
- **Observable fluency is dominated by iteration — single-wave.** "85.7% of the conversations in our sample
  exhibited iteration and refinement"; conversations that iterate carry "more than double the number of AI
  fluency behaviors"; "In only 30% of conversations do users tell Claude how they'd like it to interact with
  them" (`ai-fluency-index-2026-02`, claims 5–6, 8, 13).
- **The artifact effect: description behaviours rise and discernment behaviours fall — single-wave.** In
  artifact conversations users are more likely to clarify the goal (+14.7pp), specify a format (+14.5pp) and
  provide examples (+13.4pp), but *less* likely to identify missing context (−5.2pp), check facts (−3.7pp)
  or question the reasoning (−3.1pp) (ibid., claims 11–12).
- **Heavy delegators do not report less learning — single-wave, a published null.** "the share of people
  reporting that AI is increasing the market value of their skills rises with automation share, while the
  share reporting they learn more is roughly flat"; 68% report learning more and 57% that AI made their
  skills more valuable (`economic-index-2026-06-report`, pp.28, Fig 3.7).

**(c) Where it is open.**

- **Cohort and survivorship against learning-by-doing.** "The high-tenure users are self-selected… Further,
  there's an inherent survivorship bias: people who signed up a year before our data pull may be seeing
  positive results from their usage. We do not observe people who signed up a year ago but are no longer
  using Claude." (`economic-index-2026-03-report`, Limitations 7, p.16), and the promise: "Over time, we will
  be able to more cleanly isolate cohort and survivorship bias from learning-by-doing" (OQ 15, p.20).
- **Whether the expertise rating and the success measure are independent.** Both classifiers read the same
  transcript and one of the expertise signals is whether the user corrects Claude, while the failure signal
  scores "the user pushing back on the output" — the obvious first-prompt-only test is not run
  (**[inference]**, `claude-code-expertise-2026-06`, first item of What it did not test).
- **Whether rated expertise is task-specific, as claimed.** The construct is asserted to be task-specific
  (ibid., pp.6–7); with ~400,000 sessions from ~235,000 people the within-person test is available and is not
  run (**[inference]**, ibid., Panel structure available and unused).
- **The month-by-month expertise gradient is not shown**, although the paper names a falling return to
  expertise as the signal it is watching for: "if the returns to expertise begin to decrease over time, that
  would suggest that models are starting to supply the essential judgment that users currently bring"
  (ibid., p.16; **[inference]**, Decompositions the seven-month window supports).
- **The trial's external validity.** "This study focuses on a single task using a chat-based interface. This
  should be a lower bound for cognitive offloading since agentic AI coding tools would require even less
  human participation" (`skill-formation-rct-2026-01`, p.19), and "Ideally, skill formation takes place over
  months to years. We measured skill formation for a specific Python library over a one-hour period" (ibid.).
- **Whether immediate comprehension predicts durable skill.** "Whether immediate quiz performance predicts
  longer-term skill development is an important question this study does not resolve" (ibid., web page).
- **The artifact effect's three candidate explanations**, offered and not tested — polished outputs looking
  finished, tasks where precision matters less, and evaluation happening in unobserved channels
  (`ai-fluency-index-2026-02`, Open questions).
- **The fluency cohort analysis, promised.** "we plan to conduct 'cohort analyses,' comparing new users to
  experienced ones" (ibid.).
- **Skill erosion is not ruled out by the survey null.** "these are self-assessments, and skills can erode
  even as they become more valuable and as someone reports learning more, so the data do not rule out skill
  erosion" (`economic-index-2026-06-report`, p.28).

**(d) What the Institute says it wants next.** `ED-10` "The professional pipeline:" — "Many professions rely
on junior roles (like paralegals, junior analysts, and associate developers) to serve as training for the
senior practitioners of the future. If AI absorbs the tasks that historically built expertise, how do people
become experts in the first place? What does this mean for the long-term supply of senior judgment in a
field?" (`institute-agenda-2026-05`, Definitions 24). `ED-11` "Studying for the future:" — "What should
people study today to be well positioned for the future?" (ibid., Definitions 25). `WILD-2` "Critical
thinking:" — "how do we detect and avoid the degradation of human critical thinking skills that may come from
increasing deference to AI judgment?" (ibid., Open questions 29). Research Fund priority 2 makes the pipeline
question fundable: "Field experiments on the early-career and professional pipeline, e.g., what
apprenticeship, mentorship, or rotational models can build expertise if junior tasks are absorbed by AI"
(`programme-and-product-pages`, `economic-futures-research-fund-2026-07`, priority 2).

**(e) The mentor's interests ⟨mentor⟩.** ⟨mentor⟩ This is the thread where the mentor publicly revised an
Anthropic hypothesis: "More experienced users tend to use Claude more collaboratively, for more work-related
reasons, in more complex tasks, and with more success. This pushes back against a hypothesis we made last
year that automated use may be more typical of more experienced, sophisticated users; instead, we find that
the most advanced users are more likely to iterate with Claude."
(`economic-index-2026-03-report`, OQ 14, p.19.) ⟨mentor⟩ He states the distributional stake plainly: "These
observed differences in success rates could deepen inequalities in the labor market… early adopters with
high-skill tasks have more successful interactions with Claude than later, less technical adopters" (ibid.,
OQ 21, p.20). ⟨mentor⟩ He is second author of the paper whose title claim is *persistent* returns to
expertise (`claude-code-expertise-2026-06`, p.1), which argues "Coding agents are not substituting for domain
expertise—the more understanding a worker brings to an agent, the more quality work the agent is able to do"
(p.3).

**(f) Reach of the public data.**

| Open item | Reach |
|---|---|
| Tenure, cohorts, learning curves | **Blocked.** No tenure column and no user or account identifier in any release (§Cuts 26, 27b); the March 2026 report's tenure analysis "run[s] on log-level data that is not in the release" (`economic-index-2026-03-report`, §Data and methods). |
| Expertise ratings and session success | **Blocked.** No Claude Code data anywhere in the Index dataset (§Components). The `Anthropic/enabling-independent-research` METR file carries Claude Code session-level facets on an April–May 2026 window, but it is "a set of researcher-defined facets on a non-random opted-in sample" with "no denominator in common with the Index" (§Supplementary sources). |
| Fluency behaviours | **Blocked twice over.** No turn count and no artifact flag at conversation level; artifacts exist only as the 32 aggregate `artifact_*_pct` shares of 2026-06-26, which are shares of a geography-month (§Cuts 27). And the report's window, 20–26 January 2026, falls in a gap: "No window covering 20–26 January 2026, or any other date between 2025-11-20 and 2026-02-05" (§Cuts 27a; steward answer 1). |
| Skill formation | **Not an Index question as released.** The trial's own artefacts are third-party (GitHub, OSF) and the paper releases no participant-level data (`skill-formation-rct-2026-01`, §Data and methods). |
| Education-years primitives as a skill proxy | **Feasible.** `human_education_years` and `ai_education_years` exist at all three grains in 2026-01-15 and 2026-03-24 with eight statistics each, and `human_education_years` is the one numeric facet carrying CIs in 2026-03-24 (§Cuts, Family B primitives row; §Cuts 20). |
| Success × task, over waves | Task success exists as a facet in both 2026 long waves and as a metric in 2026-06-26; wave-to-wave comparison needs the same base and taxonomy, and the O\*NET ladder changed to version 30.2 in 2026-06-26 (§Releases at a glance; §Cuts 15a) — `steward?` on a crosswalk. |

---

### T7 · Agentic coding and the agentic surfaces

**(a) Publications, in date order.** `economic-index-2025-04-software-development`;
`work-at-anthropic-2025-12`; `coding-agents-social-sciences-2026-05`;
`coding-agents-social-sciences-2026-05-appendix`; `claude-code-expertise-2026-06`;
`claude-code-expertise-2026-06-appendix`; `economic-index-2026-06-report` (Claude Code and Cowork as named
surfaces); `independent-research-access-2026-08` (the METR partner study).

**(b) What is established.**

- **The agentic surface automates more than the chat surface — repeated (see also T3).** 79% against 49%
  (`economic-index-2025-04-software-development`, claim 4); 0.37 autonomy points on the 1–5 scale, two thirds
  of it within-task (`economic-index-2026-06-report`, pp.14–15).
- **What agentic sessions are for, at scale — single-wave.** Nine work modes; "About 56% of sessions consist
  of writing (25%) fixing (26%), or testing and orchestrating code 5%. Operating software comprises 17%,
  while 14% of sessions are planning or exploring, and 13% produce analysis or prose"
  (`claude-code-expertise-2026-06`, p.4, Fig 1). "Most sessions are anchored to an existing codebase: 48%
  primarily modify existing code and another 17% explore code, while 14% create new code from scratch"
  (p.4, PDF only).
- **The mode mix moved sharply in seven months — single-wave series.** Fixing broken code fell "from 33% to
  19%"; operating software grew "from 14% to 21%"; writing and data analysis "roughly doubled, from about 10%
  to 20%" (ibid., p.9, Fig 4). Estimated task value "rose by 27% between October and April" (p.10) — the key
  findings say "about 25%" (p.2), and the wiki file flags both as published without reconciliation (claim 23).
- **Who decides, and how much the agent does per prompt — single-wave.** ~4 turns per session, "each prompt
  the user sends sets off a chain of around 10 actions taken by Claude on average—and sometimes over a
  hundred", 2,400 words of output per turn (ibid., p.6); "About 2% of sessions average more than 100 actions
  per prompt" (fn 6 p.17).
- **A single firm's own adoption, three instruments — single-wave.** 132 engineers surveyed, 53 interviews,
  and "200,000 internal transcripts from Claude Code from February and August 2025"
  (`work-at-anthropic-2025-12`, claims 1, 3).
- **Coding agents have reached a minority of one measured research population — single-wave.** 1,260
  quantitative social scientists; 81% have tried genAI in research but "only 20% have adopted coding agents";
  among adopters "86% of users reporting Claude Code use (31% report using Codex)"
  (`coding-agents-social-sciences-2026-05`, claims 2, 3, 15).
- **Adoption is steeply unequal on that population — single-wave.** 39% of economists against 6% public
  health, 4% education, 6% communication; "more than twice the rate" among typically male names; "Researchers
  at top universities are 40% more likely than others to use coding agents" (ibid., claims 17, 20, 5, with
  the last appearing only in the Summary).
- **Adopters show more output at the early stages and no more at the late ones — single-wave, descriptive.**
  "around 10% (empirical projects started) to 75% (working papers posted) more productive than others in
  their discipline and career stage"; "We find no evidence that coding agent users are submitting more new
  papers to journals" (ibid., claims 34–35).
- **Model choice tracks the value of the task — single-wave.** "for every additional $10 of hourly wage for a
  task, the share of conversations using Opus increases by 1.5 percentage points for Claude.ai users… Its
  slope is about twice as large" on the API (`economic-index-2026-03-report`, p.14, Fig 2.2); 54% of Claude
  Code sessions are served by Opus against 10% of chat and Cowork conversations
  (`economic-index-2026-06-report`, p.16).

**(c) Where it is open.**

- **Non-interactive agentic use is excluded and unmeasured, and this is named as a priority.** "the
  non-interactive usage this report excludes is a substantial share of activity. Developing a framework to
  measure it is a priority for future work" (`claude-code-expertise-2026-06`, p.15).
- **Real-world outcomes are unobserved.** "we cannot measure real-world outcomes, like whether code written
  in a session is actually used or discarded thereafter, or whether it produces an economically valuable
  artifact" (ibid., p.15).
- **Whether the mode-mix and task-value shifts are entry effects.** Neither is decomposed into new users
  arriving and existing users changing, over a window in which management, sales and legal are the
  fastest-growing occupation groups (**[inference]**, ibid., Decompositions the seven-month window supports).
- **Decision attribution is never crossed with success or with expertise** (**[inference]**, ibid.,
  Cross-tabulations between its own new measures).
- **The randomised experiment on research productivity is promised, not delivered.** "The survey is the
  baseline wave of a larger ongoing study … including a randomized experiment providing researchers with
  access to Claude Code. We will publish results from this experiment in the future."
  (`coding-agents-social-sciences-2026-05`, Open questions 2), and "In future updates on this study, we will
  show results comparing coding agent users to a clean comparison group, and assess whether the content, and
  not just quantity, of coding agent augmented work looks different." (ibid., Open questions 4).
- **The social-science survey was never linked to usage**, although the respondents were recruited with
  Claude Max accounts by the firm that holds the logs (**[inference]**, ibid., item 1 — the wiki file calls
  it "the single largest missing validation").
- **What agentic coding implies for knowledge work is a conjecture.** "What happens on Claude Code may be a
  preview of where knowledge work is headed, as agents become embedded in non-coding work"
  (`claude-code-expertise-2026-06`, p.3).
- **Whether the "vibe coding" disruption conjecture holds.** "Speculatively, these findings suggest that
  jobs that center on making simple applications and user interfaces might face earlier disruption"
  (`economic-index-2025-04-software-development`, Limitations).

**(d) What the Institute says it wants next.** The agenda's evidence for its own headline claim is this
thread: "At Anthropic, we can see early evidence that jobs like software engineering are changing radically"
(`institute-agenda-2026-05`, *Lead ¶4*). `WILD-4` asks "How might humans manage teams composed of a mixture
of humans and AI systems effectively? And how might this be inverted…?" (ibid., Open questions 31), and
`Share 3` promises "More detailed information about how our work at Anthropic has sped up as a result of new
AI tools" (ibid., Definitions 6). `RD-3` asks "How can we measure the aggregate speed of AI research and
development?" (ibid., Open questions 41).

**(e) The mentor's interests ⟨mentor⟩.** ⟨mentor⟩ Massenkoff is second author of the agentic-coding paper
(`claude-code-expertise-2026-06`, p.1) and co-author of the coding-agents survey
(`coding-agents-social-sciences-2026-05`, Authors). ⟨mentor⟩ In the latter, his stated interest is the effect
of agents on the production of knowledge itself: "as AI handles a broadening swath of research tasks, its
distinctive analytical choices could stamp our collective understanding of our economy, our society, and
ourselves" (ibid., Open questions 10), and "The way we study the economy and politics, for example, is
increasingly through analysis decisions made in part by AI coding agents" (Open questions 13).

**(f) Reach of the public data.**

| Open item | Reach |
|---|---|
| Any Claude Code measure | **Blocked in the Index.** "there is no Claude Code data anywhere in this dataset" — no folder, file, facet, variable, `metric_id`, `category_name` or column mentions it at revision `2ea58ff`; the June 2026 file explicitly excludes it from the API aggregate (§Components, Claude Code). |
| The nearest public substitute | `Anthropic/enabling-independent-research`, `metr_clusters.csv` (604 rows × 163 columns) and `metr_addendum_clusters.csv`, with `cc_session_turn_count`, `model_version`, `lines_added/removed`, `compaction_auto/manual`, `session_duration_seconds`, `active_human_time`, `estimated_time_with_ai`, `time_without_ai`; CC BY 4.0; one fixed April–May 2026 window (§Supplementary sources). Cautions: researcher-defined facets, opted-in sample, `num_records` are cluster memberships not conversations. |
| Surface comparison (chat, Cowork, Claude Code, API) | **Partly blocked.** 2026-06-26 splits Claude.ai "chat and Cowork" from the 1P API in two files, but Cowork is pooled with chat and Claude Code is absent (§Releases at a glance; §Components). The API file is global only, always (§Cuts 2). |
| Turn counts, session length, actions | **Blocked in the Index.** "No token, turn, extended-thinking, session-length or active-time field outside the API token indices" (§Cuts 27). Available only in the partner-cluster file above. |
| Model selection by task value | **Blocked.** No model column in any release (§Cuts 26); the March 2026 report's model analysis is on log-level data (`economic-index-2026-03-report`, §Data and methods). |
| Social-science adoption | Not an Index cut. "No emergent-task cut and no research-field cut… For fields of research the nearest cuts are SOC `Life, Physical, and Social Science` (4.54% / 4.51% global) with 57 detailed `19-*` nodes, and the `request` Major node `Research & Intelligence`" (§Cuts 15a; steward answer 5). |
| The April 2025 software-development report's numbers | **Blocked.** No `release_2025_04*` folder exists and no file in the repository names Claude Code (`economic-index-2025-04-software-development`, §Source; §Components). |

---

### T8 · Measurement, methods and data access

**(a) Publications, in date order.** `clio-insights-2024-12`; `economic-index-2025-02-paper` (Appendices B, C,
G); `economic-index-2025-03-report` (the pipeline changes); `economic-index-2025-09-report` (the only released
code library); `economic-index-2026-01-report` and its online appendix (the nine classifier prompts);
`economic-index-2026-03-appendix`; `economic-index-2026-06-report`; `economic-index-2026-06-appendix`;
`claude-code-expertise-2026-06-appendix`; `independent-research-access-2026-08`;
`programme-and-product-pages` (`economic-index-connector-2026-07`, `economic-index-hub-page`).

**(b) What is established.**

- **The whole stream runs on one privacy-preserving system, and every release states the same constraint —
  repeated.** "No researcher reads individual transcripts, occupation labels are never linked to identifiable
  users, and we only observe aggregates over a minimum number of distinct users"
  (`claude-code-expertise-2026-06`, fn 7 p.17); the hub page names it for a lay reader: "The Anthropic
  Economic Index is made possible by Clio, a system that allows us to analyze conversations with Claude while
  preserving user privacy" (`programme-and-product-pages`, `economic-futures-hub-page`, Definitions).
- **Classifier accuracy was measured once, in 2025, and not since — single-wave.** Human validation on 150
  examples: "At the top level, 95.3% … At the middle level, 91.3% … At the base (O\*NET) level, 86%", and
  "90.7% of conversations are assigned to their optimal label" for the collaboration pattern
  (`economic-index-2025-02-paper`, p.21). Cluster reconstruction: ≥0.95 Pearson at category level, ≥0.70 at
  occupation level, ≥0.47 at task level (ibid., Appendix G, pp.28–30).
- **The primitives are published as prompts, with process validation but no metric — single-wave.** Nine
  classifiers, "all of which are directionally accurate even if they may deviate somewhat from human
  ratings", validated against "a human researcher on a small set of transcripts in which users gave feedback"
  (`economic-index-2026-01-report`, p.22); the only quantified external check is the human-education
  primitive against BLS attainment, N = 576, R² = 0.282, slope 8.09 (Fig 2.1 p.24).
- **Every measurement generation is reported as a break — repeated.** The occupational-relevance filter was
  dropped and the classifier model swapped between waves 1 and 2
  (`economic-index-2025-03-report`, §"Additional methodological details"); Sonnet 4 → Sonnet 4.5 between
  waves 3 and 4 (`economic-index-2026-01-report`, fn 7 p.18); 2010 → 2019 O\*NET-SOC codes at wave 5
  (`economic-index-2026-03-report`, fn 2 p.11); and at wave 6 a two-step DWA-then-Task classifier, O\*NET
  30.2, a new 20-item top-level request list, an expanded transcript window and hourly sampling
  (`economic-index-2026-06-appendix`, claims 1–7).
- **Randomised tie-breaking makes the pipeline non-deterministic — single statement.** "It is asked to
  provide pairs of {task, confidence (1-5)}, and we randomly choose a task among those with the highest
  confidence" (ibid., Definitions 5).
- **An artifact classifier exists, with 32 single-label options and a published taxonomy — single-wave.**
  (ibid., Definitions 6–7.) "Our classifier identified 93% of Claude conversations as producing an artifact"
  (`economic-index-2026-06-report`, p.9).
- **External researchers have run studies on Anthropic's own usage data, once — single pilot.** Three
  partners, "roughly 250,000 Claude.ai or Claude Code conversations from April-May 2026"; redaction "Less
  than 5% of categories and conversations were affected in each study", with per-run figures 1.9%/4.28%,
  3.33%/3.85%, 1.8%/2.96%; a third-party red team "were unable to reidentify any users or find any violation
  of our threat model" (`independent-research-access-2026-08`, claims 13, 16, 17, 18).
- **Two measurement facts published only there.** "roughly 3% of conversations were not clearly described by
  the cluster they were assigned to", with the footnote that behaviour and emotional-state facets "were not
  validated in the original paper"; and "As of May 2026, we estimate that roughly 10% of Claude.ai
  conversations span multiple topics" (ibid., claims 21–22).

**(c) Where it is open.**

- **No validation of the sixth wave's new pipeline.** The rebuild, the O\*NET vintage change and the expanded
  transcript window are validated by "some example classifications using transcripts drawn from WildChat, an
  open-source dataset of user-ChatGPT interactions" — seven examples, two of them adjudicated by the authors
  (`economic-index-2026-06-appendix`, claim 8, Limitations 1–4); no old-versus-new agreement rate, no
  position-bias test, no tie-break reliability figure (**[inference]**, ibid., items 1–6).
- **The artifact classifier has no reported accuracy** and the "None" residual bundles abandoned exchanges,
  errors and unanswered clarifying questions (`economic-index-2026-06-report`, fn 2 p.18; **[inference]**,
  items 23–24).
- **Task success, the most load-bearing primitive, is the least validated** (**[inference]**,
  `economic-index-2026-01-report` item 1).
- **Occupation inferred from the task has never been checked against a self-report**, although the sixth
  report has ~9,700 respondents' self-reported SOC codes alongside their linked sessions (**[inference]**,
  `economic-index-2026-06-report` item 11).
- **The pilot does not scale as run.** "all of this made the pilot slow for an AI lab's normal research speed
  and resource intensive to run. Both factors present a challenge to effectively scaling it"
  (`independent-research-access-2026-08`, claim 15) — with no duration, cost or headcount published.
- **Public datasets are the wrong instrument for validation.** "WildChat skews toward casual and creative
  use, unlike Claude traffic, so some questions that performed well on WildChat produced misleading
  categories once applied to actual Claude conversations" (ibid., claim 20).
- **Measurement is expected to decay.** "Accurately classifying the work that Claude does will remain a
  moving target. For example, as AI capabilities increase, AIs may increasingly interact and exchange with
  each other, perhaps in ways inscrutable to humans or simple classifiers"
  (`economic-index-2026-06-report`, p.32).
- **Released code stopped after the third wave.** Only `release_2025_09_15` ships a code library; the three
  2026 waves ship none (`economic-index-2026-01-report`, §Data and methods, "No code was released for this
  wave").

**(d) What the Institute says it wants next.** `Share 1`: granularity, cadence and an early-warning function
(`institute-agenda-2026-05`, Definitions 6). `WILD-6` "Enabling research:" — "Are there transparency regimes
and tools that can enable a broad set of people, not just frontier AI companies, to easily study real-world AI
usage?" (ibid., Open questions 33), which the wiki file records as the agenda's clearest kept promise, via
`independent-research-access-2026-08`. `WILD intro ¶1` commits to tool-building "ranging from software for
better observability of our platform to tools for conducting large-scale qualitative surveys" (ibid.,
Definitions 28). The Economic Policy Framework asks the same of the state and of itself: "reporting
requirements for AI labs and firms—including Anthropic—on deployment patterns and workforce effects", and
concedes "data from a single company cannot tell the whole story"
(`programme-and-product-pages`, `economic-policy-framework-2026-06`, PDF p.5).

**(e) The mentor's interests ⟨mentor⟩.** ⟨mentor⟩ The mentor's methodological signature is robustness by
rank: "the Spearman (rank-rank) correlation of job exposure across many resolutions to these questions is
exceedingly high" (`labor-market-impacts-2026-03`, fn 6 p.16), implemented as the ten-measure heatmap
(`labor-market-impacts-2026-03-appendix`, Fig 4 p.10). ⟨mentor⟩ He also states the judgement problem
explicitly: "There are judgment calls involved at every step. Should the Eloundou et al. (2023) measure enter
as {0, 0.5, 1} or something else? What determines 'significant' use?"
(`labor-market-impacts-2026-03`, fn 6 pp.15–16). ⟨mentor⟩ In the retraining review he applies the same
discipline to other people's evidence, and sets the standard: "Impose a high evidentiary standard. We favor
randomized trials, along with studies that make prima facie plausible claims to frame compelling natural
experiments." (`worker-retraining-2026-08`, p.5.)

**(f) Reach of the public data.**

| Open item | Reach |
|---|---|
| Any classifier-validation re-run | **Blocked.** Releases are aggregates only; no transcript, no per-conversation label, no confidence field (§Cuts 26, 27b). |
| Old-versus-new pipeline agreement | **Blocked.** The two pipelines' outputs exist only as separate waves on different taxonomies; cluster ids "do not survive a wave" (§Cuts 15a) and there is "No request-hierarchy file after 2025-09-15" (§Cuts 25). |
| Reproducing published numbers at all | **Feasible and documented, wave by wave** — the atlas records the exact specification for the AUI, automation, task mix, Ginis, the June pooling rule, the v1/v2 base and blank thinking fractions (§Conventions). Two general traps: `NA` is Namibia, and 2026-03-24 also needs `na_values=[]` because `geo_id` `NONE` is a real pseudo-geography (§Traps 1–2). |
| Suppression and thresholds | Documented but not decomposable: "Suppression is always silent. No release has a suppression flag or a count of suppressed cells"; in June 2026 median `pct` sums per unit-month are 36.9 (country `onet` L0) and 16.7 (subregion), and country `usage_pct` sums to only 82.03 / 87.49 (§Thresholds). |
| Released code | Only `release_2025_09_15` ships `code/` (6 `.py` + 4 `.ipynb`), and "The released code disagrees with the released index" on the AUI denominator (§Releases at a glance; §Conventions, AUI). |
| The partner-cluster data | CC BY 4.0, 2,077 rows over four files, one April–May 2026 window; "Treat it as a separate instrument, cite it as one, and read Anthropic's interpretation guidance first" (§Supplementary sources). |
| Whether the public releases changed after the Institute's cadence promise | **Answered: once.** "There is no release after 2026-06-26… So in the released data the granularity-and-cadence promise is kept exactly once, by the June 2026 schema change" (steward answer 5; §Revision). |
| A second distribution channel | Exists and is incomplete: `economic-research.anthropic.com/releases/econ-index/` serves the two most recent waves only, byte-identical to Hugging Face, with misleading names — the file inside `release-2026-03-24.zip` is the 5–12 February 2026 window (§Hugging Face is not the only channel; steward answer 7(d)). |

---

### T9 · The survey, perceptions and self-reported effects

**(a) Publications, in date order.** `anthropic-interviewer-2025-12`; `survey-81k-interviews-2026-03`;
`survey-81k-interviews-2026-03-appendix`; `economic-index-survey-2026-04-announcement`;
`survey-81k-economics-2026-04`; `coding-agents-social-sciences-2026-05` (a different population);
`economic-index-2026-06-report` ch.3; `econ-scenarios-explorer-2026-09` (a general-population survey);
`econ-scenarios-paper-2026-09` App. B.

**(b) What is established.**

- **An instrument exists, it is conversational, and it runs on the consumer surfaces only — repeated.**
  "Anthropic Interviewer is a tool, powered by Claude, that conducts detailed user research interviews
  automatically and at scale"; "*Anthropic Interviewer is not currently available for our commercial products
  such as Claude for Work and the Anthropic API.*"
  (`economic-index-survey-2026-04-announcement`, Definitions 12–13, quoting the linked privacy article).
- **The survey is monthly, rotating, and invited from a small random sample — single announcement.** "Each
  month, we will invite a small, randomly selected group of Claude users: anyone with a personal account at
  least two weeks old may be invited. We will rotate the sample each month" (ibid., Definitions 6).
- **Perceived threat tracks observed exposure and career stage — single-wave.** 1.3pp per 10pp of exposure,
  3× top against bottom quartile, "One fifth of the respondents in our survey voiced concern about economic
  displacement", and "early-career respondents were much more likely to express concern"
  (`survey-81k-economics-2026-04`, claims 2–4, 6).
- **Self-reported productivity gains are large, skewed and mostly captured by the user — single-wave.** Mean
  inferred productivity 5.1 of 7, with 3% negative or neutral and 42% unclear; scope cited by 48% and speed
  by 40% of those mentioning productivity; "10% of respondents who named a recipient said that employers or
  clients were asking for and getting more work"; "only 60% of early-career workers indicated that they
  personally benefited from AI, compared to 80% of senior professionals" (ibid., claims 7–8, 13–15).
- **Speedup and fear are U-shaped — single-wave.** "the relationship between speedup and perceived job threat
  is U-shaped"; the left-hand bar is respondents who report being slowed down (ibid., claim 16).
- **The first linked survey–usage wave exists, at individual level — single-wave.** ~9,700 respondents, up to
  20 randomly sampled sessions each in a mid-May to early-June window, respondents with fewer than five
  sessions excluded (`economic-index-2026-06-report`, p.19).
- **Expectations about the pace of progress are near-uniform while beliefs about the present are not —
  single-wave.** "the best-fit lines for reported and anticipated exposure 12 months from now … are
  essentially parallel"; "a software engineer and a construction manager anticipate roughly the same
  increment of progress within their profession" (ibid., pp.22–23, Fig 3.3). Reported exposure is "about 10
  percentage points lower among high-income countries" and about 10pp lower for those with 15+ years of
  experience (pp.24, Fig 3.4).
- **Heavier delegators are more optimistic, not less — single-wave.** "Across all six dimensions, people with
  a higher share of automated sessions feel more optimistic"; controlling for tenure "doesn't meaningfully
  change" it (ibid., p.27, Fig 3.6).
- **Perceived risk to others exceeds perceived risk to self — single-wave.** "10% rated losing their own jobs
  as likely or very likely", against a JOLTS-implied "~13.4% annualized" involuntary-separation incidence;
  "over one third stating that the probability of a junior colleague losing their job in the next year was
  over 60%" (ibid., pp.26, fn 10 p.31).
- **The survey frame is not the population, and Anthropic says so — repeated.** "The Economic Index Survey is
  not representative of the general population. We reach a random sample of Claude users, there may be
  selection in who completes the survey, and we filter out infrequent users from our analysis" (ibid., p.20);
  "our survey is limited to users of personal accounts on Claude.ai who chose to respond"
  (`survey-81k-economics-2026-04`, p.11).

**(c) Where it is open.**

- **The monthly promise is not yet exercised.** "Collecting these data monthly will enable measurement of not
  just what people experience and expect, but how quickly their views shift"
  (`economic-index-survey-2026-04-announcement`, Open questions 1) — the wiki file records that no
  wave-over-wave survey comparison exists in the corpus.
- **The lead-indicator conjecture is asserted and untested.** "Combined with Claude usage data in a
  privacy-preserving way, these first-hand accounts can surface change before it shows up in aggregate labor
  market data" (ibid., Open questions 2) — "the single most load-bearing untested conjecture on the page".
- **Structured replication is asked for by the authors.** "because the survey is open-ended, our measures are
  based on what respondents happen to mention; these findings should be confirmed in structured surveys that
  ask about these topics directly" (`survey-81k-economics-2026-04`, p.11).
- **Classifier-derived survey variables are unvalidated.** Seven constructs are classifier outputs and none
  is validated against human coding (**[inference]**, ibid., item 4); coverage is partial throughout — 61% of
  respondents have no occupation label, ~50% no career stage, 42% no productivity indication, ~75% no named
  beneficiary (ibid., claims 8, 21, and §Data and methods).
- **Non-response is measurable and not measured.** The linkage infrastructure means usage is observable for
  invited non-respondents (**[inference]**, `economic-index-survey-2026-04-announcement` item 3).
- **The self-reported productivity numbers are never triangulated** against the estimator-based measures
  (**[inference]**, `economic-index-2026-06-report` item 31).
- **Person-level observed exposure is not computed**, although linked sessions would allow it and would
  remove the "not everybody does every task" confound the report itself names (**[inference]**, ibid.,
  item 12).
- **The engagement promise of the launch note is unkept in the sampled population.** "It will engage with
  workers and industries facing displacement" (`institute-launch-2026-03`, *¶6*); the wiki file records that
  "No publication in the corpus samples workers or industries selected for displacement" (ibid., Open
  questions 11).

**(d) What the Institute says it wants next.** `ED-9` "Worker views of their jobs:" — "How are workers across
the economy experiencing changes in their professions? How much influence do they have over these changes, and
can 'worker' power be preserved or transformed?" (`institute-agenda-2026-05`, Definitions 23). `ED-7` names
the survey as the instrument: "Our Anthropic Economic Index Survey will provide monthly signals of how people
see AI affecting their work, and what they expect for the future" (ibid., Definitions 21). `ED-12` asks about
the role of paid work and about "what can we learn from historical or contemporary populations where work has
been scarce or optional" (ibid., Definitions 26).

**(e) The mentor's interests ⟨mentor⟩.** ⟨mentor⟩ The economics pass over the 81k interviews is
Massenkoff-first-authored, and the acknowledgements state the division: "Maxim Massenkoff led the analysis and
wrote the blog post" (`survey-81k-economics-2026-04`, PDF p.12). ⟨mentor⟩ Its stated methodological claim is
that qualitative data should generate quantitative hypotheses: "the interviews surface real insights about
people's feelings around the economics of AI, showing how qualitative data can surface quantitative
hypotheses" (ibid., p.11). ⟨mentor⟩ Its substantive claim is that perception tracks measurement: "people's
intuitions track the usage data: they worry most about AI's effect in the jobs where we observe Claude doing
the most work" (ibid., p.11). ⟨mentor⟩ He is also first-named author of the report carrying the first linked
survey wave (`economic-index-2026-06-report`, p.1, ch.3).

**(f) Reach of the public data.**

| Open item | Reach |
|---|---|
| Any survey variable | **Blocked.** "there is no Anthropic survey data anywhere in the dataset", and no `facet`, `variable`, `metric_id` or `category_name` in any wave matches `survey|respond|sentiment|expect|concern|opinion|interview` (§Components, Survey; steward answer 8). Run that regex on structural columns only — over `cluster_name`/`node_name` it returns ~180 false positives from O\*NET task text (same). |
| The 81k responses | **Blocked.** `Anthropic/AnthropicInterviewer` holds "exactly 1,250 transcripts" with two columns, `transcript_id` and `text`; "The 80,508 interviews of the March 2026 feature are not released, at any grain", and no percentage in that feature is reproducible from the file (steward answer 9; §Supplementary sources). |
| Respondent- or country-level survey cuts | **Blocked.** The Interviewer file carries no demographics, occupation, country, date or label (steward answer 9). |
| Linking perception to exposure | Only through published occupation-level numbers; job-level exposure joins on `occ_code` "and nothing else — no geography, no title crosswalk beyond `title`" (steward answer 8). |
| The only survey file in the repository | The **Census** BTOS national workbook in `release_2025_09_15/data/input/BTOS_National.xlsx`, "used as the input to Figure 3.1 and never joined to any Claude data" (§Components, Survey). |
| Wave-over-wave survey change | **Blocked, and there is nothing to compare to.** No release after 2026-06-26 (§Revision), and no survey variable in any release. |
| Non-response comparison | **Blocked.** No account identifier and no invited-sample indicator anywhere (§Cuts 26, 27b). |

---

### T10 · Retraining, adjustment and the policy response

**(a) Publications, in date order.** `programme-and-product-pages`
(`economic-advisory-council-2025-04`, `economic-futures-launch-2025-06`,
`becker-friedman-partnership-2025-07`, `economic-futures-symposium-proposals-2025-10`,
`economic-policy-responses-2025-10`, `economic-futures-uk-europe-2025-11`,
`economic-policy-framework-2026-06`, `economic-futures-research-fund-2026-07`);
`worker-retraining-2026-08`.

**(b) What is established.**

- **Retraining is the most favoured policy and the evidence for it is positive but small — the corpus's one
  meta-analysis.** "Among experts and the public, worker retraining is the most popular policy for mitigating
  labor market disruption from AI"; on 146 impact estimates from 56 US randomised trials, programmes
  "increased employment by 1.7 percentage points, compared to a baseline employment rate of 63% in the control
  group. They increase earnings by $800 per year on average" (years 3–5), against costs averaging "$13,598
  per treatment group member" (`worker-retraining-2026-08`, pp.2, 6). Medium-term impacts are 2.8pp and
  $1,139 (p.6).
- **The fiscal arithmetic, which is what a policymaker would quote — single review.** "training programs
  ultimately generate flows to government equal to about three-quarters of their costs… So when government
  funds them, the long-term fiscal cost is only ~24% of the upfront cost", with a narrow benefit–cost ratio of
  1.44, a wide one of 1.80, an MVPF of 2.52 and a societal IRR of 5.97% (ibid., pp.6, 61).
- **Sector programmes are the exception, at a price — single review.** "Some 'sector programs' boost earnings
  10 times as much… A few programs have lifted pay by $5–10,000 per year"; cost $11,602 against $13,598 with
  a discounted earnings benefit of $60,319 against $14,146, a benefit–cost ratio of 7.18 (ibid., pp.2, 9, 77).
  But "They filter out >80% of applicants" (p.2), control-group employment is 80% against 60% for other
  training experiments (p.76), and replication has mostly failed: "An attempt to replicate one strong
  program, the CET in San Jose, failed at all 14 trial sites" (p.10).
- **The big federal programmes did not move the needle — single review.** "the main-line programs have not
  moved the needle much on labor market outcomes" (ibid., p.36); Job Corps "did not affect employment or
  earnings in follow-ups extending 20 years" (p.7).
- **Training helps more when unemployment is high, for a reason that is not flattering — single review.**
  "Where the unemployment rate is 1 point higher, a training program boosts employment by 1.2 points more in
  the medium term"; the favoured mechanism is that competition for training rises so "each training program
  becomes more needed and less redundant" (ibid., pp.63–64).
- **Anthropic's policy framework is tiered on the unemployment rate — single document.** Tier 1 "~5%
  unemployment with churn", Tier 2 "~10%", Tier 3 "unemployment exceeding historical peaks"
  (`programme-and-product-pages`, `economic-policy-framework-2026-06`, PDF pp.7, 10, 12), with the framework's
  one empirical claim about AI being "entry-level workers in occupations most exposed to AI have seen weaker
  employment growth in recent years" (PDF p.1, fn 1 citing Brynjolfsson et al. and
  `labor-market-impacts-2026-03`).
- **The money and its object are on the record — single document.** "$200 million commitment to an Economic
  Futures Research Fund" and "A $150 million national fellowship program", "totaling $350 million" (ibid., web
  page), with the Fund's five priorities and their fundable directions published in July 2026 (ibid.,
  `economic-futures-research-fund-2026-07`, Open questions).

**(c) Where it is open.**

- **There is no evidence on retraining under AI displacement, and the review says so first.** "We have no
  research evidence on how well job training helps people adjust when large language models start doing their
  jobs." (`worker-retraining-2026-08`, p.80.)
- **Current programmes are probably not adequate to the scenario.** "the impacts are small enough that they
  would not leave a dent in a persistently high unemployment rate"; "it seems doubtful that we currently have
  programs capable of meeting the moment" (ibid., pp.85, 3).
- **Short programmes are the wrong instrument for skilled workers.** §8.2's heading: "Short-duration programs
  are ill-matched to the needs of more-skilled workers" (ibid., pp.83–84), and deep reskilling "takes years"
  — the Danish injured-worker case earned 25% more "after a typical four years of college" (p.83).
- **The trigger-based design fails for the most likely AI channel.** "When the labor market transforms not
  through firings, but by firms not hiring new people in certain roles when old people leave or when the firms
  grow, trigger-based aid will not fire." (ibid., p.84.)
- **The proposed remedy is an experiment that has not been run.** "A 'fire drill' evaluation meant to rapidly
  scale and test leading job retraining programs could pay lasting dividends" (ibid., p.3); the Research Fund
  restates it as a fundable direction (`programme-and-product-pages`,
  `economic-futures-research-fund-2026-07`, priority 2).
- **Tier 3 has no policy recommendation.** "We are not yet ready to advocate specific policies for this
  scenario. But we can name a few candidate mechanisms" (ibid., `economic-policy-framework-2026-06`, PDF
  p.13).
- **Promised programme outputs that the corpus does not contain.** No LSE/London symposium awardee list; no
  award list or funded-project output from the 2025 rapid awards; no first pilot programme of the Research
  Fund; no delivery of the $150M fellowship; no output of the BFI partnership; no membership change to the
  Advisory Council after 2025-05-09 (ibid., Open questions, each marked in the wiki file).
- **Who bears the incidence of the new revenue instruments is unknown.** "we lack evidence on who would bear
  the economic incidence of such taxes, and how different designs would affect collected revenue and adoption"
  (ibid., `economic-futures-research-fund-2026-07`, priority 4 rationale).

**(d) What the Institute says it wants next.** `ED-5` "Sharing the gains: What pre- or re-distributive
mechanisms could effectively spread the gains from AI development and deployment more broadly?"
(`institute-agenda-2026-05`, Definitions 19). `ED-8`'s diffusion dials (ibid., Definitions 22). The Research
Fund's five priorities are the most specific published statement of what Anthropic is paying others to answer,
including "Longer-duration unconditional income pilots at livable levels", "RCTs testing the design of
pre-distributive capital accounts at scale" and "Guaranteed-jobs pilots for displaced or long-term unemployed
workers" (`programme-and-product-pages`, `economic-futures-research-fund-2026-07`, priorities 3–5). The EPF's
measurement asks are quoted at T8(d).

**(e) The mentor's interests ⟨mentor⟩.** ⟨mentor⟩ The retraining review is the mentor's second-authored
publication with an independent researcher (`worker-retraining-2026-08`, p.1), and it is the corpus's only
systematic evidence synthesis. ⟨mentor⟩ Its posture is the same scepticism he brings to exposure measures —
"ineffective until credibly proven otherwise", "stars are generally found, not made" (ibid., §Source, terms
it fixes) — and its central recommendation is an evaluation design rather than a policy: "Public and private
funders should aggressively support demonstrations, evaluations, and scaling of sector programs" (§8.4,
p.84). ⟨mentor⟩ The review is also where his own exposure measure is used to say who is at risk: "If current
data on AI usage are any guide, college-educated workers—software developers, paralegals, accountants—are most
at risk (Massenkoff and McCrory 2026). But this is highly uncertain." (ibid., p.4.)

**(f) Reach of the public data.**

| Open item | Reach |
|---|---|
| Any retraining outcome | **Not an Index question.** The review's own code and data are third-party (`github.com/droodman/job-training-meta-analysis`, `worker-retraining-2026-08`, §Source); nothing in the Economic Index releases bears on programme evaluation. |
| Who is at risk, for targeting a programme | Job-level `observed_exposure` on 756 detailed 2018 SOC codes is the released instrument (steward answer 8), joinable to BLS Employment Projections on `occ_code` (755 of 756 matched; §Supplementary sources). |
| Entry-level and youth effects | **Blocked in the releases** — no demographics anywhere (§Cuts 28). External: CPS, and the ETA 203 UI series the appendix used (`labor-market-impacts-2026-03-appendix`, Definitions 19). |
| Unemployment as the trigger variable | External. No employment, wage or unemployment series ships in any 2026 release (§Cuts 29); BLS OEWS and `download.bls.gov` return 403 from this sandbox and `web.archive.org` is egress-blocked (steward answer, Open for the record). |
| Incidence of compute or token taxes | **Blocked.** No token or cost measure outside the 1P API indices, which are re-based to mean 1.0 and global only (§Components; §Cuts 27). |
| Sector-programme targeting by task mix | Feasible in principle at country and subregion grain through `request` L1/L2, with the fill caveat (median 39 of 104 `request` L1 cells per country in Feb 2026; §Cuts, Family B fill table); no industry (NAICS) column exists (§Cuts 26) — `steward?` on a request-cluster-to-sector mapping. |

---

### T11 · Scenarios and macro aggregation

**(a) Publications, in date order.** `productivity-gains-2025-11` (the aggregation method);
`economic-index-2026-01-report` ch.4 (the CES generalisation);
`programme-and-product-pages` (`economic-policy-framework-2026-06`, the scenario tiers);
`econ-scenarios-explorer-2026-09`; `econ-scenarios-paper-2026-09`.

**(b) What is established.**

- **A published mapping from five parameters to six macro paths — single model.** "a simple, integrated
  economic framework that converts a small set of parameters … into paths for productivity, growth, wages,
  the labor share, job reallocation, and unemployment from now until 2030"
  (`econ-scenarios-paper-2026-09`, p.3), with "The scenarios are not predictions, and we attach no
  probabilities to them" (p.3).
- **Three scenarios, and their 2030 outcomes — single model.** GDP above the no-AI path 1.6% / 8.3% / 32.4%;
  GDP growth 2.4 / 5.4 / 15.4 percent a year against 2.0 without AI; average wage +0.7 / +2.1 / +9.7 percent;
  cognitive wage +0.4 / −0.3 / −11.5; labour share 59.4 / 56.1 / 45.2 against 60.0; cognitive unemployment
  2.9 / 4.5 / 17.9 percent (ibid., Table 3 p.31).
- **The innovation channel is small in every scenario, and this is flagged as a surprise — single model.**
  "One surprising finding of our model is that the growth speedup from AI in innovation is relatively minor,
  even in the extreme change scenario… Labor productivity rises through this channel by well under one
  percent in all three scenarios" (ibid., p.4); the ideas stock is 0.61% above the no-AI path in the extreme
  scenario against measured TFP 13.4% (Table 3 panel D).
- **The distributional arithmetic, stated explicitly — single model.** In the extreme scenario "All of the
  increase in GDP therefore accrues as capital income, which is 81 percent above its no-AI path", the
  cognitive wage bill is "31 percent below its previous path", and "a transfer of about 9 percent of GDP,
  roughly the size of Social Security and Medicare combined, would hold cognitive workers' income at its
  no-AI level" — with "Transfers of that scale in response to technological change have no precedent"
  (ibid., p.35).
- **The public lands near the middle scenario — single survey.** 10,980 US adults, 11–23 August 2026; implied
  `m_2030` 0.44, `d_2030` 0.40, `ψ` 0.47, `a_2030` 0.44, `μ` 0.064 (medians), and "GDP is 8.6 percent above
  its no-AI path and the unemployment rate in both cognitive occupations and in the broader economy is around
  4.6 percent" (ibid., pp.29–30, 36, Tables 2 and 4).
- **The model is anchored on three Index-programme numbers — single model.** The affected mass from observed
  exposure: "It averages 0.22 in the cognitive group, 0.01 in the other, and 0.14 overall, so m = 0.14"; the
  automation share from the Index's collaboration facet, "about half of use on Claude.ai and about three
  quarters on the API"; and the per-instance gain set at 0.30–0.45 in logs, "about a quarter of the gain of
  1.6 estimated from conversations with Claude (Tamkin and McCrory, 2025)" (ibid., pp.27–28).
- **The stream's own statement of the division of labour — single page.** "While our Economic Index measures
  how AI is being used across the economy right now, this scenario explorer is about looking ahead."
  (`econ-scenarios-explorer-2026-09`, claim 2.)

**(c) Where it is open.**

- **Current macro data do not discriminate between the ends of the range.** "Two interpretations are
  consistent with this fact. One is that we are in a modest change scenario … The other is that we are only
  at the very beginning of a more extreme scenario." (`econ-scenarios-paper-2026-09`, p.4.)
- **The model does not follow workers.** "Reviewers pointed out that the model does not follow individual
  workers, so it can only paint a very coarse picture of the costs of job displacement"
  (`econ-scenarios-explorer-2026-09`, Open questions), one of five reviewer criticisms the page records as
  unresolved.
- **Whether exposed occupations shrink at all.** "Some questioned whether occupations exposed to AI will
  shrink at all rather than grow" (ibid.).
- **Recursive self-improvement is hard-coded, not modelled.** "the gains from recursive self-improvement
  (RSI) can be thought of as being hard-coded into a_t" (`econ-scenarios-paper-2026-09`, p.17).
- **Everything downstream of 2027 is assumption.** "almost all of the divergence comes after 2027, a year and
  a half from the mid-2026 anchor" (ibid., pp.4, 38).
- **The productivity aggregation's own scope conditions are neither tested nor discussed** — Hulten's
  first-order result in "a competitive equilibrium without distortions" (**[inference]**,
  `productivity-gains-2025-11` item 8), and the ten-year universal-adoption horizon is asserted and never
  varied (item 4).
- **The model is a work in progress by its own account.** "The scenario explorer is a work in progress, and we
  expect it to evolve both as we invest more time and as economic research itself develops"; "Other criticisms
  are still open, and we plan to address many of them in future versions"
  (`econ-scenarios-explorer-2026-09`, Open questions).

**(d) What the Institute says it wants next.** `ED intro ¶2`: "We'll also explore other methods to sharpen
our models of how powerful AI could affect society, whether by driving job loss, unprecedented economic
growth, or other effects." (`institute-agenda-2026-05`, Definitions 13.) `ED-4` (productivity and innovation)
and `ED-5` (sharing the gains), quoted above. The explorer states what the model is for: "This model,
alongside our full research portfolio, will inform the research Anthropic funds to identify effective
interventions for labor market disruptions. It'll also inform the policy ideas we propose"
(`econ-scenarios-explorer-2026-09`, Open questions). The launch note's incubation promise — "forecasting AI
progress" (`institute-launch-2026-03`, *¶5*) — is recorded as delivered in part by this thread (ibid., Open
questions 8).

**(e) The mentor's interests ⟨mentor⟩.** ⟨mentor⟩ Massenkoff is not an author of either scenario
publication (`econ-scenarios-paper-2026-09`, p.1: Korinek, Jones, Sacher, Cotter, McCrory). His contribution
to the thread is the measure it is calibrated on: the affected-mass anchor is "the observed-exposure measure
of Massenkoff and McCrory (2026)" (ibid., p.25, and Table 1's source line, pp.23–24). ⟨mentor⟩ The thread
therefore contains the corpus's clearest instance of one mentor publication being discounted against another:
the scenario paper takes a per-instance gain "about a quarter of the gain of 1.6 estimated from conversations
with Claude" (ibid., p.27) — see §Cross-thread tensions, pair 3.

**(f) Reach of the public data.**

| Open item | Reach |
|---|---|
| Re-anchoring `m` (affected mass) | **Feasible.** `job_exposure.csv` (756 SOC rows) is the published measure; averaging it over occupations needs employment weights, which are external (§Components, Labour-market files; §Cuts 30). |
| Re-anchoring `ψ` (automation share) | **Feasible, with the base stated.** The collaboration facet exists in every wave; the Claude.ai/API contrast the paper cites is the 2025-09-15 pair 49.0980 / 77.3723 on the all-seven-pattern base (§Conventions, automation table). |
| Re-anchoring `d` (diffusion) | **External.** The anchor is Census BTOS firm adoption, not Claude data; the only BTOS file in the repository is the national workbook in `release_2025_09_15/data/input/` (§Components, Survey). |
| Re-anchoring `a` (gain per instance) | Time primitives exist at all three grains from 2026-01-15 (§Cuts, Family B primitives row), but the units differ by wave (§Traps 8) and the paper's own comparison is to a conversation-level estimate that is not released. |
| Cognitive vs all-other occupations | The paper's split is by 2018 SOC major group (`econ-scenarios-paper-2026-09`, fn 10 p.25). In the releases, `soc_occupation` exists only in the 2025-09-15 enriched file and in 2026-06-26's `soc_occupation` ladder; it is absent at every grain in 2026-01-15 and 2026-03-24 (§Cuts 13); the 2025-09-15 state-level version is "unusable as a mix (74.28% mean `not_classified`)" (§Cuts 14). |
| The 10,980-respondent survey | **Blocked.** No Institute-branded dataset is public; `author=Anthropic` lists 14 datasets and "none is survey microdata, the 81k responses or a scenario explorer" (steward answer 6). |
| Testing the model against outcomes | **External.** No GDP, wage, employment or unemployment series in any 2026 release (§Cuts 29). |

---

## Cross-thread tensions and unconfronted pairs

Stated neutrally: each is a place where two publications in the corpus say things that have not been
reconciled in print. None of these is a claim that either side is wrong.

1. **Early adopters automate more, against experienced users collaborating more.** The September 2025 report
   speculates "perhaps that early adopters in each country tend to use AI in a more automotive way—but more
   research is needed here" (`economic-index-2025-09-report`, pp.26–27). The March 2026 report finds the
   opposite at user level and says so: "This pushes back against a hypothesis we made last year that
   automated use may be more typical of more experienced, sophisticated users"
   (`economic-index-2026-03-report`, p.19, and Table 2.1's directive 38.1% → 29.4%). The two are at
   different units — country and user — and neither publication reconciles them.

2. **Large measured speedups, against no measured speedup in a trial.** Anthropic's estimator-based work
   reports "Claude estimates that AI reduces task completion time by 80%" and 1.8pp of annual labour
   productivity (`productivity-gains-2025-11`, pp.2–3, Fig 7 p.15). Anthropic's randomised trial reports "we
   did not find a statistically significant acceleration in completion time with AI assistance" (p = 0.391)
   and a 4.15-point comprehension penalty (`skill-formation-rct-2026-01`, pp.2, 9). The trial's web page
   offers the reconciliation — "the two studies ask different questions and use different methods… though
   more research is needed to understand this relationship" — and the productivity note does not mention the
   trial. Note also that the trial's treatment was GPT-4o, not Claude (ibid., p.6).

3. **Anthropic's macro model discounts Anthropic's own productivity estimate by four.** The scenario paper
   sets the log gain per AI-performed instance at 0.30–0.45, "about a quarter of the gain of 1.6 estimated
   from conversations with Claude (Tamkin and McCrory, 2025)", preferring field trials
   (`econ-scenarios-paper-2026-09`, p.27). No publication in the corpus adjudicates between the two.

4. **Persistent returns to expertise, against a coding background becoming less relevant.** The same paper
   reports a novice-to-expert verified-success gradient of 15% to 33% and "It appears that coding agents are
   making a coding background less relevant to successful programming"
   (`claude-code-expertise-2026-06`, Fig 5 p.13, p.14). Its own framing holds both: expertise is
   task-specific, not occupational (pp.6–7). The tension is internal and named in neither the paper nor the
   appendix.

5. **Fear tracks exposure, while exposure has produced no detectable employment effect.** The exposure paper
   reports no differential unemployment rise with a ~1pp detectability floor
   (`labor-market-impacts-2026-03`, pp.11–12); the survey pass over the same measure reports that the top
   exposure quartile "mentioned the worry three times as often as those in the bottom 25%"
   (`survey-81k-economics-2026-04`, p.3). The word "unemployment" does not appear in the survey paper
   (recorded in that file's Verification).

6. **Delegation and learning.** The sixth report's survey finds "heavier delegators report learning at the
   same rate as everyone else" and that perceived skill value rises with automation share
   (`economic-index-2026-06-report`, p.28, Fig 3.7). The skill-formation trial finds that delegating
   generation without asking for explanation is associated with the lowest comprehension scores
   (`skill-formation-rct-2026-01`, p.14, Fig 11 p.13). One is self-report on a linked user sample, the other
   an experiment on 52 developers; no publication puts them side by side.

7. **Within-US convergence, against cross-country divergence — in one figure.** State AUI Gini falls
   0.37 → 0.31 → 0.29 while country AUI Gini moves 0.48 → 0.46 → 0.50
   (`economic-index-2026-03-report`, Fig 1.5 p.10). The text reports the country rise "over the same period"
   and does not address the November dip; the convergence horizon for states was simultaneously revised from
   "2-5 years" (`economic-index-2026-01-report`, p.6) to "5-9 years" (`economic-index-2026-03-report`, p.10).

8. **Cost is immaterial, and cost has a negative elasticity.** "The positive correlation between cost and
   usage suggests that cost plays an immaterial role in shaping patterns of enterprise AI deployment"
   (`economic-index-2025-09-report`, p.41) sits beside "each 1% cost increase is associated with a 0.29%
   reduction in usage frequency" (p.42) and the companion blog's "fundamental model capabilities … matters
   more to businesses than the cost of completing the task itself"
   (`economic-index-2025-09-blog`, claim 39). The wiki file records all three as published
   (`economic-index-2025-09-report`, item I3).

9. **Geography's measure gets finer and geography's reporting stops.** The sixth release ships
   `usage_per_capita_index` for countries and US states and a 652-unit subregion grain
   (`economic-index-2026-06-report`, Definitions 46–47), and the sixth report publishes no AUI figure, no
   country ranking and no state map (ibid., §Notes on the cuts). No publication explains the gap.

10. **The Index as a capability claim, against the Index's own caveat.** The Institute's founding note cites
    the Index to support the statement that models "take on a wide range of real work"
    (`institute-launch-2026-03`, *¶1*), while the product post says "the Index reflects patterns in Claude
    usage rather than the labor market as a whole"
    (`programme-and-product-pages`, `economic-index-connector-2026-07`, final paragraph).

11. **Retraining is a Tier 1 instrument, and Anthropic's own review finds its impacts small.** The Economic
    Policy Framework lists workforce training grants among Tier 1 interventions with the note "Evidence is
    mixed on traditional government retraining, but shorter-term programs connected to specific employers and
    sectors have shown significant income gains"
    (`programme-and-product-pages`, `economic-policy-framework-2026-06`, PDF p.10). The review published two
    months later concludes "it seems doubtful that we currently have programs capable of meeting the moment"
    (`worker-retraining-2026-08`, p.3); the wiki file records that the review is not cited in the EPF's
    footnotes (`programme-and-product-pages`, Claims 9 note).

12. **Self-reported productivity, against estimated productivity.** 86% report gains in speed, 82% in scope
    and 69% in quality (`economic-index-2026-06-report`, p.28); the estimator-based figure is 1.8pp of annual
    labour productivity, 1.0–1.2pp after the reliability adjustment
    (`economic-index-2026-01-report`, p.48). The two are never placed on a common scale; the sixth report's
    wiki file records the absence as item 31.

13. **Task-inferred occupation, against self-reported occupation.** The sixth report has ~9,700 respondents'
    self-reported SOC codes and their linked sessions (`economic-index-2026-06-report`, p.19, Fig 3.1), and
    compares respondent shares with employment shares and session shares (claims 60–61) without ever checking
    whether a respondent's task-inferred occupation matches the one they report (**[inference]**, item 11) —
    the inference on which T1, T2, T5 and three prior reports all depend.

14. **Two readings of the same macro silence.** The scenario paper reads muted labour-market effects as
    consistent with both the modest and the extreme scenario
    (`econ-scenarios-paper-2026-09`, p.4); the exposure paper reads a 14% fall in youth job-finding into
    exposed occupations as "some signal of the early effects of AI on employment"
    (`labor-market-impacts-2026-03`, pp.12–13). Neither cites the other on this point.

---

## What the Institute wants that the corpus has not delivered

Agenda and programme items with no publication against them, as of 2026-09-16. Each is quoted, sourced, and
paired with the thread it would sit in. Status judgements are taken from the per-item audits in
`wiki/reports/institute-agenda-2026-05.md` (Open questions, items 10–21; What it did not test, items 1–11),
`wiki/reports/institute-launch-2026-03.md` (Open questions, items 1–17) and
`wiki/reports/programme-and-product-pages.md` (Open questions); each of those files marks its status lines as
the wiki author's inference.

| Agenda item | Quoted | Thread | Status |
|---|---|---|---|
| `ED-2` firm-level economics | "How does AI change the scale at which a firm or team can be most efficient? How concentrated is AI usage across firms? How do changes in concentration of AI adoption translate into markups and labor share?" | T1 | Nothing. The unit of observation in every release is a conversation; `work-at-anthropic-2025-12` is one firm, and that firm is Anthropic. |
| `ED-1` determinants and value capture | "What determines whether a country, region, or city can access AI? If it can access it, how does it capture economic value from AI? … How do free or open weight models contribute to this dynamic?" | T2 | Adoption is described, never explained; no outcome variable is joined to usage anywhere; "open weight" appears in no wiki file. |
| `ED-3` general-purpose technology | "Is AI following the pattern of previous 'general purpose technologies,' where adoption is fastest in high-margin commercial applications, and slowest where social returns exceed private returns?" | T1, T11 | Nothing. The phrase appears in no publication; no corpus publication classifies usage by private against social return. Posed twice on the agenda, with `RD-6`. |
| `ED-6` transaction costs | "How does AI affect systems of exchange and transaction costs in marketplaces? When does access to agents able to negotiate on your behalf improve market efficiency…?" | — | Nothing. "Transaction cost" appears in no wiki file. |
| `ED-8` diffusion dials | "Are there analogous dials that AI companies (at an industry level, in partnership with government) might turn to control the rate of AI diffusion on a sector-by-sector basis?" | T3, T10 | Nothing. No publication estimates a response of usage to any lever a lab controls, although `economic-index-2025-03-report` is a re-measurement 11 days after a model launch. |
| `ED-9` worker power | "How much influence do they have over these changes, and can 'worker' power be preserved or transformed?" | T9 | The experience half is served by four survey publications; bargaining, voice and workplace monitoring appear in no wiki file. |
| `ED-7` emergent tasks | "What new tasks and jobs could emerge as AI automates existing parts of the economy?" | T1 | Nothing, and structurally blocked: every measure classifies into existing O\*NET tasks (§Cuts 15a). |
| `ED-10` long-run supply of senior judgment | "What does this mean for the long-term supply of senior judgment in a field?" | T6 | The gradient today is the best-served question on the agenda; the stock question is untouched, and the named professions — paralegals, junior analysts — are measured nowhere. |
| `ED-11` professions of the future | "What are the professions of the future?" | T6, T11 | Nothing occupational and forward-looking; `econ-scenarios-paper-2026-09` is aggregate, with a two-group occupational split. |
| `ED-12` the role of paid work | "what conditions will allow people to reallocate their time and effort toward other sources of meaning…?" | T9, T10 | Nothing. No release observes non-users or non-work time. |
| `Share 1` early warning | "We'll try to be an early warning signal for significant change and disruption." | T5, T8, T9 | Undefined and untested: no trigger, threshold or lead-lag validation in any publication. The same conjecture is made independently for the survey (`economic-index-survey-2026-04-announcement`, Open questions 2). |
| `Share 1` granularity and cadence | "More granular information from The Anthropic Economic Index, at a higher cadence" | T8 | Kept once, by the June 2026 telemetry change; the released data changed schema once and there is no release after 2026-06-26 (steward answer 5). |
| `Share 3` internal speed-up | "More detailed information about how our work at Anthropic has sped up as a result of new AI tools" | T7 | Pre-empted by `work-at-anthropic-2025-12` (December 2025) and not followed up after the agenda. |
| Launch `¶6` engagement | "It will engage with workers and industries facing displacement, and with the people and communities who feel the future bearing down on them" | T9 | Every survey frame in the corpus is Claude users or a general panel; no publication samples workers selected for displacement. |
| Launch `Hire 3` remit | "joining to connect our economics work to model training and development" | T8 | No publication reports an economics input to what Anthropic trains or ships. |
| `RD-3` telemetry for research speed | "How can we measure the aggregate speed of AI research and development?" | T7 | `work-at-anthropic-2025-12` and `coding-agents-social-sciences-2026-05` measure one organisation and one profession; neither is aggregate. |
| `RD-5` the tech tree | "How uneven is this gradient, and what does the changing composition of scientific progress imply for which human problems get solved first?" | T7 | Nothing; and no research-field cut exists in the data (steward answer 5). |
| Monthly survey waves | "Collecting these data monthly will enable measurement of … how quickly their views shift" | T9 | One published wave; no wave-over-wave comparison. |
| Europe-specific releases | "regular public data releases tracking AI adoption across European industries and regions" | T2 | Promised November 2025; no such release in the corpus, and the five European usage claims do not reproduce as worded (steward answer 7(b)). |
| LSE symposium awardees | "Researchers selected through LSE's and Anthropic's open-call process will present policy proposals" | T10 | The DC list is published; no London list exists in the corpus. |
| Research Fund first pilot | "We'll have more to share soon on our first pilot program" | T10 | Not announced in any entry. |
| $150M fellowship | "A $150 million national fellowship program … We'll have more to share soon." | T10 | Not delivered in any entry. |
| BFI partnership output | "Working hand-in-hand with BFI economists, we hope to develop a more precise understanding of these patterns" | T1, T4 | No output of the partnership is published in the corpus. |
| Advisory Council expansion | "We look forward to expanding membership over time as our research advances." | — | No change recorded after 2025-05-09; what the Council advised is never reported. |

---

## Mentor summary

Maxim Massenkoff's Anthropic publications, with the interests they express. His work outside Anthropic is out
of scope (`team/SETUP.md` §10.4; `wiki/INDEX.md`, "Excluded: the mentor's non-Anthropic work"); the one
exception permitted, and used once above, is that the labour-market paper cites his Occupational Outlook
working paper as the authority for official forecasts adding "little predictive value beyond linear
extrapolation of past trends" (`labor-market-impacts-2026-03`, p.3, fn 1) — a stated interest, not a
summarised publication.

| Publication | Role | Source for the role |
|---|---|---|
| `economic-index-2026-01-report` | lead author (with Appel, McCrory) | p.1 |
| `labor-market-impacts-2026-03` + `-appendix` | first author (with McCrory) | p.1 |
| `survey-81k-economics-2026-04` | first author; "led the analysis and wrote the blog post" | PDF pp.1, 12 |
| `coding-agents-social-sciences-2026-05` + `-appendix` | co-author (Lyttelton, Massenkoff, Wilmers) | §Authors |
| `claude-code-expertise-2026-06` + `-appendix` | second author | p.1 |
| `economic-index-2026-03-report` | lead author, first named | p.1 |
| `economic-index-2026-06-report` | first named author | p.1 |
| `worker-retraining-2026-08` | second author (with Roodman) | p.1 |

**The recurring interests, each with its source.**

1. **Building a displacement measure that can be checked against official series, and saying so.** "An
   established approach may help future observers separate signal from noise"
   (`labor-market-impacts-2026-03`, p.14); the measure is validated against BLS projections, CPS
   unemployment, CPS youth job-starts and ETA 203 UI claims (ibid., pp.8–13;
   `labor-market-impacts-2026-03-appendix`, pp.5–6).
2. **Scepticism about measures and forecasts, expressed as robustness by rank.** "There are judgment calls
   involved at every step" (ibid., fn 6 pp.15–16); ten measure variants compared by Spearman correlation
   (`labor-market-impacts-2026-03-appendix`, Fig 4 p.10).
3. **Stating the design's power, and publishing nulls.** "differential increases in unemployment on the order
   of 1 percentage point would be detectable (this will change as new data comes in, so it is merely a
   ballpark estimate)" (`labor-market-impacts-2026-03`, p.12); "no such correlation using the Eloundou et al.
   measure alone" (p.9); "it has neither widened nor narrowed over seven months"
   (`claude-code-expertise-2026-06`, p.14).
4. **Learning-by-doing and returns to expertise, including revising an Anthropic hypothesis in public.**
   "This pushes back against a hypothesis we made last year" (`economic-index-2026-03-report`, p.19);
   "Sessions rated expert reach verified success more than twice as often as those rated novice"
   (`claude-code-expertise-2026-06`, p.14).
5. **Pricing the work: wages as the value of a task, and compute as its cost.** Task value as "the average
   hourly wage of US workers who perform that task" (`economic-index-2026-03-report`, p.8, fn 5 p.11);
   "more compute is associated with more valuable artifacts"
   (`economic-index-2026-06-report`, pp.2–3, Fig 2.3).
6. **Putting subjective reports against observed measurement.** "people's intuitions track the usage data"
   (`survey-81k-economics-2026-04`, p.11); reported against observed and theoretical exposure
   (`economic-index-2026-06-report`, Fig 3.3 p.23).
7. **Programme evaluation and what actually works for displaced workers.** "Impose a high evidentiary
   standard" (`worker-retraining-2026-08`, p.5); the "fire drill" recommendation (p.3, §8.4 p.84).
8. **What agents do to the production of knowledge itself.** "its distinctive analytical choices could stamp
   our collective understanding of our economy, our society, and ourselves"
   (`coding-agents-social-sciences-2026-05`, Open questions 10), with a randomised experiment promised
   (Open questions 2).
9. **Migration between surfaces as the leading indicator of labour-market change.** "As tasks migrate to the
   API, they may become more exposed to automation" (`economic-index-2026-03-report`, p.9).

---

## Verification

- **Date written:** 2026-09-16. **Corpus snapshot:** the state of `wiki/reports/` and `wiki/INDEX.md` on
  2026-09-16, i.e. 38 `wiki/reports/` files covering 49 `wiki/INDEX.md` entries, whose newest economics
  publication is `econ-scenarios-explorer-2026-09` (2026-09-09).
- **Files read for this map.** All 38 files in `wiki/reports/`. Thirty were read in full. Eight exceeded the
  read tool's per-call limit or were read in part, and for those the sections used are named here so a
  referee can check the same text: `economic-index-2026-01-report.md` (read in two ranges, lines 1–812, i.e.
  in full); `economic-index-2026-06-report.md` (two ranges, lines 1–448, in full);
  `worker-retraining-2026-08.md` (lines 1–300: Source, Claims, Definitions);
  `econ-scenarios-paper-2026-09.md` (lines 1–220: Source, Claims, Definitions);
  `programme-and-product-pages.md` (lines 1–460 and 621–840: Source, Claims, Definitions for pages 1–12, and
  the whole of Open questions); `ai-fluency-index-2026-02.md`, `independent-research-access-2026-08.md`,
  `work-at-anthropic-2025-12.md`, `econ-scenarios-explorer-2026-09.md`,
  `country-brief-india-2026-02.md`, `country-report-australia-2026-03.md`,
  `country-report-canada-2026-07.md` (Claims and Open-questions sections extracted section-by-section). Every
  quotation and every number in this map comes from a passage that was read in this session; nothing is
  quoted from a section that was not read.
- **Files read but not cited**, because the threads they bear on are carried by later publications:
  `clio-insights-2024-12.md` (T8's methods substrate, cited at second hand through the hub page's
  description), `anthropic-interviewer-2025-12.md`, `survey-81k-interviews-2026-03.md`,
  `survey-81k-interviews-2026-03-appendix.md`, `coding-agents-social-sciences-2026-05-appendix.md`,
  `claude-code-expertise-2026-06-appendix.md`. They are listed in the relevant thread's (a) section so the
  thread's publication list is complete.
- **Also read:** `README.md`; `team/SETUP.md` (§§2, 5, 10); `.claude/skills/room-protocol/SKILL.md`;
  `room/director-2026-09-16-session-1-2-kickoff.md`; `/mnt/memory/standards/terminology.md`,
  `register.md`, `criteria.md`, `file-ownership.md`; `/mnt/memory/research-journal/status/*`;
  `wiki/INDEX.md` in full; `data/ATLAS.md` §§How to use this atlas, Releases at a glance, Components, Which
  cuts exist at which grain, Cuts that do not exist, Conventions that reproduce published numbers, Thresholds
  and suppression, Traps (reading files; units and scales), Supplementary sources, Dated log;
  `room/steward-2026-09-16-question-batch-answers.md` (all ten answers).
- **Method.** (1) Read the corpus. (2) For each publication, extract the construct it introduces or re-uses
  and the finding it states with a number, from that wiki file's `Claims` and `Definitions (verbatim)`
  sections, keeping the page or figure reference. (3) Group constructs into threads by the rule in
  `## How to read this map`. (4) For each thread, take the open items from the wiki file's
  `Limitations (verbatim)` and `Open questions…(verbatim)` sections first, and only then from
  `What it did not test`, marking the latter **[inference]**. (5) Take the Institute's stated wants from
  `institute-agenda-2026-05`, `institute-launch-2026-03`, `economic-index-survey-2026-04-announcement` and
  `programme-and-product-pages`, using the agenda's own bullet ids (`ED-1`…`ED-12`, `TR-*`, `WILD-*`,
  `RD-*`, `Share 1`–`Share 3`) as those files define them. (6) For each open item, look up the relevant cut
  in `data/ATLAS.md` §Which cuts exist at which grain and §Cuts that do not exist, and the reproduction
  specification in §Conventions; where the atlas is silent, flag `steward?`.
- **What this map does not do.** It proposes no research question, names no candidate post and scores
  nothing; that is session 1.3's work (`team/SETUP.md` §5 rows 0.5–0.6). It contains no number that is not
  traceable to a `wiki/reports/` file with a page, figure, table, footnote or section reference. No data file
  was opened; every reach-of-data statement cites `data/ATLAS.md` or the steward's answer note. No
  `wiki/reports/` file was edited; three defects noticed while reading are reported in
  `room/lead-2026-09-16-threads-status.md`, not corrected here.
- **Counts.** 11 threads; 38 `wiki/reports/` files mapped, of which 36 are named in at least one thread's (a)
  list. The two exceptions are `institute-agenda-2026-05` and `institute-launch-2026-03`: they state no
  finding and carry no measure, so they are the sources for §(d) of every thread and for
  §"What the Institute wants that the corpus has not delivered" rather than members of any thread, and they
  are cited in both places throughout. 14 cross-thread tensions; 24 undelivered Institute and programme
  items; 8 mentor publications.
