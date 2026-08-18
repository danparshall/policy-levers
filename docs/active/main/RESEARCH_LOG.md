# Research Log — main (misc / cross-line sessions)

## Session: 2026-08-17 — watcher_notify
### Topics Explored
- Health check on the 2026-08-15/16/17 leg-watcher digests (18 sources, `consecutive_failures=0` across the board, 215 UIDs seen in the API poller; only 8/15 surfaced any items — the 8/17 pro forma notice, exactly what senate-daily-schedule was enabled for; 8/16 and 8/17 both empty).
- Whether launchd → digest-file has any push component (it doesn't — tool is fundamentally pull-shaped for a use case that's push-shaped).
- Notification transport tradeoffs (macOS Notification Center vs `open`-file vs email vs Slack vs GH Issue vs private-branch commit); Gmail SMTP won on reach × complexity × phone-accessibility.
- Idempotency key design given `write_digest`'s "Later run" mid-day append behaviour (content-hash keyed on `(digest_filename, sha256(text))` beats date-only).

### Provisional Findings
- **Watcher is healthy but silent.** All 18 sources fetching cleanly, digests landing on disk; no signal path to Dan. Fixed in-session.
- **Recess-week emptiness is real, not broken.** 8/15 correctly caught the 8/17 pro forma 2 days ahead. Real content signal defers to ~Sep 2 when Congress returns.
- **Content-hash idempotency handles both cases correctly**: identical re-run = skip, appended new items via "Later run" = re-send with the full updated digest.
- **Multi-machine problem persists.** launchd only on the Air; if the Air is closed no digest for that day. Deferred — notification path is orthogonal.

### Results
- **PR #12** — <https://github.com/danparshall/policy-levers/pull/12> — merged as `28b23ab` with `71c8699` underneath.
- **New**: `src/watcher/notify.py` (166 LoC), `tests/test_notify.py` (12 tests). Total 108/108 green (was 96), ruff clean.
- **CLI**: `--no-notify`, `--notified-state-path`; new "Email notifications" section in `src/watcher/README.md`.
- **Follow-up**: `0a6db9c` chore(gitignore) — `.worktrees/` + `data/watcher-notified.json`.

### Next Steps
- Dan generates a Gmail app password (<https://myaccount.google.com/apppasswords>) and adds five `WATCHER_SMTP_*` / `WATCHER_NOTIFY_*` vars to `.env.local` to activate.
- Real send smoke: `uv run watcher --include-backlog 30 --sources rep-trahan-press` → verify email arrives → re-run → verify `notify: skipped:same-hash`.
- Snooze issue #7 (keyword retune, fires 2026-08-18) to ~2026-09-09 since we don't have a real week of digest signal yet.
- Close/snooze fired reminder #5 (FRONTIER outreach).

See convo: `convos/20260817_watcher_notify.md`


## Session: 2026-08-16 — covert_adversaries_treaty_verification
### Topics Explored
- Aumann–Lindell 2010 *Security Against Covert Adversaries* (J. Cryptol. 23:281–343) — paper landed at repo root; parallel `add-paper` agent handled integration (rename, extract, index, summarize); this session did analytical work only.
- Whether either author currently publishes on AI verification / treaty topics.
- Structure and definitional variants of the covert-adversary security model.
- Simulator-vs-adversary distinction in the ideal/real simulation paradigm (Dan asked directly).
- Mapping the covert-adversary framework onto AI-treaty verification and what "the simulator cheating" means operationally.

### Provisional Findings
- **Neither Lindell nor Yonatan Aumann currently publishes on AI treaty verification.** Lindell (Coinbase Chief Cryptographer) is in pure MPC / VRF / VSS work. Yonatan Aumann (Bar-Ilan Multi-Agent AI Group) works on mechanism design, coalition games, LLMs instructing multi-agent systems — thematically adjacent, not on treaties by name.
- **Yonatan Aumann is Robert Aumann's son.** Different person; the Aumann Agreement Theorem belongs to Robert. Worth flagging for citation hygiene.
- **The covert-adversary framing is being re-derived, uncredited, in the current AI-verification-of-treaties literature** — MIRI's Nov 2024 mechanisms paper, Baker et al. six-layers, Scher et al. verification methods, hardware-governance taxonomy. All frame the threat model as "state actor willing to spend billions to cheat but sensitive to being caught" — which is Aumann–Lindell's ε-deterrent covert adversary. None cite the 2010 paper. **Citation gap worth flagging.**
- **Definitional insight transfers cleanly; ideal/real machinery strains.** The "cheating detected with probability ≥ ε" frame + strong-explicit-cheat's "detection interrupts payoff" (Aumann–Lindell's *"less deterrence to not rob a bank if when you are caught you are allowed to keep the stolen money"*) map directly to escrow/kill-switch/forfeit treaty regimes. But F_treaty (ideal functionality) isn't well-specified in compute-trace terms; there are no "honest inputs" (treaty verification is unilateral observation, not joint computation); "cheating = not simulatable" needs relaxation for heterogeneous attestation + inspection + audit + intel stacks. Formalization gap → *paper-shaped*, not just brief-shaped.
- **Reframe worth pushing on policymakers:** *"confirm they aren't training X"* is impossible; *"make undetected training expected-loss-negative"* is the frame that admits mathematical shape. IAEA doesn't prove nobody's enriching — they make undetected enrichment probabilistically expensive. Covert-adversary framework is the vocabulary for making that shift precise.

### Results
None saved to `results/` — outputs are analytical text in the convo doc + the parallel agent's `PAPER_SUMMARIES.md` entry.

### Next Steps
- Dan handing off to a web agent to walk through the paper in detail — convo doc + PAPER_SUMMARIES entry are the context anchors.
- Consider: reach out to Yonatan Aumann? Multi-agent + mechanism-design + family game-theory pedigree = plausible collaborator on the formalization gap. Lindell is Coinbase-locked, lower leverage.
- If the citation-gap observation becomes public writeup material, save at `results/YYYYMMDD_covert_adversary_treaty_citation_gap.md`.

See convo: `convos/20260816_covert_adversaries_treaty_verification.md`


## Session: 2026-08-12 — ai_open_letters_inventory
### Topics Explored
- Which AI open letters exist beyond CAIS Global Statement + wemustactnow.ai + aitreaty.org (Dan's starting set); how many total; whether signatory documentation would be valuable for policymaker outreach
- Cross-category scope (all types), 2023-present, full signatory analysis with cross-letter overlap

### Provisional Findings
- **30+ distinct letters** March 2023 → July 2026 clustering into 9 categories (x-risk, governance, ethics/faith, labor, copyright, open-source, military, child safety, direct action) and five waves tied to focusing events (GPT-4, Bletchley Summit, SB 1047, UNGA, 2026 layoffs).
- **Super-signer spine**: Bengio, Hinton, Russell, Tegmark, Harari, Wozniak. Yann LeCun as the boundary marker — non-signer of x-risk letters, signer of We Must Act Now.
- **Contradictions**: Musk (Pause + xAI incorporation March 9, 2023 — sharpest), Altman/Amodei/Hassabis (CAIS but not Superintelligence), Mistral (Stop the Clock + GPAI Code), Acemoglu/Autor (We Must Act Now reversal after years of downplaying displacement).
- **Six flagship letters** for policymaker briefings: Pause (2023), CAIS Statement (2023), Right to Warn (2024), Global Call for AI Red Lines (2025), Statement on Superintelligence (2025), We Must Act Now (2026).
- **Signatory counts drift by source and date**: Pause 27,565 → 30,000+; Superintelligence 700+ launch → 32,214 late Oct 2025; Newton-Rex 11,500 → 19,000 → 50,000+. Every count needs its observation date.
- **Existing trackers close but not comprehensive**: AI Lab Watch open-letters list (best curated x-risk), FLI's own page (FLI-run only), Georgetown ETO AGORA (documents-focused, not letters). None is a cross-category signatory-level tracker — confirms the value of building one.
- **Gap topics with no flagship letter**: healthcare/clinical AI, journalism (lawsuits but no unified letter), education, environment/datacenter energy, financial-systems/systemic risk, Chinese-language domestic letters.
- **Red Lines near-term impact assessment** (Transformer News, Sept 2025): "unlikely to move the needle on concrete governance" due to US opposition (Cruz + Trump AI Action Plan). Caveat for Hill-facing use.

### Process Note
- Session-start protocol was **skipped** at the outset — deep-research task launched directly on Dan's ask without cloning policy-levers, reading RESEARCHER.md, STATUS.md, or personal_info.md. Recovered at finish-convo when Dan invoked task-create + finish-convo skills. Convo doc + results doc + RESEARCH_LOG entry backfilled at wrap. Lesson: a well-scoped research ask is not license to skip RESEARCHER.md. Reminder issue #11 was already filed via REST API (`[2026-08-19]` prefix) before the clone existed; back-link into the convo doc added on the same commit.

### Results
- `results/20260812_ai_open_letters_inventory.md`

### Captured Tasks
- [#11: Follow up on AI open letters tracker — re-scrape counts, check for new letters](https://github.com/danparshall/policy-levers/issues/11) — captured 2026-08-12

### Next Steps
- Re-scrape live signatory counts quarterly (Pause, Superintelligence, Red Lines, Newton-Rex, We Must Act Now all still open). Reminder #11 fires 2026-08-19.
- Verify uncorroborated specifics before publication (ERLC 2019 ~65–70, We Must Act Now 1,649, Superintelligence totals beyond 32,214, March 2026 "Pro-Human AI" declaration).
- Decide: own research line (branch, ongoing tracker) or landscape doc on main with periodic re-scrape?

See convo: `convos/20260812_ai_open_letters_inventory.md`


## Session: 2026-08-11 — policy_actor_map


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
- `results/20260731_slopchecker_prior_art.md` — deep-research prior-art / landscape report for funder-side submission screening (Run 2, using actual team-doc contents; Run 1 targeted the wrong feature list)

### Next Steps
- Dan: create public hackathon repo + write PAT (or tarball mode); confirm pat-helper-extract + hosts-in-corpus defaults; laptop keys
- Fable: bill fetches, corpus, sanitized scaffold, README-as-pitch, zip export

See convo: `convos/20260731_hackathon_brainstorm.md`

## Session: 2026-07-30 — policy_actor_map

### Topics Explored
- Whether a "Group X works on Problem Y via Approach Z" page already exists for AI policy; what a good one would need
- ControlAI's published UK parliamentary-outreach learnings (Dan recalled them as "500 MPs")

### Provisional Findings
- Target schema appears unoccupied, but every partial map drops a different axis: AISafety.com/map (group + area), Mapping AI / aimapping.org (group + stance, ~1,800 entries, launched ~May 2026 — the live incumbent), AGORA/CSET+MIT (documents + risk taxonomy, 1,000+ docs), IAPS arXiv 2409.07878 (problem + approach + group, but 3 labs and a Jul 2024 cutoff — closest precedent, and the one that demonstrates the gap-finding payoff).
- Two objections raised at full strength: (1) the "approach" axis has no consensus vocabulary — IAPS synthesized 7+ prior taxonomies into 11 categories and practitioners still disputed the labels; (2) maintenance is the actual project and its failure mode is silent, since a stale map launders obsolete info as current. Survivors have institutional funding or a community with a recruiting function; Canary has neither yet.
- Design forks on consumer (Hill staffer / funder / Canary coalition-building) — unanswered. Claude's read: the coalition framing argues for inverting the schema to index on problem and lever with groups as leaves.
- ControlAI: two LW posts by Leticia García Martínez ("70+", May 2025, `Xwrajm92fdjd7cqnN`; "140+", Feb 2026, `A7BtBD9BAfK2kKSEr`) plus a Torchbearer/EA Forum evaluation (June 2026). Dan's "500" doesn't match anything published — UK campaign is ~150-160 meetings; 200+ is the cross-jurisdiction total (UK/US/Canada/Germany). **Conversion-rate discrepancy to watch:** ControlAI says 1-in-3 briefed lawmakers take a public stance; Torchbearer computes ~48.5% restricted to prior non-supporters. Different denominators; the higher figure needs its caveat attached before it enters a Canary document.

### Results
- `results/20260730_actor_map_prior_art.md`

### Next Steps
- Answer the consumer question before any build; the artifact differs completely across the three
- Decide whether to park until the FRONTIER comment window closes
- If it proceeds, cut its own research line rather than continuing on `main`
- Decide whether/where the ControlAI posts get filed (advocacy writeups, not research papers — `add-paper` may be the wrong home)
- Verify the possible third ControlAI post (ambiguous April 2026 entry on their blog index)

See convo: `convos/20260730_policy_actor_map.md` (wrapped late, 2026-08-11)

## Session: 20260730T1749 — 20260730_lw_karma_baseline
*Substance took place 2026-07-30; session left open and wrapped 2026-08-12, so the commit date (`4f45fa6`, 08-12) trails the work by ~12 days. All karma/comment figures are a snapshot as of 2026-07-30 17:50 UTC.*

### Topics Explored
- Whether tools exist for LW posting-rate / karma-distribution reporting, and how scrapeable LW is
- LW public GraphQL API (`https://www.lesswrong.com/graphql`) — query shape, field semantics, rate tolerance
- 12-month baseline pull (2025-08-01→2026-07-30, n=7,429): posting rate, karma distribution, karma-vs-age, comment counts conditioned on karma
- Dan's own 5 substantive posts ranked against those baselines; comment-thread detail on the April economists post

### Provisional Findings
- **No scraping needed.** LW runs ForumMagnum with a public unauthenticated GraphQL endpoint; ~500 records/request in <1s, ~52 requests for a 12-month pull, no rate limiting hit. No maintained public dashboard for these stats was found, so a tool would be new but thin.
- **`filter: "all"` is mandatory** — the default `new` view silently drops ~10% of posts, mostly personal blogposts (107 vs 120 on a test week).
- Posting rate 20.5/day (monthly 16.4–30.5). Karma median 15, p90 80, p99 264, 3.8% end ≤0. Frontpage median 20 vs personal 6 (~3x for promotion).
- **`baseScore` is vote-weight-summed karma, not upvotes.** Dan's 11–30 karma posts have only 4–9 distinct voters.
- **Median karma is flat past ~3 days** ⇒ retrospective single-pull analysis is valid for ordinary posts; no prospective snapshotting needed. Does NOT extend to the tail — viral posts keep accruing and that shape is unrecoverable after the fact.
- **43% of mature LW posts get zero comments**; median is 1. Zero-comment rate ~50% at 10–15 karma, ~30% at 20–30.
- **Dan is at the median, not top-half:** median post 14 karma = 48.0th percentile sitewide, 57.6th vs low-frequency authors. n=5 with single-digit voter counts, so noise swamps 40th-vs-60th.
- **Economists post is the engagement outlier** (+4 comment residual; 5 comments where karma predicts 1). Two of three commenters engaged the same specific number ("less than a dozen economists"); one was academic economist Jakub Growiec. Hypothesis: a bounded contestable claim gives readers a flag to plant, accurate summaries don't. Heavily confounded (n=1, only post with a named foil, only one with a resident LW expert audience, 3 months older, frontpaged).
- **Both bill posts were personal-blog, not frontpaged** — plausibly costing more reach than any content variable measured.

### Corrections (Claude errors caught by Dan)
- Switched maturity cutoffs between messages (≥30d, max 833 → ≥14d, max 1038) without flagging it; Dan caught it via the 1038-karma DeepMind post. Pull was not lossy; near-median percentiles are insensitive (48.0 vs 48.4). Always state the cutoff alongside a distribution figure.
- Over-generalized a median result ("current score IS the two-week score") to a universal claim; false for the tail.
- Called zero comments "worse news than the karma" before checking the baseline. 43% of LW posts get zero comments; only proof-of-retention (30 karma, 0 comments) is actually anomalous.

### Results
- `results/20260730_lw_karma_comment_baselines.md`
- `results/20260730_lw_dan_post_performance.md`
- `scripts/lw_pull.py`

### Next Steps
- Resolve what LW is FOR in the portfolio before building anything. If it's a citable artifact for staffers, karma/comments are the wrong metrics entirely (want referral traffic, inbound links, citations); if it's standing with the safety research community, engagement is the right target.
- Tag-conditioned baseline (`ai-governance` / `ai-risk`) — offered, not run. This is the denominator that says whether bill analysis lands with people who read bill analysis.
- Implement comment residual (observed minus karma-bucket median) as the headline engagement metric.
- Check whether the bill posts were declined for frontpage or never submitted.
- Standing objection Dan hasn't answered: accurate bill summaries commoditize fast; the judgment layer in this repo (which of the 31 tiered asks matter, what Obernolte's office accepts, severability/NetChoice) is largely absent from the posts.

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

## Session: 2026-07-08 — zhou_adele_rename_and_paper_locations
### Topics Explored
- Paper naming maintenance: Zhou/ADeLe filename mismatch with naming spec (surname+initial required only where surname collisions likely; `OralloJ` was over-applied)
- Cross-repo audit of where IAISR reports and Shah 2025 AGI-safety paper live

### Provisional Findings
- Renamed Zhou/ADeLe paper (`OralloJ` → `Orallo`) in both `policy-levers` and `general-ai-abilities`
- IAISR reports confirmed live only on `general-ai-abilities` `origin/loc-abilities` branch (not main); Shah 2025 AGI-safety paper (arXiv 2504.01849) not yet in any repo

### Next Steps
- Backfill Shah 2025 into the appropriate repo when a session touches AGI-safety literature

See convo: `convos/20260708_zhou_adele_rename_and_paper_locations.md` — also cited in top-level `STATUS.md`.
