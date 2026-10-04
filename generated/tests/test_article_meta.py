import os, sys, unittest, xml.etree.ElementTree as ET
from datetime import datetime, timezone
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from article_meta import parse_article_meta, enrich_batch, prune_cache, add_media_and_guid, stable_guid, MEDIA_NS

NOW = datetime(2026, 10, 4, 12, 0, tzinfo=timezone.utc)
PAGE = '''<html><head>
<meta property="og:image" content="/img/a.jpg">
<meta property="og:description" content="Teaser &amp; more">
<meta name="author" content="Dana Levi">
<meta property="article:section" content="Tech">
<meta property="article:tag" content="AI"><meta property="article:tag" content="Chips">
</head></html>'''


def feed(inner):
    return ('<rss version="2.0"><channel><title>T</title>' + inner + '</channel></rss>').encode()


def item(extra=''):
    return '<item><title>t</title><link>https://x.co.il/1</link>' + extra + '</item>'


class ParseTest(unittest.TestCase):
    def test_fields(self):
        m = parse_article_meta(PAGE, 'https://x.co.il/1')
        self.assertEqual(m['image'], 'https://x.co.il/img/a.jpg')
        self.assertEqual(m['description'], 'Teaser & more')
        self.assertEqual(m['author'], 'Dana Levi')
        self.assertEqual(m['categories'], ['Tech', 'AI', 'Chips'])

    def test_json_ld_fallback(self):
        page = '<script type="application/ld+json">{"image":{"url":"https://c/i.png"},"author":{"name":"A B"}}</script>'
        m = parse_article_meta(page)
        self.assertEqual(m['image'], 'https://c/i.png')
        self.assertEqual(m['author'], 'A B')


class EnrichTest(unittest.TestCase):
    def run_enrich(self, xml, cache=None, budget=5):
        cache = {} if cache is None else cache
        calls = []
        def fetch(url):
            calls.append(url)
            return PAGE
        out, n = enrich_batch(xml, fetch, cache, [budget], NOW)
        return ET.fromstring(out), n, calls, cache

    def test_fills_missing_fields(self):
        root, n, calls, _ = self.run_enrich(feed(item()))
        it = root.find('./channel/item')
        self.assertEqual(it.find('enclosure').get('url'), 'https://x.co.il/img/a.jpg')
        self.assertEqual(it.findtext('description'), 'Teaser & more')
        self.assertEqual(len(it.findall('category')), 3)
        self.assertEqual(n, 4)

    def test_never_overwrites_source_data(self):
        xml = feed(item('<description>source text</description><enclosure url="https://s/i.jpg" type="image/jpeg" length="0"/>'))
        root, n, calls, _ = self.run_enrich(xml)
        it = root.find('./channel/item')
        self.assertEqual(it.findtext('description'), 'source text')
        self.assertEqual(it.find('enclosure').get('url'), 'https://s/i.jpg')
        self.assertEqual(calls, [])  # image and description present: no fetch needed

    def test_cache_prevents_second_fetch_and_budget_caps(self):
        _, _, calls, cache = self.run_enrich(feed(item()))
        self.assertEqual(len(calls), 1)
        _, _, calls2, _ = self.run_enrich(feed(item()), cache)
        self.assertEqual(calls2, [])
        _, _, calls3, _ = self.run_enrich(feed(item()), {}, budget=0)
        self.assertEqual(calls3, [])

    def test_failed_fetch_is_cached_as_nothing_and_not_retried_at_once(self):
        cache = {}
        out, n = enrich_batch(feed(item()), lambda u: None, cache, [5], NOW)
        self.assertEqual(n, 0)
        self.assertEqual(cache['https://x.co.il/1']['meta'], {})
        calls = []
        enrich_batch(feed(item()), lambda u: calls.append(u), cache, [5], NOW)
        self.assertEqual(calls, [])

    def test_prune(self):
        cache = {'a': {}, 'b': {}}
        prune_cache(cache, {'a'})
        self.assertEqual(list(cache), ['a'])


class MediaGuidTest(unittest.TestCase):
    def test_thumbnail_and_guid_added_only_when_missing(self):
        xml = feed('<item><title>a</title><link>https://x.co.il/a?utm_source=t&amp;id=3#top</link>'
                   '<enclosure url="https://c/i.jpg" type="image/jpeg" length="0"/></item>'
                   '<item><title>b</title><link>https://x.co.il/b</link><guid>keep-me</guid></item>')
        out, n = add_media_and_guid(xml)
        a, b = ET.fromstring(out).findall('./channel/item')
        self.assertEqual(a.find('{%s}thumbnail' % MEDIA_NS).get('url'), 'https://c/i.jpg')
        self.assertEqual(a.findtext('guid'), 'https://x.co.il/a?id=3')
        self.assertEqual(b.findtext('guid'), 'keep-me')
        self.assertIsNone(b.find('{%s}thumbnail' % MEDIA_NS))
        again, n2 = add_media_and_guid(out)
        self.assertEqual(n2, 0)

    def test_stable_guid(self):
        self.assertEqual(stable_guid('https://x/y?fbclid=1&a=2#f'), 'https://x/y?a=2')


if __name__ == '__main__':
    unittest.main()
