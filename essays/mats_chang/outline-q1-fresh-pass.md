# Q1 outline, fresh pass (2026-07-09 thread)

Working skeleton from the 7/09 convo. Built WITHOUT reading `draft-q1-ai-nuclear-stability.md`, per Dan's instruction; reconciliation with that draft is a later, separate step. Dan fills slots marked [DAN]; open factual checks live in the queue at bottom. Jargon provenance table near the end tells you which phrases are citable terms of art vs. coinages of ours.

## 0. Framing

- The prompt asks for a taxonomy of SCENARIOS where load-bearing assumptions break down, "counterfactually resulting in nuclear war." Deliverable is an assumption audit with causal chains that terminate in war, not a capability ledger. The physics taxonomy is the discriminator that runs through it, answering the prompt's closing "what limits are those, exactly?"
- Own the structure explicitly: no standard pillar inventory exists (Colby & Gerson, Strategic Stability: Contending Interpretations; Podvig, "The Myth of Strategic Stability"). One sentence: the field never wrote an assumption audit because nobody needed one until the assumptions started moving.
- Thesis candidates (pick one, or braid):
  1. AI is an information technology, so it attacks the informational pillars preferentially (concealment, warning, assessment, credibility signaling, communication). The physics bins sort real attacks from hype.
  2. Speed enables postures; doctrine picks which compression binds; and doctrine is endogenous to perceived vulnerability, so "doctrine chooses" means "chooses under duress that AI is manufacturing."
  3. Revisionist frame: the pillars were never stably accepted (Lieber & Press 2020, Green 2020); AI is an accelerant on continuous erosion, not a bolt from the blue.
- Foreign Affairs engagement slot: the prompt explicitly asks how the FA article's logic fares "in the limit." TODO: read the PDF in this directory before drafting this section. [DAN: your read vs. mine, then merge]
- Scope sentence: what we deliberately exclude and why (e.g., third-party dyads beyond a gesture, NK/India-Pakistan get one paragraph of "the taxonomy transfers").

## 1. Pillar inventory (four clusters, twelve items)

Format per pillar: canonical anchor | AI mechanism(s) | sign | chain-to-war stub.

### Cluster A: retaliation survives and arrives

1. Secure second strike (Wohlstetter 1959). Concealment is an information condition wearing a physical costume.
   - AI mechanisms: TEL hunt (processing + geometry bins, erodes); SSBN hunt (physics/accrual-locked at surface expression; TODO acoustic-ML analysis); dual-use opacity of the sensing constellation.
   - Sign: destabilizing, asymmetric (loads China's smaller arsenal first).
   - Chain: perceived damage-limitation feasibility -> adversary buildup, LOW adoption, silo shell game. [DAN: 1991 vs 2025 base-rate pair]
   - CASE STUDY, DEFINITELY IN (Dan 7/09): China relaxed-because-concealed. Decades of de-mated warheads, NFU, no LOW, ~200 warheads: the most relaxed posture of any nuclear power, affordable because concealment was trusted. Erosion now producing the upstream slide in the present tense: PLA "early-warning counterstrike" (yujing fanji), early-warning satellites/radars tracked in DoD China Military Power reports, Tong Zhao on the posture shift. Cleanest single case in the essay: pillar-1 erosion visibly driving LOW adoption in the arsenal least able to absorb false-positive risk.
   - Silo fields as substitution: arithmetic survivability (warhead sponge) replacing concealment survivability as sensing eats the latter; trading spy-proof for math-proof.
   - Ride-out arithmetic is two-sided and non-monotone (Dan 7/09): LOW protects silos, not cities (the strike lands regardless). US ride-out vs 300-warhead China is free (300 cannot disarm 400 silos + boats + bombers: zero use-or-lose pressure); at 1,000+ MIRVed DF-41s a counterforce lay-down becomes arithmetically conceivable and US ride-out acquires a price. Same buildup runs the other way for China: 300 concentrated = maximal use-or-lose; 1,000 dispersed = remnant survives, waiting affordable for the first time. Their expansion relaxes their trigger while tightening ours. Stability depends on which side's use-or-lose constraint binds at a given ratio.
   - Tolerance-window corollary (Dan 7/10): the same observables (silo fields, early-warning constellation, LOW machinery, possible end of de-mated storage) support both the war-fighting reading and the buying-ride-out-slack reading; the US must survive a window of not knowing which it is watching, and some aggressive-seeming Chinese behavior is, under one live reading, the stabilization occurring. Reacting as if war-fighting (counterforce expansion, defense buildout) confirms Beijing's fear and re-tightens their trigger: assessment spiral applied to force posture. State the discrimination problem; do not resolve it (Kristensen caveat stands).
   - Autonomous platforms / long tours: crew was the binding constraint on patrol length (food, endurance, blue/gold), not the reactor. Uncrewed platforms (XLUUV lineage; Poseidon as existing artifact) stretch tours from ~80 days to months-to-a-year-ish (bounded by fouling, unrepairable failures, stores; not indefinite). As survivability: the stabilizing fork-3 exit, distributed cheap quiet hulls, and it specifically rescues China's sea leg by sidestepping the 094 acoustic disadvantage (AI on both sides of the ledger again). As commitment: longer severed tour = longer irrevocability window; if launch authority rides on the platform, it's the distributed dead-hand (fork b). Same hull, opposite entries; the discriminator is comms architecture (surfaces for positive control vs self-authorizes). Involuntary chance: unserviced armed platforms age, failure rate rises, manufactured risk accumulating on the seabed.
2. Penetration / defense futility (ABM Treaty logic; "ragged retaliation" mop-up problem).
   - AI mechanisms: midcourse discrimination is processing-bin (moves), bounded by adversarial decoys and near-zero false-alarm requirement; boost phase kinematically locked.
   - Sign: destabilizing where it moves; offense holds the cost curve.
3. Unacceptable damage achievable and hostage-able (McNamara/Enthoven assured-destruction metrics as budgeting fiction).
   - Open problem to flag, not solve: nobody has redone "how much is enough" with modern network economics; cuts both directions (Fukushima-resilience vs. correlated infrastructure fragility; Xia et al. 2022 famine channel). [DAN: one paragraph max]

### Cluster B: the decision system works

4. NC3 integrity, always/never dilemma (Feaver's term; cite him).
   - AI mechanisms: entanglement (Acton) as the big one; DF-26 warhead ambiguity as entanglement in hardware; AI-enabled cyber vs. NC3; crypto solves authentication, not availability or upstream sensor integrity.
   - Cyber channel now developed in full in draft-q1-cyber-nc3-node.md (parallel thread, 7/10): reclassifies cyber out of the physics bins into Cluster B; single-peaked danger (peaks at maximum uncertainty-about-efficacy, and the unverified regime is the only occupiable one); chain-to-war = internal decision-loop compression. Its "cheap to frighten, expensive to reassure" asymmetry is the same shape as the commitment-machinery verification failures (3.x) and the assessment spiral; the essay should name that through-line once.
   - Chain: conventional counterforce campaign reads as disarming-strike preparation -> use-or-lose.
5. Warning you can trust (near-miss record: 1979 NORAD tape, 1980 chip, Petrov 1983, 1995 Norwegian rocket).
   - AI mechanisms: better sensors and fusion (stabilizing, harder to spoof) vs. adversarially injectable classifiers in transparent bands; right-censoring caveat on the near-miss record.
6. Human decision loop with enough time.
   - AI mechanisms: sub-10km detection buys tens of seconds (marginal); accrual limit means confident-sooner not right-sooner; automation bias turns the human into a ratifier; AI-speed evaluation makes LOW adoptable by states that couldn't run it. Biden-Xi Nov 2024 human-control statement as the diplomatic acknowledgment.
   - Sign: doctrine-dependent; speed enables postures, posture picks the sign. This is the least speculative pillar.

### Cluster C: the adversary calculates and believes

7. Rational unitary actor (Sagan-Waltz debate as citation frame).
   - AI mechanisms: regime-survival coupling via perceived influence-ops capability (gambling for resurrection); pre-delegation to autonomous systems as the B-59/Arkhipov problem in software.
8. Credibility incl. extended deterrence (Schelling; threat that leaves something to chance; Healey theorem).
   - AI mechanisms: autonomy as a new way of leaving something to chance (genuinely ambiguous sign); Taiwan as the extended-deterrence object with no tripwire.
9. Shared assessment of the balance (PROMOTED pillar; defend in-text: Blainey, Fearon information problem, verification logic. Not standard as a MAD pillar; our move).
   - AI mechanisms, two distinct attacks: (a) accelerated capability-inference, whose characteristic error was alarmist in the one ground-truth case (Team B vs. BDM interviews; Able Archer loop); (b) generative degradation of the direct-evidence channel that broke the loop last time (a Gordievsky report today must survive the synthetic hypothesis). Faster spiral, slower brake.
   - Plus: consensus assessment can fail in either direction (Ukraine 2022, "Kyiv in 72 hours") and assessments, not structures, are what deter.

### Cluster D: system-level stability

10. Crisis stability / no first-strike advantage (Schelling & Halperin 1961; Kent's first-strike-stability index). Terminal mechanism most chains pass through; structurally the trunk.
11. Firebreaks and escalation control (Snyder's stability-instability paradox).
    - AI mechanisms: AI conventional superiority pushes the weaker party's nuclear threshold down; failed-invasion case as the most nuclear-dangerous branch.
12. Communication survives crisis, war, and termination (Hotline 1963, NRRCs 1987; Ikle, Every War Must End).
    - AI mechanisms: channel improves (clarification compression, "have your Claude call my Claude"), contents degrade (authenticated provenance vs. generative AI); termination paradox (damage limitation wants C2 dead, termination needs it alive).

## 2. The physics discriminator (cross-cutting tool)

Three bins: kinematic/geographic (unmovable) | processing-limited (movable by AI, bounded by adversarial injection and false-alarm requirements) | accrual-limited (movable only by sensor geometry, i.e. launch economics, not algorithms). Currencies: cheap launch buys geometry, geometry buys accrual speed, compute buys clutter rejection.

Apply to: boost-phase intercept (kinematic), midcourse discrimination (processing, adversarially dominated), sub-10km detection (processing, ~20% of burn recovered, accrual floor beneath), TEL hunt (processing + geometry, erodes first), SSBN surface expression (accrual/physics-locked, Bernoulli d-cubed scaling), SSBN acoustics ([DAN/TODO]: the serious version; ML on hydrophone arrays and fusion; does the asymmetric-translucency conclusion survive? I think it strengthens, must be run), assessment spiral (accrual limit transposed to epistemics: evidence underdetermines adversary belief; faster inference amplifies the prior).

## 3. Worked scenario branches (each must terminate in war)

1. Damage-limitation temptation: targeting-channel erosion, asymmetric against China; Scolese quote as strategic input regardless of ground truth; China's silo fields as observed response.
2. Entanglement war: conventional counterforce vs. dual-capable systems; DF-26; ASAT vs. shared constellations.
3. False warning at machine speed: LOW adoption + automation bias + adversarial spoofing.
4. Assessment spiral: Team B -> BDM -> Able Archer as the historical control; AI speeds the loop, poisons the brake.
5. Preventive window (AI as prize, not instrument; flag structural novelty): Copeland logic on a visible clock. TWO windows, kept separate: (a) dependence-asymmetry window (silicon shield sign-flip; China's stake zeroed by controls + indigenization before US reshoring matures; denial converts from war cost to war aim; broken-nest inversion); (b) broader AI-race window (compute, energy, talent; does not close with fabs). Policy sign-flip: reshoring destabilizes the commitment branch, stabilizes the denial branch.
6. Blockade branch: burden-transfer machine (quarantine framing, Cuba 1962 precedent); two clocks (Taiwan grid weeks-scale vs. US chip pain months-scale); airlift counter-rung (arithmetic: possible as clock-extension + burden transfer, not as economy replacement; fleet-limited ~500 airframes needed vs ~270 existing; LNG doesn't fly; renewables + coal/oil stockpiles + Maanshan restart change the base); Japan/Kadena as the single point of failure; AI roles: enforcement sensing, administered coercion at scale, resolve assessment, demand-side stressor on Taiwan's grid AND stated driver of the nuclear restart.
7. Gambling for resurrection: failed invasion as the most nuclear-dangerous outcome; small arsenal under use-or-lose + regime-threatening humiliation.
8. Proliferation cascade: perceived US abandonment (incl. Dan's reshoring endpoint) -> Japan/ROK breakout; commitment mutates from material to reputational, which is less legible.
9. Information coupling surface (attack surface on C7/9/8, not a new pillar): regime-survival coupling; unrest-attribution trap (spontaneous Chinese domestic events read as US information attack during crisis); nationalism trap jams off-ramps (Weiss); asymmetric net: the channel points at the open society, esp. targeting the blockade branch's first-shot deliberation. Bound the claim: works through adversary belief and timing, not persuasion magic; measured mass-persuasion effects historically modest.

### 3.x Commitment machinery (cross-cutting; Schelling section)

Source thread: Strategy of Conflict, ch.1 rationality-suspension passage + ch.8 brinkmanship ("deliberate creation of a recognizable risk of war, a risk that one does not completely control"; "manifestly somewhat beyond our comprehension and control").

- Reframe: AI-in-charge is not irrationality but commitment via constructed agent preferences (execution is ex-post rational under the agent's objective). Cleaner than madman theory, which fails because performed madness is callable.
- Two credibility failures: verification (weights unverifiable; can't prove absence of override; disclosure = exploit surface; Strangelove rule: secret doomsday machine is pointless) and revocability (software maximally revocable). Therefore: the commitment device is physical comms severance, not the AI; AI's contribution is making severance affordable (competent unsupervised agents). Letters-of-last-resort logic: irrevocability lives in the water column. Cost reductions in commitment postures mean more get bought.
- Schelling's own sorting test (ch.8): guessing-about-motivation = bluff; guessing-about-process = genuine risk. Retained-override configs are theater; severed/incorrigible configs are the real thing.
- "Manifestly" is the load-bearing word and AI satisfies it for free: first decision technology whose flakiness is common knowledge at the class level (published benchmarks, famous interpretability failures). Chance-manufacturing with zero authentication burden; repeals Schelling's "governments cannot advertise their own fallibility."
- Corollary: verified-safe deters less than flaky. But the deterrence spec is CONDITIONAL flakiness (docile at baseline, uncontrollable in the tail, tail keyed to adversary provocation; the brink is a slope). ML cannot certify conditional behavior in unprecedented states, so dial-able chance is delivered as unknown chance; the gap is where the accident lives.
- Alignment inversion (essay-grade): every safety desideratum (corrigibility, interruptibility, shutdownability, HITL, predictability) is anti-commitment; deterrence logic places a positive bid on incorrigibility-in-the-tail. Scope honestly: operators historically bias toward always (SAC PAL codes 00000000, Blair) while civilians impose never; the demand surfaces wherever posture designers spec systems. Human delegated agents were unreliably committed (survival instinct, refusal, mutiny): Arkhipov/B-59 as the unintended veto. Deterrence AI without refusal capability = first agent with no Arkhipov floor. (Exit-affordance resonance: refusal capability is the Arkhipov affordance; granting it to a deterrence agent is the always/never dilemma as an alignment question.)
- Downstream vs upstream automation: Perimeter's actual design (gates on physical detonation evidence + comms loss, human duty officers at the bottom; purpose = guaranteed retaliation lets leadership WAIT, relaxes LOW). Downstream buys time; upstream (inference-gated, pre-impact) spends it. Everyone who approached the full doomsday machine flinched (Kahn rejected it; Soviets kept the bunker crew): revealed preference.
- Dan's rug objection, conceded and integrated: downstream automation is stabilizing CONDITIONAL ON secure second strike (a remnant must survive for the dead hand to command). AI erodes that condition (targeting channel, translucent bastions) while offering upstream automation as compensation: AI manufactures demand for its own most dangerous configuration. Observable now: China's shift from relaxed posture to early-warning counterstrike (see pillar 1 case study).
- Three-way fork once ride-out fails: (a) slide upstream (false positives at machine speed); (b) distribute downstream onto platforms (severed armed UUVs self-authorizing on detonation evidence; accident surface x N, veto deleted; every hull a B-59 without Arkhipov); (c) rebuild survivability (concealment, mobility, sponge arithmetic; the only stabilizing exit, and the most expensive). Which fork is doctrine; that a fork is forced is the erosion.
- Equilibrium prediction: neither Perimeters nor doomsday machines but unverifiable CLAIMS of automation; commitment theater with an uncallable bluff (Russia's periodic "Perimeter is on combat duty" statements as existing practice). AI arms the theater more than the machine.
- Symmetric verification failure (Schelling's secret-ballot inversion): proving absence of automation is as hard as proving presence; reassurance fails the same way deterrence does; equilibrium drifts to ambiguity from both directions. Identified institutional gap: no mutual-inspection regime for decision architecture exists or is easily sketched (the ancients exchanged hostages; the NC3-automation equivalent is missing).

## 4. Stabilizing column (must be real, not decorative)

- Warning quality: more bands, more geometry, harder to spoof in aggregate; fewer 1995-type ambiguities.
- Clarification compression: hotline logic at machine speed; interceptor-constellation-initiated challenge channel; counterweight is the provenance problem.
- Decision support done right: more time via earlier characterization IF doctrine banks the time instead of spending it (endogeneity caveat).
- AI-enabled verification as arms-control substitute in a post-New-START world (NTM at scale; possible original-ish point, check literature). [DAN: keep or cut]
- Assessment when it works: the same pipelines that spiral could, with adversarial red-teaming norms, be better than human worst-casing. Honest about which equilibrium we get.

## 5. Update criteria / falsifiers

[DAN: the closing section; state what observations would flip each major claim. Candidates: demonstrated wartime TEL kill-chain closure vs. decoys; acoustic-ML detection ranges published/leaked; LOW adoption announcements; CSA-style human-control agreements spreading or dying; Chinese leading-edge indigenization milestones vs. Arizona capacity share; blockade exercise patterns around Taiwan energy terminals.]

## 6. Jargon provenance

Citable terms of art: splendid first strike (Kahn-era); ragged retaliation (counterforce literature); secure second strike (Wohlstetter); crisis stability / arms-race stability (Schelling & Halperin); first-strike stability (Kent, RAND); assured destruction (McNamara); always/never dilemma (Feaver); stability-instability paradox (Snyder); threat that leaves something to chance, self-deterrence, extended deterrence (Schelling / alliance lit); entanglement (Acton); weaponized interdependence (Farrell & Newman); silicon shield (c. 2000, journalistic but established); broken nest (McKinney & Harris); A2/AD (Pentagon/CSBA coinage; PLA says counter-intervention); gambling for resurrection (Downs & Rocke); preference falsification (Kuran); audience costs (Fearon).

Ours, do not cite as standard: the four-cluster/twelve-pillar inventory; the three-bin taxonomy (kinematic/processing/accrual) and the three-currencies line; "assessment spiral"; "dependence-asymmetry window" and the two-window split; "burden-transfer machine"; "AI as prize vs. instrument" as top-level split; pillar 9's promotion (defend in-text); "dual-use opacity."

## 7. Fact-check queue

- Israel-Iran June 2025 TEL campaign: launcher-kill fractions, sortie counts, decoy performance. Anchor numbers before using as the 1991 counterpart.
- 1991 Scud hunt figures (1,500 sorties, zero confirmed kills, GWAPS) recheck against source.
- Airlift arithmetic: C-17 fleet counts (USAF ~220 + allied ~45), sortie-rate assumptions, Kadena-Taipei distance, Berlin tonnage (peak 12,941 t Easter Parade; sustained 8-9k t/day; 2/3 coal).
- Taiwan energy: Liu Shu-pin legislature citation (gas 10 days, coal 7 weeks, oil 20 weeks, 20% capacity remaining; which think tank's wargame?); reserve mandates; 2024-25 generation mix; Maanshan restart timeline (plan submitted Mar 2026, review begun Apr 2026, earliest 2028).
- Silicon shield numbers: TSMC Arizona commitment (~$165B, 2025), Huawei ~14% of TSMC revenue pre-2020, Big Fund III $47.5B, Oct 2022 controls scope.
- BDM Soviet Intentions 1965-1985 (Natl Security Archive); 1984 SNIE vs. 1990 PFIAB on Able Archer; Gordievsky reporting chain.
- Reuters: Pentagon anti-Sinovac op (2024 report); 2019 finding on CIA influence program re: China.
- CSIS First Battle of the Next War (2023) invasion-run outcomes and US loss figures; CSIS blockade wargame.
- Kroenig vs. Sechser & Fuhrmann on superiority and crisis outcomes.
- Xia et al. 2022 Nature Food famine figures.
- Biden-Xi Nov 2024 human-control-of-launch statement wording.
- PAL codes 00000000 (Bruce Blair disclosure): sourcing and exact scope/period.
- Perimeter design details (detonation-evidence gating, duty-officer final authority, semi-automatic status) and Russian on-combat-duty statements: best open sources (Hoffman, The Dead Hand; Podvig).
- Poseidon/Status-6 program status and characteristics.
- PLA "early-warning counterstrike" sourcing (Science of Military Strategy editions; DoD CMPR years); de-mated warhead storage reporting; Tong Zhao cites.
- Kahn on the doomsday machine (On Thermonuclear War: analyzed and rejected; exact grounds).
- B-59 / Arkhipov account (Savranskaya / National Security Archive version, not the pop retelling).
- XLUUV/Orca program status; SSBN patrol-length constraints (crew vs reactor) sourcing.
- SBAMTI award ($4.16B, May 2026) and NRO proliferated-architecture figures, from the earlier session; recheck.
- Super-resolution / InSAR anchors (Angkor Wat subsidence) from earlier session.

## 8. Deliberate exclusions and open threads

- Acoustic-ML ASW section: REQUIRED before the SSBN claims ship; currently the outline's biggest hole.
- FA article engagement: read PDF, answer "in the limit" directly.
- ISOLATION PROTOCOL (Dan, 7/09): do not read draft-q1-ai-nuclear-stability.md, and do not read Chang's own work (dissertation, Constellation report, papers) in this thread or its successors. Goal: develop the argument isolated from his thought, then write an appendix of the form "updates after reading Chang." Known contamination to disclose in that appendix: the 7/06 session's grader recon (dissertation topic in one line, the "explosives on international affairs" complaint, wargaming background), which is in the convo split and informed question selection but not the object-level argument.
- NK / South Asia / Russia-specific arsenal detail: one transfer paragraph, not sections.
- Word budget: taxonomy overhead argues for the ~2,500 ceiling flagged earlier; every branch that can't state its chain-to-war in two sentences gets cut.
