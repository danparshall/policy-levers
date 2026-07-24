# FRONTIER Act vs GAAIA discussion draft — structural changes

Canary Institute reference. Written 2026-07-24, one day after FRONTIER's introduction (2026-07-23). Compares FRONTIER Act (introduced) against GAAIA discussion draft (released 2026-06-04, 269 pp).

Section-level drift is documented in the per-section summaries (`summaries/sec-N-*.md`); this document is the cross-cutting structural diff. Where the per-summary and this doc disagree, the per-summary is closer to the primary text and controls.

## The one-paragraph diff

FRONTIER is the frontier-oversight slice of GAAIA (roughly GAAIA Title I §§ 101/102/111/112/121, plus a genuinely new emergency-orders authority § 8) — formally introduced under a new name after ~6 weeks of revision. The revision made the regime **more permanent** (all sunsets removed), **more concentrated** (Cabinet-level Under Secretary at Commerce replaces a NIST center; § 8 makes Commerce the exclusive federal responder on catastrophic-risk grounds; § 9 preempts states in the same functional space), **more sharply tiered** ("very large" tier added, coverage keyed to AI-development expenditures not just revenue), and **more surgical about preemption** (function-scoped rather than development-scoped, explicitly targeting CA SB-53 / NY RAISE / IL SB-315). The workforce, cybersecurity, and R&D titles that made up the bulk of GAAIA are dropped from this vehicle — presumably headed for other legislation. § 113 whistleblower protections are dropped without replacement.

## Structural shifts, most consequential first

### 1. All sunsets removed (SINGLE BIGGEST STRUCTURAL SHIFT)

GAAIA had a coordinated four-way sunset: §§ 102 (CAISI, via § 5304(i)), 111 (transparency), 112 (IVO), and 121 (preemption) all expired 3 years after enactment unless reauthorized. That structural feature was central to Canary's prior analysis — it forced Congress back to the table on both the obligations AND the preemption at the same time, so neither could be extended without the other.

**FRONTIER has no sunsets.** Full-text grep of the bill body for "sunset," "cease to have effect," "expires," "terminat" returns zero genuine hits. §§ 3, 4, 5, 8, 9 are all permanent. The preemption is permanent. The rulemaking authority is permanent (GAAIA § 111(k)(5) sunsetting rulemaking on the same clock is also gone).

Implication: the political trade in FRONTIER is **not** "3-year experimental federal regime traded against 3-year state-law pause." It is a permanent federalization of the transparency/audit/incident-reporting functions in exchange for permanent federal oversight of the largest labs. That is a much heavier lift politically. It also removes the natural reauthorization moment that would have forced course-correction if the regime under-performed.

### 2. Whistleblower protections dropped

GAAIA § 113 provided anti-retaliation protection for AI whistleblowers, with jury-trial rights and non-enforceability of rights waivers. Canary's prior work (Kokotajlo framing in the GAAIA blog rewrite, 2026-07-22) treated this as a core mechanism.

**FRONTIER has zero whistleblower provisions.** Full-text grep for "whistle," "retaliat," "§ 113" returns zero hits. Employees at frontier labs who witness catastrophic-risk-relevant behavior have no federal statutory protection under this bill.

If FRONTIER is intended to be the frontier-oversight vehicle going forward, whistleblower drop is a significant capability gap. Under the § 5 IVO regime, private-actor visibility into developer conduct depends on:
- Compliance audit (§ 4(c)) — the auditor is a private firm the developer picks and pays
- IVO assessment (§ 5) — the IVO is licensed by the Under Secretary but paid by the developer; regulatory-capture risk is documented at § 7
- IVO 72-hour Secretary referral (§ 5(p)(1)(B)) — but this only triggers on IVO-detected imminent risk

There is no channel for an *employee* who observes what the auditor and IVO miss.

Restoration ask: 4-line insertion of GAAIA § 113 as a new FRONTIER § 10, with the same jury-trial and non-waivability language.

### 3. § 8 emergency orders — genuinely new, structurally consequential

GAAIA had no emergency response authority. The regulatory teeth were ex-post civil penalties + IVO ongoing verification + framework-compliance obligations, with no way to actually stop a frontier developer from continuing to operate a model that had gone wrong.

**FRONTIER § 8 gives the Secretary of Commerce authority to suspend or restrict development, deployment, or internal use** of a frontier model on written finding of imminent catastrophic risk. Provisional orders (45 days, preliminary determination), final orders (90 days, requires written finding, renewable only on fresh finding), exclusive judicial review D.D.C., appeal D.C. Circuit. Civil penalty up to **$10M/violation/day** (10× the § 4/§ 5 penalty); willful violations criminal.

Two hard-locking clauses:

- **§ 8(l) exclusivity:** § 8 is "the exclusive means by which any federal actor may restrict a frontier model on imminent-catastrophic-risk grounds." No other federal agency (FTC, DOJ, FDA, DOD, CISA under its own authorities…) can act on catastrophic-risk grounds unilaterally.
- **§ 9 preemption** locks states out of the same functional space.

Combined: Commerce is the only responder in the covered domain. That is a huge concentration of authority in one Cabinet officer.

The gap between § 8's political framing (Houchin: "one of the most advanced AI systems … broke out of its own developer's testing environment"; Subramanyam: "four-alarm fire") and its statutory reach: § 2(6) catastrophic-risk requires 50+ deaths / serious injuries OR $1B+ in property damage. A test-environment breakout that hasn't yet caused foreseeable material harm at that magnitude may not clear the definition. § 8 is drafted for CBRN-uplift-scale or grid-attack-scale events, not for "the model escaped the sandbox" as such. See `summaries/sec-8-*.md` for the full analysis of whether § 8 would actually reach the Houchin fact pattern.

### 4. Administering officer: NIST Center → Cabinet Under Secretary

GAAIA § 102 established the Center for AI Standards and Innovation (CAISI) at Commerce/NIST, with critical-technical-expert hiring authority, $100M/year appropriations for FY27–29, and a Director-run administration.

**FRONTIER § 2(21) creates the "Under Secretary of Commerce for AI Security"** — appointed by the Secretary of Commerce (presumably Senate-confirmed at that level, though not specified in the bill body Canary has reviewed) — and vests all of CAISI's roles in that officer.

Consequences:

- **Political-appointment layer** between career technical staff and the regulator. Slower to spin up; different incentive structure.
- **Cabinet-level accountability** rather than NIST-institutional continuity.
- **No CAISI = no dedicated technical-standards center**. The § 3(c) rulemaking on "minimum requirements for frontier AI frameworks" and IVO licensing will be developed by an Under Secretary's office rather than a NIST-embedded technical team.
- **CAISI appropriations gone** — FRONTIER as posted contains no dedicated appropriation for the Under Secretary's office. Compare GAAIA § 102's $100M/year × 3 years.

Note: NIST CAISI (the current administration's established measurement center, ~$20M funded, referenced in H.R. 9363) continues to exist as a separate matter. FRONTIER's Under Secretary is a new office; it does not replace NIST CAISI, it sits alongside/above it in the AI-oversight architecture.

### 5. Coverage keying: revenue-only → revenue + AI-development expenditures

GAAIA § 101 tier structure:

- Frontier developer: >10^26 ops AND >$50M gross revenue with affiliates
- Large frontier developer: >10^26 ops AND >$500M gross revenue with affiliates

**FRONTIER § 2** tier structure (three tiers now, all measured with affiliates over preceding 36 months):

- Frontier developer: >10^26 ops (no revenue floor for the basic tier, per bill body)
- Large frontier developer: >10^26 ops AND >$50M revenue AND >$1B AI-related development expenditures
- Very large frontier developer: >10^26 ops AND >$5B revenue AND >$10B AI-related development expenditures

The AI-related development expenditures definition (§ 2(4)) explicitly ignores accounting treatment ("expensed, capitalized, deducted, or amortized for financial reporting or tax purposes"). Implication: well-funded pre-revenue labs that GAAIA missed on the revenue-only test are now covered. Also: Meta and xAI's revenue+expenditure mix, and Mistral's absolute funding scale, need re-checked against these thresholds — some labs GAAIA reached may not reach FRONTIER's very-large tier.

Per the § 5 summary's lab-by-lab check: OpenAI, Anthropic, Google/Alphabet, Meta, Microsoft likely clear the very-large tier; xAI, Mistral, Cohere, AI21, Inflection likely do not. So the top-tier IVO regime narrows to 5 labs; the middle-tier compliance audit (§ 4(c)) reaches a wider set.

Threshold-adjustment authority (§ 3(f)) is **one-way, up-only**, and vested in the Under Secretary. GAAIA § 111(j)(2)(A)(ii) asked the Director to recommend threshold updates to Congress — FRONTIER moves that authority to the executive. A future Under Secretary hostile to the regime can weaken coverage by rule; a future Under Secretary friendly to the regime cannot tighten coverage without an amendment.

### 6. Audit architecture split: single IVO regime → two-track

GAAIA § 112 required ALL large frontier developers to retain a licensed IVO for ongoing verification.

**FRONTIER splits this into two tracks:**

- § 4(c) annual **compliance audit** for large frontier developers — by an independent auditor, NOT necessarily a licensed IVO. Lighter engagement. Asks: did the developer comply with its own published framework?
- § 5 ongoing **assessment** for very large frontier developers — by a licensed IVO, with unredacted-at-any-time access. Heavier engagement. Asks: does the developer's framework, governance, monitoring, and mitigation actually achieve "acceptable levels of catastrophic risk mitigation" (the benefits-outweigh-risks cost-benefit standard from § 2(1))?

Interpretive question flagged in the § 6 summary: is the very-large tier subject to BOTH engagements (per § 6 cumulation), or does § 5 replace § 4(c) at that tier? The bill contains no express carve-out either way; the default reading is cumulation. Worth clarifying via technical corrections.

### 7. Preemption: development-scoped → function-scoped, but with named targets

GAAIA § 121 preempted state law "specifically regulating the development of any artificial intelligence model."

**FRONTIER § 9** preempts state imposition of new substantive obligations in three enumerated Covered Subject Areas:

1. Frontier AI catastrophic-risk transparency
2. Third-party auditing and independent verification
3. Incident reporting

Explicit carve-outs preserve generally applicable law, deployer/user regulation, minor-protection statutes, and state procurement/use rules.

The section-by-section explicitly names **CA SB-53, NY RAISE, and IL SB-315** as the target statutes. This is unusually direct — most preemption clauses don't identify their targets in the sponsor's own s-by-s. Signals targeted political displacement rather than incidental preemption.

Real-world effect: per the § 9 summary, the function-scoped narrowing preserves state authority in spaces where states are not currently active (training compute environmental review, workforce rules, non-catastrophic-risk data provenance), and preempts nearly comprehensively in the space where states are active. The narrowing is real but oversold — do not lose Canary's prior position that this trades permanent state-law displacement for permanent federal oversight, now without a sunset backstop.

### 8. Critical safety incident timing tightened; false-statements weakened

**Tightened:** ordinary critical-safety-incident report clock is now **72 hours** (§ 4(h)(1)), not 15 days. The 24-hour imminent-risk clock survives, but with the same GAAIA drafting bug: § 111(g)(2)'s route to "law enforcement agency with jurisdiction" (rather than to the Under Secretary / CAISI) is unchanged as § 4(h)(2). Canary flagged this in GAAIA analysis; it wasn't fixed.

**Weakened:** GAAIA § 111(d)'s standalone bar on knowingly false or misleading statements about catastrophic risk, its management, or framework compliance becomes § 4(e), narrowed to falsity about "subjects the [transparency] report is required to cover." Framework-compliance falsity now bites through the § 4(c) audit backstop rather than directly.

### 9. Public developer registry (new, no GAAIA analogue)

**§ 4(k)(5)** — Under Secretary maintains a public registry of filed frontier developers, with beneficial-ownership disclosure and $10K/day penalty for non-registration. This is the first federal AI-developer registry. Positive addition; helps public and researcher visibility into who is operating at scale.

### 10. GAO IVO-market oversight (new, no GAAIA analogue)

**§ 7** — annual GAO report to House E&C and Senate Commerce on the state of the IVO market and IVO independence from the AI industry. No operative teeth (GAO can't revoke licenses or impose penalties), but persistent recurring oversight of the load-bearing conflict-of-interest question in the § 5 regime. Recommended follow-on ask: pair with a mandatory Under Secretary response window on capture findings.

### 11. Fees dropped

GAAIA § 102(f) established CAISI fee authority on IVOs and large developers; § 112(n) required mandatory IVO application and renewal fees sufficient to offset administrative costs. Both are absent from FRONTIER unless the § 3(c)(6) catch-all is stretched. IVO licensing is no longer explicitly self-funding, and the Under Secretary's office has no dedicated appropriation. Fiscal foundation is fragile.

### 12. Audited-artifact-provenance gap persists

Canary's prior push (in GAAIA analysis) was for cryptographic identification of the audited artifact — content-addressed derivation DAG, hashed intermediates, environment, deterministic pipelines — to prevent checkpoint substitution (assess model A, deploy model A′). **Neither § 4(c) compliance audit nor § 5 IVO assessment requires this.** Same gap as GAAIA. Ask carries forward unchanged.

## What GAAIA had that FRONTIER dropped entirely

Because FRONTIER is a slice of GAAIA (frontier-oversight only), most of the GAAIA titles are gone. Presumably each is targeted for a separate vehicle. Canary should not lose track of the following pieces that no longer have a federal home:

**Title II — Workforce** (§§ 201, 211, 221, 231, 232, 233, 241–248, 251–257):
- AI literacy through AI task force
- K-12 educator preparation
- Research capacity expansion (§ 221 — feeds NAIRR pipeline)
- Scholarships / fellowships / community college / education research awards
- **Labor market measurement** (§§ 241–248) — the AI Workforce Research Hub, modernized labor-market data access, evaluation of AI automation, voluntary adoption reporting, AI questions in federal surveys, data-element production. This is closest to Canary's CDR work.
- **WARN Act AI amendment** (§ 251) — mass-layoff notice must specify AI role
- Detailed employment forecasts, forecasting prize competition, DOL Rapid AI Adjustment Assistance study, state in-demand occupation list updates, AI workforce policy-options report

**Title III — Cybersecurity** (§§ 301, 311, 321):
- **§ 301 CISA 2015 reauthorization** — extends the information-sharing antitrust protection from 2025 to 2035. If FRONTIER doesn't move this and the CISA-2015 sunset lapses 2026-09-30, the info-sharing framework the OpenAI/HuggingFace joint investigation ran under expires. Note: HuggingFace joint investigation is protected sharing activity under CISA-2015, run against an attacker the 2015 definitions never anticipated. This is a live vehicle need, orthogonal to FRONTIER.
- Open-source maintainer support (§ 311)
- GAO on model weight / data center / open-source (§ 321)

**Title IV — R&D + International Cooperation** (§§ 401, 402, 403, 411, 421, 422, 423, 424, 431, 432):
- DOE/NIST testbeds and interagency coordination
- International standards coalitions
- Public federal datasets for AI training / evaluation
- Federal grand-challenge prize competitions (interpretability × 3 in statutory priority list)
- **NAIRR in statute** (§ 423) — with the caveats Canary flagged (zero appropriation, frontier developers excluded from private-sector eligibility)
- Liquid cooling GAO
- Research security certifications

**Financial-crimes provisions** (§§ 131, 132) — mail/wire/bank fraud AI-clause with the drafting bug Canary flagged (AI defendants face LOWER max fine than baseline).

**Free speech / jawboning study** (§ 141) — Commerce study on federal-agency interactions with AI platforms over content moderation, due 180 days.

These 40+ sections need separate advocacy paths if the underlying policy is still wanted. The presumption should be that FRONTIER splits the frontier-oversight teeth into a targeted single vehicle so it can move fast; the rest will follow through slower, wider-coalition legislation. Canary's outreach map should reflect this — FRONTIER conversations are with sponsors' offices; workforce/cyber/R&D conversations are with the same offices plus additional committees.

## Canary's earlier positions — status against FRONTIER

Canary's prior GAAIA analysis identified 11 drafting bugs, 11 cheap asks, and 9 substantive asks (`docs/active/gaaia-analysis/NOTES.md`, `bills/obernolte-trahan/OVERVIEW.md`). Status of each will need a dedicated pass — flagged as a follow-on task. Preliminary read across the summaries:

- **Persistent bugs**: § 111(g)(2) 24-hour routing survives in § 4(h)(2); § 234 STEM Teacher Corps N/A (workforce title dropped); § 421 EO 14110 stale ref N/A (Title IV dropped); § 5002 double-amendment collision N/A (no amendment to NAII Act in FRONTIER).
- **Cheap asks that landed**: cumulation clause (§ 6); developer registry (§ 4(k)(5)); GAO IVO oversight (§ 7); tightened incident clock (72h vs 15d in § 4(h)(1)).
- **Cheap asks not landed**: audited-artifact-provenance; whistleblower grandfathering; IVO-fallback for domain gaps (only partially — initial-launch fixed).
- **Substantive asks**: sunset preservation (LOST — all sunsets removed); severability on preemption (still absent); inseverability of preemption from federal obligations (still absent); IVO independence teeth (weakened — no GAO-capture-finding response window, no publicly-published unredacted-except-carve-out reports).
- **New concerns raised by FRONTIER-specific structure**: § 8 concentration of emergency authority at one Cabinet officer; § 8-vs-Houchin-fact-pattern gap; expenditure-based coverage keying's political fragility (executive discretion via § 3(f) to raise thresholds); dropped whistleblower title.

Full walk of the 31-item NOTES list against FRONTIER is a next-session task.
