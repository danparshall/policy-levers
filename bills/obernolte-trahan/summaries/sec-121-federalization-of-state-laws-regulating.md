<!--
Section file: bills/obernolte-trahan/sections/sec-121-federalization-of-state-laws-regulating.md
Section-by-section: bills/obernolte-trahan/gaaia_section_by_section.txt
Summary written: 2026-07-14
Written by: Claude (Canary Institute automation), YOLO-mode session
-->

# SEC. 121. FEDERALIZATION OF STATE LAWS REGULATING AI MODEL DEVELOPMENT — summary

**One-line:** Preempts any state or local law "specifically regulating the development of any artificial intelligence model," preserves general-applicability laws / common-law remedies / all post-deployment regulation / state authority under GAAIA itself, and sunsets in 3 years unless reauthorized.

## What it does

Congress makes a Commerce Clause finding (§ 121(a)) that AI model development is a matter of national economic significance and international competitiveness requiring uniform federal oversight, then in § 121(b) bars any State or political subdivision from establishing, continuing in effect, or enforcing "any law or regulation specifically regulating the development of any artificial intelligence model." Three rules of construction (§ 121(c)) carve out laws of general applicability, common-law remedies, all post-deployment activities, and state authority granted elsewhere in the Act. The preemption sunsets 3 years after enactment (§ 121(d)) unless Congress reauthorizes.

## Key provisions

- **Preemption scope (§ 121(b)):** "law or regulation specifically regulating the development" — reaches statutes, regulations, and enforcement actions; covers both new and existing laws (bars "continue in effect").
- **General-applicability carve-out (§ 121(c)(1)):** State consumer-protection statutes, biometric-privacy laws (BIPA-style), unfair-competition acts, and common-law tort / products-liability remedies survive.
- **Post-deployment carve-out (§ 121(c)(2)):** Any state law reaching "implementation, deployment, distribution, offering, or use" of an AI system, product, or service that incorporates or is derived from an AI model is not preempted. Colorado SB 24-205, NYC Local Law 144 (AEDT), and state deepfake/impersonation statutes are deployment-side and survive.
- **State-AG carve-out (§ 121(c)(3)):** State authority granted under GAAIA — the § 111 CSIR opt-in, § 112 IVO-report opt-in, and derivative enforcement authority — is preserved.
- **Sunset (§ 121(d)):** Preemption "shall cease to have effect" 3 years after enactment unless Congress reauthorizes prior to that date.
- **Local definitions (§ 121(e)):** "Deploy" = making a model available for use, copying, or combination with other software; "developer" = person/entity that determines training or fine-tuning objectives AND performs or directs training, fine-tuning, or substantial weight modification prior to deployment; "development" = pre-deployment acts by a developer, expressly including determining training objectives, training/fine-tuning/modifying weights, AND "evaluating and deciding, prior to deployment, whether an AI model satisfies applicable safety or capability thresholds for deployment."

## Who it affects

- **Regulated parties (indirectly benefited):** All AI developers, but the practical bite is on frontier developers presently subject to state-level pre-deployment obligations — most conspicuously California SB 53 (Frontier AI Transparency Act, 2025), which imposes framework publication and critical-safety-incident reporting on frontier developers. § 121 is not named at SB 53 but the fit is exact.
- **Displaced actors:** State legislatures, state AGs enforcing state AI-development laws, city councils. Their post-deployment authority is intact; their pre-deployment authority is not.
- **Empowered actors:** CAISI (§ 102) and federal AGs, plus state AGs acting *under GAAIA's* opt-in provisions.

## Cross-references

- **Defined terms used:** § 121 supplies its own "deploy" / "developer" / "development" definitions in § 121(e) rather than borrowing from § 101 — those § 101 terms ("frontier developer," "large frontier developer," "material modification") do not govern the preemption scope. This is a self-contained definitional package.
- **Depends on / paired with:** § 111 (transparency), § 112 (IVO), § 113 (whistleblower). Together these substitute a federal development-side regime for the state regimes § 121 displaces; if §§ 111–112 are diluted in markup, § 121 still fires as written and states have less to fall back on.

## Notable statutory language

> "No State or political subdivision thereof may establish, continue in effect, or enforce any law or regulation specifically regulating the development of any artificial intelligence model." (§ 121(b))

> "'[D]evelopment' means the acts performed or directed by a developer with respect to an artificial intelligence model prior to its deployment, including determining training or fine-tuning objectives; training, fine-tuning, or otherwise substantially modifying the weights or other parameters of an artificial intelligence model; and evaluating and deciding, prior to deployment, whether an artificial intelligence model satisfies applicable safety or capability thresholds for deployment." (§ 121(e)(3))

## Drafting notes & open questions

- **Bill text says "specifically regulating"; section-by-section says "specifically targeting."** These are not synonyms in preemption practice. "Specifically regulating" tracks the (b) text and is the operative phrase; the Trahan section-by-section is a paraphrase. Worth flagging in briefings — reporters and members quoting the summary will be quoting language that is not in the bill.
- **"Specifically regulating" is not a term of art with settled case law.** Analogous formulations ("specifically directed at" in *Cipollone*, "relates to" in ERISA, "with respect to" in the ADA) each generated decades of litigation. This phrasing is fresh, and the line between "specifically regulating development" and "of general applicability that incidentally reaches development" is where every fight will land.
- **The develop/deploy line is load-bearing and porous.** § 121(e)(3) sweeps pre-release safety-and-capability evaluation into "development." A state law requiring pre-deployment red-team disclosures = preempted. A state law regulating training-data provenance, including copyright-inflected regimes = preempted (it targets training). But a state law on model *outputs* observed in commercial use = not preempted (deployment). Litigants will test whether liability regimes that fire on training-data ingestion escape preemption by pleading downstream harm.
- **Sunset mechanism is silent on revival.** § 121(d) says the section "shall cease to have effect" after 3 years absent reauthorization. Textually, state laws that were barred from being "continue[d] in effect" during years 1–3 should be enforceable again on day one of year 4 — but the section does not affirmatively revive them, and states that repealed pre-empted statutes during the window would have to re-enact. If the federal framework fails to stand up, this is a soft-landing to state authority rather than a cliff, but the mechanics will be litigated.
- **Nothing in § 121 addresses federal-agency preemption.** The section preempts states, not FTC / CFPB / EEOC / SEC AI enforcement — federal actors retain everything they have today.

## Policy conversation angles

- **Innovation / anti-patchwork:** This is the section Rep. Houchin's press-release quote foregrounds. Supporters will frame § 121 as the price of admission for a coherent federal regime: developers can't comply with 50 different pre-deployment testing rules, and states retain everything downstream. The carve-outs are unusually clean — common law preserved, general-applicability preserved, all deployment preserved — which is designed to defuse the standard preemption objection.
- **Safety / catastrophic-risk:** Substitutes federal §§ 111–112 for CA SB 53 and any successor state pre-deployment regime. The safety case for § 121 rises or falls with whether §§ 111–112 as enacted are stronger than what states are producing. Progressive-Democratic senators wary of preemption will read § 121 as a floor-not-ceiling failure — the federal duties are development-side transparency, not development-side prohibition, so states are trading concrete disclosure regimes for a federal one with the same shape. Advocates of the Bengio / CAIS worldview will note the 3-year sunset partially mitigates the lock-in objection, but only if the sunset is credible against the political economy of reauthorization.
- **State AG / enforcement:** § 121(c)(3) is the key concession to state enforcement authority. State AGs can still receive § 111 critical-safety-incident reports, receive § 112 IVO audit reports, and pursue enforcement under those federal duties. They cannot bring parallel state-law actions on development-side conduct. This is a "cooperative federalism" enforcement design paired with substantive preemption.
- **Free speech / civil liberties:** Model-output regulation is deployment-side and survives; state laws on AI-generated CSAM, election deepfakes, and non-consensual intimate imagery are not touched.
