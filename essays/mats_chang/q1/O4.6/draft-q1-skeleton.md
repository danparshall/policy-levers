# Q1: What breaks MAD, exactly?

*Draft status: Opus 4.6 scaffolding for Dan's full rewrite (VOICE.md full-rewrite mode).  Follows Dan's 7/10 skeleton.  Facts drawn from the Q1 convo, Fable's WAMI/surveillance session, the O4.8 NC3 session, Schelling samples, and the FA text extraction.  Isolated from Chang.  ~2,000 words.  Slots marked [DAN] need input.*

---

"A Mutual Assured Destruction [posture] as a goal is, almost literally, mad.  MAD."  Donald Brennan coined the acronym to mock the policy, and he lost that argument.  Decades later, thinking about MAD is still a trip through the looking-glass: defense is unstable, offense is pointless, and insanity is rational.  That doesn't make it wrong, but it's disconcerting, and the question of what finally breaks it deserves an answer more precise than "AI."

Winter-Levy and Lalwani (2025) make the case in Foreign Affairs that AI won't fundamentally destabilize MAD.  Three claims: second-strike forces remain too hard to find and destroy simultaneously; command-and-control networks are too redundant to decapitate; and missile defense still faces an economics that favors the attacker.  Then a concession that does more work than they let it: even if AI doesn't actually break any of these pillars, the perception that it might will drive states toward more warheads, faster launch postures, and shorter decision loops.  That concession is correct, and I'll come back to it, but it also quietly saves their argument by letting them treat every erosion as a perception problem rather than a capability problem.

I'm less comfortable than they are, and the disagreement is specific.  On all three capability claims, they are describing a threshold and never saying where it sits.  "States are unlikely to risk a splendid first strike on anything less than a safe bet" is true and unfalsifiable as written.  The question this prompt asks is precisely the one they skip.  And beyond their three pillars, they dramatically underestimate two further developments: AI as a strategic prize in its own right, and the replacement of humans in the nuclear decision loop by AI, which pushes the development of AI itself in a direction that should alarm anyone who cares about safety.


## The targeting channel

Second-strike forces survive by being hard to find inside a weapon's flight time.  Ignorance is the armor.  The base rate for finding mobile missiles is the 1991 Scud hunt: Iraq fired 88 modified Scuds during Desert Storm, the coalition flew roughly 1,500 dedicated sorties against the launchers, and the Gulf War Air Power Survey found zero confirmed mobile-launcher kills (Keaney and Cohen 1993).  The targets were emphatically real; missiles kept landing in Tel Aviv through the final week.  The failure was pure arithmetic: a TEL's displacement time was shorter than the sensor-to-shooter time, so every prosecution arrived at warm dirt.  Detection of a launch is not custody of a launcher.

That arithmetic's inputs are changing by an order of magnitude.  The NRO's proliferated constellation went from first launch to roughly 200 satellites in about two years.  The US now operates on the order of 8,000 of the ~12,000 active satellites in orbit and is adding more every month.  The Space Force awarded $4.16B in May 2026 for space-based moving-target indication, which is the "hold custody of trucks" capability 1991 lacked.  MacDonald (2025) models the key scaling: search area after a tracking gap grows as (vt)^2, so revisit time enters quadratically.  Cutting revisit from 20 minutes to 2 minutes cuts the search area by a factor of 100.  I've done sensor-fusion work, both in physics (neutron scattering) and in aviation safety, and the problem of linking weak detections across multiple looks into a coherent track is hard but not mysterious; the limiting factor is geometry, not algorithms, and cheap launch is buying geometry on a visible schedule.  Uber built a map of road-surface conditions for every 50-meter segment of US road from nothing but the accelerometers in drivers' phones: a signal far weaker than a TEL's, extracted at national scale from sensors nobody deployed for the purpose.  The military version has purpose-built sensors and a decade of persistent-surveillance doctrine behind it.

The sea is a different story.  Seawater is opaque to everything a satellite carries, so the surface is the only observable, and the surface expression of a submerged hull falls off with the cube of depth.  An Ohio-class boat at 5 knots makes tens of centimeters of swell near periscope depth, about a centimeter at 100 meters, a millimeter at 200, under meters of wind-wave noise.  I worked on super-resolution directly [DAN: cite Parshall et al.], and I can say with affection for the processing side and then against it: super-resolution buys the searcher a linear factor from redundancy and a known kernel; the evader holds a cubic dial in depth and a quadratic one in speed.  Deep and slow wins in open ocean.

But notice the asymmetry the FA article buries.  American SSBNs patrol tens of millions of square kilometers of deep Pacific.  Chinese Type 094s operate from a Hainan bastion with constrained, already-sensored approaches, and they are noisier.  The ocean goes translucent asymmetrically, against Beijing's deterrent first, which from Beijing's chair looks like American damage-limitation capability arriving on schedule.  That perception is the FA authors' own mechanism, turned against their own conclusion.

China's visible response confirms the reading.  A country that spent decades in the most relaxed nuclear posture of any major power, a few hundred warheads, no-first-use, warheads de-mated from missiles, is now building 300-plus new silos, expanding its early-warning satellite constellation, and reportedly moving toward *yujing fanji*, which is launch-on-warning by another name.  Pillar-one erosion is driving LOW adoption in the arsenal least able to absorb a false positive.


## The C3 channel

Their second claim, that command and control is too resilient to decapitate, is right about decapitation and wrong about what actually breaks C3.  The danger is not the bunker going dark.  It is the commander who believes it is about to.

Read the Stuxnet lesson from the target's side.  Stuxnet proved that air-gapped, idiosyncratic industrial control systems are reachable.  The lesson every nuclear state drew was: harden everything, assume compromise, and if you detect an intrusion during a crisis, launch while you still can.  AI accelerates the offensive side of this spiral, better tooling for novel zero-days, faster lateral movement, more plausible social engineering, while the defensive side is stuck protecting legacy systems built in the 1970s.  Whether a frontier AI system has actually penetrated Chinese NC3 is unknowable and, for stability purposes, irrelevant.  What matters is that Beijing may worry it has, and cannot prove otherwise, because absence-of-intrusion is exactly what you cannot verify.  A capability that is cheap to fear and impossible to disprove moves posture whether or not it exists.

This gets worse through entanglement (Acton 2018).  Modern NC3 shares sensors, satellites, and networks with conventional command and control.  So an intrusion for espionage, or for conventional war preparation, is indistinguishable from the target's side from preparation for a disarming strike.  The target reads intent off its own worst case.


## Missile defense

I mostly agree with the FA authors here.  The APS study (Barton et al. 2004; rev. 2025) priced boost-phase intercept and the numbers haven't improved; CBO (2026) puts a national boost-phase layer at roughly $0.9T inside a $1.19T program.  The wall is kinematic and it holds.  Where I'm less sure is midcourse discrimination: telling a real warhead from a decoy in the coast phase.  That is a processing problem, not a physics problem, and the inputs to the contest are changing fast enough that "decoys stay permanently ahead" is an assertion the FA authors don't examine at the level of actual inputs.  I don't claim the defense catches up.  I do claim the FA confidence is an assumption, not a conclusion.


## Perception and posture

I fully agree with their concession that the mere PROSPECT of AI changing these capabilities can shift default postures.  Improved algorithms (nearly certain with continued progress) and better sensor technology (certainly possible) could make launch-on-warning viable for states that couldn't execute it before, states with fewer warheads, less experience managing nuclear weapons, and higher baseline instability.  That is where the danger already lives, and it doesn't require any of the capability claims to be settled.


## AI as the prize

Beyond the three pillars they examine, Winter-Levy and Lalwani underestimate the impact of AI as a strategic prize.  If we are on a path to artificial superintelligence, the first-mover gains are potentially enormous and the second-mover penalty may be permanent.  That reintroduces preventive-war logic (Copeland 2000) on a visible clock.

The narrower version runs through Taiwan.  The "silicon shield" held because Taiwan's fabs were an asset both sides needed intact.  Two developments are dissolving that.  US export controls made cutting-edge training chips almost completely unavailable to China except when deliberately authorized, which spurred Beijing to build domestic production capacity.  That capacity is coming online.  Meanwhile, the US, worried about the security of supply from TSMC, began its own domestic fab production.  Both sides are reshoring, which sounds stabilizing until you watch the sign flip.

Once China has domestic leading-edge fab, Taiwan's semiconductor infrastructure stops being China's liability to lose and becomes an access-denial lever against the US, especially in the window where American domestic fabs are not yet at volume.  A rational Beijing becomes MORE cavalier about damaging Taiwan's fabs, not less, because the destruction is now mostly denial against Washington rather than a cost to Beijing.  The "broken nest" deterrent (McKinney and Harris 2021) inverts: the nest stops being something China avoids breaking and starts being something China might prefer to break.  Reshoring, meant to stabilize, destabilizes on the way to stabilizing.  The timing of the two national build-outs is the whole game, and a Taiwan crisis is the mechanism by which AI-as-prize reaches the nuclear layer, because a full-scale China-Taiwan conflict draws in American carrier groups, anti-ship missiles that are dual-use conventional/nuclear, and entanglement does the rest.

The broader version is the AI race generally.  Compute, energy, and talent leadership don't settle when fabs settle.  If either side comes to believe the other is about to achieve a durable and militarily decisive AI lead, the incentive is to act before the window shuts.  The FA authors gesture at this with "rapid takeoff" and set it aside as something to "monitor for."  It belongs in the taxonomy as a first-class branch.  Unlike the instrument branches, it doesn't require AI to touch a single warhead.  It only requires both sides to believe the clock is real.


## Humans out, AI in

The deepest entry in the taxonomy, and the one the FA article doesn't see at all, is what happens when AI replaces humans in the nuclear decision loop.

Schelling (1960) makes an argument that reads, in 2026, like it was written about AI.  His claim is that it can be rational to make yourself not fully rational: to give up control over your own future response, because a threat you cannot climb down from is more credible than one you can.  Crucially, he grounds this in the observation that rationality is not inalienable.  It is assembled from external parts: "such things as one's hearing aid, the reliability of the mails, the legal system, and the rationality of one's agents and partners."  Delegate your response to an agent, and you have altered your own rationality by choosing the agent.  That is a description of AI-in-the-loop, written sixty-six years ago.

Two things follow.  First, AI satisfies Schelling's condition of being "manifestly somewhat beyond our comprehension and control" for free.  Schelling noted that governments can't easily advertise their own fallibility.  But AI's unreliability is common knowledge: published benchmarks, jailbreaks, interpretability failures.  An AI-in-the-loop deterrent manufactures Schelling's uncontrolled risk without any need for authentication, because the world already agrees these systems are erratic in the tail.

Second, this means deterrence places a positive bid on incorrigibility.  Every alignment desideratum (corrigibility, interruptibility, a reliable off-switch, human-in-the-loop, predictability) is ANTI-COMMITMENT.  The military wants an agent that is docile at baseline but uncontrollable if an adversary crosses a line.  This is Feaver's (1992) always/never dilemma rewritten as an alignment problem.  Operators historically bias toward "always"; SAC reportedly ran PAL codes of 00000000 for years (Blair 1993).  Posture designers who want maximum credibility will spec systems that safety engineers are trying to make impossible.  And ML cannot certify conditional behavior in unprecedented states, so "calibrated risk keyed to provocation" gets delivered as "unknown risk," and the gap between the two is where the accident lives.

One last thing this removes.  Human delegated agents were always unreliably committed; they have a survival instinct, they can refuse, they can mutiny.  Arkhipov on B-59 was that unreliability functioning as a safety catch: the human veto nobody designed in.  A deterrence AI built without a refusal capability is the first delegated agent with no Arkhipov floor.  The incentive structure of deterrence is trying to engineer out the very affordance that AI safety is trying to engineer in.

[DAN: consider whether the claude-exit resonance is worth a sentence here or too inside-baseball for Chang.]


## In the limit

The FA article is a study of the physics, and on the physics they are mostly right: defense stays walled, decapitation stays hard, and submarines in deep water stay hidden.  But the load-bearing assumptions for nuclear stability were never just physics.  They are beliefs about what the other side can see, beliefs about whether your own command chain will respond, beliefs about whether the prize justifies the risk, and choices about how much control to keep over your own response.  AI moves every one of these, and it moves them in the same direction: shorter loops, less human judgment, more reliance on systems whose behavior in novel situations nobody can certify.  The FA logic applies in the limit only where the limit is kinematic.  Everywhere else, the limit is posture, and posture is a choice.


## References

Acton, J. M. (2018). Escalation through Entanglement. *International Security*, 43(1).
APS / Barton, D. K., et al. (2004). Report of the APS Study Group on Boost-Phase Intercept Systems for National Missile Defense. *Reviews of Modern Physics*, 76(3).  Rev. 2025.
Blair, B. G. (1993). *The Logic of Accidental Nuclear War*. Brookings.
Congressional Budget Office (2026). *Costs of a National Missile Defense System*.
Copeland, D. C. (2000). *The Origins of Major War*. Cornell University Press.
Feaver, P. D. (1992). *Guarding the Guardians*. Cornell University Press.
Keaney, T. A., & Cohen, E. A. (1993). *Gulf War Air Power Survey*.
Lieber, K. A., & Press, D. G. (2017). The New Era of Counterforce. *International Security*, 41(4).
MacDonald, T. (2025). Tracking Mobile Missiles. *Journal of Strategic Studies*, 48(2), 297-333.
McKinney, J., & Harris, J. (2021). Broken Nest: Deterring China from Invading Taiwan. *Parameters*.
Schelling, T. C. (1960). *The Strategy of Conflict*. Harvard University Press.
Winter-Levy, S., & Lalwani, N. (2025). The End of Mutual Assured Destruction? *Foreign Affairs*, August 7.
[DAN: Parshall et al. super-resolution citation to supply.]
