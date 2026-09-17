"""Referee, post1 (LL-07), brief stage — independent re-derivation of the steward numbers the
brief carries, plus the facts the assumptions sweep needs. Written from the raw files with
no reference to the steward's scripts. NO quartile automation share is computed: the
headline statistic stays unseen at the brief stage.

Run from the repository root:  python posts/post1/notes/rederivation/referee_brief_post1.py
"""
import sys
import numpy as np
import pandas as pd

ROOT = "data/cache"
WAVES = {
    "aug2025": (f"{ROOT}/release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv", "csv"),
    "nov2025": (f"{ROOT}/release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.parquet", "pq"),
    "feb2026": (f"{ROOT}/release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.parquet", "pq"),
}
AUTO = ["directive", "feedback loop"]
AUG = ["learning", "task iteration", "validation"]
FIVE = AUTO + AUG
RESID_NODES = {"none", "not_classified"}

out = []
def say(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.append(s)

def load(path, kind):
    if kind == "csv":
        df = pd.read_csv(path, keep_default_na=False, na_values=[], dtype=str)
        df["value"] = df["value"].astype(float)
    else:
        df = pd.read_parquet(path)
        for c in df.columns:
            if c != "value":
                df[c] = df[c].astype(str)
        df["value"] = df["value"].astype(float)
    return df

def kish(w):
    w = np.asarray(w, float)
    return w.sum() ** 2 / (w ** 2).sum()

# ---- supplementary files -------------------------------------------------------------------
stm = pd.read_csv(f"{ROOT}/release_2025_09_15/data/intermediate/onet_task_statements.csv",
                  keep_default_na=False, na_values=[], dtype=str)
stm["key"] = stm["Task"].str.lower().str.strip()
say("C5 statements file:", stm.shape, "codes", stm["O*NET-SOC Code"].nunique(),
    "7-char", stm["O*NET-SOC Code"].str[:7].nunique(), "keys", stm["key"].nunique(),
    "max rows/key", stm.groupby("key").size().max())
holders = stm.groupby("key")["O*NET-SOC Code"].apply(lambda s: sorted(set(s)))

wage = pd.read_csv(f"{ROOT}/release_2025_02_10/wage_data.csv", keep_default_na=False, na_values=[])
wage["MedianSalary"] = pd.to_numeric(wage["MedianSalary"], errors="coerce")
say("C6 wage_data:", wage.shape, "SOCcode len", wage["SOCcode"].str.len().unique(),
    "unique", wage["SOCcode"].is_unique)
w100 = wage[wage["MedianSalary"] > 100]
say("C6 MedianSalary>100 keeps", len(w100), "of", len(wage),
    "| removed:", sorted(wage.loc[wage["MedianSalary"] <= 100, "MedianSalary"].tolist()))
codes = set(stm["O*NET-SOC Code"])
say("C6 join full 10-char code:", len(codes & set(w100["SOCcode"])), "of", len(codes))
say("C6 join [:7] prefix:", len({c[:7] for c in codes} & set(w100["SOCcode"])), "of", len({c[:7] for c in codes}))
say("C6 top-code $208,000 occupations:", (w100["MedianSalary"] == 208000).sum(),
    "| JobZone -1:", (w100["JobZone"] == -1).sum(), "| ChanceAuto -1:", (w100["ChanceAuto"] == -1).sum())
wage_by_code = w100.set_index("SOCcode")["MedianSalary"] / 2080.0
jz_by_code = w100.set_index("SOCcode")["JobZone"]

xw = pd.read_csv(f"{ROOT}/supplementary/onet_soc_2019_crosswalk/2010_to_2019_onet_soc_crosswalk.csv",
                 keep_default_na=False, na_values=[], dtype=str)
xw_map = xw.groupby("O*NET-SOC 2010 Code")["O*NET-SOC 2019 Code"].apply(lambda s: sorted(set(s)))
say("Crosswalk 2010->2019:", xw.shape, "2010 codes", xw["O*NET-SOC 2010 Code"].nunique(),
    "one-to-many 2010 codes:", int((xw_map.apply(len) > 1).sum()))

# major-group employment (only employment file shipped with the wage file)
emp = pd.read_csv(f"{ROOT}/release_2025_02_10/bls_employment_may_2023.csv", keep_default_na=False, na_values=[])
soc_struct = pd.read_csv(f"{ROOT}/release_2025_09_15/data/intermediate/soc_structure.csv",
                         keep_default_na=False, na_values=[], dtype=str)
mg = soc_struct[soc_struct["Major Group"] != ""][["Major Group", "SOC or O*NET-SOC 2019 Title"]] \
    if "Major Group" in soc_struct.columns else None
if mg is not None:
    mg = mg.rename(columns={"Major Group": "mg", "SOC or O*NET-SOC 2019 Title": "title"})
    mg["mg2"] = mg["mg"].str[:2]
    emp = emp.rename(columns={"SOC or O*NET-SOC 2019 Title": "title"}).merge(mg[["mg2", "title"]], on="title", how="left")
    emp_by_mg = emp.dropna(subset=["mg2"]).set_index("mg2")["bls_distribution"].astype(float)
    say("BLS May-2023 major-group employment joined:", emp_by_mg.shape[0], "of 22 groups")
    # US occupation-wage distribution on the same wage file: each occupation weighted by its major
    # group's employment divided by the number of priced occupations in the group (crude, stated).
    wd = w100.copy(); wd["mg2"] = wd["SOCcode"].str[:2]
    wd["emp_w"] = wd["mg2"].map(emp_by_mg) / wd.groupby("mg2")["SOCcode"].transform("count")
    wd = wd.dropna(subset=["emp_w"]); wd["hr"] = wd["MedianSalary"] / 2080
    def wquantile(x, w, q):
        o = np.argsort(x); cx = np.cumsum(np.asarray(w)[o]) / np.sum(w)
        return np.asarray(x)[o][np.searchsorted(cx, q)]
    us_med = wquantile(wd["hr"].values, wd["emp_w"].values, 0.5)
    say(f"US occupation wage on wage_data.csv, group-employment-weighted median ≈ ${us_med:.2f}/hr "
        f"(unweighted median over {len(w100)} occupations ${w100['MedianSalary'].median()/2080:.2f}/hr)")

# ---- per wave ------------------------------------------------------------------------------
summary = {}
for wv, (path, kind) in WAVES.items():
    df = load(path, kind)
    g = df[df["geography"] == "global"]
    say(f"\n===== {wv} ===== rows {len(df):,} | platform {sorted(df['platform_and_product'].unique())}")

    # C1-C3 intersection
    ix = g[g["facet"] == "onet_task::collaboration"].copy()
    parts = ix["cluster_name"].str.rsplit("::", n=1)
    ix["task"] = parts.str[0]; ix["pattern"] = parts.str[1]
    cnt = ix[ix["variable"].str.endswith("_count")]
    pct = ix[ix["variable"].str.endswith("_pct")]
    non_global_ix = (df["facet"] == "onet_task::collaboration").sum() - len(ix)
    say("intersection rows", len(ix), "| level", sorted(ix["level"].unique()), "| tasks", ix["task"].nunique(),
        "| named", ix.loc[~ix["task"].isin(RESID_NODES), "task"].nunique(),
        "| patterns", sorted(ix["pattern"].unique()), "| min _count", cnt["value"].min(),
        "| non-global intersection rows", non_global_ix)
    pct_sum = pct.groupby("task")["value"].sum()
    say("per-task _pct sum min/median/max", round(pct_sum.min(), 4), round(pct_sum.median(), 4), round(pct_sum.max(), 4))
    C = cnt.pivot_table(index="task", columns="pattern", values="value", aggfunc="sum").fillna(0.0)
    for p in FIVE + ["none", "not_classified"]:
        if p not in C: C[p] = 0.0
    named = C[~C.index.isin(RESID_NODES)]
    tot_named = named.sum().sum()
    say("named intersection counts", f"{tot_named:,.0f}",
        "| classified %", round(100 * named[FIVE].sum().sum() / tot_named, 2),
        "| none %", round(100 * named["none"].sum() / tot_named, 2),
        "| not_classified %", round(100 * named["not_classified"].sum() / tot_named, 2))

    # wave-level collaboration facet: two bases
    col = g[(g["facet"] == "collaboration") & (g["variable"] == "collaboration_count")].set_index("cluster_name")["value"]
    all_base = 100 * col[AUTO].sum() / col.sum()
    five_base = 100 * col[AUTO].sum() / col[FIVE].sum()
    say("wave automation: all-conversation base", round(all_base, 4), "| five-classified base", round(five_base, 4),
        "| not_classified in marginal facet", col.get("not_classified", 0.0))

    # C4 base facet weights
    bt = g[g["facet"] == "onet_task"]
    wpct = bt[bt["variable"] == "onet_task_pct"].set_index("cluster_name")["value"]
    wcnt = bt[bt["variable"] == "onet_task_count"].set_index("cluster_name")["value"]
    named_w = wpct[~wpct.index.isin(RESID_NODES)]
    say("onet_task nodes", len(wpct), "| named", len(named_w), "| pct sum", round(wpct.sum(), 6),
        "| min count", wcnt.min(), "| none mass", round(wpct.get("none", 0), 4),
        "| not_classified mass", round(wpct.get("not_classified", 0), 4), "| named mass", round(named_w.sum(), 4),
        "| named conversations", f"{wcnt[~wcnt.index.isin(RESID_NODES)].sum():,.0f}")
    say("base-facet task set minus intersection task set:", sorted(set(wpct.index) - set(C.index)),
        "| intersection minus base:", sorted(set(C.index) - set(wpct.index)))
    say("intersection publishes % of base named counts:",
        round(100 * tot_named / wcnt[~wcnt.index.isin(RESID_NODES)].sum(), 2))
    say("Kish N on onet_task_pct, named nodes:", round(kish(named_w.values), 1), "of", len(named_w))

    # internal check (ii): usage-weighted mean of per-task five-pattern automation, named tasks with a classified cell
    named_cls = named[named[FIVE].sum(axis=1) > 0]
    a_task = 100 * named_cls[AUTO].sum(axis=1) / named_cls[FIVE].sum(axis=1)
    w_task = named_w.reindex(a_task.index)
    wmean = np.average(a_task, weights=w_task)
    say("internal check: usage-weighted mean per-task automation", round(wmean, 4),
        "| minus wave five-pattern value", round(wmean - five_base, 4))

    # C5 join
    tasks = pd.DataFrame({"task": named_w.index, "w": named_w.values})
    tasks["key"] = tasks["task"].str.lower().str.strip()
    tasks["holders"] = tasks["key"].map(holders)
    unmatched = tasks["holders"].isna().sum()
    tasks = tasks.dropna(subset=["holders"])
    tasks["n10"] = tasks["holders"].apply(len)
    tasks["n7"] = tasks["holders"].apply(lambda h: len({c[:7] for c in h}))
    tasks["nmg"] = tasks["holders"].apply(lambda h: len({c[:2] for c in h}))
    collisions = tasks.groupby("key")["task"].nunique().gt(1).sum()
    multi = tasks[tasks["n10"] > 1]
    say("C5 join: named in", len(named_w), "| matched", len(tasks), "| unmatched", unmatched, "| key collisions", collisions)
    say("multi-holder tasks: 10-char", len(multi), "| 7-char", (tasks["n7"] > 1).sum(), "| span >1 major group", (tasks["nmg"] > 1).sum(),
        "| multi mass pp of wave", round(multi["w"].sum(), 2), "| % of named mass", round(100 * multi["w"].sum() / named_w.sum(), 2))

    # 2019 recode: duplicate (task key, 2019 code) source rows
    rec = tasks[["key", "holders"]].explode("holders").rename(columns={"holders": "c2010"})
    rec["c2019"] = rec["c2010"].map(xw_map)
    unmapped = rec["c2019"].isna().sum()
    rec = rec.dropna(subset=["c2019"]).explode("c2019")
    dup = rec.duplicated(subset=["key", "c2019"]).sum()
    say("2019 recode of this wave's holder rows:", len(rec), "rows | 2010 codes without a crosswalk row", unmapped,
        "| duplicate (task key, 2019 code) rows", int(dup),
        "| tasks whose 2019 group set differs from 2010 group set",
        int((rec.groupby("key")["c2019"].apply(lambda s: {c[:2] for c in s}) !=
             tasks.set_index("key")["holders"].apply(lambda h: {c[:2] for c in h})).sum()))

    # C6 wage: equal-split mean over holder occupations (the employment-weighted rule needs BLS-EP, external)
    def eq_wage(h):
        v = [wage_by_code.get(c) for c in h]; v = [x for x in v if x is not None and not np.isnan(x)]
        return np.mean(v) if v else np.nan
    tasks["wage"] = tasks["holders"].apply(eq_wage)
    priced = tasks.dropna(subset=["wage"])
    say("C6 coverage: priced tasks", len(priced), "of", len(tasks), "| % of named mass", round(100 * priced["w"].sum() / named_w.sum(), 2))
    def jz(h):
        v = [jz_by_code.get(c) for c in h]; v = [x for x in v if x is not None and x != -1]
        return np.mean(v) if v else np.nan
    tasks["jz"] = tasks["holders"].apply(jz)
    say("JobZone coverage % of named mass, -1 sentinels dropped", round(100 * tasks.dropna(subset=['jz'])["w"].sum() / named_w.sum(), 2),
        "| any JobZone value incl. -1", round(100 * tasks[tasks["holders"].apply(lambda h: any(c in jz_by_code.index for c in h))]["w"].sum() / named_w.sum(), 2))

    # analysis set = C6 wage and >=1 classified cell
    cls_tasks = set(named_cls.index)
    an = priced[priced["task"].isin(cls_tasks)].copy()
    say("analysis set:", len(an), "tasks |", round(an["w"].sum(), 2), "pp of wave |", round(100 * an["w"].sum() / named_w.sum(), 2), "% of named",
        "| classified conversations", f"{named_cls.loc[an['task'], FIVE].sum().sum():,.0f}",
        "| classified-but-no-wage", len(cls_tasks - set(priced["task"])),
        "| wage-but-no-classified", len(set(priced["task"]) - cls_tasks))
    say("Kish N, analysis set:", round(kish(an["w"].values), 1))
    # SOC-15 share of analysis mass (2010 codes): equal-split allocation of a task's mass over its holders' groups
    an["soc15_eq"] = an["holders"].apply(lambda h: np.mean([c.startswith("15-") for c in h]))
    an["soc15_modal"] = an["holders"].apply(lambda h: float(pd.Series([c[:2] for c in h]).mode().iloc[0] == "15"))
    say("SOC-15 share of analysis mass (2010 codes): equal-split", round(100 * (an["w"] * an["soc15_eq"]).sum() / an["w"].sum(), 2),
        "| modal-group", round(100 * (an["w"] * an["soc15_modal"]).sum() / an["w"].sum(), 2))

    # usage-weighted wage quartiles (boundaries on the equal-split wage — steward's primary is employment-weighted)
    an = an.sort_values("wage"); cw = an["w"].cumsum() / an["w"].sum()
    bounds = [an["wage"].values[np.searchsorted(cw.values, q)] for q in (0.25, 0.5, 0.75)]
    an["q"] = 1 + np.searchsorted(np.array(bounds), an["wage"].values, side="right")
    an["q"] = an["q"].clip(1, 4)
    say("usage-weighted wage quartile boundaries (equal-split wage):", [round(b, 2) for b in bounds],
        "| Q4 max", round(an["wage"].max(), 2))
    qk = an.groupby("q")["w"].apply(lambda s: round(kish(s.values), 1)).tolist()
    qn = an.groupby("q")["task"].count().tolist()
    qmass = an.groupby("q")["w"].sum().round(2).tolist()
    say("per quartile: tasks", qn, "| Kish N", qk, "| mass pp", qmass)
    ncls = named_cls[FIVE].sum(axis=1)
    qconv = an.groupby("q")["task"].apply(lambda t: ncls.loc[t].sum()).astype(int).tolist()
    say("classified conversations per quartile", [f"{x:,}" for x in qconv])
    p = five_base / 100
    se = 100 * np.sqrt(p * (1 - p) / qconv[0] + p * (1 - p) / qconv[3])
    say(f"conversation-level binomial SE for Q4-Q1 at p={p:.3f}: {se:.3f} pp | MDE(80%, two-sided 5%) = 2.80*SE = {2.8*se:.2f} pp"
        " (quartile automation shares NOT computed)")
    if us_med is not None:
        say(f"share of (group-employment-weighted) US occupation wage mass below Q1 boundary ${bounds[0]:.2f}: "
            f"{100*wd.loc[wd['hr'] < bounds[0], 'emp_w'].sum()/wd['emp_w'].sum():.1f}%")
    # SOC-15 share inside Q4
    q4 = an[an["q"] == 4]
    say("SOC-15 (equal-split) share of Q4 mass:", round(100 * (q4["w"] * q4["soc15_eq"]).sum() / q4["w"].sum(), 1), "%")
    # translation of a 1 pp Q4-Q1 gap into the wage-weighted automation share
    qw = an.groupby("q")["w"].sum() / an["w"].sum()
    qwage = an.groupby("q")[["wage", "w"]].apply(lambda d: np.average(d["wage"], weights=d["w"]))
    omega = qw * qwage / (qw * qwage).sum()
    coef = 0.5 * ((omega[4] - qw[4]) - (omega[1] - qw[1]))
    say("quartile mean wages", [round(x, 2) for x in qwage.tolist()], "| a symmetric 1 pp Q4-Q1 gap moves (wage-weighted minus unweighted) automation share by",
        round(coef, 3), "pp")

    # use_case intersection (composition rival) and human_only_time
    uc = g[g["facet"] == "onet_task::use_case"]
    hot = g[g["facet"] == "onet_task::human_only_time"]
    say("onet_task::use_case rows", len(uc), "| onet_task::human_only_time rows", len(hot))
    if len(uc):
        u = uc[uc["variable"].str.endswith("_count")].copy()
        pr = u["cluster_name"].str.rsplit("::", n=1); u["task"] = pr.str[0]; u["cat"] = pr.str[1]
        U = u.pivot_table(index="task", columns="cat", values="value", aggfunc="sum").fillna(0.0)
        say("use_case categories:", sorted(U.columns.tolist()), "| tasks", len(U))
        work_cols = [c for c in U.columns if c.lower().startswith("work")]
        work_share = U[work_cols].sum(axis=1) / U.sum(axis=1)
        an["work_share"] = an["task"].map(work_share)
        cov = an["work_share"].notna().mean()
        say("per-task work share (of all use_case cells) p10/p50/p90:", [round(100 * work_share.quantile(q), 1) for q in (0.1, 0.5, 0.9)],
            "| coverage of analysis set", round(100 * cov, 1), "%")
        by_q = an.dropna(subset=["work_share"]).groupby("q")[["work_share", "w"]].apply(lambda d: 100 * np.average(d["work_share"], weights=d["w"]))
        say("usage-weighted work share by wage quartile Q1..Q4:", [round(x, 1) for x in by_q.tolist()])
        # the whole-wave use-case mix from the marginal facet
        m = g[(g["facet"] == "use_case") & (g["variable"] == "use_case_count")].set_index("cluster_name")["value"]
        say("wave use_case mix %:", {k: round(100 * v / m.sum(), 1) for k, v in m.items()})

    # Seychelles (Nov)
    if wv == "nov2025":
        sc = df[(df["geography"] == "country") & (df["geo_id"] == "SC")]
        syc = df[(df["geography"] == "country") & (df["geo_id"] == "SYC")]
        uc_sc = sc[(sc["facet"] == "country") & (sc["variable"] == "usage_count")]["value"].sum()
        up_sc = sc[(sc["facet"] == "country") & (sc["variable"] == "usage_pct")]["value"].sum()
        say("Seychelles: SC rows", len(sc), "| SYC rows", len(syc), "| usage_count", f"{uc_sc:,.0f}", "| usage_pct", round(up_sc, 4),
            "| SC onet_task::collaboration rows", (sc["facet"] == "onet_task::collaboration").sum())
        sct = sc[(sc["facet"] == "onet_task") & (sc["variable"] == "onet_task_count")].set_index("cluster_name")["value"]
        gl = wcnt.reindex(sct.index)
        share = (sct / gl).dropna()
        say("SC share of a task's global count: max", round(100 * share.max(), 1), "% | median", round(100 * share.median(), 1), "%",
            "| tasks >10%:", int((share > 0.10).sum()), "| >20%:", int((share > 0.20).sum()))
        hi = share[share > 0.10].index
        hi_an = an[an["task"].isin(hi)]
        say("in analysis set, tasks with SC >10%:", len(hi_an), "| mass pp", round(hi_an["w"].sum(), 2),
            "| of which in Q4", round(hi_an.loc[hi_an["q"] == 4, "w"].sum(), 2), "pp | Q4 total", round(an.loc[an["q"] == 4, "w"].sum(), 2))
        scc = sc[(sc["facet"] == "collaboration") & (sc["variable"] == "collaboration_count")].set_index("cluster_name")["value"]
        say("SC collaboration mix: feedback loop %", round(100 * scc.get("feedback loop", 0) / scc.sum(), 1),
            "| global feedback loop %", round(100 * col["feedback loop"] / col.sum(), 1))

    summary[wv] = dict(all_base=all_base, five_base=five_base, kish=kish(named_w.values), n_an=len(an))

# top-10 concentration
say("\nDone.")
open("posts/post1/notes/rederivation/referee_brief_post1.out.txt", "w").write("\n".join(out) + "\n")
