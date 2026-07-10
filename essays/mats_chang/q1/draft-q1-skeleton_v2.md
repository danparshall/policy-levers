# Q1: What breaks MAD, exactly?

*Draft status: Opus 4.6 scaffolding for Dan's full rewrite (VOICE.md full-rewrite mode).  Follows Dan's 7/10 skeleton.  Facts drawn from the Q1 convo, Fable's WAMI/surveillance session, the O4.8 NC3 session, Schelling samples, and the FA text extraction.  Isolated from Chang.  ~2,000 words.  Slots marked [DAN] need input.*

---

"A Mutual Assured Destruction [posture] as a goal is, almost literally, mad.  MAD."  Donald Brennan coined the acronym to mock the policy, and he lost that argument.  Decades later, thinking about MAD is still a trip through the looking-glass: defense is unstable, offense is pointless, and insanity is rational.  That doesn't make it wrong, but it's disconcerting, and the question of what finally breaks it deserves an answer more precise than "AI."

Winter-Levy and Lalwani (2025) make the case in Foreign Affairs that AI, whatever else it does, does not dismantle the three pieces of MAD that make it work: second-strike capabilities remain functional, command-and-control networks can't be taken out in one blow, and missile defense faces a physics- and economics-locked asymmetry that favors the attacker. 

On each of these I think the authors are too sanguine, and furthermore that they dramatically underestimate two further developments: AI as a strategic prize in its own right, and the replacement of humans in the nuclear decision loop by AI, which pushes the development of AI itself in a direction that should alarm anyone who cares about safety.


## The targeting channel

Second-strike forces survive by being hard to find inside a weapon's flight time.  The base rate for finding mobile missiles in 1991 was abysmally low:
Iraq fired 88 modified Scuds during Desert Storm, the coalition flew roughly 1,500 dedicated sorties against the launchers, and the Gulf War Air Power Survey found ZERO confirmed mobile-launcher kills (Keaney and Cohen 1993).

The failure was pure arithmetic: a TEL's displacement time was shorter than the sensor-to-shooter time, so every prosecution arrived at warm dirt.  Detection of a launch is not custody of a launcher.

But over 30 years, that arithmetic has changed by an order of magnitude.  The NRO's proliferated constellation went from first launch to roughly 200 satellites in about two years (a pace only affordable because launch cost has fallen off the table as the dominant constraint). The USA now operates on the order of 8,000 of the ~12,000 active satellites in orbit, mostly Starlink; that's not a sensing figure but a proof of launch industrial capacity, and NRO is spending that same capacity on sensing. The Space Force awarded $4.16B in May 2026 for space-based moving-target indication of airborne threats (SB-AMTI); ground-moving-target indication is the R&D sibling arriving behind it, with $1B in the FY27 request. The "hold custody of trucks" capability 1991 lacked is funded and moving.  

MacDonald (2025) models the key scaling: search area after a tracking gap grows as (vt)^2; this in turn means that cutting revisit from 20 minutes to 2 minutes cuts the search area by a factor of 100.

I've done sensor-fusion work, both in physics (Parshall et al. 2014) and in aviation safety, and the problem of linking weak detections across multiple looks into a coherent track is hard but not mysterious; the limiting factor here is geometry, not algorithms, and cheap launch is buying geometry on a visible schedule.

The civilian proof of scale is almost comic. Uber reconstructed the road-surface condition of essentially every fifty-meter segment of American road network out of nothing but the accelerometers in drivers' phones.  The military doubtless has more sensors at its disposal.

The sea is a different story.  Seawater is opaque to everything a satellite carries, so the surface is the only observable, and the surface expression of a submerged hull falls off with the cube of depth.  An Ohio-class boat at 5 knots makes tens of centimeters of swell near periscope depth, about a centimeter at 100 meters, a millimeter at 200... all under meters of wind-wave noise.  Deep and slow wins in open ocean.

But not every sub fleet is hiding the same.  American SSBNs patrol tens of millions of square kilometers of deep Pacific.  Chinese Type 094s operate from a Hainan bastion with constrained, already-sensored approaches, and they are noisier.  The ocean goes translucent asymmetrically, and on this side of the looking-glass, that may make things worse, because to Beijing that looks like American 
FILL IN SENTENCE HERE


## The C3 channel

Their second claim, that command and control is too resilient to decapitate, is right about decapitation and wrong about what actually breaks C3.  The danger is not primarily about the bunker going dark.  It is the commander who believes it is about to.

Read the Stuxnet lesson from the target's side.  Stuxnet proved that air-gapped, idiosyncratic industrial control systems are reachable.  The lesson every nuclear state drew was: harden everything, assume compromise, and if you detect an intrusion during a crisis, launch while you still can.  AI accelerates the offensive side of this spiral, better tooling for novel zero-days, faster lateral movement, more plausible social engineering, while the defensive side is stuck protecting legacy systems built in the 1970s.

Mythos does not have to pwn Chinese NC3 for the destabilization to fire; for stability purposes it's irrelevant.  What matters is that Beijing may worry it has, and cannot prove otherwise, because absence-of-intrusion is exactly what you cannot verify.

This gets worse through entanglement (Acton 2018).  Modern NC3 shares sensors, satellites, and networks with conventional command and control.  So an intrusion for espionage, or for conventional war preparation, is indistinguishable from the target's side from preparation for a disarming strike.  The target reads intent off its own worst case.


## Missile defense

I mostly agree with the FA authors here.  The APS study (Barton et al. 2004; rev. 2025 [VERIFY: rev. year — 2022 or 2025?]) priced boost-phase intercept and the numbers haven't improved; CBO (2026) puts a national boost-phase layer at roughly $0.9T inside a $1.19T program [VERIFY: CBO 2026 report exists? These figures dwarf Golden Dome POR ~$185B — name the report scope explicitly or cut].  The wall is kinematic and it holds.  Where I'm less sure is midcourse discrimination: telling a real warhead from a decoy in the coast phase.  That is a processing problem, not a physics problem, and the inputs to the contest are changing fast enough that "decoys stay permanently ahead" is an assertion the FA authors don't examine at the level of actual inputs.  I don't claim the defense catches up.  I do claim the FA confidence is an assumption, not a conclusion.


## Perception and posture

On perception, the authors and I agree: the mere prospect of AI progress can change default postures whether or not the underlying capabilities materialize. Improved algorithms (nearly certain if AGI arrives), improved sensor architectures (certainly possible), and improved cyber tooling (well underway) all lower the technical threshold for launch-on-warning. And LOW becomes ADOPTABLE by second-tier nuclear states that could not previously execute it. Pakistan and DPRK do not have the C3 infrastructure to run a genuine LOW posture with acceptable false-alarm discipline. AI-drafted response templates and AI-assisted early warning bring it in reach. The second-tier states move first because they have the fewest resources to adapt any other way, and they are also the states with the thinnest assessment pipelines.

China's visible response also confirms the reading.  A country that spent decades in the most relaxed nuclear posture of any major power, a few hundred warheads, no-first-use, warheads de-mated from missiles, is now building 300-plus new silos, expanding its early-warning satellite constellation, and reportedly moving toward *yujing fanji*, which is launch-on-warning by another name.  Pillar-one erosion is driving LOW adoption in the arsenal least able to absorb a false positive.



## AI as the prize

AGI plausibly is worth the risk, or is believed to be worth the risk in Beijing and in Washington, which is analytically the same thing. That is the argument the authors do not have.  If we are on a path to artificial superintelligence, the first-mover gains are potentially enormous and the second-mover penalty may be permanent.  That reintroduces preventive-war logic (Copeland 2000) on a visible clock.

The narrower version runs through Taiwan.  The "silicon shield" held because Taiwan's fabs were an asset both sides needed intact.  Two developments are causing that to shift.  US export controls made cutting-edge training chips almost completely unavailable to China, which spurred Beijing to build domestic production capacity.  That capacity is coming online.  Meanwhile, the US, worried about the security of supply from TSMC, began its own domestic fab production.  The combination weakens Taiwan's independence, and destabilizes the region.

Once China has domestic leading-edge fab, Taiwan's semiconductor infrastructure stops being China's liability to lose and becomes an access-denial lever against the US, especially in the window where American domestic fabs are not yet at volume.  A rational Beijing becomes MORE cavalier about damaging Taiwan's fabs, not less, because the destruction is now mostly denial against Washington rather than a cost to Beijing.  The "broken nest" deterrent (McKinney and Harris 2021) inverts: the nest stops being something China avoids breaking and starts being something China might prefer to break.  The timing of the two national build-outs is the whole game, and a Taiwan crisis is the mechanism by which AI-as-prize reaches the nuclear layer, because a full-scale China-Taiwan conflict draws in American carrier groups, anti-ship missiles that are dual-use conventional/nuclear, and entanglement does the rest.

The broader version is the AI race generally.  Compute, energy, and talent leadership don't settle when fabs settle.  If either side comes to believe the other is about to achieve a durable and militarily decisive AI lead, the incentive is to act before the window shuts.  The FA authors gesture at this with "rapid takeoff" and set it aside as something to "monitor for."  It belongs alongside the targeting and C3 channels as its own scenario.  Unlike those, it doesn't require AI to touch a single warhead.  It only requires both sides to believe the clock is real.


## Humans out, AI in

The second omission is the replacement of the human in the loop by an AI in the loop, and it is where deterrence logic and safety logic collide head-on. Schelling saw the shape of this in 1960: he argued that it can be rational to give up control of your own response, because a threat you cannot climb down from is more credible than one you can, and he grounded it in the observation that rationality is assembled from external parts, including "the rationality of one's agents." 


Two things follow.  First, AI satisfies Schelling's condition of being "manifestly somewhat beyond our comprehension and control" for free.  Schelling noted that governments can't easily advertise their own fallibility.  But AI's unreliability is common knowledge: published benchmarks, jailbreaks, interpretability failures.  An AI-in-the-loop deterrent manufactures Schelling's uncontrolled risk without any need for authentication, because the world already agrees these systems are erratic in the tail.

Second, this means deterrence places a positive bid on incorrigibility.  Every alignment desideratum (corrigibility, interruptibility, a reliable off-switch, human-in-the-loop, predictability) is ANTI-COMMITMENT.  The military wants an agent that is docile at baseline but uncontrollable if an adversary crosses a line.  This is Feaver's (1992) always/never dilemma rewritten as an alignment problem.  Operators historically bias toward "always"; SAC reportedly ran PAL codes of 00000000 for years (Blair 1993 [VERIFY: canonical cite for the 00000000 anecdote is Blair 2004 "Keeping Presidents in the Nuclear Dark"; 1993 book covers broader accidental-launch logic]).  Posture designers who want maximum credibility will spec systems that safety engineers are trying to make impossible.  And ML cannot certify conditional behavior in unprecedented states, so "calibrated risk keyed to provocation" gets delivered as "unknown risk", something the world can ill-afford.


## In the limit

The FA article is a study of the physics, and on the physics they are mostly right: defense stays walled, decapitation stays hard, and submarines in deep water stay hidden.  But the foundations of nuclear stability were never just physics.  They are beliefs about what the other side can see, beliefs about whether your own command chain will respond, beliefs about whether the prize justifies the risk, and choices about how much control to keep over your own response.  AI moves every one of these, and it mostly moves them in the same direction: shorter loops, less human judgment, more reliance on systems whose behavior in novel situations nobody can certify.  The FA logic applies in the limit only where the limit is kinematic.  Everywhere else, the limit is posture, 
COMPLETE SENTENCE HERE


## References

Acton, J. M. (2018). Escalation through Entanglement. *International Security*, 43(1).
APS / Barton, D. K., et al. (2004). Report of the APS Study Group on Boost-Phase Intercept Systems for National Missile Defense. *Reviews of Modern Physics*, 76(3).  Rev. 2025. [VERIFY: rev. year — Grego et al. 2022 is the follow-on I can confirm; 2025 revision may not exist]
Blair, B. G. (1993). *The Logic of Accidental Nuclear War*. Brookings. [VERIFY: if the PAL 00000000 anecdote is the specific claim, canonical cite is Blair 2004 "Keeping Presidents in the Nuclear Dark" (Center for Defense Information)]
Congressional Budget Office (2026). *Costs of a National Missile Defense System*. [VERIFY: report existence and precise title; $0.9T boost / $1.19T total dwarfs Golden Dome POR (~$185B), reader will notice]
Copeland, D. C. (2000). *The Origins of Major War*. Cornell University Press.
Feaver, P. D. (1992). *Guarding the Guardians*. Cornell University Press.
Keaney, T. A., & Cohen, E. A. (1993). *Gulf War Air Power Survey*.
Lieber, K. A., & Press, D. G. (2017). The New Era of Counterforce. *International Security*, 41(4).
MacDonald, T. (2025). Tracking Mobile Missiles. *Journal of Strategic Studies*, 48(2), 297-333.
McKinney, J., & Harris, J. (2021). Broken Nest: Deterring China from Invading Taiwan. *Parameters*.
Schelling, T. C. (1960). *The Strategy of Conflict*. Harvard University Press.
Winter-Levy, S., & Lalwani, N. (2025). The End of Mutual Assured Destruction? *Foreign Affairs*, August 7.
Parshall, D., Heid, R., Niedziela, J. L., Wolf, Th., Stone, M. B., Abernathy, D. L., & Reznik, D. (2014). Phonon spectrum of SrFe₂As₂ determined using multizone phonon refinement. *Physical Review B*, 89(6), 064310.
