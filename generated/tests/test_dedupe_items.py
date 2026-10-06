import os, sys, unittest, xml.etree.ElementTree as ET
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from feedlib import dedupe_items

def feed(items):
    body = ''.join('<item><title>%s</title><link>%s</link><guid>%s</guid><pubDate>%s</pubDate></item>' % i for i in items)
    return ('<?xml version="1.0"?><rss version="2.0"><channel><title>t</title><link>https://x</link><description>d</description>%s</channel></rss>' % body).encode()

class DedupeItemsTest(unittest.TestCase):
    def links(self, xml):
        return [i.findtext('link') for i in ET.fromstring(xml).findall('channel/item')]

    def test_www_and_bare_host_are_one_article_earliest_date_stays(self):
        xml = feed([('a', 'https://kan.org.il/p/1106412/', 'g1', 'Tue, 06 Oct 2026 09:09:27 GMT'),
                    ('a', 'https://www.kan.org.il/p/1106412/', 'g2', 'Tue, 06 Oct 2026 09:07:13 GMT'),
                    ('b', 'https://www.kan.org.il/p/2/', 'g3', 'Tue, 06 Oct 2026 08:00:00 GMT')])
        out, removed = dedupe_items(xml)
        self.assertEqual(removed, 1)
        self.assertEqual(self.links(out), ['https://www.kan.org.il/p/1106412/', 'https://www.kan.org.il/p/2/'])

    def test_trailing_slash_scheme_fragment_and_utm(self):
        xml = feed([('a', 'http://x.co.il/a', '1', 'Tue, 06 Oct 2026 09:00:00 GMT'),
                    ('a', 'https://x.co.il/a/?utm_source=z#top', '2', 'Tue, 06 Oct 2026 09:01:00 GMT')])
        out, removed = dedupe_items(xml)
        self.assertEqual(removed, 1)

    def test_different_query_ids_are_kept(self):
        xml = feed([('a', 'https://x.co.il/p?id=1', '1', 'Tue, 06 Oct 2026 09:00:00 GMT'),
                    ('b', 'https://x.co.il/p?id=2', '2', 'Tue, 06 Oct 2026 09:01:00 GMT')])
        out, removed = dedupe_items(xml)
        self.assertEqual(removed, 0)
        self.assertEqual(out, xml)

if __name__ == '__main__':
    unittest.main()
