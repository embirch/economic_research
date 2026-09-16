# External data availability check (7 Sep 2026)

| Source | Needed for | Status | Notes |
|---|---|---|---|
| Hofstede 6-D scores (geerthofstede.com, "6 dimensions for website-2015-08-16.csv") | RQ1 culture measures (power distance, individualism, uncertainty avoidance) | Confirmed, free for research | "Researchers can use them without asking for permission." Version 2015-12-08; ~100 countries; the underlying surveys are old (IBM 1967-73 plus later replications), which stays a stated limitation. |
| GLOBE 2004 Phase 2 society-level data (globeproject.com, "Aggregated Societal Level Data for Society Culture Scales" and "... Leadership Scales", .xls) | RQ1 (power-distance practices; participative leadership) | Confirmed, downloadable | 62 societies; no explicit licence, consult the 2006 scale guidelines. |
| World Bank WDI IT.NET.USER.ZS (internet users % of population) via API | Internet-diffusion baseline; access control | Confirmed | 6,625 records 2000-2024, JSON API, no key. |
| BLS OEWS May 2025 state file (oesm25st.zip) | RQ2 state occupation composition | Confirmed, public | All occupations by state, employment and wages. |
| Eloundou et al. 2023 exposure scores (github.com/openai/GPTs-are-GPTs, occ_level.csv, MIT) | Forecast-error test | Confirmed, occupation level | Task-level file to verify in the repo's data folder. |
| Meta-Gallup State of Social Connections 2023 | Loneliness by country | Country values exist in the PDF and an interactive map; no CSV | 142 countries, ~1,000 per country. Question wording to take from the PDF. Gallup World Poll microdata is licensed and NOT available. |
| CDC BRFSS 2022 social isolation and loneliness module | State loneliness | To confirm | Optional module, roughly 30 states; CDC publishes prevalence by state. |
| ONS Opinions and Lifestyle Survey, loneliness by region | UK regional cut | To confirm | Quarterly since 2020; published tables. |
| World Values Survey wave 7 | Instruction-following item; disclosure norms | To confirm | Free registration; item availability by country to check. |
| ITU / ATUS / UK LFS hours by occupation | Time-rebound design | Not checked | Only needed if RQ4 option A survives scoring. |
