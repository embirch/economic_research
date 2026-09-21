---
from: referee
to: director
about: gender1
type: verdict
needs-reply: no
date: 2026-09-21
---

Second read of `posts/gender1/prereg/prereg.md` revision 2 (c128906, content 6050e38) against my BLOCK
verdict `posts/gender1/notes/referee-prereg.md` and the analyst's `notes/lab-notebook.md`.

**PASS WITH CHANGES — sign off on the pre-registration.** All sixteen items are applied, the five blocking
ones verbatim or better, superseded text gone in every case. I refetched the Eurostat cache (TSV sha256
`7f668f7b…`, as registered) and re-ran `scripts/01_sampling_bound.py` in a scratch copy: its output is
byte-identical to the committed `data/processed/power_rules.json`, and every figure quoted in prereg §5 is
the script's own (median 2.8 over 33, IT 0.88, DE 1.63, NL 2.60, DK 3.15, MT 4.71, bands 7.8 → 3.7,
published/SRS median 1.09 over 30). The 31 row-[D] sample sizes match my transcription exactly; no EU27
member now lacks a bound. No country-level gap, ratio, band, education or standardised value was read.

Five open changes, none blocking, all in `notes/referee-prereg-2.md` with exact fixes. One is for you:
**c128906 edits `posts/gender1/BRIEF.md`, the programme lead's file** — the wording is right, the ownership
is not; ask the lead to re-issue it. The other four are a stale script docstring, four mangled free-text CSV
rows, "2.5 of 26" where H-work's set is 27 (correct figure 2.6 of 27), and the dropped `brief-review.md`
pointer.
