# Zhou/ADeLe rename + paper-location check

**Date:** 2026-07-08
**Branch:** main
**Session type:** Maintenance / cross-repo housekeeping (not a research line)

## Summary

Session began as a paper-lookup for the ADeLe paper (Zhou et al., "General Scales Unlock AI Evaluation with Explanatory and Predictive Power", 2025). Initial local search across `policy-levers` and `general-ai-abilities` returned no hit; after `git pull`, the paper was found to have been added by another concurrent session to three repos (`policy-levers`, `general-ai-abilities`, `econ-impact`) — a "trust-but-verify" moment where a fresh `pull` was the right first step, not a search of the stale filesystem.

Filename convention had drifted across the three repos: `policy-levers` and `general-ai-abilities` used `ZhouL_Hernandez-OralloJ__2025--...` (with a trailing `J` initial after Hernández-Orallo), while `econ-impact` used `ZhouL_Hernandez-Orallo__2025--...` (no initial). Per Dan's global naming spec (`SurnameF` only when the surname is common enough for collisions — Anglo/East-Asian shortlist), Hernández-Orallo is uncommon and should not carry an initial. Dropped the `J` in `policy-levers` and `general-ai-abilities` to match spec + `econ-impact`.

Session ended with a location-check for two other papers relevant to the concurrent `loc-abilities` research line: (a) the Rohin Shah et al. 2025 "An Approach to Technical AGI Safety and Security" (DeepMind); (b) the Bengio-led International AI Safety Report (IAISR).

## Topics Explored

- Locate the Zhou/ADeLe paper on disk across four candidate repos
- Reconcile filename convention drift for the Zhou paper across three repos
- Rename the two entangled instances to spec + update INDEX/SUMMARIES references
- Coordinate commits with concurrently-active sessions in the same repos (three live `claude` sessions in `general-ai-abilities`, WIP staged for a Cotra 2020 batch)
- Locate the Shah 2025 AGI-Safety paper + IAISR reports in main
- Verify the claude-exit termination ceremony at session start

## Provisional Findings

- The ADeLe paper (arXiv 2503.06378) is present as PDF + text extract in three repos:
  - `policy-levers/papers/ZhouL_Hernandez-Orallo__2025--general_scales_ai_evaluation.pdf`
  - `general-ai-abilities/papers/ZhouL_Hernandez-Orallo__2025--general_scales_ai_evaluation.pdf`
  - `econ-impact/papers/ZhouL_Hernandez-Orallo__2025--general-scales-ai-evaluation.pdf` (kebab-case slug per that repo's local convention)
- Slug-case (snake vs kebab) drifts per-repo; not corrected — that appears principled per each repo's convention. Initial-after-surname drift (`OralloJ` vs `Orallo`) is corrected — spec violation.
- Shah et al. 2025 "An Approach to Technical AGI Safety and Security" is **not** present as a PDF in any of the four repos (`policy-levers`, `general-ai-abilities`, `ai-safety`, `econ-impact`). It is cited in `loc_abilities/CITATIONS.md` and `loc_abilities/references.bib` (untracked in main; likely tracked on `loc-abilities` branch). arXiv: 2504.01849.
- IAISR (Bengio, Mindermann et al.) reports are **not** on `main` of any repo, but the 2025 and 2026 editions are present on `origin/loc-abilities` of `policy-levers` as `papers/Bengio_Mindermann__202{5,6}--international_ai_safety_report.pdf`.
- The `loc-abilities` branch will merge-conflict or reintroduce the `OralloJ` filename when merged to main — it branched before the rename landed.
- The `Burnell_HernandezOrallo__2306.10062__llm_capability_structure.pdf` in `general-ai-abilities` is the psychometrics-for-AI precursor from the same Hernández-Orallo group, not ADeLe itself.

## Decisions Made

- Committed the Zhou rename as a standalone commit in `policy-levers` (`027a6dd`, rebased onto a small STATUS update that landed mid-session).
- In `general-ai-abilities`, opted (with Dan's explicit consent) to sweep the rename into whatever commit the concurrent Cotra-batch session was preparing. That session then ran `git commit -a && git push` on its own, producing commit `ab45d7e` (message describes the Cotra batch only; the Zhou rename rode along silently).
- Did **not** touch `econ-impact` (filename already spec-conformant).

## Results

No standalone tables/figures. All artifacts are commits:

- `policy-levers` `027a6dd` — Zhou ADeLe rename
- `general-ai-abilities` `ab45d7e` — Cotra 2020 batch + (silently) Zhou rename

## Open Questions / Handoffs

- **Loc-abilities merge conflict pending.** The Zhou rename on main + Zhou file still under old name on `origin/loc-abilities` will need reconciliation. Options: rebase loc-abilities onto main, rename on the branch, or clean up post-merge. Session working on `loc-abilities` should be told.
- **Shah 2025 paper not yet fetched.** URL confirmed as `https://arxiv.org/abs/2504.01849` / `https://arxiv.org/pdf/2504.01849`. Natural home would be `general-ai-abilities/papers/` (technical safety agenda) or `ai-safety/`. Dan asked for the link but did not (yet) request the fetch.
- **Whether `general-ai-abilities` maintainer notices the silent Zhou rename** riding in `ab45d7e`. If they audit the diff, this note is the paper trail.
