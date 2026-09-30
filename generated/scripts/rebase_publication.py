#!/usr/bin/env python3
"""Change only RSS atom:self links while retaining article IDs and dates."""
from pathlib import Path
import re

OLD = b'https://yohaybn.github.io/israeli-no-rss-feeds/feeds/'
NEW = b'https://yohaybn.github.io/israeli-rss-feeds/feeds/'


def rebase(data):
    def link(match):
        tag = match.group(0)
        if re.search(rb'\brel\s*=\s*[\"\']self[\"\']', tag):
            return tag.replace(OLD, NEW)
        return tag
    return re.sub(rb'<(?:[A-Za-z_][\w.-]*:)?link\b[^>]*>', link, data)


if __name__ == '__main__':
    import sys
    for path in Path(sys.argv[1]).glob('*.xml'):
        path.write_bytes(rebase(path.read_bytes()))
