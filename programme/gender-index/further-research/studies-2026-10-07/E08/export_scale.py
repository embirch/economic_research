#!/usr/bin/env python3
"""Describe the absolute and proportional scales of the four original rates.

Run after analysis.py. This does not estimate a new model or ratio uncertainty.
Only source-permitted, one-decimal aggregate descriptions are exported.
"""
import csv
import hashlib
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

HERE = Path(__file__).resolve().parent


def rounded(x):
    return str(Decimal(str(x)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))


def main():
    source = HERE / 'results.json'
    rates = json.loads(source.read_text())['raw']['frequent']['rates']
    rows = []
    for sex, indices in [('Men+', (0, 1)), ('Women+', (2, 3))]:
        nonuser, user = [rates[i] for i in indices]
        assert nonuser['release_quality'] == user['release_quality'] == 'A'
        x, y = nonuser['estimate'], user['estimate']
        rows.append(dict(group=sex, nonuser_percent=rounded(100*x),
                         user_percent=rounded(100*y), absolute_gap_pp=rounded(100*(y-x)),
                         user_to_nonuser_ratio=rounded(y/x),
                         result_ids=';'.join(f'frequent.raw.rate.{i}' for i in indices)))
    with (HERE / 'scale-comparison.csv').open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)
    (HERE / 'scale-provenance.json').write_text(json.dumps({
        'source': source.name, 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'formula': 'user/nonuser, from unrounded original rates; absolute gap is 100*(user−nonuser).',
        'scope': 'Descriptive scale explanation. No ratio equality test, new primary outcome, or causal comparison.',
        'rounding': 'One decimal, half up, after all arithmetic.',
    }, indent=2) + '\n')
    print('Exported two descriptive Canadian scale comparisons.')


if __name__ == '__main__':
    main()
