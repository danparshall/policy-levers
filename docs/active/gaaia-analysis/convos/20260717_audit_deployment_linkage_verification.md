# Audit-deployment linkage verification (+ multi-session git reconciliation)

**Date:** 2026-07-17 → 2026-07-18
**Branch:** main (line: `gaaia-analysis`)

## Summary

Short session running alongside the full-day contact-matrix/blog-v3 session (other terminal). Two jobs: keep this machine's `main` reconciled with the other session's pushes, and adversarially verify a claim from that session's close read — that GAAIA contains "no provision joining" the audited model to the deployed model ("The developer chooses what to show; the IVO certifies what it saw; … no provision joins them"). Dan flagged the claim as suspiciously strong and asked for an independent Opus review of the full bill text.

The Opus pass (adversarial stance, prompted to refute) found the claim **partly right but materially overstated**: the grep kernel holds exactly (0 hits for hash/checksum/cryptographic/fingerprint; the 4 "version" hits are as described), and no clause resembles "deployed model shall conform to the audit report" — but the framing is refutable. The IVO audit is compliance-and-adequacy scoped (§101(5), §112(b)), not artifact-scoped, so there is no "show a model, get it cleared" gate to game; and §111(c) per-deployment assessment + §101(20) substantial-modification retrigger + §112(b) ongoing §111-compliance verification + §112(g)(1)(B) out-of-cycle reports jointly refute the blanket "nothing ties deployment to the audit." The defensible residual gap is narrower: assess checkpoint A, silently ship checkpoint B — caught only by §111(d)'s knowing-false-impression bar (intent must be proven). This converged independently with the other session's own close-read memo (`results/20260717_audit_deployment_close_read` line of work; see its erratum and Issue #1 closure) — the two reviews are complementary: this one adds the refutation table with line-numbered citations and exact grep verification.

Git reconciliation happened twice: first a simple divergence (Dan's essay edits committed + rebased + pushed), then a race with the other session's blog-v3 push that turned Dan's uncommitted essay edit into a stash conflict. Resolved by keeping v3's new "SOX for AI" section (it fulfilled Dan's `> Want a section about the IVO…` placeholder, which was dropped) and keeping Dan's new DeepSeek/extraterritoriality tidbit.

## Topics Explored

- Whether GAAIA contains any provision linking the audited artifact to the deployed artifact (definitions, audit scope, attestation, retrigger, recordkeeping, enforcement — full-text Opus review with line citations)
- Verification of the literal grep claims (hash/checksum/cryptographic/fingerprint/version/conform/identical)
- Multi-session git reconciliation on `main` (two divergence events; one stash conflict in the blog draft)
- Whether H.R. 9363 text was in the repo (answered "no" mid-session; **stale within hours** — other session landed `bills/hr9363/` with introduced text + comparison + adversarial-review memos)

## Provisional Findings

- Blanket "no provision joins audited to deployed" is refutable via §111(c) + §101(20) + §112(b) + §112(g)(1)(B); the checkpoint-substitution framing (assess A, ship B; §111(d) knowing-falsity is the only hook) is the defensible version. This is now the controlling framing per the other session's Issue #1 erratum.
- Grep kernel of the original claim verified exact: 0×{hash, checksum, cryptographic, fingerprint}; 4×version (redactions + NIST CSF); 7×conform* all framework-conformance or boilerplate; 0×identical; no SOX-style officer certification; §112(j) recordkeeping is report-level only.
- Tier 3.8's layered provenance ask survives the review intact — only its motivating sentence needed the reword (applied).
- Blog v3's provenance paragraph already uses the corrected testimony-vs-verification framing; consistent with the Opus findings.
- Flagged for verify-before-publish: the essay's new DeepSeek/extraterritoriality tidbit ("nothing about US creators") — hinges on §101 developer definitions and the territorial reach of "deploy"; not yet checked against text.

## Decisions Made

- NOTES.md Tier 3.8 motivating sentence reworded from the refutable blanket claim to the checkpoint-substitution framing, with a do-NOT-phrase-it-the-old-way warning and pointer to the review doc.
- Essay stash conflict resolved: keep v3 SOX section, drop fulfilled placeholder, keep DeepSeek tidbit (commit 723c8d6).

## Results

- `results/20260717_audit_deployment_linkage_review.md` — Opus adversarial review: verdict, refutation table (provision / lines / quote-gist / strength), verified grep counts, defensible-critique reframing. Committed 9bac8b0 along with the Tier 3.8 reword.

## Open Questions

- DeepSeek/extraterritoriality tidbit needs a text check before the blog publishes.
- Consolidation: this review doc and the other session's close-read memo cover the same ground from opposite directions; decide whether to merge them or leave both with cross-references (currently: STATUS Issue-#1 erratum names this doc as controlling).
