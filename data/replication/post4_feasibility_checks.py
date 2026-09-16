"""post4 (LL-09) feasibility and replication checks — data steward, 2026-09-16.

Confirms every cut named in posts/post4/BRIEF.md §8 at column level, reproduces the
fourth report's Figure 2.2 task-success levels, and sizes the panel, the instrument,
the placebo, the H4 margin and the Seychelles composition term.

Run from the repository root with the cache built
(`python data/fetch/release_2025_09_15.py` etc.):

    python data/replication/post4_feasibility_checks.py

Writes data/replication/results/post4_feasibility_checks.txt and prints the same.
Raw files are never modified.
"""
import numpy as np
import pandas as pd

BASE = 'data/cache'
CLAUDE = {
    'Aug 2025': f'{BASE}/release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv',
    'Nov 2025': f'{BASE}/release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.parquet',
    'Feb 2026': f'{BASE}/release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.parquet',
}
API = {
    'Aug 2025': f'{BASE}/release_2025_09_15/data/intermediate/aei_raw_1p_api_2025-08-04_to_2025-08-11.csv',
    'Nov 2025': f'{BASE}/release_2026_01_15/data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.parquet',
    'Feb 2026': f'{BASE}/release_2026_03_24/data/aei_raw_1p_api_2026-02-05_to_2026-02-12.parquet',
}
ENRICHED_AUG = f'{BASE}/release_2025_09_15/data/output/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.parquet'
PSEUDO = {'none', 'not_classified'}
DEN = {'Aug 2025': 964494, 'Nov 2025': 999875, 'Feb 2026': 1000000}

LOG = []


def P(*a):
    s = ' '.join(str(x) for x in a)
    LOG.append(s)
    print(s)


def read(path):
    """Trap 1/2: NA is Namibia and NONE is a pseudo-geography; trap 7: level is a string."""
    if path.endswith('.parquet'):
        d = pd.read_parquet(path)
    else:
        d = pd.read_csv(path, keep_default_na=False, na_values=[], dtype=str)
        d['value'] = pd.to_numeric(d['value'])
    d['level'] = d['level'].astype(str)
    for c in ['geo_id', 'geography', 'facet', 'variable', 'cluster_name']:
        d[c] = d[c].astype(str)
    return d


def key(s):
    return s.strip().lower()


def task_frame(df, label):
    """Cut 1/3/4: onet_task at geography=global, level=0."""
    g = df[(df.geography == 'global') & (df.facet == 'onet_task') & (df.level == '0')]
    w = g.pivot_table(index='cluster_name', columns='variable', values='value', aggfunc='first')
    raw_nodes = len(w)
    w.index = [key(i) for i in w.index]
    named = w.drop(index=[i for i in w.index if i in PSEUDO])
    P(f'[{label}] onet_task global L0: rows={len(g)} nodes={raw_nodes} named={len(named)} '
      f'vars={sorted(g.variable.unique())}')
    P(f'[{label}]   pct sum={w["onet_task_pct"].sum():.6f} count sum={w["onet_task_count"].sum():.0f} '
      f'min count={w["onet_task_count"].min():.0f} named mass={named["onet_task_pct"].sum():.4f} '
      f'pseudo={sorted(set(w.index) & PSEUDO)} lower-case collisions={raw_nodes - len(set(w.index))}')
    return w


def success_frame(df, label):
    """Cut 2: onet_task::task_success at geography=global."""
    g = df[(df.geography == 'global') & (df.facet == 'onet_task::task_success')]
    if not len(g):
        P(f'[{label}] onet_task::task_success ABSENT at global')
        return None, None
    sp = g.cluster_name.str.rsplit('::', n=1, expand=True)
    g = g.assign(task=sp[0].map(key), cat=sp[1])
    pct = g[g.variable == 'onet_task_task_success_pct'].pivot_table(index='task', columns='cat', values='value')
    cnt = g[g.variable == 'onet_task_task_success_count'].pivot_table(index='task', columns='cat', values='value')
    pat = g.groupby('task').cat.apply(lambda s: tuple(sorted(set(s))))
    P(f'[{label}] onet_task::task_success: rows={len(g)} vars={sorted(g.variable.unique())} '
      f'levels={sorted(g.level.unique())} categories={sorted(g.cat.unique())} task keys={len(pct)} '
      f'pseudo task keys={sorted(set(pct.index) & PSEUDO)}')
    P(f'[{label}]   publication patterns: ' + '; '.join(f'{k}={v}' for k, v in pat.value_counts().items()))
    for c in ['yes', 'no', 'not_classified']:
        if c in cnt:
            s = cnt[c].dropna()
            P(f'[{label}]   {c}: nodes={len(s)} count min={s.min():.0f} max={s.max():.0f} #<15={int((s < 15).sum())}')
    s3 = pct.reindex(columns=['yes', 'no', 'not_classified']).sum(axis=1, min_count=1)
    s2 = pct.reindex(columns=['yes', 'no']).sum(axis=1, min_count=1)
    P(f'[{label}]   sum(yes,no,not_classified) == 100 for {int((s3.sub(100).abs() < 1e-6).sum())} of {len(pct)} nodes '
      f'(min {s3.min():.4f}, max {s3.max():.4f})')
    P(f'[{label}]   sum(yes,no) == 100 for {int((s2.sub(100).abs() < 1e-6).sum())} of {len(pct)} nodes')
    return pct, cnt


P('=' * 78)
P('1. onet_task global, three waves (brief §8 rows 1, 3, 4)')
P('=' * 78)
cl = {k: read(v) for k, v in CLAUDE.items()}
W = {k: task_frame(v, k) for k, v in cl.items()}
for lab in W:
    w = W[lab]
    r = (w.onet_task_count / DEN[lab] * 100 - w.onet_task_pct).abs().max()
    P(f'[{lab}] second-implementation identity max|count/{DEN[lab]}*100 - pct| = {r:.3e}')
ge = read(ENRICHED_AUG)
ge = ge[(ge.geography == 'global') & (ge.facet == 'onet_task') & (ge.level == '0')]
we = ge.pivot_table(index='cluster_name', columns='variable', values='value', aggfunc='first')
we.index = [key(i) for i in we.index]
P(f'[Aug 2025 enriched] nodes={len(we)}; onet_task_pct identical to the raw file: '
  f'{np.allclose(we.reindex(W["Aug 2025"].index).onet_task_pct.values, W["Aug 2025"].onet_task_pct.values)}')

P('')
P('=' * 78)
P('2. onet_task::task_success global (brief §8 row 2)')
P('=' * 78)
S = {}
for lab in ['Nov 2025', 'Feb 2026']:
    S[lab] = success_frame(cl[lab], lab)
P(f'[Aug 2025] facets matching "success" at global: '
  f'{sorted(f for f in cl["Aug 2025"][cl["Aug 2025"].geography == "global"].facet.unique() if "success" in f)}')
for lab in ['Nov 2025', 'Feb 2026']:
    pct, cnt = S[lab]
    w = W[lab]
    j = pd.concat([cnt.sum(axis=1, min_count=1).rename('cells'), w['onet_task_count'].rename('task')],
                  axis=1, join='inner')
    P(f'[{lab}] the three cells partition onet_task_count exactly for {int((j.cells == j.task).sum())} of {len(j)} nodes '
      f'-> the intersection _pct base is the task\'s own conversations')
    nolabel = pct[pct.reindex(columns=['yes', 'no']).isna().all(axis=1)]
    onesided = pct[pct['yes'].notna() & pct['no'].isna()]
    folded = pct[pct.reindex(columns=['yes', 'no']).notna().any(axis=1) & pct['not_classified'].notna()]
    P(f'[{lab}]   nodes with no yes and no no cell (no success rate at all) = {len(nolabel)}')
    P(f'[{lab}]   nodes with yes but no `no` cell = {len(onesided)} (renormalising over published cells '
      f'would set every one of them to 100%)')
    P(f'[{lab}]   nodes with a label and a folded not_classified cell = {len(folded)}; '
      f'bound width = not_classified _pct, median {folded["not_classified"].median():.2f} pp, '
      f'max {folded["not_classified"].max():.2f} pp')

P('')
P('=' * 78)
P('3. the matched panel, the regression sample, the instrument, the placebo')
P('=' * 78)
sn, sf, sa = set(W['Nov 2025'].index), set(W['Feb 2026'].index), set(W['Aug 2025'].index)
P(f'nodes incl pseudo: Nov={len(sn)} Feb={len(sf)} Aug={len(sa)}')
P(f'Nov n Feb incl pseudo = {len(sn & sf)}; the two pseudo-nodes are {sorted((sn & sf) & PSEUDO)} '
  f'-> named matched = {len((sn & sf) - PSEUDO)}   [the 2,888 vs 2,886 reconciliation]')
matched = (sn & sf) - PSEUDO
nov_only, feb_only = sn - PSEUDO - sf, sf - PSEUDO - sn
P(f'Nov-only named = {len(nov_only)}; Feb-only named = {len(feb_only)}; '
  f'named in all three long waves = {len(matched & (sa - PSEUDO))} (2,282 named + 2 pseudo = the atlas 2,284)')
pn, cn = S['Nov 2025']
pf, cf = S['Feb 2026']
lab_n = set(pn.index[pn.reindex(columns=['yes', 'no']).notna().any(axis=1)])
lab_f = set(pf.index[pf.reindex(columns=['yes', 'no']).notna().any(axis=1)])
yes_n = set(pn.index[pn['yes'].notna()])
exact_n = set(pn.index[pn.reindex(columns=['yes', 'no']).notna().all(axis=1)]) | \
          set(pn.index[pn['yes'].notna() & pn['not_classified'].isna()])
wn, wf, wa = W['Nov 2025'], W['Feb 2026'], W['Aug 2025']
named_mass = wn.drop(index=[i for i in wn.index if i in PSEUDO])['onet_task_pct'].sum()
samples = [('any Nov yes/no cell', sorted(matched & lab_n)),
           ('published Nov `yes` cell (the long-list 2,427)', sorted(matched & yes_n)),
           ('exactly identified (no folded not_classified cell)', sorted(matched & exact_n))]
for lab, s in samples:
    m = wn.loc[s, 'onet_task_pct'].sum()
    P(f'  {lab}: N={len(s)}; Nov mass={m:.4f} pp of 100 = {100 * m / named_mass:.2f}% of Nov named mass; '
      f'with an Aug-2025 share = {len(set(s) & sa)}')
s_all = sorted(matched & lab_n)
s_inst = sorted(set(s_all) & sa)
fold = pn.reindex(s_all)
fold = fold[fold['not_classified'].notna()]
P(f'  folding error inside the {len(s_all)}-task sample: {len(fold)} nodes carry a folded '
  f'not_classified cell; bound width median {fold["not_classified"].median():.2f} pp, '
  f'max {fold["not_classified"].max():.2f} pp')
d = wf.loc[s_all, 'onet_task_pct'] - wn.loc[s_all, 'onet_task_pct']
dp = wn.loc[s_inst, 'onet_task_pct'] - wa.loc[s_inst, 'onet_task_pct']
P(f'  outcome Nov->Feb over N={len(s_all)}: mean={d.mean():+.5f} sd={d.std():.5f} '
  f'p5={d.quantile(.05):+.4f} p95={d.quantile(.95):+.4f} max|.|={d.abs().max():.4f} pp')
P(f'  placebo Aug->Nov over N={len(s_inst)}: mean={dp.mean():+.5f} sd={dp.std():.5f} max|.|={dp.abs().max():.4f} pp; '
  f'corr with the outcome = {d.reindex(s_inst).corr(dp):.4f}')
for lab, s in samples:
    for wlab, ww in [('Nov share', wn.loc[s, 'onet_task_pct'].values), ('Feb share', wf.loc[s, 'onet_task_pct'].values)]:
        k = ww.sum() ** 2 / (ww ** 2).sum()
        P(f'  power, {lab} (N={len(s)}), weights={wlab}: Kish N_eff={k:.1f}; '
          f'MDE|r| nominal={2.8 / np.sqrt(len(s) - 3):.4f} vs weighted={2.8 / np.sqrt(k - 3):.4f}')
P(f'  H4 margin: Nov-only exits={len(nov_only)} (mass {wn.loc[sorted(nov_only), "onet_task_pct"].sum():.4f} pp, '
  f'{int((wn.loc[sorted(nov_only), "onet_task_count"] <= 20).sum())} within 15-20 conversations), '
  f'with a Nov success label={len(nov_only & lab_n)}')
P(f'  H4 margin: Feb-only entrants={len(feb_only)} (mass {wf.loc[sorted(feb_only), "onet_task_pct"].sum():.4f} pp, '
  f'{int((wf.loc[sorted(feb_only), "onet_task_count"] <= 20).sum())} within 15-20 conversations), '
  f'with a Feb success label={len(feb_only & lab_f)}')
e, f_ = sorted(nov_only & lab_n), sorted(feb_only & lab_f)
xa, yn = wa.loc[s_inst, 'onet_task_pct'], wn.loc[s_inst, 'onet_task_pct']
P(f'  first stage on the {len(s_inst)} instrumented tasks: corr(Aug pct, Nov pct)={xa.corr(yn):.4f} '
  f'(R2 {xa.corr(yn) ** 2:.4f}) in levels; {np.log(xa).corr(np.log(yn)):.4f} '
  f'(R2 {np.log(xa).corr(np.log(yn)) ** 2:.4f}) in logs')
ye, yf_ = pn.reindex(e)['yes'].fillna(0), pf.reindex(f_)['yes'].fillna(0)
ys_n, ys_f = pn.reindex(s_all)['yes'].fillna(0), pf.reindex(s_all)['yes'].fillna(0)
P(f'  H4 unweighted means and MDEs: exits {ye.mean():.2f} (sd {ye.std():.2f}, n {len(ye)}) vs survivors '
  f'{ys_n.mean():.2f} (sd {ys_n.std():.2f}, n {len(ys_n)}), MDE '
  f'{2.8 * np.sqrt(ye.var() / len(ye) + ys_n.var() / len(ys_n)):.2f} pp; entrants {yf_.mean():.2f} '
  f'(sd {yf_.std():.2f}, n {len(yf_)}) vs survivors Feb {ys_f.mean():.2f}, MDE '
  f'{2.8 * np.sqrt(yf_.var() / len(yf_) + ys_f.var() / len(ys_f)):.2f} pp')
P(f'  exits mean Nov yes_pct={pn.reindex(e)["yes"].fillna(0).mean():.4f}%; '
  f'entrants mean Feb yes_pct={pf.reindex(f_)["yes"].fillna(0).mean():.4f}%; '
  f'survivors usage-weighted Nov yes_pct='
  f'{(pn.reindex(s_all)["yes"].fillna(0) * wn.loc[s_all, "onet_task_count"]).sum() / wn.loc[s_all, "onet_task_count"].sum():.4f}%')

P('')
P('=' * 78)
P('4. the controls at global, November (brief §8 row 5)')
P('=' * 78)
g = cl['Nov 2025']
uc = g[(g.geography == 'global') & (g.facet == 'onet_task::use_case')]
sp = uc.cluster_name.str.rsplit('::', n=1, expand=True)
uc = uc.assign(task=sp[0].map(key), cat=sp[1])
ucp = uc[uc.variable == 'onet_task_use_case_pct'].pivot_table(index='task', columns='cat', values='value')
ucc = uc[uc.variable == 'onet_task_use_case_count'].pivot_table(index='task', columns='cat', values='value')
P(f'[Nov 2025] onet_task::use_case: vars={sorted(uc.variable.unique())} categories={sorted(uc.cat.unique())} '
  f'task keys={len(ucp)}; pct sums to 100 for {int((ucp.sum(axis=1, min_count=1).sub(100).abs() < 1e-6).sum())} of {len(ucp)}')
for c in ucp.columns:
    s = ucc[c].dropna()
    P(f'  {c}: published for {ucp[c].notna().sum()} tasks ({ucp.reindex(s_all)[c].notna().sum()} of the '
      f'{len(s_all)} regression tasks); count min={s.min():.0f} max={s.max():.0f} #<15={int((s < 15).sum())}')
wsh = ucp.reindex(s_all)['work']
P(f'  H2 split: `work` published for {wsh.notna().sum()} of {len(s_all)} sample tasks, median published '
  f'work share {wsh.median():.2f}; folded for {int(wsh.isna().sum())}, median with folded set to zero '
  f'{wsh.fillna(0).median():.2f}')
ed = g[(g.geography == 'global') & (g.facet == 'onet_task::human_education_years')].copy()
ed['task'] = ed.cluster_name.map(key)
edw = ed.pivot_table(index='task', columns='variable', values='value')
m, c = 'onet_task_human_education_years_mean', 'onet_task_human_education_years_count'
P(f'[Nov 2025] onet_task::human_education_years: cluster_name is the task alone (no ::category); '
  f'vars={sorted(ed.variable.unique())}; task keys={len(edw)}')
P(f'  _mean published for {edw[m].notna().sum()} of {len(edw)} keys, '
  f'{edw.reindex(s_all)[m].notna().sum()} of the {len(s_all)} regression tasks, '
  f'{edw.reindex(s_inst)[m].notna().sum()} of the {len(s_inst)} instrumented tasks; '
  f'range {edw[m].min():.3f}-{edw[m].max():.3f} yr')
P(f'  _count equals onet_task_count for {int((edw[c].reindex(wn.index) == wn["onet_task_count"]).sum())} of {len(edw)} nodes '
  f'(min {edw[c].min():.0f})')
sub = pd.DataFrame({'s': pn.reindex(s_all)['yes'].fillna(0.0), 'e': edw.reindex(s_all)[m],
                    'w': wn.loc[s_all, 'onet_task_count']}).dropna()
wm = lambda x, w: np.average(x, weights=w)
cov = lambda x, y, w: (w * (x - wm(x, w)) * (y - wm(y, w))).sum() / w.sum()
rw = cov(sub.s.values, sub.e.values, sub.w.values) / np.sqrt(
    cov(sub.s.values, sub.s.values, sub.w.values) * cov(sub.e.values, sub.e.values, sub.w.values))
P(f'  H3 pre-check corr(Nov yes_pct, education mean) over {len(sub)} nodes: '
  f'unweighted {sub.s.corr(sub.e):.4f}, usage-weighted {rw:.4f}')

P('')
P('=' * 78)
P('5. the 1P API leg (brief §8 row 6)')
P('=' * 78)
ap = {k: read(v) for k, v in API.items()}
WA, SA = {}, {}
for lab, df in ap.items():
    P(f'[{lab} API] geographies={sorted(df.geography.unique())}; '
      f'usage_count variable present={"usage_count" in set(df.variable)}')
    WA[lab] = task_frame(df, lab + ' API')
    SA[lab] = success_frame(df, lab + ' API')
mapi = (set(WA['Nov 2025'].index) & set(WA['Feb 2026'].index)) - PSEUDO
pna = SA['Nov 2025'][0]
labna = set(pna.index[pna.reindex(columns=['yes', 'no']).notna().any(axis=1)])
P(f'[API] matched named Nov n Feb = {len(mapi)}; with a Nov success label = {len(mapi & labna)}; '
  f'also carrying an Aug API share = {len((mapi & labna) & set(WA["Aug 2025"].index))}')

P('')
P('=' * 78)
P('6. replication: the published task-success levels (fourth report, Fig 2.2 p.25 and p.26)')
P('=' * 78)
for lab, df in [('Nov Claude.ai', cl['Nov 2025']), ('Nov 1P API', ap['Nov 2025']),
                ('Feb Claude.ai', cl['Feb 2026']), ('Feb 1P API', ap['Feb 2026'])]:
    t = df[(df.geography == 'global') & (df.facet == 'task_success')]
    w = t.pivot_table(index='cluster_name', columns='variable', values='value', aggfunc='first')
    P(f'[{lab}] ' + '; '.join(f'{i} pct={r.task_success_pct:.4f} count={r.task_success_count:.0f}'
                              for i, r in w.iterrows()))
    P(f'[{lab}]   pct sum={w["task_success_pct"].sum():.6f}; N={w["task_success_count"].sum():.0f}; '
      f'yes on the all-conversation base={w.loc["yes", "task_success_pct"]:.4f}% '
      f'(count route {100 * w.loc["yes", "task_success_count"] / w["task_success_count"].sum():.4f}%)')
for lab in ['Nov 2025', 'Feb 2026']:
    pct, _ = S[lab]
    w = W[lab]
    ls = sorted(set(pct.index[pct.reindex(columns=['yes', 'no']).notna().any(axis=1)]))
    yy, ww = pct.loc[ls, 'yes'].fillna(0.0), w.loc[ls, 'onet_task_count']
    P(f'[{lab} Claude.ai] usage-weighted mean per-task yes_pct over {len(ls)} labelled task nodes = '
      f'{(yy * ww).sum() / ww.sum():.4f}% on {ww.sum():.0f} conversations '
      f'(against the published global level)')

P('')
P('=' * 78)
P('7. the Seychelles composition term (brief §7.3c, §10)')
P('=' * 78)
nv = cl['Nov 2025']
P(f'Nov: SC rows={len(nv[nv.geo_id == "SC"])}, usage_count='
  f'{nv[(nv.geo_id == "SC") & (nv.variable == "usage_count")].value.tolist()}; '
  f'Feb: SC rows={len(cl["Feb 2026"][cl["Feb 2026"].geo_id == "SC"])}')
sc = nv[(nv.geo_id == 'SC') & (nv.facet == 'onet_task') & (nv.variable == 'onet_task_count')].copy()
sc['k'] = sc.cluster_name.map(key)
scn = sc[~sc.k.isin(PSEUDO)].set_index('k').value
P(f'  SC publishes {len(sc)} onet_task nodes ({len(scn)} named), counts summing to {sc.value.sum():.0f} '
  f'= its usage_count exactly; {sc.value.sum() - scn.sum():.0f} conversations '
  f'({100 * (sc.value.sum() - scn.sum()) / sc.value.sum():.1f}% of SC) sit in its none/not_classified nodes')
P(f'  SC named nodes inside the regression sample = {len(set(scn.index) & set(s_all))}, '
  f'{scn.reindex(s_all).dropna().sum():.0f} conversations = '
  f'{100 * scn.reindex(s_all).dropna().sum() / DEN["Nov 2025"]:.4f} pp of the Nov base')
adj = (wn['onet_task_count'].reindex(s_all).fillna(0) - scn.reindex(s_all).fillna(0)) / (DEN['Nov 2025'] - 24715) * 100
shift = adj - wn.loc[s_all, 'onet_task_pct']
P(f'  netting SC out of the Nov numerator and denominator moves the Nov share by median {shift.median():+.4f}, '
  f'min {shift.min():+.4f}, max {shift.max():+.4f} pp; {int((shift.abs() > 0.01).sum())} tasks move by >0.01 pp')
big = wn.loc[s_all, 'onet_task_count'].idxmax()
P(f'  largest task "{big[:58]}...": Nov {wn.loc[big, "onet_task_count"]:.0f} conversations of which SC '
  f'{scn.get(big, 0):.0f} ({100 * scn.get(big, 0) / wn.loc[big, "onet_task_count"]:.2f}%); raw change '
  f'{wf.loc[big, "onet_task_pct"] - wn.loc[big, "onet_task_pct"]:+.4f} pp, SC-netted '
  f'{wf.loc[big, "onet_task_pct"] - adj[big]:+.4f} pp')
P(f'  no correction is available for the regressor: SC rows at facet onet_task::task_success = '
  f'{len(nv[(nv.geo_id == "SC") & (nv.facet == "onet_task::task_success")])} (intersections are global only)')
for lab in ['Nov 2025', 'Feb 2026']:
    w = W[lab]
    P(f'[{lab}] pseudo-node sizes: none={w.loc["none", "onet_task_count"]:.0f} '
      f'({w.loc["none", "onet_task_pct"]:.4f} pp), not_classified={w.loc["not_classified", "onet_task_count"]:.0f} '
      f'({w.loc["not_classified", "onet_task_pct"]:.4f} pp); success rows for the task key `not_classified` = '
      f'{len(cl[lab][(cl[lab].geography == "global") & (cl[lab].facet == "onet_task::task_success") & (cl[lab].cluster_name.str.startswith("not_classified::"))])}')

with open('data/replication/results/post4_feasibility_checks.txt', 'w') as fh:
    fh.write('\n'.join(LOG) + '\n')
print('\nwrote data/replication/results/post4_feasibility_checks.txt')
