# Appendix: Coding Agents in the Social Sciences (2026-05-27)

Slug: `coding-agents-social-sciences-2026-05-appendix`. Wiki file written 2026-09-16 from the PDF.

## Source

- **Title.** "Appendix: Coding Agents in the Social Sciences" (title page, p.1; identical to the PDF's `Title` metadata field).
- **Authors.** "Thomas Lyttelton (MIT), Maxim Massenkoff, and Nathan Wilmers (MIT)" (p.1, under the heading "Authors"). Massenkoff is the only author with no affiliation in parentheses — *wiki author's reading:* the un-parenthesised author is the Anthropic-side author, on a document carrying the Anthropic wordmark; the appendix itself never states an affiliation for him. **This is the intended mentor's document**, which makes it a priority entry for `programme/THREADS.md`.
- **Date.** "Published May 27, 2026" (p.1).
- **URL.** https://cdn.sanity.io/files/4zrzovbb/website/403415e54964751190003985896630e56829e797.pdf — a Sanity CDN asset; there is no HTML version of the appendix and the PDF contains no hyperlinks (checked: zero URI annotations).
- **Document type.** Methods-and-robustness appendix to a research post. It is not self-contained: it refers outward to "Figure 5" and "Figure 5b" of the main text, and its Table A1 names a survey ("the WFL Baseline Survey") that it never expands or defines.
- **Main text (cross-reference, not summarised here).** Slug `coding-agents-social-sciences-2026-05`, "Coding agents in the social sciences", 2026-05-27, https://www.anthropic.com/research/coding-agents-social-sciences (see `wiki/INDEX.md`; that thread owns the main-text entry). Nothing below is quoted from the main text; where the appendix defers to it, the deferral is recorded rather than resolved.
- **Length.** 6 pages: p.1 title page, pp.2–6 content. Approximately **1,200 words** of extractable text. Three exhibits — **Table A1** (p.3), **Figure A1** (p.5) and **Table A2** (p.6) — plus the p.1 wordmark are embedded as **raster images with no text layer**; their contents were read from 200 dpi and 400 dpi renders of those pages (see §Verification). Produced by the "Skia/PDF m150 Google Docs Renderer".
- **The data it rests on.** One purpose-built survey — "The survey was fielded from February 20 to March 24, 2026" (p.2) — with an analytic sample of 1,260 respondents, plus a smaller pilot run "in early February" (p.5). No Economic Index release, no Claude usage logs, no administrative data. *Wiki author's note:* this document therefore sits beside the Index rather than on it; the survey it documents is the baseline wave of a **randomised experiment providing access to Claude Max accounts** (p.2) / "an experiment on Claude Code access and research productivity" (p.5), which has not, as of today, produced a published results paper in `wiki/INDEX.md`.

## Claims

Numbered; each carries its page and exhibit reference, the number exactly as published, and the comparison it rests on. Values from Table A1, Figure A1 and Table A2 were read from page renders because those exhibits carry no text layer.

**Sample construction**

1. **p.2.** "The survey was fielded from February 20 to March 24, 2026." A 33-day field window; no claim of stratification or quota within it.
2. **p.2.** "We directly emailed **44,700** academics we identified in these ways." Comparison: none offered — the appendix never sets this against the number who opened, started or completed, so no response rate can be formed from the document.
3. **p.2.** "After applying the screener and limiting to respondents who completed the full survey, the analytic sample consists of **1,260** respondents". Comparison: the analytic sample against the invited frame is *not* made; the sample is only described (Table A1), never compared with the population of R1 social scientists it was drawn from.
4. **Table A1, p.3 (career stage).** PhD Student **384 (31%)**; Postdoc **87 (7%)**; Assistant Professor **311 (25%)**; Associate Professor **235 (19%)**; Full Professor **243 (19%)**; Total **1,260 (100)**. Comparison: internal composition only. (*Wiki author's arithmetic:* the counts sum to 1,260; the shares sum to 101 through rounding.)
5. **Table A1, p.3 (discipline).** Economics **209 (17%)**; Political Science **216 (17%)**; Sociology **262 (21%)**; Psychology **172 (14%)**; Management Sciences **202 (16%)**; Public Health **84 (7%)**; Education **45 (4%)**; Communication **36 (3%)**; Other **34 (3%)**; Total **1,260 (100)**. (*Wiki author's arithmetic:* counts sum to 1,260; shares sum to 102 through rounding. Nine rows = "eight substantive discipline buckets plus a residual 'Other' category", matching the "nine categories" of discipline fixed effects on p.4.)
6. **p.3.** "The raw responses contain **318** unique values, many of which are idiosyncratic subfield descriptions." Comparison: 318 free-text values against the nine analytic buckets — i.e. the compression the classification performs.
7. **p.3.** "**28%** of respondents are from the top 25 institutions" (Nature Index 2025 Leading Institutions ranking, list of 25 named on pp.3–4). Comparison: respondents at top-25 institutions against all respondents; no benchmark for what share of the invited frame or of US/Canadian social scientists sits at those institutions.

**The adjusted specification and its results**

8. **p.4.** The Figure 5b estimates come from OLS of an output measure on a coding-agent-user indicator with fixed effects for career stage (five categories), discipline (nine categories) and survey week, with heteroskedasticity-robust standard errors; "The coefficient beta is the adjusted difference in mean output between coding agent users and non-users, conditional on career stage, discipline, and survey timing." Comparison: coding agent users against non-users within cells of career stage × discipline × survey week. The estimates themselves are in the main text's Figure 5, not in the appendix.
9. **p.4.** "We fit this model with OLS, and then divide by the control group's mean of each outcome to back out percent differences." The published percentages are therefore ratios of an OLS coefficient to the non-user mean, not log-point or Poisson coefficients.
10. **p.4.** "A Poisson model specification gives similar results." Asserted robustness; no coefficients, no table, no definition of "similar" anywhere in the appendix.
11. **p.4.** Raw (unadjusted) differences "show that agent users post more working papers and submit more grants, but actually submit fewer papers to journals". Comparison: unadjusted means of agent users against non-users, across six self-reported output measures.
12. **p.4.** "as Figure 5 shows, this lower rate of submitting to journals reflects the distribution of coding agent use across disciplines and career stages". Comparison: the unadjusted journal-submission gap against the adjusted one — the appendix's explanation for the sign flip, resting entirely on a main-text figure.
13. **Figure A1, p.5 (unadjusted gaps, "Coding agent user — non-user (% of non-user mean)").** Empirical projects started **+1%**; Grant proposals submitted **+22%\***; Working papers posted **+69%\*\***; Conference submissions **+1%**; Journal submissions **−19%\*\***; Journal resubmissions **−26%\*\*\***. Comparison: agent users against non-users with no covariates. Whiskers are "95% confidence intervals calculated using the robust standard errors scaled by the outcome mean"; the caption's legend reads "\* p < 0.05, \*\* p < 0.01" — *wiki author's note:* the three-star marker on journal resubmissions is not defined in that legend, and the figure reports no sample sizes.

**The pilot-versus-main selection check**

14. **p.6 and Table A2 (AI adoption).** AI use: main sample **84.5%** (N = **446**), pilot sample **87.3%** (N = **102**), difference **+2.7pp** (unstarred). Comparison: the main sample narrowed to sociology, political science and management and excluding full professors, against the pilot sample, which was recruited without mention of the experiment. *Wiki author's arithmetic:* the Difference column runs **pilot minus main** throughout, and is the only column in the document whose sign convention must be inferred rather than read.
15. **Table A2 (beliefs, 1–10 scale).** Productivity: **7.56** (N = 446) vs **7.10** (N = 102), difference **−0.46\***. Field impact: **5.68** (N = 446) vs **4.75** (N = 102), difference **−0.93\*\*\***. Comparison: as claim 14. Table A2 carries **no significance legend at all**.
16. **Table A2 (AI use cases among AI users; N = 377 main, 89 pilot).** Code **84.1%** vs **76.4%** (**−7.7pp**); Edit prose **74.8%** vs **68.5%** (**−6.3pp**); Method advice **69.2%** vs **64.0%** (**−5.2pp**); Lit review **66.0%** vs **40.4%** (**−25.6pp\*\*\***); Generate ideas **41.1%** vs **36.0%** (**−5.2pp**); Draft prose **35.8%** vs **27.0%** (**−8.8pp**); N use cases (mean) **3.71** vs **3.12** (**−0.59\*\***). Comparison: as claim 14, conditional on AI use ("Use case shares are conditional on AI use", Notes, p.6).
17. **p.6.** "There is little difference in overall rates of AI use across the two samples, but the full sample uses AI for more research tasks and is more optimistic about its impact." Comparison: claims 14–16 taken together; "little difference" rests on an unstarred 2.7pp gap with a pilot of 102 respondents, and no minimum detectable effect is stated.
18. **p.6.** "the key gaps persist: coding and editing are the most common uses in both samples and drafting prose is rare in both". Comparison: the *ranking* of use cases within each sample, rather than their levels — the appendix's central defence of the main text's pattern claims.
19. **p.6.** "On the 1 to 10 slider, the full sample is one point more optimistic about field impacts and a half point more optimistic about paper productivity effects. But the gap between paper productivity and field impact beliefs persist." Comparison: the within-sample gap between the two belief items (main 7.56 − 5.68 = 1.88; pilot 7.10 − 4.75 = 2.35, *wiki author's arithmetic*) across the two samples — i.e. a difference-in-differences read off levels, without a standard error for the difference of differences.
20. **p.6.** "Overall, the full sample is composed of more pro-AI respondents, but the key gradients that we can measure are similar in the pilot sample drawn without AI-related recruitment materials." The appendix's summary verdict on selection; the hedge "that we can measure" is the authors', and the productivity gradient of Figure 5 is not among the gradients tested, because the pilot "is missing our detailed coding agent question" (p.5).

## Definitions (verbatim)

Every construct, rule, threshold and specification the appendix defines, quoted in full, with the page reference. No paraphrase in this section.

**Recruitment — the five channels** (p.2):
> "We identified respondents in five ways. First, we scraped faculty and student contact information from sociology, political science, management, economics, psychology, education, and public health department websites at R1 and major Canadian research universities. Second, we used OpenAlex, an open source repository of academic research, to identify research-active social scientists based on publication and working paper topics. We restricted to researchers who had published within the last year, in hopes of identifying active, working researchers. We also used academic conference programs for the same purpose. We directly emailed 44,700 academics we identified in these ways. Additionally, we asked directors of graduate studies in sociology, political science, and economics to distribute invitations to their graduate students, and we distributed invitations via the message boards and email lists of scholarly communities such as the Academy of Management and the American Sociological Association."

**Eligibility, the screener and the incentives** (p.2):
> "Throughout these recruitment efforts, we targeted researchers based in the US or Canada actively doing quantitative, empirical research. In an opening screener for the survey, we further restricted participants to those who work with quantitative empirical data, and, among doctoral students, those who have finished at least 2 years of their training and who plan to enter academia. Invitations were sent by email. Respondents were informed that the study concerns academic workflows and that participants would be eligible for a randomized experiment providing access to Claude Max accounts. They were also offered a $10 gift card for completing the survey."

**The analytic sample** (p.2):
> "After applying the screener and limiting to respondents who completed the full survey, the analytic sample consists of 1,260 respondents, described by discipline and career stage in Table A1."

**Table A1 title** (p.3):
> "Table A1: Sample of respondents to the WFL Baseline Survey, by career stage and discipline"

**Discipline buckets** (p.3):
> "Respondents provided their discipline via free text entry. The raw responses contain 318 unique values, many of which are idiosyncratic subfield descriptions. We consolidate these into eight substantive discipline buckets plus a residual "Other" category, using a mix of Claude classification and hand coding. Economics includes its applied subfields (health economics, development economics) and political economy. Political science includes public administration and law. Sociology includes urban studies, geography and social work. Management sciences includes all applied disciplines typically housed in business schools (including finance, accounting, and organizational behavior). Public health includes epidemiology. “Other” is a residual category, including the small number of respondents doing quantitative research in anthropology, archaeology, history and linguistics."

**Gender** (p.3):
> "We infer gender from each respondent's self-reported first name using the gender_guesser Python library. We collapse "male" and "mostly_male" into a single "typically male name" category, and "female" and "mostly_female" into "typically female name." Unknown or androgynous names are left out of the analysis."

**Institution rank** (pp.3–4):
> "We classify respondents' institutions as top 25 in the US and Canada using the Nature Index 2025 Leading Institutions ranking. 28% of respondents are from the top 25 institutions, which include Harvard University, Stanford University, MIT, National Institutes of Health, University of Michigan, Yale University, University of Pennsylvania, University of Toronto, UCLA, UC Berkeley, Johns Hopkins University, University of Washington, UC San Diego, Columbia University, Cornell University, Northwestern University, University of Chicago, Washington University in St. Louis, Princeton University, Caltech, UC San Francisco, UT Austin, University of Wisconsin-Madison, Duke University, and University of Minnesota."

**The regression specification** (p.4):
> "The adjusted output comparisons in Figure 5b use OLS regressions of the form:"

> "𝑂𝑢𝑡𝑝𝑢𝑡𝑖 = β × 𝐶𝑜𝑑𝑖𝑛𝑔𝐴𝑔𝑒𝑛𝑡𝑈𝑠𝑒𝑟𝑖 + γ × 𝑋𝑖 + ϵ𝑖"

*(The equation is set in mathematical-italic characters; the trailing "𝑖" on each term is the observation subscript. In plain type: Output_i = β × CodingAgentUser_i + γ × X_i + ε_i.)*

> "where 𝑋𝑖 includes fixed effects for career stage (five categories: PhD student, postdoc, assistant professor, associate professor, full professor), discipline bucket (nine categories), and the calendar week the respondent completed the survey. Standard errors are heteroskedasticity-robust. The coefficient beta is the adjusted difference in mean output between coding agent users and non-users, conditional on career stage, discipline, and survey timing. We fit this model with OLS, and then divide by the control group's mean of each outcome to back out percent differences. A Poisson model specification gives similar results."

**Why the raw differences are shown separately** (p.4):
> "The raw differences in output among respondents are more difficult to interpret, as they reflect differences between disciplines in practices like posting working papers, timing of conference submissions, and expected number of journal publications per year. These unadjusted differences are shown in Figure A1 and show that agent users post more working papers and submit more grants, but actually submit fewer papers to journals. However, as Figure 5 shows, this lower rate of submitting to journals reflects the distribution of coding agent use across disciplines and career stages."

**Figure A1 caption — outcome definitions, uncertainty and the star legend** (p.5):
> "Figure A1: Unadjusted research productivity differences between coding agent users and other researchers. Outcomes are self-reported by respondents. Working papers posted, journal submissions and journal resubmissions are mutually exclusive categories. See Figure 5 for estimates adjusted by discipline, career stage and survey week. Whiskers show 95% confidence intervals calculated using the robust standard errors scaled by the outcome mean. * p < 0.05, ** p < 0.01."

**Figure A1 axis and panel labels** (p.5, read from the page render):
> "Coding agent user — non-user (% of non-user mean)"

> "Agent users produce fewer" / "Agent users produce more"

**The pilot sample** (p.5):
> "How much is selection into the survey biasing results? The main sample we use here suffers from its function as recruitment for an experiment on Claude Code access and research productivity. To assess how important this distortion is, we compare results in this sample to those from a pilot we ran in early February. This pilot was much smaller, explicitly excluded full professors, and only targeted sociologists, political scientists and management scholars. In the main sample, we expanded disciplines and career stage to draw in a broader range of respondents. The pilot survey also had some different questions on it, as we piloted and improved the survey. Crucially, it is missing our detailed coding agent question."

**Why the pilot identifies selection** (pp.5–6):
> "But the pilot data are useful because we did not advertise the subsequent experiment in recruitment for it. Instead we simply described a study on changes in research workflows."

> "This means we can use the pilot data to assess whether our results in the main sample are driven by selection into the experiment."

**The comparability restriction for Table A2** (p.6):
> "Table A2 shows results comparing the pilot sample to the full survey. To make the recruitment logic of the two samples comparable, we narrow the main survey sample to sociologists, political scientists and management scholars and exclude full professors."

**Table A2 title and Notes** (p.6):
> "Table A2: Comparison of main and pilot samples"

> "Notes: The main sample is restricted to include only sociology, political science, and management and exclude full professors, for clearer comparison to the narrow pilot sample. Use case shares are conditional on AI use."

**Table A2 row and column headings** (p.6, read from the page render): the columns are "Main sample" (Mean, N), "Pilot sample" (Mean, N) and "Difference"; the panels are "AI adoption" (row "AI use"), "Beliefs about AI (1-10 scale)" (rows "Productivity", "Field impact") and "AI use cases (among AI users)" (rows "Code", "Edit prose", "Method advice", "Lit review", "Generate ideas", "Draft prose", "N use cases (mean)").

**The belief scale, as described in the body** (p.6):
> "On the 1 to 10 slider, the full sample is one point more optimistic about field impacts and a half point more optimistic about paper productivity effects."

*Constructs used but never defined in this document (recorded for the ledger, and flagged again in §What it did not test):* "coding agent user" (the regressor; the appendix says only that the pilot "is missing our detailed coding agent question" and never gives that question's wording, options or threshold); "AI use" in Table A2, and how it differs from coding agent use; "WFL"; the six output measures' question wording and reference period; the wording of the two belief items; and which of the nine disciplines the five Figure-5b career stages interact with, if any.

## Data and methods

In the wiki author's words, with page references.

- **Design.** A cross-sectional online survey of North American quantitative social scientists, fielded 20 February – 24 March 2026 (p.2), serving simultaneously as the baseline instrument and as recruitment for a randomised trial of Claude Max access (p.2; described on p.5 as "an experiment on Claude Code access and research productivity"). All estimates in the appendix are observational comparisons between self-selected coding-agent users and non-users; no randomisation is used anywhere in this document.
- **Frame and recruitment.** Five channels (p.2): scraped department websites at R1 and major Canadian universities across seven named fields; OpenAlex-identified researchers publishing within the last year; conference programmes; directors of graduate studies in three fields; and scholarly-society mailing lists and message boards. 44,700 academics were emailed directly; the list-based channels have no denominator.
- **Eligibility.** US- or Canada-based, active in quantitative empirical research; screener requires work with quantitative empirical data; doctoral students must have completed at least two years and plan to enter academia (p.2).
- **Incentives and disclosure.** Respondents were told the study concerns academic workflows and that participation made them eligible for a randomised experiment giving access to Claude Max accounts; a $10 gift card was offered for completion (p.2). This disclosure is the source of the selection concern the appendix then tests.
- **Analytic sample.** 1,260 completed, screened responses (p.2), composition in Table A1 (p.3). For Table A2 the main sample is narrowed to sociology, political science and management and full professors are dropped, leaving N = 446 (N = 377 among AI users) against a pilot of 102 (89 AI users).
- **Derived variables.** (i) *Discipline bucket* — 318 free-text responses compressed into eight substantive buckets plus "Other", "using a mix of Claude classification and hand coding" (p.3), with the membership rules for each bucket spelled out. (ii) *Gender* — inferred from first name with the `gender_guesser` Python library, four categories collapsed into two, unknown and androgynous names dropped (p.3); no result in this appendix uses it. (iii) *Top-25 institution* — Nature Index 2025 Leading Institutions, 28% of respondents (pp.3–4); no result in this appendix uses it either. (iv) *Coding agent user* — used as the sole regressor of interest but never defined here.
- **Outcomes.** Six self-reported research-output counts (Figure A1, p.5): empirical projects started, grant proposals submitted, working papers posted, conference submissions, journal submissions, journal resubmissions. The caption states that working papers posted, journal submissions and journal resubmissions are mutually exclusive categories. No reference period is given in the appendix.
- **Estimation.** OLS of each outcome on the coding-agent-user indicator with career-stage (5), discipline (9) and survey-week fixed effects, heteroskedasticity-robust standard errors; coefficients divided by the control-group mean to express percent differences (p.4). Poisson is said to give similar results, without display. Figure A1 reports the same comparisons without covariates, with 95% intervals formed from "the robust standard errors scaled by the outcome mean".
- **The selection check.** A pilot fielded in early February, recruited *without* mentioning the experiment, restricted to sociology, political science and management and excluding full professors (p.5). Because the pilot lacks the detailed coding-agent question, the check compares **AI use, beliefs and use-case shares** across the two samples (Table A2), not the productivity estimates themselves. *Wiki author's observation:* the Difference column is pilot minus main (verified against all ten rows); the convention is stated nowhere in the document.
- **Thresholds and conventions.** Two years of doctoral training (screener); top 25 institutions (Nature Index); significance stars * p < 0.05 and ** p < 0.01 in Figure A1, with a *** marker used but undefined; Table A2 uses stars with no legend. No privacy thresholds, no cell-suppression rules and no minimum-N rule appear — the unit is a consenting survey respondent, not a Claude conversation.
- **Released data and code.** None named. The appendix does not link a replication package, a questionnaire, a pre-registration or a data deposit, and contains no URLs at all.

## Limitations (verbatim)

Every limitation the authors state, quoted with its page reference.

p.4 — the unadjusted comparison is hard to interpret:
> "The raw differences in output among respondents are more difficult to interpret, as they reflect differences between disciplines in practices like posting working papers, timing of conference submissions, and expected number of journal publications per year."

p.5 — the sample is contaminated by its recruitment purpose:
> "How much is selection into the survey biasing results? The main sample we use here suffers from its function as recruitment for an experiment on Claude Code access and research productivity."

p.5 — the comparison sample is small and differently scoped:
> "This pilot was much smaller, explicitly excluded full professors, and only targeted sociologists, political scientists and management scholars."

p.5 — the two instruments differ, and the key question is missing from one:
> "The pilot survey also had some different questions on it, as we piloted and improved the survey. Crucially, it is missing our detailed coding agent question."

p.6 — the residual selection the check leaves in place:
> "Overall, the full sample is composed of more pro-AI respondents, but the key gradients that we can measure are similar in the pilot sample drawn without AI-related recruitment materials."

p.6 — the direction and size of the belief gap between samples:
> "There is little difference in overall rates of AI use across the two samples, but the full sample uses AI for more research tasks and is more optimistic about its impact."

p.5 (Figure A1 caption) — the outcomes are not administrative records:
> "Outcomes are self-reported by respondents."

p.3 — the discipline variable is noisy free text, compressed by a mix of machine and hand coding:
> "The raw responses contain 318 unique values, many of which are idiosyncratic subfield descriptions. We consolidate these into eight substantive discipline buckets plus a residual "Other" category, using a mix of Claude classification and hand coding."

p.3 — respondents are dropped from the gender analysis:
> "Unknown or androgynous names are left out of the analysis."

p.2 — the population is restricted by geography and method:
> "Throughout these recruitment efforts, we targeted researchers based in the US or Canada actively doing quantitative, empirical research."

## Open questions, conjectures and promised follow-ups (verbatim)

The appendix poses one explicit research question and makes several hedged or undisplayed claims. All of them, quoted.

p.5 — the question the section exists to answer:
> "How much is selection into the survey biasing results?"

pp.5–6 — the identifying argument offered for the answer:
> "But the pilot data are useful because we did not advertise the subsequent experiment in recruitment for it. Instead we simply described a study on changes in research workflows."

> "This means we can use the pilot data to assess whether our results in the main sample are driven by selection into the experiment."

p.6 — the hedge that leaves the question partly open ("that we can measure"):
> "Overall, the full sample is composed of more pro-AI respondents, but the key gradients that we can measure are similar in the pilot sample drawn without AI-related recruitment materials."

p.4 — a robustness result asserted but not shown:
> "A Poisson model specification gives similar results."

p.2 — the stated purpose behind a recruitment rule, i.e. an assumption about who the frame captures:
> "We restricted to researchers who had published within the last year, in hopes of identifying active, working researchers."

p.2 — the promised follow-up study this survey recruits for:
> "Respondents were informed that the study concerns academic workflows and that participants would be eligible for a randomized experiment providing access to Claude Max accounts."

p.5 — the same experiment, named again:
> "The main sample we use here suffers from its function as recruitment for an experiment on Claude Code access and research productivity."

p.6 — the conjecture that the mechanism behind the raw journal-submission gap is composition, referred to a main-text figure:
> "However, as Figure 5 shows, this lower rate of submitting to journals reflects the distribution of coding agent use across disciplines and career stages."

p.6 — the belief gap the authors flag as surviving the selection check, without offering an explanation for it:
> "But the gap between paper productivity and field impact beliefs persist."

## What it did not test

**This section is the wiki author's inference, not the source's words.** It lists adjacent questions the appendix had the material to answer, robustness checks it could have run with the data in hand, and constructs it used without validating. *(main text)* marks items that may be handled in `wiki/reports/coding-agents-social-sciences-2026-05.md`; that must be checked before any of them is treated as open.

*Non-response and the frame — the appendix builds a frame and never uses it:*
1. **No response rate and no funnel.** 44,700 direct emails plus list-serv and society distribution produce 1,260 completions, but the appendix reports no starts, no screen-outs, no partials and no channel-level counts. The share of the analytic sample arriving through each of the five channels is knowable and unreported, though channel is exactly what determines how much the Claude Max offer could have distorted entry.
2. **No comparison of respondents to the frame.** OpenAlex was used to build the invitation list, so publication records for invitees exist; the discipline, seniority and productivity of respondents are never benchmarked against those of non-respondents.
3. **No completer-versus-abandoner comparison**, although "limiting to respondents who completed the full survey" is an explicit filter.
4. **No early-versus-late respondent check.** Survey week enters as a fixed effect, which absorbs the drift; the standard cheap proxy for non-response bias — do estimates move across the 33-day window? — is never run.
5. **No weighting.** Sociology at 21% and economics at 17% of respondents almost certainly do not match their shares of North American quantitative social science; no reweighted estimate is shown.

*The regressor of interest is never defined or characterised:*
6. **"Coding agent user" has no definition here** — no question wording, no product list, no frequency threshold, no reference period — while the entire appendix exists to document the specification in which it is the sole regressor *(main text)*.
7. **No balance table.** The appendix conditions on career stage, discipline and week but never shows how users and non-users differ on those or on the two covariates it does construct (gender, top-25 institution).
8. **Neither constructed covariate is used.** Gender via `gender_guesser` and the Nature-Index top-25 flag are defined in detail and then appear in no estimate in this document; adding them as controls, or reporting heterogeneity by them, was a one-line change *(main text)*.
9. **`gender_guesser` is not validated** and the number of names dropped as unknown or androgynous is not reported, so the analytic sample for any gender cut is unknown.
10. **The discipline classifier is not validated.** "A mix of Claude classification and hand coding" is reported with no agreement rate between machine and human, no audit sample, and no sensitivity of the estimates to the bucketing (nine buckets versus, say, the raw 318 strings or a coarser three-field split).
11. **The Nature Index is a natural-science-weighted ranking** applied to social scientists; no alternative (QS/THE social science, NRC, departmental placement rankings) is checked.

*Inference and robustness the appendix could have shown and did not:*
12. **Poisson "gives similar results" is undisplayed.** No coefficients, no standard errors, no definition of similar. A second column in Figure A1 would have settled it.
13. **The percent conversion is not treated as a ratio.** Coefficients are divided by the control mean and intervals are "robust standard errors scaled by the outcome mean", so the sampling variation of the denominator is ignored; no delta-method or bootstrap interval is offered.
14. **No multiple-hypothesis adjustment** across six outcomes in Figure A1 and ten rows in Table A2, and no pre-registration is cited.
15. **Star legends are incomplete or absent.** Figure A1 defines * and ** but prints ***; Table A2 prints *, ** and *** with no legend. No p-values or N are shown in Figure A1.
16. **No clustering discussion.** Standard errors are robust only; the natural clusters (institution, department, discipline) are constructed in the data and never used, even as a robustness row.
17. **No MDE for the null results.** "Little difference in overall rates of AI use" rests on an unstarred 2.7pp gap with 102 pilot respondents; the claim of similarity is a failure to reject, and the appendix never says what gap it could have detected.
18. **The difference-in-differences in beliefs is eyeballed.** "The gap between paper productivity and field impact beliefs persist" compares 1.88 against 2.35 points with no standard error for the difference of differences.

*The selection check does not test the estimate it is defending:*
19. **The pilot check compares AI use, beliefs and use-case shares — never the productivity gaps.** Because the pilot lacks the coding-agent question, the appendix cannot and does not re-estimate Figure 5 out of the selected sample; the defence is that correlates of the estimate look similar, not that the estimate does. A weaker proxy — e.g. splitting the main sample by how AI-salient the respondent's recruitment channel was, or by whether they opted into the experiment — was available and is not run.
20. **"AI use" and "coding agent use" are used interchangeably across the two halves of the document.** Table A2 measures the first; Figure A1 and Figure 5b measure the second; whether the selection that matters operates on the same margin is assumed, not shown.
21. **No falsification criterion is stated.** The section asks how much selection biases results but never says what pattern in Table A2 would have counted as evidence that it does.

*Design questions left untouched:*
22. **No time ordering.** Agent use and output are measured in the same cross-section, with no pre-period output measure and no "when did you start" question reported, so reverse causality (productive researchers adopt agents) is untested. The appendix's own framing — that the randomised experiment is still to come — concedes this implicitly but never states it as a limitation.
23. **Self-reported counts are never validated** against an external record, although the OpenAlex data used for recruitment could have been linked to check working-paper and publication counts for at least part of the sample.
24. **No heterogeneity at all.** Career stage and discipline enter only as fixed effects; whether the +69% working-paper gap is concentrated among PhD students or full professors, economists or sociologists, is not reported here *(main text)*.
25. **The mutual exclusivity of the output categories is asserted** in the caption but its consequence is unexamined: a researcher shifting effort from journal submissions to working papers would produce exactly the observed pattern of +69% and −19%, and the appendix does not test composition-versus-volume.

## Verification

- **URL fetched, 2026-09-16:** https://cdn.sanity.io/files/4zrzovbb/website/403415e54964751190003985896630e56829e797.pdf — HTTP 200, `application/pdf`, 510,411 bytes, 6 pages, PDF 1.4, producer "Skia/PDF m150 Google Docs Renderer", document `Title` "Appendix: Coding Agents in the Social Sciences". Saved to `/tmp/cass_appendix.pdf`.
- **How it was read.** Full text extracted with `pdftotext -layout` (1,205 words, saved to `/tmp/cass_appendix.txt`) and read in full. Because Table A1 (p.3), Figure A1 (p.5) and Table A2 (p.6) are embedded raster images with no text layer — confirmed with `pdfimages -list`, which shows images on pages 1, 3, 5 and 6 — those three exhibits were read from page renders produced with `pdftoppm` at 200 dpi, and Figure A1 was re-read from a 400 dpi crop to confirm the star markers on each estimate. Every number attributed to Table A1, Figure A1 or Table A2 in §Claims comes from those renders.
- **Quotation check.** All 27 block quotations were checked against the text layer: the 24 that come from body text were matched by script against the `pdftotext` extraction (ignoring line breaks, hyphenation and quote-mark style) — 24 of 24 matched, 0 missing. The three that come from the image-only exhibits (the Figure A1 axis label, the "Agent users produce fewer/more" panel labels, and — for the caption — none, since the Figure A1 caption is body text) were transcribed from the 400 dpi render and re-read twice. The regression equation is reproduced as extracted, in the mathematical-italic characters the PDF uses, with a plain-type rendering supplied outside the quotation.
- **Internal arithmetic checks (wiki author's, not the source's).** Table A1 counts sum to 1,260 in both panels (shares sum to 101 and 102 respectively, consistent with rounding to whole numbers). The Table A2 Difference column equals pilot mean minus main mean in all ten rows to within rounding (e.g. 87.3 − 84.5 = 2.8 against a published +2.7pp, 7.10 − 7.56 = −0.46, 76.4 − 84.1 = −7.7). These checks are recorded because the sign convention is not stated in the document.
- **Could not be fetched or resolved.** Nothing failed to download. Three things cannot be resolved from this document and are not guessed at: the expansion of "WFL" in the Table A1 title; the wording of the "detailed coding agent question"; and the contents of "Figure 5" and "Figure 5b", which live in the main text.
- **Deliberately not fetched in this thread.** The main post (https://www.anthropic.com/research/coding-agents-social-sciences), which is another thread's slug. Nothing above is quoted from it; the cross-reference in §Source is taken from `wiki/INDEX.md`.
