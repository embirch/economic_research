# What 81,000 people told us about the economics of AI

## Source

- **Slug:** `survey-81k-economics-2026-04`
- **Title:** "What 81,000 people told us about the economics of AI"
- **Type:** survey (the write-up of the economics variables derived from the 81k interview study). The document calls itself "this report" (PDF p.3: "Throughout this report, we use Claude-powered classifiers") while its own acknowledgements call it a blog post (PDF p.12: "Maxim Massenkoff led the analysis and wrote the blog post"). The page files it under the category label **Economic Research**.
- **Authors:** Maxim Massenkoff and Saffron Huang (PDF p.1; citation block, PDF p.12)
- **Published:** 22 April 2026 (PDF p.1: "Published April 22, 2026"; page dateline "Apr 22, 2026"; PDF CreationDate 2026-04-22 16:42:32 UTC)
- **Corrections:** none. The page carries no Corrections block.
- **Primary URL:** https://www.anthropic.com/research/81k-economics
- **PDF:** https://cdn.sanity.io/files/4zrzovbb/website/3a8d990bc90098038eabd77b0d12ff636ed58d50.pdf (15 pp: p.1 cover, p.2 key findings and introduction, pp.3–11 body, p.12 citation and acknowledgements, p.13 footnotes, pp.14–15 appendix)
- **Separate appendix:** no separate document of its own. The appendix is **pp.14–15 of this PDF**, and the page's Appendix section reads only "See the final section of the linked PDF." The appendix is therefore covered here, not in a sibling file. But it in turn defers the sample, method and limitations to the companion Institute study (PDF p.14, quoted in full under `Definitions`), which is **not** summarised here: see `wiki/reports/survey-81k-interviews-2026-03.md` (slug `survey-81k-interviews-2026-03`) and `wiki/reports/survey-81k-interviews-2026-03-appendix.md`. Wherever this file records that the sample, weighting, survey instrument or consent rules are "deferred to the companion study", the content is deliberately left to those two files.
- **Data availability:** **none stated.** The document contains no data-availability sentence, no filename, no repository link and no mention of Hugging Face — in contrast to the paper it builds on, which does carry one. Whether any released file carries the classifier variables used here is not established by this document; it is a question for the data steward.
- **Bibtex key:** `massenkoff2026interviewer` (PDF p.12) — note the key says *interviewer*, not *economics*, while `title` is this document's title. Any citation must be read from the block, not guessed from the slug.
- **Acknowledgements (PDF p.12):** "We thank the 80,508 Claude users who shared their stories." Division of labour is stated: "Maxim Massenkoff led the analysis and wrote the blog post. Saffron Huang led the interview project and provided guidance throughout." Named for feedback and guidance: Zoe Hitzig, Eva Lyubich (methodological guidance); Peter McCrory, Deep Ganguli, Jack Clark (critical feedback, direction); Theodore Sumers (data processing and clustering infrastructure); Grace Yun, AJ Alt, Thomas Millar (implemented Anthropic Interviewer within Claude.ai); Chelsea Larsson, Jane Leibrock, Matt Gallivan (survey and experience design); Keir Bradwell, Rebecca Hiscott (editorial); Hanah Ho, Kim Withee (design); Miriam Chaum, Ankur Rathi, Santi Ruiz, David Saunders.
- **Mentor relevance:** this is a **first-authored Massenkoff publication**, and it is the only Anthropic document that puts his `observed exposure` measure against a subjective outcome. It is also the document that links the exposure measure to a wage-quartile productivity result.
- **Prior Anthropic work it stands on** (links live on the page; the PDF names no URLs in the body):
  - the Economic Index generally → page links to the March 2026 report (`economic-index-2026-03-report`);
  - "Our recent survey study with 81,000 Claude users provides a way to connect people's economic concerns with what we've quantified in Claude traffic." (PDF p.2), hyperlinked on the page at "survey study with 81,000 Claude users" → https://www.anthropic.com/features/81k-interviews (`survey-81k-interviews-2026-03`);
  - "observed exposure (our measure of AI displacement risk)" → https://www.anthropic.com/research/labor-market-impacts (`labor-market-impacts-2026-03`), linked twice;
  - "tentative signs of a slowdown in the hiring of recent graduates and early-career workers" → https://cdn.sanity.io/files/4zrzovbb/website/a42bc3fc08283562f08fd8bdee8f6f9a3d506e87.pdf, which is the **earlier PDF URL of the same Massenkoff–McCrory paper** (recorded as an alternative URL in `wiki/reports/labor-market-impacts-2026-03.md`), not a third document;
  - "a previous Economic Index finding" → https://www-cdn.anthropic.com/096d94c1a91c6480806d8f24b2344c7e2a4bc666.pdf, which is **"The Anthropic Economic Index report: Economic Primitives", published January 15, 2026** (identified by fetching its first pages; slug `economic-index-2026-01-report`). Not summarised here.
- **Non-Anthropic prior work:** none. The document has **no reference list and cites no external literature** — the only named citation is to Massenkoff and McCrory (2026), in the Figure 1 caption. BLS occupational median wages are used (Figure 3 caption) but not cited to a source document.
- **Terms it introduces into the Anthropic vocabulary:** perceived job threat (also "perceived threat from AI", "job threat"); inferred productivity gain / inferred productivity benefit (the 1–7 scale); inferred speedup; productivity type as scope / speed / quality / cost; career stage (the five-label ladder plus `unclear`); "where does the surplus from AI productivity go"; "solopreneurs"; "qualitative data can surface quantitative hypotheses".

### Differences between the page and the PDF (recorded because quotations must be reproducible)

| Location | PDF | Page |
|---|---|---|
| Key findings (p.2) | three plain bullets | the same three bullets, rendered in italics |
| p.3, quote attribution | "­— Software engineer 1" (a soft hyphen precedes the em dash; footnote marker after a space) | "—Software engineer.1" (a full stop before the footnote marker) |
| Figure 6 caption | "…already happening or likely in the near term by the level of inferred speedup." | "…already happening or likely in the near term, by the level of inferred speedup." (comma added) |
| Appendix section | p.14 begins "See "What 81,000 people want from AI" and its accompanying appendix…" and pp.14–15 give the occupation-inference detail and two full prompts | "See the final section of the linked PDF." The page reproduces **neither** the appendix text nor the prompts |
| Body links | no URLs in the body | seven hyperlinks (listed above) |
| Meta description (page only) | — | "Anthropic's recent survey of 81,000 Claude users provides a way to connect people's economic concerns with what we've quantified in Claude traffic." |

Page references below are **the PDF's**. Body wording is otherwise identical between the two renderings, sentence for sentence; the four differences above are the only ones found.

**Alt text.** Per `room/director-2026-09-16-alt-text-ruling.md`: all six figures on the page are images with **empty alt attributes** (only the hero image carries alt text, and it is the title). No number in this publication exists only in alt text, and none is recorded from a chart image. The bold sentence(s) beneath each figure are the caption and are quoted below.

## Claims

Numbers are reproduced as published. Each claim names the comparison it rests on. Two things to hold throughout: the denominator shifts between claims (all respondents · those with an inferred occupation · those who mentioned productivity · those who named a beneficiary), and every variable on both sides of every comparison except observed exposure and the BLS wage is a **Claude classifier output**, not a survey answer.

1. **The headline pairing: perceived threat rises with observed exposure.** "Our recent survey of 81,000 Claude users shows that people who work in roles that are more exposed to AI have more concerns about AI-driven job displacement. These concerns are also higher among early-career respondents." (key findings, PDF p.2). *Comparison:* occupation-level perceived job threat against the Massenkoff–McCrory observed exposure measure for the same occupation.

2. **The slope: +1.3pp per +10pp exposure.** "For every 10-percentage-point increase in exposure, perceived job threat increased by 1.3 percentage points." (PDF p.3, Figure 1). *Comparison:* a simple linear fit through occupations, y = share of that occupation's respondents indicating job threat, x = observed exposure ("The green line shows a simple linear fit", Figure 1 caption). No standard error, no N, no weighting stated.

3. **The ratio: three times as often at the top of the exposure distribution.** "People in the top 25% of exposure mentioned the worry three times as often as those in the bottom 25%." (PDF p.3, Figure 1). *Comparison:* top exposure quartile against bottom exposure quartile. The base rates behind the ratio are not given in the text.

4. **One fifth of respondents voiced the concern at all.** "One fifth of the respondents in our survey voiced concern about economic displacement." (PDF p.3). *Comparison:* the level, on all respondents; this is the only unconditional share of concern in the document, and the denominator for it is the full sample, not the 39% with occupation labels.

5. **The illustration of the gradient, by occupation.** "Elementary school teachers were less worried about their own displacement than software engineers, for example, consistent with the fact that Claude usage skews toward coding tasks." (PDF p.3). *Comparison:* two named occupations, with Claude's coding skew as the mechanism. The only occupations named on the Figure 1 scatter in the text; the rest of the points are legible only in the image.

6. **Early-career respondents worry more.** "We found that early-career respondents were much more likely to express concern about job displacement than senior workers." (PDF p.4, Figure 2). *Comparison:* career-stage groups against each other, on the same job-threat classifier. **No number appears in the text**; the levels exist only in the Figure 2 image. The coverage of the variable is stated: "For about half of respondents in this survey, we were able to infer career stage from their answers." (PDF p.4).

7. **Mean inferred productivity: 5.1 of 7.** "Overall, people reported meaningful productivity gains on average. The mean productivity rating was 5.1, corresponding to "substantially more productive."" (PDF p.5). *Comparison:* the mean against the scale's own labels (footnote 3 gives all seven).

8. **The negative and missing tails.** "Some 3% reported negative or neutral impacts, and 42% did not give a clear indication on productivity." (PDF pp.5–6 — the sentence straddles the page break). *Comparison:* shares of all respondents across classifier outcomes. This 42% is the missingness that every later productivity share is conditional on.

9. **Productivity gains by wage quartile — the U across pay.** "Those in the highest- and lowest-paid occupations report the largest productivity gains, most commonly from increases in scope (doing new tasks)." (key findings, PDF p.2), with the body: "This splits somewhat across income lines. The left panel in Figure 3 shows that people in high-paying jobs, like software developers, conveyed the largest productivity gains from AI." (PDF p.6) and "Some of the lowest-paid workers describe high productivity gains as well." (PDF p.6). *Comparison:* mean inferred productivity benefit by **quartile of occupational median wage from the BLS** (Figure 3 caption, left panel). Quartile means and confidence intervals exist only in the image.

10. **The wage-quartile result is not just coding.** "This result is not driven only by coding; it holds when we leave out computer and math occupations." (PDF p.6). *Comparison:* the same left-panel gradient with the computer-and-math major group dropped. Asserted; no numbers reported.

11. **It echoes an Economic Index result that also favoured higher-paid workers.** "It echoes a previous Economic Index finding that also favored higher-paid workers: in tasks requiring greater levels of education, Claude tended to reduce the time taken to complete a task (relative to doing it without AI) by a higher percentage." (PDF p.6). *Comparison:* this report's self-reported productivity gradient against the January 2026 Economic Index report's time-savings-by-education gradient. Cross-reference only: see `wiki/reports/economic-index-2026-01-report.md`.

12. **By major occupational group: management first, science and law last.** "At the top are management occupations. These respondents are mostly entrepreneurs using Claude to build a business.4 The next highest category is computer and math, which includes software developers. The two groups exhibiting the mildest productivity improvements were workers in scientific and legal professions." (PDF p.7, Figure 3 right panel). *Comparison:* mean inferred productivity benefit across major occupational groups. Footnote 4 adds the robustness: "Removing these "solopreneurs" still leaves management tied with computer and math occupations for showing the highest productivity benefit." (PDF p.13).

13. **Who gets the surplus: mostly the respondent.** "Respondents indicated the recipient of these gains in about a quarter of interviews. Overall, most of these people cited benefits to themselves, through faster tasks, expanded scope, and freed-up time.5 But 10% of respondents who named a recipient said that employers or clients were asking for and getting more work. A smaller share mentioned benefits to AI companies, and an even smaller share said that AI would be a net negative." (PDF p.7; Figure 4 and its caption are on p.8). *Comparison:* shares of the ~quarter who named a beneficiary, across destinations (self · employers or clients · AI companies · net negative). Only the 10% is quantified in the text; the remaining shares are ordinal in the text and numeric only in the image.

14. **The surplus split by career stage.** "This depended on career stage: only 60% of early-career workers indicated that they personally benefited from AI, compared to 80% of senior professionals." (PDF p.7). *Comparison:* early-career against senior, within those who named a beneficiary. This is the second career-stage result and the only one with numbers.

15. **Scope beats speed as the kind of gain.** "We find that the most common productivity enhancement is in scope, which was cited by 48% of users who explicitly mentioned productivity effects. 40% of users who mentioned productivity emphasized speed." (PDF p.8, Figure 5). *Comparison:* the four productivity types against one another, on the base of users who mentioned productivity effects. Quality and cost shares are not stated in the text.

16. **Speedup and fear are U-shaped.** "Respondents experiencing the largest speedups from AI express higher concern about job displacement." (key findings, PDF p.2) and "We found that the relationship between speedup and perceived job threat is U-shaped (see Figure 6). The leftmost bar shows respondents who reported that AI slowed them down. These respondents were more likely to indicate that AI posed a significant threat to their livelihoods." (PDF p.9), then "For the remaining respondents, perceived job threat increases consistently with the level of speedup implied by their answers." (PDF p.10). *Comparison:* the job-threat share across bins of the inferred 1–7 speedup scale. No bar heights, Ns or intervals in the text; the shape is the claim.

17. **The mechanism offered for the rising arm, as reasoning not evidence.** "This makes some economic sense: if the time required to do one's tasks is shrinking quickly, there may be more uncertainty about the future viability of the role." (PDF p.10). *Comparison:* none; this is interpretation.

18. **The mechanism offered for the left-hand bar, from quotes.** "For example, some creative workers, like fine artists and writers, found AI too stifling and rigid to help them at their own work. At the same time, they feared the diffusion of AI into creative fields would make it harder for them to find work." (PDF p.9). *Comparison:* qualitative, within the slowed-down group.

19. **The synthesis claim: intuitions track the usage data.** "The responses explored here show that people's intuitions track the usage data: they worry most about AI's effect in the jobs where we observe Claude doing the most work. We also find higher levels of economic anxiety among early-career workers, which aligns with past research." (PDF p.11, Discussion). *Comparison:* the survey's subjective measures against the Economic Index's observed usage; and the career-stage gradient against the earlier hiring-slowdown result.

20. **The empowerment claim.** "There are also signs that Claude empowers its users. People are most likely to talk about benefits flowing to themselves rather than to employers or AI companies. High-wage workers were the most enthusiastic about the productivity impacts of AI, but people with low-wage jobs and lower levels of education also reported large productivity gains." (PDF p.11, Discussion). *Comparison:* high-wage against low-wage and low-education respondents. **Note:** education appears in no figure caption and no other sentence in the document; the "lower levels of education" half of this claim has no supporting number anywhere in the fetched text.

21. **Coverage of the occupation variable (appendix).** "Throughout, we inferred people's jobs from their responses, although we instructed Claude to leave this missing if it was unclear, which was the case for 61% of respondents. The remaining 39% have occupation labels. For about 11% of all respondents, an occupation was explicitly mentioned" (PDF p.14), and "For the remaining 28%, we inferred occupation from other clues in the responses." (PDF p.14). *Comparison:* shares of all respondents by how the occupation label was obtained — 61% missing, 11% explicit, 28% inferred from clues.

22. **The one robustness check reported (appendix).** "As a robustness check, we confirmed that we got the same qualitative results as in Figures 1 and 3 when we use only the 11% who had explicitly reported their line of work in their response." (PDF p.14). *Comparison:* the full 39% with occupation labels against the 11% who stated their occupation outright. Stated qualitatively; no coefficients.

23. **Respondent count, as acknowledged.** "We thank the 80,508 Claude users who shared their stories." (PDF p.12), against the title's and key findings' "81,000 Claude users" (PDF pp.1–2). *Comparison:* the exact count against the rounded one. 80,508 is the only precise sample count in the document; no analysis N is given for any figure.

## Definitions (verbatim)

All quotations are the document's own words. Every construct below except observed exposure and the BLS wage quartile is produced by a Claude classifier run over interview transcripts.

**The classifier method in general (PDF p.3):**
> "Throughout this report, we use Claude-powered classifiers to infer people's attributes and sentiments from their responses. For example, many participants mention their line of work in passing or give informative details about their work life, which allows us to infer their occupation. Similarly, we quantify concerns about job loss by prompting Claude to identify and interpret direct quotes in which respondents indicate that their own role is at risk of AI-driven displacement. We give example prompts in the Appendix."

**What the added variables are, relative to the companion study (PDF p.14, the appendix's opening):**
> "See "What 81,000 people want from AI" and its accompanying appendix for more details on the sample, survey methodology, and limitations. This study uses the same data, but adds additional variables using Claude-powered classifiers."

**Perceived job threat — the coding rule (Figure 1 caption, PDF p.4):**
> "A respondent was coded as indicating job threat if they said their role was already being replaced or substantially reduced, or that such changes were likely in the near term (coded using Claude)."

**Perceived job threat — the y-axis, stated in the body (PDF p.3):**
> "The y-axis is the percentage of respondents in a given occupation who said that AI is already replacing their role or is likely to do so soon."

**Perceived job threat — the Figure 6 restatement (Figure 6 caption, PDF p.10):**
> "Percentage of respondents who said that displacement at their own job was already happening or likely in the near term by the level of inferred speedup."

(The page inserts a comma before "by the level".)

**Observed exposure — as glossed in this document (PDF p.3):**
> "Respondents' perceived threat from AI was correlated with our own measure of observed exposure, which reflects the percentage of a job's tasks for which Claude is used."

**Observed exposure — as introduced (PDF p.2):**
> "The survey's results provide initial evidence that observed exposure (our measure of AI displacement risk) is correlated with economic concern around AI. People in highly exposed occupations—as defined by the tasks Claude is observed performing—were more nervous about economic displacement."

**Observed exposure — the source named (Figure 1 caption, PDF p.4):**
> "Percentage of respondents indicating some job threat from AI vs. the Observed Exposure measure from Massenkoff and McCrory (2026)."

*Construct note (the wiki author's, not the document's):* this document's gloss — "the percentage of a job's tasks for which Claude is used" — drops two components of the measure as defined in its source, namely the Eloundou β feasibility gate and the weighting that gives "fully automated implementations … full weight, while augmentative use receives half weight" (see `wiki/reports/labor-market-impacts-2026-03.md`). The document also states no **vintage** of the measure, no file, and no crosswalk from its inferred occupations onto the measure's occupation codes. Anything built on this pairing must go back to the source definition.

**Occupation — how it is inferred (footnote 1, PDF p.13):**
> "We inferred people's occupations using the first question in the survey ("What's the last thing you used an AI chatbot for?") or indications given in other responses."

**Occupation — the missingness rule and the two routes (appendix, PDF p.14):**
> "Throughout, we inferred people's jobs from their responses, although we instructed Claude to leave this missing if it was unclear, which was the case for 61% of respondents. The remaining 39% have occupation labels. For about 11% of all respondents, an occupation was explicitly mentioned:"

> "For the remaining 28%, we inferred occupation from other clues in the responses. For example, one respondent who was labeled a physician reported that they wanted AI to improve "my interactions with patients." Some of these inferences will be wrong. As a robustness check, we confirmed that we got the same qualitative results as in Figures 1 and 3 when we use only the 11% who had explicitly reported their line of work in their response."

**Career stage — the figure's construct (Figure 2 caption, PDF p.5):**
> "Percentage of respondents indicating some job threat from AI, by career stage. Both fields are inferred from free-form responses using Claude-powered classifiers."

**Career stage — the coverage and the signals used (PDF p.4 and footnote 2, PDF p.13):**
> "For about half of respondents in this survey, we were able to infer career stage from their answers.2"

> "This came from various indications in the written responses. For example, several users mentioned using Claude for homework, which put them in the early-career group. And many referred to running their own businesses and being involved in hiring decisions, which put them in the senior group."

**Career stage — the classifier prompt in full (appendix, PDF p.15):**
> "The content above is the full transcript of a research interview about AI. The lines marked "User:" are the respondent's own words.
>
> What career stage is the respondent at? Use any signal you can find — job title, years of experience they mention, whether they manage people, how they describe their role.
>
> - student_or_entry: student, intern, very first job, or just entering the workforce
> - junior: early-career, roughly under three years in
> - mid: mid-career individual contributor — experienced, not managing
> - senior_or_lead: senior individual contributor, tech lead, team lead, or similar
> - executive: founder, C-level, VP, director, or runs their own business
> - unclear: not enough signal to place them
>
> Return exactly one label, lowercase, with no other text."

(The document does not say how the six labels collapse into the "early-career" and "senior" groups used in Figure 2 and in claim 14, nor which label the Figure 2 axis carries.)

**Inferred productivity gain — the scale as described in the body (PDF p.5):**
> "Using Claude to assess the survey responses, we rated the extent of people's self-reported productivity gains from AI on a 1–7 scale, where 1 is "less productive," 2 is "no change," and each subsequent level denotes a larger gain. Responses that scored 7 included testimonials like, "It used to take months to make the website I [made] in 4-5 days"; Claude gave a 5 to statements like, "What might have taken four hours was accomplished in half the time," and a 2 to ones like, "Personally, I had AI help me fix code on a website. But it took multiple passes to get the result I was after."3"

**Inferred productivity gain — the full scale and why it is not centred (footnote 3, PDF p.13):**
> "The scale is not centered because most people say positive things about productivity, yielding almost entirely 6s and 7s on the original Likert scale. The scale we use here ran from 1 = less productive, 2 = no change, 3 = slightly more productive, 4 = moderately more productive, 5 = substantially more productive, 6 = much more productive, to 7 = transformatively more productive—AI has fundamentally changed what or how much they can produce."

**Inferred productivity gain — the figure's construction and the wage variable (Figure 3 caption, PDF p.6):**
> "The left panel shows the mean inferred productivity benefit from AI (inferred using a Claude-powered classifier) by quartile of occupational median wage from the BLS. The right panel shows the same outcome, split by major occupational group. Error bars show 95% confidence intervals."

**Type of productivity gain — the four categories as described in the body (PDF p.8):**
> "Respondents also shared where they experienced gains in productivity. We separate this into scope, speed, quality, and cost. For example, many people using AI for coding tasks said things like, "I'm a non tech guy but now I'm a full stack developer." This is an expansion of scope; AI unlocks new abilities for them. In contrast, some users sped up tasks they were already doing, like the accountant who said, "I built a tool that helps me finish a financing task in 15 minutes that used to take 2 hours." Quality gains often came from more thorough checks of code, contracts, and other paperwork. And a small share of respondents mentioned the low cost of using AI: "[I]f I hire a social media manager it's over my budget.""

**Type of productivity gain — the classifier prompt in full (appendix, PDF p.15):**
> "To measure the nature of productivity gains, we used the following prompt along with each individual interview transcript:
>
> The content above is the full transcript of a research interview about AI. The lines marked "User:" are the respondent's own words.
>
> Along which dimension does this respondent say AI improves their work? If they mention several, pick the one they lean on most. If they claim no productivity gain at all, use not_discussed.
> - speed: faster at what they already do — saves time, quicker turnaround
> - quality: better output — fewer errors, higher polish, more thorough
> - scope: doing things they COULDN'T do before — new capabilities, tasks that were previously out of reach
> - cost: replacing a paid input — not hiring someone, dropping a vendor, avoiding an expense
> - not_discussed: no productivity gain described
>
> Return exactly one label, lowercase, with no other text."

(Note that the type classifier is forced-choice and single-label — "pick the one they lean on most … Return exactly one label" — so the 48% / 40% shares in claim 15 are shares of a dominant-dimension label, not of mentions.)

**Type of productivity gain — the figure's base (Figure 5 caption, PDF p.9):**
> "Share of respondents describing each type of productivity benefit."

(The caption says "respondents"; the body says "users who explicitly mentioned productivity effects" and "users who mentioned productivity" (PDF p.8). The two bases are not reconciled in the document.)

**Inferred speedup — the coding (PDF p.9):**
> "People's experience with Claude might also shape their concerns about AI. To assess this, we measured the speedup reported by respondents, by extracting whether their work was now much slower (which we coded as 1), showed no change in speed (4), or had become much faster (7)."

(Only the three anchors 1, 4 and 7 are defined. No prompt for this classifier is given in the appendix — the appendix supplies prompts for productivity type and career stage only.)

**Destination of the surplus — the question and the base (PDF p.7 and Figure 4 caption, PDF p.8):**
> "A key question as AI diffuses through the economy is where the benefits will accrue—to workers, their managers, consumers, or corporations. Respondents indicated the recipient of these gains in about a quarter of interviews."

> "Among respondents who named a beneficiary of their AI productivity gains, the share identifying each destination."

**Sample — the only statement of who is in it (PDF p.11):**
> "First, our survey is limited to users of personal accounts on Claude.ai who chose to respond."

**Sample — size, as titled and as acknowledged (PDF pp.2, 12):**
> "Our recent survey of 81,000 Claude users shows that people who work in roles that are more exposed to AI have more concerns about AI-driven job displacement."

> "We thank the 80,508 Claude users who shared their stories."

**Sample — the exclusion that bears on the surplus result (footnote 5, PDF p.13):**
> "A major caveat, however, is that this survey went out to people with personal Claude accounts. A more representative picture would also include enterprise users, who may be more likely to say the value accrues to their employers."

**Weighting rules:** **none.** The document contains no statement of survey weights, no population benchmark, no non-response adjustment and no mention of stratification. The word "weighted" does not appear; the only aggregation rules stated are the figure bases quoted above. The sample, survey methodology and limitations are expressly deferred to the companion study (PDF p.14, quoted above), so any weighting rule that exists must be read from `survey-81k-interviews-2026-03` and its appendix, not from this document.

**The survey instrument:** only one question is quoted anywhere — "What's the last thing you used an AI chatbot for?" (footnote 1, PDF p.13) — described as "the first question in the survey". The document also characterises the instrument twice: "The survey asked people about their visions and fears around advances in AI" (PDF p.2) and "because the survey is open-ended, our measures are based on what respondents happen to mention" (PDF p.11). The full instrument is in the companion study.

## Data and methods

In the wiki author's words, with page references.

**One dataset, re-coded.** The document is not a new survey. It is a second pass over the 81k interview corpus: "This study uses the same data, but adds additional variables using Claude-powered classifiers" (PDF p.14). Sample construction, recruitment, consent, language coverage and the instrument all belong to the companion Institute study and its appendix and are left to those wiki files. What is new here is the variable layer and the linkage to the exposure measure.

**The interviews.** 81,000 Claude users (PDF p.2), 80,508 in the acknowledgements (PDF p.12), all on **personal Claude.ai accounts**, self-selected into responding (PDF p.11). Free-form, open-ended answers; respondents were not asked about occupation, career stage, productivity or displacement directly (PDF p.11).

**The classifier pipeline.** Claude is run over each full interview transcript to produce, per respondent: an occupation label (or missing), a career stage on a six-label ladder, a productivity-gain rating 1–7, a single dominant productivity-type label out of scope/speed/quality/cost/not_discussed, an inferred speedup 1–7, a binary job-threat indicator, and a beneficiary-of-the-gains label. Two of the seven prompts are published in full (productivity type, career stage; PDF p.15); the others are described in prose only. Each prompt is single-label, lowercase, no free text — i.e. the outputs are hard labels, not probabilities, so no confidence or uncertainty from the classifier enters any figure. The job-threat construct is described as "prompting Claude to identify and interpret direct quotes in which respondents indicate that their own role is at risk of AI-driven displacement" (PDF p.3).

**Coverage of each derived variable, where stated.** Occupation: 39% labelled (11% explicit, 28% inferred from clues), 61% missing by instruction (PDF p.14). Career stage: "about half" (PDF p.4). Productivity rating: 42% "did not give a clear indication", 3% negative or neutral (PDF p.5). Beneficiary: "about a quarter of interviews" (PDF p.7). Job threat: one fifth voiced the concern (PDF p.3), with no statement of how many were classifiable either way. No figure reports its own N.

**Linkage to the labour-market exposure measure.** Respondents' inferred occupations are matched to the `observed exposure` measure of Massenkoff and McCrory (2026) (Figure 1 caption, PDF p.4), and Figure 1 plots, per occupation, the share of that occupation's respondents coded as indicating job threat against that occupation's exposure, with "a simple linear fit" through the points (Figure 1 caption). The document reports the fitted slope (1.3pp per 10pp) and a top-versus-bottom-quartile ratio (3×). It does **not** state the occupational classification used, the vintage of the exposure measure, the crosswalk, the number of occupations plotted, whether points are weighted by respondent counts, how the zero-exposure occupations enter, or any standard error. Exposure quartiles in claim 3 are quartiles of exposure; wage quartiles in claim 9 are "quartile of occupational median wage from the BLS" (Figure 3 caption) — two different quartile variables, and their relationship is not shown.

**Estimators.** Three, all descriptive: (i) a simple unweighted-looking linear fit across occupations for Figure 1, reported as a slope; (ii) group means with 95% confidence intervals for Figure 3 (the only figure whose caption mentions intervals); (iii) group shares for Figures 2, 4, 5 and 6, reported without intervals. No regression table, no controls, no fixed effects, no hypothesis test, no multiple-comparison adjustment and no formal test of the U-shape appear anywhere. The one sensitivity check is the restriction to the 11% explicit-occupation subset, reported as giving "the same qualitative results as in Figures 1 and 3" (PDF p.14); the one composition check is dropping computer-and-math occupations (PDF p.6) and dropping "solopreneurs" from management (footnote 4, PDF p.13). Both are asserted without numbers.

**Released data.** None named. There is no data-availability statement, no filename and no repository reference in the document. The `observed exposure` input is released with its source paper (task- and job-level coverage on the Economic Index dataset), but this document does not say which file or column it used, and the transcripts and classifier labels behind every other variable here are not mentioned as released. **Column-level facts are the data steward's to establish**; a brief that builds on this report needs the steward to confirm (a) which released file carries job-level observed exposure and on which occupation coding, and (b) whether any release carries interview-level or occupation-level survey variables at all. Nothing in this file may be treated as evidence that either exists.

## Limitations (verbatim)

**The three caveats stated together (PDF p.11, Discussion):**
> "There are key caveats to our analysis, owing to the nature of the data. First, our survey is limited to users of personal accounts on Claude.ai who chose to respond. Among other potential biases, these users could be more likely to perceive the benefits as flowing to themselves. Second, the users weren't asked directly about many of the derived variables here, so our inferences on occupation, career stage, and other variables from contextual clues could be wrong. Relatedly, because the survey is open-ended, our measures are based on what respondents happen to mention; these findings should be confirmed in structured surveys that ask about these topics directly."

**On selection into reporting productivity benefits (PDF p.5):**
> "Our respondents were, of course, active Claude users who were willing to take a survey. This could make them more likely to report productivity benefits than the average user."

**On the scale being uncentred (footnote 3, PDF p.13):**
> "The scale is not centered because most people say positive things about productivity, yielding almost entirely 6s and 7s on the original Likert scale."

**On missing productivity information (PDF p.5):**
> "Some 3% reported negative or neutral impacts, and 42% did not give a clear indication on productivity."

**On the occupation labels being wrong in part (appendix, PDF p.14):**
> "Some of these inferences will be wrong."

**On the exclusion of enterprise users, at the point where it bites (footnote 5, PDF p.13):**
> "A major caveat, however, is that this survey went out to people with personal Claude accounts. A more representative picture would also include enterprise users, who may be more likely to say the value accrues to their employers."

**On the strength of the evidence claimed for the headline relationship (PDF p.2):**
> "The survey's results provide initial evidence that observed exposure (our measure of AI displacement risk) is correlated with economic concern around AI."

**On how the wage-quartile result should be read (PDF p.6):**
> "This splits somewhat across income lines."

**On what the whole exercise is for (PDF p.11):**
> "Still, the interviews surface real insights about people's feelings around the economics of AI, showing how qualitative data can surface quantitative hypotheses."

## Open questions, conjectures and promised follow-ups (verbatim)

**The explicit call for structured replication — the document's main promised follow-up (PDF p.11):**
> "Relatedly, because the survey is open-ended, our measures are based on what respondents happen to mention; these findings should be confirmed in structured surveys that ask about these topics directly."

**The standing open question the document poses and answers only partly (PDF p.7):**
> "A key question as AI diffuses through the economy is where the benefits will accrue—to workers, their managers, consumers, or corporations."

**The stated gap this document exists to close (PDF p.2):**
> "To date, however, we've lacked information on how these usage patterns map onto people's thoughts and impressions of AI."

**Conjecture about why awareness tracks exposure (PDF p.2):**
> "This is consistent with people being broadly aware of AI's diffusion and potential impacts."

**Conjecture offered for the rising arm of the U (PDF p.10):**
> "This makes some economic sense: if the time required to do one's tasks is shrinking quickly, there may be more uncertainty about the future viability of the role."

**Conjecture about what shapes concern (PDF p.9):**
> "People's experience with Claude might also shape their concerns about AI."

**Claimed methodological lesson, put forward as a programme (PDF p.11):**
> "showing how qualitative data can surface quantitative hypotheses"

**The residual claim left standing without a test (PDF p.11):**
> "And the large share of economic-related concerns is a strong signal in itself."

**Named, unexplained heterogeneity — the creative-work case (PDF p.9):**
> "For example, some creative workers, like fine artists and writers, found AI too stifling and rigid to help them at their own work. At the same time, they feared the diffusion of AI into creative fields would make it harder for them to find work."

**Named, unexplained heterogeneity — the legal case (PDF p.7):**
> "Some lawyers worried about AI's ability to follow precise instructions."

**Named, unexamined mechanism — AI imposed by employers (PDF p.2):**
> "In some cases, AI has enabled them to start businesses, or given them time for more important things; in others, AI feels stifling, or imposed on them by their employers."

**Named, unexamined mechanism — work intensification (PDF p.3):**
> "In some jobs, people felt it made their work harder. One software developer observed that "when AI arrived, the project managers started giving harder and harder tickets and bugs to solve.""

**Named, unexamined mechanism — junior positions specifically (PDF p.3):**
> "one software developer cautioned about "the possibility of AI in its current state being used to replace junior positions.""

**The one deferral to other documents (appendix, PDF p.14):**
> "See "What 81,000 people want from AI" and its accompanying appendix for more details on the sample, survey methodology, and limitations."

## What it did not test

The wiki author's inference, not the document's claims. Each item is something its own text leaves open, and each is a candidate opening rather than a criticism of a blog-length report.

1. **Whether perceived threat is *warranted*.** This is the largest gap, and it is invisible inside the document. The same exposure measure, in the paper this report builds on, produced **no detectable differential rise in unemployment** for exposed workers and a ~1pp detectability floor (see `wiki/reports/labor-market-impacts-2026-03.md`). Here, workers in those same exposed occupations are three times as likely to fear displacement. Nothing in this document confronts the pairing: fear is never compared with any realised labour-market outcome. The word "unemployment" does not appear in the document at all; "hiring" appears three times, only once about the labour market (the reference to the earlier hiring-slowdown result, PDF p.4) and otherwise as a career-stage signal (footnote 2) and as a productivity-classifier label (PDF p.15).
2. **Any individual-level estimate.** The text asserts a respondent-level relationship — "A respondent was more concerned about AI when our observed exposure measure for that respondent was higher" (PDF p.3) — but the reported evidence (Figure 1, its slope and its quartile ratio) is occupation-level. No individual-level regression, no clustering, no controls (not even for career stage, which is the document's other main covariate), and no statement of how many occupations the fit runs over.
3. **Precision of anything.** Only Figure 3 has confidence intervals. The 1.3pp slope, the 3× ratio, the one-fifth share, the 48/40 split, the 60%-vs-80% gap and the U-shape are all reported without an interval, an N or a test. There is no power statement anywhere, which matters most for the U-shape's left-hand bar (respondents who reported being slowed down are, by the document's own account of the scale, a small group).
4. **Classifier validity.** Seven constructs are classifier outputs and none is validated against human coding. There is no gold-standard subsample, no inter-rater or inter-model agreement, no measured false-positive rate on job threat, no sensitivity to prompt wording, and no statement of which Claude model ran the classifiers or when. The only check offered is a subsample restriction (item 5), which tests occupation *coverage*, not classifier *accuracy*.
5. **Whether missingness is informative, anywhere.** 61% have no occupation, ~50% no career stage, 42% no productivity indication, ~75% no beneficiary. Every result conditions on the classifiable, and no result is reported both ways. Silence could plausibly mean "no gain" or "not a worker"; the 11%-subset check (PDF p.14) speaks to the occupation variable alone, qualitatively, with no numbers, and says nothing about the other three.
6. **Whether the wage-quartile U is about work at all.** The lowest-paid quartile's gains are illustrated by a delivery driver building an e-commerce business and a landscaper building a music application (PDF p.6). Those are new ventures and side projects, not productivity in the current job — and the productivity classifier's `scope` label ("doing things they COULDN'T do before") will capture exactly that. Work and non-work use are never separated, even though the Economic Index has a not-work/work distinction available. The document's own framing of management as "mostly entrepreneurs" (PDF p.7) is the same phenomenon at the top of the wage distribution.
7. **Any objective anchor on productivity.** The measure is Claude's reading of what a respondent said about their own productivity, on an uncentred scale. It is never benchmarked against a measured time saving, a task duration, an output count, or the Economic Index's own primitives — even though the document invokes one of those Index findings as an echo (claim 11). Whether self-reported gains and measured gains order occupations the same way is untested.
8. **The education claim.** "people with … lower levels of education also reported large productivity gains" (PDF p.11) rests on no reported number, figure or classifier described anywhere in the document. Education appears exactly twice in the whole text: here, as a property of respondents, and in claim 11, as a property of *tasks* in the January 2026 Economic Index finding ("in tasks requiring greater levels of education", PDF p.6). No respondent-level education variable is described among the classifier outputs, no figure is split by education, and no number is given — so either such a variable exists and is unreported, or the claim is an inference from the wage quartile.
9. **Composition behind the career-stage results.** Early-career respondents are more fearful (Figure 2) and less likely to say they benefit (60% vs 80%). Neither result is decomposed by occupation or exposure, so the gradient could be a career-stage effect or the fact that early-career respondents are concentrated in exposed, coding-adjacent work. The career-stage classifier itself routes students to "early-career" on signals like using Claude for homework (footnote 2), which mixes students with junior workers in a document about job displacement.
10. **Direction of causation in the speedup–fear relationship.** The document offers a forward mechanism (fast speedups → uncertainty about the role) and, for the left bar, a backward one (fearful creative workers describe AI as unhelpful). Both are narrated from quotes; neither is tested, and nothing distinguishes fear driving the description of speedup from speedup driving the fear.
11. **The collapse of the career-stage ladder.** Six labels are published; two groups ("early-career", "senior") are analysed. The mapping is never stated, so neither Figure 2 nor the 60/80 split is reproducible from the published prompt.
12. **The provenance of the exposure link.** No vintage, file, column, occupational coding or crosswalk is named for `observed exposure`, and the 30% of workers whom that measure assigns zero coverage are not mentioned — although they are the bottom of the x-axis in Figure 1 and, by the source paper's construction, occupations whose tasks fell below a usage gate rather than occupations shown to be safe.
13. **Geography and language.** The companion study spans many countries and languages; every quantitative anchor here is American (BLS median wages, US major occupational groups, the US hiring result). No country, region or language cut is reported, and no statement is made about whether the exposure measure — built on O*NET and US employment — is being applied to non-US respondents.
14. **Enterprise and API users.** Excluded by construction, and named as the caveat that bites precisely on the surplus-destination result (footnote 5). Not tested, not bounded.
15. **Time.** A single wave. No test of whether concern moves as Claude usage arrives in an occupation, no repeat measurement promised, and no link to the Index's monthly or quarterly series.
16. **Every level that lives only in a figure.** Figure 1's occupation points and base rates, Figure 2's career-stage levels, Figure 3's quartile and group means and their intervals, Figure 4's shares other than the 10%, Figure 5's quality and cost shares, and all six of Figure 6's bar heights are images only, with empty alt text. They are not recorded in this file and cannot be quoted.

## Verification

- **Fetched 2026-09-16.**
  - https://www.anthropic.com/research/81k-economics — HTTP 200 via `web_fetch`; full rendered text extracted and read in full, including the three key findings, all six figure captions, the citation block, the acknowledgements, all five footnotes, the Appendix pointer and every body hyperlink.
  - https://cdn.sanity.io/files/4zrzovbb/website/3a8d990bc90098038eabd77b0d12ff636ed58d50.pdf — HTTP 200, 593,780 bytes, 15 pages (`pdfinfo`); text extracted with `pdftotext -layout` (449 lines) and read in full, including footnotes 1–5 (p.13) and the appendix (pp.14–15) with both classifier prompts.
  - https://www-cdn.anthropic.com/096d94c1a91c6480806d8f24b2344c7e2a4bc666.pdf — HTTP 200, 7,263,335 bytes; **first two pages only**, fetched solely to identify the link target of "a previous Economic Index finding". It is "The Anthropic Economic Index report: Economic Primitives", published January 15, 2026, authors Ruth Appel, Maxim Massenkoff, Peter McCrory (lead authors), Miles McCain, Ryan Heller, Tyler Neylon, Alex Tamkin. Not read further and not summarised here; that is `wiki/reports/economic-index-2026-01-report.md`.
- **Fetch method note.** `web_fetch` refuses `cdn.sanity.io` (`url_not_allowed`), a known constraint recorded in the research journal; the PDF was retrieved with `curl` and parsed locally. No `web_fetch` attempt on that host was made, so this is not counted as a failure.
- **Fetch failures:** none.
- **Not fetched, by instruction:** the companion Institute study https://www.anthropic.com/features/81k-interviews and its appendix PDF, to which this document defers the sample, survey methodology and limitations. They are cross-referenced above and left to `survey-81k-interviews-2026-03` and `survey-81k-interviews-2026-03-appendix`. Also not fetched: the March 2026 Economic Index report linked from the first paragraph.
- **Quotation check.** Every block quotation in `Definitions`, `Limitations` and `Open questions`, and every quoted passage in `Claims`, was matched against the extracted PDF text by script — **82 verbatim passages, all 82 matched string-for-string** after normalising whitespace, curly quotation marks, apostrophes, en/em dashes and the soft hyphen, and after reconstructing two classes of text-layer artefact: line-break hyphenation (the PDF renders "AI-driven" as "AI-" + newline + "driven") and the running head "What 81,000 people told us about the economics of AI <n>", which the extraction interleaves between pages. Quotations containing an ellipsis were split and each part matched separately; the only elided quotations are three in the wiki author's own commentary, each marked with "…". Convention: quotations are taken from the **PDF** and page references are always to the PDF. The four page/PDF differences are tabulated in `Source` and, where they touch a quoted passage (the Figure 6 caption's comma, the p.3 attribution, the Appendix section), noted inline at the point of use.
- **Page assignment checked page by page.** Every page reference was set by extracting the PDF one page at a time, not from the continuous text. Two consequences are recorded: the "3% / 42%" sentence straddles the page break and is cited pp.5–6 (claim 8); and each figure's image and caption sit on the page **after** the body text that introduces it, so the Figure 1 caption is p.4 while its lead-in is p.3, the Figure 2 caption is p.5, the Figure 4 caption p.8, the Figure 5 caption p.9 and the Figure 6 caption p.10. Captions are cited where they physically appear.
- **Words checked as absent.** "weight"/"weighted" (0 occurrences — hence the empty weighting rule under `Definitions`), "unemployment" (0), "wages" (0; only "median wage", "low-wage", "high-wage"), "education" (2, both recorded in `What it did not test` item 8).
- **Two appendix prompts** are set with hard line breaks and bullets in the PDF and are reproduced here as single block quotes with the bullets preserved; no wording was altered.
- **Internal discrepancies recorded, not resolved.** (a) 81,000 in the title and key findings against 80,508 in the acknowledgements (PDF pp.1–2 vs p.12). (b) Figure 5's caption base ("Share of respondents") against the body's ("users who explicitly mentioned productivity effects"), PDF p.8. (c) The bibtex key `massenkoff2026interviewer` against this document's title, PDF p.12. (d) The gloss of `observed exposure` here (PDF p.3) against the fuller definition in its source paper, flagged under `Definitions`. None is a misquotation; all four are in the published text.
- **Figures that could not be read.** Figures 1–6 are images in both renderings, all with empty alt attributes on the page. Only numbers stated in body text or captions are recorded; see `What it did not test`, item 16, for the list of what is not available.
- **Data files.** None opened. The programme lead does not open data files (`team/agents/programme-lead.md`, and the standing reminder in `room/director-2026-09-16-alt-text-ruling.md`); the two column-level questions this entry raises are put to the steward in the accompanying room note.
- **Cross-file consistency.** Slug, title, date, type, primary URL and PDF URL match the row for `survey-81k-economics-2026-04` in `wiki/INDEX.md`, including its "(15 pp)" annotation, which the fetched PDF confirms. `wiki/INDEX.md` was not edited in this thread.
