<!--
Section file: bills/obernolte-trahan/sections/sec-112-independent-verification-organization-audits-and-assessments.md
Section-by-section: bills/obernolte-trahan/gaaia_section_by_section.txt
Summary written: 2026-07-14
Written by: Claude (Canary Institute automation), YOLO-mode session
-->

# SEC. 112. INDEPENDENT VERIFICATION ORGANIZATION AUDITS AND ASSESSMENTS — summary

**One-line:** Stands up the private-auditor regime — CAISI licenses IVOs; large frontier developers must retain a licensed IVO every 6 months to verify § 111 compliance and framework adequacy; IVOs get near-total civil immunity for models they audit; state AGs opt in; 3-year sunset.

## What it does

The CAISI Director (§ 102) licenses and disciplines Independent Verification Organizations (§ 112(a)). Beginning one year after enactment and every six months thereafter, each large frontier developer must retain a licensed IVO to (1) verify compliance with §§ 111 and 112 and (2) assess whether the developer's frontier AI framework, governance, risk-monitoring, and mitigation achieve "acceptable levels of catastrophic risk mitigation" (§ 112(b)). IVOs submit signed audit and assessment reports to the Director (§ 112(e)); developers file a companion post-audit report within 30 days (§ 112(h)); a 7-day out-of-cycle trigger fires whenever an IVO learns that a prior finding is no longer valid (§ 112(g)).

## Key provisions

- **IVO licensing (§ 112(a)(2)(B–C)).** Application-and-plan model. Grant findings require demonstrated industry independence and adequacy of methods (§ 112(a)(2)(B)(i)–(ii)); seven enumerated revocation grounds cover misleading plans, non-adherence, loss of independence, audited-model failures, obsolete methods, non-compliance, and a catch-all (§ 112(a)(2)(C)(i)–(vii)). Director may convene per-risk expert panels (§ 112(a)(2)(D)).
- **Access (§ 112(d)).** IVO gets "timely access upon request to unredacted materials, records, personnel, systems, and all other information reasonably necessary." Developer may impose "narrowly tailored" trade-secret protocols; any material scope limitation must be disclosed in the report.
- **Reports (§ 112(e), (h)).** Nine mandatory elements including lead-partner certification of accuracy, competence, freedom from conflicts, and regulatory compliance (§ 112(e)(8)). Post-audit report from developer within 30 days (§ 112(h)); implementation description within 14 more days (§ 112(h)(3)(E)).
- **Out-of-cycle trigger (§ 112(g)).** IVO must file supplemental report within 7 days of concluding a prior finding is invalidated; developer response due 7 days after; implementation description 21 days after.
- **Immunity (§ 112(r)).** IVOs are immune from all federal and state suits "for loss caused by, arising out of, relating to, or resulting from the materialization of a catastrophic risk of a frontier model audited and assessed by the IVO." Sole carve-out: exclusive federal cause of action for death or serious physical injury from willful misconduct, adopting the PREP Act standard at 42 U.S.C. § 247d-6d(c)(1) — clear-and-convincing burden, particularity-pleading, no discovery before motion-to-dismiss ruling, and a statutory presumption of no willful misconduct where the IVO followed CAISI regulations (§ 112(r)(2)(B)).
- **Enforcement (§ 112(q)).** IVO *may* refer any violation to DOJ and opted-in state AGs; *shall* refer within 7 days when non-compliance poses an imminent catastrophic risk. Developer violations of subsections (b), (d), (h), or (j) or material misrepresentation carry a civil penalty up to $1,000,000 per violation, with each day a separate violation. DOJ preemption of state AG action once federal action filed (§ 112(q)(2)(C)(iv)).
- **Fees, FOIA, records, sunset.** Cost-recovery fees to Director (§ 112(n)); reports FOIA-exempt (§ 112(o)); 5-year retention (§ 112(j)); section sunsets 3 years after enactment absent reauthorization (§ 112(s)).

## Who it affects

- **Regulated parties:** Large frontier developers (§ 101(15): >$500M prior-year gross revenue including affiliates) — the only entities required to retain IVOs.
- **Empowered actors:** CAISI Director (licensing, revocation, ad hoc audits, expert panels); DOJ (civil-penalty and injunction actions); opted-in state AGs (parallel civil-penalty and injunction actions, with DOJ preemption); IVOs themselves (referral authority to DOJ + state AGs).
- **Beneficiaries:** IVOs, by virtue of the § 112(r) liability shield and the fee-funded market for their services.

## Cross-references

- **Defined terms used:** "Independent verification organization" (§ 101(14)); "large frontier developer" (§ 101(15)); "frontier AI framework" (§ 101(11)); "acceptable levels of catastrophic risk mitigation" (§ 101(1)); "catastrophic risk" (§ 101(6)(A)); "critical safety incident" (§ 101(7)); "material modification" and "substantial modification" (§ 101).
- **Depends on / paired with:** § 102 (CAISI, the licensor); § 111 (the substantive framework and reporting duties an IVO verifies — § 112 is toothless without § 111); § 113 (whistleblower protections plausibly reach IVO staff who report developer violations).

## Notable statutory language

> "An IVO shall be immune from suit and liability under Federal and State law with respect to all claims for loss caused by, arising out of, relating to, or resulting from the materialization of a catastrophic risk of a frontier model audited and assessed by the IVO if the IVO was licensed by the Director under this section at the time of the audit and assessment." (§ 112(r)(1))

Combined with § 112(r)(2)(B)'s presumption of no willful misconduct where the IVO followed CAISI regulations, this is a PREP-Act-caliber liability shield — the vaccine-manufacturer immunity model imported into AI auditing.

## Drafting notes & open questions

- **The FAA/Boeing DER (Designated Engineering Representative) problem is only partially addressed.** CAISI-side controls — COI and funding-transparency rules (§ 112(a)(1)), independence findings (§ 112(a)(2)(B)(i)), broad revocation grounds (§ 112(a)(2)(C)), lead-partner certification (§ 112(e)(8)(C)) — are real. But the market structure is the classic captured-auditor arrangement: the developer selects, retains, and pays the IVO (§ 112(b)) and can rotate to a friendlier one at the next 6-month cycle. CAISI collects only application/renewal fees from IVOs (§ 112(n)), not per-audit fees; there is no rotation requirement, no PCAOB-style peer review, no cooling-off period for IVO staff moving to industry. The § 112(r) immunity further reduces market discipline: the tort tail that ordinarily prices auditor negligence is severed, leaving only CAISI's revocation power and criminal referral as backstops. Independent-verification scholarship on financial audit, credit ratings, and DERs suggests this structure is capture-prone unless a payer-of-record other than the audited entity, or mandatory rotation, is added.
- **No fallback if no IVO is licensed in a given technical area.** § 112(b) says a large frontier developer "shall retain" a licensed IVO; § 112(c) says every IVO must be licensed. There is no provision for CAISI to conduct audits directly, no default to another accreditor (ISO, NIST-recognized third parties), and no suspension of the underlying § 111 framework duty (which is independent of § 112). A developer facing a genuinely empty licensing pool would be in structural non-compliance with § 112(b) — a $1M/day violation — through no fault of its own. This is likely a drafting gap rather than intent.
- **Frequency mismatch.** § 112(b) sets a "semi-annual" cadence (every 6 months) but § 112(f) authorizes ad hoc audits "more frequently than once every 12 months." The 12-month reference in (f) reads as a stale artifact of an earlier annual cadence.
- **Immunity plus willful-misconduct presumption is functionally near-absolute.** § 112(r)(2)(B) states that acting "consistent with its obligations under this section and all applicable regulations, guidelines, or recommendations by the Director" is not willful misconduct "as a matter of law." Because CAISI writes those regulations under § 112(a) and (p), an IVO that mechanically applies CAISI-blessed methods — even methods that miss a catastrophe — has a summary-judgment defense. This mirrors PREP Act practice, where willful-misconduct claims almost never survive motion-to-dismiss.
- **Enforcement asymmetry.** IVO violations are handled through license revocation only (§ 112(a)(2)(C)); developer violations carry $1M/day penalties (§ 112(q)(2)). An IVO that misses a real risk faces professional consequences; a developer that lies to its IVO faces bankruptcy-scale penalties. That gap is defensible on capacity grounds but worth surfacing.
- **State AG opt-in mechanics undefined.** § 112(i) forwards to regulations under paragraph (a)(8); no baseline procedure is spelled out. State AGs cannot receive reports or referrals until CAISI writes those rules, which is not on any statutory clock.

## Policy conversation angles

- **Safety / catastrophic-risk:** The audit regime is the operational core of the safety title — § 111 sets the paper duties, § 112 puts a licensed auditor on them. But the § 112(r) immunity and the developer-pays-IVO structure will be first-order concerns for anyone in the CAIS / Bengio-aligned camp. A safety-forward amendment set would (a) require payer-of-record separation (fee pool at CAISI, IVO selected from a rotating panel), (b) narrow (r)(2)(B)'s "as a matter of law" presumption, and (c) add a CAISI-conducted-audit backstop.
- **Innovation / anti-patchwork:** Industry supporters will emphasize the § 112(r) shield (attracts qualified audit talent by pricing out ruinous tail liability), the FOIA exemption (§ 112(o)), and the trade-secret carve-out in § 112(d)(1). The 3-year sunset (§ 112(s)) is a live selling point — regime terminates unless Congress reauthorizes.
- **State AG / enforcement:** State AGs get opt-in access to reports (§ 112(i)) and referrals (§ 112(q)(1)(B)), plus concurrent civil-penalty authority (§ 112(q)(2)(C)(i)) — but DOJ can freeze state action by filing (§ 112(q)(2)(C)(iv)–(v)) and the underlying receipt of information depends on CAISI rules not yet written. This is real state authority on paper, softer in practice than § 111's parallel structure.
- **National security:** The FOIA exemption (§ 112(o)) plus (k) redaction rules keep audit contents out of adversary hands, but also out of independent-researcher hands. No express DOD/IC access route in § 112 itself.
