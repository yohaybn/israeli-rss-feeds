#!/usr/bin/env python3
"""Regenerate every derived file from feeds.json. Run after editing feeds.json:
   python scripts/build_opml.py

Writes:
- opml/israeli-rss-feeds.opml        all feeds, one outline per category
- opml/by-category/<id>.opml         one file per category (empty categories too,
                                     so the paths stay stable for apps)
- opml/by-language/<lang>.opml       e.g. en.opml for the English-language feeds
- README.md                          the catalog tables between the
                                     <!-- catalog:start --> / <!-- catalog:end --> markers
Stdlib only."""
import json, html, os, glob
from datetime import date

def esc(s): return html.escape(str(s or ''), quote=True)

def opml_doc(title, cats):
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           f'<opml version="2.0">\n  <head>\n    <title>{esc(title)}</title>',
           f'    <dateCreated>{date.today().isoformat()}</dateCreated>\n    <ownerName>israeli-rss-feeds</ownerName>\n  </head>\n  <body>']
    for cat in cats:
        if not cat['feeds']:
            out.append(f'    <outline text="{esc(cat["name_he"])}" title="{esc(cat["name_he"])}"/>')
            continue
        out.append(f'    <outline text="{esc(cat["name_he"])}" title="{esc(cat["name_he"])}">')
        for fd in cat['feeds']:
            out.append(f'      <outline type="rss" text="{esc(fd["title"])}" title="{esc(fd["title"])}" xmlUrl="{esc(fd["url"])}" htmlUrl="{esc(fd.get("homepage") or "")}"/>')
        out.append('    </outline>')
    out.append('  </body>\n</opml>')
    return '\n'.join(out) + '\n'

def fmt_num(n): return '-' if n is None else f'{n:,}'

def readme_block(catalog):
    cats = catalog['categories']
    total = sum(len(c['feeds']) for c in cats)
    filled = sum(1 for c in cats if c['feeds'])
    lines = [f'**{total} פידים ב-{len(cats)} קטגוריות** ({filled} מהן עם פידים כרגע; השאר ריקות עד שהגילוי השבועי ימצא מקורות מתאימים).', '',
             '| קטגוריה | תחום | פידים |', '|---|---|---|']
    for c in cats:
        lines.append(f"| {c['name_he']} | {c.get('description_he', '')} | {len(c['feeds'])} |")
    for c in cats:
        lines += ['', f"### {c['name_he']} ({c['name_en']})", '']
        if not c['feeds']:
            lines.append('_אין עדיין פידים בקטגוריה הזו._')
            continue
        lines += ['| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |', '|---|---|---|---|---|']
        for f in c['feeds']:
            p = f.get('popularity') or {}
            lines.append(f"| [{f['title']}]({f['url']}) | {f['site']} | {f.get('language', '')} | "
                         f"{fmt_num(p.get('feedly_subscribers'))} | {fmt_num(p.get('tranco_rank'))} |")
    return '\n'.join(lines)

def update_readme(catalog, path='README.md'):
    if not os.path.exists(path): return
    text = open(path, encoding='utf-8').read()
    start, end = '<!-- catalog:start -->', '<!-- catalog:end -->'
    if start not in text or end not in text:
        print('README.md has no catalog markers - skipped'); return
    head, rest = text.split(start, 1)
    _, tail = rest.split(end, 1)
    open(path, 'w', encoding='utf-8').write(f'{head}{start}\n{readme_block(catalog)}\n{end}{tail}')

catalog = json.load(open('feeds.json', encoding='utf-8'))
cats = catalog['categories']
os.makedirs('opml/by-category', exist_ok=True)
os.makedirs('opml/by-language', exist_ok=True)
open('opml/israeli-rss-feeds.opml', 'w').write(opml_doc('Israeli RSS Feeds - קטלוג פידים ישראלי', cats))
ids = {c['id'] for c in cats}
for stale in glob.glob('opml/by-category/*.opml'):
    if os.path.basename(stale)[:-5] not in ids:
        os.remove(stale)
for cat in cats:
    open(f'opml/by-category/{cat["id"]}.opml', 'w').write(opml_doc(f'Israeli RSS - {cat["name_he"]}', [cat]))
langs = sorted({f.get('language') for c in cats for f in c['feeds']} - {None, 'he'})
for stale in glob.glob('opml/by-language/*.opml'):
    if os.path.basename(stale)[:-5] not in langs:
        os.remove(stale)
for lang in langs:
    sub = [dict(c, feeds=[f for f in c['feeds'] if f.get('language') == lang]) for c in cats]
    sub = [c for c in sub if c['feeds']]
    open(f'opml/by-language/{lang}.opml', 'w').write(opml_doc(f'Israeli RSS - {lang}', sub))
update_readme(catalog)
print('Regenerated:', sum(len(c['feeds']) for c in cats), 'feeds in', len(cats), 'categories')
