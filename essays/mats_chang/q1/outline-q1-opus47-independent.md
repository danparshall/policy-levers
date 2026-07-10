# Q1 Outline — Opus 4.7 independent pass

Written 2026-07-10 before the FA article was read in full and independent of Fable's prior drafts and Chang lookups. Purpose: fix the argument structure so the draft has something to hang on, name the load-bearing claims and where they get pressure-tested, and mark spots where Schelling-style commitment-machinery language should land.

## Thesis

Nuclear stability's load-bearing assumptions are physics-locked at the capability level and epistemic-and-doctrinal everywhere else. The FA analysis is correct about the physics-locked layer and inverts the weighting on everything above it. A taxonomy of AI-driven breakdown scenarios has four channels, not three: targeting-channel erosion (partial and asymmetric, favoring the US against China first), decision-channel compression (Schelling's imperfect decision system meets an AI-accelerated military-operational preference for commitment devices over civilian control), NC3-belief-channel (perceived vulnerability drives doctrine even absent confirmed capability, Acton entanglement with an AI accelerant), and prize-channel (AI as strategic stake changes the payoff matrix on Taiwan, closing fab windows create action-forcing pressures, load-bearing "great powers avoid direct conflict" assumption gets stressed). The FA article is a good analysis of the pre-takeoff regime; the operative constraint in Chang's question is "assume AI progress continues," which is where the FA hedge on sudden takeoff fires and their meta-model breaks.

## Section 1: Framing (~200 words)

- Chang's question stated and the "assume AI progress continues" clause named as the operative constraint that shapes what we're asked to survey
- Approach: taxonomy first (Chang asked for one), FA as comparison anchor second, sudden-takeoff regime last as the case where the taxonomy itself becomes brittle
- Concession up front so it doesn't have to be re-negotiated later: FA's physics-locked observations are correct at the capability layer; the argument is about weighting between capability and perception, not about the underlying physics

## Section 2: The taxonomy (~1500 words)

### 2a. Targeting-channel erosion

- Three-bin decomposition from prior work: kinematic/geographic limits (unmovable), processing limits (movable by AI, bounded by adversarial spoofing and near-zero acceptable false-alarm rate), accrual limits (movable only by adding sensor geometry, bought with launch economics)
- TEL: 1991 Scud hunt as the clean base rate (1,500 sorties, zero confirmed mobile kills against real launchers in open desert against a mediocre adversary). Erosion mechanism: Falcon 9 launch economics buy revisit rate, revisit rate buys custody, SBAMTI/SBGMTI ($4.16B May 2026 award) buys moving-target indication from orbit, MacDonald (vt)² gap-scaling arithmetic shows launcher survivability shrinking as inter-satellite gaps close. NRO director's "harder to hide" quote as strategic input regardless of ground truth
- SSBN: Bernoulli hump d³ scaling is the physics-lock and it is asymmetric. Shallow-noisy patrols erode; deep-quiet patrols do not. US Ohios in open ocean tens of millions of km² of stratification-messy deep water: unlayerable. China 094s in Hainan bastion with constrained approaches and chokepoints: layerable. Erosion is lopsided toward China's deterrent first, which is the destabilizing direction from Beijing's chair and feeds the silo-sponge buildup
- Signal-extraction ceiling is not where FA places it. Uber road-quality map from millions of phone accelerometers is the cross-domain rhyme: sensor fusion plus ML extracts signals that look physics-forbidden at any single measurement. The FA "manipulate sensor data" and "inject false information" countermeasures are real but the operating point on the ROC still moves, and the acceptable false-alarm rate for autonomous intercept is near-zero against a heavy-tailed adversarially-injectable clutter distribution, so where the OP sits matters more than whether the classifier is perfect
- Where this leaves us: partial erosion, asymmetric direction, driving the weaker deterrent toward destabilizing responses (more warheads, LOW, pre-delegation, ASAT), and none of this requires the strong claim FA correctly rebuts ("splendid strike now feasible")

### 2b. Decision-channel compression

- Schelling frame first: threat that leaves something to chance is a stability resource; imperfect decision system is a feature, not a defect; military operational preferences (pre-delegation, pre-scripted response, LOW/LUA, dead-hand) are the commitment devices that carry credibility. Civilian control adds ratification lag as a safety measure. The tension is structural not accidental (Schelling passage on the imperfect decision process is the anchor)
- AI accelerates every military-preferred move: faster evaluation compresses ratification lag, pre-scripted response becomes cheaper to author and rehearse, dead-hand becomes technically tractable, human-in-the-loop empirically collapses to human-as-ratifier (automation bias literature; the Biden-Xi Nov 2024 statement affirming human control was worth extracting precisely because it was slipping)
- The critical shift: LOW becomes *adoptable* by states that could not previously execute it. Pakistan and DPRK are the obvious cases; the second-tier nuclear states move first because they have the fewest resources to adapt any other way
- Petrov failure mode inverted: the accrual bin from 2a says the discriminating information does not exist in the photons yet at early flight. A faster evaluator does not get the right answer sooner; it gets a confident answer sooner. AI decision support in an LOW posture is a machine for producing confident wrong classifications at the moment they most bind
- Ties to 2c: military's structural preference for commitment devices explains why the perceived-NC3-vulnerability channel produces LOW/pre-delegation responses rather than technical remediation

### 2c. NC3-belief channel

- Reframe: the destabilizing dynamic is not "Mythos has compromised Chinese NC3" (unverifiable, wrong artifact) but "Beijing may reasonably believe Mythos could compromise Chinese NC3 without their knowledge, and cannot verify otherwise." Perceived vulnerability drives doctrine (see 2b)
- AI progress shifts the threat model on classical NC3 assumptions across the board: airgap, custom hardware, physical isolation, novel-language compilers, human-in-loop authentication. Each was a reliable assumption; each is now conditional on the adversary's AI capability, which is itself uncertain. Response is doctrine-level (LOW, pre-delegation, dead-hand) not technical (harden, patch, isolate)
- Acton entanglement with AI accelerant: target cannot distinguish espionage from attack-preparation, cannot distinguish disarming cyber first strike from decapitation cyber op until too late. AI compresses the timescale on which the distinction would resolve
- Stuxnet's actual lesson: adversary hardens and creates use-it-or-lose-it pressure on the arsenal that is threatened. Cyber counterforce is destabilizing precisely because states will believe it might work whether or not it does. This connects to the "military wants unsafe" thread from 2b
- Ties to 2d: NC3 is a target inside a larger question about what the AI race puts up as the strategic stake

### 2d. Prize-channel (original contribution)

- AI is not only a capability that acts on the balance; it is a *stake* that changes the payoff matrix. This is the taxonomy entry FA does not have
- Compute is the bottleneck resource. Fabs are the bottleneck for compute. Leading-node fabs are physically concentrated (TSMC Taiwan primary, Samsung and Intel trailing, TSMC Arizona ramping). The chip supply chain is the AI supply chain
- Two asymmetric closing windows: China's window to act on Taiwan *before* domestic leading-node self-sufficiency reduces the strategic value of TSMC-intact-for-China (after which talent-loss is mostly access-denial against the US, so Chinese calculus is more cavalier about physical destruction), and US window to *deter* action on Taiwan before its own domestic ramp reduces the cost of losing TSMC (after which extended-deterrence credibility toward Taipei drops). The dangerous regime is when the windows close on different timelines; the side whose window closes later has strong incentive to act while the other side's leverage is still binding. Argument does not require getting the ordering right, only the closing-window structure right
- The "silicon shield" load-bearing assumption breaks when both sides *no longer want TSMC intact* for the same reasons. Classical shield-value assumed both parties inherit the fabs if they win; that assumption is conditional on both parties still needing them
- Schelling commitment paradox: US hedging against TSMC loss (airlift planning, Arizona ramp, allied fab diversification) reduces vulnerability *and* reduces credibility to defend Taiwan, because visible hedging signals reduced willingness to bear the cost. Cannot credibly commit and credibly hedge simultaneously
- Escalation chain to nuclear stability: fab-race pressure → conventional Taiwan crisis → conventional-nuclear entanglement (DF-21D/DF-26 dual-capable ambiguity, US SIOP-connected satellites as targets, potential JASSM/LRHW ambiguity in US strike packages) → nuclear stability's classical assumption stressed. That assumption: "great powers avoid direct conflict because nuclear risk exceeds any conventional prize." Historically prizes were not worth the risk. AGI plausibly is
- Where I pressure-test my own argument: the Chinese calculus for Taiwan is primarily nationalist (Xi's stated timeline, One China ideology, domestic legitimacy). The fab layer adds pressure at the margin; it is not the driver. The essay should be honest about that ordering and argue that the AI-race adds a *new* accelerant to a pressure system that already existed, not that it invents the pressure

## Section 3: FA comparison and limits (~400 words)

- Where FA is correct and the draft concedes it: physics-locked constraints at the capability layer; splendid first strike remains infeasible at any credible probability of success; C3 elimination in one fell swoop is not tractable; missile defense will not close the gap alone. These are load-bearing observations and the essay is not arguing against them
- Where FA underweights: perceptions as caveat versus load-bearing thesis. FA's Section 5 explicitly concedes "even if predictions of AI power overestimate the technology's actual capabilities, states may perceive greater threats and take potentially destabilizing actions" then treats this as a modest add-on to a stability conclusion. My critique is that this is the load-bearing thesis for the Chang-audience question, not a caveat, and the FA structure inverts the weighting
- Where FA misses: (i) prize-channel entirely, (ii) sudden-takeoff regime hedged in one sentence, (iii) asymmetric erosion (US-vs-China postures generate structurally different threat pictures; the average destabilization is small, the marginal destabilization for the weaker deterrent is not, and average is the wrong metric for stability questions where the tail dominates)
- Their strongest point to concede: nuclear stability logic is deeper than any single technology, and "AI transformation" as a phrase does too much analytical work in the discourse. Correct
- Their weakest point to press: their analysis is calibrated to the pre-takeoff regime. The FA meta-model assumes both sides have decades to adapt to new tech, and this assumption fails first if AI R&D fully automates. Under Chang's operative constraint ("assume AI progress continues"), the pre-takeoff regime is not where the taxonomy needs to be robust

## Section 4: Sudden-takeoff regime (~200 words)

- FA hedges in one sentence: "national security experts should not dismiss this eventuality, and they should continuously monitor for evidence of rapid takeoffs in AI capabilities among rivals." This is where the whole taxonomy shifts
- Time-to-adaptation collapses; offense-defense balance can shift within crisis-relevant timescales; the "AI is transformative but slow enough to adapt to" assumption breaks
- "Wonder weapon" pathologies become operationally relevant: an opponent's *belief* that you have unmatchable capability drives preemption incentive even if you do not (Kahn-era doctrine on "the threat that leaves something to chance" applies here in a form Schelling did not anticipate)
- This is where MAD's classical mutual-knowledge-of-mutual-vulnerability assumption breaks decisively, because mutual knowledge collapses when the AI-progress rate exceeds the arms-control-negotiation rate

## Section 5: Close (~150 words)

- Restated in Schelling frame: nuclear stability was always epistemic and doctrinal, not purely technical. AI attacks the epistemic and doctrinal foundations directly, and the physics-locks FA correctly identifies protect *capabilities* but not *stability*. The distinction is what the essay is arguing
- What would change my mind (marked update criteria per M3 stipulation-and-trigger discipline): explicit no-first-use commitments matched by observable force posture; verifiable de-alerting; arms-control on AI in NC3 decision-support functions; visible slowing of the fab-race window-closing dynamics. Absent those, the taxonomy's channels are all active and reinforcing

## Fact-check queue

- SMIC leading-node status July 2026; TSMC Arizona Phase 1 volume; Intel 18A schedule (my figures need verification before the draft)
- MacDonald (vt)² gap-scaling exact source (I have it from Fable's convo; want to confirm the citation)
- FA article citation form (Winter-Levy and Lalwani, Foreign Affairs, Aug 7, 2025)
- Biden-Xi Nov 2024 human-control statement citation
- Acton entanglement citation (probably Carnegie 2018 or 2020 paper on "Escalation through Entanglement")
- Any recent USSTRATCOM or DoD statements on AI in NC3 that should be named directly
- Uber road-quality-map source (published where?)
- Schelling passages that anchor 2b (I have samples; need clean cites)

## Voice targets and reminders

- Schelling as voice model; long conjunctive sentences with a punchy short one for landing
- No em-dashes anywhere in Dan's output
- CAPS for in-line emphasis over bold or italics (A17, anti-detection overlay)
- Aphoristic compression at turns, budgeted sparse per M6
- Direct in first person on my own claims, marked as opinion where they are opinion
- One buried Schelling-echo line per section maximum; do not over-signature
- Baseline density is variable, not uniformly maximum; keep slack sentences for pacing
