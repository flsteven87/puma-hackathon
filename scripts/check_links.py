"""Check every relative link and anchor in the research documents.

Usage: python3 scripts/check_links.py [files...]
Without arguments it checks README, AGENTS, MEMORY and every Markdown/HTML file under docs/.
Anchors follow GitHub's heading slugs, including the -1, -2 suffixes for repeated headings.
Links into the public edition (PUBLIC) are checked against the local copy of the same file.
Exit status is 1 when any link or anchor is missing.
"""
import glob
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = "https://github.com/flsteven87/puma-hackathon/blob/main/"


def slug(text):
    a = text.strip().lower()
    a = re.sub(r"[^\w\- ]", "", a)
    return a.replace(" ", "-")


def anchors(path, cache={}):
    if path in cache:
        return cache[path]
    s = open(path, encoding="utf-8").read()
    if path.endswith(".html"):
        out = set(re.findall(r'id="([^"]+)"', s))
    else:
        seen, out, fence = defaultdict(int), set(), False
        for line in s.split("\n"):
            if line.startswith("```"):
                fence = not fence
                continue
            m = re.match(r"^(#{1,6}) (.+)$", line)
            if m and not fence:
                a = slug(m.group(2))
                n = seen[a]
                seen[a] += 1
                out.add(a if n == 0 else f"{a}-{n}")
    cache[path] = out
    return out


def default_files():
    files = [f for f in ("README.md", "AGENTS.md", "MEMORY.md") if os.path.exists(os.path.join(ROOT, f))]
    for pattern in ("docs/*.md", "docs/*.html", "docs/topics/*.md", "docs/topics/*.html"):
        files += sorted(os.path.relpath(p, ROOT) for p in glob.glob(os.path.join(ROOT, pattern)))
    return files


def main(files):
    bad = 0
    for f in files:
        path = os.path.join(ROOT, f)
        s = open(path, encoding="utf-8").read()
        pattern = r'href="([^"]+)"' if f.endswith(".html") else r"\]\(([^)\s]+)\)"
        for url in re.findall(pattern, s):
            public = url.startswith(PUBLIC)
            if re.match(r"^[a-z]+:", url) and not public:
                continue
            target, _, anchor = url.partition("#")
            if public:
                tpath = os.path.join(ROOT, target[len(PUBLIC):])
            else:
                tpath = os.path.normpath(os.path.join(os.path.dirname(path), target)) if target else path
            if not os.path.exists(tpath):
                print(f"missing file: {f} -> {url}")
                bad += 1
            elif anchor and tpath.endswith((".md", ".html")) and anchor not in anchors(tpath):
                print(f"missing anchor: {f} -> {url}")
                bad += 1
    print(f"checked {len(files)} files, {bad} problems")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or default_files()))
