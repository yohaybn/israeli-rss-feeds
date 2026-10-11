import os, sys, unittest, xml.etree.ElementTree as ET
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from football_feed import (detect_teams, league_for, is_match_highlight, listings_to_rss, load_teams, CATEGORIES)
from feedlib import validate_feed_bytes

TEAMS = load_teams()
SITE = {'name': 'תקצירי כדורגל (ONE)', 'url': 'https://www.one.co.il/vod', 'lang': 'he'}


def item(i, title, duration='00:02:10', date='2026-10-10T17:05:00'):
    return {'ID': i, 'Title': {'Main': title}, 'Duration': duration, 'Date': date,
            'URL': {'PC': 'https://www.one.co.il/VOD/Play/%d/%s' % (i, 'slug')},
            'MediaFile': {'HD': 'https://example.invalid/secret.mp4'}}


def listing(*items):
    return {'Data': {'Videos': {'Items': list(items)}}}


class FootballFeedTest(unittest.TestCase):
    def test_team_index_is_sane(self):
        self.assertGreater(len(TEAMS), 90)
        self.assertEqual(len(TEAMS), len({t['id'] for t in TEAMS}))
        self.assertTrue(all(t['aliases'] for t in TEAMS))

    def test_two_teams_longest_alias_and_prefix(self):
        self.assertEqual([t['id'] for t in detect_teams('מכבי חיפה ניצחה את מכבי ת"א', TEAMS)], ['mha', 'mta'])
        self.assertEqual([t['id'] for t in detect_teams('הכוכב עובר לברצלונה', TEAMS)], ['bar'])
        self.assertEqual(detect_teams('עובדי המטרו יהרסו לכולם', TEAMS), [])

    def test_league_from_category_competition_or_teams(self):
        self.assertEqual(league_for('הליגה הספרדית', 'כל כותרת', TEAMS), 'הליגה הספרדית')
        self.assertEqual(league_for('כדורגל', 'ליברפול גברה 1:2 על אתלטיקו', TEAMS), 'מפעלים אירופיים')
        self.assertEqual(league_for('כדורגל', 'תקציר ליגת האלופות: ליברפול', TEAMS), 'ליגת האלופות')
        self.assertEqual(league_for('כדורגל', 'חדשות כלליות', TEAMS), 'כדורגל')

    def test_match_only_heuristic(self):
        self.assertTrue(is_match_highlight('אתלטיקו מנצחת 1:2 את ריאל', '00:05:29', TEAMS))
        self.assertFalse(is_match_highlight('צפו: שערי בית"ר 1:0', '00:00:52', TEAMS))
        self.assertFalse(is_match_highlight('ראיון עם מאמן מכבי חיפה 2:1', '00:03:00', TEAMS))

    def test_feed_is_title_and_link_only_valid_rss(self):
        data = listing(item(1, 'ברצלונה מנצחת 0:3 את חטאפה'), item(2, 'ראיון מיוחד 1:0'), item(3, 'קצר 2:0', '00:00:40'))
        rss, n = listings_to_rss([('הליגה הספרדית', data)], SITE, TEAMS, 'https://x.example/f.xml')
        self.assertEqual(n, 1)
        self.assertEqual(validate_feed_bytes(rss), [])
        self.assertNotIn(b'secret.mp4', rss)
        self.assertNotIn(b'<enclosure', rss)
        self.assertNotIn(b'<description>\n', rss.split(b'<item>')[1])
        it = ET.fromstring(rss).find('channel/item')
        self.assertEqual(it.findtext('guid'), 'one:1')
        self.assertEqual(it.find('guid').get('isPermaLink'), 'false')
        self.assertEqual(it.findtext('category'), 'הליגה הספרדית')
        self.assertTrue(it.findtext('link').startswith('https://www.one.co.il/VOD/Play/1/'))
        # ONE gives Israel local time; 17:05 +03:00 is 14:05 GMT.
        self.assertEqual(it.findtext('pubDate'), 'Sat, 10 Oct 2026 14:05:00 GMT')

    def test_dedupes_across_categories_and_never_includes_basketball(self):
        a = listing(item(5, 'מכבי חיפה ניצחה 1:0'))
        rss, n = listings_to_rss([('כדורגל', a), ('הליגה הספרדית', a)], SITE, TEAMS)
        self.assertEqual(n, 1)
        self.assertNotIn(19, [c for c, _ in CATEGORIES])

    def test_no_usable_items_raises(self):
        with self.assertRaises(ValueError):
            listings_to_rss([('כדורגל', listing(item(9, 'ראיון 1:0')))], SITE, TEAMS)


if __name__ == '__main__':
    unittest.main()
