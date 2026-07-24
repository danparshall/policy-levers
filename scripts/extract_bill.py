"""Extract text from a Congressional bill PDF into a plain-text file.

Congressional bill PDFs render with two visual columns: a narrow left column of
line numbers (1, 2, 3, ...) and the main text column. PyMuPDF's default reader
lays them out in position-based reading order, which places each line-number
integer on its own output line after the content line it labels. We strip those
standalone integers so the resulting text file is clean and matches the visual
reading order.

Usage:
    python3 scripts/extract_bill.py <input.pdf> <output.txt>
    python3 scripts/extract_bill.py <input.pdf> <output.txt> --keep-line-numbers

Line-number stripping removes any line that consists solely of digits and
whitespace. Set --keep-line-numbers to disable, which is useful when the target
downstream is a citation-checker that wants the original bill line numbers.

Requires: pymupdf (installed globally on the author's machines; `uv add pymupdf`
in project venvs). If poppler is available and the caller wants left-column
line-number formatting matching `pdftotext -layout`, use pdftotext instead —
both extractions cover the same content.
"""
import argparse
import re
import sys
from pathlib import Path

import fitz  # PyMuPDF


def extract(pdf_path: Path, keep_line_numbers: bool = False) -> str:
    """Return the text content of `pdf_path` as a single string.

    Pages are separated by `--- PAGE N ---` markers so downstream splitters
    can map back to a page range for citation.
    """
    doc = fitz.open(pdf_path)
    chunks = []
    for i, page in enumerate(doc):
        chunks.append(f"--- PAGE {i + 1} ---")
        chunks.append(page.get_text("text"))
    text = "\n".join(chunks)

    if not keep_line_numbers:
        text = strip_standalone_line_numbers(text)

    return text


def strip_standalone_line_numbers(text: str) -> str:
    """Remove lines consisting solely of an integer (bill line-number artifacts).

    Preserves integers that are part of a content line (e.g. `$1,000,000` in the
    middle of a sentence). Only removes lines whose entire content, after
    stripping whitespace, is one or more digits.
    """
    return re.sub(r"(?m)^\s*\d+\s*$\n?", "", text)


def main(argv):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input_pdf", type=Path)
    p.add_argument("output_txt", type=Path)
    p.add_argument(
        "--keep-line-numbers",
        action="store_true",
        help="Do not strip standalone bill-line-number lines.",
    )
    args = p.parse_args(argv)

    if not args.input_pdf.exists():
        p.error(f"input not found: {args.input_pdf}")

    text = extract(args.input_pdf, keep_line_numbers=args.keep_line_numbers)
    args.output_txt.write_text(text)
    bytes_written = args.output_txt.stat().st_size
    print(f"wrote {args.output_txt} ({bytes_written} bytes)")


if __name__ == "__main__":
    main(sys.argv[1:])
