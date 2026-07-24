<!--
Section file: bills/frontier-act/sections/sec-5-independent-verification.md
Section-by-section: bills/frontier-act/frontier_act_section_by_section.txt
GAAIA analogue: bills/obernolte-trahan/sections/sec-112-independent-verification-organization-audits-and-assessments.md
Summary written: 2026-07-24
Written by: Claude (Canary Institute automation)
-->

# SEC. 5. INDEPENDENT VERIFICATION — summary

**One-line:** Under Secretary licenses IVOs; only *very large* frontier developers ($5B revenue + $10B AI-dev spend over 36 months) must retain one for ongoing assessment against "acceptable levels of catastrophic risk mitigation"; IVO gets unredacted access at any time; a determination of imminent catastrophic risk triggers a 72-hour referral to the Secretary for a § 8 emergency order; civil penalty up to $1M/violation/day, each day a separate violation.

## What it does

Two-tier audit stack, split across § 4 and § 5. Under § 4(c), every **large** frontier developer ($50M rev + $1B AI-dev spend) must retain a third party for an **annual compliance audit** of its published frontier AI framework — a lighter, contract-based engagement with no licensing regime behind it. Under § 5, every **very large** frontier developer ($5B rev + $10B AI-dev spend, § 2(28)) must additionally retain a **licensed IVO** for **ongoing assessment** — not just compliance, but a running professional judgment on whether the developer's framework, governance, risk-monitoring, and mitigation actually "achieve acceptable levels of catastrophic risk mitigation" (§ 5(b)), extending to catastrophic risks arising from the developer's **internal** use of frontier models (§ 5(b)). Reports go simultaneously to the developer and the Under Secretary at least every six months, and the developer publishes a redacted version within 30 days (§ 5(j)(1)).

## Key provisions

- **IVO licensing by the Under Secretary (§ 5(a), (c)).** Replaces the GAAIA "Director" (of CAISI). Substantive licensing criteria — independence, adequacy of methods, revocation grounds — live in § 3(c) rulemaking, not § 5.
- **Very-large-only trigger (§ 5(b)).** Retention required within one year after the first IVO with capacity is licensed, or 90 days after qualifying as very-large, whichever is later.
- **Unredacted access "at any time" (§ 5(e)(1)).** Developer must grant "timely access upon request to unredacted materials, records, personnel, systems, and all other information reasonably necessary." Security protocols must be "narrowly tailored" to trade-secret/CBI (§ 5(e)(2)); any material scope limitation must appear in the report (§ 5(e)(3)). § 5(n) additionally requires the developer *and* IVO to give the Under Secretary and Attorney General unredacted materials on request.
- **Subcontracting with pass-through obligation (§ 5(d)).** IVOs may subcontract "one or more portions of an assessment to an organization with specialized expertise," but the retaining IVO "remain[s] fully responsible" (§ 5(d)(1), (3)) and the subcontractor "shall stand in the place of the retaining IVO" for all qualification, COI, and confidentiality obligations (§ 5(d)(2)). New vs GAAIA.
- **Assessment reports (§ 5(f)).** IVO sets frequency in "professional judgment," floor of once every 6 months (§ 5(f)(1)). Seven mandatory content elements including lead-partner certification of accuracy, competence, freedom from conflicts, and regulatory compliance (§ 5(f)(2)(F)).
- **Public disclosure with redaction-dispute mechanism (§ 5(j)).** Developer publishes a high-level summary plus redacted report within 30 days and transmits to Under Secretary, AG, and opted-in State AGs. Under Secretary, AG, or opt-in State AG may challenge overbroad redactions; Under Secretary reviews within 30 days and may conduct in camera review of the unredacted report (§ 5(j)(2)). New dispute mechanism vs GAAIA.
- **72-hour referral to Secretary on imminent catastrophic risk (§ 5(p)(1)(B)).** If an IVO determines that a very large frontier developer's model "fails to achieve acceptable levels of catastrophic risk mitigation in a manner that poses an imminent catastrophic risk," the IVO "shall refer the matter to the Secretary, for consideration of an emergency order under section 8, as soon as practicable, and in any event not more than 72 hours." This is the pipe between § 5 and § 8. **New mechanism vs GAAIA**, whose § 112(q)(1)(B) required a 7-day referral to DOJ + state AGs — an enforcement-track referral, not an emergency-order-track referral.
- **Misrepresentation bar (§ 5(o)).** "An IVO shall not knowingly make a material misrepresentation or omission in any report or opinion prepared pursuant to this section." Broadened from GAAIA § 112(m)'s narrower "audit and assessment report."
- **Civil penalty (§ 5(p)(2)).** Up to $1,000,000 per violation for developer breach of subsections (b), (e), (g), (h), (i), (j), or (k), or for material misrepresentation in a post-assessment report; each day is a separate violation. AG and opted-in State AG enforcement; DOJ preemption of state action while DOJ suit pending (§ 5(p)(2)(C)(iv)).
- **Immunity (§ 5(q)).** IVO-side liability shield materially unchanged from GAAIA § 112(r): near-absolute Federal + State immunity with a PREP-Act willful-misconduct carve-out (42 U.S.C. § 247d-6d(c)(1)), clear-and-convincing burden, and a matter-of-law presumption that following the Under Secretary's regulations is not willful misconduct.

## Who it affects

- **Regulated parties:** Very large frontier developers only — per § 2(28), gross revenues > $5B and AI-related development expenditures ≥ $10B with affiliates over the preceding 36 months. Massive narrowing from GAAIA § 112, which reached every large frontier developer (GAAIA § 101(15): > $500M prior-year gross revenue).
- **Empowered actors:** Under Secretary of Commerce for AI Security (licensing, ad hoc assessments under § 5(h), redaction review); Secretary of Commerce (receives 72-hour IVO referrals, exercises § 8 emergency-order authority); DOJ and opted-in State AGs (civil-penalty enforcement); IVOs themselves (referral authority).
- **Beneficiaries:** IVOs, via the § 5(q) liability shield.

## Cross-references

- **Defined terms used:** "IVO" / "independent verification organization" (§ 2(15)); "very large frontier developer" (§ 2(28)); "large frontier developer" (§ 2(16)); "frontier AI framework" (§ 2(11)); "acceptable levels of catastrophic risk mitigation" (§ 2(1)); "catastrophic risk" (§ 2(6)); "imminent catastrophic risk" (§ 2(14)); "critical safety incident" (§ 2(7)); "Under Secretary" (§ 2(27)).
- **Depends on / paired with:** § 3(c) (IVO licensing regs, the substantive criteria § 5(a) forwards to); § 4 (the compliance-audit tier below § 5 and the framework the IVO assesses); § 8 (the emergency-order backstop the 72-hour referral feeds into); § 2 definitions of "acceptable levels of catastrophic risk mitigation" and "imminent catastrophic risk" (the load-bearing assessment standards).

## Notable statutory language

> "If, in the course of performing its responsibilities under this section, an IVO determines that a very large frontier developer's frontier model fails to achieve acceptable levels of catastrophic risk mitigation in a manner that poses an imminent catastrophic risk, the IVO shall refer the matter to the Secretary, for consideration of an emergency order under section 8, as soon as practicable, and in any event not more than 72 hours, after its determination." (§ 5(p)(1)(B))

This is the only statutory pathway in FRONTIER for a private actor to trigger the § 8 emergency-order machinery. It makes the IVO not just an auditor but an early-warning tripwire.

## Drafting notes & open questions

- **Standard collapse relative to GAAIA.** GAAIA § 112(b) split IVO work into two duties: (1) "verify compliance with §§ 111 and 112" and (2) "assess adequacy … for achieving acceptable levels of catastrophic risk mitigation." FRONTIER § 5(b) drops (1) and keeps only (2). Statutory compliance auditing has migrated to § 4(c)'s unlicensed annual third-party regime. That means IVO judgment is now purely qualitative-risk, not compliance-check — a professionalization of the role, but one that leaves the § 4 compliance function untethered from the licensed-auditor ecosystem.
- **IVO-fallback gap survives.** Canary previously flagged that GAAIA had no fallback if no IVO were licensed in a given technical area; a developer would be in structural $1M/day non-compliance through no fault of its own. FRONTIER § 5(b) partially answers this by anchoring the clock to "the date on which the Under Secretary first licenses an IVO with capacity to accept an engagement" — solving the *initial* gap but not the *domain-specific* gap (no licensed IVO for a novel CBRN or cyber-weapon assessment vector). No Under-Secretary-conducted-assessment backstop.
- **IVO carve-out from license revocation (§ 3(c)(2)(C)(iv)(I)–(II)).** New in FRONTIER: an IVO's license is *not* revoked for models that fail to achieve acceptable mitigation if the IVO can show it identified the deficiency in a § 5(f) or § 5(i) report *and* the developer failed to implement corrective actions. Meaningful shield against post-hoc second-guessing; also weakens CAISI's ability to discipline IVOs whose methods systematically miss risks the developer plausibly-fixes-then-doesn't.
- **Sunset dropped.** GAAIA § 112(s) sunset the entire IVO regime 3 years after enactment absent reauthorization. **FRONTIER § 5 has no sunset.** The IVO structure is now permanent absent affirmative repeal — a policy shift worth flagging on the Hill.
- **IVO fee mechanism dropped.** GAAIA § 112(n) authorized cost-recovery application and renewal fees payable to the Director. **FRONTIER § 5 has no fee provision.** § 4(f)(4) authorizes fees on large frontier developers to fund the registry, but nothing funds IVO licensing and oversight. Absent an appropriation, this is an unfunded mandate on the new Under Secretary office.
- **No IVO retaliation / whistleblower protection in FRONTIER.** GAAIA carried a whistleblower title (§ 113) that plausibly reached IVO staff; FRONTIER drops it entirely. An IVO lead partner who signs a hostile report has neither statutory job protection nor a contractual anti-retaliation floor.
- **Enforcement asymmetry preserved and sharpened.** IVO breaches route to license revocation only (via § 3(c) grounds); developer breaches carry $1M/day penalties (§ 5(p)(2)). The FRONTIER additions — the § 3(c)(2)(C)(iv) escape hatch, the missing whistleblower title, the dropped sunset — all lean the same direction: more secure IVO market, more concentrated developer exposure.
- **Assessment standard is benefits-outweigh-risks, not zero-risk.** § 2(1) defines "acceptable levels of catastrophic risk mitigation" as mitigation "adequate to ensure a frontier model's anticipated benefits outweigh its catastrophic risk." An IVO signing off is certifying a cost-benefit judgment call, not a safety guarantee. Worth surfacing to Hill audiences who read "acceptable" as "safe."

## Changes vs GAAIA discussion draft (2026-06-04)

This is one of the two deepest structural shifts in the bill (the other being new § 8). Compared to GAAIA § 112:

- **Coverage tier narrowed from large ($500M rev) to very-large ($5B rev + $10B AI-dev spend, 36-month window).** Order-of-magnitude reduction in the covered universe. Of the current frontier lab set: OpenAI, Google/Alphabet (as frontier developer), Meta, Microsoft, and Anthropic almost certainly clear both thresholds on 2026 trajectories; **xAI and Mistral almost certainly do not** (xAI on revenue; Mistral on both). Cohere, AI21, Inflection also drop out. Net: ~5 mega-labs remain on the IVO hook, versus ~8–12 under GAAIA's large-tier trigger. The § 4(c) unlicensed annual compliance audit still catches the broader large-tier set — but that audit is only against the developer's own published framework, not against the "acceptable levels of catastrophic risk mitigation" standard.
- **72-hour IVO-to-Secretary emergency referral (§ 5(p)(1)(B)).** Genuinely new. GAAIA § 112(q)(1)(B) had a 7-day IVO-to-DOJ enforcement referral only; there was no fast pipe into any emergency-order authority (because GAAIA had no § 8 analogue). FRONTIER creates both the § 8 authority and the § 5 tripwire that feeds it.
- **Access carve-out narrowed.** GAAIA § 112(d)(1) let developers impose "reasonable security protocols, access limitations, and confidentiality requirements" — the "access limitations" phrase invited developer-side scope-narrowing. FRONTIER § 5(e)(2) drops "access limitations," leaving only "security protocols and confidentiality requirements." Modest tightening in the developer's favor of complying with the "at any time" access norm.
- **Misrepresentation bar broadened.** GAAIA § 112(m) prohibited misrepresentation "in an audit and assessment report." FRONTIER § 5(o) prohibits it "in any report or opinion" — reaches the § 5(g)(2) opinions and § 5(i) supplemental reports and opinions, not just the primary assessment.
- **Redaction-dispute mechanism (§ 5(j)(2))**: new. Under Secretary, AG, or opted-in State AG may challenge overbroad redactions with in camera review.
- **Subcontracting regime (§ 5(d))**: new. GAAIA § 112 was silent on subcontracting; the pass-through-obligations design fills a gap.
- **Frequency floor kept, cadence flexed.** GAAIA § 112(b) hard-coded semi-annual; FRONTIER § 5(f)(1) gives IVO professional-judgment discretion above a 6-month floor.
- **Fee mechanism dropped** (see drafting notes).
- **3-year sunset dropped** (see drafting notes).
- **Whistleblower/retaliation protection dropped** (see drafting notes).
- **IVO license-revocation carve-out added** (§ 3(c)(2)(C)(iv)(I)–(II) — see drafting notes).
- **Immunity structure preserved** (§ 5(q) ≈ GAAIA § 112(r)).

## Policy conversation angles

- **Safety / catastrophic-risk:** The § 5 → § 8 pipe (72-hour referral into emergency-order authority) is the most substantive safety upgrade in the bill; on paper it makes the IVO an early-warning function, not just a compliance checkpoint. But the tier narrowing means the mechanism reaches roughly five companies; smaller labs building CBRN- or cyber-relevant capability sit under § 4's lighter compliance audit and § 4's transparency-report pathway to catastrophic-risk incident reporting, with no IVO tripwire. The dropped sunset is a genuine win for structural continuity; the dropped whistleblower title, the dropped IVO fee mechanism, and the developer-pays market structure remain first-order concerns. Canary's prior CAISI-conducted-audit-backstop ask is not answered; the "no IVO with capacity" clock in § 5(b) is a partial fix for launch timing but not for domain gaps.
- **Innovation / anti-patchwork:** Industry supporters will lean hard on the very-large-tier narrowing (regulatory certainty for the second tier of labs), the § 5(q) immunity shield, the FOIA exemption (§ 5(r)), the § 9 preemption of "third-party auditing and independent verification" state law, and the new § 3(c)(2)(C)(iv) IVO revocation carve-out.
- **State AG / enforcement:** State AGs still get opt-in access to reports (§ 5(k)) plus referrals plus concurrent civil-penalty authority, subject to DOJ preemption when DOJ files. The new redaction-dispute standing in § 5(j)(2) gives opted-in State AGs a real hand in transparency policing that GAAIA lacked.
- **National security:** § 5(r) FOIA exemption plus § 5(m) redaction rules keep assessment contents out of adversary hands but also out of independent-researcher hands. The 72-hour → § 8 pipe gives the Secretary of Commerce a fast switch to suspend or restrict a very-large-tier model — a real national-security lever that GAAIA lacked, though it triggers only on IVO determination and only against the ~5 mega-labs.
