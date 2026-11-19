#!/usr/bin/env python3
"""Add a content hash (?v=...) to the asset links in index.html.

Browsers keep files from this site for ten minutes. With the hash in the link, a changed
image, stylesheet or CV is fetched again at once. Run from the repository root after
changing any file under assets/ or the CV:  python3 tools/stamp_assets.py
The link preview image (og:image) gets the same hash, so sites that cache previews fetch a
changed card. The card is rendered from tools/og-card.html (headless Chrome, 1200 x 630).
"""
import hashlib
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
page = root / "index.html"
html = page.read_text(encoding="utf-8")
pattern = re.compile(r'(?P<attr>src|href)="(?P<path>(?:assets/(?:img/[^"?#]+|style\.css)|Junsung_Park_CV\.pdf|favicon\.svg))(?:\?v=[0-9a-f]+)?"')


def stamp(match):
    path = match.group("path")
    digest = hashlib.sha256((root / path).read_bytes()).hexdigest()[:8]
    return f'{match.group("attr")}="{path}?v={digest}"'


# The link preview image is referenced by its full address in the og:image tag.
og_pattern = re.compile(r'content="https://parkquasar\.github\.io/(?P<path>assets/img/[^"?#]+)(?:\?v=[0-9a-f]+)?"')


def stamp_og(match):
    path = match.group("path")
    digest = hashlib.sha256((root / path).read_bytes()).hexdigest()[:8]
    return f'content="https://parkquasar.github.io/{path}?v={digest}"'


new_html, count = pattern.subn(stamp, html)
new_html, og_count = og_pattern.subn(stamp_og, new_html)
count += og_count
page.write_text(new_html, encoding="utf-8")
print(f"stamped {count} links")
