"""post1 · 08 · The three exploratory tests the brief §9 names, run after the confirmatory set and
labelled exploratory everywhere.

WHAT, and the exact wording that authorises each (prereg "Exploratory allowance — three tests, after
the confirmatory set, none in the headline, each labelled exploratory"; BRIEF §9):

  (a) **the same gradient on the 1P API global intersection** — "to say whether the sign is a
      property of the surface rather than of the work — the API is automation-dominant and its
      February sample includes Claude Code, which moves its automation share by construction, so
      this is context, not a replication". The February file's intersection has 11,660 rows at
      global, which the check block asserts. The construction is the confirmatory one: the same
      analysis-set rule, the same wage join and wage rule, the quartiles drawn on the API wave's own
      usage-weighted wage, the same conversation-level variance model.
  (b) **the pattern-level split** — which of `directive` and `feedback loop` carries a positive
      gradient, and whether `learning`, `task iteration` and `validation` move the other way. Each
      of the five patterns' Q4−Q1 difference with its own interval and MDE; the five differences sum
      to zero by construction, which the check block asserts.
  (c) **the gradient against `JobZone`** — a non-wage ordering separating price from required
      preparation, with the `-1` sentinel occupations dropped. Reported as the usage-weighted slope
      of the automation share per +1 Job Zone and as the top-minus-bottom Job-Zone difference, with
      the automation share by Job Zone beside them.

WHY THEY ARE SEPARATE. They are **in no decision rule**, they cannot declare or refute an owner, and
none of them may appear in a headline. They are stored in `results.json` under `exploratory: true`.
No further cut is run: any additional one would be a logged deviation.

OUTPUT. `posts/post1/data/processed/exploratory.json` and a console log.
"""

from __future__ import annotations

import importlib.util
import json
import pathlib

import numpy as np
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).resolve().parent
PROCESSED = ROOT / "posts/post1/data/processed"

Z = 1.959964
MDE_K = 2.8


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


B = _load("02_build")
H = _load("03_headline")
WAVES = B.WAVE_ORDER
AUTO, AUGM, CLASSIFIED, PATTERNS = B.AUTO, B.AUGM, B.CLASSIFIED, B.PATTERNS


# ---------------------------------------------------------------- (a) the 1P API surface
def api_analysis_set(wave: str) -> tuple[pd.DataFrame, dict]:
    """The confirmatory construction applied to the 1P API frame of the same release."""
    holders, _ = B.holder_tables()
    c6, jz, c7, emp, _, _ = B.wage_tables()
    df = B.load_frame(B.WAVES[wave]["api"])
    g = df[df.geography == "global"]
    audit = dict(rows_global=int(len(g)),
                 geographies=sorted(df.geography.unique()))
    ix = g[g.facet == "onet_task::collaboration"].copy()
    audit["intersection_rows_global"] = int(len(ix))
    if not len(ix):
        return pd.DataFrame(), audit
    ix["task"], ix["pattern"] = B.split_cluster(ix.cluster_name)
    ixn = ix[(~ix.task.isin(B.RESID)) & ix.variable.str.endswith("_count")]
    tab = ixn.pivot_table(index="task", columns="pattern", values="value",
                          aggfunc="sum").reindex(columns=PATTERNS).fillna(0.0)
    base = g[(g.facet == "onet_task") & (g.variable == "onet_task_pct")]
    w = base[~base.cluster_name.isin(B.RESID)].set_index("cluster_name").value
    audit["named_nodes"] = int(len(w))
    audit["named_mass"] = float(w.sum())
    t = pd.DataFrame(dict(task=w.index, w=w.values))
    t["key"] = t.task.str.lower().str.strip()
    t = t[t.key.isin(holders.index)].copy()
    t["holders"] = [holders[k] for k in t.key]
    t["wage"] = [B.wage_under_rules(hs, c6, emp, False)[0] for hs in t.holders]
    t["n5"] = tab[CLASSIFIED].sum(1).reindex(t.task).fillna(0.0).values
    t["p"] = np.where(t.n5 > 0, tab[AUTO].sum(1).reindex(t.task).fillna(0.0).values / t.n5 * 100, np.nan)
    for pat in PATTERNS:
        t["c_" + pat] = tab[pat].reindex(t.task).fillna(0.0).values
    t = t[(t.n5 > 0) & t.wage.notna()].reset_index(drop=True)
    audit["analysis_tasks"] = int(len(t))
    audit["analysis_mass"] = float(t.w.sum())
    audit["analysis_share_named"] = float(t.w.sum() / audit["named_mass"] * 100)
    audit["classified_conversations"] = float(t.n5.sum())
    audit["wave_automation_share_five_pattern"] = float(
        t[["c_" + p for p in AUTO]].sum().sum() / t.n5.sum() * 100)
    return t, audit


def main():
    out: dict = dict(script="posts/post1/scripts/08_exploratory.py",
                     prereg="posts/post1/prereg/prereg.md content c9b1b45",
                     exploratory=True,
                     note=("three tests, after the confirmatory set, none in the headline, each "
                           "labelled exploratory; in no decision rule"),
                     a_api={}, b_pattern_split={}, c_jobzone={})

    print("=" * 96)
    print("EXPLORATORY (a) · the same gradient on the 1P API global intersection")
    print("  context, not a replication: the API is automation-dominant and its February sample")
    print("  includes Claude Code, which moves its automation share by construction")
    for wave in WAVES:
        t, audit = api_analysis_set(wave)
        if not len(t):
            out["a_api"][wave] = dict(audit=audit, available=False)
            print(f"  [{wave}] no API intersection at global: {audit}")
            continue
        qw = B.quartile_weights(t, "wage", "registered")
        d, _ = H.d_stat(t, qw)
        dw, _ = H.delta_w(t)
        sl, _ = H.slope(t)
        shares = {f"Q{k+1}": H.quartile_share(t, qw, k) for k in range(4)}
        out["a_api"][wave] = dict(audit=audit, available=True, D=d, Delta_W=dw, slope=sl,
                                  quartile_shares=shares,
                                  bounds=[float(b) for b in B.quartiles(t, "wage")[1]],
                                  kish=B.kish(t.w.values))
        print(f"  [{wave}] API analysis set {audit['analysis_tasks']} tasks "
              f"({audit['analysis_share_named']:.2f}% of named mass, "
              f"{audit['classified_conversations']:,.0f} classified conversations); wave automation "
              f"share {audit['wave_automation_share_five_pattern']:.4f}%")
        print(f"          D {d['coef']:+.4f} [{d['ci'][0]:+.4f}, {d['ci'][1]:+.4f}] MDE {d['mde']:.4f}"
              f"   Δ_W {dw['coef']:+.4f}   slope per +$10/hr {sl['coef']:+.4f}"
              f" [{sl['ci'][0]:+.4f}, {sl['ci'][1]:+.4f}]")

    print("\n" + "=" * 96)
    print("EXPLORATORY (b) · the pattern-level split: which pattern carries the gradient")
    for wave in WAVES:
        an = B.analysis_set(wave)
        qw = B.quartile_weights(an, "wage", "registered")
        row = {}
        for pat in CLASSIFIED:
            with np.errstate(invalid="ignore", divide="ignore"):
                rate = np.where(an.n5 > 0, an["c_" + pat] / an.n5 * 100, np.nan)
            sub = an.assign(rate=rate)
            c = H.quartile_coefficients(qw, 3) - H.quartile_coefficients(qw, 0)
            e = H.linear_stat(c, sub.rate.to_numpy(), sub.n5.to_numpy())
            row[pat] = e
        row["sum_of_five_differences"] = float(sum(row[p]["coef"] for p in CLASSIFIED))
        row["automation_patterns_positive"] = [p for p in AUTO if row[p]["coef"] > 0]
        row["augmentation_patterns_negative"] = [p for p in AUGM if row[p]["coef"] < 0]
        out["b_pattern_split"][wave] = row
        print(f"  [{wave}]  " + "  ".join(
            f"{p}: {row[p]['coef']:+.3f} [{row[p]['ci'][0]:+.3f}, {row[p]['ci'][1]:+.3f}]"
            for p in CLASSIFIED))
        print(f"          the five Q4−Q1 differences sum to {row['sum_of_five_differences']:.2e} "
              f"(they must, by construction); automation patterns with a positive gradient: "
              f"{row['automation_patterns_positive']}; augmentation patterns negative: "
              f"{row['augmentation_patterns_negative']}")

    print("\n" + "=" * 96)
    print("EXPLORATORY (c) · the gradient against `JobZone` (the `-1` sentinel occupations dropped)")
    facts = json.loads((PROCESSED / "build_facts.json").read_text())["waves"]
    for wave in WAVES:
        an = B.analysis_set(wave)
        sub = an[an.jobzone.notna()].copy()
        cover = float(sub.w.sum() / an.w.sum() * 100)
        cover_named = float(sub.w.sum() / facts[wave]["named_mass"] * 100)
        sl, _ = H.slope(sub, x_col="jobzone", per=1.0)
        qw = B.quartile_weights(sub, "jobzone", "registered")
        d, _ = H.d_stat(sub, qw)
        by_zone = {}
        for zone in sorted(set(np.round(sub.jobzone).astype(int))):
            m = (np.round(sub.jobzone).astype(int) == zone).to_numpy()
            c = np.where(m, sub.w.to_numpy(), 0.0)
            c = c / c.sum()
            e = H.linear_stat(c, sub.p.to_numpy(), sub.n5.to_numpy())
            by_zone[int(zone)] = dict(share=e["coef"], ci=e["ci"], mde=e["mde"],
                                      tasks=int(m.sum()), mass=float(sub.w.to_numpy()[m].sum()))
        out["c_jobzone"][wave] = dict(
            coverage_share_of_analysis_mass=cover,
            coverage_share_of_named_mass_of_the_analysis_set=cover_named,
            # the pre-registration's 99.22 / 98.83 / 99.06% is Job-Zone coverage over ALL named
            # tasks, which script 02 computes; both denominators are carried, as §10 requires
            jobzone_coverage_of_all_named_mass=facts[wave]["jobzone_share_named"],
            tasks=int(len(sub)), slope_per_jobzone=sl, D_top_minus_bottom_jobzone_quartile=d,
            automation_share_by_jobzone=by_zone,
            jobzone_sentinel_occupations=facts[wave]["c6_audit"]["jobzone_sentinels"])
        print(f"  [{wave}] {len(sub)} tasks, {cover:.2f}% of analysis mass ({cover_named:.2f}% of "
              f"named mass); {facts[wave]['c6_audit']['jobzone_sentinels']} occupations carry the "
              f"`-1` sentinel and are dropped")
        print(f"          slope per +1 Job Zone {sl['coef']:+.4f} [{sl['ci'][0]:+.4f}, "
              f"{sl['ci'][1]:+.4f}] MDE {sl['mde']:.4f};  top-minus-bottom Job-Zone quartile "
              f"{d['coef']:+.4f} [{d['ci'][0]:+.4f}, {d['ci'][1]:+.4f}]")
        print("          automation share by Job Zone: " + ", ".join(
            f"{z}: {v['share']:.2f} ({v['tasks']} tasks)" for z, v in by_zone.items()))

    PROCESSED.mkdir(parents=True, exist_ok=True)
    (PROCESSED / "exploratory.json").write_text(json.dumps(out, indent=2, default=float) + "\n")
    print(f"\nwrote {(PROCESSED / 'exploratory.json').relative_to(ROOT)}")
    return out


if __name__ == "__main__":
    O = main()

    # ------------------------------------------------------------ check block
    # exactly three exploratory tests, and every one labelled exploratory
    assert set(k for k in O if k in ("a_api", "b_pattern_split", "c_jobzone")) == \
        {"a_api", "b_pattern_split", "c_jobzone"}
    assert O["exploratory"] is True

    # (a) the API frame: the February intersection has the 11,660 rows at global the brief records,
    # the API is automation-dominant (its wave share exceeds Claude.ai's), and every estimate carries
    # an interval and an MDE
    assert O["a_api"]["feb2026"]["audit"]["intersection_rows_global"] == 11660, \
        O["a_api"]["feb2026"]["audit"]["intersection_rows_global"]
    head = json.loads((PROCESSED / "headline.json").read_text())["results"]
    for wave in WAVES:
        r = O["a_api"][wave]
        if not r["available"]:
            continue
        assert r["audit"]["geographies"] == ["global"], (wave, r["audit"]["geographies"])
        assert r["audit"]["analysis_tasks"] > 100, wave
        assert abs(r["D"]["mde"] - MDE_K * r["D"]["se"]) < 1e-12, wave
        assert r["D"]["ci"][0] < r["D"]["coef"] < r["D"]["ci"][1], wave
        # automation-dominant surface: the API's own five-pattern share is above Claude.ai's
        assert r["audit"]["wave_automation_share_five_pattern"] > \
            {"aug2025": 51.0698, "nov2025": 46.7394, "feb2026": 45.5456}[wave], \
            (wave, r["audit"]["wave_automation_share_five_pattern"])

    # (b) the five pattern differences sum to zero by construction, and directive + feedback loop
    # reproduces the confirmatory D exactly
    for wave in WAVES:
        r = O["b_pattern_split"][wave]
        assert abs(r["sum_of_five_differences"]) < 1e-9, (wave, r["sum_of_five_differences"])
        auto_sum = r["directive"]["coef"] + r["feedback loop"]["coef"]
        assert abs(auto_sum - head[wave]["registered"]["D"]["coef"]) < 1e-9, (wave, auto_sum)
        for pat in CLASSIFIED:
            assert abs(r[pat]["mde"] - MDE_K * r[pat]["se"]) < 1e-12, (wave, pat)

    # (c) JobZone: the sentinels are dropped, the coverage is the recorded one, and the ordering is
    # a non-wage one (Job Zones run 1-5)
    for wave in WAVES:
        r = O["c_jobzone"][wave]
        assert r["jobzone_sentinel_occupations"] == 119, (wave, r["jobzone_sentinel_occupations"])
        assert r["coverage_share_of_analysis_mass"] > 99.5, (wave, r["coverage_share_of_analysis_mass"])
        assert abs(r["jobzone_coverage_of_all_named_mass"]
                   - {"aug2025": 99.22, "nov2025": 98.83, "feb2026": 99.06}[wave]) < 0.05, \
            (wave, r["jobzone_coverage_of_all_named_mass"])
        assert set(r["automation_share_by_jobzone"]).issubset({1, 2, 3, 4, 5}), wave
        assert abs(r["slope_per_jobzone"]["mde"] - MDE_K * r["slope_per_jobzone"]["se"]) < 1e-12, wave
        for z, v in r["automation_share_by_jobzone"].items():
            assert 0.0 <= v["share"] <= 100.0, (wave, z)

    print("\nCHECK BLOCK PASSED — 08_exploratory.py")
