#!/usr/bin/env python3
"""Weekly feed health check for israeli-rss-feeds.

Validates every feed in feeds.json against the live site:
HTTP 200, parseable RSS/Atom XML, at least one item, and a newest item
no older than STALE_DAYS. Writes FEEDS-STATUS.md and exits non-zero when
feeds are dead, so the workflow can open an issue.

Feeds answering 401/403/429 are marked 'blocked' (bot protection), not
dead - many Israeli sites block datacenter IPs while serving readers fine.
Stdlib only, no pip installs.
"""
import json, re, sys, urllib.request, urllib.error, urllib.parse
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from email.utils import parsedate_to_datetime
from datetime import datetime, timezone

STALE_DAYS = 90
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
NOW = datetime.now(timezone.utc)

def fetch(url, timeout=25, cap=4_000_000, hops=0):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*", "Accept-Encoding": "identity"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read(cap)
    except urllib.error.HTTPError as e:
        if e.code in (301, 302, 303, 307, 308) and hops < 5 and e.headers.get('Location'):
            return fetch(urllib.parse.urljoin(url, e.headers['Location']), timeout, cap, hops + 1)
        raise

INVALID_XML = re.compile(rb'[\x00-\x08\x0b\x0c\x0e-\x1f]')

def parse_feed(data):
    data = INVALID_XML.sub(b'', data.lstrip(b"\xef\xbb\xbf \t\r\n"))
    root = ET.fromstring(data)
    tag = root.tag.lower().split('}')[-1]
    items, newest = 0, None
    def dt(v):
        if not v: return None
        try: return parsedate_to_datetime(v.strip())
        except Exception:
            try: return datetime.fromisoformat(v.strip().replace('Z', '+00:00'))
            except Exception: return None
    if tag in ('rss', 'rdf'):
        chan = root.find('channel') if tag == 'rss' else root
        its = (chan.findall('item') if chan is not None else []) or root.findall('item')
        items = len(its)
        for it in its[:15]:
            e = it.find('pubDate') or it.find('{http://purl.org/dc/elements/1.1/}date')
            d = dt(e.text if e is not None else None)
            if d and (newest is None or d > newest): newest = d
    elif tag == 'feed':
        ns = {'a': 'http://www.w3.org/2005/Atom'}
        ents = root.findall('a:entry', ns) or root.findall('entry')
        items = len(ents)
        for it in ents[:15]:
            for p in ('a:updated', 'a:published', 'updated', 'published'):
                e = it.find(p, ns if p.startswith('a:') else {})
                d = dt(e.text if e is not None else None)
                if d: break
            if d and (newest is None or d > newest): newest = d
    else:
        raise ValueError(f"root <{tag}> is not a feed")
    return items, newest

def check(feed):
    url = feed['url']
    try:
        st, body = fetch(url)
        items, newest = parse_feed(body)
        if items == 0:
            return feed, 'dead', 'no items'
        if newest:
            if newest.tzinfo is None: newest = newest.replace(tzinfo=timezone.utc)
            age = (NOW - newest).total_seconds() / 86400
            if age > STALE_DAYS:
                return feed, 'stale', f'newest item {int(age)}d old'
        return feed, 'ok', ''
    except urllib.error.HTTPError as e:
        if e.code in (401, 403, 429):
            return feed, 'blocked', f'HTTP {e.code} (bot protection?)'
        return feed, 'dead', f'HTTP {e.code}'
    except Exception as e:
        return feed, 'dead', f'{type(e).__name__}: {str(e)[:80]}'

def main():
    catalog = json.load(open('feeds.json'))
    flat = [(c['name_he'], f) for c in catalog['categories'] for f in c['feeds']]
    results = {'ok': [], 'stale': [], 'blocked': [], 'dead': []}
    with ThreadPoolExecutor(12) as ex:
        futs = [ex.submit(check, f) for _, f in flat]
        for fut in as_completed(futs):
            feed, status, note = fut.result()
            results[status].append((feed, note))
    date = NOW.strftime('%Y-%m-%d')
    lines = [f'# Feed status - {date}', '',
             f"Checked {len(flat)} feeds: {len(results['ok'])} OK, {len(results['stale'])} stale, "
             f"{len(results['blocked'])} blocked (bot protection), {len(results['dead'])} dead.", '']
    for status, he in (('dead', 'Dead feeds'), ('stale', f'Stale (no item in {STALE_DAYS} days)'),
                       ('blocked', 'Blocked from CI (verify manually)')):
        if results[status]:
            lines += [f'## {he}', '']
            for feed, note in sorted(results[status], key=lambda x: x[0]['title']):
                lines.append(f"- **{feed['title']}** ({feed['site']}) - {note}  ")
                lines.append(f"  `{feed['url']}`")
            lines.append('')
    open('FEEDS-STATUS.md', 'w').write('\n'.join(lines) + '\n')
    print('\n'.join(lines[:4]))
    dead = results['dead'] + results['stale']
    if '--print-issue' in sys.argv and dead:
        body = ['Automatic weekly check found feeds that need attention:', '']
        for feed, note in sorted(dead, key=lambda x: x[0]['title']):
            body.append(f"- [ ] **{feed['title']}** ({feed['site']}) - {note}\n  `{feed['url']}`")
        body += ['', 'Fix: update the URL in `feeds.json`, remove the feed, or find a replacement.', '']
        open('dead-feeds-issue.md', 'w').write('\n'.join(body))
    sys.exit(1 if results['dead'] else 0)

if __name__ == '__main__':
    main()
