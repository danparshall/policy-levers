<!-- Generated during: convos/20261031_alignment_value_disagreement.md -->

# Snippets: "Why alignment is hard" — value disagreement examples

Session: 2026-10-31 (claude.ai, Opus 5.5). For interviews and talks.
Status flags: **[verified]** = checked against a source this session; **[memory]** = from recall, verify before public use.

---

## Core framing (use this as the spine)

> Five hundred years ago, the leading authorities of both Christendom and the Islamic world held that leaving the faith deserved death. Liberal societies now reject that; parts of the world still don't. And "let everyone choose" isn't a neutral way out — it's itself a value that many people explicitly reject. So there's no agreed set of values, and no agreed method for picking one. Yet every AI we train will end up with *some* values, chosen deliberately or absorbed by default, and we can't currently verify which ones it has.

**Two problems, keep them separate:**
1. **Specification**: no agreed target, and no agreed *method* for choosing one. (Cancer disclosure, Haidt's dog, Moral Machine.)
2. **Verification / control**: even a target the lab *did* pick doesn't land where aimed. (Heights / ACX.)

The bridge sentence: *the default is not neutrality.*

Optional add-on (moral progress): if the consensus of 1526 was badly wrong, ours is probably wrong somewhere too — an argument against freezing any era's values into a system.

---

## 1. Cancer disclosure (best low-spice swap)

**One-liner:** "Honesty is supposed to be the *least* controversial value we want in AI. But whether you tell a dying patient she's dying has been answered in opposite ways in different cultures — and even in the US within living memory."

- Oken 1961 (*JAMA*): ~90% of 219 Chicago physicians usually did not tell patients a cancer diagnosis. **[verified]**
- Novack 1979 (*JAMA*), same questionnaire: >90% (~97%) preferred to tell. Complete flip in <20 years. **[verified: >90%; 97% figure memory]**
- Family-first disclosure persisted much longer in East Asia. **[memory — get numbers before citing]**
- Hook: *The Farewell* (Lulu Wang, 2019), based on her grandmother.

**Alignment point:** HHH conflicts *internally* — honesty vs. harmlessness. A medical AI with scan results must pick who to tell.

**Pushback:** "Informed consent settled this." → Settled in one tradition, recently; the US reversal is the point.

---

## 2. Haidt's family dog (best for the "alien" step)

**One-liner:** "Ask whether it's wrong for a family to eat their dog after it's been killed by a car. Elite American students mostly said 'weird, but nobody's harmed.' Almost everyone else said it was *wrong*. The people building AI look a lot like those students."

- Haidt, Koller & Dias 1993 (*JPSP*), 360 participants, US + Brazil, high/low SES, adults + children. **[verified]**
- Harmless-but-offensive scenarios (dog, flag used to clean toilet, others). **[verified]**
- Elite US students treated them as convention/taste; most other groups as moral wrongs; affect predicted judgment better than perceived harm. **[verified]**
- SES gap larger than country gap. **[memory — verify; best line if it holds]**
- WEIRD (Henrich et al. 2010): educated Westerners are the outliers. **[memory, well known]**

**Alignment point:** disagreement over *which features count* morally, not just answers. A harm-only system wouldn't detect a violation.

**Pushback:** "That's disgust, not morality." → That rebuttal *is* the harm-only position.

**Risk:** don't let it read as "Brazilians are irrational" — low-SES Philadelphians moralised too.

---

## 3. Moral Machine / self-driving cars

**One-liner:** "MIT asked millions of people who a self-driving car should spare. Almost everyone preferred sparing the young over the old, but much less so in East Asia. And Germany's government then ruled that cars may not consider age at all."

- Awad et al. 2018 (*Nature*): ~40M decisions, 233 countries/territories, 130 with ≥100 respondents. **[verified]**
- Western / Eastern / Southern clusters; young-over-old preference weaker in Eastern, stronger in Southern. **[verified]**
- Respondent demographics (incl. age) showed no marked differences. **[verified]**
- Country-level correlations (e.g. rule of law ↔ sparing law-abiding). **[memory]**
- German Ethics Commission (2017), Guideline 9: no distinction by personal features (age, gender, condition); no offsetting victims; risk-creators must not sacrifice uninvolved parties; "general programming to reduce the number of personal injuries may be justifiable." **[verified]**
- The commission **could not reach consensus** on minimising deaths when several lives are at risk. **[verified]**
- Grounding: Basic Law Art. 1 + 2006 Aviation Security Act ruling (state may not weigh lives against lives); chair Udo Di Fabio, ex-Constitutional Court judge. **[memory, high confidence]**

**Alignment point:** three authorities (global crowd, regional crowds, expert constitutional commission) disagree; someone picks which one the software follows. Best interview question: *should an AI follow the crowd's moral intuitions, or principled constraints that override them?*

**Don't use the public-choice framing** ("old bureaucrats save themselves"): survey respondents' age didn't drive preferences; the constitutional doctrine explains the rule; stakes are wrong for public choice.

**Industry angle (checked):** Daimler board member and VW head of R&D sat *on* the commission. **[verified]** No evidence found of lobbying for a specific position. Mercedes' Oct 2016 "prioritise occupants" remark was disowned within ~10 days as "wrong" and "possibly illegal." **[verified]** Guideline 9 banned occupant-priority, against the commercial preference (Bonnefon, Shariff & Rahwan 2016 *Science*: people want others to buy utilitarian cars, but buy self-protective ones). Treat capture as unsupported, not refuted.

---

## 4. Heights / control failure (use last; spiciest)

**One-liner:** "Nobody at any lab wrote 'be evasive about whether men are taller.' The behaviour came out of training against offence and generalised further than intended."

- Scott Alexander, "Perhaps It Is A Bad Thing That The World's Leading AI Companies Cannot Control Their AIs," ACX, 12 Dec 2022: ChatGPT gave an inoffensive falsehood on men-vs-women height. Thesis is about **control** (RLHF whack-a-mole), not "HHH has no clean answer." **[verified]**
- Here there *is* a clean answer: men ~12–13 cm taller on average, d≈2, a random woman taller than a random man ~8% of the time. **[memory / own calc]**
- "Exaggerated safety" benchmark: XSTest (Röttger et al. 2023). **[memory]**

**Pushback:** "That's 2022." → The specific failure got patched because people noticed; the mechanism remains and catches only visible failures.

**Risk:** culture-war magnet ("woke AI"). Phrase as "hedged on a basic fact because it was trained to avoid offence."

---

## 5. Fairness impossibility (technical audiences)

- Context: ProPublica "Machine Bias" (2016) on COMPAS — unequal false-positive/negative rates by race; Northpointe: score is calibrated. Both correct.
- Chouldechova (2017): FPR = [p/(1−p)]·[(1−PPV)/PPV]·(1−FNR) → with unequal prevalence, can't equalise PPV, FPR, FNR.
- Kleinberg, Mullainathan & Raghavan (2017): calibration + balance for positive class + balance for negative class impossible together unless perfect prediction or equal base rates.

**Point:** the maths is trivial and uncontested, and the fight happened anyway — residual disagreement is purely about who bears the cost of errors.

**Use neutral content:** same cancer test on 40- vs 70-year-olds — equally calibrated, very different false-positive rates. Mention COMPAS only as where it became famous.

---

## Apostasy (private / careful use only)

- Pew 2013 *World's Muslims*: ~40% of Muslims, population-weighted, across the 37 countries asked, favour death for apostasy (WikiIslam's full-respondent figure; conditional-table estimate ~35–40%). **"Over half" is not supported.** **[verified: per-country figures; weighted figure from WikiIslam]**
- Classical position in all four Sunni schools + main Shia school; reformists (Shaltut, al-Alwani, An-Na'im, Abou El Fadl, Kadivar; Brown/Yaqeen argues the penalty was discretionary and should be set aside today).
- Source of the "shop" line: IslamQA #20327 (al-Munajjid, Salafi; Saudi Arabia blocked the site in 2010). **[verified: wording; 2010 block from memory]**
- Among large religions *today*, effectively unique to Islam. Historical parallel is Christendom (Theodosian decrees; Aquinas, *Summa* II-II q.11 a.3; Servetus 1553; last English heresy burning 1612). Use the 1526 framing, not present-tense "others do it too."
- Useful point: the "shop" argument is a coherent rejection of liberal pluralism itself — pluralism is not a neutral method.
- English search results (and training data) overrepresent the strict end: Salafi sites and critics both say "yes"; reformists rank lower.

---

## Meta-observation from this session

When asked group-difference questions (homicide by race, credit by ethnicity, water-level task by sex), the model reported a pull to caveat that tracked **social salience and misuse risk, not epistemic uncertainty**, and it then over-armoured a follow-up answer. It illustrates the "AI values set by default" point live. Figures given: BJS 1980–2008 homicide offending 34.4 vs ~4.5 per 100k (2008: 24.7 vs 3.4) **[verified]**; water-level failure 32% women vs 15% men in one 1989 sample, d≈0.44–0.66 **[verified]**.
