#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pypdf>=4.0"]
# ///
"""Extract the main effort-post text from FireDistinguishers's r/neoliberal
Congress-series PDFs, stripping Reddit chrome and truncating before comments.

Emits one .md per PDF into reddit_advice/text/. Each output starts with a
lightweight YAML-ish header capturing source URL and post title, then the
prose body of the effortpost only (no replies).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from pypdf import PdfReader

SRC = Path("/Users/dan/code/policy-levers/reddit_advice")
DST = SRC / "text"

# Deliberately kebab-case output names per project convention.
MAPPING: dict[str, str] = {
    "Congress 100_ House Leadership and What They're Leading _ r_neoliberal.pdf":
        "congress-100-house-leadership.md",
    "Congress 101_ House Rules, the House Floor, and the Parties _ r_neoliberal.pdf":
        "congress-101-house-rules.md",
    "Congress 102_ The Very Very Very Start of Understanding the Senate _ r_neoliberal.pdf":
        "congress-102-senate-intro.md",
    "Congress 103_ The Filibuster _ r_neoliberal.pdf":
        "congress-103-filibuster.md",
    "Congress 201_ An Introduction to Committees _ r_neoliberal.pdf":
        "congress-201-committees.md",
    "Congress 202_ Washington, D.C. - by Fire Distinguishers.pdf":
        "congress-202-washington-dc.md",
    "Congress 408_ Seminar - Senate Office Structure _ r_neoliberal.pdf":
        "congress-408-senate-office-structure.md",
    "Congress 409_ Seminar - Lobbying 1 _ r_neoliberal.pdf":
        "congress-409-lobbying-1.md",
    "Congress 509_ How to lobby with an internet connection and a $3 post card _ r_neoliberal.pdf":
        "congress-509-lobbying-with-postcard.md",
    "Congressional Procedure 104_ The Budget _ r_neoliberal.pdf":
        "congressional-procedure-104-budget.md",
}

# Lines that are pure Reddit UI chrome — drop when matched exactly (post-strip).
CHROME_EXACT = {
    "Skip to main content",
    "Find anything",
    "Ask",
    "Log In",
    "Find anything Ask Log In",
    "Find anything Find anything Ask Log In",
    "Effortpost",
    "FireDistinguishers",
    "FireDistinguishers OP",
    "OP",
}

# Substring hits mark chrome even when pypdf collapses whitespace and mashes
# the UI-widget words onto a single line (e.g. "AskFind anythingSkip to main content").
CHROME_SUBSTRINGS = [
    "Skip to main content",
]

# Lines that match these regexes are chrome — drop.
CHROME_PATTERNS = [
    re.compile(r"^\d+/\d+/\d+, \d+:\d+ ?(AM|PM)?"),   # date-time page header
    re.compile(r"^https?://"),                          # URL footer
    re.compile(r"^r/\w+\s*•\s*\d+\w+ ago"),            # subreddit + timestamp (space-agnostic)
    re.compile(r"^\d+/\d+$"),                           # page counter "1/9"
    re.compile(r"^Congress \d+.*: r/\w+$"),            # running page title
    re.compile(r"^Congressional Procedure \d+.*: r/\w+$"),
]

# Truncate at the first occurrence of any of these — everything after is
# comments / related posts / "top posts" clutter.
TRUNCATE_MARKERS = [
    "Join the conversation",             # Reddit
    "Sort by: Best",                      # Reddit (fallback)
    "Subscribe to Congress Confidential", # Substack CTA — cuts before the footer
    "Discussion about this post",         # Substack (fallback)
]


def extract_raw(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def clean(text: str) -> str:
    kept: list[str] = []
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped:
            kept.append("")
            continue
        if stripped in CHROME_EXACT:
            continue
        if any(sub in stripped for sub in CHROME_SUBSTRINGS):
            continue
        if any(p.match(stripped) for p in CHROME_PATTERNS):
            continue
        kept.append(line)
    body = "\n".join(kept)

    # Truncate at first comment-section marker.
    cut = len(body)
    for marker in TRUNCATE_MARKERS:
        idx = body.find(marker)
        if idx != -1 and idx < cut:
            cut = idx
    body = body[:cut]

    # Also trim a trailing "NN NN" upvote/comment counter line if present.
    body = re.sub(r"\n\s*\d+\s+\d+\s*$", "", body)

    # Collapse runs of blank lines.
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    return body


def title_from_pdf_name(name: str) -> str:
    # "Congress 100_ House Leadership and What They're Leading _ r_neoliberal.pdf"
    # -> "Congress 100: House Leadership and What They're Leading"
    stem = name.removesuffix(".pdf")
    # Strip the trailing " _ r_neoliberal"
    stem = re.sub(r"\s*_\s*r_neoliberal$", "", stem)
    # First underscore acts as the colon after the number.
    stem = stem.replace("_", ":", 1)
    return stem.strip()


def emit(pdf_path: Path, out_path: Path) -> tuple[int, int]:
    raw = extract_raw(pdf_path)
    cleaned = clean(raw)
    title = title_from_pdf_name(pdf_path.name)
    # Strip an initial line that just repeats the title (we're re-emitting it in the header).
    lines = cleaned.split("\n", 1)
    if lines and lines[0].strip() == title:
        cleaned = lines[1].lstrip("\n") if len(lines) > 1 else ""
    header = (
        f"# {title}\n\n"
        f"Source: r/neoliberal, u/FireDistinguishers (\"effortpost\" flair)\n"
        f"Original PDF: `{pdf_path.name}`\n\n"
        f"---\n\n"
    )
    out_path.write_text(header + cleaned + "\n", encoding="utf-8")
    return len(raw), len(cleaned)


def main() -> int:
    if not SRC.exists():
        print(f"missing source dir: {SRC}", file=sys.stderr)
        return 1
    DST.mkdir(exist_ok=True)

    missing: list[str] = []
    for pdf_name, out_name in MAPPING.items():
        pdf_path = SRC / pdf_name
        if not pdf_path.exists():
            missing.append(pdf_name)
            continue
        raw_len, clean_len = emit(pdf_path, DST / out_name)
        print(f"{out_name:60s}  raw={raw_len:>6}  kept={clean_len:>6}")

    if missing:
        print("\nMISSING PDFS:", file=sys.stderr)
        for m in missing:
            print(f"  {m}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
