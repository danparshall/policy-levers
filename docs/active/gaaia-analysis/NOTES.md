# GAAIA comment-window notes — running list

Working list for the eventual comment to GAAIA@mail.house.gov. Three tiers: (1) drafting bugs, zero-cost to accept, credibility-builders; (2) cheap technical asks, small text changes with outsized effect; (3) substantive asks, where Canary has actual comparative advantage. Provenance: 2026-07-14 ingest session (46 per-section summaries) + walkthrough session with Dan. Body citations verified against `bills/obernolte-trahan/sections/` unless marked.

## Tier 1 — drafting bugs (technical corrections annex)

1. **§ 234 / § 403 bidirectional index errors.** § 234 (STEM Teacher Corps) appears in Trahan's section-by-section but not the bill body (likely collapsed into § 201's endorsement of the existing NSF pilot); § 403 appears in the body but not the section-by-section.
2. **§ 131 fine-increase scope.** Section-by-section claims across-the-board increases; body raises only mail (18 USC 1341) and wire (1343) base fines $1M→$2M.
3. **§ 131 inverted AI penalty.** AI-assisted mail/wire clause caps at $1M — *below* the newly raised $2M base. Read literally, using AI lowers the max fine. Presumably the AI clause predates the base-fine change; harmonize.
4. **§ 253(f)(2) cross-reference.** Cites "section 101" (Definitions); referent that fits the text (input on scored crowd-sourced forecasting best practices) is § 241.
5. **§ 255 deadline discrepancy.** Section-by-section says study *completed* within 12 months; body says Secretary "provide[s] for" the study within 12 months, publication at 24 (§ 255(b)). Cite the body.
6. **§ 247 survey count.** Section-by-section names four surveys; body names five — the omitted one (Business Trends and Outlook Survey) is the highest-frequency and the one Census actually uses for AI-adoption tracking.
7. **§ 111(g)(2) routing.** 24-hour imminent-risk reports go to "a law enforcement agency with jurisdiction," not CAISI; section-by-section says CAISI.
8. **§ 121 paraphrase drift.** Body: "specifically regulating"; section-by-section: "specifically targeting." Not identical scopes; the body's term is the operative one.
9. **§ 421 stale EO reference.** New § 5103A(c)(2) points at EO 14110, rescinded January 2025.

## Tier 2 — cheap technical asks

1. **§ 241(b)(2): strike the guardrail carve-out.** Composition (b)(1)(B) and viewpoint-diversity (b)(1)(C) requirements apply only to the first workshop; annual workshops are Secretary's-choice. Apply (B)–(C) to all workshops. Without this, the "critical evaluation of BLS assumptions" is self-graded after year one.
2. **§ 252: define "proper scoring rule" and lock the metric ex ante.** Term is used bare (§ 252(c)(1)(B)). Add a one-line definition (expected score optimized by truthful reporting, per the statistics literature) and require the chosen rule be published *before* the first forecast — closes the pick-your-metric-after-the-data hole. Also reconcile clause (ii): "aggregate calibration" is not what a proper scoring rule measures; specify a separate calibration diagnostic or fold it in deliberately.
3. **§ 244 ↔ § 252 designation lists.** Both require SecLabor to designate ≥15 AI-sensitive occupations every 2 years; nothing says they're the same list. Cross-reference them so the observed-transitions data (244) and the scored forecasts (252) cover the same occupations.
4. **§ 244: replicate § 252's machine-readable archive mandate.** Same agency ecosystem, same occupations; the asymmetry is presumably oversight.
5. **§ 245: define "reproducible."** Require open methodology, contamination-audit protocol, and public test-set governance; as written, a private test set held by the prize winner satisfies the text.
6. **§ 112: CAISI-conducted-audit fallback.** If no licensed IVO exists in a required risk domain, a large frontier developer is in structural noncompliance at $1M/day through no act of its own. Add a Director-conducted or provisionally-licensed audit path.
7. **§ 402: testbed cost-recovery waiver standards.** DOE full-cost-recovery default makes § 401 testbeds unaffordable for startups absent liberal Commerce waivers; specify waiver criteria.
8. **§ 423: NAIRR eligibility + resourcing.** Codified with donations-only funding (pilot needs ~$2.6B/6yr per Task Force estimate); private-sector eligibility (<7yr AND <500 employees) excludes every frontier developer from contributing compute through the front door. At minimum flag the eligibility screen as presumably unintended for *resource contributors* vs. resource *recipients*.

## Tier 3 — substantive asks (Canary comparative advantage)

1. **The zero-revenue frontier lab gap.** Frontier duties require 10^26 ops AND >$50M prior-year revenue (§ 101). A capital-rich, revenue-free lab (SSI-type) trains frontier models owing nothing under §§ 111–112 while § 121 bars states from touching it. Fix options: revenue OR capital-raised/compute-expenditure disjunct; or make the compute threshold alone sufficient for § 111(c)–(g) reporting duties (keeping the $500M tier for frameworks/audits). Strongest single substantive criticism; lead with it.
2. **Harm gate excludes bloodless power concentration.** § 101(6)(A) requires 50+ deaths/serious injuries or $1B+ damage; a successful AI-enabled seizure of power can involve neither. "Evading control" is a channel but must pass the gate. See `notes/20260714_coup_mitigation_mapping.md`. Minimal ask: exempt the evading-control channel from the death/damage gate, or add a power-concentration/critical-institution channel.
3. **Federal carve-out points backwards for state-actor risk.** § 101(6)(B) excludes "lawful activity of the Federal Government" — the buildup phase of executive misuse is mostly lawful until it isn't. Same note.
4. **Model-internals auditing absent.** § 112 audits frameworks and compliance, not models; no secret-loyalty/backdoor testing anywhere (interpretability only in § 422 prize priorities). Connect to loc-abilities line: what would an IVO actually test?
5. **Attribution methodology for § 251 / § 255.** WARN notices must state an AI-attribution percentage with no methodology constraint and adverse incentives; § 255's study menu never asks the counterfactual question (AI vs. cyclical vs. offshoring vs. ordinary tech churn). Ask: DOL guidance requirement with a safe-harbor methodology; add attribution to § 255(a)(2) explicitly.
6. **Wire measurement into decisions.** § 245 benchmarks → § 252 forecasts → § 254/§ 256 uses are all optional couplings ("consider," "report on"). Minimal hardening: require § 252 forecasts to incorporate or address § 245 benchmark results; require § 254 report to state incorporation decisions with justifications, not intentions.
7. **§ 252 sunset.** Forecasting obligation dies at 5 years just as the accuracy record matures; add a reauthorization trigger tied to the § 252(c) evaluation results (reuse the bill's own scored-forecast machinery as the renewal criterion).

## Structural observations (framing, not asks)

- **Labor vs. Commerce resourcing asymmetry.** CAISI: uncapped headcount, VP pay, fee authority. DOL: § 242 capped at 20 heads on $6M/5yr (funds ~5–6), § 243 Hub detail-only + zero-dollar, 4-year sunsets. The design is what the worried staff wanted; the budget is what the unworried members allowed.
- **Everything runs off the enactment clock.** Discussion draft, no number: § 241 RFC at 45 days, CAISI channels at 180, frameworks at 1 year, first § 252 forecasts ~2 years post-enactment. Optimistic passage in 2027 → first scored forecasts ~2030.
- **Sunsets as compromise instrument.** §§ 111/112/121 at 3 years (the core trade expires as a package); §§ 241/243/244/252 at 4–5. Reauthorization is the intended forcing function for the wiring Tier 3.6 asks for now.
- **§ 141 ↔ CAISI tension.** The jawboning study's definitions plausibly sweep CAISI-lab safety pressure; simultaneously, § 141 doubles as an anti-executive-aggrandizement record-builder (coup-note inversion). Watch how follow-on legislation scopes it.
