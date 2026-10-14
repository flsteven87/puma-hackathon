"""Render HTML reports at desktop and phone widths and save full-page screenshots.

Usage: uv run --with playwright python scripts/render_check.py OUT_DIR page.html [page.html ...]
Uses the installed Chrome (Playwright's bundled browsers are not installed here).
Fails when a page scrolls horizontally. Look at the saved screenshots before calling a page done.
"""
import os
import sys

from playwright.sync_api import sync_playwright

WIDTHS = (1200, 390)


def main(out_dir, pages):
    os.makedirs(out_dir, exist_ok=True)
    bad = 0
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        for page_path in pages:
            name = os.path.splitext(os.path.basename(page_path))[0]
            for width in WIDTHS:
                page = browser.new_page(viewport={"width": width, "height": 900})
                page.goto("file://" + os.path.abspath(page_path))
                page.wait_for_timeout(300)
                shot = os.path.join(out_dir, f"{name}-{width}.png")
                page.screenshot(path=shot, full_page=True)
                scroll = page.evaluate("document.documentElement.scrollWidth")
                status = "ok" if scroll <= width else "HORIZONTAL SCROLL"
                bad += status != "ok"
                print(f"{status}: {page_path} at {width}px (scrollWidth {scroll}) -> {shot}")
                page.close()
        browser.close()
    return 1 if bad else 0


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1], sys.argv[2:]))
