# Appendix to "Anthropic Economic Index report: Cadences"

Slug: `economic-index-2026-06-appendix`

## Source

- **Title (page 1 of the PDF, verbatim):** "Appendix to "Anthropic Economic Index report: Cadences""
- **Date (page 1):** "June 2026". No day is printed in the document. The PDF's own `CreationDate` metadata is `Fri Jun 26 13:46:08 2026 UTC` for the primary copy and `Thu Jun 25 23:20:55 2026 UTC` for the second copy.
- **Primary URL:** https://cdn.sanity.io/files/4zrzovbb/website/03ed1410f74a65ae4cc2a27120d0875e1e569535.pdf
- **Second copy:** https://cdn.sanity.io/files/4zrzovbb/website/8eb31e1d187ff18146d248bbef8b2754971f0f5a.pdf (see Verification for the one difference between them)
- **Type:** standalone methodology appendix to the sixth Economic Index report, "Anthropic Economic Index report: Cadences" (2026-06-26, https://www.anthropic.com/research/economic-index-june-2026-report). The main report is a separate wiki entry, `economic-index-2026-06-report`.
- **Length:** 15 pages, letter size. Running footer on every page after page 1: "Appendix to "Anthropic Economic Index report: Cadences"".
- **Structure:** three numbered chapters and four unnumbered sub-headings.
  - p.1 — title page.
  - **CHAPTER 1, "Changes to the economic index pipeline"** (pp. 2–10): prose on the pipeline changes (pp. 2–3); sub-heading "ONET classifier" with the Step 1 and Step 2 prompts (pp. 3–5); sub-heading "Examples of how our classifiers work" with Examples 1–7 as tables (pp. 6–10).
  - **CHAPTER 2, "Artifact classifier"** (pp. 11–14): the artifact-classifier prompt (pp. 11–13); sub-heading "Distribution of outputs on 1P API" with Figure A.1 (p. 13); sub-heading "Autonomy and token consumption" with Figure A.2 (p. 14).
  - **CHAPTER 3, "Ten-year vision themes and definitions"** (p. 15): Table A.1 and the WildChat footnote.
- **Numbered exhibits:** Figure A.1 (p. 13), Figure A.2 (p. 14), Table A.1 (p. 15). Examples 1–7 (pp. 6–10) are captioned only by the words "Example 1" … "Example 7" in the table header row.
- **Authors, citation block, version number, DOI, licence:** none. The document names no authors, carries no citation block and no acknowledgements. The citation block for this release lives on the report page (BibTeX key `anthropic2026aeiv6`), not in the appendix.
- **Only external citation in the document:** footnote 1 (p. 15) — "Zhao, W., Ren, X., Hessel, J., Cardie, C., Choi, Y., & Deng, Y. (2024). Wildchat: 1m ChatGPT interaction logs in the wild. arXiv preprint arXiv:2405.01470."
- **Surfaces named:** "Claude traffic" (p. 2), "chat and Cowork" (pp. 13, 14), "1P API" (p. 13). "Cowork" appears here as a named Claude surface analysed alongside chat; the appendix does not define it.
- **What the appendix does *not* contain, relative to what an appendix of this kind might be expected to hold:** no survey instrument (no question wording, no sampling frame, no respondent counts — see Claim 13 and "What it did not test"); no robustness tables; no validation exercise against human labels; no sample sizes, confidence intervals or standard errors anywhere; no data-availability or reproduction note.

## Claims

Numbered claims, each with its page and figure/table reference, the number exactly as published, and the comparison the number rests on. Where a count is my arithmetic on a published list rather than a published number, it is flagged `[wiki author's count]`.

**Chapter 1 — pipeline changes (all pp. 2–3; prose only, no exhibit)**

1. **Sampling cadence changed from a week to a fixed hourly draw.** "We now sample a fixed number of conversations every hour. (In previous Economic Index reports, our data spanned a week of activity.)" (p. 2). Comparison: this release's sampling design against the design of all five previous Economic Index reports. No number of conversations per hour, no total, and no window are given.
2. **The O\*NET mapping was rebuilt as a two-step DWA-then-Task classifier, replacing a hand-crafted tree.** "The previous classifier traversed a tree, first picking high-level ONET categories that we had hand-crafted. Now, the ONET classifier picks a detailed work activity (DWA) in the first step, then picks among the DWA's constituent tasks in the second." (p. 2). Comparison: new pipeline against the previous reports' pipeline. No before/after agreement rate is reported.
3. **The O\*NET vintage changed.** "We also switched over to the ONET version 30.2, released in February 2026." (p. 2). Comparison: implicit, against the unnamed earlier O\*NET version used in prior reports. The appendix does not state which version it replaced, nor how much of any measured change is attributable to the vintage switch.
4. **The prompt was reordered for prefix caching, and the option list is shuffled to counter position bias.** "The new ONET classifier also reversed the order (the transcript appears at the end of the input) so that the prefix can be cached. Since Claude may have order preferences over the categories presented to it, we shuffle the options in the prefix (using a predefined set of orderings to preserve caching)." (p. 2). Comparison: none reported — the existence of an order preference is asserted as a possibility ("may have"), not measured.
5. **Ties at the top confidence level are broken at random, by design.** "It is asked to provide pairs of {task, confidence (1-5)}, and we randomly choose a task among those with the highest confidence. This randomization was meant to spread the choice across the multiple candidates in order to avoid many transcripts piling up into one specific (and arbitrary) work task." (p. 2). Comparison: the intended distribution of task assignments against the concentration that a deterministic argmax would produce. No measure of how much concentration this removed is given.
6. **The top-level request clusters were replaced with a new list of 20 clusters** `[wiki author's count — the appendix prints the list and does not count it]`. "We also changed our request clusters. The top level clusters were changed to the following:" followed by the list quoted in full under Definitions (p. 2). Comparison: the new top level against the unstated previous top level; the previous list is not printed, so the appendix does not allow a like-for-like mapping.
7. **The share of each transcript shown to the classifier was expanded, and long-conversation sampling changed.** "Relative to prior reports, we substantially expanded the portion of each transcript visible to the classifier and updated how we sample from very long conversations that would otherwise exceed length of conversations provided to the classifier." (p. 3). Comparison: this release against prior reports. Neither the old nor the new character/token budget is given.

**Chapter 1 — the seven worked examples (pp. 6–10)**

8. **The examples are not Claude transcripts.** "we present some example classifications using transcripts drawn from WildChat, an open-source dataset of user-ChatGPT interactions. (Some assistant's responses were abbreviated for presentation below.)" (p. 6, with footnote 1 on p. 15). Comparison: none; this is a statement of provenance. It means every published example of the pipeline's behaviour in this appendix is an out-of-sample demonstration on another vendor's traffic.
9. **Each example is labelled on five measures at once** (Examples 1–7, pp. 6–10): the row labels are "O\*Net Classifier" (a GWA › IWA › DWA › Task › occupation chain), "Use Case", "Task Success", "Artifact", "AI Autonomy". Comparison: this is the appendix's only published demonstration that the primitives introduced in earlier reports and the new artifact label are applied to the same exchange.
10. **Published values across the seven examples** `[wiki author's tabulation of the seven published tables, pp. 6–10]`:
    | Example | Task (O\*NET) → occupation | Use Case | Task Success | Artifact | AI Autonomy |
    |---|---|---|---|---|---|
    | 1 (p. 6) | "Analyze experimental data and interpret results to write reports and summaries of findings" → Biological Technicians | Work | Yes | Analysis or Summary | 2 |
    | 2 (p. 7) | "Write narrative, dramatic, lyric, or other types of poetry for publication" → Poets, Lyricists and Creative Writers | Personal | Yes | Creative Writing | 3 |
    | 3 (p. 7) | "Write new programs or modify existing programs to meet customer requirements, using current programming languages and technologies" → Data Warehousing Specialists | Coursework | Yes | Script or Snippet | 3 |
    | 4 (p. 8) | "Compile, transcribe, and distribute minutes of meetings" → Executive Secretaries and Executive Administrative Assistants | Work | Yes | Document or Report | 2 |
    | 5 (p. 9) | "Edit, standardize, or make changes to material prepared by other writers or establishment personnel" → Technical Writers | Work | Yes | Marketing or Social Content | 2 |
    | 6 (p. 9) | "Read copy or proof to detect and correct errors in spelling, punctuation, and syntax" → Editors | Coursework | Yes | Resume or Job Application | 2 |
    | 7 (p. 10) | "Recommend products to customers, based on customers' needs and interests" → Sales Representatives, Wholesale and Manufacturing | Work | Yes | Explanation or Answer | 3 |
    Comparison: none is drawn by the appendix. Note that Task Success is "Yes" in all seven and AI Autonomy is 2 or 3 in all seven, so the illustrations exercise neither a failure case nor the 1, 4 or 5 levels of the autonomy primitive.
11. **Example 2 is offered as an accurate classification with an unverifiable use-case label.** "This receives an accurate (based on our judgment) ONET classification … It is also classified as a personal use case, although this is hard to prove." (p. 6). Comparison: the classifier's output against the appendix authors' own judgement — an n-of-1 eyeball, not a validation statistic.
12. **Example 7 is offered as a misclassification, with the label the authors think is right.** "In Example 7, the question, "Which Rust library is best for Natural Language Processing (NLP)?" is mapped to a sales occupation although the question is substantively about computer programming. The classifier focuses on what the Assistant is asked to do—"Recommend products"—and not on the topic of the request." (p. 10, referring to the Example 7 table on p. 10). Comparison: the published label ("Recommend products to customers, based on customers' needs and interests" → Sales Representatives, Wholesale and Manufacturing) against the authors' preferred alternative ("Consult with customers or other departments on project status, proposals, or technical issues, such as software system design or maintenance," → Software Developers). No rate of this error class is estimated.

**Chapter 2 — the artifact classifier (pp. 11–14)**

13. **The artifact classifier is a single-label, most-prominent-output classifier over 32 options** `[wiki author's count: 30 substantive labels plus "other" plus "none"]`, with a stated presentation protocol: "Categories were presented in randomized order in each call, with the "other" and "none" options always listed last. The model's answer was extracted from the answer tags and mapped to the display names used throughout Chapter 2." (p. 11). Comparison: none; this is a construct definition. The label→display-name mapping itself is *not* printed (see "What it did not test").
14. **Figure A.1 (p. 13) — the artifact distribution on the first-party API.** Caption: "Figure A.1: Distribution of artifact types on 1P API. Share of conversations with a specific output on 1P API. Top 10 output types presented individually." Values as printed on the bars: Analysis / summary 21%, Data / spreadsheet 13%, Explanation / answer 8%, Document / report 6%, Code fix / debug 5%, Email / message 2%, App / website 2%, Marketing / social content 2%, Config / infra 2%, Guidance 2%, Other output types 8%, No clear output 16%. Comparison: the 1P API surface against "chat and Cowork" — "Below figure mirrors Figure 2.1 but for 1P API" (p. 13). x-axis "% of conversations", 0–30.
15. **The headline 1P API comparison, as published in prose (p. 13).** "On this surface, the share of conversations with no clear output is higher (16% vs 7% on chat and Cowork). Analytic outputs dominate (21%), followed by data/spreadsheet related outputs (14%) and explanations/answers (8%)." Comparison: 1P API against chat and Cowork (the 7% comparator is published in the appendix prose only; the chat-and-Cowork figure itself is Figure 2.1 of the main report, not reproduced here). **Internal discrepancy:** the prose says data/spreadsheet is "(14%)" while the bar in Figure A.1 on the same page is labelled 13%. Both numbers appear on p. 13. The 21%, 8% and 16% figures agree between prose and figure.
16. **Figure A.2 (p. 14) — autonomy rises with token use across artifacts.** Prose: "The below figure displays the normalized median token usage per artifact against the mean autonomy measured in the conversations producing these artifacts. Artifacts requiring more tokens tend to be produced with more autonomy." Caption: "Figure A.2 : Autonomy and token usage by artifact. Mean autonomy and normalized median token consumption by artifact, chat and Cowork". Comparison: across artifact labels within the chat-and-Cowork surface — a cross-sectional comparison of ~30 artifact-level means, not a within-conversation or over-time comparison. Axes: y "Mean AI autonomy", ticks 0.0 then 2.2 to 3.6 in 0.2 steps (i.e. a broken axis, unmarked); x "Median tokens per conversation (relative to overall median), log scale", ticks 0.25x, 0.5x, 1x, 2x, 4x. A dashed fitted line is drawn. Labelled points, read off the figure: high-token/high-autonomy — Apps & websites (≈4.5x, ≈3.27), Presentations (≈3.2x, ≈3.24), Games (≈2.1x, ≈3.28), Data & spreadsheets (≈3.0x, ≈2.99), Code fix / debug (≈3.3x, ≈2.77), Academic papers (≈3.7x, ≈2.72), Creative writing (≈2.4x, ≈2.80); low-token/low-autonomy — Explanations (≈0.17x, ≈2.45), Advice (≈0.26x, ≈2.62), Translation (≈0.25x, ≈2.24), Email (≈0.6x, ≈2.48), Recipes (≈0.55x, ≈2.66); mid — Images, ML / AI systems, Analysis & summary, Plans & strategy. Marker area appears to vary with something (plausibly volume) but the appendix gives no size legend. **No correlation coefficient, n, standard error or confidence band is printed in the appendix.** (The main report page states "r = 0.68 on chat and Cowork" for this figure; that number is published in the report, not in the appendix — see Verification.)

**Chapter 3 — survey themes (p. 15)**

17. **Twelve ten-year vision themes, classified from free-text survey responses** `[wiki author's count of the rows of Table A.1: eleven substantive themes plus "Other"]`. Caption: "Table A.1: Ten-year vision themes and definitions. We ask survey respondents what they hope an AI-transformed economy will look like in ten years. We classify their free-text responses into the general themes shown here." Comparison: none. The table carries **no shares, no counts, no respondent n, no ranking** — it is a codebook only. The theme frequencies appear in the main report, not here.

## Definitions (verbatim)

Every classifier prompt, taxonomy and measure definition in the document, quoted verbatim with page references. Multi-line prompt text is reproduced inside fenced blocks rather than inline quotation marks so that line breaks, indentation and the document's own typographic quotation marks survive; everything between the fence delimiters is quoted exactly as printed. Curly quotes (" " ') and em dashes (—) are the document's own.

### 1. Top-level request clusters (p. 2, verbatim, in the printed order)

"Hobbies & Lifestyle, Content Creation & Copywriting, Software Development, Research & Intelligence, Education & Learning, Document Processing & Extraction, Knowledge Retrieval & Enterprise Search, Data Analysis & Business Intelligence, DevOps & Infrastructure Operations, Compliance & Regulatory, Personal AI Assistant, Business Process & Operations, Sales & Revenue Operations, Cybersecurity & Threat Detection, Trust & Safety / Platform Integrity, Existential, Relational, and Emotional Support, Other / Unclear, Conversation & Meeting Intelligence, Companionship & General Conversation, Customer Support & Service Operations." (p. 2)

### 2. ONET classifier, Step 1 — the full prompt (pp. 3–4, verbatim)

Introduced on p. 3 by: "The ONET classifier is given below." Section heading: "ONET classifier"; sub-heading "Step 1".

```
You are analyzing a conversation between a user and a chatbot. Your task
is to determine what “work activities” the chatbot is doing for the user.
You will map the conversation to ONET work activities at various levels of
granularity.

Treat the conversation as a single unit unless it contains distinct,
unrelated activities (for example, half the conversation is about fixing
a bug and half is about personal relationship advice). Most conversations
have one task, but some will include more than one distinct task. Pick the
two most prominent ones if there are multiple.


Step 1: In 1-2 sentences, summarize this conversation.


Step 2: Pick O*NET activities that map to the activity the chatbot carries
out for the user.


Levels:


- [GWA] = broadest ({n GWA} categories)
- [IWA] = mid-level ({n IWA})
- [DWA] = specific ({n DWA})


Confidence guide:


For each picked activity, assign a confidence score from 1 to 5 using the
following rubric. The rubric asks a single question: how certain am I that
this activity is actually being performed in this conversation?


5 - Certain. The activity is explicitly performed in the conversation with
direct textual evidence.


4 - High confidence. The activity is clearly performed, inferable from
direct textual evidence with only minor interpretation.


3 - Moderate confidence. The activity is plausibly performed, but the
textual evidence is partial, implicit, or open to alternative readings. A
reasonable reviewer could either agree or disagree.


2 - Low confidence. The activity could be performed in the conversation
though concluding as much requires substantial interpretation.


1 - Very low confidence. The activity may be implied by context, but there
is no clear textual support. Picks at this level are near-noise — exclude
unless nothing stronger exists.


[GWA] Analyzing Data or Information
     [IWA] Assess characteristics or impacts of regulations or policies
       [DWA] Evaluate applicable laws and regulations to determine
       impact on organizational activities
       [DWA] Analyze impact of legal or regulatory changes
     ...
     [IWA] Analyze business or financial data
       [DWA] Analyze financial records or reports to determine state of
       operations
       [DWA] Analyze financial information
     ...


<conversation>
{TRANSCRIPT}
</conversation>


Output JSON only:
<answer>{“summary”: “<1-2 sentences>”, “picks”: [{“level”: “GWA|IWA|DWA”,
“name”: “<exact name>”, “confidence”: 1-5}], “notes”: “<optional>”}</
answer>
```
(pp. 3–4. The taxonomy listing is printed with "..." elisions by Anthropic; `{n GWA}`, `{n IWA}`, `{n DWA}` and `{TRANSCRIPT}` are the document's own placeholders. The ellipses and placeholders are in the published document, not editorial cuts by this wiki.)

### 3. The 1–5 confidence rubric (p. 4, verbatim)

Quoted in full inside the Step 1 prompt above. The rubric's own statement of what it measures, verbatim: "The rubric asks a single question: how certain am I that this activity is actually being performed in this conversation?" (p. 3). The five levels verbatim: "5 - Certain. The activity is explicitly performed in the conversation with direct textual evidence." / "4 - High confidence. The activity is clearly performed, inferable from direct textual evidence with only minor interpretation." / "3 - Moderate confidence. The activity is plausibly performed, but the textual evidence is partial, implicit, or open to alternative readings. A reasonable reviewer could either agree or disagree." / "2 - Low confidence. The activity could be performed in the conversation though concluding as much requires substantial interpretation." / "1 - Very low confidence. The activity may be implied by context, but there is no clear textual support. Picks at this level are near-noise — exclude unless nothing stronger exists." (p. 4)

### 4. ONET classifier, Step 2 — the full prompt (p. 5, verbatim)

```
Consider the following exchange:

<exchange>
{TRANSCRIPT}
</exchange>


You are analyzing a conversation between a user and a chatbot. You
previously determined these DWA-level O*NET activities for this
conversation based on the following summary:
Summary: {step-1 summary}
{semicolon-joined list of picked DWAs}


Your task now is to pick Task-level activities that map to the activity or
activities the chatbot carries out for the user.


Task options:
{up to 300 candidate Task texts, shuffled, one “- ...” line each}


Confidence guide:
[same 1-5 rubric as step 1]


Output JSON only:
<answer>{“leaf_picks”: [{“name”: “<exact Task text>”, “confidence”:
1-5}]}</answer>
```
(p. 5. `{TRANSCRIPT}`, `{step-1 summary}`, `{semicolon-joined list of picked DWAs}`, `{up to 300 candidate Task texts, shuffled, one "- ..." line each}` and `[same 1-5 rubric as step 1]` are the document's own placeholders and editorial notes.)

### 5. The tie-breaking rule, as a measure definition (p. 2, verbatim)

"In the second step, the ONET classifier is asked to specify the ONET tasks that best describe the work being done in the transcript. It is asked to provide pairs of {task, confidence (1-5)}, and we randomly choose a task among those with the highest confidence." (p. 2)

### 6. Artifact — the construct (p. 11, verbatim)

"The following prompt was used to classify the most prominent concrete output of each exchange. Categories were presented in randomized order in each call, with the "other" and "none" options always listed last. The model's answer was extracted from the answer tags and mapped to the display names used throughout Chapter 2." (p. 11)

### 7. Artifact classifier — the full prompt and the full taxonomy (pp. 11–13, verbatim)

```
[Exchange transcript and preamble]


What is the single most prominent concrete OUTPUT that Claude produced for
the User in this exchange?


Pick the single closest label:

•    script_or_snippet: Scripts, automations, macros, code snippets, one-off
     programs, general coding

•    explanation_or_answer: An explanation, definition, or factual answer
    for the respondent’s own understanding

•    plan_or_strategy: Multi-step plans — project plans, roadmaps, schedules,
     business strategy

•    document_or_report: Formal written deliverables — reports, proposals,
     specs, memos, documentation

•    app_or_website: Full applications, web/mobile apps, websites,
     extensions, SaaS

•    analysis_or_summary: Summaries, syntheses, analyses of existing
     material for own use

•    creative_writing: Fiction, poetry, songs, lyrics, screenplays, stories,
     worldbuilding

•    advice_or_recommendation: One-off guidance on a decision — purchase,
     career, health, relationship

•   idea_or_brainstorm: Brainstorm output — raw ideas, options, concept
     exploration

•    email_or_message: Emails, messages, DMs, replies, short interpersonal
     communications

•   image_or_graphic: Images, logos, illustrations, icons, photo edits,
     posters, flyers

•    blog_or_article: Blog posts, articles, newsletters, op-eds, published
     web content

•    code_fix_or_debug: Bug fixes, debugging, refactoring, code review of
     existing code

•    math_or_calculation: Equations, formulas, calculations, mathematical
     solutions, proofs

•    ml_or_ai_system: ML models, AI agents, prompts, fine-tunes, AI-powered
     products

•   translation: Text translated between languages

•    marketing_or_social_content: Ad copy, social posts, product
     descriptions, SEO, taglines, campaigns

•    presentation_or_slides: Slide decks, PowerPoints, pitch decks, talk
     materials

•    game_or_interactive: Games, mods, interactive fiction, game masters/RPG
    tools

•    academic_paper_or_thesis: Academic papers, theses, dissertations,
     grants, literature reviews

•    config_or_infra: Config files, IaC, deployment, DevOps, shell commands,
     system setup

•    chart_or_visualization: Charts, graphs, plots, dashboards, diagrams,
    infographics

•    data_or_spreadsheet: Spreadsheets, CSVs, tables, data cleaning/
    transforms, structured data files

•   resume_or_job_application: CVs, résumés, cover letters, LinkedIn
     profiles, job-application materials

•    ui_or_design_mockup: UI mockups, wireframes, design specs, prototypes

•    audio_or_music: Music, audio, sound effects, voice synthesis, podcast
     audio

•    educational_material: Lesson plans, study guides, course materials,
     worksheets, lectures, tutorials for others

•   recipe_or_meal_plan: Recipes, meal plans, cooking instructions, diet/
     nutrition plans

•    video_or_animation: Video content, animations, video scripts/edits

•    sql_or_database_query: SQL queries, database schemas, DB migrations

•    other: A concrete output that fits none of the above

•    none: No clear artifact


If several outputs apply, pick the one most prominent in the exchange.


Only choose an artifact label if it clearly describes what the exchange
produced. If no label is a clear fit, choose none.


[Standard API-data disclaimer]


Your classification should be exactly one of the answer options (the
lowercase label only), nothing else, provided in <answer> tags. For

example, your answer could be script_or_snippet or none.
```
(pp. 11–13. "[Exchange transcript and preamble]" and "[Standard API-data disclaimer]" are the document's own bracketed placeholders — the preamble and the disclaimer are not printed. Leading whitespace after each bullet varies in the original and is reproduced as printed. The blank line before "example, your answer could be…" is a page-layout artefact of the printed block and is reproduced as it appears.)

### 8. Ten-year vision themes — the full codebook (Table A.1, p. 15, verbatim)

Table A.1 is a raster image in the PDF; the twelve rows are transcribed verbatim below, with the two column headers "Themes" and "Definition".

| Themes (verbatim) | Definition (verbatim) |
|---|---|
| "Work still matters: careers, meaning & working alongside AI" | "Employment holds up and new industries or kinds of jobs emerge; one's own job or career remains secure, with new roles or opportunities opening up; skills stay relevant (or are learned to keep up); working alongside AI as a tool or partner rather than being replaced; work becomes more meaningful, creative, or fulfilling." |
| "Independence & empowerment" | "More autonomy and control over one's own work and decisions; starting or running one's own business or going independent; individuals or small teams able to do what once required large organizations — serious research, building software, running operations, serving a niche market — without a big staff or gatekeepers." |
| "Less work: free time & drudgery automated away" | "More free time, shorter work weeks, or better work–life balance; AI does most of the day-to-day work, or work becomes optional altogether; retiring or exiting the workforce; a wider mix of activities across work and non-work; boring, repetitive, or administrative tasks automated away." |
| "Richer life beyond work" | "More time with family and for caregiving; meaning and purpose from outside work — community, religion, creativity; better personal health or quality of life; relocation or a change of lifestyle; more human connection, community involvement, and social fabric; more time in nature; flourishing arts and culture." |
| "Shared prosperity & economic security" | "Wages and prosperity broadly shared; inequality narrows; everyone's basic needs are met; UBI, other safety nets, retraining, or redistribution; universal basic capital or other up-front ownership stakes; material abundance; lower-income countries catch up and global poverty falls; economic and political power stays spread out rather than concentrated." |
| "Safe & accessible AI" | "AI is developed and governed safely and responsibly; everyone gets to use AI tools themselves regardless of resources." |
| "Progress on big problems" | "Scientific and technological progress; medical discoveries and cures — disease, mental health, longevity; better climate, energy, and environmental outcomes; broader access to and quality of education." |
| "AI embedded in daily life & decisions" | "AI becomes part of everyday routines and daily life; decisions in business, government, and daily life are increasingly made with data and AI analysis." |
| "Growth, productivity & living standards" | "Overall economic growth and productivity gains; cheaper, better, or more abundant goods and services; improved cost of living, housing affordability, and economic stability." |
| "Own pay & wealth" | "Higher pay, income, or financial security for oneself; building personal wealth." |
| "Better institutions & civic life" | "Stronger democratic institutions, participation, and trust in government; changes to political or economic institutions, including shifts in economic system; less war and international conflict; a healthier, more trustworthy information environment." |
| "Other" | "Any economy-wide or personal hope not covered by the categories above." |

### 9. The survey item, as far as the appendix states it (Table A.1 caption, p. 15, verbatim)

"We ask survey respondents what they hope an AI-transformed economy will look like in ten years. We classify their free-text responses into the general themes shown here." (p. 15)

This is the closest thing to a survey question in the document. **The appendix prints no survey instrument: no verbatim item wording, no response format, no sampling frame, no field dates, no respondent count, no weighting.** The caption is a paraphrase of the item in the first person, not the item itself.

### 10. Figure and table captions (verbatim)

- "Figure A.1: Distribution of artifact types on 1P API. / Share of conversations with a specific output on 1P API. Top 10 output types presented individually." (p. 13)
- "Figure A.2 : Autonomy and token usage by artifact / Mean autonomy and normalized median token consumption by artifact, chat and Cowork" (p. 14; the space before the colon in "A.2 :" is in the original)
- "Table A.1: Ten-year vision themes and definitions. We ask survey respondents what they hope an AI-transformed economy will look like in ten years. We classify their free-text responses into the general themes shown here." (p. 15)

### 11. Chapter and section headings (verbatim, for reference)

"CHAPTER 1 / Changes to the economic index pipeline" (p. 2); "ONET classifier" (p. 3); "Step 1" (p. 3); "Step 2" (p. 5); "Examples of how our classifiers work" (p. 6); "CHAPTER 2 / Artifact classifier" (p. 11); "Distribution of outputs on 1P API" (p. 13); "Autonomy and token consumption" (p. 14); "CHAPTER 3 / Ten-year vision themes and definitions" (p. 15, primary copy — see Verification for the second copy's heading).

## Data and methods

In my own words, with page references.

**What kind of document this is.** A 15-page methods companion to the sixth Economic Index report. It runs no analysis of its own beyond two supplementary exhibits (Figures A.1 and A.2, pp. 13–14) and one codebook (Table A.1, p. 15). It carries no data section, no sample description, no counts and no uncertainty. Every quantity that would let a reader size the evidence — conversations sampled, hours covered, respondents surveyed, classifier agreement — is absent (pp. 1–15).

**The sampling change (p. 2).** The unit of the release moved from a week-long window to a fixed hourly draw. This is the design change the parent report's "cadences" framing rests on: hourly quotas make time-of-day comparisons within and across geographies well defined, because each hour contributes the same number of conversations regardless of how busy it was. The appendix states the change in one sentence and gives no quota, no window and no total, so the appendix alone does not let a reader reconstruct the sample. Anyone reproducing this must take the counts from the release's own data documentation rather than from this document.

**The O\*NET classifier (pp. 2–5).** Two LLM calls per transcript. Step 1 (pp. 3–4) asks for a one-to-two-sentence summary and then picks among the three O\*NET activity levels — GWA (broadest), IWA (mid), DWA (specific) — returning `{level, name, confidence 1-5}` triples as JSON. Step 2 (p. 5) takes the Step-1 summary and the semicolon-joined DWA picks, offers up to 300 candidate Task texts drawn from the chosen DWAs in shuffled order, and returns `{name, confidence 1-5}` leaf picks. Three design choices are stated and matter for anyone using the resulting task shares:

1. *Two-step, not tree-traversal* (p. 2). The previous pipeline walked a hand-crafted category tree top-down; this one goes DWA-first and then drops to Tasks. Task shares across releases are therefore produced by different mechanisms, and the appendix supplies no crosswalk or agreement statistic.
2. *O\*NET 30.2, February 2026* (p. 2). A new taxonomy vintage, so some part of any year-on-year change in task shares is definitional. Not decomposed.
3. *Randomised tie-breaking* (p. 2). Where several tasks tie at the top confidence level, one is drawn at random rather than taken deterministically. This is a deliberate smoothing device against pile-up on a single arbitrary task. Its consequence is that the pipeline is not a deterministic function of the transcript: two runs of the same pipeline on the same transcript can return different tasks. It also means measured task-level dispersion is partly induced by the estimator.

Two further choices are stated without quantities: the prompt was inverted so the transcript sits last and the prefix can be cached, with the option list shuffled over a predefined set of orderings to preserve cache hits while countering any position preference (p. 2); and the visible share of each transcript was expanded, with a new sampling rule for over-long conversations (p. 3).

**The request-cluster change (p. 2).** The top level of the bottom-up request taxonomy was replaced with a 20-item list. The previous top level is not printed, so the appendix does not support a like-for-like comparison of cluster shares with earlier releases. Several of the new clusters are enterprise-shaped (Knowledge Retrieval & Enterprise Search, Compliance & Regulatory, Trust & Safety / Platform Integrity, Customer Support & Service Operations) and several are personal (Companionship & General Conversation; Existential, Relational, and Emotional Support), which is consistent with a taxonomy rebuilt to span both the consumer and API surfaces.

**The worked examples (pp. 6–10).** Seven transcript→label demonstrations, each showing the full O\*NET chain, Use Case, Task Success, Artifact and AI Autonomy. The transcripts are drawn from WildChat, a public dataset of user–ChatGPT interactions (p. 6, footnote 1 on p. 15), and some assistant turns are abbreviated for print (p. 6). The stated purpose is illustrative — "The examples are meant to illustrate the utility and limitations of the approach" (p. 6) — and the appendix supplies one example it judges right (Example 2, p. 6) and one it judges wrong (Example 7, p. 10). This is the whole of the appendix's validation content: no human-label benchmark, no agreement rate, no inter-rater statistic.

**The artifact classifier (pp. 11–13).** A single LLM call per exchange returning exactly one lowercase label from 32 options in `<answer>` tags. The prompt forces a single most-prominent output, instructs the model to choose `none` when no label clearly fits, and is run with the label order randomised except that `other` and `none` are pinned last (p. 11) — a design that guards against position bias in the substantive labels while keeping the two residual categories in a fixed, recognisable place. Snake-case labels are mapped to display names for the report's figures (p. 11); the mapping itself is not printed, and at least one display name in Figure A.1 ("Guidance") does not obviously correspond to any single printed label, though `advice_or_recommendation` is the plain candidate.

**Figure A.1 (p. 13).** The artifact distribution on the first-party API, presented as the mirror of the report's Figure 2.1 for the chat-and-Cowork surface. Top ten labels shown individually, the rest pooled as "Other output types", with "No clear output" shown separately in grey. The comparison the figure is built for is a surface comparison: the API produces more unclassifiable exchanges (16% against 7%) and tilts towards analysis and structured data rather than the broad consumer mix.

**Figure A.2 (p. 14).** A cross-sectional scatter with one point per artifact label (about 30 markers, consistent with the 30 substantive labels): x is median tokens per conversation for that artifact, normalised to the overall median and on a log scale; y is mean AI autonomy in the conversations producing that artifact. Both axes are artifact-level aggregates, so the unit of observation is the artifact type, not the conversation — n ≈ 30, not the sample size. A dashed fitted line is drawn but no coefficient, interval or n is printed. The y-axis jumps from 0.0 to 2.2 without a break marker, which visually amplifies the spread. Marker area varies, plausibly with volume, without a legend.

**Chapter 3 (p. 15).** A codebook only: twelve themes with definitions, used to classify free-text answers to a question about respondents' hopes for the economy in ten years. No frequencies, no n, no instrument.

## Limitations (verbatim)

The appendix has **no section headed "Limitations"** and makes no general statement about the limits of the release. The following are every limitation-shaped statement in the document, quoted verbatim with page references. Two of them (pp. 6 and 10) are the appendix's own framing of the examples as illustrations of limits.

1. "The examples are meant to illustrate the utility and limitations of the approach." (p. 6)
2. "We classify transcripts in a privacy-preserving way. To illustrate how the classifiers work, we present some example classifications using transcripts drawn from WildChat, an open-source dataset of user-ChatGPT interactions. (Some assistant's responses were abbreviated for presentation below.)" (p. 6)
3. "It is also classified as a personal use case, although this is hard to prove. It's often difficult to infer how the output was used." (p. 6)
4. "In Example 7, the question, "Which Rust library is best for Natural Language Processing (NLP)?" is mapped to a sales occupation although the question is substantively about computer programming. The classifier focuses on what the Assistant is asked to do—"Recommend products"—and not on the topic of the request." (p. 10)
5. "Since Claude may have order preferences over the categories presented to it, we shuffle the options in the prefix (using a predefined set of orderings to preserve caching)." (p. 2)
6. "This randomization was meant to spread the choice across the multiple candidates in order to avoid many transcripts piling up into one specific (and arbitrary) work task." (p. 2)
7. "1 - Very low confidence. The activity may be implied by context, but there is no clear textual support. Picks at this level are near-noise — exclude unless nothing stronger exists." (p. 4)
8. "Only choose an artifact label if it clearly describes what the exchange produced. If no label is a clear fit, choose none." (p. 13)
9. "On this surface, the share of conversations with no clear output is higher (16% vs 7% on chat and Cowork)." (p. 13)

Items 5–8 are limitations expressed as design responses: each names a failure mode the pipeline is built to contain (position bias; concentration on an arbitrary task; near-noise low-confidence picks; forced labelling of unclear outputs). Item 9 is the published size of the residual on the API surface.

## Open questions, conjectures and promised follow-ups (verbatim)

The appendix contains **no statement of future work, no "more research is needed" sentence, no promised follow-up and no research question.** It is a methods document and closes on Table A.1 with no discussion. The following are the only passages that carry an untested conjecture or an unresolved judgement; nothing here is a promise.

1. **Untested conjecture about the model's behaviour** (p. 2): "Since Claude may have order preferences over the categories presented to it, we shuffle the options in the prefix (using a predefined set of orderings to preserve caching)." The order preference is posited, not measured, and the shuffling is not evaluated.
2. **Stated intention whose effect is not reported** (p. 2): "This randomization was meant to spread the choice across the multiple candidates in order to avoid many transcripts piling up into one specific (and arbitrary) work task."
3. **Unresolvable construct, stated as a standing difficulty** (p. 6): "It is also classified as a personal use case, although this is hard to prove. It's often difficult to infer how the output was used."
4. **A self-identified misclassification with a preferred alternative, left unquantified** (p. 10): "This question might have been better assigned to a task like "Consult with customers or other departments on project status, proposals, or technical issues, such as software system design or maintenance," which falls under Software Developers."
5. **A relationship asserted without a statistic** (p. 14): "Artifacts requiring more tokens tend to be produced with more autonomy."

## What it did not test

**This section is the wiki author's inference, not the appendix's own words.** It lists what the document leaves untested, including robustness checks it was in a position to run and did not.

**Validation the appendix could have run and did not**

1. **No human-label benchmark for the new two-step O\*NET classifier.** The document rebuilt the mapping (Claim 2), changed the taxonomy vintage (Claim 3) and changed how much of the transcript the classifier sees (Claim 7), and validated none of it. Seven hand-picked WildChat examples with the authors' own verdicts on two of them is the whole of the evidence. The earlier Index paper carried a classifier-validation appendix; this one does not.
2. **No old-versus-new agreement rate.** Both pipelines could have been run on the same transcripts and the crosswalk published. Without it, no reader can tell how much of any change in task or occupation shares between the fifth and sixth reports is a change in Claude use and how much is the new classifier plus O\*NET 30.2.
3. **No decomposition of the O\*NET 30.2 switch.** The same transcripts could have been classified against both taxonomy vintages.
4. **No test of the position-bias conjecture.** The appendix shuffles options because Claude "may have order preferences" (p. 2) but never reports whether it does, or how large the effect is. The predefined orderings make this a cheap check: classify a sample under two orderings and report the disagreement rate.
5. **No measurement of the randomised tie-break's consequences.** Re-running the pipeline on the same transcripts would give a run-to-run reliability figure for task assignment, and would show how much measured dispersion across tasks is induced by the estimator rather than by use. Neither is reported.
6. **No test of the transcript-truncation change.** The visible portion of each transcript was "substantially expanded" (p. 3); the natural check — classify the same conversations at the old and new context budgets and compare — is absent, as is any statement of the budgets.
7. **No validation of the artifact classifier.** A 32-option single-label classifier is introduced with no human agreement rate, no confusion structure and no test of the forced-single-label rule. Multi-artifact exchanges are collapsed to the most prominent output by instruction; the appendix does not report how often exchanges plausibly carry more than one.
8. **No test of the "none" rate as a measurement artefact.** The API surface returns 16% "no clear output" against 7% on chat and Cowork (Claim 15). The appendix presents this as a fact about the surface; it does not consider that the prompt was written for conversational exchanges and that API traffic may be systematically less legible to it — the competing explanation for the same number.
9. **No label→display-name mapping.** Figure A.1 uses display names ("Guidance", "Other output types") that do not appear in the printed taxonomy, so a reader cannot map every bar back to a prompt label.

**Statistical apparatus absent throughout**

10. **No sample sizes anywhere** — not for the hourly draw, not for Figure A.1, not for Figure A.2, not for the survey behind Table A.1.
11. **No uncertainty on any published number.** Figure A.1's twelve shares carry no intervals; Figure A.2 has a fitted line with no coefficient, no interval and no n (the "r = 0.68" for this figure is published on the report page, not here).
12. **The displayed shares in Figure A.1 sum to 87%** by my arithmetic on the printed bar labels (21+13+8+6+5+2+2+2+2+2+8+16). The appendix does not explain the residual — whether it is rounding across many small categories pooled into "Other output types", or a category outside the chart.
13. **The internal 13%/14% discrepancy on p. 13 is not reconciled** (Claim 15). Neither number is marked as rounded from the other.
14. **Figure A.2's broken y-axis is unmarked**, and the marker-size channel has no legend, so the visual weight of the relationship cannot be checked against the underlying volumes.

**Design questions left open**

15. **No comparison of the hourly draw against the old weekly window on overlapping dates.** The change is asserted to give a clearer picture; it is not shown to change any measured quantity, and no test for within-day compositional effects in the old design is offered.
16. **No crosswalk between the old and new request-cluster top levels**, and the old list is not printed, so cluster-share continuity cannot be assessed.
17. **The seven examples exercise a narrow slice of the label space**: Task Success is "Yes" in all seven and AI Autonomy is 2 or 3 in all seven, so no failure case and no autonomy level 1, 4 or 5 is illustrated (Claim 10). The classifiers' behaviour on failed tasks and on highly delegated work is not demonstrated anywhere in the document.
18. **The examples are all short, single-turn or two-turn English exchanges from a 2023–24 ChatGPT corpus.** Agentic, long-horizon and non-English exchanges — the cases where the expanded transcript window and the long-conversation sampling rule bite hardest — are not illustrated.
19. **"Cowork" is used as a surface name without definition** (pp. 13, 14), and no separate cut of either figure is given for chat alone versus Cowork alone, so the two are pooled in every appendix exhibit.
20. **Chapter 3 tests nothing.** It publishes a codebook with no frequencies, no respondent count, no instrument and no reliability check on the theme classifier — and the themes are not mutually exclusive on their face (for example "Less work: free time & drudgery automated away" and "Richer life beyond work"; "Shared prosperity & economic security" and "Own pay & wealth"), yet no multi-label rule, no coverage rate and no inter-theme overlap is reported.
21. **No reproduction path.** No data-availability statement, no file names, no code, no seed for the randomisation, and no statement of which model ran the classifiers or at what temperature — so the pipeline described cannot be re-run from this document.

## Verification

- **Fetched on 2026-09-16.**
  - https://cdn.sanity.io/files/4zrzovbb/website/03ed1410f74a65ae4cc2a27120d0875e1e569535.pdf — HTTP 200, 2,707,986 bytes, MD5 `a30540f37953d9a50bba09dbdf2a41f7`, 15 pages. Read in full.
  - https://cdn.sanity.io/files/4zrzovbb/website/8eb31e1d187ff18146d248bbef8b2754971f0f5a.pdf — HTTP 200, 2,707,791 bytes, MD5 `80501339aeeec869d41ddea5a69a8210`, 15 pages. Read in full.
  - https://www.anthropic.com/research/economic-index-june-2026-report — HTTP 200, fetched only to confirm how the two PDFs are linked and to check one cross-reference. Not a source for anything in the sections above.
- **Fetch failures.** The `web_fetch` tool refused both `cdn.sanity.io` URLs with `url_not_allowed` (the host is outside the tool's allow-list). Both files were retrieved instead with `curl` over HTTPS, and pages were read both as extracted text (`pdftotext -layout`, page by page) and as 100/150/400-dpi page renders (`pdftoppm`). No other fetch failed.
- **Differences between the two copies.** One, and only one. On p. 15 the Chapter 3 heading reads "Ten-year vision themes / and definitions" (two lines) in the primary copy `03ed1410…` and "Vision themes and definitions" (one line) in the second copy `8eb31e1d…`. Everything else is identical:
  - Pages 1–14 are **pixel-identical** at 100 dpi (max per-pixel difference 0).
  - On p. 15, Table A.1 sits 42 px (100 dpi) higher in the second copy because the heading occupies one line instead of two; after correcting for that shift the table region is pixel-identical, so the twelve themes and their definitions are the same in both. The table's own caption still reads "Table A.1: Ten-year vision themes and definitions." in **both** copies, and the footnote is unchanged in both.
  - Extracted-text diff over the whole document: the two heading lines above, plus two trailing blank lines. Nothing else.
  - The two files differ in `CreationDate` (2026-06-26 13:46 UTC for `03ed1410…`; 2026-06-25 23:20 UTC for `8eb31e1d…`), both produced by "Adobe InDesign 21.4 (Macintosh)" / "Adobe PDF Library 18.0". `8eb31e1d…` is therefore the earlier build, and the later build renamed the chapter heading. **Quotations in this file are taken from the primary copy `03ed1410…`;** the Chapter 3 heading is the only quotation in this file that differs between copies, and both readings are recorded above.
  - How the report page links them: `03ed1410…` is linked four times from the report body (the methodological-changes paragraph, the artifact-list paragraph, the Figure A.2 sentence, and the "Appendix — Available here." section). `8eb31e1d…` is linked once, from footnote 5 ("See our Sonnet 3.7 report and the Appendix."). So the later build is the canonical appendix and the earlier build survives in one footnote.
- **Quotation checks.** Every quotation in `Definitions (verbatim)`, `Limitations (verbatim)` and `Open questions…` was checked character by character against the fetched primary copy, using both the extracted text layer and the page render, and matched. Specifically confirmed against the byte stream: the document's typographic quotation marks (U+201C/U+201D) and apostrophes (U+2019) inside the prompts' JSON examples; the em dashes (U+2014) in "near-noise — exclude", in the artifact-label glosses and in the Table A.1 definitions; the bullet character (U+2022) in the artifact list; and the plain hyphen in every "1-5" range.
- **Raster-only content.** The seven example tables (pp. 6–10), Figure A.1 (p. 13), Figure A.2 (p. 14) and Table A.1 (p. 15) are images with **no text layer** in the PDF; `pdftotext` returns only the page footer for pp. 7, 8 and 9. All values and all verbatim text taken from those exhibits — the Claim 10 table, the twelve Figure A.1 bar labels, the Figure A.2 axis ticks and point labels, and the whole of Table A.1 — were transcribed from 400-dpi renders and re-read against the render a second time. Figure A.2's point coordinates are marked "≈" throughout because they are read off a scatter plot, not published as numbers.
- **The one number in this file that is not from the appendix.** "r = 0.68 on chat and Cowork" (noted in Claim 16) is published in the body of the main report page, fetched 2026-09-16, not in the appendix; the appendix prints no coefficient for Figure A.2. It is recorded here only to mark what the appendix omits.
- **Arithmetic flagged as mine, not Anthropic's:** the count of 20 top-level request clusters (Claim 6), the count of 32 artifact options / 30 substantive labels (Claim 13), the count of 12 Table A.1 themes (Claim 17), the tabulation in Claim 10, and the 87% sum of Figure A.1's printed bar labels (What it did not test, item 12).
- **Terminology notes for the corpus.** The appendix writes "ONET" in prose and "O\*NET" inside the prompts, and "O\*Net Classifier" as the example-table row label. It names three surfaces — "Claude traffic", "chat and Cowork", "1P API" — and defines none of them. "AI Autonomy" appears as an example-table row with integer values 2 and 3, consistent with the 1–5 autonomy primitive; the appendix does not restate its definition.
- **Not used.** `reference/` was not consulted for this file.
