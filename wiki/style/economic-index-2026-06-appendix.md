# economic-index-2026-06-appendix — style annotation

## Source

- **Title on the cover page:** "Appendix to “Anthropic Economic Index report: Cadences”" (set over three lines under the ANTHROP\C wordmark, with a rule beneath).
- **Date on the cover page:** "June 2026". No day. The PDF's own creation date is 2026-06-26, the same day as the parent report.
- **Primary URL fetched:** https://cdn.sanity.io/files/4zrzovbb/website/03ed1410f74a65ae4cc2a27120d0875e1e569535.pdf — 15 pages.
- **Second copy fetched:** https://cdn.sanity.io/files/4zrzovbb/website/8eb31e1d187ff18146d248bbef8b2754971f0f5a.pdf — 15 pages, byte-for-byte the same document except for one heading (see `## Close` and `## Verification`).
- **Parent piece:** the sixth Economic Index report, slug `economic-index-2026-06-report` (https://www.anthropic.com/research/economic-index-june-2026-report, PDF https://cdn.sanity.io/files/4zrzovbb/website/9e0eadc8097864886c5d5060ebb1f89b02ea29d6.pdf). Not fetched for this file; its style entry is a separate slug.
- **Document type:** methodology appendix. It carries no argument of its own. It exists to hold three things the report could not: the two classifier prompts in full, seven worked example classifications, and two exhibits that did not fit the report — plus a coding scheme for one survey question.
- **Byline, abstract, contents, references:** none, none, none, and one footnote (the WildChat citation). No named authors anywhere. No acknowledgements. No "how to cite". No version number.
- **Approximate length:** roughly 2,300 words of body prose and prompt text across 15 pages, of which pages 6–10 and 15 are almost entirely rasterised images of tables. Three chapters, four sub-headings, two numbered figures, one numbered table, seven unnumbered example cards.
- **Running furniture:** every page after the cover carries the full title in grey at the foot left — "Appendix to “Anthropic Economic Index report: Cadences”" — and the page number at the foot right. The cover carries "anthropic.com" in its place. The appendix is designed to be read as a detached file; the footer is what tells a reader who downloaded only this PDF what it belongs to.
- **Audience:** a reader who has already read the report and wants to know exactly what was asked of the model. Not a reader being persuaded of anything. There is no why-it-matters sentence in the document.

## Section order

Headings in order, with what each does and where it runs.

1. **Cover page (p. 1)** — wordmark, title, rule, date. Nothing else. No summary, no chapter list.
2. **"CHAPTER 1 / Changes to the economic index pipeline" (pp. 2–10)** — the eyebrow "CHAPTER 1" in small bold caps above a two-line sans-serif chapter title. ~430 words of prose (pp. 2–3), then two sub-sections:
   - Prose (pp. 2–3): the sampling change; the classifier redesign; the two-step task pick and its randomisation; the new top-level request clusters, given as one running list of twenty-one names inside body prose; the transcript-window change; then the one-line pointer **"The ONET classifier is given below."**
   - **"ONET classifier" (pp. 3–5)** — sub-head, then "Step 1" and "Step 2" as labels over two grey monospace prompt boxes running to the foot of p. 5.
   - **"Examples of how our classifiers work" (pp. 6–10)** — ~120 words of preamble, seven example cards (Examples 1–7) as full-width tables, and ~80 words of commentary on Example 7 placed *after* the last card.
3. **"CHAPTER 2 / Artifact classifier" (pp. 11–14)** — ~60 words of preamble, then one grey monospace box running two and a half pages (the artifact prompt with all 32 labels), then two sub-sections:
   - **"Distribution of outputs on 1P API" (p. 13)** — three sentences and Figure A.1.
   - **"Autonomy and token consumption" (p. 14)** — three sentences and Figure A.2.
4. **"CHAPTER 3 / Ten-year vision themes and definitions" (p. 15)** — heading, Table A.1, nothing else. No prose at all.
5. **Footnote 1 (foot of p. 15)** — the WildChat citation, in full academic form.

**What the order tells you.** The chapters are numbered to match the *parent report's* chapters, not to sequence an argument of their own: Chapter 2 here supplies Chapter 2 there ("mapped to the display names used throughout Chapter 2"), Figure A.1 is introduced as mirroring "Figure 2.1" in the report, and Chapter 3 is the survey chapter's coding scheme. An appendix built this way needs no cross-reference prose, because the numbering *is* the cross-reference. There is no introduction and no conclusion; the document begins in the middle of a sentence about method and stops when the last table ends.

**Where the prose sits relative to the exhibits.** Always before, never after — except once. Each prompt box, figure and table is preceded by two to five sentences saying what it is and, where relevant, what to notice in it. The single exception is Example 7, whose commentary sits below the card; and the reason is visible in the layout — the card fills the top half of p. 10, so the criticism had nowhere else to go. Everything else reads *setup, then object*.

## Opening move

Verbatim, the first paragraph of Chapter 1, which is also the first prose in the document:

> With this release, we made several changes to how we sample and classify Claude traffic. We now sample a fixed number of conversations every hour. (In previous Economic Index reports, our data spanned a week of activity.)

And, for contrast, the opening of Chapter 2 and the opening of the examples section:

> The following prompt was used to classify the most prominent concrete output of each exchange. Categories were presented in randomized order in each call, with the “other” and “none” options always listed last. The model’s answer was extracted from the answer tags and mapped to the display names used throughout Chapter 2.

> We classify transcripts in a privacy-preserving way. To illustrate how the classifiers work, we present some example classifications using transcripts drawn from WildChat,1 an open-source dataset of user-ChatGPT interactions. (Some assistant’s responses were abbreviated for presentation below.)

**Annotation.**

- **How it links to the report.** Only three ways, none of them a sentence of cross-reference: the title, the running footer, and shared chapter numbering. There is no "this appendix accompanies…", no restatement of the report's question, no list of what the appendix contains. The link is structural. The one explicit pointer in the document runs the other way — "mapped to the display names used throughout Chapter 2" tells the reader that the machine-readable labels here become the human-readable labels there.
- **What the first sentence does.** It names a change, its scope and its object in fourteen words: *what changed* ("several changes"), *to what* ("how we sample and classify"), *of what* ("Claude traffic"). No stakes, no motivation, no claim that the change matters. An appendix opening states a delta, where a report opening states a finding.
- **The parenthesis is the comparison.** "(In previous Economic Index reports, our data spanned a week of activity.)" — the old design is given in brackets immediately after the new one, in the same breath, with no comparative adjective and no assessment. This is the appendix's whole comparative vocabulary in one move, and it is used three times (see `## Comparisons`). Putting the baseline in parentheses signals that the change is being *recorded*, not defended.
- **How soon the first technical detail appears.** Sentence two. "We now sample a fixed number of conversations every hour" is the load-bearing methodological fact of the entire release, and it arrives twenty-five words in, with no run-up. Compare the launch post, which spends three paragraphs before its first number. The genre difference is total: an appendix has already been granted the reader's attention and spends none of it on earning attention.
- **What is *not* in the opening.** No sample size, no date range, no number of conversations, no model version, no country coverage, no statement of what the classifier's accuracy is. None of these appear anywhere in the document. A reader who wants n must go to the report.
- **Register.** First person plural throughout, and only ever for methodological acts: "we made", "We now sample", "we map", "we shuffle", "we randomly choose", "we present", "We classify", "We ask", "We do this to". Never for a finding. The one non-agentive construction is reserved for the prompt's provenance — "The following prompt **was used** to classify…" — which puts the prompt, not the team, in subject position at the moment the prompt is handed over. Our house style forbids the first person outright; the substitute for these sentences is the passive that Chapter 2 already demonstrates.
- **Tense discipline worth copying.** Present tense for the pipeline as it now stands ("We now sample", "we shuffle", "the ONET classifier is asked"), past tense for what was done to produce this release's numbers ("The following prompt was used", "Categories were presented", "The model's answer was extracted", "This randomization was meant to"). The two tenses separate *the standing method* from *this run of it*, and the document never mixes them inside a sentence.

## Findings and their caveats

This is an appendix: it reports no findings about the economy. What it reports is method, and two exhibits that did not fit the report. Each is treated below in the order it appears, because the *phrasing* of method is the thing being annotated.

### Method statement 1 — a change with its reason attached

> We also changed how we map conversations to ONET tasks. The previous classifier traversed a tree, first picking high-level ONET categories that we had hand-crafted. Now, the ONET classifier picks a detailed work activity (DWA) in the first step, then picks among the DWA’s constituent tasks in the second. We also switched over to the ONET version 30.2, released in February 2026. The new ONET classifier also reversed the order (the transcript appears at the end of the input) so that the prefix can be cached. Since Claude may have order preferences over the categories presented to it, we shuffle the options in the prefix (using a predefined set of orderings to preserve caching).

**Annotation.** Four changes in six sentences, and every one of them is given a reason in the same sentence as the change — the reason is never deferred to a later paragraph and never omitted. Two of the reasons are engineering ("so that the prefix can be cached"; "to preserve caching") and are stated as plainly as the scientific one, with no embarrassment about the fact that cost shaped the design. The scientific reason is the best sentence in the chapter: "Since Claude may have order preferences over the categories presented to it, we shuffle the options in the prefix." Note its shape — *a named risk to validity in a subordinate clause, hedged with "may", then the mitigation as the main clause*. The risk is not tested, quantified or cited; it is conceded as possible and then designed around. That construction ("Since X may be true, we do Y") is the appendix's characteristic caveat, and it is worth copying exactly, because it discloses a threat without either overstating it or hiding it. Note also the parenthetical constraint that follows the mitigation: "(using a predefined set of orderings to preserve caching)" tells the reader the shuffle is *not* fully random, which is precisely the detail a replicator needs and the detail a weaker write-up would drop. Finally, the version is pinned with its release date ("ONET version 30.2, released in February 2026") — a construct-provenance move: the reader can tell which taxonomy was live.

### Method statement 2 — a design choice that concedes its own arbitrariness

> In the second step, the ONET classifier is asked to specify the ONET tasks that best describe the work being done in the transcript. It is asked to provide pairs of {task, confidence (1-5)}, and we randomly choose a task among those with the highest confidence. This randomization was meant to spread the choice across the multiple candidates in order to avoid many transcripts piling up into one specific (and arbitrary) work task.

**Annotation.** The caveat is a single parenthesised adjective: "one specific (and arbitrary) work task." The document concedes, in two words, that the leaf-level task assignment has no ground truth — and having conceded it, justifies a randomisation that would otherwise look like noise injection. This is the most economical limitation in the document and the model for how to write one inline. What is missing is equally instructive: no number for how often ties occur, no statement of how much the assignment changes under a different seed, and no sensitivity check. A referee's first question of this paragraph is "how often does the randomisation bind?", and the appendix does not answer it. The notation is also a tell — "{task, confidence (1-5)}" uses the prompt's own brace syntax inside body prose, so that the prose and the prompt box three pages later use one vocabulary.

### How prompts are presented

Both prompts are set verbatim in grey monospace boxes, full width, with no line numbers and no commentary inside the box. Three conventions govern what appears inside:

- **Braces for variable content.** `{TRANSCRIPT}`, `{n GWA} categories`, `{n IWA}`, `{n DWA}`, `{step-1 summary}`, `{semicolon-joined list of picked DWAs}`, and — the best of them — `{up to 300 candidate Task texts, shuffled, one “- ...” line each}`. The braces do double duty: they mark the slot, and their contents *describe* what fills it, including its cardinality and its formatting. A reader learns the candidate set is capped at 300 and is shuffled per call without a sentence of prose being spent on it.
- **Square brackets for editorial elision.** `[same 1-5 rubric as step 1]`, `[Standard API-data disclaimer]`, `[Exchange transcript and preamble]`. Where text is repeated or boilerplate, it is cut and the cut is named. Nothing is silently removed.
- **An ellipsis line for truncated enumeration.** Inside the Step 1 taxonomy illustration the hierarchy is shown two branches deep and then broken with a bare `...` at the indentation level of the omitted items, twice. The reader sees the *shape* of the option tree — `[GWA] Analyzing Data or Information` → `[IWA] Assess characteristics or impacts of regulations or policies` → two `[DWA]` lines — without being shown a taxonomy of thousands.

The output contract is shown in both prompts, in full, as the last thing in the box:

> Output JSON only:
> <answer>{“summary”: “<1-2 sentences>”, “picks”: [{“level”: “GWA|IWA|DWA”, “name”: “<exact name>”, “confidence”: 1-5}], “notes”: “<optional>”}</answer>

**Annotation.** Prompts are reproduced whole, not paraphrased and not excerpted to their "interesting" parts; the confidence rubric is given at full length with all five anchor definitions, including the operational instruction attached to the lowest one ("Picks at this level are near-noise — exclude unless nothing stronger exists"), which is a coding rule a replicator must have. The only things abridged are the things that repeat. The artifact prompt in Chapter 2 goes further and prints all thirty-two labels with their glosses — a two-and-a-half-page block — rather than summarising the taxonomy in a table, because the *wording shown to the model* is the artefact, and a tabulated summary would not be that. The rule this implies: in an appendix, show the instrument as the instrument was, and mark every cut.

Note the naming discipline inside the prompts, which differs from the report's. The ONET prompt never says Claude; it says **"a chatbot"** ("what “work activities” the chatbot is doing for the user", "the activity the chatbot carries out for the user"), because the same prompt is run over WildChat transcripts of a different assistant. The artifact prompt does say Claude, twice, in capitals-adjacent emphasis: **"the single most prominent concrete OUTPUT that Claude produced for the User in this exchange?"**. Body prose says "Claude traffic". So: the measured system is named Claude in prose and in the prompt that only ever sees Claude; the generic term is used in the prompt that must also see other systems. That is a stricter version of our own rule (the question says AI; the finding says Claude), and the reason given for it is validity, not branding.

### The worked examples, and how failure is phrased

The preamble and the two pieces of commentary are the only prose in the section:

> The examples are meant to illustrate the utility and limitations of the approach. In Example 2, the user asks for and receives a poem. This receives an accurate (based on our judgment) ONET classification: it’s labeled as “Write narrative, dramatic, lyric, or other types of poetry for publication,” a task belonging to Poets, Lyricists and Creative Writers. It is also classified as a personal use case, although this is hard to prove. It’s often difficult to infer how the output was used.

> In Example 7, the question, “Which Rust library is best for Natural Language Processing (NLP)?” is mapped to a sales occupation although the question is substantively about computer programming. The classifier focuses on what the Assistant is asked to do—“Recommend products”—and not on the topic of the request. This question might have been better assigned to a task like “Consult with customers or other departments on project status, proposals, or technical issues, such as software system design or maintenance,” which falls under Software Developers.

**Annotation.** This is the appendix's substitute for a limitations section, and it is better than most limitations sections, for four reasons worth copying.

1. **The section announces that it will show failures before it shows any.** "meant to illustrate the utility *and limitations* of the approach" — the reader is told the sample of examples is not a highlight reel.
2. **Even the success is hedged, in the same sentence, twice.** "an accurate (based on our judgment) ONET classification" fences the verdict as a judgement rather than a measurement — there is no rater, no agreement statistic, no ground truth — and then the *second* label on the same example is conceded outright: "It is also classified as a personal use case, although this is hard to prove." The concession is then generalised into a standing limitation in a seven-word sentence: "It's often difficult to infer how the output was used." A specific doubt about one example is promoted into a property of the instrument; that promotion is the move.
3. **The failure is diagnosed, not merely displayed.** Example 7 is not left as "sometimes it gets things wrong". The mechanism is named — the classifier keys on the requested *act* rather than the request's *subject matter* — which makes the error predictable rather than random, and tells a reader which downstream numbers (occupational shares for sales versus software) are likely biased and in which direction.
4. **The better answer is supplied.** "might have been better assigned to a task like “Consult with customers…”, which falls under Software Developers." Naming the correct label, verbatim and with its occupation, converts a confession into a reproducible test that someone else could run. "might have been better" keeps it a judgement.

The examples themselves are rasterised tables, one per card, with a grey header row carrying only "Example *n*" and six labelled rows: **Transcript**, **O\*Net Classifier**, **Use Case**, **Task Success**, **Artifact**, **AI Autonomy**. The transcript is shown as `Human:` / `Assistant:` turns with bracketed elision `[...]` where the response was cut, and code is shown in a monospace, syntax-coloured block. The classifier row prints the whole chain in one line — `[GWA] … › [IWA] … › [DWA] … › [Task] … > [occupation] …` — so the reader sees every rung of the ladder that produced the occupation, not just the endpoint. Five classifiers are shown per example even though only one is discussed; the card is a fixed schema, not a curated exhibit. (These cards have no text layer; see `## Verification`.)

### The two exhibits, and how a secondary result is phrased

> Below figure mirrors Figure 2.1 but for 1P API. On this surface, the share of conversations with no clear output is higher (16% vs 7% on chat and Cowork). Analytic outputs dominate (21%), followed by data/spreadsheet related outputs (14%) and explanations/answers (8%).

> The below figure displays the normalized median token usage per artifact against the mean autonomy measured in the conversations producing these artifacts. Artifacts requiring more tokens tend to be produced with more autonomy.

**Annotation.** Three sentences each, and the shape is identical: *what the figure is* → *the one contrast that matters* → *the ranking or the direction*. The first sentence of each is pure orientation and names the comparison object ("mirrors Figure 2.1 but for 1P API") or the two axes ("normalized median token usage per artifact against the mean autonomy"). No sentence in either paragraph exceeds one clause of interpretation.

The caveat work is carried by two words. "On this surface" fences every number in the paragraph to 1P API, and it is placed at the head of the sentence, before the finding, so the fence cannot be read past. "tend to" is the entire hedge on the autonomy result: a positive association is asserted, no coefficient is given, no correlation is reported, and the dashed fit line drawn on the chart is never mentioned in the text — so the claim in prose is strictly weaker than the claim in the image. That gap is deliberate and worth copying in the direction the appendix uses it: *state less in prose than the picture shows*, never more. What a referee would still ask: the appendix gives no n for either surface, no uncertainty on any share, and no test behind "tend to", and it does not say whether the 1P API figure uses the same denominator as Figure 2.1.

One inconsistency to record, because it is the kind of thing our own verification script exists to catch: the prose value for data/spreadsheet outputs does not match the label drawn on the bar in the chart image. (Per the house ruling, values read off a chart image are not recorded here; the prose value is quoted above.) A number that appears twice in two renderings and disagrees with itself is a defect the build should refuse.

### The survey instrument

There is none. The brief for this file asked how the survey instrument is presented; the honest answer is that it is not. Chapter 3 contains no questionnaire, no item wording, no response options, no sampling frame, no field dates and no n. It contains one table of coding categories and one sentence of description, inside the caption:

> We ask survey respondents what they hope an AI-transformed economy will look like in ten years. We classify their free-text responses into the general themes shown here.

**Annotation.** Twelve themes plus "Other" are defined, each in one semicolon-chained sentence of exemplars rather than a definition proper — "Less work: free time & drudgery automated away" is glossed as "More free time, shorter work weeks, or better work–life balance; AI does most of the day-to-day work, or work becomes optional altogether; retiring or exiting the workforce; a wider mix of activities across work and non-work; boring, repetitive, or administrative tasks automated away." The gloss enumerates what would *count*, which is what a coder needs and what a one-line abstract definition would not give. The residual category is defined by exclusion and nothing else: "Any economy-wide or personal hope not covered by the categories above." Themes are not defined as mutually exclusive, nor is it stated whether a response may receive more than one, nor who or what did the classifying — the sentence "We classify their free-text responses" leaves open whether the coder was a model or a person. For our own posts the equivalent table must say both. (Table A.1 is a rasterised image; see `## Verification`.)

## Comparisons

The document makes five comparisons and no others. Four are old-versus-new statements of method; one is numeric.

### The sampling baseline, in parentheses

> We now sample a fixed number of conversations every hour. (In previous Economic Index reports, our data spanned a week of activity.)

**Annotation.** New design as a main clause in the present tense; old design in parentheses in the past tense. No adjective of improvement, no claim that hourly sampling is better, no statement of what it costs — and, notably, no statement of what it does to comparability with the five earlier reports. The parenthesis is a record, not an argument. Copy the construction; do not copy the silence about comparability.

### The classifier, old and new, in adjacent sentences

> The previous classifier traversed a tree, first picking high-level ONET categories that we had hand-crafted. Now, the ONET classifier picks a detailed work activity (DWA) in the first step, then picks among the DWA’s constituent tasks in the second.

**Annotation.** Two sentences of equal length, one per design, with "Now," carrying the whole contrast. Both are described at the same grain — what it picks, in what order — so the difference is legible without a single comparative word. The pejorative is hidden in a relative clause on the old design only: "categories that we had hand-crafted." Nothing says the hand-crafted tree was worse; the reader is left to draw it. This is how to retire your own prior method without either defending or disowning it.

### The transcript window, with no number

> Relative to prior reports, we substantially expanded the portion of each transcript visible to the classifier and updated how we sample from very long conversations that would otherwise exceed length of conversations provided to the classifier. We do this to give the classifier as much context as possible for inferring the work being performed.

**Annotation.** The weakest comparison in the document, and useful as a negative example. "Relative to prior reports" promises a comparison; "substantially expanded" delivers an adverb instead of a magnitude. No token count, no character limit, no before-and-after. The sentence also contains the document's only grammatical slip ("exceed length of conversations provided to the classifier"), which is evidence these pages were written by the people who built the pipeline and lightly copy-edited. The second sentence recovers some ground by stating the objective ("as much context as possible") — a design *criterion* is given where a design *parameter* is withheld. A referee would ask for the number, and our own posts must state it.

### The cluster taxonomy, replaced without a mapping

> We also changed our request clusters. The top level clusters were changed to the following:

followed by the twenty-one cluster names run together as body prose, ending "Companionship & General Conversation, Customer Support & Service Operations."

**Annotation.** The new list is given in full; the old list is not given at all, and no crosswalk between them is offered. The reader is told a taxonomy changed and shown only one side of the change. Note also the presentation choice: twenty-one labels set as a running paragraph rather than a bulleted list or a table, with no counts and no definitions — the opposite of the artifact taxonomy on pp. 11–13, which gets a gloss per label. The asymmetry is unexplained. For our own posts the rule this suggests is explicit: if a classification changes between waves, publish the crosswalk or state plainly that none exists.

### The only numeric comparison

> On this surface, the share of conversations with no clear output is higher (16% vs 7% on chat and Cowork).

**Annotation.** Both sides of the contrast are given, in the same parenthesis, with the benchmark population named inside it — "vs 7% on chat and Cowork" — so neither number can be lifted without the other. The direction word ("higher") precedes the numbers; the numbers confirm it rather than announce it. Whole percentages, no decimals, no interval. This is the appendix's one sentence in the report's register.

**Robustness variants: none.** There is no robustness table anywhere in this document, no sensitivity analysis, no alternative specification, no leave-one-out, no comparison of the new classifier against the old one on the same transcripts, and no validation of either classifier against human labels. Figure A.1 is sometimes read as a robustness check — a second surface for the same measure — but it is presented as a description of 1P API, not as a test of whether the chat result survives. For an appendix whose first chapter documents a wholesale break in the measurement instrument, the absence of a single old-versus-new comparison on shared data is the most conspicuous thing in it, and it is the first thing a referee would raise.

## Figure captions

Two figures and one table, all in the "A." series. Captions sit below the exhibit, left-aligned to the page text block, in two parts: a **bold** label-and-title line, then a regular-weight gloss. Numbering is by appendix prefix (A.1, A.2), separate from the report's series (2.1), which is what allows the prose to say "mirrors Figure 2.1" without ambiguity.

### Figure A.1 — artifact distribution on 1P API

> **Figure A.1: Distribution of artifact types on 1P API.**
> Share of conversations with a specific output on 1P API. Top 10 output types presented individually.

**Annotation.** Pattern: *label, colon, noun-phrase title naming the quantity and the population, full stop* — then a gloss sentence that restates the quantity as a **unit** ("Share of conversations with a specific output"), repeats the population, and a second sentence that gives the **construction rule** ("Top 10 output types presented individually"). That second sentence is the one to copy: it discloses that the chart is truncated and that everything outside the top ten has been pooled, which is the difference between a reader understanding the residual bar and mis-reading it. The population appears twice in twenty-two words, which reads redundant and is not — the bold line travels alone when the figure is lifted. No n, no date range, no colour key, no axis names (the x-axis is labelled on the chart itself, and the caption does not duplicate it).

### Figure A.2 — autonomy against tokens

> **Figure A.2 : Autonomy and token usage by artifact**
> Mean autonomy and normalized median token consumption by artifact, chat and Cowork

**Annotation.** Same two-part pattern, and the same content ordering: *what is plotted, by what unit of observation, on what surface*. Both statistics are named with their estimator attached — "Mean autonomy", "normalized median token consumption" — so the reader knows one is a mean and one a normalised median before looking at an axis. "by artifact" names the unit of observation: each point is an artifact type, not a conversation, which is the single fact most likely to be misread off this chart, and the caption puts it in both lines. The surface is a bare appositive at the end, "chat and Cowork", with no preposition — terse to the point of telegraphic. What the caption does not do: it does not mention the dashed fit line, does not say the x-axis is a log scale relative to the overall median (that is printed on the chart), and does not say what the point sizes encode. Three chart elements go unexplained in the caption, and two of them (the fit line, the point size) are not explained anywhere.

Two typographic slips in this one caption, both worth recording because they show the captions were hand-set rather than generated: a stray space before the colon ("Figure A.2 :"), and no terminal full stop on either line, where A.1 has one on both.

### Table A.1 — the survey coding scheme

> **Table A.1: Ten-year vision themes and definitions.** We ask survey respondents what they hope an AI-transformed economy will look like in ten years. We classify their free-text responses into the general themes shown here.

**Annotation.** The only caption in the document whose gloss is *method* rather than units, and the reason is that the table is an instrument, not a result: there is nothing to give units for. The gloss does the two things the reader needs — it gives the question in reported speech ("what they hope an AI-transformed economy will look like in ten years", which is as close to item wording as the document comes) and it states the operation performed on the answers ("We classify their free-text responses into the general themes shown here"). Note the tense shift from every other caption: present habitual "We ask", "We classify", describing a standing procedure rather than one run of it. Note too that the bold portion here runs to a full stop and the gloss continues on the same line, where the two figure captions break the line — the table caption is set as a paragraph, the figure captions as a stacked pair. The table's own header row is two words, "Themes" and "Definition"; there is no count column, no share column and no n, so the table cannot be mistaken for a result.

**The caption pattern in summary.** Bold label with an "A."-prefixed number and a colon; a noun-phrase title naming the quantity and the population; then a gloss giving the estimator, the unit, the surface and any truncation or construction rule, in that order. Provenance of the classification goes in the caption when the exhibit *is* a classification. Nothing on the chart that is already legible on the chart is repeated. Neither "AI" nor "Claude" appears in any of the three captions; the sampled population is named by surface — "1P API", "chat and Cowork" — which is more precise than either, and is the convention to prefer when the surface is the thing that varies. (The chart image in Figure A.2 carries the panel title "Claude chat and Cowork"; the caption does not.)

**The seven example cards carry no captions at all** and are not in the figure series. They are identified only by the words "Example 1" … "Example 7" in the card's own header row, and referenced from prose as "In Example 2" and "In Example 7". Two consequences: the cards cannot be cited from outside the document, and five of the seven are never discussed anywhere. Showing exhibits you do not discuss is a deliberate choice here — it is what makes the seven read as a sample rather than a selection — but it only works because the cards use a fixed schema. Uncaptioned exhibits are not a licence for uncaptioned figures.

## Limitations

**There is no limitations section, no caveats heading, and no paragraph that collects the document's qualifications in one place.** Every limitation is stated at the point where the method that causes it is described. Collected, verbatim, in order of appearance:

> Since Claude may have order preferences over the categories presented to it, we shuffle the options in the prefix (using a predefined set of orderings to preserve caching).

> This randomization was meant to spread the choice across the multiple candidates in order to avoid many transcripts piling up into one specific (and arbitrary) work task.

> We classify transcripts in a privacy-preserving way. To illustrate how the classifiers work, we present some example classifications using transcripts drawn from WildChat,1 an open-source dataset of user-ChatGPT interactions. (Some assistant’s responses were abbreviated for presentation below.)

> The examples are meant to illustrate the utility and limitations of the approach.

> This receives an accurate (based on our judgment) ONET classification

> It is also classified as a personal use case, although this is hard to prove. It’s often difficult to infer how the output was used.

> In Example 7, the question, “Which Rust library is best for Natural Language Processing (NLP)?” is mapped to a sales occupation although the question is substantively about computer programming.

**Annotation.**

- **Where they sit.** Inline, each within a sentence or two of the design decision it qualifies. There is nothing to skip and nothing to defer to, which is the strength of the arrangement; the weakness is that no reader can see the set of them at once, and the document never totals up what it does not know.
- **The WildChat substitution is the largest limitation in the document and is never labelled as one.** Because classification is privacy-preserving, no Claude transcript can be shown, so every worked example is a ChatGPT transcript from a public 2024 dataset. The consequence — that the seven examples demonstrate the classifier's behaviour on *other* traffic, not on the traffic the report's numbers come from — is left for the reader to draw. The sentence is written as a description of a method ("We classify transcripts in a privacy-preserving way"), and the cost is implicit. A version of this constraint will apply to our own posts whenever an illustration cannot use the analysed data; the house treatment must name the cost explicitly, in the same paragraph.
- **How specific.** Particular, never ritual. There is no "as with all studies" sentence, no "these findings should be interpreted with caution", no generic appeal to future work. Every concession names a mechanism: order sensitivity, tie-breaking arbitrariness, unobservable use of output, act-versus-topic confusion in the occupational mapping. Two of them come with a worked instance.
- **The hedge inventory is small and consistent.** "may", "meant to", "(and arbitrary)", "based on our judgment", "hard to prove", "often difficult", "might have been better", "tend to". Every one is attached to the claim it qualifies, in the same sentence, and none is a stand-alone disclaimer sentence.
- **What is missing, in the order a referee would raise it.** (1) No comparability statement: the sampling design, the ONET version and the classifier architecture all changed at once, so this release's occupational shares are not on the same footing as the five earlier reports', and the document neither says so nor bounds it. (2) No validation: no human-labelled sample, no agreement statistic, no accuracy rate for either classifier — the only evidence of quality is seven examples and the authors' own judgement. (3) No frequency for the step-2 tie-breaking randomisation, so its influence is unbounded. (4) No n anywhere, for any surface, and no uncertainty on any share. (5) No crosswalk from the old request clusters to the new twenty-one. (6) No statement of the confidence threshold used in production, although the prompt defines a 1–5 scale and tells the model that 1 is "near-noise". (7) The classifier prompts are shown but the model that ran them is not named, nor is the date it ran. Any one of these would be a first-round referee comment on our own post.

## Close

**There is no close.** The document's last elements, in order, are: the Chapter 3 heading, Table A.1, the table's caption, a horizontal rule, and footnote 1. No concluding sentence, no summary of what the appendix established, no pointer back to the report, no statement of what comes next, no data or code availability note, no contact address.

Verbatim, the last prose in the document — the Table A.1 caption and the footnote:

> **Table A.1: Ten-year vision themes and definitions.** We ask survey respondents what they hope an AI-transformed economy will look like in ten years. We classify their free-text responses into the general themes shown here.

> 1 Zhao, W., Ren, X., Hessel, J., Cardie, C., Choi, Y., & Deng, Y. (2024). Wildchat: 1m ChatGPT interaction logs in the wild. arXiv preprint arXiv:2405.01470.

**Annotation.**

- **What ending on a table achieves.** The appendix stops when it has handed over the last object it was holding. Nothing is concluded because nothing was argued. This is the correct ending for the genre and the clearest single lesson in this file: an appendix that ends with "In conclusion, this appendix has presented…" has misunderstood what it is. The reader's exit is back to the report, and the running footer on the final page is what points them there.
- **The one reference is a footnote, not a bibliography.** A fifteen-page document that cites one external work cites it where it is used (p. 6, superscript 1) and prints it in full author-date form at the foot of the page it appears on — fourteen pages later, because the footnote is deferred to the end of the document rather than the foot of p. 6. That deferral is almost certainly a layout artefact rather than a choice, and it is the one thing in the document's construction that actively hinders the reader.
- **Why it matters is absent, and correctly so.** The document contains no sentence about why any of this is important. The stakes were spent in the report. An appendix that re-argues the stakes is padding; an appendix that omits a design parameter to make room for stakes has traded the wrong way.
- **Title against ending.** The title names its parent and nothing else, and the ending is a coding scheme — so the "title matches the ending" test does not apply to this genre in the form it applies to a post. The equivalent test for an appendix is *does the last page belong to the chapter its number claims*, and here it does: Chapter 3 of the appendix serves Chapter 3 of the report.
- **The heading that differs between the two published copies.** The Chapter 3 heading reads "Ten-year vision themes and definitions" in the copy at `03ed1410…` and "Vision themes and definitions" in the copy at `8eb31e1d…`. The Table A.1 caption reads "Ten-year vision themes and definitions." in both. Nothing else in the two files differs. Two copies of a methodology appendix are live on the CDN with different last-page headings, and neither carries a version marker or a revision date — which is an argument, for our own work, for a version line and a content hash on anything republished.

## Verification

- **URLs fetched:** https://cdn.sanity.io/files/4zrzovbb/website/03ed1410f74a65ae4cc2a27120d0875e1e569535.pdf (HTTP 200, 2,707,986 bytes, 15 pages) and https://cdn.sanity.io/files/4zrzovbb/website/8eb31e1d187ff18146d248bbef8b2754971f0f5a.pdf (HTTP 200, 2,707,791 bytes, 15 pages). Both fetched 2026-09-16.
- **Fetch method.** `web_fetch` refuses `cdn.sanity.io`, so both files were retrieved with `curl` in the sandbox. Text was extracted with `pdftotext -layout` and `pdftotext`, page inventory with `pypdf`, and page images rendered with `pdftoppm -r 120/130 -png`. PDF metadata: Creator "Adobe InDesign 21.4 (Macintosh)", Producer "Adobe PDF Library 18.0", CreationDate 2026-06-26.
- **Difference between the two copies.** `diff` of the two `-layout` extractions returns exactly one substantive hunk: the Chapter 3 heading, "Ten-year vision themes / and definitions" in `03ed1410…` against "Vision themes and definitions" in `8eb31e1d…`. All other text, including the Table A.1 caption, is identical. All quotations in this file are from `03ed1410…`, the primary URL in `wiki/INDEX.md`.
- **Pages with no text layer.** Pages 6–10 and 15 carry their tables as rasterised images (JP2), and page 13 carries its chart as a PNG. `pdftotext` returns only the running footer for pages 7, 8 and 9. The content of the seven example cards, the six row labels in each card, and the twelve theme names and definitions in Table A.1 were therefore **transcribed from page renders**, not from a text layer; they are described and quoted in this file as structure and wording, and each place where that applies is marked in the text. All body prose, all prompt text, both figure captions, the Table A.1 caption, the chapter headings and the footnote **do** have a text layer and were copied from it.
- **Chart values.** Applying `room/director-2026-09-16-alt-text-ruling.md`: no number was read off the chart images in Figure A.1 or Figure A.2 and none is recorded here. The percentages quoted in `## Findings and their caveats` and `## Comparisons` are from the body prose on page 13, which is text-layer. The one-point disagreement between a prose value and the corresponding bar label on Figure A.1 is noted without recording the chart value.
- **Quotation caveats.** Typographic apostrophes, quotation marks, dashes and the multiplication-style separators in the source were left as they appear where they are part of the quoted text and normalised only where the extraction produced soft-hyphen or line-break artefacts; no word was changed, no word was added, and hard line wraps inside a quoted paragraph were closed up. The footnote marker "1" appears inline in the WildChat sentence as it does in the extraction. Emphasis and bold are reproduced as set. Where the source itself is ungrammatical ("exceed length of conversations provided to the classifier") the error is quoted intact and flagged in annotation.
- **Not fetched, deliberately:** the parent report at https://www.anthropic.com/research/economic-index-june-2026-report and its PDF `9e0eadc8…` (separate slug, `economic-index-2026-06-report`); the WildChat paper at arXiv:2405.01470; the Economic Index hub page. Nothing from any of them is quoted here, and no claim in this file about the parent report's contents goes beyond what the appendix itself states (its chapter numbering and the phrases "mirrors Figure 2.1" and "the display names used throughout Chapter 2").
- **Could not fetch:** nothing. Both URLs returned in full on the first attempt. `web_fetch` on `cdn.sanity.io` was not attempted, per the standing instruction that it refuses that host.
- **Scope.** This file annotates how the piece is written. It makes no judgement about whether its method is sound or its numbers are correct.
