#!/usr/bin/env python3
"""Build review pages and vector figures from the studies' checked figure records.

Standard library only. This presentation step never fits a statistical model.
The same chart geometry is consumed by the PDF builder.
"""
from pathlib import Path
import argparse, csv, html, json, math, re, textwrap

HERE = Path(__file__).resolve().parent
MEN = '#343434'
WOMEN = '#f05a00'
ACCENT = '#384ec7'
INK = '#202623'
MUTED = '#5a625e'
BG = '#f8f9f6'
STUDIES = ['E08', 'E03', 'E10']
META = {'E08': ('Canada', 'AI use and unpaid work'),
        'E03': ('Brazil', 'Understanding overlapping reasons for nonuse'),
        'E10': ('United States', 'Measuring AI exposure within couples')}

def escape(value):
    return html.escape(str(value), quote=True)

def plain(value):
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', str(value))
    return text.replace('**', '').replace('`', '').replace('*', '')

def inline(value):
    """Render a deliberately small safe Markdown subset."""
    held = []
    def save(markup):
        held.append(markup)
        return f'ZZPLACEHOLDER{len(held)-1}ZZ'
    def link(m):
        label, target = m.groups()
        if re.match(r'^(?:javascript|data):', target, re.I):
            return label
        return save(f'<a href="{escape(target)}">{escape(label)}</a>')
    value = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, str(value))
    value = escape(value)
    value = re.sub(r'`([^`]+)`', r'<code>\1</code>', value)
    value = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', value)
    value = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', value)
    for i, markup in enumerate(held):
        value = value.replace(f'ZZPLACEHOLDER{i}ZZ', markup)
    return value

def blocks(text):
    """Shared block parser for the HTML and PDF editions."""
    lines = text.splitlines(); i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1; continue
        m = re.fullmatch(r'<!--\s*FIGURE:\s*([\w-]+)\s*-->', line)
        if m:
            yield ('figure', m[1]); i += 1; continue
        m = re.match(r'^(#{1,6})\s+(.*)$', line)
        if m:
            yield ('heading', (len(m[1]), m[2])); i += 1; continue
        if line.startswith('```'):
            chunk = []; i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                chunk.append(lines[i]); i += 1
            yield ('code', '\n'.join(chunk)); i += 1; continue
        if line.startswith('|') and i+1 < len(lines) and re.match(r'^\s*\|?[\s:|-]+\|\s*$', lines[i+1]):
            rows = [[x.strip() for x in line.strip('|').split('|')]]; i += 2
            while i < len(lines) and lines[i].strip().startswith('|'):
                rows.append([x.strip() for x in lines[i].strip().strip('|').split('|')]); i += 1
            yield ('table', rows); continue
        if re.match(r'^[-*]\s|^\d+\.\s', line):
            ordered = bool(re.match(r'^\d+\.\s', line)); items = []
            while i < len(lines) and re.match(r'^\s*(?:[-*]|\d+\.)\s+', lines[i]):
                items.append(re.sub(r'^\s*(?:[-*]|\d+\.)\s+', '', lines[i])); i += 1
            yield ('olist' if ordered else 'list', items); continue
        if re.fullmatch(r'[-*_]{3,}', line):
            yield ('rule', None); i += 1; continue
        paragraph = [line]; i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r'^\s*(?:#|```|<!--|\||[-*]\s|\d+\.\s)', lines[i]):
            paragraph.append(lines[i].strip()); i += 1
        yield ('paragraph', ' '.join(paragraph))

def markdown(text, figures=None, omit_first_title=False):
    out = []; omitted = False
    for kind, item in blocks(text):
        if kind == 'heading':
            level, value = item
            if omit_first_title and level == 1 and not omitted:
                omitted = True; continue
            level = max(2, min(5, level))
            anchor = re.sub(r'[^a-z0-9]+', '-', plain(value).lower()).strip('-')
            out.append(f'<h{level} id="{anchor}">{inline(value)}</h{level}>')
        elif kind == 'paragraph': out.append(f'<p>{inline(item)}</p>')
        elif kind == 'code': out.append(f'<pre><code>{escape(item)}</code></pre>')
        elif kind in ('list', 'olist'):
            tag = 'ol' if kind == 'olist' else 'ul'
            out.append(f'<{tag}>'+''.join(f'<li>{inline(x)}</li>' for x in item)+f'</{tag}>')
        elif kind == 'table':
            out.append('<div class="table-wrap"><table><thead><tr>'+''.join(f'<th>{inline(x)}</th>' for x in item[0])+'</tr></thead><tbody>')
            out.extend('<tr>'+''.join(f'<td>{inline(x)}</td>' for x in row)+'</tr>' for row in item[1:])
            out.append('</tbody></table></div>')
        elif kind == 'rule': out.append('<hr>')
        elif kind == 'figure':
            if figures is None or item not in figures: raise ValueError(f'Unknown figure marker {item}')
            out.append(figure_html(figures[item]))
    return '\n'.join(out)

def row_colour(row):
    group = row.get('group', '').lower()
    if 'women' in group or 'female' in group: return WOMEN
    if group in ('men', 'men+', 'male'): return MEN
    return ACCENT

def number(value, unit='percent'):
    if value is None: return 'Not estimated'
    text = f'{float(value):.1f}'
    return text + ('%' if unit == 'percent' else ' pp' if unit == 'percentage_points' else '')

def row_label(row):
    label=plain(row['label']); group=row.get('group','')
    if group.lower() in ('men','men+','women','women+','male','female') and group.lower() not in label.lower():
        label=group+': '+label
    if row.get('quality')=='E':label+=' [E]'
    return label

def chart_geometry(fig, compact=False):
    """Shared data and scales, with stacked labels on narrow screens."""
    rows=fig['rows']; width=346 if compact else 760
    left,right,top=(10,330,30) if compact else (280,657,36)
    numeric=[float(r[k]) for r in rows for k in ('value','low','high') if r.get(k) is not None]
    if not numeric: raise ValueError('No figure estimates')
    lo,hi=min(0,min(numeric)),max(numeric)
    if fig.get('domain'):lo,hi=map(float,fig['domain'])
    elif fig.get('unit')=='percent':
        lo=math.floor(lo/10)*10;hi=min(100,max(10,math.ceil(hi/10)*10))
    else:
        lim=max(abs(lo),abs(hi),1);tick=1 if lim<=5 else 5 if lim<=25 else 10
        lo=math.floor(lo/tick)*tick;hi=math.ceil(hi/tick)*tick
    if lo==hi:hi=lo+1
    transform=lambda x:left+(float(x)-lo)/(hi-lo)*(right-left)
    wrapped=[textwrap.wrap(row_label(r),width=41 if compact else 33,break_long_words=False,break_on_hyphens=False) for r in rows]
    steps=[max(76,len(lines)*18+48) if compact else max(53,len(lines)*16+20) for lines in wrapped]
    sections=[];last=None
    for r in rows:
        section=r.get('section')
        sections.append(section if section and section!=last else None);last=section
    section_gaps=[38 if x else 0 for x in sections]
    bottom=top+sum(steps)+sum(section_gaps)
    axis_lines=textwrap.wrap(fig.get('x_label',''),width=45 if compact else 78,break_long_words=False)
    height=bottom+39+len(axis_lines)*16
    primitives=[]
    def line(x1,y1,x2,y2,colour,stroke=1,**kwargs):primitives.append(dict(kind='line',x1=x1,y1=y1,x2=x2,y2=y2,colour=colour,stroke=stroke,**kwargs))
    def text(x,y,value,size=13,anchor='start',colour=INK,weight='normal'):primitives.append(dict(kind='text',x=x,y=y,text=str(value),size=size,anchor=anchor,colour=colour,weight=weight))
    ticks=fig.get('ticks') or [lo+(hi-lo)*j/4 for j in range(5)]
    references=([0] if lo<0<hi else [])
    if fig.get('reference_line') is not None:references.append(float(fig['reference_line']))
    references=sorted(set(v for v in references if lo<=v<=hi))
    ticks=sorted(set(ticks+references))
    # In compact view the scale is repeated lightly on each row. It never runs through labels.
    if not compact:
        for v in ticks:line(transform(v),top-19,transform(v),bottom-12,'#d9ded8',0.7)
        for ref in references:line(transform(ref),top-19,transform(ref),bottom-12,'#939d96',1.2)
    for v in ticks:text(transform(v),bottom+11,f'{v:g}',12,'middle',MUTED)
    offset=0
    for i,row in enumerate(rows):
        if sections[i]:
            section_lines=textwrap.wrap(sections[i],width=44 if compact else 90)
            for j,label in enumerate(section_lines):text(0,top+offset+j*16,label,13,colour=ACCENT,weight='bold')
            offset+=section_gaps[i]
        step=steps[i];base=top+offset;offset+=step;colour=row_colour(row);label_lines=wrapped[i]
        if compact:
            for j,label in enumerate(label_lines):text(0,base+j*18,label,14)
            y=base+len(label_lines)*18+24
            for v in ticks:line(transform(v),y-11,transform(v),y+3,'#d9ded8',0.8)
            for ref in references:line(transform(ref),y-11,transform(ref),y+3,'#939d96',1.2)
            line(left,y-4,right,y-4,'#d9ded8',0.7)
        else:
            y=base+step/2-18
            for j,label in enumerate(label_lines):text(0,y-((len(label_lines)-1)*8)+j*16,label,13)
        if row.get('value') is None:
            text(left,y,'Not estimated',13,colour=MUTED);continue
        tip=f'{row_label(row)}: {number(row["value"],fig.get("unit"))}'
        if row.get('low') is not None and row.get('high') is not None:
            tip+=f'; interval {number(row["low"],fig.get("unit"))} to {number(row["high"],fig.get("unit"))}'
            x1,x2=transform(row['low']),transform(row['high'])
            line(x1,y-4,x2,y-4,colour,2.2)
            line(x1,y-8,x1,y,colour,1.5);line(x2,y-8,x2,y,colour,1.5)
        if row.get('n') is not None:tip+=f'; sample count {row["n"]:,}'
        if row.get('quality')=='E':tip+='; use with caution'
        if row.get('section'):tip=row['section']+'; '+tip
        primitives.append(dict(kind='point',x=transform(row['value']),y=y-4,colour=colour,radius=4.5,tip=tip,row=i))
        text(right if compact else right+15,y-18 if compact else y,number(row['value'],fig.get('unit')),14 if compact else 13,anchor='end' if compact else 'start',colour=INK,weight='bold')
        if i<len(rows)-1:line(0,base+step-14 if compact else y+step/2,width,base+step-14 if compact else y+step/2,'#e7eae4',0.5)
    for j,label in enumerate(axis_lines):text((left+right)/2,bottom+34+j*16,label,12,'middle',MUTED)
    return dict(width=width,height=height,primitives=primitives,domain=[lo,hi])

def svg_figure(fig, compact=False):
    geo=chart_geometry(fig, compact); parts=[]
    suffix="-compact" if compact else ""
    for p in geo['primitives']:
        if p['kind']=='line': parts.append(f'<line x1="{p["x1"]:.2f}" y1="{p["y1"]:.2f}" x2="{p["x2"]:.2f}" y2="{p["y2"]:.2f}" stroke="{p["colour"]}" stroke-width="{p["stroke"]}"/>')
        elif p['kind']=='text': parts.append(f'<text x="{p["x"]:.2f}" y="{p["y"]:.2f}" fill="{p["colour"]}" font-size="{p["size"]}" text-anchor="{p["anchor"]}" font-weight="{p["weight"]}">{escape(p["text"])}</text>')
        else:parts.append(f'<g class="data-mark" tabindex="0" role="img" aria-label="{escape(p["tip"])}"><title>{escape(p["tip"])}</title><circle cx="{p["x"]:.2f}" cy="{p["y"]:.2f}" r="{p["radius"]}" fill="{p["colour"]}"/></g>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {geo["width"]} {geo["height"]}" width="{geo["width"]}" height="{geo["height"]}" role="img" aria-labelledby="title-{fig["id"]}{suffix} desc-{fig["id"]}{suffix}"><title id="title-{fig["id"]}{suffix}">{escape(fig["title"])}</title><desc id="desc-{fig["id"]}{suffix}">{escape(fig.get("description",""))}</desc><g font-family="Arial,sans-serif">'+''.join(parts)+'</g></svg>'

def figure_html(fig):
    fields=['label','group','value','low','high','n']
    names=['Comparison','Group','Estimate','Lower interval','Upper interval','Sample count']
    if all(r.get('group') == 'neutral' for r in fig['rows']):
        fields.remove('group');names.remove('Group')
    if any(r.get('section') for r in fig['rows']):fields.insert(0,'section');names.insert(0,fig.get('section_label','Respondent eligibility'))
    if any(r.get('quality') for r in fig['rows']):fields+=['quality'];names+=['Quality flag']
    head='<tr>'+''.join(f'<th>{escape(x)}</th>' for x in names)+'</tr>'
    def value(row,key):
        v=row.get(key)
        if v is None:return 'Not reported'
        if key in ('value','low','high'):return number(v,fig.get('unit'))
        if key=='n':return f'{v:,}'
        if key=='quality':return {'A':'Meets release threshold','E':'Use with caution','F':'Suppressed'}.get(v,v)
        return str(v)
    body=''.join('<tr>'+''.join(f'<td>{escape(value(row,k))}</td>' for k in fields)+'</tr>' for row in fig['rows'])
    source=f'<a href="{escape(fig["source_url"])}">{escape(fig["source_label"])}</a>' if fig.get('source_url') else escape(fig.get('source_label',''))
    markup = f'''<figure id="{fig['id']}"><figcaption><h3>{escape(fig['title'])}</h3><p>{inline(fig.get('description',''))}</p></figcaption><div class="figure-desktop">{svg_figure(fig)}</div><div class="figure-mobile">{svg_figure(fig, compact=True)}</div><p class="chart-note">{inline(fig.get('footnote',''))}</p><p class="source">Source: {source.rstrip('.')}</p><div class="figure-tools"><details><summary>View chart values</summary><div class="table-wrap"><table><thead>{head}</thead><tbody>{body}</tbody></table></div><p><a href="figures/{fig['id']}.csv" download>Download values (CSV)</a> · Units: {escape(fig.get('unit',''))}</p></details><a href="methods.html">View methodology</a><a href="analysis.py">View Python script</a></div></figure>'''
    if fig.get('optional'):
        return '<details class="supporting-figure"><summary>'+escape(fig.get('optional_label','Explore the supporting figure'))+'</summary>'+markup+'</details>'
    return markup

def shell(title,content,study=None):
    prefix='../' if study else ''
    report='../../../report-v1/index.html' if study else '../../report-v1/index.html'
    explorer='../../../explore-data-v1/index.html' if study else '../../explore-data-v1/index.html'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Original public-data research on gender and generative AI"><title>{escape(title)} | Gender &amp; Generative AI</title><link rel="stylesheet" href="{prefix}studies.css?v=20261008-narrative"></head><body><a class="skip" href="#main">Skip to content</a><header class="topbar"><a class="brand" href="{report}">The State of Gender &amp; Generative AI</a><nav aria-label="Main navigation"><a href="{report}">Read report</a><a href="{explorer}">Explore data</a><a href="{prefix}../index.html" aria-current="page">Further research</a></nav></header><main id="main">{content}</main><footer>Sources are linked at the point of use. <a href="{prefix}README.md">Research and reproduction record</a></footer><script src="{prefix}studies.js?v=20261008-revised"></script></body></html>'''

def build_study(sid):
    directory=HERE/sid
    text=(directory/'manuscript.md').read_text()
    title=next(item[1] for kind,item in blocks(text) if kind=='heading' and item[0]==1)
    data=json.loads((directory/'figure-specs.json').read_text())
    copy_path=directory/'presentation-copy.json'
    if copy_path.is_file():
        edits=json.loads(copy_path.read_text())
        # Derived displays select existing rows, so a clean analysis rebuild
        # recreates them without introducing or changing an estimator.
        data['figures'] = [f for f in data['figures'] if not edits.get(f['id'], {}).get('derived_from')]
        for fid, edit in edits.items():
            if 'derived_from' not in edit:
                continue
            source = next(f for f in data['figures'] if f['id'] == edit['derived_from'])
            available = {r['result_id']: r for r in source['rows']}
            ids = edit['selected_result_ids']
            if len(ids) != len(set(ids)) or not set(ids) <= set(available):
                raise ValueError(f'Invalid derived display: {sid}/{fid}')
            data['figures'].append(dict(source, id=fid, rows=[dict(available[i]) for i in ids]))
        for fig in data['figures']:
            edit=edits[fig['id']]
            fig.update(edit['figure'])
            for row in fig['rows']:
                row.update(edit['rows'][row['result_id']])
            if 'row_order' in edit:
                order = edit['row_order']
                by_id = {row['result_id']: row for row in fig['rows']}
                if len(by_id) != len(fig['rows']) or len(order) != len(by_id) or set(order) != set(by_id):
                    raise ValueError(f'Incomplete or duplicate presentation order: {sid}/{fig["id"]}')
                fig['rows'] = [by_id[result_id] for result_id in order]
        (directory/'figure-specs.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
    figs={f['id']:f for f in data['figures']}
    fdir=directory/'figures';fdir.mkdir(exist_ok=True)
    for fid,fig in figs.items():
        (fdir/f'{fid}.svg').write_text(svg_figure(fig))
        with (fdir/f'{fid}.csv').open('w',newline='') as stream:
            fields=['section','label','group','value','low','high','n','quality','result_id'];w=csv.DictWriter(stream,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(fig['rows'])
    # Keep consolidated chart downloads aligned with the final presentation labels.
    values_path=directory/'figure-values.csv'
    if values_path.is_file():
        with values_path.open() as stream:
            reader=csv.DictReader(stream);columns=reader.fieldnames;values=list(reader)
        by_key={(f['id'],r['result_id']):r for f in figs.values() for r in f['rows']}
        for row in values:
            source=by_key.get((row['figure_id'],row['result_id']))
            if source:
                for key in ('label','group'):
                    if key in row:row[key]=source[key]
        with values_path.open('w',newline='') as stream:
            writer=csv.DictWriter(stream,fieldnames=columns);writer.writeheader();writer.writerows(values)
    country,_=META[sid]
    hero=f'<div class="article-head"><p class="eyebrow">Original research · {country}</p><h1>{inline(title)}</h1><p class="edition">Emily Birch · 9 October 2026</p><p class="article-links"><a href="paper.pdf">Download PDF</a><a href="methods.html">Methodology</a><a href="reproduction.zip">Reproduction files</a></p></div>'
    (directory/'index.html').write_text(shell(plain(title),hero+'<article>'+markdown(text,figs,True)+'</article>',sid))
    method=(directory/'METHODS.md').read_text()
    (directory/'methods.html').write_text(shell('Methodology: '+plain(title),'<p class="eyebrow">Methods and reproducibility</p><h1>'+inline(title)+'</h1><p><a href="index.html">Return to the paper</a> · <a href="analysis.py">Python analysis</a> · <a href="source-manifest.json">Source versions</a></p>'+markdown(method),sid))
    return dict(id=sid,title=plain(title),country=country,figures=len(figs),figure_rows=sum(len(x['rows']) for x in figs.values()))

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--study',choices=STUDIES);args=parser.parse_args()
    rows=[build_study(s) for s in ([args.study] if args.study else STUDIES)]
    if not args.study:
        cards=''.join(f'<a class="paper-card" href="{r["id"]}/index.html"><span class="eyebrow">{r["country"]}</span><h2>{escape(r["title"])}</h2><span>Read the research →</span></a>' for r in rows)
        content='<div class="article-head"><p class="eyebrow">The State of Gender &amp; Generative AI</p><h1>Original research</h1><p>Three studies investigate what AI participation means for working time, how reported barriers combine, and how measurement choices shape gender comparisons.</p><p class="edition">9 October 2026</p></div><div class="paper-cards">'+cards+'</div><p class="scope">Each paper states its population and the limits of its evidence. The studies describe associations and measurement choices; they do not identify the causal effects of adopting AI.</p>'
        (HERE/'index.html').write_text(shell('Original research',content))
    (HERE/'site-build.json').write_text(json.dumps({'studies':rows,'browser_review_record':'../approved-revision-2026-10-09/PRESENTATION-CHECKS.json','renderer':'page-native vector SVG from figure-specs.json'},indent=2)+'\n')
    print(json.dumps(rows))

if __name__=='__main__':main()
