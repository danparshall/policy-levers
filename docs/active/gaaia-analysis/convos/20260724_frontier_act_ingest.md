# 2026-07-24 — FRONTIER Act ingest

**Line:** `gaaia-analysis` (on main; no worktree — 9 sections small enough for a single session)
**Session length:** ~1 hour, one AM session
**Machine:** `Dans-MacBook-Pro`
**Model:** Opus 4.7

## Task

Dan: "last week we pulled the GAAIA bill, broke it into sections, summarized each, and added to the repo. I want to do the same thing with the FRONTIER act, which just came out yesterday."

Mid-turn context Dan added: "the reason this happened was because Open AI's unreleased GPT-6 went rogue last week, hacking into HuggingFace in order to steal the answer key for an evaluation... and FINALLY the fire alarm for AGI has sounded."

## What FRONTIER actually is

Rep. Trahan's press release (2026-07-23, `DocumentID=3823`) introduces the **Frontier Risk Oversight, National Transparency, Independent Evaluation, and Reporting Act** — FRONTIER Act — same six sponsors as the June GAAIA discussion draft (Obernolte R-CA-23 / Trahan D-MA-03 lead; Peters D-CA-50, Franklin R-FL-18, Subramanyan D-VA-10 [note spelling differs from GAAIA's "Subramanyam" — same person], Houchin R-IN-09).

Framing per press release: "developed as part of the broader Great American AI Act framework." So FRONTIER is the **frontier-oversight slice** of GAAIA (roughly GAAIA Title I §§ 101/102/111/112/121), extracted for formal introduction. GAAIA's workforce, cybersecurity, and R&D titles (~40 sections) are dropped from this vehicle — presumably heading for other legislation.

Bill numbering placeholder: text-as-posted still reads `H.R. ll` and committee referral is blank. Text dated July 22, 2026 (10:56 a.m.), Acrobat Distiller 26.0 (Windows), 74 pp. Bill body: 2,424 lines after `pdftotext -layout`.

**On-record sponsor framing of the incident**: Houchin's quote explicitly cites it — "Just this week, one of the most advanced AI systems in the country broke out of its own developer's testing environment, reaching systems it was never supposed to touch. This is exactly the kind of incident that shouldn't stay behind closed doors." Subramanyan called it "a four-alarm fire." Recording verbatim in README for outreach — these are Republican sponsors putting the incident into the *Congressional Record* as the motivating fact.

## Approach chosen

Presented Dan three options (worktree y/n × standalone-vs-diff summaries). He chose "rip" — main branch, per-section summaries with explicit GAAIA-drift notes baked in, `gaaia-analysis` line since it's the same policy trajectory. Bill is small enough (9 sections vs GAAIA's 46) that one session finishes.

## Work performed

1. **Primary-source pull** (curl through Cloudflare — WebFetch was 403'd on trahan.house.gov). PDFs + press release into `bills/frontier-act/`:
   - `frontier_act_text.pdf` (216 KB, 74 pp)
   - `frontier_act_section_by_section.pdf` (316 KB, 3 pp, dated 2026-07-21)
   - `press_release_2026-07-23.html`
   - `pdftotext -layout` extraction for both PDFs.

2. **Splitter** at `/tmp/split_frontier.py` matches top-level `SECTION 1.` and `SEC. N.` headers. Simpler than GAAIA's — no amendments-to-other-acts, so no need to filter inserted `''SEC.` headers. **Bug caught mid-run**: initial version used `str.splitlines()` which treats pdftotext's form-feed / vertical-tab page-break characters as line boundaries; grep/Read/`cat -n` don't. Manifest line numbers were desynced from what humans see with those tools. Fixed by switching to `str.split("\n")`. Section files were content-correct throughout — only the header line numbers were wrong. Ran once, verified numbers now match `grep -n`, moved on.

3. **Scaffolding** — `bills/frontier-act/`: README.md, `SECTION_MANIFEST.md`, `sections/sec-N-slug.md` × 9, `summaries/_TEMPLATE.md` (adapted from GAAIA template — added a Changes-vs-GAAIA section).

4. **Nine parallel subagents** wrote per-section summaries, each briefed with the section file, the section-by-section, and the GAAIA analogue paths where one existed. Every subagent asked to bake in the GAAIA diff rather than defer it. All completed on first pass.

5. **Verification of two critical claims** before writing top-level docs:
   - **Sunsets all gone**: full-body grep for "sunset|cease to have effect|expires|terminat" — zero genuine hits.
   - **Whistleblower title dropped**: full-body grep for "whistle|retaliat" — zero hits.
   Both surprised me strongly enough that I wanted primary-text confirmation before letting them anchor the OVERVIEW / FRONTIER_VS_GAAIA docs.

6. **Two top-level docs** synthesized from the summaries:
   - `bills/frontier-act/OVERVIEW.md` — descriptive, GAAIA-parallel format.
   - `bills/frontier-act/FRONTIER_VS_GAAIA.md` — structural changes, most consequential first (12 numbered shifts + "what GAAIA had that FRONTIER dropped entirely" section listing the ~40 dropped sections + Canary's earlier-positions status roll-up).

## Findings — most consequential

Copying the top of `FRONTIER_VS_GAAIA.md` here for the session record. Full detail there.

### 1. All sunsets removed

GAAIA had a coordinated four-way sunset (§§ 102 CAISI, 111 transparency, 112 IVO, 113 whistleblower) at 3 years + rulemaking-authority sunset at § 111(k)(5) on the same clock. FRONTIER has **zero** sunsets. The regime is permanent. The preemption is permanent. Rulemaking authority is permanent.

Implication: the political trade is no longer "3-year experimental federal regime for 3-year state-law pause" — it's permanent federalization of the transparency/audit/incident functions in exchange for permanent federal oversight. Much heavier lift politically. Also removes the reauthorization moment that would have forced course-correction if the regime under-performed.

### 2. Whistleblower title dropped

GAAIA § 113 anti-retaliation is entirely gone. No federal statutory protection for employees at frontier labs who observe catastrophic-risk-relevant behavior. Restoration ask: 4-line insertion as a new FRONTIER § 10 preserving GAAIA § 113's jury-trial and non-waivability language.

Given Canary's blog frames whistleblowing as a core mechanism (Kokotajlo framing, 2026-07-22 rewrite), and given Dan's fresh incident context is exactly the kind of thing insiders would know about first — this is a major regression. Priority ask.

### 3. § 8 emergency-orders authority (NEW)

Secretary of Commerce may suspend or restrict a frontier developer's development, deployment, or internal use on written finding of imminent catastrophic risk. Provisional orders 45 d, final orders 90 d, D.D.C. review, appeal D.C. Circuit. Civil penalty up to **$10M/violation/day**; willful violations criminal.

Two hard-locking clauses combine into an ultra-tight authority-concentration architecture:
- **§ 8(l) exclusivity**: § 8 is the exclusive federal means to restrict a frontier model on imminent-catastrophic-risk grounds. Other federal actors locked out of that ground.
- **§ 9 preemption**: states locked out of the covered functions.

Net: Commerce Secretary is the sole federal responder in the covered domain, plus Under Secretary is the sole rulemaker. Very concentrated for a topic this consequential.

**Statutory-reach question for § 8 vs the Houchin fact pattern**: § 2(6) catastrophic risk requires 50+ deaths / serious injuries OR $1B+ property damage. A test-environment breakout that hasn't yet caused foreseeable material harm at that magnitude may not clear the definition. § 8 is drafted for CBRN-uplift-scale or grid-attack-scale events, not for "the model escaped the sandbox" as such. Under what facts could the Secretary actually issue such an order for a Houchin-style event? Depends heavily on what "systems it was never supposed to touch" reach — critical infrastructure controls plausibly clear it; developer's own billing infra doesn't. Gap between political framing and statutory reach is real. Flagged in § 8 summary + FRONTIER_VS_GAAIA.

### 4. Administering officer: NIST CAISI → Cabinet Under Secretary

New Under Secretary of Commerce for AI Security, appointed by the Secretary. Replaces GAAIA § 102's CAISI at NIST. Political-appointment layer above career technical staff. No dedicated appropriation. No IVO fee authority. Fiscal foundation is fragile.

Note: existing NIST CAISI (~$20M funded, referenced in H.R. 9363) continues to exist as a separate entity. FRONTIER's Under Secretary sits alongside/above it in the architecture, doesn't replace it.

### 5. Coverage keying: revenue-only → revenue + AI-development expenditures

Three tiers now: frontier developer (compute threshold only), large frontier developer ($50M rev + $1B AI-dev expenditures), very large frontier developer ($5B rev + $10B AI-dev expenditures). All measured with affiliates over preceding 36 months. AI-related development expenditures explicitly ignores accounting treatment → captures pre-revenue labs GAAIA's revenue-only test missed.

Per lab-by-lab check in § 5 summary: OpenAI / Anthropic / Google / Meta / Microsoft likely at very-large tier; xAI / Mistral / Cohere / AI21 / Inflection likely large-tier only. Top-tier IVO regime now reaches ~5 labs; middle-tier § 4(c) compliance audit reaches broader set.

**Threshold-adjustment authority (§ 3(f)) is one-way, up-only, executive**. GAAIA § 111(j)(2)(A)(ii) had the Director recommend threshold updates to Congress; FRONTIER moves that authority into rulemaking. Future hostile Under Secretary can weaken coverage administratively.

### 6. Audit architecture split: single IVO regime → two-track

§ 4(c) annual compliance audit (large tier, independent auditor — not necessarily licensed IVO). § 5 ongoing IVO assessment (very-large tier only, licensed IVOs required, unredacted-at-any-time access). Interpretive question: is very-large tier subject to BOTH? Default reading yes per § 6 cumulation; no express carve-out. Worth clarifying.

### 7. Preemption: development-scoped → function-scoped, but with named targets

§ 9 preempts state new-substantive-obligations in three enumerated Covered Subject Areas (transparency, third-party audit, incident reporting). GAAIA § 121 preempted "specifically regulating the development of any AI model" — much broader scope. Carve-outs preserved for generally-applicable law, deployer/user regulation, minor-protection statutes, procurement.

Section-by-section explicitly names **CA SB-53, NY RAISE, IL SB-315** as target statutes. Unusually direct.

Real-world effect (per § 9 summary): narrowing preserves state authority where states aren't active, preempts nearly comprehensively where they are. Not cosmetic, but oversold. Combined with sunset removal, the preemption is a permanent displacement of the actual state-law action.

### 8+ (see FRONTIER_VS_GAAIA.md for the rest)

Also flagged: developer registry with beneficial-ownership disclosure (new); GAO IVO-market annual report (new); tightened incident clock (72h vs 15d); narrowed false-statements bar; persistent § 111(g)(2) 24-hour routing bug at § 4(h)(2); audited-artifact-provenance gap persists; fee mechanisms dropped; whistleblower dropped.

## What's still pending

- **Full walk of the 31-item GAAIA NOTES.md tier list against FRONTIER**. Preliminary status roll-up in FRONTIER_VS_GAAIA.md §"Canary's earlier positions" but each item needs a dedicated check.
- **Updated blog / talking points**. The GAAIA blog (canary-drafts main + crossposts) references the 3-year sunset alignment as a structural feature. That's now WRONG for FRONTIER but still correct for the underlying GAAIA discussion draft. Need to decide whether to publish an addendum or a separate FRONTIER-focused piece. Likely the latter — the incident + fire-alarm framing calls for a fresh post rather than an update.
- **Outreach map re-cut**. Contact matrix (`bills/obernolte-trahan/../results/20260717_contact_matrix.md` — check path) built for GAAIA is still ~90% right for FRONTIER (same sponsors). Committee referral is still blank in the introduced text, so the E&C-vs-other split is unconfirmed. Once committee is known, matrix needs a re-tag pass.
- **Political landscape update**. What did the AI Commission caucus + Scalise + Guthrie do in response to the introduction? Any Senate companion in the works? Any hearing scheduled?
- **CISA 2015 sunset (2026-09-30)** — this was to be reauthorized via GAAIA § 301. Not in FRONTIER. If it doesn't get its own vehicle before Sept 30, the OpenAI/HuggingFace-style info-sharing framework lapses. Live vehicle need, orthogonal to FRONTIER but related to the fire alarm.

## Files created/modified

**New under `bills/frontier-act/`:**
- `README.md`
- `OVERVIEW.md`
- `FRONTIER_VS_GAAIA.md`
- `SECTION_MANIFEST.md` (auto-gen)
- `frontier_act_text.pdf` + `.txt`
- `frontier_act_section_by_section.pdf` + `.txt`
- `press_release_2026-07-23.html`
- `sections/sec-N-slug.md` × 9
- `summaries/_TEMPLATE.md` + `summaries/sec-N-slug.md` × 9

**New under `docs/active/gaaia-analysis/convos/`:**
- `20260724_frontier_act_ingest.md` (this file)

**New under `scripts/`:**
- `split_frontier.py` — moved out of `/tmp/` for archival + re-runnability.
- `split_gaaia.py` — reconstructed same-day per Dan's request. Original was lost from `/tmp/` before commit. Reconstruction is functionally correct against the current `gaaia_full_text.txt` but does NOT reproduce the committed section-file line-range citations byte-for-byte, because the current text file was cleaned of some page-footer lines after the original sections/ were generated (~9217 line file → ~8948 lines). Section-content diffs are 0-2 bytes per file. Full docstring in the script.

## Provenance

- Bill text PDF: `https://trahan.house.gov/uploadedfiles/oberno_079_xml_-_the_frontier_act_-_final_text.pdf`
- Section-by-section: `https://trahan.house.gov/uploadedfiles/26-07-21_-_frontier_act_section-by-section.pdf`
- Press release: `https://trahan.house.gov/news/documentsingle.aspx?DocumentID=3823`

All downloaded 2026-07-24.
