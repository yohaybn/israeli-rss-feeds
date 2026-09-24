#!/usr/bin/env python3
"""Regenerate the OPML files from feeds.json. Run after editing feeds.json:
   python scripts/build_opml.py
Stdlib only."""
import json, html, os
from datetime import date

def esc(s): return html.escape(str(s or ''), quote=True)

def opml_doc(title, cats):
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           f'<opml version="2.0">\n  <head>\n    <title>{esc(title)}</title>',
           f'    <dateCreated>{date.today().isoformat()}</dateCreated>\n    <ownerName>israeli-rss-feeds</ownerName>\n  </head>\n  <body>']
    for cat in cats:
        out.append(f'    <outline text="{esc(cat["name_he"])}" title="{esc(cat["name_he"])}">')
        for fd in cat['feeds']:
            out.append(f'      <outline type="rss" text="{esc(fd["title"])}" title="{esc(fd["title"])}" xmlUrl="{esc(fd["url"])}" htmlUrl="{esc(fd.get("homepage") or "")}"/>')
        out.append('    </outline>')
    out.append('  </body>\n</opml>')
    return '\n'.join(out) + '\n'

catalog = json.load(open('feeds.json'))
cats = catalog['categories']
os.makedirs('opml/by-category', exist_ok=True)
open('opml/israeli-rss-feeds.opml', 'w').write(opml_doc('Israeli RSS Feeds - קטלוג פידים ישראלי', cats))
for cat in cats:
    open(f'opml/by-category/{cat["id"]}.opml', 'w').write(opml_doc(f'Israeli RSS - {cat["name_he"]}', [cat]))
print('OPML regenerated:', sum(len(c['feeds']) for c in cats), 'feeds')
