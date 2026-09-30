"""Seed the two memory stores from README.md and team/LESSONS.md. Idempotent: existing paths are updated."""
import anthropic, json, re
c=anthropic.Anthropic(); stores=json.load(open("team/memory-stores.json"))
def put(store,path,content):
    sid=stores[store]; path="/"+path.lstrip("/")   # paths are absolute inside the store
    try: c.beta.memory_stores.memories.create(sid,path=path,content=content[:95000])
    except anthropic.APIStatusError as e:
        if e.status_code==409: c.beta.memory_stores.memories.update(sid,memory_id=None,path=path,content=content[:95000]) if False else None; print("exists",path); return
        raise
    print("put",store,path)
readme=open("README.md").read()
put("standards","criteria.md",readme[readme.index("## Working criteria"):readme.index("## File ownership")])
put("standards","file-ownership.md",readme[readme.index("## File ownership"):readme.index("## Layout")])
put("standards","terminology.md","""# Verified Economic Index terminology (against Anthropic's own text)
- collaboration: the NAME OF THE WHOLE FACET (five patterns), not a pole.
- automation = Directive + Feedback Loop; augmentation = Task Iteration + Learning + Validation. Anthropic glosses automation as delegating complete tasks and augmentation as collaborative use. In our posts: delegation = automation share, collaboration = augmentation share; tables use Anthropic's terms.
- AI autonomy (1-5 primitive) = decision-making delegated to Claude; a separate construct from automation ("translate this paragraph" is high automation, low autonomy). Never conflate.
- AI Usage Index (AUI) = geography's share of Claude usage / share of working-age (15-64) population; 1.0 = proportional. Published for countries and US states only.
- Occupation in the data is inferred from the task, not the user.
- Naming rule: the question says AI; every finding and measurement says Claude; limitations carry one sentence on what generalises.
""")
put("standards","register.md","""# Register (working version; the editor rewrites it from the style corpus in Stage 1)
Why it matters first. Findings as plain sentences with the number and its caveat together. The comparison is the finding. Observation separated from conjecture. Limitations a referee would raise first. A close about what was learned and why it matters. No first person. No summary block. Figures captioned Anthropic-style: what is plotted, units, sample, what the line is.
""")
L=open("team/LESSONS.md").read(); n=0
for p in re.split(r"\n(?=## )",L)[1:]:
    title=p.split("\n",1)[0].lstrip("# ").strip(); slug=re.sub(r"[^a-z0-9]+","-",title.lower()).strip("-")[:60]
    put("research-journal",f"lessons/{slug}.md",p); n+=1
put("research-journal","status/programme.md","# Programme status\n2026-09-16: team created; Stage 1 (discovery) not yet started. No posts briefed. reference/ holds two earlier single-session posts (countries; US states) as citable, non-inherited material.\n")
print("seeded lessons:",n)
for s,sid in stores.items():
    print(s, "memories:", [m.path for m in c.beta.memory_stores.memories.list(sid)])
