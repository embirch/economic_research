# Source profile: UK DSIT Public Engagement Survey 2025/2026 — outstanding checks closed

Data steward, 1 October 2026. ID `UK_DSIT_USE`; sample family `UK_DSIT_PES_2025_2026`.
Builds on the coordinator's audit note
[`../../landscape-v1/coordination/UK-DSIT.md`](../../landscape-v1/coordination/UK-DSIT.md)
and its extractor `check_dsit.py`, which are read-only inputs here.

## Prior extraction reused and re-verified, not redone

The coordinator's workbook vintage was re-downloaded independently today and is
**byte-identical**: 325,288 bytes, SHA-256
`a34ed705b6f8c2966d82586917befaae975fee8f61206ef3a2d679cc95c4610a`. Running the
coordinator's `check_dsit.py` against this download reproduces the published `Table_E5`
cells exactly (TOTAL 58.9; Male 63.2 / unweighted base 13,902 / weighted base 14,428;
Female 55.5 / 15,953 / 15,343; “Identify in another way” 49.2 / 99 / 141; “Prefer not to
say” 45.0 / 671 / 694). No new extraction script was written.

## Outstanding questions from the coordinator note — now answered

### 1. Design, weighting and precision

From the published **technical report** (GOV.UK, 16 July 2026):

- Design: Address Based Online Sampling (“push-to-web”), stratified random sample of
  **106,612 addresses**, with sampling probability varied across three age-profile strata
  to offset expected response differences; respondents answer **online or on paper**.
- Weighting: three-step process, finishing with Random Iterative Method (raking)
  calibration to ONS Labour Force Survey and mid-year population estimates on
  **(1) gender by age**, education by age, ethnic group, tenure, **ITL2 area by age and
  gender**, employment status by age and more. The report explicitly warns that raking
  matches margins only and does not guarantee correction of bias in relationships
  between variables — relevant to any gender comparison.
- Precision: published data tables were produced in R with the `survey` package, with
  **95% confidence intervals using a logit method**, and a separate weight set for
  online-only questions. The **estimated design effect from weighting is 1.67**.
- Mode effects: a single set of weights for mixed-mode questions, a separate set for
  web-only questions.

**Where those intervals are published is unresolved.** The technical report (sections 7.5
to 8.2) is explicit that the published data tables were produced in R with the `survey`
package at the 95% level by a logit method, so intervals were computed. They are not in
the products inspected here:

- `Table_E5` columns are exactly Subgroup, Subgroup value, *Generative AI user*,
  *Generative AI non-user*, unweighted base, weighted base. The AI workbook's XML contains
  **zero occurrences of the string “confidence”** and no lower/upper columns.
- The digital inclusion and skills workbook (SHA-256 `bc449398…b42e5`, 279,706 bytes,
  retrieved 2026-10-01) was checked as a second product and is the same: no interval
  columns, no “confidence” string.

So the correct statement for v1 is: **the gender-cell intervals exist in the producer's
analysis but their published location has not been found**, across two inspected PES
workbooks. Do not write that DSIT publishes no confidence intervals anywhere, and do not
derive an interval from base counts. The design effect of 1.67 and the documented CI
method may be cited as documentation of precision practice.

*Next check:* look for a CI-bearing table product in the remaining three PES workbooks or
an accompanying dataset, and if none exists, record it as a question for the producer
rather than as an absence.

Suppression rule (Notes): cells are suppressed with a `u` where fewer than 30 respondents
answered or fewer than 5 gave that response. Values are weighted percentages, displayed to
one decimal place, stored to three.

### 2. Paper-questionnaire consistency

The **paper questionnaire** (published alongside the release) carries the AI grid as
`Q46`, with a general AI definition and five technology rows, each answered on a scale of
“Yes, in the past week / past 3 months / longer ago / never used but heard of this /
never used and not heard of this / don't know”. The gender item is paper `Q5` “Would you
describe yourself as… Male / Female / Identify in another way (please write in) / Prefer
not to say”, matching the online `GENDER` item.

The derived measure is defined in the workbook's own note 1:

> A “generative AI user” is defined as a respondent that reported that they had used at
> least one of the following types of AI in the last three months: AI that creates
> human-like text or speech in response to prompts or queries, such as ChatGPT, Copilot
> and Gemini; Technology which uses AI to create or edit an image, video or piece of
> music; Workplace AI systems that can perform tasks, make decisions and take action on
> their own such as setting and prioritising goals or initiating new tasks or workflows.

Two consequences, both material for comparison:

1. The composite **excludes** voice assistants (Siri/Alexa) and AI robotics rows, but
   **includes autonomous workplace AI systems**, which are not generative tools. The DSIT
   “generative AI user” rate is therefore **broader than Eurostat's B5** (content creation
   with named generative tools) on one dimension and narrower on another. The two rates
   are not interchangeable, and the UK figure should not be placed in a European ranking.
2. Because `Table_E5` is a mixed-mode question, it uses the main weights; the purpose
   table `Table_E7` is **online-only, multiple-response, with its own weights and
   item-specific bases**, and cannot inherit E5's all-adult denominator (as the
   coordinator already noted).

### 3. Finer joint cells and microdata

`Table_E5` publishes **one-way subgroup rows only** (age, gender, disability, financial
hardship, household income, NS-SEC, rurality, nation and so on). There is **no published
gender × age cell**, even though gender-by-age is used as a weighting margin. A joint cell
would require respondent-level data; no UK PES microdata release was located in this
audit, and no data request was made.

## Sex/gender measurement

Four provider categories: Male, Female, **Identify in another way**, Prefer not to say.
This is the only audited source with a published third category for a generative-AI rate.
Its unweighted base is **99** respondents (weighted 141), i.e. comfortably above the
suppression threshold but very imprecise; the category must keep the provider's label and
must not be re-described as “non-binary people”, and the 49.2% estimate should always
appear with its base.

## Population, period and access

UK adults **aged 16 and over** (so above Eurostat's 74 ceiling), fieldwork **November 2025
– March 2026**, 30,698 final respondents overall (table bases differ; `Table_E5`
unweighted base 30,653). Published as **Official Statistics** under **Open Government
Licence v3.0** “except where otherwise stated” — the exception clause must be checked
before republication, and attribution is required.

## Open items

1. Decide whether to display the UK composite at all, given that it mixes generative and
   autonomous workplace AI; if yes, display the note-1 definition next to it.
2. If a UK purposes indicator is wanted, audit `Table_E7` bases and online-only weights
   separately.
3. Ask whether DSIT publishes or plans any gender × age table, or a UK Data Service
   deposit, before assuming the joint cell is unavailable permanently.
