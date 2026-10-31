# LA-602 and a "Trinity standard" for ASI

Convo: `20261031_la602_trinity_standard` · Session: Dan (web, policy-levers, 20261031T1358, opus-5.5) · Status: **DRAFT — primary text of LA-602 not yet read**

## Source status (read this first)

The primary PDF (`https://fas.org/sgp/othergov/doe/lanl/docs1/00329010.pdf`, the copy cited by Wikipedia and by Wellerstein) could not be fetched this session: the workspace shell is blocked from fas.org and two WebFetch attempts timed out awaiting approval. **Every LA-602 sentence below is quoted through a secondary source and labelled with it.** Nothing here should go into a hard-constraint callout for external use until checked against the PDF. The paper-collection entry is deliberately held for the same reason.

The secondary sources already disagree on a word of the conclusion: Wellerstein (nuclearsecrecy, 2018) quotes "the **distant** possibility that some other less simple mode of burning may maintain itself"; the LessWrong *LA-602 vs. RHIC Review* post quotes "the **distinct** possibility". That word carries the residual-risk claim, so it must be read on the page.

Other conflicts to settle from the primary or a catalogue record:
- Declassification year: 1973 (Ball, Nautilus 2023) vs 1979 (Physics Today, *Manhattan Project astrophysics*).
- Author order/spelling: Konopinski, Marvin & Teller (title page per Wikipedia) vs "Teller, Konopinski, Marvin" (Ball) vs "Konopinsky" (EPJ reference list).

**Date matters for the framing.** LA-602 is dated 14 Aug 1946, thirteen months *after* Trinity (16 Jul 1945). It writes up calculations done 1942–45 (Berkeley summer study; Konopinski and Teller at Los Alamos; Bethe's independent check). So "builders produced LA-602 before proceeding" is wrong as history: the pre-test gate was the unwritten-up calculations plus (reportedly) Compton's threshold. LA-602 is the *archival form* of the argument, not the go/no-go document.

## 1. How the argument is built

**Question.** Can the hot region left by a fission bomb start a self-propagating nuclear reaction in air (or water)?

**Criterion.** An energy balance. Propagation requires the rate of energy production by fusion in the heated region to exceed the rate at which that region loses energy. Define the "safety factor" as loss rate ÷ production rate; ignition needs it below 1.

**Production side** (Physics Today; Wiescher, EPJ Web Conf 2024, describing the report's figure):
- Dominant channel: ¹⁴N + ¹⁴N, chosen because nitrogen dominates air. Also considered: ¹⁴N + H from dissociated water vapour; for the ocean, reactions involving oxygen and hydrogen.
- Two production curves, as bounding cases: a **constant (geometric) cross section** taken from nuclear size — an upper bound that ignores Coulomb suppression — and a **Gamow-penetration** cross section that falls steeply at low energy.

**Loss side:** radiative cooling — bremsstrahlung / X-ray emission and energy transfer from hot electrons to the radiation field by the Compton effect ("as predicted by Arthur Compton" in the figure caption, per EPJ). Air is thin enough that this radiation escapes or soaks up the energy.

**Structural move.** The report does not estimate how hot the bomb gets and then check that one point. It sweeps temperature and shows loss > production *at every temperature*, then locates the minimum margin and observes that the minimum sits at temperatures no fission bomb can reach. This is a worst case over the uncontrolled variable, not an estimate of it.

## 2. Numerical safety margins

> **Hard number — LA-602 minimum safety factor.** "The disquieting feature is that the "safety factor", i.e. the ratio of losses to gains of energy, decreases rapidly with the initial temperature, and descends to a value of only about 1.6 just beyond a 10-MeV temperature. It is impossible to reach such temperatures unless fission bombs or thermonuclear bombs are used which greatly exceed the bombs now under consideration."
> **Source:** LA-602 as quoted by M. Wiescher, *The Manhattan Project and the Development of Nuclear Astrophysics*, EPJ Web of Conferences (SNP 2024), §3. **Read on:** the EPJ PDF via a summarizing fetch, not LA-602 itself. **Scope:** air, ¹⁴N+¹⁴N with the report's cross-section assumptions; "bombs now under consideration" = 1945–46 fission weapons.

> **Hard number — abstract.** "The energy losses to radiation always overcompensate the gains due to reactions" (abstract, as quoted by Physics Today). **Read on:** Physics Today feature, via summarizing fetch. **Scope:** same.

**Inferences (my arithmetic, not the report's):**
- 10 MeV ≈ 1.2 × 10¹¹ K. Physics Today puts the relevant fireball temperatures at "a few million degrees", i.e. a few hundred eV. The temperature gap between where the bomb is and where the margin is thinnest is therefore **~10⁴–10⁵**.
- So the protection has two layers: (a) loss/gain ≥ ~1.6 even at the worst temperature; (b) the reachable temperature is four to five orders of magnitude below that worst point, where the factor is (per the report's wording) much larger. **The values of the safety factor at bomb-relevant temperatures are the numbers to extract from the primary** — the secondary sources give only the 1.6 minimum.
- Direction of the bound: 1.6 is a *floor* on loss/gain over all temperatures, under the report's cross sections. It says nothing about channels not modelled.

**What happened to the margin later.** Wiescher reports that Teller worried about the margin shrinking at "higher temperature and density conditions" — larger thermonuclear devices and deep underwater tests. Physics Today adds that 1950s Oak Ridge measurements found fusion probabilities *below* the geometric cross section assumed, i.e. the report's production estimate was conservative in the direction that mattered. Tsar Bomba (50 Mt, 1961) did not ignite anything.

## 3. Assumptions it depends on, and what it leaves open

Depends on:
1. **The modelled channels are the dominant ones** (¹⁴N+¹⁴N; N+H; O for water).
2. **Cross sections bounded from geometry**, with no measurement behind them ("crude… but most likely provided a reliable upper limit" — Wiescher's characterization).
3. **The radiation-loss physics** (bremsstrahlung, Compton coupling) applies in the regime considered.
4. **Bomb temperature** stays well below the ~10 MeV minimum-margin point (scope: "bombs now under consideration").

Leaves open (per the conclusion as quoted secondhand):
- "There remains the [distinct/distant] possibility that some other less simple mode of burning may maintain itself in the atmosphere."
- "the complexity of the argument and the absence of satisfactory experimental foundations makes further work on the subject highly desirable."
- Scope beyond 1946 bombs — explicitly flagged as a re-analysis trigger.

**The historical failure mode of this argument class.** Castle Bravo (1 Mar 1954): predicted ~6 Mt, actual 15 Mt, because designers "considered only the lithium-6 isotope… to be reactive" and lithium-7 was not inert (Wikipedia, *Castle Bravo*). A margin of 2.5× was blown through by an unmodelled channel — exactly LA-602's "less simple mode" residual. Physics-grade arguments do not fail by being slightly off; they fail by missing a mechanism, and the stated margin says nothing about that.

## 4. Why it is a physics-grade argument, not a probability

- **It is an inequality over a swept variable.** Loss > gain for every temperature, under inputs biased toward ignition. The output is "no", conditional on the model — not a number between 0 and 1.
- **Unknown inputs are bounded from the dangerous side.** The cross section, the one quantity they could not measure, is set to its geometric maximum.
- **The margin is quantified and located** (≥1.6, thinnest at ~10 MeV), so a reader knows where the argument is weakest.
- **The residual is named, not priced.** Unmodelled modes are stated as open; no probability is attached.
- **It was independently checkable and checked.** Bethe worked the problem in 1942 and found the reaction "incredibly unlikely"; he called Konopinski's calculations a detailed demonstration (Horgan interview, Scientific American blog).
- Bethe's own gloss (letter replying to Dudley, *Bulletin of the Atomic Scientists*, 1976, as quoted by Ball): **"Ignition is not a matter of probabilities; it is simply impossible."**

In Narayanan & Kapoor's taxonomy, LA-602 is the clean case of a **deductive (model-based)** argument — the kind they accept (they use the asteroid case the same way). It is not a subjective probability, and it contains no inductive base rate.

## 5. Compton's threshold — kept separate

- **Origin:** Pearl S. Buck, "The Bomb — The End of the World?", *The American Weekly*, 1959, reporting an interview with Arthur Compton. Repeated by H. C. Dudley, "The Ultimate Catastrophe", *Bulletin of the Atomic Scientists*, Nov 1975.
- **Rebuttal:** Bethe, replying in the *Bulletin* (1976): Buck "had completely misunderstood Compton"; "no chance whatever"; "not a matter of probabilities".
- **Two different numbers may be in play.** Ball (Nautilus 2023) gives Compton's *decision threshold* as "less-than three-in-1-million". Horgan gives Buck's report of the *computed* odds as "slightly less" than **one in three** million. 3 × 10⁻⁶ vs 3.3 × 10⁻⁷ differ by 9×. The handoff's "~3 in a million (or slightly less than one in three million)" may be conflating a threshold with an estimate. **Needs Buck's text.**
- **Provenance doubt:** Ball notes many of Buck's Compton quotes "repeat essentially verbatim" Compton's 1956 memoir *Atomic Quest*. Whether *Atomic Quest* itself contains a number is unverified — if it does, "the figure comes only from Buck" is false.
- **Status:** no number appears in LA-602. The ~10⁻⁶ "Trinity standard" is therefore a **normative proposal borrowing a disputed anecdote**, not a documented historical policy. Pitch it that way, or a hostile staffer will.

Scale check (my arithmetic): 10⁻⁶ × 8.2 × 10⁹ people ≈ 8,200 expected deaths, present population only. At a $10M VSL (Jones, citing EPA/DOT) that is ~$8 × 10¹⁰ — a cost-benefit-sized number, which is one reason 10⁻⁶ is a defensible bar.

## 6. What an "LA-602 for ASI" would have to contain

Mapping each structural feature of LA-602 onto ASI, with whether we can supply it today:

| LA-602 feature | ASI analogue | Available now? |
|---|---|---|
| A necessary condition for catastrophe (gain > loss) | A decomposition: catastrophe requires capability **and** propensity **and** failure of external control; show one fails with margin | Decompositions exist (safety-case literature: inability / control / trustworthiness); none has a quantitative criterion |
| Worst case swept over the free variable (all temperatures) | Show the failing condition holds **at every capability level the system can reach** | **No.** Control and oversight arguments weaken as capability rises — the safety factor falls with temperature here too — and ASI is by definition the high-temperature end |
| Unknown inputs bounded from the dangerous side (geometric cross section) | **Upper** bounds on dangerous capability or propensity | **No, and the direction is inverted.** Evals give *lower* bounds on capability (a demonstrated success); failure to elicit does not upper-bound it, and sandbagging makes it worse |
| Stationary physics (nitrogen does not adapt) | The analysed system does not search for the unmodelled channel | **No.** An optimizer looks for exactly the "less simple mode of burning"; LA-602's tolerable residual becomes the dominant term |
| Quantified, located margin | Margin on the failing condition, and where it is thinnest | No accepted metric |
| Named residual | Enumerated failure channels outside the argument | Partly (threat models exist) |
| Independent replication (Bethe) | Third parties can rerun the argument on weights, internals and training data | Not under current access |
| Explicit scope + re-analysis trigger ("bombs now under consideration") | Authorization scoped to a capability/compute level, re-opened on scale-up | **Yes** — maps cleanly onto threshold-based licensing |

**Strongest conclusion — and the one that cuts against the "LA-602 for ASI" framing:** LA-602 is an **inability** argument (air cannot sustain the burn) whose margin comes from the gap between reachable and dangerous temperatures. For ASI, inability is ruled out by definition and the system sits at the dangerous end. So no LA-602-*type* argument can be written for ASI with known science. What *can* be written are LA-602-type arguments for systems **below** a capability threshold — which is an argument for capability-scoped authorization, not for an ASI certificate. Whether a 10⁻⁶ argument for ASI is possible in principle is open; that none exists now is not.

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

## Open items

1. Read LA-602 primary: verify the 1.6 quote, "distinct/distant", the safety factor at bomb-relevant temperatures, the full list of channels and loss mechanisms, the ocean/water section, and the abstract. Then add to the paper collection.
2. Get Buck (1959) and Bethe's 1976 *Bulletin* letter; check *Atomic Quest* (1956) for any number. Settle threshold vs estimate (3 × 10⁻⁶ vs 3.3 × 10⁻⁷).
3. Read AC 25.1309-1B and RG 1.174 on the page to upgrade the two callouts from secondary.
4. Prior art on the framing: Tegmark's "Compton constant" (arXiv 2504.18530; don't cite the paper for a number); Yudkowsky-era *LA-602 vs. RHIC Review* (LessWrong) on argument form; Stojan, HackerNoon, 16 Oct 2026 (promotional, no numbers).

## Sources

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
