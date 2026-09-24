#!/usr/bin/env python3
"""Weekly discovery of new Israeli feeds.

Scans the seed sites in scripts/discovery-sites.txt (homepage <link> tags +
common feed paths), skips feeds already catalogued in feeds.json, validates
that candidates are live, and writes discovery-issue.md. The seed file is
split into "[category-id]" sections, so each candidate comes with a suggested
category; the issue lists empty categories first. The workflow opens it as a
GitHub issue for manual review - nothing is added automatically.

Sites answering with bot-protection codes are skipped quietly (they need a
real browser to verify). Stdlib only.
"""
import json, re, sys, os, urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_feeds import fetch, parse_feed, is_stale  # noqa: E402

LINK_RE = re.compile(r'<link[^>]+type=["\'](?:application/(?:rss|atom)\+xml)["\'][^>]*>', re.I)
HREF_RE = re.compile(r'href=["\']([^"\']+)["\']', re.I)
COMMON_PATHS = ("/feed/", "/feed", "/rss", "/rss.xml", "/feed.xml", "/atom.xml", "/?feed=rss2")
MAX_CANDIDATES_PER_SITE = 4

def load_catalog():
    return json.load(open('feeds.json', encoding='utf-8'))

def known_urls(catalog):
    return {f['url'] for c in catalog['categories'] for f in c['feeds']}

def seed_sites(valid_ids):
    """Return [(site, category_id)] from the sectioned seed file."""
    sites, current = [], None
    for line in open('scripts/discovery-sites.txt', encoding='utf-8'):
        line = line.split('#', 1)[0].strip()
        if not line:
            continue
        if line.startswith('[') and line.endswith(']'):
            current = line[1:-1].strip()
            if current not in valid_ids:
                print(f'warning: unknown category [{current}] in discovery-sites.txt', file=sys.stderr)
            continue
        sites.append((line, current))
    return sites

def candidates_for(site, known):
    found = []
    try:
        _st, body = fetch(site, cap=800_000)
        final_html = body.decode('utf-8', 'ignore')
        for tag in LINK_RE.findall(final_html):
            m = HREF_RE.search(tag)
            if m:
                found.append(urllib.parse.urljoin(site, m.group(1)))
    except Exception:
        pass
    for path in COMMON_PATHS:
        found.append(urllib.parse.urljoin(site, path))
    out, seen = [], set()
    known_norm = {k.rstrip('/') for k in known}
    for u in found:
        if '/comments/feed' in u:  # WordPress comment feeds, not content
            continue
        key = u.rstrip('/')
        if key not in known_norm and key not in seen:
            seen.add(key)
            out.append(u)
    return out[:MAX_CANDIDATES_PER_SITE]

def validate(u):
    try:
        _st, body = fetch(u)
        items, newest = parse_feed(body)
        return items > 0 and not is_stale(newest)
    except Exception:
        return False

def main():
    catalog = load_catalog()
    cats = catalog['categories']
    names = {c['id']: c['name_he'] for c in cats}
    sizes = {c['id']: len(c['feeds']) for c in cats}
    known = known_urls(catalog)
    candidates, seen = [], set()
    with ThreadPoolExecutor(10) as ex:
        futs = {ex.submit(candidates_for, s, known): (s, cid) for s, cid in seed_sites(set(names))}
        for fut in as_completed(futs):
            site, cid = futs[fut]
            for u in fut.result():
                if u not in seen:
                    seen.add(u)
                    candidates.append((cid, site, u))
    fresh = []
    with ThreadPoolExecutor(12) as ex:
        futs = {ex.submit(validate, u): (cid, s, u) for cid, s, u in candidates}
        for fut in as_completed(futs):
            if fut.result():
                fresh.append(futs[fut])
    if not fresh:
        print('no new live feeds found')
        return
    empty = [names[c] for c in names if sizes[c] == 0]
    lines = ['The weekly discovery scan found live feeds that are not in the catalog yet.',
             '', 'Review and add worthy ones to `feeds.json` under the suggested category '
             '(or a better one), then run `scripts/build_opml.py`.', '']
    if empty:
        lines += ['Categories still empty: ' + ', '.join(empty), '']
    order = {c['id']: i for i, c in enumerate(cats)}
    by_cat = {}
    for cid, site, u in fresh:
        by_cat.setdefault(cid, []).append((site, u))
    # empty categories first, then thin ones, then catalog order
    for cid in sorted(by_cat, key=lambda c: (sizes.get(c, 0) > 0, sizes.get(c, 0), order.get(c, 99))):
        label = f"{names[cid]} (`{cid}`, {sizes[cid]} feeds now)" if cid in names else 'Uncategorized'
        lines += [f'### {label}', '']
        for site, u in sorted(by_cat[cid]):
            lines.append(f'- [ ] `{u}` (found via {urllib.parse.urlparse(site).netloc})')
        lines.append('')
    open('discovery-issue.md', 'w').write('\n'.join(lines))
    print(f'{len(fresh)} new candidates -> discovery-issue.md')

if __name__ == '__main__':
    main()
