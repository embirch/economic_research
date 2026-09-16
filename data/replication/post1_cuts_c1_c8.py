"""C1-C4 + replication target for post1 feasibility. Writes /tmp/p1/a_out.txt."""
import pandas as pd, numpy as np, io, sys

ROOT = '/workspace/economic_research/'
import os as _os; _os.makedirs('/tmp/p1', exist_ok=True)
OUT = open('/tmp/p1/a_out.txt', 'w')
def p(*a):
    print(*a); print(*a, file=OUT)

WAVES = {
 'aug2025': ('release_2025_09_15', ROOT+'data/cache/release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv', 'csv'),
 'nov2025': ('release_2026_01_15', ROOT+'data/cache/release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.parquet', 'pq'),
 'feb2026': ('release_2026_03_24', ROOT+'data/cache/release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.parquet', 'pq'),
}
AUTO = {'directive', 'feedback loop'}
AUG = {'learning', 'task iteration', 'validation'}
CLASSIFIED = AUTO | AUG
RESID = {'none', 'not_classified'}

def load(path, kind):
    if kind == 'csv':
        df = pd.read_csv(path, keep_default_na=False, na_values=[], dtype=str)
        df['value'] = pd.to_numeric(df['value'])
    else:
        df = pd.read_parquet(path)
        for c in df.columns:
            if c != 'value':
                df[c] = df[c].astype(str)
        df['value'] = pd.to_numeric(df['value'])
    return df

store = {}
for w, (rel, path, kind) in WAVES.items():
    df = load(path, kind)
    p('='*70)
    p(f'[{w}] {rel}  rows={len(df):,}  file={path.split("cache/")[1]}')
    p('  platform_and_product values:', sorted(df.platform_and_product.unique()))
    p('  date_start/date_end:', sorted(df.date_start.unique()), sorted(df.date_end.unique()))
    g = df[df.geography == 'global']
    p('  geography values:', sorted(df.geography.unique()), ' global rows:', len(g))

    # ---- C1/C2/C3 : onet_task::collaboration at global
    ix = g[g.facet == 'onet_task::collaboration'].copy()
    p(f'  C{list(WAVES).index(w)+1}: facet onet_task::collaboration  rows={len(ix):,}'
      f'  variables={sorted(ix.variable.unique())}  levels={sorted(ix.level.unique())}')
    parts = ix.cluster_name.str.rsplit('::', n=1)
    ix['task'] = parts.str[0]; ix['pattern'] = parts.str[1]
    p('     patterns present:', sorted(ix.pattern.unique()))
    p('     distinct base tasks (all):', ix.task.nunique(),
      ' named (excl none/not_classified):', ix[~ix.task.isin(RESID)].task.nunique())
    p('     which residual task node appears:', sorted(set(ix.task) & RESID))
    cnt = ix[ix.variable.str.endswith('_count')]
    pct = ix[ix.variable.str.endswith('_pct')]
    p('     _count rows:', len(cnt), ' min/max count:', cnt.value.min(), cnt.value.max())
    p('     _pct rows:', len(pct), ' min/max pct:', round(pct.value.min(), 4), round(pct.value.max(), 4))
    # per-task pct sums over the patterns
    s = pct.groupby('task').value.sum()
    p('     per-task _pct sum over patterns: median %.4f  min %.4f  max %.4f  (share of base cluster)'
      % (s.median(), s.min(), s.max()))
    # also check geography-level availability of the intersection outside global
    other = df[(df.facet == 'onet_task::collaboration') & (df.geography != 'global')]
    p('     intersection rows outside global:', len(other))

    # ---- C4 : onet_task base facet at global
    base = g[(g.facet == 'onet_task')].copy()
    p('  C4: facet onet_task at global  rows=%d  variables=%s' % (len(base), sorted(base.variable.unique())))
    bp = base[base.variable == 'onet_task_pct']
    bc = base[base.variable == 'onet_task_count']
    p('     distinct task nodes (all): %d  named: %d  residual nodes present: %s'
      % (bp.cluster_name.nunique(), bp[~bp.cluster_name.isin(RESID)].cluster_name.nunique(),
         sorted(set(bp.cluster_name) & RESID)))
    p('     onet_task_pct sum (all nodes): %.6f   named only: %.4f'
      % (bp.value.sum(), bp[~bp.cluster_name.isin(RESID)].value.sum()))
    p('     onet_task_count: min %s  sum %s' % (bc.value.min(), f'{bc.value.sum():,.0f}'))
    # node-set relations
    ixtasks = set(ix.task); btasks = set(bp.cluster_name)
    p('     intersection tasks not in base facet: %d ; base tasks not in intersection: %d %s'
      % (len(ixtasks - btasks), len(btasks - ixtasks), sorted(btasks - ixtasks)[:5]))

    # ---- automation per task (counts base and pct base), named tasks only
    ixn = ix[~ix.task.isin(RESID)]
    cw = ixn[ixn.variable.str.endswith('_count')].pivot_table(index='task', columns='pattern', values='value', aggfunc='sum').fillna(0.0)
    pw = ixn[ixn.variable.str.endswith('_pct')].pivot_table(index='task', columns='pattern', values='value', aggfunc='sum').fillna(0.0)
    for name, tab in (('count', cw), ('pct', pw)):
        cols5 = [c for c in tab.columns if c in CLASSIFIED]
        colsa = [c for c in tab.columns if c in AUTO]
        b5 = tab[cols5].sum(1)
        p('     per-task automation on %s: tasks with b5>0: %d of %d' % (name, (b5 > 0).sum(), len(tab)))
    store[w] = dict(df=df, g=g, ix=ix, base=base, bp=bp, bc=bc, cw=cw, pw=pw)

# ---------- 2. Replication target: global collaboration split ----------
p('='*70); p('REPLICATION (2i): global collaboration split per wave')
for w in WAVES:
    g = store[w]['g']
    col = g[(g.facet == 'collaboration') & (g.variable == 'collaboration_pct')]
    s = col.set_index('cluster_name').value
    p(f'[{w}] collaboration_pct nodes: {dict(s.round(4))}  sum={s.sum():.4f}')
    allbase = s.sum()
    five = s[[i for i in s.index if i in CLASSIFIED]].sum()
    auto_all = s[[i for i in s.index if i in AUTO]].sum() / allbase * 100
    auto_5 = s[[i for i in s.index if i in AUTO]].sum() / five * 100
    augm_all = s[[i for i in s.index if i in AUG]].sum() / allbase * 100
    p('   automation: all-pattern base %.4f | five-classified base %.4f | augmentation(all) %.4f'
      % (auto_all, auto_5, augm_all))
    store[w]['auto_all'] = auto_all; store[w]['auto_5'] = auto_5

p('='*70); p('REPLICATION (2ii): usage-weighted mean of per-task automation vs the wave global value')
for w in WAVES:
    st = store[w]
    bp = st['bp']; cw = st['cw']; pw = st['pw']
    wt = bp[~bp.cluster_name.isin(RESID)].set_index('cluster_name').value
    # (a) sum intersection counts over named tasks
    cols5 = [c for c in cw.columns if c in CLASSIFIED]; colsa = [c for c in cw.columns if c in AUTO]
    tot = cw.sum(0)
    a_from_counts_5 = tot[colsa].sum() / tot[cols5].sum() * 100
    a_from_counts_all = tot[colsa].sum() / tot.sum() * 100
    # (b) usage-weighted mean of per-task automation share (five-pattern base), weights onet_task_pct
    b5 = pw[cols5].sum(1); a5 = pw[colsa].sum(1)
    ok = b5 > 0
    tw = wt.reindex(pw.index).fillna(0.0)
    wa5 = np.average((a5[ok] / b5[ok]) * 100, weights=tw[ok])
    ball = pw.sum(1); wall = np.average((a5 / ball.replace(0, np.nan)).fillna(0) * 100, weights=tw)
    # (c) same but weights = intersection base counts
    basecnt = cw.sum(1)
    wa5_c = np.average((a5[ok] / b5[ok]) * 100, weights=basecnt[ok])
    p(f'[{w}] global (collaboration facet): five-pattern {st["auto_5"]:.4f} | all-pattern {st["auto_all"]:.4f}')
    p('   (a) sum of intersection _count over named tasks -> five-pattern %.4f | all-pattern %.4f'
      % (a_from_counts_5, a_from_counts_all))
    p('   (b) onet_task_pct-weighted mean of per-task five-pattern automation -> %.4f  (diff %+.4f)'
      % (wa5, wa5 - st['auto_5']))
    p('   (c) intersection-count-weighted mean of the same -> %.4f  (diff %+.4f)'
      % (wa5_c, wa5_c - st['auto_5']))
    p('   named-task usage mass covered by the intersection: %.4f of 100' % tw[ok].sum())

# ---------- C8: Seychelles ----------
p('='*70); p('C8: Seychelles in release_2026_01_15')
df = store['nov2025']['df']
for gid in ('SC', 'SYC'):
    sub = df[df.geo_id == gid]
    p(f'  geo_id=="{gid}": rows={len(sub)}  facets={sorted(sub.facet.unique())[:8]}')
sc = df[(df.geo_id == 'SC') & (df.geography == 'country')]
u = sc[sc.facet == 'country']
p('  SC country facet rows:', dict(zip(u.variable, u.value.round(5))))
sct = sc[(sc.facet == 'onet_task')]
p('  SC onet_task rows: %d ; task nodes: %d ; onet_task_count sum %.0f ; onet_task_pct sum %.4f'
  % (len(sct), sct[sct.variable == 'onet_task_pct'].cluster_name.nunique(),
     sct[sct.variable == 'onet_task_count'].value.sum(), sct[sct.variable == 'onet_task_pct'].value.sum()))
p('  SC onet_task::collaboration rows:', len(df[(df.geo_id == 'SC') & (df.facet == 'onet_task::collaboration')]))
scc = sc[(sc.facet == 'collaboration')]
p('  SC collaboration rows: %d  counts=%s' % (len(scc), dict(zip(scc[scc.variable=='collaboration_count'].cluster_name, scc[scc.variable=='collaboration_count'].value))))
# global collaboration netting
gl = store['nov2025']['g']
gc = gl[(gl.facet == 'collaboration') & (gl.variable == 'collaboration_count')].set_index('cluster_name').value
sccnt = scc[scc.variable == 'collaboration_count'].set_index('cluster_name').value.reindex(gc.index).fillna(0.0)
net = gc - sccnt
before = gc / gc.sum() * 100; after = net / net.sum() * 100
p('  netting SC out of the global collaboration mix: max |shift| %.4f pp (%s)'
  % ((after - before).abs().max(), (after - before).abs().idxmax()))
p('  automation five-pattern before %.4f after %.4f'
  % (gc[[i for i in gc.index if i in AUTO]].sum()/gc[[i for i in gc.index if i in CLASSIFIED]].sum()*100,
     net[[i for i in net.index if i in AUTO]].sum()/net[[i for i in net.index if i in CLASSIFIED]].sum()*100))
# task weight netting feasibility
gbp = store['nov2025']['bp'].set_index('cluster_name').value
gbc = store['nov2025']['bc'].set_index('cluster_name').value
sct_c = sct[sct.variable == 'onet_task_count'].set_index('cluster_name').value
inter = sct_c.index.intersection(gbc.index)
p('  SC published task nodes: %d ; of these in the global task set: %d ; SC count sum %.0f of SC usage_count %s'
  % (len(sct_c), len(inter), sct_c.sum(), u[u.variable == 'usage_count'].value.values))
nb = gbc.copy(); nb.loc[inter] = nb.loc[inter] - sct_c.loc[inter]
p('  netting SC task counts: max |weight shift| %.5f pp over named tasks'
  % ((nb/nb.sum()*100 - gbc/gbc.sum()*100).abs().max()))
OUT.close()
