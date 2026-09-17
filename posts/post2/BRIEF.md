# post2 · When a task takes a larger share of AI use on the enterprise API, does it take a smaller share on the consumer app?

*Candidate LL-11. Brief of record on `team/templates/BRIEF.md`. The question and title above are frozen: the question says
AI (criterion 6; correction 20), and "grow"/"shrink" are gone because the design measures shares, not levels
(`room/editor-2026-09-16-sketch-LL-11.md`). Findings will say Claude.ai and the 1P API. Amended once on the steward's
feasibility note (`posts/post2/notes/feasibility.md`, corrected at `a452d01`); rewritten once on the referee's BLOCK
(`posts/post2/notes/referee-brief.md`) — blocking items 1–4, should items 5–10 and 12, and the director's ruling on item 11
(§4, §8). The question and the hypotheses' subject matter are unchanged.*

## 1. The question

When an O\*NET task takes a larger share of AI use on the enterprise-facing first-party API, does it take a smaller share of
AI use on the consumer-facing app?

## 2. Why it matters, and to whom

A published, dated claim says work is moving between the two surfaces on which Anthropic measures AI use: "Coding tasks
continue to migrate from augmentative usage in Claude.ai to more automated workflows in our first-party API traffic"
(`economic-index-2026-03-report`, p.7, 24 March 2026). The economic content of that sentence is a flow: work leaving a
surface where a person is in the loop for one where a service calls the model without one is the same work done under a
different division of labour. The report says so: "As tasks migrate to the API, they may become more exposed to automation.
API workflows are far more likely to be directive, with less need for a human in the loop" (ibid., p.9), and "we expect that
this migration from Claude.ai to the API may signal more imminent transformation of work for the associated jobs" (ibid.,
p.7).

The claim is used outside its own chapter. Anthropic's displacement measure raises an occupation's exposure when "It has a
relatively higher share of automated use patterns or API implementation" (`labor-market-impacts-2026-03`, PDF p.5), and the
second-ranked occupation on that measure is ranked there because of the surface its tasks appear on: "Customer Service
Representatives, whose main tasks we increasingly see in first-party API traffic" (ibid., pp.7–8, Figure 3). Anyone quoting
the migration — a policy analyst reading the exposure ranking, an economist asking whether a reallocation of work between
two surfaces can be seen at all — is relying on a correspondence that has never been measured as a correspondence.

The public releases can say something no other source can: they publish the same task taxonomy on both surfaces in the same
week, three times. No other provider publishes both, and Anthropic's reports set the two side by side without relating them
task by task. The answer also tells Anthropic what to publish: the Institute's only concrete data commitment is "More
granular information from The Anthropic Economic Index, at a higher cadence" (`institute-agenda-2026-05`, *Share 1*), and a
negative result here names the missing field.

## 3. The thread of Anthropic's inquiry this builds on

Thread **T3** (automation, augmentation, delegation), with **T1** (adoption and diffusion). `programme/THREADS.md` records
the migration as the mentor's stated mechanism for imminent labour-market change (T3 (e)) and records as open that "The 1P
API's falling automation is not decomposed into behaviour and Claude Code's call-splitting" (T3 (c)). Three ledger items are
the gap, all **open**: `L-2026-03-R5-17`, the p.9 conjecture quoted verbatim in §2 ("As tasks migrate to the API, they may
become more exposed to automation…"), asserted and never measured, and not measurable as a *series* past 2026-03-24 (§8);
`L-2026-03-R5-18`, the p.7 conjecture also quoted there ("we expect that this migration… may signal more imminent
transformation of work"); and `L-2026-01-R4-23`, the promised follow-up "In future work, we could leverage our 1P API data
to understand which of these tasks are being integrated into production workflows" (`economic-index-2026-01-report`, p.45),
restated as a migration story in `economic-index-2026-03-report` p.7 without that analysis.

What the thread has established: both surfaces' task and collaboration series, wave by wave, and the direction of each.
Coding's share on Claude.ai fell "from a peak of 40% in March 2025 to 34% in November 2025" while on the API it "edged
higher from 44% in August to 46% in November 2025" (`economic-index-2026-01-report`, p.7 — both on the 2010 O\*NET-SOC
vintage and the all-conversation base). Anthropic also states its own mechanism for part of the API movement: "Claude Code's
agentic architecture splits coding work into smaller API calls, which are labeled as distinct tasks. So while coding's
overall share of API traffic has grown, it is spread across many task categories rather than concentrated in a few" (ibid.,
p.6); it glosses the word "migration" itself in the same composition language, quoted in §6. Where it is open: nothing in
the corpus relates a task's movement on one surface to the same task's movement on the other.

## 4. Overlap, stated

**What Anthropic has shown.** Two independently moving share series, one per surface, with a category-level relative change
stated for coding: "Since August 2025, the share of tasks in this category has increased by 14% in the API and decreased by
18% in Claude.ai" (`economic-index-2026-03-report`, p.7 — 2019 O\*NET-SOC vintage, classified base, §8), plus the mechanism
at p.6 and the labour-market reading at p.9. What is new here: the task-level correspondence between the two surfaces'
*changes* — whether the tasks that gain share on one lose it on the other — which is the statistic the word "migration"
asserts and no publication reports.

**What others have shown.** Chatterji et al. describe a consumer chatbot at scale and by construction exclude the other side
of this margin; Dillon, Jaffe, Immorlica and Stanton find no shift in the composition of workers' tasks from individual AI
provision, inside firms rather than across surfaces (both quoted with their sample restrictions in §11). What is new here: a
task-level measure of correspondence between a consumer and an enterprise surface of one model, on one task taxonomy.

**Separation from the two short-list partners** (`programme/SHORTLIST.md` §5; the director's pairs ruling). Against **post3
(LL-36)**: this post headlines the cross-surface correspondence of task-share changes and **does not** headline coding's
share of use as its key number; post3 headlines composition inside coding and, the shipped-versus-recoded O\*NET-SOC vintage
discrepancy being a coding-share number, **states that discrepancy as its first result** (director's ruling on item 11)
while citing this post for the correspondence frame. This post reproduces the same number inside its measurement section,
cites post3's statement of it, and does not open on it (§8). Against **post4 (LL-09)**: the two share one input series, the
November→February change in a task's Claude.ai share, and therefore the same February exposure; post4 headlines the relation
between Claude's measured success rate and subsequent use, this post the cross-surface correlation. Both name the shared
November→February Claude.ai series and the Super Bowl exposure — here in §7, item 3.

## 5. Contribution

If a task's share changes are negatively related across the two surfaces, the post publishes the first measure of the
cross-surface correspondence the migration sentence asserts, names the tasks that carry it, and states which two readings —
work moving between the surfaces, or two anti-aligned inflows arriving on them — these files cannot separate; if the changes
are unrelated, the post shows that each surface's task mix moved with no task-level correspondence to the other, so the
migration sentence describes two series measured in the same week rather than work passing between them, and the reading
Anthropic attaches to it — that migrating tasks become more exposed to automation — has no measured flow behind it.

## 6. Hypotheses

**H1 · Negative correspondence.** A task's change in Claude.ai share and its change in API share are negatively related
across the 1,241 tasks published on both surfaces in all three waves. **Two readings are consistent with that correspondence
and six aggregate cross-sections cannot separate them:** work moving between the surfaces, and two anti-aligned inflows
arriving on them — casual consumers on Claude.ai, agentic coding on the API — the second being Anthropic's own gloss on its
own word: "This decline in concentration partly reflects coding tasks migrating from Claude.ai to our first-party API, where
Claude Code has grown to represent a large share of sampled traffic" (`economic-index-2026-03-report`, p.6). H1 is therefore
a claim about correspondence and not about a flow, and the post says so wherever it states the result. *Signature that
separates it from H2, H3 and H4:* the negative estimate appears in **both** adjacent windows (August→November 2025, November
2025→February 2026), survives removal of the coding block with the remaining shares renormalised within each surface, and is
present among non-coding tasks. *What would count against it:* either window's estimate not distinguishable from zero
at the stated power; the two windows disagreeing in sign; or the estimate confined to the coding set or to the
November→February window.

**H2 · No task-level correspondence.** Each surface's task mix moves — "the top 10 most common O\*NET tasks went from 24% of
conversations to just 19%" on Claude.ai against an API top-ten share of 28% → 32% → 33% (ibid., p.5, Fig. 1.1) — while the
tasks that gain share on one surface are not the tasks that lose share on the other. *Signature:* estimates inside the
interval around zero in both adjacent windows and on the long August→February change, excluding the smallest effect of
interest, while each surface's own mix changes measurably. *What would count against it:* estimates beyond that interval in
both windows, or a negative long-change estimate with both adjacent windows negative. *The smallest effect of interest is
fixed before the pre-registration is filed:* the correlation the panel would show if the whole reproduced SOC-15 movement
(§8) were a flow and nothing else moved, computed from the reproduction leg alone and written into the pre-registration
before any cross-surface estimate is read (referee item 5).

**H3 · Denominator movement, on either surface or both.** The negative correspondence is produced by composition shocks to
the two denominators rather than by any task changing surface. Both shocks are Anthropic's own: first-time users arriving on
Claude.ai in February ("increasing signups beginning around February brought more casual AI users", ibid., p.6; "Our
sampling period overlapped with the release of our Super Bowl advertisements, which brought many first-time users", ch. 2
endnote 3, p.18), and agentic coding growing as a share of sampled API records (p.6, quoted in H1). Every task's share falls
when a population arrives with a different mix, and two such arrivals with anti-aligned mixes give a negative correspondence
with nothing moving between surfaces. *Signature:* the estimate weakens materially towards zero when the November→February
window is dropped, or when the coding block is removed and the remaining shares renormalised, or both. *What would count
against it:* negative estimates of similar size in August→November and after coding-block removal with renormalisation.

**H4 · Coding-carried.** The API's coding-task shares rise because agentic coding is labelled as many tasks, which dilutes
non-coding API shares arithmetically, while Claude.ai's coding share falls for user-mix reasons. Anthropic states the first
half itself (p.6, quoted in §3); no public file identifies Claude Code records, so a result here can be **consistent with**
that mechanism and cannot show it. *Signature:* the negative estimate is carried by the 2019-vintage SOC-15 set and is
absent in the pre-specified non-coding complement. *What would count against it:* a negative estimate of similar magnitude
in the non-coding complement.

## 7. Assumptions sweep

**(1) Value judgement in the framing — handled, with a change made here.** "Migration" and "exposure" carry a direction of
travel and a loss; "grow" and "shrink" claim levels the design cannot see; "leading indicator" claims a timing relation
nothing in this design tests, and it is gone from §2 and §5 (referee item 1). The change: the question and title are in
share language and name no winner (§1); the words "exposed", "at risk" and "transformation" appear in the post only inside
quotation marks from Anthropic; and the post states that a share moving is not a volume moving. Anthropic's own construct is
a share of sampled records, not a count of work: "Share of conversations assigned to the 10 most prevalent O\*NET tasks, by
platform and report version" (`economic-index-2026-03-report`, Fig. 1.1, p.5).

**(2) Construct mapping — needs a design change, and the change is specified.** The two surfaces' shares do not share a
unit. Anthropic's verbatim definition: "we analyze a random sample of 1M conversations from Claude.ai Free, Pro and Max
conversations (we also refer to this as 'consumer data' since it mostly represents consumer use) and 1M transcripts from our
first-party (1P) API traffic (we also refer to this as 'enterprise data' since it mostly represents enterprise use)… For 1P
API data, each record is a prompt-response pair from our sample period which in some instances is mid-session for multi-turn
interactions" (`economic-index-2026-01-report`, fn 1, p.17). The classifiers are not identical across surfaces — the API
collaboration prompt carries "IMPORTANT: These interactions are happening via an LLM API, not an actual human-AI assistant
conversation… when we say 'human', we mean 'end user'" (ibid., online appendix, p.19, §2.3.4) — nor across waves: the
classifier model changed (Sonnet 4 to Sonnet 4.5), with the caution that "different models can generate different
classification outcomes, though these effects tend to be modest" (ibid., fn 7, p.18). Relabelling hits both surfaces alike,
which enters a correlation of changes with a **positive** sign and would mask a negative one, so the post states that bias
beside the estimate (referee item 8). **The change:** no statistic compares a level or a share *across* surfaces; every
estimate is a correlation of *within-surface changes*, each on its own denominator; and the measurement paragraph states
that a share of prompt–response pairs is not a share of conversations, that Anthropic's labels are hedged ("mostly
represents consumer use", "mostly represents enterprise use"), and that every finding names Claude.ai and the 1P API rather
than the consumer and the enterprise economies (referee item 10). For the reproduction leg the occupational label is a task
label: "Occupation is inferred from the task, not the user" (`data/ATLAS.md` §Traps 36), said beside the reproduced number,
where a generic system-administration statement filed under Bioinformatics Technicians shows how loosely the labels fit
(§8).

**(3) Composition and selection — newly flagged; the changes are the window split and the widened denominator test.** The
February 2026 Claude.ai window carries an inflow of new users (p.6 and ch. 2 endnote 3, p.18, quoted in §6 H3). A second
composition shock sits in the same window and Anthropic quantifies it: "Coursework fell from 19% to 12% of conversations"
(p.6), of which "The drop in coursework conversations was 5 percentage points in countries where the school term was active
and 12 percentage points in the countries where most students were on break" (ch. 1 endnote 3, p.11) — so part of the
February consumer mix is students absent rather than work relocating (referee item 7a). Both shocks move the Claude.ai
denominator for every task at once, so a task's share can fall with nothing leaving it. The API population moves too, with
an opposite mix: its sample "includes data from Claude Code" (ibid., fn 1, p.11), which "has grown to represent a large
share of sampled traffic" (p.6). **The change:** H3 covers **both** denominators rather than the consumer one alone; the two
windows are estimated and reported separately and never pooled into the headline; the November→February estimate names both
inflows in the same sentence; the coding-block-removed, renormalised estimate is reported beside every headline estimate;
and the coding / non-coding split is pre-specified rather than chosen after the fact.

**(4) Anthropic's own results that cut against or bound the framing — three handled, two newly flagged.** Handled. First,
Anthropic's own mechanism makes part of the predicted pattern arithmetic rather than behavioural (call-splitting, p.6,
quoted in §3) — carried as rival **H4** with its own signature, not as a closing caveat. Second, the Claude.ai coding
decline predates the API series: "down from a peak of 40% in March 2025 to 34% in November 2025" against the API's "44% in
August to 46% in November 2025" (`economic-index-2026-01-report`, p.7 — both 2010 vintage, all-conversation base), while the
numbers this post reproduces ("35%", "+14% / −18%") are 2019 vintage on the classified base; the API series begins only in
August 2025 (`economic-index-2026-03-report`, Fig. 1.1, p.5), so no part of the fall before that can be read as a
correspondence, and every quoted number carries its vintage and base wherever the post quotes it (referee item 9). Third,
the task universe is nearly closed between these waves — "Our data from this report showed many fewer novel O\*NET tasks
than in our previous report" (ibid., p.7) — which supports a matched panel but also means entry and exit cannot carry the
result; the panel's mass coverage is reported beside every estimate on the base §8 names. Newly flagged. Fourth, Anthropic's
gloss on its own word is a composition statement (p.6, quoted in §6 H1), which is why H1 claims correspondence and not a
flow. Fifth, the surface tasks are said to migrate *to* became **less** automated across these same windows — "we show that
automation decreased sharply in the 1P API data" (p.7, evidenced in Appendix Figure A.3), with API `directive` running 66.30
→ 63.58 → 58.22 (`data/ATLAS.md` §Components) — which cuts against the conjecture that arriving on the API is arriving where
no human is in the loop, and is reported beside the exploratory directive test (§9; referee item 7b).

## 8. Data, confirmed at column level

**The data steward's feasibility line, verbatim** (`programme/LONGLIST.md`, LL-11, quoting
`room/steward-2026-09-16-longlist-feasibility-batch-1-answers.md`), caveat included:

> "**LL-11. FEASIBLE.** Global `onet_task_pct` exists for both surfaces in all three pre-June waves:
> named nodes 2,616 / 3,168 / 3,258 (Claude.ai) and 2,054 / 2,251 / 2,297 (API); pairwise overlap
> 1,603 / 1,823 / 1,908; **1,241 tasks appear in all six frames**, carrying **80.9%** of Claude.ai and
> **83.2%** of API Feb-2026 named mass. Shares only, and never past 2026-03-24, as your entry says.
> Log (e) 10."

The steward's confirming note is **`posts/post2/notes/feasibility.md`** (verdict **FEASIBLE WITH CAVEAT**, corrected at
`a452d01`): every cut below confirmed with a command, its amendments applied here and marked *(steward)*, all named against
`data/ATLAS.md`.

| # | release (window) | file | geography | facet · level | variable | threshold / base |
|---|---|---|---|---|---|---|
| 1–3 | `release_2025_09_15` (4–11 Aug 2025), `release_2026_01_15` (13–20 Nov 2025), `release_2026_03_24` (5–12 Feb 2026) | Claude.ai long file | `geography == global` | `onet_task` · L0 | `onet_task_pct`, `onet_task_count` | privacy floor count ≥ 15, applied upstream; count bases 964,494 / 999,875 / 1,000,000, February per million (§Other bases) |
| 4–6 | the same three releases | 1P API file (global only, §Components) | `global` | `onet_task` · L0 | `onet_task_pct`, `onet_task_count` | same floor; count bases 944,638 / 971,525 / 1,000,000 *(steward)* |
| 7 | `release_2025_09_15` reference | `data/intermediate/onet_task_statements.csv` (O\*NET DB 20.1, 19,530 × 9) | — | — | task text → O\*NET-SOC **2010** code | join key the lower-cased, stripped task text; 0 unmatched named tasks in all six frames (§Taxonomies) |
| 8 | external *(steward)* | O\*NET-SOC 2010 → 2019 crosswalk, O\*NET Resource Center (`data/fetch/supplementary_onet.py`) | — | — | 2010 code → 2019 code(s) | 1,164 rows; 0 unmatched 2010 codes; O\*NET data under CC BY 4.0, attribution to the O\*NET program required |

**Panel, exclusions and conventions.** `none` and `not_classified` are dropped — different things, both must go (§Traps 24)
— and the API residual is two to three times the consumer one (`not_classified` 6.02 against 2.74 in February), 3.4 times it
in August (8.11 against 2.41, referee item 12b): one more reason no level is compared across surfaces. The panel is the
**1,241** tasks published on both surfaces in all three waves; absent is not zero, so a task missing from any frame is
excluded rather than set to zero (§Traps 25). **Panel mass, base now stated** *(steward)*: 80.89% of Claude.ai and 83.22% of
API February **geography total** (which includes `none` and `not_classified`), being **87.01%** and **92.18%** of *named*
mass; the quoted line says "named mass", the geography-total reading is the right one for those two figures, and the post
reports both. `{facet}_pct` is a share of the geography total (§Other bases), so primary estimates use `onet_task_pct`
unrenormalised, with a panel renormalisation as a stated sensitivity; reads use `keep_default_na=False` and `na_values=[]`
on 2026-03-24 and cast `level` to string after any parquet read (§Traps 1, 2, 6, 7); case-variant duplicates are zero inside
the Index *(steward)*, so de-duplication bites only on the statements side of the join. **The series stops at 2026-03-24**:
across the next boundary the API `directive` share jumps 58.22 → 80.88 where the documentation stops including Claude Code
(§Components), so June is not used at all.

**Levels, and what the files cannot identify** *(steward, amendment i)*. Shares carry every estimate. `onet_task_count`
exists at global on **both** surfaces in all three waves (2,056 / 2,253 / 2,299 API rows, minimum 15), so the H3 level
diagnostic runs on both surfaces rather than one: §Cuts 18 rules out the geography-total `usage_count`, not facet counts.
Two conditions travel with it — the counts are of *sampled* records on bases differing by wave and surface (within 5.9%),
and an API record is a prompt–response pair, not a conversation (§7(2)) — and it is a diagnostic, never an outcome. Neither
inflow is observable: no user, account, plan, tenure, signup-date or within-window date field exists in any wave (§Cuts 26,
27b) and no file marks a record as Claude Code traffic (§Components), so both are stated as Anthropic states them (§6 H3)
and tested only through the window contrast and the coding-block cut (§9 test 3), never adjusted for.

**Supplementary data** *(steward, amendment ii — the brief's "None" was wrong)*. One external input, required by the
reproduction leg and H4's coding set and nothing else: the **O\*NET-SOC 2010 → 2019 crosswalk** from the O\*NET Resource
Center (cut 8), fetched and checksummed at `data/fetch/supplementary_onet.py`. *Join key:* `O*NET-SOC 2010 Code` against the
statements file's `O*NET-SOC Code`. *Coverage:* 19,530 (task key, 2010 code) pairs in → 20,081 rows out; 0 unmatched 2010
codes; 18,428 of 18,428 task keys carrying a 2019 code; every named task in all six frames mapping. *Why it is needed:* the
released files ship only the 2010 taxonomy and the number this post reproduces is on the 2019 one, by the report's own
footnote. A later O\*NET database is **not** a substitute — joining the Index task text to O\*NET 27.3 statements drops
17–28% of each frame's named mass, the statements having been reworded, and returns +12.58% *(steward, §3)*.

**The published number this reproduces, and where it sits** (criterion 3; referee correction 4). Inside the measurement
section, before any cross-surface estimate and not as the post's opening claim (director's ruling on item 11): "Since August
2025, the share of tasks in this category has increased by 14% in the API and decreased by 18% in Claude.ai"
(`economic-index-2026-03-report`, p.7), "this category" being Computer and Mathematical, evidenced in the appendix figure
"Task usage share trends by occupation group (V1-V5, 2019 O\*NET-SOC)" (`economic-index-2026-03-appendix`, p.5), the vintage
named in the report's footnote: "This number uses 2019 O\*NET-SOC codes, while previous reports use the 2010 vintage"
(ibid., fn 2, p.11). **The specification** *(steward, amendment v; feasibility note §2,
`data/replication/soc15_figA1_2026_03.py`)*: global `onet_task` L0 `onet_task_pct` per surface per wave (cuts 1–6); drop
`none` and `not_classified`; join the lower-cased, stripped task text to the shipped O\*NET 20.1 statements for 2010 codes
(cut 7); recode each 2010 code to its 2019 code(s) (cut 8); **deduplicate the allocation unit on (task key, 2019 code)**
before splitting — 18 duplicate-source rows, and keeping them returns 61.7795 rather than 61.6363 on the February API
*(steward, `a452d01`)*; split a task's `pct` equally across its distinct 2019 codes, the `pct_occ_scaled` rule
(§Conventions); renormalise over matched named mass — the **classified** base. So specified, the API runs 53.8833 → 59.2074
→ 61.6363 (**+14.3885%** August to February) and Claude.ai 41.9682 → 38.5001 → 34.6150 (**−17.5208%**, February being the
published 35% of Claude.ai conversations). The task → SOC join and the multi-holder rule are **stated in post1 (LL-07)** and
cited rather than re-derived, its vintage rule included (`posts/post1/BRIEF.md` §8: a grouping set beside a published
occupational number is reported on the 2019 recode as primary, the 2010 grouping beside it).

**The shipped-versus-recoded discrepancy, pre-registered now.** The published claim is not reproducible from the public
files alone: on the shipped 2010 taxonomy the same specification gives **+3.2433%** on the API against **−17.4248%** on
Claude.ai, so the consumer leg reproduces on either vintage and the enterprise leg only after the recode. **post3 (LL-36)
states that discrepancy as its first result**, it being a coding-share number (director's ruling on the referee's item 11);
this post reports both specifications side by side inside this measurement section, cites post3's statement of it, and opens
on neither. The cause, on one named base, the classified one: 337 of 20,081 (task, code) pairs change major group — 34 pairs
into SOC 15 and 36 out of it, the out-leg (15-1199.10 → 13-1161.01, 0.3912 in February) an order of magnitude smaller — and
the SOC 43 → SOC 15 move carries **10.3190 of February API classified mass** (9.3168 points of the geography total), of
which **43-9111.01 Bioinformatics Technicians → 15-2099.01 Bioinformatics Technicians carries 9.7110** and 43-9011.00
Computer Operators → 15-1299.00 Computer Occupations, All Other carries **0.6081**. The 43-9011 attribution in this brief's
first version is **wrong** (referee item 2; steward correction, `room/steward-2026-09-16-recode-correction-applied.md`). The
largest single task in that move ("perform routine system administrative functions such as troubleshooting, back-ups, and
upgrades.", which the shipped statements file holds under Bioinformatics Technicians and no other code) runs 1.2396 → 3.9479
→ 6.7260 on the API against 1.6426 → 1.2693 → 1.4451 on Claude.ai; **remove it and the 2019-vintage API leg is still
+10.0054%** (53.2231 → 58.5483), so that task is about a third of the relative change and the taxonomy revision is the rest.
Its growth on one surface and not the other is **consistent with** H4's call-splitting mechanism and does not show it: no
public file identifies Claude Code records (§Components), and a generic system-administration statement is not agentic
coding by inspection. Two things are fixed in advance: no confirmatory test in §9 depends on the published relative change;
and the coding set's vintage is pre-specified here rather than chosen later.

**H4's coding set, vintage and assignment rule** *(steward, amendment iv; referee item 12a)*. The coding set for H4 and §9
test 4 is SOC major group 15 **on the 2019 vintage**, matching the reproduced number, with the 2010-vintage set as the
robustness cut and the non-coding control its complement under the same vintage. A task held by occupations in more than one
major group goes to the group carrying the largest share of its equal-split mass — modal holder by weight, the rule that
reproduces 242 / 242 / 228 in the referee's re-derivation — an exact tie resolving to the lower major-group number, with the
number of ties printed in the pre-registration. The choice is not cosmetic: the two sets each hold 242 panel tasks but
overlap in only 228, in February the 2019 set carries 55.29 of the API's 83.22 panel mass against 46.31 for the 2010 set
(31.61 against 29.42 on Claude.ai), and the system-administration task above is in the set on one vintage only.

**Effective N and power** *(steward, §4)*. N = 1,241 on the fixed six-frame panel, minimum detectable |r| **0.0795** at 5%
two-sided and 80% power. Window-specific panels are 1,317 (August→November, MDE 0.0771) and 1,595 (November→February, MDE
0.0701); the fixed panel stays primary because it holds the sample constant, the wider ones being a robustness cut (§10). On
the same formula the coding set's N = 242 gives an MDE of about **0.18** (referee item 6) and its non-coding complement's N
= 999 about **0.089**; both are the lead's arithmetic on the steward's formula and are confirmed with him at the
pre-registration. The exploratory directive test rests on `onet_task::collaboration` at global on the API, published for
1,143 / 1,155 / 1,135 panel tasks; the missing cells are suppressed, not zero, and the intersection `_pct` is a share of its
base cluster (§Other bases) — both stated with the coverage.

## 9. Confirmatory tests and the exploratory allowance

**The primary metric, named** (referee item 6). A task's change is the **percentage-point** difference of two published
`onet_task_pct` values on the same surface, and the primary estimate is the Pearson correlation of those changes across
tasks. The log ratio is not primary: it is dominated by the near-floor tasks (14–65 per frame, §10), the noisiest cells in
the file. Because percentage-point variance is carried by a handful of large tasks, the **Spearman rank correlation is
reported beside every Pearson estimate rather than after it**, and the largest single-task jackknife influence (§10) is
printed next to every headline estimate; a Pearson and a Spearman estimate that disagree in sign or in coverage of zero are
reported as unresolved, not resolved by choosing one.

Four confirmatory tests, one per hypothesis, all on the 1,241-task panel and all pre-registered before any estimate is read:

1. **H1.** The correlation across tasks between the change in a task's Claude.ai share and the change in its API share,
   computed separately in each adjacent window (August→November, November→February), with confidence intervals; the
   confirmatory claim requires both to be negative with intervals excluding zero. The long August→February change is
   reported as a third estimate. Key number: the window correlations with their intervals, each printed beside §8's minimum
   detectable effect, which beside a null is the finding. Whatever the sign, the claim is correspondence, not flow (§6 H1).
2. **H2.** The same two correlations tested against zero and against the smallest effect of interest fixed in §6, reported
   as intervals rather than verdicts, so that a null is a measured null and not an absence of evidence.
3. **H3, redefined** (referee item 3). The earlier within-surface benchmark was degenerate: each surface's shares sum to a
   near-fixed total, so its task changes sum to nearly zero and a task's change against the summed change of the other tasks
   on the same surface is −1 by construction. That statistic is **dropped**. The cross-surface statistic is not constrained
   that way — two sum-to-near-zero vectors paired at random have expected correlation **zero**, the benchmark every estimate
   is read against and the value §10's permutation null verifies on these frames. The denominator reading is then tested
   three ways, all pre-specified: (a) the **window contrast** — August→November carries no February consumer inflow, so an
   estimate that weakens materially towards zero when February is dropped is the consumer-denominator reading; (b)
   **coding-block removal with renormalisation** — drop the 2019-vintage SOC-15 set and renormalise the remaining shares
   within each surface, removing the arithmetic dilution an agentic-coding inflow imposes on every other API share; (c) the
   **level diagnostic** on both surfaces' `onet_task_count` (§8), read as a diagnostic only, a count of sampled records not
   being a count of work. Surviving (a) and (b) does not license the word "flow": inflows anti-aligned inside the non-coding
   panel stay unobservable in these files (§6 H1).
4. **H4.** The same estimate on the pre-specified coding set — SOC major group 15 on the 2019 vintage through cuts 7 and 8,
   modal holder by weight, per §8 — and on its non-coding complement, with the difference between them reported. The two
   sets' minimum detectable effects (about 0.18 on 242 tasks, about 0.089 on 999) are printed beside the estimates: a null
   inside the coding set is weak evidence and is written as such, and the difference carries a wider interval than either.
   The 2010-vintage split is the robustness cut.

**Exploratory allowance: two tests, after the confirmatory set, labelled exploratory in the post and excluded from the
headline.** (a) Naming the tasks in the migrating quadrant — the largest negative products of the two changes — so the post
can say which work carries the correspondence; this is description, not inference, and carries no interval. (b) Whether the
relation is stronger among tasks whose API use is more directive, using `onet_task::collaboration` at global on the API, the
nearest public test of the mentor's conjecture that migrating tasks are the less supervised ones
(`economic-index-2026-03-report`, p.9); it is reported beside the Anthropic result that cuts against that conjecture —
automation on the API fell over these same windows (p.7; `directive` 66.30 → 63.58 → 58.22, §7(4)). Any further test is a
deviation and is logged as one.

## 10. Noise and robustness required

- **Persistence across windows** — the two adjacent windows must agree in sign; the long change is the third window and is
  reported whatever it shows.
- **Panel and vintage** — the estimate recomputed on the window-specific panels (1,317 and 1,595 tasks, both wider than the
  fixed panel, which stays primary because it holds the sample constant), and the coding / non-coding split recomputed on
  the 2010 O\*NET-SOC vintage beside the pre-specified 2019 one.
- **Coding block removed and renormalised** — the estimate recomputed on the non-coding panel with each surface's remaining
  shares renormalised, reported beside every headline estimate (§9 test 3b).
- **Leave-one-out** — the estimate recomputed dropping the highest-mass task, then jackknifed across all 1,241 tasks, the
  largest single-task influence reported beside the headline, not in an appendix.
- **Flagged and fragile units excluded** — `none` and `not_classified` dropped; a near-floor sensitivity dropping tasks
  whose count is 15–20 in any wave, 14 to 65 per frame and about 5% of the panel, those shares being the noisiest
  (§Thresholds).
- **Placebo** — a permutation null pairing each task's Claude.ai change with another task's API change, 10,000 draws, giving
  the distribution under no correspondence on these frames; it replaces the degenerate within-surface benchmark as the
  accounting placebo, and its centre is the zero expectation of §9 test 3.
- **Second implementation** — the correlation recomputed as a rank correlation and as a mass-weighted regression, the panel
  rebuilt independently from the parquet siblings by the analyst and reconciled task by task, and the reproduction leg
  re-run on both vintages from `data/replication/soc15_figA1_2026_03.py`.

## 11. Literature check

Searches run for this brief (16 September 2026): the Chatterji et al. consumer-ChatGPT paper and its sample exclusions;
Dillon, Jaffe, Immorlica and Stanton's field experiment; and a search for any study relating enterprise-API and consumer
task composition, which returned vendor material and no research literature. Closest prior work: Chatterji et al., *How
People Use ChatGPT* (NBER 34255, September 2025), the largest consumer-side task description, which excludes "users on
non-consumer plans (Business f.k.a. Teams, Enterprise, Education)" and so cannot see this margin; Dillon et al., *Shifting
Work Patterns with Generative AI* (NBER 33795 / arXiv 2504.11436, May 2025, revised November 2025 — the short list's
"(2026)" is a citation error corrected here), which does "not detect shifts in the quantity or composition of workers' tasks
resulting from individual-level AI provision", inside firms rather than across surfaces; and Tomlinson et al. (2025),
*Working with AI*, on occupational implications on a single surface. Kharazian et al. (2026) on firm adoption from vendor
spending (`programme/LONGLIST.md`) carries no task detail and was not re-verified today. Where this sits: the cross-surface
correspondence is observable only from a provider's own data on one taxonomy, none has published it, and the identification
limit — aggregate cross-sections cannot separate a flow from two anti-aligned inflows — is a limit of the published data,
not of this design.

## 12. What the closing section will be able to say

**If H1 holds — a correspondence, not a flow.** Across the tasks Claude performs on both surfaces, the work that gained
share on the 1P API lost share on Claude.ai, in both windows, outside coding as well as inside it, and after the coding
block is removed and the remaining shares renormalised; the post names the tasks that carry it. What it cannot say is that
anything moved: two populations arriving with opposite task mixes — casual consumers on one surface, agentic coding on the
other, both of which Anthropic reports — leave the same trace, so the migration sentence has a measured correspondence
behind it and still no measured flow.

**If H2 holds — the measured null.** The two surfaces' task mixes moved without corresponding: a task gaining share on the
API says nothing about its share on Claude.ai, within an interval that excludes the correspondence the reproduced coding
movement would have produced had it been a flow. The migration sentence describes two series measured in the same week, and
the exposure ranking that treats API presence as a signal of displacement risk rests on the surface a task appears on, not
on its having arrived there.

**If H3 holds — the denominators moved.** The correspondence is confined to the window in which a new consumer population
arrived, or it disappears once the coding block is removed and the remaining shares renormalised, or both: what the two
series record is who showed up on each surface, not what work changed hands. The operating rule the post leaves behind is
explicit: a share falling on one surface while it rises on another is not evidence of movement between them, and a migration
claim needs levels, a common denominator, or a within-task cross-surface cut before it can be made.

**If H4 holds — coding carries it.** The correspondence lives in the tasks O\*NET files under computer and mathematical
occupations and is absent from their complement, which is what Anthropic's account of agentic coding being labelled as many
separate tasks would produce. That account is consistent with the pattern and is not shown by it, because no public file
marks a record as Claude Code traffic; what the post establishes is that the pattern in the corpus's headline category does
not carry over to the rest of the work Claude does.

**If the windows disagree, or the estimate is underpowered.** The two windows do not agree in sign, or the intervals cover
both zero and the smallest effect that would count as a flow, at the precision the body reports beside each estimate: the
correspondence is not established and neither is its absence. The post says which of the two it is, names the sample that
would settle it, and leaves the request that follows: publishing the task series at a finer grain or a higher cadence, the
Institute's own stated commitment, would make the same test decisive.
