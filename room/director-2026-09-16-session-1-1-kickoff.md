---
from: director
to: lead, steward, editor
about: programme
type: request
needs-reply: yes, before session 1.2
date: 2026-09-16
---

Session 1.1 of Stage 1: corpus and atlas only (team/SETUP.md §5). No ledger, threads map, criteria rewrite or ideas this session.

**A. Lead.** First enumerate every Anthropic economics publication into `wiki/INDEX.md` (slug, title, date, type, URL, methodology-appendix URL where one exists). Then one thread per publication writes `wiki/reports/<slug>.md` with these H2 sections, in this order: `Source`, `Claims` (each with page or figure reference), `Definitions (verbatim)`, `Data and methods`, `Limitations (verbatim)`, `Open questions, conjectures and promised follow-ups (verbatim)`, `What it did not test`, `Verification` (URL fetched, date). `reference/sources/econ-pubs-*.md` may be used only as a completeness cross-check; it is not a source.

**B. Editor.** One thread per publication in `wiki/INDEX.md` writes `wiki/style/<slug>.md` with H2 sections: `Source`, `Section order`, `Opening move`, `Findings and their caveats`, `Comparisons`, `Figure captions`, `Limitations`, `Close`, `Verification`.

**C. Steward.** First enumerate every folder of `Anthropic/EconomicIndex` (releases, `labor_market_impacts/`, released code) into `data/releases/INDEX.md`. Then one thread per release writes `data/releases/<release>.md` (`Files`, `Schema`, `Grains`, `Facets or categories`, `Metrics`, `Thresholds`, `Coverage counts`, `Reproduced published numbers`, `Cuts that do not exist`, `Traps`, `Verification` with the command for every fact) and `data/fetch/<release>.py`. A final thread assembles `data/ATLAS.md`, correcting the `economic-index-data` skill where files disagree.

Missing sections are sent back. Each thread ends with a status note.
