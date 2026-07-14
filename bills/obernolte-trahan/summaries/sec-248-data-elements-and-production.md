<!--
Section file: bills/obernolte-trahan/sections/sec-248-data-elements-and-production.md
Section-by-section: bills/obernolte-trahan/gaaia_section_by_section.txt
Summary written: 2026-07-14
Written by: Claude (Canary Institute automation), YOLO-mode session
-->

# SEC. 248. DATA ELEMENTS AND PRODUCTION — summary

**One-line:** Tasks the Secretary of Labor with (i) identifying standardized workforce data elements and reporting to Congress within 12 months on how they could be standardized, securely stored, and opened to researchers, and (ii) leading a NSF-partnered, explicitly *voluntary* effort to develop federal — and facilitate state/local — standards for producing "trusted" AI-related data, funded at $3M over FY26–FY30.

## What it does

Under § 248(a)(1) the Secretary identifies the data elements needed to fulfill reporting obligations elsewhere in the Act, in consultation with States, local workforce development boards, private employers, and other Secretary-chosen entities. Scope is enumerated but open-ended: "the workforce, job vacancies, hiring, earnings, education, skills, and any other aspects … selected by the Secretary" (§ 248(a)(1)). Within 12 months of enactment, the Secretary reports to Senate HELP and House Education & Workforce on how those elements *could be* (A) reported in a standardized manner, (B) collected in a secure repository, and (C) made accessible to researchers (§ 248(a)(2)). Separately, under § 248(b), the Secretary — coordinating with NSF and other federal agencies — leads a "voluntary and, when feasible, consensus-driven effort" to develop federal standards, facilitate state/local standards, and support voluntary implementation. $3M is authorized for FY26–FY30 (§ 248(c)) — roughly $600K/yr.

## Key provisions

- 12-month deadline for the Congressional report on data-element standardization (§ 248(a)(2)).
- Consultation set for element identification: States, local workforce development boards, private employers, other Secretary-chosen entities (§ 248(a)(1)).
- Scope of elements: workforce, job vacancies, hiring, earnings, education, skills, "and any other aspects … selected by the Secretary" (§ 248(a)(1)).
- Report must address a secure repository AND researcher access — not just publication (§ 248(a)(2)(B)–(C)).
- Standards development is led by Sec Labor "in coordination with the National Science Foundation and other relevant Federal agencies" (§ 248(b)) — NIST is **not** named.
- Standards effort is "voluntary and, when feasible, consensus-driven" (§ 248(b)); implementation across levels of government is likewise "voluntary, consistent" (§ 248(b)(2)).
- Authorization: $3,000,000 total for FY26–FY30 (§ 248(c)).

## Who it affects

- **Empowered actors:** Secretary of Labor (identification, report, standards lead); NSF (coordination partner); other unspecified federal agencies. NIST is conspicuously absent from § 248(b) despite being the natural SDO-facilitation home.
- **Beneficiaries:** researchers seeking a secure federal repository of AI-workforce microdata (§ 248(a)(2)(C)); state and local workforce agencies that would receive facilitated standards to adopt if they choose; federal statistical agencies (BLS, Census, BEA) that would ingest or produce data conforming to the standards.
- **Regulated parties:** none directly. Nothing in § 248 compels a private employer, state, or local entity to adopt the resulting standards or contribute data.

## Cross-references

- **Defined terms used:** "Secretary" — Subtitle B context implies Secretary of Labor; confirm against § 101 / any subtitle-level definition.
- **Depends on / paired with:** § 241 (workshops that identify ≥5 high-value datasets — § 248 is where those elements get formalized), § 243 (AI Workforce Research Hub — the operational home for much of this data), § 244 (job-flow pilot), § 246 (BLS voluntary AI-adoption reporting — § 248 standards would define its schema), § 247 (Census/BLS revisions to ABS, CPS, ORS, ATUS surveys — § 248 could align their question banks), § 251 (WARN AI-statement content), § 252 (AI-sensitive occupation forecast archive).

## Notable statutory language

> "The Secretary, in coordination with the National Science Foundation and other relevant Federal agencies, shall lead a voluntary and, when feasible, consensus-driven effort — (1) to develop Federal standards, and facilitate the development of State and local standards, for the production, including collection and reporting, under this Act of trusted data that relates to artificial intelligence; and (2) to support voluntary, consistent implementation and use of the standards at all appropriate levels of government." — § 248(b)

> "[H]ow the data on data elements described in paragraph (1) could be — (A) reported in a standardized manner; (B) collected in a secure repository; and (C) made accessible to researchers." — § 248(a)(2)

## Drafting notes & open questions

- **"Voluntary" appears three times in one subsection — this is a menu, not a mandate.** § 248(b) instructs Labor to *develop* federal standards and *facilitate* state/local standards, but nothing requires any level of government — or the private sector — to adopt them. Even the federal standards get only "voluntary, consistent implementation" language (§ 248(b)(2)). If a future BLS or state workforce agency wants to keep its incompatible schema, § 248 offers no lever to change that. Contrast § 247, which *directs* Census and BLS to revise specified surveys within one year.
- **"Consensus-driven effort" is undefined.** Not tied to OMB Circular A-119 or ANSI-accredited voluntary consensus SDOs, not tied to NIST's standards processes, no requirement to publish a process description. In practice this could range from a rigorous multi-stakeholder SDO convening to a Labor-run working group that ratifies whatever Labor drafts.
- **NIST is missing.** § 248(b) names NSF as the coordinating agency but not NIST — which is the federal government's standards-development lead and the counterpart to the § 102 Center for AI Standards and Innovation. This is either an oversight or a deliberate choice to route the effort through science-funding rather than standards-setting infrastructure. Either way, it means the standards produced under § 248 sit outside the CAISI/NIST orbit that Title I builds up.
- **12-month report is descriptive, not operative.** § 248(a)(2) asks how the data elements "could be" reported/collected/accessed — a scoping exercise, not a build order. No follow-on deadline requires Labor to actually establish the secure repository (§ 248(a)(2)(B)) or the researcher access mechanism (§ 248(a)(2)(C)). Compare § 241(b)(1)(G)(i)(II)'s "≥5 datasets producible in 2 years" — that is more specific and still has no appropriation attached. § 248's report is a step further from action.
- **$3M / 5 years (≈$600K/yr)** is a study-and-convene line, consistent with a scoping mission. It is not enough to stand up a secure federal repository, let alone maintain researcher access infrastructure at scale. If the standards effort succeeds in identifying real data-production gaps, appropriating against them would require separate action.
- **"Trusted data" is not defined here.** § 248(b)(1) refers to "trusted data that relates to artificial intelligence" without cross-reference. Whether "trusted" means privacy-preserving, provenance-tagged, statistically-audited, or something else is left to the standards process to work out — which is fine if the process happens, and a significant hole in the statute if it does not.

## Policy conversation angles

- **Worker / labor:** This is the plumbing under Subtitle B. If it works, § 247's revised surveys, § 246's voluntary employer reporting, and § 243's Hub all speak a common schema — a real precondition for cross-source analysis of AI's labor impact. If it doesn't (which the "voluntary" language makes plausible), each program keeps producing incommensurable data and the Hub's value degrades. **Push:** Canary should watch (a) whether the 12-month report actually names specific standards processes and adopting entities or stays in "could be" language, (b) whether NIST is quietly folded into the § 248(b) coordination via the "other relevant Federal agencies" catch-all, and (c) whether any adopting agency (BLS is the natural candidate) commits publicly to the resulting standards.
- **Innovation / anti-patchwork:** Supporters can frame § 248 as the coordination mechanism that prevents 50 state workforce agencies from inventing 50 incompatible AI-reporting schemas. That framing depends on states actually adopting the federal standards — which § 248 does not require. As drafted it is closer to "menu published" than "patchwork prevented."
