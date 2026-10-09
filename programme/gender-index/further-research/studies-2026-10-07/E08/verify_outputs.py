#!/usr/bin/env python3
"""Aggregate delivery checks; independent raw-file review is a separate task."""
import csv
import hashlib
import json
import re
from pathlib import Path
import numpy as np

P = Path(__file__).resolve().parent
r = json.loads((P/'results.json').read_text())
tables = list(csv.DictReader((P/'public-tables.csv').open()))
index = {x['result_id']: x for x in tables}
fig = json.loads((P/'figure-specs.json').read_text())
env = json.loads((P/'environment.json').read_text())
assert len(index) == len(tables) == 101
assert env['script_sha256'] == hashlib.sha256((P/'analysis.py').read_bytes()).hexdigest()
checks = []
for name, obj in r['raw'].items():
    rates = np.array([x['estimate'] for x in obj['rates']])
    c = np.array([1, -1, -1, 1])
    assert abs(c @ rates-obj['interaction']['estimate']) < 1e-12
    assert abs(c @ np.array(obj['rate_covariance']) @ c-obj['interaction']['se']**2) < 1e-12
    assert all(x['finite_replicates'] == 1000 and x['release_quality'] == 'A' for x in obj['rates'])
    assert all(not x['normal_interval_outside_unit_range'] and not x['boundary_event_count'] for x in obj['rates'])
    for g in range(4):
        vals = [x for x in r['distributions'][name] if x['group'] == obj['rates'][g]['group']]
        assert abs(sum(x['estimate'] for x in vals)-1) < 1e-12
    checks.append(name+': raw contrast/covariance, domain quality and frequency totals pass')
for name, target in r['common_composition'].items():
    for outcome, obj in target['outcomes'].items():
        if 'failed' in name:
            assert obj['standardized_interaction']['finite_replicates'] == 998
            assert obj['standardized_interaction']['se'] is None
        else:
            C = np.array(obj['joint_covariance'])
            assert np.max(np.abs(C-C.T)) < 1e-12
            assert np.linalg.eigvalsh(C).min() > -1e-12
            for contrast, coefficients in [('restriction_change', [-1, 1, 0, 0, 0]), ('composition_change', [0, -1, 1, 0, 0])]:
                a = np.array(coefficients)
                assert abs(a @ C @ a-obj[contrast]['se']**2) < 1e-12
            assert obj['decomposition_max_error'] < 1e-12
    checks.append(name+': joint covariance/decomposition or preserved failed replicates pass')
for x in tables:
    if x['quality'] == 'F' or 'Companion suppression' in x['note']:
        assert all(x[k] == '' for k in ['estimate', 'low', 'high', 'events'])
    elif x['quality'] == 'E':
        assert 'Use with caution' in x['note']
assert not index['difficult.distribution.1.3']['estimate']
assert not index['difficult.distribution.1.4']['estimate']
for figure in fig['figures']:
    for x in figure['rows']:
        source = index[x['result_id']]
        assert source['estimate'] and source['quality'] != 'F'
        assert all(float(source[k]) == x[v] for k, v in [('estimate', 'value'), ('low', 'low'), ('high', 'high')])
        if source['quality'] == 'E':
            assert 'caution' in figure['footnote'].lower()
text = (P/'manuscript.md').read_text()
word_count = len(text.split())
# Coverage is adjudicated editorially, not by a word-count quota.
assert word_count > 500
assert '\u2014' not in text
assert set(re.findall(r'<!-- FIGURE: ([\w-]+) -->', text)) == {f['id'] for f in fig['figures']}
checks += ['Release suppression and companion suppression pass', 'All figure rows match rounded public tables; E warnings retained',
           'Eight percentile rows confirmed', 'Manuscript length, no-em-dash and figure markers pass']
assert len(list(csv.DictReader((P/'percentile-sensitivity.csv').open()))) == 8
result = {'date': '2026-10-08', 'status': 'pass', 'checks': checks, 'manuscript_word_count': word_count,
          'public_rows': len(tables), 'figures': len(fig['figures']),
          'scope': 'Author aggregate/output checks; not independent raw-data or manuscript review'}
(P/'verification.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
