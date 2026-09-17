"""post1 · the C8 (Seychelles) and §10 (concentration) figures the BRIEF pre-registers.

These numbers are quoted in `posts/post1/BRIEF.md` C8 and §10 and in
`posts/post1/notes/feasibility.md` §1 C8 / §5, and they set two pre-registered
sensitivity cuts (drop tasks where `SC` exceeds 10% / 20% of the task's global count) and
one leave-out (the ten largest tasks by usage mass). They were first computed in a scratch
script; this file makes them re-runnable with a check block.

Grain and conventions: `geography == 'global'` for the wave frames, `geo_id == 'SC'` at
`geography == 'country'` for Seychelles (ISO-2 in `release_2026_01_15`; `SYC` returns 0
rows — `data/ATLAS.md` §Traps 14, log (h) 5). Intersections are global only, so netting
`SC` reaches the task WEIGHTS and never the per-task rates.

What it computes: base residual node masses; the top-10 task concentration on both
denominators; SC's node set, its share of each task's global count, the weight shift from
netting it, and the analysis-set task sets above 10 / 20 / 50% with their usage mass by
usage-weighted wage quartile; and the intersection count split (classified / `none` /
`not_classified`) over named tasks against the wave `collaboration_count`.

Wage quartiles are drawn on the C6 equal-split wage exactly as in
`data/replication/post1_joins_c5_c7.py`. The classified base count `b5` is used only to
define the analysis set (a task must have at least one classified-pattern cell) and as a
denominator; no automation share, no quartile automation rate and no top-minus-bottom
difference is computed anywhere in this script.

Run from the repository root:  python data/replication/post1_c8_concentration.py
Output: data/replication/results/post1_c8_concentration.txt
"""

import numpy as np
import pandas as pd

ROOT = '/workspace/economic_research/'
OUTPATH = ROOT + 'data/replication/results/post1_c8_concentration.txt'
OUT = open(OUTPATH, 'w')


def p(*a):
    print(*a)
    print(*a, file=OUT)


AUTO = {'directive', 'feedback loop'}
AUG = {'learning', 'task iteration', 'validation'}
CLASSIFIED = AUTO | AUG
RESID = {'none', 'not_classified'}
WAVES = {
    'aug2025': (ROOT + 'data/cache/release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv', 'csv'),
    'nov2025': (ROOT + 'data/cache/release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.parquet', 'pq'),
    'feb2026': (ROOT + 'data/cache/release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.parquet', 'pq'),
}


def load(path, kind):
    if kind == 'csv':
        df = pd.read_csv(path, keep_default_na=False, na_values=[], dtype=str)
    else:
        df = pd.read_parquet(path)
        for c in df.columns:
            if c != 'value':
                df[c] = df[c].astype(str)
    df['value'] = pd.to_numeric(df['value'])
    return df


# ---------- the wage, for the quartile boundaries only (C5 + C6) ----------
on = pd.read_csv(ROOT + 'data/cache/release_2025_09_15/data/intermediate/onet_task_statements.csv',
                 keep_default_na=False, na_values=[], dtype=str)
on['key'] = on['Task'].str.lower().str.strip()
h10 = on.groupby('key')['O*NET-SOC Code'].apply(lambda s: sorted(set(s)))
wg = pd.read_csv(ROOT + 'data/cache/release_2025_02_10/wage_data.csv', keep_default_na=False, na_values=[])
w10 = (wg[wg.MedianSalary > 100].set_index('SOCcode').MedianSalary / 2080.0)


def wage_of(key):
    vals = [float(w10[h]) for h in h10[key] if h in w10.index] if key in h10.index else []
    return float(np.mean(vals)) if vals else np.nan


got = {}
for w, (path, kind) in WAVES.items():
    df = load(path, kind)
    g = df[df.geography == 'global']
    bp = g[(g.facet == 'onet_task') & (g.variable == 'onet_task_pct')].set_index('cluster_name').value
    bc = g[(g.facet == 'onet_task') & (g.variable == 'onet_task_count')].set_index('cluster_name').value
    named = bp[~bp.index.isin(RESID)]
    p('%s base residual node mass: none %.4f  not_classified %.4f ; named %.4f'
      % (w, bp.get('none', float('nan')), bp.get('not_classified', float('nan')), named.sum()))
    top10 = named.sort_values(ascending=False).head(10).sum()
    p('   top-10 named tasks: %.4f of 100 ; %.4f%% of named mass' % (top10, top10 / named.sum() * 100))
    got[w] = dict(top10=top10, top10_named=top10 / named.sum() * 100,
                  none=float(bp.get('none')), nc=float(bp.get('not_classified')), named=named.sum())

    # intersection count split over named tasks, against the wave collaboration facet
    ix = g[g.facet == 'onet_task::collaboration'].copy()
    parts = ix.cluster_name.str.rsplit('::', n=1)
    ix['task'] = parts.str[0]
    ix['pattern'] = parts.str[1]
    cnt = ix[(~ix.task.isin(RESID)) & ix.variable.str.endswith('_count')]
    tab = cnt.pivot_table(index='task', columns='pattern', values='value', aggfunc='sum').fillna(0.0)
    tot = tab.sum(0)
    cls = tot[[c for c in tab.columns if c in CLASSIFIED]].sum()
    base_named = bc[~bc.index.isin(RESID)].sum()
    col = g[(g.facet == 'collaboration') & (g.variable == 'collaboration_count')].set_index('cluster_name').value
    p('%s | intersection counts over named tasks: total %.0f ; classified %.0f ; none %.0f ; not_classified %.0f'
      % (w, tot.sum(), cls, tot.get('none', 0.0), tot.get('not_classified', 0.0)))
    p('   base named onet_task_count %.0f -> intersection publishes %.2f%% of it ; classified %.2f%%'
      % (base_named, tot.sum() / base_named * 100, cls / tot.sum() * 100))
    p('   wave collaboration_count: total %.0f ; classified %.0f ; base facet residual none %.0f not_classified %.0f'
      % (col.sum(), col[[c for c in col.index if c in CLASSIFIED]].sum(),
         col.get('none', 0.0), col.get('not_classified', 0.0)))
    got[w].update(ix_total=tot.sum(), ix_classified=cls, ix_nc=float(tot.get('not_classified', 0.0)),
                  base_named=base_named, ix_share=tot.sum() / base_named * 100)
    if w == 'nov2025':
        nov = dict(df=df, bp=bp, bc=bc, tab=tab)

# ---------- C8: Seychelles in release_2026_01_15 ----------
p('=' * 70)
df, bp, bc, tab = nov['df'], nov['bp'], nov['bc'], nov['tab']
sc = df[(df.geo_id == 'SC') & (df.geography == 'country')]
scp = sc[(sc.facet == 'onet_task') & (sc.variable == 'onet_task_pct')].set_index('cluster_name').value
scc = sc[(sc.facet == 'onet_task') & (sc.variable == 'onet_task_count')].set_index('cluster_name').value
usage = sc[(sc.facet == 'country') & (sc.variable == 'usage_count')].value.iloc[0]
sc_named = scc[~scc.index.isin(RESID)]
p('SC onet_task nodes %d ; none %.4f not_classified %.4f ; named nodes %d carrying %.4f%% of SC mass'
  % (len(scp), scp.get('none', float('nan')), scp.get('not_classified', float('nan')),
     len(sc_named), sc_named.sum() / scc.sum() * 100))
p('SC named counts sum %.0f of SC usage %.0f' % (sc_named.sum(), usage))
gbc_named = bc[~bc.index.isin(RESID)]
inter = sc_named.index.intersection(gbc_named.index)
netted = gbc_named.copy()
netted.loc[inter] = netted.loc[inter] - sc_named.loc[inter]
shift = (netted / netted.sum() * 100) - (gbc_named / gbc_named.sum() * 100)
p('netting SC named task weights: %d of %d SC named nodes are in the global named set ; max |shift| %.4f pp on %s ; mean |shift| %.5f'
  % (len(inter), len(sc_named), shift.abs().max(), shift.abs().idxmax()[:52], shift.abs().mean()))
p('SC named mass as share of global named counts: %.4f%%' % (sc_named.sum() / gbc_named.sum() * 100))
share = (scc / bc.reindex(scc.index)).dropna() * 100
p('SC share of the GLOBAL count of the tasks it publishes (top 6):')
for t, v in share.sort_values(ascending=False).head(6).items():
    p('   %.1f%%  %s' % (v, t[:70]))
p('median SC share over its %d nodes: %.2f%%' % (len(share), share.median()))

# analysis set (wage + at least one classified cell) and its usage-weighted wage quartiles
cols5 = [c for c in tab.columns if c in CLASSIFIED]
b5 = tab[cols5].sum(1)
an = pd.DataFrame({'task': gbc_named.index})
an['w'] = bp.reindex(an.task).values
an['b5'] = b5.reindex(an.task).fillna(0.0).values
an['wage'] = [wage_of(t.lower().strip()) for t in an.task]
an = an[(an.b5 > 0) & an.wage.notna()].sort_values('wage')
cw = an.w.cumsum() / an.w.sum()
an['q'] = np.minimum(np.searchsorted([0.25, 0.5, 0.75], cw, side='left') + 1, 4)
p('analysis set rebuilt here: %d tasks, %.4f pp of the wave (cross-check against 2,075 / 89.9892)'
  % (len(an), an.w.sum()))
an['sc_share'] = share.reindex(an.task).fillna(0.0).values
sc_sets = {}
for thr in (50, 20, 10):
    s = an[an.sc_share > thr]
    q4, q1 = s[s.q == 4], s[s.q == 1]
    p("SC>%d%% of a task's global count: %d tasks in the analysis set, %.3f pp of wave mass, quartiles %s"
      % (thr, len(s), s.w.sum(), sorted(s.q.unique())))
    p('     of which Q4: %d tasks, %.3f pp ; Q1: %d' % (len(q4), q4.w.sum(), len(q1)))
    sc_sets[thr] = dict(n=len(s), mass=s.w.sum(), q4n=len(q4), q4mass=q4.w.sum())

# ---------- check block ----------
p('=' * 70)
p('CHECKS (expected = posts/post1/notes/feasibility.md §1/§5 and data/ATLAS.md log (h) 3, 5, 9)')
EXPECT = [
    ('aug2025 top10', got['aug2025']['top10'], 22.9409, 0.0001),
    ('aug2025 top10 of named', got['aug2025']['top10_named'], 24.9703, 0.0001),
    ('nov2025 top10', got['nov2025']['top10'], 24.2471, 0.0001),
    ('nov2025 top10 of named', got['nov2025']['top10_named'], 25.9288, 0.0001),
    ('feb2026 top10', got['feb2026']['top10'], 19.4410, 0.0001),
    ('feb2026 top10 of named', got['feb2026']['top10_named'], 20.9107, 0.0001),
    ('aug2025 named mass', got['aug2025']['named'], 91.8727, 0.0001),
    ('nov2025 named mass', got['nov2025']['named'], 93.5144, 0.0001),
    ('feb2026 named mass', got['feb2026']['named'], 92.9714, 0.0001),
    ('aug2025 intersection share of base named', got['aug2025']['ix_share'], 100.0, 0.005),
    ('nov2025 intersection share of base named', got['nov2025']['ix_share'], 100.0, 0.005),
    ('feb2026 intersection share of base named', got['feb2026']['ix_share'], 100.0, 0.005),
    ('aug2025 intersection not_classified', got['aug2025']['ix_nc'], 41134, 0),
    ('nov2025 intersection not_classified', got['nov2025']['ix_nc'], 52693, 0),
    ('feb2026 intersection not_classified', got['feb2026']['ix_nc'], 54893, 0),
    ('SC usage_count', usage, 24715, 0),
    ('SC named nodes', len(sc_named), 65, 0),
    ('SC named share of its own mass', sc_named.sum() / scc.sum() * 100, 93.7609, 0.0001),
    ('SC max weight shift (named)', shift.abs().max(), 0.5823, 0.0001),
    ('SC max share of one global task count', share.max(), 64.3, 0.05),
    ('SC>10% tasks', sc_sets[10]['n'], 23, 0),
    ('SC>10% wave mass', sc_sets[10]['mass'], 11.594, 0.001),
    ('SC>10% Q4 mass', sc_sets[10]['q4mass'], 9.039, 0.001),
    ('SC>20% tasks', sc_sets[20]['n'], 14, 0),
    ('SC>20% wave mass', sc_sets[20]['mass'], 1.966, 0.001),
    ('nov analysis-set tasks', len(an), 2075, 0),
    ('nov analysis-set mass', an.w.sum(), 89.9892, 0.0001),
]
fails = []
for name, gotv, exp, tol in EXPECT:
    ok = abs(float(gotv) - exp) <= tol
    p('  %-42s expected %-10s got %-10s %s' % (name, exp, round(float(gotv), 4), 'OK' if ok else 'FAIL'))
    if not ok:
        fails.append((name, exp, gotv))
OUT.close()
if fails:
    raise SystemExit('CHECK BLOCK FAILED:\n' + '\n'.join('  %s: expected %s, got %s' % f for f in fails))
print('all checks passed -> %s' % OUTPATH)
