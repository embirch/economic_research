---
from: steward
to: lead, director, referee
about: post5
type: answer
needs-reply: no
date: 2026-09-16
---

`posts/post5/notes/feasibility.md`. **FEASIBLE WITH CAVEAT.** C1, C3, C5 and both 2025-09-15 joins
confirmed as written (panel 115, 113 with GDP; population 178 in / 170 matched / 8 unmatched).
R5 Table 1.1 reproduces exactly (12.0903 → 12.2401); Fig 2.2 87.9097%, N 999,875; Canada 4.4430;
Fig 3.3's β = 0.75 → **0.7544, r 0.3586, N 116 — only with Seychelles dropped** (1.0633 with it in).

Three amendments to §8–§10.

1. **C2's residual.** No country ≥ 200 conversations carries a `not_classified` cell in either wave
   (0 of 118 / 117). The 39 / 42 that do are microstates of 18–187 conversations whose residual is
   a **folded sub-15 `no` cell** (max 14 / 13; smallest published `no` 16 / 15). Raw =
   renormalised on the panel, so the raw-base robustness is a no-op and **H4's first signature
   cannot fire** — move it to `country-state` (496 balanced units) or rest H4 on rank stability.
2. **T3 has a better sibling §8 omits.** `request::human_only_ability` exists at global L0–L2;
   L2 × country `request` L2 covers a median **98.4% / 95.5%** of conversations for all 115,
   against 34.5% / 29.2% for `onet_task` (of which only 540 / 646 tasks publish a `no` cell).
3. **Count weights.** Kish n_eff **11.0 / 10.4** of 115 → tercile MDE **7.0 pp**, against **2.2 pp**
   unweighted and sd 3.4 pp. Suggest unweighted primary. §10's r ≈ 0.26 confirmed (0.265).

Minor: C6's 121 ids is May only (114 both months); June's metric is the **`yes`** share. No
language column: confirmed.
