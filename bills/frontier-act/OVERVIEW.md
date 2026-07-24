# FRONTIER Act — descriptive overview

Canary Institute reference document. Descriptive only: what the bill does, as written in the 2026-07-23 introduced text. Positions, feedback-letter material, and comparative analysis vs GAAIA belong elsewhere — analysis in `docs/active/gaaia-analysis/`, structural changes in `FRONTIER_VS_GAAIA.md`. Section citations refer to the bill body (see `sections/` and `SECTION_MANIFEST.md`); where the body and Trahan's section-by-section disagree, the body governs.

## The one-paragraph version

FRONTIER is a 74-page, 9-section House bill (Obernolte R-CA / Trahan D-MA, plus four cosponsors) that establishes a permanent federal transparency-audit-incident regime for frontier AI, administered by a new Under Secretary of Commerce for AI Security, with a Cabinet-level emergency-orders authority as backstop. It creates a three-tier coverage structure keyed to compute (10²⁶ ops), gross revenue, and — new vs the GAAIA discussion draft — AI-related development expenditures. It preempts state law in three enumerated frontier-safety functions (transparency, third-party audit, incident reporting) and grants the Secretary of Commerce exclusive federal authority to restrict a frontier model on imminent-catastrophic-risk grounds. Unlike the GAAIA discussion draft it was extracted from, FRONTIER's obligations, preemption, and rulemaking authority are all permanent — there are no sunsets anywhere in the bill.

## Definitions architecture (§ 2)

The § 2 definitions carry most of the bill's coverage weight. Twenty-two defined terms. The load-bearing ones:

- **Frontier model** — a foundation model trained using more than 10²⁶ operations, aggregating the original training run plus any subsequent substantial modification. Post-training compute counts.
- **Frontier developer** — an entity operating in interstate or foreign commerce that has trained (or initiated training of) a frontier model. No revenue floor for the basic tier.
- **Large frontier developer** — a frontier developer that, with affiliates over the preceding 36 months, both had gross revenues over $50M AND incurred at least $1B in AI-related development expenditures. Both prongs required.
- **Very large frontier developer** — same, with the thresholds raised to $5B gross revenues AND $10B AI-related development expenditures.
- **AI-related development expenditures** (§ 2(4)) — amounts paid or incurred in interstate/foreign commerce attributable to AI development, training, fine-tuning, modification, security, or evaluation, without regard to accounting treatment (expensed, capitalized, deducted, amortized). The accounting-neutral drafting captures pre-revenue labs that a pure-revenue test would miss.
- **Catastrophic risk** (§ 2(6)) — a foreseeable and material risk that a frontier developer's development, storage, use, or deployment of a frontier model will materially contribute to (A) death of or serious injury to 50+ people OR $1B+ in property damage, arising from (B) a single incident involving the model (i) providing CBRN or cyber-weapon assistance not publicly available, (ii) engaging in conduct with no meaningful human oversight that is a cyberattack or would be murder/assault/extortion/theft if done by a person, or (iii) evading control of the developer or user. Carve-outs for publicly accessible information, lawful federal-government activity, and harm to which the model did not materially contribute. The $1B property-damage prong excludes loss of equity value (§ 2(18)(B)).
- **Imminent catastrophic risk** (§ 2(11) or nearby — check body for exact numbering) — a present or impending catastrophic risk. The temporal predicate for § 8 emergency orders and the § 5 IVO 72-hour Secretary referral. Definition is thin — "present or impending" — so the operative work is done by the § 2(6) magnitude threshold.
- **Critical safety incident** — four prongs: (A) unauthorized access to / modification of / exfiltration of model weights; (B) harm from a materialized catastrophic risk; (C) loss of control; (D) frontier model using deceptive techniques against its developer to subvert controls, outside a designed evaluation, demonstrating materially increased catastrophic risk. Prong (D) is new vs GAAIA.
- **Acceptable levels of catastrophic risk mitigation** (§ 2(1)) — risk mitigation adequate to ensure that anticipated benefits of the model outweigh its catastrophic risk. Explicitly a cost-benefit standard; not a safety-floor standard. This is the assessment benchmark for the § 5 IVO regime.
- **Under Secretary** (§ 2(21)) — the Under Secretary of Commerce for AI Security, appointed by the Secretary of Commerce. Holds the bill's rulemaking authority, receives incident reports and registrations, licenses and oversees IVOs.
- **Deploy** — making a frontier model available in interstate/foreign commerce to a third party for use, modification, copying, or combination with other software, and other operative senses. Excludes availability for development or assessment.
- **Substantial modification** (of a model) and **material modification** (of a framework) — trigger disclosure duties in § 4. Criteria to be defined by rulemaking under § 3(c)(3).

Full walk of all 22 defined terms is in `summaries/sec-2-definitions.md`.

## The nine sections

**§ 1 — Short title.** Names the Act (Frontier Risk Oversight, National Transparency, Independent Evaluation, and Reporting Act — FRONTIER Act).

**§ 2 — Definitions.** As above. 22 terms.

**§ 3 — Rulemaking.** Vests the Under Secretary with notice-and-comment rulemaking authority (5 USC § 553). Three mandatory rulemakings on 180-day clocks: (1) minimum requirements for frontier AI frameworks (feeds § 4); (2) IVO licensing and oversight criteria (feeds § 5); (3) criteria for "substantial modification" (of a model) and "material modification" (of a framework). Authorizes the Under Secretary to INCREASE by rule the compute, revenue, and expenditure coverage thresholds — one-way ratchet, up-only. Effective-date rule: no earlier than 180 days after publication in final form; prospective-only. No sunset on rulemaking authority (unlike GAAIA § 111(k)(5)).

**§ 4 — Transparency and reporting.** The substantive transparency obligation. Large frontier developers must write, implement, comply with, and publish a frontier AI framework covering catastrophic-risk thresholds and assessment, model-weight cybersecurity, incident response, and deployment / internal-use decisions, incorporating widely-accepted approaches. Timing: 1 year after enactment OR 90 days after qualifying as a large frontier developer, whichever is later. Annual review; material modifications published with justification. Annual independent compliance audit (§ 4(c)) — not necessarily by a licensed IVO, contrast § 5. Registration required with the Under Secretary. Public developer registry maintained by the Under Secretary (§ 4(k)(5)), with beneficial-ownership disclosure and $10K/day non-registration penalty.

All frontier developers (not just large) must publish, before or when deploying a new or substantially modified frontier model, a transparency report (capabilities, intended uses, restrictions, risk assessments), with redactions permitted to protect trade secrets, risk-prevention mechanisms, cybersecurity, public safety, or national security. Unredacted transmittal to the Under Secretary (§ 4(f)(2)(C)) is required.

Critical safety incident reporting: 72 hours to the Under Secretary (§ 4(h)(1)); 24 hours to law enforcement if the incident poses imminent risk of death or serious physical injury (§ 4(h)(2)) — this last routing is the surviving GAAIA drafting bug (routes to "law enforcement agency with jurisdiction" rather than to the Under Secretary; CAISI/Commerce oversight bypassed). Large frontier developers must additionally report catastrophic risk arising from their models, INCLUDING INTERNAL USE (§ 4(g)); quarterly transmittal of internal-use catastrophic-risk assessments (§ 4(g)(2)(B)).

False-statements bar (§ 4(e)) — narrower than GAAIA § 111(d); tied to falsity about subjects the transparency report is required to cover.

State AGs may opt in to receive incident and risk reports.

Civil penalty up to $1M/violation/day, each day a separate violation. Enforceable by the U.S. Attorney General AND by opted-in state AGs, the latter subject to DOJ notice, federal intervention right, and stay of state actions when DOJ sues on the same violations.

No sunset.

**§ 5 — Independent verification.** Under Secretary licenses and oversees IVOs. Beginning at IVO-availability (§ 5(b)) and semi-annually thereafter, each **very large** frontier developer must retain a licensed IVO for ongoing assessment of whether its frontier AI framework, governance policies, risk-monitoring, and mitigations achieve acceptable levels of catastrophic risk mitigation. IVO gets unredacted access to materials, records, and assessments at any time.

**72-hour IVO referral to Secretary on imminent catastrophic risk** (§ 5(p)(1)(B)) — the only private-actor channel into § 8 emergency-order authority. When an IVO determines a model presents imminent catastrophic risk, it must refer the matter to the Secretary within 72 hours for consideration of a § 8 order.

IVO may subcontract specialized portions while remaining fully responsible. Material misrepresentations in any IVO report or opinion prohibited.

IVO revocation carve-out (via § 3(c)(2)(C)(iv)(I)-(II)) shields the IVO from post-hoc discipline when the developer failed to implement recommended corrective actions.

Civil penalty for developer violations: up to $1M/violation/day; AG + opted-in state AG enforcement.

No IVO fee authority (dropped from GAAIA § 112(n)). No CAISI-conducted-audit fallback for domain-specific IVO absence.

No sunset.

**§ 6 — Cumulative obligations.** Except as expressly provided, each higher-tier developer complies with every requirement applicable to the tiers below it. New clause; GAAIA had no dedicated cumulation section. The "except as expressly provided" carve-out is currently empty on its face — no existing section deviates from cumulation. Interpretive question: is the very-large tier subject to BOTH the § 4(c) compliance audit AND the § 5 IVO assessment? Default reading is yes; see `summaries/sec-6-*.md`.

**§ 7 — GAO report on IVO market.** Comptroller General reports annually to House Energy & Commerce and Senate Commerce on the state of the IVO market, IVO independence from the AI industry, and recommendations to preserve that independence. No operative teeth beyond congressional information. New oversight mechanism; no GAAIA analogue.

**§ 8 — Emergency orders addressing imminent catastrophic risk.** New authority, no GAAIA analogue. Secretary of Commerce may suspend or restrict a frontier developer's development, deployment, or internal use of a frontier model upon written finding of imminent catastrophic risk.

- **Provisional order**: preliminary determination, notice and opportunity to cure UNLESS imminence forecloses them, expires after 45 days.
- **Final order**: written finding required, expires after 90 days, renewable only on fresh finding.
- Each order must state basis, restrictions imposed, and conditions for rescission. Secretary must rescind once conditions are met or the risk has passed.
- **Developer administrative hearing** — expedited; Secretary bears the burden of justifying the order.
- **Exclusive judicial review D.D.C.**, appeal to D.C. Circuit.
- **Congressional oversight** — each order transmitted to Congress; semiannual reports on use of the authority.
- **§ 8(l) exclusivity** — "This section is the exclusive means by which any federal actor may restrict a frontier model on imminent-catastrophic-risk grounds." Locks out other federal actors from parallel action on that ground. Preserves other-authority action (CISA/FBI/DOD acting under their own statutes on their own grounds).
- **Civil penalty up to $10M/violation/day** (10× the § 4/§ 5 penalty); **willful violations criminal**.

Whether § 8 would actually reach the Houchin-cited fact pattern ("one of the most advanced AI systems … broke out of its own developer's testing environment, reaching systems it was never supposed to touch") depends on whether the sandbox breakout produced foreseeable material harm meeting the § 2(6) magnitude threshold (50+ deaths / serious injuries OR $1B+ property damage). Test-environment breakout to unauthorized systems may not automatically clear it. § 8 is drafted for CBRN-uplift-scale or grid-attack-scale events. See `summaries/sec-8-*.md` for the full analysis.

No sunset.

**§ 9 — Relationship to State laws.** Preempts state or political subdivision imposition of new substantive obligations on AI developers as to three enumerated Covered Subject Areas: (1) frontier AI catastrophic-risk transparency, (2) third-party auditing and independent verification, (3) incident reporting.

Explicit rule of construction preserves:
- Generally applicable laws (contract, tort, consumer protection)
- Use- and deployment-based regulation of DEPLOYERS and USERS
- State laws protecting minors
- State procurement and use rules

Section-by-section explicitly names CA SB-53, NY RAISE, and IL SB-315 as target statutes. Unusually direct.

No sunset (GAAIA § 121's 3-year sunset removed). No severability language. No inseverability tying preemption to federal obligations.

## Structural observations

**No sunsets anywhere.** GAAIA's coordinated four-way sunset (§§ 102/111/112/113 + rulemaking-authority sunset at § 111(k)(5)) is entirely gone. The regime is permanent, the preemption is permanent, the rulemaking authority is permanent. Verified by full-text grep for "sunset," "cease to have effect," "expires," "terminat" — zero genuine hits in the bill body. This is the single largest structural difference from GAAIA. See `FRONTIER_VS_GAAIA.md § 1`.

**No whistleblower title.** GAAIA § 113 anti-retaliation protection is entirely dropped. Full-text grep for "whistle," "retaliat" returns zero hits. No federal statutory protection for employees at frontier labs who observe catastrophic-risk-relevant behavior. See `FRONTIER_VS_GAAIA.md § 2`.

**Commerce-exclusive federal responder architecture.** § 8(l) locks out other federal actors from imminent-catastrophic-risk action on that ground; § 9 locks out states from the covered functions. Combined: the Secretary of Commerce (via § 8) and the Under Secretary of Commerce for AI Security (via §§ 3–5) are the exclusive federal responders in the covered domain. Very tight authority concentration.

**Two-track audit architecture** rather than GAAIA's single IVO regime. § 4(c) compliance audit (large tier, non-licensed auditors OK); § 5 IVO assessment (very-large tier only, licensed IVOs required, unredacted access). Splits the audit population, reduces the top-tier auditor pool to ~5 mega-labs, and creates an interpretive question about cumulation at the very-large tier (§ 6).

**One-way threshold ratchet.** § 3(f) authorizes the Under Secretary to raise coverage thresholds by rule. No parallel authority to lower thresholds. A future hostile administration can weaken coverage administratively; a friendly administration cannot tighten it without amendment.

**No dedicated appropriation.** GAAIA § 102 funded CAISI at $100M/year × 3 years. FRONTIER contains no dedicated appropriation for the Under Secretary of Commerce for AI Security's office, and no IVO fee authority. Fiscal foundation for administration is fragile.

**Coverage keying to expenditures** captures pre-revenue labs GAAIA missed. § 2(4)'s accounting-neutral definition of AI-related development expenditures reaches well-funded labs regardless of revenue.

**Persistent drafting bug** at § 4(h)(2): 24-hour imminent-risk-to-life report routes to "law enforcement agency with jurisdiction" rather than to the Under Secretary. This is the same bug Canary flagged in GAAIA § 111(g)(2). Cheap ask.
