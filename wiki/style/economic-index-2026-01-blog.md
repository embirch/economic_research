# economic-index-2026-01-blog — style annotation

## Source

- **Title on page:** "Anthropic Economic Index: New building blocks for understanding AI use" (H1). Browser/OG title is shorter and drops two words: "Economic Index: New building blocks for AI use". The H1 keeps "understanding" — the post is about an instrument for understanding, not about AI use itself, and the H1 is the version the close matches.
- **Date on page:** "Jan 15, 2026".
- **Primary URL fetched:** https://www.anthropic.com/research/economic-index-primitives
- **Category label above the H1:** "Economics". No named authors anywhere on the page; no acknowledgements section; no "Work with us" block. This is the leanest of the Economic Index companion posts.
- **Other URLs it points at (not fetched for this file):** the fourth report at https://www.anthropic.com/research/anthropic-economic-index-january-2026-report (own slug `economic-index-2026-01-report`), the Clio post, Claude.ai, the first three Index publications (`the-anthropic-economic-index`, `impact-software-development`, `economic-index-geography`), the productivity-gains post (https://www.anthropic.com/research/estimating-productivity-gains), METR's site and its task-horizons blog post, an NBER working paper (w32966), a Microsoft New Future of Work report, the Rwandan-government partnership announcement, and Webb's patent paper (footnote 3).
- **PDF or appendix:** none. The `wiki/INDEX.md` row carries `—` in the PDF column; all depth is delegated to the report, which has its own 55-page PDF under its own slug.
- **Document type:** companion blog to a report published the same day. It does one job: summarise the report for a reader who will not open it. The framing sentence is explicit — "Below, we summarize its results." This is the *summary-companion* variant of the form, and it is the closest genre in the corpus to a post that has to carry six findings at a readable length.
- **Approximate length:** roughly 2,150 words of body prose, plus five figure captions (~250 words) and three footnotes (~400 words, of which footnote 2 is a five-item definition list). Six images: one uncaptioned hero, five captioned exhibits. Two H2 sections of substance plus a Conclusion; three H3s and five H4s beneath the first H2.
- **Audience:** general — "researchers, journalists, and the public" is the page's own enumeration, in that order. Written for a reader who is told the name of a new construct, given one sentence of gloss, and trusted to accept it; the definitions are in the footnote and the validation is in the report.

## Section order

Headings in order, with what each does and how long it runs.

1. **Category "Economics" + H1 + "Jan 15, 2026" + "Read the full report" link + hero image.** The report link sits above the article, in the same position the February 2025 post gave "Read the paper". Same signal: this page is an entry point, not the record. The hero image carries no caption.
2. **Untitled opening (no heading)** — five paragraphs, ~380 words. Three questions; the standing measurement programme and its two data sources; the new construct named and enumerated; what the construct buys; the pointer to the report. No bullet list, no findings summary — the sharpest structural break from `economic-index-2025-02-report`, which put its three headline numbers in bullets 150 words in. Here the first finding number arrives only after the opening ends.
3. **H2 "What we've learned from our economic primitives"** — one paragraph, ~50 words: the three-level ladder the section will climb (tasks → occupations → aggregate impacts) and a parenthesis delegating methodology to chapter two of the report. The whole method section of the February 2025 post is replaced by one parenthesis.
   - **H3 "Tasks"** — no prose of its own, three H4s beneath it.
     - **H4 "Which tasks does AI speed up, and by how much?"** — ~200 words, two paragraphs, then the figure and caption. Finding, then robustness, then implication.
     - **H4 "What are the time horizons over which Claude can support tasks?"** — ~320 words: external benchmark set up, figure and caption, then the comparison and *then* two paragraphs of caveat. The longest H4, and the only one where the caveat is longer than the finding.
     - **H4 "How does the nature of Claude's work vary across countries?"** — ~200 words, two paragraphs, then figure and caption. The only finding on the page stated with no number at all.
   - **H3 "Occupations"** — no prose of its own, two H4s.
     - **H4 "Coverage"** — ~180 words: the updated headline number, the new adjusted measure, figure and caption, then a standalone limitation paragraph.
     - **H4 "Task content"** — ~250 words: the skill-content finding, figure and caption, then the deskilling counterfactual and its disclaimer.
   - **H3 "Aggregate impact"** — ~250 words, three paragraphs, **no H4 and no figure**. The structural asymmetry is deliberate: the two levels that rest on the new primitives get question-headings and exhibits; the level that rests on a model inherited from earlier research gets neither.
4. **H2 "Updates on our previous measures"** — ~320 words: one framing paragraph plus three paragraphs ordinal-marked "First," "Second," "Third,". Everything continuous with the earlier reports is quarantined here, after everything new.
5. **H2 "Conclusion"** — three paragraphs, ~280 words. What the report showed, what the next reports will measure, and an invitation.
6. **H4 "Footnotes"** — three. Footnote 1 is the sample. Footnote 2 is the full definition list of all five primitives. Footnote 3 is a historical-evidence citation attached to the deskilling paragraph.

**Where the findings sit:** after the method framing and nowhere else. There is no abstract, no bullet summary and no restatement in the close — the reverse of the February 2025 arrangement, where the findings appeared twice. Each finding appears exactly once, under a heading that asks it as a question. **The question headings are the summary block**: a reader who scans only the H4s gets "Which tasks does AI speed up, and by how much?", "What are the time horizons…", "How does the nature of Claude's work vary across countries?" — three questions, no answers, and no number they could carry away wrongly. This is the device to copy when house style forbids a summary block.

**Where the caveats sit:** each beside its own finding, in the paragraph immediately after it, with no "Caveats" or "Limitations" heading anywhere on the page. Also the reverse of February 2025, where six caveats were pooled at the end of Results and the challenge to a finding sat 400 words from the finding. This placement is better and is the one to imitate.

## Opening move

Verbatim, the five paragraphs of the untitled opening (hyperlink URLs stripped; anchor text retained and listed below; footnote markers removed):

> Is artificial intelligence really making people faster at work? What sort of tasks does AI support best? And how might it change the nature of people's occupations?

> At Anthropic, we're measuring real-world AI use on an ongoing basis to answer questions exactly like these. Our privacy-preserving analysis method allows us to learn more about conversations on Claude.ai (capturing uses by consumers) and our first-party API (mostly capturing uses by businesses). In past reports, we've assessed AI tasks by occupation and wage level, looked more closely at software development, and studied AI use by country and by US state.

> We're now adding a new level of detail to our Economic Index. In our fourth report, we're introducing what we've called **economic primitives**: a set of five simple, foundational measurements to track the economic impacts of Claude over time. Our initial set includes task complexity, skill level, purpose (work, education, or personal use), AI autonomy, and success. We derive these primitives from asking Claude to answer a common set of questions about every conversation in our sample for this report.

> These primitives provide a leading indicator of AI's potential economic impacts—and allow us to answer far more complex questions about how AI is already changing jobs. Our latest report, which samples conversations from November 2025 (predominantly using Claude Sonnet 4.5), uses our primitives to explore a wide range of questions that we wouldn't otherwise be able to answer—including how Claude's task-level success rates change for more complex tasks, and whether the use of Claude to date might portend a net-deskilling effect on many jobs.

> You can read the fourth Economic Index report here. Below, we summarize its results.

Anchor text carrying links, in order: "analysis method" → the Clio post; "Claude.ai" → claude.ai; "occupation and wage level" → the first report; "software development" → the April 2025 report; "by country and by US state" → the September 2025 blog; "here" → the fourth report.

**Annotation.**

- **What question is posed.** Three, in the first twenty-eight words, all with question marks, all about **AI** rather than Claude: is it making people faster, what does it support best, how might it change occupations. The move is *question → therefore instrument*, where February 2025 was *forecast → therefore measure*. The three questions map one-to-one onto the three levels of the body (tasks/speedup, tasks/coverage, occupations), so the opening is a table of contents disguised as curiosity. Note "really" in the first question: it concedes that the reader has heard the claim already and is entitled to doubt it. That single adverb does the work that a paragraph of stakes-setting does elsewhere, and it is the cheapest honest opening in the corpus.
- **Who is said to be affected.** "people work", "people's occupations" — the workforce in the aggregate, unmodified, as in February 2025. Nobody is named as harmed or helped. The one named population anywhere in the post is the Rwandan partnership's participants, and they appear as beneficiaries of a programme, not as a measured group.
- **What the data is said uniquely to show.** No superlative at all. There is no "first-of-its-kind", no "clearest picture yet". The uniqueness claim has migrated into the construct: the primitives "allow us to answer far more complex questions about how AI is already changing jobs" and "provide a leading indicator". Claiming novelty for the *measurement* rather than for the *finding* is the same discipline as February 2025, executed with a quieter vocabulary.
- **How soon the first number appears.** The first quantity is "five" — the count of primitives, para. 3, ~150 words in — and the first *finding* number ("a factor of 9") is roughly 480 words in, under the first H4. Longer than any other opening in the corpus. The reader is asked to accept a new construct before being shown anything it produced.
- **Register details worth copying.** First person plural throughout, and only for institutional acts and choices: "we're measuring", "we're introducing", "what we've called", "We derive these primitives from", "we summarize". No finding is in the first person. The AI/Claude alternation is set up in the first two paragraphs and holds for the whole page: the questions ask about *artificial intelligence* and *AI*; the sentence that says what is actually observed says *Claude.ai* and *our first-party API*. The two-source description is itself a hedge in apposition — "(capturing uses by consumers)" and "(mostly capturing uses by businesses)", with "mostly" on the second and not the first.
- **The lineage sentence.** "In past reports, we've assessed AI tasks by occupation and wage level, looked more closely at software development, and studied AI use by country and by US state." Three prior publications compressed into one sentence of three verb phrases, each hyperlinked, in publication order, with no findings attached. This is how a fourth instalment claims its thread in twenty-eight words. A post of ours that positions itself against a named Anthropic thread should copy the shape exactly: what the earlier work looked at, never what it found.
- **The pointer sentence.** "Below, we summarize its results." Flat, four words of subject and verb, no hedging and no promise. It also tells the reader the page holds no claim the report does not — which is what licenses the absence of a method section.

## Findings and their caveats

### How a new measure is introduced to a general reader

> In our fourth report, we're introducing what we've called **economic primitives**: a set of five simple, foundational measurements to track the economic impacts of Claude over time. Our initial set includes task complexity, skill level, purpose (work, education, or personal use), AI autonomy, and success. We derive these primitives from asking Claude to answer a common set of questions about every conversation in our sample for this report.

**Annotation.** The four-move introduction of a coined construct, in three sentences: (1) **name it as coined** — "what we've called", which marks the term as the authors' own and not a term of art the reader should recognise; (2) **gloss it by count and purpose** before any content — "a set of five simple, foundational measurements to track the economic impacts of Claude over time"; (3) **enumerate the members in one flat list**, no sub-clauses, one parenthetical gloss where a name is opaque ("purpose (work, education, or personal use)"); (4) **state the derivation in one sentence** — "asking Claude to answer a common set of questions about every conversation" — so the reader knows immediately that these are model-generated estimates, not instrumented measurements. Full definitions are displaced to footnote 2. "Initial set" is a hedge in an adjective: the taxonomy is declared incomplete at the moment of its introduction.

**Two cautions, both of which we must not inherit.** The body list renames two of the five relative to the page's own footnote 2 — "skill level" for *Human and AI skills*, "purpose (work, education, or personal use)" for *Use case* — and shortens *Task success* to "success". Quote footnote 2 or the report, never the body list. And the page twice calls the sample a "survey" ("since our survey"; "our future surveys"); the sample is a random draw of transcripts. See `/mnt/memory/standards/terminology.md`.

Operationalisation is also always stated before the number it produces, in the reader's units:

> We measure this by what Claude estimates as the number of years of schooling required to understand the conversation's inputs: in Claude.ai, tasks with prompts requiring a high school education (12 years) were sped up by a factor of 9, while those requiring a college degree (16 years) were sped up by a factor of 12.

**Annotation.** "what Claude estimates as" is the provenance fence, placed inside the definition of the variable rather than appended to the result — the reader cannot use the number without carrying the fact that a model produced it. The scale is then anchored at two points the reader already owns (high school, college degree) with the raw units in parentheses, not the reverse. Later the same device: "14.4 years of education (equivalent to a US associate's degree)". Translate the unit, keep the number.

### Finding 1 — complexity and speedup

> We found that more complex tasks were sped up the most by Claude. We measure this by what Claude estimates as the number of years of schooling required to understand the conversation's inputs: in Claude.ai, tasks with prompts requiring a high school education (12 years) were sped up by a factor of 9, while those requiring a college degree (16 years) were sped up by a factor of 12. (On the API, the speedup was greater still.) These results imply that AI's productivity gains are currently accruing in tasks that require relatively high human capital, which is consistent with the evidence that white collar professionals are more likely to use AI at work.

> This same trend holds—albeit in weaker form—when we adjust for tasks' success rates. Claude successfully completes tasks that require a college degree 66% of the time, compared to 70% for those tasks that require less than a high school education. This reduces, but doesn't eliminate, the overall effect: Claude's impact on task speedup scales more sharply with complexity than complexity correlates with a decrease in success rate.

**Annotation.** The claim sentence names Claude as the agent ("sped up the most by Claude"); the inference sentence names AI ("AI's productivity gains are currently accruing…"). That is the page's standing rule and its one soft spot: the inference generalises from a Claude measurement to AI in general, and the only thing holding it back is the verb "imply" plus an external corroboration ("which is consistent with the evidence that…", hyperlinked to an NBER paper). A referee would say a corroborating citation is not a warrant for the generalisation; our version of this sentence must stay on Claude or state the extrapolation as an assumption.

The second paragraph is the piece of this post most worth copying: **the robustness check is given as a finding, with its own numbers, and its effect on the headline is quantified in words.** "This same trend holds—albeit in weaker form—" states the direction and the attenuation before the evidence; "66% of the time, compared to 70%" gives both arms of the comparison rather than a difference; "This reduces, but doesn't eliminate, the overall effect" tells the reader exactly how much of the finding survives. The closing clause is a statement about which of two gradients is steeper — a comparison of slopes stated without a single coefficient. No standard errors, no sample sizes, no confidence intervals appear anywhere on the page; that is the form's limit, not a model for us.

"(On the API, the speedup was greater still.)" — a direction with no magnitude, in parentheses. Honest and cheap: it tells the reader the second platform agrees without committing to a number the blog has no room to defend.

### Finding 2 — time horizons, against METR

> METR's benchmark suggests that Claude Sonnet 4.5 (the model in our own analysis) achieves 50% success rates on tasks of 2 hours. By contrast, our own API data finds that Claude is 50% successful at tasks that take nearly twice as long (around 3.5 hours), and on Claude.ai, the duration is vastly longer still—around 19 hours. But this might not be as discordant as it seems: our methodology is different to METR's in some important ways. In our sample, users can break down complex tasks into smaller steps, creating a feedback loop that allows Claude to correct course. And rather than a fixed set of tasks, our sample contains a form of selection bias: users bring tasks to Claude that they're more confident will work.

> Our analysis shows how Claude's *effective* time horizons might look different to those found in a study with a consistent set of tasks. We'll track this indicator in further reports.

**Annotation.** The most disciplined passage on the page, and the template for reporting a number that disagrees with someone else's. Its order: **hold the model constant** (the same Claude Sonnet 4.5 is on both sides, stated parenthetically so the comparison cannot be dismissed as version drift) → **state the external number** → **state ours, both platforms, with the ratio in words** ("nearly twice as long", "vastly longer still") and the magnitudes in parentheses → **refuse the exciting reading in the same paragraph** ("But this might not be as discordant as it seems") → **name two mechanisms for the gap, one favourable and one unfavourable to us**. The unfavourable one is named as what it is — "our sample contains a form of selection bias" — in the authors' own voice, unhedged, before anybody else can say it. Naming your own selection problem in the sentence that follows your largest number is the single most transferable move in this file.

The italic on *effective* in the next paragraph does the rest of the work: it narrows the construct so that "19 hours" cannot be read as a capability claim. The finding is then demoted to an "indicator" to be tracked, which is what a number with an unquantified selection problem is worth. Note also "around 3.5 hours" and "around 19 hours" — approximation markers on both, where 66% and 70% a section earlier carry none. Precision is granted to within-sample comparisons and withheld from cross-study ones.

### Finding 3 — use case across countries

> We find that Claude completes very different kinds of tasks in countries at different stages of economic development. In countries with higher GDP per capita, Claude is used much more frequently for work or for personal use—whereas countries at the other end of the spectrum are more likely to use it for educational coursework. This fits a straightforward "adoption curve" story, in which lower-income countries show a large share of AI use on education and on a smaller number of work tasks, while AI use diversifies towards personal purposes as countries become richer.

> These results align with recent work by Microsoft that associates AI use in education with lower per-capita income, and AI use for leisure with higher incomes.

**Annotation.** A whole finding with no number in it — the quantities live only in the figure and its axes. The relationship is given as a direction ("much more frequently", "more likely"), the covariate is named ("GDP per capita"), and no slope, correlation or significance is offered. Defensible here because the claim is monotone and the exhibit is three panels; not defensible for us, where the ratio or the slope has to be in the prose.

The conjecture is fenced three ways at once: "This **fits** a **straightforward** "**adoption curve**" **story**" — a verb that claims consistency rather than support, an adjective conceding the account is the obvious one, and scare quotes marking the label as borrowed rather than established. The corroboration then comes from a competitor's research, which is the strongest available form: an independent instrument, different sample, same gradient. What the passage does not do is test any alternative explanation (price, connectivity, language, tier mix), and it does not claim to have.

The paragraph that follows, on the Rwandan partnership, is the one place where the post advertises: a product programme presented as a response to the finding. It is the clearest thing in the corpus to avoid — a recommendation to ourselves, stated as already implemented, in the middle of the findings.

### Finding 4 — occupational coverage, adjusted for success

> In our first report, with data from January 2025, we found that 36% of jobs in our sample saw Claude being used for at least a quarter of their tasks. Pooling data across reports, this has risen to 49%. But once we account for Claude's *success* *rate* (which we weight according to how often workers do that task and how long the task takes), we get a different picture of which jobs are most affected by the use of AI.

> On the graph below, we plot that earlier measure of occupations' task coverage along the *x* axis, and our new, adjusted measure on the *y* axis. Although the two are certainly correlated, we now find that some occupations (like data entry keyers and radiologists) are much more heavily affected by AI than task coverage alone would suggest, while others (like teachers and software developers) are relatively less affected.

> That said, even our revised assessment is still limited: we only assess tasks that are performed on Claude.ai, and it's not always clear how these conversations might map onto changes in the real world. This is an area we plan to dig into further in future.

**Annotation.** The construction to study is **old measure → new measure → what changes**. The 36% is re-quoted with its provenance and vintage attached ("In our first report, with data from January 2025") so the reader can see which number moved; the new measure is defined by its weighting in a parenthesis ("how often workers do that task and how long the task takes") before it is used; and the payoff is not a number but a re-ranking, carried by four named occupations in two pairs — data entry keyers and radiologists up, teachers and software developers down. Naming occupations the reader can picture, two on each side, does more than any correlation coefficient would.

Two weaknesses a referee raises immediately. First, "Pooling data across reports, this has risen to 49%" compares a single-sample figure with a pooled-across-samples figure; pooling mechanically raises coverage by accumulating rare tasks, and the page neither decomposes the 13-point rise nor flags the asymmetry. If we write a sentence of this shape, the like-for-like statement has to be in it. Second, "some occupations … are much more heavily affected by AI" says AI where the measurement says Claude.ai — the naming rule slips precisely where the claim is strongest.

The limitation paragraph is the model for placement: a separate paragraph, immediately after the exhibit, opening with "That said," and closing on what will be done about it. "it's not always clear how these conversations might map onto changes in the real world" is the honest core of the entire Economic Index, stated in one clause and not repeated.

### Finding 5 — task content and the deskilling counterfactual

> A further question we asked is whether the tasks that AI covers represent the higher- or the lower-skilled components of a given occupation. Using an estimate that we create of the skill level required for each task, we find that Claude is relatively more likely to cover the tasks that require *higher* education levels—specifically, tasks that require an average of 14.4 years of education (equivalent to a US associate's degree), relative to the economy's average of 13.2 (shown below). This aligns with our earlier finding that Claude is used more frequently by white-collar workers.

> As an experiment, we estimated how removing these Claude-covered tasks would shift the task composition of people's jobs. As a first-order effect, this would *deskill* jobs on average, since it would remove those higher-education tasks. Professions like technical writers, travel agents, and teachers would be affected (as we discuss further in the report), though a rarer few (like real estate managers) would see effects going the other way.

> We're not necessarily *predicting* that this deskilling will occur: it's possible that *even if* AI fully automated the tasks it currently supports, the labor market would dynamically adjust in ways that this analysis doesn't account for. (Of course, as models improve, the composition of tasks that AI covers will change, too.) That said, we think this offers a useful signal as to the most immediate effects that AI might have on occupations in the near future.

**Annotation.** "Using an estimate that we create of the skill level required for each task" — the construct is flagged as constructed, in the same clause as the result, before the result. 14.4 against 13.2 is the whole finding: two means, the comparison group named as "the economy's average", the difference left for the reader. 1.2 years of schooling is a small gap stated without an adjective, which is the right treatment of a small gap.

The counterfactual is the most carefully fenced passage on the page and the one to imitate when reporting an arithmetic what-if. Four fences in sequence: **"As an experiment"** (the status of the exercise, first word); **"As a first-order effect"** (the order of approximation); **"on average"** with the exception immediately supplied and named ("though a rarer few (like real estate managers) would see effects going the other way"); and then the explicit withdrawal — **"We're not necessarily *predicting* that this deskilling will occur"** — with the reason given as a named omitted mechanism, not a shrug ("the labor market would dynamically adjust in ways that this analysis doesn't account for"). The italics carry the fences: *predicting*, *even if*. A counterfactual that says in its own voice which mechanism it omits is worth more than one hedged with "may".

What is missing, and what a referee raises: the whole result is a function of one construct — predicted years of schooling per task — and the page never says whether the sign survives a different skill measure. (The report does raise this; the blog drops it.) A construct-dependent result needs one sentence saying so.

### Finding 6 — aggregate productivity

> Based on our estimates of task speedups alone, we replicated our earlier finding of a 1.8 percentage point increase (even when we added in our API data). But when we account for task *reliability*—that is, when we adjust our estimate of task-level time savings by the probability that the task is *successful*, our estimate falls by about one-third for tasks completed on Claude.ai (to 1.2 percentage points per year), and by slightly more (to 1.0 percentage points) for the typically more challenging tasks completed on our API.

> Even a 1 percentage point increase in annual labor productivity growth would still be notable: it would return US productivity growth to the rates of the late 1990s and early 2000s. And, as we mentioned in our earlier research, this top-line estimate does not account for the possibilities that AI models become much more powerful, or that the use of AI at work becomes much more sophisticated—which could push the number much higher.

**Annotation.** Replication stated before revision: the old number is reproduced first ("we replicated our earlier finding of a 1.8 percentage point increase"), including under the new data, and only then adjusted downward. That order is the house requirement in our own criteria, and this is the corpus's clearest example of it. The adjustment is reported as both a proportion and a level ("falls by about one-third … to 1.2 percentage points per year"), which lets the reader check the arithmetic against the 1.8. The lower API figure is explained in the same clause by a property of the sample ("the typically more challenging tasks completed on our API"), not left as an unexplained platform difference.

The second paragraph is how to keep a revised-down number meaningful without re-inflating it: instead of an adjective, a **historical benchmark** — a 1pp increase "would return US productivity growth to the rates of the late 1990s and early 2000s". The reader is given a period, not a superlative.

The referee's point is the asymmetry of what follows. Only the upside omissions are listed ("could push the number much higher"); no downside is named on this page, and the report's task-complementarity range, which runs below 1.0pp, is absent entirely. A sentence that lists the reasons an estimate could be too low must list the reasons it could be too high, or it is advocacy.

### The "Updates on our previous measures" block

> First, we find that the use of Claude has remained highly concentrated among certain tasks: even though our sample includes 3,000 unique work tasks on Claude.ai, the top ten account for 24% of the set, which has steadily increased from 21% in January 2025.

> Second, our new report finds that augmentation (52% of conversations) has overtaken automation (45%) as the most popular pattern of interaction with Claude on Claude.ai. This is a reversal of what we saw in our August sample (when automation led by 49% to 47%), but, when we assess this question over a longer time-frame, we still see a slow rise in *automation*'s share of tasks: augmentation led by 55% to 41% in January of last year, and by 55% to 42% in March.

> Third, our latest analysis shows that the geographic concentration of AI use (as we discussed last time) remains evident. The US, India, Japan, the UK, and South Korea still lead in overall Claude.ai use, and adoption remains well-explained by GDP per capita. That said, in the US, we've observed greater changes: Claude use has become noticeably more evenly distributed across US states. In fact, if this trend was sustained, our model predicts that Claude use would be equalized across the country within two to five years.

**Annotation.** The framing sentence sets expectations downward before any of the three: "Here, we mostly find only small evolutions from the results of previous analyses". Continuity is reported as continuity, which is what makes the one genuine change stand out.

"Second," is the best short lesson in the corpus on **not letting a reversal become the story**. The headline reversal is stated (52 over 45, against August's 49 over 47), and then immediately subordinated to the longer series in the same sentence — "but, when we assess this question over a longer time-frame, we still see a slow rise in *automation*'s share" — with the four earlier readings supplied so the reader can see the trend the single flip contradicts. A one-period reversal inside a multi-period trend is reported with the trend attached. Copy this.

Two things not to copy. The shares do not sum to 100 (52 + 45), and the page never says why, so a reader is left to infer a residual category that is never named; when we quote a collaboration-mode split, the unclassified remainder is stated. And "our model predicts that Claude use would be equalized across the country within two to five years" is the most assertive sentence on the page, resting on a three-month change under a convergence model that is described nowhere here — the conditional "if this trend was sustained" carries the whole load, and it is not enough.

**Naming discipline across all findings.** The rule holds with three exceptions. **AI** is the subject of every question heading and of every sentence about the phenomenon or the economy: "Which tasks does AI speed up, and by how much?", "the geographic concentration of AI use", "the impact of AI on the global workforce". **Claude** is the subject or object of every sentence with a measurement attached: "sped up the most by Claude", "Claude successfully completes tasks … 66% of the time", "Claude use has become noticeably more evenly distributed", "3,000 unique work tasks on Claude.ai". The exceptions are all inferences one step beyond the data — "AI's productivity gains are currently accruing in tasks that require relatively high human capital", "much more heavily affected by AI than task coverage alone would suggest", "removing these Claude-covered tasks" followed by "even if AI fully automated the tasks it currently supports". Each is marked as an implication or a counterfactual, and each is a place where our own rule would require Claude.

## Comparisons

Every place where a comparison carries the finding.

### Against an outside laboratory's benchmark

> METR's benchmark suggests that Claude Sonnet 4.5 (the model in our own analysis) achieves 50% success rates on tasks of 2 hours. By contrast, our own API data finds that Claude is 50% successful at tasks that take nearly twice as long (around 3.5 hours), and on Claude.ai, the duration is vastly longer still—around 19 hours.

**Annotation.** The comparison is constructed so it can be read: the same success threshold on both sides (50%), the same model named on both sides, one axis (hours) and three values. The disagreement is large — roughly 2, 3.5 and 19 hours — and the prose gives the ratios in words before the magnitudes in parentheses, so a reader who takes nothing else away takes "nearly twice" and "vastly longer". Setting up a disagreement with an external estimate by first equalising everything that could explain it away is what makes the two named mechanisms that follow credible rather than defensive.

### Against the team's own earlier numbers

> In our first report, with data from January 2025, we found that 36% of jobs in our sample saw Claude being used for at least a quarter of their tasks. Pooling data across reports, this has risen to 49%.

> Based on our estimates of task speedups alone, we replicated our earlier finding of a 1.8 percentage point increase (even when we added in our API data).

> augmentation led by 55% to 41% in January of last year, and by 55% to 42% in March.

**Annotation.** Three self-comparisons, three different jobs: an update (36 → 49), a replication (1.8 reproduced before being revised), and a time series quoted at four points to contextualise a reversal. In every case the earlier number is quoted with the report and the month it came from. The rule visible here: **never compare to your own past number without naming which publication and which sample month it came from** — and, where the basis changed, say so ("Pooling data across reports", which this page states but does not adjust for).

### Across platforms, as a proxy for consumer versus business

> Our privacy-preserving analysis method allows us to learn more about conversations on Claude.ai (capturing uses by consumers) and our first-party API (mostly capturing uses by businesses).

> our estimate falls by about one-third for tasks completed on Claude.ai (to 1.2 percentage points per year), and by slightly more (to 1.0 percentage points) for the typically more challenging tasks completed on our API.

> We also expect that tasks might move from Claude.ai to the API (that is, from predominantly consumers to predominantly businesses) as they become more reliable

**Annotation.** The page's structural comparison, and the best argument in the corpus for **one claim tested at more than one level**: the same primitive is reported for both platforms in findings 1, 2 and 6, the two platforms are glossed as two populations, and the close then converts the split into a forward-looking indicator. The gloss is re-stated in parentheses each time it matters rather than assumed from the opening — and the hedge "mostly"/"predominantly" is re-stated with it every single time. A proxy that is restated with its hedge at every use is a proxy a reader can hold you to.

### Against the whole economy

> tasks that require an average of 14.4 years of education (equivalent to a US associate's degree), relative to the economy's average of 13.2

**Annotation.** Two means against each other with the benchmark population named in the same clause, the unit translated once for the reader, and no adjective anywhere. The figure caption then supplies the distributions the two means came from — the prose carries the comparison, the exhibit carries the dispersion. This is the division of labour to copy.

### Against a historical period

> Even a 1 percentage point increase in annual labor productivity growth would still be notable: it would return US productivity growth to the rates of the late 1990s and early 2000s.

**Annotation.** A magnitude made meaningful by an era rather than an adjective. Note that the sentence benchmarks the *lowest* of the three estimates, not the highest — the defensive number is the one given the rhetorical support. Taking your weakest number and showing it would still matter is more persuasive than defending your strongest.

### Against the outside literature

> which is consistent with the evidence that white collar professionals are more likely to use AI at work

> These results align with recent work by Microsoft that associates AI use in education with lower per-capita income, and AI use for leisure with higher incomes.

**Annotation.** Both use the vocabulary of consistency, not of confirmation: "is consistent with", "align with". Neither claims the external work validates the measurement, and neither reports the external work's numbers. Corroboration is used to make a conjecture admissible, never to promote it to a finding. Footnote 3 does the same job in the other direction, supplying historical evidence that the deskilling channel has precedent, safely outside the body text.

### Within the data — occupation against occupation

> some occupations (like data entry keyers and radiologists) are much more heavily affected by AI than task coverage alone would suggest, while others (like teachers and software developers) are relatively less affected

> Professions like technical writers, travel agents, and teachers would be affected (as we discuss further in the report), though a rarer few (like real estate managers) would see effects going the other way

**Annotation.** Both comparisons are made entirely by naming occupations in opposed pairs or groups, with no numbers. Data entry keyers beside radiologists is the deliberate shock — the lowest- and one of the highest-paid occupations on the same side of the result — doing the same work that shampooers and obstetricians did in the February 2025 post. Choose the pair that violates the reader's prior, and say the finding once.

## Figure captions

Five captioned exhibits plus an uncaptioned hero. Captions are set in bold below the image, unnumbered, with no "Figure 1" label and no separate source line. The first sentence of each caption is a bold short title ending in a full stop, set inside the already-bold caption as a second emphasis level, and every one of the five is built the same way: **`<Y> vs. <X>.`** or **`<X> predicts <Y>.`** Then one or two sentences of what is plotted, at what unit of observation, from what source, and what the dashed line is.

### Exhibit 1 — speedup and success against schooling (two panels)

> **Speedup and success rate vs. human years of schooling.** The chart on the left shows a scatterplot of the relationship between speedup and human years of schooling, measured at the O*NET task level. The dashed lines show the line of best fit. The chart on the right shows the relationship with the success rate.

**Annotation.** Title as `Y1 and Y2 vs. X`, then panel-by-panel narration with position cues ("on the left", "on the right"), the unit of observation named once and inherited by both panels ("measured at the O\*NET task level"), and an explicit gloss of the non-data ink ("The dashed lines show the line of best fit"). The right panel is described by difference rather than repeated in full — "the relationship with the success rate" — which is how to caption a two-panel exhibit without doubling the words. Nothing about the sample, the platform or the period; the reader must take those from the body.

### Exhibit 2 — success against human-only time

> **Task success vs. human-only time.** This chart shows the relationship between task success (%) and the time the task would require a human to complete alone, all measured at the O*NET task level and split by platform. The dashed lines show the fit from a linear regression.

**Annotation.** The tightest caption of the five. Units inside the variable name ("task success (%)"), the x-variable defined rather than labelled ("the time the task would require a human to complete alone" — the counterfactual is spelled out, which is the whole content of the measure), the stratification named ("split by platform"), and the fitted line attributed to a stated method ("the fit from a linear regression") rather than to a vague "trend". Naming the estimator in the caption is the detail to carry into house style.

### Exhibit 3 — use case against income, three panels

> **Per capita income predicts how Claude is used across countries.** Each plot shows the relationship between the share of a specific kind of use (work, coursework, or personal) for Claude.ai conversations, and log GDP per capita.

**Annotation.** The only caption of the five whose title is a full sentence, and the only one with a directional verb — "predicts". It is the strongest claim in any caption on the page and it sits over the one finding with no number in the prose, which is the wrong way round: the caption is carrying an assertion the body text declined to quantify. In our own posts, a caption never states a relationship the prose has not already stated with its number. The body of the caption is otherwise exemplary: "Each plot shows" handles all three panels at once, the three categories are enumerated in the order they appear, the population is named ("for Claude.ai conversations"), and the transform is in the axis name ("log GDP per capita").

### Exhibit 4 — effective coverage against task coverage

> **Effective AI coverage vs. task coverage.** The plot shows the relationship between task effective AI coverage (%) and task coverage, measured at the occupation level. Effective AI coverage tracks the share of a worker's time-weighted duties that AI could successfully perform, based on Claude.ai data. Task coverage is the share of tasks that appear in Claude.ai usage. The dashed line shows where effective AI coverage share equals task coverage.

**Annotation.** The longest caption, because it carries two constructed measures, and the best one on the page. Its parts: title, what is plotted at what unit of observation, **then a definition sentence for each of the two axes in turn**, each ending in its data source ("based on Claude.ai data", "that appear in Claude.ai usage"), then the meaning of the reference line ("shows where effective AI coverage share equals task coverage"). The 45-degree line is defined by what it means rather than by its slope, so the reader knows without being told that distance from the line is the finding. When a figure introduces a measure the body text only names, define it in the caption — as here, and as `economic-index-2025-02-report` does with the five collaboration subtypes.

Worth noting for our own use: the axis label says "AI coverage" while the definition says the data is Claude.ai. The naming rule is broken inside the caption, which is exactly where the claims list says it must not be.

### Exhibit 5 — education distribution, all tasks against Claude-covered tasks

> **Education level of all tasks vs. Claude-covered tasks.** The blue bars give the distribution of the predicted task-level education required for all tasks in the O*NET database, weighted by employment. The orange bars show the same, restricting to tasks that appear in Claude.ai data.

**Annotation.** Two series, two colours, and the second defined entirely as a restriction of the first ("The blue bars give … The orange bars show the same, restricting to…"). Stating a comparison series as a subset of the baseline rather than describing it independently makes the comparison legible in one reading, and it makes the selection explicit. "predicted" keeps the constructed variable marked; "weighted by employment" gives the weighting in two words and applies to both series by inheritance.

**The caption pattern in summary.** Bold; no number; a bold sentence-case title of the form `Y vs. X.`; then what is plotted, at what unit of observation, from what source; a definition sentence for any constructed axis; an explicit gloss of every dashed or reference line; colour used as the series key where there are two series; panel position cues where there are multiple panels. No sample sizes, no periods, no uncertainty in any caption. Claude.ai is named in three of five captions and O\*NET in three; unlike `economic-index-2025-02-report`, **not** every caption names Claude — exhibits 1 and 2 report Claude measurements under unattributed variable names, which is a regression from the earlier post's discipline and not to be copied.

**Alt text.** None of the five captioned exhibits carries alt text in the fetched page — every one is an empty `alt` attribute. The only alt text on the page is on the uncaptioned hero image, where it repeats the H1. **No number on this page exists only in alt text**, so the `(alt text)` convention from `room/director-2026-09-16-alt-text-ruling.md` has no occasion to be used in this file. Recorded because the absence is itself a data point: the page is not readable by a screen reader at the level of any exhibit, and every number a reader can obtain from the exhibits must be read off the chart — and therefore, under the same ruling, is not recorded here at all.

## Limitations

**There is no limitations section.** No "Caveats" heading, no "Limitations" heading, no bulleted list, nothing in the conclusion. Every limitation on the page is a sentence or a paragraph adjacent to the finding it limits. In full, in page order:

On the time-horizon comparison:

> But this might not be as discordant as it seems: our methodology is different to METR's in some important ways. In our sample, users can break down complex tasks into smaller steps, creating a feedback loop that allows Claude to correct course. And rather than a fixed set of tasks, our sample contains a form of selection bias: users bring tasks to Claude that they're more confident will work.

> Our analysis shows how Claude's *effective* time horizons might look different to those found in a study with a consistent set of tasks.

On occupational coverage:

> That said, even our revised assessment is still limited: we only assess tasks that are performed on Claude.ai, and it's not always clear how these conversations might map onto changes in the real world. This is an area we plan to dig into further in future.

On the deskilling counterfactual:

> We're not necessarily *predicting* that this deskilling will occur: it's possible that *even if* AI fully automated the tasks it currently supports, the labor market would dynamically adjust in ways that this analysis doesn't account for. (Of course, as models improve, the composition of tasks that AI covers will change, too.)

On the productivity estimate:

> And, as we mentioned in our earlier research, this top-line estimate does not account for the possibilities that AI models become much more powerful, or that the use of AI at work becomes much more sophisticated—which could push the number much higher.

And the sample boundary, stated once, in footnote 1:

> As with previous reports, all our analysis is based on privacy-preserving analysis. Throughout the report we analyze a random sample of 1M conversations from Claude.ai Free, Pro and Max conversations (we also refer to this as "consumer data" since it mostly represents consumer use) and 1M transcripts from our first-party (1P) API traffic (we also refer to this as "enterprise data" since it mostly represents enterprise use).

**Annotation.**

- **Where they sit.** Beside their findings, every one, with the limitation in the paragraph immediately following the claim or the exhibit. The reader cannot reach a number without meeting its caveat within a screen. This is strictly better than the February 2025 arrangement — a pooled "Caveats" block 400 words downstream of the finding it undercut — and it is the placement our posts should use.
- **The connective is always the same.** "But this might not be as discordant as it seems"; "That said, even our revised assessment is still limited"; "We're not necessarily predicting". Each opens by naming the reading it is about to withdraw. The limitation is written as a correction to a specific misreading, not as a general disclaimer, and there is no "as with all studies" ritual sentence anywhere on the page.
- **Two of them withdraw a claim.** The selection-bias passage converts 19 hours from a capability number into an "indicator"; the deskilling passage converts an arithmetic result into a "signal". A limitation that changes what the post is willing to assert is worth three that describe noise — the same lesson as February 2025, executed twice here.
- **One names the direction of its own bias.** "users bring tasks to Claude that they're more confident will work" says which way the number is wrong, which is what makes it actionable. The others do not: neither the coverage limitation nor the productivity caveat is signed.
- **What a referee raises first, in order.** (1) The productivity caveat is one-sided — the only omitted possibilities listed are ones that would raise the estimate. (2) Nothing anywhere on the page acknowledges classifier error: every primitive is Claude's own estimate of a conversation, two of the headline numbers multiply two such estimates together (time saving × success probability), and no agreement rate, validation result or uncertainty appears. The page delegates this to chapter two of the report, which a blog-only reader will not open. (3) No uncertainty of any kind: not one interval, standard error or sample size in the body, and no minimum detectable effect beside any comparison. (4) The deskilling result depends entirely on one constructed skill measure and is not shown to survive another. (5) The "two to five years" convergence prediction has no stated model and rests on a three-month change, with the conditional carrying all of the weight. (6) The 36%-to-49% comparison changes basis mid-sentence. A post of ours carrying any one of these would be sent back.
- **The footnote-1 boundary.** Coverage is stated as an enumerated inclusion (Free, Pro and Max; first-party API) rather than an enumerated exclusion, which is the softer construction — a reader has to notice for themselves that third-party API traffic and Claude Code are absent. February 2025 named its exclusions ("rather than API, Team, or Enterprise users"). Name what is out, not only what is in.

## Close

Verbatim, the three paragraphs of "Conclusion" (hyperlink URLs stripped):

> ## Conclusion

> The most immediate conclusion from our latest Economic Index report is that the impact of AI on the global workforce remains a highly uneven one: AI use remains concentrated in specific countries and occupations, and it affects some occupations in a very different way to others, as the evidence on task coverage suggests.

> More generally, this report has given us a new baseline against which to compare our future surveys. As Claude improves, we expect it'll be asked to take on harder tasks, and that it'll likely find greater success. We also expect that tasks might move from Claude.ai to the API (that is, from predominantly consumers to predominantly businesses) as they become more reliable—and if this happens, it'll give us another possible indication of coming economic impacts, given the importance of business adoption for AI's effect on productivity. Through our primitives, we'll be able to measure how changes like these are beginning to impact real-world outcomes, including the nature of people's work, and which people (and where) are likely to be most affected during this period of rapid technological transition.

> In the meantime, researchers, journalists, and the public can use our data to inform their own research and thinking, and to provide an empirical foundation for the potential policy responses we might need. For much more detail on each of the areas we've discussed above, see our full report.

**Annotation.**

- **What was learned.** One sentence, one word of substance: **uneven**. Six findings collapse into a single qualitative claim, supported by two clauses naming where the unevenness shows (countries and occupations) and a pointer to the evidence for the second ("as the evidence on task coverage suggests"). Not one number from the body reappears. Not one of the six findings is restated. The close is 280 words and contains no digits at all — the same discipline as February 2025, and the reason neither post has a summary block to delete.
- **Why it matters.** Carried by the API-migration paragraph, which is the best sentence in the close: "We also expect that tasks might move from Claude.ai to the API (that is, from predominantly consumers to predominantly businesses) as they become more reliable—and if this happens, it'll give us another possible indication of coming economic impacts, given the importance of business adoption for AI's effect on productivity." The structure is *expectation → what it would look like in the data → why anyone should care*, with the causal premise named at the end rather than assumed ("given the importance of business adoption for AI's effect on productivity"). Three hedges in one sentence ("might move", "if this happens", "possible indication") and none of them is dropped. This is how to state a stake without promoting a conjecture: name the observable that would move, and say what it would be evidence of.
- **What comes next.** Concrete and falsifiable, and stated as expectations that could be wrong: harder tasks, greater success, migration from Claude.ai to the API. A later report can be held to all three. The method is promised; the *direction* of two of the three is also promised, which is a step further than February 2025 went and a step our own posts should not take without a pre-registration to point at.
- **Recommendation.** Displaced onto the reader, as in February 2025, and again a refusal to prescribe — but a softer one. "researchers, journalists, and the public can use our data to inform their own research and thinking, and to provide an empirical foundation for the potential policy responses we might need" names policy as someone else's output while claiming the evidential floor for it. Note "we might need": the need for policy is hedged, the shape of it is not discussed at all.
- **Title against ending.** Title: "Anthropic Economic Index: New building blocks for understanding AI use" — building blocks, an instrument. Ending: "Through our primitives, we'll be able to measure how changes like these are beginning to impact real-world outcomes." The instrument opens the post and closes it, and the final clause of the final substantive sentence names the primitives by name. The match is exact, and it is what licenses six findings in one post without any of them reaching the title. **The inverse still holds for us:** a post whose title names a finding must close on that finding's consequence.
- **How it avoids a template summary.** (1) No numbers. (2) No enumeration of findings — the one sentence that could have been a list is written as a single adjective with two supporting clauses. (3) Each paragraph is about a different tense: what the report found, what the next ones will find, what other people can do now. (4) The one sentence claiming a contribution is about the baseline, not the results: "this report has given us a new baseline against which to compare our future surveys."
- **First person.** Used throughout, as in every Anthropic post in the corpus, and for three things: institutional commitment ("we'll be able to measure"), expectation ("we expect it'll be asked"), and framing ("the areas we've discussed above"). House style forbids it. The expectation sentences are the hard ones to convert: "we expect X" has to become a statement about what the next release would show if the mechanism holds, not a bare passive, or the epistemic status is lost along with the pronoun.
- **One word not to inherit.** "our future surveys". The sample is a random draw of transcripts classified by Claude; the Index's survey component is a separate instrument in a separate publication. The page uses "survey" loosely twice, and quoting it would import an error into our own text.

## Verification

- **URL fetched:** https://www.anthropic.com/research/economic-index-primitives — fetched 2026-09-16, returned in full (page title "Economic Index: New building blocks for AI use \ Anthropic", H1 "Anthropic Economic Index: New building blocks for understanding AI use", dated "Jan 15, 2026" on the page). The fetch included the untitled opening, both H2 sections, all three H3s, all five H4s, all five figure captions, the Conclusion and all three footnotes. Every quotation in this file was copied from that fetch and checked back against it word by word after transcription.
- **Fetch date:** 2026-09-16.
- **PDF or appendix:** none exists for this slug; the `wiki/INDEX.md` row carries `—` in the PDF column. Nothing was missing.
- **Fetch failures:** none. The page returned on the first attempt and was not truncated.
- **Not fetched, deliberately:** the fourth report (https://www.anthropic.com/research/anthropic-economic-index-january-2026-report and its PDF), which is the separate corpus slug `economic-index-2026-01-report`; the Clio post; the first, third and fourth Index publications, each with its own slug; the productivity-gains post; METR's blog post; the NBER working paper; the Microsoft report; the Rwanda partnership announcement; Webb's paper. No content from any of them is quoted here. Where this file refers to what the report contains rather than what the blog says, it says so and makes no quotation.
- **Could not fetch:** nothing.
- **Quotation caveats.** Hyperlink URLs were stripped from quoted prose and the anchor text retained; the anchors for the opening are listed in `## Opening move`. Footnote reference markers were removed from quoted sentences. Typographic apostrophes and quotation marks in the source were normalised to ASCII; em dashes and all numerals are as fetched; no word was changed. Elisions inside short inline quotations in the annotation prose are marked `…`; no block quotation is elided. Source emphasis is reproduced: italics as `*…*`, bold as `**…**`. Figure captions are wholly bold on the page with their first sentence set in a further emphasis level; here the first sentence is rendered bold and the remainder plain, which is a rendering choice, not a change of text.
- **Alt text.** The five captioned exhibits have empty `alt` attributes in the fetched page; the hero image's alt repeats the H1. No number on this page appears only in alt text, so `room/director-2026-09-16-alt-text-ruling.md`'s `(alt text)` marking is not used anywhere in this file, and no number has been read off a chart image.
- **Page defect noted in passing.** Three of the page's seven links to the report are malformed (the domain is duplicated inside the path). Recorded in `wiki/reports/economic-index-2026-01-blog.md`; irrelevant to style and not pursued here.
- **Scope.** This file annotates how the piece is written. It makes no judgement about whether its findings are correct, and it reproduces no number from the released data.
