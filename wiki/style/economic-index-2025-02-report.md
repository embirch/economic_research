# economic-index-2025-02-report — style annotation

## Source

- **Title on page:** "The Anthropic Economic Index" (H1). Browser/OG title: "Introducing the Anthropic Economic Index".
- **Date on page:** "Feb 10, 2025".
- **Primary URL fetched:** https://www.anthropic.com/news/the-anthropic-economic-index
- **Other URLs it points at (not fetched for this file):** the companion paper at http://arxiv.org/abs/2503.04761 (own slug `economic-index-2025-02-paper`), the dataset at https://huggingface.co/datasets/Anthropic/EconomicIndex, the Clio post at https://www.anthropic.com/research/clio, https://www.anthropic.com/economic-futures, a Google Forms feedback form, and the QJE article at https://academic.oup.com/qje/article-abstract/118/4/1279/1925105.
- **PDF or appendix:** none. The `wiki/INDEX.md` row carries `—` in the PDF column; all depth is delegated to the arXiv paper.
- **Document type:** launch post plus first-report summary. It does two jobs at once: it announces a standing initiative (the Index) and it reports the findings of that initiative's first paper. Byline area is categorical, not personal — "Societal Impacts" / "Economics"; no named authors on the page (names appear only in Acknowledgements as commenters).
- **Approximate length:** roughly 1,600–1,800 words of body prose, five images (one decorative hero, four captioned exhibits), six H2 sections of substance plus Acknowledgements and Work with us, two H3s under the first H2, one H3 ("Caveats") under Results, one footnote.
- **Audience:** economists, policy experts and researchers, addressed as such and invited to act ("we are also inviting economists, policy experts, and other researchers to provide input on the Index"). Written for a reader who will be trusted with a share-of-conversations number but not with a regression table — the table is in the paper.

## Section order

Headings in order, with what each does and how long it runs.

1. **H1 "The Anthropic Economic Index"** + date + "Read the paper" link + hero image. ~1 line. The paper link sits above the article, before any prose: the post is positioned from the first screen as an entry point, not the record.
2. **Untitled opening (no heading)** — three paragraphs, then a three-bullet findings list, then the one-line pointer "See below for further details on our initial findings." ~250 words. This is the whole post in miniature: why it matters, what the data is, what was found, an invitation.
3. **Captioned infographic (no heading)** — the six-category overview exhibit with a bold caption. Placed immediately after the bullets, before any method.
4. **H2 "Mapping AI usage across the labor market"** — ~120 words of framing plus two H3s. States the lineage and the method's distinguishing feature.
   - **H3 "Analyzing occupational tasks"** — ~120 words. Why tasks rather than occupations, sourced to the economics literature.
   - **H3 "Using Clio to match AI use to tasks"** — ~180 words plus the pipeline diagram and its caption. The instrument, the sample, the classification scheme (O*NET), the aggregation ladder (task → occupation → category).
5. **H2 "Results"** — ~520 words, four bold-lead paragraphs, each with its own figure and caption:
   - "**Uses of AI by job type.**" → category shares, then the comparison figure against workforce shares.
   - "**Depth of AI use within occupations.**" → the 4% / 36% breadth result. No figure; the number is carried in prose.
   - "**AI use and salary.**" → the wage gradient, then the scatter.
   - "**Automation versus augmentation.**" → 57/43 and the five subtypes, then the stacked bar.
   - **H3 "Caveats"** — ~290 words, six bullets. Sits *inside* Results, after the last finding and before the conclusion.
6. **H2 "Conclusions and future research"** — three paragraphs, ~250 words. What the series will make answerable; the conditional inference; the refusal to prescribe policy; a closing pointer to the paper.
7. **H2 "Open data and call for input"** — ~90 words. Names the methodology as the contribution, releases the data, repeats the feedback link.
8. **H2 "Acknowledgements"** — one sentence, fifteen named external commenters.
9. **H2 "Work with us"** — recruiting. Boilerplate; not part of the argument.
10. **Footnotes** — one, on Clio's privacy properties.

**Where the findings sit:** before the methods, and then again after them. The three headline numbers appear in the opening bullets — roughly 150 words into the post, ahead of any word about Clio, O*NET or the sample. The method section then earns them, and Results restates each with its figure and its qualifiers. A reader who stops after the bullets has the findings; a reader who stops after Results has the findings with their evidence; only the paper has the identification. Caveats come after all four findings, not distributed among them.

## Opening move

Verbatim, the first three paragraphs and the findings list (hyperlink URLs stripped; the anchor text is marked below):

> In the coming years, AI systems will have a major impact on the ways people work. For that reason, we're launching the Anthropic Economic Index, an initiative aimed at understanding AI's effects on labor markets and the economy over time.

> The Index's initial report provides first-of-its-kind data and analysis based on millions of anonymized conversations on Claude.ai, revealing the clearest picture yet of how AI is being incorporated into real-world tasks across the modern economy.

> We're also open sourcing the dataset used for this analysis, so researchers can build on and extend our findings. Developing policy responses to address the coming transformation in the labor market and its effects on employment and productivity will take a range of perspectives. To that end, we are also inviting economists, policy experts, and other researchers to provide input on the Index.

> The main findings from the Economic Index's first paper are:
>
> - Today, usage is concentrated in software development and technical writing tasks. Over one-third of occupations (roughly 36%) see AI use in at least a quarter of their associated tasks, while approximately 4% of occupations use it across three-quarters of their associated tasks.
> - AI use leans more toward augmentation (57%), where AI collaborates with and enhances human capabilities, compared to automation (43%), where AI directly performs tasks.
> - AI use is more prevalent for tasks associated with mid-to-high wage occupations like computer programmers and data scientists, but is lower for both the lowest- and highest-paid roles. This likely reflects both the limits of current AI capabilities, as well as practical barriers to using the technology.

> See below for further details on our initial findings.

Anchor text carrying links, in order: "Anthropic Economic Index" → economic-futures; "initial report" → arXiv; "Claude.ai" → claude.ai; "open sourcing the dataset" → Hugging Face; "provide input" → the form.

**Annotation.**

- **What question is posed.** None, strictly — no question mark, no puzzle. The first sentence is an assertion about the future ("AI systems will have a major impact on the ways people work") and the second sentence converts it into a reason to build an instrument ("For that reason, we're launching…"). The move is *forecast → therefore measure*, not *question → therefore test*. This is the launch-post variant of the opening; the later reports in the series open on a change or a gap instead.
- **Who is said to be affected.** "people work" — the whole labour market, unmodified, in the first eight words. Then a second audience is named as affected in a different sense: policy responses "will take a range of perspectives," which is what licenses the invitation to economists and policy experts. Nobody is named as harmed or helped; the affected party is the economy in aggregate.
- **What the data is said uniquely to show.** Two superlatives, both attached to the *data and analysis* rather than to any finding: "first-of-its-kind data and analysis" and "the clearest picture yet of how AI is being incorporated into real-world tasks." The uniqueness claim is sourced to the nature of the observation — "millions of anonymized conversations" — and is sharpened later into the methodological contrast (no survey, no forecast). Note the discipline: the superlative never says *the findings are unprecedented*, only that the vantage point is.
- **How soon the first number appears.** Not in the first three paragraphs. The first quantitative statement is "roughly 36%" in the first bullet, about 150 words in; "millions" (para. 2) is the only earlier magnitude, and it is deliberately imprecise. So the order is: stakes, instrument, openness, invitation, *then* numbers. Three paragraphs of why-it-matters buy the right to a bare bullet of percentages with no method attached.
- **Register details worth copying.** "we're launching" and "We're also open sourcing" are first person plural for institutional acts, never for findings — findings in the bullets have no agent at all ("usage is concentrated", "AI use leans", "AI use is more prevalent"). The hedge is fused to the claim in the same sentence in every bullet: "Today, usage is concentrated" (temporal fence), "roughly 36%" / "approximately 4%" (precision fence), "leans more toward" (magnitude fence), "This likely reflects" (mechanism fence, flagged as conjecture).
- **The bullet list itself is a stylistic choice.** Three bullets, one per pre-specified dimension (breadth, mode, wage gradient), each a complete sentence pair: the number, then what it means or why it might be so. No bullet cites a figure. No bullet cites the sample. The list is the abstract; the sample arrives 500 words later.

## Findings and their caveats

### Finding 1 — concentration by occupational category

> **Uses of AI by job type.** The tasks and occupations with by far the largest adoption of AI in our dataset were those in the "computer and mathematical" category, which in large part covers software engineering roles. 37.2% of queries sent to Claude were in this category, covering tasks like software modification, code debugging, and network troubleshooting.

> The second largest category was "arts, design, sports, entertainment, and media" (10.3% of queries), which mainly reflected people using Claude for various kinds of writing and editing. Unsurprisingly, occupations involving a high degree of physical labor, such as those in the "farming, fishing, and forestry" category (0.1% of queries), were least represented.

> We also compared the rates in our data to the rates at which each occupation appeared in the labor market in general. The comparisons are shown in the figure below.

**Annotation.** The caveat is inside the claim's grammar, not appended: "in our dataset" is placed *between* the superlative and the subject ("by far the largest adoption of AI in our dataset"), so the reader cannot take the superlative away without the fence. The number is then given in the units actually measured — "37.2% of queries sent to Claude", not "37.2% of AI use" — and immediately glossed with exemplar tasks so the reader knows what the category contains. Note the substitution: the bold lead-in and the framing sentence say **AI**; the measured quantity says **Claude**. That alternation is consistent across all four findings. `Unsurprisingly` is doing caveat work of a different kind: it pre-empts the objection that a coding-heavy distribution is an artefact by conceding that the low end is exactly what anyone would predict. One decimal place is used for the shares (37.2%, 10.3%, 0.1%) in Results, where the opening bullets used whole numbers — precision increases as the reader goes deeper, never the reverse.

### Finding 2 — depth, or breadth of task coverage

> **Depth of AI use within occupations.** Our analysis found that very few occupations see AI use across most of their associated tasks: only approximately 4% of jobs used AI for at least 75% of tasks. However, more moderate use of AI is much more widespread: roughly 36% of jobs had some use of AI for at least 25% of their tasks.

> As we predicted, there wasn't evidence in this dataset of jobs being entirely automated: instead, AI was diffused across the many tasks in the economy, having stronger impacts for some groups of tasks than others.

**Annotation.** The finding is built as a contrast pair inside one sentence-and-a-half — "very few … However, … much more widespread" — so the number's meaning is carried by its opposite number rather than by an adjective. Both figures are hedged with "approximately" and "roughly" even though the underlying quantities are computable to a decimal; the imprecision signals that the threshold (75%, 25%) is the arbitrary part, not the arithmetic. The second paragraph is the most instructive sentence in the post for how to separate observation from inference: "there wasn't evidence in this dataset of jobs being entirely automated" is a statement about the *absence of evidence in a named dataset*, not a statement that no job is automated — and the alternative reading is then supplied positively ("instead, AI was diffused across…") so the null does not read as a failure. "As we predicted" reports a prior without documenting it; in our own posts the equivalent sentence has to point at the pre-registration. There is no figure for this finding: the two numbers do the work alone, which is a defensible choice when the result is a pair of scalars.

### Finding 3 — the wage gradient

> **AI use and salary.** The O*NET database provides the median U.S. salary for each of the occupations listed. We added this information to our analysis, allowing us to compare professions' median salaries and the level of AI use in their corresponding tasks.

> Interestingly, both low-paying and very-high-paying jobs had very low rates of AI use (these were generally jobs involving a large degree of manual dexterity, such as shampooers and obstetricians). It was specific occupations in the mid-to-high median salary ranges, like computer programmers and copywriters, who were—in our data—among the heaviest users of AI.

And from the opening bullets, the same finding with its mechanism:

> AI use is more prevalent for tasks associated with mid-to-high wage occupations like computer programmers and data scientists, but is lower for both the lowest- and highest-paid roles. This likely reflects both the limits of current AI capabilities, as well as practical barriers to using the technology.

**Annotation.** The paragraph opens by naming the data joined in and where it came from — the provenance sentence precedes the result sentence, so the reader knows the salary variable is O*NET's median, not Anthropic's. No coefficient, no correlation, no functional form: the shape is described in words ("both low-paying and very-high-paying … very low") and the ends are named with concrete occupations (shampooers, obstetricians) so the non-monotonicity is memorable rather than statistical. The hedge here is the em-dash interruption — "who were—in our data—among the heaviest users of AI" — which puts the fence in the most emphatic position available, mid-predicate, and costs the sentence its fluency on purpose. "among the heaviest" rather than "the heaviest" is a second fence. The mechanism sentence is quarantined in the opening bullet and marked as conjecture by "This likely reflects", and it offers two candidate explanations rather than one, with no attempt to choose between them — the post declines to adjudicate a mechanism it did not test.

### Finding 4 — automation versus augmentation

> **Automation versus augmentation.** We also looked in more detail at *how* the tasks were being performed—specifically, at which tasks involved "automation" (where AI directly performs tasks such as formatting a document) versus "augmentation" (where AI collaborates with a user to perform a task).

> Overall, we saw a slight lean towards augmentation, with 57% of tasks being augmented and 43% of tasks being automated. That is, in just over half of cases, AI was not being used to replace people doing tasks, but instead worked *with* them, engaging in tasks like validation (e.g., double-checking the user's work), learning (e.g., helping the user acquire new knowledge and skills), and task iteration (e.g., helping the user brainstorm or otherwise doing repeated, generative tasks).

**Annotation.** Both terms are defined in the same sentence in which they are introduced, in parentheses, with a worked example each ("such as formatting a document"). The magnitude is characterised before it is quantified — "a slight lean towards augmentation" — so a reader who mistakes 57/43 for a landslide has already been corrected. The "That is," sentence restates the split in the register the reader actually cares about (replacement versus collaboration) and immediately deflates the stronger reading with "in just over half of cases": the post refuses to let 57% mean "AI augments". Two of the five subtypes named in the prose (validation, learning, task iteration) are exactly the three that compose augmentation, each with an example; the automation subtypes are left to the caption. The caveats bullet later concedes that the classification itself may misallocate cases between the two poles — the finding and the challenge to the finding are 400 words apart, which is the one thing here worth *not* copying.

**Naming discipline across all four findings.** "AI" is the subject when the sentence is about the phenomenon or the economy ("AI use is more prevalent", "AI was diffused across the many tasks in the economy"). "Claude" is the subject or the object whenever a number is attached to a measurement ("37.2% of queries sent to Claude", "conversations with Claude", "people using Claude for various kinds of writing"). Every figure caption without exception says Claude. The question is about AI; the measurement is about Claude.

## Comparisons

Every place where a comparison carries the finding.

### To the history of technology

> Our new paper builds on a long line of research on the labor market impact of technologies, from the Spinning Jenny of the Industrial Revolution to the car-manufacturing robots of the present day. We focus on the ongoing impact of AI. We don't survey people on their AI use, or attempt to forecast the future; instead, we have direct data on how AI is actually being used.

**Annotation.** Two comparisons in three sentences, doing different jobs. The first places the work in a lineage by naming its two temporal extremes (Spinning Jenny → car-manufacturing robots) — the reader is told this is labour economics, not AI commentary, in one clause. The second is a comparison *of method to the alternatives*, stated as a pair of negations before the positive claim: not a survey, not a forecast, "instead, we have direct data on how AI is actually being used." The rhetorical shape is "what we are not, then what we are" — and it is the strongest sentence in the post, because the differentiator is the evidence type rather than the finding.

### To the economics literature

> Our research began with an important insight from the economics literature: sometimes it makes sense to focus on *occupational tasks* rather than *occupations themselves*. Jobs often share certain tasks and skills in common: for example, visual pattern recognition is a task performed by designers, photographers, security screeners, and radiologists.

> Certain tasks lend themselves better to being automated or augmented by a new technology than others. We'd therefore expect AI to be adopted selectively for different tasks across different occupations, and that analyzing tasks—in addition to jobs as a whole—would give us a fuller picture of how AI is being integrated into the economy.

**Annotation.** The theoretical commitment (task-based rather than occupation-based analysis) is hyperlinked to the primary source rather than cited in text, and then *immediately* illustrated with a four-occupation example (designers, photographers, security screeners, radiologists) that makes the abstraction concrete without a definition. The comparison then generates a prediction — "We'd therefore expect AI to be adopted selectively" — which is what Finding 2 later reports against. Theory is used to set an expectation before the data is shown; the expectation is stated in the conditional, never as a result. Note "in addition to jobs as a whole": the unit choice is framed as additive, not as a correction of prior work.

### To official statistics — usage share against workforce share

> We also compared the rates in our data to the rates at which each occupation appeared in the labor market in general. The comparisons are shown in the figure below.

And in the caption of that figure:

> **For each job type, the percentage of relevant conversations with Claude is shown in orange compared to the percentage of workers in the U.S. economy with that job type (from the U.S. Department of Labor's O*NET categories) in gray.**

**Annotation.** The single most important comparison in the post, and the prose does almost nothing with it — one sentence of setup and a pointer. The comparison itself is delegated entirely to the exhibit and its caption: two series, one per colour, with the benchmark's provenance named inside the caption. The over- and under-representation ratios (computer and mathematical at 37.2% of conversations against 3.4% of workers; transportation at 0.3% against 9.1%) appear only in the image's alt text, not in the body prose. Worth noting as a limit of the form: the post never states a representation ratio in a sentence, so the finding a reader takes away depends on reading the chart. Our own posts state the ratio in prose and put the figure beside it.

### Within the data — category against category

> The second largest category was "arts, design, sports, entertainment, and media" (10.3% of queries) … Unsurprisingly, occupations involving a high degree of physical labor, such as those in the "farming, fishing, and forestry" category (0.1% of queries), were least represented.

**Annotation.** Rank-ordered comparison: largest, second largest, least. The 37.2% / 10.3% / 0.1% spread makes the concentration claim without any dispersion statistic. Phrasing is by superlative plus parenthetical number, and the low end is given a mechanism in the same clause ("involving a high degree of physical labor") so the comparison explains itself.

### Against the poles of a distribution

> Interestingly, both low-paying and very-high-paying jobs had very low rates of AI use (these were generally jobs involving a large degree of manual dexterity, such as shampooers and obstetricians). It was specific occupations in the mid-to-high median salary ranges, like computer programmers and copywriters, who were—in our data—among the heaviest users of AI.

**Annotation.** A non-monotonic relationship described by comparing three regions of a single covariate (low / mid-to-high / very high), each anchored to a named occupation. Shampooers and obstetricians are the rhetorical device: two jobs with a 175,000-dollar salary gap and the same low usage, which establishes the shape more efficiently than a scatter would. The single explanatory thread offered for both poles — manual dexterity — is presented as a description of the occupations, not as a tested cause.

### Against the mode dichotomy

> Overall, we saw a slight lean towards augmentation, with 57% of tasks being augmented and 43% of tasks being automated.

**Annotation.** The comparison *is* the finding: neither share means anything alone, and the post states both rather than one plus a complement, so the reader does the subtraction and sees how close to even it is. "Slight lean" is the interpretation, placed before the numbers.

### Against prior expectation

> As we predicted, there wasn't evidence in this dataset of jobs being entirely automated

> Given that Claude is advertised for use as a state-of-the-art coding model, we might expect coding to be overrepresented as a use case. For that reason, we don't argue that the uses in our dataset are a representative sample of AI use in general.

**Annotation.** Two comparisons to expectations, pointing opposite ways. The first is confirmatory and stated in four words. The second is a comparison between the sample and the population it might be mistaken for, and it is used to *withdraw* a claim rather than support one — the expectation of bias is named, its source is named (Claude's market positioning), and the consequence is an explicit refusal of external validity. This is the model for how a sampling-frame comparison should be written: expectation, reason, claim not made.

## Figure captions

Four captioned exhibits. Captions are bold, set immediately below the image, unnumbered, with no "Figure 1" label and no source line separate from the caption text. The hero illustration carries no caption at all.

### Exhibit 1 — the six-category overview infographic

> **Where and how AI is used across the economy, drawn from real-world usage data from Claude.ai. The numbers refer to the percentage of conversations with Claude that were related to those individual tasks, occupations, and categories.**

**Annotation.** Pattern: *what the exhibit is about* (noun phrase, no verb — "Where and how AI is used across the economy"), then *provenance* ("drawn from real-world usage data from Claude.ai"), then a second sentence that defines the unit of every number on the chart ("the percentage of conversations with Claude that were related to…"). The units sentence is the load-bearing one: the infographic shows a dozen percentages at three different levels of aggregation, and one sentence tells the reader that all of them are conversation shares. Subject in the topic phrase is "AI"; subject in the units sentence is "Claude".

### Exhibit 2 — the Clio pipeline diagram

> **The process by which our Clio system translates conversations with Claude (which are kept strictly private; top left) into occupational tasks (top middle) and occupations/occupational categories derived from O\*NET (top right). These can then be entered into various analyses (bottom row; discussed in more detail below).**

**Annotation.** A schematic, so the caption plots nothing; instead it narrates the panel layout with inline position cues ("top left", "top middle", "top right", "bottom row"). The privacy property is inserted as a parenthetical inside the first clause rather than as a separate sentence — the caption is where the ethical constraint is restated. The last clause manages the reader's expectations forward ("discussed in more detail below") so the diagram does not have to be understood yet.

### Exhibit 3 — usage share against workforce share

> **For each job type, the percentage of relevant conversations with Claude is shown in orange compared to the percentage of workers in the U.S. economy with that job type (from the U.S. Department of Labor's O\*NET categories) in gray.**

**Annotation.** The tightest caption in the post and the closest to a house template. Its parts, in order: unit of observation ("For each job type"), series one with its measure and its colour ("the percentage of relevant conversations with Claude … in orange"), the comparison word ("compared to"), series two with its measure ("the percentage of workers in the U.S. economy with that job type"), the benchmark's source in parentheses, series two's colour ("in gray"). Colour is used as the series key because the chart has no legend in the caption's view. No axis names, no sample size, no date range — the reader must go to the method section for the ~1M-conversation sample. Note "relevant conversations", which quietly carries the occupational-relevance filter.

### Exhibit 4 — wage against usage scatter

> **Annual wage (x-axis) versus percent of conversations with Claude that involved that occupation (y-axis). Some illustrative occupations are highlighted.**

**Annotation.** Two sentences, twenty-three words. Pattern: *y versus x with both axes named explicitly by label*, then a one-clause note on annotation ("Some illustrative occupations are highlighted"). "Some illustrative" is a hedge in a caption — it tells the reader the labelled points were chosen to illustrate, not sampled, so no inference should be drawn from which occupations are named. The x-axis unit (dollars, annual) is in the variable name; the y-axis unit is spelled out as a share of conversations again. No trend line is claimed and none is described.

### Exhibit 5 — augmentation and automation shares

> **The percentage of conversations with Claude that involved augmentation versus automation, and the breakdown of task subtypes within each category. Subtypes are defined in our paper as follows. Directive: Complete task delegation with minimal interaction; Feedback Loop: Task completion guided by environmental feedback; Task Iteration: Collaborative refinement process; Learning: Knowledge acquisition and understanding; Validation: Work verification and improvement.**

**Annotation.** The longest caption, because it carries the taxonomy. Pattern: what is plotted and in what units (first clause), what the sub-bars are (second clause), then a definition list for all five subtypes with the source of the definitions named ("defined in our paper as follows"). The definitions are given in the caption rather than the body so that the figure is self-contained if lifted — which is exactly what happens to this chart. Each gloss is a noun phrase of four to seven words, no verbs, parallel in form. This is the caption to imitate when a figure introduces a classification the body text has not fully enumerated.

**The caption pattern in summary.** Bold, no number, no title-case; one sentence of *what is plotted in what unit for what sample*, one optional sentence of *what the colours or marks are*, provenance of any external benchmark inside parentheses, definitions appended when the figure carries a taxonomy, hedges preserved ("relevant", "illustrative"). "Claude" appears in every single caption; "AI" appears only in the topic phrase of the first.

## Limitations

The whole passage, verbatim, under its own H3 inside Results:

> ### Caveats

> Our study provides a unique glimpse into how AI is changing the labor market. But as with all studies it has important limitations. Some of these include:

> - We can't know for certain whether someone using Claude for a task was completing a task for work. Someone asking Claude for writing or editing advice *could* be doing so at work, but they could also be doing so for the novel they're writing as a hobby.
> - Relatedly, we don't know *how* the users were using the responses from Claude. Were they, for instance, copy-pasting code snippets? Were they fact-checking responses or accepting them uncritically? Some of what appears in our data to be automation could, in fact, be augmentation: for example, a user might ask Claude to write a full memo for them (which would appear as automation), but then edit it themselves afterwards (which would be augmentation).
> - We also only analyze data from Claude.ai Free and Pro plans, rather than API, Team, or Enterprise users. While Claude.ai data contains some non-work conversations, we used a language model to filter this data to only contain conversations relevant to an occupational task, which helps to mitigate this concern.
> - The sheer number of different tasks means it is possible that Clio classified some conversations incorrectly (please see the full paper, in particular Appendix B, for details on how we validated the analysis);
> - Claude can't generate images (except indirectly via code), and so some creative uses won't be referenced in the data;
> - Given that Claude is advertised for use as a state-of-the-art coding model, we might expect coding to be overrepresented as a use case. For that reason, we don't argue that the uses in our dataset are a representative sample of AI use in general.

A seventh limitation is stated in the conclusion rather than here:

> Our research gives data on how AI is being used, but it doesn't provide policy prescriptions.

**Annotation.**

- **Where it sits.** Under Results, after all four findings and before the conclusion — so the reader meets the caveats while the numbers are still on the screen, and the conclusion is read *through* them. The heading is "Caveats", not "Limitations"; the register is conversational but the content is not softened. Nothing is hidden in a footnote and nothing is deferred to the paper except the validation evidence.
- **The framing sentences.** "Our study provides a unique glimpse into how AI is changing the labor market. But as with all studies it has important limitations." The first sentence re-asserts the contribution, the second generalises the existence of limits ("as with all studies") — that second move is the ritual part, and it is the only ritual part. "Some of these include" concedes the list is not exhaustive, which is honest and also unfalsifiable; a referee would ask which ones were left out.
- **How specific.** Particular, not ritual, in five of six bullets. Each names a concrete mechanism and, where possible, a worked counter-example: the hobby novelist for the work-relevance problem; the copy-pasted code snippet and the edited memo for the response-use problem; image generation for the coverage gap. The memo example is the strongest thing in the passage — it names the *direction* of the bias ("Some of what appears in our data to be automation could, in fact, be augmentation"), which is what makes a limitation actionable rather than decorative. Bullet three states the coverage boundary as an enumerated exclusion (API, Team, Enterprise named individually) and then attaches its own mitigation in the same bullet, with the mitigation's mechanism stated ("we used a language model to filter"). Bullet four points at a specific appendix by letter for the validation the bullet does not contain.
- **Which bullets are weakest.** Bullet four asserts classification error is "possible" without a rate or a bound, and outsources the answer. Bullet five is the least consequential (image generation) and sits alongside the most consequential, unranked — the list is not ordered by severity, which a referee would raise. The passage also gives no minimum detectable effect, no sampling uncertainty, and no statement of how many conversations survived the occupational-relevance filter.
- **What the last bullet achieves.** It converts a limitation into a withdrawn claim: "we don't argue that the uses in our dataset are a representative sample of AI use in general." A limitation that changes what the post is willing to assert is worth more than three that only describe noise. Copy this construction.
- **Punctuation tell.** Bullets four and five end in semicolons and bullets one to three in full stops — the list was assembled from two drafts. Immaterial, but it shows these were written as they were thought of, not generated from a checklist.

## Close

Verbatim, the three paragraphs of "Conclusions and future research", the pointer that follows them, and the "Open data and call for input" section:

> ## Conclusions and future research

> AI use is rapidly expanding, and models are becoming ever-more capable. The labor-market picture may look quite different within a relatively short time. For that reason, we'll repeat many of the analyses above over time to help track the societal and economic changes that are likely to occur. We'll regularly release the results and the associated datasets as part of the Anthropic Economic Index.

> These kinds of longitudinal analyses can give us new insights into AI and the job market. For example, we'll be able to monitor changes in the depth of AI use within occupations. If it remains the case that AI is used only for certain tasks, and only a few jobs use AI for the vast majority of their tasks, the future might be one where most current jobs evolve rather than disappear. We can also monitor the ratio of automation to augmentation, providing signals of areas where automation is becoming more prevalent.

> Our research gives data on how AI is being used, but it doesn't provide policy prescriptions. Answers to questions about how to prepare for AI's impact on the labor market can't come directly from research in isolation; instead, they'll come from a combination of evidence, values, and experience from broad perspectives. We look forward to using our new methodology to shed more light on these issues.

> Read the full paper for more details of our analyses and results.

> ## Open data and call for input

> The most important contribution of this paper, and of the Anthropic Economic Index, is its new methodology providing detailed data on the impacts of AI. We're immediately openly sharing the dataset we used for the above analyses, and we plan to share further such datasets as they become available in the future.

**Annotation.**

- **What was learned.** Never restated as a list. Not one of the four findings is repeated with its number in the close; the 57/43 split and the 36%/4% pair appear only as *things that can now be monitored* ("changes in the depth of AI use within occupations", "the ratio of automation to augmentation"). The close treats the findings as a baseline rather than a conclusion, which is the correct move for a first wave and the reason this post has no summary block to cut.
- **Why it matters.** Located in the conditional sentence, which is the best sentence in the close: "If it remains the case that AI is used only for certain tasks, and only a few jobs use AI for the vast majority of their tasks, the future might be one where most current jobs evolve rather than disappear." Two hedges in one sentence ("If it remains the case", "might be"), a stated antecedent that is exactly Finding 2, and a consequent in the vocabulary a policy reader cares about (evolve versus disappear). The stake is drawn out of the finding by conditional extrapolation, and the conditionality is never dropped. This is how to write why-it-matters without overclaiming: state the inference, state what it depends on, keep the modal verb.
- **What comes next.** Concrete and committal: repeat the analyses, release results and datasets regularly, monitor two specific quantities (depth within occupations; the automation-to-augmentation ratio). Both are named, so a later report can be held to them — and the March, April and September 2025 reports are the discharge of exactly this promise. Note the asymmetry: the *method* is promised, the *direction of the result* is not.
- **Recommendation.** A refusal, not a prescription. "Our research gives data on how AI is being used, but it doesn't provide policy prescriptions." The reasoning is given rather than asserted — answers "can't come directly from research in isolation; instead, they'll come from a combination of evidence, values, and experience from broad perspectives" — and the practical recommendation is displaced onto the reader as an invitation (the open dataset, the feedback form). The only thing recommended is participation.
- **How it avoids a template summary.** Four ways worth copying. (1) No numbers in the close at all. (2) Every paragraph's first sentence is about the world, not about the post: "AI use is rapidly expanding"; "These kinds of longitudinal analyses can give us new insights"; "Our research gives data on how AI is being used, but…". (3) The close names the limit of its own genre (no policy prescriptions) before it names its ambition. (4) The claim to contribution is deferred to a separate section and phrased about the method rather than the results — "The most important contribution of this paper, and of the Anthropic Economic Index, is its new methodology". A launch post ends by saying the instrument matters more than this reading of it.
- **Title against ending.** Title: "The Anthropic Economic Index" — an instrument, not a finding. Ending: the Index will be repeated, released and extended, and the methodology is the contribution. The two match exactly, and that is why the post can carry four findings without any of them being promoted into the title. The lesson for a single-finding post is the inverse: if the title names a finding, the close must end on that finding's consequence.
- **First person.** Used throughout the close for institutional commitments ("we'll repeat", "We'll regularly release", "We're immediately openly sharing", "We look forward to"). Our house style forbids it; the substitute is to state the commitment in the passive or to attribute it to the series. The rhetorical work being done — a promise that binds the author — has to be replaced, not merely de-personalised.

## Verification

- **URL fetched:** https://www.anthropic.com/news/the-anthropic-economic-index — fetched 2026-09-16, returned in full (title "Introducing the Anthropic Economic Index \ Anthropic", dated "Feb 10, 2025" on the page). Every quotation in this file was copied from that fetch and checked back against it word by word after transcription.
- **Fetch date:** 2026-09-16.
- **PDF or appendix:** none exists for this slug; the `wiki/INDEX.md` row carries `—` in the PDF column. Nothing was missing.
- **Not fetched, deliberately:** the companion paper (http://arxiv.org/abs/2503.04761 and its PDF), which is a separate corpus slug, `economic-index-2025-02-paper`; the Clio post (https://www.anthropic.com/research/clio), slug `clio-insights-2024-12`; the Hugging Face dataset card; the QJE article; the Economic Futures page; the feedback form; the two job postings. No content from any of them is quoted here.
- **Could not fetch:** nothing. No fetch failed.
- **Quotation caveats.** Hyperlink URLs were stripped from quoted prose and the anchor text retained; the anchors are listed in `## Opening move`. Typographic apostrophes and quotation marks in the source were normalised to ASCII in this file; no word was changed. Emphasis (italic, bold) is reproduced as it appears in the fetched text. Image **alt text** is not caption text: where alt text is the only source of a number — the 3.4% workforce share for computer and mathematical, the 9.1% for transportation, the $60,070 median-wage reference line, the 57.4%/42.6% and subtype percentages on the last exhibit — it is identified as alt text in the annotation and is never quoted as prose. The bold sentences under each image are the on-page captions and are quoted as such.
- **Scope.** This file annotates how the piece is written. It makes no judgement about whether its findings are correct.
