#!/usr/bin/env python3
"""Verify red-font coverage in the clean and marked manuscripts.

Usage:
    python3 check_red.py is26.pdf is26_marked.pdf

Detection method (must use the explicit list-handling branch):
    page.get_contents() may return either a ContentStream or a list of them.
    Calling .get_data() directly on a list silently yields nothing, which makes
    every page look "unmarked". Always join the streams first.
"""

from pypdf import PdfReader
import re
import sys

RED = re.compile(rb"1\s+0\s+0\s+rg")


def page_content_bytes(page):
    """Return the raw content stream bytes of a page, handling both shapes."""
    contents = page.get_contents()
    if contents is None:
        return b""
    if isinstance(contents, list):
        data = b"".join(c.get_data() for c in contents)
    else:
        data = contents.get_data()
    return data or b""


def runs(pages):
    """Collapse a sorted page list into compact ranges."""
    if not pages:
        return "NONE"
    out, start, prev = [], pages[0], pages[0]
    for pg in pages[1:]:
        if pg == prev + 1:
            prev = pg
            continue
        out.append((start, prev))
        start = prev = pg
    out.append((start, prev))
    return ", ".join(str(a) if a == b else f"{a}-{b}" for a, b in out)


def scan(fname):
    reader = PdfReader(fname)
    red_pages, all_colors, per_page = [], {}, {}
    for i, page in enumerate(reader.pages, 1):
        raw = page_content_bytes(page).decode("latin-1", errors="ignore")
        if not raw:
            continue
        for m in re.finditer(r"([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+rg\b", raw):
            all_colors.setdefault(m.group(0).strip(), []).append(i)
        n = len(RED.findall(raw.encode("latin-1", errors="ignore")))
        per_page[i] = n
        if n:
            red_pages.append(i)

    total_marks = sum(per_page.values())
    print(f"=== {fname} ===")
    print(f"  pages                : {len(reader.pages)}")
    print(f"  pages containing red : {len(red_pages)}")
    print(f"  total red operators  : {total_marks}")
    print(f"  red page runs        : {runs(red_pages)}")
    print("  fill colours in use  :")
    for c, pages in sorted(all_colors.items(), key=lambda x: -len(x[1]))[:6]:
        print(f"    {c!r}: {len(pages)} pages")
    print()
    return red_pages


if __name__ == "__main__":
    for f in sys.argv[1:] or ["is26_marked.pdf"]:
        scan(f)
