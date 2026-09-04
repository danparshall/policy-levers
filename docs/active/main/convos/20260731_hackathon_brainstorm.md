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

---

## Session addendum: team-formation deck build (morning, pre-event)

**Machine:** Dans-MacBook-Air

Built the team-formation stand-up pitch deck at `hackathon/team-formation-pitch.html` (untracked at the time, committed 2026-09-04). Format decisions locked before writing:

- **Deck target:** team-formation pitch (not end-of-day demo) — recruit 2–3 collaborators; employment-networking is the real product per morning brainstorm.
- **Format:** stand-up pitch to whole room, ~60–90s, projected, 4 slides, high-contrast dark theme with green accents (fits "physicist walks into DC and demands error bars" tone).
- **Hook:** "sensors before engines" (echoes organizers' self-driving triptych; ties to the umbrella pitch).
- **Slide structure:**
  1. Cover — big title, tagline, event kicker.
  2. Four modules, one engine — 2×2 grid (Bill pipeline / Semantic bill diff / Claim-audit / Kent-o-meter) + engine badge (pat-helper, arXiv 2606.28277).
  3. The receipt — "7 drafting bugs found solo, with AI in the loop, in two weeks" + 4 sample bugs (§ 131 fine inversion, § 4(h)(2) 24-hr routing survivor, § 421 stale EO 14110, § 253(f)(2) cross-ref) + punchline callout: *"I'm not speculating about the AI-native think tank. I operate one."*
  4. Come find me — 3 role slots (Ingestion & retrieval / Frontend & viz / Domain reviewer, "nontechnical welcome" hedge) + dashed-border contact block. "Created with Nori Agentic" small-tag bottom-left per creating-slides skill.

Design calls made without asking (recorded here for future context): punchline placed on slide 3 tied to the receipt (not slide 4); CTA is 3 specific role buckets, not open enthusiasm; FRONTIER samples pick funniest/most concrete 4 of the 7 bugs with fine inversion first for the laugh; "Domain reviewer — nontechnical welcome" hedges against a policy-heavy room.

## Outcome (post-event)

Deck was **not used**. At the event Dan pivoted from pitching the verification stack to joining the **SlopChecker** team (funder-side submission screening; part of the IFP internal tool set). Same day, Dan contributed a Deep Research prior-art report for that team's actual feature list — see `results/20260731_slopchecker_prior_art.md` (commit `2b26378`, 14:09 UTC). Deep Research Run 1 targeted the verification-stack list reconstructed from the morning brainstorm because the agent couldn't open the SlopChecker team doc; Run 2 used the actual doc contents.

Deck preserved for design reference — dark-theme structure and stand-up 4-slide module-grid layout carry over to any future policy-tools pitch. Original "blocking" items in the Open Questions section (hackathon repo + PAT, pat-helper extraction defaults) are moot under the pivot.

## Tasks created

- [#6 Write up staffer-routing methodology; publish as standalone shareable repo](https://github.com/danparshall/policy-levers/issues/6) — for local agent; gift to Jackson (pitch-to-lawmaker matching). Open-ended, no date prefix.
