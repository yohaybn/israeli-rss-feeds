#!/usr/bin/env python3
"""Build world/feeds.json - an international catalog converted from
plenaryapp/awesome-rss-feeds (CC0) - and verify every feed against the live site.

    python scripts/sync_world.py            # re-sync from upstream + verify
    python scripts/sync_world.py --local DIR  # use an already-downloaded upstream checkout
    python scripts/sync_world.py --only-new   # verify only feeds missing from status.json, keep the rest as-is

Upstream publishes OPML files by topic (recommended/with_category/*.opml) and by
country (countries/with_category/*.opml). Each upstream topic maps to one of our
21 categories (CATEGORY_MAP); country files are general news and go to "news"
with a "country" field.

world/curated.json adds hand-picked feeds for categories upstream does not cover
(e.g. ai). They go through the same verification; their category and language
are fixed (no podcast re-mapping) and upstream_category is "Curated".

A feed enters the catalog only if it passes verification: HTTP 200, parseable
RSS/Atom, at least one item, newest item no older than STALE_DAYS.
Feeds already in world/feeds.json get a grace period: a feed is dropped only
after failing MAX_FAILS weekly runs in a row, and 401/403/429 answers (bot
protection against CI IPs) do not count as failures for them. If more than
ABORT_RATIO of the feeds fail in one run, nothing is written (network trouble,
not dead feeds).

Writes world/feeds.json, world/opml/*, world/status.json, world/FEEDS-STATUS.md
and the tables in world/README.md. Stdlib only.
"""
import io, json, os, re, sys, zipfile, html, urllib.request, urllib.error, urllib.parse
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from email.utils import parsedate_to_datetime
from datetime import datetime, timezone, date

UPSTREAM = 'plenaryapp/awesome-rss-feeds'
UPSTREAM_ZIP = 'https://codeload.github.com/plenaryapp/awesome-rss-feeds/zip/refs/heads/master'
STALE_DAYS = 90
MAX_FAILS = 2
ABORT_RATIO = 0.4
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
UA_READER = "Feedly/1.0 (+http://www.feedly.com/fetcher.html; like FeedFetcher-Google)"
NOW = datetime.now(timezone.utc)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORLD = os.path.join(ROOT, 'world')

# upstream topic -> our category id (same 21 ids as the Israeli feeds.json)
CATEGORY_MAP = {
    'News': 'news',
    'Tech': 'tech', 'Android': 'tech', 'Apple': 'tech', 'Programming': 'tech',
    'Android Development': 'tech', 'iOS Development': 'tech', 'Web Development': 'tech',
    'UI - UX': 'tech', 'Cyber security': 'tech',
    'Business & Economy': 'business', 'Startups': 'business',
    'Personal finance': 'business', 'Cryptocurrency': 'business',
    'Sports': 'sports', 'Football': 'sports', 'Cricket': 'sports', 'Tennis': 'sports',
    'Movies': 'culture', 'Television': 'culture', 'Books': 'culture',
    'History': 'culture', 'Photography': 'culture',
    'Science': 'science', 'Space': 'science', 'Environment': 'science',
    'Nature': 'science', 'Animal & Wildlife': 'science',
    'Music': 'music',
    'Gaming': 'gaming', 'Chess': 'gaming',
    'Food': 'food',
    'Travel': 'travel',
    'Cars': 'auto',
    'Fashion': 'fashion', 'Beauty': 'fashion',
    'Interior design': 'real-estate', 'Architecture': 'real-estate', 'DIY': 'real-estate',
    'Funny': 'digital-culture', 'Memes': 'digital-culture',
}

COUNTRY_CODES = {
    'Australia': 'AU', 'Bangladesh': 'BD', 'Brazil': 'BR', 'Canada': 'CA', 'France': 'FR',
    'Germany': 'DE', 'Hong Kong SAR China': 'HK', 'India': 'IN', 'Indonesia': 'ID', 'Iran': 'IR',
    'Ireland': 'IE', 'Italy': 'IT', 'Japan': 'JP', 'Mexico': 'MX', 'Myanmar (Burma)': 'MM',
    'Nigeria': 'NG', 'Pakistan': 'PK', 'Philippines': 'PH', 'Poland': 'PL', 'Russia': 'RU',
    'South Africa': 'ZA', 'Spain': 'ES', 'Ukraine': 'UA', 'United Kingdom': 'GB', 'United States': 'US',
}

CATEGORIES = [  # same ids/names as the root feeds.json
    ('news', 'חדשות ואקטואליה', 'News & Current Affairs', 'חדשות בארץ ובעולם, מבזקים'),
    ('tech', "טכנולוגיה וגאדג'טים", 'Technology & Gadgets', 'חדשות הייטק, מוצרי צריכה'),
    ('business', 'כלכלה ועסקים', 'Economy & Business', 'שוק ההון, פיננסים, יזמות'),
    ('sports', 'ספורט', 'Sports', 'חדשות ספורט, תוצאות, פרשנויות'),
    ('culture', 'תרבות ופנאי', 'Culture & Entertainment', 'קולנוע, טלוויזיה, ספרות'),
    ('health', 'בריאות ורפואה', 'Health & Medicine', 'חדשות רפואיות, בריאות הציבור'),
    ('science', 'מדע וסביבה', 'Science & Environment', 'תגליות, אקולוגיה, חלל'),
    ('music', 'מוזיקה', 'Music', 'עדכוני אמנים, ביקורות אלבומים'),
    ('gaming', 'גיימינג', 'Gaming', 'חדשות משחקי וידאו, קונסולות'),
    ('food', 'אוכל וקולינריה', 'Food & Cooking', 'מתכונים, מסעדות'),
    ('travel', 'תיירות ופנאי', 'Travel & Leisure', 'טיולים, חופשות, תעופה'),
    ('auto', 'רכב ותחבורה', 'Cars & Transportation', 'חדשות רכב, תחבורה ציבורית'),
    ('fashion', 'אופנה ולייף סטייל', 'Fashion & Lifestyle', 'טרנדים, טיפוח'),
    ('real-estate', 'נדל"ן ועיצוב הבית', 'Real Estate & Home Design', 'שוק הדיור, עיצוב פנים'),
    ('parenting', 'הורות ומשפחה', 'Parenting & Family', 'גידול ילדים, חינוך'),
    ('opinion', 'דעה וטורים אישיים', 'Opinion & Personal Columns', 'מאמרי דעה, בלוגים כלליים'),
    ('podcasts', 'פודקאסטים', 'Podcasts', 'עדכונים על פרקים חדשים'),
    ('career', 'קריירה ועבודה', 'Career & Work', 'חיפוש עבודה, ניהול, התפתחות מקצועית'),
    ('consumer', 'צרכנות ומבצעים', 'Consumer & Deals', 'חדשות צרכנות, דילים'),
    ('digital-culture', 'תרבות דיגיטלית ורשת', 'Digital Culture & Web', 'ממים, טרנדים ברשתות חברתיות'),
    ('ai', 'בינה מלאכותית', 'Artificial Intelligence', 'חדשות, בלוגים ומדריכים על בינה מלאכותית'),
]

# ---------- upstream ----------
BAD_AMP = re.compile(rb'&(?!amp;|lt;|gt;|quot;|apos;|#\d+;|#x[0-9a-fA-F]+;)')

def parse_opml(data):
    data = BAD_AMP.sub(b'&amp;', data)
    try:
        root = ET.fromstring(data)
        return [o.attrib for o in root.iter('outline') if o.get('xmlUrl')]
    except ET.ParseError:
        # some upstream files have unescaped quotes inside attributes - fall back to a line scan
        out = []
        for line in data.decode('utf-8', 'replace').splitlines():
            u = re.search(r'xmlUrl="([^"]+)"', line)
            if not u: continue
            t = re.search(r'text="(.*?)" title=', line)
            out.append({'xmlUrl': html.unescape(u.group(1)), 'title': html.unescape(t.group(1)) if t else ''})
        return out

def load_upstream(local=None):
    files = {}
    if local:
        for sub in ('recommended/with_category', 'countries/with_category'):
            for fn in os.listdir(os.path.join(local, sub)):
                if fn.endswith('.opml'):
                    files[f'{sub}/{fn}'] = open(os.path.join(local, sub, fn), 'rb').read()
    else:
        z = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(
            urllib.request.Request(UPSTREAM_ZIP, headers={'User-Agent': UA}), timeout=60).read()))
        for n in z.namelist():
            rel = n.split('/', 1)[1] if '/' in n else n
            if rel.endswith('.opml') and '/with_category/' in rel:
                files[rel] = z.read(n)
    cands, unmapped = [], {}
    for rel in sorted(files, key=lambda r: (not r.startswith('recommended'), r)):
        name = os.path.basename(rel)[:-5]
        try:
            outlines = parse_opml(files[rel])
        except ET.ParseError as e:
            print(f'skip unparseable upstream file {rel}: {e}'); continue
        if rel.startswith('recommended'):
            cat, extra = CATEGORY_MAP.get(name), {'upstream_category': name}
            if not cat:
                unmapped[name] = len(outlines); continue
        else:
            cat, extra = 'news', {'upstream_category': f'Country: {name}', 'country': COUNTRY_CODES.get(name, name)}
        for o in outlines:
            cands.append({'title': html.unescape(o.get('title') or o.get('text') or '').strip(),
                          'url': o['xmlUrl'].strip(), 'category': cat, **extra})
    return cands, unmapped

def load_curated():
    path = os.path.join(WORLD, 'curated.json')
    if not os.path.exists(path): return []
    out = []
    for f in json.load(open(path, encoding='utf-8'))['feeds']:
        assert f['category'] in {c[0] for c in CATEGORIES}, f"unknown category {f['category']} in curated.json"
        out.append({'title': f['title'], 'url': f['url'].strip(), 'category': f['category'],
                    'upstream_category': 'Curated', 'curated': True,
                    'language': f.get('language'), 'homepage': f.get('homepage')})
    return out

# ---------- verification ----------
def fetch(url, ua=UA, timeout=12, cap=40_000_000, hops=0):
    req = urllib.request.Request(url, headers={'User-Agent': ua, 'Accept': 'application/rss+xml, application/atom+xml, application/xml, text/xml, */*',
                                               'Accept-Encoding': 'identity'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read(cap)
            if body[:2] == b'\x1f\x8b':  # some servers gzip even when asked not to
                import gzip
                body = gzip.decompress(body)
            return r.status, r.geturl(), body
    except urllib.error.HTTPError as e:
        if e.code in (301, 302, 303, 307, 308) and hops < 5 and e.headers.get('Location'):
            return fetch(urllib.parse.urljoin(url, e.headers['Location']), ua, timeout, cap, hops + 1)
        raise

INVALID_XML = re.compile(rb'[\x00-\x08\x0b\x0c\x0e-\x1f]')
DC = '{http://purl.org/dc/elements/1.1/}'
ATOM = '{http://www.w3.org/2005/Atom}'
XML_LANG = '{http://www.w3.org/XML/1998/namespace}lang'

def to_dt(v):
    if not v or not v.strip(): return None
    v = v.strip()
    try: d = parsedate_to_datetime(v)
    except Exception:
        try: d = datetime.fromisoformat(v.replace('Z', '+00:00'))
        except Exception: return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)

def first(el, *paths):
    # NB: never use `el.find(a) or el.find(b)` - an Element with no children is falsy
    for p in paths:
        e = el.find(p)
        if e is not None and (e.text or '').strip():
            return e.text.strip()
    return None

import html.entities
ENTITY = re.compile(rb'&([A-Za-z][A-Za-z0-9]*);')

def lenient_root(data):
    data = INVALID_XML.sub(b'', data.lstrip(b'\xef\xbb\xbf \t\r\n'))
    try:
        return ET.fromstring(data)
    except ET.ParseError:
        # what feed readers tolerate: HTML entities (&nbsp;) and bare ampersands
        def ent(m):
            n = m.group(1).decode()
            if n in ('amp', 'lt', 'gt', 'quot', 'apos'): return m.group(0)
            cp = html.entities.name2codepoint.get(n)
            return f'&#{cp};'.encode() if cp else b'&amp;' + m.group(1) + b';'
        fixed = BAD_AMP.sub(b'&amp;', ENTITY.sub(ent, data))
        return ET.fromstring(fixed)

def parse_feed(data):
    root = lenient_root(data)
    tag = root.tag.lower().split('}')[-1]
    info = {'items': 0, 'newest': None, 'link': None, 'language': None, 'feed_title': None, 'audio': False}
    dates = []
    if tag in ('rss', 'rdf'):
        chan = root.find('channel')
        if chan is None:
            chan = next((c for c in root if c.tag.endswith('channel')), root)
        its = chan.findall('item') or root.findall('item') or [c for c in root if c.tag.endswith('}item')]
        info['items'] = len(its)
        info['link'] = first(chan, 'link', '{http://purl.org/rss/1.0/}link')
        info['language'] = first(chan, 'language', DC + 'language')
        info['feed_title'] = first(chan, 'title', '{http://purl.org/rss/1.0/}title')
        for it in its[:30]:
            dates.append(to_dt(first(it, 'pubDate', DC + 'date', ATOM + 'updated', ATOM + 'published')))
            enc = it.find('enclosure')
            if enc is not None and (enc.get('type') or '').startswith('audio'): info['audio'] = True
    elif tag == 'feed':
        ents = root.findall(ATOM + 'entry') or root.findall('entry')
        info['items'] = len(ents)
        info['language'] = root.get(XML_LANG)
        info['feed_title'] = first(root, ATOM + 'title', 'title')
        for l in root.findall(ATOM + 'link') + root.findall('link'):
            if l.get('rel', 'alternate') == 'alternate' and l.get('href'):
                info['link'] = l.get('href'); break
        for it in ents[:30]:
            dates.append(to_dt(first(it, ATOM + 'published', ATOM + 'updated', 'published', 'updated')))
    else:
        raise ValueError(f'root <{tag}> is not a feed')
    dates = [d for d in dates if d and d <= NOW.replace(year=NOW.year + 1)]
    info['newest'] = max(dates) if dates else None
    return info

def verify(url, timeout=12):
    """-> (status, note, info). status: ok | stale | blocked | dead"""
    last = None
    for ua in (UA, UA_READER):
        try:
            st, final, body = fetch(url, ua, timeout)
            info = parse_feed(body)
            info['final_url'] = final
            if info['items'] == 0:
                return 'dead', 'no items', info
            if info['newest'] is None:
                return 'stale', 'no item dates', info
            age = (NOW - info['newest']).total_seconds() / 86400
            if age > STALE_DAYS:
                return 'stale', f'newest item {int(age)}d old', info
            return 'ok', '', info
        except urllib.error.HTTPError as e:
            last = ('blocked', f'HTTP {e.code}') if e.code in (401, 403, 429) else ('dead', f'HTTP {e.code}')
            if e.code == 404 and 'youtube.com/feeds/' in url:
                # YouTube answers 404 to datacenter IPs (this sandbox and GitHub Actions) even for live channels
                return 'blocked', 'HTTP 404 (YouTube blocks datacenter IPs)', {}
            if e.code not in (401, 403, 406, 429): break
        except (ET.ParseError, ValueError) as e:
            last = ('dead', f'not a valid feed: {str(e)[:70]}')  # retry with the reader UA (some sites serve bots HTML/empty)
        except Exception as e:
            last = ('dead', f'{type(e).__name__}: {str(e)[:80]}')
            break
    return last[0], last[1], {}

# ---------- output ----------
LANG_BY_COUNTRY = {'FR': 'fr', 'DE': 'de', 'IT': 'it', 'ES': 'es', 'MX': 'es', 'BR': 'pt', 'JP': 'ja',
                   'RU': 'ru', 'UA': 'uk', 'PL': 'pl', 'IR': 'fa', 'ID': 'id', 'MM': 'my', 'BD': 'bn'}

def norm_lang(v, country=None):
    if v:
        v = v.strip().lower().replace('_', '-').split('-')[0]
        if re.fullmatch(r'[a-z]{2,3}', v): return v
    return LANG_BY_COUNTRY.get(country, 'en')

def site_name(url):
    h = urllib.parse.urlsplit(url).hostname or ''
    return h[4:] if h.startswith('www.') else h

def upgrade_url(orig, final):
    """Use the redirect target only for a same-host http->https (or trailing-slash) move."""
    if not final or final == orig: return orig
    a, b = urllib.parse.urlsplit(orig), urllib.parse.urlsplit(final)
    if (a.hostname or '').removeprefix('www.') == (b.hostname or '').removeprefix('www.') and b.scheme == 'https' \
            and a.path.rstrip('/') == b.path.rstrip('/') and a.query == b.query:
        return final
    return orig

def esc(s): return html.escape(str(s or ''), quote=True)

def opml_doc(title, cats):
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           f'<opml version="2.0">\n  <head>\n    <title>{esc(title)}</title>',
           f'    <dateCreated>{date.today().isoformat()}</dateCreated>\n    <ownerName>israeli-rss-feeds</ownerName>\n  </head>\n  <body>']
    for c in cats:
        if not c['feeds']:
            out.append(f'    <outline text="{esc(c["name_en"])}" title="{esc(c["name_en"])}"/>'); continue
        out.append(f'    <outline text="{esc(c["name_en"])}" title="{esc(c["name_en"])}">')
        for f in c['feeds']:
            out.append(f'      <outline type="rss" text="{esc(f["title"])}" title="{esc(f["title"])}" xmlUrl="{esc(f["url"])}" htmlUrl="{esc(f.get("homepage") or "")}"/>')
        out.append('    </outline>')
    out.append('  </body>\n</opml>')
    return '\n'.join(out) + '\n'

def md(s): return str(s).replace('|', '\\|').replace('[', '(').replace(']', ')')

def readme_block(catalog, rejected_count, unmapped):
    cats = catalog['categories']
    total = catalog['feed_count']
    lines = [f'**{total} פידים מאומתים ב-{sum(1 for c in cats if c["feeds"])} מתוך {len(cats)} קטגוריות** '
             f'(עודכן {catalog["generated_at"]}; {rejected_count} פידים מהמקור נפסלו בבדיקה - הפירוט ב-[`FEEDS-STATUS.md`](FEEDS-STATUS.md)).', '',
             '| קטגוריה | פידים | קטגוריות במקור |', '|---|---|---|']
    src = {}
    for k, v in CATEGORY_MAP.items(): src.setdefault(v, []).append(k)
    src.setdefault('news', []).append('כל קובצי המדינות')
    src.setdefault('podcasts', []).append('כל פיד עם פרקי אודיו, מכל נושא')
    for f in load_curated():
        if 'רשימה ידנית (curated.json)' not in src.get(f['category'], []):
            src.setdefault(f['category'], []).append('רשימה ידנית (curated.json)')
    for c in cats:
        lines.append(f"| {c['name_he']} ({c['name_en']}) | {len(c['feeds'])} | {', '.join(src.get(c['id'], [])) or '-'} |")
    if unmapped:
        lines += ['', 'קטגוריות במקור שלא ממופות (לא נכנסו): ' + ', '.join(sorted(unmapped))]
    for c in cats:
        if not c['feeds']: continue
        lines += ['', f"### {c['name_he']} ({c['name_en']})", '', '| פיד | אתר | שפה | מקור |', '|---|---|---|---|']
        for f in c['feeds']:
            lines.append(f"| [{md(f['title'])}]({f['url']}) | {md(f['site'])} | {f['language']} | {md(f['upstream_category'])} |")
    return '\n'.join(lines)

def update_readme(block, path):
    text = open(path, encoding='utf-8').read()
    s, e = '<!-- catalog:start -->', '<!-- catalog:end -->'
    head, rest = text.split(s, 1); _, tail = rest.split(e, 1)
    open(path, 'w', encoding='utf-8').write(f'{head}{s}\n{block}\n{e}{tail}')

def main():
    local = sys.argv[sys.argv.index('--local') + 1] if '--local' in sys.argv else None
    only_new = '--only-new' in sys.argv
    cands, unmapped = load_upstream(local)
    cands = load_curated() + cands  # curated first, so a curated entry wins the dedupe
    if unmapped: print('unmapped upstream categories:', unmapped)
    # dedupe by URL, first mapping wins (topic files before country files)
    seen, uniq = set(), []
    for c in cands:
        k = c['url'].lower().rstrip('/').replace('http://', 'https://')
        if k in seen: continue
        seen.add(k); uniq.append(c)
    fjson = os.path.join(WORLD, 'feeds.json'); sjson = os.path.join(WORLD, 'status.json')
    prev_urls = set()
    if os.path.exists(fjson):
        prev = json.load(open(fjson, encoding='utf-8'))
        prev_urls = {f['source_url'] for c in prev['categories'] for f in c['feeds']}
    status = json.load(open(sjson, encoding='utf-8')) if os.path.exists(sjson) else {}
    # --only-new: feeds already in status.json keep their last result ('frozen'), only the rest are fetched
    todo = [i for i, c in enumerate(uniq) if not (only_new and c['url'] in status)]
    results = [('frozen', '', {})] * len(uniq)
    with ThreadPoolExecutor(96) as ex:
        for i, r in zip(todo, ex.map(lambda i: verify(uniq[i]['url']), todo)):
            results[i] = r
    # second pass for network errors (timeouts, TLS, DNS) - usually transient
    retry = [i for i, r in enumerate(results) if r[0] == 'dead' and ('Error' in r[1] and 'HTTP' not in r[1])]
    with ThreadPoolExecutor(32) as ex:
        for i, r in zip(retry, ex.map(lambda i: verify(uniq[i]['url'], timeout=30), retry)):
            results[i] = r
    failed = sum(1 for i in todo if results[i][0] != 'ok')
    print(f'{len(uniq)} feeds, {len(todo)} verified, {len(todo) - failed} passed')
    if todo and failed / len(todo) > ABORT_RATIO and prev_urls:
        print(f'{failed}/{len(todo)} failed - looks like a network problem, not writing'); sys.exit(1)
    by_cat = {cid: [] for cid, *_ in CATEGORIES}
    rejected, new_status = [], {}
    for c, (st, note, info) in zip(uniq, results):
        u = c['url']
        old = status.get(u, {})
        if st == 'frozen':
            new_status[u] = old
            if u in prev_urls and old.get('entry'):
                by_cat[old.get('category', c['category'])].append(old['entry'])
            else:
                rejected.append((c, old.get('status', 'dead'), old.get('note', '')))
            continue
        fails = 0 if st == 'ok' else old.get('fails', 0) + (0 if st == 'blocked' else 1)
        keep = st == 'ok' or (u in prev_urls and fails < MAX_FAILS)
        new_status[u] = {'status': st, 'note': note, 'fails': fails,
                         'last_ok': NOW.date().isoformat() if st == 'ok' else old.get('last_ok')}
        if not keep:
            rejected.append((c, st, note)); continue
        if st != 'ok' and old.get('entry'):
            by_cat[old.get('category', c['category'])].append(old['entry'])
            new_status[u].update(entry=old['entry'], category=old.get('category', c['category'])); continue
        url = upgrade_url(u, info.get('final_url'))
        homepage = c.get('homepage') or info.get('link') or f"{urllib.parse.urlsplit(url).scheme}://{urllib.parse.urlsplit(url).netloc}/"
        entry = {'title': c['title'] or info.get('feed_title') or site_name(url), 'url': url,
                 'site': site_name(homepage if homepage.startswith('http') else url),
                 'homepage': homepage, 'language': norm_lang(c.get('language') or info.get('language'), c.get('country')),
                 'popularity': {'feedly_subscribers': None, 'tranco_rank': None, 'source': []},
                 'upstream_category': c['upstream_category'], 'source_url': u}
        if c.get('country'): entry['country'] = c['country']
        if info.get('newest'): entry['last_item'] = info['newest'].date().isoformat()
        # podcasts (audio enclosures) go to the podcasts category; upstream_category keeps the topic.
        # curated feeds keep the category they were picked for.
        cat = 'podcasts' if info.get('audio') and not c.get('curated') else c['category']
        new_status[u]['entry'] = entry
        new_status[u]['category'] = cat
        by_cat[cat].append(entry)
    cats = [{'id': cid, 'name_he': he, 'name_en': en, 'description_he': d,
             'feeds': sorted(by_cat[cid], key=lambda f: (f.get('country') is not None, f.get('country') or '', f['title'].lower()))}
            for cid, he, en, d in CATEGORIES]
    total = sum(len(c['feeds']) for c in cats)
    catalog = {'version': 2, 'name': 'israeli-rss-feeds/world',
               'description': 'International RSS catalog converted from plenaryapp/awesome-rss-feeds (CC0) plus a curated list (world/curated.json), every feed verified live',
               'source': f'https://github.com/{UPSTREAM}', 'generated_at': NOW.date().isoformat(),
               'feed_count': total, 'categories': cats}
    os.makedirs(os.path.join(WORLD, 'opml', 'by-category'), exist_ok=True)
    json.dump(catalog, open(fjson, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    open(fjson, 'a').write('\n')
    json.dump(dict(sorted(new_status.items())), open(sjson, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    open(os.path.join(WORLD, 'opml', 'world-rss-feeds.opml'), 'w', encoding='utf-8').write(opml_doc('World RSS Feeds (verified, from plenaryapp/awesome-rss-feeds)', cats))
    for c in cats:
        open(os.path.join(WORLD, 'opml', 'by-category', f"{c['id']}.opml"), 'w', encoding='utf-8').write(opml_doc(f"World RSS - {c['name_en']}", [c]))
    lines = [f'# World feeds status - {NOW.date().isoformat()}', '',
             f'Candidates (upstream + curated): {len(uniq)} unique feeds. In catalog: {total}. Rejected: {len(rejected)}.', '']
    for st, title in (('dead', 'Dead (HTTP error, not a feed, or no items)'), ('stale', f'Stale (no item in {STALE_DAYS} days)'),
                      ('blocked', 'Blocked (401/403/429, or YouTube feeds - could not be verified from CI)')):
        rs = [r for r in rejected if r[1] == st]
        if rs:
            lines += [f'## {title} - {len(rs)}', '']
            lines += [f"- {r[0]['title']} ({r[0]['upstream_category']}) - {r[2]}  \n  `{r[0]['url']}`" for r in sorted(rs, key=lambda r: r[0]['title'].lower())]
            lines.append('')
    open(os.path.join(WORLD, 'FEEDS-STATUS.md'), 'w', encoding='utf-8').write('\n'.join(lines))
    rp = os.path.join(WORLD, 'README.md')
    if os.path.exists(rp): update_readme(readme_block(catalog, len(rejected), unmapped), rp)
    from collections import Counter
    print('per category:', {c['id']: len(c['feeds']) for c in cats})
    print('rejected:', Counter(r[1] for r in rejected))

if __name__ == '__main__':
    main()
