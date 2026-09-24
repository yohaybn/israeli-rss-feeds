#!/usr/bin/env python3
"""Weekly discovery of new Israeli feeds.

Scans the seed sites in scripts/discovery-sites.txt (homepage <link> tags +
common feed paths), skips feeds already catalogued in feeds.json, validates
that candidates are live, and writes discovery-issue.md. The workflow opens
it as a GitHub issue for manual review - nothing is added automatically.

Sites answering with bot-protection codes are skipped quietly (they need a
real browser to verify). Stdlib only.
"""
import json, re, sys, os, urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_feeds import fetch, parse_feed  # noqa: E402

LINK_RE = re.compile(r'<link[^>]+type=["\'](?:application/(?:rss|atom)\+xml)["\'][^>]*>', re.I)
HREF_RE = re.compile(r'href=["\']([^"\']+)["\']', re.I)
COMMON_PATHS = ("/feed/", "/feed", "/rss", "/rss.xml", "/feed.xml", "/atom.xml", "/?feed=rss2")
MAX_CANDIDATES_PER_SITE = 4

def known_urls():
    catalog = json.load(open('feeds.json'))
    return {f['url'] for c in catalog['categories'] for f in c['feeds']}

def seed_sites():
    sites = []
    for line in open('scripts/discovery-sites.txt'):
        line = line.strip()
        if line and not line.startswith('#'):
            sites.append(line)
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
    for u in found:
        if u not in known and u not in seen:
            seen.add(u)
            out.append(u)
    return out[:MAX_CANDIDATES_PER_SITE]

def validate(u):
    try:
        _st, body = fetch(u)
        items, newest = parse_feed(body)
        return items > 0
    except Exception:
        return False

def main():
    known = known_urls()
    candidates = []
    with ThreadPoolExecutor(10) as ex:
        futs = {ex.submit(candidates_for, s, known): s for s in seed_sites()}
        for fut in as_completed(futs):
            site = futs[fut]
            for u in fut.result():
                candidates.append((site, u))
    fresh = []
    with ThreadPoolExecutor(12) as ex:
        futs = {ex.submit(validate, u): (s, u) for s, u in candidates}
        for fut in as_completed(futs):
            s, u = futs[fut]
            if fut.result():
                fresh.append((s, u))
    if not fresh:
        print('no new live feeds found')
        return
    lines = ['The weekly discovery scan found live feeds that are not in the catalog yet.',
             '', 'Review and add worthy ones to `feeds.json` (then run `scripts/build_opml.py`).', '']
    for site, u in sorted(fresh):
        lines.append(f'- [ ] `{u}` (found via {urllib.parse.urlparse(site).netloc})')
    lines.append('')
    open('discovery-issue.md', 'w').write('\n'.join(lines))
    print(f'{len(fresh)} new candidates -> discovery-issue.md')

if __name__ == '__main__':
    main()
