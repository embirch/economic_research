# Appendix to "What 81,000 people want from AI"

## Source

| Field | Value |
|---|---|
| Slug | `survey-81k-interviews-2026-03-appendix` |
| Title (from page 1) | Appendix to "What 81,000 people want from AI" |
| Date (from page 1) | March 2026 |
| Date (from page 2, "Corrections") | Mar 19, 2026 |
| Type | Appendix (standalone 14-page PDF; not bound into the feature page) |
| Publisher | Anthropic |
| Primary URL | https://cdn.sanity.io/files/4zrzovbb/website/99156863ed4a812569fe00a2adfb1c93f7e5a911.pdf |
| Parent publication | "What 81,000 people want from AI", https://www.anthropic.com/features/81k-interviews — separate wiki entry `survey-81k-interviews-2026-03`. **Cross-reference only; the feature's own claims are not recorded here.** |
| Length | 14 pages |
| Contents | p.1 title; p.2 "Corrections"; pp.3–8 "Methods" (incl. two classifier prompts in full, pp.4–8); p.9 "Limitations" and "Reflections on method"; p.10 response-quality table; pp.11–14 "Additional analysis" (p.11 geographical breakdown; pp.12–14 "Light and shade co-occurrence statistics") |
| Only one copy | Unlike the two Economic Index appendices (`economic-index-2026-03-appendix`, `economic-index-2026-06-appendix`), this appendix is served from a single CDN URL, linked four times from the feature page. |
| Build | Exported from a Google Doc (`Producer: Skia/PDF m148 Google Docs Renderer`; `Title: Appendix 81K`; `content-disposition: inline;filename="Appendix 81K.pdf"`), not from InDesign as the Economic Index appendices are. This matters: the two classifier prompts are Google Docs code blocks, and each carries the word "None" above it in grey — the Docs code-block language selector, not part of the prompt (see `## Verification`). |

The feature page links this one PDF from four places, each naming a different role for it (link targets confirmed in the page's own Sanity content blocks, fetched 2026-09-16):

1. "The **Appendix** describes our methods in more detail, as well as limitations and some additional analysis." (end of the feature's method paragraph)
2. "…(see more analysis of these correlations in the **Appendix**)." (after the feature's light-and-shade correlation claim)
3. "…(see **Appendix** for geographical breakdown of respondents.)" (opening the feature's regional section)
4. Under the feature's "Appendix" H3: "Available **here**."

The feature page's own citation block gives `date = {2026-03-18}` and `title = {What 81,000 People Want from AI}`; the appendix's own Corrections page is dated Mar 19, 2026 and the CDN reports `last-modified: Thu, 19 Mar 2026 17:46:03 GMT`. `wiki/INDEX.md` dates the feature 2026-03-19. The one-day gap is recorded here and left to the INDEX owner.

## Claims

The appendix is predominantly methodological. Its substantive assertions are the sample description (p.3), the representativeness comparison (p.3), the validation statement (p.4), the response-quality table (p.10), the geographical table (p.11), and the co-occurrence analysis (pp.12–13). Numbers are as published. Every claim below names the comparison it rests on; where there is none, that is said.

1. **112,846 interviews were received, of which 80,508 met the quality threshold, over one week in December 2025.** "We received 112,846 interviews over the course of one week in December 2025, of which 80,508 met our quality threshold—we filtered out conversations that were spammy, unserious, or extremely minimal (e.g. a very short initial response, then disengagement)." (p.3, "Data collection"). No table or figure. The comparison it rests on: none — this is the sample frame. Note that 80,508 is the analytic N throughout, and that the parent publication's title rounds it to 81,000 (a 0.6% upward round of a filtered count).

2. **Respondents came from 159 countries and wrote in 70 languages.** "Respondents came from 159 countries and wrote in 70 languages." (p.3, "Data collection"). No table or figure; no country-level or language-level counts are published anywhere in the appendix. The comparison it rests on: none.

3. **Dropouts were retained; only spam, unseriousness and extreme minimality were filtered.** "We did not filter out people who engaged earnestly and then dropped out partway." (p.3, "Data collection"). The comparison it rests on: none, but this is the rule that makes the p.10 "Not reached" row non-zero and makes the per-question analytic denominators differ from 80,508.

4. **The interviewees' stated last-use mix matched the Economic Index and prior Anthropic work: 34% software development and programming against 36% computer-and-mathematical in the September 2025 report; 10% learning and education against a 7–12% range; 9% business strategy and operations against ~6%.** "For example, software development and programming accounted for 34% of interviewees’ last usage, comparable to the 36% of Claude.ai conversations classified under computer and mathematical occupations in the September 2025 Anthropic Economic Index report. Learning and education (10%) and business strategy and operations (9%) fell within the ranges reported across the Economic Index and other prior analyses, which placed education at 7–12% and business strategy at ~6%." (p.3, "Representativeness"). No table or figure. **This is the appendix's one explicitly external comparison**, and it is the comparison the whole representativeness claim rests on: self-reported last use of *any* AI chatbot, from the warm-up question, set against classifier-inferred occupational shares of *Claude.ai conversations* in `economic-index-2025-09-report`. The hyperlink under "September 2025 Anthropic Economic Index report" points to https://www.anthropic.com/research/anthropic-economic-index-september-2025-report; "research" and "analyses" both point to https://www.anthropic.com/research/clio. Note that 9% against "~6%" is stated as falling "within the ranges reported" while no range is given for business strategy.

5. **The interviewee distribution matched Claude.ai weekly active users for that week by tier and region.** "We also found that the distribution of interviewees closely matched our weekly active user distribution for that week by Claude tier (Free/Pro/Max) and region (APAC, EMEA, etc)." (p.3). No table or figure; neither distribution is printed, and "closely matched" is not quantified. The comparison it rests on: interviewees against weekly active users in the same week, on two margins (tier, region). This is the appendix's only within-Claude.ai benchmark, and it is asserted rather than shown.

6. **72% of respondents stated some job information.** "72% of respondents stated some job information." (p.4, "How we analyzed responses"), repeated in the Limitations bullet on p.9 as "72% did mention some occupational details". No table or figure. The comparison it rests on: none; it is the coverage rate of the job-context classifier, and therefore the implicit denominator of every job-level cut.

7. **Every classifier was validated at ≥90% agreement with a human on 25 labels.** "Each classifier was validated for at least 90% agreement with a human on 25 labels." (p.4). No table or figure; no per-classifier agreement rate, no κ, no confusion matrix, no identity of the human. The comparison it rests on: classifier label against one human label, on 25 items per classifier.

8. **Response quality was high on all three substantive questions, and non-response rose monotonically with question position: 97.6% / 92.5% / 88.1% substantive, and 0.9% / 6.3% / 9.7% "Not reached".** Table on p.10 (untitled; introduced by "Over the 80,508 interviews, these were the quality breakdowns of the answers. “Not reached” means they dropped off before finishing"), rows Substantive / Refused / Minimal / Rushed / Confused / Not reached, columns for questions 2, 3 and 4. Full table as published:

   | Quality label | "If you could wave a magic wand, what would AI do for you?" (%) | ""Has AI ever taken a step towards that vision for you?" (%) | "Are there ways AI might be developed that would be contrary to your vision or what you value?" (%) |
   |---|---|---|---|
   | Substantive | 97.6% | 92.5% | 88.1% |
   | Refused | 1.1% | 0.5% | 1.1% |
   | Minimal | 0.2% | 0.3% | 0.7% |
   | Rushed | 0.1% | 0.2% | 0.1% |
   | Confused | 0.1% | 0.2% | 0.3% |
   | Not reached | 0.9% | 6.3% | 9.7% |

   The comparison the claim rests on: the same six labels across the three questions, i.e. position in the interview. Each column sums to exactly 100.0% (checked; see `## Verification`), so the denominator is the full 80,508 in every column. Question 1 (the warm-up, "What's the last thing you used an AI chatbot for?") has no column. The header of the middle column carries a doubled opening quotation mark, `""Has AI ever taken`, as printed.

9. **The geographical distribution of interviewees, in twelve regions, from 29.5% North America to 0.4% Central Asia.** Table on p.11 under "Geographical breakdown" ("This was the geographical breakdown of interviewees:"), columns Region / N / %. Full table as published:

   | Region | N | % |
   |---|---|---|
   | North America | 23,727 | 29.5% |
   | Western Europe | 15,261 | 19.0% |
   | East Asia | 10,250 | 12.7% |
   | Southern & Eastern Europe | 9,385 | 11.7% |
   | Latin America & Caribbean | 8,139 | 10.1% |
   | South Asia | 4,579 | 5.7% |
   | Southeast Asia | 2,828 | 3.5% |
   | Middle East | 1,929 | 2.4% |
   | Oceania | 1,832 | 2.3% |
   | Sub-Saharan Africa | 1,651 | 2.1% |
   | North Africa | 574 | 0.7% |
   | Central Asia | 315 | 0.4% |

   The comparison it rests on: none — it is a composition table, with no population, GDP or Claude-usage benchmark beside it, and no link to the AI Usage Index of `economic-index-2025-09-report`. The twelve N values sum to 80,470, 38 short of 80,508, and the percentages sum to 100.1% (both checked; see `## Verification`). There is no "unknown" or "other" row, so 38 interviews (0.05%) are unaccounted for and the appendix does not say so. The twelve regions are not the same regional scheme as the "(APAC, EMEA, etc)" of the p.3 representativeness check.

10. **In every one of the five light-and-shade tensions, mentioning the benefit raises the probability of mentioning the harm; emotional support / dependence is the extreme case at 3.04× baseline.** Table on p.13 (untitled, columns Pairing / Lift / Lift (Experienced) / Lift (Anticipated) / φ / φ (Experienced) / φ (Anticipated)), with the p.12 text: "The answer is yes, consistently: people who raise the positive side are substantially more likely to also raise the negative side. Emotional support and dependence is particularly elevated here; mentioning one makes the other roughly 3× more likely than baseline." Full table as published:

   | Pairing | Lift | Lift (Experienced) | Lift (Anticipated) | φ | φ (Experienced) | φ (Anticipated) |
   |---|---|---|---|---|---|---|
   | Time-saving / Illusory productivity | 1.58× | 1.59× | 1.66× | 0.277 | 0.207 | 0.047 |
   | Economic empowerment / Displacement | 1.55× | 1.88× | 1.37× | 0.163 | 0.089 | 0.056 |
   | Learning / Cognitive atrophy | 1.64× | 1.63× | 1.87× | 0.206 | 0.122 | 0.070 |
   | Emotional support / Dependence | 3.04× | 4.69× | 2.73× | 0.326 | 0.337 | 0.098 |
   | Better decision-making / Unreliability | 1.71× | 1.78× | 1.94× | 0.286 | 0.244 | 0.059 |
   | Average | | | | +0.252 | +0.200 | +0.066 |

   The comparison the claim rests on: observed co-occurrence of the benefit code and the harm code within an interview, against the baseline rate of the harm code — i.e. lift. The Average row is printed for the three φ columns only; no average Lift is given. All three printed averages are the unweighted means of the five rows above them (checked; see `## Verification`). Economic empowerment / Displacement has the lowest φ of the five (0.163), which is the number behind the feature page's parenthetical that the correlation "was weakest in the economic tension".

11. **Co-occurrence is roughly three times stronger among people speaking from experience than among people speculating (avg φ = +0.200 against +0.066), and the appendix reads this as the tensions being learned rather than forecast.** "When people speak from experience, benefit and harm co-occur strongly (avg φ = +0.20); when they speculate, the link is more than twice as weak (avg φ = +0.07). The tensions, in other words, are discovered through use—people don't forecast that the thing helping them will also cost them, they learn it." (p.12), with the Average row of the p.13 table (+0.200, +0.066). The comparison the claim rests on: φ computed separately on the experienced and the anticipated subsets of mentions, averaged over the five pairings. φ (Experienced) exceeds φ (Anticipated) in all five pairings. **The ordering reverses on the lift measure:** Lift (Anticipated) exceeds Lift (Experienced) for three of the five pairings (time-saving 1.66× vs 1.59×; learning 1.87× vs 1.63×; better decision-making 1.94× vs 1.78×). The appendix anticipates exactly this and is why it prefers φ: "a correlation metric that adjusts for base rates, used here because hypothetical mentions are much rarer and would otherwise inflate any ratio-based measure" (p.12). Note also that the published "more than twice as weak" is conservative: +0.200/+0.066 = 3.03.

12. **The one thing the correction changed: incomplete interviews are excluded from the sentiment analysis.** "Mar 19, 2026: Updated to reflect that incomplete interviews were not included in sentiment analysis." (p.2, "Corrections"), consistent with the exclusion rule on p.4. The comparison it rests on: none; it is an erratum against the appendix's own earlier text, and the superseded wording is not reproduced.

## Definitions (verbatim)

All quotations are from the single PDF at the primary URL, fetched 2026-09-16. Quotation marks around a quoted block are this file's; the typographic quotation marks and dashes *inside* the quoted text are Anthropic's, reproduced as printed. The two classifier prompts are printed in the source as monospace code blocks; they are given here in fenced code blocks so that every character survives, and every character in them has been checked against both the text layer and the 150 dpi page rendering.

### The interview protocol — the four core questions (p.3, "What we asked")

> "**What we asked**. Our interview had four core questions: (1) What's the last thing you used an AI chatbot for? (2) If you could wave a magic wand, what would AI do for you? (3) Has AI ever taken a step towards that vision for you? (4) Are there ways AI might be developed that would be contrary to your vision or what you value? Anthropic Interviewer followed up on each, probing for the underlying values and experiences behind people's answers." (p.3)

The instrument itself is not reproduced; the appendix points elsewhere for it:

> "For a full description of the Anthropic Interviewer methodology, see here. What follows is a brief overview of how we collected and analyzed data for this study." (p.3; "here" links to https://www.anthropic.com/research/anthropic-interviewer — separate wiki entry `anthropic-interviewer-2025-12`)

### Sampling and filtering rules (p.3, "Data collection")

> "**Data collection**. We received 112,846 interviews over the course of one week in December 2025, of which 80,508 met our quality threshold—we filtered out conversations that were spammy, unserious, or extremely minimal (e.g. a very short initial response, then disengagement). We did not filter out people who engaged earnestly and then dropped out partway. Respondents came from 159 countries and wrote in 70 languages." (p.3)

### Representativeness rule — validation, not weighting (p.3, "Representativeness")

> "**Representativeness**. We validated the representativeness of our Claude.ai user base by usage patterns, region, and tier. The first question we asked people, as a warm-up question, was what they last used an AI chatbot for. We found that this matched our Anthropic Economic Index and other similar prior research well. For example, software development and programming accounted for 34% of interviewees’ last usage, comparable to the 36% of Claude.ai conversations classified under computer and mathematical occupations in the September 2025 Anthropic Economic Index report. Learning and education (10%) and business strategy and operations (9%) fell within the ranges reported across the Economic Index and other prior analyses, which placed education at 7–12% and business strategy at ~6%." (p.3)

> "We also found that the distribution of interviewees closely matched our weekly active user distribution for that week by Claude tier (Free/Pro/Max) and region (APAC, EMEA, etc)." (p.3)

**There is no weighting rule anywhere in the appendix.** The two passages above are the whole of what it says about representativeness, and both are validation statements. No sentence in the fetched text contains "weight" in a sampling sense, "weighted", "post-stratif", "raked" or "propensity"; the only occurrences of "weight" are inside the sentiment prompt ("Note and weight what they emphasize") and in its own text ("concerns weigh heavier"). Every published number is therefore an unweighted count or share of the 80,508.

### The classifier suite and its dimensions (pp.3–4, "How we analyzed responses")

> "**How we analyzed responses.** Interview transcripts were processed through a suite of hand-validated Claude-powered classifiers, each designed to extract a specific dimension of a respondent's answers. Each interview was classified across multiple dimensions, including: visions (how they answered the question about what they’d want AI to do if they had a magic wand), experiences (how they answered the question about whether AI had taken a step towards their vision) and concerns (how they answered the question about how AI might be developed contrary to their values or vision). We also classified job domain (inferred from self-description, e.g. legal or healthcare work) and job structure (what kind of employment setup they had, e.g. employee or entrepreneur). 72% of respondents stated some job information." (pp.3–4)

### Multi-label rule, category derivation, validation rule and exclusion rule (p.4)

> "Concerns were multi-label, i.e. a single interview could receive multiple codes, since interviewees tended to state multiple concerns. Some classifiers (e.g. the “concerns” classifier) were designed first by analyzing answers with a bottom-up clustering algorithm—categories were derived from clusters that surfaced during initial analysis—to ensure comprehensive yet cleanly separated categories. Each classifier was validated for at least 90% agreement with a human on 25 labels. Transcripts where interviewees did not reach the relevant part of the interview were excluded from the relevant analysis (e.g. those who did not answer the concerns question were excluded from the concerns classifier, the sentiment analysis and the light and shade analysis)." (p.4; "bottom-up clustering algorithm" links to https://www.anthropic.com/research/clio — separate wiki entry `clio-insights-2024-12`)

### Classifier prompt 1 of 2 — sentiment score, in full (pp.4–5)

Introduced by:

> "Example of classifier prompt for extracting sentiment score:" (p.4)

```
Rate this person's overall sentiment toward AI on a 1-7 scale based on the FULL
interview.

1—Extremely negative.
2—Negative: Concerns clearly dominate.
3—Lean negative: Overall more negative than positive, e.g. concerns weigh
heavier.
4—Mixed/neutral: Genuinely in the middle—real benefits AND real concerns,
roughly balanced, hard to find that this person leans towards one side or
another, or they are simply neutral.
5—Lean positive: Overall more positive than negative.
6—Positive: Clearly enthusiastic. Concerns are minor, hypothetical, or
mentioned only when directly asked.
7—Extremely positive.

Guidance:
- Note and weight what they emphasize and return to.
- Someone who lists benefits then pivots to a long passionate concern monologue
is probably a 3-4, not a 5-6.
- Most people have mixed feelings—don't default to extremes. Use the full 1-7
range.

<interview>
{TRANSCRIPT}
</interview>

Return ONLY a single integer (1-7) in <answer> tags.
```
(pp.4–5, block spans the page break after "- Note and weight what they emphasize and return to.")

The seven scale points above are the whole of the sentiment scale definition. The appendix does not define "net positive sentiment"; that cut appears only on the feature page (`survey-81k-interviews-2026-03`).

### Classifier prompt 2 of 2 — job context, in full, with all category definitions (pp.5–8)

Introduced by:

> "Example of classifier prompt for classifying job context:" (p.5)

```
Classify this person's professional context along TWO dimensions based on what
they say about themselves in the interview.

Respond with exactly two labels, comma-separated, no spaces:
employment_structure,professional_domain

Use the MOST SPECIFIC label you can confidently support. When you have LIMITED
information, use BROADER categories (e.g. employee, independent) or
UNCLEAR/OTHER. When you have CLEAR information, use the more SPECIFIC
categories.

DIMENSION 1 — EMPLOYMENT STRUCTURE (how is your work organized?):

BROAD:
employee - works for someone.
independent - works for themselves.

SPECIFIC:
entrepreneur_founder — Building or scaling a business. If unsure vs
solopreneur, choose entrepreneur_founder.
solopreneur — One-person operation without scaling ambitions. Solo builders,
indie hackers, side hustles.
freelancer_independent_contractor — Sells labor/skills to clients. Talks about
"my clients," "gigs," rates, finding work.
small_business_owner — Runs a small business (shop, restaurant, practice,
agency) focused on steady operations rather than growth/scaling (as
entrepreneurs tend to be).
employee_large_org — Works for someone else in a medium-to-large organization
(~50+ people).
employee_small_org — Works for someone else in a small company or startup (<~50
people).
employee_with_side_hustle — Has a steady job but also runs a serious AI side
project (not just hobby use).
academic_institutional — Employed by a university or research institution, e.g.
tenure-track, lab, or grant-funded structure.
student — In school at any level. (This generally means their domain is
not_working)
not_working — Retired, unemployed, on disability, stay-at-home parent, between
jobs.

FALLBACKS:
unclear_structure — Not enough information to classify employment structure.
other_structure – Some other structure not described.

DIMENSION 2 — PROFESSIONAL DOMAIN (what kind of work do you do?):

BROAD:
white_collar_office — Office/desk-based professional work but unclear which
specific type (e.g. mentions having lots of emails).

SPECIFIC:
technical_software — Software engineering, web/app development,
blockchain/Web3, data engineering, DevOps, IT. Building or troubleshooting
technical systems.
science_research — Scientific research in any discipline — bench science,
computational science, social science, clinical research, R&D. Oriented toward
knowledge production, experiments, publications.
creative_arts — Writing, visual art, music, film, design, photography, game
design, content creation. The creative craft is the primary identity (e.g.
content creation for instrumental marketing doesn't count).
education_teaching — Teaching, tutoring, curriculum development
healthcare_medical — Doctors, nurses, therapists, pharmacists, medical
technicians; clinical or patient-facing healthcare work.
legal — Lawyers, paralegals. Licensed or specialized professional services in
law.
finance_accounting – accountants, financial analysts, auditors. Licensed or
specialized professional services in finance.
sales_marketing_communications — Sales, marketing, PR, communications,
advertising, growth, account management, social media management.
administrative_operations — Office management, executive assistance, data
entry, bookkeeping, HR administration, office coordination, project
coordination.
trades_physical — Electricians, construction, mechanics, manufacturing,
trucking, logistics, agriculture, maintenance, dispatching, etc.
government_policy_military — Government administration, policy analysis, civil
service, military, law enforcement. Distinguished by public-sector
institutional context.
community_social_services — Social work, nonprofit work, community organizing,
religious leadership, counseling (non-clinical), advocacy.
management_executive — Primary identity is managing people or organizations
rather than doing domain-specific work. Executives, general managers, C-suite.
not_working - student (non-PhD i.e. not doing research) or not currently
working for any reason.
other_domain — Doesn't fit neatly into the above.
unclear_domain — Not enough information to classify professional domain. If
they don't mention their job this is likely the best choice, since not_working
is meant for people who are explicitly not working

EXAMPLES:
- Software engineer at Google → employee_large_org,technical_software
- Freelance graphic designer → freelancer_independent_contractor,creative_arts
- Physics professor → academic_institutional,science_research
- Stay-at-home mom using AI for personal projects → not_working,unclear_domain
- High school teacher → employee_large_org,education_teaching
- Medical doctor at a hospital → employee_large_org,healthcare_medical
- PhD student in biology → student,science_research
- no mention of work -> unclear_structure,unclear_domain
- "I'm in the tech sector" → employee,white_collar_office
- Retired accountant → not_working,not_working (since retired, not currently
working in accounting)
- Undergrad student learning ML -> student,not_working

<interview>
{{TRANSCRIPT}}
</interview>

Think for 2-3 sentences in <thinking> tags first. Don't confuse hobbies/side
projects with their actual profession.
Then output: <answer>structure,domain</answer>
```
(pp.5–8; the block spans four pages, breaking after "…rates, finding work." on p.5, after "…services in law." on p.6, and after "</interview>" on p.7)

**Category counts, from the prompt as printed.** Employment structure: 14 labels (2 BROAD — `employee`, `independent`; 10 SPECIFIC — `entrepreneur_founder`, `solopreneur`, `freelancer_independent_contractor`, `small_business_owner`, `employee_large_org`, `employee_small_org`, `employee_with_side_hustle`, `academic_institutional`, `student`, `not_working`; 2 FALLBACKS — `unclear_structure`, `other_structure`). Professional domain: 17 labels (1 BROAD — `white_collar_office`; 14 SPECIFIC — `technical_software`, `science_research`, `creative_arts`, `education_teaching`, `healthcare_medical`, `legal`, `finance_accounting`, `sales_marketing_communications`, `administrative_operations`, `trades_physical`, `government_policy_military`, `community_social_services`, `management_executive`, `not_working`; plus `other_domain`, `unclear_domain`, which are not under a FALLBACKS heading in this dimension). `not_working` is a label in both dimensions, with different definitions in each.

### The validation rule (p.4) — restated here because it is the appendix's definition of "hand-validated"

> "Each classifier was validated for at least 90% agreement with a human on 25 labels." (p.4)

This one sentence, together with "a suite of hand-validated Claude-powered classifiers" (p.3), is the whole of the validation definition. No agreement statistic other than raw percent agreement is defined or reported.

### The co-occurrence measures (p.12)

> "For each tension, we measured whether mentioning the benefit predicts mentioning the harm." (p.12)

> "A more revealing split is between experienced and anticipated accounts. We measured co-occurrence separately for each, using φ (a correlation metric that adjusts for base rates, used here because hypothetical mentions are much rarer and would otherwise inflate any ratio-based measure)." (p.12)

"Lift" is used as a column header on p.13 and glossed in text only as "more likely than baseline" (p.12) and "above baseline" (p.13); the appendix gives no formula for either Lift or φ, and does not define "baseline".

### Section and sub-section headings, and the table stubs (pp.2–13)

> "Corrections" (p.2) · "Methods" (p.3) · "Limitations" (p.9) · "Additional analysis" (p.11) · "Geographical breakdown" (p.11) · "Light and shade co-occurrence statistics" (p.12)

> "Mar 19, 2026: Updated to reflect that incomplete interviews were not included in sentiment analysis." (p.2, the whole of the Corrections section)

> "Over the 80,508 interviews, these were the quality breakdowns of the answers. “Not reached” means they dropped off before finishing:" (p.10, the only definition given for any quality label)

> "This was the geographical breakdown of interviewees:" (p.11)

The six quality labels — Substantive, Refused, Minimal, Rushed, Confused, Not reached — are defined only for "Not reached". The twelve regions are named in the table and nowhere defined by country list.

## Data and methods

In this file's words, with page references.

**Instrument.** A four-question open-ended interview conducted by Anthropic Interviewer, with model-generated follow-up probes on each answer (p.3). The four core questions are printed in full (p.3); the probes are not, and the instrument as a whole is delegated to `anthropic-interviewer-2025-12`. Question 1 is a warm-up used for the representativeness check, not for the substantive analysis (p.3).

**Field period and frame.** One week in December 2025; the frame is existing Claude.ai users who opted in (p.3; p.9, "User sample"). 112,846 interviews received; 80,508 retained after quality filtering; the retained set is the analytic N for every published number (p.3, p.10).

**Filtering.** A single quality gate on the conversation (spammy, unserious, extremely minimal), applied before analysis, and deliberately *not* applied to earnest dropouts (p.3). Neither the gate's operationalisation nor its classifier is published, and the 32,338 excluded interviews are not described or profiled anywhere.

**Representativeness handling.** Validated on three margins — self-reported last use against published Economic Index occupational shares, and interviewee composition against Claude.ai weekly active users by tier and by region (p.3). **No weights are constructed and none are applied**; there is no sentence in the appendix that reweights, post-stratifies or rakes the sample to any external population, and no comparison to any non-Claude population. Every published share is an unweighted share of the retained interviews.

**Measurement.** A suite of Claude-powered classifiers, one per dimension, run over de-identified transcripts (p.3). At least six dimensions are named — visions, experiences, concerns, job domain, job structure (p.3–4) — plus sentiment (p.4), plus whatever produces the light/shade benefit and harm codes and the experienced/anticipated split (p.12) and the six response-quality labels (p.10). **Two prompts of the suite are printed** (sentiment, job context; pp.4–8), each labelled an "Example". The concerns taxonomy was derived bottom-up by clustering answers before a top-down classifier was written over the resulting categories (p.4); which other classifiers were built that way is left as "Some classifiers (e.g. the “concerns” classifier)".

**Label structure.** Concerns are multi-label (p.4). Sentiment is a single integer 1–7 (p.4). Job context is exactly two labels drawn from 14 × 17 category sets, forced-choice with explicit fallbacks, with an instruction to prefer breadth under limited information and a chain-of-thought step before the answer (pp.5–8). The response-quality labels are a single choice among six per question (p.10).

**Validation.** Per classifier: at least 90% agreement with a single human on 25 labels (p.4). That is the entire validation apparatus reported.

**Analytic denominators.** Interviewees who did not reach a question are excluded from that question's analyses, and the appendix names three analyses affected: the concerns classifier, the sentiment analysis, and the light and shade analysis (p.4). The p.2 correction exists to make that true of sentiment. The p.10 table gives the raw material for those denominators — 9.7% did not reach the concerns question — but **the appendix never prints the resulting N for any analysis**, so every sentiment, concerns and light/shade number in the parent publication rests on an unstated denominator smaller than 80,508.

**Co-occurrence analysis.** For each of five named benefit/harm pairings, the appendix computes lift (the factor by which mentioning one raises the probability of mentioning the other, relative to "baseline") and φ, separately for all mentions, for mentions grounded in experience, and for anticipated mentions (pp.12–13). φ is preferred on the stated ground that the anticipated subset is much rarer and would inflate a ratio measure. The unit is the interview; the codes are "discussed … substantively anywhere in their interview", a definition that appears on the feature page rather than here.

**Statistics of inference.** None. The appendix reports no standard errors, no confidence intervals, no p-values, no cell counts for any co-occurrence cell, and no N for any analysis other than 80,508 and the twelve regional counts. The only uncertainty language is "roughly 3×" and "~6%".

## Limitations (verbatim)

The appendix has a section headed "Limitations" on p.9, with a four-bullet list, followed by an unlabelled "Reflections on method" passage. All four bullets are quoted in full. The bullet lead-ins are italic in the source.

> "A few limitations are worth naming:" (p.9)

> "● *Self-reported occupational categories.* Occupational categories are inferred from what respondents said about themselves, not from verified metadata. 72% did mention some occupational details, but people who didn't mention any such details weren't coded. Our job-level analyses perhaps overrepresent people who use AI at work, and thus have more reason to mention their work in the context of this interview." (p.9)

> "● *Label ambiguity.* Classifying open-ended natural language text is often inherently subjective and requires judgment calls." (p.9)

> "● *User sample.* All respondents were existing Claude.ai users who opted in to the interview. This skews toward people who have found enough value in AI to keep using it, and likely toward more positive visions than a general population sample would produce." (p.9)

> "● *Ordering effects*. The interview structure creates natural priming: by the time respondents reach the question about AI being developed contrary to their values, they've already articulated their hopes. Someone who just described wanting emotional companionship may be primed to voice concerns about authentic connection. This could inflate the co-occurrence between light and shade that we discovered. The interview's length also produced some dropout and possibly less elaboration on later questions; we corrected for this where relevant (e.g., removing those who didn't reach the concerns question from that specific analysis)." (p.9)

Two further passages outside the Limitations section bear on the scope of the appendix's own numbers and are quoted here because they function as limitations:

> "Response quality was generally high. Few interviews were minimal, incoherent, or clearly disengaged—see breakdown below—which we attribute partly to the conversational format and partly to novelty." (p.10)

> "In the Limitations section above, we discuss “ordering effects” that might prime some of these results or inflate the co-occurrence between light and shade to some degree. However, we believe that the strength of the associations we found (e.g. 3× above baseline) is beyond what priming alone could explain. The priming story is also not entirely obvious—you might expect enthusiasts to defend their desired use case, and articulate concerns about e.g. being *prevented* from engaging in emotional partnership with AI rather than articulate the first-order risks of what they desire (i.e. emotional dependence). That they disproportionately did the latter is itself interesting." (pp.13–14)

Note what the named limitations do **not** include: the size of the validation exercise, the absence of weights, the unstated per-analysis denominators, or the missing 38 interviews in the regional table.

## Open questions, conjectures and promised follow-ups (verbatim)

**No promised follow-up exists in this appendix.** The fetched text contains no sentence with "future work", "further research", "more research", "we plan", "we will", "next step", "remains an open question", "leave for", or any equivalent (grep-confirmed over the full text layer; see `## Verification`). There is no forward-looking programme statement of any kind. Ledger entries for this publication's promises therefore have to be taken from the parent feature (`survey-81k-interviews-2026-03`) or from `survey-81k-economics-2026-04`, not from here.

What the appendix does contain is **five untested conjectures**, each stated in Anthropic's own hedged voice. They are quoted in full.

1. On why respondents were candid — a conjecture about the instrument, offered with an alternative explanation and not tested against one:

> "**Reflections on method.** One thing we didn't fully anticipate was how candid people would be. Respondents shared things—grief, mental health crises, financial precarity, relationship failures—that our human user researchers rarely encounter in traditional interviews. While this might be due to the nature of the questions we asked, we also think this reflects something real about the AI interviewer format: there's little social cost to vulnerability when the “someone” on the other end isn’t a person. The same qualities that make people turn to AI for emotional support in their daily lives appear to make them more forthcoming in an AI-led interview. This increased shamelessness may be a double-edged sword: it both leads to sharing more authentic details, and can lead to people acting in a more hostile or dismissive manner than they would be in a human interview." (p.9)

2. On why response quality was high — a two-part attribution with no test and, in the case of novelty, no way to test it from one wave:

> "…which we attribute partly to the conversational format and partly to novelty." (p.10)

3. On the direction of causation in the light-and-shade result — a causal reading of a cross-sectional co-occurrence:

> "The tensions, in other words, are discovered through use—people don't forecast that the thing helping them will also cost them, they learn it." (p.12)

4. On whether priming explains the co-occurrence — a belief, with a reason, and no sensitivity analysis behind it:

> "However, we believe that the strength of the associations we found (e.g. 3× above baseline) is beyond what priming alone could explain." (p.13)

5. On why the priming story is unattractive — an argument from expectation, explicitly flagged as interesting rather than settled:

> "The priming story is also not entirely obvious—you might expect enthusiasts to defend their desired use case, and articulate concerns about e.g. being *prevented* from engaging in emotional partnership with AI rather than articulate the first-order risks of what they desire (i.e. emotional dependence). That they disproportionately did the latter is itself interesting." (pp.13–14)

Two hedges in the Limitations section are also conjectures rather than measured facts, and are recorded as such: "Our job-level analyses **perhaps** overrepresent people who use AI at work" and "**likely** toward more positive visions than a general population sample would produce" (p.9, emphasis added). Neither is bounded.

The Corrections section is an erratum, not a follow-up: it records a change already made and does not reproduce the superseded wording (p.2).

## What it did not test

This section is **this file's inference, not the appendix's own words**. Each item is something the appendix's own material makes checkable, and which it did not check.

**Robustness and validation checks it could have run and did not**

1. **The validation is far too small to support "hand-validated".** 90% agreement on 25 labels per classifier (p.4) is 22 or 23 correct out of 25. *This file's calculation, not published:* the 95% Clopper–Pearson interval around 23/25 runs from about 0.74 to 0.99, and around 22/25 from about 0.69 to 0.98. A classifier whose true agreement is 75% passes this gate routinely. No power statement, no per-classifier figure, no second rater, no κ or any chance-corrected statistic, no confusion matrix, no error analysis, and no statement of who the human was or whether they were blind to the classifier's output. Given that the appendix's own second limitation is that classifying open-ended text "is often inherently subjective and requires judgment calls" (p.9), a single-rater agreement rate cannot separate classifier error from rater disagreement, and the appendix does not say so.

2. **Most of the prompts are not published.** Two prompts are printed, each explicitly an "Example" (pp.4, 5). The visions, experiences, concerns, job-*domain*-versus-*structure* taxonomy (the printed prompt covers both, but the concerns taxonomy that carries the feature's headline categories is not printed), light/shade benefit and harm codes, the experienced/anticipated split, and the six response-quality labels all run on prompts and category lists that are not reproduced. The concerns taxonomy in particular is the one described as clustering-derived, and the clusters, their sizes and the category list are absent.

3. **The exclusion rule's effect on results is never bounded.** The rule is stated (p.4) and the non-response rates are printed (p.10), but no analysis is run on the excluded group and no result is shown with and without the exclusion. *This file's arithmetic on the published percentages:* 9.7% of 80,508 is about 7,809 interviews that did not reach the concerns question, so the concerns, sentiment and light/shade analyses run on roughly 72,700, not 80,508. That number is never printed. Whether the ~7,800 excluded differ systematically — they are, by construction, the people who gave up on a long interview — is not examined, and the appendix's own Limitations bullet ("we corrected for this where relevant") treats deletion as a correction rather than as a selection to be bounded.

4. **Refusals are not distinguished from absences of concern.** For the concerns question, 1.1% Refused, 0.7% Minimal, 0.1% Rushed and 0.3% Confused (p.10) — 2.2% in total — are, on the stated rule, *not* excluded, since those respondents reached the question. Whether they are coded as expressing no concern (which would depress every concern rate and every light/shade lift) or dropped is not stated and not tested either way.

5. **The response-quality classifier is itself unvalidated and un-prompted.** Six labels, three columns, no definition except for "Not reached", no prompt, and no agreement rate — and the appendix uses the resulting table to support a substantive claim ("Response quality was generally high", p.10).

6. **No test of the representativeness claim it makes.** "Closely matched" (p.3) is asserted for tier and region with neither distribution printed and no distance measure, so the reader cannot judge it or reproduce it. The one quantified comparison compares unlike things without saying so: self-reported last use of *any AI chatbot*, from a warm-up question, against Claude-classified occupational shares of *Claude.ai conversations* in a *September 2025* release, when this field period is December 2025. Three months of drift, a different unit (respondent vs conversation) and a different construct (self-described activity vs inferred O*NET occupational group) are all left unaddressed. The appendix runs no comparison against the nearer release, and no comparison of the interviewees' own usage logs against the frame, though the survey stream elsewhere links interviews to usage data.

7. **No weighting, and no sensitivity to its absence.** Having established that the sample resembles Claude.ai weekly actives on two margins, the appendix neither weights to that distribution nor shows what any headline number would become under weights. North America is 29.5% of interviewees (p.11) with no benchmark beside it, so the reader cannot tell whether the regional composition is a finding or an artefact of who opted in.

8. **The regional table does not reconcile to the sample.** *This file's arithmetic on the published table:* the twelve N values sum to 80,470, 38 short of 80,508, and the twelve percentages sum to 100.1%. There is no "unknown" or "other" row and no note. 38 interviews (0.05%) are silently unaccounted for. Whether they are region-unknown, or a rounding/deduplication residue, is not said.

9. **The twelve regions are never defined, and are not the regions used for the representativeness check.** The p.3 check is by "(APAC, EMEA, etc)"; the p.11 table is by twelve finer regions. No country-to-region mapping is published, so neither the table nor the check is reproducible, and the two cannot be put on the same footing. 159 countries are claimed (p.3) and none is named.

10. **No small-cell noise check on the regional table.** Central Asia is 315 interviews and North Africa 574 (p.11). The feature page cuts sentiment by country off this sample; the appendix reports no minimum cell size, no suppression threshold and no interval for any regional or national quantity, and does not state a privacy threshold of the kind the Economic Index appendices state.

11. **Lift and φ have no uncertainty, and no cell counts.** Twelve co-occurrence quantities per pairing are implied by the p.13 table and none is accompanied by a count, an interval, or a test. The two subsets are of very different size — the appendix says so, "hypothetical mentions are much rarer" (p.12) — which makes φ (Anticipated) the least precisely estimated column in the table and the one carrying the paper's causal reading. No minimum detectable difference is given for the +0.200 vs +0.066 contrast.

12. **The experienced/anticipated split is treated as exogenous.** Whether a mention is "experienced" or "anticipated" is itself a classifier output, and it is correlated with how much a person has used AI — which is also what the benefit/harm codes are about. The appendix does not test whether the φ gap survives conditioning on interview length, elaboration, tier, or the volume of a respondent's mentions, so the finding that tensions are "discovered through use" is not separated from the mechanical fact that people who say more, and who speak concretely, generate more co-occurring codes.

13. **The measure disagreement in its own table is not discussed.** Lift (Anticipated) exceeds Lift (Experienced) in three of five pairings while φ (Experienced) exceeds φ (Anticipated) in all five. The appendix explains in advance why it prefers φ (p.12) but never shows the reader that the two measures order the subsets differently, and never reports the base rates that would let anyone reconcile them. The Average row is printed for φ only, which has the effect of showing the agreeing measure and not the disagreeing one.

14. **Ordering effects are named as a limitation and then argued away without a test.** The design admits three cheap tests the appendix does not run: co-occurrence among people who answered the concerns question before elaborating a vision; co-occurrence as a function of how much was said at question 2; and, most directly, a randomised or reversed question order in a later wave. Instead the defence is "we believe … is beyond what priming alone could explain" (p.13). One row of the table cuts against that defence and is not mentioned: Emotional support / Dependence is the only pairing where φ (Experienced), 0.337, exceeds the pooled φ, 0.326, and it is also the pairing the priming argument is built around.

15. **The AI-interviewer candour conjecture has no comparison group.** The claim that respondents were more forthcoming than in human-led interviews (p.9) is offered against "our human user researchers rarely encounter" — an impression, not a matched human-interview arm. A parallel human interview, or a comparison against the same protocol run without the AI interviewer, is not attempted, and the appendix concedes an alternative explanation ("the nature of the questions we asked") without testing it. The second half of the conjecture, that the format also makes people more hostile or dismissive, is not measured at all, though the response-quality labels on p.10 would have been the obvious place.

16. **"Novelty" as an explanation of response quality is untestable from one wave and is not flagged as such.** A single December 2025 field period cannot separate format from novelty; the appendix asserts both (p.10) and does not say that a second wave is required.

17. **The 32,338 filtered interviews are never characterised.** 28.7% of what was received was discarded on an unpublished rule (*this file's arithmetic:* 112,846 − 80,508 = 32,338, a 71.3% retention rate). No region, tier, language or question-position breakdown of the discarded group, no sensitivity of any headline number to a looser or tighter gate, and no statement of whether the gate was applied by a classifier or by hand.

18. **Language is claimed and then never used.** 70 languages (p.3); no per-language counts, and no test of whether classifier agreement — validated on 25 labels, in an unstated language — holds outside English. Given that every construct in the study is a judgement about open-ended natural-language text, language-wise validation is the most consequential omission in the appendix, and it is not named as a limitation.

19. **Opt-in selection is named but not bounded.** The "User sample" bullet (p.9) states the direction of the bias — toward people who find value in AI, and toward more positive visions — and stops. The appendix holds the material for a partial bound (sentiment by tier, by tenure, by usage intensity, or against the 112,846 received) and computes none of it, so the reader has a direction with no magnitude.

**Constructs its own definitions raise and leave open**

20. **"Net positive sentiment" is not defined in the appendix.** The seven scale points are printed (pp.4–5); the threshold that turns them into the feature's headline percentages is not, and neither is any check that the 1–7 labels are used as written. Points 1 and 7 are labelled only "Extremely negative"/"Extremely positive", and the prompt itself warns the model away from them ("don't default to extremes"), a nudge whose effect on the distribution is not reported.

21. **The job-context prompt's forced-choice structure is not examined.** Exactly two labels, always, from 14 × 17 sets, with `not_working` defined differently in each dimension and an instruction to fall back to breadth. No distribution over the 31 labels is published, no share falling to `unclear_*`, and no check of whether the 72% coverage figure (p.4) means 72% avoided both `unclear_` fallbacks or 72% said anything at all about work. The Limitations bullet says people who didn't mention details "weren't coded", which suggests the former; the prompt's own fallbacks suggest everyone gets a label.

22. **The prompt's own internal inconsistencies are not reconciled and suggest it was never linted.** `other_structure` and `finance_accounting` use an en dash where every other definition uses an em dash; two of eleven examples use `->` where nine use `→`; `education_teaching` has no closing full stop; `finance_accounting` begins lowercase where every sibling begins capitalised; the sentiment prompt interpolates `{TRANSCRIPT}` while the job prompt interpolates `{{TRANSCRIPT}}`. Individually trivial; together they are evidence that the published text is a transcription of working prompts rather than a versioned artefact, and the appendix carries no version, hash or date for any prompt.

23. **Multi-label concerns are reported as shares without a denominator convention.** Concerns are multi-label (p.4); whether a published concern share is per interview or per code, and how multiply-coded interviews enter the lift and φ calculations, is not stated.

24. **Light and shade are five pairings, and the choice of five is not justified.** The pairings are named only in the p.13 table. Whether they exhaust the taxonomy, how they were selected from the clustering output, and whether other benefit/harm pairs were measured and not reported, is not addressed — so the "This pattern held across every tension we measured" framing cannot be checked against the set actually measured.

25. **Nothing links the interviews to usage logs.** Every respondent is a Claude.ai account holder and the Economic Index measures what those accounts do. The appendix validates self-reported last use against *published aggregate* Index shares (p.3) rather than against the respondents' own conversations, which is the one check that would settle the self-report question and the one the survey stream later makes routine. It is not attempted or mentioned here.

## Verification

**Fetch record — 2026-09-16.**

| URL | Method | Result |
|---|---|---|
| https://cdn.sanity.io/files/4zrzovbb/website/99156863ed4a812569fe00a2adfb1c93f7e5a911.pdf | `web_fetch` | **Not attempted** — the fetch service refuses `cdn.sanity.io` (`url_not_allowed`), as recorded for the two Learning-curves appendix copies in `room/lead-2026-09-16-wiki-economic-index-2026-03-appendix.md`. |
| https://cdn.sanity.io/files/4zrzovbb/website/99156863ed4a812569fe00a2adfb1c93f7e5a911.pdf | `curl` to `/tmp/app81k.pdf` | **HTTP 200**, 263,879 bytes, 14 pages. `etag`/`x-sanity-md5` `01185b2de5e8131a3cba085fe79ecdbe`; local `md5sum` identical. `last-modified: Thu, 19 Mar 2026 17:46:03 GMT`. `content-disposition: inline;filename="Appendix 81K.pdf"`. PDF `Title: Appendix 81K`, `Producer: Skia/PDF m148 Google Docs Renderer`, PDF 1.4, letter, no creation-date key. |
| https://www.anthropic.com/features/81k-interviews | `curl` to `/tmp/81kfeat.html` | **HTTP 200.** Fetched only to establish which URLs the feature links as its appendix and in what role (four links, all to the same PDF; the four anchor texts and their surrounding sentences are quoted in `## Source`), and to read the page's citation date. The feature's own claims are covered by `wiki/reports/survey-81k-interviews-2026-03.md`, not here. |

No fetch failed. Only one copy of the appendix exists on the CDN; the four feature-page links resolve to the same file hash.

**Reading record.** The PDF was read in full twice: through the text layer (`pdftotext -layout`, `pdftotext`, and `pypdf` page by page, all 14 pages) and visually (`pdftoppm` at 150 dpi, all 14 pages inspected as images). Pages 1, 2 and 14 carry little text and were confirmed as such visually. The only embedded image in the document is the Anthropic wordmark on p.1 (`/XObject` present on p.1 only, checked with `pypdf`); there are **no figures or charts anywhere in the appendix**, so the alt-text convention of `room/director-2026-09-16-alt-text-ruling.md` has no application here and no number in this file was read off a chart.

**Quotation check.** Every quotation in `## Definitions (verbatim)`, `## Limitations (verbatim)` and `## Open questions, conjectures and promised follow-ups (verbatim)` was checked character-by-character against the `pypdf` text layer and, where the extractor produced artefacts, against the 150 dpi page image. Extractor artefacts identified and corrected to what is printed:

- Ligature substitutions in the body font: the extractor returns "ﬁltered", "veriﬁed", "classiﬁers", "beneﬁt", "inﬂate", "Reﬂections", "speciﬁc" with a single `ﬁ`/`ﬂ` glyph. Quotations above use ordinary letters, which is what the page displays.
- Word-splitting in italic bullet lead-ins: the extractor returns "Label am biguity" and "User sam ple". The page prints "Label ambiguity" and "User sample" (confirmed at 150 dpi). Corrected in the quotations.
- **The word "None" above each of the two prompt code blocks is not part of the prompt.** It appears in grey, in the code-block header position, and is the Google Docs code-block language selector reading "None"; the extractor emits it at the top of pages 4 and 5. It is excluded from the quoted prompts and recorded here instead.
- Hyperlink run boundaries produce a spurious space before a following em dash: the extractor returns "clustering algorithm —categories" on p.4. The page prints "algorithm—categories" closed up (confirmed at 150 dpi). Quoted closed up.

After correcting for those four artefact classes, all 28 blockquoted passages and both prompt code blocks in this file match the extracted text exactly, verified by substring test.

Characters reproduced as printed and deliberately not normalised: the em dashes in the sentiment scale ("1—Extremely negative."), the en dashes on `other_structure` and `finance_accounting` against em dashes elsewhere, the `→` in nine examples against `->` in two, the single vs double braces (`{TRANSCRIPT}` / `{{TRANSCRIPT}}`), the en dash in "7–12%", the `×` in the lift column, the Greek φ, the curly apostrophes and quotation marks, and the doubled opening quotation mark in the p.10 table header.

**Claim check — arithmetic on the published numbers.** All checks below are on numbers printed in the appendix; no data file was opened (`team/agents/programme-lead.md`; `room/director-2026-09-16-alt-text-ruling.md`).

| Check | Result |
|---|---|
| p.10 table, each column sums to 100% | 97.6+1.1+0.2+0.1+0.1+0.9 = **100.0**; 92.5+0.5+0.3+0.2+0.2+6.3 = **100.0**; 88.1+1.1+0.7+0.1+0.3+9.7 = **100.0**. Denominator is the full 80,508 in all three columns. |
| p.11 table, N sums to the sample | 23,727+…+315 = **80,470**, i.e. **38 short of 80,508**. No residual row exists. Recorded as Claim 9 and item 8 of `## What it did not test`. |
| p.11 table, % sums to 100 | **100.1%** (rounding). |
| p.11 table, each % equals N/80,508 | Every row agrees to the printed decimal (e.g. 23,727/80,508 = 29.47% → 29.5%; 1,651/80,508 = 2.05% → 2.1%). So 80,508 is the published denominator and the 38 are genuinely missing from the table, not from the sample. |
| p.13 Average row reproduces the five rows above it | φ: (0.277+0.163+0.206+0.326+0.286)/5 = 0.2516 → printed **+0.252** ✓. φ (Experienced): (0.207+0.089+0.122+0.337+0.244)/5 = 0.1998 → printed **+0.200** ✓. φ (Anticipated): (0.047+0.056+0.070+0.098+0.059)/5 = 0.0660 → printed **+0.066** ✓. Unweighted means, all three. |
| p.12 "more than twice as weak" against p.13 averages | +0.200/+0.066 = **3.03**, so the published wording understates the gap. |
| p.12 "roughly 3× more likely" against p.13 | Matches the pooled Lift for Emotional support / Dependence, **3.04×** ✓. |
| Retention rate implied by p.3 | 80,508/112,846 = **71.3%**; 32,338 interviews discarded. Not published as either figure. |
| Analytic N implied by p.10 for the concerns/sentiment/light-and-shade analyses | 9.7% of 80,508 ≈ **7,809 excluded**, leaving ≈ **72,700**. Not published. |
| 95% interval around the p.4 validation gate | Clopper–Pearson on 23/25 ≈ **[0.74, 0.99]**; on 22/25 ≈ **[0.69, 0.98]**. This file's calculation, not published. |

**Open-questions grep.** The full text layer was searched case-insensitively for `future work`, `further research`, `more research`, `we plan`, `we will`, `next step`, `open question`, `leave for`, `yet to`, `remains`, `would be (valuable|useful|interesting)`. **No match.** The forward-looking and conjectural material is limited to the five passages quoted in `## Open questions, conjectures and promised follow-ups (verbatim)`, found by searching for `future|further|anticipat|didn't|worth|might|perhaps|likely|possibly|could|would|we believe|we think|we attribute` and reading every hit.

**Date discrepancy, recorded not resolved.** The appendix's title page says "March 2026"; its Corrections page says "Mar 19, 2026"; the CDN says `last-modified` 19 March 2026; the feature page's own BibTeX block says `date = {2026-03-18}`; `wiki/INDEX.md` row 39 dates the feature 2026-03-19. The Corrections section implies an earlier build of this PDF existed before 19 March 2026; no URL for it was found, and the superseded sentence is not reproduced in the current file.

**Not attempted.** The parent feature page's claims, figures and quotes (covered by `survey-81k-interviews-2026-03`); the Anthropic Interviewer post the Methods section delegates to (`anthropic-interviewer-2025-12`); the Clio paper the clustering and classifier links point to (`clio-insights-2024-12`); the September 2025 report whose 36% the representativeness check uses (`economic-index-2025-09-report`); and the 15-page `survey-81k-economics-2026-04` PDF built on the same 80,508 interviews. Each belongs to another wiki entry. The 36% was not re-verified against the September 2025 report here; it is recorded as the appendix quotes it, and the report's own wiki entry governs.
