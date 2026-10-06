#!/usr/bin/env python3
"""Fill popularity for world/feeds.json: Feedly followers (public API) and Tranco rank (public list).

    python scripts/world_popularity.py              # fill feeds whose popularity.source is empty
    python scripts/world_popularity.py --all        # refresh every feed
    python scripts/world_popularity.py --no-feedly  # Tranco only (Feedly rate-limits some networks)
    python scripts/world_popularity.py --tranco FILE.csv   # use a downloaded Tranco CSV (rank,domain)

Same fields and meaning as the Israeli feeds.json: feedly_subscribers is null when Feedly does not
know the exact feed URL; tranco_rank is null when the site's domain is outside the top million.
Also updates the entries kept in world/status.json so a later sync_world.py run keeps the numbers.
Stdlib only. Feedly is asked politely: one request at a time, backing off on 429.
"""
import csv, io, json, os, sys, time, urllib.request, urllib.error, urllib.parse, zipfile
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORLD = os.path.join(ROOT, 'world')
UA_FEEDLY = "Feedly/1.0 (+http://www.feedly.com/fetcher.html; like FeedFetcher-Google)"
TRANCO_ZIP = 'https://tranco-list.eu/top-1m.csv.zip'
# two-part public suffixes that matter for the catalog (bbc.co.uk, theguardian.com is plain)
SECOND_LEVEL = {'co', 'com', 'org', 'net', 'gov', 'ac', 'edu', 'or', 'ne'}


def load_tranco(path=None):
    raw = open(path, 'rb').read() if path else urllib.request.urlopen(
        urllib.request.Request(TRANCO_ZIP, headers={'User-Agent': UA_FEEDLY}), timeout=120).read()
    if raw[:2] == b'PK':
        z = zipfile.ZipFile(io.BytesIO(raw)); raw = z.read(z.namelist()[0])
    ranks = {}
    for row in csv.reader(io.StringIO(raw.decode('utf-8', 'replace'))):
        if len(row) >= 2 and row[0].isdigit():
            ranks[row[1].lower()] = int(row[0])
    return ranks


def domain_candidates(url):
    """Host first, then parents: news.bbc.co.uk -> news.bbc.co.uk, bbc.co.uk. Never a bare public suffix."""
    host = (urllib.parse.urlsplit(url).hostname or '').lower()
    parts = host.split('.')
    out = []
    for i in range(len(parts) - 1):
        cand = parts[i:]
        if len(cand) == 2 and cand[0] in SECOND_LEVEL and len(cand[1]) == 2:
            continue  # co.uk
        out.append('.'.join(cand))
    return out


def tranco_rank(ranks, *urls):
    best = None
    for url in urls:
        for cand in domain_candidates(url or ''):
            r = ranks.get(cand)
            if r is not None and (best is None or r < best): best = r
            if r is not None: break
    return best


def feedly_subscribers(feed_url):
    """(subscribers or None, answered). Feedly rate-limits (429): wait and retry, never hammer."""
    api = 'https://cloud.feedly.com/v3/feeds/' + urllib.parse.quote('feed/' + feed_url, safe='')
    wait = 60
    for attempt in range(6):
        try:
            req = urllib.request.Request(api, headers={'User-Agent': UA_FEEDLY})
            data = json.loads(urllib.request.urlopen(req, timeout=25).read())
            subs = data.get('subscribers')
            return (subs if isinstance(subs, int) else None), True
        except urllib.error.HTTPError as e:
            if e.code == 404: return None, True      # Feedly does not know this feed: a real answer
            if e.code == 429:
                print('429, waiting', wait, 's', flush=True); time.sleep(wait); wait = min(wait * 2, 300); continue
            return None, False
        except Exception:
            return None, False
    return None, False


def main(argv):
    redo_all = '--all' in argv
    skip_feedly = '--no-feedly' in argv
    tranco_file = argv[argv.index('--tranco') + 1] if '--tranco' in argv else None
    ranks = load_tranco(tranco_file)
    print('tranco domains:', len(ranks))
    path = os.path.join(WORLD, 'feeds.json')
    catalog = json.load(open(path, encoding='utf-8'))
    feeds = [f for c in catalog['categories'] for f in c['feeds']]
    todo = [f for f in feeds if redo_all or not (f.get('popularity') or {}).get('source')]
    print('feeds to fill:', len(todo), 'of', len(feeds))

    def work(f):
        if skip_feedly: return f, None, False
        subs, ok = feedly_subscribers(f['url'])
        return f, subs, ok
    answered = 0
    def paced():
        for f in todo:
            if not skip_feedly: time.sleep(1.2)  # one request at a time, about 50 a minute
            yield work(f)
    if True:
        for n, (f, subs, ok) in enumerate(paced(), 1):
            if n % 25 == 0: print('done', n, 'of', len(todo), flush=True)
            rank = tranco_rank(ranks, f.get('homepage'), f['url'])
            src = []
            if ok: src.append('feedly')
            if rank is not None: src.append('tranco')
            old = f.get('popularity') or {}
            f['popularity'] = {
                'feedly_subscribers': subs if ok else old.get('feedly_subscribers'),
                'tranco_rank': rank,
                'source': src if ok or rank is not None else old.get('source', []),
            }
            if not ok and 'feedly' in old.get('source', []): f['popularity']['source'] = sorted(set(src) | {'feedly'})
            answered += 1 if ok else 0
    print('feedly answered:', answered, 'of', len(todo))
    json.dump(catalog, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    open(path, 'a').write('\n')
    by_url = {f['url']: f['popularity'] for f in feeds}
    spath = os.path.join(WORLD, 'status.json')
    status = json.load(open(spath, encoding='utf-8'))
    for st in status.values():
        e = st.get('entry')
        if e and e.get('url') in by_url: e['popularity'] = by_url[e['url']]
    json.dump(status, open(spath, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    open(spath, 'a').write('\n')


if __name__ == '__main__':
    main(sys.argv[1:])
