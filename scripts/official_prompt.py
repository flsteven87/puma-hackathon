"""Fetch the live hackathon page and print one issue's prompt verbatim with its retrieval record.

Usage: python3 scripts/official_prompt.py ISSUE_NUMBER [--rules]
Prints the retrieval time (Asia/Taipei), byte count and SHA-256 of the page, then the issue text
and its listed data links. --rules also prints the rules section, which carries deadlines and
data-use terms that change over time. Nothing is saved; copy what the topic document needs.
"""
import datetime
import hashlib
import re
import sys
import urllib.request
from html.parser import HTMLParser

URL = "https://puma.taipei/hackathon"


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style"):
            self.skip += 1
        anchor = a.get("id") or ""
        if anchor.startswith("issue-") or anchor == "rules":
            self.out.append(f"\n=== {anchor} ===\n")
        if tag == "a" and a.get("href"):
            self.out.append(f" [{a['href']}] ")
        if tag in ("p", "li", "h2", "h3", "h4", "div", "br"):
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip and data.strip():
            self.out.append(data.strip())


def section(text, name, nxt):
    m = re.search(rf"=== {name} ===\n(.*?)(?:=== {nxt} ===|\Z)", text, re.S)
    return m.group(1).strip() if m else f"(section {name} not found)"


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    n = int(sys.argv[1])
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(req, timeout=30).read()
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
    parser = Text()
    parser.feed(raw.decode("utf-8"))
    text = re.sub(r"\n\s*\n+", "\n", "".join(parser.out))
    print(f"Retrieved {now:%Y-%m-%d %H:%M} Asia/Taipei; {len(raw)} bytes; SHA-256 {hashlib.sha256(raw).hexdigest()}")
    print(f"\n--- issue-{n} ---\n" + section(text, f"issue-{n}", r"(?:issue-\d|rules)"))
    if "--rules" in sys.argv:
        print("\n--- rules ---\n" + section(text, "rules", r"issue-\d")[:4000])


if __name__ == "__main__":
    main()
