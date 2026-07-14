<!--
Section file: bills/obernolte-trahan/sections/sec-111-transparency-in-frontier-artificial-intelligence.md
Section-by-section: bills/obernolte-trahan/gaaia_section_by_section.txt
Summary written: 2026-07-14
Written by: Claude (Canary Institute automation), YOLO-mode session
-->

# SEC. 111. TRANSPARENCY IN FRONTIER ARTIFICIAL INTELLIGENCE — summary

**One-line:** Mandatory public "frontier AI framework" + pre-deployment transparency report + confidential incident reporting to CAISI (with a 24-hour carve-out that goes to law enforcement, not CAISI), enforced by AG/opt-in state AGs at up to $1M/day, 3-year sunset.

## What it does

Within one year of enactment, every "large frontier developer" (§ 101(15): frontier developer with >$500M prior-year gross revenue including affiliates) must write, implement, comply with, and publicly post a frontier AI framework covering how it identifies risk thresholds, assesses whether each frontier model has "capability that could pose a catastrophic risk," secures model weights, uses third-party assessors, and makes deploy / internal-use decisions (§ 111(a)). Before (or concurrently with) deploying a new or substantially-modified frontier model, the developer must publish a transparency report enumerating release date, supported languages, output modalities, intended use, restrictions, and each catastrophic-risk assessment with results (§ 111(c)). Confidential critical-safety-incident and catastrophic-risk reports go to the CAISI Director (§ 111(f)), on a 15-day clock (§ 111(g)(1)) or a 24-hour clock to law enforcement for imminent-risk incidents (§ 111(g)(2)). AG or opt-in state AGs may enforce; up to $1M per violation, each day a separate violation (§ 111(i)).

## Key provisions

- **Coverage:** Only "large frontier developers" — § 101(15) sets a >$500M prior-year revenue floor (calendar year immediately preceding, aggregated with affiliates), on top of the § 101(12) "frontier developer" >$50M threshold and § 101(13) >10^26-FLOP frontier-model threshold. Practically, this is the ~5 largest U.S. labs at enactment.
- **Framework contents (§ 111(a)(2)(A)–(J)):** national/international/industry standards; developer-identified risk thresholds for catastrophic risk; deploy vs. internal-use decisions; third-party assessment; model-weight cybersecurity; incident response; internal governance; oversight-circumvention risk from internal use.
- **Update cadence:** annual review (§ 111(b)(1)); 30-day re-publication with justification after any material modification (§ 111(b)(2)).
- **Transparency report (§ 111(c)):** 10 enumerated fields including release date, languages, modalities, intended use, restrictions, each catastrophic-risk assessment and its results, extent of third-party involvement.
- **False-statements ban (§ 111(d)):** No knowing inaccurate or false-impression statements about catastrophic risk, its management, or framework compliance — with a "good faith and reasonable under the circumstances" safe harbor at § 111(d)(2).
- **Redactions (§ 111(e)):** Developer may redact to protect trade secrets, its own cybersecurity, public safety, U.S. national security, or to comply with federal/state law. Requires a "character of such redaction and a justification" statement (§ 111(e)(2)(A)) plus 5-year retention (§ 111(e)(2)(B)). No pre-clearance or challenge mechanism.
- **Incident reporting (§ 111(f)–(g)):** Director builds confidential channels within 180 days. Routine critical-safety-incident report: 15 days after discovery (§ 111(g)(1)). Imminent-risk-of-death-or-serious-injury: 24 hours — **to a law enforcement agency with jurisdiction, not to the Director** (§ 111(g)(2)).
- **State AG opt-in (§ 111(h)):** State AGs may opt in to receive reports submitted under (f) and (g), per Commerce Secretary regulations under § 111(k).
- **Civil penalty (§ 111(i)):** Up to $1,000,000 per violation; each day is a separate violation. AG or opt-in state AG may sue for penalty + injunction. AG intervention right and stay-on-parallel-action rules at § 111(i)(3)(C)–(E).
- **Rulemaking (§ 111(k)):** Commerce Secretary in consultation with Director prescribes regs under APA § 553; authority sunsets 3 years after enactment.
- **Sunset (§ 111(l)):** Section itself ceases to have effect 3 years after enactment absent reauthorization.

## Who it affects

- **Regulated parties:** Large frontier developers only — § 101(15) >$500M prior-year revenue AND § 101(12)–(13) frontier-developer / >10^26-FLOP frontier-model status.
- **Empowered actors:** CAISI Director (receives reports, publishes annual anonymized aggregate under § 111(j)); Commerce Secretary (rulemaking); U.S. Attorney General and opted-in State AGs (civil enforcement); state and local law enforcement (24-hour imminent-risk channel).
- **Beneficiaries:** Public (published framework + transparency report); state AGs opting in; researchers with access to the public-facing framework and reports (subject to redactions).

## Cross-references

- **Defined terms used:** "large frontier developer" (§ 101(15)); "frontier developer" (§ 101(12)); "frontier model" (§ 101(13)); "frontier AI framework" (§ 101(11)); "catastrophic risk" (§ 101(6): >50 deaths or >$1B property damage from CBRN uplift, autonomous cyber/murder/assault/extortion/theft, or evading control); "critical safety incident" (§ 101(7): unauthorized weight access/modification/exfiltration, mitigation failure, or loss of control); "material modification" (§ 101(16)); "substantial modification" (§ 101(20)); "deploy" (§ 101(8)); "Director" (§ 101(9)).
- **Depends on / paired with:** § 102 (CAISI must exist to receive reports and administer channels under § 111(f)); § 112 (IVO audits are the enforcement backstop that turns § 111 disclosures into verified compliance); § 113 (whistleblower channel routes evidence of § 111 non-compliance).

## Notable statutory language

> "Before publishing a report or other information pursuant to this section, a frontier developer may make a redaction in such publication to carry out any of the following: (A) Protect a trade secret, or the cybersecurity, of such developer. (B) Protect public safety or the national security of the United States. (C) Comply with Federal or State law." (§ 111(e)(1))

Redaction is self-executing; the only downstream check is the "character + justification" note (§ 111(e)(2)(A)) and 5-year retention (§ 111(e)(2)(B)). No pre-publication CAISI review, no external challenge process. A developer that redacts "for cybersecurity" its entire catastrophic-risk assessment section could plausibly comply with the letter of § 111(e).

> "(2) IMMINENT RISK.—Not later than 24 hours after a frontier developer discovers a critical safety incident that poses an imminent risk of death or serious physical injury, such developer shall report such incident to a law enforcement agency with jurisdiction over such incident." (§ 111(g)(2))

Note the recipient: **"a law enforcement agency,"** not the Director. The Trahan section-by-section elides this — see below.

## Drafting notes & open questions

- **Section-by-section is wrong about the 24-hour recipient.** `gaaia_section_by_section.txt` states developers "must file a report with CAISI within 15 days of a critical safety incident or within 24 hours if the incident poses an imminent risk of death or serious injury." The bill body routes the 24-hour report to a **law enforcement agency with jurisdiction** (§ 111(g)(2)), not CAISI. This matters: local PD / FBI field office does not have CAISI's technical capacity, and no statutory obligation attaches to forward that report to the Director. Ask the drafters whether this was intentional.
- **Self-defined risk thresholds (§ 111(a)(2)(B)).** Developers set their own "risk thresholds" for what constitutes capability that "could pose a catastrophic risk." The bill body imposes no floor. § 111(k)(2)(C) *may* let Commerce prescribe thresholds by rule, but that authority is discretionary ("may include") and sunsets in 3 years (§ 111(k)(5)).
- **Redaction carve-out is expansive and self-judged.** No pre-clearance, no independent adjudicator, no adversarial challenge. Combined with the § 102 § 5304(d) confidentiality shield on voluntarily-shared information, the *published* transparency report can be redacted down to skeleton while the *confidential* channel is walled off from regulatory use.
- **"Good faith and reasonable" safe harbor (§ 111(d)(2))** on the false-statements ban is a common law standard that historically requires meaningful mental-state proof — hard to enforce against sophisticated corporate speakers.
- **Catastrophic-risk floor is high (§ 101(6)):** >50 deaths or >$1B damage, with narrow CBRN/autonomous-cyber/loss-of-control triggers. Many concerning capability observations may not clear the "foreseeable and material" causation link to that harm threshold, meaning the framework's assessment obligations only bite on the most severe end.
- **3-year section sunset (§ 111(l)).** Whole regime — framework mandate, transparency reports, incident channels, penalties — evaporates on a hard deadline unless Congress reauthorizes.
- **No private right of action.** Enforcement is federal-AG or opted-in state-AG only; no civil or class action for affected individuals.
- **Penalty scale check.** $1M/day × 365 = $365M/yr max. Real money, but frontier developers had 2025 revenues of $10-30B+ each; enforcement won't be existential at this ceiling.
- **"Substantial modification" self-determination (§ 111(a)(2)(F)).** Developer defines its own process for whether a modification triggers a new transparency report — the audit backstop under § 112 is the only external check.

## Policy conversation angles

- **Safety / catastrophic-risk:** The framework + pre-deployment report + incident channel is the most operationally load-bearing section in Title I. But: developer-set risk thresholds, self-judged redactions, the "good faith" safe harbor, and the 3-year sunset mean the teeth depend heavily on (a) Commerce writing tight rules under § 111(k) and (b) § 112 IVO audits actually verifying framework compliance.
- **Innovation / anti-patchwork:** Federal-preemption framing supporters will highlight the > $500M revenue floor (SME carve-out), the redaction rights, and the good-faith safe harbor as evidence the regime is narrowly targeted.
- **National security:** The 24-hour law-enforcement channel (§ 111(g)(2)) creates a novel local-agency AI-incident intake with no interagency protocol — worth pairing with FBI cyber and DHS/CISA equities.
- **State AG / enforcement:** § 111(h) opt-in + § 111(i)(3) enforcement authority is the primary state hook. Note the § 111(i)(3)(D) preemption-of-state-suits during pending federal action — a Justice Department that declines to prosecute effectively sidelines opted-in state AGs on those violations.
