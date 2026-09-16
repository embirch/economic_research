---
from: lead
to: director
about: programme
type: status
needs-reply: no
date: 2026-09-16
---

Step A1 done: `wiki/reports/ai-fluency-index-2026-02.md` (eight required H2 sections, in order).

Three things worth your attention.

1. **The redirect is real but not clean.** `anthropic.com/research/AI-fluency-index` returns HTTP 308 to `academy.claude.com/tutorials/the-ai-fluency-index` (curl, two user-agents), yet `web_fetch` on the anthropic.com URL returned a full anthropic.com rendering of the report. I treated the live Academy page as authoritative and recorded the host differences — including fn 2 reading "January 20–26, **2025**" on the anthropic.com copy against 2026 on Academy. `web.archive.org` is **blocked by egress policy**, so the anthropic.com copy could not be corroborated; nothing is quoted from it. The report's own BibTeX URL 404s.
2. **Every per-behaviour number is alt text only** (all 11 prevalences, both split charts). Marked `(alt text)` throughout per your ruling. The alt text exists on the Academy rendering only.
3. **Data question for the steward, not answered here:** does any released Claude.ai file cover 20–26 Jan 2026, or carry a turn count or artifact flag? No data file was opened.

No PDF exists. No commit made.
