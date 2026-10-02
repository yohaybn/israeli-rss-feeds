import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from rebase_publication import rebase, OLD, NEW

class RebaseTests(unittest.TestCase):
    def test_only_self_changes(self):
        data = (b'<rss><channel><atom:link href="' + OLD +
                b'tech-il.xml" rel="self"/><item><guid>' + OLD +
                b'example</guid><pubDate>Wed, 30 Sep 2026 10:00:00 GMT</pubDate>'
                b'</item></channel></rss>')
        result = rebase(data)
        self.assertIn(NEW + b'tech-il.xml', result)
        self.assertIn(b'<guid>' + OLD + b'example</guid>', result)
        self.assertIn(b'Wed, 30 Sep 2026 10:00:00 GMT', result)
        self.assertEqual(rebase(result), result)

    def test_nonself_link_stays(self):
        data = b'<atom:link rel="alternate" href="' + OLD + b'x.xml"/>'
        self.assertEqual(rebase(data), data)
