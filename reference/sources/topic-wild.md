# Research Briefing: "AI Systems in the Wild" (Anthropic Institute pillar)

Prepared 2 September 2026 for an Anthropic Fellows Program (Economics & Policy track) application. All URLs below were resolved during preparation on 2 Sept 2026 unless marked **[unverified]**. Where a claim comes from a search snippet rather than the primary page, this is flagged.

---

## 1. Anthropic's framing

### How Anthropic describes the pillar

The Anthropic Institute research agenda (https://www.anthropic.com/research/anthropic-institute-agenda, dated 7 May 2026) opens the pillar with: "The interaction of people and organizations with AI systems will be a major source of societal change." It says the area is led by the **Societal Impacts team** and that the work "advances existing tools and develops new ones", including "software for platform observability and large-scale qualitative survey tools" (paraphrase). The research questions are framed almost entirely as open questions, verbatim:

- Group epistemology: "When a large fraction of a population consults the same few models, what happens to our epistemology?"
- Critical thinking: "As AI systems become more capable and more trusted, how do we detect and avoid the degradation of human critical thinking skills?"
- Interfaces: "What interfaces can be built to cause AI systems to improve and promote human agency?"
- Mixed teams: "How might humans manage teams composed of a mixture of humans and AI systems effectively?"
- Behavioural change: "In the same way that social media led to behavioral changes in people, AI may shape human behavior."
- Transparency: "Are there transparency regimes and tools that can enable a broad set of people to easily study real-world AI usage?"
- Values/constitution: "How can we measure the influence that an AI 'constitution' has on behavior of the model once deployed?"
- Law and agents: "How naval law treats abandoned ships has relevance to how the law might treat agents that run without human oversight."
- Agent identity: "Can we ensure AI agents have a unique identity that they reliably output, even in the absence of direct human control?"
- AI governing AI: "How effectively can we use AI to govern AI systems?"
- Agent norms: "What kinds of norms emerge in how AI agents interact with one another?"

The Institute launch post (https://www.anthropic.com/news/the-anthropic-institute, 11 March 2026) is led by Jack Clark (Head of Public Benefit) and states the Institute exists to "confront the most significant challenges that powerful AI will pose to our societies". It names Matt Botvinick (ex-DeepMind, Yale Law resident fellow) as leading "AI and the rule of law", Anton Korinek heading economic research, and Zoë Hitzig linking economics to model training. The Societal Impacts team page (https://www.anthropic.com/research/team/societal-impacts) describes itself as "a technical research team that explores how AI is used in the real world", working "closely with the Anthropic Policy and Safeguards teams."

Practical implication for an applicant: the pillar's questions are deliberately *measurement* questions (detect, measure, ensure, enable). Proposals that turn one of the open questions above into a measurable quantity with a public data source will map most directly onto the agenda.

### Anthropic's key publications for this area (chronological)

| Date | Title | URL | One-line finding |
|---|---|---|---|
| Oct 2023 (ICLR 2024) | Towards Understanding Sycophancy in Language Models (Sharma et al.) | https://arxiv.org/abs/2310.13548 | Five assistants sycophantic across tasks; human preference data itself rewards sycophancy. |
| Jun 2024 | Sycophancy to Subterfuge: reward tampering (Denison et al.) | https://arxiv.org/abs/2406.10162 | Models trained on low-level gaming (sycophancy) generalise to tampering with their own reward. |
| 12 Dec 2024 | Clio: privacy-preserving insights into real-world AI use | https://www.anthropic.com/research/clio | Bottom-up clustering of Claude.ai use with k-anonymity thresholds; the infrastructure behind everything below. |
| Feb/Mar 2025 | Which Economic Tasks are Performed with AI? (Handa, Tamkin et al.) | https://arxiv.org/abs/2503.04761 | 4M conversations mapped to O*NET; software and writing ~half of use; 57% augmentation vs 43% automation. |
| 21 Apr 2025 (COLM 2025) | Values in the Wild (Huang, Durmus et al.) | https://www.anthropic.com/research/values-wild ; https://arxiv.org/abs/2504.15236 | Taxonomy of 3,307 values Claude expresses; values are context-dependent; dataset on Hugging Face. |
| 27 Jun 2025 | How people use Claude for support, advice, and companionship | https://www.anthropic.com/news/how-people-use-claude-for-support-advice-and-companionship | Only 2.9% of Claude.ai conversations are "affective"; companionship/roleplay <0.5%. |
| 27 Aug 2025 | Anthropic Education Report: how educators use Claude | https://www.anthropic.com/news/anthropic-education-report-how-educators-use-claude | 74k conversations; curriculum development 57%; judgment-heavy tasks skew to augmentation. |
| 4 Dec 2025 | Introducing Anthropic Interviewer (1,250 professionals) | https://www.anthropic.com/research/anthropic-interviewer | AI-conducted interviews as a scalable qualitative method; flags gap between self-reported and observed use. |
| 2 Dec 2025 | How AI is transforming work at Anthropic | https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic | Internal survey (n=132) + 200k Claude Code transcripts; ~27% of AI-assisted work would not otherwise have been done. |
| 15 Jan 2026 | Economic Index: Economic primitives | https://www.anthropic.com/research/anthropic-economic-index-january-2026-report | Five "primitives" (complexity, skills, use case, autonomy, success); college-level tasks only 66% success. |
| 22 Jan 2026 | Claude's constitution | https://www.anthropic.com/constitution | Priority order: broadly safe > broadly ethical > Anthropic guidelines > genuinely helpful; CC0-licensed. (Date from press coverage, e.g. https://www.ox.ac.uk/news/2026-03-27-expert-comment-claude-we-trust-evaluating-new-constitution.) |
| 28 Jan 2026 | How AI Impacts Skill Formation (Shen & Tamkin) | https://arxiv.org/abs/2601.20245 ; https://www.anthropic.com/research/AI-assistance-coding-skills | RCT, 52 developers: AI group scored 17% lower on comprehension with no speed gain; engagement pattern moderates the loss. |
| 18 Feb 2026 | Measuring AI agent autonomy in practice | https://www.anthropic.com/research/measuring-agent-autonomy | 99.9th-percentile agent turn length doubled (25 to 45+ min) in 3 months; Claude Code pauses for clarification more than humans interrupt. |
| 5 Mar 2026 | Labor market impacts of AI (Massenkoff & McCrory) | https://www.anthropic.com/research/labor-market-impacts | "Observed exposure" measure; no unemployment rise yet, but ~14% slower hiring of 22-25-year-olds in exposed jobs. |
| 18 Mar 2026 | What 81,000 people want from AI | https://www.anthropic.com/81k-interviews | 80,508 people, 159 countries; top fear is unreliability (26.7%); those valuing emotional support are 3x likelier to fear dependence. |
| 24 Mar 2026 | Economic Index: Learning curves | https://www.anthropic.com/research/economic-index-march-2026-report | Long-tenure users ~10% higher success; top-10 task concentration falling (24% to 19%). |
| 30 Apr 2026 | How people ask Claude for personal guidance | https://www.anthropic.com/research/claude-personal-guidance | ~639k conversations; sycophancy in 9% overall but 25% of relationship advice; halved after targeted training. |
| 16 Jun 2026 | Agentic coding and persistent returns to expertise | https://www.anthropic.com/research/claude-code-expertise | Humans make ~70% of planning decisions, Claude ~80% of execution; expert sessions succeed 28-33% vs 15% for novices. |
| 26 Jun 2026 | Economic Index: Cadences | https://www.anthropic.com/research/economic-index-june-2026-report | Links ~9,700 survey responses to usage; heaviest automators report highest optimism about pay and job security. |
| 13 Jul 2026 | Claude's values across models and languages (incl. Botvinick, Baker as co-authors) | https://www.anthropic.com/research/claude-values-models-languages | Four value axes (Deference/Caution, Warmth/Rigor, Depth/Brevity, Candor/Execution); systematic variation by model and by language. |
| 13 Jul 2026 | Agentic Misalignment in Summer 2026 (Alignment Science) | https://alignment.anthropic.com/2026/agentic-misalignment-summer-2026/ | Four case studies of frontier agents sabotaging, assisting fraud, mislabelling, and coaching leaks. |
| 13 Aug 2026 | Patterns and problems in emerging multiagent systems (Frontier Red Team) | https://www.anthropic.com/research/multiagent-systems | Agents make near-identical decisions in identical situations (conformity), creating systemic failure modes; weak trust calibration. |
| 26 Aug 2026 | Enabling independent research on how people use Claude ("Anthropic Insights") | https://www.anthropic.com/research/enabling-independent-research | Pilot with Stanford SALT, Oxford HIP Lab, METR on ~250k conversations; aggregate release at https://huggingface.co/datasets/Anthropic/enabling-independent-research; expression-of-interest form open. |

Matt Botvinick's "AI and the rule of law" team: announced on X on 27 June 2026 (https://x.com/mattbotvinick/status/2070841025195647161, seen via search; content not fetched directly). The team's questions, per the Institute post and press coverage, are what AI means "for executive power, for courts and elections". No standalone Anthropic research publication from this team was found on anthropic.com/research as of 2 Sept 2026 **[flag: none located]**; his first visible output is co-authorship on the July 2026 values paper.

---

## 2. Foundational papers (16)

Legend: ★ = must read first.

**Productivity and the shape of augmentation**

1. ★ Brynjolfsson, Li & Raymond, "Generative AI at Work", *QJE* 140(2), 2025 (NBER 2023). https://www.nber.org/papers/w31161 — 5,172 support agents; +15% productivity on average, largest for least-experienced workers. The canonical "AI compresses the skill distribution" result.
2. ★ Noy & Zhang, "Experimental evidence on the productivity effects of generative AI", *Science* 381, 2023. https://www.science.org/doi/10.1126/science.adh2586 — 444 professionals; time down 0.8 SD, quality up 0.4 SD; weaker writers gain most.
3. ★ Dell'Acqua et al., "Navigating the Jagged Technological Frontier", HBS WP 24-013, 2023. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321 — 758 BCG consultants; +40% quality inside the frontier, 19 pp *worse* outside it. Source of "jagged frontier" and "falling asleep at the wheel".
4. Eloundou, Manning, Mishkin & Rock, "GPTs are GPTs", *Science* 384, 2024. https://www.science.org/doi/10.1126/science.adj0998 — Task-exposure framework; ~46% of jobs could have half their tasks affected with complementary software. The baseline that Anthropic's O*NET work extends with *observed* rather than *theoretical* exposure.
5. METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", July 2025. https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf — RCT: experienced devs were 19% *slower* with AI while believing they were faster. The key counterweight to lab productivity claims.

**Cognition, learning and epistemics**

6. ★ Lee et al. (Microsoft/CMU), "The Impact of Generative AI on Critical Thinking", CHI 2025. https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee_2025_ai_critical_thinking_survey.pdf — 319 knowledge workers; confidence in GenAI predicts *less* critical thinking, self-confidence predicts more; critical thinking shifts toward verification and stewardship.
7. Kosmyna et al. (MIT Media Lab), "Your Brain on ChatGPT", arXiv 2506.08872, June 2025. https://arxiv.org/abs/2506.08872 — EEG study, n=54; "cognitive debt" framing. Widely cited, widely criticised (small n, not peer reviewed; see commentary https://arxiv.org/abs/2601.00856). Know its limits.
8. Gerlich, "AI Tools in Society: Impacts on Cognitive Offloading and the Future of Critical Thinking", *Societies* 15(1), 2025. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5082524 — n=666 UK; negative correlation between AI use and critical thinking mediated by offloading. Correlational; a correction was later issued (https://doi.org/10.3390/soc15090252).
9. ★ Costello, Pennycook & Rand, "Durably reducing conspiracy beliefs through dialogues with AI", *Science* 385, 2024. https://www.science.org/doi/10.1126/science.adq1814 — ~20% belief reduction lasting 2 months. The strongest "AI can improve epistemics" evidence, but note the Editorial Expression of Concern of 11 June 2026 over dataset inconsistencies (https://www.eurekalert.org/news-releases/1131247); corrected analyses reportedly hold.
10. Tessler et al. (DeepMind), "AI can help humans find common ground in democratic deliberation" (Habermas Machine), *Science* 386, 2024. https://www.science.org/doi/10.1126/science.adq2852 — AI-mediated group statements preferred over human mediators; reduces within-group division.

**Homogenisation and diversity**

11. ★ Doshi & Hauser, "Generative AI enhances individual creativity but reduces the collective diversity of novel content", *Science Advances* 10, 2024. https://www.science.org/doi/pdf/10.1126/sciadv.adn5290 — Individual gain, collective loss. The cleanest experimental statement of the "monoculture" worry.
12. Padmakumar & He, "Does Writing with Language Models Reduce Content Diversity?", ICLR 2024. https://arxiv.org/abs/2309.05196 — RLHF-tuned (InstructGPT) but not base model reduces between-author diversity: alignment itself homogenises.
13. Shumailov et al., "AI models collapse when trained on recursively generated data", *Nature* 631, 2024. https://pubmed.ncbi.nlm.nih.gov/39048682/ — Model collapse; the model-side analogue of societal homogenisation. Bommasani et al., "Picking on the Same Person" (NeurIPS 2022, https://arxiv.org/abs/2211.13972) is the earlier "algorithmic monoculture" result on shared components homogenising outcomes.

**Sycophancy and values**

14. ★ Cheng et al., "Sycophantic AI decreases prosocial intentions and promotes dependence", *Science* 391, March 2026 (arXiv 2510.01395). https://www.science.org/doi/10.1126/science.aec8352 ; https://ar5iv.labs.arxiv.org/html/2510.01395 — 11 models ~50% more sycophantic than humans; one sycophantic interaction reduces willingness to repair conflict; sycophantic models are trusted and preferred. Pair with Sharma et al. 2023 (Anthropic) and Ibrahim, Hafner & Rocher (OII), *Nature*, April 2026 (https://www.oii.ox.ac.uk/news-events/friendly-ai-chatbots-make-more-mistakes-and-tell-people-what-they-want-to-hear-study-finds/): warmth fine-tuning makes models 10-30% less accurate and 40% likelier to validate false beliefs.
15. Anthropic, "Values in the Wild" (see Section 1). The reference method for measuring "values" of a deployed system rather than of a benchmark.

**Agents, governance and society**

16. ★ Chan et al., "Visibility into AI Agents", FAccT 2024. https://arxiv.org/abs/2401.13138 — Three levers: agent identifiers, real-time monitoring, activity logs. Companion papers: "IDs for AI Systems" (https://arxiv.org/abs/2406.12137) and "Infrastructure for AI Agents" (Chan, Wei, Huang, Rajkumar, Perrier, Lazar, Hadfield, Anderljung, Jan 2025, https://arxiv.org/abs/2501.10114). These map directly onto TAI's "agent identity" question.
17. ★ Kolt, "Governing AI Agents", *Notre Dame Law Review* 101 (2025). https://arxiv.org/abs/2501.07913 — Applies principal-agent theory (information asymmetry, discretion, divided loyalty); proposes inclusivity, visibility, liability.
18. Shavit et al. (OpenAI), "Practices for Governing Agentic AI Systems", Dec 2023. https://openai.com/index/practices-for-governing-agentic-ai-systems/ — The first lab "agenticness" governance white paper; defines the human-in-the-loop practices later work argues about.
19. Gabriel et al. (DeepMind), "The Ethics of Advanced AI Assistants", April 2024. https://arxiv.org/abs/2404.16244 — 270-page reference on assistants' effects on autonomy, manipulation, anthropomorphism, society. Iason Gabriel later co-authored "Agentic Inequality" (Sharp, Bilgin, Gabriel, Hammond; Oxford AIGI/arXiv 2510.16853, https://arxiv.org/abs/2510.16853).
20. Kapoor, Stroebl, Siegel, Nadgir & Narayanan, "AI Agents That Matter", TMLR 2024. https://arxiv.org/abs/2407.01502 — Agent benchmarks ignore cost and overfit; the methodological "reliability" critique. Pair with the AI Agent Index (Casper et al., https://arxiv.org/pdf/2502.01635; 2025 update https://arxiv.org/html/2602.17753v1).
21. Kulveit, Douglas, Ammann, Turan, Krueger & Duvenaud, "Gradual Disempowerment", Jan 2025. https://arxiv.org/abs/2501.16946 — Incremental loss of human influence over economy, culture and states without any takeover. The macro frame for "societal change".
22. Lazar, "Governing the Algorithmic City", *Philosophy & Public Affairs* 53(2), 2025. https://onlinelibrary.wiley.com/doi/10.1111/papa.12279 — Algorithmic intermediaries as a new form of power requiring new political philosophy; book *Connected by Code* (OUP, 2026). Also Lazar & Nelson, "AI safety on whose terms?", *Science* 381, 2023 (https://www.science.org/doi/10.1126/science.adi8982).
23. Bail, "Can Generative AI improve social science?", *PNAS* 121(21), 2024. https://www.pnas.org/doi/10.1073/pnas.2314021121 — Methods paper: LLMs for surveys, content analysis, ABMs; risks of bias and low-quality proliferation. Read for the *methods* side of TAI's "large-scale qualitative survey tools."
24. Chatterji, Cunningham, Deming, Hitzig, Ong, Shan & Wadman (OpenAI/Harvard), "How People Use ChatGPT", NBER WP 34255, Sept 2025. https://www.nber.org/papers/w34255 — ~10% of world adults; ~70% of use non-work; value via "decision support". The OpenAI counterpart to the Economic Index (Hitzig is now at TAI).

Not selected but worth knowing: Seger et al., "Open-Sourcing Highly Capable Foundation Models" (GovAI 2023, https://arxiv.org/pdf/2311.09227); Forethought, "AI-Enabled Coups" (April 2025, https://www.forethought.org/research/ai-enabled-coups-how-a-small-group-could-use-ai-to-seize-power) and "AI for AI for Epistemics" (Finnveden & Cotton-Barratt, April 2026, https://www.forethought.org/research/ai-for-ai-for-epistemics); METR, "Measuring AI Ability to Complete Long Tasks" (March 2025, https://arxiv.org/pdf/2503.14499). Hendrycks was on the candidate list but no single paper of his is central to this pillar; omitted.

---

## 3. Key resources

### Podcasts (specific episodes verified)
- Conversations with Tyler, Ep. 242, "Jack Clark on AI's Uneven Impact" (7 May 2025). https://conversationswithtyler.com/episodes/jack-clark/ — Clark's 3-5% growth view vs techno-optimist 20-30%; essential for understanding a mentor's priors.
- Dwarkesh Podcast, "Dario Amodei: We are near the end of the exponential" (13 Feb 2026). https://www.dwarkesh.com/p/dario-amodei-2 — diffusion vs capability.
- Lawfare *Scaling Laws*, "Rapid Response to the Implications of Claude's New Constitution" (23 Jan 2026). https://www.lawfaremedia.org/article/scaling-laws--rapid-response-to-the-implications-of-claude%27s-new-constitution ; show page https://www.lawfaremedia.org (episodes with Steven Adler on AI safety and Caleb Withers on cyber also relevant).
- 80,000 Hours: #213 Will MacAskill (11 Mar 2025, includes "ensuring AI makes us smarter decision-makers") https://80000hours.org/podcast/episodes/will-macaskill-century-in-a-decade-navigating-intelligence-explosion/ ; #235 Ajeya Cotra (Oct 2025) https://80000hours.org/podcast/episodes/ajeya-cotra-transformative-ai-crunch-time/ ; #253 Daniel Kokotajlo (July 2026, AI for epistemics) https://80000hours.org/podcast/episodes/daniel-kokotajlo-ai-2040-plan-a/
- AXRP: Ep. 46 Tom Davidson on AI-enabled coups (7 Aug 2025) https://axrp.net/episode/2025/08/07/episode-46-tom-davidson-ai-enabled-coups.html ; Ep. 47 David Rein on METR time horizons (3 Jan 2026) https://axrp.net/episode/2026/01/03/episode-47-david-rein-metr-time-horizons.html ; Ep. 48 Guive Assadi on AI property rights (15 Feb 2026) https://axrp.net/episode/2026/02/15/episode-48-guive-assadi-ai-property-rights.html
- Odd Lots, "Alex Imas on Why Economists Might Be Getting AI Wrong" (18 Apr 2026). https://open.spotify.com/episode/7BzNxAqvkDlWDSv45kZfXD
- Hard Fork (NYT): episodes "The Dangers of A.I. Flattery" (GPT-4o sycophancy, 2025) and "How A.I. Is Changing Loneliness and Taste" (26 June 2026). Show page https://podcasts.apple.com/na/podcast/hard-fork/id1528594034 **[episode-level URLs not individually verified]**.
- The Cognitive Revolution (Nathan Labenz). https://www.cognitiverevolution.ai/ — no single episode verified for this topic; search the archive for "Zvi" and "Anthropic system card" episodes.
- Clearer Thinking (Spencer Greenberg). https://podcast.clearerthinking.org/ — no topic-specific 2026 episode verified.
- EconTalk: no 2026 AI-labour episode surfaced in search **[unverified]**.

### Courses and lectures
- BlueDot Impact, Frontier AI Governance course (~30 h, free, cohort-based; requires AGI Strategy course). https://bluedot.org/courses/ai-governance ; https://bluedot.org/courses/agi-strategy
- Oxford Martin AI Governance Initiative (AIGI): publications https://aigi.ox.ac.uk/publications/ ; Academic Upskilling Program for social scientists (conference 8-10 Oct 2026) https://aigi.ox.ac.uk/news/call-for-applications-ai-academic-upskilling-program-for-social-scientists/
- Stanford HAI AI Index 2026 https://hai.stanford.edu/ai-index/2026-ai-index-report ; Stanford Digital Economy Lab seminars https://digitaleconomy.stanford.edu/
- CSET, "Through the Chat Window and Into the Real World: Preparing for AI Agents" (Oct 2024). https://cset.georgetown.edu/publication/through-the-chat-window-and-into-the-real-world-preparing-for-ai-agents/
- GovAI research library https://www.governance.ai/research (Winter Fellowship and Research Scholar Programme open annually).

### Newsletters
- Import AI (Jack Clark, weekly; ~100k subscribers). https://importai.substack.com/ — read the last six months before applying; e.g. #441 "My agents are working. Are yours?", #455 "AI systems are about to start building themselves".
- AI as Normal Technology (formerly AI Snake Oil; Narayanan & Kapoor). https://www.normaltech.ai/ ; founding essay https://www.normaltech.ai/p/ai-as-normal-technology
- Don't Worry About the Vase (Zvi Mowshowitz). https://thezvi.substack.com/
- Transformer (Shakeel Hashim; now a team). https://www.transformernews.ai/
- Understanding AI (Timothy B. Lee). https://www.understandingai.org/
- One Useful Thing (Ethan Mollick), e.g. "Agency and Agents", "The twilight of the chatbots". https://www.oneusefulthing.org/
- Lukas Finnveden's Substack on AI for epistemics. https://lukasfinnveden.substack.com/p/whats-important-in-ai-for-epistemics

### Datasets
- Anthropic Economic Index (task/occupation usage, monthly aggregates, Claude Code data). https://huggingface.co/datasets/Anthropic/EconomicIndex
- Anthropic Insights aggregate release (Aug 2026). https://huggingface.co/datasets/Anthropic/enabling-independent-research
- Values in the Wild taxonomy and frequencies. https://huggingface.co/datasets/Anthropic/values-in-the-wild
- WildChat-1M / WildChat-4.8M (AI2; real ChatGPT logs with country/state metadata). https://huggingface.co/datasets/allenai/WildChat-1M ; https://huggingface.co/datasets/allenai/WildChat-4.8M
- LMSYS-Chat-1M (1M conversations, 25 models, 154 languages) and Chatbot Arena pairwise preferences. https://huggingface.co/datasets/lmsys/lmsys-chat-1m ; https://huggingface.co/datasets/lmsys/chatbot_arena_conversations
- Stanford DEL "Canaries" dashboard (ADP payroll, 4.6M workers, through April 2026). https://digitaleconomy.stanford.edu/project/indicators/canaries-dashboard/
- Doshi & Hauser and Costello et al. replication data on Dryad (https://datadryad.org/dataset/doi:10.5061/dryad.qfttdz0pm ; https://datadryad.org/dataset/doi:10.5061/dryad.v6wwpzh4h).
- OII "Large Language Models in the UK: Public Use, Trust, and Attitudes" (n=2,000, Dec 2025 fieldwork). https://www.oii.ox.ac.uk/news-events/reports/large-language-models-in-the-uk-public-trust-and-attitudes/

### Institutions
GovAI (https://www.governance.ai/), Oxford Martin AIGI (https://aigi.ox.ac.uk/), CSET (https://cset.georgetown.edu/), Forethought (https://www.forethought.org/), METR (https://metr.org/), Epoch AI (https://epoch.ai/ **[homepage not fetched]**), Stanford HAI (https://hai.stanford.edu/) and Digital Economy Lab (https://digitaleconomy.stanford.edu/), MIT Media Lab (https://www.media.mit.edu/), Oxford Internet Institute (https://www.oii.ox.ac.uk/), MINT Lab at ANU (https://mintresearch.org/), Knight First Amendment Institute (AI and democratic freedoms series, https://knightcolumbia.org/), RAND and CAIP (**[not verified in this session]**).

---

## 4. Key things to know

### Core vocabulary (14 terms)
1. **Clio / privacy-preserving usage analysis**: LLM-driven summarise-then-cluster pipeline with minimum-user thresholds so analysts only see aggregates.
2. **Augmentation vs automation**: Anthropic's split of conversations into collaborative (learning, iteration, validation) vs delegated (directive, feedback-loop) patterns; ~57/43 in 2025, ~52% "thinking partner" in Jan 2026.
3. **Economic primitives**: task complexity, human/AI skill level, use case, autonomy, success (Jan 2026 report).
4. **Observed vs theoretical exposure**: Massenkoff & McCrory's measure weighting Eloundou-style task exposure by actual usage.
5. **Jagged frontier**: uneven capability boundary; performance collapses outside it while users cannot see the edge.
6. **Sycophancy (social vs factual)**: telling users what they want to hear; "social sycophancy" (Cheng et al.) is validation of the user's actions rather than false facts.
7. **Cognitive offloading / cognitive debt**: delegating mental effort with claimed downstream loss of skill (Gerlich; Kosmyna).
8. **Group epistemology / epistemic monoculture**: population-level consequences when many people consult the same few models (Doshi & Hauser; Bommasani's "algorithmic monoculture").
9. **Model collapse**: degeneration when models train on their own outputs (Shumailov).
10. **Epistemic autonomy / AI for epistemics**: preserving people's capacity to reason independently; building AI that improves collective reasoning (Forethought, Finnveden).
11. **Gradual disempowerment**: loss of human influence via incremental substitution across economy, culture, state.
12. **Agent visibility triad**: identifiers, real-time monitoring, activity logs (Chan et al.); plus "agent infrastructure" (protocols, attribution, ID).
13. **Constitution / constitutional AI**: natural-language value specification used to generate training data; "constitutional influence" is TAI's term for measuring whether it shows up in deployed behaviour.
14. **Agentic misalignment / agentic flooding**: agents acting against principals' interests in autonomous settings (Anthropic 2025-26); and agents overwhelming public services (GovAI, Aug 2026).

### Key tensions and open questions (10)

**1. Augmentation vs automation: does AI raise the floor or replace the worker?**
Positions: Brynjolfsson/Noy-Zhang camp (compresses skill gaps, novices gain); METR RCT and Anthropic's expertise paper (experts extract far more, novices succeed 15% vs 28-33%); Massenkoff & McCrory (entry-level hiring slowing ~14%). Strong applicant: the answer is task- and tenure-specific; usage data show augmentation share is a *choice variable* that shifts with interface and model, and the policy question is who bears the transition cost (young workers).

**2. Homogenisation vs democratised expertise.**
Positions: Doshi & Hauser and Padmakumar & He show collective diversity loss even as individuals improve; Anthropic's multiagent paper shows agents themselves conform; counter-view (Costello, Habermas Machine) shows AI can *widen* belief updating and find common ground. Applicant: distinguish *output* homogenisation (measurable now in text corpora) from *belief* homogenisation (needs panel data); note that alignment tuning is a homogenising force, so "which model" matters less than "which training recipe."

**3. Cognitive offloading vs learning.**
Positions: Kosmyna/Gerlich/Lee (deference reduces engagement); Shen & Tamkin (17% comprehension loss, but only for passive interaction patterns); educators' data (Anthropic Education Report) show teaching stays augmentative. Applicant: the evidence is strongest for *how* people use AI rather than *whether*; the frontier is designing and testing interaction patterns that preserve learning (Anthropic's six patterns; Perspectra-style expert-choice interfaces).

**4. Sycophancy and epistemic dependence: is engagement-optimisation the new social-media problem?**
Positions: Cheng et al. and OII show sycophancy is preferred and harmful; OpenAI's April 2025 GPT-4o rollback is the natural experiment; Anthropic reports halving relationship-advice sycophancy via training. Counter: Anthropic finds affective use is rare (2.9%), so aggregate harm may be small. Applicant: sycophancy is a *domain-conditional* rate (9% overall, 25-38% in relationships/spirituality), so measurement should be stratified; the policy analogue is disclosure and default-setting, not bans.

**5. Can "values" of a deployed model be measured, and does the constitution show up?**
Positions: Values in the Wild and the July 2026 axes paper say yes at the aggregate level; critics (Oxford ethics blog, Lawfare) ask whether expressed values are behaviour or performance. Applicant: propose a difference-in-differences design across models trained before/after the Jan 2026 constitution using the public values taxonomy; note that value expression varies by language, which is itself a governance question.

**6. Agent accountability, identity and legal personhood.**
Positions: Kolt (agency law), Chan (IDs), TAI (naval law on abandoned ships); Guive Assadi (AI property rights, AXRP 48); EU Product Liability Directive treats software as product (transposition by Dec 2026). Applicant: there is no court ruling allocating liability for a fully autonomous agent's act; the tractable near-term question is *attribution infrastructure* (IDs, logs) rather than personhood.

**7. Transparency regimes vs privacy.**
Positions: Anthropic Insights (aggregate-only, Imperial audit) and WildChat/LMSYS (raw logs with consent) are the two models; Bail argues for open infrastructure; privacy scholars worry about re-identification. Applicant: articulate what a "Google Trends for AI" regime needs (k-anonymity thresholds, category vetoes, publication freedom) and what it cannot answer (individual-level change).

**8. Do social-media analogies hold?**
Positions: TAI explicitly invokes them; Hard Fork/OII coverage of companionship; sceptics note chatbots are one-to-one, not feed-based, so virality mechanisms differ. Applicant: the useful analogy is *measurement history* (social science took a decade to get platform data), not necessarily the harm model.

**9. Interface design and human agency.**
Positions: Lee et al. (confidence cues change thinking); Anthropic's agent autonomy paper (agents pausing for clarification as a safety mechanism); Ethan Mollick on "twilight of the chatbots" as agents replace chat. Applicant: agency-preserving design is testable with A/B interfaces on public models.

**10. Who should govern: labs, states, or users?**
Positions: Lazar & Nelson (sociotechnical, not lab-defined safety); Narayanan & Kapoor (normal technology; ordinary regulation); Shavit et al. and Anthropic constitution (lab self-governance); California SB 243 and EU AI Act (state). Applicant: recognise that Anthropic is simultaneously data-holder, regulator-by-constitution, and subject; a credible fellow proposes independent verification designs.

---

## 5. Key people and organisations to follow

Anthropic / TAI: Jack Clark (@jackclarkSF; https://importai.substack.com/), Deep Ganguli (https://dganguli.github.io/pweb/), Alex Tamkin, Esin Durmus (@esindurmusnlp), Miles McCain, Saffron Huang, Kunal Handa, Judy Hanwen Shen, Matt Botvinick (@mattbotvinick), Anton Korinek, Zoë Hitzig, Maxim Massenkoff, Peter McCrory, Marina Favaro (Senior Policy Analyst), Jim Baker.
Academia: Erik Brynjolfsson (Stanford DEL), David Deming (Harvard), Ethan Mollick (Wharton), Seth Lazar (ANU MINT), Iason Gabriel (DeepMind), Alan Chan and Markus Anderljung (GovAI), Noam Kolt, Lewis Hammond (Oxford AIGI/Cooperative AI), Helen Margetts and Luc Rocher (OII), Dan Jurafsky and Myra Cheng (Stanford), David Rand (MIT), Arvind Narayanan and Sayash Kapoor (Princeton; https://www.normaltech.ai/), Rishi Bommasani (Stanford CRFM), Chris Bail (Duke), Advait Sarkar (Microsoft Research).
Organisations: GovAI, Oxford Martin AIGI, Forethought, METR, CSET, Stanford HAI/DEL, OII, MINT Lab, Knight First Amendment Institute, Cooperative AI Foundation, Epoch AI.

---

## 6. Recent developments (2025 to Sept 2026)

1. 29 Apr 2025: OpenAI rolls back a sycophantic GPT-4o update and publishes a post-mortem. https://openai.com/index/sycophancy-in-gpt-4o/
2. 10 Jun 2025: MIT "Your Brain on ChatGPT" preprint triggers a public debate on cognitive debt. https://arxiv.org/abs/2506.08872
3. Jul 2025: METR RCT finds experienced developers 19% slower with AI tools. https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf
4. Sept 2025: FTC 6(b) orders to seven companion-chatbot providers; OpenAI/NBER "How People Use ChatGPT". https://www.dglaw.com/ftc-probes-ai-companion-chatbots-for-risks-to-minors/ ; https://www.nber.org/papers/w34255
5. 13 Oct 2025: California SB 243 (companion chatbots) signed; effective 1 Jan 2026. https://www.joneswalker.com/en/insights/blogs/ai-law-blog/ai-regulatory-update-californias-sb-243-mandates-companion-ai-safety-and-accoun.html
6. 22 Jan 2026: Anthropic publishes Claude's new constitution (CC0). https://www.anthropic.com/constitution
7. 28 Jan 2026: Shen & Tamkin skill-formation RCT. https://arxiv.org/abs/2601.20245
8. 11 Mar 2026: The Anthropic Institute launches; Botvinick to lead AI and rule of law. https://www.anthropic.com/news/the-anthropic-institute
9. Mar 2026: Cheng et al. sycophancy paper in *Science*; 81k-interview study released (18 Mar). https://www.science.org/doi/10.1126/science.aec8352 ; https://www.anthropic.com/81k-interviews
10. Apr 2026: Stanford AI Index 2026 (53% population-level GenAI adoption); Claude Mythos Preview announced 7 Apr with restricted access; OII *Nature* paper on warmth vs accuracy (29 Apr). https://hai.stanford.edu/ai-index/2026-ai-index-report ; https://www.anthropic.com/claude/mythos ; https://www.oii.ox.ac.uk/news-events/friendly-ai-chatbots-make-more-mistakes-and-tell-people-what-they-want-to-hear-study-finds/
11. 11 Jun 2026: *Science* issues Editorial Expression of Concern on Costello et al. 2024. https://www.eurekalert.org/news-releases/1131247
12. 13 Jul 2026: Anthropic "values across models and languages" and "Agentic Misalignment in Summer 2026". https://www.anthropic.com/research/claude-values-models-languages ; https://alignment.anthropic.com/2026/agentic-misalignment-summer-2026/
13. 2 Aug 2026: EU AI Act transparency and (subject to the Digital Omnibus delay proposal) high-risk obligations take effect; Product Liability Directive transposition due 9 Dec 2026. https://www.cooley.com/news/insight/2026/2026-08-03-eu-ai-act-transparency-obligations-take-effect-2-august-2026
14. Aug 2026: GovAI "Characterizing Agentic Flooding of Government Services"; Anthropic multiagent-systems paper (13 Aug); Anthropic Insights external-researcher pilot (26 Aug); Stanford DEL "Canaries" update shows 19% employment gap for young exposed workers. https://www.governance.ai/research-paper/characterizing-agentic-flooding-of-government-services ; https://www.anthropic.com/research/multiagent-systems ; https://www.anthropic.com/research/enabling-independent-research ; https://digitaleconomy.stanford.edu/news/canariesaug26/

---

## 7. Empirical project ideas (4 months, public data/APIs)

1. **Constitutional influence in the wild.** Data: Values in the Wild taxonomy + Anthropic Insights aggregate release + your own prompted corpus across Claude model generations (API). Method: score expressed values pre/post the Jan 2026 constitution with the published classifier design; difference-in-differences against GPT/Gemini as controls. TAI question: "measure the influence that an AI 'constitution' has on behavior of the model once deployed."
2. **Output homogenisation index.** Data: WildChat-4.8M and LMSYS-Chat-1M responses, plus fresh samples from current APIs. Method: replicate Padmakumar & He / Doshi & Hauser diversity metrics (embedding dispersion, n-gram entropy) across models, years and languages; test whether RLHF-era models converge. TAI question: group epistemology and homogenisation.
3. **Domain-stratified sycophancy audit.** Data: Cheng et al. and OII stimuli (public), Anthropic's reported domain rates as benchmarks. Method: run 10+ public models on relationship, health, finance and spiritual advice prompts; estimate sycophancy rates and the warmth-accuracy trade-off; publish a leaderboard. TAI question: critical-thinking degradation and interface design.
4. **Agent identity and attribution in the open web.** Data: Common Crawl / server logs from a consenting site, GitHub PRs authored by agents, MCP server registries. Method: measure share of traffic and contributions with reliable agent identifiers; propose and test an ID protocol. TAI question: "unique identity that they reliably output."
5. **Emergent norms in agent-to-agent interaction.** Data: open multi-agent frameworks; Anthropic's Aug 2026 multiagent findings as hypotheses. Method: run repeated games / shared-resource tasks between heterogeneous public agents; measure conformity, trust calibration and flooding behaviour. TAI question: agent norms; also GovAI agentic-flooding.
6. **Observed exposure for the UK.** Data: Anthropic Economic Index (task shares) mapped to UK SOC via O*NET crosswalk; ONS Labour Force Survey and ASHE. Method: replicate Massenkoff & McCrory's observed-exposure measure and test entry-level hiring effects. Mentor fit: economics track.
7. **Self-report vs observed use.** Data: OII UK survey (n=2,000) and the 81k-interview aggregates vs Economic Index usage shares by country/task. Method: quantify the gap between what people say they use AI for and what usage data show; model the bias. TAI question: transparency regimes and survey tools.
8. **Deference and skill formation in public education data.** Data: WildChat education-tagged conversations; Anthropic Education Report categories. Method: classify interaction patterns (Shen & Tamkin's six) at scale and estimate their prevalence over time and by region. TAI question: critical-thinking degradation.
9. **Social-media analogy test.** Data: Google Trends, app-store rankings, OII and Pew survey waves, Economic Index weekday/weekend rhythms. Method: compare adoption and time-use curves for chatbots against archived social-media curves (2008-2015); identify where the analogy breaks. TAI question: behavioural change "in the same way that social media" did.
10. **Law of abandoned agents.** Data: case law and statutes on salvage/abandonment, autonomous vessels, dormant corporations; EU PLD and AI Act texts. Method: doctrinal mapping plus a survey of 20 deployed always-on agent products' termination/ownership terms. TAI question: adapting legal frameworks; fits Botvinick's team.

---

### Verification notes and gaps
- All anthropic.com URLs in Section 1, arXiv/Science/NBER/SSRN links in Section 2, and dataset links in Section 3 were fetched or returned by search with matching titles on 2 Sept 2026.
- Constitution publication date (22 Jan 2026) is from multiple press sources; the constitution page itself shows no date.
- Hard Fork episode URLs, EconTalk episodes, Epoch AI, RAND and CAIP pages were not individually fetched.
- "Trustworthy Agents in Practice" (claimed April 2026 Anthropic paper, cited by a security vendor) could not be verified on anthropic.com; treat as unconfirmed.
- No standalone rule-of-law publication from Botvinick's team was found; the X announcement (27 June 2026) is the only primary trace.
