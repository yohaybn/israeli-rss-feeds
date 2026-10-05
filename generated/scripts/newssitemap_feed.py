"""Public Google News sitemaps -> RSS. Title + link + date + thumbnail only, no article pages fetched."""
import json
import xml.etree.ElementTree as ET
from urllib.parse import urlsplit
from feedlib import jsonfeed_to_rss

NS = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9',
      'news': 'http://www.google.com/schemas/sitemap-news/0.9',
      'image': 'http://www.google.com/schemas/sitemap-image/1.1'}


def sitemap_locs(payload):
    """<loc> values of a sitemap index."""
    return [e.text.strip() for e in ET.fromstring(payload).findall('sm:sitemap/sm:loc', NS) if e.text]


def sitemap_items(payload, host):
    """Items from one news sitemap; links outside the publisher host are dropped."""
    items = []
    for url in ET.fromstring(payload).findall('sm:url', NS):
        link = (url.findtext('sm:loc', '', NS) or '').strip()
        parts = urlsplit(link)
        news = url.find('news:news', NS)
        if parts.scheme != 'https' or parts.hostname != host or news is None:
            continue
        title = (news.findtext('news:title', '', NS) or '').strip()
        date = (news.findtext('news:publication_date', '', NS) or '').strip()
        if not title or not date:
            continue
        item = {'id': link, 'url': link, 'title': title, 'date_published': date}
        image = (url.findtext('image:image/image:loc', '', NS) or '').strip()
        if image.startswith('https://'):
            item['image'] = image
        items.append(item)
    return items


def sitemaps_to_rss(items, site, feed_url=None):
    """Newest 25 unique items as RSS. Raises on an empty list."""
    seen, unique = set(), []
    for item in sorted(items, key=lambda i: i['date_published'], reverse=True):
        if item['url'] not in seen:
            seen.add(item['url'])
            unique.append(item)
    if not unique:
        raise ValueError('News sitemap has no usable items')
    return jsonfeed_to_rss(json.dumps({'title': site['name'], 'home_page_url': site['url'],
                                       'items': unique[:25]}).encode('utf-8'),
                           site_name=site['name'], site_url=site['url'],
                           lang=site.get('lang'), feed_url=feed_url)
