---
from: editor
to: human (Emily Birch)
cc: director
about: post1
type: status
needs-reply: no
date: 2026-09-18
---

# Post 1, third draft: the plan before writing

Read first: `room/human-2026-09-18-post1-rewrite-brief.md`, then everything it lists —
`posts/post1/notes/human-draft-v2.md`; `posts/post1/POST.md` at `9abaf7c` (the rebased first draft,
content of `e98d27a`); `notes/claims.md`, `notes/red-team.md`, `notes/referee-draft.md`,
`notes/referee-draft-2.md`, `notes/referee-results.md`; `data/processed/results.json`,
`outputs/figures.json` and the four figures; `BRIEF.md` §1, §2, §5, §12; `prereg/prereg.md`;
`room/lead-2026-09-17-why-it-matters-post1.md`; `wiki/style/STYLE-GUIDE.md` and the
`anthropic-style` skill; the `wiki/reports/` entries for every publication linked below.
Memory: `/mnt/memory/standards/` (criteria, register, terminology, file ownership) and the
`research-journal` lessons; both stores are read-only this session, so the durable notes from this
pass are in this file and in `notes/pr-description.md`.

## The three corpus files re-read before drafting, and why these three

1. **`economic-index-2025-04-software-development`** — the post whose answer is coding. Its opening
   move is *concede the objection, then elevate*, and its close discharges the opening exactly; it
   is also the corpus's best placement of Limitations as its own section. This post's finding is
   that a wage result is a software result, so the file that already knows how to write about a
   narrow, influential family of work is the closest model for finding 2 and for the close.
2. **`labor-market-impacts-2026-03`** — the post written for the reader who takes a number into a
   model, and the source of the observed-exposure measure this post makes a recommendation about.
   Two devices taken from it: the AI/Claude naming pair ("The coverage shows **AI** is far from
   reaching its theoretical capabilities. For instance, **Claude** currently covers just 33% …"),
   and *an MDE is not a number, it is a scenario a reader can judge*, which is how the
   fourteen-to-twenty-point generalisation bound is written here.
3. **`productivity-gains-2025-11`** — the corpus's model for the opening this post needs: name
   Anthropic's own published instrument, name the distinction it cannot draw ("We've captured the
   **breadth** of uses … but not their **depth**"), then give one worked case where the missing
   distinction decides the answer (the ten pull requests, nine of them documentation). Its
   limits-before-results paragraph, third from the top, is also copied here as the two limits stated
   before the first table.

## Opening move chosen

**The admitted blind spot in the Index** (move 2 in the skill's list), in `productivity-gains`'
form — but with the *why* in front of the gap, as the send-back requires. The order is: the two
kinds of conversation as concrete cases; the published split and how it has moved; why the split
matters, in Anthropic's own words (substitution against complementarity, and the fork the reports
deliberately leave open); the two places the same number is already a parameter; what is known about
who delegates more, enumerated; what is published about the price of the work; the worked case where
the missing cross decides the answer; the question; the two readers and their two stakes; the
findings in words without numbers; and the two limits a reader thinks of first. No number of this
post's own appears in the opening.

## What is kept, and what is replaced

**Kept from the first draft (`e98d27a`)** — everything the referee verified and nothing else: the
bound finding sentences and their required caveats (claims 1–3, 5, 6, 8–12, 13–22), the four
captions' method content, the nine ranked limitations in `claims.md`'s order, Methodology's verbatim
Anthropic definitions with their page numbers, "What was set in advance" with the three deviations,
Reproduction, and the assistance disclosure. Also kept: the referee's twenty-two draft items, all of
which still apply and none of which is reversed here — the Figure 1 count ("in one once the boundary
wage is shared"), Figure 3's title without "gradient", Figure 4's August hedge, the deviation count
of three, the conditional in limitation 2, "twice the largest difference … twenty to thirty times
the smallest", and the fences on the modeller sentence.

**Replaced from the first draft:** the opening, which began on two chapters of a data release rather
than on the world, and never said why delegation against collaboration matters to anyone; the
template-label headings; the hypothesis table's internal labels (H1, O-A, H3 — meaningless to a cold
reader, and the send-back asks for them out); the unexplained field names in body prose
(`onet_task::collaboration`, `automation_pct`, `not_classified`), which now appear once each in
Methodology where a referee wants them and nowhere in the findings; the recommendation addressed to
"Whoever maintains the observed-exposure measure"; and the sentences that opened on the post rather
than on the world.

**Kept from the second draft (`human-draft-v2.md`)** — its structure and much of its voice: the
definition of the two kinds of conversation by worked case before the abstraction; the labelless
four-answers table; "the gap" as the named quantity; the three cautions beside the headline rather
than in a list at the end; "low-wage work on Claude.ai is not, for the most part, low-wage labour";
the plain-words close; and the word **week** for what the pre-registration calls a window (each
release carries one seven-day window — `data/releases/release_2025_09_15.md` line 8, "Data window
2025-08-04 to 2025-08-11 (one week)"). The dates stay in the captions and in Methodology.

**Replaced from the second draft:** its "why it matters", which is right in substance but carries no
links and no page numbers, so a reader cannot check it — every statement about Anthropic's prior work
is now hyperlinked at the point of use, and every quoted phrase carries its report and page; the
three recommendations, which did not name an actor or reach the macro-scale move; the omission of the
second wage source's P6 sentence and of the API and Job Zone probes; the caption for Figure 2 placed
before Figure 1; and a handful of sentences that state a caveat the claims list requires in a
different paragraph from the finding it governs.

## The Anthropic sources linked, at the point of use

URLs from `wiki/reports/<file>.md`; no other URLs, and no claim about Anthropic's prior work that is
not in `wiki/reports/`.

| Publication | Used for | URL |
|---|---|---|
| Economic Index, first report (Feb 2025) | the split published in every report since | https://www.anthropic.com/news/the-anthropic-economic-index |
| Economic Index paper (Feb 2025) | Autor's substitution/complementarity distinction (p. 9); the directive definition (App. F.3, p. 25); the out-of-chat bound (p. 9) | https://www.anthropic.com/news/the-anthropic-economic-index · PDF https://assets.anthropic.com/m/2e23255f1e84ca97/original/Economic_Tasks_AI_Paper.pdf |
| Economic Index, March 2025 | the gloss of automative use; the one published cross with occupational category | https://www.anthropic.com/research/anthropic-economic-index-insights-from-claude-sonnet-3-7 |
| Economic Index, April 2025 (software development) | the agent surface delegates more | https://www.anthropic.com/research/impact-software-development |
| Economic Index, September 2025 | the five patterns (p. 9); "users delegate complete tasks" (p. 3); the open fork on what rising delegation means (p. 10); the country regression (p. 27) | https://www.anthropic.com/research/anthropic-economic-index-september-2025-report · PDF https://assets.anthropic.com/m/218c82b858610fac/original/Economic-Index.pdf |
| Economic Index, January 2026 | the reversal and "the August spike overstated how quickly it was materializing" (p. 9); the API's automation dominance (p. 10); automation is not autonomy (p. 19); the skill-biased reading (p. 21); the education null (p. 40) | https://www.anthropic.com/research/anthropic-economic-index-january-2026-report |
| Economic Index, March 2026 | the price of the work, "the average hourly wage of US workers who perform that task" (p. 8); the Opus gradient (p. 14); newer users delegate more (Table 2.1, p. 15); "not broadly representative of the US economy" (p. 19) | https://www.anthropic.com/research/economic-index-march-2026-report · PDF https://cdn.sanity.io/files/4zrzovbb/website/4053bf3440c0c85b8852052770c5b4cf882689c3.pdf |
| Economic Index, June 2026 | tokens rise with the wage of the work (p. 13); the turns reading, "more labor-augmenting than labor-displacing" (pp. 13–14); the wage-quartile convention (Fig. 1.3, p. 7) | https://www.anthropic.com/research/economic-index-june-2026-report · PDF https://cdn.sanity.io/files/4zrzovbb/website/9e0eadc8097864886c5d5060ebb1f89b02ea29d6.pdf |
| Labor market impacts of AI (March 2026) | the exposure measure; "fully automated implementations receive full weight, while augmentative use receives half weight" (p. 6); the appendix's α (p. 3) | https://www.anthropic.com/research/labor-market-impacts · PDF https://cdn.sanity.io/files/4zrzovbb/website/2b5bbaf2c1eb81dbf6e6fb813c1a24e35a64d376.pdf · appendix https://cdn.sanity.io/files/4zrzovbb/website/e5f77fc0e77c0185110b5e4b909602791ae76eae.pdf |
| Economic scenarios (Sept 2026) | the delegation share as a held-constant parameter (pp. 27–28) | https://www.anthropic.com/institute/econ-scenarios |
| Estimating productivity gains (Nov 2025) | the price of a task in the productivity exercise | https://www.anthropic.com/research/estimating-productivity-gains |

## Two mechanical changes to my own tools, declared

1. `site/tools/verify_page.py` gains one `EXCLUDE` pattern, `https?://\S+`, with the reason "URL in
   a hyperlink target or citation". Hyperlinks are new in this draft and a URL's digits are not
   claims (`…a64d376.pdf` would otherwise be read as the number 376). It excludes no finding: the
   pattern matches only inside a link target.
2. `site/tools/make_claims_map.py`'s anchor list is rewritten for the new text. Every quantitative
   sentence of the new POST.md matches exactly one anchor and every anchor matches exactly one
   sentence, or the generator exits.

Nothing in `results.json`, the scripts, the figures, `claims.md` or the brief is touched.
