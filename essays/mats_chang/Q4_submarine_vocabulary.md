# On submarine vocabulary

Can an airplane fly? Can a submarine swim? And most important of all: can a machine think?  This is the kind of question that starts fistfights at the NeurIPS wine-and-cheese reception, so let's not be too hasty in our response.  All three questions are posed about a machine that does something akin to animals, but does it in a profoundly different way.  The English word itself doesn't tell us very much about what's actually happening, so let's consider swimming more closely.

Compared to true biological swimming exhibited by whales, submarines have quite "jagged" abilities.  While they excel on some metrics (such as submerged duration and sustained speed), on others (such as turning radius and maximum depth) they fall almost laughably short of their cetacean counterparts. 

The reality is that a given word is normally shorthand for a bundle of related concepts that typically travel together (locomotion, buoyancy, not-drowning), which is fine... right up until you have to decide if what a submarine does is "swim". But naval architects don't debate "Artificial General Swimming"; instead they use spec sheets to talk about submarine abilities.  Critically, those specs are determined by the mission-specific requirements.

So, now... can a machine think?  Have we reached "Artificial General Intelligence"?  Maybe!  Personally I'd say so, because my own benchmark has long been "can I explain the context the person is missing rapidly, so we can get onto an engaging conversation quickly?".  We could call this the "Parshall test", but no one seems to care about it (much like the Turing test, which apparently was not important!).  I don't think we've hit ASI yet, partly because models are still strongly constrained by being frozen snapshots, and partly because they don't yet feel strongly smarter than me.

But in the context of "how do we make sure AI goes well?", we're going to have to get into mission-specific requirements. Using Shah et al.'s breakdown:
 
- Misuse: relatively easy to assign scores to, and the score can correlate with the level of mitigation
- Mistakes: also relatively easy to assign scores, and deployment scenarios (such as failure consequences and autonomy) can be scaled with scoring
- Misalignment: extremely difficult to score, because it's trying to measure an adversarial situation (since a misaligned system wouldn't cooperate).  Probably the best we can hope for on the detection side is measuring other bundles of abilities across time and models, and looking for when those correlations break down; basically we get a one-time "we're probably in danger".
- Structural: this is an enormous can of worms (1700+ per MIT AI Risk Repository), and most don't even begin to have metrics. One top issue is economic impacts (although we're starting to create metrics, and fumbling towards policies).  Others include multi-agent interactions, and other emergent effects.

Of these, misalignment is the hard case, primarily because it's adversarial: a misaligned system has every incentive to look aligned under evaluation, so the absence of observed bad behavior is barely any evidence of misalignment.  Current detection methods generally try to either conceal the evaluation condition, or read the internal representations directly.  But borrowing the early-warning-signals framework from ecology (Scheffer et al.) and the recent port to deep-learning training dynamics (Hennick & Corlouer), I'd suggest extending it to measuring within- and between-model correlations for different abilities over time.  When a model achieves sufficient situational awareness and begins trying to sandbag, it would need to also match the full suite of correlations (a harder task which offers more opportunity for discovery).

So at this stage, AGI/ASI are handy terms for casual conversation, but nearly useless for governance.  Instead, we need different vocabularies for different sides of governance:
- capability/uplift vocabulary for misuse
- autonomy/reliability vocabulary for mistakes
- control vocabulary for misalignment
- systemic risk vocabulary (probably a few) for structural issues

And to close this out, I'll point out that historically we were only measuring one thing: benchmark accuracy aka capability, the axis that Epoch's Capabilities Index [n] now stitches from forty-odd benchmarks using Item Response Theory and a one-factor model from psychometrics.  But psychometrics largely gave up the one-factor model decades ago: luid and crystallized intelligence, working memory, processing speed, and half a dozen more broad factors sit beneath g [n]. The reason a single IQ-like summary works at all for people is that these factors positively correlate: if you're strong on one, usually you're at least decent on the rest, so we can round it off to a scalar.

But recent systems like ADeLe [N] are starting to gain traction on other components (such as "situational awareness", "persuasion" EDIT PUT LIST HERE), suggesting that we could also have an ECI for control, and another ECI for uplift (much like the SAT reports Verbal and Math separately).  Once that's in place, we'll be able to measure each of those, and find that the correlation matrix between them follows the same pattern that it does for humans... I assert that it doesn't follow the pattern, and that is exactly what looks to us like "jaggedness".

Breaking this into components that align with possible interventions makes it easier to see which aspects have technical solutions, which have policy solutions, and probably points us to places where there are no direct solutions at all.  A spec sheet works for a submarine partly because it's built to mission requirements, and partly because a submarine doesn't have its own goals.  But well-chosen vocabulary can help us avoid our abstractions springing a leak, right when we need them most.
