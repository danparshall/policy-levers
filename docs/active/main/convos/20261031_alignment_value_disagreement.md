# alignment_value_disagreement

**Date:** 2026-10-31
**Branch:** main
**Surface:** claude.ai
**Machine:** sandbox
**Session:** Dan (web, policy-levers, 20261031T1353, opus-5.5) · — · https://claude.ai/code/session_01HDEm374G4yqQB9SLyjG4PQ

## Summary

Brainstorm for interview-ready examples of "alignment is hard because humans can't even agree on values, and AI will be more alien still." Dan's private go-to example (death for apostasy in Islam) was fact-checked. The Pew 2013 data supports roughly 40% of Muslims, population-weighted across the 37 countries asked, not "over half." The "shop" argument Dan remembered was traced to IslamQA #20327. Among large religions today the position is effectively unique to Islam; the usable parallel is historical, from Christendom around 1526. That led to a reframing: an AI aligned to the 1550 consensus would have endorsed killing heretics, so which era's values do we freeze?

Low-spice replacements were developed and partly verified: cancer-diagnosis disclosure (US physicians flipped from about 90% non-disclosure in 1961 to over 90% disclosure in 1979), Haidt's family-dog study, and the Moral Machine plus the German Ethics Commission's Guideline 9. Kleinberg/Chouldechova fairness impossibility was added for technical audiences. The heights example was tied to Scott Alexander's Dec 2022 ACX post, whose thesis turned out to be about *control* (RLHF whack-a-mole), not "HHH has no clean answer."

Dan's draft framing was critiqued. The key fix is to separate the specification problem (no agreed target, and no agreed *method* for choosing one) from the verification/control problem, joined by "the default is not neutrality." Dan also tested the model's pull to caveat on group-difference questions; the model reported that its caveating tracked social salience rather than epistemic uncertainty. The snippets file captures all of this with verified/memory flags.

## Topics Explored
- Pew apostasy figures: conditional tables vs. full-respondent tables; Yaqeen (Jonathan Brown) positive vs. normative claims; IslamQA as a Salafi source that ranks highly in search
- Other religions and apostasy: Judaism (Deut. 13, rabbinic near-abolition), Christendom (Aquinas, Servetus, 1612), Hinduism/Buddhism
- Cancer disclosure, Haidt 1993, Moral Machine 2018, German Guideline 9 (and the commission's own non-consensus on minimising deaths)
- COMPAS / Chouldechova / Kleinberg context; neutral reframing via cancer screening by age
- ACX "Perhaps It Is A Bad Thing…" (12 Dec 2022) on heights and the control problem
- Live test of the model's caveating on homicide by race (BJS), credit by ethnicity (Fed 2007), and the water-level task by sex
- Public-choice reading of Guideline 9 (rejected); automaker involvement (Daimler and VW sat on the commission; no lobbying evidence found)

## Provisional Findings
- "Over half the world's Muslims" is not supported; about 40% in the countries surveyed is defensible.
- The strongest spine argument: liberal pluralism is not a neutral method, since a large share of humanity explicitly rejects it (the IslamQA "shop" argument). So there is no agreed target and no agreed procedure for choosing one.
- The heights example is a control failure, not a values conflict; present it separately from cancer disclosure, which is a real trade-off.
- English search results (and plausibly training data) overrepresent the strict end on apostasy: Salafi sites and critics both say "yes"; reformist scholars rank lower.
- Moral Machine respondents' age did not drive their preferences, which undercuts the "old bureaucrats save themselves" story; constitutional doctrine explains Guideline 9.

## Decisions Made
- Recommended order for interviews: dog → cancer → car, with heights last as the control-failure illustration.
- Use the 1526 historical framing rather than present-tense "other religions do it too."

## Results
- [results/20261031_alignment_value_disagreement_snippets.md](../results/20261031_alignment_value_disagreement_snippets.md): interview snippets with verified/memory flags

## Open Questions
- Verify the memory-flagged items before public use: the Haidt class-vs-country effect size, East Asian disclosure statistics, Moral Machine country-level correlations, and the Guideline 9 wording (already partly verified).
- Read ACX "The Road To Honest AI" for the honesty section (not read).
- Industry lobbying on Guideline 9: would need the full commission report membership or FOI; currently "unsupported, not refuted."
