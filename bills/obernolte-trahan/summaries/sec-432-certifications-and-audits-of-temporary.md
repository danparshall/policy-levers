<!--
Section file: bills/obernolte-trahan/sections/sec-432-certifications-and-audits-of-temporary.md
Section-by-section: bills/obernolte-trahan/gaaia_section_by_section.txt
Summary written: 2026-07-14
Written by: Claude (Canary Institute automation), YOLO-mode session
-->

# SEC. 432. CERTIFICATIONS AND AUDITS OF TEMPORARY FELLOWS — summary

**One-line:** Before any non-federal individual (fellow, contractor, or consultant) does AI or critical-and-emerging-tech work for an agency, the individual and the agency head must sign a certification that the individual will not perform "inherently governmental functions," and the agency IG must audit compliance annually.

## What it does

Section 432 creates a two-step control on temporary AI-adjacent labor inside federal agencies. First, a pre-engagement **certification**: the temporary fellow and the agency head both sign a statement that the fellow will not perform inherently governmental functions (§ 432(a)(1)); the head then transmits that certification to OMB and the four committees of jurisdiction within 30 days (§ 432(a)(2)). Second, an annual **audit** by the agency's inspector general enumerating headcount, hiring authority, funding source, work performed, and compliance status for each temporary fellow (§ 432(b)(1)), with a 30-day submission window to OMB and the same committees (§ 432(b)(2)).

## Key provisions

- **Covered individuals** — "temporary fellow" is defined broadly: "a fellow, contractor, consultant, or any other individual performing work for such agency who is not an employee of the Federal Government" (§ 432(c)(5)). Reaches essentially anyone doing agency AI work outside the federal civil service.
- **Covered work** — AI or any other technology on the NSTC critical-and-emerging-technologies list (§ 432(c)(2)).
- **"Inherently governmental function"** — imported from § 5 of the Federal Activities Inventory Reform Act of 1998 (31 U.S.C. 501 note) and FAR subpart 7.5 (§ 432(c)(4)). In an AI context this reaches: rulemaking and policy determinations, procurement source-selection and award decisions, adjudication of individual rights, and any exercise of discretion that binds the U.S. government.
- **Sign-off** — the statute specifies the agency head personally as signatory (§ 432(a)(1)); no delegation language is included, though standard agency delegation authorities under 5 U.S.C. § 302 likely still apply absent a bar.
- **Reporting audience** — OMB Director plus Senate Commerce, Senate Energy & Natural Resources, House Science, and House Energy & Commerce (§ 432(c)(3)).

## Who it affects

- **Regulated parties:** Any non-federal individual doing AI or CET work under an agency contract, IPA, fellowship, or consultancy — with no dollar or duration threshold.
- **Empowered actors:** Agency heads (must certify), inspectors general (must audit), OMB and the four committees of jurisdiction (receive certifications and audit reports).
- **Beneficiaries:** Congressional oversight; civil-service integrity; downstream targets of agency AI decisions (regulated firms, affected workers) insofar as they rely on those decisions being made by accountable federal officials.

## Cross-references

- **Defined terms used:** "agency" per 44 U.S.C. § 3502 (§ 432(c)(1)); "critical and emerging technology" tied to the NSTC list (§ 432(c)(2)); "inherently governmental function" via FAIR Act 1998 and FAR 7.5 (§ 432(c)(4)).
- **Paired with:** § 102 (CAISI hiring) and § 242 (Labor Department AI experts) both create excepted-service AI hiring pipelines; § 432 is the counterweight, constraining what the *non-federal* leg of the AI workforce can do inside an agency.

## Notable statutory language

> "Before a temporary fellow performs work for an agency under this Act relating to artificial intelligence or another critical and emerging technology, such temporary fellow and the head of such agency shall sign a certification that such temporary fellow will not perform an inherently governmental function." — § 432(a)(1)

## Drafting notes & open questions

- **No enforcement mechanism.** The section is certification + audit + report — full stop. There is no penalty for a false certification, no automatic remedy if the IG finds non-compliance, no requirement that a non-compliant fellow be removed, no bar on the fellow's future federal service, no contract-clawback, and no cure period. An IG finding of "this fellow was making policy decisions" flows to OMB and four committees and then depends entirely on political will for a consequence. Compared to § 111-style civil penalties elsewhere in the bill, § 432 is a pure sunshine mechanism.
- **"Under this Act" scoping (§ 432(a)(1)).** The certification requirement attaches to work "under this Act" — arguably reaching only AI/CET work funded or authorized by GAAIA itself, not the broader universe of agency AI contracting. If read narrowly, most existing agency AI contractors are outside the section entirely. This should be clarified before markup.
- **Head-of-agency signature not obviously delegable.** The text specifies "the head of such agency shall sign" (§ 432(a)(1)). At large agencies (DoD, HHS) with hundreds of AI-related contractors this is either administratively unworkable, requiring routine delegation, or intentionally frictional. Which the drafters intend is not stated.
- **"Inherently governmental" is a contested line in AI.** FAR 7.5's illustrative list predates modern ML systems. Whether tuning an agency's model, curating its training data, or selecting a benchmark counts as inherently governmental is genuinely unsettled — and the section punts that question to agency heads and IGs without guidance.

## Policy conversation angles

- **National security / civil-service integrity:** Frames § 432 as a guardrail against private technologists making binding federal decisions on AI systems the public depends on. Anchored in the settled principle that policy calls belong to accountable officials, not to contracted specialists.
- **Anti-DOGE / accountability:** The section reads as a direct response to the 2025 pattern of political-appointee and contractor embeds accreting decisional authority inside agencies without Senate confirmation or civil-service accountability. Democrats will read it that way; some Republicans will read it as targeting a recent administration's workforce model and object on those grounds.
- **Innovation / speed of government AI adoption:** Certification + IG audit adds administrative friction to bringing outside AI expertise into agencies quickly. Advocates for rapid federal AI adoption (a core GAAIA goal elsewhere) will argue that a head-of-agency signature per fellow is overkill and will slow the very hiring pipelines §§ 102 and 242 aim to speed up. Whether the friction is proportionate depends on how narrowly "inherently governmental" is drawn in practice.
