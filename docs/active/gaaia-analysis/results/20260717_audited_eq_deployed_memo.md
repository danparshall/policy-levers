# Memo: audited == deployed — close read of GAAIA §§111–112

- Date: 2026-07-17 (evening session)
- Task: policy-levers issue #1
- Method: full-text read of §111(c), §112(b), (e), (f), (g), (h); §101 definitions consulted ((1) acceptable levels, (8) deploy, (12)/(15) developer tiers); earlier keyword passes (hash/checksum/cryptograph/fingerprint/version: 0/0/0/0/4-irrelevant) treated as corroborating, not primary.

## Verdict

CONFIRMED: no provision requires that a deployed frontier model be the artifact any audit, assessment, or report attaches to. Checked against all three acceptance criteria from the issue:

1. **Artifact identification (any mechanism):** none. §111(c) identifies a model by release date, supported languages, output modalities, intended use, and framework-assessment summaries. §112(h)(2) requires the IVO's name, address, email, and phone number; no model identifier of any kind. No fingerprinting, registration, versioning, or descriptive-uniqueness requirement anywhere in Title I.
2. **Conformity duty (deployed must be assessed):** none. "Deploy" (§101(8)) is making a model available to a third party; nothing conditions deployment on, or ties it to, any assessment, and the §111(c) report is due "before, or concurrently with" the act.
3. **Joining language between §111(c) report and §112 audit:** none. Note the structural point: §112(b) audits are compliance-and-adequacy audits of the FRAMEWORK (SOX-style); model-level risk assessments are the developer's own, conducted "pursuant to the frontier AI framework at issue" (§111(c)(7)) and self-published. The IVO audits whether the developer follows its own plan, not the model.

## Sharpenings beyond the original claim

- The machinery *contemplates* model-level conformance findings without artifact identity: §112(g)(1)(B) (supplemental report when "a frontier model is in conformance with its published frontier AI framework is no longer valid") and §112(f)(4) (ad hoc audit after "substantial modification to [the] model"). The findings exist; nothing says which artifact they attach to.
- Internal-coherence argument for the annex: §112(f)(2) authorizes ad hoc audits to "reproduce or validate audit and assessment findings." Reproduction presupposes artifact identity the bill never requires. The bill's own validation power is inoperable as drafted.
- Fair characterization of what the regime IS: testimony-based. §111(d) false-statement liability + §113 whistleblower protection + §112(g)(1)(D) misleading-representation triggers police *lying about* the artifact. The provenance fix (register evaluated-weights fingerprint; IVO certifies hash match; tamper-evident derivation records to a registered parent) converts testimony into evidence at ~zero marginal burden (records emitted by build systems; post-SolarWinds federal vendor stack).

## Also filed while in the text (candidates for NOTES.md, pending dedupe against Tier 1 list)

- §112 tier-term inconsistency: audit obligation attaches to "large frontier developer" (§112(b)) but the section's machinery repeatedly says plain "frontier developer" (licensing criteria, report contents (e)(4), (g)(1)(A)/(D), (g)(4)). Ambiguous whether mid-tier can be swept in; likely drafting shorthand; one global term fixes it.
- No US-nexus/applicability clause in Title I: "developer" is "a person or entity," "deploy" has no geography. Facially global; presumption against extraterritoriality creates ambiguity for foreign developers (Mistral, DeepSeek). One-sentence applicability provision fixes it.
- §101(1) "acceptable levels of catastrophic risk mitigation" = mitigation adequate to ensure anticipated benefits outweigh catastrophic risk, considering probability and magnitude of both. A cost-benefit balancing definition, self-referential to the developer's own anticipations; everything in §112(e)(4)/(6) findings cashes out against this. Worth a line in the substantive tier: the standard the entire audit regime certifies against is a benefits-outweigh-risks judgment with no floor.

## Feeds

- Blog v3 provenance paragraph (reword: IVO audits the framework, not the model; testimony-vs-evidence framing).
- Comment letter annex (reproduce-and-validate coherence argument; tier-term fix; applicability clause).
- Issue #1: closed by this memo.

---

## ERRATUM (2026-07-17, later same evening)

Superseded in part by `20260717_audit_deployment_linkage_review.md` (adversarial pass, Opus/Nori, requested by Dan). Corrections to this memo:
- Acceptance criterion 2 verdict ("conformity duty: none") was WRONG as stated: § 111(c) attaches the assessment duty to "such model" (per-deployed-model), § 101(20) retriggers on substantial modification, § 112(b) makes deploy-without-assessment auditable. Obligation-level closure exists.
- "Developer chooses what to show the IVO" overstated: § 112(d)(2) requires material access limitations to appear in the audit report.
- § 112(f)(2) reproduce-and-validate coherence argument weakened: reproduced findings are compliance/adequacy findings, not artifact findings. Do not lead with it.
- SURVIVING claim (use this framing everywhere): no provision binds assessed weights to served weights; checkpoint substitution (assess A, ship B) is undetectable as drafted and reachable only via § 111(d) knowing-falsity. Keyword absences confirmed by the review. Tier 3.8 layered ask unaffected.
