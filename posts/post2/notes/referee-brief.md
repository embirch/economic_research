# Referee verdict · post2 (LL-11) · brief · 2026-09-16

Reviewed: `posts/post2/BRIEF.md` at `31e5297`; `posts/post2/notes/feasibility.md` at `5541442`;
`room/steward-2026-09-16-feasibility-post2.md`; `room/editor-2026-09-16-brief-post2.md`;
`room/lead-2026-09-16-brief-post2-status.md`; `room/director-2026-09-16-gate-1a.md`. Anthropic's
sources re-read from the PDFs (`economic-index-2026-03-report` and its appendix, downloaded today;
the January 2026 report and the labour-market paper through `wiki/reports/`, whose verbatim
sections were checked against the page cited). Chatterji et al. (NBER w34255) and Dillon et al.
(arXiv 2504.11436) fetched for the two quoted sentences. Room notes between the analyst and the
director were not read; `reference/` was opened only to check for inherited framing.

## Verdict

**BLOCK.** Four blocking items, one design change among them (item 1) and one factual error in a
pre-registered first result (item 2). The brief goes back to the lead once. Every steward number the
brief carries re-derives with my own code (below); the block is about what the design can and cannot
identify, and about one wrong occupation code.

## Items

**1. H1's signature is shared by a rival the brief does not name; Anthropic's own gloss on
"migration" is that rival.** *Checked:* §6 signatures against Anthropic's text. *Found:* the report
glosses the word itself: "This decline in concentration partly reflects coding tasks migrating from
Claude.ai to our first-party API, where Claude Code has grown to represent a large share of sampled
traffic" (`economic-index-2026-03-report`, p.6). That is a composition change *in the API sample*
— a new population of records arriving on the enterprise surface — and it is the API mirror of the
February inflow on Claude.ai. Two inflows with anti-aligned task mixes (casual consumers on
Claude.ai, agentic coding on the API) produce a negative cross-task correlation of share changes in
**both** windows, with no task, user or piece of work moving anywhere. So H1's "signature only it
predicts" (negative in both windows, present outside coding) is not unique; H2's premise
("the two surfaces' task mixes move for their own reasons **and** the cross-surface relation is
zero") is false as stated — independent but anti-aligned inflows give a negative relation; and H3
covers only the Claude.ai denominator when Anthropic says the API denominator moved too. The
within-non-coding test helps (Claude Code alone cannot carry a relation inside non-coding tasks) but
does not close it: the consumer inflow's tasks and the enterprise workflows' tasks are disjoint sets
inside non-coding as well. Nothing in six aggregate frames can separate a flow from anti-aligned
inflows, and the brief should say so rather than let H1 be read as one. *Must change:* §6 — widen
H3 to both denominators, quoting p.6 for the API side; rewrite H1's signature as "the negative
correspondence", with the two readings (flow; anti-aligned inflows) named as indistinguishable in
these files; rename and redefine H2 so its prediction follows from its premise. §5 — the
holds-branch may claim "the first measure of the cross-surface correspondence the migration
sentence asserts", not "the first measure of the corpus's central leading-indicator claim": nothing
in the design tests whether anything leads anything (the phrase is inherited from
`reference/sources/econ-pubs-reports.md` line 537, where it is a different design against
BLS/CPS outcomes). The fails-branch may not say "the exposure framing built on it loses its anchor":
the observed-exposure measure raises exposure for API *presence* and automated *share*
(`labor-market-impacts-2026-03`, PDF p.5) and never used a migration; what fails is the reading
Anthropic attaches to it, and §12's H2 paragraph already says this correctly. §12 — the H1 ending
must carry the concession. §5 freezes at Gate 1b, so this is now or not at all. **Severity:
blocking (design change).**

**2. The occupational attribution in the pre-registered first result is wrong.** *Checked:* the
recode by 2010 code, my own code. *Found:* §8 says "one move, 43-9011 Computer Operators (2010) →
Computer Occupations, All Other 15-1299.\* (2019), carries 9.32 pp of February API matched mass,
most of it one task ('perform routine system administrative functions…')". In the shipped O\*NET
20.1 statements that task is held by **43-9111.01 Bioinformatics Technicians**, which the crosswalk
sends to **15-2099.01 Bioinformatics Technicians** (a major-group-15 code in 2019). By 2010 source
code, the whole SOC 43 → SOC 15 move in February API is 10.32 of 100 classified mass (9.32 points of
the geography total — the brief's figure, mislabelled "matched mass"): 43-9111.01 → 15-2099.01
carries **9.71**, 43-9011.00 → 15-1299.00 carries **0.61**. The same holds in August (3.74 / 0.62)
and November (7.28 / 0.56). The steward's note, `data/ATLAS.md` §Conventions and the research
journal all carry the 43-9011 attribution; the lead copied it in good faith. Two further
overstatements ride on it: "that one task is H4's mechanism inside the replication target" is a
conjecture (a generic system-administration statement that O\*NET files under Bioinformatics
Technicians grew 5.4× on the API; whether that is Claude Code call-splitting is not shown by
anything in the files); and "in large part one task" — with that task removed the 2019-vintage API
leg is still **+10.01%** (53.22 → 58.55) against +3.24% on the shipped vintage, so the task is about
a third of the relative change and the taxonomy revision as a whole is the rest. *Must change:* §8,
discrepancy paragraph — correct the code and title, state the mass on one named base, write
"consistent with H4" and give the without-the-task figure; the steward corrects
`posts/post2/notes/feasibility.md` §2 and §6 and `data/ATLAS.md` (room note sent). **Severity:
blocking.**

**3. The within-surface "share-accounting benchmark" is −1 by construction as described.**
*Checked:* §6 H1 third signature and §9 test 3. *Found:* "a task's change against the mass-weighted
change of the other tasks on the same surface" — if that is the sum of the other tasks' changes,
then because shares sum to a near-constant, Δᵢ = C − Σⱼ≠ᵢΔⱼ and the correlation is −1 identically
(on the panel, C is the small change in panel mass). H1's requirement to be "larger in magnitude
than" it can never be met and H3's test cannot fail. If a mass-weighted *mean relative* change is
meant, the statistic is different and the brief does not say so. *Must change:* §9 test 3 — define
the benchmark so it is not degenerate and state its expected value under no correspondence; the
permutation null already in §10 is the natural accounting placebo, and the coding-block-removed,
renormalised correlation is the natural check on the two-inflow rival of item 1. **Severity:
blocking.**

**4. §12 does not end every outcome.** *Checked:* §12 against §6 and §9. *Found:* the editor is
right on both counts. H4 (coding-carried) has a confirmatory test and no ending. The third paragraph
fuses two outcomes — "distinguishable from neither zero nor the share-accounting benchmark" is an
inconclusive result, "carried by the one window in which the consumer denominator moved" is H3's
signature, and the two cannot both be true of one estimate. There is also no ending for the mixed
case §6 names as counting against H1 (windows disagreeing in sign). *Must change:* §12 — five short
endings: H1 (with item 1's concession), H2 as the measured null, H3, H4, and the mixed or
underpowered case. Gate 1a's instruction was "section 12 written for every outcome including the
null". **Severity: blocking.**

**5. The smallest effect that would count as a flow is not stated.** *Checked:* §6 H2, §9 test 2,
§12. *Found:* the MDE (|r| 0.0795 at N = 1,241) is a detection floor, carried correctly from the
steward. §12's "an interval that excludes any relation large enough to be called a flow" needs a
number the design has not named. It can be set without reading the outcome: e.g. the correlation the
panel would show if the whole reproduced SOC-15 movement were a flow with nothing else moving.
*Must change:* §6 H2 — one sentence saying how the smallest effect of interest is fixed before the
pre-registration; I will block the pre-registration if it is absent there. **Severity: should.**

**6. The primary change metric and its effective N are not stated.** *Checked:* §9 test 1, §10.
*Found:* "the change in a task's Claude.ai share" does not say percentage points or log ratio. On
percentage points the variance of 1,241 changes is carried by a handful of tasks (the largest
coding task is 6–10% of a surface), so the nominal N behind the 0.08 MDE overstates the information;
on log ratios the near-floor tasks (14–65 per frame) dominate and are the noisiest. The rank
correlation and jackknife in §10 are the right instruments but are listed as secondary. The
coding-set test in §9 test 4 runs on 242 tasks, MDE |r| ≈ 0.18, unstated; a null there is weak.
*Must change:* §9 — name the primary metric; state the coding-set MDE beside the 242; report the
largest single-task influence next to the headline (already in §10, make it a reporting rule).
**Severity: should.**

**7. Two Anthropic results that bound the framing are missing from §7.** *Checked:* sweep item 4.
*Found:* (a) the winter-break shock in the same Claude.ai window — "Coursework fell from 19% to 12%
of conversations" (p.6) and "The drop in coursework conversations was 5 percentage points in
countries where the school term was active and 12 percentage points in the countries where most
students were on break" (fn 3, p.11) — a second composition shock beside the Super Bowl, quantified
by Anthropic and absent from §7(3); (b) the surface that tasks are said to migrate *to* became less
directive across exactly these windows — "we show that automation decreased sharply in the 1P API
data" (p.7; Appendix Figure A.3), API `directive` 66.30 → 63.58 → 58.22 in `data/ATLAS.md`
§Components — which cuts against the conjecture the exploratory test (b) is built on and belongs
beside it. *Must change:* §7(3) add (a); §7(4) and §9 exploratory (b) add (b). **Severity: should.**

**8. A common shock across surfaces pushes the sign positive and is not named.** *Checked:* sweep
item 2, direction of sign. *Found:* the classifier changed between waves ("different models can
generate different classification outcomes, though these effects tend to be modest",
`economic-index-2026-01-report`, fn 7, p.18: Sonnet 4 → Sonnet 4.5), and any relabelling hits both
surfaces the same way, which is a positive component in a correlation of changes and would mask a
negative one. *Must change:* §7(2) one sentence. **Severity: should.**

**9. Vintages and bases are mixed in one paragraph.** *Checked:* §7(4). *Found:* "peak of 40% in
March 2025 to 34% in November 2025" and "44% in August to 46% in November" are the January report's
numbers on the 2010 vintage and the all-conversation base (they reproduce from the steward's 2010
classified series times the named-mass ratio: 50.08 × 0.878 ≈ 44, 51.83 × 0.883 ≈ 46, 36.06 × 0.935
≈ 34); "35%" and "+14% / −18%" are 2019 vintage on the classified base. The argument (the Claude.ai
decline predates the API series) survives either way. *Must change:* attach vintage and base to each
quoted number wherever the post quotes them. **Severity: should.**

**10. Title words, "enterprise" and "consumer".** *Checked:* every title word against the design
(the editor's (c)). *Found:* "task", "larger share", "smaller share", "AI use" (question-level term)
are tested; "enterprise API" and "consumer app" are Anthropic's own glosses and Anthropic hedges
them — "we also refer to this as 'consumer data' since it **mostly** represents consumer use … 'enterprise
data' since it **mostly** represents enterprise use" (`economic-index-2026-01-report`, fn 1, p.17)
— and the report's noun is "consumer-facing web product". I accept the title on the editor's
condition (findings say Claude.ai and 1P API) plus one: the measurement paragraph carries the
"mostly". The question says AI. **Severity: should.**

**11. Shared first result with post3.** *Checked:* the pairs ruling. *Found:* §4 separates the
headlines correctly and names the shared November→February Claude.ai series and the Super Bowl
exposure in §4 and §7(3), as required. But the shipped-vs-recoded discrepancy is now a first result
of **both** post2 and post3 (referee correction 7 asks post3 to reproduce R5 p.7 first). The
director should assign which post states the vintage discrepancy and which cites it; and post2's
reproduction leg, a coding-share number, must not become its opening claim. **Severity: should
(director).**

**12. Smaller points.** (a) The H4 coding set's assignment rule for multi-holder tasks is "modal
holder" in the steward's note and unstated in the brief; say by what and how ties resolve (my
modal-by-weight rule reproduces 242 / 242 / 228). (b) "two to three times" for the API residual —
August is 3.4×. (c) The editor's register notes (no numerals in the close; "load-bearing") stand.
**Severity: could.**

**Confirmations.** §8 matches the steward at column level: all four amendments (API
`onet_task_count`; crosswalk as supplementary data with key, coverage, licence; mass base stated on
both bases; 2019-vintage coding set with 2010 as robustness) are carried, as are the wider panels,
the near-floor sensitivity, the directive coverage, the unobservability of the inflow and the
stop at 2026-03-24. The vintage is pre-registered and the shipped-vs-recoded discrepancy is the
first reported result (with item 2's correction). MDE and effective N are carried (0.0795 / 0.0771 /
0.0701). §9 states the exploratory allowance (two tests, labelled, excluded from the headline). §2
is something an economist would care about — whether a provider's two-surface task series
identifies a reallocation of work — once "leading indicator" is removed. The Chatterji et al.
exclusion sentence and the Dillon et al. sentence in §4 and §11 are verbatim.

## Independent re-derivations

Re-ran, own code (`/tmp/referee-post2-rederive.py`, not the steward's scripts), from the cached
raw files:

| quantity | brief / steward | mine | match |
|---|---|---|---|
| six-frame panel | 1,241 | 1,241 | yes |
| Feb panel mass, geography total, Claude.ai / API | 80.89 / 83.22 | 80.8906 / 83.2233 | yes |
| Feb panel mass, named base | 87.01 / 92.18 | 87.0059 / 92.1758 | yes |
| SOC-15, 2010 shipped, API Aug→Feb | +3.2433% | 50.0841 → 51.7084, +3.2433% | yes |
| SOC-15, 2019 recode, API Aug→Feb | +14.3885% | 53.8833 → 61.6363, +14.3885% | yes |
| SOC-15, 2019 recode, Claude.ai Aug→Feb | −17.5208% | 41.9682 → 34.6150, −17.5208% | yes |
| MDE \|r\|, N = 1,241 / 1,317 / 1,595 | 0.0795 / 0.0771 / 0.0701 | same | yes |
| window panels | 1,317 / 1,595 | 1,317 / 1,595 | yes |
| coding set 2010 / 2019 / overlap; Feb API mass | 242 / 242 / 228; 46.31 / 55.29 | same | yes |
| pairs after recode; changing major group | 20,081; 337 | 20,081 (20,063 distinct); 337 | yes |
| occupation carrying the 43→15 move | 43-9011 Computer Operators → 15-1299.\* | **43-9111.01 Bioinformatics Technicians → 15-2099.01**: 9.71 of Feb API classified mass; 43-9011 → 15-1299.00: 0.61 | **no — item 2** |
| "9.32 pp of February API matched mass" | 9.32 | 9.32 of the geography total; 10.32 of classified mass | label |
| API SOC-15 2019 without the sysadmin task | not stated | 53.2231 → 58.5483, **+10.01%** | new |

I did not compute any cross-surface correlation, the outcome of §9; it stays unread until the
pre-registration is filed.

## Assumptions sweep

**(1) Value judgement — handled, with one residue newly flagged.** Share language in the question
and title, "exposed"/"at risk" only inside quotation marks, "a share moving is not a volume moving"
— all in §7(1), and Anthropic's construct quoted ("Share of conversations assigned to the 10 most
prevalent O\*NET tasks, by platform and report version", p.5). Residue: "leading indicator" in §2
and §5 and "loses its anchor" in §5 carry a judgement the design does not test (item 1).

**(2) Construct mapping — needs a design change (item 1); the unit mismatch itself is handled.**
Verbatim definitions: "we analyze a random sample of 1M conversations from Claude.ai Free, Pro and
Max conversations (we also refer to this as 'consumer data' since it mostly represents consumer use)
and 1M transcripts from our first-party (1P) API traffic (we also refer to this as 'enterprise data'
since it mostly represents enterprise use)… For 1P API data, each record is a prompt-response pair
from our sample period which in some instances is mid-session for multi-turn interactions"
(`economic-index-2026-01-report`, fn 1, p.17, 15 January 2026); "We sample 1 million conversations
from both Claude.ai, our consumer-facing web product, and our first-party API, the developer-facing
interface for integrating Claude into products and workflows" (`economic-index-2026-03-report`, p.5,
24 March 2026); "This includes data from Claude Code" (ibid., fn 1, p.11). What the measure
measures: a task's share of sampled records on one surface, where an API record is one call and an
agentic session is many. What "migration" means in Anthropic's own words: "coding tasks migrating
from Claude.ai to our first-party API, where Claude Code has grown to represent a large share of
sampled traffic" (p.6) — a category-level statement explained by sample composition, not a
task-by-task flow. Direction the sign could run: negative under a flow **and** under anti-aligned
inflows on the two surfaces (item 1); positive under any shock common to both surfaces, of which
the classifier change between waves is one (item 8). The brief's own change — no level compared
across surfaces, every estimate a correlation of within-surface changes — is right and stays.

**(3) Composition or selection — newly flagged beyond what §7(3) carries.** Who the users are:
Claude.ai Free, Pro and Max, with "increasing signups beginning around February brought more casual
AI users" (p.6), "Our sampling period overlapped with the release of our Super Bowl advertisements,
which brought many first-time users" (fn 3, p.18), and students partly on break (fn 3, p.11); the 1P
API, developer traffic that "includes data from Claude Code" and where Claude Code "has grown to
represent a large share of sampled traffic" (p.6) — both hedged by Anthropic with "mostly". The mix
that produces the pattern without the mechanism: casual consumers arriving on one surface and
agentic coding arriving on the other (item 1). Occupation is inferred from the task, not the user
(`/mnt/memory/standards/terminology.md`; `data/ATLAS.md` §Traps 36) — the brief says so and the
replication leg is a task aggregate wearing occupation labels; item 2 shows how loosely they fit (a
generic system-administration statement filed under Bioinformatics Technicians). The window split,
the within-surface benchmark (once item 3 is fixed) and the pre-specified coding split are the
right responses; they bound, they do not identify.

**(4) Anthropic's own results that cut against or bound — handled for three, newly flagged for
three.** Handled: call-splitting (p.6, as H4); the Claude.ai coding decline predating the API
series ("down from a peak of 40% in March 2025 to 34% in November 2025", January 2026, p.7); the
near-closed task universe ("many fewer novel O\*NET tasks", p.7). Newly flagged: Anthropic's
composition gloss on "migration" (p.6, item 1); the coursework fall with its 5 pp / 12 pp
term-versus-break split (p.6; fn 3, p.11; item 7a); the API becoming less directive over the same
windows ("automation decreased sharply in the 1P API data", p.7; item 7b). Bounding rather than
against: "task concentration in the API remained roughly flat despite the influx of coding
activity" (p.6) and Fig. 1.1's API top-10 share 28% → 32% → 33% — the API's own mix moved, which
H2's signature requires and H1 must not read as movement from elsewhere.

## What I could not verify

- Whether the growth of the system-administration task on the API is Claude Code traffic: no file
  identifies Claude Code records (`data/ATLAS.md` §Components), so "H4's mechanism" cannot be shown
  or refuted; the post may say "consistent with".
- The exact 2019-vintage rule Anthropic used for Figure A.1 (equal split over codes vs Titles vs
  its released `map_to_occupational_categories`): the steward reports all three agree to within
  0.2 pp and I did not re-run the released function.
- The count bases (964,494 / 999,875 / 1,000,000; 944,638 / 971,525 / 1,000,000) and the directive
  coverage (1,143 / 1,155 / 1,135 panel tasks): I confirmed the API count sums and minimum of 15
  and the base-task counts (2,055 / 2,252 / 2,298) but did not recount the panel intersection with
  the directive cells.
- Any cross-surface correlation: deliberately not computed.
