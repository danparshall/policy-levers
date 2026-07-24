<!--
Section file: bills/frontier-act/sections/sec-9-relationship-to-state-laws.md
Section-by-section: bills/frontier-act/frontier_act_section_by_section.txt
GAAIA analogue: bills/obernolte-trahan/sections/sec-121-federalization-of-state-laws-regulating.md
Summary written: 2026-07-24
Written by: Claude (Canary Institute automation)
-->

# SEC. 9. RELATIONSHIP TO STATE LAWS — summary

**One-line:** Preempts state or local laws that impose "new substantive obligations" on AI developers in three defined governance functions — frontier-risk transparency, third-party auditing / independent verification, and incident reporting — while preserving generally applicable laws, deployer/user regulation, minor-protection laws, and state procurement rules; no sunset, no severability clause.

## What it does

Section 9 defines a "Covered Subject Area" (§ 9(a)) as the three federally-occupied governance functions of frontier AI safety: (1) developer disclosure about catastrophic-risk policies, testing methodologies, and model characteristics; (2) third-party assessment, audit, certification, attestation, or verification of a developer's catastrophic-risk activities, policies, or compliance; and (3) developer reporting of safety/security incidents to any governmental entity. Section 9(b) then bars any State or political subdivision from adopting or enforcing "any law, regulation, order, or other requirement that imposes new substantive obligations on artificial intelligence developers with respect to any Covered Subject Area." A rule of construction (§ 9(c)) carves four spaces out of that preemption, and § 9(d) supplies a self-contained definition of "artificial intelligence developer" that excludes pure deployers.

## Key provisions

- **Function-scoped preemption (§ 9(b)):** Preemption fires only against "new substantive obligations" on developers within the three enumerated Covered Subject Areas — not against all state regulation of AI model development.
- **Rule-of-construction carve-outs (§ 9(c)):** Preserved are (1) generally applicable laws that "do not target artificial intelligence developers"; (2) "regulate the use or deployment of AI systems by deployers or users, including via consumer protection, civil rights, contract, criminal, or privacy laws, provided that no substantive obligations are imposed on developers with respect to model development, training, evaluation, or release"; (3) laws "specifically relating to the protection of minors from harms arising from the use of AI systems, including . . . sexually explicit content, content promoting self-harm, content facilitating exploitation, age verification, parental controls, or similar matters"; and (4) state procurement and government-use rules.
- **Developer definition (§ 9(d)):** Any entity that "builds, designs, codes, produces, trains, or owns" an AI model for internal or third-party use; expressly "does not include an entity that is solely a deployer."
- **No sunset.** Unlike GAAIA § 121(d), § 9 contains no expiration date. Verified by full-text search of the enrolled bill — the words "sunset," "cease to have effect," and "expires" do not appear anywhere in the FRONTIER Act.
- **No severability clause.** The bill contains no severability language; if a court invalidates § 4 or § 5, the preemption trade is not textually linked to the substantive federal duties.

## Who it affects

- **Regulated parties (indirectly benefited):** All AI developers as defined in § 9(d) — but the practical bite is on frontier developers subject to California SB-53 (Frontier AI Transparency Act), New York's RAISE Act, and Illinois SB-315, which the sponsors' section-by-section names explicitly as the "closely related State frontier-safety statutes" § 9 is aimed at.
- **Displaced actors:** State legislatures and AGs enforcing state frontier-safety statutes on transparency, third-party audit, and incident reporting. Their authority over deployment, use, minor protection, procurement, and generally applicable law survives.
- **Empowered actors (indirectly):** The Under Secretary and federal AG, plus opted-in State AGs acting *under* federal §§ 4 and 5 — see interaction note below.

## Cross-references

- **Defined terms used:** § 9 supplies its own "artificial intelligence developer" definition rather than adopting the § 2 "frontier developer" (10²⁶-op) threshold. This is important — § 9's preemption reach is not limited to frontier developers, so a state law imposing catastrophic-risk transparency duties on a sub-frontier developer is also preempted.
- **Depends on / paired with:** § 4 (transparency and reporting), § 5 (independent verification), § 8 (emergency orders). Together these three substitute a federal frontier-safety regime for the state regimes § 9 displaces; § 9's substantive occupancy of the field is the tradeoff for federal duties elsewhere in the Act.

## Notable statutory language

> "Except as provided in subsection (c), no State or political subdivision of a State may adopt or enforce any law, regulation, order, or other requirement that imposes new substantive obligations on artificial intelligence developers with respect to any Covered Subject Area." (§ 9(b))

> "regulate the use or deployment of AI systems by deployers or users, including via consumer protection, civil rights, contract, criminal, or privacy laws, provided that no substantive obligations are imposed on developers with respect to model development, training, evaluation, or release" (§ 9(c)(2))

## Drafting notes & open questions

- **The sunset is gone.** GAAIA § 121(d) sunset preemption after 3 years unless reauthorized — this was, per Canary's June read, "the section's most-noted structural feature." FRONTIER § 9 makes the preemption permanent. This is the single largest substantive change in this section.
- **No severability, and no explicit inseverability either.** Canary flagged in June that GAAIA § 121 lacked severability and that inseverability with §§ 111/112 was a Canary ask so litigation could not decouple the federal-duties/preemption trade. FRONTIER § 9 carries the same absence forward. If a court invalidates § 4 or § 5, states may find themselves with no federal frontier-safety regime *and* no ability to legislate one — the worst-case bargain if either federal duty falls.
- **"Imposes new substantive obligations" is not settled preemption art.** The phrase is narrower than GAAIA's "specifically regulating the development" but broader than "conflicts with" — it appears designed to preserve enforcement authority (states can enforce federal law under §§ 4(f) and 5) while barring parallel substantive state duties. "New" is doing subtle work: it suggests existing state duties enacted pre-enactment survive until amended, but subsection (b) also bars "enforce," which cuts the other way. Litigants will fight over whether SB-53 is a "new substantive obligation" preempted at enforcement or a pre-existing statute enforceable as of enactment.
- **§ 9(a)(1) transparency is defined extremely broadly.** It reaches disclosure of "characteristics, capabilities, training, or deployment of an AI model, where the disclosure relates to the assessment, monitoring, communication, or mitigation of catastrophic risks." That is nearly co-extensive with the SB-53 / RAISE / IL SB-315 substantive obligations, so the "narrower scope than GAAIA" framing (see below) should not be oversold — in the space where states are actually legislating, the preemption is comprehensive.
- **Explicit target-law naming in the section-by-section is politically unusual.** Sponsors' section-by-section documents rarely name-check the specific state statutes they intend to displace. The FRONTIER s-by-s names CA SB-53, NY RAISE, and IL SB-315 by initials — a clear signal that § 9 is not incidental preemption but a targeted displacement, and one that will feature in the political framing on both sides.
- **§ 9 does not touch federal-agency preemption.** FTC, CFPB, EEOC, SEC AI enforcement under existing federal statutes is unaffected; only state action in the Covered Subject Areas is preempted.

## Changes vs GAAIA discussion draft (2026-06-04)

Direct analogue: GAAIA § 121 (Federalization of State Laws Regulating AI Model Development). Every substantive change is worth flagging:

- **Scope: DEVELOPMENT-scoped → FUNCTION-scoped.** GAAIA § 121(b) preempted "any law or regulation specifically regulating the development of any artificial intelligence model" — a category defined broadly in § 121(e)(3) to include training-objective determination, weight modification, and pre-deployment safety-threshold evaluation. FRONTIER § 9(b) preempts only "new substantive obligations . . . with respect to any Covered Subject Area," where the three Covered Subject Areas are transparency, third-party audit, and incident reporting. In principle, state legislation on AI model development that is *not* in one of the three functional categories (e.g., environmental review of training compute, labor-relations rules for AI-development workforces, non-catastrophic-risk-related training-data provenance rules) is no longer preempted. In practice, the three functions are exactly the space where states are actively legislating on frontier safety, so the practical narrowing is smaller than the textual narrowing suggests.
- **Sunset dropped.** GAAIA § 121(d) sunset the preemption at 3 years unless reauthorized. FRONTIER § 9 has no sunset. This is a material shift — the preemption trade becomes permanent rather than time-limited.
- **Explicit protection-of-minors carve-out (§ 9(c)(3)) added.** GAAIA § 121(c) had no analogous minor-protection carve-out. This is a new, politically salient express preservation — CSAM, self-harm content, and age-verification laws are explicitly outside preemption.
- **Explicit procurement carve-out (§ 9(c)(4)) added.** GAAIA § 121(c) did not name procurement; FRONTIER § 9 does. Likely responsive to state and municipal AI procurement rules already in force.
- **"General applicability" carve-out sharpened.** GAAIA § 121(c)(1) preserved laws "of general applicability" and common-law remedies. FRONTIER § 9(c)(1) preserves generally applicable laws that "do not target artificial intelligence developers." The new language is more restrictive on the states — a general consumer-protection statute is fine, but a general-looking statute that in fact targets developers is not. Common-law remedies are not textually preserved here but presumably fall within (c)(1) or (c)(2).
- **State AG carve-out reworked (indirect).** GAAIA § 121(c)(3) expressly preserved state authority granted under the Act. FRONTIER § 9(c) has no analogous "authority granted under this Act" clause — but §§ 4(f) and 5(d) themselves grant opted-in State AGs enforcement authority over the federal duties, so the AG opt-in is a federal-authority grant rather than preserved state substantive authority. The mechanism is compatible with § 9's substantive preemption (states have no independent substantive authority in the Covered Subject Areas, but carry federal water when they opt in).
- **New interaction with § 8 exclusivity.** GAAIA had no § 8 emergency-order authority. FRONTIER § 8 declares itself the "exclusive means by which any federal actor may restrict a frontier model on imminent-catastrophic-risk grounds." Combined with § 9's occupancy of the transparency/audit/incident space, the result is a very tight architecture: the Commerce Secretary is the sole federal responder on imminent catastrophic risk, and states cannot legislate substantive frontier-safety obligations. That two-sided closure is entirely new relative to GAAIA and is the deepest structural change in this preemption slice.

## Policy conversation angles

- **Innovation / anti-patchwork:** Supporters will foreground the function-scoping and the four carve-outs as evidence this is not a blunt preemption. The rule of construction is unusually explicit — general laws, deployer/user regulation, minor protection, and state procurement are all expressly preserved. Contrast with GAAIA § 121, which was development-scoped and correspondingly broader.
- **Safety / catastrophic-risk:** The Bengio/CAIS-worldview read is that the preemption is now permanent (no sunset), the substantive occupancy in the space where states are actually legislating is essentially total, and there is no severability protection — so if § 4 or § 5 is struck down or diluted in markup, states are left with neither a federal frontier-safety regime nor the authority to build one. The 3-year sunset in GAAIA was a partial safety valve against exactly that failure mode; FRONTIER removes it.
- **State AG / enforcement:** State AGs retain enforcement teeth under §§ 4(f) and 5(d) — up to $1M per violation per day for opted-in AGs, on federal duties. What they lose is the ability to bring state-law actions on developer catastrophic-risk transparency, audit compliance, or incident reporting. Cooperative-federalism enforcement, substantive federal-only law.
- **Free speech / civil liberties:** Model-output regulation (deepfakes, election content, NCII, CSAM) is deployer/user-side and preserved under § 9(c)(2). The added § 9(c)(3) minor-protection carve-out is textually broader than the deployer/user carve-out and explicitly reaches "sexually explicit content, content promoting self-harm, content facilitating exploitation, age verification, parental controls" — a deliberate political concession to state child-safety statutes.
