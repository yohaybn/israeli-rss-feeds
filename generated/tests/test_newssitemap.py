import os, sys, unittest, xml.etree.ElementTree as ET
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from newssitemap_feed import sitemap_items, sitemap_locs, sitemaps_to_rss
from feedlib import validate_feed_bytes
SITE = {'name': 'Kikar', 'url': 'https://www.kikar.co.il/', 'lang': 'he'}
HEAD = ('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:news="http://www.google.com/schemas/sitemap-news/0.9" '
        'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">')
def url(loc, title, date, img=''):
    image = '<image:image><image:loc>%s</image:loc></image:image>' % img if img else ''
    return ('<url><loc>%s</loc><news:news><news:publication><news:name>K</news:name></news:publication>'
            '<news:publication_date>%s</news:publication_date><news:title>%s</news:title></news:news>%s</url>' % (loc, date, title, image))
SM = (HEAD + url('https://www.kikar.co.il/a/1', 'old &amp; first', '2026-10-01T10:00:00.000Z') +
      url('https://www.kikar.co.il/a/2', 'newer', '2026-10-05T04:00:00.000Z', 'https://i.kikar.co.il/x.jpeg') +
      url('https://evil.example/a/3', 'foreign', '2026-10-05T05:00:00.000Z') +
      url('http://www.kikar.co.il/a/4', 'not https', '2026-10-05T05:00:00.000Z') +
      url('https://www.kikar.co.il/a/5', '', '2026-10-05T05:00:00.000Z') + '</urlset>').encode()
class NewsSitemapTest(unittest.TestCase):
    def test_items_filtered_to_publisher_https_with_title(self):
        items = sitemap_items(SM, 'www.kikar.co.il')
        self.assertEqual([i['url'] for i in items], ['https://www.kikar.co.il/a/1', 'https://www.kikar.co.il/a/2'])
        self.assertEqual(items[0]['title'], 'old & first')
        self.assertEqual(items[1]['image'], 'https://i.kikar.co.il/x.jpeg')
    def test_rss_newest_first_valid_no_body(self):
        rss, n = sitemaps_to_rss(sitemap_items(SM, 'www.kikar.co.il') * 2, SITE)
        self.assertEqual(n, 2); self.assertEqual(validate_feed_bytes(rss), [])
        titles = [i.findtext('title') for i in ET.fromstring(rss).findall('channel/item')]
        self.assertEqual(titles, ['newer', 'old & first'])
        self.assertIsNone(ET.fromstring(rss).find('channel/item/description'))
    def test_caps_at_25_and_empty_raises(self):
        many = [{'id': 'https://k/%d' % i, 'url': 'https://k/%d' % i, 'title': 't%d' % i, 'date_published': '2026-10-05T04:%02d:00Z' % i} for i in range(40)]
        self.assertEqual(sitemaps_to_rss(many, SITE)[1], 25)
        with self.assertRaises(ValueError): sitemaps_to_rss([], SITE)
    def test_index_locs(self):
        idx = b'<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><sitemap><loc>https://a/1</loc></sitemap><sitemap><loc>https://a/2</loc></sitemap></sitemapindex>'
        self.assertEqual(sitemap_locs(idx), ['https://a/1', 'https://a/2'])
if __name__ == '__main__': unittest.main()
