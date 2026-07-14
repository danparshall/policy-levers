<!--
Section file: bills/obernolte-trahan/sections/sec-401-interagency-coordination-and-program-to.md
Section-by-section: bills/obernolte-trahan/gaaia_section_by_section.txt
Summary written: 2026-07-14
Written by: Claude (Canary Institute automation), YOLO-mode session
-->

# SEC. 401. INTERAGENCY COORDINATION AND PROGRAM TO FACILITATE AI TESTBEDS — summary

**One-line:** DOE + NIST jointly stand up (in coordination with NSF) an AI testbed program running out of the National Labs, NAIRR, and private-sector partners for capability evals, security/vulnerability assessments, and hackathons — coordination-only, no new appropriation, reimbursable use of Lab compute.

## What it does

Not later than one year after enactment, the Secretary of Energy and the NIST Under Secretary — in coordination with the NSF Director — jointly establish a "Program" that stitches together the National Laboratories, other federal labs, NIST, the NAIRR pilot, and public/private sector entities (including companies of all sizes) to run tests, evaluations, and security/vulnerability risk assessments on AI systems, and to develop measurement methodologies and a third-party evaluation ecosystem (§ 401(a)). A parallel "Voluntary Foundation Models Test Program" lets vendors of foundation models — and of agents/robots built on top of them — opt in for cross-modality testing (§ 401(h)). Both sunset seven years after enactment (§ 401(j)).

## Key provisions

- **Standup deadline:** 1 year from enactment (§ 401(a)).
- **Three-agency structure:** DOE + NIST are the joint operators; NSF is "in coordination with" — a weaker role that mostly maps to NAIRR (§ 401(a)).
- **Activities menu (§ 401(b)):** capability/limitation evals on federal or private compute; automated + reproducible tests (b)(3); high/medium/low compute-intensity variants (b)(6); prioritized security vulnerability work at the National Labs, including classified testbeds where necessary (b)(7); a hackathon (b)(8) — one, unspecified format.
- **Security scope (§ 401(b)(7)(A)–(D)):** autonomous offensive cyber, AI software supply-chain vulnerabilities, CBRN + critical-infrastructure + energy-security threats, and whatever else Secretary/Under Secretary designate. This is model-capability red-teaming, not infrastructure pentesting.
- **Bio/pandemic carve-in (§ 401(c)):** must consider applicability to AI systems trained primarily on biological sequence data, including gene-synthesis models.
- **Consultation (§ 401(g)):** industry (including U.S. financial sector), academia, civil society.
- **Confidentiality (§ 401(i)):** private-sector submissions get FOIA (b)(3) exemption; access limited to the contributor + Program personnel; only aggregated/de-identified info can be released.
- **Metrics + report (§ 401(d), (f)):** joint metrics on collaboration and public/private integration; three-year evaluation to Commerce/Energy/SST committees.
- **Existing-program authority (§ 401(e)):** the Program *may* be run through a pre-enactment program — the whole thing can be a rebadging exercise.

## Who it affects

- **Regulated parties:** None directly. Foundation-model vendors and downstream agent/robot vendors are eligible participants under § 401(h) but participation is voluntary.
- **Empowered actors:** DOE Secretary and NIST Under Secretary (co-leads); NSF Director (coordination); National Labs and federal labs (execution venues); NAIRR (compute partner).
- **Beneficiaries:** Frontier developers seeking third-party evaluations, third-party evaluators building on Program methodologies, and — indirectly — CAISI (§ 102) and the IVO ecosystem (§ 112) that depend on reproducible eval infrastructure.

## Cross-references

- **Defined terms used:** "artificial intelligence system," "foundation model" (§ 101); NAIRR under § 423.
- **Depends on / paired with:**
  - § 402 — coordination + reimbursement + savings; National Lab resources are provided on a **reimbursable basis** unless Commerce waives.
  - § 245 — NIST prize competition for reproducible automation/augmentation benchmarks. The § 401(b)(3) "automated and reproducible" evals should feed and be fed by § 245.
  - § 111 — transparency reports and critical-safety-incident filings would plausibly cite § 401 evaluation methodologies.
  - § 423 — statutorily establishes NAIRR, which § 401 relies on as a compute partner.
  - § 411 — international standards; § 401 methodologies are the domestic input to that pipeline.

## Notable statutory language

> "In carrying out the Program, the Secretary, the Under Secretary, and the Director may utilize a program in effect on the date immediately before the date of the enactment of this Act." — § 401(e).

> "shall prioritize assessments by identifying security vulnerabilities of artificial intelligence systems, including the establishment and utilization of existing classified testbeds, at the National Laboratories if necessary, including with respect to—(A) autonomous offensive cyber capabilities; (B) cybersecurity vulnerabilities in the artificial intelligence software ecosystem and beyond; (C) chemical, biological, radiological, nuclear, critical infrastructure, and energy-security threats or hazards…" — § 401(b)(7).

## Drafting notes & open questions

- **No authorization of appropriations in § 401.** § 402 further requires that National Lab resources be provided on a **reimbursable basis** unless Commerce waives. Combined with the § 401(e) "utilize a program in effect" language and § 401(b)(2)'s "utilize existing solutions to the extent practicable," the Program can be stood up as pure interagency coordination with zero net new capacity. If this is meant to be the National Labs + NIST answer to industry's ask for shared safety-eval infrastructure, the bill's own mechanism doesn't fund it — participants pay the Labs to run their evals. Section-by-section elides this entirely.
- **Section-by-section mismatch.** The § 401 entry in `gaaia_section_by_section.txt` (lines 226–230) mentions collaboration/hackathons/security assessments but omits: the CBRN + critical-infrastructure + energy-security enumeration in (b)(7), the biological-sequence-data consideration in (c), the Voluntary Foundation Models Test Program in (h), the FOIA exemption in (i), and the seven-year sunset in (j). Non-trivial substance is dropped from summary.
- **"Hackathon" (§ 401(b)(8)) is one word, one bullet.** No detail on format, frequency, compensation, disclosure, or safe-harbor. Contrast bug-bounty programs (defined scope, payout schedule, disclosure timeline, legal safe harbor). As drafted this could be a single one-off event.
- **DOE/NIST/NSF coordination reality.** Energy owns compute at scale (Frontier, Aurora, El Capitan). NIST owns evaluation methodology (AISI-lineage). NSF owns academic grants (NAIRR pilot). Joint DOE+NIST leadership with NSF only "in coordination with" undersells NSF's operational role via NAIRR and creates two co-equal leads on a program whose deliverables — reproducible evals, third-party ecosystem, standards — sit downstream of NIST, not DOE. Expect Lab-vs-NIST turf on evaluation ownership.
- **"Security vulnerability assessments" scope ambiguity.** Reading (b)(7) together with the CBRN/critical-infrastructure list, this is model-capability red-teaming (does the model uplift a bio attack? cyber offense?), not infrastructure pentesting of the AI stack. § 321 (GAO report on model weight security) is where infra-side questions live.
- **FOIA exemption asymmetry (§ 401(i)).** Standard trade-secret protection, but combined with § 401(i)(2) limiting access to "personnel of the Program" and the contributor, this locks even other federal agencies out unless data is aggregated. Interaction with CAISI's § 111/§ 112 access rights is unresolved.

## Policy conversation angles

- **Innovation / anti-patchwork:** Reads as low-cost federal infrastructure for a "third-party ecosystem" (§ 401(a)) — voluntary, opt-in, FOIA-protected, no new regulatory burden. Coordinated federal offer to industry that a state patchwork can't replicate.
- **Safety / catastrophic-risk:** The CBRN + autonomous-cyber prioritization in § 401(b)(7) and the biological-sequence-data hook in § 401(c) are what the CAIS/Bengio worldview would want highlighted, though absent dedicated capacity or a required participation trigger, this is a menu of things the Program *may* study rather than a mandatory catastrophic-risk eval regime.
- **National security:** Classified testbeds at the National Labs (§ 401(b)(7)) let cleared work happen where it should. Consultation with the U.S. financial sector (§ 401(g)(1)) is unusual for a testbed statute — signals concern about AI in financial infrastructure.
