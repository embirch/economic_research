# Partner-file viability check, 3 Sep 2026

Files: data/stanford_clusters.csv (974 rows x 600 cols), data/oxford_clusters.csv (472 x 310). Downloaded from Anthropic/enabling-independent-research.

## Politeness facet (Stanford), share of all conversations
blunt 81.5% (203,512) · neutral 11.6% · polite 5.6% · rude 0.9% (2,332) · deferential 0.4% (1,109)

## Politeness x engagement with output (share within each tone)
- rude: critique 46.6%, reject 14.5%, adapt 28.3%, direct_use 1.9%
- blunt: critique 8.9%, reject 0.8%, adapt 32.7%, direct_use 10.9%
- deferential: adapt 58.9%, direct_use 5.5%, reject suppressed
- polite: direct_use 16.8% (highest), adapt 37.7%
Cross-facets populated for all 5 tones on engagement, friction, criticality, agency (agency 'ai_handles_alone' missing for 2 tones).

## Frustration x model behaviour (Oxford; user_frustrated 1..6)
- flattery: 13.6% -> 6.7% -> 4.2% -> 3.7% -> 3.0% -> 2.7%
- challenge: 6.8% -> 16.0% -> 20.8% -> 19.0% -> 30.3% -> 23.5%
- compliance: 95.9% -> 90.9% -> 85.4% -> 75.5% -> 73.4% -> 47.0%
- refusal: 1.9% -> 3.8% -> 4.4% -> 5.2% -> 7.6% -> 10.0%
Caveat: Oxford emotional facets were never validated (card says so); n at level 6 is 1,115.

## Politeness by country and language (P(tone | country/lang))
- Japan: deferential 1.09% (2.4x US), polite 7.5%, blunt 69.8% (lowest of large countries)
- Korea: polite 3.0%, rude 1.58% (highest), blunt 79.5%
- China (language): polite 2.5%, deferential 0.28%
- France/Spanish-speaking: polite 7.7-8.0%; Mexico 8.9%, Colombia 9.5%
- US: deferential 0.46%, polite 4.7%, rude 0.94%
Deferential is populated for only 16 of 153 countries (suppressed elsewhere); polite for 78; rude for 26; blunt for 143.
Implication: the by-country cut works for 'polite' and 'blunt'; 'deferential' only for the biggest countries. Note the classifier judged tone in each language, so cross-language comparison partly measures the classifier's own calibration (ties to values-across-languages).
