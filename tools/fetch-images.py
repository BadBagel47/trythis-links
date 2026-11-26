#!/usr/bin/env python3
"""Fetch a picture for every link in links.json and store it under assets/images/ (F-004).

YouTube channels get the channel avatar (og:image). Other sites get their app icon
(apple-touch-icon, then the largest PNG icon, then og:image). Pictures are saved
locally so visitors never contact the linked sites just by opening the page.

Usage:  python3 tools/fetch-images.py            # only links without a picture
        python3 tools/fetch-images.py --force    # refetch all
Needs:  Pillow (pip install pillow). Not published (tools/ is excluded).
"""
import io
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
LINKS = ROOT / "links.json"
OUT = ROOT / "assets" / "images"
SIZE = 160  # px, square; shown at 52-60 px, so sharp on 2x screens
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.geturl(), r.read()


class Head(HTMLParser):
    def __init__(self):
        super().__init__()
        self.og = None
        self.icons = []  # (score, href)

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        if tag == "meta" and "og:image" in (a.get("property", ""), a.get("name", "")) and not self.og:
            self.og = a.get("content")
        if tag == "link":
            rel = a.get("rel", "").lower()
            href = a.get("href")
            if not href:
                return
            m = re.match(r"(\d+)x\d+", a.get("sizes", "")) or re.search(r"(\d+)x\d+", href)
            size = int(m.group(1)) if m else 0
            if "apple-touch-icon" in rel or "apple-icon" in href:
                self.icons.append((1000 + (size or 180), href))
            elif "icon" in rel and not href.endswith(".ico"):
                self.icons.append((size or 1, href))


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def pick_image(url):
    final, body = get(url)
    head = Head()
    head.feed(body.decode("utf-8", "replace"))
    host = urlparse(final).hostname or ""
    if host.endswith("youtube.com"):
        candidates = [head.og]
    else:
        candidates = [h for _, h in sorted(head.icons, reverse=True)] + [head.og]
    for c in candidates:
        if c:
            return urljoin(final, c)
    return None


def square(img):
    img = img.convert("RGBA")
    w, h = img.size
    s = min(w, h)
    img = img.crop(((w - s) // 2, (h - s) // 2, (w - s) // 2 + s, (h - s) // 2 + s))
    return img.resize((SIZE, SIZE), Image.LANCZOS)


def main():
    force = "--force" in sys.argv
    data = json.loads(LINKS.read_text(encoding="utf-8"))
    OUT.mkdir(parents=True, exist_ok=True)
    changed = False
    for link in data["links"]:
        if link.get("image") and not force:
            continue
        try:
            src = pick_image(link["url"])
            if not src:
                print(f"no picture found: {link['name']}")
                continue
            _, raw = get(src)
            img = square(Image.open(io.BytesIO(raw)))
            rel = f"assets/images/{slug(link['name'])}.webp"
            img.save(ROOT / rel, "WEBP", quality=86, method=6)
            link["image"] = rel
            changed = True
            print(f"ok: {link['name']} <- {src}")
        except Exception as e:  # keep going; the page falls back to initials
            print(f"failed: {link['name']}: {e}")
    if changed:
        LINKS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
