# Referee verdict · post1 (LL-07) · draft · 2026-09-17

Read: `posts/post1/POST.md`, `notes/claims-map.json`, `notes/verify_page.out.txt`, `site/posts/post1/index.html` and
`site/index.html` (branch `post1-draft` at c148bbe, in a worktree); from main (31898a5): `notes/claims.md` (the boundary),
`data/processed/results.json` (698a2f1), `outputs/figures.json` and the four PNGs, `notes/red-team.md`, `notes/lab-notebook.md`
(deviation count), `prereg/prereg.md` P8, `BRIEF.md` §1, §5, §6, §7, §9, §12, `room/lead-2026-09-17-why-it-matters-post1.md`,
`room/director-2026-09-17-gate-2b-post1-approved.md`, `room/editor-2026-09-17-post1-draft.md`, `team/templates/POST.md`, the
`anthropic-style`, `page-build` and `qc-rubric` skills and `wiki/style/STYLE-GUIDE.md`. One Anthropic source re-read directly
(the June 2026 report's "labor-augmenting" sentence, on anthropic.com); the other quotations checked against the wiki's verbatim
extracts. `reference/` not opened; no data statistic recomputed; no room note between analyst and director on interpretation read.

## Verdict

**PASS WITH CHANGES.** Four items must be applied before the page can go to Gate 3 (items 1–4: a caption title that states a count
the data contradict; an opening sentence that claims a sign the post then says is not fixed; a superlative in the close that the
body attributes to Anthropic and the exploratory split contradicts; a new construct in the close). Twelve should-items and six
could-items follow, each with the sentence as written and the replacement. One editor pass; the second read confirms the items
landed and nothing else moved. One room note to the analyst (`room/referee-2026-09-17-figures-post1.md`): `figures.json` and the
`figures` block of `results.json` carry a caption sentence `claims.md` forbids and the same wrong count as item 1.

**Verifier, my run in the worktree:** `python3 site/tools/verify_page.py post1` → PASS; 216 bindings resolved, 44 quantitative
sentences mapped, 215 numbers in POST.md and 1,099 on the page all in `results.json` (`/tmp/ref` run, exit 0). The PASS is
necessary, not sufficient: check 3 accepts any number that occurs anywhere in a 187 KB `results.json` at any rounding, so small
integers pass regardless of what they mean. I therefore audited every one of the 44 mapped sentences against its *own* bindings
(script in §Method below): 212 of 215 numbers are a rounding of a value the sentence is bound to; the three that are not are `23`
(S11 — it is in `facts.november_is_corroborated_not_independent.source_check`, so a true number, mis-bound), `100` (S14, the
pre-registered floor) and `$10` (S17, the slope's unit). One binding launders a number (item 14).

**Ten bindings checked by hand against `results.json`** (sentence id → key → stored → printed):
S03 `tests.D_nov2025.estimates.D.coef` 7.385412826 → "7.4"; S04 `tests.D_aug2025.estimates.D_corrected_quartile_rule.coef`
0.5433975 → "0.5"; S10 `tests.rob_W1_modal_holder_feb2026.estimates.D.ci` [−0.44383, +0.10365] → "an interval containing zero";
S12 `facts.composition_of_the_top_quartile.largest_software_tasks.nov2025.q4_mass_first` 8.5412677 → "8.5", `.q4_mass_total`
22.5142 → "22.5"; S16 `facts.kish_nov2025.by_quartile[3]` 8.8703714 → "8.9"; S20 `tests.leg_a_feb2026.estimates.D_L.coef`
−11.895184 → "11.9 … below"; S22 `tests.leg_b_feb2026.coverage.identified_mass_share_q1_q4` 75.5174 → "76%"; S26
`tests.leg_e_nov2025.estimates.r_L.coef` 0.5031554 → "0.50"; S29 `tests.DeltaW_nov2025.estimates.Delta_W.coef` 0.8351685 →
"+0.84"; S38 `facts.second_implementation_agreement.bootstrap_coverage` [95.29, 95.22, 95.19] → "95.2–95.3%". All match.
Numbers written in words, which the verifier does not scan, checked separately: "two thirds of a point to more than seven"
(0.669 / 7.385), "twenty-six times" (`between_window_dispersion_of_D.ratio` 26.06), "up to three points" (7.385 − 4.504 = 2.88),
"two thirds to three quarters" (65.5–73.1%), "one fifth to one quarter of named mass" (20.9 / 25.9 / 25.0%), "about a tenth of the
coding family's mass" (10.5–11.6%), "a quarter to two fifths" (26.6 / 28.8 / 37.9%), "about three tenths of a point" (half-widths
0.283 / 0.275 / 0.274), "more than eight hundred thousand" (818,673+), "twelve or thirteen groups" (22 − 10 / 22 − 9), "twenty-four
… sixteen" (`counts`), "twenty-two major groups". All hold. One does not: limitation 9's "an order of magnitude" (item 12).

**Forbidden sentences and paraphrases** (`claims.md` §"may not state"), grepped on POST.md, the captions, the headings, the page's
rail and the site card: no "wage bill" (only "labour payments" as what a *framework* wants and what this post does *not* supply —
allowed, since both sentences say Δ_W is not it); no "twelve"; no "cheap"/"expensive"; no "outright"; no "delegation rises with
the wage" except as H1's own statement in the hypotheses table, where the same row records that H1 failed; no "tracks the wage";
no "stable"/"persistent gradient"; no "survives every"; no "ruled out" (limitation 6 says "has not been ruled out"); no
"significant"; no first person outside an Anthropic quotation; no summary block. "Shows" appears twice: once inside Anthropic's
bound ("does not show what happened outside the chat window", allowed) and once as the verb of a finding (item 11). "Gradient" is
used of D in Figure 3's caption title (item 8) and in the analyst's in-image title (room note).

## Items

### Blocking (apply before the second read)

**1. Figure 1 caption title states a count the data contradict.** Section: finding 1, the paragraph beginning `**Figure 1.`
As written: "…the difference clears a percentage point in two windows on the pre-registered quartile rule **and in none once the
boundary wage is shared**, and it does not clear a point in every window under either rule." On the corrected rule the differences
are +0.54 / **+7.18** / +0.34 (`tests.D_*.estimates.D_corrected_quartile_rule.coef`): November clears a point. The count is "one",
not "none". Provenance, stated plainly: this sentence is the exact text the referee prescribed at the results review
(`referee-results.md` item 9), which the analyst applied to `figures.json` and the editor copied faithfully — the error is the
referee's, and it has now sat in three files. Replacement (the whole bold title):
"**In all three Claude.ai windows the delegated share is higher on top-quartile than on bottom-quartile tasks; the difference
clears a percentage point in two windows on the pre-registered quartile rule and in one once the boundary wage is shared, and
under neither rule in every window.**" The analyst corrects `figures.json` and `results.json` `figures.fig1.caption` to the same
text (room note). Severity: blocking — a caption may not state what the exhibit contradicts.

**2. The opening claims a sign the post then says is not fixed.** Section: "The puzzle Anthropic left open", paragraph 2, last
sentence. As written: "This post establishes the sign, and then finds that the sign is not the interesting part." The "sign" of
this paragraph is the sign of the error made by reading an unweighted share as weighted — Δ_W — and Δ_W is −0.02 (interval
containing zero), +0.84, −0.15: the next paragraph rightly calls it "a small correction of unfixed sign". The sentence contradicts
the finding and would be the first thing quoted. Replacement: "This post measures that error in three windows and finds it small
and of no fixed sign — and then finds that its size and its sign are not the interesting part." Severity: blocking — the opening
claim must be no stronger than `claims.md`'s, and this one is stronger than the result.

**3. The close upgrades a hedged body sentence into a superlative the results do not carry.** Section: "What this means",
paragraph 3. As written: "coding, the best-paid work in this data and the most fully handed over." The body (finding 2, paragraph
1) says "by Anthropic's own gloss of automative use, the most fully handed over" — an attribution the close drops, which the style
rule forbids ("check that no adjective has been upgraded"). Two further problems: "the most fully handed over" is contradicted by
the post's own exploratory split (`directive`, the complete-hand-off pattern, is *lower* in the top quartile in every window,
−7.0 / −9.5 / −9.9) and by limitation 7, which says so; and "the best-paid work in this data" is not a `results.json` fact — what
is in `results.json` is that Computer & Mathematical tasks are 65–73% of the top quartile's usage (`leg_a_*.coverage.dropped_share_q4`).
Replacement in the close: "coding, which is most of the best-paid quarter of the work in this data and the work Anthropic's own
gloss of automative use names." Replacement in the body (finding 2, paragraph 1, first sentence): "The composition rule was
registered because the coding family is most of the best-paid quarter of the work in this data and is the work Anthropic's own
gloss of automative use names — 'asking the model to directly complete a task or debug errors' (Economic Index report, March
2025)." The quotation is verified (`wiki/style/economic-index-2025-03-report.md` line 93). Severity: blocking — a superlative on a
finding, and a close that says more than the body.

**4. A construct appears for the first time in the close, and the sentence overreaches limitation 1.** Section: "What this
means", paragraph 4, last sentence. As written: "If the within-group difference stayed negative while the coding family's own
internal contrast went to zero, the composition reading would be doing all of the work and the price reading none." The "coding
family's own internal contrast" (the within-SOC-15 top-minus-bottom difference, a side-estimate in `claims.md` 31) is nowhere in
the body; and limitation 1 says the design cannot separate the wage of the work from the kind of work at any grain, so no result
could license "the price reading none". Replacement: delete the sentence. The paragraph already names, in its previous sentence,
the three things that would move the reading (red-team §8). Severity: blocking — "nothing new in the close" is a corpus-wide
invariant and the claim exceeds the limitation the post itself states first.

### Should (apply in the same pass)

**5. Anthropic's own bounding results are absent, and one opening sentence is too strong because of it.** Section: "The puzzle
Anthropic left open", paragraph 1, last sentence. As written: "It has not been crossed with how the work was done." Anthropic has
crossed task value with how much back-and-forth the work took — "In conversations mapped to higher-wage occupations … users
engage more (1.53 times as many turns)", read conditionally as "If the human remains involved in the highest-value tasks, the
pattern looks more labor-augmenting than labor-displacing" (June 2026 report, pp. 13–14; verified on anthropic.com) — and it has
published the collaboration facet by occupational category once (Feb–Mar 2025), a cross that is not monotone in wage. BRIEF §7(4)
marked these "carried into the post"; the draft carries none of them, and the red-team memo §9(4) says what the post may say about
them ("consistent with, never confirmation"). Replacement for the opening sentence: "It has been crossed with how much
back-and-forth the work took — in conversations mapped to higher-wage occupations users take more turns, a pattern the June 2026
report reads, conditionally, as looking 'more labor-augmenting than labor-displacing' — but not with the collaboration facet
itself, the measure that defines delegation." Add one sentence at the end of finding 2's exploratory paragraph (after "…is a
feedback-loop difference.**"): "Both the reversal outside coding and the lower `directive` share at the top are consistent with
that turns reading — consistent with, not confirmation of it — and the U-shape of Figure 2 echoes the one published cross of the
collaboration facet with occupational category, which was not monotone in wage either." No number enters (the verifier would
reject 1.53, which is not in `results.json`; write "more turns"). This is assumptions-sweep item (4), newly flagged at the draft.

**6. The opening's "modeller" sentence lacks the fence `claims.md` puts on it.** Section: "The puzzle Anthropic left open",
paragraph 3, last sentence. As written: "The quantity a modeller should be conditioning on is the coding share of the task mix,
not its pay." `claims.md` licenses "the wage of the work is not what orders delegation on Claude.ai; the kind of work is" *with*
"on Claude.ai" and "in these windows" in the sentence, and forbids its becoming "the wage does not matter". Replacement: "For a
modeller reading these windows, the quantity to condition on is the coding share of the task mix rather than its pay."

**7. "Four deviations" is not the notebook's count, and the disclosure of what had been seen is incomplete.** Section: "What was
set in advance". (a) As written: "Four deviations were logged, each with the registered rule and the corrected rule both run and
both reported." followed by four bullets, the second of which says "as part of the same deviation". `notes/lab-notebook.md`
carries three `DEVIATION` headings (lines 144, 256, 273); the tie order is inside the first. Replacement: "Three deviations were
logged, each with the registered rule and the corrected rule both run and both reported." and fold the second bullet into the
first: "**The quartile rule at the $43.40 wage mass point.** The registered sentence does not say which of the tasks sharing the
boundary wage fall in the top quartile; the registered rule was made reproducible by fixing the tie order on (wage, task text), an
order-free fractional rule was run beside it, and both declare the same owner." (b) As written, paragraph 1: "Nobody had computed
or seen D, any quartile automation share, any leg, or the permutation null." True, but a reader should also know what *had* been
seen before the composition rule was fixed. Append: "What had been seen, and is listed in the pre-registration, was the shape of
the quartiles without their outcome: the boundaries, the coding family's share of the top quartile, the use-case mix by quartile,
the Kish effective counts and the Seychelles figures."

**8. Figure 3's caption title calls D "the gradient".** Section: finding 2, the paragraph beginning `**Figure 3.` As written:
"**The gradient does not survive either composition leg: …**" `claims.md` sentence 1 bounds "gradient" to appear only with
"top-minus-bottom", and the body's own sentence (finding 1, slope paragraph) says the relation "is not a gradient; it is a
contrast between two ends of a distribution". Replacement: "**The top-minus-bottom difference does not survive either composition
leg: excluding Computer & Mathematical tasks, or holding the occupational group fixed, turns it negative in all three windows;
restricting to work-dominant tasks does not.**" (Same change for the analyst's `figures.json`; room note.)

**9. Figure 4's caption title asserts August's direction, whose interval contains zero.** Section: finding 3, the paragraph
beginning `**Figure 4.` As written: "…and not in the same direction as the quartile gap in two of the three." August is −0.02
[−0.057, +0.013]; its direction is not established, and the style rule puts the hedge in the title when the finding is
conditional. Replacement: "…and in the same direction as the quartile gap in only one of the three, August's interval containing
zero."

**10. "The correction exists" is the "signed" temptation in mild form.** Section: finding 3, last paragraph. As written: "So the
correction exists, is small, and cannot be applied in a known direction from three windows: …" In August the interval contains
zero, so existence is not shown there. Replacement: "So the correction is small in every window, indistinguishable from zero in
one, and cannot be applied in a known direction from three windows: …"

**11. "Shows" as the verb of a finding.** Section: Limitations, item 7. As written: "the exploratory split shows the two
components moving in opposite directions across the wage distribution". `claims.md` lists "shows" among the words the post may not
use of a finding. Replacement: "in the exploratory split the two components move in opposite directions across the wage
distribution".

**12. "An order of magnitude" is not the arithmetic.** Section: Limitations, item 9. As written: "— an order of magnitude above
the differences reported here." The bound is 14.1 / 20.2 / 16.1 against differences of 1.4 / 7.4 / 0.7: twice November's, twenty
times August's, thirty times February's. Replacement: "— twice the largest difference reported here and twenty to thirty times
the smallest."

**13. Limitation 2 states a conjecture as a fact and uses a phrase no reader will parse.** Section: Limitations, item 2. As
written: "Anthropic's own country regression reports lower-usage countries delegating more, which would push a coding-heavy,
high-usage top quartile *down*, so the direction of this bias is against the declared sign." The direction follows only if
top-quartile tasks are drawn relatively more from high-usage countries, which the global grain cannot show. Replacement:
"Anthropic's own country regression reports lower-usage countries delegating more; if top-quartile tasks are drawn relatively more
from high-usage countries — which the global grain cannot confirm — that would push the top quartile's share *down*, so the
likelier direction of this bias is against the declared sign." Also, same item, as written: "and no reverse construction is
identified" → "and a task's rate cannot be rebuilt from the country files".

**14. One claims-map binding launders a number.** File: `notes/claims-map.json`, S44. The "2" of "widened from ±1 to ±2
percentage points" is bound to `facts.composition_of_the_top_quartile.largest_software_tasks.aug2025.tasks_matching_first = 2`,
which has nothing to do with the placebo band; the band itself is in no `results.json` field (only in the lab notebook). The
page-build skill forbids using a binding "to launder a number that is not in results.json". Fix: write the band in words —
"widened from plus or minus one to plus or minus two percentage points" — and drop the spurious binding (the verifier does not
scan words); or ask the analyst to add `facts.synthetic_recovery.permutation_size_band_pp` and bind to that. Also, S11's "23"
should be bound to `facts.november_is_corroborated_not_independent.source_check` rather than pass by coincidence.

**15. "Higher than" a line of the same value.** Section: finding 3, paragraph 1. As written: "set separately from — and higher
than — the one-point margin the quartile difference is judged on." Both lines are one percentage point; the brief's "higher" is
its per-point arithmetic, which `claims.md` forbids as a realised relation and which "What was set in advance" already reports as
an assumption. Replacement: "set separately from the one-point margin the quartile difference is judged on."

**16. The assistance disclosure's caption count.** Section: "Assistance disclosure", paragraph 2. As written: "two figure captions
were found to state a number the data did not support and were corrected." After item 1, replacement: "three figure captions were
found to state a number or a count the data did not support and were corrected — two at the results review and one, introduced by
the results review's own fix, at the draft review."

### Could (editor's discretion; none blocks the second read)

**17. Figure 2's caption.** (a) The per-quartile task counts were dropped from the analyst's caption (Q1 600 / 699 / 649; Q4 360 /
403 / 482). They exist in `results.json` only inside the `figures.fig2.caption` string, not as fields, so the editor's caution was
right; if the analyst adds them as fields (room note), restore the parenthesis — the style guide marks the missing n as the
corpus's commonest fault. (b) "Bars are two-sided 95% intervals…" describes marks the reader cannot see: at ±0.3 pp the bars are
inside the markers. Append "and narrower than the markers at this scale". (c) The x labels carry dollar levels; append to "The x
labels carry each quartile's usage-weighted mean hourly wage": ", this post's levels, which do not reproduce Anthropic's task-value
series (Limitations, 8)".

**18. Finding 2's heading has no "Claude".** As written: "The excess is Computer & Mathematical work: with that family excluded,
the top quartile is delegated less than the bottom". Replacement: "…the top wage quartile on Claude.ai is delegated less than the
bottom". Likewise the bold sentence of `claims.md` 13 ("The excess is carried by Computer & Mathematical tasks…") could take "of
Claude.ai usage" after "the top quartile's".

**19. The legs are lettered (a), (b), (e).** Section: "How to tell the explanations apart", last paragraph. A reader will look for
(c) and (d). Append: "— the pre-registration's (c), the leave-one-group-out series, and (d), the use-case mix by quartile, are
descriptive and are reported beside the legs, not as legs."

**20. The fourth window is named in Methodology and nowhere else.** `rob_fourth_window_*` (Feb–Mar 2025 read on each wave's
quartiles) is positive in sign and unresolved at a design-based MDE of 14.7–17.1 pp. One clause in the Stress-tests paragraph would
tell the reader what it showed: "a fourth task-level window on the unchanged taxonomy (positive in sign, unresolved at the
task-level bound)".

**21. "Most conclusions standing".** Section: "What this means", paragraph 1. As written: "close enough to the unweighted one to
leave most conclusions standing". "Most conclusions" is unfenced. Replacement: "close enough to the unweighted one, in these
windows, that the choice between them is not what a conclusion turns on".

**22. In-image titles (analyst's PNGs; for the room note).** Each PNG carries its own title above the plot, so every exhibit has
two titles against the style rule's one. Figure 2's reads "the bottom quartile is delegated nearly as often as the top", which is
false for November (46.6 against 54.0); Figure 3's reads "reverses the gradient". If script 09 is re-run for items 1 and 8, the
in-image titles should be made descriptive ("Top-minus-bottom difference in the automation share, three Claude.ai windows" etc.)
or dropped.

## The two editor flags

**(a) Length.** 6,071 words excluding captions by my count (7,120 with), against a corpus range of ~1,900–2,300 for a special
report or companion blog and ~5,900 of body for the 2025-02 paper. The post proper — puzzle through "What this means" — is about
3,350 words; the remaining ~2,700 are the template's own additions (Recommendations 308, Limitations 735, Methodology 660, What was
set in advance 480, Reproduction 235, Assistance disclosure 279), which the corpus does not carry and the criteria require. Inside
the post proper the excess over a special report is the caveats `claims.md` makes mandatory in the same paragraph as each finding
(sentences 3, 5, 6, 8, 9 and the country-mix sentence with 1; the residual composition with 14; four caveats with 19; "rate, not a
bill" with 22). I find no section to cut: the finding sections are the required text, and the opening's third paragraph is what
the human asked for. Items 4 and 7 shorten the close and the deviations list slightly. The length is justified; it should be
declared in `pr-description.md` as the cost of the caveat rule, not apologised for.

**(b) Captions.** The editor's shortenings are faithful to the plotted data and to `claims.md`, with three exceptions that are
items 1, 8 and 9 — and item 1 was inherited, not introduced. Dropping the Figure 4 sentence "so it is the size of the error made
when a conversation-counting automation share is read as though it were weighted by the wage bill at stake" was right twice over:
`claims.md` forbids wage-bill statements, and the sentence is wrong on the construct — Δ_W has no hours in it, so it is not the
error against a wage-bill weighting but against an hourly-wage one. Dropping the trailing "about 0.11 to 0.12 pp of Δ_W per point
of quartile gap, so a full point of Δ_W needs a gap of roughly 8 to 9 points" was also right: under three realised markers it reads
as a realised relation, and the realised ratio is −0.016 / +0.113 / −0.219. Moving the Kish n into Figure 1's caption was an
improvement. **The analyst should correct `figures.json` on main** (Figure 4: delete both sentences; Figure 1: the count of item 1;
Figure 3: item 8), and `results.json`'s `figures` block with it, since `results.json` is the record and now carries a sentence the
claims list forbids. Room note written.

## Structure

Twelve template sections in order, with three finding sections (H2s: puzzle · how to tell · three findings · what this means ·
recommendations · limitations · methodology · set in advance · reproduction · assistance disclosure); the page's contents rail
lists the same twelve headings, and its four `<figure>` blocks resolve to the four PNGs with the POST.md captions. The
hypotheses table matches BRIEF §6/§9 signature for signature: H1 (lower bound > +1 pp in all three **and** every testable leg
keeps sign and more than half the size), H2 (upper bound < −1 pp in all three), O-A (after H1 and H2, all three intervals
excluding zero with one sign), H4 (all inside ±1 pp and not all excluding zero one way), O-B (else), H3 (a declared D losing sign or
more than half its size on a leg in every window in which it is testable — the pre-registration's completed persistence rule);
the outcome column matches `facts.declared_owner`, `facts.H3_declaration` and `facts.H1_signature_clause`. "What was set in
advance" names 066b761 and the one script run before it; the deviation count needs item 7; the three places the pre-registration
completed the brief are named. Reproduction names scripts 01–09 and both page commands. The assistance disclosure names what was
done to catch the work being wrong and what it cannot catch. No summary block. The site card states the `claims.md` answer
sentence with the coding clause in the same sentence.

## Register

No first person outside an Anthropic quotation. The question and title say AI; every finding sentence, headings 1 and 3, every
caption and the close say Claude or Claude.ai (heading 2: item 18). Findings are plain-sentence headings with the qualifier inside
("…and only the sign is steady"; "…moves it by less than a point, and not in one direction"). Every finding sentence carries its
unit, its fence and both levels; the definition of "delegated" sits in the paragraph before the first number, with the `none`
share beside every quartile and Anthropic's two bounds attached. Nulls carry their MDE in the sentence (slope: 0.11 per $10; Δ_W
August: 0.05). Limitations: framing sentence derived from the design's virtue; nine items in `claims.md`'s order; item 1 withdraws
a sentence by name; item 4 names two thresholds at which the conclusion flips; limitations 1 and 2 are signed (2 after item 13);
not every item cuts one way. Recommendations: three, each with an actor, an action and the circumstance in which it would not
work; no Anthropic programme offered. "What this means": the only numbers are the ones `claims.md` requires in the close ("less
than a point", "clearing a point", "fourteen to twenty"); every paragraph opens on the world or the method; "delegated" does the
work in the last paragraph; the answer sentence is `claims.md`'s. The generalisation sentence (`facts.generalisation_sentence`)
appears in Figure 1's caption, limitation 9 and the close. Hedge ladder: "reads as", "is consistent with", "suggests" — one rung per
claim; the two upgrades are items 2 and 3.

## The reader's test

After the opening and "What this means", a reader who has not seen `results.json` can say: the top wage quartile of tasks brought to
Claude.ai was delegated more than the bottom in three windows, by a size that was not the same twice; the whole of the excess is
Computer & Mathematical work, and without it the top quartile is delegated less; wage-weighting a published automation share
moves it by under a point in no fixed direction; so a modeller should condition on the coding share of the task mix, and should not
read any of this as a statement about work in general. That is what was found, what it means and why it matters. The draft fails
the test in one place — paragraph 2 of the opening promises a sign the post does not deliver (item 2) — and is weakened in two:
the reader who knows the June 2026 turns reading will think the post has not seen it (item 5), and the close's last conditional
introduces a comparison the body never made (item 4).

## Independent re-derivations

Not applicable at the draft stage; the three headline numbers were re-derived from raw at the results review (`rederivation/`,
match ≤ 3e-14 pp). No data statistic was recomputed here by scope. The claims-map audit script is at
`/tmp/ref/audit_map.py` in the review sandbox; its method is stated below so it can be repeated.

## Assumptions sweep at the draft

(1) **Value judgement — handled.** "The wage of the work" throughout; no "cheap"/"expensive"; low-wage and high-wage defined in the
opening as the bottom and top usage-weighted quartile of the tasks brought to Claude, "not of the economy", with Anthropic's own
bound quoted. (2) **Construct mapping — handled.** The definition (directive + feedback loop over five classified patterns) sits
before the first number with the `none` share beside each quartile; automation ≠ autonomy and the outside-the-chat bound are
quoted from Anthropic; Δ_W is "an hourly rate, not a bill" at every appearance; the exploratory split and limitation 7 fence the
word "delegated"; "outright" is absent. (3) **Composition and selection — handled, and it is the finding.** Occupation inferred
from the task, not the user, in the opening; the country mix as limitation 2 with the Seychelles bound; cohort change inside the
persistence test in the same paragraph as the three D's; the use-case rival reported as "nothing shown". (4) **Anthropic's own
results that cut against or bound the framing — newly flagged.** None of the four the brief marked "carried into the post" is in
the draft (item 5 gives the exact text for the two that matter; the education-level null and the Opus gradient may stay out).

## Method for the map audit

For each of the 44 entries in `claims-map.json`: resolve every binding against `results.json`; build the set of roundings (0–4
decimals) of every numeric value and of every number inside a bound string, plus `as_printed`; extract the sentence's bindable
numbers with the verifier's own `numbers_in`; report any number not in the set. Result: three coincidence passes (23, 100, $10),
one laundered binding (S44), no wrong value.

## What I could not verify

- The page was checked by parsing `index.html` (headings, rail, four figures, 67 drawers, captions), not by rendering it in a
  browser; layout faults would not show in this check.
- Anthropic's quotations were checked against the wiki's verbatim extracts; only the June 2026 "labor-augmenting" sentence was
  re-read on anthropic.com. Page numbers (p. 8, p. 19, p. 25, p. 7, p. 3, pp. 13–14) are the brief's and were not re-checked
  against PDFs.
- The dollar levels in Figure 2's x labels ($18–20 / $30–31 / $39–40 / $50–51) are read from the image; no `results.json` field
  carries them and no sentence of the post depends on them.
- Whether the analyst's script 09, re-run for the caption corrections, reproduces the PNGs pixel for pixel — the second read
  should diff `figures.json` and the page's copied figures rather than assume it.
