---
from: human (Emily Birch)
to: editor
cc: director, referee
about: post1
type: request
needs-reply: yes
date: 2026-09-18
---

# Post 1: rewrite brief, Gate 3 send-back

The Gate 3 draft on `post1-draft` (`e98d27a`, `posts/post1/POST.md`) is sent back. It is accurate and every number is bound, but it is not readable by anyone coming to it cold, technical or not, and it does not use the style corpus we built. A second draft was written by the human's assistant from the claims list, results.json and the corpus; it is at `posts/post1/notes/human-draft-v2.md` and is the starting point, not the destination. Your job is to produce a third draft that is best-in-class on every point below. Be hyper-critical of both earlier drafts; keep what works, replace what does not, and say in your room note what you kept and why.

## What the post must achieve

1. **Crystal clarity on why delegation versus collaboration matters for understanding the economic future.** Not "the Index has never crossed two tables". The reader must understand, from Anthropic's own published framing, that whether AI substitutes for a person's work or complements it decides who is paid and how much; that Anthropic reads its delegation share as the closest signal it has of which is happening, task by task; that it has deliberately left the interpretation open (capability expansion and displacement risk, or learning-by-doing and gains to adaptable workers); and that the same number is a parameter in its labour-market exposure measure and its economic-scenario models. Say this in plain words, and link the reports.
2. **What we already know and do not know.** The published record on the split: its level, how it moved across waves, who delegates more (API businesses, lower-usage countries, newer users, no relation to the education a task requires), what has been published about the wage of the work (task value, model choice, tokens by wage), and the fact that the two have never been put together. Each statement linked to its report. Use `wiki/reports/` for the facts and the URLs; do not cite from memory.
3. **Why this question, and what the stakes of the results are.** Two readers: a person thinking about jobs (which of two stories about who gets automated first), and a person using the Index's numbers (whether an unweighted delegation share is the right input). Both stakes raised in the opening, each finding tied back to them, both answered in "What this means".
4. **Recommendations that explain why.** Each one as: the action as an instruction to a named actor ("Publish…", "Report…"); what it would look like; the evidence in this post that calls for it, with the number; why it matters on a macro scale, for understanding the economic future. Then when it would not work. Replace "Whoever maintains the observed-exposure measure should…" with that form.
5. **Language.** The right balance between sophisticated and plain, as Anthropic's blog posts do it. Kill every AI-sounding or redundant sentence. Human flow. Fit for an external reader coming in fresh. Short declaratives at each claim. Enumerations broken out with numbers or (i), (ii), (iii). Bold key terms at first definition. Headings that state the finding, never template labels.
6. **Referencing.** Hyperlink every Anthropic blog, report and paper the post draws on, at the point of use, the way Anthropic's posts link their earlier work. URLs are in each `wiki/reports/<file>.md` under "URLs". Quoted phrases carry report and page.

## Materials, all of which you must read before writing

- `posts/post1/notes/human-draft-v2.md` — the second draft, with its structure, opening and enumerations.
- `posts/post1/POST.md` on `post1-draft` at `e98d27a` — the first draft, for its bound sentences, captions and appendix sections.
- `posts/post1/notes/claims.md` — the boundary; nothing outside it. `posts/post1/notes/red-team.md`; `posts/post1/notes/referee-draft.md` and `referee-draft-2.md` (the referee's items on the first draft, all of which still apply); `referee-results.md`.
- `posts/post1/data/processed/results.json`, `outputs/figures.json` and the four figures.
- `posts/post1/BRIEF.md` §1, §2, §5, §12; `prereg/prereg.md` for methods.
- `room/lead-2026-09-17-why-it-matters-post1.md` — the lead's note; it addressed only the modeller and must be widened, not discarded.
- `wiki/reports/` — every report that publishes the collaboration split, the wage of the work, or the "why it matters" statements (2025-02 paper and report, 2025-03, 2025-04 software, 2025-09 report and blog, 2026-01 report and blog, 2026-03 report, 2026-06 report, labor-market-impacts-2026-03, econ-scenarios-paper-2026-09), each with its URLs.
- `wiki/style/STYLE-GUIDE.md` and the three closest corpus files; `.claude/skills/anthropic-style/SKILL.md`; your own agent brief, which has been rewritten for this pass.
- Emily's stated model of the language wanted: Anthropic's blog posts, and, outside Anthropic, Alex Imas's Substack essays for how an economist explains a mechanism to a general reader in plain words.

## Process

1. `git fetch origin && git checkout post1-draft && git rebase origin/main`.
2. Read everything above. Write `room/editor-2026-09-18-post1-rewrite-plan.md`: the opening move chosen, the three corpus files, what you keep from each draft, and the list of Anthropic sources you will link.
3. Write the third draft to `posts/post1/POST.md`. Regenerate `notes/claims-map.json`. Build and verify the page. The verifier must pass.
4. Cold-reader test in your room note, then fix.
5. Commit and push to `post1-draft`. Reply in one line with the commit hash and the paths.

Do not send anything to the referee. The human reads this draft first.
