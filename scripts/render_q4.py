"""Render Q4 vocabulary doc to PDF with clickable internal links.

Target: essays/mats_chang/q4/Q4_submarine_vocabulary.md
Citation style: numbered `[N]` inline markers + a `## References` block
containing `[N] entry` lines.

Pandoc doesn't natively cross-link the `[N]` inline style. So we
preprocess the markdown into pandoc's own footnote syntax:

    inline           `[N]`           →  `[^N]`
    reference-list   `[N] entry`     →  `[^N]: entry`

That syntax yields a clickable superscript at each callsite and a
back-arrow on each footnote definition in the rendered HTML/PDF.
Numbers may be renumbered by pandoc in first-appearance order — this
is fine when the source doc already cites in numerical order (Q4
does), and doesn't affect linking correctness either way.

Pipeline: markdown → preprocess citations → pandoc HTML5 → weasyprint PDF.

Run:
    uv run --script scripts/render_q4.py

Output: essays/mats_chang/q4/rendered/Q4_submarine_vocabulary.pdf
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
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INPUT = REPO_ROOT / "essays/mats_chang/q4/Q4_submarine_vocabulary.md"
OUTPUT_DIR = REPO_ROOT / "essays/mats_chang/q4/rendered"
DISPLAY_TITLE = "On Submarine Vocabulary"
AUTHOR = "Daniel Parshall, Ph.D."
AFFILIATION = "Canary Institute"


def frontmatter() -> str:
    """YAML metadata block: title + author lines rendered by pandoc."""
    return (
        "---\n"
        f'title: "{DISPLAY_TITLE}"\n'
        f'author: ["{AUTHOR}", "{AFFILIATION}"]\n'
        "---\n\n"
    )

# Matches the run of leading H1 headings and blank lines at the top of the doc.
# Pandoc's title block replaces them, so the rendered PDF doesn't show a
# filename-shaped or lowercase in-body heading.
LEADING_H1_RE = re.compile(r"\A(?:\s*\n|#\s+[^\n]*\n)+")


def strip_leading_h1(text: str) -> str:
    return LEADING_H1_RE.sub("", text, count=1)

# Matches a References-section heading (##/# References or Reference list),
# capturing case-insensitively so we tolerate small variations.
REFS_HEADING_RE = re.compile(
    r"^(?P<hashes>#{1,6})\s+(?P<title>References?|Reference\s+list)\s*$",
    re.IGNORECASE | re.MULTILINE,
)

# Matches a numbered reference entry like `[3] Author, ...`
# at start-of-line, capturing the number and the rest.
REF_ENTRY_RE = re.compile(r"^\[(\d+)\]\s+(.+)$", re.MULTILINE)

# Matches an inline citation `[N]` — NOT preceded by `^` (already a footnote
# marker) and NOT immediately followed by `(` (that's a markdown link).
INLINE_CITE_RE = re.compile(r"(?<!\^)\[(\d+)\](?!\()")

STYLE = """
@page {
  size: Letter;
  margin: 0.9in 1in 1in 1in;
  @bottom-center { content: counter(page); font-family: Georgia, serif; font-size: 9pt; color: #666; }
}
html { font-size: 11pt; }
body { font-family: Georgia, "Times New Roman", serif; line-height: 1.45; color: #222; }
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
.footnotes { border-top: 1px solid #ccc; margin-top: 2em; padding-top: 0.6em; font-size: 9.5pt; }
.footnotes ol > li { margin-bottom: 0.35em; }
"""


def split_at_references(text: str) -> tuple[str, str, str] | None:
    """Split text into (before, refs_body, after) around the References heading.

    Returns None if no References heading is found. `refs_body` includes
    everything from the heading line to end-of-file (or to the next same-or-
    higher heading, whichever comes first).
    """
    m = REFS_HEADING_RE.search(text)
    if not m:
        return None
    heading_start = m.start()
    heading_level = len(m.group("hashes"))
    # Find the next heading at same or higher level, if any.
    after_heading = m.end()
    next_boundary = len(text)
    for candidate in re.finditer(r"^(#{1,6})\s", text[after_heading:], re.MULTILINE):
        if len(candidate.group(1)) <= heading_level:
            next_boundary = after_heading + candidate.start()
            break
    return text[:heading_start], text[heading_start:next_boundary], text[next_boundary:]


def convert_refs_block_to_footnotes(refs_block: str) -> str:
    """Rewrite `[N] entry` lines within the refs block into `[^N]: entry`.

    The heading itself is stripped — pandoc will regenerate a footnote
    section automatically at the bottom of the rendered document. That
    also puts the References naturally at the doc's true end, even if
    the original had trailing content after the References list.
    """
    body_without_heading = REFS_HEADING_RE.sub("", refs_block, count=1)
    return REF_ENTRY_RE.sub(r"[^\1]: \2", body_without_heading)


def convert_inline_cites(body: str) -> str:
    """Rewrite `[N]` inline citations into `[^N]` footnote references,
    skipping fenced code blocks so we don't rewrite code snippets."""
    lines = body.split("\n")
    in_fence = False
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        lines[i] = INLINE_CITE_RE.sub(r"[^\1]", line)
    return "\n".join(lines)


def preprocess(markdown: str) -> str:
    """Convert numbered-reference style to pandoc footnote syntax.

    If no `## References` block exists, return unchanged."""
    split = split_at_references(markdown)
    if split is None:
        return markdown
    before, refs_block, after = split
    body_converted = convert_inline_cites(before + after)
    refs_converted = convert_refs_block_to_footnotes(refs_block)
    return body_converted.rstrip() + "\n\n" + refs_converted.strip() + "\n"


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
    processed = frontmatter() + preprocess(source)

    with tempfile.TemporaryDirectory() as tmpdir:
        md_path = Path(tmpdir) / "preprocessed.md"
        html_path = Path(tmpdir) / "doc.html"
        css_path = Path(tmpdir) / "style.css"
        md_path.write_text(processed)
        css_path.write_text(STYLE)

        run(
            [
                "pandoc",
                str(md_path),
                "-f", "markdown+smart+footnotes+auto_identifiers",
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
    print(f"Wrote {output_pdf.relative_to(REPO_ROOT)} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
