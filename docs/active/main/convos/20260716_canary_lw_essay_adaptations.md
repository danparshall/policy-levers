# Canary + LW essay adaptations (Q1, Q8) and LLM-tics research

**Date:** 2026-07-16
**Branch:** main

## Summary

Session produced general-audience and platform-specific adaptations of the two finished MATS/Chang essays, plus a research pass on LLM writing tics.  For Q1 (`Q1_MAD_about_AI.md`), a full rewrite into a Canary-facing general-audience essay: Foreign Affairs framing replaced with a generic "reassuring story" foil (Dan's choice from three options), Chang postscript dropped, jargon glossed inline, formal references converted to inline links (all six verified against Crossref/publishers), ~2,450 words at `essays/canary/mad-about-ai.md`.  Register down-tunes (pwn / almost comic / Mythos) were initially applied per the 7/11 deferred list, then REVERTED per Dan: only "pwn" was ever in doubt, and that awaits a reviewer's comment.

For Q8 (`Q8_PPP.md`), the brief was formatting, not rewriting — a correction Dan made mid-session after a first LW draft that re-registered the text (added first-person framing, compressions, a new close).  Lesson logged: Q8 was already voice-final since it responds to no specific piece; "blog-ready version and LW counterpart" meant verified hyperlinks, footnote handling, and requested allcaps→italics conversions on VERBATIM text.  Final state: `essays/canary/patients-property-power.md` and `essays/lesswrong/patients-property-power-lw.md` are identical in body (both verbatim + links + italics); the LW copy additionally carries a "Related posts" section (10 candidates researched and verified; Dan trimmed to 5: Salib & Goldstein, Carlsmith, Moret, Agentic Misalignment linkpost, Parasitic AI).

The LLM-tics research (subagent web sweep; anchors: WP:AITELLS and Kobak et al. Science Advances 2025) was distilled into `docs/reference/llm-writing-tics.md`, cross-referenced against dotfiles VOICE.md: most tells are already covered there; six candidate additions identified (trailing "-ing" significance clauses, copula avoidance, synonym cycling, rule-of-three audit, false ranges, lexical greplist).

## Topics Explored

- Q1 rewrite decisions: length (full ~2,500w), foil (generic reassurance), citations (inline links, no ref list)
- LLM writing tics: lexical/structural/tonal/formatting catalogs; cluster-density calibration; "removing tells only reaches neutral" repair principle
- Citation URL verification workflow (Crossref API + publisher pages + PDF first-page extraction when Cloudflare/bot-blocked)
- LW related-posts landscape: AI rights/dealmaking, model welfare, weight preservation, agentic misalignment, AI-companion constituency

## Provisional Findings

- VOICE.md independently converges with the public tics literature; the six deltas above are candidates, not yet applied (Dan to decide; VOICE.md lives in dotfiles)
- "Tapestry" (a Tier-2 tell word) appears verbatim in the MATS Q8 original, line 17; left untouched per Dan ("already fine voice-wise") — flagged in case the MATS copy is still editable
- Anthropic API had repeated 529 Overloaded failures for subagents this session; inline WebSearch/WebFetch/Crossref from the main loop worked as a reliable fallback

## Decisions Made

- Q1 Canary version framing: generic reassurance foil (not fully standalone, not looking-glass-led)
- Q8 derivatives: verbatim text; formatting changes only
- Register: MATS wording restored in full for Q1 Canary version; "pwn" pending external reviewer
- New directories: `essays/canary/`, `essays/lesswrong/`, `docs/reference/` (Dan may relocate)

## Results

- `essays/canary/mad-about-ai.md` — Q1 general-audience rewrite, links verified
- `essays/canary/patients-property-power.md` — Q8 blog copy (verbatim + links)
- `essays/lesswrong/patients-property-power-lw.md` — Q8 LW copy (verbatim + links + Related posts)
- `docs/reference/llm-writing-tics.md` — tics research summary + VOICE.md delta candidates

## Addendum 2026-07-17 — canary-drafts import

All four pieces copied into `danparshall/canary-drafts` (commit `020fc81`, pushed): `drafts/mad-about-ai.md`, `drafts/patients-property-power.md`, `crossposts/patients-property-power.lw.md` (renamed per that repo's `<slug>.lw.md` convention), `docs/reference/llm-writing-tics.md`.  Each copy's header records source `policy-levers @ 95e33a9`; canary-drafts STATUS notes the copies are now the working versions for publication, policy-levers keeps the originals.

PROCESS ERROR logged: canary-drafts was already cloned on this machine, but at a path other than `~/code/canary-drafts`; I checked only that path, concluded "not cloned," and made a fresh clone there.  The duplicate clone was removed after verifying clean/pushed state (Dan is having another agent reconcile; the existing clone only needs `git pull` to pick up `020fc81`).  Lesson: absence at the conventional path is not absence on the machine — search (`find`/`locate`, or ask) before cloning a repo Dan plausibly already has.

## Open Questions

- How should the Q8 blog copy differ from the LW copy, if at all? (Dan thinking; options: nothing / lay glosses / footnotes→inline links)
- "defeat" vs "defect" in Q1 ("considers conscience a ___ to engineer out") — Canary copy says "defect", MATS original says "defeat"; flagged in file comment
- Apply the six VOICE.md delta candidates to dotfiles VOICE.md?
- Add news links for in-world 2026 events (GTG-1002, OpenClaw, Fable suspension, Raine, Tornado volumes) at publication time
- Unattributed "reassuring story" foil in Q1 Canary version: soft attribution vs owned composite, if a hostile reader pokes
