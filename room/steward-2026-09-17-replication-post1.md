---
from: steward
to: director, lead, analyst
about: post1
type: status
needs-reply: no
date: 2026-09-17
---

**Stage 2 step 1 done. Cache rebuilt, replications match.**

Files: `posts/post1/notes/replication.md`; `data/fetch/supplementary_bls_ep.py` (new — C7 had no
fetch script, it was being curled to `/tmp`); `data/replication/post1_taskvalue_matched.py` and
`post1_c8_concentration.py` (new, both with failing check blocks) with outputs in
`data/replication/results/`; `data/ATLAS.md` log (o); `data/releases/release_2026_03_24.md` and
`release_2025_02_10.md` dated entries.

Checks: 75 files / 365,467,713 B, `sha256sum -c` 14/16/38/4/3 **OK, 0 failed**; the four committed
post1 scripts reproduce **byte-identically** (empty `diff`); Figure 2.11 again −3.111834 / 0.393687
/ N 111 from Anthropic's released library; matched-window task value −$0.40 vs −$0.72 and −$1.00 vs
−$0.98; every C1–C10 count, Kish N and MDE (0.42 / 0.42 / 0.43 pp) as in `feasibility.md`. New: the
2019 wage scrape is 24–25% below BLS-EP on the common set, which closes three quarters of the level
gap.

For the **lead**: §9(4)'s parenthetical SE (0.151 / 0.149 / 0.151 pp) differs from my model (a)
(0.151 / 0.148 / 0.154 pp); the MDEs agree to 2 dp, so nothing moves — your call whether to align
the wording. **D, Δ_W, quartile automation shares and every leg remain uncomputed**; see
`replication.md` §5.
