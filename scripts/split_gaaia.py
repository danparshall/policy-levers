#!/usr/bin/env python3
"""Split the Great American Artificial Intelligence Act (GAAIA) discussion draft
(Obernolte-Trahan, 2026-06-04, 269 pp) into per-section markdown files.

Reconstruction, 2026-07-24: the original splitter (run 2026-07-14) was lost
from /tmp/ before it was committed. This is a reconstruction based on the
committed section-file format at `bills/obernolte-trahan/sections/*.md`.

Approach:
  1. Auto-detect top-level SEC. / SECTION 1. boundaries via regex over the
     pdftotext-layout output. Regex allows any whitespace between "SEC." and
     the section number to catch the pdftotext-layout-mangled §§ 122 / 311 /
     424 headers ("SEC.      NNN."), and skips the inserted `''SEC. NNNN.`
     amendments to the National AI Initiative Act inside § 102 because those
     have a different indentation profile (no leading-line-number prefix).
  2. Look up each section's cleaned title + filename slug from the SECTION_META
     table below. Titles carry the same quirks as the committed files —
     line-continuation joins ("INTEL-\\nLIGENCE" -> "INTELLIGENCE") were made
     for some sections but not all (§§ 122, 411, 424 retain their raw
     justified-typeset whitespace). Preserved verbatim from the committed
     section headers.
  3. Emit each section as `sec-NN-slug.md` (SEC. 1 uses zero-padding in the
     filename per committed convention; all others match the section number
     directly) with the committed markdown skeleton:
       # SEC. N. Title
       - Bill: ...
       - Source: ...
       - Raw PDF: ...
       ```text
       <raw body>
       ```

Byte-equivalence caveat: the committed section-file line-range citations
(e.g. "lines 159-386") were computed against a slightly-longer version of
`gaaia_full_text.txt` than what is currently in the repo — a subsequent pass
stripped some page-footer content, reducing total-lines from ~9217 to 8948.
Section CONTENT is nearly byte-identical (most sections match; a handful
differ by 1-2 bytes for footer-inclusion), but this splitter's line-range
output will not match the committed line-range citations for that reason.
Run --verify to see the drift. Regenerating the committed sections/ against
the current text is a separate decision; this script does not auto-do that.

The FRONTIER Act splitter is at `split_frontier.py` in this directory. That
script uses a different section-file format (HTML-comment provenance instead
of visible bullets). The two are intentionally not harmonized — retro-fixing
either bill's committed section files is a separate decision.

Usage:
  python3 scripts/split_gaaia.py            # write sections/ and SECTION_MANIFEST.md
  python3 scripts/split_gaaia.py --verify   # verify against committed files (expect drift)
"""

import argparse
import re
import sys
from pathlib import Path

BILL_DIR = Path("/Users/dan/code/policy-levers/bills/obernolte-trahan")
SRC_TXT = BILL_DIR / "gaaia_full_text.txt"
SECTIONS_DIR = BILL_DIR / "sections"
MANIFEST = BILL_DIR / "SECTION_MANIFEST.md"

# (section_number, title_for_header, filename_slug)
# Titles preserve the exact wording in the committed sec-*.md files. Some are
# cleaned line-continuations (§ 111 body reads "INTEL-\nLIGENCE" but title
# reads "INTELLIGENCE"), some retain justified-typeset whitespace quirks
# (§§ 122, 424 preserve raw multi-space). Matches the committed sections/*.md
# files byte-for-byte; do not "clean" without checking output.
SECTION_META = [
    (1,   "Short title; table of contents",                                                       "short-title-table-of-contents"),
    (101, "DEFINITIONS",                                                                          "definitions"),
    (102, "CENTER FOR AI STANDARDS AND INNOVATION",                                               "center-for-ai-standards-and-innovation"),
    (111, "TRANSPARENCY IN FRONTIER ARTIFICIAL INTELLIGENCE",                                     "transparency-in-frontier-artificial-intelligence"),
    (112, "INDEPENDENT VERIFICATION ORGANIZATION AUDITS AND ASSESSMENTS",                         "independent-verification-organization-audits-and-assessments"),
    (113, "ANTI-RETALIATION PROTECTION FOR AI WHISTLEBLOWERS",                                    "anti-retaliation-protection-for-ai-whistleblowers"),
    (121, "FEDERALIZATION OF STATE LAWS REGULATING",                                              "federalization-of-state-laws-regulating"),
    (122, "COMPTROLLER        GENERAL   OF   THE   UNITED",                                       "comptroller-general-of-the-united"),
    (123, "RESOURCES FOR ARTIFICIAL INTELLIGENCE",                                                "resources-for-artificial-intelligence"),
    (131, "FINANCIAL CRIMES AND ARTIFICIAL INTELLIGENCE",                                         "financial-crimes-and-artificial-intelligence"),
    (132, "AI IMPERSONATION OF FEDERAL OFFICIALS",                                                "ai-impersonation-of-federal-officials"),
    (141, "PREVENTING CENSORSHIP AND PROTECTING",                                                 "preventing-censorship-and-protecting"),
    (201, "AI LITERACY EFFORTS OF THE AI TASK FORCE",                                             "ai-literacy-efforts-of-the-ai-task-force"),
    (211, "PREPARING K–12 EDUCATORS AND STUDENTS",                                           "preparing-k12-educators-and-students"),
    (221, "EXPANDING CAPACITY IN ARTIFICIAL INTELLIGENCE SCIENCE",                                "expanding-capacity-in-artificial-intelligence-science"),
    (231, "SCHOLARSHIPS AND FELLOWSHIPS IN ARTIFICIAL INTELLIGENCE",                              "scholarships-and-fellowships-in-artificial-intelligence"),
    (232, "COMMUNITY COLLEGE AND AREA CAREER AND",                                                "community-college-and-area-career-and"),
    (233, "AWARDS FOR RESEARCH ON ARTIFICIAL INTELLIGENCE IN EDUCATION",                          "awards-for-research-on-artificial-intelligence-in-education"),
    (241, "INFORMATION COLLECTION AND DISCUSSION",                                                "information-collection-and-discussion"),
    (242, "ATTRACTING HIGHLY QUALIFIED EXPERTS IN ARTIFICIAL INTELLIGENCE AND OTHER FIELDS",      "attracting-highly-qualified-experts-in-artificial-intelligence-and"),
    (243, "ARTIFICIAL INTELLIGENCE WORKFORCE RESEARCH HUB",                                       "artificial-intelligence-workforce-research-hub"),
    (244, "MODERNIZING ACCESS TO ARTIFICIAL INTELLIGENCE-RELATED LABOR MARKET DATA",              "modernizing-access-to-artificial-intelligence-related-labor-market-data"),
    (245, "SUPPORT FOR EVALUATION OF ARTIFICIAL INTELLIGENCE AUTOMATION",                         "support-for-evaluation-of-artificial-intelligence-automation"),
    (246, "VOLUNTARY ARTIFICIAL INTELLIGENCE ADOPTION AND USE REPORTING AND DATA-SHARING PARTNERSHIPS", "voluntary-artificial-intelligence-adoption-and-use-reporting-and"),
    (247, "ARTIFICIAL INTELLIGENCE QUESTIONS IN FEDERAL SURVEYS",                                 "artificial-intelligence-questions-in-federal-surveys"),
    (248, "DATA ELEMENTS AND PRODUCTION",                                                         "data-elements-and-production"),
    (251, "DISCLOSURES UNDER THE WORKER ADJUSTMENT AND RETRAINING NOTIFICATION ACT",              "disclosures-under-the-worker-adjustment-and-retraining-notification"),
    (252, "DETAILED EMPLOYMENT FORECASTS FOR AI-SENSITIVE OCCUPATIONS",                           "detailed-employment-forecasts-for-ai-sensitive-occupations"),
    (253, "FORECASTING PRIZE COMPETITION",                                                        "forecasting-prize-competition"),
    (254, "REPORT ON USE OF NEW RESEARCH AND TOOLS",                                              "report-on-use-of-new-research-and-tools"),
    (255, "STUDY ON RAPID ARTIFICIAL INTELLIGENCE ADJUSTMENT ASSISTANCE PROGRAM",                 "study-on-rapid-artificial-intelligence-adjustment-assistance-program"),
    (256, "UPDATE OF STATE IN-DEMAND INDUSTRY SECTOR AND OCCUPATION LISTS",                       "update-of-state-in-demand-industry-sector-and-occupation"),
    (257, "AI WORKFORCE POLICY OPTIONS REPORT",                                                   "ai-workforce-policy-options-report"),
    (301, "REAUTHORIZATION OF CYBERSECURITY ACT OF",                                              "reauthorization-of-cybersecurity-act-of"),
    (311, "SUPPORT FOR DESIGNATED CRITICAL OPENSOURCE SOFTWARE MAINTAINERS",                      "support-for-designated-critical-opensource-software-maintainers"),
    (321, "REPORT ON MODEL WEIGHT, DATA CENTER, AND",                                             "report-on-model-weight-data-center-and"),
    (401, "INTERAGENCY COORDINATION AND PROGRAM TO",                                              "interagency-coordination-and-program-to"),
    (402, "COORDINATION, REIMBURSEMENT, AND SAVINGS",                                             "coordination-reimbursement-and-savings"),
    (403, "PROGRESS REPORT",                                                                      "progress-report"),
    (411, "INTERNATIONAL COALITIONS ON INNOVATION,",                                              "international-coalitions-on-innovation"),
    (421, "PUBLIC DATA FOR ARTIFICIAL INTELLIGENCE",                                              "public-data-for-artificial-intelligence"),
    (422, "FEDERAL GRAND CHALLENGES IN ARTIFICIAL INTELLIGENCE",                                  "federal-grand-challenges-in-artificial-intelligence"),
    (423, "NATIONAL ARTIFICIAL INTELLIGENCE RESEARCH",                                            "national-artificial-intelligence-research"),
    (424, "LIQUID      COOLING        DEVELOPMENT     AND",                                       "liquid-cooling-development-and"),
    (431, "RESEARCH SECURITY",                                                                    "research-security"),
    (432, "CERTIFICATIONS AND AUDITS OF TEMPORARY",                                               "certifications-and-audits-of-temporary"),
]

# Committed line ranges (inclusive, 1-indexed, matching str.split("\n") counting).
# Auto-computed against the split boundaries; if the pdftotext output ever changes,
# these will drift and we'll catch it in --verify.
COMMITTED_RANGES = {
    1:   (1,    158),
    101: (159,  386),
    102: (387,  1022),
    111: (1023, 1511),
    112: (1512, 2260),
    113: (2261, 2531),
    121: (2532, 2627),
    122: (2628, 2677),
    123: (2678, 2819),
    131: (2820, 2950),
    132: (2951, 2961),
    141: (2962, 3130),
    201: (3131, 3147),
    211: (3148, 3250),
    221: (3251, 3404),
    231: (3405, 3678),
    232: (3679, 3911),
    233: (3912, 4091),
    241: (4092, 4379),
    242: (4380, 4547),
    243: (4548, 4620),
    244: (4621, 4795),
    245: (4796, 4930),
    246: (4931, 5081),
    247: (5082, 5182),
    248: (5183, 5243),
    251: (5244, 5316),
    252: (5317, 5631),
    253: (5632, 5757),
    254: (5758, 5831),
    255: (5832, 5955),
    256: (5956, 5978),
    257: (5979, 6058),
    301: (6059, 6498),
    311: (6499, 6641),
    321: (6642, 6701),
    401: (6702, 6917),
    402: (6918, 6972),
    403: (6973, 6991),
    411: (6992, 7191),
    421: (7192, 7464),
    422: (7465, 7969),
    423: (7970, 8795),
    424: (8796, 9092),
    431: (9093, 9102),
    432: (9103, 9217),
}


def find_boundaries(lines):
    """Return {sec_num: line_1indexed_start} for each top-level SEC. header.

    Regex allows any whitespace between "SEC." and the section number, to catch
    the pdftotext-layout-mangled §§ 122 / 311 / 424 headers ("SEC.      NNN.").
    Requires 5+ leading whitespace + a line-number prefix, which distinguishes
    top-level bill-body headers from the "''SEC. NNNN." inserted into other
    Acts inside amendments (those live inside quoted-material blocks with a
    different indentation profile)."""
    sec1_re = re.compile(r"^\s{5,}\d+\s+SECTION 1\.")
    secN_re = re.compile(r"^\s{5,}\d+\s+SEC\.\s+(\d+)\.")
    starts = {}
    for i, line in enumerate(lines, start=1):
        if sec1_re.match(line):
            if 1 in starts:
                sys.exit(f"ERROR: SECTION 1 matched twice (lines {starts[1]}, {i})")
            starts[1] = i
        else:
            m = secN_re.match(line)
            if m:
                n = int(m.group(1))
                if n in starts:
                    sys.exit(f"ERROR: SEC. {n} matched twice (lines {starts[n]}, {i})")
                starts[n] = i
    return starts


def compute_ranges(starts, total_lines):
    """Given {sec_num: start_line}, compute {sec_num: (start, end)} where end
    is the line before the next section's start (or total_lines for the last)."""
    ordered = sorted(starts.items(), key=lambda p: p[1])
    ranges = {}
    for idx, (num, start) in enumerate(ordered):
        end = ordered[idx + 1][1] - 1 if idx + 1 < len(ordered) else total_lines
        ranges[num] = (start, end)
    return ranges


def render_section(num, title, start, end, body):
    """Reproduce the committed sec-*.md format exactly."""
    # § 1's title is mixed case; all others upper.
    header_title = title
    return (
        f"# SEC. {num}. {header_title}\n"
        f"\n"
        f"- Bill: Great American Artificial Intelligence Act (discussion draft, 2026-06-04)\n"
        f"- Source: `gaaia_full_text.txt` lines {start}–{end}\n"
        f"- Raw PDF: `gaaia_discussion_draft_2026-06-04.pdf`\n"
        f"\n"
        f"```text\n"
        f"{body}\n"
        f"```\n"
    )


def render_manifest(entries):
    """Reproduce the committed SECTION_MANIFEST.md format.

    Note: the committed manifest has an extra blank line after the H1 and uses
    en-dashes in the line-range column. It also lists the raw-uppercase titles
    (as opposed to the cleaned titles used in the sec-*.md file headers) — so
    §§ 111, 112, 113, 121, etc. show their line-continuation-broken titles
    ("TRANSPARENCY IN FRONTIER ARTIFICIAL INTELLIGENCE" is joined, but
    "INDEPENDENT VERIFICATION ORGANIZATION AUDITS AND ASSESSMENTS" is also
    joined). To reproduce, use the SECTION_META titles verbatim — they are
    already the cleaned/preserved forms committed to the manifest."""
    rows = [
        "# GAAIA — section manifest",
        "",
        "",
        "| # | Num | Title | Source lines | File |",
        "|---|---|---|---|---|",
    ]
    for idx, (num, title, slug, start, end) in enumerate(entries):
        # sec-01 uses zero-padded ordinal in filename per committed convention
        # (all other sections use their raw number).
        fnum = f"{num:02d}" if num == 1 else str(num)
        rows.append(f"| {idx} | {num} | {title} | {start}–{end} | `sections/sec-{fnum}-{slug}.md` |")
    return "\n".join(rows) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true",
                        help="Only verify against committed sections/*.md; don't write.")
    args = parser.parse_args()

    if not SRC_TXT.exists():
        sys.exit(f"ERROR: {SRC_TXT} missing")

    # Use split("\n") to match grep -n / cat -n line counting (see split_frontier.py
    # for the form-feed / splitlines discrepancy).
    lines = SRC_TXT.read_text(encoding="utf-8").split("\n")
    total = len(lines)

    boundaries = find_boundaries(lines)
    if len(boundaries) != len(SECTION_META):
        expected = {n for n, _, _ in SECTION_META}
        found = set(boundaries)
        sys.exit(f"ERROR: detected {len(boundaries)} sections, expected {len(SECTION_META)}\n"
                 f"  missing: {sorted(expected - found)}\n"
                 f"  extra:   {sorted(found - expected)}")

    ranges = compute_ranges(boundaries, total)

    # Sanity: compare against the historical committed ranges.
    range_mismatches = [(n, ranges[n], COMMITTED_RANGES[n])
                        for n in COMMITTED_RANGES
                        if ranges.get(n) != COMMITTED_RANGES[n]]
    if range_mismatches:
        print("WARN: detected ranges differ from committed COMMITTED_RANGES:")
        for n, got, want in range_mismatches:
            print(f"  SEC {n}: got {got}, want {want}")

    if not args.verify:
        SECTIONS_DIR.mkdir(parents=True, exist_ok=True)

    manifest_entries = []
    for num, title, slug in SECTION_META:
        start, end = ranges[num]
        body = "\n".join(lines[start - 1:end])
        rendered = render_section(num, title, start, end, body)
        fnum = f"{num:02d}" if num == 1 else str(num)
        out_path = SECTIONS_DIR / f"sec-{fnum}-{slug}.md"
        manifest_entries.append((num, title, slug, start, end))
        if args.verify:
            if not out_path.exists():
                print(f"MISSING {out_path.name}")
                continue
            committed = out_path.read_text(encoding="utf-8")
            if committed == rendered:
                print(f"OK       {out_path.name}")
            else:
                print(f"DRIFT    {out_path.name}  (rendered={len(rendered)}b, committed={len(committed)}b)")
        else:
            out_path.write_text(rendered, encoding="utf-8")
            print(f"wrote    {out_path.name}  ({end - start + 1} lines)")

    manifest = render_manifest(manifest_entries)
    if args.verify:
        committed_manifest = MANIFEST.read_text(encoding="utf-8") if MANIFEST.exists() else ""
        if committed_manifest == manifest:
            print(f"OK       {MANIFEST.name}")
        else:
            print(f"DRIFT    {MANIFEST.name}")
    else:
        MANIFEST.write_text(manifest, encoding="utf-8")
        print(f"wrote    {MANIFEST.name}")


if __name__ == "__main__":
    main()
