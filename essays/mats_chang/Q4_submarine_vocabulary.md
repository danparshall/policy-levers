# On submarine vocabulary

Can an airplane fly? Can a submarine swim? And most important of all: can a machine think?  This is the kind of question that starts fistfights at the NeurIPS wine-and-cheese reception, so let's not be too hasty in our response.  All three questions are posed about a machine that does something akin to animals, but does it in a profoundly different way.  The English word itself doesn't tell us very much about what's actually happening, so let's consider swimming more closely.

Compared to true biological swimming exhibited by whales, submarines have quite "jagged" abilities.  While they excel on some metrics (such as submerged duration and sustained speed) on others (such as turning radius and maximum depth) they fall almost laughably short of their cetacean counterparts. 

The reality is that a given word is normally shorthand for a bundle of related concepts that typically travel together (locomotion, buoyancy, not-drowning), which is fine... right up until you have to decide if what a submarine does is "swim". But naval architects don't debate "Artificial General Swimming"; instead they use spec sheets to talk about submarine abilities.  Critically, those specs are determined by the mission-specific requirements.

So, now... can a machine think?  Have we reached "Artificial General Intelligence"? Maybe!  Personally I'd say so, because my own benchmark has long been "can I explain the context the person is missing rapidly, so we can get onto an engaging conversation quickly?".  We could call this the "Parshall test", but no one seems to care about it (much like the Turing test, which, having been clearly surpassed, was obviously not important!)

But in the context of "how do we make sure AI goes well?" then we're going to have to get into mission-specific requirements. Using Shah et al.'s breakdown:
 
- Misuse: relatively easy to assign scores to, and the score can correlate with the level of mitigation
- Mistakes: also relatively easy to assign scores, and deployment scenarios (such as failure consequences and autonomy) can be scaled with scoring
- Misalignment: extremely difficult to score, because it's trying to measure an adversarial situation (since a misaligned system wouldn't cooperate).  Probably the best we can hope for is measuring other bundles of abilities across time and models, and looking for when those correlations break down; basically we get a one-time "we're probably in danger".
- Structural: this is an enormous can of worms (1700+ per MIT AI Risk Repository), and most don't even begin to have metrics. One top issue is economic impacts (although we're starting to create metrics, and fumbling towards policies).  Others include multi-agent interactions, and other emergent effects.

So at this stage, AGI/ASI are handy terms for casual conversation, but nearly useless for governance.  Instead, we need different vocabularies for different sides of governance:
- capability/uplift vocabulary for misuse
- autonomy/reliability vocabulary for mistakes
- control vocabulary for misalignment
- systemic risk vocabulary (probably a few) for structural issues


This makes it easier to see which aspects have technical solutions, which have policy solutions, and probably points us to places where there are no direct solutions at all.  A spec sheet works for a submarine partly because it's built to mission requirements, and partly because a submarine doesn't have its own goals.  But well-chosen vocabulary can help us avoid our mental models springing a leak, right when we go off the deep end.
