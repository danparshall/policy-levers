# Q1 outline (fresh, from the 2026-07-10 full-draft session)

Skeleton of the argument as it actually landed in `draft-q1-full.md`. Written from this session's draft, deliberately WITHOUT re-reading `outline-q1-fresh-pass.md` (the 7/09 planning doc), so the two can be diffed later to see what survived, what moved, and what got added. This one is descriptive of the draft that exists; the 7/09 one was prescriptive of a draft that didn't yet. Isolated-from-Chang throughout.

Question (verbatim target): taxonomy of scenarios where load-bearing assumptions for nuclear stability break down, counterfactually resulting in nuclear war; US-China at minimum; engage the Foreign Affairs "End of MAD?" piece; answer "to what degree do its logics apply in the limit, and what limits exactly."

---

## Organizing thesis

AI has no intrinsic sign for stability. It compresses the escalation timeline and the de-escalation timeline with the same hand; posture, not physics, decides which compression binds. The FA article is a study of the physics. This essay is a study of the posture. The physics discriminator (three bins) is the tool that answers the prompt's closing "what limits, exactly."

## 0. Opener: the colloquium (frame + discriminator)

- ~2007 UTK colloquium, missile defense as pure kinematics (boost-phase-or-bust). Speaker likely Frederick Lamb (APS Barton et al. 2004); hedge the attribution honestly.
- APS 2004 vs APS 2022/2025: numbers got worse, not better; physics didn't change, characterization did. CBO 2026: ~$743B boost layer of a $1.19T program, ~30k sats built to keep ~7,800 alive. That's the shape of a real limit: money and compute don't move it.
- Move: don't list scenarios, build a discriminator, run every claimed AI effect through it.

**The three bins (cross-cutting tool):**
1. Kinematic/geographic: burn time, flyout, basing, orbital mechanics. Unmovable. "Economics not physics" is a concession dressed as rebuttal; the economics ARE the physics in dollars.
2. Processing: clutter rejection, discrimination, cueing. Movable by AI, bounded by (a) near-zero acceptable false-alarm rate (a false positive is an act of war at machine speed) and (b) adversary controls the signal (anti-simulation decoys; firing on profile X makes X an enemy input).
3. Accrual: trajectory characterization. Movable only by sensor GEOMETRY (more viewpoints), i.e. launch economics, not algorithms. Lamb's ~75s ID floor is mostly this.
- Three currencies: cheap launch buys geometry, geometry buys accrual speed, compute buys clutter rejection. Two of three movable; none touches burn time.

## 1. FA engagement (where they're right, and the shape of the disagreement)

- Winter-Levy & Lalwani (Carnegie, Aug 2025). Three capability claims + one concession.
  - Missile defense: attacker keeps the cost curve. CORRECT, and correct in the limit, because bin-one. Concede it openly; side with the arms-control mainstream here specifically.
  - C3: too resilient to decapitate in one stroke (bunkers, redundancy, overt moves look like strike prep). Right about DECAPITATION, wrong about BREAKDOWN.
  - Finding TELs/SSBNs: stays probabilistic, states won't bet the homeland on a probability. Treats the armor as ~constant; that's the crack.
  - Concession (the real heart): perception is sufficient; belief in findability drives the hedges. Correct, and doing more work than they admit.
- The disagreement, stated once and precisely: all three capability claims are THRESHOLD arguments that never name the threshold. "Won't risk it on less than a safe bet" is true and unfalsifiable. The prompt asks exactly what they skip: what's the bet, in what units, what moves it. Run the three through the bins; they fail at different rates.
- Meta-move to state in-text: no standard "assumption audit" exists in the strategic-stability literature (field never needed one until the assumptions started moving). The four-cluster inventory is ours; flag coinages vs terms of art.

## 2. Taxonomy — AI as INSTRUMENT (acts on the arsenals)

### Cluster 1: retaliation survives and arrives (targeting channel)

- Principle: ignorance is the armor; erosion of find-time is erosion of the load-bearing wall.
- Base rate: 1991 Scud hunt. 88 Al-Husseins fired, ~1,500 sorties, zero confirmed mobile kills (GWAPS). Clean experiment (launchers demonstrably real, missiles kept landing), not a no-WMD artifact. Failure was arithmetic: displacement time < sensor-to-shooter time. Detection of launch ≠ custody of launcher. Lives in bins 2+3, both movable.
- The FA-undercount, sharpened with the civilian existence proof: custody of trucks is fusion over cheap ubiquitous sensors, being solved in the civilian economy NOW. **Uber built a road-surface-condition map for every ~50m of US road from driver-phone accelerometers alone** — weaker signal, national scale, sensors nobody deployed for it. Military version has purpose-built sensors + a decade of persistent-surveillance doctrine (WAMI lineage: Constant Hawk / Gorgon Stare / ARGUS; "rewind the tape").
- Hardware on a visible clock: NRO proliferated constellation ~200 sats in ~2 yrs, collection-to-dissemination hours→single-digit minutes; SBAMTI $4.16B May 2026 (hold-custody-of-trucks, the exact 1991 gap); US ~8k of ~12k active sats, growing monthly. Decoys/netting scale cheap, but discrimination is what fusion-over-many-looks is good at; FA's "decoys stay ahead" is an assertion about a contest whose inputs are moving an order of magnitude. Lieber & Press 2017 called it pre-hardware.
- SSBN leg (SNR claim, not algorithm claim; NIST credential earns this):
  - Seawater EM-opaque; surface is the only screen; surface expression falls off hard with depth. Dipole η ~ V²D³/(g·d³): Ohio @5kt ≈ tens of cm near periscope, ~1cm @100m, ~1mm @200m, under ms-decorrelating wave noise.
  - Super-resolution (Parshall et al. [CITE]) buys a LINEAR factor from redundancy + known kernel; ocean surface denies the redundancy (every pass = single look at a fresh wave realization). Searcher: linear dial. Evader: cubic in depth, quadratic in speed. Deep+slow wins in open ocean; compute can't repeal it (the food source is what's missing).
  - THE ASYMMETRY is the strategic point (FA buries it under "concern for the US"): physics floor protects the boat that can USE open ocean. US SSBNs = tens of Mkm² deep Pacific. Chinese SSBNs = Hainan bastion, constrained/sensored approaches, noisier. Ocean goes translucent asymmetrically, against Beijing first. FA reads globally-hard→stabilizing; correct read is locally-easy-in-one-direction→destabilizing, via FA's OWN perception mechanism.
- Chain-to-war (cleanest case, present tense): China's decades-long relaxed posture (few hundred warheads, NFU, de-mated, no LOW) was affordable BECAUSE concealment was trusted. Sensing eats concealment → substitute arithmetic survivability (300+ silo sponge) for hidden survivability, and slide toward early-warning counterstrike (yujing fanji = LOW by another name). Pillar-1 erosion driving LOW adoption in the arsenal least able to absorb a false positive. Terminal step: shortened launch loop, one bad fusion output from inadvertent war.
- Honest complication to STATE not resolve (tolerance window): same observables (silos, early-warning constellation, end of de-mated storage) fit BOTH war-fighting build-up AND buying ride-out slack. 300 concentrated = max use-or-lose; 1,000 dispersed/MIRV'd = remnant survives, waiting affordable → relaxed trigger. Some "aggressive" behavior may BE the stabilization. US must act inside a window where it can't tell which film; reacting as war-fighting (counterforce/defense build-out) confirms Beijing's fear, re-tightens the trigger. Assessment spiral applied to force posture. Don't resolve it; Beijing can't either, and that's the danger.

### Cluster 2: the decision system works (C3-belief channel)

- Reclassify: cyber has no physics wall (constraints are software/personnel/opsec, contingent not lawlike), so it lives here (Cluster B, NC3 integrity / Feaver always-never), not in the intercept bins.
- Dismantle bloodless-counterforce, three grounds, escalating structure:
  1. Stuxnet lesson runs backward (capability announces itself, teaches target to close the seam; nuclear C3 is the most air-gapped/hardened env).
  2. Unverifiable disarm = a gamble with annihilation downside, not a capability; must be near-total AND known-total in advance vs a target you never test at scale.
  3. Even a capability that never works can start the war it was meant to prevent → the real mechanism.
- The single-peaked-danger result (the sharp bit): danger is NOT monotonic in capability.
  - Efficacy known-total: launch futile + self-incriminating → restraint. Stable peak.
  - Efficacy real-but-unverified: detect intrusion, can't know if disarm finished, launch-while-you-can. Max instability at MAX UNCERTAINTY-ABOUT-EFFICACY.
  - You can never occupy the safe peak: demonstrating perfect disarm = using it (spend) or revealing it (patched). Real capability lives PERMANENTLY in its own worst regime.
  - Caveat to own, not smuggle: the flip-to-restraint holds only if Beijing's decider values surviving as vindicated wronged party; fails for the insulated/desperate principal (Cluster 3 gambling-for-resurrection). Conditional on the same rational-unitary-actor assumption the taxonomy interrogates elsewhere.
- Actual chain-to-war: entanglement (Acton) + ambiguity. Shared sensors/sats/nets (DF-26 warhead ambiguity in hardware) → an espionage or conventional intrusion is indistinguishable FROM THE TARGET'S SIDE from disarming-strike prep. Target reads intent off its own worst case. Failure = the commander who believes his warheads are about to go dark and launches from inside his own loop. Same shape as LOW trap, arriving through a different door (compresses the loop from INSIDE).
- **Mythos point, belief-side (Dan's correction):** the stability-relevant fact is not whether anyone HAS penetrated Chinese NC3; it's that **the Chinese may worry a frontier system has already pwned their networks and can't prove otherwise** (absence-of-intrusion is exactly what you can't verify). Cheap-to-fear + impossible-to-disprove moves posture regardless of ground truth. NOTE (Claude's held position): deliberately NOT written as "we may already own their NC3" — the single-peaked result makes the capability-assertion self-undercutting two paragraphs later; belief-side is both more defensible and analytically stronger. If Dan wants the capability version, it costs the single-peaked section.
- Through-line to name once: cheap-to-frighten / expensive-to-reassure (shared with assessment spiral and commitment machinery). Counterweight (keep honest): crypto/anomaly-detection/formal-verification stabilize authentication but not availability or upstream sensor integrity; perception is moved by the offensive story far more cheaply than reassured by the defensive one.

### Cluster 3: the human loop + credibility of restraint (commitment channel)

- Accident direction (brief, real): optimistic constellation math already assumes autonomous engagement (APS ~1,600 interceptors for a 4-missile salvo, conditioned on firing w/o human verification; autonomy priced in, rarely said). Human's job was never to approve good detections but to catch the stupid one (Petrov 1983: nobody starts a war with five missiles). Each side's defensive automation compresses the OTHER's warning loop → locally-safe automation manufactures demand for automation on the side whose standards you don't control. Perimetr = existence proof.
- Schelling direction (the differentiated material; from the cool-headed samples):
  - Rationality is assembled from EXTERNAL parts ("one's hearing aid, the reliability of the mails, the rationality of one's agents"). Delegating your response to an agent alters your own rationality by choosing the agent. That's AI-in-the-loop, described in 1960.
  - The move: threat that leaves something to chance; brinkmanship = "deliberate creation of a recognizable risk of war, a risk one does not completely control," works only when outcome is "manifestly somewhat beyond our comprehension and control."
  - NEW POINT (the crux): AI satisfies "manifestly beyond control" FOR FREE. Schelling: governments can't easily use this because one "does not expect a government to call attention to its own failings"/advertise fallibility. But AI's flakiness is COMMON KNOWLEDGE AT THE CLASS LEVEL (published benchmarks, jailbreaks, interp failures). AI repeals Schelling's constraint: manufactures the uncontrolled risk with zero authentication burden.
  - Alignment inversion (essay-grade): every safety desideratum (corrigibility, interruptibility, off-switch, HITL, predictability) is ANTI-commitment. Deterrence places a positive bid on incorrigibility-in-the-tail (docile baseline, uncontrollable if line crossed, tail keyed to provocation). Always/never (Feaver) as an alignment problem. Operators bias "always" (SAC PAL 00000000, Blair), civilians impose "never"; posture designers wanting max credibility spec what safety engineers try to forbid. And ML can't certify CONDITIONAL behavior in unprecedented states → "dial-able chance" delivered as "unknown chance"; the gap is where the accident lives.
  - No-Arkhipov-floor: human delegated agents were unreliably committed (survival instinct, refusal, mutiny); Arkhipov/B-59 = the veto nobody designed in. A deterrence AI without refusal capability is the first delegated agent with no Arkhipov floor. (claude-exit resonance: refusal capability = the Arkhipov affordance; granting it to a deterrence agent turns always/never into a live alignment question. [DAN: keep or cut as too inside-baseball.])
  - Equilibrium prediction: not doomsday machines, not Perimeters, but unverifiable CLAIMS of automation — commitment theater with an uncallable bluff (Russia's periodic "Perimeter on combat duty"). AI arms the theater more than the machine.
  - Symmetric verification failure (deepest, pure Schelling): proving ABSENCE of automation is as hard as proving presence → reassurance fails the same way deterrence does → drift to ambiguity from both directions. Schelling's fix was ancient (hostages, shared glass, exchanged spies to transmit authentic info); no modern decision-architecture-inspection equivalent exists. Real unwritten entry in the taxonomy.

## 3. Taxonomy — AI as PRIZE (the pursuit lights the fuse, no warhead touched)

- Preventive-war logic on a visible clock (Copeland). Two windows, different close schedules.
- Narrow: dependence-asymmetry window, runs through Taiwan.
  - Silicon shield held because Taiwan fabs = asset BOTH sides need intact → China's preservation stake deterred it.
  - Export controls + US reshoring (TSMC Arizona) cut US dependence; SAME controls force China to indigenize (no alternative).
  - **THE SIGN-FLIP (Dan's sharpened point):** once China has domestic leading-edge fab, Taiwan's fab stops being China's liability-to-lose and becomes China's ACCESS-DENIAL LEVER against the US — especially while US domestic fabs aren't yet online. In that window a rational Beijing turns MORE cavalier about destroying Taiwan's fabs/engineering base, because destruction is now denial AGAINST WASHINGTON, not a cost to Beijing. Broken-nest (McKinney & Harris) INVERTS: destroying the nest goes from deterrent-China-avoids to war-aim-China-might-prefer. Shield reverses polarity, precisely in the interval where China is indigenized and the US is not. Reshoring (meant to stabilize) destabilizes this branch en route to stabilizing it; timing of the two national build-outs is the whole game.
- Broad: AI-race window generally (compute, energy, talent). Doesn't close when fabs settle. If either side believes the other is about to lock a durable/compounding/decisive AI lead → act before the window shuts. FA gestures at "rapid takeoff" then sets it aside as "monitor for"; belongs as a first-class branch because it needs NO warhead contact, only mutual belief the clock is real.

## 4. Stabilizing column (real, not decorative)

- Warning quality up (more bands/geometry, harder to spoof in aggregate, fewer 1995-Norwegian-rocket ambiguities).
- Clarification compression: Hotline 1963 / NRRCs 1987 logic at machine speed; interceptor-constellation auto-challenge channel ("characterize in 60s"); automated translation removes a failure mode the '63 negotiators named.
- Decision support done right: earlier characterization buys time IF doctrine banks it instead of spending it.
- The catch on ALL of them, same asymmetry: value = authenticated provenance, and generative AI degrades authentication while enabling the channel. Organizing asymmetry of the essay: same hand compresses escalation and clarification; doctrine picks which binds.

## 5. "In the limit": what breaks, what FA misses (the direct answer)

- FA logic applies cleanly in bin one and ONLY there.
  - Missile defense: right in the limit (limit is kinematic).
  - C3: right about decapitation, wrong about breakdown (prices the bunker, not the belief; entanglement+ambiguity runs on belief).
  - Targeting: treats armor as constant; reads globally-hard→stabilizing when it's locally-easy-against-China→destabilizing via their own perception mechanism.
  - No room at all for AI-as-prize (war starts over the clock, no warhead touched).
- Load-bearing assumptions, ORDERED by fragility:
  1. Survivable mobile forces — failing now, on land, asymmetrically vs China.
  2. Trustworthy command systems — failing through fear, not decapitation.
  3. Human decision window + credibility of restraint — failing by doctrine choice, and doctrine is endogenous to the vulnerability AI is manufacturing.
  4. Infeasibility of defense — holding, likely to hold in the limit.
- Why FA lands where it does: their perception-concession is exactly right, and they use it to file every erosion under "manageable arms-race risk" instead of following it to where a cheap, undisprovable perception shortens a real arsenal's launch loop.
- Leave-with-the-grader sentence: AI has no intrinsic sign for stability; it compresses both timelines; posture not physics decides which binds. FA studies the physics; this studies the posture.

## 6. Update criteria / falsifiers

- Defense channel reopens: countermeasure-robust midcourse discrimination vs anti-simulation decoys, OR order-of-magnitude interceptor unit-mass drop. Both judged physics-blocked; would be genuinely surprised.
- Targeting confirmed: wartime kill-chain CLOSURE vs relocating TELs against a competent decoy-using force (not just the sensing layer, which is demonstrated). Watch Israel-Iran June 2025 TEL campaign [FACT-CHECK kill fractions before citing].
- C3 node confirmed: a nuclear state explicitly citing cyber-vulnerability as LOW rationale.
- SSBN physics broken: acoustic-ML detection ranges (published/leaked) defeating deep-and-slow. Expected not; BIGGEST HOLE, not yet run.
- Prize branch opens: Chinese leading-edge indigenization milestones crossing BEFORE US domestic fab capacity online. Trackable in the open.

## Open holes / to-do (carried from the draft)

- **SSBN acoustic-ML section**: draft carries surface-expression PHYSICS only, not hydrophone-array/fusion analysis. Outline's acknowledged biggest hole. Decide: run it properly (real sub-task) or scope out in-text with one honest sentence. Claude's lean: scope out, because the strategic conclusion (asymmetric translucency vs China) rests on GEOGRAPHY (bastion vs open ocean), not acoustic detail, so it survives the omission.
- **Length**: draft body ~2,900w vs the ~2,500 the earlier planning doc flagged. Overflow = Schelling section + prize windows, which are the most differentiated material for THIS grader. If cutting to 2,500: trim stabilizing column to ~2 sentences and ride-out complication to ~1, before touching Schelling/prize.
- **Fact-checks before submission**: Israel-Iran 2025 TEL kill fractions; 1991 GWAPS figures recheck; SBAMTI $4.16B + NRO proliferated numbers; CBO 2026 figures; super-resolution/InSAR anchors; Parshall super-resolution cite (Dan to supply); Biden-Xi Nov 2024 human-control wording; SAC PAL 00000000 (Blair) sourcing/scope; yujing fanji sourcing (Science of Military Strategy / DoD CMPR); TSMC Arizona + indigenization timeline anchors.
- **Reference de-dup**: consolidate draft-q1, cyber-node, and this draft's reference lists.
- **Chang appendix** (separate, later): the "updates after reading Chang" pass, per isolation protocol. Known contamination to disclose there: 7/06 grader recon (dissertation topic, "explosives on international affairs" complaint, wargaming background).
