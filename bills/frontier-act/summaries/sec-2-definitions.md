<!--
Section file: bills/frontier-act/sections/sec-2-definitions.md
Section-by-section: bills/frontier-act/frontier_act_section_by_section.txt
GAAIA analogue: bills/obernolte-trahan/sections/sec-101-definitions.md
Summary written: 2026-07-24
Written by: Claude (Canary Institute automation)
-->

# SEC. 2. DEFINITIONS — summary

**One-line:** Establishes the 22 defined terms that carry all of the Act's regulatory weight — most importantly a new three-tier developer stack keyed to AI-development expenditures (not revenue alone), a broadened catastrophic-risk taxonomy, and a new "Under Secretary of Commerce for AI Security" as the administering officer.

## What it does

Supplies the working vocabulary for the entire Act. Three families of definitions carry the load: (a) the *who-is-covered* stack (`foundation model` → `frontier model` → `frontier developer` → `large frontier developer` → `very large frontier developer`), which combines a compute threshold with tiered revenue-plus-expenditure floors; (b) the *what-counts-as-harm* stack (`catastrophic risk`, `imminent catastrophic risk`, `critical safety incident`, `acceptable levels of catastrophic risk mitigation`); and (c) the *who-administers* stack (`Secretary`, `Under Secretary`), which relocates administration from a NIST center to a new Commerce sub-cabinet officer.

## Key provisions — the load-bearing thresholds

- **Frontier model:** foundation model trained with `>10^26` integer or floating-point operations, counting "computing for the original training run and for any subsequent fine-tuning, reinforcement learning, or other substantial modification" (§ 2(12)).
- **Frontier developer:** entity in interstate/foreign commerce that has trained or initiated training of a frontier model — no revenue floor at this tier (§ 2(11)).
- **Large frontier developer:** with affiliates, over the "preceding 36-month period, determined as of the first day of each calendar month," had `>$50,000,000` in gross revenues *and* `>$1,000,000,000` in AI-related development expenditures (§ 2(15)).
- **Very large frontier developer:** same 36-month/affiliate measurement, `>$5,000,000,000` in gross revenues *and* `>$10,000,000,000` in AI-related development expenditures (§ 2(22)). Only this tier triggers § 5 IVO assessment.
- **AI-related development expenditures:** amounts "paid or incurred in interstate or foreign commerce, without regard to whether such amounts are expensed, capitalized, deducted, or amortized for financial reporting or tax purposes, that are attributable to artificial intelligence development, training, fine-tuning, modification, security, or evaluation" (§ 2(4)). Cross-cutting new term — captures spend regardless of accounting treatment, so lab-in-a-holding-company structures cannot escape by choice of expense classification.
- **Catastrophic risk:** foreseeable, material risk that a frontier developer's development, storage, use, or deployment of a frontier model materially contributes to `>50` deaths/serious injuries or `>$1B` property damage in a single incident, arising from the model (i) providing CBRN-or-cyber-weapon assistance "not publicly available," (ii) autonomously conducting a cyberattack or acts that would be murder/assault/extortion/theft, or (iii) evading control (§ 2(6)(A)). Carve-outs: outputs "otherwise publicly accessible in a substantially similar form from a source other than a foundation model," lawful federal activity, and harm to which the model "did not materially contribute" (§ 2(6)(B)).
- **Imminent catastrophic risk:** "a present or impending catastrophic risk" (§ 2(13)). Predicate for § 5 mandatory IVO referral within 72 hours and § 8 emergency orders.
- **Critical safety incident:** unauthorized weight access/modification/exfiltration; harm from a materialized catastrophic risk; loss of control; *or* "a frontier model using deceptive techniques against its frontier developer to subvert the controls or monitoring of such developer, outside the context of an evaluation designed to elicit such behavior, in a manner that demonstrates materially increased catastrophic risk" (§ 2(7)(D)).
- **Under Secretary:** the "Under Secretary of Commerce for AI Security, who shall be appointed by the Secretary" (§ 2(21)). Holds all rulemaking authority (§ 3), receives filings and incident reports (§ 4), and licenses IVOs (§ 5).
- **Assessment:** IVO review of a *very large* developer's framework, governance, risk-monitoring, and mitigation for achieving acceptable mitigation (§ 2(5)). Note: no separate "audit" term — the § 4(b) annual audit is done by an "independent third party," not an IVO.
- **Foundation model / frontier AI framework / IVO / model weight / material modification / substantial modification / affiliate / deploy / property:** carry the definitional vocabulary for §§ 3–5 duties. `Property` now explicitly excludes "loss of value of equity" (§ 2(18)(B)) — a carve-out for stock-price drops.
- **AI / artificial intelligence / artificial intelligence model:** cross-referenced to 15 U.S.C. 9401 (NAIIA 2020 § 5002) (§ 2(3)) rather than defined in the bill.

## Who it affects

- **Regulated parties:** three concentric rings. Any developer of a `>10^26` FLOP foundation model is a *frontier developer* (transparency, incident reporting, deployment reports). *Large frontier developers* (`>$50M`/`$1B`) add the frontier AI framework, annual audit, and registry duties. *Very large frontier developers* (`>$5B`/`$10B`) add ongoing IVO assessment.
- **Empowered actors:** the new Under Secretary of Commerce for AI Security (rulemaking, licensing, receipt of filings); IVOs (independent verification); the Secretary of Commerce (§ 8 emergency orders); the Attorney General and opted-in State AGs (enforcement).
- **Beneficiaries:** none directly — this is definitional.

## Cross-references

- **Defined terms used:** all 22 are self-defined here. Three cross-reference other sections or statutes: `AI/AI model` → 15 U.S.C. 9401 (§ 2(3)); `assessment` → § 5 (§ 2(5)); `IVO` → §§ 5(c), 3(c) (§ 2(14)).
- **Depends on / paired with:** every substantive section keys off this vocabulary. § 3 (rulemaking, threshold adjustment) turns on `frontier developer`, `large`, `very large`, and `AI-related development expenditures`. § 4 (transparency/incident reporting) keys off `large frontier developer`, `critical safety incident`, `frontier AI framework`. § 5 (IVO) keys off `very large frontier developer`, `assessment`, `imminent catastrophic risk`. § 8 (emergency orders) keys off `imminent catastrophic risk`.

## Notable statutory language

> "The term 'AI-related development expenditures' means amounts paid or incurred in interstate or foreign commerce, without regard to whether such amounts are expensed, capitalized, deducted, or amortized for financial reporting or tax purposes, that are attributable to artificial intelligence development, training, fine-tuning, modification, security, or evaluation." (§ 2(4)).

> "The term 'catastrophic risk' means — (A) a foreseeable and material risk that a frontier developer's development, storage, use, or deployment of a frontier model will materially contribute to the death of, or serious injury to, more than 50 people, or more than $1,000,000,000 in damage to, or loss of, property, arising from a single incident involving a frontier model doing any of the following: (i) providing, in the development or release of a chemical, biological, radiological, nuclear, or cyber weapon, assistance that is not publicly available …" (§ 2(6)(A)).

> "A frontier model using deceptive techniques against its frontier developer to subvert the controls or monitoring of such developer, outside the context of an evaluation designed to elicit such behavior, in a manner that demonstrates materially increased catastrophic risk." (§ 2(7)(D)).

> "The term 'Under Secretary' means the Under Secretary of Commerce for AI Security, who shall be appointed by the Secretary." (§ 2(21)).

## Drafting notes & open questions

- **The `>10^26` FLOP threshold is still fixed in statute** (§ 2(12)), though § 3 now delegates authority to the Under Secretary to raise compute, revenue, and expenditure thresholds by rule "calibrated to reach the developers whose activities present catastrophic risk." That partially cures the age-poorly problem the GAAIA definition had — but only upward. If sub-`10^26` capability emerges, no relief valve to expand coverage.
- **AI-related development expenditures does most of the work of the new tier structure.** By keying on cumulative training/eval spend rather than revenue alone, the drafters catch well-funded pre-revenue labs (Anthropic circa 2023, xAI at founding) that GAAIA's revenue-only $500M line would have missed. The 36-month rolling window means a lab crosses the line once cumulative spend does, without waiting for a fiscal year to close.
- **The `>$10B expenditure` threshold for very large frontier developer is very high.** As of mid-2026 disclosures, the developers plausibly over `$10B` in three-year AI spend are OpenAI, Google/DeepMind, Meta, Microsoft, xAI, and Anthropic. § 5 IVO assessment attaches to that small set — the entire IVO regime is a big-6-plus governance layer, not a broad frontier regime.
- **`Imminent catastrophic risk`** (§ 2(13)) is defined circularly as "a present or impending catastrophic risk." "Impending" carries all the definitional weight; there's no probability floor, no time horizon, and no burden-of-proof rule. Given that this is the predicate for § 8 emergency suspensions, the vagueness is load-bearing and will be litigated.
- **The § 2(7)(D) "deceptive techniques" incident trigger** is genuinely new and important — it treats an evaluation-context vs. deployment-context distinction as material. If a model schemes inside an eval designed to elicit it, that's science; if the same behavior surfaces outside such an eval and shows "materially increased catastrophic risk," that's a reportable incident. This is likely the most consequential drafting change from GAAIA for the alignment/interpretability research community.
- **The § 2(6)(B)(i) "otherwise publicly accessible in a substantially similar form" carve-out** is broader than GAAIA's carve-out (which only excluded lawful federal activity). The "substantially similar form" qualifier softens the SB-1047-style "publicly available information" exemption — model output about a bioweapon synthesis path isn't uplift-free just because a textbook describes the pathway if the model's rendering is more actionable. Real litigation risk here about what "substantially similar form" means.
- **The § 2(6)(B)(iii) "did not materially contribute" carve-out** duplicates the "materially contribute" element already in (A). Together they set up a double-materiality test that will make catastrophic-risk claims harder to prove.
- **`Property` explicitly excludes "loss of value of equity"** (§ 2(18)(B)). Stock-price drops from a catastrophic AI incident don't count toward the `$1B` property-damage threshold. Given how quickly market-cap losses can dwarf physical damage in a major incident, this carve-out substantially narrows the (A)(ii) autonomous-crime prong.
- **`AI` and `AI model` are now cross-referenced to 15 U.S.C. 9401** (§ 2(3)) rather than defined in-bill. Tidier drafting, but any future amendment to NAIIA definitions silently updates the coverage of this Act.
- **`Assessment` (§ 2(5)) has narrowed vs. GAAIA's `audit and assessment`.** The GAAIA term did both compliance auditing and framework-adequacy review; the FRONTIER Act splits them — IVOs do assessment, an "independent third party" does the § 4(b) audit. Whether these can be the same entity is not specified.
- **`Loss of control` (§ 2(7)(C)) remains undefined**, as in GAAIA, and still anchors both the incident trigger and — via `evading control` in § 2(6)(A)(iii) — the substantive harm standard.

## Changes vs GAAIA discussion draft (2026-06-04)

The FRONTIER Act's § 2 is a substantial rewrite of GAAIA § 101, not a rename. Key drifts:

- **Tier structure fundamentally restructured** (§ 2(11), (15), (22) vs. GAAIA § 101(12), (15)). GAAIA had a two-ring stack keyed to revenue only: `frontier developer` (`>$50M`), `large frontier developer` (`>$500M`). FRONTIER moves to three rings and adds an expenditure floor to each covered tier: `frontier developer` (no revenue floor — pure compute), `large` (`>$50M rev` + `>$1B` AI expenditures), `very large` (`>$5B rev` + `>$10B` AI expenditures). Measurement window changes from "calendar year immediately preceding" (GAAIA) to a rolling "preceding 36-month period, determined as of the first day of each calendar month" (FRONTIER). Consequence: a well-funded pre-revenue lab that GAAIA missed entirely is now a covered `frontier developer` on day one of first training; the tiers where duties bite have moved up.
- **AI-related development expenditures is entirely new** (§ 2(4), no GAAIA analogue). Enables the new coverage keying above.
- **CAISI at NIST replaced by Under Secretary of Commerce for AI Security** (§ 2(21) vs. GAAIA § 101(9) `Director`, tied to GAAIA § 102 establishment of CAISI). The GAAIA Center-inside-NIST design (a semi-technical research body wearing a regulatory hat) is gone; instead a Commerce sub-cabinet officer administers the regime. This moves administration from technical staff into the political appointee chain and consolidates authority in a single person rather than an institution.
- **Imminent catastrophic risk is new** (§ 2(13), no GAAIA analogue). Without this predicate GAAIA had no emergency-order authority; FRONTIER § 8 emergency suspensions rest on it.
- **Very large frontier developer is new** (§ 2(22)). Creates the tier that triggers § 5 IVO assessment.
- **Critical safety incident (D) — deceptive techniques — is new** (§ 2(7)(D)). GAAIA's § 101(7)(B) was "failure of a model's risk-mitigation measures"; FRONTIER replaces that with "harm resulting from the materialization of a catastrophic risk" (§ 2(7)(B)) and adds the deceptive-techniques prong. The GAAIA "failure of mitigation" trigger is gone — worth flagging.
- **Catastrophic risk broadened in scope, narrowed by new carve-outs.** Prong (i) now covers cyber weapons alongside CBRN (§ 2(6)(A)(i) vs. GAAIA § 101(6)(A)(i)); the harm nexus adds "development, storage, use, or deployment" and requires "materially contribute" (§ 2(6)(A), not present in GAAIA). Carve-outs expand from GAAIA's single lawful-federal-activity exclusion to three: publicly accessible outputs, lawful federal activity, and harm the model did not materially contribute to (§ 2(6)(B)).
- **Assessment narrowed** (§ 2(5)) vs. GAAIA's `audit and assessment` (§ 101(5)) — see drafting notes.
- **Foundation model, deploy** now require "interstate or foreign commerce" nexus (§ 2(8), (9)); the `deploy` carve-out narrows to a "primary purpose" test (§ 2(8)(B)) vs. GAAIA's broader "for the development or assessment" exclusion (§ 101(8)(B)).
- **Property carve-out for equity losses added** (§ 2(18)(B)). GAAIA § 101(19) had no such exclusion.
- **AI and AI model now cross-referenced to 15 U.S.C. 9401** (§ 2(3)) instead of GAAIA's open-ended in-bill list (§ 101(3), (4)).
- **Dropped terms:** `open-source community` (GAAIA § 101(18)) and `Director` (GAAIA § 101(9)) do not appear in FRONTIER — consistent with dropping CAISI as administrator and dropping GAAIA's Title I sections that referenced open-source explicitly.

## Policy conversation angles

- **Innovation / anti-patchwork:** Expenditure floors let the sponsors argue that only well-funded labs face the heaviest tier duties — the `>$1B` AI-spend line clears every mid-size lab and every academic effort. The `>10^26` FLOP threshold still sits at or above most publicly disclosed training runs. Combined with § 9 preemption, supporters can pitch this as targeted, big-lab-only federal coverage.
- **Safety / catastrophic-risk:** The CBRN taxonomy is expanded to cover cyber weapons (§ 2(6)(A)(i)) and the incident regime now captures scheming/deception (§ 2(7)(D)) — both are wins the CAIS/Bengio-aligned community will read as meaningful. But the `>50 deaths / >$1B` gate remains high, the new "materially contribute" and "publicly accessible in substantially similar form" carve-outs raise proof burdens, and the equity-loss exclusion narrows the property prong further.
- **National security:** `Critical safety incident` still names weight exfiltration (§ 2(7)(A)). Cyber weapon added alongside CBRN (§ 2(6)(A)(i)) is a direct nod to BIS/CISA framings. The Under Secretary title — "for AI Security" — signals a Commerce-security posture rather than NIST's standards-and-measurement posture.
- **Free speech / civil liberties:** As with GAAIA, § 2 does not define persuasion, manipulation, or content harm — Title I is not about those risks. The `publicly accessible in substantially similar form` carve-out (§ 2(6)(B)(i)) has some speech-adjacent flavor: model outputs that mirror what's already in the public library aren't catastrophic-risk-generating on their own.
- **State AG / enforcement:** The definitions are the vocabulary state AGs will litigate against under § 4 and § 5 penalty regimes. The vagueness of `imminent catastrophic risk` (§ 2(13)) and the undefined `loss of control` (§ 2(7)(C)) are where enforcement disputes will concentrate.
