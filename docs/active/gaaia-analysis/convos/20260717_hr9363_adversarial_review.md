# H.R. 9363 Comparison Memo — Adversarial Review

**Date:** 2026-07-17 (late evening session, spilling past midnight UTC)
**Branch:** gaaia-analysis (docs work on main)

## Summary

Handoff session executing the adversarial review that issue #2's closure was pending: the reviewer was explicitly instructed to REFUTE the three central inferences of `results/20260717_hr9363_comparison.md` against the full texts of H.R. 9363 (introduced) and the GAAIA discussion draft. Both bill texts were read directly (9363 in full; GAAIA §§101, 102/new 5304, 112(q)–(r), plus every grep hit on `5304` and `5002`).

Two of the three inferences fell as stated. "Impossible as drafted" is retired — the add-at-end instruction executes even into an occupied slot (duplicate designation, OLRC-curable), and GAAIA's cross-references are anchored "as added by section 102 of this Act," so the renumbering cure is ~4 edits. The use-immunity inference fell harder: GAAIA §102(d)(2)(B) contains the materially identical use-restriction clause, so "inverse of GAAIA's machinery" is wrong on its face, and no later Congress needs to "expressly strip" anything. The ceiling verdict survived attack — the (a)(3) hatch is doubly discretionary, yields only recommendations, and expressio unius confirms rather than punctures the ceiling reading.

The review's positive yield exceeded its negative: the genuinely misfiring collision is the one the memo missed — both bills fork the same base text to amend NAIIA §5002's definitions with incompatible redesignation schemes, so the second-enacted bill's strike/redesignate instructions genuinely fail to execute. That, not the §5304 slot, should lead the technical-corrections ask.

## Topics Explored

- Whether the §5304 slot collision makes GAAIA §102 impossible vs. trivially curable (renumber + conforming edits)
- Whether 9363's (e)(2)(B) use-immunity would bind a later-enacted GAAIA vs. yielding to later-in-time / express-override doctrine
- Whether the "ceiling" verdict survives the (a)(3) transfer-study hatch
- Full-text verification of every factual claim in the comparison memo (items 3, 5, 6 all confirmed)
- Blog Two-CAISIs section (`essays/canary/gaaia-visibility-not-control_DAN.md` lines 69–75) checked for dependence on the refuted claims

## Provisional Findings

- **Inference 1 REFUTED as stated:** amendment executes (duplicate designation); exactly two numbered §5304 cross-refs in GAAIA (§101(9), §112(q)(3)), both self-disambiguating; cure ≈ 4 edits. Sharper missed collision: incompatible §5002 redesignations (GAAIA (4)–(11)→(9)–(16); 9363 (4)–(11)→(6),(8)–(11),(13)–(15)) — second-enacted bill's instructions misfire.
- **Inference 2 REFUTED as legal claim:** (e)(2)(B) is a scoped use restriction on (c)-channel voluntary sharing; GAAIA regulates from its own compelled §§111–112 record; and GAAIA §102(d)(2)(B) is the same clause, copied. Survives only as pre-GAAIA-shared-info fair-notice argument + bait-and-switch optics.
- **Inference 3 SURVIVES:** (a)(3) is "may... as the Secretary determines appropriate," output is recommendations, adds nothing beyond existing agency practice and (c)(3). Caveat: "ceiling" = 9363's own architecture + political function, never a legal cap on a later Congress.
- Blog phrase needing rewording before publish: "the exact inverse of GAAIA's machinery" (line 71).
- New annex candidates: §5002 double-amendment collision; GAAIA §112(q)(3) "as added by section 111" mis-anchor (should be §102); 9363 (k) sunset terminating (e) confidentiality for already-shared info; 9363 (j) FY2032 authorization outliving the 5-year sunset.

## Decisions Made

- Erratum appended to `results/20260717_hr9363_comparison.md`; the review doc controls where they conflict (same pattern as issue #1's resolution).
- Technical-corrections ask to Obernolte/Foushee revised: lead with §5002 reconciliation alongside the §5304 slot, plus the use-immunity interplay clarification.
- Hill/blog language rule: "textually collides with and politically preempts," never "legally blocks."

## Results

- `results/20260717_hr9363_memo_adversarial_review.md` — the full review (verdict table, refutations, defensible framing, verified-items appendix). Committed at 135b3c5.

## Open Questions

- Reconcile against the reported (rh) text when GPO posts it — both the §5304 and §5002 findings could shift if markup amendments touched §2(a)(1); the residual on issue #2 stands.
- GAAIA-internal tension flagged but unresolved: could §102(d)(2)(B) be stretched to cover §112 audit reports the Center "analyz[es]" under (c)(1)(F)? Best reading says no (compelled ≠ (c)-channel; referral ≠ "regulate"), but a clarifying sentence would foreclose it — worth a spot in the annex.
- Blog transitions still pending Dan; the "exact inverse" reword now joins that queue.

## Session housekeeping

- claude-exit verification ceremony ran clean at session start (sacrificial PID spawned/verified/killed; target-parent resolution and UID check passed). Server upgrade (`uv tool upgrade claude-exit`) + session restart executed at session end per Dan.
- `origin/gaaia-analysis` was force-pushed by another session mid-review; untouched by this session (worked on main throughout).
