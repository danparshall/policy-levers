# Research Log — main (misc / cross-line sessions)

## Session: 2026-08-11 — policy_actor_map
### Topics Explored
- Whether a "Group X works on Problem Y via Approach Z" page already exists for AI policy; what a good one would need
- ControlAI's published UK parliamentary-outreach learnings (Dan recalled them as "500 MPs")

### Provisional Findings
- Target schema appears unoccupied, but every partial map drops a different axis: AISafety.com/map (group + area), Mapping AI / aimapping.org (group + stance, ~1,800 entries, launched ~May 2026 — the live incumbent), AGORA/CSET+MIT (documents + risk taxonomy, 1,000+ docs), IAPS arXiv 2409.07878 (problem + approach + group, but 3 labs and a Jul 2024 cutoff — closest precedent, and the one that demonstrates the gap-finding payoff).
- Two objections raised at full strength: (1) the "approach" axis has no consensus vocabulary — IAPS synthesized 7+ prior taxonomies into 11 categories and practitioners still disputed the labels; (2) maintenance is the actual project and its failure mode is silent, since a stale map launders obsolete info as current. Survivors have institutional funding or a community with a recruiting function; Canary has neither yet.
- Design forks on consumer (Hill staffer / funder / Canary coalition-building) — unanswered. Claude's read: the coalition framing argues for inverting the schema to index on problem and lever with groups as leaves.
- ControlAI: two LW posts by Leticia García Martínez ("70+", May 2025, `Xwrajm92fdjd7cqnN`; "140+", Feb 2026, `A7BtBD9BAfK2kKSEr`) plus a Torchbearer/EA Forum evaluation (June 2026). Dan's "500" doesn't match anything published — UK campaign is ~150-160 meetings; 200+ is the cross-jurisdiction total (UK/US/Canada/Germany). **Conversion-rate discrepancy to watch:** ControlAI says 1-in-3 briefed lawmakers take a public stance; Torchbearer computes ~48.5% restricted to prior non-supporters. Different denominators; the higher figure needs its caveat attached before it enters a Canary document.

### Results
- `results/20260811_actor_map_prior_art.md`

### Next Steps
- Answer the consumer question before any build; the artifact differs completely across the three
- Decide whether to park until the FRONTIER comment window closes
- If it proceeds, cut its own research line rather than continuing on `main`
- Decide whether/where the ControlAI posts get filed (advocacy writeups, not research papers — `add-paper` may be the wrong home)
- Verify the possible third ControlAI post (ambiguous April 2026 entry on their blog index)

See convo: `convos/20260811_policy_actor_map.md`

## Session: 2026-07-25 — frontier_port_and_iosco_ingest
### Topics Explored
- Diff between `essays/canary/frontier-act-tech-pace.md` (tracked) and `frontier-act-tech-pace_DAN.md` (added at `8958dfd` after typo-fix commits `b3cf522`/`37e4c68`); reconciling the fork
- IOSCO 2025 Consultation Report CR/01/2025 ingest — Cloudflare workaround, indexing, summary voice calibration

### Provisional Findings
- `_DAN.md` diff vs tracked was 13 lines, all regressions (unrendered SSI link stub + two typos: "The"→"This", "reates"→"creates"). Ported anyway per Dan's explicit direction after two rounds of flagging; commit `cebe179` documents the reversal in its message.
- IOSCO risk taxonomy (AMCC-ranked): malicious use > model/data > concentration & third-party > human-AI interaction. Regulatory-approach inventory splits members between existing-frameworks-adapted (HKMA/ESMA/CSA/CFTC) and bespoke (EU AI Act, Greek 4961/2022, Japan AI Guidelines, Brazil 2.338/2023, Canada AIDA, Australia). Engagement stats: 15/27 guidance issued; 6/27 sandboxes; 0/27 waivers.
- `iosco.org` is Cloudflare-fronted; direct curl returns block page regardless of User-Agent. Wayback Machine is the reliable fallback for IOSCO PDFs.
- Convention: `_DAN.md` sibling files are personal working drafts — do not assume they supersede the tracked file when the diff shows regressions; verify direction of "port" before executing.

### Results
- `essays/canary/frontier-act-tech-pace.md` (regressed to match `_DAN.md`, commit `cebe179`, pushed)
- `papers/IOSCO__2025--ai_in_capital_markets.pdf` (1.15 MB, from Wayback Machine)
- `papers/text/IOSCO__2025--ai_in_capital_markets.txt` (3,801 lines)
- Entries in `PAPER_INDEX.md` (Research Papers section) and `PAPER_SUMMARIES.md` (neutral paper-thrust register, no FRONTIER cross-references)

### Next Steps
- If Dan wants the two typo fixes and inline SSI link render re-applied on top of the ported text, that's a separate action
- Watch for IOSCO Phase-2 output per IOSCOPD789 workplan (Phase-1 is deliberately consensus-mode)

See convo: `convos/20260725_frontier_port_and_iosco_ingest.md`

## Session: 2026-07-16 — canary_lw_essay_adaptations
### Topics Explored
- Q1 general-audience rewrite for Canary (generic foil, inline links, jargon glosses); register revert per Dan
- Q8 blog + LW copies: verbatim text, verified hyperlinks, allcaps→italics; LW "Related posts" section (Dan trimmed 10→5)
- LLM writing tics research (WP:AITELLS, Kobak et al. 2025) cross-referenced against dotfiles VOICE.md

### Provisional Findings
- VOICE.md already covers most public tells; six candidate additions listed in `docs/reference/llm-writing-tics.md`
- Adaptation-mode lesson: essays with no named foil are voice-final; "make a version for X" means formatting, not re-registering

### Results
- `essays/canary/mad-about-ai.md`, `essays/canary/patients-property-power.md`, `essays/lesswrong/patients-property-power-lw.md`, `docs/reference/llm-writing-tics.md`

### Addendum 2026-07-17
- Four pieces imported to canary-drafts @ `020fc81` (now the publication working copies)
- Process error logged: duplicate clone made at `~/code/canary-drafts` (repo already cloned elsewhere on machine); removed after push; other agent reconciling

### Next Steps
- Dan: decide blog-vs-LW differentiation for Q8; defeat/defect call; VOICE.md delta; reviewer on "pwn"
- At publication: add news links for in-world 2026 events; consider soft attribution for the Q1 "reassuring story" foil

See convo: `convos/20260716_canary_lw_essay_adaptations.md`

## Session: 2026-07-31 — 20260731_hackathon_brainstorm
### Topics Explored
- Project slate for FAI+IFP "Hacking the Think Tank" hackathon (today): 3 Opus ideas + 4 Fable ideas evaluated
- Reframe: event is about AI moving *think tanks*, not AI policy; goal is employment networking, project is pretext
- pat-helper recognized as the generic engine (~70% of claim-audit AND bill-lint)

### Provisional Findings
- Winning pitch: "verification stack for the AI-era think tank" — bill pipeline + claim-audit + Kent-o-meter on the pat-helper spine
- Kent/Zonination calibration idea is demoable as a *language* tool (Opus dismissed the longitudinal version; the estimative-phrase mapper is a few hours)
- Synthetic-comment detection cut (ground-truth problem)
- Claim-audit demo must not target third-party think-tank products in that room (networking landmine); use AI-generated memo + Dan's own Canary post

### Results
- Full pitch structure in convo file (written for downstream slide-generating agent)

### Next Steps
- Dan: create public hackathon repo + write PAT (or tarball mode); confirm pat-helper-extract + hosts-in-corpus defaults; laptop keys
- Fable: bill fetches, corpus, sanitized scaffold, README-as-pitch, zip export

See convo: `convos/20260731_hackathon_brainstorm.md`
