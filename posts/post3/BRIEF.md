# post3 · When AI's coding share falls on one surface, does the coding that remains narrow?

## 1. The question

As the share of AI use classified to coding tasks falls on the consumer surface and rises on the
developer surface, is the coding work that remains on the consumer surface becoming more
concentrated, less concentrated, or unchanged in composition?

*Title form, settled here (editor's note, `room/editor-2026-09-16-sketch-LL-36.md`).* The sketch's
"leading edge" is dropped: the corpus's term is leading **indicator**, applied to the migration of
coding work to the API — "we expect that this migration from Claude.ai to the API may signal more
imminent transformation of work for the associated jobs" (`economic-index-2026-03-report`,
2026-03-24, p.7) — not to a frontier of capability. "Or just its largest share" is also dropped: it
presupposes that a series cannot be both the largest share and an indicator. The question says AI;
every finding and every measurement in the post says Claude.

## 2. Why it matters, and to whom

The Institute's most load-bearing labour-market assertion is a sentence with no number attached:
"At Anthropic, we can see early evidence that jobs like software engineering are changing radically."
(`institute-agenda-2026-05`, 2026-05, *Lead ¶4*). The corpus's coding series is what a reader reaches
for as its evidence, and that series is falling on Claude.ai: "the share of conversations on
Claude.ai assigned to such (mostly) coding-related tasks is down from a peak of 40% in March 2025 to
34% in November 2025" (`economic-index-2026-01-report`, 2026-01-15, p.7), then "Since August 2025,
the share of tasks in this category has increased by 14% in the API and decreased by 18% in
Claude.ai" (`economic-index-2026-03-report`, p.7).

A falling share admits two readings and the corpus has never separated them. If the share falls
while the work inside the category concentrates into fewer tasks, the series is saying something
about the work itself; if the composition is unchanged, the claim is about the denominator —
everything else arrived, and coding did not change. The readings imply different actions for those
who use this series: the Institute, committed to "updating the Economic Index to share more
high-frequency, granular data" (`institute-agenda-2026-05`, *ED-7*) and to using it as "an early
warning signal for significant change and disruption" (ibid., *Share 1*); and the labour-market
researchers who now build exposure measures on provider logs.

Only the Economic Index can settle it: it is the one public series that publishes task-level usage
shares on two surfaces of the same provider, in three windows built on a comparable task taxonomy,
with enough detail to look **inside** an occupational category rather than at its total. No
`soc_occupation` facet exists after August 2025 (`data/ATLAS.md` §Cuts 13), so the category must be
rebuilt — and the rebuild reproduces Anthropic's published facet exactly (0.0000 pp mean absolute
error across the 22 major groups, steward §8), which makes the question answerable at all.

## 3. The thread of Anthropic's inquiry this builds on

**Thread T7 (agentic coding and the agentic surfaces), with T1 (adoption and diffusion).** The gap
this post occupies is `L-2025-03-R2-09`, *open*: "the increase in these other categories could
reflect either ongoing diffusion of AI throughout the economy, novel applications of coding to those
domains, or unexpected capability improvements in the model" (`economic-index-2025-03-report`,
2025-03-27, § "What's changed since the launch of Claude 3.7 Sonnet?") — three explanations for
movement in the category shares, none tested, and the same fork recurs in the September 2025 report.

Two further ledger items are **touched, not addressed** (referee correction 7): `L-2025-04-SWE-11`,
"Which software development roles will change the most, and which might disappear entirely?" and
`L-2025-04-SWE-14`, "jobs that center on making simple applications and user interfaces might face
earlier disruption from AI systems" (`economic-index-2025-04-software-development`, 2025-04,
§ "Looking ahead" and key pattern 2). A concentration statistic says nothing about which roles
disappear and nothing about front-end work specifically, and the post says so in its limitations.
`L-2025-02-P1-28` (allocating a task's conversations across the occupations that share it) is
rehoused here from the deleted LL-32 as a pre-registered robustness cut, not a question.

The measure this post extends is Anthropic's own, defined for the whole task universe: "Figure 1.1:
Usage shares among top 10 tasks over time by platform, Claude.ai and 1P API / Share of conversations
assigned to the 10 most prevalent O\*NET tasks, by platform and report version."
(`economic-index-2026-03-report`, p.5). What the thread has established is a set of totals — the
category share by wave and surface, and a whole-universe concentration series (Claude.ai 21 / 24 /
23 / 24 / 19; API 28 / 32 / 33, ibid., Fig. 1.1); what is open is everything inside the category. The
one mechanism the corpus offers for the divergence is asserted without a number: "Claude Code's
agentic architecture splits coding work into smaller API calls, which are labeled as distinct tasks.
So while coding's overall share of API traffic has grown, it is spread across many task categories
rather than concentrated in a few" (ibid., p.6). It is also unidentifiable from the public files: the
API sample includes Claude Code ("This includes data from Claude Code.", ibid., fn 1, p.11) and no
column names a product. ⟨mentor⟩ The migration is the mentor's stated leading indicator: "As tasks
migrate to the API, they may become more exposed to automation. API workflows are far more likely to
be directive, with less need for a human in the loop." (ibid., p.9).

## 4. Overlap, stated

**What Anthropic has shown and has not.** The Computer and Mathematical share is the corpus's
most-cited series — 37.2% in the first paper (`economic-index-2025-02-paper`, 2025-02-10, p.6,
Fig. 2), 37.2 → 39.6 → 36.9 across the first three waves (`economic-index-2025-09-report`,
2025-09-15, Fig. 1.1, p.8), 34% in November with the API "edged higher from 44% in August to 46% in
November 2025" (`economic-index-2026-01-report`, p.7), 35% in February
(`economic-index-2026-03-report`, p.5) — and it is always published as one number per wave per
surface. Concentration is published for the whole task universe only (§3 above), never within a
category, and the call-splitting mechanism offered for the API's behaviour (p.6) carries no
measurement. New here, in one sentence: the same category decomposed from the inside as a
concentration series on both surfaces, which is also the first test of that mechanism's own
signature — a category share rising while concentration inside the category falls.

**What others have shown.** On a different consumer product coding is a small share — "Computer
programming and self-expression both represent relatively small shares of use" (Chatterji et al.,
*How People Use ChatGPT*, NBER WP 34255, 2025, abstract; §11) — but no provider decomposes its own
coding share. New here: the comparison is made inside one provider's category, not across taxonomies.

**Separation from the other posts of this programme** (director's pairs ruling, `programme/SHORTLIST.md` §5):
- **post2 (LL-11)** headlines cross-surface task **migration** and may not headline coding's share.
  This post headlines **composition inside coding** on one surface at a time and cites post2 for the
  migration frame; the two share no key number.
- **post7 (LL-12)** works concentration over the **whole** task universe within a window. This post
  works concentration **inside SOC major group 15 only**, and says so in its first figure caption.
- **post1 (LL-07)** is written first in the construction triple and states the task → SOC join and
  the multi-holder allocation rule in its §8. This post **cites `posts/post1/BRIEF.md` §8 for the
  construction** rather than re-deriving it, and carries the allocation-rule bound (≤0.18 pp on `S`,
  ≤0.39 pp on `C`) as its own pre-registered robustness cut.

**Unblinding notice (what has been seen, and by whom).** Confirming the cuts required the steward to
compute `C` itself; the series sit in `data/checks/results/post3_C_series.csv` and he has
deliberately not printed ΔC. He reports three structural facts without values: `C` is base-invariant;
**the O\*NET vintage flips the sign of the API's ΔC**; and **the Aug→Nov and Aug→Feb legs of ΔC on
Claude.ai do not agree in sign**, which under §10's persistence rule downgrades T1 to descriptive. No
analyst has seen any series. The consequences are fixed in §7(iv), §8 and §10 of this brief, before
the pre-registration is written and before the analyst opens a file; no rule is relaxed in response
to what has been seen, and §10's persistence rule stands exactly as written.

## 5. Contribution

If concentration inside the category moves, the post supplies the first within-category decomposition
of the corpus's most-quoted share and states which of the two readings a concentration statistic
licenses — a narrowing frontier, or a surface left with the routine — without choosing between them on
this evidence alone; if it does not move, the post establishes, with a stated equivalence bound, that
the fall in coding's share on Claude.ai is a fact about the denominator and not about coding.

## 6. Hypotheses

The confirmatory statistic is **C**, the share of a surface's Computer and Mathematical (SOC major
group 15) usage mass sitting in that category's ten largest O\*NET tasks, renormalised inside the
category, computed per wave per surface; **ΔC** is its August 2025 → February 2026 change. The
pre-registered band is **δ = 1.0 pp** (§9 gives the arithmetic behind it). H1–H3 are the three
regions of one test and are mutually exclusive by construction; H4 is a second test on the other
surface.

**H1 · Concentration (ΔC ≥ +1.0 pp on Claude.ai).** The category's share falls while the work inside
it concentrates into fewer tasks.
*Signature only H1 predicts:* C rises **while** the published whole-universe concentration on the same
surface falls (24% → 19%, `economic-index-2026-03-report`, Fig. 1.1, p.5), so the movement is specific
to the category, not the general diversification.
*Counter-evidence:* C flat or falling; or C's rise reproduced in the whole-universe series or in the
two next-largest SOC groups, which would make it a property of the sample rather than of coding; or
C's rise accounted for by a falling node count (a top-ten share rises mechanically when a category
loses tail nodes), which §10's node-count and name-match checks would show.

**H2 · Internal broadening (ΔC ≤ −1.0 pp on Claude.ai).** The category's share falls **and** what
remains is spread more thinly, consistent with the largest coding tasks being the ones that left.
*Signature only H2 predicts:* C falls on Claude.ai while the tasks leaving the Claude.ai top ten are
present and large in the API's SOC-15 top ten in the same wave.
*Counter-evidence:* C falls without any correspondence between the Claude.ai tasks that shrink and
the API tasks that grow; or C falls on both surfaces at once, which points at the classifier or the
taxonomy rather than at migration.

**H3 · Flat composition (|ΔC| < 1.0 pp on Claude.ai, with the equivalence interval excluding ±1.0
pp).** The category's share falls with its internal composition unchanged: dilution from outside.
*Signature only H3 predicts:* C within band **and** a total-variation distance between the August and
February SOC-15 mixes no larger than that of the rest of the task universe over the same window.
*Counter-evidence:* the equivalence interval fails to exclude ±1.0 pp (the result is then
indeterminate, not flat, and is reported as such); or the TVD inside SOC-15 is materially larger than
outside it, meaning the mix changed without the top-ten statistic registering it.

**H4 · The call-splitting signature on the API (share up, C down).** Anthropic's stated mechanism —
"Claude Code's agentic architecture splits coding work into smaller API calls, which are labeled as
distinct tasks" (`economic-index-2026-03-report`, p.6) — predicts the API's category share rising
while concentration inside the category falls.
*Signature only H4 predicts:* opposite signs on the same statistic across the two surfaces in the
same waves, with the API's SOC-15 node count rising.
*Counter-evidence:* the API's C rises with its share; or both surfaces move the same way; or the
API's node count is flat while C falls, making the fall a re-weighting rather than a splitting.

## 7. Assumptions sweep

**(i) Value judgement in the framing — *needs a design change; the change is made here.*** "Leading
edge", "narrowing" and "frontier" all rank the work that remains as better or worse than the work
that left. Anthropic's own term is about location, not quality: "we expect that this migration from
Claude.ai to the API may signal more imminent transformation of work for the associated jobs"
(`economic-index-2026-03-report`, p.7). *Change:* the title and question drop "leading edge" (§1);
the post's finding sentence is about **concentration**, and both readings a concentration statistic
licenses — a narrowing frontier, or a surface left with the routine after the professional work moved
— are stated side by side and neither is chosen on this evidence (referee correction 7).

**(ii) Construct mapping — *newly flagged; two design changes.*** The published statistic is "Share
of conversations assigned to the 10 most prevalent O\*NET tasks, by platform and report version"
(`economic-index-2026-03-report`, Fig. 1.1, p.5), computed over the **whole** universe and, per
`data/ATLAS.md` §Conventions, **not renormalised**; C is the same shape on the category's own mass,
so it is not comparable in level to the published 19% or 24%. Second, the category is a task taxonomy
wearing occupation labels: "a task involving software debugging would fall into the Computer and
Mathematical occupation group" (`economic-index-2025-09-report`, p.20), occupation being inferred
from the task, not the user (`data/ATLAS.md` §Traps 36). *Changes:* every table prints C beside the
published whole-universe series and states the denominator in the caption; and the post never calls
SOC-15 "software engineers" — it says "tasks Claude was used for that O\*NET assigns to Computer and
Mathematical occupations".

**(iii) Composition or selection — *needs a design change; the change is made here.*** The February
window carries a named user-composition shock: "Our sampling period overlapped with the release of
our Super Bowl advertisements, which brought many first-time users" (`economic-index-2026-03-report`,
ch. 2 endnote 3, p.18). An inflow of new consumer users changes the denominator and can move the
within-category mix with no change in anyone's coding behaviour; and November's mix carries a second
composition shock, Seychelles, whose netting is now specified in §8. Externally the problem is
formalised: "platform-derived exposure scores combine task-level AI applicability with the
occupational composition of the platform's user base … consumer and enterprise channels within the
same vendor disagree in sign" (Yin and Ogut, arXiv:2605.21743v2, 2026-05-27, abstract; fetched
2026-09-16). *Change:* the August → November leg, which carries no advertising inflow, is a
pre-registered placebo; ΔC over August → February is reported only alongside it and a finding requires
the two legs to agree in sign. The design cannot separate "who is using Claude" from "what coding is
brought to Claude", no release publishing a user column, and the post says so.

**(iv) Anthropic's own results that cut against or bound the framing — *handled.*** Three bite.
First, the aggregate runs the other way on the same surface and window — whole-universe concentration
on Claude.ai fell, "the top 10 most common O\*NET tasks went from 24% of conversations to just 19%"
(`economic-index-2026-03-report`, p.5) — so an H1 result is a claim about a category moving against
its own sample; the post prints the published series beside C in every table and reports the two
comparison categories (§9, exploratory test 2). Second, a "new coding work" reading is bounded by the
report's own statement that "In this data pull, that cumulative estimate barely changed (Appendix
Figure A.2). Our data from this report showed many fewer novel O\*NET tasks than in our previous
report" (ibid., p.7). Third, the published category
series is not internally consistent across vintages: "This number uses 2019 O\*NET-SOC codes, while
previous reports use the 2010 vintage" (ibid., footnote 2, p.11). *Handling, revised after the
steward's note:* the vintage is not a detail but the free parameter of this construction — it
decides whether the published +14% API leg reproduces (2019: +14.38%; 2010: +3.27%) and, the steward
reports, it flips the sign of the API's ΔC. It is therefore **pre-registered in §8 rather than left
fixed by convenience**: the 2019 recode is primary because it is the taxonomy of the figures being
reproduced, the shipped 2010 statements are the robustness arm, both series are published, and the
choice is frozen before any ΔC is read (§4, unblinding notice). The post states that a level
computed on the other vintage will differ, and by how much.

## 8. Data, confirmed at column level

**The data steward's feasibility line, verbatim** (`room/steward-2026-09-16-longlist-feasibility-batch-3-answers.md`,
2026-09-16; quotation marks as in the original):

> "**LL-36. FEASIBLE — and the reconstruction gap you feared is 0.02 pp.** Rebuilding SOC major group
> 15 from global `onet_task_pct` through the shipped O\*NET 20.1 statements gives, for August 2025,
> **39.03%** (classified base) and **35.86%** (all-conversation base) against the published
> `soc_occupation` facet's **39.0412%** and **35.8771%**. Series: Claude.ai 39.03 → 36.02 → **32.23**
> (classified); 1P API 49.98 → 51.73 → 51.61, i.e. 45.67 / 46.60 on the all-conversation base — the
> published "~46%" and "34–35%" both reproduce once the base is named. Log (g) 5."

**The caveat that travels with it**, verbatim, on the allocation rule this candidate absorbs from
the deleted LL-32 (same note): "**LL-32. FEASIBLE WITH CAVEAT: the answer is almost certainly 'the
rule barely matters', and the effect size is the finding.** … Equal-split, employment-weighted and
modal-holder allocation move the SOC-15 share by **≤0.17 pp** and the 22-group ranking by at most
**one** position (Aug 2025) or **none** (Nov, Feb). Publishable as a bound on a construction choice,
not as a correction. Log (g) 4." (Superseded in part below: ≤0.18 pp on `S`, ≤0.39 pp on `C`.)

The steward's confirming note is **`posts/post3/notes/feasibility.md`** (2026-09-16, verdict
**FEASIBLE WITH CAVEAT**): every cut below is confirmed at column level — 0 unmatched in 13,644
node-rows, February join 3,258/3,258 (Claude.ai) and 2,297/2,297 (1P API) — and four of his
amendments are carried into this section, this pass.

**Cuts, at column level.** Long schema (Family B), columns `geo_id, geography, date_start, date_end,
platform_and_product, facet, level, variable, cluster_name, value`.

| # | release (window) | grain | facet / level | variable | filter and threshold |
|---|---|---|---|---|---|
| 1 | `release_2025_09_15` (4–11 Aug 2025) | `geography == global` | `onet_task`, `level == "0"` | `onet_task_pct` (with `onet_task_count`) | `platform_and_product` ∈ {`Claude AI (Free and Pro)`, `1P API`}; privacy floor confirmed at exactly 15 conversations |
| 2 | `release_2026_01_15` (13–20 Nov 2025) | same | same | same | same |
| 3 | `release_2026_03_24` (5–12 Feb 2026) | same | same | same | same; platform label `Claude AI (Free, Pro, and Max)`; counts are a scaled 1,000,000 base, so the three waves' counted bases are unequal (Claude.ai 964,494 / 999,875 / 1,000,000) |
| 4 | `release_2025_09_15` **enriched**, Claude.ai only | global | `soc_occupation` | `soc_pct` | reproduction target only: published 39.0412 (classified) / 35.877057 (all-conversation) |

Conventions applied, each from `data/ATLAS.md`: read with `keep_default_na=False` and, for
`release_2026_03_24`, `na_values=[]` (§Traps 1–2); cast `level` to `str` after any parquet read
(§Traps 7); drop the pseudo-task `none` **and** `not_classified`, which are different things
(§Traps 23–24) and, per the steward, are also different from the `soc_occupation` facet's own
residual (8.1047 against 8.1273 in August); the 200 / 100 geography thresholds do not apply here.

**Bases.** The classified base (named tasks) and the all-conversation base (including the unnamed
residual) are both quoted in the corpus and give different levels for the same series
(`data/ATLAS.md` §Conventions). **The two-base rule applies to `S` only: `C` is base-invariant**, a
ratio of SOC-15 mass to SOC-15 mass, identical to every decimal on either base (steward, cut 6).

**Derived metrics.** *Category share* `S` = Σ `onet_task_pct` over SOC-15 tasks, on each base.
*Within-category concentration* `C` = (Σ of the ten largest SOC-15 `onet_task_pct`) ÷ `S`,
renormalised inside the category; the top ten is recomputed within each wave, matching Anthropic's
within-window convention, with a fixed-August-basket variant as the second implementation.
*Secondary:* SOC-15 Herfindahl index; SOC-15 node count per wave, always printed beside its counted
base (a node count rises partly because more cells clear the fixed 15-conversation floor in a larger
base — steward, cut 3); total-variation distance between waves on the name-matched SOC-15 node set.

**Supplementary data, with join key and coverage.**
1. `release_2025_09_15/data/intermediate/onet_task_statements.csv` — O\*NET DB 20.1, 19,530 × 9,
   carrying `soc_major_group` on **974 O\*NET-SOC 2010 codes**; shipped inside a release, and needed
   because no `soc_occupation` facet exists at any grain in the 2026 waves (`data/ATLAS.md` §Cuts 13).
   Join key: the **lower-cased, stripped** task text, 18,428 distinct keys after collapsing case
   variants (§Traps 21). Coverage: rows in 2,616 / 2,054 / 3,168 / 2,251 / 3,258 / 2,297 across the
   six frames, **0 unmatched, 0.0000% of named mass unmatched**.
2. **O\*NET-SOC 2010 → 2019 crosswalk**, `2010_to_2019.csv` from the O\*NET Center, fetched by
   `data/fetch/supplementary_onet.py` (sha256 `8f026a33…`, 1,164 rows), on the model of post2's §8
   cut 8; join key the 2010 O\*NET-SOC code. Coverage: 19,530 (key, 2010-code) pairs in → 20,081 out,
   **0 unmatched**, all 974 codes matched, **337 pairs change major group**. Needed because
   Anthropic's published occupational figures are on the 2019 taxonomy; a text join to a later O\*NET
   **database** is not a substitute, losing ~18–19% of named mass.

The multi-holder allocation rule is **cited from `posts/post1/BRIEF.md` §8**, not re-derived here;
its measured bound is **≤0.18 pp on `S` and ≤0.39 pp on `C`** (steward, cut 8), superseding the
≤0.17 pp figure LL-36 inherited, which was a bound on `S` alone.

**The published number this reproduces first, and the vintage decision** (criterion 3; referee
correction 7). The target is `economic-index-2026-03-report`, p.7: "Since August 2025, the share of
tasks in this category has increased by 14% in the API and decreased by 18% in Claude.ai", read with
`economic-index-2026-03-appendix` Figure A.1 (p.5, "Task usage share trends by occupation group
(V1-V5, 2019 O\*NET-SOC)") and its footnote 1 (p.6): "This figure uses 2019 O\*NET-SOC codes, while
previous reports use the 2010 vintage." **The reproducing specification is: classified base, 2019
O\*NET-SOC recode via the crosswalk, and Anthropic's own released
`map_to_occupational_categories(df, task_statements, soc_structure)`** from
`release_2025_09_15/code/aei_analysis_functions_1p_api.py` (full duplication across holder
occupations, then renormalisation). On it the steward reproduces **+14.380%** on the API and
**−17.512%** on Claude.ai, an independent re-implementation gives +14.389% / −17.521%, and p.5's
"35% of conversations on Claude.ai" lands at **34.59**. On the shipped 2010 vintage the Claude.ai
leg still reproduces (**−17.403%**) while the API leg gives **+3.265%**, and no base rescues it: the
February API all-conversation level is **46.61** (2010) against **55.52** (2019), an Aug→Feb change
of +6.12% against +17.54%. **The free parameter is the taxonomy vintage, not the base**, and this
brief's earlier reading — "the API leg does not reproduce" — and its ±3 pp stop rule are withdrawn.
The **2019 recode is therefore pre-registered as primary**, with the shipped 2010 statements as the
robustness arm, on the stated ground that 2019 is the taxonomy of the figures being reproduced and
the only one on which both published legs reproduce; the choice is fixed now and may not be revisited
after the series are read (§4, unblinding notice; §7(iv)). Its largest single driver is named in
advance: `43-9011 Computer Operators` moves into major group 15 in 2019, carrying 3.83 / 6.92 /
9.32 pp of matched API mass across the three waves. **The post's first published number is that
vintage pair** — the same series on both taxonomies, with the published +14% / −18% beside them —
not a new finding.

**Seychelles, corrected rather than bounded** (steward, cut 9 and §2b; supersedes this brief's
earlier "cannot be removed at global grain"). Seychelles' November country task rows are complete —
67 rows summing to its published 24,715 conversations — and 84.1% of its named conversations are
SOC-15, so it is 5.78% of the entire global SOC-15 mass. Netting it out moves the November point by
**−1.22 pp on `S` (classified) and −1.29 pp on `C`**, both larger than δ, with the residual
uncertainty from its 1,542 unnamed conversations bounded in [−1.33, −1.22] pp on `S`. The November
point therefore enters every test **netted**, with the uncorrected point reported beside it.

## 9. Confirmatory tests and the exploratory allowance

**T1 (H1 / H2 / H3), Claude.ai.** Compute C for August 2025, November 2025 (Seychelles-netted) and
February 2026 on the primary vintage; the confirmatory quantity is ΔC over August → February,
assigned to one of the three pre-registered regions: ≥ +1.0 pp (H1), ≤ −1.0 pp (H2), or inside the
band with an equivalence interval excluding ±1.0 pp (H3). ΔC is reported beside ΔS, the change in
the category share, in the same sentence, with ΔS on both bases and ΔC on one (C is base-invariant).

**Why δ = 1.0 pp, and the power behind the null.** Sampling is not the constraint: on the steward's
effective N (Claude.ai SOC-15 conversations 346,207 / 337,154 / 299,950) the binomial SE on C is
0.083–0.091 pp, so SE(ΔC) ≈ **0.12 pp** and the MDE at 2.8 SE is **≈0.35 pp**; the "raise δ if the SE
exceeds 0.33 pp" clause is **not triggered**. The binding uncertainty is construction — the
allocation rule moves **C** by up to **0.39 pp** and the vintage by several points — so H3's
equivalence interval is built as sampling SE **plus** an explicit construction term (the
allocation-rule spread and the Seychelles correction), never as a sampling interval alone. Two limits
travel with every equivalence claim: conversations are not independent draws and no release carries a
unit identifier, so no clustered error can be computed and the true interval is wider by an unknown
factor; and the counted bases differ across waves, so these are sample, not population, errors.

**T2 (H4), 1P API.** The same statistic and the same three waves on the API, plus the cross-surface
sign test: H4 requires ΔS > 0 with ΔC < 0 on the API in the window where ΔS < 0 on Claude.ai, and the
API's SOC-15 node count rising **relative to its counted base**, which grows 944,638 → 1,000,000
across the window. T2 states in the post what §3 states here: Claude Code is inside the API sample
and no column names a product, so the test can show the mechanism's shape and can never attribute it
to Claude Code.

**Exploratory allowance: three tests, after the confirmatory set, each labelled exploratory, none
in a headline and none carrying a p-value.** (1) Which tasks enter and leave the SOC-15 top ten
between waves, named and tabulated — for interpreting H1 against H2 only. (2) The same C statistic
for the two next-largest SOC groups (Educational Instruction and Library; Office and Administrative
Support), reported on both vintages because group 43 itself changes under the recode — to show
whether a Claude.ai movement is specific to coding. (3) C beside the published whole-universe series,
to show how the two denominators differ.

## 10. Noise and robustness required

- **Persistence across windows.** The August → November leg must agree in sign with August →
  February; a disagreement is reported and downgrades the finding to descriptive. The rule stands as
  written and is evaluated on the Seychelles-netted November point, which is the point the design
  always required (§8); the uncorrected comparison is reported beside it.
- **Placebo.** August → November is the pre-advertising window (assumption (iii)); a movement of the
  same size there means the February result is not about the February window.
- **Leave-one-out.** Recompute C dropping the largest SOC-15 task in each wave, and dropping the
  August wave's largest task from all three.
- **Flagged units netted.** Utah (August 2025) and Wyoming (November 2025) are geographic flags and
  do not bite a global cut. Seychelles does bite November's global mix and **can be netted out at
  global grain** from its complete country task rows (−1.22 pp on S, −1.29 pp on C, both above δ):
  the netted November point is the one used in every test, with the uncorrected point reported beside
  it and the [−1.33, −1.22] pp residual band stated.
- **Second implementation.** The fixed-August-basket variant of C, and an independent re-derivation
  of the task → SOC join written from the O\*NET file without reusing the first script's loader.
- **Allocation-rule robustness (the LL-32 cut, pre-registered).** C and S recomputed under
  equal-split over SOC codes, over major groups, over occupation Titles, and Anthropic's own
  full-duplication rule; the measured bound is ≤0.18 pp on S and **≤0.39 pp on C**.
- **Vintage robustness.** Every headline number is published on both the 2019 recode (primary) and
  the shipped 2010 statements; a sign that depends on the vintage is reported as such and never
  headlined without it.
- **Node-count and taxonomy checks.** SOC-15 node counts per wave and surface beside their counted
  bases, and the name match across **named** nodes (Claude.ai Nov↔Feb 2,886 of 3,168 / 3,258,
  carrying 99.42% / 99.19% of each wave's named mass; API Aug↔Feb only 1,702 of 2,054, the weakest of
  the four), so that a concentration movement cannot be read off a changing node set.
- **Base robustness, and boundaries not crossed.** S is reported on both bases and a finding on one
  base only is not a finding, while C is base-invariant and reported once; the 2025 flat releases use
  `pct_occ_scaled` and are reported separately; the June 2026 release rebuilt on O\*NET 30.2 with a
  new classifier and is not spliced to this series.

## 11. Literature check

**Searches run (2026-09-16):** "Chatterji Cunningham Deming how people use ChatGPT programming share
of messages"; "within-occupation concentration of AI task usage decomposition coding tasks 2026"; a
direct fetch of arXiv 2605.21743; and a search of `programme/LEDGER.md` for every item attached to
the coding thread (`R2-09`, `SWE-11`, `SWE-14`, `P1-28`).

**Closest prior work.** (1) Chatterji, Cunningham, Deming, Hitzig, Ong, Shan and Wadman, *How
People Use ChatGPT* (NBER WP 34255, 2025), the nearest rival series on a consumer product: "Computer
programming and self-expression both represent relatively small shares of use" (abstract) — a level,
not a decomposition, on its own taxonomy. (2) Yin and Ogut, *Who Uses AI? Platform Selection and the
Measurement of Occupational AI Exposure* (arXiv:2605.21743v2, 2026-05-27): "Holding the empirical
design fixed, changing only the platform input changes the post-ChatGPT employment coefficient by a
factor of 1.9, and consumer and enterprise channels within the same vendor disagree in sign"
(abstract) — the formal statement of this post's selection problem, and the reason the two surfaces
are reported separately and never pooled. (3) Anthropic's own reports, above.

**Where this sits.** Between a literature that compares providers' totals and a corpus that publishes
one number per category per wave, nobody — Anthropic included — has decomposed a provider's own
coding share from the inside; this post does that on the release data alone, and takes its
interpretive discipline from the selection literature: a composition statistic on a self-selected
user base bounds a reading, it does not identify a mechanism.

## 12. What the closing section will be able to say

**If H1 holds (concentration).** The coding work left on Claude.ai is a more concentrated thing than
it was a year ago: as the category's share fell by roughly a fifth, the ten largest coding tasks took
a larger share of what remained, and did so while the surface as a whole was diversifying. Two
readings survive this evidence — a narrowing frontier, where the coding that stays is the coding
worth doing in a chat window, and a surface left with the routine after the professional work moved
to the API — and which one the next wave supports is what this leaves open.

**If H2 holds (internal broadening).** Coding on Claude.ai is not shrinking so much as being
hollowed out: its share fell and what remained was spread more thinly across its own tasks, with the
tasks that thinned on the consumer surface sitting among the largest on the developer surface in the
same weeks. The corpus's most-quoted series is then a statement about where coding is done rather
than about how much of it there is, which is a weaker claim than the one the agenda's sentence
invites.

**If H3 holds (flat composition, the null the design can deliver).** The composition of coding on
Claude.ai did not move: the ten largest coding tasks held the same share of the category across a
window in which the category itself lost roughly a fifth of its share, with an equivalence interval
that excludes a movement of one percentage point. The fall in coding's share is then a fact about the
denominator — everything else arrived — and a reader who takes the series as evidence that software
work is changing is reading the arrival of other work as the departure of this one.
