# Staffer name-hunt — 11 uncaptured priority House offices

**Date:** 2026-07-18
**Branch:** main (gaaia-analysis research line)

## Summary

Handoff session executing mechanics item #1 from
`docs/active/gaaia-analysis/results/20260717_contact_matrix.md`: run a
name-hunt for the Legislative Director or AI/tech Legislative Assistant
at each of the 11 uncaptured priority House offices identified in the
07-17 contact matrix — Tier A minus Obernolte (Trahan, Subramanyam,
Franklin, Houchin, Peters, Foushee), the front-of-queue Science sweep
(Babin, Lofgren, Stevens), the MD constituent lane (McClain Delaney),
and the technical uptake candidate (Whitesides). Dan pre-vetted the
list of 11 (with phone/office info) in the handoff and asked for
disagreement; none noted — the list matches Tier A/B exactly.

The hunt fanned out to 11 parallel general-purpose subagents, one per
office, each briefed with the member's name/party/district/phone/office
and a source-priority list (LegiStorm free tier → LinkedIn → press
releases → aggregators). All 11 returned a routable staffer with source
URLs and a confidence rating; results were aggregated into
`crm/contacts.yaml` under a new "GAAIA HOUSE OUTREACH (2026-07-18
name-hunt pass)" section, preserving Burns/Kindler/samantha-foster per
handoff constraint.

Post-hunt, at Dan's request, a durable reference doc
(`results/20260718_staffer_name_hunt.md`) consolidates the summary
table, per-office notes, cross-cutting findings, corrections/flags,
next steps, and a methodology section (source-of-truth ranking + the
observed WebFetch failure modes on several .house.gov subdomains).
STATUS.md and RESEARCH_LOG.md updated so the pass is discoverable via
either entry point.

## Topics Explored

- Parallel-agent fan-out pattern for staffer-identification work across
  many offices (one agent per office, structured prompts, standardized
  return format)
- LegiStorm free-tier coverage vs paywalled portfolio-tagged staff
  rosters — the latter blocks direct "who is the AI LA" identification;
  free tier still yields LD + Sr Policy Adviser + CoS with high fidelity
- Cross-referencing LegiStorm salary records against aggregator staff
  lists (Legisletter, RocketReach, ContactOut, AASLH LD PDF) — the
  aggregators lag reality by 3-12 months
- Committee-vs-personal-office routing when a member chairs the relevant
  committee (Babin/Science): AI portfolio flows through committee
  majority staff, personal-office LA becomes vestigial for that topic
- Cross-office staff-mobility signals (Bagwell Whitesides → Subramanyam
  with overlapping March 2026 salary) as a check on transition state

## Provisional Findings

- **11/11 hit rate** identifying a routable staffer (LD or Sr Policy
  Adviser); no office fell back to pure webform
- **Best AI-portfolio hit: Niel Schrage (Houchin)** — Sr Policy Adviser
  with CS background (Harvard), prior tech-and-competition work at
  Invariant, spring 2026 MIT senior-Hill-only "Future of AI" seminar
  invitee, and an email header-verified via the AARST disbursement
  scrape (not just standard-format construction). HIGH confidence;
  candidate for the pilot email
- **Weakest coverage: Babin (Science Chair)** — no personal-office AI
  LA surfaced; personal-office LD slot appears vacant (Tucker → Blue
  Origin Nov 2025). Route via House Science majority committee staff
  (Janushkowsky = Staff Director, Danny Smith = Sr Adviser; both
  ex-Babin personal-office). Same pattern likely repeats at Guthrie
  (E&C chair) when we get there
- **No dedicated "AI LA" title surfaced in free tier at any of the 11
  offices** — LegiStorm Pro paywalls the portfolio-tagged roster. Route
  via LD or Sr Policy Adviser; front-desk confirmation is the cheapest
  way to close the specific-AI-owner question
- **Recent-turnover risk is universal:** 6 of 11 offices show major LD
  or CoS reshuffles in the last ~12 months; aggregators are lagging
  indicators. Trust LegiStorm salary records + fresh press releases,
  distrust aggregators
- **Two Democratic offices flagged for tone:** Foushee (competitive
  2026 primary with heavy AI-PAC involvement on both sides — lead with
  Canary's non-industry framing) and Stevens (2026 Senate run — House
  office attention shift likely; verify Steadman still in role)

## Decisions Made

- Aggregated 11 hits directly into `crm/contacts.yaml` under a new
  dated section, one primary staffer per office with 1-3 alternatives
  in the `context` block rather than as separate CRM entries (keeps
  file manageable; existing offices with multiple entries already have
  this looser pattern)
- Preserved Burns/Kindler/samantha-foster entries verbatim per handoff
  constraint; validated post-write that all three retain their original
  `first_met`/`priority`/`followup_by` values
- Created durable reference doc at
  `results/20260718_staffer_name_hunt.md` (269 lines) as the
  scan-friendly summary + provenance record — separate from the CRM
  entries, which are the operational data
- Franklin district discrepancy (FL-15 in 07-17 matrix; actually FL-18
  since 2023 redistricting) flagged in the report and in RESEARCH_LOG
  next-steps; not corrected in the 07-17 matrix itself this session
  (single-file mechanical edit, low-priority follow-up)
- No plan doc created — this session executed a handoff task; no
  new implementation work emerged

## Results

- `../results/20260718_staffer_name_hunt.md` — full report: summary
  table (11 rows), per-office notes with source URLs and fallback
  paths, cross-cutting findings, corrections/flags, recommended next
  steps, and methodology (source-of-truth ranking + observed WebFetch
  failure modes)
- `../../../crm/contacts.yaml` — 11 new entries under "GAAIA HOUSE
  OUTREACH (2026-07-18 name-hunt pass)"; contacts count 25 → 36;
  Burns/Kindler/samantha-foster untouched; YAML validated

## Open Questions

- Whether Powell (Lofgren) actually carries the AI portfolio or is a
  bad inference (no explicit AI/tech title surfaced; based on the
  office's Silicon Valley tech identity and no other tech-titled
  staffer being visible) — front-desk call would settle it
- Whether Bagwell's Whitesides→Subramanyam transition is fully cut
  over (overlapping March-2026 salary suggests mid-month); if
  `shaefer.bagwell@mail.house.gov` bounces, need to fall back to the
  Subramanyam webform + FD call
- Whether Foushee's 2026-primary AI-PAC filtering meaningfully blocks
  educational outreach from a small nonprofit or just from industry
  entities — not testable without an outreach attempt
- Whether committee-staff routing at Babin is durable or a symptom of
  the personal-office LD vacancy (Tucker → Blue Origin Nov 2025); may
  resolve if we identify a current personal-office LD via front-desk
  call
- Whether the Lawfare "fix it" author (contact-matrix open item, row
  72) has any overlap with our staffer set — not investigated this
  session; carried forward

## Captured Tasks

- [#4: [2026-07-21] Add Hassabis manifesto + Amodei FAA-call to papers/](https://github.com/danparshall/policy-levers/issues/4) — captured 2026-07-18
