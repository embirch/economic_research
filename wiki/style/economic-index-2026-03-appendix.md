# economic-index-2026-03-appendix — style annotation

## Source

- **Title on cover:** "Appendix to "Anthropic Economic Index report: Learning curves"" — set as the document's only H1-scale line, with the parent report's title inside quotation marks. No sub-title, no appendix letter, no author list, no byline, no abstract, no contents page.
- **Date on cover:** "March 2026" — month and year only, below a horizontal rule.
- **Governing copy fetched:** https://cdn.sanity.io/files/4zrzovbb/website/a3cdcd9e67c3c4c51440429dd016cacba514b35b.pdf (6 pp; PDF CreationDate 2026-03-24 17:26 UTC). Called **copy B** below.
- **Earlier build fetched:** https://cdn.sanity.io/files/4zrzovbb/website/f065d6e6f92c65df8244042c83d48872ea308c3a.pdf (6 pp; CreationDate 2026-03-24 00:19 UTC). Called **copy A**. Same six pages, four substantive textual differences, listed in `## Verification`. Every quotation in this file is from copy B unless it is marked as copy A.
- **Other URLs it points at:** exactly one hyperlink in the whole document — the words "Claude.ai" in the *1P API* glossary entry on p. 3 link to https://claude.ai/new. The appendix contains **no link and no URL for the parent report**, no dataset link, no citation list and no footnote references beyond its own single footnote.
- **Document type:** stand-alone methodology appendix to a report published elsewhere on anthropic.com. It carries the method, the glossary, the classifier prompts and the figures that did not fit in the report; it carries no argument.
- **Length:** 1,019 words of extractable text across six pages, of which 472 words are inside Table A.1 and 103 are figure captions and the footnote. Body prose is therefore about 400 words. Three figures, one table, one footnote, four headings.
- **Audience:** a reader who has read the report and wants to know what was asked of the model, of which data, under what privacy constraint — and who is assumed to be able to read a chart without help. Nothing is explained twice.

## Section order

Headings in order, with what each does and how long it runs.

1. **Cover (p. 1)** — wordmark, the quoted parent title, rule, "March 2026", footer. ~10 words. The whole of the appendix's relationship to the report is carried by the title's quotation marks; there is no "this appendix accompanies…" sentence anywhere.
2. **H1 "Appendix" (p. 2)** — a bare page title with no text under it, immediately followed by its first H2. It names the genre and nothing else.
3. **H2 "Methodology" (p. 2)** — three paragraphs, 172 words. Paragraph 1 defines the two samples and the two words the report uses for them; paragraph 2 dates them and states the retention and record-definition facts; paragraph 3 states the privacy thresholds and their consequence for estimation. One page, one page only, and no sub-headings.
4. **H2 "Key terms" (p. 3)** — five glossary entries, 223 words, term in bold followed by a colon and a definition; the fourth entry expands into two bullets and five nested sub-bullets. Ends with the one-line pointer "See Table A.1 for additional details for each Economic Primitive."
5. **Table page (p. 4)** — the page-width heading "Economic primitives overview" sits *inside* the table graphic, not in the text flow; below it the nine classifier prompts in a five-group table; below that the caption "Table A.1: Economic Primitives Overview". No prose on the page at all.
6. **H2 "Additional figures and results" (p. 5)** — a heading with no prose under it. Figure A.1 and its caption, then Figure A.2 and its caption. 47 words of caption; nothing else.
7. **(p. 6)** — Figure A.3 and its caption, then a rule and the single footnote. No heading; the section started on p. 5 simply continues.
8. **Running footer** — on every page after the cover: "Appendix to "Anthropic Economic Index report: Learning curves"" left, page number right. In copy A the footer is "anthropic.com" instead, on every page.

**Where the results sit:** at the end, and only as figures. The order is sample → vocabulary → instrument → output, which is the reverse of a report: no number is shown until the reader has been given the prompt that produced it. Nothing is stated twice — the automation/augmentation taxonomy is defined once in Key terms and thereafter referred to, never redefined in a caption.

**What is shown and what is not.** Shown in full: the two sample definitions, the five key terms, all nine primitive prompts with their response options, three figures. Not shown anywhere: the model used for classification, its version or settings, the numeric privacy thresholds, the number of conversations behind any figure, any validation of the primitives against human labels, any equation, any regression table, any code. The appendix's answer to "how much is shown" is: *the questions asked, in full; the machinery that asked them, not at all.*

## Opening move

The cover, verbatim:

> Appendix to "Anthropic Economic Index report: Learning curves"
>
> March 2026

Then p. 2, verbatim, the page title, the first heading and the first paragraph:

> ## Appendix
>
> ### Methodology
>
> Our results are based on privacy-preserving analysis. Throughout the report we analyze a random sample of 1M conversations from Claude.ai Free, Pro and Max conversations (we also refer to this as "consumer data" since it mostly represents consumer use) and 1M transcripts from our first-party (1P) API traffic (we also refer to this as "enterprise data" since it mostly represents enterprise use).

Copy A's version of the same sentence:

> Our analysis is based on privacy-preserving analysis.

**Annotation.**

- **How it links to the report.** Typographically, not textually. The title quotes the report's title; the running footer repeats that quoted title on all five inner pages; the first body sentence says "Throughout the report" as though the reader were still inside it. There is no cross-reference, no section number, no hyperlink and no summary of the report's findings. The appendix behaves as a chapter that was bound separately, which is why it needs no introduction: the only sentence that positions it is the second clause of the first paragraph.
- **What the first sentence is about.** Privacy, not data. "Our results are based on privacy-preserving analysis" leads with the constraint under which the evidence was produced, before the reader learns what the evidence is. The claim of the appendix's genre is therefore *this was done legitimately*, stated before *this is what was done*.
- **How soon the first number appears.** Second sentence: "1M conversations" and "1M transcripts". In a methodology appendix the sample size is the opening move; there is no why-it-matters paragraph to buy, and none is attempted.
- **Definition inside the sentence that needs it.** Both samples are named and then glossed in a parenthesis with the *word the report uses for them* and the reason that word is approximate: "(we also refer to this as "consumer data" since it mostly represents consumer use)". The hedge "mostly" is fused to the label at the moment the label is introduced, so the report's shorthand can never be read as a population claim. This is the single most copyable sentence in the document.
- **The copy A → copy B edit.** "Our analysis is based on privacy-preserving analysis" became "Our results are based on privacy-preserving analysis" — a same-word repetition fixed in the later build, and evidence that the opening sentence of a methodology appendix is edited as carefully as the opening of a post.
- **Register.** First person plural throughout, for institutional acts and for analytical choices alike ("we analyze", "we also refer", "we rely", "we only estimate"). Unlike the 2025-02 report, where first person is reserved for institutional acts and findings have no agent, here the method *is* the agent: every methodological sentence has "we" as its subject. House style forbids it; the substitute is the passive with the choice named ("a random sample of 1M conversations … was analysed"), and the reason for the choice kept.

## Findings and their caveats

**There are no findings in prose.** No sentence in the appendix states a result, a direction, a magnitude or a comparison. The only numbers in the body text are sample descriptors (1M, 1M), sample dates (February 5, 2026, to February 12, 2026), the response ranges written into two prompts (0-20 years, 1 - 5 autonomy) and the three coverage thresholds named in a caption (25%, 50%, 75%). Every estimate in the document is inside a chart image. What follows is therefore how the *method* is phrased, which is the lesson this file exists to carry.

### How the sample and its record are defined

> Both samples come from February 5, 2026, to February 12, 2026. We continue to manage data according to our privacy and retention policies, and our analysis is consistent with our terms, policies, and contractual agreements. For 1P API data, each record is a prompt-response pair from our sample period which in some instances is mid-session for multi-turn interactions.

**Annotation.** Three sentences doing three different jobs: the observation window; the compliance statement; the unit of observation. The third sentence is where the caveat lives, and it is written as a definition rather than as a limitation — "each record is a prompt-response pair … which in some instances is mid-session for multi-turn interactions" concedes that the enterprise unit is a fragment of a session, not a session, and does so in the same breath as naming the unit. A reader who wants to know whether the consumer and enterprise series are measuring the same object gets the answer here and nowhere else. The pattern worth copying: **put the awkward fact in the sentence that defines the variable, not in a later list.** The compliance sentence is ritual and is the one sentence in the appendix that carries no information a replicator could use.

### How the privacy constraint is stated as an estimation rule

> When we analyze log-level data, we rely on statistical models in which minimum aggregate thresholds for both unique accounts and conversations are satisfied for any reported statistics. For example, in our regression analysis we only estimate fixed effects for groupings that satisfy our privacy requirements—otherwise such cells are dropped prior to estimation.

Copy A's first clause:

> In the analysis described in Chapter 2, we rely on statistical models in which …

**Annotation.** The privacy rule is not described as a policy but as a step in the estimator: thresholds on two dimensions at once (unique accounts *and* conversations), applied to "any reported statistics", with the consequence spelled out after the em-dash — "otherwise such cells are dropped prior to estimation". *Prior to* is the load-bearing phrase: it tells a reader that the sample selection happens before the fit, which is the difference between a suppressed cell and a dropped observation. What is withheld is the threshold itself; the rule is stated in full and its parameter is not. A referee reads that as unreproducible, and it is; the construction is still worth copying with the number filled in.

The copy A → copy B edit is the most instructive change between the two builds: a cross-reference to the report's own structure ("In the analysis described in Chapter 2") was replaced by a condition on the data ("When we analyze log-level data"). The later build makes the appendix legible without the report in hand, and it widens the scope of the sentence at the same time.

### How the glossary is written

> **1P API:** First-party API. This traffic represents users accessing Claude programmatically, rather than through a web user interface (as with Claude.ai).

> **Log-level data:** This refers to analysis performed at the log level, as opposed to aggregated task groupings. This is necessary for estimating the correlation between two primitives, for example.

> **Request clusters**: A bottom-up taxonomy of what people ask Claude to do, generated using a privacy-preserving method that groups semantically similar conversations.

> **Economic Primitives:** Simple measures of how Claude is used generated by asking Claude specific questions about anonymized conversations and transcripts. Our Economic Primitives cover five dimensions relevant to AI's economic impact: user and AI skills, how complex tasks are, the degree of autonomy afforded to Claude, how successful Claude is, and whether Claude is used for personal, educational, or work purposes.

**Annotation.** Each entry is one or two sentences and each is built the same way: *what it is*, then *what it is not* or *what it is for*. Two of the four define by contrast rather than by property — "rather than through a web user interface", "as opposed to aggregated task groupings" — and one of those then supplies the reason the distinction exists at all ("This is necessary for estimating the correlation between two primitives, for example"). A definition that says why it is needed cannot be skipped by the reader.

The *Economic Primitives* entry is the appendix in miniature. It states the instrument in fourteen words — "generated by asking Claude specific questions about anonymized conversations and transcripts" — and then enumerates the five dimensions in plain-language paraphrase rather than in the variable names used in the table ("how complex tasks are", "how successful Claude is"). The enumeration is ordered differently from the table, and deliberately: the sentence is written to be read, the table to be used. Note the naming discipline: the measured object is **Claude** in every clause ("how Claude is used", "asking Claude", "afforded to Claude"), while the stake is **AI** ("relevant to AI's economic impact"). The same rule as the 2025-02 report, held inside a single sentence.

> **Automation and augmentation:**
> - Automation encompasses interaction patterns focused on task completion:
>   - Directive: Users give Claude a task and it completes it with minimal back-and-forth
>   - Feedback Loops: Users automate tasks and provide feedback to Claude as needed
> - Augmentation focuses on collaborative interaction patterns:
>   - Learning: Users ask Claude for information or explanations about various topics
>   - Task Iteration: Users iterate on tasks collaboratively with Claude
>   - Validation: Users ask Claude for feedback on their work

**Annotation.** The taxonomy is presented as a two-level bullet tree with the composition rule visible in the indentation — two subtypes under automation, three under augmentation — so the reader can see that the dichotomy is a sum of named parts before any share is plotted. Each subtype gloss is a full clause in the same grammatical frame ("Users …"), five to eleven words, present tense, user as subject and Claude as object in every one. The 2025-02 report put this taxonomy in a figure caption; here it is in the glossary and appears in the figure area only as an equation (see `## Figure captions`). Either placement works; what does not vary is that the taxonomy is written out in full somewhere on the page where its shares are shown.

### How the prompts are presented

Table A.1 gives nine prompts in five groups. Verbatim, in table order, with their group labels:

> **Task complexity / Human time estimate.** Estimate how many hours a competent professional would need to complete the tasks done by the Assistant. Assume they have:
> - The necessary domain knowledge and skills
> - All relevant context and background information
> - Access to required tools and resources
> - No access to AI tools to assist with the work

> **Task complexity / Human with AI time estimate.** Estimate how many minutes the User spent completing the tasks in the prompt with the Assistant. Consider:
> - Number and complexity of User messages
> - Time reading Assistant's responses
> - Time thinking and formulating questions
> - Time reviewing outputs and iterating
> - Realistic typing/reading speeds
> - Time implementing suggestions or running code outside of the conversation (only if directly relevant to the tasks)

> **Task complexity / Multitasking.** Did the User multitask in this conversation? Choose from these options:
> - Yes: the User was working on multiple tasks over the course of the conversation
> - No: the User was working on a single task over the course of the conversation

> **Human and AI skills / Human ability to complete task alone.** Could the User have completed this task by themselves? Choose from these options:
> - Yes: the User would have been able to complete the task without the Assistant, even if it would have taken more time
> - No: the User would not have been able to complete the task without the Assistant, even with more time

> **Human and AI skills / Human education years.** Estimate how many years of formal education someone would need to understand the User prompts in this conversation. Your answer should be a single number out of the discrete numbers ranging from 0-20.

> **Human and AI skills / AI education years.** Estimate how many years of formal education someone would need to understand the Assistant responses in this conversation. Your answer should be a single number out of the discrete numbers ranging from 0-20.

> **Use case / Work vs. coursework vs. personal.** Analyze whether the conversation between the User and the Assistant primarily focuses on work, coursework, or personal use. Analyze the use case according to these categories:
> - Work: professional use to accomplish tasks that are part of the User's job
> - Coursework: use to help the User complete coursework in educational contexts
> - Personal: use for any domain that is not work or coursework

> **AI autonomy.** Estimate how much autonomy the Assistant had to make decisions in this conversation (a discrete number ranging from 1 - 5, where 1 is none and 5 is extreme).

> **Task success.** Did the Assistant complete the task provided by the User successfully? Choose from these options:
> - Yes: the Assistant completed the task provided by the User successfully
> - No: the Assistant did not complete the task provided by the User successfully

**Annotation — how a prompt is written down.**

- **The prompt is quoted, not described.** No row says "we asked the model to judge complexity"; each row is the instruction itself, in the imperative, as it was issued. This is the appendix's central stylistic commitment and the reason it needs no prose: an instruction shown in full cannot be paraphrased unfairly.
- **Three verbs only.** "Estimate…" for quantities (four rows), "Did…" / "Could…" for binaries (three rows), "Analyze whether…" for the one nominal classification. The verb tells the reader the response type before the response options do.
- **The response space is inside the prompt.** Every non-open row ends with "Choose from these options:" and then *both* options written out as full sentences, or with the range stated as a constraint on the answer: "Your answer should be a single number out of the discrete numbers ranging from 0-20"; "(a discrete number ranging from 1 - 5, where 1 is none and 5 is extreme)". Nothing is left to a codebook. Note that the two-point scales spell out the negative option at the same length as the positive one, so neither is the default.
- **Assumptions are itemised, not prose.** The two time-estimate prompts carry bulleted stipulations — the counterfactual worker's endowment ("The necessary domain knowledge and skills … No access to AI tools to assist with the work") and the components of elapsed human time. The counterfactual that makes the measure meaningful is written *into the instruction*, not into the surrounding text. A reader disputing the construct disputes a bullet, which is the point.
- **Scope fences inside a bullet.** "Time implementing suggestions or running code outside of the conversation (only if directly relevant to the tasks)" — the one place the appendix hedges an instruction, and it does so parenthetically at the end of the bullet it qualifies.
- **The actors are roles, not products.** Inside every prompt the parties are "the User" and "the Assistant", capitalised; "Claude" never appears in Table A.1, and "the Assistant" never appears in the glossary or the captions. The prompt is written to be model-agnostic; the prose around it is not. When our own posts quote a classifier prompt, the prompt keeps its own vocabulary and the surrounding sentence says Claude.
- **Symmetry as a design tell.** *Human education years* and *AI education years* are the same sentence with "User prompts" swapped for "Assistant responses"; *Human time estimate* and *Human with AI time estimate* differ in unit (hours against minutes) and in counterfactual. Paired primitives are written as edits of one another, so a reader can see that the pair is comparable by construction.
- **What no row contains.** The classifying model and its settings; the sampling of conversations into the classifier; whether a row was validated against human labels; what happens to refusals or unparseable answers; the unit of aggregation. The prompts are complete and the pipeline is absent.

## Comparisons

**No robustness variant is reported anywhere in this appendix.** There is no alternative specification, no sensitivity analysis, no measure-variant table, no comparison of the primitives against an external benchmark, and no statement of what would change under a different threshold. Any post that treats this appendix as the model for a robustness section will find nothing to imitate; the variant-tabulation lesson has to be taken from a different file in this corpus.

Three comparison devices do appear, all of them inside figure furniture rather than in prose.

### The two data sources, held side by side

> This plot shows changes in usage shares across the largest occupational categories in our data, splitting by Claude.ai and 1P API.

**Annotation.** The consumer/enterprise split is the appendix's only recurring comparison, and the caption states it as a property of the plot ("splitting by") without saying what the split shows. Figure A.1 draws both series on each of eight small panels; Figure A.3 drops to one source and says so in its own title ("Collaboration mode share, 1P API"), which is how the appendix signals that a result is not available for both samples — by naming the sample in the label rather than by explaining the absence.

### The taxonomy restated as an equation

Inside the Figure A.3 image, below the plot area and above the caption, in italics:

> Automation = Directive + Feedback loop. Augmentation = Validation + Task iteration + Learning.

**Annotation.** In-figure text, not caption text. A two-clause definition written as addition, so the reader of a two-line chart can verify what each line is a sum of without turning back to Key terms. Worth copying wherever a plotted dichotomy is an aggregate of named subtypes: the components belong on the exhibit.

### Across releases — the one comparability caveat

> ¹ This figure uses 2019 O*NET-SOC codes, while previous reports use the 2010 vintage.

**Annotation.** The only sentence in the appendix that compares this release to earlier ones, and it compares *classifications*, not results: the crosswalk vintage changed, so a reader stacking Figure A.1 against an earlier report's category shares is warned, once, in a footnote, that the categories are not the same objects. The construction is "this uses X, while previous reports use Y" — no claim about how much it matters, no bridge estimate, no restatement in the body. It is a comparison used to withdraw comparability.

## Figure captions

Four captions — one table, three figures. All are set below the exhibit in two lines: a bold label-and-title line, then one sentence of description in regular weight. No caption is a bold run-on sentence in the manner of the 2025-02 report; the label is numbered ("Table A.1:", "Figure A.1:") and the title is a short noun phrase in sentence case.

### Table A.1

> **Table A.1: Economic Primitives Overview**
> This table provides definitions for the Economic Primitives we study in this report.

**Annotation.** Twelve words. The caption says what kind of content the table holds ("definitions") and whose ("we study in this report") and nothing about how to read it — the table's own internal heading, "Economic primitives overview", and its group column do that. Note that the caption calls the prompts *definitions*: in this house, the operational definition of a construct **is** the instruction given to the classifier, and the caption says so without argument. Title case in the caption label, sentence case in the in-table heading; the two do not match, which is a production artefact rather than a choice.

### Figure A.1

> **Figure A.1: Shifts in usage across occupational categories**
> This plot shows changes in usage shares across the largest occupational categories in our data, splitting by Claude.ai and 1P API.¹

Copy A's title line:

> **Figure A.1: Shifts in the usage across occupational categories**

In-figure title (not caption text): "Task usage share trends by occupation group (V1-V5, 2019 O*NET-SOC)".

**Annotation.** The caption names the quantity ("usage shares"), the unit of the panels ("the largest occupational categories"), the provenance ("in our data") and the series key ("splitting by Claude.ai and 1P API"), then hangs the vintage caveat off the end as a footnote marker. What it does not do is say which way anything moved — "Shifts" and "changes" are direction-free nouns, and the eight panels are left to speak. The selection rule is stated only as "the largest", with no threshold and no count: a referee's first question. The in-figure title carries what the caption omits — the release versions plotted and the crosswalk vintage — so the exhibit is self-contained when lifted, and the caption is the shorter of the two. Copy B's title drops the stray "the" from copy A's.

### Figure A.2

> **Figure A.2: Cumulative job coverage**
> This plot shows changes in the cumulative share of occupations with task coverage at or exceeding 25%, 50%, or 75%.

In-figure title (not caption text): "Occupation coverage thresholds (claude.ai + API, cumulative)".

**Annotation.** The tightest caption in the document and the most complete: quantity ("the cumulative share of occupations"), the definition of the qualifying condition ("with task coverage at or exceeding"), and all three thresholds enumerated in the caption itself. The three numbers in this caption are the only estimates-adjacent numbers in the appendix's text, and they are *thresholds*, not results — the caption states the cut-points and leaves the heights to the chart. This is the caption pattern to imitate for any threshold-based coverage measure: name the condition, enumerate the cuts, claim nothing. Here the caption also does not say that the two samples are pooled; only the in-figure title does ("claude.ai + API").

### Figure A.3

> **Figure A.3: Collaboration mode share, 1P API**
> This plot shows changes in the share of automation vs. augmentation in 1P API traffic.

In-figure title (not caption text): "Automation vs augmentation over time (1P API)".

**Annotation.** The sample qualifier is in the title line after a comma and again in the sentence — the one piece of information the appendix is willing to repeat, because a mode share for enterprise traffic read as a mode share for all traffic would be a serious misreading. "Collaboration mode" is the label for the dichotomy; "automation vs. augmentation" is its content; both appear, so a reader who knows only one vocabulary is served.

**The caption pattern in summary.** Bold numbered label, short noun-phrase title, then exactly one sentence beginning "This plot shows changes in…" or "This table provides…". The sentence names the quantity, the unit, the sample split and any threshold; it never names an axis, a colour, a date range, a sample size, or a direction of movement. Axis labels, legends, panel titles, data labels and any component identity live inside the image. Every caption says either "Claude.ai", "1P API" or "our data" — the sample is never left implicit — and no caption says "AI". Where a caveat attaches to a single exhibit it becomes a footnote on the caption, not a clause in it.

## Limitations

**There is no limitations section, no caveats section and no bullet list of either.** The words "limitation" and "caveat" do not appear in the document. Three sentences do limitation work; all three are quoted above and all three are placed inside the definition of the thing they qualify, which is the pattern worth drawing out:

> For 1P API data, each record is a prompt-response pair from our sample period which in some instances is mid-session for multi-turn interactions.

> … otherwise such cells are dropped prior to estimation.

> ¹ This figure uses 2019 O*NET-SOC codes, while previous reports use the 2010 vintage.

**Annotation.**

- **Where limitations sit.** At the point of definition, not in a list. The enterprise unit's truncation is in the sentence defining the enterprise unit; the sample-selection consequence is in the sentence defining the privacy rule; the comparability break is in a footnote attached to the figure it breaks. Nothing is aggregated, so nothing can be skipped by a reader who skips one section — and nothing can be counted, either, which is the cost.
- **Each is one sentence and none is softened.** No "as with all studies", no "important limitations", no framing sentence re-asserting the contribution. The register is flat declarative; the concession is carried by a relative clause ("which in some instances is mid-session"), a subordinating adverb ("otherwise"), and a contrastive conjunction ("while previous reports use the 2010 vintage").
- **What a referee would raise first, and the appendix does not.** No sample size for any figure. No uncertainty of any kind — no interval, no standard error, no statement that the plotted differences exceed sampling noise, no minimum detectable effect. The privacy thresholds are invoked as binding but never stated as numbers, so no reader can tell which cells were dropped or how many. The primitives are defined by their prompts and never validated: no human-label agreement, no reliability across runs, no treatment of refusals. Selection into Figure A.1 is "the largest occupational categories" with no rule. The consumer sample is a random sample of conversations while the enterprise sample is a set of prompt-response pairs, and the appendix names that asymmetry without addressing whether the two series are comparable.
- **The lesson to take and the lesson to leave.** Take the placement: a caveat written into the definition of a variable is read by everyone who uses the variable. Leave the absence: a methodology section in this house states the threshold, the n and the MDE, because the point of showing the prompt in full is defeated by hiding the parameter that decided which answers survived.

## Close

The document ends on p. 6 with Figure A.3, its caption, a short horizontal rule, and then the footnote — which is the last text in the appendix:

> **Figure A.3: Collaboration mode share, 1P API**
> This plot shows changes in the share of automation vs. augmentation in 1P API traffic.
>
> ¹ This figure uses 2019 O*NET-SOC codes, while previous reports use the 2010 vintage.

**Annotation.**

- **There is no close.** No conclusion, no summary, no "what comes next", no acknowledgements, no references, no author contacts, no pointer back to the report or forward to the next release. The final page is two-thirds white space below the footnote. An appendix in this house is allowed to simply stop.
- **What the last words are.** A caveat about comparability with earlier releases. The document's final sentence reduces what a reader may do with its own figure — the same construction as the strongest caveat in `wiki/style/economic-index-2025-02-report.md`, where a limitation is used to withdraw a claim, demoted here to a footnote. Ending on a restriction rather than a claim is available to an appendix precisely because the claims are made elsewhere.
- **Title against ending.** The title is a pointer ("Appendix to …") and the ending is a pointer ("while previous reports use the 2010 vintage"): both face outward, one to the parent report and one to the series. Nothing in the document points at itself, and that consistency is why it needs no close.
- **What this licenses in our own posts, and what it does not.** A *methodology* section may end without a summary, and a figure-level caveat may be a footnote. The post's own close may not: a post that ends on a comparability footnote has no answer to why it matters. The transferable move is the ordering — instrument first, output last, and the last thing said about an exhibit is what may not be concluded from it.

## Verification

- **URLs fetched:** both builds, 2026-09-16. Copy B (governing) https://cdn.sanity.io/files/4zrzovbb/website/a3cdcd9e67c3c4c51440429dd016cacba514b35b.pdf — HTTP 200, 641,935 bytes, 6 pages. Copy A https://cdn.sanity.io/files/4zrzovbb/website/f065d6e6f92c65df8244042c83d48872ea308c3a.pdf — HTTP 200, 846,979 bytes, 6 pages.
- **Fetch method.** `web_fetch` refuses `cdn.sanity.io` (`url_not_allowed`), as the lead's thread also recorded; both files were retrieved with `curl` in the sandbox. Text extracted with `pdftotext -layout` (poppler) and cross-checked with `pypdf` 3.17.4; pages 1–6 of copy B rendered with `pdftoppm` and inspected for heading hierarchy, table structure and in-figure text. Every quotation here was copied from those extractions and checked back against the rendered page.
- **Which copy governs.** Copy B, the later build (CreationDate 2026-03-24 17:26 UTC against copy A's 00:19 UTC the same day). `wiki/INDEX.md` lists copy A as the primary URL; that is a question for the INDEX thread, not for this file.
- **Differences between the two builds**, from a line diff of the two text layers — four substantive, all recorded at the point of use above: (1) "Our results are based on" (B) against "Our analysis is based on" (A); (2) "When we analyze log-level data" (B) against "In the analysis described in Chapter 2" (A); (3) Figure A.1 title "Shifts in usage" (B) against "Shifts in the usage" (A); (4) running footer, the quoted report title (B) against "anthropic.com" (A). Table A.1, the Key terms page and all three figure images are identical.
- **Hyperlinks.** One link annotation in each copy: "Claude.ai" on p. 3 → https://claude.ai/new. No other URL appears in or under the text of either copy.
- **Figures are raster images.** All three figures are JPEGs (2048 px wide) with no text layer, and neither PDF is tagged, so **no alt text exists** for any exhibit. In-figure text quoted in this file — panel titles and the automation/augmentation equation — was read from the rendered page and is marked "in-figure" at every point of use; it is never presented as caption text. Per `room/director-2026-09-16-alt-text-ruling.md`, numbers printed inside the charts (axis ticks and the end-of-series data labels on Figures A.2 and A.3) are read off chart images and are **not recorded here**.
- **Not fetched, deliberately:** the parent report "Anthropic Economic Index report: Learning curves" (its own corpus slug) and the claude.ai link. No content from either is quoted here; the appendix contains no URL for the report, so none was followed.
- **Could not fetch:** nothing. No fetch failed.
- **Quotation caveats.** Typographic quotation marks, apostrophes and em-dashes in the source were normalised to ASCII where quoted inline; no word was changed. Bullet glyphs are rendered as Markdown list items and the two-level structure of the Key terms taxonomy and the Table A.1 rows is preserved. Table A.1 is a two-column layout in the PDF whose left column carries the group name and whose second column carries the primitive name; in this file each prompt is labelled "**Group / Primitive.**" and the two bulleted lists that the PDF sets side by side (under *Human time estimate* and *Human with AI time estimate*) are transcribed as single lists in reading order — left column then right. Bold in quoted glossary entries and captions is as set in the PDF. Word counts were computed from the `pdftotext` layer.
- **Scope.** This file annotates how the piece is written. It makes no judgement about whether its methods are sound or its figures correct.
