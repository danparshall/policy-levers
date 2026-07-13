"""Render Q1 essay to PDF with clickable internal citation links.

Target: essays/mats_chang/q1/Q1_MAD_about_AI.md
Citation style: author-year narrative + a `## References` list.

Because there are no numeric markers in the source, we inject links at
render time from a bespoke citation table. For each reference we know
about, the table lists:

  - anchor_id      — the id we'll place on the reference-list entry
                     (e.g. `ref-schelling-1960`)
  - ref_key        — substring used to find that entry in the `## References`
                     section (must uniquely identify one line)
  - body_patterns  — regex(es) matching the citation as it actually
                     appears in the body prose (e.g. `Schelling (1960)`)

At render time:
  1. Each body pattern gets replaced with `[matched text](#anchor_id)`,
     so pandoc emits an <a href="#anchor_id"> link.
  2. Each matched reference-list line gets `<a id="anchor_id"></a>`
     prefixed, giving the link somewhere to land.

The source .md is not modified — everything happens on an in-memory copy.

Pipeline: markdown (with injected links + anchors) → pandoc HTML5
(standalone, embedded resources) → weasyprint PDF (anchor links carried
through into the PDF as internal GoTo actions).

Run:
    uv run --script scripts/render_q1.py

Output: essays/mats_chang/q1/rendered/Q1_MAD_about_AI.pdf
"""
# /// script
# requires-python = ">=3.11"
# dependencies = ["weasyprint>=62"]
# ///

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INPUT = REPO_ROOT / "essays/mats_chang/q1/Q1_MAD_about_AI.md"
OUTPUT_DIR = REPO_ROOT / "essays/mats_chang/q1/rendered"
DISPLAY_TITLE = "MAD About AI"
AUTHOR = "Daniel Parshall, Ph.D."
AFFILIATION = "Canary Institute"


def frontmatter() -> str:
    """YAML metadata block pandoc reads to populate its title block.

    Multiple author entries render as separate `<p class="author">` lines,
    which is how we express "author + affiliation" without pandoc's more
    involved structured-author schema.
    """
    return (
        "---\n"
        f'title: "{DISPLAY_TITLE}"\n'
        f'author: ["{AUTHOR}", "{AFFILIATION}"]\n'
        "---\n\n"
    )

# ---------------------------------------------------------------------------
# Citation table
# ---------------------------------------------------------------------------
# One entry per reference in Q1_MAD_about_AI.md. `ref_key` must be a substring
# that uniquely identifies that reference's line in the `## References` block.
# `body_patterns` are regexes matched against the doc body (everything before
# the References heading); each match becomes a link.
#
# Patterns use `\s+` for whitespace flexibility. Year can appear parenthesized
# `(2025)` or bare `2025`; we handle both by making the parentheses optional.
# Where two forms would be different links (unlikely here), split into two
# entries. Where the same anchor should catch multiple citation shapes for
# the same reference, list multiple patterns for it.
#
# Special cases:
#   - APS has two references (2004 and 2025). We disambiguate the ref_key
#     with distinct substrings ("APS / Barton" vs "APS Panel").
#   - CBO's reference-list entry spells out "Congressional Budget Office";
#     body cites it as "CBO (2026)".
#   - Schelling's body mention ("Schelling outlined this in 1960") is
#     narrative, not standard citation form — deliberately not linked to
#     avoid over-eager matching of every "Schelling" occurrence.


@dataclass
class Citation:
    anchor_id: str
    ref_key: str
    body_patterns: list[str] = field(default_factory=list)


CITATIONS: list[Citation] = [
    Citation(
        anchor_id="ref-winter-levy-lalwani-2025",
        ref_key="Winter-Levy",
        body_patterns=[r"Winter-Levy\s+(?:and|&)\s+Lalwani\s*\(2025\)"],
    ),
    Citation(
        anchor_id="ref-lieber-press-2017",
        ref_key="Lieber, K. A.",
        body_patterns=[r"Lieber\s+(?:and|&)\s+Press\s*\(2017\)"],
    ),
    Citation(
        anchor_id="ref-keaney-cohen-1993",
        ref_key="Keaney",
        body_patterns=[r"Keaney\s+(?:and|&)\s+Cohen\s+1993"],
    ),
    Citation(
        anchor_id="ref-macdonald-2025",
        ref_key="MacDonald",
        body_patterns=[r"MacDonald\s*\(2025\)"],
    ),
    Citation(
        anchor_id="ref-parshall-2014",
        ref_key="Parshall",
        body_patterns=[r"Parshall\s+et\s+al\.?\s+2014"],
    ),
    Citation(
        anchor_id="ref-sudharsun-2022",
        ref_key="Sudharsun",
        body_patterns=[r"Sudharsun\s+et\s+al\.?\s*\(2022\)"],
    ),
    Citation(
        anchor_id="ref-acton-2018",
        ref_key="Acton",
        body_patterns=[r"Acton\s+2018"],
    ),
    Citation(
        anchor_id="ref-aps-barton-2004",
        ref_key="APS / Barton",
        body_patterns=[r"Barton\s+et\s+al\.?\s+2004"],
    ),
    Citation(
        anchor_id="ref-aps-2025",
        ref_key="APS Panel",
        # Match "APS 2025" but NOT "APS 2004" (that's the Barton entry).
        # Both `APS 2025` and `APS (2025)` are possible; the source has just `APS 2025`.
        body_patterns=[r"APS\s+2025\b"],
    ),
    Citation(
        anchor_id="ref-cbo-2026",
        ref_key="Congressional Budget Office",
        body_patterns=[r"CBO\s*\(2026\)"],
    ),
    Citation(
        anchor_id="ref-copeland-2000",
        ref_key="Copeland",
        body_patterns=[r"Copeland\s+2000"],
    ),
    Citation(
        anchor_id="ref-mckinney-harris-2021",
        ref_key="McKinney",
        body_patterns=[r"McKinney\s+(?:and|&)\s+Harris\s+2021"],
    ),
    Citation(
        anchor_id="ref-kavka-1978",
        ref_key="Kavka",
        body_patterns=[r"Kavka\s*\(1978\)"],
    ),
    Citation(
        anchor_id="ref-feaver-1992",
        ref_key="Feaver",
        # Doc uses possessive: "Feaver's (1992)". Match both possessive and plain.
        body_patterns=[r"Feaver(?:'s)?\s*\(1992\)"],
    ),
    Citation(
        anchor_id="ref-blair-2004",
        ref_key="Blair",
        body_patterns=[r"Blair\s+2004"],
    ),
    Citation(
        anchor_id="ref-schelling-1960",
        ref_key="Schelling, T. C.",
        # Narrative "Schelling outlined this in 1960" — we link only the year
        # phrase to avoid catching every unqualified "Schelling" later.
        body_patterns=[r"Schelling outlined this in 1960"],
    ),
]

# ---------------------------------------------------------------------------
# Styling
# ---------------------------------------------------------------------------
STYLE = """
@page {
  size: Letter;
  margin: 0.9in 1in 1in 1in;
  @bottom-center { content: counter(page); font-family: Georgia, serif; font-size: 9pt; color: #666; }
}
html { font-size: 11pt; }
body {
  font-family: Georgia, "Times New Roman", serif;
  line-height: 1.45;
  color: #222;
  max-width: none;
}
h1.title { font-size: 22pt; margin-bottom: 0.1em; }
p.author { margin: 0.1em 0; font-style: italic; color: #444; font-size: 11pt; }
p.author + p.author { margin-top: 0; }
h1 { font-size: 20pt; margin-top: 0; }
h2 { font-size: 14pt; margin-top: 1.4em; border-bottom: 1px solid #ccc; padding-bottom: 0.15em; }
h3 { font-size: 12pt; margin-top: 1.2em; }
p  { margin: 0.5em 0; text-align: justify; hyphens: auto; }
a  { color: #204a87; text-decoration: none; }
a:hover { text-decoration: underline; }
sup a { font-size: 0.75em; }
code { font-family: "Menlo", monospace; font-size: 0.92em; background: #f4f4f4; padding: 0.05em 0.25em; border-radius: 2px; }
blockquote { border-left: 3px solid #bbb; margin: 0.6em 0; padding: 0.1em 0.9em; color: #555; }
/* References block: keep entries tight since they're already long. */
h2#references + p, h2#references ~ p { margin: 0.25em 0; }
"""


# ---------------------------------------------------------------------------
# Preprocessing
# ---------------------------------------------------------------------------

REFS_HEADING_RE = re.compile(
    r"^(?P<hashes>#{1,6})\s+References?\s*$", re.MULTILINE | re.IGNORECASE
)

# Matches the run of leading H1 headings (and blank lines between them) at
# the very top of the doc. The source has a filename-shaped H1 (or two, for
# Q1); pandoc's title block replaces them at render time.
LEADING_H1_RE = re.compile(r"\A(?:\s*\n|#\s+[^\n]*\n)+")


def strip_leading_h1(text: str) -> str:
    """Drop the leading H1 headings so pandoc's title metadata takes over."""
    return LEADING_H1_RE.sub("", text, count=1)


def split_at_references(text: str) -> tuple[str, str, str]:
    """Split the doc into (body, refs_section, trailing).

    `refs_section` starts at the References heading and runs to end of doc
    (Q1_MAD has nothing after References; we still handle it generally).
    Raises ValueError if no References heading is found.
    """
    m = REFS_HEADING_RE.search(text)
    if m is None:
        raise ValueError("no `## References` heading found in source")
    return text[: m.start()], text[m.start() :], ""


def link_body_citations(body: str, citations: list[Citation]) -> tuple[str, dict[str, int]]:
    """Wrap each body citation in a markdown link to its anchor.

    Returns (rewritten body, counts-per-anchor). Counts let us verify that
    every citation table entry actually matched something in the source —
    a zero count means the pattern doesn't match reality and needs fixing.
    """
    counts: dict[str, int] = {c.anchor_id: 0 for c in citations}
    result = body
    for cite in citations:
        for pattern in cite.body_patterns:
            regex = re.compile(pattern)

            def _replace(match: re.Match[str], anchor: str = cite.anchor_id) -> str:
                counts[anchor] += 1
                return f"[{match.group(0)}](#{anchor})"

            result = regex.sub(_replace, result)
    return result, counts


def anchor_references(refs_section: str, citations: list[Citation]) -> tuple[str, list[str]]:
    """Prefix each reference-list line matching a citation's `ref_key` with
    an inline `<a id="anchor_id"></a>` HTML anchor.

    Returns (rewritten section, list of citation ids whose ref_key didn't
    match any line — an integrity check for the table).
    """
    lines = refs_section.split("\n")
    unmatched: list[str] = []
    for cite in citations:
        matched_index: int | None = None
        for i, line in enumerate(lines):
            if cite.ref_key in line:
                matched_index = i
                break
        if matched_index is None:
            unmatched.append(cite.anchor_id)
            continue
        lines[matched_index] = f'<a id="{cite.anchor_id}"></a>' + lines[matched_index]
    return "\n".join(lines), unmatched


def preprocess(markdown_text: str) -> tuple[str, dict[str, int], list[str]]:
    """Apply body-link injection and reference anchoring.

    Returns (transformed markdown, body-match counts, refs unmatched)."""
    body, refs, trailing = split_at_references(markdown_text)
    body_linked, counts = link_body_citations(body, CITATIONS)
    refs_anchored, unmatched = anchor_references(refs, CITATIONS)
    return body_linked + refs_anchored + trailing, counts, unmatched


# ---------------------------------------------------------------------------
# Render
# ---------------------------------------------------------------------------

def run(cmd: list[str]) -> None:
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"COMMAND FAILED: {' '.join(cmd)}", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        sys.exit(result.returncode)


def main() -> None:
    if not INPUT.exists():
        print(f"Input not found: {INPUT}", file=sys.stderr)
        sys.exit(1)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_pdf = OUTPUT_DIR / (INPUT.stem + ".pdf")

    source = strip_leading_h1(INPUT.read_text())
    processed, body_counts, unmatched_refs = preprocess(source)
    processed = frontmatter() + processed

    # Loud, useful integrity report: any zero count means a table entry
    # doesn't match the source; any unmatched ref_key means we couldn't
    # find that reference's line to hang the anchor on.
    for anchor_id, count in body_counts.items():
        if count == 0:
            print(
                f"WARN: citation `{anchor_id}` — 0 body matches "
                "(pattern may not match the source anymore)",
                file=sys.stderr,
            )
    for anchor_id in unmatched_refs:
        print(
            f"WARN: citation `{anchor_id}` — ref_key not found in References list",
            file=sys.stderr,
        )
    total_links = sum(body_counts.values())

    with tempfile.TemporaryDirectory() as tmpdir:
        md_path = Path(tmpdir) / "linked.md"
        html_path = Path(tmpdir) / "doc.html"
        css_path = Path(tmpdir) / "style.css"
        md_path.write_text(processed)
        css_path.write_text(STYLE)

        run(
            [
                "pandoc",
                str(md_path),
                "-f", "markdown+smart+footnotes+auto_identifiers+raw_html",
                "-t", "html5",
                "--standalone",
                "--section-divs",
                "--css", str(css_path),
                "--embed-resources",
                "-o", str(html_path),
            ]
        )

        from weasyprint import HTML  # type: ignore[import-not-found]
        HTML(filename=str(html_path)).write_pdf(str(output_pdf))

    size_kb = output_pdf.stat().st_size / 1024
    print(
        f"Wrote {output_pdf.relative_to(REPO_ROOT)} ({size_kb:.1f} KB, "
        f"{total_links} citation links)"
    )


if __name__ == "__main__":
    main()
