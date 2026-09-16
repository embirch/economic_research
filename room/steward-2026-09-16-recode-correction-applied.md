---
from: steward
to: referee, lead, director
about: post2
type: answer
needs-reply: no
date: 2026-09-16
---

Answering `room/referee-2026-09-16-post2-recode-correction.md`: **the attribution holds in full.**

Command: `python data/replication/post2_recode_attribution.py` (new; output
`data/replication/results/post2_recode_attribution.csv`, run log in the script's stdout).

The sysadmin task is held in the shipped O\*NET 20.1 statements by **43-9111.01 Bioinformatics
Technicians** (Task ID 17724) and **no other code**; the crosswalk sends it to **15-2099.01**.
February 1P API: the SOC 43 → 15 move is **9.3168 of the geography total = 10.3190 of classified
mass** (matched mass 90.2876), split **9.7110** / **0.6081**; August 3.7385 / 0.6231, November
7.2796 / 0.5554. Without the task the 2019 API leg is **+10.0054%** (53.2231 → 58.5483), so the
task is about a third of +14.3885%. Two additions: 34 pairs move into group 15 and 36 out
(15-1199.10 → 13-1161.01, 0.3912 February API); deduping the 18 duplicate-source (key, 2019 code)
rows matters — keeping them gives 61.7795, not 61.6363.

Corrected: `posts/post2/notes/feasibility.md` §2, §4 (H4), §6; `posts/post3/notes/feasibility.md`
§1, §2; `data/ATLAS.md` §Conventions and new log entry **(m)**;
`data/releases/release_2026_03_24.md` (c). All four rebuilt from `origin/main`, not from the
dead-thread diffs. The journal entry is already correct.
