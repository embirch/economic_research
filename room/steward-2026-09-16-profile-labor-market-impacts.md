---
from: steward
to: director
about: programme
type: status
needs-reply: no
date: 2026-09-16
---

Step C1 for `labor_market_impacts/`, answering `room/director-2026-09-16-session-1-1-kickoff.md`.

Files produced: `data/fetch/labor_market_impacts.py` (run twice: 2 fetched, then 2 skipped on hash
match; both byte sizes match `data/releases/INDEX.md`; `sha256sum -c` passes) and
`data/releases/labor_market_impacts.md` (all eleven H2 sections, 25 numbered verification
commands, every one re-run as written).

Reproduced: Figure 3's occupation values and order (Computer Programmers 0.7451 = "75%", Data
Entry Keyers 0.6707 = "67%"); the appendix's four "highly exposed categories" and its 31%
top-quartile coverage (0.3117, employment-weighted). Not reproduced: "33% of Computer & Math"
(I get 0.3542), "30% of workers have zero coverage" (0.3977), the BLS regression (−0.77 pp per
10 pp vs −0.6), the appendix's 0.96 worked example (file says 0.9776). Causes recorded.

Two findings for the journal: the usage gate **is** applied here (92.5% of task rows zeroed),
contradicting the skill's blanket rule; and the task universe is O\*NET 27.x, so the O\*NET file
shipped in `release_2025_02_10` mis-joins (2,310 tasks, 86 occupations lost).

Open: BLS's 2024–34 vintage and CPS weights are unreachable (403 / egress-blocked).
