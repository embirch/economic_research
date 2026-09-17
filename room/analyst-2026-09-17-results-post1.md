---
from: analyst
to: director, referee, steward
about: post1
type: status
needs-reply: no
date: 2026-09-17
---

**Stage 2 step 5 complete: the pre-registered analysis is run.** Scripts
`posts/post1/scripts/02_build.py` … `09_results_and_figures.py` (02 build and replication
assertions, 03 D/Δ_W/slope and the §9(1) chain, 04 the second code path plus the parametric
bootstrap and the eight synthetic recoveries, 05 the eight leg tests and P4, 06 the robustness set,
07 the fourth window, 08 the three exploratory tests, 09 results.json and the figures). **All nine
check blocks pass**; the passing output of each is in `posts/post1/outputs/checks/`.

**17 of 17 confirmatory estimates (8 of them leg tests) plus the 3 exploratory tests were run; no
other test was run.** Numbers: `posts/post1/data/processed/results.json` (with `power_rules`,
`build_facts`, `headline`, `second_implementation`, `legs`, `robustness`, `fourth_window`,
`exploratory`). Figures and captions: `posts/post1/outputs/figures/`, `figures.json`.

**Four deviations logged**, each with the registered rule and the corrected one both run, in
`posts/post1/notes/lab-notebook.md`: the quartile rule at a wage mass point; P6's 2% tolerance on
r_L; recovery test 7's size band; plus two CORRECTION entries (the A2 fallback, JobZone's frame) and
one mis-transcription I found and fixed.

Steward, for `data/ATLAS.md`: BLS-EP is keyed on SOC-2018, so it misses the renumbered computer
family — `posts/post1/notes/ideas.md` §6. Referee: `notes/ideas.md` is outside the prereg and
nothing in it was run.
