# On submarine vocabulary

Can an airplane fly? Can a submarine swim? And most important of all: can a machine think?  This is the kind of question that starts fistfights at the NeurIPS wine-and-cheese reception, so let's not be too hasty in our response. All three questions are posed about a machine that does something akin to animals, but does it in a profoundly different way. The English word itself doesn't tell us very much about what's actually happening, so let's consider swimming more closely.

Compared to true biological swimming exhibited by whales, submarines have quite "jagged" abilities. While they excel on some metrics (such as submerged duration and sustained speed), on others (such as turning radius and maximum depth) they fall almost laughably short of their cetacean counterparts. But naval architects don't debate "Artificial General Swimming"; instead they use spec sheets to talk about submarine abilities. Critically, those specs are determined by the mission-specific requirements.

But the goal of measurement is generally to allow better decision-making. And at this point, the most important thing about AI is "making sure it goes well", so our mission-specific requirements should serve that end (so we can make better decisions as we get progress). One useful framework is by Shah et al. [1], because their division is focused on which kinds of interventios are possible. Under that breakdown:
 
- Misuse: relatively easy to assign scores to, and the score can correlate with the level of mitigation
- Mistakes: also relatively easy to assign scores, and deployment scenarios (such as failure consequences and autonomy) can be scaled with scoring
- Misalignment: extremely difficult to score, our best case is probably a one-time "we're in danger".
- Structural: this is an enormous can of worms (1700+ per MIT AI Risk Repository [2]), and most don't even begin to have metrics. One top issue is economic impacts (although we're starting to create metrics, and fumbling towards policies). Others include multi-agent interactions, and other emergent effects.

Of these, misalignment is the hard case, primarily because it's adversarial: a misaligned system has every incentive to look aligned under evaluation, so the absence of observed bad behavior is barely any evidence of misalignment. Current detection methods generally try to either conceal the evaluation condition, or read the internal representations directly. But borrowing the early-warning-signals framework from ecology (Scheffer et al. [3]) and the recent port to deep-learning training dynamics (Hennick & Corlouer [4]), I'd suggest extending it to measuring within- and between-model correlations for different abilities over time. When a model achieves sufficient situational awareness and begins trying to sandbag, it would need to also match the full suite of correlations (a harder task which offers more opportunity for discovery).

So, now... can a machine think?  Have we reached "Artificial General Intelligence"?  Maybe!  Personally I'd say so, because my own benchmark has long been "can I explain the context the person is missing rapidly, so we can get onto an engaging conversation quickly?". It's a variation on the Turing test [5], and we blew past several models ago (and apparently was not important after all).

So at this stage, I feel AGI/ASI are handy terms for casual conversation, but nearly useless for governance. Instead, we need different vocabularies for different aspects of governance:
- capability/uplift vocabulary for misuse
- autonomy/reliability vocabulary for mistakes
- control vocabulary for misalignment
- systemic risk vocabulary (probably a few) for structural issues

And to close this out, I'll point out that historically we were only measuring one thing: benchmark accuracy aka capability, the axis that Epoch's Capabilities Index [6] now stitches from forty-odd benchmarks, based on Item Response Theory and a one-factor model from psychometrics. But psychometrics largely gave up the one-factor model of intelligence decades ago: fluid and crystallized intelligence, working memory, processing speed, and half a dozen more broad factors sit beneath `g` [n]. The reason a single IQ-like summary works for humans is that these factors positively correlate: if you're strong on one, usually you're at least decent on the rest, so we can round it off to a scalar.

But recent systems like ADeLe [7] are starting to gain traction on other components (such as "Calibrating Knowns & Unknowns", "Mind Modelling & Social Cognition", etc.), suggesting that we could also have an ECI for control, and another ECI for uplift (much like the SAT reports Verbal and Math separately). Once that's in place, we'll be able to measure each of those, and I assert we'll find that the correlation matrix between them doesn't follow the same pattern that it does for humans... and that, in turn, is exactly what looks to us like "jaggedness".

Breaking our notion of machine intelligence into vocabulary that align with possible interventions makes it easier to see which aspects have technical solutions, which have policy solutions, and probably points us to places where there are no direct solutions at all. A spec sheet works for a submarine partly because it's built to mission requirements, and partly because a submarine doesn't have its own goals. But well-chosen vocabulary can help us avoid our abstractions springing a leak, right when we need them most.

---

## References

[1] R. Shah et al., "An Approach to Technical AGI Safety and Security," Google DeepMind, 2025. arXiv:2504.01849.

[2] P. Slattery et al., "The AI Risk Repository: A Comprehensive Meta-Review, Database, and Taxonomy of Risks From Artificial Intelligence," MIT, 2024. arXiv:2408.12622. (1700+ risks as of the December 2025 update.)

[3] M. Scheffer et al., "Early-warning signals for critical transitions," *Nature* 461:53–59, 2009.

[4] M. Hennick and G. Corlouer, "From Density Matrices to Phase Transitions in Deep Learning: Spectral Early Warnings and Interpretability," 2026. arXiv:2603.29805.

[5] A. M. Turing, "Computing Machinery and Intelligence," *Mind* 59(236):433–460, 1950.

[6] A. Ho et al., "A Rosetta Stone for AI Benchmarks," Epoch AI, 2025. arXiv:2512.00193. (Basis for the Epoch Capabilities Index.)

[7] L. Zhou et al., "General Scales Unlock AI Evaluation with Explanatory and Predictive Power," *Nature*, 2026. arXiv:2503.06378. (The ADeLe battery: 18 demand scales.)
