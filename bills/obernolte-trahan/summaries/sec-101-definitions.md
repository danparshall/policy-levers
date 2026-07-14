<!--
Section file: bills/obernolte-trahan/sections/sec-101-definitions.md
Section-by-section: bills/obernolte-trahan/gaaia_section_by_section.txt
Summary written: 2026-07-14
Written by: Claude (Canary Institute automation), YOLO-mode session
-->

# SEC. 101. DEFINITIONS — summary

**One-line:** Establishes the 20 defined terms that carry all of Title I's regulatory weight — most importantly the compute + revenue thresholds that decide which developers are in scope and the harm thresholds that decide which risks count as "catastrophic."

## What it does

Provides the working vocabulary for the entire Act. Two families of definitions matter most: (a) the *who-is-covered* stack (`foundation model` → `frontier model` → `frontier developer` → `large frontier developer`), which mixes a compute threshold with two revenue thresholds to scope the regulated population; and (b) the *what-counts-as-harm* stack (`catastrophic risk`, `critical safety incident`, `acceptable levels of catastrophic risk mitigation`), which sets the substantive trigger for every duty in §§ 111–113.

## Key provisions — the load-bearing thresholds

- **Frontier model:** a foundation model trained with `>10^26` integer or floating-point operations, "including … the original training run … and for any subsequent fine-tuning, reinforcement learning, or other substantial modification" (§ 101(13)).
- **Frontier developer:** entity that (A) trained or initiated training of a frontier model AND (B) had, with all affiliates, `>$50,000,000` in gross revenue in the prior calendar year (§ 101(12)).
- **Large frontier developer:** frontier developer with `>$500,000,000` in prior-year gross revenue, affiliates included (§ 101(15)). Most §§ 111–113 duties attach here, not at the $50M tier.
- **Catastrophic risk:** foreseeable, material risk of death/serious injury to `>50 people` OR `>$1,000,000,000` in property damage, caused by a frontier model (i) uplift on CBRN weapons beyond publicly available info, (ii) autonomous-cyberattack or autonomous crimes (murder, assault, extortion, theft) "with no meaningful human oversight or intervention," or (iii) evading control of the developer or user; excludes lawful federal-government activity (§ 101(6)).
- **Critical safety incident:** unauthorized access/modification/exfiltration of model weights; failure of mitigation measures; or loss of control of a frontier model (§ 101(7)).
- **Acceptable levels of catastrophic risk mitigation:** mitigation "adequate to ensure that the anticipated benefits of a frontier model outweigh its level of catastrophic risk, taking into consideration the probability and magnitude" of each (§ 101(1)). A cost-benefit standard, not a bright line.
- **IVO:** an independent verification organization licensed by CAISI under § 112(c) (§ 101(14)).
- **Model weight:** numerical parameter in a frontier model, adjusted through training, that facilitates input-to-output transformation (§ 101(17)).
- **Material modification** (of the framework): a "significant change" in framework-driven assessment, mitigation, or management (§ 101(16)).
- **Substantial modification** (of the model): a "significant change in how such model is deployed, such as enabling a new fine-tuning capability for, releasing a model weight of, or adding a new feature" that necessitates a new catastrophic-risk assessment (§ 101(20)).
- **Deploy:** making a frontier model available to a third party for use, modification, copying, or combination — but *not* for development or assessment (§ 101(8)).
- **Foundation model:** trained on a broad data set, designed for generality, adaptable to a wide range of tasks (§ 101(10)).
- **Frontier AI framework:** technical and organizational protocols to assess, mitigate, and manage catastrophic risk (§ 101(11)).
- **Audit and assessment:** IVO-conducted review of frontier-developer compliance with §§ 111–112 and of the adequacy of the developer's framework for achieving acceptable mitigation (§ 101(5)).
- **Affiliate:** entity that controls, is controlled by, or is under common control with another through an intermediary (§ 101(2)) — hooks revenue aggregation for the developer thresholds.
- **Artificial intelligence:** open-ended list including systems that operate under uncertainty without oversight, that solve tasks requiring human-like cognition, that are designed to think/act like humans, or that use ML techniques (§ 101(3)).
- **Artificial intelligence model:** the parameter set defining a function mapping inputs to outputs, produced by ML training (§ 101(4)).
- **Director / Property / Open-source community:** CAISI Director per § 102 (§ 101(9)); property is tangible or intangible (§ 101(19)); open-source community covers individuals, foundations, nonprofits, and private-sector entities that develop, contribute to, or publish open-source software (§ 101(18)).

## Who it affects

- **Regulated parties:** the whole substantive Title I is scoped by these definitions. `Frontier developer` (>$50M) is the outer ring; `large frontier developer` (>$500M) is the inner ring where most duties bite. The `>10^26` FLOP threshold sits below the model class; only foundation models above it become "frontier."
- **Empowered actors:** CAISI (as licensor of IVOs), IVOs (as auditors), federal and state AGs (as enforcers under later sections that key off these terms).
- **Beneficiaries:** none directly — this is a definitional section. Downstream sections use the terms to allocate benefits.

## Cross-references

- **Defined terms used:** all 20 terms are self-defined here. Two definitions cross-reference other sections: `Director` → § 102 (§ 101(9)); `IVO` → § 112(c) (§ 101(14)).
- **Depends on / paired with:** every substantive section in Title I (§§ 102, 111, 112, 113, 121, 131, 141) draws from this vocabulary. § 111 keys duties off "large frontier developer" and "frontier AI framework"; § 112 off "IVO" and "audit and assessment"; § 113 off "critical safety incident."

## Notable statutory language

> "The term 'catastrophic risk' … means a foreseeable and material risk of the death of, or serious injury to, more than 50 people, or more than $1,000,000,000 in damage to, or loss of, property, as a result of a frontier model … (i) providing, in the development or release of a chemical, biological, radiological, or nuclear weapon, assistance that is not publicly available; (ii) engaging in conduct with no meaningful human oversight or intervention, that — (I) is a cyberattack; or (II) if such conduct is committed by an individual, would constitute murder, assault, extortion, or theft …; or (iii) evading control of such developer or a user of such model …" (§ 101(6)(A)).

> "The term 'frontier model' means a foundation model trained utilizing a quantity of computing power greater than 10^26 integer or floating-point operations, including computing for the original training run … and for any subsequent fine-tuning, reinforcement learning, or other substantial modification …" (§ 101(13)).

> "The term 'acceptable levels of catastrophic risk mitigation' means risk mitigation adequate to ensure that the anticipated benefits of a frontier model outweigh its level of catastrophic risk, taking into consideration the probability and magnitude of the model's anticipated benefits and catastrophic risks." (§ 101(1)).

## Drafting notes & open questions

- **The `>10^26` FLOP threshold is fixed in statute.** No indexing, no delegated authority to update. If training compute for frontier-class capability drops (algorithmic efficiency, distillation, specialization), the threshold becomes over-inclusive; if it rises, under-inclusive. Compare to the EU AI Act's `>10^25` FLOP tier, which the Commission can adjust by delegated act. Fixing this in primary legislation is unusual and will likely age poorly.
- **The `>$500M` revenue threshold for "large frontier developer" is the real regulatory line.** A well-funded lab under $500M in gross revenue (plausible for many current model developers pre-monetization, though not for OpenAI/Anthropic/Google DeepMind/Meta) is a `frontier developer` but not a `large frontier developer` and escapes most § 111–112 obligations. The section-by-section is explicit that "Large frontier developers (>$500M in revenue) must … publicly post a frontier AI framework" — the sub-$500M tier has almost nothing to do.
- **`Catastrophic risk` is CBRN-plus-cyber-plus-autonomous-crime-plus-loss-of-control.** Notably absent from the enumerated harms: election interference, mass persuasion/manipulation, systemic financial harm, large-scale privacy harm, and civil-rights harm. The `>50 deaths` OR `>$1B property` gate must also be met — a pandemic uplift risk that doesn't cross those thresholds isn't "catastrophic" as defined.
- **"Foreseeable and material" is doing a lot of work.** Combined with the benefits-outweigh-risks framing in § 101(1), the operative standard is closer to a Learned-Hand cost-benefit test than to a precautionary rule. Litigation over "foreseeable" will decide what actually counts.
- **The `acceptable levels` definition is circular in practice.** It requires that "anticipated benefits … outweigh … catastrophic risk," but supplies no methodology, no baseline, and no burden-of-proof rule for who estimates what. IVOs will effectively invent the methodology in early audits.
- **`Material modification` (of framework, § 101(16)) vs. `substantial modification` (of model, § 101(20))** — the near-identical wording invites confusion. Framework changes and model changes trigger different downstream duties; the drafters should either merge or more sharply distinguish these terms.
- **`Deploy` excludes making a model available to a third party "for the development or assessment of such model"** (§ 101(8)(B)). This carve-out is broad and load-bearing — a developer sharing weights with a "red team," an "evaluator," or a "researcher" is not deploying, and downstream deployment duties don't attach. Who qualifies as "assessment" is undefined.
- **`Critical safety incident`** includes "loss of control of such model" (§ 101(7)(C)) with no definition of "loss of control." Given that "evading control" is also an element of `catastrophic risk` (§ 101(6)(A)(iii)), the same undefined concept anchors both the trigger for post-incident reporting and the substantive harm standard.
- **`Artificial intelligence` is defined by an open list ("includes any of the following")** — non-exclusive, which is deliberate and appropriate, but means the outer boundary is set by whatever CAISI/courts decide fits the list.

## Policy conversation angles

- **Innovation / anti-patchwork:** The `>$50M` and `>$500M` revenue tiers exempt startups and mid-size labs from the heaviest obligations, which is a genuine tailoring win for the "don't crush innovation" framing. The `>10^26` FLOP threshold sits above every publicly disclosed training run to date, meaning no currently deployed model is in scope on release — a fact supporters can point to.
- **Safety / catastrophic-risk:** The `catastrophic risk` definition (§ 101(6)) codifies the CBRN + autonomous-cyber + loss-of-control taxonomy that CAIS, MIRI, and Bengio-aligned researchers have argued for. But the `>50 deaths / >$1B property` gate is high — sub-threshold harms (a bio-uplift that kills 40; a cyberattack causing $800M in damage) formally aren't "catastrophic," and the benefits-outweigh-risks framing in § 101(1) is weaker than a precautionary standard.
- **National security:** `Critical safety incident` (§ 101(7)) explicitly names "unauthorized … exfiltration of … model weights" as a reportable event — the first federal statutory recognition of model-weight theft as a distinct harm class. CBRN uplift is enumerated (§ 101(6)(A)(i)), aligning with export-control and BIS concerns.
- **Free speech / civil liberties:** No direct load in § 101, but the *absence* of definitions covering persuasion, manipulation, discriminatory impact, or content harm signals that Title I is not about those risks. Advocates on either side of the speech debate should note that § 101 forecloses reading catastrophic risk to include mass-persuasion harms.
- **State AG / enforcement:** Definitions here are the vocabulary state AGs will litigate against under § 111(e)-(f). The circularity in `acceptable levels of catastrophic risk mitigation` (§ 101(1)) will be the terrain of most enforcement disputes.
