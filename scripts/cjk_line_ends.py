"""Keep the last few Chinese characters of each text block on one line in an HTML report.

Usage: python3 scripts/cjk_line_ends.py page.html [page.html ...]
Chrome's `text-wrap: pretty` does not prevent a Chinese paragraph from ending on a line of one or
two characters. This wraps the final characters of every block (p, li, td, dd, figcaption) whose
plain-text tail ends in Chinese in `<span class="nowrap">`, to reduce very short last lines. Endings inside existing inline elements are left unchanged;
this is a best-effort typography pass, not a guarantee for every block. It edits files in place and is idempotent; the page must define `.nowrap`.
"""
import re
import sys

KEEP = 4  # characters (excluding trailing punctuation) kept together at the end of a block
CJK = re.compile(r"[㐀-鿿豈-﫿]")
TAIL = re.compile(r"(?<=>)([^<>]+)(</(?:p|li|td|dd|figcaption)>)")


def glue(text):
    if text.endswith("</span>") or not CJK.search(text[-8:]):
        return None
    counted, i = 0, len(text)
    while i > 0 and counted < KEEP:
        ch = text[i - 1]
        if ch in "&; \n\t":
            break
        if CJK.match(ch) or ch.isalnum():
            counted += 1
        i -= 1
    if counted < KEEP or i == 0:
        return None
    return text[:i] + '<span class="nowrap">' + text[i:] + "</span>"


def main(paths):
    for path in paths:
        s = open(path, encoding="utf-8").read()
        n = 0

        def sub(m):
            nonlocal n
            g = glue(m.group(1))
            if g is None:
                return m.group(0)
            n += 1
            return g + m.group(2)

        s = TAIL.sub(sub, s)
        open(path, "w", encoding="utf-8").write(s)
        print(f"{path}: {n} block endings kept together")


if __name__ == "__main__":
    main(sys.argv[1:])
