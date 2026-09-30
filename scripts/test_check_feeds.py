#!/usr/bin/env python3
"""Offline tests for date parsing in check_feeds.parse_feed.

Run: python -m unittest discover -s scripts -p 'test_*.py'
"""
import os, sys, unittest
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_feeds  # noqa: E402
from check_feeds import parse_feed, is_stale  # noqa: E402

NOW = check_feeds.NOW

def rss(*dates, tag='pubDate', extra_ns=''):
    items = ''.join(f'<item><title>t</title><{tag}>{d}</{tag}></item>' for d in dates)
    return f'<?xml version="1.0"?><rss version="2.0"{extra_ns}><channel><title>x</title>{items}</channel></rss>'.encode()

def atom(*dates, tag='updated'):
    ents = ''.join(f'<entry><title>t</title><{tag}>{d}</{tag}></entry>' for d in dates)
    return f'<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom"><title>x</title>{ents}</feed>'.encode()

class ParseFeedDates(unittest.TestCase):
    def test_rss_pubdate_is_read(self):
        # Regression: `it.find('pubDate') or ...` treated the childless element as False.
        old = datetime(2008, 5, 1, 12, 0, tzinfo=timezone.utc)
        items, newest = parse_feed(rss(format_datetime(old)))
        self.assertEqual(items, 1)
        self.assertEqual(newest, old)
        self.assertTrue(is_stale(newest))

    def test_rss_fresh_feed_is_not_stale(self):
        recent = NOW - timedelta(days=2)
        items, newest = parse_feed(rss(format_datetime(recent), format_datetime(recent - timedelta(days=30))))
        self.assertEqual(items, 2)
        self.assertFalse(is_stale(newest))

    def test_dc_date_fallback(self):
        ns = ' xmlns:dc="http://purl.org/dc/elements/1.1/"'
        items, newest = parse_feed(rss('2010-01-02T03:04:05Z', tag='dc:date', extra_ns=ns))
        self.assertEqual(newest, datetime(2010, 1, 2, 3, 4, 5, tzinfo=timezone.utc))

    def test_naive_date_does_not_crash(self):
        # "-0000" parses to a naive datetime; mixing it with aware dates used to raise.
        items, newest = parse_feed(rss('Mon, 01 Jan 2024 10:00:00 -0000', 'Tue, 02 Jan 2024 10:00:00 +0200'))
        self.assertIsNotNone(newest.tzinfo)
        self.assertTrue(is_stale(newest))

    def test_atom_updated(self):
        items, newest = parse_feed(atom('2012-06-01T00:00:00Z'))
        self.assertEqual(newest, datetime(2012, 6, 1, tzinfo=timezone.utc))
        self.assertTrue(is_stale(newest))

    def test_atom_published_fallback(self):
        items, newest = parse_feed(atom('2012-06-01T00:00:00Z', tag='published'))
        self.assertEqual(newest, datetime(2012, 6, 1, tzinfo=timezone.utc))

    def test_undated_feed_is_not_stale(self):
        items, newest = parse_feed(b'<rss><channel><item><title>t</title></item></channel></rss>')
        self.assertEqual(items, 1)
        self.assertIsNone(newest)
        self.assertFalse(is_stale(newest))

if __name__ == '__main__':
    unittest.main()

class HealthReport(unittest.TestCase):
    def test_report_updates_readme_and_lists_valid_feeds(self):
        import tempfile,json
        from unittest.mock import patch
        old=os.getcwd()
        with tempfile.TemporaryDirectory() as path:
            try:
                os.chdir(path)
                with open('feeds.json','w') as f:json.dump({'categories':[{'name_he':'Test','feeds':[{'title':'Example','url':'https://example.test/feed','site':'Example'}]}]},f)
                with open('README.md','w') as f:f.write('Before\n<!-- health:start -->old<!-- health:end -->\nAfter')
                feed={'title':'Example','url':'https://example.test/feed','site':'Example'}
                with patch('check_feeds.check',return_value=(feed,'ok','valid XML; no publication dates')), self.assertRaises(SystemExit) as exit:
                    check_feeds.main()
                self.assertEqual(exit.exception.code,0)
                with open('README.md') as f:text=f.read()
                self.assertIn('Before',text);self.assertIn('After',text);self.assertIn('XML תקין',text);self.assertIn('1 ללא תאריכי',text)
                with open('FEEDS-STATUS.md') as f:self.assertIn('Valid feeds',f.read())
            finally:os.chdir(old)
