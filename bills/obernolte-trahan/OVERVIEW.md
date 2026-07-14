# GAAIA — descriptive overview

Canary Institute reference document. Descriptive only: what the bill does, as written in the 2026-06-04 discussion draft. Positions, feedback-letter material, and analysis belong in a research line under `docs/active/`, not here. Section citations refer to the bill body (see `sections/` and `SECTION_MANIFEST.md`); where the body and Trahan's section-by-section disagree, the body governs (known divergence: § 234, see README).

## The one-paragraph version

GAAIA is a 269-page bipartisan House discussion draft (Obernolte R-CA / Trahan D-MA, both E&C) that trades a time-boxed federal frontier-AI transparency-and-audit regime for an equally time-boxed preemption of state laws regulating AI model development. Around that core trade it attaches a large workforce title (education pipeline plus labor-market measurement plus displacement disclosure), a cybersecurity title (CISA 2015 reauthorization, open-source maintainer support), and an R&D title (testbeds, NAIRR in statute, international standards work). The three regulatory sections at the core (§§ 111, 112, 121) all sunset 3 years after enactment unless reauthorized, which structurally forces Congress back to the table on both the obligations and the preemption at the same time.

## Definitions architecture (§ 101)

The regime is two-tiered by revenue, single-threshold by compute:

- **Frontier model**: a foundation model trained with more than 10^26 integer or floating-point operations, *counting the original training run plus any subsequent fine-tuning, RL, or other substantial modification by the developer*. The threshold aggregates post-training compute rather than measuring the pretraining run alone.
- **Frontier developer**: has trained (or initiated training of) a frontier model AND had, with affiliates, more than $50M gross revenue in the preceding calendar year.
- **Large frontier developer**: same, at more than $500M gross revenue. The heaviest obligations (published framework, IVO audits, access grants) attach only at this tier; some obligations (pre-deployment transparency reports, incident reporting, the false-statements bar, civil penalties) attach to frontier developers generally.
- **Catastrophic risk**: foreseeable and material risk of death/serious injury to more than 50 people or more than $1B in property damage, arising from a frontier model (i) providing non-public CBRN-weapon assistance, (ii) autonomously (no meaningful human oversight) conducting a cyberattack or conduct that would be murder, assault, extortion, or theft if done by a person, or (iii) evading control of the developer or a user. Lawful federal-government activity is carved out.
- **Critical safety incident**: weight exfiltration or unauthorized modification, failure of risk-mitigation measures, or loss of control of a model.
- Supporting definitions: "acceptable levels of catastrophic risk mitigation" is explicitly a cost-benefit standard (benefits outweigh catastrophic risk); "deploy" means making a model available to third parties, excluding availability for development or assessment; "substantial modification" (to a model) and "material modification" (to a framework) trigger disclosure duties below.

## Title I — Frontier AI governance

**§ 102 — CAISI.** Amends the National AI Initiative Act of 2020 (new § 5304) to establish the Center for AI Standards and Innovation at Commerce/NIST, with critical-technical-expert hiring authority. The CAISI Director administers the § 111 reporting mechanisms and licenses IVOs under § 112.

**§ 111 — Transparency.** Within one year of enactment, each large frontier developer must write, implement, comply with, and publish a "frontier AI framework" covering: standards incorporation, risk thresholds for catastrophic-risk capability, capability assessment against those thresholds, deploy/internal-use decision review, third-party assessment, framework update criteria, weight cybersecurity, incident identification and response, internal governance, and catastrophic risk from internal deployment (explicitly including a model circumventing an oversight mechanism). Annual review; material modifications must be published with justification within 30 days. Before or concurrent with deploying a new or substantially modified frontier model, the developer must publish a transparency report (release date, modalities, intended use, restrictions, each catastrophic-risk assessment and its results, third-party involvement). Knowingly false or misleading statements about catastrophic risk, its management, or framework compliance are prohibited, with a good-faith-and-reasonable exception. Redactions permitted for trade secrets, cybersecurity, and public safety, with justification requirements. CAISI must stand up confidential reporting mechanisms within 180 days (critical safety incidents, submittable by developers or the public; catastrophic-risk reports from large frontier developers, explicitly covering internal use). Developers must report a discovered critical safety incident within 15 days, and within 24 hours to law enforcement if it poses imminent risk of death or serious physical injury. State Attorneys General may opt in to receive incident and risk reports. Civil penalty up to $1M per violation, each day a separate violation, enforceable by the U.S. Attorney General. Commerce rulemaking authority (itself sunsetting at 3 years). **Whole section sunsets 3 years after enactment unless reauthorized.**

**§ 112 — IVO audits.** CAISI licenses independent verification organizations. Beginning one year after enactment and semi-annually thereafter, each large frontier developer must retain a licensed IVO for ongoing verification of §§ 111–112 compliance and assessment of framework adequacy against the "acceptable levels of catastrophic risk mitigation" standard. Developers must grant IVOs access; the section provides for audit reports, Director-initiated ad hoc audits, out-of-cycle monitoring, post-audit reports within 30 days, recordkeeping, redacted public report versions with unredacted access provisions, a misrepresentation bar, fees, and the same state-AG opt-in. **Sunsets at 3 years.**

**§ 113 — Whistleblowers.** Anti-retaliation protection for AI whistleblowers, with an enforcement mechanism including jury-trial rights and non-enforceability of rights waivers. No sunset identified.

**§ 121 — Preemption.** Narrower than the headline: no state or political subdivision may establish, continue, or enforce any law "specifically regulating the *development* of any artificial intelligence model." Explicit carve-outs preserve (1) state laws of general applicability and common-law remedies, (2) all state regulation of post-deployment activity, including deployment, distribution, offering, and use of AI systems, products, and services, and (3) state authority granted under this Act itself (notably the AG opt-ins). "Developer" includes fine-tuners of pre-existing models. **Sunsets at 3 years.** The three-way alignment of sunsets across §§ 111, 112, and 121 means the preemption and the federal obligations expire together.

**Remainder of Title I.** § 122: GAO report on federal regulatory impediments to AI innovation and infrastructure (including energy). § 123: NIST pilot for a standard AI model documentation template. § 131: raises maximum fines in the mail/wire/bank fraud and money-laundering statutes from $1M to $2M and adds AI-use penalty enhancements. § 132: penalties for AI impersonation of federal officials. § 141: Commerce study on federal-agency interactions with AI platforms over content moderation and output generation (the jawboning question), due in 180 days.

## Title II — Workforce

Two distinct halves. The first is education pipeline: AI literacy through the existing AI task force (§ 201), K-12 educator preparation (§ 211), research capacity expansion (§ 221), scholarships and fellowships (§ 231), community college and career-technical programs (§ 232), and education research awards (§ 233). The section-by-section also describes a § 234 (STEM Teacher Corps) that does not exist in the bill body.

The second half is labor-market measurement and displacement response, the part closest to Canary's CDR work:

- §§ 241–248: information collection, expert hiring, an AI Workforce Research Hub, modernized access to AI-related labor-market data, evaluation support for AI automation, voluntary AI adoption-and-use reporting, AI questions in federal surveys, and data-element production requirements.
- § 251: amends the WARN Act so that when AI was a "substantial factor" in a mass layoff (per DOL guidance), the required notice must say so, specify the type and usage of the AI, and estimate the percentage of employment loss attributable to it.
- § 252: detailed employment forecasts for AI-sensitive occupations. § 253: a forecasting prize competition. § 254: report on use of new research and tools. § 255: DOL study, due in 12 months, on design options for a Rapid AI Adjustment Assistance Program modeled on trade adjustment assistance precedents. §§ 256–257: state in-demand occupation-list updates and an AI workforce policy-options report.

## Title III — Cybersecurity

§ 301 extends the Cybersecurity Act of 2015 (information-sharing antitrust protection) from 2025 to 2035. § 311 authorizes CISA grants, in consultation with CAISI, to maintainers of designated critical open-source software, and requires large frontier developers to provide AI model access to eligible maintainers. § 321 requires a GAO report on model-weight security protocols, data-center security, and the resource adequacy and supply-chain exposure of the open-source ecosystem.

## Title IV — R&D and international cooperation

§ 401: DOE/NIST testbed program spanning National Labs, NAIRR, and public/private entities for AI testing and evaluation. §§ 402–403: interagency coordination and a progress report. § 411: DOE/NIST-led international AI standards coalitions with like-minded governments, promoting private-sector-led and U.S.-developed standards. § 421: OSTP prioritized list of federal datasets for public release for AI training and evaluation. § 422: OSTP-administered federal grand-challenge prize competitions, with AI interpretability and explainability named among the priority areas. § 423: puts NAIRR in statute. § 424: GAO review of liquid cooling for AI data centers. §§ 431–432: research-security compliance and certification/audit requirements.

## Structural facts worth holding onto

1. The core regulatory trade (§§ 111 + 112 for § 121) is symmetric in time: all three sunset at 3 years. Reauthorization is a package renegotiation by construction.
2. The compute threshold counts cumulative post-training compute, not just the pretraining run.
3. Obligations are revenue-tiered: the $500M tier carries the framework and audit regime; the $50M tier still carries transparency reports, incident reporting, and penalty exposure.
4. Loss of control appears three times in load-bearing places: in the catastrophic-risk definition (§ 101(6)(A)(iii)), the critical-safety-incident definition (§ 101(7)(C)), and the framework requirement on internal-use risk from models circumventing oversight (§ 111(a)(2)(J)). Internal deployment is explicitly in scope.
5. Preemption covers development only; states retain the entire post-deployment field plus general-applicability and common law.
6. Enforcement is federal (U.S. AG) with a state-AG information opt-in, not a state enforcement role.
7. Status: discussion draft, no bill number, no introduction, comment period open at GAAIA@mail.house.gov with no stated deadline. Anticipated referral: House Energy & Commerce.

## Provenance

Derived from the section files in `sections/` (pdftotext of the 2026-06-04 draft), cross-checked against Trahan's section-by-section summary for Title II-IV minor sections. Prepared 2026-07-14.
