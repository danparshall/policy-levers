<!--
Section file: bills/frontier-act/sections/sec-3-rulemaking.md
Section-by-section: bills/frontier-act/frontier_act_section_by_section.txt
GAAIA analogue: bills/obernolte-trahan/sections/sec-102-center-for-ai-standards-and-innovation.md (§ 5304); § 111(k); § 112(a)/(p)
Summary written: 2026-07-24
Written by: Claude (Canary Institute automation)
-->

# SEC. 3. RULEMAKING — summary

**One-line:** Vests the Under Secretary of Commerce for AI Security with notice-and-comment rulemaking authority to implement the Act, imposes three mandatory 180-day rulemakings, and — critically — lets the Under Secretary raise (but not lower) the compute, revenue, and expenditure thresholds that define who is covered.

## What it does

Section 3 is the Act's plumbing. All regulations must follow 5 USC § 553 notice-and-comment (§ 3(a)). The Under Secretary must promulgate three regulations within 180 days of enactment: minimum requirements for frontier AI frameworks (§ 3(b)) that feed § 4; IVO licensing and oversight rules (§ 3(c)) that feed § 5; and criteria for what counts as a "substantial modification" of a model and a "material modification" of a framework (§ 3(d)) — the triggers that pull disclosure duties in § 4 into gear. It also gives the Under Secretary discretionary authority (§ 3(e)) over report formats, redaction procedures, and State AG opt-in mechanics, and — most consequentially — authority (§ 3(f)) to increase the compute, revenue, and expenditure coverage thresholds by rule.

## Key provisions

- **Three 180-day rulemakings** — frontier AI framework minima (§ 3(b)(1)); IVO licensing (§ 3(c)); modification criteria (§ 3(d)).
- **Framework rulemaking must at minimum address each § 4(a) requirement** (§ 3(b)(2)); annual periodic review required (§ 3(b)(3)).
- **IVO rulemaking must cover:** conflict-of-interest and funding transparency (§ 3(c)(1)); application procedures, license findings, and revocation findings (§ 3(c)(2)); minimum assessment requirements (§ 3(c)(3)); corrective action / loss-of-license provisions (§ 3(c)(4)); secure submission of assessment reports (§ 3(c)(5)); catch-all (§ 3(c)(6)).
- **Threshold adjustment — one-way ratchet (§ 3(f)):** the Under Secretary may only *increase* the 10^26-op compute threshold (§ 2(l)) and the $50M/$5B revenue and $1B/$10B expenditure thresholds (§§ 2(o), 2(v)). Calibration standard is "encompass the artificial intelligence models and developers whose activities present catastrophic risk, and do not encompass those whose activities do not" (§ 3(f)(2)). Biennial review required (§ 3(f)(3)).
- **Prospective-only effective date:** threshold rules take effect no earlier than 180 days after publication in final form and apply only to obligations arising on or after effective date (§ 3(f)(4)).

## Who it affects

- **Regulated parties:** Frontier developers (10^26-op threshold, § 2), large frontier developers ($50M revenue + $1B expenditure), very large frontier developers ($5B + $10B). Also IVOs seeking licensure under § 5.
- **Empowered actor:** Under Secretary of Commerce for AI Security — the entire Act's rulemaking authority is concentrated in this one office.
- **Beneficiaries / affected downstream:** State AGs (their opt-in mechanics are set by rule, § 3(e)(3)); developers that redact reports (justification standards are set by rule, § 3(e)(2)).

## Cross-references

- **Defined terms used:** "frontier AI framework" (§ 2(n)); "IVO" (§ 2(q)); "substantial modification" (§ 2(t)); "material modification" (§ 2(p)); "Under Secretary" (§ 2(w)); "acceptable levels of catastrophic risk mitigation" (§ 2(a)).
- **Depends on / paired with:** § 4 (framework and reporting duties can't fully operate until the § 3(b) minima and § 3(d) modification criteria issue); § 5 (IVO regime can't operate until § 3(c) rules issue); § 2 (thresholds § 3(f) may adjust).

## Notable statutory language

> "The Under Secretary may by regulation increase—(A) the threshold quantity of computing power specified in subsection (l) of section 2; or (B) the threshold amounts of gross revenues and AI-related development expenditures specified in subsections (o) and (v) of section 2." (§ 3(f)(1))

The word "increase" is load-bearing — the Under Secretary has no statutory authority to lower any threshold by rule, no matter what algorithmic-efficiency or hardware-efficiency data reveal.

## Drafting notes & open questions

- **One-way ratchet is a design choice, not an oversight.** § 3(f)(2) explicitly directs calibration to "encompass the artificial intelligence models and developers whose activities present catastrophic risk, and do not encompass those whose activities do not, taking into account advances in algorithmic and hardware efficiency" — yet the operative verb in § 3(f)(1) is "increase." If algorithmic efficiency renders a 10^25-op training run as capable as today's 10^26-op run, the Under Secretary can only respond by *raising* the compute threshold (removing more developers from coverage), never by lowering it (pulling in newly-dangerous smaller developers). If Congress intended calibration in both directions, the statute needs a corresponding "decrease" authority.
- **No consultation requirement.** § 3 does not require the Under Secretary to consult with academia, the open-source community, private-sector entities, public-sector entities, or international-standards bodies before issuing any of these rules. GAAIA § 111(k)(3) and § 112(p)(3) both required stakeholder consultation; FRONTIER dropped it. This is not a drafting oversight — FRONTIER § 3 has no consultation clause at all.
- **No sunset on the rulemaking authority.** GAAIA § 111(k)(5) sunsetted the rulemaking authority after 3 years (except ministerial corrections). FRONTIER § 3 has no analogous sunset — the Under Secretary's authority is permanent unless Congress amends.
- **Fees are absent.** GAAIA § 102(f) authorized CAISI to establish and collect fees from IVOs and large developers by rule (§ 102(f)(4)); GAAIA § 112(n) required IVO application and renewal fees sufficient to offset admin costs. Neither appears in FRONTIER § 3. The IVO catch-all in § 3(c)(6) ("any other rules reasonably necessary to the administration of the IVO oversight and licensing regime") arguably reaches fees, but the explicit fee authority is gone. If IVO licensing is to be self-funding, someone will need to argue that § 3(c)(6) carries it.
- **Public-availability requirement dropped.** GAAIA § 111(k)(4) / § 112(p)(4) required regulations to be posted on NIST/CAISI's website. FRONTIER § 3 requires only that threshold-review determinations be posted on a Commerce website (§ 3(f)(3)); the rules themselves have no publication requirement beyond the Federal Register default of § 553.

## Changes vs GAAIA discussion draft (2026-06-04)

FRONTIER § 3 consolidates rulemaking authority that GAAIA scattered across three sections — GAAIA § 102 (§ 5304(c)(1)(X) IVO licensing), GAAIA § 111(k) (transparency), and GAAIA § 112(a) and (p) (IVO audit regime). Cleaner drafting on its face. But several substantive shifts:

- **Rulemaker changed.** GAAIA vested the rulemaking authority in the CAISI Director (appointed by the Secretary of Commerce under § 5304(b), no Senate confirmation, housed at NIST). FRONTIER vests it in the Under Secretary of Commerce for AI Security (§ 2(w)) — a new Under Secretary–grade position that would typically require presidential appointment with Senate confirmation. Higher political accountability, slower to stand up (Senate confirmations on AI policy positions have taken 8–14 months in prior sessions), and structurally more insulated from career technical staff at NIST.
- **Threshold adjustment authority is new.** GAAIA § 111(j)(2)(A)(ii) only directed the Director to *recommend* updated definitions to Congress; actual updates required legislation. FRONTIER § 3(f) hands the Under Secretary unilateral rulemaking authority to raise thresholds — with no counterpart authority to lower them. This is a meaningful transfer of power from Congress to the executive that has no direct GAAIA analogue.
- **Consultation dropped.** GAAIA § 111(k)(3) and § 112(p)(3) both required consultation with academia, open-source community, private-sector, and public-sector stakeholders. FRONTIER § 3 requires none.
- **3-year sunset dropped.** GAAIA § 111(k)(5) sunsetted the rulemaking authority; FRONTIER does not.
- **Fee authority dropped.** GAAIA § 102(f) and § 112(n) both authorized fees; FRONTIER § 3 does not.
- **Public-availability requirement dropped.** GAAIA § 111(k)(4) / § 112(p)(4) required NIST/CAISI to post regulations; FRONTIER § 3 does not.

Note also that GAAIA § 111(k)(2)(C) — rulemaking on "thresholds, methodologies, and other considerations applicable to the assessment, mitigation, and management of catastrophic risk" — is picked up in FRONTIER § 3(b) via the framework-minima rulemaking, which "shall, at a minimum, address each of the requirements of section 4(a)." Coverage of substance appears intact, though the specific wording is now indirect.

## Policy conversation angles

- **Innovation / anti-patchwork:** Rulemaking consolidation into a single Under Secretary supports a "one federal regulator" narrative and simplifies the compliance surface. Prospective-only effective dates (§ 3(f)(4)) provide investment certainty. Notice-and-comment through 5 USC § 553 gives industry a formal channel to influence rules.
- **Safety / catastrophic-risk:** The one-way threshold ratchet in § 3(f) is the single biggest concern. If algorithmic and hardware efficiency continues on trend, catastrophic-risk-capable models will be trainable well below 10^26 ops within the Act's lifespan; the Under Secretary has no authority to respond. The absence of a mandatory-consultation clause also cuts off the safety-research community's formal seat at the rulemaking table that GAAIA had preserved.
- **Congressional oversight:** Threshold-raising authority under § 3(f) is a delegation to the executive that GAAIA did not make. Members concerned about executive discretion over who is covered by the Act should note this shift. The biennial review-and-publish requirement (§ 3(f)(3)) creates a public record but not a Congressional-approval gate.
- **State AG / enforcement:** The opt-in mechanics for State AGs to receive § 4 and § 5 reports are set by rule under § 3(e)(3), not statute. State AGs will need to engage the rulemaking to ensure the transmission procedures are workable and secure.
