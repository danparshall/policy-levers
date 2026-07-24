<!--
Section file: bills/frontier-act/sections/sec-4-transparency-and-reporting.md
Section-by-section: bills/frontier-act/frontier_act_section_by_section.txt
GAAIA analogue: bills/obernolte-trahan/sections/sec-111-transparency-in-frontier-artificial-intelligence.md
Summary written: 2026-07-24
Written by: Claude (Canary Institute automation)
-->

# SEC. 4. TRANSPARENCY AND REPORTING — summary

**One-line:** The bill's substantive transparency obligation — mandatory frontier AI framework, annual third-party compliance audit, public developer registry, pre-deployment transparency report, and confidential critical-safety-incident and catastrophic-risk reporting to the Under Secretary — enforced by DOJ and opt-in state AGs at up to $1M/violation/day, with **no sunset**.

## What it does

Within one year of enactment (or 90 days after a developer first qualifies), every "large frontier developer" (§ 2: >$50M revenue **and** >$1B in AI-related development expenditures over 36 months, with affiliates) must write, implement, comply with, and publicly post a frontier AI framework (§ 4(a)); retain an independent third party for an annual **compliance audit** against that framework (§ 4(c)); and file a public disclosure/registration statement with the Under Secretary (§ 4(k)). All "frontier developers" (§ 2: any developer of a >10²⁶-FLOP model) must publish a pre-deployment **transparency report** before or when deploying a new or substantially-modified model (§ 4(d)), report critical safety incidents to the Under Secretary within **72 hours** of a reasonable belief they occurred (§ 4(h)(1)), and — for imminent risk of death or serious physical injury — report within **24 hours** to "a law enforcement agency with jurisdiction" (§ 4(h)(2)). Large frontier developers additionally submit catastrophic-risk reports on internal use, with quarterly summary transmittals (§ 4(g)(2)).

## Key provisions

- **Framework content (§ 4(a)(2)(A)–(I)):** risk-mitigation practices; developer-identified catastrophic-risk thresholds and capability assessment; deploy vs. internal-use decision; third-party risk assessment; framework-update and substantial-modification criteria; model-weight cybersecurity; incident response; internal governance.
- **Compliance audit (§ 4(c)):** annual, independent (no financial interest, no results-contingent payment); unredacted access with security protocols (§ 4(c)(1)); report covers substantial compliance, material deviations, internal controls, personnel, COI, methodology, and lead-auditor signature (§ 4(c)(2)); retain unredacted for as-long-as-deployed plus 5 years (§ 4(c)(3)); publish redacted report + high-level summary and transmit redacted report to Under Secretary, AG, and opted-in state AGs within 30 days (§ 4(c)(4)); Under Secretary and AG get unredacted access on request (§ 4(c)(5)).
- **Transparency report (§ 4(d)):** 11 enumerated fields; **machine-readable format** (§ 4(d)(2)); confidential-deployment carve-out permits deferred publication if transmitted to Under Secretary before/with deployment (§ 4(d)(3)).
- **False-statements ban (§ 4(e)):** No knowing inaccurate or false-impression statement in the § 4(d) report, with good-faith-and-reasonable safe harbor (§ 4(e)(2)).
- **Redactions (§ 4(f)):** Trade secret, **risk-prevention mechanisms**, developer cybersecurity, public safety, U.S. national security, or federal/state law. Requires character-and-justification note (§ 4(f)(2)(A)), 5-year retention (§ 4(f)(2)(B)), **and mandatory transmittal of an unredacted copy to the Under Secretary** (§ 4(f)(2)(C)).
- **Reporting channels (§ 4(g)):** Under Secretary builds confidential critical-safety-incident and catastrophic-risk channels within 180 days. Large frontier developers submit catastrophic-risk reports "including internal use and internally deployed models" (§ 4(g)(2)(A)), with quarterly (or agreed) summary transmittals of internal-use assessments (§ 4(g)(2)(B)).
- **Registration and public registry (§ 4(k)):** Large frontier developers cannot develop, deploy, or operate a frontier model without a filed disclosure statement covering legal identity, addresses, 5%-beneficial-owners (private/closely held) or 50% (public), and three points of contact. Under Secretary **maintains and publishes the list of filed developers** (§ 4(k)(5)). $10,000/day penalty for operating without a current statement or filing false information (§ 4(k)(6)).
- **State AG opt-in (§ 4(i))** for § 4(g) and § 4(h) reports, per § 3 rulemaking.
- **Civil penalty (§ 4(j)):** Up to $1M per violation, each day separate. AG or opt-in state AG enforces, with DOJ notice / stay / intervention protections at § 4(j)(3)(B)–(E).
- **Congressional report (§ 4(l)):** Anonymized/aggregated incidents to Congress and the President by Jan. 1, 2028, and annually thereafter.

## Who it affects

- **Regulated parties:** All "frontier developers" (§ 2) get the transparency-report and 72-hour incident obligations. "Large frontier developers" additionally get the framework, compliance audit, registry, and catastrophic-risk-reporting obligations. FRONTIER splits GAAIA's single IVO regime across two tiers: **compliance audit at § 4(c)** (large tier) and **IVO assessment at § 5** (very large tier — >$5B revenue + >$10B expenditure).
- **Empowered actors:** Under Secretary of Commerce for AI Security (receives reports, maintains registry, holds unredacted copies of everything published); U.S. AG and opted-in state AGs (civil enforcement); law-enforcement agencies with jurisdiction (24-hour imminent-risk channel — see below).
- **Beneficiaries:** Public (framework, transparency report, high-level audit summary, developer registry); researchers subject to § 4(f) redactions; state AGs; Congress.

## Cross-references

- **Defined terms used:** "frontier model," "frontier developer," "large frontier developer," "catastrophic risk," "critical safety incident," "Under Secretary," "frontier AI framework" — all § 2.
- **Depends on / paired with:** § 3 (rulemaking, including § 3(b) minimum framework requirements and the state-AG opt-in procedure); § 5 (very-large-tier IVO); § 8 (emergency-order authority the Under Secretary can invoke on § 4(g)/(h) intake); § 9 (state-law preemption).

## Notable statutory language

> "Not later than 24 hours after a frontier developer discovers a critical safety incident that poses an imminent risk of death or serious physical injury, such developer shall report such incident to a law enforcement agency with jurisdiction over such incident." (§ 4(h)(2))

Recipient is a **law enforcement agency**, not the Under Secretary. Unchanged from GAAIA § 111(g)(2), despite Canary flagging it as a probable drafting artifact. Local PD / FBI field office has neither technical AI-incident capacity nor a statutory duty to forward.

## Drafting notes & open questions

- **No cryptographic identification of the audited artifact.** Neither § 4(c) compliance audit nor § 5 IVO assessment binds the audit report to a specific model-weights hash / signed artifact. No statutory tether between "the model audited" and "the model deployed" — a developer could pass audit on artifact A and deploy near-identical artifact A′ without triggering "substantial modification." Canary's audited-artifact-provenance gap remains unaddressed.
- **Self-defined risk thresholds unchanged (§ 4(a)(2)(B)).** Developers still set their own catastrophic-risk thresholds; the only external floor is what the Under Secretary prescribes as § 3(b)(1) minimum framework requirements within 180 days.
- **Redaction basis broadened.** "The risk-prevention mechanisms" (§ 4(f)(1)(A)) is new versus GAAIA § 111(e)(1)(A) — self-executing and potentially expansive. Partly offset by § 4(f)(2)(C)'s new mandatory unredacted transmittal: the public read may be gutted, but the regulator holds the full text.
- **False-statements ban narrowed in scope.** GAAIA § 111(d) prohibited knowing falsity about catastrophic risk, its management, **and** framework compliance. § 4(e) reaches only "subjects on which subsection (d) requires such report to include information." Framework-compliance falsity now bites through the § 4(c) audit backstop rather than a direct falsity ban.

## Changes vs GAAIA discussion draft (2026-06-04)

This is the meatiest diff in FRONTIER. GAAIA § 111 was Canary's most-analyzed section; nearly every subsection moved:

- **Sunset eliminated.** GAAIA § 111(l) sunset the section 3 years after enactment; GAAIA § 111(k)(5) sunset Commerce's rulemaking authority on the same clock. **Neither survives in FRONTIER § 4** — the transparency regime is now permanent. In GAAIA this sat inside a coordinated four-way sunset (§§ 102, 111, 112, 113 all expiring together); that architecture is gone from FRONTIER as a bill-wide feature. **Single largest structural change in the section.**
- **Audit regime split by tier.** GAAIA had one IVO regime at § 112 covering all large frontier developers. FRONTIER splits: § 4(c) is a lighter, financial-audit-style annual **compliance audit** for all large frontier developers; § 5 is the ongoing IVO **assessment** of risk-mitigation adequacy for very large frontier developers only.
- **Incident clock tightened 15 days → 72 hours** (§ 4(h)(1) vs. GAAIA § 111(g)(1)) — the most operationally significant change in reporting cadence.
- **24-hour imminent-risk law-enforcement routing preserved verbatim** (§ 4(h)(2) = GAAIA § 111(g)(2)), including the routing bug — Canary flagged this two months ago and it wasn't fixed.
- **Public developer registry added** (§ 4(k)). No GAAIA analogue. First federal AI-developer registry with public visibility, with beneficial-ownership disclosure and $10K/day penalty.
- **State AG opt-in preserved intact** (§ 4(i)) with DOJ notice / stay / intervention protections at § 4(j)(3)(B)–(E) — same architecture as GAAIA § 111(h) + (i)(3).
- **Redaction basis broadened** to include "risk-prevention mechanisms," paired with a **new mandatory unredacted transmittal to the Under Secretary** (§ 4(f)(2)(C)). No GAAIA analogue for the transmittal.
- **Machine-readable transparency report and confidential-deployment carve-out** added (§ 4(d)(2)–(3)).
- **Quarterly transmittal of internal-use catastrophic-risk assessments** (§ 4(g)(2)(B)). New. Replaces GAAIA § 111(a)(2)(J)'s dropped framework-content item on internal-use oversight-circumvention risk — the obligation shifts from framework design to periodic reporting.
- **Framework-update publication weakened** (§ 4(b)(2)): only a justification, not the amended framework text (GAAIA § 111(b)(2) required both).
- **Under Secretary "recommendations" report dropped.** GAAIA § 111(j)(2) directed the Director to identify legal-authority gaps and recommend legislative/regulatory action annually. Not carried forward; § 4(l) retains only anonymized incidents. Sec. 7's GAO IVO-market report is scoped narrowly to IVO independence, so most of the recommendations function is lost.

## Policy conversation angles

- **Safety / catastrophic-risk:** Annual compliance audit, 72-hour incident clock, quarterly internal-use risk summary, mandatory unredacted transmittal to the Under Secretary, and — decisively — the eliminated 3-year sunset all substantially strengthen the regime versus GAAIA. Unaddressed: developer-set risk thresholds; no cryptographic tether between audited and deployed artifact; § 4(h)(2) imminent-risk routing bug; false-statements ban leaves framework-compliance falsity to the audit rather than a direct bar.
- **Innovation / anti-patchwork:** Tiered structure (only very large developers face § 5 IVO), broadened § 4(f) redaction rights, the § 4(e) good-faith safe harbor, and a familiar financial-audit-style compliance audit will all read as narrowly targeted to preemption supporters. § 4(k) registry is a modest Commerce-desk filing, not a substantive obligation.
- **National security:** § 4(h)(2)'s 24-hour local-law-enforcement channel remains a novel intake with no interagency protocol — pair with FBI cyber and DHS/CISA. § 4(f)(1)(A) "risk-prevention mechanisms" + § 4(f)(2)(C) regulator hold-back create a controlled-disclosure envelope for sensitive material.
- **State AG / enforcement:** § 4(i) opt-in + § 4(j)(3) authority preserved. § 4(j)(3)(D) preemption-of-state-suits during pending federal action means a DOJ that declines to prosecute effectively sidelines opted-in state AGs. Sec. 9's preemption clause will interact — opted-in state AGs enforce federal law, not state substantive transparency obligations.
