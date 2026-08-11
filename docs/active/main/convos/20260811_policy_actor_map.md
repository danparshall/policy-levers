# Policy actor map — prior-art scan + ControlAI outreach writeups

**Date:** 2026-08-11
**Branch:** main
**Surface:** claude.ai

## Summary

Two loosely related tasks, both exploratory, neither tied to an active research line.

First, Dan asked whether a webpage already exists organizing "Group X is working on Problem Y
using Approach Z" for AI policy (safety, governance, control), and if not, what a good one would
need. Web scan turned up four families of partial prior art, none in the target schema: actor-plus-
category maps (AISafety.com/map), actor-plus-stance maps (Mapping AI at aimapping.org, ~1,800
entries, launched ~May 2026; Sorensen's AI Stance Directory), document-plus-risk-taxonomy work
(AGORA / CSET + MIT AI Risk Initiative, 1,000+ governance documents), and one narrow
problem-plus-approach-plus-group study (IAPS, 80 papers across 3 labs, 2022-2024 cutoff). Full
inventory in results. Claude pushed back on two grounds — the "approach" axis has no consensus
vocabulary and inventing one means owning a definitional fight, and maintenance is the actual
project with a silent failure mode — and raised the consumer fork (Hill staffer / funder /
Canary coalition-building) as the thing that determines what gets built. Dan did not answer the
consumer question this session.

Second, Dan asked for ControlAI's LessWrong writeups on briefing UK parliamentarians. Found two,
both by Leticia García Martínez, plus a third-party evaluation on the EA Forum. Dan's recalled
figure ("500 MPs") does not match anything published; the UK campaign is ~150-160 meetings, and
the 200+ number is cross-jurisdiction lawmakers briefed across UK/US/Canada/Germany.

## Topics Explored

- Existing AI-policy / AI-safety landscape maps and their axes; whether the Group x Problem x
  Approach schema is already occupied
- Design constraints on building one: taxonomy vocabulary, maintenance mechanism, differentiation
  against an incumbent that launched three months ago
- ControlAI's published parliamentary-outreach learnings and the independent evaluation of them

## Provisional Findings

- The Group x Problem x Approach cell appears genuinely empty; every existing map drops one axis.
  Emptiness is not by itself the argument for filling it.
- Nearest structural precedent is IAPS arXiv 2409.07878 — it demonstrates the gap-finding payoff
  ("nobody is working on X") that makes this class of map useful to funders, but is scoped to 3
  companies with a July 2024 cutoff.
- Mapping AI (aimapping.org) is the live incumbent for a general US AI-policy actor map. A
  general-purpose competitor looks unwinnable; a differentiated slice may not be.
- **ControlAI writeups** (relevant as the only published cold-outreach base rate from an org in
  Canary's position):
  - "What We Learned from Briefing 70+ Lawmakers on the Threat from AI", May 2025 —
    `lesswrong.com/posts/Xwrajm92fdjd7cqnN/...`. Late 2024 to mid-May 2025; 70+ cross-party UK
    parliamentarians plus 8 staffer-only meetings. Author calls this the core-insights post.
  - "What We Learned from Briefing 140+ Lawmakers on the Threat from AI", Feb 2026 —
    `lesswrong.com/posts/A7BtBD9BAfK2kKSEr/...`. From Sept 2024; 140 initial briefings, 126 direct
    to parliamentarians, 14 staffer-only. Composition 42% MPs / 35% Lords / 22% devolved.
    Explicitly an increment on the first post, not a replacement.
  - "How effective is ControlAI's parliamentary outreach?", Torchbearer, June 2026 (EA Forum) —
    125 cross-party signatories as of 2026-05-05 (93 Westminster roughly split Commons/Lords, 32
    devolved) from 160+ meetings, starting from zero contacts Dec 2024 with ~3 FTE UK policy
    advisors. Two Lords debates plus cross-party Commons amendment NC12 (March 2026). Benchmarked
    against 8 other UK advocacy campaigns.
  - **Conversion-rate caveat:** ControlAI's own framing is 1-in-3 briefed lawmakers taking a public
    stance; Torchbearer computes ~48.5% restricted to politicians not already supporting the cause.
    Different denominators, not a contradiction. The higher figure needs the caveat attached if it
    ever appears in a Canary document.
  - UK-to-US transfer is not clean: no constituency-service analogue to a Hill LA, much thinner
    staffer layer between advocate and member, different attention economy.

## Decisions Made

- No plan doc written; the project is pre-decision pending the consumer question.
- Convo logged under the `main` line (misc / cross-line), consistent with repo convention of
  date-prefixed convo filenames there.

## Results

- `results/20260811_actor_map_prior_art.md` — full prior-art inventory table, gap analysis, and
  the consumer fork

## Open Questions

- **Who is the map for?** Hill staffer (routing table), funder (gap analysis), or Canary
  coalition-building (legible artifact that generates inbound). Unanswered. Determines the artifact.
- Timing: stand this up now, or park until the FRONTIER comment window closes?
- If it graduates past brainstorm it should be its own research line, not `main`.
- Whether to ingest the ControlAI posts into `papers/`. They are advocacy writeups rather than
  research papers, so `add-paper` would route them to institutional protocol at best; a different
  home may be more appropriate. Not done.
- Possible third ControlAI post (their blog index shows an ambiguous April 2026 entry). Unverified.

## Session note — clock discrepancy

At session start the sandbox `date` returned 2026-07-30 and Claude reported that to Dan; the
platform context said 2026-08-11, and a later `date` call agreed with the platform. The earlier
report was wrong. All artifacts from this session are dated 2026-08-11. Worth watching whether
sandbox clock skew recurs, since the session-start `date` call is a standing instruction.
