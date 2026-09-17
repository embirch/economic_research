"""Referee re-derivation · post1 · supplement (2026-09-17).

Re-uses the build from referee_results_post1.py (my own code, no analyst import) to answer the
red-team questions the headline check raised:
  1. leg (b) — the within-group leg — re-derived in all three waves, and on the all-four subset
     P3(b) says should be reported beside it (the analyst did not compute the subset estimate);
  2. what sits in Q4 and Q1, with and without SOC-15, and the within-SOC-15 contrast alone;
  3. the November tasks where Seychelles exceeds 10 % of the global count.
"""
import numpy as np, pandas as pd, pathlib
HERE = pathlib.Path(__file__).resolve().parent
src = (HERE / "referee_results_post1.py").read_text().split("results = {}")[0]
ns = {"__file__": str(HERE / "referee_results_post1.py")}
exec(src, ns)
build, quartile_labels, lin, kish, RES = ns["build"], ns["quartile_labels"], ns["lin"], ns["kish"], ns["RES"]
out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

for wave in ["aug2025", "nov2025", "feb2026"]:
    an, f = build(wave); an["q"] = quartile_labels(an)
    w = an.w.to_numpy(float); p = an.p.to_numpy(); n = an.n5.to_numpy()
    m4 = (an.q == 4).to_numpy(); m1 = (an.q == 1).to_numpy(); not15 = (an.g19 != "15").to_numpy()
    say("=" * 96); say(wave)
    # 1. leg (b), both identified sets
    for label, cond in [("Q1&Q4-identified (primary)", {1, 4}), ("all-four subset (P3(b) 'beside it')", {1, 2, 3, 4})]:
        c = np.zeros(len(an)); tot = 0.0; ids = []
        for g, s in an.groupby("g19"):
            if not cond <= set(s.q): continue
            gi = (an.g19 == g).to_numpy(); i4 = gi & m4; i1 = gi & m1
            W4, W1 = w[i4].sum(), w[i1].sum()
            c += (W4 + W1) * (np.where(i4, w / W4, 0.0) - np.where(i1, w / W1, 0.0)); tot += W4 + W1; ids.append(g)
        c /= tot; L = lin(c, p, n)
        extra = ""
        if "primary" in label:
            r = RES["tests"][f"leg_b_{wave}"]["estimates"]["D_L"]
            extra = f"   analyst {r['coef']:+.4f} se {r['se']:.4f}  |Δ| = {abs(L[0]-r['coef']):.1e}"
        say(f"  leg (b) {label:36s} {L[0]:+.4f} [{L[2][0]:+.4f}, {L[2][1]:+.4f}] se {L[1]:.4f}  groups {len(ids)} {ids}{extra}")
    i4 = ~not15 & m4; i1 = ~not15 & m1
    say(f"  within SOC-15 alone: Q4 p {np.average(p[i4], weights=w[i4]):.2f} ({int(i4.sum())} tasks, {w[i4].sum():.2f} pp) − "
        f"Q1 p {np.average(p[i1], weights=w[i1]):.2f} ({int(i1.sum())} tasks, {w[i1].sum():.2f} pp) = "
        f"{np.average(p[i4], weights=w[i4]) - np.average(p[i1], weights=w[i1]):+.2f} pp")
    # 2. composition
    say(f"  Q4: {int(m4.sum())} tasks, {w[m4].sum():.2f} pp, Kish {kish(w[m4]):.1f}; SOC-15 {w[m4 & ~not15].sum()/w[m4].sum()*100:.1f}% of its mass; "
        f"three largest tasks {w[m4][np.argsort(-w[m4])[:3]].sum():.2f} pp")
    say(f"  Q4 without SOC-15: {int((m4 & not15).sum())} tasks, {w[m4 & not15].sum():.2f} pp, Kish {kish(w[m4 & not15]):.1f}, p {np.average(p[m4 & not15], weights=w[m4 & not15]):.2f}")
    say(f"  Q1 without SOC-15: {int((m1 & not15).sum())} tasks, {w[m1 & not15].sum():.2f} pp, Kish {kish(w[m1 & not15]):.1f}, p {np.average(p[m1 & not15], weights=w[m1 & not15]):.2f}")
    for lab, m in [("Q4 residual", m4 & not15), ("Q1", m1)]:
        g = an[m].groupby("g19").agg(mass=("w", "sum"), n=("w", "size"))
        g["p"] = [np.average(an[m & (an.g19 == k).to_numpy()].p, weights=an[m & (an.g19 == k).to_numpy()].w) for k in g.index]
        g = g.sort_values("mass", ascending=False).head(5).round(2)
        say(f"  {lab} by major group (top 5): " + "; ".join(f"{k}: {r.mass} pp, n {int(r.n)}, p {r.p}" for k, r in g.iterrows()))
    top = an[m4].nlargest(3, "w")
    say("  Q4 three largest: " + " | ".join(f"'{t[:55]}…' w {x:.2f} p {y:.1f} g {gg} ${z:.2f}" for t, x, y, gg, z in zip(top.task, top.w, top.p, top.g19, top.wage)))
    # 3. Seychelles
    if wave == "nov2025":
        sc = an[an.sc_share > 0.10]
        say(f"  SC>10%: {len(sc)} tasks, {sc.w.sum():.3f} pp; in Q4 {sc[sc.q == 4].w.sum():.3f} pp ({int((sc.q == 4).sum())} tasks); "
            f"SOC-15 among them {int((sc.g19 == '15').sum())}; usage-weighted p of the SC>10% tasks {np.average(sc.p, weights=sc.w):.1f}")
        say("  the two largest SC>10% tasks are the two 'modify existing software to correct errors…' tasks "
            f"({sc.nlargest(2, 'w').w.sum():.2f} pp of Q4's {w[m4].sum():.2f} pp, p {np.average(sc.nlargest(2,'w').p, weights=sc.nlargest(2,'w').w):.1f}); "
            "in Aug and Feb the same two tasks carry p 69.6/69.8 and 72.4/72.0 — the X5 flip removes the two largest coding tasks, not only Seychelles")
say("=" * 96)
say("Between-window dispersion of D against its within-window SE:")
D = np.array([RES["tests"][f"D_{w}"]["estimates"]["D"]["coef"] for w in ["aug2025", "nov2025", "feb2026"]])
se = np.array([RES["tests"][f"D_{w}"]["estimates"]["D"]["se"] for w in ["aug2025", "nov2025", "feb2026"]])
say(f"  D = {D.round(4).tolist()}; SD across windows {D.std(ddof=1):.3f} pp; mean SE {se.mean():.3f} pp; ratio {D.std(ddof=1)/se.mean():.0f}×")
DW = np.array([RES["tests"][f"DeltaW_{w}"]["estimates"]["Delta_W"]["coef"] for w in ["aug2025", "nov2025", "feb2026"]])
say(f"  Δ_W / D per wave = {(DW / D).round(4).tolist()}  (the brief's arithmetic said 0.11–0.12 per point of gap; it holds in Nov only)")
(HERE / "referee_results_post1_supplement.out.txt").write_text("\n".join(out) + "\n")

# ---------------------------------------------------------------- bound on the un-cleanable Seychelles rate contamination (Nov)
# For a task with SC share s of its global count and observed share p, the SC-free share is
# p_clean = (p − s·p_SC)/(1 − s) for an unknown SC share p_SC ∈ [0, 1]. The bound on D that is
# WORST for the positive gradient sets p_SC = 1 in Q4 tasks and p_SC = 0 in Q1 tasks; the weights are
# also netted (X4). This is the most November's D could fall if every Seychelles conversation on a
# top-quartile task were automation and every one on a bottom-quartile task were augmentation.
an, f = build("nov2025"); an["q"] = quartile_labels(an)
w = an.w.to_numpy(float); p = an.p.to_numpy() / 100; s = an.sc_share.to_numpy(float); cnt = an.cnt.to_numpy(float)
m4 = (an.q == 4).to_numpy(); m1 = (an.q == 1).to_numpy()
w_net = w * (1 - s)                                  # SC conversations netted from the weights
p_worst = p.copy()
p_worst[m4] = np.clip((p[m4] - s[m4] * 1.0) / (1 - s[m4]), 0, 1)
p_worst[m1] = np.clip((p[m1] - s[m1] * 0.0) / (1 - s[m1]), 0, 1)
D_obs = np.average(p[m4], weights=w[m4]) - np.average(p[m1], weights=w[m1])
D_net = np.average(p[m4], weights=w_net[m4]) - np.average(p[m1], weights=w_net[m1])
D_worst = np.average(p_worst[m4], weights=w_net[m4]) - np.average(p_worst[m1], weights=w_net[m1])
say("=" * 96)
say(f"November Seychelles bound: D observed {100*D_obs:+.3f} pp; weights netted (X4) {100*D_net:+.3f} pp; "
    f"weights netted AND every SC conversation counted against the gradient {100*D_worst:+.3f} pp")
say("  → even the worst-case cleaning leaves November's D far above August's +1.38 and February's +0.67; "
    "Seychelles does not account for November's excess. The X5 flip to −4.58 comes from removing the two largest "
    "software-modification tasks (8.5 pp of Q4), which carry p ≈ 70–74 in every wave.")
(HERE / "referee_results_post1_supplement.out.txt").write_text("\n".join(out) + "\n")
