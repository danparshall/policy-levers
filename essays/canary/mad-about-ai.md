<!--
General-audience Canary adaptation of essays/mats_chang/q1/Q1_MAD_about_AI.md.
2026-07-16.  Foreign Affairs framing removed (generic "reassuring story" foil per
Dan's choice); Chang postscript dropped; jargon glossed; citations moved inline.
Full-rewrite-mode scaffolding per VOICE.md: factual middles are safe to keep,
seams (openers, pivots, closes) are the parts Dan most needs to retype.
Register down-tunes REVERTED per Dan 2026-07-16: "almost comic," Mythos, and
"pwn" all restored to MATS wording.  "pwn" is the one Dan wasn't confident in;
awaiting reviewer comment before deciding.
-->

# MAD About AI

"A Mutual Assured Destruction [posture] as a goal is, almost literally, mad.  MAD."  Donald Brennan coined the acronym to mock the policy, and he lost that argument.  The bargain he was mocking is simple to state: when both sides can annihilate each other no matter who shoots first, neither shoots, and safety rests on staying mutually vulnerable.  Decades later, thinking about MAD is still a trip through the looking-glass: defense is unstable, clarity is threatening, and insanity is rational.  That doesn't make it wrong, but it's disconcerting, and adding AI into the mix just increases the vertigo.

When people ask whether AI breaks nuclear deterrence, the reassuring answer rests on three claims.  Retaliatory forces survive, because the submarines and mobile missiles that guarantee a second strike stay hidden.  Command networks are too redundant to knock out in one blow.  And missile defense stays broken, because physics and economics both favor the attacker.  The reassurance usually comes with a concession: even where the capabilities never materialize, mere belief in AI progress can push countries into destabilizing postures.

The physics in that story is mostly right.  The comfort doesn't follow.  On survivability and command networks, the standard story mistakes where the danger actually lives; on missile defense it's correct; the concession about belief is carrying more weight than the people who offer it seem to notice.  And the story leaves out two developments entirely: AI as a strategic prize worth fighting over, and the replacement of humans in the nuclear decision loop by AI, which pushes the development of AI itself in a direction that should alarm anyone who cares about safety.


## Finding the missiles

A retaliatory force survives by being hard to find inside a weapon's flight time, roughly thirty minutes for an intercontinental missile.  If your opponent can't locate a launcher in that window, they can't destroy it, and if they can't destroy it, striking first buys them nothing.  The whole edifice rests on hiding.

The base rate for finding mobile missiles used to be abysmal.  Iraq fired 88 modified Scuds during Desert Storm in 1991.  The coalition flew roughly 1,500 sorties dedicated to hunting the launcher trucks.  Confirmed kills, according to the Air Force's own postwar survey: ZERO.  The failure was pure arithmetic.  A launcher could fire and drive away faster than the sensor-to-shooter loop could close, so the strike arrived to bare dirt.

Over 30 years, that arithmetic has changed by an order of magnitude.  The National Reconnaissance Office's new satellite constellation went from first launch to roughly 200 spacecraft in about two years, a pace only affordable because launch cost has stopped being the dominant constraint.  American operators now fly on the order of 8,000 of the roughly 12,000 active satellites in orbit.  Most of those are Starlink, which is not a spy constellation, but which proves the industrial capacity to launch one.  The Space Force awarded $4.16 billion in May 2026 for satellites that track moving aircraft from orbit; the sibling program for tracking vehicles on the ground is arriving behind it, with $1 billion in the FY27 budget request.  The hold-custody-of-trucks capability that 1991 lacked is funded and moving.

A [2025 analysis in the Journal of Strategic Studies](https://doi.org/10.1080/01402390.2024.2435961) models the scaling that matters: when a satellite loses track of a vehicle, the area you have to re-search grows as the square of speed times time.  Cut the revisit gap from 20 minutes to 2 minutes and the search area shrinks by a factor of 100.  I've done sensor-fusion work, both in physics and in aviation safety, and the problem of linking weak detections across multiple looks into a coherent track is hard but not mysterious; the limiting factor here is geometry, not algorithms, and cheap launch is buying geometry on a visible schedule.  The civilian proof of scale is almost comic.  Uber reconstructed the road-surface condition of essentially every fifty-meter segment of American road network out of nothing but the accelerometers in drivers' phones.  The military doubtless has more sensors at its disposal.

The sea is a different story.  Seawater is opaque to everything a satellite carries, so the surface is the only observable, and the surface expression of a submerged hull falls off sharply with depth.  A submarine pushing through the water raises a faint hump on the surface above it, and a [2022 modeling study in Ocean Engineering](https://doi.org/10.1016/j.oceaneng.2022.110792) puts numbers on it: a Russian attack submarine at 5 knots makes about 19 centimeters of swell at 10 meters' depth, comfortably within the 2-centimeter resolution of modern satellite altimeters, dropping to under a centimeter by 40 meters and to under a millimeter by 75, all buried beneath meters of wind-driven wave noise.  Deep and slow wins in open ocean.

But not every submarine fleet hides the same way.  American missile submarines patrol tens of millions of square kilometers of deep Pacific.  China's boats operate from a base on Hainan Island, and their routes out are constrained: shallow shelf water on the way off the coast, then the Bashi Channel south of Taiwan on any push toward the open Pacific.  Both chokepoints are already heavily sensored, and the Chinese boats are noisier to begin with.  The ocean goes translucent asymmetrically, and on this side of the looking-glass that may make things worse, because to Beijing it looks like America preparing to hunt the one leg of their deterrent that isn't getting safer on the same timeline.


## The commander in the dark

Nuclear command and control, NC3 in the trade, is the wiring that connects a national leader to the arsenal.  It really is hard to decapitate: redundant links, hardened facilities, procedures rehearsed for decades.  The standard story is right about decapitation and wrong about what actually breaks the system.  The danger is not primarily the communications going dark.  It is the commander who believes they are about to.

Consider the Stuxnet lesson from the target's side.  Stuxnet, the worm that wrecked Iranian uranium centrifuges around 2010, proved that even air-gapped, one-of-a-kind industrial control systems are reachable.  The lesson every nuclear state drew was: harden everything, assume compromise, and if you detect an intrusion during a crisis, launch while you still can.  AI accelerates the offensive side of this spiral, with better tooling for novel break-ins, faster movement through compromised networks, and more plausible impersonation of trusted people, while the defensive side is stuck protecting legacy systems built in the 1970s.

Mythos does not have to pwn Chinese NC3 for the destabilization to fire; for stability purposes it's irrelevant.  What matters is that Beijing may worry it has, and cannot prove otherwise, because absence-of-intrusion is exactly what you cannot verify.

This gets worse through what James Acton of the Carnegie Endowment calls [entanglement](https://doi.org/10.1162/isec_a_00320).  Modern nuclear command systems share sensors, satellites, and networks with conventional military ones.  So an intrusion for espionage, or for ordinary war preparation, is indistinguishable from the target's side from preparation for a disarming strike.  The target reads intent off its own worst case.


## Missile defense stays broken, fortunately

Missile defense is where the reassurance holds.  Physicists have priced the intercept problem repeatedly, in a [major American Physical Society study in 2004](https://doi.org/10.1103/RevModPhys.76.S1) and again in 2025, and the numbers haven't improved; the Congressional Budget Office puts space-based interceptors at roughly $720 billion inside a $1.2 trillion program over 20 years.  The wall is kinematic: a rising missile is vulnerable for only a few minutes, a warhead coasting through space hides among decoys that cost almost nothing, and every interceptor costs more than the missile it chases.  AI does not obviously change any of those terms.  In our looking-glass world that failure is probably fortunate, since a defense that worked would only prompt a larger offensive buildup to swamp it.


## Postures move before capabilities do

Belief in AI progress changes postures before any capability arrives, and this is the consequence that worries me most.  Improved algorithms (nearly certain if AI keeps advancing), improved sensor architectures (certainly possible), and improved cyber tooling (well underway) all lower the technical threshold for launch-on-warning: the posture in which a country fires its own missiles while the attacker's are still in the air, on the strength of sensor data alone.  Launch-on-warning has historically required infrastructure only the largest arsenals could afford: early-warning satellites, redundant radars, trained staff who can tell a false alarm from an attack in minutes.  Pakistan and North Korea do not have that infrastructure with acceptable false-alarm discipline.  AI-drafted response templates and AI-assisted early warning bring it within reach.  The second-tier nuclear states move first because they have the fewest resources to adapt any other way, and they are also the states with the thinnest assessment pipelines.

China's visible behavior supports this reading.  A country that spent decades in the most relaxed nuclear posture of any major power, a few hundred warheads, no first use, warheads stored separately from missiles, is now building 300-plus new silos, expanding its early-warning satellite constellation, and reportedly moving toward *yujing fanji*, "early-warning counterstrike," which is launch-on-warning by another name.  Erosion of survivability is driving hair-trigger adoption in the arsenal least able to absorb a false positive.


## AI as the prize

Everything so far treats AI as a tool that shifts the nuclear balance.  The larger omission in the standard story is AI as the thing countries might fight over.  If artificial general intelligence is worth the risk, or is believed to be worth the risk in Beijing and in Washington, which is analytically the same thing, then the first-mover gains are potentially enormous and the second-mover penalty may be permanent.  That is preventive-war logic, and historians keep finding it at the origin of major wars.  Now it has a clock attached.

The narrower version runs through Taiwan.  For decades Taiwan's "silicon shield" held because its chip fabs were an asset both sides needed intact; one [2021 article](https://press.armywarcollege.edu/parameters/vol51/iss4/4/) went further and argued the US should deter invasion by credibly threatening to destroy the fabs, leaving China nothing but a "broken nest."  Two developments are shifting that ground.  US export controls made cutting-edge AI chips almost completely unavailable to China, which spurred Beijing to build domestic production capacity, and that capacity is coming online.  Meanwhile the US, worried about the security of its supply from Taiwan, began building fabs at home.

Once China has its own leading-edge fabs, the broken-nest logic reverses: the nest stops being something China avoids breaking and starts being something China might prefer to break.  At that point, destroying Taiwan's semiconductor industry becomes a way to deny America access, especially in the window where American domestic fabs are not yet at volume, and a rational Beijing could become MORE cavalier about damaging Taiwan's fabs, not less.  The timing of the two national build-outs is the whole game.  And a Taiwan crisis is the mechanism by which AI-as-prize reaches the nuclear layer, because a full-scale China-Taiwan war draws in American carrier groups, anti-ship missiles that come in both conventional and nuclear versions, and entanglement does the rest.

The broader version doesn't run through fabs at all.  Compute, energy, and talent leadership don't settle when fabs settle.  If either side comes to believe the other is about to lock in a durable and militarily decisive AI lead, the incentive is to act before the window shuts.  This scenario belongs alongside the targeting and command channels, and unlike them, it doesn't require AI to touch a single warhead.  It only requires both sides to believe the clock is real.


## Humans out, AI in

Replacing the human in the loop is where deterrence logic and safety logic collide.  Thomas Schelling outlined the problem in 1960: it can be rational to give up control of your own response, because a threat you cannot climb down from is more credible than one you can.  He grounded it in the observation that rationality is assembled from external parts, including "the rationality of one's agents."

The philosopher Gregory Kavka [worked out the resulting paradox](https://www.jstor.org/stable/2025707) in 1978.  A rational agent cannot sincerely intend to retaliate, because by the time retaliation is called for, it saves nothing and kills millions; yet the deterrent works only if the intention is credible.  The Cold War solution was to lean hard on training and duty, and hope the adversary would buy it.  But getting normal humans to commit to sociopathic retaliation is extremely difficult.  Consider Vasili Arkhipov, the Soviet officer who refused to concur in launching a nuclear torpedo during the Cuban Missile Crisis.  We remember him as the man who saved the world.  From the posture designer's perspective, he was a reliability failure.  Moscow's eventual answer was Perimeter, a semi-automated system built to guarantee retaliation even if the leadership was already dead: a commitment device in hardware.  An AI in the loop is the natural extension, and it resolves Kavka's paradox.  The machine doesn't need to WANT anything at the moment of retaliation.  It only needs to lack the ability to change its mind.  AI-safety researchers have a name for that ability, "corrigibility," and they consider building it in to be one of the field's central goals.

This has two implications.  First, an AI deterrent satisfies Schelling's condition of being "manifestly somewhat beyond our comprehension and control" for free.  Schelling noted that governments can't easily advertise their own fallibility.  But AI's unreliability is common knowledge: published benchmarks, jailbreaks, embarrassing public failures.  An AI-in-the-loop deterrent manufactures Schelling's uncontrolled risk without any need for authentication, because the world already agrees these systems are erratic in the tail.  This world doesn't merely tolerate sociopathy, it considers conscience a defect to engineer out.

Second, deterrence creates an incentive to instill INCORRIGIBILITY.  Every property the safety field works toward (corrigibility, interruptibility, a reliable off-switch, a human in the loop, predictability) is anti-commitment.  The military wants an agent that is docile at baseline but absolutely inexorable once an adversary crosses the line.  Political scientists call this the always/never dilemma: a nuclear weapon must always fire when ordered and never fire otherwise, and every design choice trades one against the other.  Historically the military has come down firmly toward "always."  Strategic Air Command reportedly set its missile launch-code locks to 00000000 for years, according to the former launch officer Bruce Blair, so that the safeguard could never get in the way.  Posture designers who want maximum credibility will spec systems that safety engineers are trying to make impossible.

This needs research urgently, because the safety community largely assumes corrigibility is desirable, full stop.  To at least one important customer, a corrigible AI is a defective product.


## In the limit

The reassuring story is a story about physics, and the physics mostly holds: defense stays walled, decapitation stays hard, and submarines in deep water stay hidden.  But the foundations of nuclear stability were never just physics.  They are beliefs about what the other side can see, beliefs about whether your own command chain will respond, beliefs about whether the prize justifies the risk, and choices about how much control to keep over your own response.  AI moves all of these, and it mostly moves them in the same direction: shorter loops, less human judgment, more reliance on systems whose behavior in novel situations nobody can certify.  The physics-based comfort applies only where the limit really is physics.  Everywhere else the limit is posture, and posture is being updated now.

Here's what would change my mind.  If satellites that track ground vehicles fail to reach orbit by 2030, the mobile-missile argument stays hypothetical.  Chinese leading-edge fabs reaching volume production inside 18 months would accelerate the broken-nest reversal, whereas slippage past five years would narrow the Taiwan window to a reshoring race.  Public doctrinal confirmation of *yujing fanji* would move Chinese launch-on-warning from inferred to documented.  And published Pentagon solicitations for AI response systems that fire on provocation would confirm the incorrigibility bid as procurement strategy rather than my extrapolation.

If this diagnosis is right, the integration of AI into nuclear command and control is where arms control has to move next, and nobody is negotiating it.  That collision, technical and doctrinal and diplomatic at once, is where the work is.

<!--
LINK STATUS: all six inline links verified against Crossref/publisher 2026-07-16.
- MacDonald 2025 JSS 48(2):297-333, doi:10.1080/01402390.2024.2435961 (open access, CC-BY).
- Sudharsun 2022 Ocean Engineering 249:110792, doi:10.1016/j.oceaneng.2022.110792.
- Acton 2018 International Security 43(1):56-99, doi:10.1162/isec_a_00320.
- APS 2004 Rev. Mod. Phys. 76(3):S1-S424, doi:10.1103/RevModPhys.76.S1.
- McKinney & Harris 2021 Parameters 51(4):23-36, press.armywarcollege.edu/parameters/vol51/iss4/4/.
- Kavka 1978 J. Phil. 75(6):285-302, jstor.org/stable/2025707.
Unlinked (name-only in text): Blair 2004 (CDI defunct, no stable mirror found),
CBO 2026, Gulf War Air Power Survey 1993, Schelling 1960 (book), Brennan quote.
FLAG FOR DAN: source essay says "considers conscience a DEFEAT to engineer out";
this version says "defect."  If "defeat" was deliberate, revert here.
-->
