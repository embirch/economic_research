"""Referee brief-stage re-derivations for post4 (LL-09), 2026-09-16.

Independent of data/replication/post4_feasibility_checks.py: written from the raw files
and the brief's stated cuts, not from the steward's code. Re-derives the steward numbers
the brief carries, then adds the checks the verdict needs:
  (a) the distribution of the pp outcome (does the unweighted MDE mean anything?);
  (b) the publication floor's censoring of `yes_pct` in small nodes;
  (c) the H4 margin under the brief's own construct (published `yes` pct, no zero-imputation);
  (d) Seychelles' share of the largest task.
No relation between the November success rate and the Nov->Feb share change is computed
here: the confirmatory test waits for the pre-registration.

    python posts/post4/notes/rederivation/referee_brief_checks.py
Writes referee_brief_checks.txt beside this file.
"""
import numpy as np
import pandas as pd
import os

C = 'data/cache'
F = {
    'aug': f'{C}/release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv',
    'nov': f'{C}/release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.parquet',
    'feb': f'{C}/release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.parquet',
    'api_nov': f'{C}/release_2026_01_15/data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.parquet',
}
OUT = os.path.join(os.path.dirname(__file__), 'referee_brief_checks.txt')
lines = []


def P(*a):
    s = ' '.join(str(x) for x in a)
    lines.append(s)
    print(s)


def load(p):
    if p.endswith('.csv'):
        d = pd.read_csv(p, keep_default_na=False, na_values=[], dtype=str)
        d['value'] = d['value'].astype(float)
    else:
        d = pd.read_parquet(p)
        d['level'] = d['level'].astype(str)
    return d


def wide(d, facet, geo='global'):
    g = d[(d.geography == geo) & (d.facet == facet)]
    w = g.pivot(index='cluster_name', columns='variable', values='value')
    w.index = w.index.str.strip().str.lower()
    return w


def succ(d, geo='global'):
    """onet_task::task_success -> DataFrame indexed by task with yes/no/nc pct and count."""
    g = d[(d.geography == geo) & (d.facet == 'onet_task::task_success')].copy()
    parts = g.cluster_name.str.rsplit('::', n=1, expand=True)
    g['task'] = parts[0].str.strip().str.lower()
    g['cat'] = parts[1]
    pct = g[g.variable.str.endswith('_pct')].pivot(index='task', columns='cat', values='value')
    cnt = g[g.variable.str.endswith('_count')].pivot(index='task', columns='cat', values='value')
    return pct, cnt


nov = load(F['nov']); feb = load(F['feb']); aug = load(F['aug']); api = load(F['api_nov'])

# ---- 1. Replication anchor: global task_success facet -------------------------------
P('== 1. Global task_success facet (Figure 2.2 anchor)')
for lab, d in [('Nov Claude.ai', nov), ('Feb Claude.ai', feb), ('Nov 1P API', api)]:
    t = d[(d.geography == 'global') & (d.facet == 'task_success')]
    w = t.pivot(index='cluster_name', columns='variable', values='value')
    P(f'  {lab}: yes_pct={w.loc["yes","task_success_pct"]:.4f}  count sum={w["task_success_count"].sum():.0f}  cats={list(w.index)}')

# ---- 2. onet_task panel -----------------------------------------------------------------
P('== 2. onet_task global L0 panel')
T = {}
for k, d in [('aug', aug), ('nov', nov), ('feb', feb)]:
    g = d[(d.geography == 'global') & (d.facet == 'onet_task') & (d.level == '0')]
    w = g.pivot(index='cluster_name', columns='variable', values='value')
    n_raw = len(w)
    w.index = w.index.str.strip().str.lower()
    assert len(set(w.index)) == n_raw, 'lower-case collision'
    P(f'  {k}: nodes={n_raw} pct sum={w.onet_task_pct.sum():.4f} count sum={w.onet_task_count.sum():.0f} min count={w.onet_task_count.min():.0f}')
    T[k] = w.drop(index=[i for i in ('none', 'not_classified') if i in w.index])
named_nov, named_feb, named_aug = set(T['nov'].index), set(T['feb'].index), set(T['aug'].index)
both = named_nov & named_feb
P(f'  matched Nov∩Feb named={len(both)}  Nov-only={len(named_nov-named_feb)}  Feb-only={len(named_feb-named_nov)}  in Aug too={len(both & named_aug)}')

# ---- 3. Success intersection, samples A/B/C ---------------------------------------------
P('== 3. onet_task::task_success intersection (Nov) and samples')
spN, scN = succ(nov); spF, scF = succ(feb)
P(f'  Nov task keys={len(spN)} cats={list(spN.columns)}; Feb task keys={len(spF)}')
# partition check: published cells' counts == onet_task_count
allN = T['nov'].reindex(spN.index.difference(['none']))
part = (scN.reindex(allN.index).fillna(0).sum(axis=1) - allN.onet_task_count).abs()
P(f'  Nov partition (sum of published cell counts == onet_task_count): {int((part < 1e-6).sum())} of {len(part)}')
P(f'  Nov min published yes count={scN["yes"].min():.0f}, min no count={scN["no"].min():.0f}, not_classified count range=({scN["not_classified"].min():.0f},{scN["not_classified"].max():.0f})')
panel = pd.DataFrame(index=sorted(both))
panel['s_nov'] = T['nov'].onet_task_pct; panel['n_nov'] = T['nov'].onet_task_count
panel['s_feb'] = T['feb'].onet_task_pct; panel['n_feb'] = T['feb'].onet_task_count
panel['s_aug'] = T['aug'].onet_task_pct.reindex(panel.index)
panel['yes'] = spN['yes'].reindex(panel.index); panel['no'] = spN['no'].reindex(panel.index)
panel['nc'] = spN['not_classified'].reindex(panel.index)
A = panel[panel.yes.notna() | panel.no.notna()]
B = panel[panel.yes.notna()]
Cc = panel[panel.yes.notna() & panel.nc.isna()]
for lab, S in [('A', A), ('B', B), ('C', Cc)]:
    P(f'  sample {lab}: N={len(S)} Nov mass={S.s_nov.sum():.4f} with Aug instrument={int(S.s_aug.notna().sum())}')
P(f'  B mass as % of Nov named mass: {100*B.s_nov.sum()/T["nov"].onet_task_pct.sum():.2f}')
P(f'  A-instrumented mass {A[A.s_aug.notna()].s_nov.sum():.4f} pp = {100*A[A.s_aug.notna()].s_nov.sum()/A.s_nov.sum():.2f}% of A mass')
P(f'  A nodes with a folded cell: {int(A.nc.notna().sum())}; median folded pct={A.nc.median():.2f}, max={A.nc.max():.2f}')

# ---- 4. Power numbers the brief carries ---------------------------------------------------
P('== 4. Kish N_eff and MDE (2.8/sqrt(N-3))')
def kish(w): return w.sum()**2 / (w**2).sum()
for lab, S in [('A', A), ('B', B), ('C', Cc)]:
    kN, kF = kish(S.n_nov), kish(S.n_feb)
    P(f'  {lab}: N={len(S)} Kish Nov={kN:.1f} Feb={kF:.1f}  MDE nominal={2.8/np.sqrt(len(S)-3):.4f}  weighted Nov={2.8/np.sqrt(kN-3):.4f} Feb={2.8/np.sqrt(kF-3):.4f}')
top10 = panel.s_feb.sort_values(ascending=False).head(10)
P(f'  ten largest matched tasks: {top10.sum():.4f} pp of Feb all-conversation base; {100*top10.sum()/T["feb"].onet_task_pct.sum():.1f}% of Feb named mass')

# ---- 5. Instrument and placebo correlations ------------------------------------------------
P('== 5. First stage and placebo (no success variable enters)')
I = A[A.s_aug.notna()]
P(f'  corr(Aug, Nov share) levels on A-instrumented (N={len(I)}): {np.corrcoef(I.s_aug, I.s_nov)[0,1]:.4f}; logs: {np.corrcoef(np.log(I.s_aug), np.log(I.s_nov))[0,1]:.4f}')
d_out = I.s_feb - I.s_nov; d_pre = I.s_nov - I.s_aug
P(f'  Aug→Nov change: mean={d_pre.mean():.5f} sd={d_pre.std():.5f}; Nov→Feb change on A (N={len(A)}): mean={(A.s_feb-A.s_nov).mean():.5f} sd={(A.s_feb-A.s_nov).std():.5f}')
P(f'  corr(Nov→Feb, Aug→Nov) on instrumented A: {np.corrcoef(d_out, d_pre)[0,1]:.4f}')
P(f'  corr(Δlog Nov→Feb, Δlog Aug→Nov): {np.corrcoef(np.log(I.s_feb/I.s_nov), np.log(I.s_nov/I.s_aug))[0,1]:.4f}')

# ---- 6. (a) Is the unweighted pp outcome informative at N=2,427? ---------------------------
P('== 6. Distribution of the pp outcome on sample B')
d = (B.s_feb - B.s_nov)
z = (d - d.mean())
ss = (z**2).sort_values(ascending=False)
P(f'  sd={d.std():.4f} pp; excess kurtosis={pd.Series(d).kurt():.1f}')
for k in (1, 5, 10, 50):
    P(f'  top {k} movers carry {100*ss.head(k).sum()/ss.sum():.1f}% of the outcome sum of squares')
P(f'  variance-effective N of the outcome (Σz²)²/Σz⁴ = {ss.sum()**2/(ss**2).sum():.1f}')
small = B[B.n_nov < 100]
P(f'  tasks with n_nov<100: {len(small)} of {len(B)}, carrying {100*ss.reindex(small.index).sum()/ss.sum():.2f}% of the sum of squares')
dl = np.log(B.s_feb / B.s_nov)
P(f'  log change: sd={dl.std():.4f}, excess kurtosis={dl.kurt():.1f}; sd by n_nov bin: '
  + ', '.join(f'{lo}-{hi}: {dl[(B.n_nov>=lo)&(B.n_nov<hi)].std():.3f}' for lo, hi in [(15,50),(50,200),(200,1000),(1000,10**7)]))
P(f'  log change top-10 share of sum of squares: {100*((dl-dl.mean())**2).sort_values(ascending=False).head(10).sum()/((dl-dl.mean())**2).sum():.1f}%')

# ---- 7. (b) Floor censoring of yes_pct by node size --------------------------------------
P('== 7. Publication floor and yes_pct by November node size (sample B)')
P('  a yes cell publishes only if yes count >= 15, i.e. yes_pct >= 1500/n_nov')
for lo, hi in [(15, 21), (21, 31), (31, 51), (51, 101), (101, 501), (501, 10**7)]:
    s = B[(B.n_nov >= lo) & (B.n_nov < hi)]
    P(f'  n_nov in [{lo},{hi-1}]: N={len(s):4d} mean yes_pct={s.yes.mean():.2f} median={s.yes.median():.2f} min possible yes_pct={1500/max(lo,1):.1f}')
P(f'  sample B nodes with n_nov<30: {int((B.n_nov<30).sum())}; <100: {int((B.n_nov<100).sum())}')
# A-sample view: nodes whose ONLY label is `no` are those with yes<15 and no>=15
onlyno = A[A.yes.isna()]
P(f'  A nodes with only a `no` cell (yes folded): {len(onlyno)}; their n_nov median={onlyno.n_nov.median():.0f}')

# ---- 8. (c) H4 margin under the published-yes construct ----------------------------------
P('== 8. H4 margin: exits (Nov-only) and entrants (Feb-only)')
exits = sorted(named_nov - named_feb); entr = sorted(named_feb - named_nov)
exN = T['nov'].loc[exits]; enF = T['feb'].loc[entr]
P(f'  exits N={len(exits)}, with n_nov<=20: {int((exN.onet_task_count<=20).sum())}; entrants N={len(entr)}, with n_feb<=20: {int((enF.onet_task_count<=20).sum())}')
ex_yes = spN['yes'].reindex(exits); ex_no = spN['no'].reindex(exits)
en_yes = spF['yes'].reindex(entr); en_no = spF['no'].reindex(entr)
P(f'  exits with any Nov label={int((ex_yes.notna()|ex_no.notna()).sum())}, with a yes cell={int(ex_yes.notna().sum())}, only-no={int((ex_yes.isna()&ex_no.notna()).sum())}')
P(f'  entrants with any Feb label={int((en_yes.notna()|en_no.notna()).sum())}, with a yes cell={int(en_yes.notna().sum())}, only-no={int((en_yes.isna()&en_no.notna()).sum())}')
P(f'  exits published yes_pct: mean={ex_yes.mean():.2f} (N={int(ex_yes.notna().sum())}); with only-no imputed 0: mean={ex_yes.fillna(0)[ex_yes.notna()|ex_no.notna()].mean():.2f}')
P(f'  entrants published yes_pct: mean={en_yes.mean():.2f} (N={int(en_yes.notna().sum())}); with only-no imputed 0: mean={en_yes.fillna(0)[en_yes.notna()|en_no.notna()].mean():.2f}')
P(f'  survivors Nov yes_pct mean (B, published)={B.yes.mean():.2f}; (A, only-no as 0)={A.yes.fillna(0).mean():.2f}')
surv_feb_yes = spF['yes'].reindex(panel.index)
P(f'  survivors Feb yes_pct mean (published)={surv_feb_yes.mean():.2f}; (A-type, only-no as 0)={surv_feb_yes.fillna(0)[surv_feb_yes.notna()|spF["no"].reindex(panel.index).notna()].mean():.2f}')
P(f'  share of exits-with-yes at yes_pct>=75: {100*(ex_yes.dropna()>=75).mean():.1f}%; entrants: {100*(en_yes.dropna()>=75).mean():.1f}%')

# ---- 9. (d) Seychelles ------------------------------------------------------------------
P('== 9. Seychelles')
sc = nov[(nov.geo_id == 'SC') & (nov.facet == 'onet_task') & (nov.level == '0')]
scw = sc.pivot(index='cluster_name', columns='variable', values='value'); scw.index = scw.index.str.strip().str.lower()
uc = nov[(nov.geo_id == 'SC') & (nov.variable == 'usage_count')]
P(f'  SC onet_task nodes={len(scw)} count sum={scw.onet_task_count.sum():.0f}; SC usage_count={uc.value.iloc[0] if len(uc) else "n/a"}')
scf = feb[feb.geo_id == 'SC']
P(f'  SC rows in Feb release: {len(scf)}')
big = panel.n_nov.idxmax()
P(f'  largest panel task: "{big[:60]}…" n_nov={panel.n_nov[big]:.0f}, SC part={scw.onet_task_count.get(big, 0):.0f} ({100*scw.onet_task_count.get(big,0)/panel.n_nov[big]:.2f}%)')
raw_chg = panel.s_feb[big] - panel.s_nov[big]
net_chg = panel.s_feb[big] - 100*(panel.n_nov[big]-scw.onet_task_count.get(big,0))/999875
P(f'  its Nov→Feb change raw={raw_chg:.4f} pp; with SC netted from Nov numerator only={net_chg:.4f} pp')
net_full = panel.s_feb[big] - 100*(panel.n_nov[big]-scw.onet_task_count.get(big,0))/(999875-24715)
P(f'  with SC netted from numerator and the November base (999,875−24,715): {net_full:.4f} pp  [steward convention]')
P(f'  SC named nodes inside sample A: {len(set(scw.index)&set(A.index))}, conversations={scw.onet_task_count.reindex(list(set(scw.index)&set(A.index))).sum():.0f}')

# ---- 10. Education and use_case controls --------------------------------------------------
P('== 10. Controls')
edu = wide(nov, 'onet_task::human_education_years')
P(f'  human_education_years keys={len(edu)} vars={list(edu.columns)}')
e = edu['onet_task_human_education_years_mean'].reindex(A.index)
P(f'  edu mean published for {int(e.notna().sum())} of {len(A)}; range {e.min():.3f}–{e.max():.3f}')
ya = A.yes.fillna(0)
P(f'  corr(yes_pct, edu) on A (only-no as 0, as steward): unweighted={np.corrcoef(ya, e)[0,1]:.4f}; weighted={np.cov(ya, e, aweights=A.n_nov)[0,1]/np.sqrt(np.cov(ya,ya,aweights=A.n_nov)[0,1]*np.cov(e,e,aweights=A.n_nov)[0,1]):.4f}')
eb = e.reindex(B.index)
P(f'  corr(yes_pct, edu) on B (published yes only): unweighted={np.corrcoef(B.yes, eb)[0,1]:.4f}')
ucp, _ = succ(nov)  # placeholder to reuse parser: use_case parsed below
g = nov[(nov.geography == 'global') & (nov.facet == 'onet_task::use_case') & (nov.variable == 'onet_task_use_case_pct')].copy()
parts = g.cluster_name.str.rsplit('::', n=1, expand=True); g['task'] = parts[0].str.strip().str.lower(); g['cat'] = parts[1]
uw = g.pivot(index='task', columns='cat', values='value').reindex(A.index)
P(f'  use_case cats={list(uw.columns)}; work published for {int(uw.work.notna().sum())} of {len(A)}; median published work={uw.work.median():.2f}; median with folded=0: {uw.work.fillna(0).median():.2f}')

with open(OUT, 'w') as f:
    f.write('\n'.join(lines) + '\n')
P(f'-- written {OUT}')
