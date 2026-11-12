#!/usr/bin/env python3
"""Add a content hash (?v=...) to the asset links in index.html.

Browsers keep files from this site for ten minutes. With the hash in the link, a changed
image, stylesheet or CV is fetched again at once. Run from the repository root after
changing any file under assets/ or the CV:  python3 tools/stamp_assets.py
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


new_html, count = pattern.subn(stamp, html)
page.write_text(new_html, encoding="utf-8")
print(f"stamped {count} links")
