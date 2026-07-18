# Matrix and Blog Corrections (post-9363-adversarial-review)

**Date:** 2026-07-18
**Branch:** gaaia-analysis (running on main)

## Summary

Applied the correction queue that accumulated from the 7/17–18 sessions: the Franklin
district fix in the contact matrix, and the blog edits mandated by
`results/20260717_hr9363_memo_adversarial_review.md` ("defensible framing" section).
The blog's Two-CAISIs section then went through two further rewrites driven by Dan's
editorial challenge ("what *exactly* is the point?"): first a thesis-driven version
(hedge vs. substitute, intent-agnostic ratchet, reconcile-or-not as falsifiable tell),
then — per Dan's direction — a two-paragraph cut around the clean sequencing story:
**doing what can be done now, awaiting future fixes**.

Along the way the session verified several factual questions against primary text:
H.R. 9363's committee referral (sole referral to Science — confirmed from the ih print
header, which also lists introduction cosponsors Foushee, Babin, Mann, Franklin —
partially resolving the matrix's cosponsor open item; Mann is new to us), the GAAIA
DeepSeek/extraterritoriality tidbit (verified accurate — no US nexus anywhere in
§101(8) "deploy" or §101(12) "frontier developer"), and the exact text of 9363's
(k) sunset and (e) confidentiality clauses.

The sharpest new analysis: **9363's sunset unseals the archive.** "(k) This section
shall terminate" five years post-enactment, with no grandfather clause; the (e)(1)
FOIA exemption and (e)(2)(B) use-restriction are part of the terminated section, so on
a plain reading every good-faith voluntary disclosure in the files loses protection at
year five. Partial backstop on the public-disclosure side (FOIA Exemption 4, case-by-
case); no backstop on the government-use side (best lab argument: Landgraf presumption
against retroactivity — colorable, not reliable). Operational kicker: the ambiguity
chills the voluntary channel in year one, not year six (ASRS analogy: announce reports
become discoverable in five years and reporting stops tomorrow). Fix is a one-sentence
grandfather clause — new annex ask, valence-neutral, natural fit for the Foushee email
(her bill, protects the labs her channel needs).

## Topics Explored

- Franklin FL-15→FL-18 propagation (matrix Tier A; payload map carries no districts;
  remaining FL-15 mentions in repo are docs describing the correction itself).
- Folding the 9363 adversarial-review verdicts into the blog and the matrix payload
  rows (Obernolte + Foushee revised narrow ask: §5304 slot + §5002 schemes + (e)(2)(B)
  interplay, technical-corrections framing).
- DeepSeek tidbit verification: §101 definitions + full-text grep for territorial
  hooks ("United States" hits are all US-Code citations / redaction boilerplate).
- Two-CAISIs section: what is 9363 *for*? Hedge vs. substitute vs. time bomb.
  Time-bomb reading rejected on evidence (both bills Obernolte's; 9363 built from
  GAAIA's parts bin — §5002 fork, even the use-restriction clause is GAAIA's own;
  nothing to undo). Best-evidence reading: hedge by design; the substitute/ceiling
  outcome is intent-independent if 9363 passes and GAAIA stalls.
- House mechanics for Dan: suspension calendar = no-amendment consensus fast lane
  (opposite of filibustered), 2/3 threshold; sole Science referral means no House
  committee gate remains; Senate is a real filter (Commerce referral, hotline/UC or
  vehicle).
- ASRS analogy (Dan's aviation-safety domain): 9363 ≈ confidential voluntary
  reporting desk + measurement labs stood up *before* there's an FAA behind them;
  aviation's voluntary channel works because it supplements a mandatory backbone.
  9363 buys instruments and an institution, not visibility.
- Sunset-vs-archive analysis (above).

## Provisional Findings

- 9363 sole referral to House Science (verified, ih print); introduction cosponsors
  Foushee, Babin, Mann, Scott Franklin.
- DeepSeek/extraterritoriality blog tidbit is accurate as hedged; no change needed.
- Plain-reading conclusion that (k) sunset terminates (e) protections for
  already-shared information; retroactivity canon is the counter-argument; FOIA
  Exemption 4 survives independently. (Provisional — no case law checked beyond
  general doctrine; fine for annex framing since the ask is just a clarifying
  sentence.)
- Editorial: the post-adversarial-review patch left the Two-CAISIs section
  thesis-free ("weird interactions may occur"); the fix was committing to the
  sequencing story and compressing.

## Decisions Made

- Blog Two-CAISIs section is now TWO paragraphs (sequencing story; ASRS-before-FAA;
  two cheap annex fixes: §5002/§5304 reconciliation + sunset grandfather clause).
  Cut entirely: two-stories structure, down-payment/receipt tell, use-immunity
  confession paragraph, TOC-poetry parenthetical (annex/NOTES keep all the substance).
- **New annex ask adopted: (e)-protections grandfather clause** for information shared
  before termination. Should be added to NOTES.md tier structure next session.
- Matrix payload rows for Obernolte and Foushee carry the revised narrow ask per the
  adversarial review.
- Commit discipline: other session's staged Hassabis paper files left untouched;
  session commit uses explicit pathspecs.

## Results

- No new results files; session outputs are edits in place:
  - `results/20260717_contact_matrix.md` (FL-18 + correction note + revised asks)
  - `essays/canary/gaaia-visibility-not-control_DAN.md` (header changelog documents
    all three passes)

## Open Questions

- Dan seam-check of the rewritten Two-CAISIs section (Claude-drafted in his register).
- Dan's transitions + 501(h) call on the comment-invite aside — still the remaining
  publish blockers.
- Grandfather-clause ask: add to NOTES.md (which tier — cheap ask, presumably 2.x?).
- rh-text reconcile when GPO posts (standing).
- Does the ASRS-without-an-FAA frame belong anywhere else in the outreach material
  (Science-sweep emails)? It compressed well in the blog.
