"""ONE football highlights (public JSON listing) -> RSS 2.0.

Title and link only, per repo policy: no video enclosure, no description.
Football only; the league label is read from the ONE category and, when that is
generic, from the title and the teams named in it (same rules as the Android app).
"""
import json
import os
import re
from datetime import datetime, timezone
from urllib.parse import quote
from zoneinfo import ZoneInfo
from feedlib import jsonfeed_to_rss

TEAMS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'football-teams.json')
# ONE VOD categories that are football highlights. Basketball (19) is deliberately not here.
CATEGORIES = [(9, 'כדורגל'), (113, 'הליגה הספרדית'), (56, 'הליגה האיטלקית'), (158, 'מונדיאל')]
LISTING_URL = 'https://www.one.co.il/JSON/v6/Videos/VOD/%d/?page=1&qty=40'
EURO = 'מפעלים אירופיים'
PREFIXES = 'הולבמשכ'
SCORE = re.compile(r'\d+\s*[:\-]\s*\d+')
NEGATIVE = ('ראיון', 'מסיבת עיתונאים', 'מסיבת עיתונאי', 'פודקאסט', 'אימון', 'פרשנות', 'מאחורי הקלעים')
COMPETITIONS = [
    ('ליגת האלופות', ('ליגת האלופות', 'champions league')),
    ('הליגה האירופית', ('הליגה האירופית', 'europa league', 'ליגה אירופית')),
    ('ליגת הקונפרנס', ('קונפרנס', 'conference league')),
    ('גביע המדינה', ('גביע המדינה', 'גביע הטוטו')),
    ('מונדיאל', ('מונדיאל', 'world cup', 'גביע העולם')),
    ('ליגת העל', ('ליגת העל', 'ליגת ווינר', 'ליגת וינר')),
]


def norm(text):
    text = text.lower()
    text = re.sub('["\'\u05f3\u05f4\u201c\u201d\u2018\u2019`.]', '', text)
    text = re.sub('[-\u2013\u05be]', ' ', text)
    return re.sub(r'\s+', ' ', text).strip()


def load_teams(path=TEAMS_PATH):
    with open(path, encoding='utf-8') as f:
        return json.load(f)['teams']


def _entries(teams):
    out = [(norm(a), t) for t in teams for a in t['aliases']]
    return sorted([e for e in out if len(e[0]) >= 2], key=lambda e: -len(e[0]))


def detect_teams(title, teams, limit=2):
    """Longest alias first, matched spans are consumed, one Hebrew prefix letter allowed."""
    s = list(' ' + norm(title) + ' ')
    found = []
    for alias, team in _entries(teams):
        pos = 0
        while True:
            text = ''.join(s)
            i = text.find(alias, pos)
            if i < 0:
                break
            end = i + len(alias)
            ok = not (end < len(s) and s[end].isalnum())
            if ok and i > 0 and s[i - 1].isalnum():
                ok = s[i - 1] in PREFIXES and (i < 2 or not s[i - 2].isalnum())
            if ok:
                if all(t['id'] != team['id'] for _, t in found):
                    found.append((i, team))
                for k in range(i, end):
                    s[k] = '\0'
            pos = end
    return [t for _, t in sorted(found, key=lambda x: x[0])][:limit]


def league_for(category_label, title, teams):
    if category_label != 'כדורגל':
        return category_label
    n = norm(title)
    for label, names in COMPETITIONS:
        if any(norm(x) in n for x in names):
            return label
    found = detect_teams(title, teams)
    if not found:
        return 'כדורגל'
    leagues = list(dict.fromkeys(EURO if t['league'] == 'ליגת האלופות' else t['league'] for t in found))
    if len(leagues) == 1:
        return leagues[0]
    return 'נבחרות' if 'נבחרות' in leagues else EURO


def duration_seconds(text):
    parts = [int(p) for p in (text or '').split(':') if p.strip().isdigit()]
    if not parts or len(parts) > 3:
        return None
    total = 0
    for p in parts:
        total = total * 60 + p
    return total


def is_match_highlight(title, duration, teams):
    if any(w in title for w in NEGATIVE):
        return False
    sec = duration_seconds(duration)
    if sec is not None and sec < 90:
        return False
    found = len(detect_teams(title, teams))
    return bool(SCORE.search(title)) or 'תקציר' in title or found >= 2 or (found == 1 and sec is not None)


def _link(item):
    url = ((item.get('URL') or {}).get('PC') or '').strip()
    if url.startswith('https://www.one.co.il/VOD/Play/'):
        return 'https://www.one.co.il/VOD/Play/' + quote(url[len('https://www.one.co.il/VOD/Play/'):], safe="/-_.~")
    return 'https://www.one.co.il/VOD/Play/%s' % item['ID']


def listings_to_rss(listings, site, teams, feed_url=None, now=None):
    """listings: [(category_label, ONE JSON dict)] -> (rss_bytes, item_count)."""
    tz = ZoneInfo('Asia/Jerusalem')
    seen = set()
    items = []
    for label, data in listings:
        for it in (((data.get('Data') or {}).get('Videos') or {}).get('Items') or []):
            vid = it.get('ID')
            title = ((it.get('Title') or {}).get('Main') or '').strip()
            if not isinstance(vid, int) or not title or vid in seen:
                continue
            if not is_match_highlight(title, it.get('Duration'), teams):
                continue
            try:
                published = datetime.fromisoformat(it['Date']).replace(tzinfo=tz).astimezone(timezone.utc)
            except (KeyError, ValueError):
                continue
            seen.add(vid)
            items.append({'id': 'one:%d' % vid, 'url': _link(it), 'title': title,
                          'date_published': published.isoformat(), 'tags': [league_for(label, title, teams)]})
    items.sort(key=lambda x: x['date_published'], reverse=True)
    items = items[:25]
    rss, count = jsonfeed_to_rss(json.dumps({'title': site['name'], 'home_page_url': site['url'], 'items': items}).encode('utf-8'),
                                 site_name=site['name'], site_url=site['url'], lang=site.get('lang'), feed_url=feed_url, now=now)
    import xml.etree.ElementTree as ET
    root = ET.fromstring(rss)
    by_guid = {('one:' + str(i['id']).split(':')[1]): i for i in items}
    for el in root.findall('channel/item'):
        guid = el.find('guid')
        if guid is not None:
            guid.set('isPermaLink', 'false')
            tag = by_guid.get(guid.text or '')
            if tag:
                ET.SubElement(el, 'category').text = tag['tags'][0]
    return ET.tostring(root, encoding='UTF-8', xml_declaration=True), count
