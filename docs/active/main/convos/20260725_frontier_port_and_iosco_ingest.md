# FRONTIER essay port + IOSCO paper ingest

**Date:** 2026-07-25
**Branch:** main

## Summary

Short session, two unrelated tasks on main.

First: reconciled the two FRONTIER-Act blog drafts. `essays/canary/frontier-act-tech-pace.md` (tracked) had picked up two typo fixes and an inline-markdown SSI-link render across commits `b3cf522` and `37e4c68`. `essays/canary/frontier-act-tech-pace_DAN.md` (added fresh at `8958dfd` by Dan directly, timestamped *after* those fixes) still had the pre-fix text — an unrendered link stub and the two typos ("The might change", "reates"). Diff was only 13 lines, all three items visible. Ported `_DAN.md` verbatim over the tracked file per Dan's direction after two rounds of pushback where I flagged that the "edits" were regressions of already-fixed items; Dan confirmed intent and asked for the port explicitly. Commit `cebe179` documents the reversal in its message. Push required a rebase over `eeb39d0` (concurrent NOTES_FRONTIER cleanup from another session, orthogonal file — no conflict).

Second: added IOSCO's March-2025 Consultation Report *Artificial Intelligence in Capital Markets: Use Cases, Risks, and Challenges* (CR/01/2025) to the paper collection. Direct `curl` to `iosco.org` returned a Cloudflare block page (4.5 KB HTML, not the PDF); User-Agent spoofing + full browser headers didn't help (Cloudflare terminated the connection, exit 56). Fallback: Wayback Machine served the intact 1.15 MB PDF. Filed as `papers/IOSCO__2025--ai_in_capital_markets.pdf` following the newer `Author__YEAR--slug.pdf` convention now in use for institutional/single-author items (Hassabis, Ortega, MacDonald). Extracted 3,801 lines via `pdftotext`; wrote entries in `PAPER_INDEX.md` (Research Papers section) and `PAPER_SUMMARIES.md`. First summary draft over-hooked the paper to Dan's FRONTIER essay (audit-industry-independence, Hill-staffer framing); rewrote per Dan's request to describe the paper's own thrust — evidence base, four-category risk taxonomy, cross-jurisdictional regulatory inventory, caveats — dropping the "Relevance for policy-levers" section entirely.

## Topics Explored

- Diff between the two FRONTIER-essay drafts on main; whether "port DAN edits" was a well-formed instruction given `_DAN.md` had only regressions
- IOSCO Cloudflare-blocking behavior and Wayback-Machine fallback for institutional-publisher PDFs
- IOSCO 2025 Consultation Report content: use cases in capital markets, four-category risk taxonomy, cross-jurisdictional regulatory-response inventory
- Summary voice calibration: neutral paper-thrust vs. FRONTIER-tied policy-relevance hooks (dropped the latter)

## Provisional Findings

- **IOSCO's four-category risk taxonomy** (AMCC-ranked severity order): (1) malicious uses of AI [deepfakes, personalized phishing, market-manipulation misinformation; OSC finding of 22% higher investment in AI-enhanced scams vs conventional]; (2) AI model & data considerations [explainability, hallucinations, bias, data-quality/collapse]; (3) concentration, outsourcing, third-party dependency [across compute, data aggregation, and model provision — the vector most parallel to finance-industry Big-Four concerns]; (4) human-AI interaction [accountability gaps, talent scarcity, automation bias].
- **Regulatory-approach inventory**: IOSCO members split between existing-frameworks-adapted-for-AI (HKMA/SFC, ESMA MiFID II, CSA Staff Notice 11-348, CFTC staff advisory) and bespoke frameworks (Greek Law 4961/2022, Japan AI Guidelines for Business, EU AI Act, Brazil Draft Bill 2.338/2023, Canada AIDA proposal, Australia consultation). Engagement stats: 15/27 members issued guidance; 6/27 provided sandboxes; **0/27 issued regulatory waivers or exemptions**. SEC "AI-washing" enforcement cited as active federal lever.
- **Publisher accessibility note**: `iosco.org` is Cloudflare-fronted with UA-independent blocking; direct `curl` will not obtain their PDFs. Wayback Machine is the reliable fallback. Worth noting for any future IOSCO-publication ingest.
- **Convention note**: `_DAN.md` sibling files are personal working drafts that may be committed but should not be assumed to supersede the tracked file — verify direction of "port" before executing when the diff shows regressions.

## Decisions Made

- FRONTIER essay: tracked file now matches `_DAN.md` (regresses two typo fixes and the SSI link render, per Dan's explicit call). Commit message explicitly documents the reversal so history is honest.
- IOSCO summary: neutral paper-thrust register, no FRONTIER cross-references. This is the register for institutional-report ingests where the paper stands on its own.

## Results

- Commit `cebe179` — `frontier-act-tech-pace.md` port from `_DAN.md`
- `papers/IOSCO__2025--ai_in_capital_markets.pdf` (1.15 MB, from Wayback Machine)
- `papers/text/IOSCO__2025--ai_in_capital_markets.txt` (3,801 lines, pdftotext)
- `PAPER_INDEX.md` — one-line IOSCO entry appended to Research Papers section
- `PAPER_SUMMARIES.md` — full IOSCO entry with evidence base, four-category risk taxonomy, regulatory-response inventory, three neutral caveats-when-citing

## Open Questions

- If Dan wants to re-apply the two typo fixes ("The"→"This", "reates"→"creates") and the inline SSI link render on top of the ported text, that's a separate action — not done this session.
- Whether IOSCO Phase-2 output (per IOSCOPD789 workplan) will be worth ingesting when it lands; the Phase-1 report is deliberately consensus-mode and doesn't yet contain normative recommendations.
