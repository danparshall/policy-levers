"""Render Q8 PPP piece to PDF with clickable internal links.

Target: essays/mats_chang/q8/Q8_PPP.md
Citation style: pandoc `[^N]` footnotes with `[^N]: definition` lines.
Pandoc handles the cross-linking natively — every `[^N]` becomes a
superscript hyperlink to the footnote block, and every footnote gets a
back-arrow to the callsite. Weasyprint carries those anchor links from
HTML into the PDF unchanged.

No preprocessing needed for this doc's citation style.

Pipeline: markdown → pandoc HTML5 → weasyprint PDF.

Run:
    uv run --script scripts/render_q8.py

Output: essays/mats_chang/q8/rendered/Q8_PPP.pdf
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
INPUT = REPO_ROOT / "essays/mats_chang/q8/Q8_PPP.md"
OUTPUT_DIR = REPO_ROOT / "essays/mats_chang/q8/rendered"
DISPLAY_TITLE = "Patients, Property, and Power"
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

# Strip leading H1 headings so pandoc's title metadata renders as the sole
# title (the source begins with `# Patients, Property, and Power` — the
# same title, but we want pandoc's title-block styling, not an extra H1).
LEADING_H1_RE = re.compile(r"\A(?:\s*\n|#\s+[^\n]*\n)+")


def strip_leading_h1(text: str) -> str:
    return LEADING_H1_RE.sub("", text, count=1)

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
blockquote { border-left: 3px solid #bbb; margin: 0.6em 0; padding: 0.1em 0.9em; color: #555; }
/* Q8 has HTML-style comments (<!-- TODO: ... -->) inside footnotes;
   pandoc strips them by default, so nothing to hide here. */
.footnotes { border-top: 1px solid #ccc; margin-top: 2em; padding-top: 0.6em; font-size: 9.5pt; }
.footnotes ol > li { margin-bottom: 0.35em; }
"""


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

    processed = frontmatter() + strip_leading_h1(INPUT.read_text())

    with tempfile.TemporaryDirectory() as tmpdir:
        md_path = Path(tmpdir) / "input.md"
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
