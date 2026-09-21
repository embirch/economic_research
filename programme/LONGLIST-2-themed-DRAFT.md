# Long-list 2 · themed · DRAFT for the human's read, 21 September 2026

Drafted by the human's assistant from `programme/LEDGER.md`, `programme/THREADS.md`, `data/ATLAS.md`, `data/releases/*.md` and `wiki/reports/*.md`, to the themes note `room/human-2026-09-21-longlist-themes.md`. **Not yet steward-confirmed and not yet referee-swept.** Every "Steward feasibility line" is marked PENDING; every "External literature checked" is marked PENDING for the lead. Entry format follows `programme/LONGLIST.md`; ids are `TL-nn` until the referee's sweep renumbers survivors into the LL series.

## The data facts that shape this list (from the atlas and the release profiles)

- **No demographics anywhere in any release** (`data/ATLAS.md:376`, "Cuts that do not exist" 28). No sex, age, tenure, tier, user or account field. The June 2026 survey chapter (9,700 linked respondents, the gender results) is **unreleased** (`data/releases/release_2026_06_26.md:492–495`). So a women-and-AI post cannot be person-level on Anthropic data. It can be occupation-level (the female share of the occupations whose tasks are used), country-level on a second provider's public gender file (OpenAI Signals, month × country × gender, `data/ATLAS.md:1155`), or an analysis whose object is Anthropic's published aggregate figures (June 2026 Fig 3.8: women's Claude Code share 0.24 SD lower, automation share 0.33 SD or 7.3 pp lower, net of occupation).
- **Use case** (work / personal / coursework) exists from November 2025 at global, country and sub-national grain, and at every task, request and occupation node at global in June 2026; **absent from August 2025**. `use_case × collaboration` is never published as a cross, but both attach to the same task and request nodes at global, so a node-level join exists.
- **Collaboration** (directive, feedback loop, task iteration, learning, validation, none) is the one taxonomy that never changed and ships at global, country and state in every long wave; by task and request at global; by detailed occupation (718) at global in June 2026.
- **Relational clusters** (Companionship & General Conversation; Existential, Relational and Emotional Support; Personal AI Assistant; Hobbies & Lifestyle) are named request nodes in June 2026 with all 51 metrics at global and at country (ragged).
- **Outcomes**: `task_success` (binary, Claude-judged) at all three geographies and at task and request nodes at global in November 2025 and February 2026, absent in June 2026; `human_only_time` and `human_with_ai_time` at all grains in those two waves and as means at every node in June 2026; `human_education_years` and `ai_education_years` likewise. No tenure, expertise, cohort or tier anywhere. `labor_market_impacts/` carries observed exposure for 756 occupations.
- **Partner facet tables** (`Anthropic/enabling-independent-research`): Stanford's `human_agency_level`, `friction_*`, `task_criticality`, `country`, `lang`; Oxford's 17 user-experience and 9 model-behaviour facets; METR's success × counterfactual time × supervision. Cluster × facet only, April–May 2026, not joinable to the Index, affect facets unvalidated.

---

# Theme T1 · Women and AI

## TL-01 — Is AI arriving in women's work?

**Thread.** T1 (adoption: what AI is used for and by whom), with T5 (exposure) and T3.

**Ledger items.** `L-2026-06-R6-18` *open* (women use Claude differently; the 12% is never discussed as a power constraint); `L-2026-05-CASSA-17` *open* (gender covariate constructed, never used); `L-2026-03-LMI` demographics of exposed workers computed on CPS, never on use.

**Closest existing answer and why it falls short.** June 2026 report p. 29 (Fig 3.8): among linked survey respondents women delegate less and use Claude Code less, net of occupation. That is a statement about *women as users*. Nothing in the corpus asks whether the *work women do* is being reached: whether usage per worker, delegation, success and time saved differ between female-dominated and male-dominated occupations. The March 2026 exposure paper says exposed workers are 16 points more likely to be female, on CPS, using a usage-weighted measure, but never reports use itself by the sex composition of the occupation.

**External literature checked.** PENDING (lead): Humlum & Vestergaard on the gender gap in ChatGPT adoption in Denmark; Bick, Blandin & Deming's survey gender gap; Otis et al. on gender differences in generative-AI use.

**Why it matters.** Women are concentrated in the occupations Anthropic's own survey respondents say AI "will never do": care, teaching, administration, relational work. If AI's use, and its measured time savings, are concentrated in male-dominated occupations, the productivity gains and the exposure both fall on men's work first, and every aggregate in the Index carries that tilt silently. If instead female-dominated administrative and clerical occupations are among the most-used, the June result about women as *users* sits beside a different fact about women's *jobs*. For the general reader: is AI showing up in the jobs women hold? For the economist: the sex composition of observed exposure and of measured productivity gains, which the scenario paper's distributional items (`L-2026-09-SCPA-14`) name and never compute.

**Contribution.** *If it holds* (use and time saved rise with the male share of an occupation, occupation family held fixed): the first published sex-composition gradient in observed AI use, and a correction to any exposure aggregate that treats occupations as sex-blind. *If it fails* (use is higher in female-dominated occupations): the June person-level gap and an occupation-level reversal, which is a finding about who inside those occupations is using it. *If null*: use is sex-blind at the occupation level; the gender gap is a user gap, not a work gap.

**Economic Index cut (proposed).** June 2026 `soc_occupation` L0 (718 detailed occupations, global): usage share, the eight `collaboration_*` metrics, `use_case_*_pct`, the two time means, education years. November 2025 and February 2026 `soc_occupation` shares for persistence. Normalised per worker by OEWS employment.

**Supplementary data.** BLS CPS Table 11 (employed persons by detailed occupation and sex, annual, public; BLS blocks non-browser downloads, so a manual fetch is logged), joined on 2018 SOC via the O*NET-SOC crosswalk; OEWS employment for the denominator.

**Steward feasibility line.** PENDING.

**Biggest risk.** Composition, again: Computer & Mathematical is male-dominated and the most-used family, so a raw gradient is the coding gradient wearing a sex label. The design must hold the major group fixed (within-group contrast, as post 1's leg (b)) and report the leave-one-group-out series. Second: the female share is an attribute of the workforce, not of the user; the post says so in the definition.

**Mentor interests.** Massenkoff (who is exposed; people and places); the Institute's distributional questions.

**Institute agenda.** PENDING.

---

## TL-02 — AI could do women's work. Is it doing it?

**Thread.** T5 (exposure and observed impacts), with T1.

**Ledger items.** `L-2026-03-LMI-06` *open*; `L-2026-03-LMIA-09` *open*; `L-2026-09-SCPA-14` *open* (heterogeneity across demographic groups named and not computed).

**Closest existing answer and why it falls short.** The March 2026 labour-market paper builds observed exposure from theoretical capability times actual use and reports that exposed workers skew female on CPS. It never reports the *gap* between what AI could do (the theoretical measure) and what it is used for (the observed one) by the sex composition of the occupation. Its own Figure 5 shows the zero-exposure group differs by sex before ChatGPT existed, which is the artefact this post has to handle first.

**External literature checked.** PENDING (lead): Eloundou, Manning, Mishkin & Rock (2023); Felten, Raj & Seamans occupational exposure by demographics.

**Why it matters.** Exposure measures are used to say who is at risk. A theoretical measure says women's occupations are highly exposed (clerical, administrative, customer-facing text work). If observed use lags potential more in those occupations than in men's, then the risk arrives later, or through a different channel, in women's work, and any policy timed to the theoretical measure is early for half the workforce. If the lag is the same, the theoretical measure is sex-blind in practice, which is worth knowing too.

**Contribution.** *If it holds* (observed falls short of theoretical more in female-dominated occupations): the sex composition of the adoption lag, a new quantity. *If it fails* (the shortfall is larger in male-dominated occupations): observed use is running ahead of potential in men's work, which is the coding story again and says so. *If null*: the lag is sex-blind at the occupation level.

**Economic Index cut (proposed).** `labor_market_impacts/` observed exposure (756 SOC occupations); the Eloundou β and ζ ratings per occupation (public repository); CPS female share by occupation.

**Supplementary data.** Eloundou et al. GitHub release; BLS CPS Table 11; OEWS employment.

**Steward feasibility line.** PENDING. Known issue: the two labour-market files share no key with the task file, and 92% of task rows are zero after the usage floor (`data/ATLAS.md:676`).

**Biggest risk.** The zero-exposure artefact: occupations below the usage threshold read as "not used" and skew female. The design must treat the floor as censoring, report results with and without the censored group, and never read a zero as a zero.

**Mentor interests.** Massenkoff (the exposure paper is his).

**Institute agenda.** PENDING.

---

## TL-03 — Where is the gender gap in AI use widest, and why?

**Thread.** T2 (geography), with T1 and T8 (measurement: Claude is not AI).

**Ledger items.** `L-2026-06-R6-18` *open*; `L-2025-09-R3-21` *open* (benefits accruing to already-rich economies); no Anthropic geography of gender exists.

**Closest existing answer and why it falls short.** Anthropic publishes no gender by country. OpenAI's Signals release publishes the share of messages by gender, by country and month, and describes the gap without explaining it. Nothing relates the size of a country's gender gap to what AI is used for there, which Anthropic's country files carry (coding share, delegation share, personal share).

**External literature checked.** PENDING (lead): the OpenAI "How people use ChatGPT" paper's gender series; Humlum & Vestergaard; World Bank and ITU gender digital-divide indicators.

**Why it matters.** Who captures value from AI starts with who uses it. If the gender gap is widest where AI use is coding-heavy and delegation-heavy, the gap is a work-mix gap and closes as the mix broadens; if it is widest where female labour-force participation or the tertiary-education gap is largest, it is a structural gap that the mix will not close. Those are different policies. This is the one place a gender question can be asked at scale with public data, and the answer is about which force is invisible behind the published map.

**Contribution.** *If it holds* (the gap tracks the country's use mix after participation and education): the gender gap in AI use is a use-mix gap. *If it fails* (the gap tracks participation and education, not the mix): a structural gap, with the mix as a null. *If null*: neither explains the cross-country variation at the power available, stated with its MDE.

**Economic Index cut (proposed).** Anthropic country files: AUI (2025-09, 2026-06), collaboration by country (every wave), `use_case` by country (2026-01, 2026-03, 2026-06), request Major shares by country (2026-06). OpenAI Signals gender × country × month as the outcome.

**Supplementary data.** OpenAI Signals CSV bundle (CC BY 4.0); World Bank female labour-force participation; UNESCO tertiary gender parity; ITU internet use by sex.

**Steward feasibility line.** PENDING. Known issues: messages are not conversations; country coverage of the two providers differs; the gap is a share of messages, not of users.

**Biggest risk.** Scope: the outcome is another provider's data, so the post must be framed as Anthropic's country profile explaining a published gap, not as an Anthropic gender finding. Second: N of countries with both files may be small; the MDE goes in the pre-registration.

**Mentor interests.** Massenkoff (places); the Institute's access-and-benefit questions.

**Institute agenda.** PENDING.

---

# Theme T2 · Staying human while using AI

## TL-04 — Where is AI a companion, and what explains it?

**Thread.** T1, with T2 and T9.

**Ledger items.** `L-2026-06-R6A-02` *open*; `L-2026-03-S81-11` (no wellbeing study in the corpus); `L-2024-12-CLIO-24` *open*. No ledger item mentions companionship; the absence is the gap.

**Closest existing answer and why it falls short.** The June 2026 appendix names the relational clusters and the report gives their global size. No publication maps them, profiles how they are worked (delegated or collaborated, autonomy, turns), or relates them to anything about the place.

**External literature checked.** PENDING (lead): the Anthropic affective-use post (if it is in the corpus: check), Gallup World Poll loneliness items, the WHO Commission on Social Connection, ONS and BRFSS loneliness series.

**Why it matters.** Companionship is the use people worry about most when they ask whether AI keeps people human or replaces them. Whether it concentrates where people are lonely, where they are young, where they live alone, or where they are simply online more, decides whether it is a symptom, a substitute or a habit. For the economist: a new instrument for a social outcome that official statistics measure slowly and rarely. The post explains, and does not judge.

**Contribution.** *If it holds* (relational use tracks loneliness or living alone after age and internet use): AI companionship as a marker of social isolation, mapped. *If it fails* (it tracks youth and internet intensity only): a habit of the online young, not a symptom. *If null*: the geography of companionship is unexplained by the covariates tried, said with the MDE.

**Economic Index cut (proposed).** June 2026 `request` L2 at country (ragged): the four relational and personal Major nodes, their share, and their collaboration, autonomy and turn metrics. US states where published.

**Supplementary data.** Gallup World Poll loneliness (public aggregates), OECD and UN living-alone rates, UN age structure, ITU internet use, WVS religiosity.

**Steward feasibility line.** PENDING. Known issue: relational use is a few per cent of conversations; suppression will remove small countries, so the identified set and its bias must be stated first.

**Biggest risk.** Suppression and the visitors problem (tourism geographies). Second: the causal arrow is not in the data; the close must say what a survey item (a loneliness scale in the Economic Index survey) would settle.

**Mentor interests.** Massenkoff (places, wellbeing); the survey team.

**Institute agenda.** PENDING.

---

## TL-05 — When people use AI more, do they stop learning from it, or stop delegating to it?

**Thread.** T3 (delegation and autonomy), with T2 and T6.

**Ledger items.** `L-2025-09-R3-26` *open* (the capability-versus-learning-by-doing fork); `L-2025-09-R3-30` *open* (five untested explanations of the country gradient); `L-2026-01-R4-27` *partially answered* (in what contexts do users defer more).

**Closest existing answer and why it falls short.** September 2025 Fig 2.11: countries with more use per person delegate less, after task mix. The report treats augmentation as one thing. It is three: learning (asking to understand), task iteration (doing it together) and validation (checking one's own work). Which of the three rises with adoption is never reported, and the answer decides what "staying human" means as use deepens. The March 2026 tenure result (experienced users iterate more and delegate less, on unreleased data) points one way; the fork in the September report leaves it open.

**External literature checked.** PENDING (lead).

**Why it matters.** If deeper adoption means more *learning*, AI use is building understanding as it spreads. If it means more *iteration* with the same learning share, people are keeping their hands on the work but not necessarily understanding it more. If it means more *validation*, AI is becoming a checker of human work. These are three different futures for skill, and Anthropic's number cannot tell them apart as published.

**Contribution.** *If it holds* (one pattern carries the gradient): the country gradient in delegation is a learning gradient, or an iteration gradient, named. *If it fails* (all three rise together): augmentation is one thing after all, at this grain. *If null*: the gradient is inside the MDE once decomposed.

**Economic Index cut (proposed).** Collaboration by country in every long wave (2025-02 to 2026-06); AUI 2025-09 and 2026-06; task mix at country for the residualisation, as Fig 2.11 does. Same decomposition by US state.

**Supplementary data.** None beyond the 2025-09 income file already cached.

**Steward feasibility line.** PENDING.

**Biggest risk.** Inherited framing: LL-01 was cut for re-running Fig 2.11 with income added. This entry must be a decomposition of the outcome, not a re-specification of the regressor, and must say so. The referee decides.

**Mentor interests.** Massenkoff (people and places).

**Institute agenda.** PENDING.

---

## TL-06 — Is handing over the work the way to get it done?

**Thread.** T4 (task primitives and outcomes), with T3.

**Ledger items.** `L-2026-01-R4-48` *open* ("the direct test of whether delegation is efficient"); `L-2026-06-R6-13` *open*; `L-2026-01-R4-32`, `-33`.

**Closest existing answer and why it falls short.** Task success and the collaboration split are both published at task and request grain in November 2025 and February 2026, and no publication puts them together. The June 2026 survey chapter reports that heavy delegators learn at the same rate as others, on unreleased data, with no MDE.

**External literature checked.** PENDING (lead): the skill-formation RCT (Anthropic, January 2026) on the cost of delegation to learning; Dell'Acqua et al. on when AI help hurts.

**Why it matters.** The whole case for staying in the loop is that it gets better results, or builds skill, or both. If delegated tasks succeed more often than collaborated ones, staying human has a price in outcomes; if they succeed less, the loop is doing work. Either way the number is the one missing from every discussion of automation versus augmentation, and it exists at task level for six thousand tasks.

**Contribution.** *If it holds* (delegated tasks succeed more, task type held fixed): delegation is efficient, and the case for collaboration rests on skill rather than on outcome. *If it fails* (they succeed less): the human in the loop is earning their place. *If null*: no difference at the stated MDE, the honest form of "it depends on the task".

**Economic Index cut (proposed).** `onet_task::collaboration` and `onet_task::task_success` at global L0, November 2025 and February 2026; `request::` likewise; within major group and within request family.

**Supplementary data.** None.

**Steward feasibility line.** PENDING.

**Biggest risk.** Shared source: success and pattern are both read from the same transcript by the same classifier family. Second: ecological, the unit is the task not the conversation, so the design tests whether task-level delegation rates predict task-level success rates and says so.

**Mentor interests.** The Index team's own stated validation.

**Institute agenda.** PENDING.

---

## TL-07 — When do people keep their hands on the wheel?

**Thread.** T3, with T7 (agentic surfaces) and T8.

**Ledger items.** `L-2026-08-IRA-06` (emotional-state facets never validated), `L-2026-08-IRA-21`; `L-2026-01-R4-26` *open*.

**Closest existing answer and why it falls short.** The independent-research pilot released Stanford's facets (`human_agency_level`, `friction_*`, `task_criticality`) and Oxford's user-experience facets as cluster-by-facet tables for April–May 2026, and nobody has analysed them. Anthropic's own autonomy primitive is never related to the stakes of the task.

**External literature checked.** PENDING (lead).

**Why it matters.** The agency question the Institute agenda raises is whether people supervise more when it matters more. If agency rises with task criticality, the pattern is reassuring and specific; if it does not, the high-stakes work is being handed over at the same rate as the trivial. This is the only public data that carries a stakes rating beside an agency rating.

**Contribution.** *If it holds*: agency rises with stakes, quantified. *If it fails*: it does not, and the clusters where it does not are named. *If null*: the facets do not resolve it, with the reason.

**Economic Index cut (proposed).** `Anthropic/enabling-independent-research` Stanford cluster × facet tables; Oxford user facets for the friction and satisfaction side; METR's supervision intensity for the coding surface.

**Supplementary data.** None.

**Steward feasibility line.** PENDING. Known issues: not joinable to the Index; two-way tables only; the facets were never validated; the surfaces covered must be checked.

**Biggest risk.** Construct validity of unvalidated Claude-rated facets, which the post must lead with rather than bury.

**Mentor interests.** The Institute's agency and epistemics questions.

**Institute agenda.** PENDING.

---

## TL-08 — Are people more human with AI in their own lives than at work?

**Thread.** T1, with T3.

**Ledger items.** `L-2025-02-P1-26` *partially answered* (use case by occupation published nowhere); `L-2026-01-R4-49` (54% of Claude.ai conversations are not work); the `use_case × collaboration` cross exists at no grain.

**Closest existing answer and why it falls short.** Anthropic reports the work/personal split and the collaboration split separately in every wave since November 2025. Whether personal use is more collaborative (learning, iterating) or more delegated (one-shot requests) than work use is never reported, though both facets attach to the same task and request nodes.

**External literature checked.** PENDING (lead).

**Why it matters.** "Staying human" is usually argued about work. Half of Claude.ai use is not work. If people delegate their personal lives (recipes, letters, plans) and collaborate on their work, the human-in-the-loop picture is a workplace picture; if the reverse, people are learning and iterating in private and delegating at the office, which is a different story about where judgement is kept. Post 1 found the bottom of the pay scale on Claude.ai is personal use; this asks what that use looks like.

**Contribution.** *If it holds* (personal-heavy nodes are more collaborative): the personal half of AI use is where people keep the loop. *If it fails* (personal use is more delegated): private life is where the hand-over happens first. *If null*: use case does not order the pattern at node level.

**Economic Index cut (proposed).** June 2026: every request and task node at global carries `use_case_*_pct` and the eight `collaboration_*` metrics; November 2025 and February 2026: `request::use_case` and `request::collaboration` at global L0, `onet_task::` likewise.

**Supplementary data.** None.

**Steward feasibility line.** PENDING.

**Biggest risk.** Ecological inference and the construction of the categories: a one-line personal request is directive by construction. The design compares within request family and says what the categories are.

**Mentor interests.** The Index team; the Institute's "AI in daily life" strand.

**Institute agenda.** PENDING.

---

## TL-09 — Is learning the on-ramp? Where AI is new, do people ask it to teach them?

**Thread.** T6 (learning and skill), with T2.

**Ledger items.** `L-2026-03-R5-12` *open* (do experienced users get better over time); `L-2026-03-R5-22`, `-23` (tenure × geography never reported); `L-2025-03-R2-19` *open*.

**Closest existing answer and why it falls short.** The learning share was reported rising from 23% to 28% in early 2025 at global, then fell back inside the delegation surge. It has never been reported by place over time. The March 2026 tenure result (newer users delegate more) is on unreleased data and is about people, not places.

**External literature checked.** PENDING (lead).

**Why it matters.** If learning is how people start with AI and delegation is where they end up, then every place's learning share is a clock, and the "staying human" question becomes whether the clock runs everywhere at the same speed. If learning does not fall as adoption deepens, the on-ramp story is wrong and learning is a standing use. The US states give fifty-one places observed in four waves.

**Contribution.** *If it holds* (learning share falls within a place as its AUI rises): learning as the on-ramp, with the rate. *If it fails* (it rises): deepening use brings more asking-to-understand. *If null*: no within-place relation at the MDE.

**Economic Index cut (proposed).** Collaboration at `country-state` in every long wave; AUI at state in 2025-09 and 2026-06, rebuilt for the two middle waves from `usage_pct` and population as post 2 did; Utah excluded by rule.

**Supplementary data.** State population files already cached.

**Steward feasibility line.** PENDING.

**Biggest risk.** Cohort composition: a state's learning share falls because newcomers arrive and then stop being new; the design cannot see users, so it tests the place and names the cohort reading as the mechanism, not a confound.

**Mentor interests.** Massenkoff (places over time).

**Institute agenda.** PENDING.

---

# Theme T3 · Who gets the most out of AI, and why

## TL-10 — Is AI's biggest time saving on the work it does worst?

**Thread.** T4, with T6.

**Ledger items.** `L-2026-01-B4-10`; `L-2026-01-R4-32`, `-33`, `-37`; `L-2026-01-RCT-11`.

**Closest existing answer and why it falls short.** The January 2026 blog reports two gradients in the education a task requires: the speedup rises with it (nine-fold at twelve years, twelve-fold at sixteen) and the success rate falls (70% to 66%). It reports them in consecutive paragraphs and never multiplies them. The expected time saved on a task is speedup times success, and nobody has published it.

**External literature checked.** PENDING (lead): Brynjolfsson, Li & Raymond; Noy & Zhang; Dell'Acqua et al. on the "jagged frontier".

**Why it matters.** The productivity case for AI rests on time saved. If the tasks with the largest claimed speedups are the ones it fails most often, the naive time-saving number overstates the gain exactly where the gain is claimed to be largest, and the real gain sits on ordinary work. For the general reader: does AI save the most time on the hardest work, or on the work it can actually finish?

**Contribution.** *If it holds* (expected time saved peaks at lower education than the raw speedup): the productivity gradient bends back once failure is priced in. *If it fails*: success falls too little to matter and the raw gradient stands. *If null*: the product is flat in education.

**Economic Index cut (proposed).** November 2025 and February 2026 `onet_task` nodes at global: `human_only_time`, `human_with_ai_time`, `task_success`, `human_education_years`; usage weights.

**Supplementary data.** None.

**Steward feasibility line.** PENDING. Known trap: hours versus minutes between waves (`release_2026_01_15.md:265`).

**Biggest risk.** Three Claude-estimated quantities multiplied; the post reports the sensitivity to each and treats the product as ordinal.

**Mentor interests.** The productivity note's authors; Massenkoff.

**Institute agenda.** PENDING.

---

## TL-11 — Whose hours does AI save?

**Thread.** T4, with T11 (aggregation) and T5.

**Ledger items.** `L-2026-06-EPF-09`, `-18`; `L-2026-09-SCPA-03`, `-19`, `-28`; `L-2025-11-PROD-22`.

**Closest existing answer and why it falls short.** The productivity note and the scenarios paper aggregate task-level time savings to a national productivity number. Neither publishes the distribution: which occupations, and which part of the wage ladder, the saved hours fall on. The June 2026 release carries time means at every detailed occupation node, so the distribution can be built.

**External literature checked.** PENDING (lead): Acemoglu (2024) on the incidence of AI productivity gains; Autor on task-based incidence.

**Why it matters.** A productivity gain is not evenly shared, and who gets it is the political question about AI. If the saved hours fall mostly on high-wage occupations, AI's first-order gain is regressive in its incidence even before any job is lost; if they fall on middling clerical work, the opposite. This is the productivity-side twin of post 1's delegation question, on the same wage ladder.

**Contribution.** *If it holds* (saved hours per worker rise with the occupation's wage): the incidence of the gain, stated. *If it fails*: gains concentrate in mid- or low-wage work. *If null*: flat incidence at the MDE.

**Economic Index cut (proposed).** June 2026 `soc_occupation` L0 (718 occupations, global): usage share, `human_only_time` and `human_with_ai_time` means; per-worker scaling by OEWS employment; wage from OEWS.

**Supplementary data.** BLS OEWS May 2025 (manual download; BLS blocks non-browser fetches).

**Steward feasibility line.** PENDING. Known issues: usage is conversations not workers; June carries no counts or standard errors (`data/ATLAS.md:318`).

**Biggest risk.** The conversion from conversations to hours per worker rests on assumptions the scenarios paper makes explicit; the post adopts theirs, names them, and reports the ordinal result as the finding.

**Mentor interests.** The Institute's scenarios team; Massenkoff.

**Institute agenda.** PENDING.

---

## TL-12 — Does AI save more time on work, or on life?

**Thread.** T4, with T1.

**Ledger items.** `L-2026-01-R4-49` (speedup never split by use case; 54% of Claude.ai is not work); `L-2026-03-LMIA-09` *open*.

**Closest existing answer and why it falls short.** Every productivity estimate from the Index applies task-level speedups as if all use were work, or restricts to work and says so once. Whether the speedups themselves differ between work and personal use of the same task is never reported, though both attach to the same task nodes.

**External literature checked.** PENDING (lead).

**Why it matters.** If the hours AI saves are mostly hours of private life, they never reach a productivity statistic and the macro numbers are overstated; but they are still hours, and who gets them is a welfare question the productivity literature ignores. For the general reader: is AI giving people back time at work, or time at home?

**Contribution.** *If it holds* (personal-heavy tasks show larger time savings): the productivity aggregates apply a work-heavy speedup to the wrong base, and the private gain is named. *If it fails*: work tasks save more time and the aggregates are, if anything, conservative. *If null*: no difference.

**Economic Index cut (proposed).** November 2025 and February 2026 `onet_task` nodes at global: time statistics and `onet_task::use_case` work share; June 2026 every node's `use_case_*_pct` and time means.

**Supplementary data.** None.

**Steward feasibility line.** PENDING.

**Biggest risk.** Ecological again; and the time estimates are Claude's counterfactuals, which may themselves be conditioned on a work framing. The post says so in the definition.

**Mentor interests.** Massenkoff (time use); the productivity note's authors.

**Institute agenda.** PENDING.

---

# Existing long-list entries that already serve these themes (not re-drafted)

| LL | Question | Theme | Status on the first list |
|---|---|---|---|
| LL-18 | Where is AI doing work people say they could not do alone? | T2/T3 | short-listed (Σ 25) |
| LL-30 | Is the work AI does for work the same work it does for study? | T2 | short-listed (Σ 25) |
| LL-20 | Does AI work less well where it is used most? | T3 | first reserve (Σ 24) |
| LL-35 | Do places that started using AI earlier get more out of it? | T3 | Σ 23 |
| LL-42 | Is the income gradient in AI use about how much people ask, or what they ask for? | T3 | Σ 23 |
| LL-19 | Does AI bring more schooling to the work than the person asking does? | T3 | Σ 20 |
| LL-29 | Do people do one thing at a time with AI, and does it change what they get? | T2 | Σ 23 |
| LL-33 | What is the tenth of enterprise AI use that is neither delegated nor collaborative? | T2 | reserve (Σ 24) |
| LL-28 | Does the Index's autonomy measure capture what happens when AI can act on its own? | T2 | Σ 20 |

# Candidates considered and not drafted, with the reason

- **Women as users of Claude, at person level** (the June 2026 Fig 3.8 result extended): no public microdata, no gender field anywhere; gate 2 fails. Only the aggregate can be discussed, and it is an object for TL-01's opening, not a post.
- **Attitudes and feelings by usage**: the survey and the 80,508 interviews are unreleased; the 1,250-transcript Interviewer corpus carries no covariates. Gate 2 fails. The published aggregates can be cited as context in TL-05, TL-06 and TL-07.
- **Time of day and personal use** (evenings and weekends): no hour or day grain in any release (`data/ATLAS.md:283`). Gate 2 fails.
- **Homogenisation of language or writing style**: no text released. Gate 2 fails.
- **Tenure and expertise at person level**: no field in any release; the March 2026 and June 2026 results are on unreleased data. Gate 2 fails; TL-09 is the place-level route.
