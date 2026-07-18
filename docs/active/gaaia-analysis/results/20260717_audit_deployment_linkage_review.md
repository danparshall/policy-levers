<!-- Generated during: convos/20260717_audit_deployment_linkage_verification.md -->
# Adversarial review: does GAAIA link the audited model to the deployed model?

**Date:** 2026-07-17
**Provenance:** Opus subagent (adversarial verification pass) over `bills/obernolte-trahan/gaaia_full_text.txt` (~8,948 lines, full 269-page discussion draft), prompted to *refute* the prior "audit-deployment gap" claim. Requested by Dan after the claim ("no provision joins them; zero hash/checksum/cryptographic/fingerprint hits") seemed too strong. Line numbers below refer to `gaaia_full_text.txt`.
**Relates to:** NOTES.md Tier 3.8 (weight provenance / "audited == deployed") and Tier 3.7 (advance notice for weight release).

## Verdict

**The prior claim is partly right but materially overstated.** Category: functional closure exists at the framework/process/obligation level via retrigger + per-deployment assessment + ongoing compliance audit — but a genuine **residual artifact-integrity gap** remains at the bit-identity level.

Two framing errors in the prior claim:

1. **The IVO audit is not artifact-scoped.** §101(5) and §112(b) define it as a compliance-and-adequacy audit of the developer's conformance with §§111–112 and the adequacy of the frontier AI framework — not "show the IVO a model, get it cleared." There is no artifact-clearance gate for a developer to game by curating what the IVO sees. §112(d)(1) does let developers impose "reasonable security protocols, access limitations, and confidentiality requirements… narrowly tailored to protect trade secrets," but §112(d)(2) requires any material limitation on IVO scope/access to be described in the audit report — constrainable, not cherry-pickable.
2. **"No provision joins audited to deployed" is refutable as stated.** Multiple provisions attach obligations directly to the *deployed* model (below).

## Strongest provisions against the blanket gap claim

| Provision | Lines | Language (gist) | Strength |
|---|---|---|---|
| §111(c) transparency report | 1089–1107 | "Before, or concurrently with, deploying a frontier model that is **new or includes a substantial modification**," developer must publish a report including "each **assessment of catastrophic risk with respect to such model**" and its results | **Strong** — per-deployed-model duty; the central rebuttal |
| §101(20) "substantial modification" | 370–377 | A significant change in how a model is deployed (new fine-tuning capability, weight release, new feature) "that necessitates… an assessment of catastrophic risk" | **Strong** — retrigger closing the modify-then-deploy path |
| §111(a)(1) + framework gating | 1005–1006, 1027–1041 | Framework "[a]pplies to **each frontier model**"; assessment review determines "[w]hether to **deploy such model**"; framework must define the substantial-modification determination process | Strong-moderate |
| §112(b)(1) IVO scope | 1620–1622 | IVO performs "ongoing verification of the large frontier developer's **compliance with this section and section 111**" | Strong-moderate — deploying without the required assessment is an auditable §111 violation |
| §112(g)(1)(B) out-of-cycle report | 1748–1766 | If "**material changes to a frontier model**" invalidate a prior finding that "**a frontier model is in conformance with its published frontier AI framework**," IVO must report within 7 days | Moderate — closest thing to a per-model linkage, but conformance to the *framework*, not identity to an *artifact* |
| §112(f)(4) ad hoc audits | 1729–1742 | Director may require ad hoc audit after "a substantial modification to [a] large frontier developer's model" | Moderate |
| §111(d) + §111(i) | 1119–1132, 1243–1248 | No knowingly inaccurate statement / false impression re "implementation of, or compliance with, the frontier AI framework"; $1M per violation per day | Moderate — the honor-system backstop |
| IVO immunity clause | 2110–2112 | "a catastrophic risk of a **frontier model audited and assessed by the IVO**" | Weak, corroborating — drafters view models as audit objects |

## What survives of the prior claim (verified grep counts)

| Term | Count | Notes |
|---|---|---|
| hash / checksum / cryptographic / fingerprint | **0 each** | Confirmed exactly as previously claimed |
| version | **4** | L1899/1901/1923 = redacted "public version" of framework; L8464 = NIST Cybersecurity Framework version. No model-versioning sense anywhere |
| conform* | 7 | All "conformance with/to the frontier AI framework" or "CONFORMING AMENDMENT" boilerplate (L6256, L8528). None artifact-to-artifact |
| identical / "same model" | **0** | No identity language |

Also confirmed absent:
- **No clause resembling "the deployed model shall conform to the model described in the audit report."**
- **No SOX-style developer/officer certification.** The only signed certification is the IVO's lead audit partner (§112(e)(8), L1707–1719) certifying the *report's* accuracy and the IVO's independence — not artifact identity.
- **No artifact-level recordkeeping.** §112(j) (L1894–1898) requires 5-year retention of audit/assessment reports and supporting materials — report-level, no weight-hash / config-management retention.
- "Material modification" (§101(16), L342) applies to the *framework*; "substantial modification" (§101(20)) is the model-side term.

## The defensible version of the critique

The residual gap is **not** "audit one model, deploy another" — §111(c) + §112(b) refute that. It is narrower: **run the §111(c) assessment on checkpoint A and silently ship checkpoint B.** Nothing in the statute cryptographically or procedurally binds the assessed weights to the served weights; substitution is caught only by §111(d)'s *knowing false impression* bar (intent must be proven), plus whatever unspecified config management the developer's own framework happens to include. That is an honor-system backstop, not an integrity mechanism.

**Implication for drafting/comments:** Tier 3.8's layered provenance ask (fingerprint registration → IVO artifact certification → derivation DAG → attestation-as-liability-anchor) is precisely targeted at this residual gap and survives the review intact. But the *motivating sentence* should be reframed from "nothing ties deployment to the audit" (refutable) to "nothing establishes that the artifact assessed under §111(c) is the artifact served — checkpoint substitution is undetectable as drafted and reachable only through the §111(d) knowing-falsity bar" (defensible). Any blog/essay text leaning on the blanket "no provision joins them" framing should be revised the same way.
