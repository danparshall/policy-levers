# 20261030_pdoom_collection

**Date:** 2026-10-30 (ran into 2026-10-31)
**Branch:** main (no research line; doc work across four repos)
**Surface:** claude-code
**Machine:** Dans-MacBook-Air
**Session:** Dan (air, policy-levers, 20261030T1458, opus-5.5) · /Users/dan/.claude/projects/-Users-dan-code-policy-levers/a14cfe11-25d2-447c-991e-eb8649c87c58.jsonl · —

## Summary

Dan asked for the p(doom) numbers he remembered collecting. The only existing collection was a few lab-staff rows in general-ai-abilities' Sept 2026 Overton-window briefing; policy-levers held only Dan's own ~30% (used in the Han et al. critique). Dan asked for a full sourced list saved in general-ai-abilities (GAA). Over two research rounds (five web-research subagents), it became `GAA/agent-briefs/20261030_pdoom_estimates.md`: about 80 people plus about 20 surveys, forecasting tournaments and polls. Each row has its wording, what it is a probability of, horizon and conditions, date, and a source-strength tag. The file also has a definitions table, a "don't cite" list of misattributions, a pitfalls section, and a manual-check checklist. A parallel web session (`Dan (web, general-ai-abilities, 20261030T1556, opus-5.5)`) ran an extension pass from that file, `20261030_pdoom_extension_web.{md,csv,jsonl}` (168 records); its corrections were merged in, and the main file now names itself as the one to cite from.

The verification agent was first blocked by the permission classifier for reading paywalled or blocked content through archive copies. Dan then said archive copies were fine, but the routes failed on their own: the fetch tool refuses web.archive.org, and xcancel returns HTTP 451. So about 20 X, BBC and paywalled items stay on a manual-check list. Dan checked the first three (Hubinger, Krakovna, Marcus Williams) by hand and confirmed them.

Dan raised Chad Jones's "30x underinvestment" claim. The trail: Jones (2024, *AER: Insights*) is the tolerable-risk paper (4% total risk at γ=2, 33% with log utility). Jones (2026, JEP draft) says "a factor of 30 or more", citing Jones (2025) March NBER WP 33602, which contains no multiplier. Jones (2025) **v2.0 (Sept 2025)** says "more than a factor of 50": ~$100B a year justified, against "less than $1-2 billion" spent, a guesstimate sourced to a tweet. v2.0 was added to econ-impact, and the index rows in econ-impact and policy-levers that credited the 30x to Jones (2024) were corrected. Dan asked for a short report in verification, then corrected the framing mid-write: the race game's H is p(doom | AGI/ASI), not unconditional p(doom). The report was rewritten around the estimates that are already conditional on AGI.

## Topics Explored
- Locating prior p(doom) collections across policy-levers, GAA and all `~/code` and `~/data`
- Sourced p(doom) estimates: lab leaders, the Sept 2026 lab-staff wave, researchers, commentators, policymakers, declines
- Surveys and forecasts: AI Impacts ESPAI 2022/23/24, FRI XPT and its adversarial collaboration, LEAP, Metaculus, Manifold, public polls
- Hard definitions that change the numbers (XPT: extinction = population <5,000; catastrophe = ≥10% of humans die within 5 years)
- Merging the parallel web session's extension pass
- Chad Jones's tolerable-risk and spending papers; the 30x/50x trail
- Mapping the sourced numbers onto the race game's H in verification

## Provisional Findings
- The AI researcher median moved to **10%** in ESPAI 2024 (fielded Dec 2024, published Sept 2026; 5% in 2022–23). The question bundles extinction with permanent disempowerment.
- **No sitting member of Congress, cabinet official or governor has given a number of their own.** Lina Khan's ~15% (2023) is the only senior US official found; Alex Bores (NY-12 candidate) reportedly gave 20%; Sacks's "zero" is conditional on "doing the right things".
- Several aggregator figures are wrong: Leike's Sept 2026 ">10%" is Hubinger's quote; "Cotra 35%" is Lifland's own number (Cotra's own words: ~25%, 2022); LeCun "<0.01%" and Andreessen "0%" aren't their own words; Hoffman "20%" is a conversion of "2 out of 10".
- For p(doom | AGI) the best conditional anchors look like ESPAI's "extremely bad if human-level AI is built" (median 5%, mean 9.9%), the XPT superforecasters' 1% given AGI by 2070, Christiano 2023 (~20% given powerful AI), and Greenblatt's 7–75% across coordination levels. Against the 2026-10-30 race-game figure, insider-level numbers sit in the range where verification matters; the researcher median and superforecaster numbers sit below even the verified Stag line.
- Jones (2025) v2.0's robust result is the GDP shares (15.8% baseline; Monte Carlo mean 8.1%; 65% of draws ≥1%), not the 50x multiplier, whose denominator is weak.

## Decisions Made
- The p(doom) list lives in GAA (Dan's call); the web-pass file is companion data, and the main file is the one to cite.
- Archive copies are acceptable sources (Dan, 2026-10-30); in practice the routes didn't work.
- H in the race game should be p(doom | ASI) or p(doom | AGI) (Dan, 2026-10-31).
- The ~$10M value of a statistical life is accepted for order-of-magnitude "no-brainer" checks; no need to chase exact current DOT/EPA figures (Dan, 2026-10-31).
- The Jones / value-of-life material belongs in econ-impact.

## Results
- `general-ai-abilities/agent-briefs/20261030_pdoom_estimates.md` — the sourced list (commits `c34f40d` … `38579e3`, plus the Jones fix in this close-out)
- `verification/docs/results/20261031_pdoom_anchors.md` — p(doom | AGI) anchors placed against the race game's thresholds (`0a46397`)
- `econ-impact/papers/JonesC__2025--how-much-should-we-spend-to-reduce-ai-existential-risk.pdf` (v2.0), with text and summary slug `jones-25-spend-reduce-ai-xrisk`
- econ-impact issue #96 — value of a statistical life (~$10M) hard-number record, with comment on Dan's acceptance and the 30x → 50x correction
- `policy-levers/PAPER_INDEX.md` — Jones (2024) row corrected

## Open Questions
- The rest of the manual-check list in the GAA file (about 17 items: X posts, BBC Newsnight horizon for Hinton, Khan on Hard Fork, the Bores audio, Nanda's Reuters paraphrase vs his refusal policy).
- Whether the GAA Overton briefing's "~27 members of Congress" line should be reworded: it counts members who *commented*, but sits beside p(doom) numbers.
- econ-impact's "~2.5% tolerable" for Jones (2024) doesn't match its simple-model Table 1; it may come from the second model, which hasn't been checked.
- Whether the race game's H should be chosen from one group's numbers (insiders vs researchers vs superforecasters) or shown as a band; the model's verdict on verification turns on that choice.
