# Great American Artificial Intelligence Act (GAAIA) — discussion draft

**Status:** Discussion draft, released 2026-06-04. Not formally introduced (no H.R./S. number yet).
**Lead sponsors:** Rep. Jay Obernolte (R-CA-23) and Rep. Lori Trahan (D-MA-03) — both House Energy & Commerce.
**Co-releasers:** Reps. Suhas Subramanyam (D-VA-10), Scott Franklin (R-FL-18), Scott Peters (D-CA-50), Erin Houchin (R-IN-09).
**Feedback address:** `GAAIA@mail.house.gov` (public comment period; no deadline specified in release).
**Length:** 269 pages, Word-authored PDF (2026-06-02).
**Committee path:** House Energy & Commerce (all six releasers sit there).

## What's in this folder

| File | What it is |
|------|-----------|
| `gaaia_discussion_draft_2026-06-04.pdf` | The bill itself, downloaded from trahan.house.gov. 2.1 MB. |
| `gaaia_full_text.txt` | `pdftotext -layout` extraction of the bill. Preserves the two-column-with-line-numbers format of Congressional bill text. 9,000+ lines. |
| `gaaia_section_by_section.pdf` / `.txt` | Section-by-section summary from Trahan's office. **See "Drafting inconsistencies" below** — the summary and body do not fully agree. |
| `gaaia_faq.pdf` / `.txt` | FAQ prepared by Trahan's office (~100 lines). |
| `press_release_2026-06-04.txt` | Trahan press release announcing the draft. |
| `sections/` | One markdown file per SEC. header found in the bill body. See `SECTION_MANIFEST.md` for the index. |
| `SECTION_MANIFEST.md` | Auto-generated index of the section files (line ranges, titles). |
| `summaries/` | Per-section summaries produced by this repo (Canary Institute analysis, not Trahan's office). Created incrementally alongside the sections. |

## Structure of the bill

- **TITLE I — FRONTIER AI GOVERNANCE**
  - Subtitle A — Definitions and CAISI (§§ 101, 102)
  - Subtitle B — Transparency, IVO, Whistleblower (§§ 111, 112, 113)
  - Subtitle C — Federalization and Federal Resources (§§ 121, 122, 123)
  - Subtitle D — AI Fraud Deterrence (§§ 131, 132)
  - Subtitle E — Free Speech (§ 141)
- **TITLE II — WORKFORCE**
  - Subtitle A — AI Education and Capacity (§§ 201, 211, 221, 231, 232, 233, [234])
  - Subtitle B — Labor Market Data and AI Workforce Research (§§ 241–248)
  - Subtitle C — Worker Protections and Adjustment Assistance (§§ 251–257)
- **TITLE III — CYBERSECURITY** (§§ 301, 311, 321)
- **TITLE IV — R&D + INTERNATIONAL COOPERATION**
  - Subtitle A — Testbeds and Interagency Coordination (§§ 401, 402, 403)
  - Subtitle B — International Cooperation (§ 411)
  - Subtitle C — AI R&D (§§ 421, 422, 423, 424)
  - Subtitle D — Research Security (§§ 431, 432)

## Drafting inconsistencies (as of 2026-06-04 discussion draft)

Flagged for possible feedback to `GAAIA@mail.house.gov`:

- **§ 234 (National STEM Teacher Corps)** appears in the section-by-section summary from Trahan's office but is **not present in the bill body** (neither in the body's TOC nor as a `SEC. 234.` header). The section-by-section describes it as adding "AI skills development to the National STEM Teacher Corps pilot program." The functional equivalent may be implicit in § 201, which points at the same NSF Teacher Corps pilot — but no `§ 234` exists in the text as of 2026-06-04.
- **§§ 122, 311, 424** exist in the body but the `SEC.` headers use extended internal whitespace (`SEC.       122.    COMPTROLLER    GENERAL   OF   THE   UNITED`); this is a pdftotext-layout artifact of the justified-typeset original and does not indicate a real gap.
- **§ 121 (Federalization)** preempts state/local laws targeting AI model development, with a three-year sunset. Section-by-section summarizes this. The body text also includes what functionally appears to be the § 122 GAO report requirements, though its own `SEC. 122.` header is present at line ~2628 of the extracted text.

## Sponsor framing (from press release + FAQ)

- **Trahan (D):** "meet the challenges … without smothering American innovation … protects workers, establishes real accountability for the most powerful frontier systems."
- **Obernolte (R):** "thoughtful and bipartisan approach … clear federal framework that promotes innovation, protects Americans from emerging risks."
- **Franklin (R):** already secured additional FY27 CAISI appropriations funding "to keep pace with this rapidly evolving technology."
- **Houchin (R):** anti-patchwork framing — "not regulate ourselves into falling behind China through a patchwork of fifty different state laws."
- **Peters (D):** "will not address all of the issues our businesses and families will face, but it is an encouraging first step."
- **Subramanyam (D):** worker/national-security framing; "work faster to address the challenges and opportunities."

## Where this fits in the repo

- **Bill text and per-section chunks live here.** They're archival: what's actually written.
- **Analysis, essays, and outreach positions built on top of this bill** go elsewhere:
  - `docs/active/<branch>/` for research lines analyzing the bill
  - `essays/` for public-facing writing
  - `crm/bills.yaml` for the metadata entry (see `gaaia_draft_2026_06`)
  - `leave-behinds/` for anything Hill-facing

## How the sections were split

The script that produced `sections/*.md` matched top-level `SEC. NNN.` headers in the bill body (rejecting inserted `''SEC.` headers that live inside amendments to other Acts, e.g. § 102's insertion of new `SEC. 5304` into the NAII Act). Each section file is Markdown with a short header pointing back to the source line range in `gaaia_full_text.txt`, followed by the raw pdftotext output in a fenced block. Preserving the raw formatting keeps subsection numbering (e.g. `(a)(1)(A)`) legible for citation.

## Provenance

- Bill PDF: `https://trahan.house.gov/uploadedfiles/the_great_american_ai_act_discussion_draft.pdf`
- Section-by-section: `https://trahan.house.gov/uploadedfiles/gaaia_discussion_draft_section-by-section.pdf`
- FAQ: `https://trahan.house.gov/uploadedfiles/2026.06.03_trahan_obernolte_ai_framework_faq.pdf`
- Press release: `https://trahan.house.gov/news/documentsingle.aspx?DocumentID=3783`

All downloaded 2026-07-14.
