"""Fill missing item fields (image, description, author, categories) from each article page.

Only items that lack a field are fetched, and a field the source already gave is never
overwritten. The image is stored as a URL in an <enclosure> (hotlink, no image is copied).
A cache keeps each article from being fetched twice; items with nothing found are retried
after RETRY_NONE_DAYS. Stdlib only.
"""
import html
import json
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from urllib.parse import urljoin

from feedlib import DESCRIPTION_MAX, _image_type

DC_NS = 'http://purl.org/dc/elements/1.1/'
MAX_FETCH_PER_RUN = 40
RETRY_NONE_DAYS = 3
MAX_CATEGORIES = 6
_META = re.compile(r'<meta\b[^>]*>', re.I)
_ATTR = re.compile(r'([a-zA-Z_:-]+)\s*=\s*("([^"]*)"|\'([^\']*)\')')
_JSONLD = re.compile(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', re.I | re.S)

ET.register_namespace('dc', DC_NS)


def _attrs(tag):
    return {m.group(1).lower(): html.unescape(m.group(3) if m.group(3) is not None else m.group(4))
            for m in _ATTR.finditer(tag)}


def _clean(text):
    return re.sub(r'\s+', ' ', html.unescape(text or '')).strip()


def _ld_nodes(page):
    for block in _JSONLD.findall(page):
        try:
            data = json.loads(html.unescape(block).strip())
        except ValueError:
            continue
        stack = [data]
        while stack:
            node = stack.pop()
            if isinstance(node, dict):
                yield node
                stack.extend(node.values())
            elif isinstance(node, list):
                stack.extend(node)


def _first_str(value):
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        return _first_str(value.get('url') or value.get('name'))
    if isinstance(value, list):
        for v in value:
            s = _first_str(v)
            if s:
                return s
    return None


def parse_article_meta(page, base_url=''):
    """{'image','description','author','categories'} found in the page (missing ones omitted)."""
    if isinstance(page, bytes):
        page = page.decode('utf-8', 'ignore')
    metas = {}
    tags = []
    for tag in _META.findall(page):
        a = _attrs(tag)
        name = (a.get('property') or a.get('name') or a.get('itemprop') or '').lower()
        content = _clean(a.get('content'))
        if not name or not content:
            continue
        metas.setdefault(name, content)
        if name == 'article:tag':
            tags.append(content)
    out = {}
    image = metas.get('og:image') or metas.get('twitter:image') or metas.get('image')
    desc = metas.get('og:description') or metas.get('description') or metas.get('twitter:description')
    author = metas.get('author') or metas.get('article:author')
    section = metas.get('article:section')
    keywords = [k.strip() for k in re.split(r'[,;]', metas.get('keywords', '')) if k.strip()]
    for node in _ld_nodes(page):
        image = image or _first_str(node.get('image'))
        desc = desc or _first_str(node.get('description'))
        if not author and node.get('author'):
            author = _first_str(node.get('author'))
        if not section and isinstance(node.get('articleSection'), (str, list)):
            section = _first_str(node.get('articleSection'))
    if image:
        image = urljoin(base_url, image.strip())
        if re.match(r'https?://', image):
            out['image'] = image
    if desc:
        out['description'] = _clean(desc)[:DESCRIPTION_MAX]
    if author and not re.match(r'https?://', author):
        out['author'] = _clean(author)[:120]
    cats = []
    for c in ([section] if section else []) + tags + keywords:
        c = _clean(c)
        if c and c not in cats and len(c) <= 60:
            cats.append(c)
    if cats:
        out['categories'] = cats[:MAX_CATEGORIES]
    return out


def _missing(item):
    gaps = set()
    if item.find('enclosure') is None:
        gaps.add('image')
    if not (item.findtext('description') or '').strip():
        gaps.add('description')
    if item.find('{%s}creator' % DC_NS) is None and not (item.findtext('author') or '').strip():
        gaps.add('author')
    if item.find('category') is None:
        gaps.add('categories')
    return gaps


def _apply(item, meta, gaps):
    """Add only the fields in `gaps`. Returns how many fields were added."""
    added = 0
    if 'image' in gaps and meta.get('image'):
        enc = ET.SubElement(item, 'enclosure')
        enc.set('url', meta['image'])
        enc.set('type', _image_type(meta['image']))
        enc.set('length', '0')
        added += 1
    if 'description' in gaps and meta.get('description'):
        d = item.find('description')
        if d is None:
            d = ET.SubElement(item, 'description')
        d.text = meta['description']
        added += 1
    if 'author' in gaps and meta.get('author'):
        ET.SubElement(item, '{%s}creator' % DC_NS).text = meta['author']
        added += 1
    if 'categories' in gaps and meta.get('categories'):
        for c in meta['categories']:
            ET.SubElement(item, 'category').text = c
        added += 1
    return added


def enrich_batch(xml_bytes, fetch, cache, budget, now=None):
    """Return (new_xml_bytes, fields_added). `budget` is a one-element list with the fetches left
    for this run (shared across feeds). `cache` maps article URL -> {'meta':{...},'at':iso}."""
    now = now or datetime.now(timezone.utc)
    root = ET.fromstring(xml_bytes)
    added = 0
    for item in root.findall('./channel/item'):
        link = (item.findtext('link') or '').strip()
        gaps = _missing(item)
        if not link or not gaps:
            continue
        entry = cache.get(link)
        if entry is not None:
            fresh = now - datetime.fromisoformat(entry['at']) < timedelta(days=RETRY_NONE_DAYS)
            if entry['meta'] or fresh:
                added += _apply(item, entry['meta'], gaps)
                continue
        if not gaps & {'image', 'description'}:
            continue  # only items missing their image or summary justify a page fetch
        if budget[0] <= 0:
            continue
        budget[0] -= 1
        try:
            page = fetch(link)
        except Exception:
            page = None
        if page is None:
            continue  # blocked or failed: try again next run, do not cache
        meta = parse_article_meta(page, link)
        cache[link] = {'meta': meta, 'at': now.isoformat()}
        added += _apply(item, meta, gaps)
    if not added:
        return xml_bytes, 0
    return ET.tostring(root, encoding='UTF-8', xml_declaration=True), added


def prune_cache(cache, live_links):
    for link in [k for k in cache if k not in live_links]:
        del cache[link]
