# Introducing the Anthropic Economic Index (2025-02-10)

Slug: `economic-index-2025-02-report`. Wiki file written 2026-09-16 from the live page.

## Source

- **Title.** Rendered page heading: "The Anthropic Economic Index". HTML `<title>`, `og:title` and `twitter:title`: "Introducing the Anthropic Economic Index". `wiki/INDEX.md` uses the meta title.
- **Date.** "Feb 10, 2025" (dateline under the heading).
- **Authors.** None named on the page. No byline. The page carries two category tags above the heading: "Societal Impacts" and "Economics". An **Acknowledgements** section thanks non-authors: "Jonathon Hazell, Anders Humlum, Molly Kinder, Anton Korinek, Benjamin Krause, Michael Kremer, John List, Ethan Mollick, Lilach Mollick, Arjun Ramani, Will Rinehart, Robert Seamans, Michael Webb, and Chenzi Xu."
- **Primary URL (canonical).** https://www.anthropic.com/news/the-anthropic-economic-index — the page's own `canonical` meta tag gives this `/news/` path, while the social-share links at the foot of the page point at `https://www.anthropic.com/research/the-anthropic-economic-index`. Both paths serve the same document.
- **PDF.** None. The page is web-only.
- **Document type.** Launch/announcement post for the Anthropic Economic Index, summarising the Index's first report. It is the public-facing companion to the academic paper, which the page links four times ("Read the paper", "initial report", "new paper", "the full paper") as http://arxiv.org/abs/2503.04761. The paper is a **separate wiki entry** (`wiki/reports/economic-index-2025-02-paper.md`, slug `economic-index-2025-02-paper`) and is not summarised here; where this page defers to it ("please see the full paper, in particular Appendix B"), that deferral is recorded below rather than resolved.
- **Length.** Web page, no pagination. Body text from "In the coming years…" to the end of Acknowledgements: **1,928 words** (plain-text extraction of the fetched HTML, `wc`-equivalent count, 2026-09-16). Six images, five of which carry substantive alt text with numbers in it; four bold figure captions in the body. References below use **section headings**, and, for figures, the caption or the image alt text, as the director's kick-off note directs for pages without page numbers.
- **Release/data it rests on.** The page says the analysis uses "approximately one million conversations with Claude (specifically, Free and Pro conversations on Claude.ai)" and that Anthropic is "open sourcing the dataset used for this analysis", linking https://huggingface.co/datasets/Anthropic/EconomicIndex/ (§Open data and call for input: "The full dataset can be downloaded here"). The page does not name a release folder or a data window. *Cross-reference, not from the page:* the steward's enumeration maps this report to `release_2025_02_10/` (14 files; see `data/releases/INDEX.md`).
- **Other outbound links.** O\*NET (https://www.onetonline.org/); Clio (https://www.anthropic.com/research/clio); the Index initiative page (https://www.anthropic.com/economic-futures — the anchor text "Anthropic Economic Index" in the opening paragraph points at Economic Futures, not at an `/economic-index` page); a Google Form for researcher input; and one economics citation, https://academic.oup.com/qje/article-abstract/118/4/1279/1925105 (QJE vol. 118, issue 4, p. 1279; the page gives no author names — *wiki author's identification, unverified today because the OUP page is behind a bot check:* this is Autor, Levy and Murnane, 2003).

## Claims

Every substantive empirical claim on the page, with its reference, the number exactly as published, and the comparison the claim rests on. Claims 14–19 come from figure alt text; claims from alt text are marked, because alt text is written to describe a chart rather than to state a finding, and its numbers are sometimes more precise than the body's.

1. **§Summary bullets (first bullet).** "Today, usage is concentrated in software development and technical writing tasks." Qualitative; rests on comparing the conversation share of these task types against all other O\*NET task types in the same sample.
2. **§Summary bullets (first bullet).** "Over one-third of occupations (roughly **36%**) see AI use in at least a quarter of their associated tasks". Comparison: occupations classified by whether ≥25% of their O\*NET-listed tasks appear in the conversation sample at all, against the full set of O\*NET occupations.
3. **§Summary bullets (first bullet).** "approximately **4%** of occupations use it across three-quarters of their associated tasks". Same denominator as claim 2, threshold raised to ≥75% of an occupation's tasks.
4. **§Summary bullets (second bullet).** "AI use leans more toward augmentation (**57%**) … compared to automation (**43%**)". Comparison: the two collapsed halves of the five-pattern classification, as shares of classified conversations, against each other.
5. **§Summary bullets (third bullet).** "AI use is more prevalent for tasks associated with mid-to-high wage occupations like computer programmers and data scientists, but is lower for both the lowest- and highest-paid roles." Comparison: conversation share by occupation against that occupation's O\*NET median U.S. salary — an inverted-U in the wage gradient, asserted qualitatively with no coefficient, no test and no confidence interval anywhere on the page.
6. **§Results — Uses of AI by job type.** "**37.2%** of queries sent to Claude were in this category" (“computer and mathematical”, "which in large part covers software engineering roles"), "covering tasks like software modification, code debugging, and network troubleshooting". Comparison: against the other O\*NET/SOC major categories in the same sample; stated as "by far the largest".
7. **§Results — Uses of AI by job type.** "The second largest category was “arts, design, sports, entertainment, and media” (**10.3%** of queries)", "which mainly reflected people using Claude for various kinds of writing and editing". Same comparison as claim 6.
8. **§Results — Uses of AI by job type.** "occupations involving a high degree of physical labor, such as those in the “farming, fishing, and forestry” category (**0.1%** of queries), were least represented". Same comparison; the category is the minimum of the distribution.
9. **§Results — Uses of AI by job type (figure caption, bar chart).** "For each job type, the percentage of relevant conversations with Claude is shown in orange compared to the percentage of workers in the U.S. economy with that job type (from the U.S. Department of Labor's O\*NET categories) in gray." This is the page's central comparison: **usage share versus U.S. employment share**, across 20 job types.
10. **§Results — Depth of AI use within occupations.** "only approximately **4%** of jobs used AI for at least **75%** of tasks". Restates claim 3 with "jobs" in place of "occupations".
11. **§Results — Depth of AI use within occupations.** "roughly **36%** of jobs had some use of AI for at least **25%** of their tasks". Restates claim 2; note the qualifier "some use of AI".
12. **§Results — Depth of AI use within occupations.** "there wasn't evidence in this dataset of jobs being entirely automated: instead, AI was diffused across the many tasks in the economy, having stronger impacts for some groups of tasks than others". Comparison: the observed distribution of within-occupation task coverage against the counterfactual of whole-occupation coverage; framed as confirming a prior ("As we predicted").
13. **§Results — AI use and salary.** "both low-paying and very-high-paying jobs had very low rates of AI use (these were generally jobs involving a large degree of manual dexterity, such as shampooers and obstetricians)" and "specific occupations in the mid-to-high median salary ranges, like computer programmers and copywriters … were—in our data—among the heaviest users of AI". Comparison: named occupations at three points of the O\*NET median-salary distribution; the mechanism offered ("manual dexterity") is asserted, not measured.
14. **§Results — AI use and salary (scatter-plot alt text).** "Computer-related jobs (Programmers and Software Developers) cluster in the upper right with high wages ($75-100k) and high AI usage (3-6%). Lower-wage positions like Shampooers ($25k) show minimal AI usage (<1%). A vertical line marks the U.S. median wage of **$60,070**. Specialized roles like Obstetricians appear at the far right with high wages ($200k) but low AI usage." *(alt text)* Comparison: per-occupation conversation share against annual wage, with the U.S. median wage drawn as a reference line.
15. **§Results — Automation versus augmentation (bar-chart alt text).** "augmentation (**57.4%** total) versus automation (**42.6%** total) in Claude conversations". *(alt text; the body rounds these to 57% and 43%.)* Comparison: the two collapsed halves against each other.
16. **§Results — Automation versus augmentation (bar-chart alt text).** "Augmentation breaks down into three categories: Validation (**2.8%**), Task Iteration (**31.3%**), and Learning (**23.3%**)." *(alt text)* Comparison: the three augmentation patterns against each other, as shares of all classified conversations.
17. **§Results — Automation versus augmentation (bar-chart alt text).** "Automation divides into two categories: Feedback Loop (**14.8%**) and Directive (**27.8%**)." *(alt text)* Comparison: the two automation patterns against each other, as shares of all classified conversations.
18. **§Summary infographic (alt text, first image after the bullets).** "Computer & Mathematical (**37.2%**), Arts & Media (**10.3%**), Education & Library (**9.3%**), Office & Administrative (**7.9%**), Life Sciences (**6.4%**), and Business & Financial (**5.9%**)". *(alt text)* Comparison: the six largest occupational categories by conversation share. The caption below the infographic fixes the unit: "The numbers refer to the percentage of conversations with Claude that were related to those individual tasks, occupations, and categories."
19. **§Results — Uses of AI by job type (bar-chart alt text).** Usage share against U.S. employment share, per category: "Computer and mathematical jobs show the highest AI usage (**37.2%**) despite representing only **3.4%** of workers. Office and administrative support has the highest workforce percentage (**12.2%**) with **7.9%** AI usage. Other notable disparities include Arts and Media (**10.3%** AI usage vs **1.4%** workers) and Transportation (**0.3%** AI usage vs **9.1%** workers). Farming shows the lowest representation in both categories (**0.1%** AI usage, **0.3%** workers)." *(alt text)* This is the only place on the page where the usage-versus-employment comparison is given as numbers rather than as a picture.
20. **§Using Clio to match AI use to tasks (sample size).** "We used Clio on a dataset of approximately **one million** conversations with Claude (specifically, Free and Pro conversations on Claude.ai)". No date window, no country composition, no per-category counts are given.
21. **§Using Clio to match AI use to tasks (taxonomy size).** O\*NET is "a database of around **20,000** specific work-related tasks". Sets the denominator for the task-coverage claims 2, 3, 10 and 11.
22. **§Mapping AI usage across the labor market (design claim).** "We don't survey people on their AI use, or attempt to forecast the future; instead, we have direct data on how AI is actually being used." Comparison: observed-usage measurement against survey-based and forecast-based approaches.
23. **§Open data and call for input (contribution claim).** "The most important contribution of this paper, and of the Anthropic Economic Index, is its new methodology providing detailed data on the impacts of AI." A claim about the work's own contribution, not about the world; recorded because later releases build on it.

## Definitions (verbatim)

Every construct or measure the page defines, quoted exactly, with its section reference. No paraphrase in this section.

**Clio** — §Using Clio to match AI use to tasks:
> "This research was made possible by Claude insights and observations, or  "Clio", an automated analysis tool that allows us to analyze conversations with Claude while preserving user privacy1."

**Clio (privacy mechanism)** — Footnotes, footnote 1:
> "Clio takes large numbers of conversations and aggregates them into higher-level categories for analysis. Importantly, for the preservation of user privacy it does so without human researchers being able to see the original conversations. You can read more about Clio here."

**Occupational tasks (why tasks, not occupations)** — §Analyzing occupational tasks:
> "Our research began with an important insight from the economics literature: sometimes it makes sense to focus on *occupational tasks* rather than *occupations themselves*. Jobs often share certain tasks and skills in common: for example, visual pattern recognition is a task performed by designers, photographers, security screeners, and radiologists."

**O\*NET and the task taxonomy** — §Using Clio to match AI use to tasks:
> "We chose tasks according to the classification made by the U.S. Department of Labor, which maintains a database of around 20,000 specific work-related tasks called the Occupational Information Network, or O*NET."

**Conversation-to-task mapping rule** — §Using Clio to match AI use to tasks:
> "Clio matched each conversation with the O*NET task that best represented the role of the AI in the conversation (the process is summarized in the figure below). We then followed the O*NET scheme for grouping the tasks into the occupations they best represented, and the occupations into a small set of overall categories: *education and library,* *business and financial,* and so on."

**The pipeline, as captioned** — §Using Clio to match AI use to tasks, figure caption:
> "The process by which our Clio system translates conversations with Claude (which are kept strictly private; top left) into occupational tasks (top middle) and occupations/occupational categories derived from O*NET (top right). These can then be entered into various analyses (bottom row; discussed in more detail below)."

**The unit behind every percentage** — §Summary infographic, figure caption:
> "Where and how AI is used across the economy, drawn from real-world usage data from Claude.ai. The numbers refer to the percentage of conversations with Claude that were related to those individual tasks, occupations, and categories."

**Automation and augmentation** — §Results — Automation versus augmentation:
> "We also looked in more detail at *how* the tasks were being performed—specifically, at which tasks involved "automation" (where AI directly performs tasks such as formatting a document) versus "augmentation" (where AI collaborates with a user to perform a task)."

**Augmentation, glossed by example** — §Results — Automation versus augmentation:
> "That is, in just over half of cases, AI was not being used to replace people doing tasks, but instead worked *with* them, engaging in tasks like validation (e.g., double-checking the user's work), learning (e.g., helping the user acquire new knowledge and skills), and task iteration (e.g., helping the user brainstorm or otherwise doing repeated, generative tasks)."

**The five patterns (subtypes)** — §Results — Automation versus augmentation, figure caption:
> "The percentage of conversations with Claude that involved augmentation versus automation, and the breakdown of task subtypes within each category. Subtypes are defined in our paper as follows. Directive: Complete task delegation with minimal interaction; Feedback Loop: Task completion guided by environmental feedback; Task Iteration: Collaborative refinement process; Learning: Knowledge acquisition and understanding; Validation: Work verification and improvement."

**Augmentation as glossed in the summary bullets** — §Summary bullets (second bullet):
> "AI use leans more toward augmentation (57%), where AI collaborates with and enhances human capabilities, compared to automation (43%), where AI directly performs tasks."

**Usage share versus workforce share** — §Results — Uses of AI by job type, figure caption:
> "For each job type, the percentage of relevant conversations with Claude is shown in orange compared to the percentage of workers in the U.S. economy with that job type (from the U.S. Department of Labor's O*NET categories) in gray."

**Wage measure** — §Results — AI use and salary:
> "The O*NET database provides the median U.S. salary for each of the occupations listed. We added this information to our analysis, allowing us to compare professions' median salaries and the level of AI use in their corresponding tasks."

**The wage figure's axes** — §Results — AI use and salary, figure caption:
> "Annual wage (x-axis) versus percent of conversations with Claude that involved that occupation (y-axis). Some illustrative occupations are highlighted."

**The work-relevance filter** — §Caveats, third bullet:
> "While Claude.ai data contains some non-work conversations, we used a language model to filter this data to only contain conversations relevant to an occupational task, which helps to mitigate this concern."

**The Index itself** — §opening paragraph:
> "we're launching the Anthropic Economic Index, an initiative aimed at understanding AI's effects on labor markets and the economy over time."

*Not defined anywhere on the page (recorded here because the wiki's other entries will need it):* "depth of AI use", the ≥25% and ≥75% thresholds, what counts as an occupation's task "seeing AI use", the sample window, and the geographic scope of the conversations.

## Data and methods

In the wiki author's words, with section references.

- **Platform and product.** Claude.ai only, and within it the Free and Pro plans only (§Using Clio to match AI use to tasks; §Caveats bullet 3: "rather than API, Team, or Enterprise users"). No first-party API, Team or Enterprise data; no Claude Code (the product did not exist in this window).
- **Sample.** "approximately one million conversations" (§Using Clio to match AI use to tasks). The page gives no collection window, no country or language composition, no user counts and no per-category conversation counts. The window is stated in the paper, which is a separate entry.
- **Unit of analysis.** The conversation. Every published percentage is a share of conversations, not of users, tokens, sessions or time (§Summary infographic caption; §Results — AI use and salary figure caption). Conversations are unweighted: a one-line exchange and a long working session count alike (the page nowhere says otherwise).
- **Classifier.** Clio, "an automated analysis tool that allows us to analyze conversations with Claude while preserving user privacy" (§Using Clio to match AI use to tasks), operating without human researchers seeing raw conversations (footnote 1). Two classification steps are described: (i) a language-model filter that keeps only conversations "relevant to an occupational task" (§Caveats bullet 3); (ii) a match of each retained conversation to "the O\*NET task that best represented the role of the AI in the conversation" (§Using Clio…). A third classification — into the five automation/augmentation patterns — is used in the results and captioned, but the page describes its procedure only by pointing to the paper.
- **Taxonomy.** O\*NET (U.S. Department of Labor), "around 20,000 specific work-related tasks", aggregated by O\*NET's own scheme: tasks → occupations → occupational categories (§Using Clio to match AI use to tasks). Occupation is therefore inferred from the content of the conversation, never from the user.
- **External data layered in.** (i) O\*NET median U.S. salary per occupation, for the wage gradient (§Results — AI use and salary); (ii) the share of U.S. workers in each job type, attributed on the page to "the U.S. Department of Labor's O\*NET categories" (§Results — Uses of AI by job type, figure caption), used as the comparison baseline; the scatter-plot alt text also marks a U.S. median wage of $60,070.
- **Derived measures.** Two: *breadth/depth of use within an occupation* — the share of an occupation's O\*NET tasks that appear in the data, thresholded at ≥25% and ≥75% (§Results — Depth of AI use within occupations) — and the *automation/augmentation split*, the five patterns collapsed into two (§Results — Automation versus augmentation).
- **Privacy thresholds.** The page states the privacy *principle* (aggregation; no human view of raw conversations; footnote 1) but names **no minimum-cluster size, no k-anonymity threshold and no suppression rule**. Any such threshold must be taken from the paper or the release documentation, not from this page.
- **Statistical methods.** None reported. No regression, no significance test, no standard errors, no confidence intervals, no sampling-uncertainty discussion. Every result on the page is a share or a scatter; the inverted-U in wages and the "diffusion rather than replacement" reading are stated in prose.
- **Released data and code.** The dataset is released openly and immediately: "We're immediately openly sharing the dataset we used for the above analyses" (§Open data and call for input), at https://huggingface.co/datasets/Anthropic/EconomicIndex/. The page promises further datasets "as they become available". No code repository is named on the page. *Cross-reference, not from the page:* `data/releases/INDEX.md` records `release_2025_02_10/` with 14 files including `plots.ipynb`.
- **Positioning of the method.** Observed usage rather than survey or forecast (§Mapping AI usage across the labor market), built on the task-based approach to technological change cited to QJE 118(4):1279.

## Limitations (verbatim)

§Caveats, lead-in:
> "Our study provides a unique glimpse into how AI is changing the labor market. But as with all studies it has important limitations. Some of these include:"

§Caveats, bullet 1 (work versus non-work):
> "We can't know for certain whether someone using Claude for a task was completing a task for work. Someone asking Claude for writing or editing advice *could* be doing so at work, but they could also be doing so for the novel they're writing as a hobby."

§Caveats, bullet 2 (what users did with the output):
> "Relatedly, we don't know *how* the users were using the responses from Claude. Were they, for instance, copy-pasting code snippets? Were they fact-checking responses or accepting them uncritically? Some of what appears in our data to be automation could, in fact, be augmentation: for example, a user might ask Claude to write a full memo for them (which would appear as automation), but then edit it themselves afterwards (which would be augmentation)."

§Caveats, bullet 3 (coverage of plans):
> "We also only analyze data from Claude.ai Free and Pro plans, rather than API, Team, or Enterprise users. While Claude.ai data contains some non-work conversations, we used a language model to filter this data to only contain conversations relevant to an occupational task, which helps to mitigate this concern."

§Caveats, bullet 4 (classification error):
> "The sheer number of different tasks means it is possible that Clio classified some conversations incorrectly (please see the full paper, in particular Appendix B, for details on how we validated the analysis);"

§Caveats, bullet 5 (modality):
> "Claude can't generate images (except indirectly via code), and so some creative uses won't be referenced in the data;"

§Caveats, bullet 6 (selection into Claude):
> "Given that Claude is advertised for use as a state-of-the-art coding model, we might expect coding to be overrepresented as a use case. For that reason, we don't argue that the uses in our dataset are a representative sample of AI use in general."

§Conclusions and future research (shelf life of the findings):
> "AI use is rapidly expanding, and models are becoming ever-more capable. The labor-market picture may look quite different within a relatively short time."

§Conclusions and future research (scope of inference):
> "Our research gives data on how AI is being used, but it doesn't provide policy prescriptions. Answers to questions about how to prepare for AI's impact on the labor market can't come directly from research in isolation; instead, they'll come from a combination of evidence, values, and experience from broad perspectives."

§Mapping AI usage across the labor market (what the design does not do):
> "We don't survey people on their AI use, or attempt to forecast the future; instead, we have direct data on how AI is actually being used."

## Open questions, conjectures and promised follow-ups (verbatim)

§Analyzing occupational tasks — the prior that motivates the task-level design:
> "Certain tasks lend themselves better to being automated or augmented by a new technology than others. We'd therefore expect AI to be adopted selectively for different tasks across different occupations, and that analyzing tasks—in addition to jobs as a whole—would give us a fuller picture of how AI is being integrated into the economy."

§Summary bullets (third bullet) — conjectured mechanism for the wage gradient, untested on the page:
> "This likely reflects both the limits of current AI capabilities, as well as practical barriers to using the technology."

§Results — Depth of AI use within occupations — a prediction the authors say was borne out:
> "As we predicted, there wasn't evidence in this dataset of jobs being entirely automated: instead, AI was diffused across the many tasks in the economy, having stronger impacts for some groups of tasks than others."

§Caveats, bullet 2 — conjecture about measurement direction:
> "Some of what appears in our data to be automation could, in fact, be augmentation: for example, a user might ask Claude to write a full memo for them (which would appear as automation), but then edit it themselves afterwards (which would be augmentation)."

§Caveats, bullet 6 — conjecture about selection:
> "Given that Claude is advertised for use as a state-of-the-art coding model, we might expect coding to be overrepresented as a use case."

§Caveats, bullet 4 — pointer to validation elsewhere:
> "please see the full paper, in particular Appendix B, for details on how we validated the analysis"

§Conclusions and future research — the promise of repetition (the Index's founding commitment):
> "For that reason, we'll repeat many of the analyses above over time to help track the societal and economic changes that are likely to occur. We'll regularly release the results and the associated datasets as part of the Anthropic Economic Index."

§Conclusions and future research — the promised longitudinal measure, and the conditional forecast attached to it:
> "These kinds of longitudinal analyses can give us new insights into AI and the job market. For example, we'll be able to monitor changes in the depth of AI use within occupations. If it remains the case that AI is used only for certain tasks, and only a few jobs use AI for the vast majority of their tasks, the future might be one where most current jobs evolve rather than disappear."

§Conclusions and future research — the second promised longitudinal measure:
> "We can also monitor the ratio of automation to augmentation, providing signals of areas where automation is becoming more prevalent."

§Conclusions and future research — open-ended next step:
> "We look forward to using our new methodology to shed more light on these issues."

§opening paragraph — invitation to outside researchers:
> "Developing policy responses to address the coming transformation in the labor market and its effects on employment and productivity will take a range of perspectives. To that end, we are also inviting economists, policy experts, and other researchers to provide input on the Index."

§Open data and call for input — promised further releases and a request for research directions:
> "We're immediately openly sharing the dataset we used for the above analyses, and we plan to share further such datasets as they become available in the future."

> "A form for researchers to provide feedback on our data and suggest new research directions is here."

§Open data and call for input — the claim about what the Index is for:
> "The most important contribution of this paper, and of the Anthropic Economic Index, is its new methodology providing detailed data on the impacts of AI."

## What it did not test

**This section is the wiki author's inference, not the source's words.** It lists adjacent questions the page had the material to address but did not, and constructs it used without validating *on this page*. Items marked *(paper)* may be answered in the accompanying academic paper or in the released data; that must be checked against `wiki/reports/economic-index-2025-02-paper.md` and with the data steward before any of them is treated as open.

*Crossings the page reports separately but never joins:*
1. **Automation/augmentation by occupation or category.** The page gives one economy-wide 57/43 split and, separately, a category ranking. It never asks whether software tasks are more automated than writing tasks — the single most obvious cut, and the one every later release returns to.
2. **Automation/augmentation by wage.** The wage gradient is computed for usage volume only. Whether high-wage tasks are delegated or collaborated on is not reported, though both variables are constructed for the same conversations.
3. **Depth by wage, by category, or against employment share.** "Depth" (the ≥25%/≥75% task-coverage measure) is reported only as two economy-wide numbers. Which occupations sit above the thresholds is not listed on the page.
4. **Usage share versus employment share as a ratio.** The bar chart shows the two series side by side; the page never computes the representation ratio (usage ÷ employment) that would rank over- and under-representation, nor does it say which categories are closest to parity.
5. **Which tasks within an occupation are used and which are not.** The measure counts covered tasks; it never characterises the covered ones (are they the routine, the documentable, the language-heavy?).

*Constructs used without validation on this page:*
6. **The O\*NET task match as a measure of work.** The page concedes it cannot tell work from hobby (§Caveats bullet 1) but reports every share as though the mapping were a labour-market measurement; no accuracy figure, no human audit and no sensitivity check appears on the page *(paper: Appendix B is named but not summarised)*.
7. **The work-relevance language-model filter.** Its precision and recall are not given, nor the share of conversations it removed. A filter that drops a fifth of the sample and one that drops four-fifths imply very different denominators for every percentage on the page.
8. **The five patterns.** Defined only by a one-clause gloss each, in a figure caption, with the definitions attributed to the paper. No inter-rater agreement, no examples at the boundary (a Directive request followed by three revisions), and no account of how a multi-turn conversation gets a single label.
9. **The collapse of five patterns into two.** Why Feedback Loop is automation rather than augmentation is asserted, not argued; the 57/43 headline is entirely a consequence of that choice (moving Feedback Loop, 14.8%, would flip it to 72/28).
10. **The conversation as the unit.** No weighting by length, turns, tokens or user, and no test of whether the rankings survive weighting — although conversation-level data existed to do it.
11. **One user, many conversations.** No de-duplication by user is reported, so a small number of heavy users could carry a category; no per-user distribution is shown.

*Comparisons the design invites but the page does not make:*
12. **U.S. baseline against a global usage sample.** Every benchmark (employment shares, median salary, the $60,070 line) is U.S.; the conversation sample is not stated to be U.S.-only. The page neither reports the geographic composition nor flags the mismatch — the gap the September 2025 geography release later fills.
13. **Any time dimension.** A single pooled cross-section is reported and longitudinal analysis is promised in the same document; no within-window trend, no split by which Claude model served the conversation (the page never names a model version), and no before/after around any product change.
14. **Uncertainty of any kind.** No sample counts per category, no intervals, no minimum-cell rule stated. A 0.1% category and a 37.2% category are printed to the same precision.
15. **Sensitivity of the wage result to composition.** The inverted U could be produced by occupation mix, by the O\*NET median-salary measure, or by the small number of occupations at the extremes; no robustness check, alternative wage source (BLS OEWS) or binned estimate is shown, though the released files include a BLS employment table.
16. **The prior technologies the framing invokes.** The Spinning Jenny and car-manufacturing robots are used rhetorically; no diffusion comparison, no benchmark rate of adoption.
17. **Whether "not entirely automated" follows from the data.** Task coverage in a one-million-conversation sample bounds observed use, not feasible use; the page reads a low coverage rate as evidence about job destruction without testing the inferential step.

## Verification

- **URLs fetched, 2026-09-16:**
  - https://www.anthropic.com/news/the-anthropic-economic-index — fetched twice by two independent routes: the `web_fetch` tool (rendered-to-markdown, including image alt text) and a direct HTTP GET (HTTP 200, 196,245 bytes of HTML, saved to `/tmp/aei_feb.html`, plain text extracted to `/tmp/aei_feb.txt`). The two renderings agree word for word in the body; the alt-text strings quoted above were read from the raw `alt="…"` attributes in the HTML.
- **Could not be fetched:** https://academic.oup.com/qje/article-abstract/118/4/1279/1925105 returned an interstitial bot check ("Just a moment…"), so the cited article's authorship could not be confirmed today; the identification given in §Source is the wiki author's, not the page's.
- **Deliberately not fetched in this thread:** the linked paper (http://arxiv.org/abs/2503.04761), the Clio post (https://www.anthropic.com/research/clio), the Hugging Face dataset (https://huggingface.co/datasets/Anthropic/EconomicIndex/) and https://www.anthropic.com/economic-futures. Each is a separate wiki or atlas entry; nothing in this file is quoted from them.
- **Quotation check.** All 40 block quotations in §Definitions, §Limitations and §Open questions were matched by script against the plain-text extraction of the fetched HTML (and, for figure alt text, against the raw `alt` attributes), ignoring whitespace and quote-mark style only: 40 of 40 matched, 0 missing. Two normalisations are applied and are the only departures from the page's typography: apostrophes and quotation marks are written straight where the page uses curly ones (except where a nested quotation needed the page's own “…” marks), and the footnote marker in the Clio sentence is kept as the page prints it ("privacy1"). Em-dashes, ellipses, italics and bold inside quotations reproduce the page's own. Where a quotation elides words, the elision is marked "…". Numbers in §Claims are quoted as published, including the body's rounded 57%/43% and the figure's 57.4%/42.6%.
- **Page state.** The footer shows "© 2026 Anthropic PBC" and current product navigation; the article body is the February 2025 text, unchanged in substance. No revision history or "last updated" marker is present on the page.
