# FRONTIER Act — introduced 2026-07-23

**Status:** Introduced 2026-07-23 in the House. Bill-text draft dated 2026-07-22 (10:56 a.m.); the copy posted on Trahan's site still bears `H.R. ll` placeholder and blank committee referral, so the parliamentarian-assigned bill number and committee were not baked in at the moment of publication.
**Full title:** Frontier **R**isk **O**versight, **N**ational **T**ransparency, **I**ndependent **E**valuation, and **R**eporting Act (FRONTIER Act).
**Lead sponsors:** Rep. Jay Obernolte (R-CA-23) and Rep. Lori Trahan (D-MA-03).
**Cosponsors:** Reps. Scott Peters (D-CA-50), Scott Franklin (R-FL-18), Suhas Subramanyam (D-VA-10) [press release spelling; the GAAIA discussion draft used "Subramanyam" — same person], Erin Houchin (R-IN-09).
**Length:** 74 pages, 9 sections (§§ 1–9), flat structure (no titles/subtitles).

## Relationship to the Great American AI Act (GAAIA) discussion draft

FRONTIER is the frontier-oversight slice of the June 2026 GAAIA discussion draft (`bills/obernolte-trahan/`), formally introduced under a new name. Trahan's press release calls it "developed as part of the broader Great American AI Act framework." Substantively, FRONTIER corresponds to (a subset of) GAAIA Title I — the definitions, transparency, IVO audit, and preemption sections — and drops or defers the workforce, cybersecurity, and R&D titles that made up the bulk of GAAIA's 269 pages.

Substantive shifts from the GAAIA discussion draft (verify against per-section summaries):

- **New tier**: "very large frontier developer" ($5B revenue AND $10B AI-related development expenditures, both measured with affiliates over preceding 36 months) sits above "large frontier developer" ($50M revenue AND $1B expenditures). Coverage is now keyed to AI-development spend, not just gross revenue.
- **New administering officer**: "Under Secretary of Commerce for AI Security" replaces GAAIA's CAISI at NIST as the licensing/rulemaking/reporting body.
- **New authority (§ 8)**: Commerce Secretary may issue emergency orders suspending or restricting development, deployment, or internal use of a frontier model on written finding of imminent catastrophic risk. Provisional orders 45 days; final orders 90 days, renewable only on fresh finding. Civil penalty up to **$10M/day**; willful violations criminal. Exclusive judicial review D.D.C., appeal D.C. Circuit. This authority did not exist in GAAIA.
- **Whistleblower title dropped** (was GAAIA § 113 anti-retaliation).
- **Preemption (§ 9)** narrower and more targeted — s-by-s explicitly names CA SB-53, NY RAISE, IL SB-315 as the state statutes the section is aimed at.
- Definitions expanded: "cyber weapons" added to the CBRN catastrophic-risk scope; new "imminent catastrophic risk" and "deceptive techniques" clauses (the latter as a critical-safety-incident trigger).

See `FRONTIER_VS_GAAIA.md` for the structural changes writeup once it lands, and per-section summaries in `summaries/` for section-level drift.

## Sponsor framing (from press release)

- **Trahan (D):** "commonsense transparency and independent oversight for the largest AI developers … single, clear national standard … protect the public from catastrophic risks without slowing the innovation that keeps America competitive."
- **Obernolte (R):** "focuses oversight on the largest developers and most advanced models, requiring transparency, independent evaluation, and timely reporting of serious safety incidents."
- **Peters (D):** "The window to get AI policy right is closing, and Congress can't afford to miss it. … targeted bill with clear, uniform transparency, and safety standards, instead of a fifty-state patchwork."
- **Franklin (R):** "targeted approach … focusing only on the handful of companies developing the most powerful frontier AI models, not the startups and innovators driving America's AI ecosystem."
- **Subramanyam (D):** "This is a four-alarm fire. We need to take action now. … not perfect, but … an important, bipartisan step in the right direction."
- **Houchin (R):** "Just this week, one of the most advanced AI systems in the country broke out of its own developer's testing environment, reaching systems it was never supposed to touch. This is exactly the kind of incident that shouldn't stay behind closed doors."

Houchin's quote is on-record identification of a specific concurrent incident as the motivating fact. Recording her language verbatim here because it will matter for outreach positioning.

## What's in this folder

| File | What it is |
|------|-----------|
| `frontier_act_text.pdf` | The bill itself, downloaded from trahan.house.gov. Acrobat Distiller 26.0 (Windows), 74 pp, 216 KB. |
| `frontier_act_text.txt` | `pdftotext -layout` extraction. 2,424 lines. |
| `frontier_act_section_by_section.pdf` / `.txt` | Section-by-section summary from Trahan's office, dated 2026-07-21. 3 pp. |
| `press_release_2026-07-23.html` | Trahan press release, saved 2026-07-24. |
| `sections/` | One markdown file per SEC. header. See `SECTION_MANIFEST.md`. |
| `SECTION_MANIFEST.md` | Auto-generated index of the section files (line ranges, titles). |
| `summaries/` | Per-section summaries (Canary Institute analysis, not Trahan's office). |
| `OVERVIEW.md` | Canary descriptive overview. Descriptive only; analysis goes to `docs/active/`. |
| `FRONTIER_VS_GAAIA.md` | Structural-changes doc: what moved, what dropped, what's new vs the GAAIA discussion draft. |

## Structure of the bill

- **§ 1** — Short title
- **§ 2** — Definitions (22 defined terms, including the new "very large frontier developer" and "Under Secretary of Commerce for AI Security")
- **§ 3** — Rulemaking (Under Secretary notice-and-comment authority; three 180-day rulemakings; threshold adjustment)
- **§ 4** — Transparency and reporting (frontier AI framework requirements; transparency reports; incident reporting; civil penalty up to $1M/violation/day)
- **§ 5** — Independent verification (IVO licensing; very-large-tier ongoing assessment; 72-hour IVO referral to Secretary on imminent catastrophic risk)
- **§ 6** — Cumulative obligations (each higher tier complies with lower-tier duties)
- **§ 7** — GAO report on IVO market (annual, IVO independence assessment)
- **§ 8** — Emergency orders addressing imminent catastrophic risk (Secretary authority; 45d provisional / 90d final; D.D.C. judicial review; $10M/day civil / criminal for willful violations; exclusive federal remedy)
- **§ 9** — Relationship to State laws (preemption of frontier-safety statutes; carve-outs for generally applicable law, deployer/user regulation, minor-protection, procurement)

## Where this fits in the repo

- **Bill text and per-section chunks live here.** Archival: what's actually written.
- **Analysis, essays, and outreach positions built on top of this bill** go elsewhere:
  - `docs/active/gaaia-analysis/` — the analysis line is shared with the GAAIA discussion-draft work; new convos append there
  - `essays/` for public-facing writing
  - `crm/bills.yaml` for the metadata entry
  - `leave-behinds/` for anything Hill-facing

## How the sections were split

`scripts/split_frontier.py` (Python) matches `SECTION 1.` and `SEC. N.` at the top-level indentation used for section headers. FRONTIER is simpler than GAAIA on this front: no amendments-to-other-acts, so no inserted `''SEC.` headers to filter out. Line numbers in `SECTION_MANIFEST.md` correspond to `grep -n` / `cat -n` counts in `frontier_act_text.txt` (the splitter uses `str.split("\n")` rather than `str.splitlines()` to avoid a form-feed/pdftotext discrepancy — see the script's inline comment for details).

Companion script `scripts/split_gaaia.py` was reconstructed the same day (original was lost from `/tmp/` before commit). See its docstring for the byte-equivalence caveat.

## Provenance

- Bill PDF: `https://trahan.house.gov/uploadedfiles/oberno_079_xml_-_the_frontier_act_-_final_text.pdf`
- Section-by-section: `https://trahan.house.gov/uploadedfiles/26-07-21_-_frontier_act_section-by-section.pdf`
- Press release: `https://trahan.house.gov/news/documentsingle.aspx?DocumentID=3823`

All downloaded 2026-07-24.
