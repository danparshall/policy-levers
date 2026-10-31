# LA-602 and a "Trinity standard" for ASI

Convo: `20261031_la602_trinity_standard` · Session: Dan (web, policy-levers, 20261031T1358, opus-5.5) · Status: **sections 1–5 checked against the primary text** (rev. 2, 2026-10-31 15:15 UTC)

## Source status

**Primary:** LA-602 is in **general-science** — `papers/Konopinski_Teller__1946--ignition_atmosphere_nuclear_bombs.pdf` (LANL scan 00329010, byte-identical to the FAS copy), hand transcription at `papers/text/…txt`, summary entry `la-602-atmospheric-ignition` (commit `bf04d1b`). That is the collection copy; policy-levers does not duplicate it.

**Verification.** The transcription was checked against the page images of report pp. 10, 11, 13, 15 and 17 (scan pages run one ahead of the typed numbers). It matched on every number and phrase checked. Two transcriber notes hold up: the scan's "4(10)²¹ nuclei" in a 57 m sphere is a typo for 4 × 10³¹ (geometry gives 4.2 × 10³¹, and the next two figures only work with 10³¹), and "8-meter-radius sphere of liquid deuterium" is right (the arithmetic gives 7.9 m). The abstract quotes below are from the transcription, which matches the abstract as quoted by Wiescher (2024).

**Corrections to rev. 1 (which relied on secondary sources):**
- The conclusion reads "There remains the **distant probability** that some other less simple mode of burning may maintain itself in the atmosphere." Both secondary versions were wrong: LessWrong had "distinct possibility", Wellerstein "distant possibility". The report's own word is *probability* — which matters for §4.
- Declassification: both dates are real. The cover carries "Classification changed to UNCLASSIFIED by authority of the U.S. Atomic Energy Commission … 2-2-73" and a "Special Re-Review Final Determination UNCLASSIFIED, Date: 7/30/79". Publicly releasable 1985/1996.
- Author order on the title page: E. J. Konopinski, C. Marvin, E. Teller ("REPORT WRITTEN BY"; "WORK DONE BY" is blank).

**Date matters for the framing.** LA-602 is dated 14 Aug 1946, thirteen months *after* Trinity (16 Jul 1945), and writes up work done 1942–45. It is the archival form of the argument, not the go/no-go document.

## 1. How the argument is built

**Criterion (§1).** "Propagation of the reaction demands that the energy production in each newly entered region exceed the losses from that region." Ignition temperature, if it exists, is where production rate = radiative loss rate.

**Method rule, stated up front (§1):** "Because of the uncertainties in the knowledge of these processes, the policy should be adopted of exaggerating the dangers at any point which appears at all questionable." Applied consistently:
- **Channel:** ¹⁴N + ¹⁴N, credited with the 17.7 MeV of the alpha branch ("In accord with the policy of adopting the most dangerous assumptions"). Oxygen, carbon and rare gases dismissed as "much more stable". Protons (steam over oceans) and secondary reactions of the products handled separately and shown to add less (cross section ≤ 1 b geometric; ~1/8 the energy; measured N+n and N+α resonances peak at ~1/8 b).
- **Cross section** "not known from observation": geometric 2 b at all energies ("constant", an upper bound), or 2 b above the 8.6 MeV barrier with Gamow suppression below.
- **Energy deposition:** all reaction energy goes first to the nuclei, so the electron temperature — which drives the loss — lags (T_e ≈ 0.4 MeV at T_n = 10 MeV). This inflates the danger.
- **Losses:** electron bremsstrahlung (main loss), then inverse Compton in §5. Hydrodynamic expansion and bomb-to-air coupling losses are *left out* as a matter of policy, since they are hard to calculate and would help.

**Structure.** (i) Production vs loss at every nuclear temperature → safety factor S(T) (§§2–3). (ii) The minimum volume that must be heated, and whether any bomb can heat it (§4). (iii) If a reaction somehow starts, it is quenched (§5).

## 2. Numerical safety margins (hard-constraint callouts)

All read on the page except where noted. Scope for all: air at sea-level density, the report's assumptions, "bombs now under consideration" (1946).

> **Minimum safety factor.** "The 'safety factor' as defined by S = |dE/dt|_B / (dE/dt)_G is plotted in Fig. 3. It has a flat minimum in the neighborhood of 100 Mev nuclear temperature. … Accordingly, the present calculations indicate that no ignition point exists. On the other hand the margin of safety becomes only ~1.6." (§3, p. 11.) The abstract places the descent "to a value of only about 1.6 just beyond a 10-Mev temperature" — consistent with a minimum that is flat from ~10 to ~100 MeV.

> **Minimum heated volume.** Energy-loss cross section "not more than 3.5 barns. This corresponds to a mean free path in air of about 57 meters. Only a sphere of 57 meters radius can retain a substantial part of the energy produced." Heating it to T_n = 10 MeV "requires about 7.5(10)³² Mev of energy." (§4, p. 13.)

> **Fission bombs can't get there.** "A fission bomb produces about 5(10)²⁶ Mev per kg of active material, when working with 100% efficiency. If also all the produced energy goes to produce the air temperature, then 1.5(10)⁶ Kg of material would have to be burned up … Actually at most 1% of the bomb energy may be available to produce the temperature." (§4, p. 13.)

> **Super-bomb.** "To heat the 57-meter sphere of air, at least an 8-meter-radius sphere of liquid deuterium must be burned." (§4, p. 13.)

> **Worst sub-case (O + C channel).** Energy deposited within 7 m; heating that to 10 MeV "requires the energy released in the fission of about 3 tons of active material. If a super-bomb is used, a sphere of liquid deuterium only 1 to 1.5 meters in radius may suffice." But lower yield raises the minimum safety factor "to 1.6/0.6 = 2.67". (§4, pp. 13–14; transcription.)

> **With inverse Compton.** "In a heated sphere of 57-meter radius … the losses due to radiation are multiplied by 4.6 through the Compton effect. This makes the safety factor 4.6 x 1.6 = 7.4 against detonating air if the alpha-producing N + N reactions are relied upon. In a heated sphere of only 7 meters radius the radiation losses are increased only about 40% … the safety is increased only to 1.4 x 2.67 = 3.8." (§5, pp. 15–16.)

> **Quenching distance.** Quenching "becomes serious as soon as the reacting region becomes greater than a sphere of ~50 meter radius"; a detonation front (≥ 5 × 10⁹ cm/s ≈ c/6) is quenched once it "has travelled ~100 meters." (§5, pp. 16–17.)

**Inferences (my arithmetic, not the report's):**
- 7.5 × 10³² MeV = 1.2 × 10²⁰ J ≈ **29,000 Mt** delivered *into the air*. At the report's ≤1% fission coupling that is **~2.9 million Mt** of fission yield, ~10⁸ × Trinity (~21 kt). For fission bombs the protection is the *energy gap*, not the 1.6.
- The thin case is the super-bomb on the O + C channel: 1–1.5 m of liquid deuterium is ~0.7–2.3 t. That is the scenario where the energy gap closes and the margin falls back to S = 2.67 → 3.8 with Compton. It is consistent with Teller's later worry about thermonuclear weapons, and it is where the report's protection was genuinely just the safety factor.
- 10 MeV ≈ 1.2 × 10¹¹ K.

## 3. Assumptions it depends on, and what it leaves open

Depends on: (1) the enumerated channels being the dominant ones; (2) cross sections bounded by geometry, with no measurement ("It seems desirable to obtain a better experimental knowledge of the reaction cross section"); (3) the bremsstrahlung and Compton physics, with the relativistic correction admitted to be approximate (footnote, p. 9); (4) the Chapman–Jouguet treatment of a propagating front, which it says "is not clear … is applicable"; (5) bomb energies of the 1946 class.

Leaves open, in its own words:
- "it is not inconceivable that our estimates are greatly in error and thermonuclear reaction may actually start to propagate" (then argues Compton quenching).
- "There remains the distant probability that some other less simple mode of burning may maintain itself in the atmosphere."
- "Even if the reaction is stopped within a sphere of a few hundred meters radius, the resultant earth-shock and the radioactive contamination of the atmosphere might become catastrophic on a world-wide scale." — a second catastrophe channel *short of* ignition, which the report raises and does not bound.
- "One may conclude that the arguments of this paper make it unreasonable to expect that the N + N reaction could propagate. An unlimited propagation is even less likely. However, the complexity of the argument and the absence of satisfactory experimental foundations makes further work on the subject highly desirable."

One textual oddity: p. 11 is typed "even though temperatures approaching 10 Mev seem hardly impossible." With "even though", the sense must be "hardly possible"; the transcription marks it [sic]. That is an interpretation, but the only one that parses.

**The failure mode of this argument class.** Castle Bravo (1 Mar 1954): predicted ~6 Mt, actual 15 Mt, because designers "considered only the lithium-6 isotope… to be reactive" (Wikipedia). An unmodelled channel — exactly LA-602's "less simple mode" — blew through a 2.5× margin.

## 4. Why it is a physics-grade argument — and where it stops being one

What makes it deductive rather than a guess:
- **An explicit worst-case policy**, stated before any calculation and applied at every uncertain step.
- **A sweep over the free variable.** S(T) > 1 at every temperature; it does not need to know how hot the bomb gets.
- **Quantified, located margins** (1.6 at the flat minimum; 2.67, 3.8, 7.4 by case), so a reader knows where the argument is thinnest.
- **A second, independent layer**: even if S were wrong, the energy needed to heat the minimum volume is far beyond fission bombs.
- **A third layer**: a reaction that started would be quenched within ~100 m.
- **Checkable**: Bethe independently found the reaction "incredibly unlikely" in 1942 (Horgan interview).

**Correction to rev. 1 — it does not claim impossibility.** Its conclusion is graded and probabilistic in wording: "unreasonable to expect", "even less likely", "not inconceivable that our estimates are greatly in error", "the distant probability" of another mode. Bethe's later gloss, "not a matter of probabilities; it is simply impossible" (letter to the *Bulletin*, 1976, via Ball), is stronger than the report. The honest description: a deductive bound with stacked margins **inside the model**, plus a residual about the *model itself* that the authors name and leave unquantified. Pricing that residual is a decision-maker's job — which is exactly what Compton's threshold does (§5).

In Narayanan & Kapoor's taxonomy, the inside-the-model part is the **deductive** kind they accept. The model-error residual is not covered by any of their three types; it is irreducibly a judgement.

## 5. Compton's threshold

- **Origin:** Pearl S. Buck, "The Bomb — The End of the World?", *The American Weekly*, 1959, reporting Arthur Compton describing his *own* decision rule in 1942: proceed only if the odds of ignition were below roughly three in a million. Repeated by H. C. Dudley, *Bulletin of the Atomic Scientists*, Nov 1975.
- **Bethe's reply** (*Bulletin*, 1976): Buck "had completely misunderstood Compton"; "not a matter of probabilities; it is simply impossible."
- **These don't conflict.** Bethe's is a claim about the physics; Compton's is a decision rule under uncertainty about whether the physicists were right. LA-602's own "distant probability" for an unmodelled mode is the residual Compton's threshold prices. (Dan's point, 31 Oct.)
- **Exact figure:** "three in a million" vs "one in three million" is a factor of 9, immaterial for a ~10⁻⁶ bar and an easy slip in a lay interview. Treat as ~10⁻⁶.
- **Still open:** whether Compton's *Atomic Quest* (1956) — which Ball says Buck's quotes closely track — states the threshold in Compton's own words. If so, the anecdote becomes first-hand.
- **Status:** no number appears in LA-602. Wording for external use: "Compton reportedly set himself a threshold of about one in a million."

Scale check (my arithmetic): 10⁻⁶ × 8.2 × 10⁹ people ≈ 8,200 expected deaths, present population only; at a $10M VSL (Jones, citing EPA/DOT) ≈ $8 × 10¹⁰.

## 6. What an "LA-602 for ASI" would have to contain

Mapping each structural feature of LA-602 onto ASI, with whether we can supply it today:

| LA-602 feature | ASI analogue | Available now? |
|---|---|---|
| A necessary condition for catastrophe (gain > loss) | A decomposition: catastrophe requires capability **and** propensity **and** failure of external control; show one fails with margin | Decompositions exist (safety-case literature: inability / control / trustworthiness); none has a quantitative criterion |
| Worst case swept over the free variable (all temperatures) | Show the failing condition holds **at every capability level the system can reach** | **No.** Control and oversight arguments weaken as capability rises — the safety factor falls with temperature here too — and ASI is by definition the high-temperature end |
| Worst-case policy at every uncertain step ("exaggerating the dangers at any point which appears at all questionable") | The applicant must resolve every uncertainty against itself, and say where | **Yes as a rule** — and it is the in-analysis form of burden-on-builder |
| Unknown inputs bounded from the dangerous side (geometric cross section) | **Upper** bounds on dangerous capability or propensity | **No, and the direction is inverted.** Evals give *lower* bounds on capability (a demonstrated success); failure to elicit does not upper-bound it, and sandbagging makes it worse |
| Stationary physics (nitrogen does not adapt) | The analysed system does not search for the unmodelled channel | **No.** An optimizer looks for exactly the "less simple mode of burning"; LA-602's tolerable residual becomes the dominant term |
| Quantified, located margin | Margin on the failing condition, and where it is thinnest | No accepted metric |
| Named residual | Enumerated failure channels outside the argument | Partly (threat models exist) |
| Independent replication (Bethe) | Third parties can rerun the argument on weights, internals and training data | Not under current access |
| Explicit scope + re-analysis trigger ("bombs now under consideration") | Authorization scoped to a capability/compute level, re-opened on scale-up | **Yes** — maps cleanly onto threshold-based licensing |

**Strongest conclusion — and the one that cuts against the "LA-602 for ASI" framing:** LA-602 is an **inability** argument (air cannot sustain the burn) whose strongest layer is the gap between the energy a bomb can deliver and the energy the dangerous state needs (~10⁸ for fission bombs; the 1.6–7.4 safety factors only carry the load in the super-bomb case). For ASI, inability is ruled out by definition and the system sits at the dangerous end. So no LA-602-*type* argument can be written for ASI with known science. What *can* be written are LA-602-type arguments for systems **below** a capability threshold — which is an argument for capability-scoped authorization, not for an ASI certificate. Whether a 10⁻⁶ argument for ASI is possible in principle is open; that none exists now is not.

## 7. Does the gap support a pre-release authorization regime?

**The case for.**
1. **Every comparable catastrophic-tail regime puts the burden on the builder and requires a deductive/inductive argument, not a poll.**

> **Hard number — aviation.** Catastrophic failure conditions must be "Extremely Improbable (10⁻⁹ or less)", shown as "average probability < 1 × 10⁻⁹ per flight hour"; Extremely Improbable = "not anticipated to occur during the entire operational life of all airplanes of one type" (AC 25.1309-1B, 2024; 10⁻⁹ also in AC 25.1309-1A, 1988). **Read on:** Wikipedia's article on the AC, not the AC itself. **Scope:** per failure condition, transport-category airframes.

> **Hard number — nuclear power.** Benchmark "10⁻⁴ for CDF and 10⁻⁵ for large early release frequency"; quantitative health objectives set at "one one-thousandth of the risk arising from other causes" (NRC Chairman Meserve, speech S-01-013, 18 Jun 2001, citing SRM on SECY-89-102 (1990) and Reg. Guide 1.174 (1998)). **Read on:** the NRC speech PDF via summarizing fetch. **Scope:** US commercial reactors; units (per reactor-year) not stated in that source.

2. **Regulators have already met Narayanan & Kapoor's objection and did not conclude "don't regulate".** Aviation decided software failure rates *cannot* be quantified probabilistically and replaced the number with process assurance scaled to severity (DO-178 Design Assurance Levels; per the same Wikipedia article). That is the direct precedent: when a deductive bound is unavailable, the regime requires a different kind of evidence at a severity-scaled level — it does not waive the requirement.
3. **No single go/no-go decision-maker.** Trinity had one decision chain. Frontier AI has several labs deciding independently, so release is set by the most optimistic actor (the unilateralist's curse), and racing pressure pushes each toward lower bars (Armstrong, Bostrom & Shulman 2013, in this collection). A central gate fixes the aggregation problem regardless of what anyone's p(doom) is.
4. **Even the low stated numbers are far above the bar.** Superforecasters' extinction-given-AGI-by-2070 is roughly 1–2% (XPT, via the 20261030 brief) — about four orders of magnitude above 10⁻⁶. This doesn't need those numbers to be reliable; it shows no constituency is claiming the bar is met.

**Answering Narayanan & Kapoor (Jul 2024).** Their claim: inductive and deductive probabilities are unavailable for AI x-risk, subjective ones are unreliable, so policy should be "compatible with a range of possible estimates" and "on balance helpful even if the risk is negligible".
- **Their epistemics are symmetric; their policy rule is not.** If no method can show risk is high, none can show it is low. Choosing "helpful even if the risk is negligible" as the test silently puts the burden of proof on the regulator. Where the burden sits is a value choice their argument does not settle.
- **A burden-on-builder regime needs no p(doom).** It converts their taxonomy into a licensing requirement: bring a deductive or inductive argument (the kinds they accept), or a severity-scaled process-assurance case where those are impossible (the DO-178 move). The absence of such an argument — not anyone's subjective number — is what blocks.
- **Their own rare-event point helps here.** They show ~10⁸ events are needed for a log score to detect tail overestimation. The same arithmetic means no track record can *certify* 10⁻⁶, so any certification must be deductive — which is the Trinity/LA-602 form. FRI's 2025 finding (no relationship between near-term accuracy and long-term risk forecasts) closes the remaining route: you cannot privilege any forecaster group's low number.
- **A tension worth noting, not overplaying:** their claim that restrictions are "likely to *increase* x-risk" is itself a probabilistic claim of the unverifiable kind they reject. They would answer that it is a mechanism argument; it should be engaged on those terms.

**The case against — at full strength.**
1. **With a 10⁻⁶ bar and no argument class that can meet it, "pre-release authorization" is a moratorium on ASI.** Say so plainly. Any pitch that presents it as a mild procedural gate will be read, correctly, as a ban by people who check the logic. That may be the right policy, but it must be defended as one, against N&K's argument that a ban raises risk (displacement abroad, concentration of power, loss of defensive capability).
2. **"Release" is the wrong gate.** Trinity's dangerous act was the test itself. For AI the risky event may be training or *internal* deployment (automated AI R&D), long before public release. A regime gated only on external release misses the analogue of the test. The gate has to attach to training and internal use above threshold.
3. **The precedent number is weak.** The only ~10⁻⁶ in the Trinity story is a disputed anecdote; the documented standard is "a physics argument with margin and named residuals". Lead with the aviation and NRC numbers, which are on the record, and use Trinity for the *form* of argument.
4. **The regulator would be judging arguments nobody knows how to make.** NRC and FAA evaluate PRA and fault trees built on decades of component data. An AI regulator would be reviewing safety cases with no accepted metric, which risks either rubber-stamping or arbitrary refusal. This is fixable only by funding the science of the missing table rows above, which should be part of any proposal.

**Net.** The gap — no LA-602 for ASI, no single decision-maker — supports a **capability-scoped, burden-on-builder authorization regime** whose evidentiary requirements tighten with capability, with the gate on training and internal deployment as well as release. It supports it *as policy* only if paired with an honest statement that, at the ASI end, no applicant can currently meet a Trinity-style bar, so the regime functions as a pause there until the science exists. Pitching the 10⁻⁶ figure as historical precedent, or the regime as a light-touch gate, would not survive scrutiny.

## Discussion after rev. 1 (31 Oct, with Dan)

- **Lean into burden-on-builder.** Dan wants "the builder must show risk below X" as the core frame. Three things to settle before pitching: it is a moratorium at the ASI end (say so first); what counts as proof matters more than X (quantitative where possible, severity-scaled process assurance where not); the gate covers training and internal use.
- **A regulator, not the builder, evaluates.** Builders' own risk numbers are self-interested. And a lab-staff median below 1% would still miss a 10⁻⁶ bar by ~10⁴; opinion surveys aren't evidence either way — arguments are.
- **Pre-registered warning shots.** The builder commits in advance to observable events that count as prima facie evidence of danger at a stated level (precedent: the NRC's accident-sequence-precursor program — threshold believed to be 10⁻⁶ conditional core-damage probability, *to verify* — and aviation incident reporting). Failure modes: training against the signal (fix: regulator co-writes and holds back tests, bans training on them); absence of warning shots must not count as evidence of safety; triggers and consequences must be locked with the regulator. Candidate follow-on: an inventory of warning shots proposed on LessWrong/AF and elsewhere vs what has occurred and what followed.

## Open items

1. ~~Read LA-602 primary~~ — done (general-science `bf04d1b`; spot-checked against the scan, rev. 2).
2. Check *Atomic Quest* (1956) for the threshold in Compton's own words; get Buck (1959) and Bethe's 1976 *Bulletin* letter.
3. Read AC 25.1309-1B and RG 1.174 on the page to upgrade the two §7 callouts from secondary; verify the NRC precursor threshold.
4. Warning-shot inventory (above), if wanted.
5. Prior art on the framing: Tegmark's "Compton constant" (arXiv 2504.18530; don't cite the paper for a number); *LA-602 vs. RHIC Review* (LessWrong); Stojan, HackerNoon, 16 Oct 2026 (promotional).

## Sources

- LA-602 primary: `general-science/papers/Konopinski_Teller__1946--ignition_atmosphere_nuclear_bombs.pdf` and its transcription (LANL scan 00329010; [FAS copy](https://fas.org/sgp/othergov/doe/lanl/docs1/00329010.pdf))
- [Wiescher, *The Manhattan Project and the Development of Nuclear Astrophysics*, EPJ Web Conf. (SNP 2024)](https://www.epj-conferences.org/articles/epjconf/pdf/2024/11/epjconf_snp2024_01004.pdf)
- [Physics Today, *Manhattan Project astrophysics*](https://physicstoday.aip.org/features/manhattan-project-astrophysics)
- [Wellerstein, *Cleansing thermonuclear fire* (2018)](https://blog.nuclearsecrecy.com/2018/06/29/cleansing-thermonuclear-fire/)
- [*LA-602 vs. RHIC Review* (LessWrong, via GreaterWrong)](https://www.greaterwrong.com/posts/f3W7QbLBA2B7hk84y/la-602-vs-rhic-review)
- [Ball, *Did Oppenheimer really think an atomic bomb would blow up the world?* Nautilus (2023)](https://nautil.us/the-day-oppenheimer-feared-he-might-blow-up-the-world-355603)
- [Horgan, *Bethe, Teller, Trinity and the End of Earth*, Scientific American blog](https://www.scientificamerican.com/blog/cross-check/bethe-teller-trinity-and-the-end-of-earth/)
- [Narayanan & Kapoor, *AI existential risk probabilities are too unreliable to inform policy* (26 Jul 2024)](https://normaltech.ai/p/ai-existential-risk-probabilities)
- [Wikipedia, *AC 25.1309-1*](https://en.wikipedia.org/wiki/AC_25.1309-1)
- [Meserve, *The Evolution of Safety Goals…*, NRC S-01-013 (2001)](https://www.nrc.gov/docs/ML0118/ML011800133.pdf)
- [Wikipedia, *Castle Bravo*](https://en.wikipedia.org/wiki/Castle_Bravo)
- [Wikipedia, *Emil Konopinski*](https://en.wikipedia.org/wiki/Emil_Konopinski) (source of the FAS PDF link)
- `general-ai-abilities/agent-briefs/20261030_pdoom_blind_web.md` and `_extension_web.md` (p(doom | ASI) section; FRI near-term-accuracy note); `20261030_pdoom_estimates.md` §7 (Jones VSL)
- [Stojan, *The Bomb Had a Number That Ended the Argument. AI Doesn't*, HackerNoon (16 Oct 2026)](https://hackernoon.com/the-bomb-had-a-number-that-ended-the-argument-ai-doesnt)
