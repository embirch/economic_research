# Pre-registration · Post 1 · Culture or cohort?

**Title.** Delegate or collaborate? Culture, cohort and development in how countries work with AI: evidence from Claude.
**Author.** Emily Birch. **Date written.** 15 September 2026, before any test involving power distance was run.

## What has already been seen (disclosure)
Steps 01–05 have been run: the collaboration shares by country in five waves; the exact replication of Anthropic's Figure 2.11 (slope −3.112, R² 0.394, N 111) and its repetition on later waves (slopes −3.13, −2.43, −1.49, −1.44); the merge of income, composition, language and culture data; and the newness ceiling (tenure gap 8.3 points of automation; 5th–95th spread 15.8 points in Aug 2025). No regression or correlation of power distance against the outcome has been run. A spot check printed three countries' full rows (India: PDI 77, residual +7.1; Denmark: PDI 18, residual −8.7; Singapore: PDI 74, residual −4.7); this is disclosed as a three-point glimpse.

## Research question
Once task mix is held constant, is the gap between countries that delegate to AI and countries that collaborate with it explained by the norms their users bring (culture), by how new their users are (cohort), or by how rich the country is (development)?

## Hypotheses and what counts against each
- **H1 culture.** Higher Hofstede power distance → higher task-mix-adjusted automation share, holding income, adoption, coding share, personal-use share and language group constant. *Against:* the power-distance coefficient is smaller than the minimum detectable effect (MDE), or its 95% interval includes zero.
- **H2 cohort.** The gap reflects the newness of users. *Against:* (a) no within-country association between automation and adoption across waves, and (b) the US automation share does not rise, relative to the comparator set, in the wave that brought a surge of first-time users. The ceiling alone cannot reject H2.
- **H3 development.** Income carries the effect. *Against:* power distance survives with income and adoption in the model.
The three are not mutually exclusive; results are reported as shares of the story, not a single winner.

## Sample
Countries with ≥200 conversations in the wave (Anthropic's rule), with a task-mix adjustment computable (Aug 2025: 111), a country-specific Hofstede power-distance score (61), and all controls present. Regional Hofstede scores (Arab countries, Africa East, Africa West) are NOT used in the primary. **Anomaly rule:** any country-wave with a Usage Index above 25 is excluded and named (Seychelles, Nov 2025, index 1,055). South Africa uses Hofstede's published "white sample" score (49), as his site does.

## Primary test (H1 vs H3)
OLS, August 2025 wave (the exact-replication wave):
  `auto_resid ~ z(hof_pdi) + log_gdp + aui + coding_share + personal_share + lang_group dummies`
where `auto_resid` is the task-mix-adjusted automation residual from Anthropic's released function, `z(hof_pdi)` is power distance standardised over the estimation sample, `aui` is the published Usage Index, `coding_share` is the Computer & Mathematical occupation share (Aug 2025), `personal_share` is the personal-use share of classified conversations (Nov 2025, the first wave with use case), and `lang_group` is the majority conversation language (≥60%, else "mixed"). HC3 robust standard errors.
**Support for H1:** coefficient on z(hof_pdi) > 0, 95% interval excludes 0, and coefficient ≥ MDE. **Against H1:** coefficient < MDE. **MDE:** the smallest coefficient detectable at 80% power, two-sided α = 0.05, from the fitted model's standard error: MDE = (1.96 + 0.84) × SE.
Coefficients on `log_gdp` and `aui` are reported with the same standard.

## Robustness (all reported, none primary)
A. Power distance extended with Hofstede's regional scores for the member countries he names (N ≈ 72).
B. GLOBE power-distance practices in place of Hofstede; GLOBE participative leadership (sign expected negative).
C. Individualism and uncertainty avoidance added; power distance must survive.
D. Outcome = directive share residual instead of automation residual.
E. Repeat on Nov 2025 and Feb 2026 waves (income merged as a country trait).
F. English-majority countries only (illustrative; N small).
G. Stanford human-agency "AI handles alone" share as a second-instrument outcome (N ≈ 57).
H. Leave-one-country-out: any country moving the coefficient by more than 25% is named.
I. Placebo: the same model on the share of unclassified collaboration; power distance should not predict it.
J. Variance-inflation factors reported; if VIF > 5 for power distance or income, the two-variable model is shown beside the full model.

## Within-country test (H2 vs H3)
Panel of the Aug 2025, Nov 2025, Feb 2026, Apr 2026 and May 2026 waves; country and wave fixed effects; `auto_resid ~ aui` within country; standard errors clustered by country; run with and without the two June 2026 waves (regime change). Predicted signs: cohort positive, development negative, culture near zero. Reported as suggestive given four to five waves.

## Natural experiment (H2)
Change in US `auto_resid` from Nov 2025 to Feb 2026 minus the mean change over the comparator set fixed here: Canada, United Kingdom, Australia, Ireland, New Zealand. Support for cohort: the US change exceeds the comparator mean by more than one comparator standard deviation.

## Extension (not a test of H1–H3)
June 2026 within-occupation-group automation by country: does power distance raise automation as much in learning-heavy groups (Educational Instruction; Life, Physical and Social Science) as in routine groups (Office and Administrative Support; Sales)?

## Deviations
Any deviation from this document is logged in `notes/lab-notebook.md` with the reason and the date.

## Addendum (set 15 September, afternoon, after the primary test and before this analysis was run): unbundling income
Question: which of the things that travel with income carries the relationship between income and task-mix-adjusted automation?
Candidates, all by country: (a) prompt sophistication, Anthropic's `human_education_years_mean` (Nov 2025); (b) task complexity, `human_only_time_mean` (Nov 2025, hours); (c) work share and coursework share of classified conversations (Nov 2025); (d) English share of conversations (Stanford `lang:english_ratio`); (e) internet users per 100 people (World Bank, latest year); (f) tertiary enrolment, gross ratio (World Bank SE.TER.ENRR, latest year); (g) AI autonomy, `ai_autonomy_mean` (Nov 2025), reported but not a mechanism candidate.
Model: the primary specification (Aug 2025 outcome, 61-country Hofstede sample, and the wider 111-country sample without power distance) with each candidate added one at a time, then all together; standardised coefficients; HC3 errors. Read-out rule: a candidate "carries" the income effect if adding it cuts the income coefficient by at least half AND the candidate's own coefficient has an interval excluding zero. If income keeps at least half its coefficient with all candidates present, the bundle resists unbundling and the post says so. Exploratory: this analysis was specified after the primary result was known.

## Addendum 3 (written 15 September 2026, before any state-level model was run): the within-country test

**Question.** Does the income and education gradient in delegation reappear across US states, where language, product, pricing, classifier and national culture are held constant?

**Data.** August 2025 release, `geography = state_us` (50 states and DC; Anthropic applies a 100-conversation threshold in enrichment). Outcome: task-mix-adjusted automation share, computed with Anthropic's released `collaboration_task_regression(df, geography="state_us")`, exactly as for countries. Income: log of state GDP per working-age adult from the two state files Anthropic released. Education: share of adults 25 and over with a bachelor's degree or higher (ACS 2023 1-year, table B15003). Access: share of households with a broadband subscription of any type (ACS 2023 1-year, B28002). Adoption: the state Usage Index from the file. Coding share: computer and mathematical occupations' share of the state's conversations (SOC facet). No language or personal-use control exists at state level in this wave.

**Models** (HC3): (1) education alone; (2) education + log income; (3) full: education + log income + broadband + Usage Index + coding share. Standardised predictors. Report the MDE for the education coefficient in (3).

**Decision rule.** The gradient *reappears* if the education coefficient is negative with a 95% interval excluding zero in model (1) and in model (3). It *does not reappear* if the model (3) coefficient lies inside its MDE. Anything else is reported as inconclusive. Anthropic's report states that the Usage Index and automation are "not significant across US states"; that statement is checked first with their own function and reported whatever it shows.

**Robustness, fixed now:** drop DC (index 3.8, government-heavy); drop Utah (flagged by Anthropic for possible coordinated abuse); directive share as outcome; unadjusted automation share as outcome; leave-one-out on the education coefficient.

**Interpretation, fixed now.** Reappears → the cross-country gradient is a human-capital gradient, and neither national culture nor classifier language bias can be its source. Does not reappear → the cross-country gradient reflects who gains access in poorer countries (selection), not how educated users behave, and the post says so.
