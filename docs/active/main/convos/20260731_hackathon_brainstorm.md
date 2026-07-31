# 20260731_hackathon_brainstorm

**Date:** 2026-07-31
**Branch:** main
**Surface:** claude.ai

## Summary

Morning-of brainstorm for the FAI + IFP "Hacking the Think Tank" hackathon (today, 2026-07-31, FAI HQ, day-long, ends with public demo). Critical reframe from Dan mid-session: this is NOT an AI-policy hackathon — it's a hackathon about *using AI to move think tanks* (organizers' triptych: policy ideation, formation, advocacy). Tools must read as domain-agnostic think-tank workflow; AI bills survive only as demo material.

Dan's actual goal: employment networking. The project is a pretext; conversations are the product. Strategy: pitch at team formation, recruit 2-3 technologists, hand them the scaffold, circulate. Dan's personal pitch under the reframe: he already *operates* an AI-native think tank — Canary is a staff-of-one shop where AI is the research department, and the GAAIA/FRONTIER sprint is the case study. "I'm not speculating about the future think tank, I'm operating one."

Evaluated 7 candidate projects (3 from Opus, 4 from Fable). Key unlock: `pat-helper` (Dan's PAT-derived multi-model review pipeline, arXiv 2606.28277) is a generic engine — parallel lenses, mechanical quote-grounding against source, cross-model adversarial verification, severity-ranked synthesis. It's ~70% of both claim-audit and bill-lint; the day's build is "new lens pack + ingestion adapter," not "build a pipeline."

## The pitch (for slide generation)

**Umbrella: "The verification stack for the AI-era think tank."** Everyone at this event will build generators; policy work run on AI needs a QA layer. Sensors before engines (answers organizers' self-driving framing). Four modules, one engine (pat-helper):

1. **Bill pipeline** (formation): ingest bill → parallel section analysis → tiered findings (drafting bugs / cheap asks / substantive asks) → comment letter → outreach targets. Credibility garnish: 7 pre-verified drafting bugs in the FRONTIER Act (introduced last week) — § 131 fine inversion (AI fraud defendants face LOWER max fine than base offense), stale EO 14110 ref, § 253(f)(2) cross-ref bug, 24-hr routing bug surviving verbatim GAAIA § 111(g)(2) → FRONTIER § 4(h)(2), etc. Framing: "this took me two weeks with AI in the loop; today we make it an afternoon."
2. **Semantic bill diff** (formation; rider on module 1, shared ingestion): discussion draft vs. introduced text at the level of "all sunsets removed, whistleblower title dropped, new emergency-orders authority," not line noise. FRONTIER_VS_GAAIA.md is the proof of concept — its findings invalidated Canary's own published blog framing, which is the one-liner for why the tool matters. Congress's internal comparative prints are clunky and access-limited; nothing public does semantic diffing.
3. **Claim-audit** (verification): extract every factual/quantitative claim from a memo, per-claim provenance verdict: sourced / unsourced / contradicted / unverifiable-in-principle. Honest one-day fidelity: sourced/unsourced/unverifiable; live "contradicted" needs external retrieval and is the on-stage hallucination risk. Demo targets chosen to avoid dunking on the room: (a) AI-generated memo, produced live, bleeds red; (b) Dan's own published Canary post (the honesty move). Do NOT run it on a real third-party think tank product in that room.
4. **Kent-o-meter** (calibration; Dan's rescue of Opus's dismissed idea): extract estimative-probability phrases ("likely," "almost certainly," "could") from any report; map each onto empirical perception distributions (Zonination survey data, `probly.csv`, fetched); render per-claim violin plots; vagueness + unfalsifiability score. Critiques a convention, not an org's honesty — non-hostile, funny, best visuals of the slate. Brand fit: physicist walks into DC and demands error bars. Optional garnish: half-dozen hand-scored resolved pre-2024 think-tank predictions, one slide.

**Cut:** synthetic-comment detection (ground-truth problem; a one-day detector invites "how do you know it works" and the honest answer is "I don't"). Staffer routing (advocacy register, weak demo) and adversarial memo review (unverifiable on stage) also dropped for today.

**Solo fallback priority:** bill pipeline + Kent-o-meter; claim-audit shrinks to the AI-memo demo only.

## Decisions Made

- Umbrella pitch = verification stack; pat-helper is the shared engine, extracted with attribution into a fresh public hackathon repo (NOT flipping pat-helper public) — default pending Dan's confirmation.
- IFP/FAI's own pubs go in the Kent-o-meter corpus but are not the default demo target — default pending Dan's confirmation.
- Demo bills come from fresh official-source fetches (policy-levers copies can't ship — repo is private, CRM adjacency); plus 1-2 never-touched AI bills as honest live targets.
- Sandbox has no API keys: Fable builds/commits, live runs happen at the event on Dan's keys (pat-helper `.env`) or teammates' machines.
- Build structured as small resumable milestones committed to the hackathon repo (sandbox resets + usage-limit insurance); zip export as backup.

## Results

- `/home/claude/hackathon/data/probly.csv` fetched (Zonination perception data, 47 lines) — sandbox-local, will land in hackathon repo, not here.

## Open Questions

- **BLOCKING:** hackathon repo + write-scoped PAT from Dan (Fable's PAT reaches only policy-levers), or "tarball mode."
- Dan's laptop: pat-helper `.env` keys + `uv sync` + charger.
- Confirm the two defaults above.
- Team formation: which modules get handed to recruited technologists.
