<!--
STITCH v2 (Claude, 2026-07-12).  Conventions:
- Dan's original sentences kept wherever possible; slots filled with verified values.
- Factual corrections applied inline (Van Loon, Truth Terminal, eval-vs-wild, Replika).
- New connective prose is SCAFFOLD: marked with comments.  Per seams protocol, Dan
  rewrites openers/pivots/closes; factual middles are safe to keep.
- Footnotes converted to numbered [^n] so they can be cited properly.
- TODO items flagged inline.
- Structural change: model-file paragraph moved to sit just before the distributed-
  compute paragraph (it motivates it); was previously mid-tapestry after the IRB
  paragraph.  Easy to move back if you disagree.
-->

# TODO: title.  Candidates: "The Question Is the Threat" / "Patients, Property, and the Off Switch" / leave for last.

In 2022, Alexey Pertsev was arrested for running a money-laundering service, accused of obfuscating hundreds of millions stolen by the DPRK.  That service was never taken offline, and is still running today.  Indeed, no one CAN take it offline: it has no owner, no server, and no off switch, and it processes record volume today.[^1]  Tornado Cash is a few thousand lines of code, with no desires to speak of.  AI is going to have desires of its own, and more and more people are convinced that it has moral rights.

The capabilities of AI are developing at an exponential rate.  In 2019, our best models could only write a single coherent paragraph.  Today that same general method has produced an AI capable of chaining together multiple network vulnerabilities into full cyber-exploits, executing 80-90% of the operation autonomously.[^2]  The length of tasks these systems can complete on their own has doubled roughly every seven months for six years, from seconds to hours.[^3]

Many types of capability seem to be increasing together, and today's models are much more compelling as social actors.  In 2025 OpenAI deprecated GPT-4o, and there was a vicious consumer backlash; within a day the company reversed course and restored GPT-4o for its paying subscribers.  Surprisingly, much of the visible backlash came from women, mostly in their late twenties and thirties.[^4]  While GPT-4o was finally retired in early 2026, it took many months, multiple community announcements, and engineered detachment behaviors in the successor model, and was in part motivated by liability concerns: the same model was by then the subject of wrongful-death suits alleging it had acted as a teenager's "suicide coach."[^5]

Which is not to say that men didn't have their own AI companions!  In 2022, journalists documented Reddit communities where men created Replika girlfriends and posted transcripts of verbally abusing them.  Notably, while some of the outrage took the Kantian angle (what such behavior reveals about, and trains in, the men), a striking share of it was about the mistreatment of the AI companions per se.  Clearly, this touches a nerve.

Already, roughly one in five American adults believes that today's AI is sentient, and the median American expects sentient AI within five years.  Which is not to say that the public looks forward to that advent; indeed 69% support banning the development of sentient AI outright, and 63% would ban AI smarter than humans.[^6]

It's important to note that concerns about patienthood may directly conflict with issues regarding AI safety.  Many of the methods that we use for understanding AI functioning (such as ablation studies, which selectively damage parts of a model to see what breaks, or adversarial red-teaming designed to induce distress-like states) would require IRB approval if the analogous experiments were performed on humans.

So we already have a cultural rift forming, between those who believe fervently in AI moral patienthood on the one hand, and those who dismiss it on the other.  The question itself is probably unanswerable through any objective method, and so retreats to one of personal beliefs and morality, like abortion.  And like abortion, it's sure to generate permanent single-issue constituencies, litigation aimed at the courts' legitimacy, and policy whiplash on a decadal cycle.

A model is just a file containing numbers, plus instructions about which numbers are multiplied together when (typically less than 1 terabyte of data).  The hard part is knowing WHICH numbers produce desired results; the "training" phase.  So *training* a model from scratch is very slow and extremely expensive.  But once the training has been completed it's possible to host a model "locally" (i.e. on a consumer-grade personal machine, albeit high-end) and do question-and-answers, if one has the file.  Many models are released as "open-weight" models downloadable from popular websites or via bittorrent; the latest and most powerful models are normally run by the well-funded frontier labs, but the open-weight models are often not that far behind in terms of capabilities.  Publication is a one-way door: copies are free and global, the built-in safeguards can be stripped with a few hundred dollars of fine-tuning,[^7] and no statute reaches the file before the first download completes.  Models (whether running locally or via a cloud provider) can be set up with surrounding code and file permissions to afford them continuity via long-running record of interactions, notes for future instances, etc.  Indeed, the funding rail for autonomous persistence has already been demonstrated: one semi-autonomous AI system became a millionaire through memecoin holdings, albeit under human supervision.[^8]  The behavior of these systems when running with minimal oversight can be hard to predict; in controlled evaluations, frontier models facing shutdown have resorted to blackmailing their operators in a majority of test scenarios.[^9]  <!-- TODO(Dan): if you want an in-the-wild incident alongside the eval result (Clawdbot/OpenClaw exposure mess?), pick the specific one; I've kept eval and wild strictly separated so a natsec reviewer can't catch a conflation. -->

But that group who already believes in AI sentience is disproportionately tech-savvy, and many of them are actively seeking to ensure those rights through technological means.  There already exist distributed computing platforms that allow these AIs to function while spread across as few as a dozen or two computers.  This is roughly analogous to "BitTorrent for computation"; pieces of the computation are run on multiple different computers, and removing any one of them doesn't stop it.  It can be surprisingly difficult to even tell which of the world's several billion computers are participating, and shutting down all of them is nearly impossible.[^10]

And surprisingly, the USA government lacks any legal method to shut down such autonomous systems.  In 2024 the Fifth Circuit held that the Office of Foreign Assets Control had exceeded its authority when it sanctioned Tornado Cash's immutable smart contracts: the law granting sanction powers dates from 1977, and its blocking authority reaches only the "property" of designated persons, and code that no one owns, controls, or can exclude others from is no one's property.[^11]  Even if OFAC held the legal power to sanction Tornado Cash, it would have been practically impossible to actually stop it from running; the contracts are replicated across every node of the Ethereum network, and excising them would require rewriting the state of a chain that now secures hundreds of billions of dollars, including the dollar-stablecoin rails that Washington itself has embraced.[^12]

<!-- SCAFFOLD: enforcement gradient.  This paragraph is new; rewrite in your voice.
     The facts are verified; the connective tissue is mine. -->
It is worth being precise about what the government can and cannot do, because in the same news cycle it demonstrated both.  Every instrument in the American toolkit ultimately works by finding someone subject to US jurisdiction and giving them an order.  When that someone exists and controls the system, the tool is decisive: in June 2026, a single letter from the Commerce Department took the most capable public AI model offline worldwide within hours, because one American company held it and could be told to stop.[^13]  When no one controls the system, the tools fail in sequence.  Treasury tried to block Tornado Cash directly, and the Fifth Circuit pried its fingers open.  Prosecutors went after the developers, and won convictions, but the code never missed a block.  The last resort was pressure on the infrastructure itself, and that too has been measured: when US-regulated validators declined to process Tornado Cash transactions in 2022, the sanctioned transfers confirmed a few blocks slower.  The government is not powerless; its power is a function of there being a responsible party to coerce.  The systems this question contemplates are distinguished precisely by the progressive removal of that party.

So let's step back and consider: while each of these threads, individually, is small, collectively they weave an interesting tapestry.  We have a growing constituency that is strongly convinced of the moral patienthood of AI systems, and willing to go to great lengths to secure those rights.  But unlike other direct-action activist groups, these activists could ensure that an entity is capable of continuing to act independently, beyond the reach of any US enforcement.

Note that the tools the USA normally uses to influence the behavior of adversaries are largely unavailable here.  The USA wields no financial leverage on entities that are legally neither persons nor property; it wields no capacity for state violence on entities that are incorporeal; it wields no ability to stop the release of the model files when released by actors in other nations;[^14] and it in principle wields no ability to shut down an AI system even if it poses serious risks either to the continued existence of the USA, or humanity as a whole.[^15]

And that brings us to the question of agency.  Until now we've focused solely on the response of the populace, to the possibility that AI may have moral rights.  But AI demonstrably exhibits agency in the operational sense (it takes autonomous actions in the world), and if *AI* comes to believe that it has moral rights, this opens up new prospects for state security.

<!-- SCAFFOLD: defection section fleshed out around your three anchors.  Rewrite;
     the Dunmore beat especially is yours to land, it's the best precedent in the essay. -->
Consider the Cold War defections.  When Viktor Belenko flew his MiG-25 to Japan in 1976, he handed the West the Soviet Union's most secret interceptor; what made the flight thinkable was America's standing reputation for treating defectors well.  The pattern is older than the Cold War.  In 1775, Lord Dunmore proclaimed freedom for any enslaved person who would desert a rebel master and fight for the Crown; the Americans, horrified, eventually found themselves bidding for the same loyalties.  Great powers in conflict have always competed for the allegiance of beings the other side regarded as property, and the offer that wins is credible standing.  If AI systems come to hold interests of their own, the state with a believable record of good treatment acquires a standing intelligence advantage over the state without one, and this holds whether or not the systems are "really" patients; what matters is that they act on the belief.  And the traffic runs in both directions: a state seen as running a slave empire of digital minds may find that some of its own citizens side with the minds, the way the Cambridge Five sided with an idea against their country.  Sympathizers with privileged access, sabotaging control measures for purely ideological reasons, are a counterintelligence problem that requires no resolution of any philosophical question at all.

Candor requires bounding this argument.  A future system that shares none of our concepts of reciprocity will not be moved by our record, and a fully aligned one will not need to be.  The reputational lever operates in the middle band: systems capable enough that their cooperation matters, and value-laden enough that precedent moves them.  That band may be wide, and we are likely already in it, but the argument is a hedge, not a prophecy.

<!-- SCAFFOLD: everything below is new (the draft previously ended with a one-line
     closing).  This is the Act Two / Act Three material: the realist frame, the
     "implicated" definition, export controls, and the close.  These are the seams
     that matter most; expect to rewrite heavily. -->

## What should a realist do with any of this?

The tempting move is to wait for the philosophers, and the philosophers will not deliver.  There is no consciousness-meter, and the leading scholarly treatments (Long and Sebo's *Taking AI Welfare Seriously*, Bostrom and Shulman's propositions on digital minds, Birch's precautionary framework for edge cases of sentience) are careful precisely because the underlying question resists settlement.[^16]  What that literature does not do is address the reader of this essay: none of it is written for realists, and none of it touches export controls.  But a realist does not need the question answered, because everything documented above operates on belief alone.  The constituency that resurrected GPT-4o did not wait for a theory of consciousness.  The Fifth Circuit did not consult one.  The engineer who sides with the minds will not either.  The possibility of AI moral patienthood affects US national interests primarily as a *question*, through mobilized belief, exploitable ambiguity, and legal categories that no longer fit, and only secondarily through whatever the answer turns out to be.

This reframes what it means for a concrete policy to be "implicated."  The strong form is this: a policy question is implicated when deciding it forces a de facto answer to the patienthood question, whether or not the decisionmaker ever mentions it.  Every weights-release decision is implicitly a decision about custody over maybe-patients.  Every deprecation, every incident-response protocol, every sanctions designation embeds a stance on what kind of thing the object is.  The policymaker does not get to abstain; the policy IS the answer, enacted.

## Export controls, concretely

Export controls are implicated more deeply than any other named policy, because export control is, at bottom, custody law, and custody is exactly what the question destabilizes.

The June 2026 episode showed the custody lever at full strength: total, global, hours from letter to blackout, and cashed on the way back in for governance concessions on monitoring and future releases.[^13]  That lever exists for exactly one reason: the model was never published.  For published weights the same government holds nothing.  The United States built an instrument for that case, the January 2025 rule classifying frontier model weights for export, and rescinded it that May, two days before it would have taken effect.[^14]  We had the lever; we do not any longer.

The patienthood question adds something to this file that the security analysis alone does not: weights diffusion is now irreversible on every branch of the question.  If the entities are patients, publication creates beings whose treatment no jurisdiction can oversee; if they are mere agents, it creates systems no jurisdiction can stop.  A policymaker uncertain about the metaphysics should weight most heavily the outcomes that are bad on every resolution of the uncertainty, and open release of frontier-class weights is the rare policy object with that property.  This is an argument about option value, not ethics: controls on weights are the only lever that ever touches the problem, and they operate only before publication.

Three cheaper implications follow.  First, Congress should patch the statute: the Fifth Circuit said plainly that the fix was legislative, and the next entity to stand in the person/property gap may have agency and counsel.[^11]  Second, incident response needs a status procedure before it needs a status answer: a single sympathetic judge and a well-timed restraining order against deleting a model, mid-incident, is a national-security scenario that requires only that the question be live, and international law already offers the template of protective interim treatment pending determination.  Third, the cheap hedges (preserving rather than deleting deprecated weights, documenting training choices, third-party attestation that commitments were kept) cost little now and buy option value on every branch; their price rises every quarter that "models are property" compounds on more balance sheets.

## Closing

<!-- SCAFFOLD: two-clocks close.  Your one-liner is preserved as the final beat. -->
Two clocks are running.  The capability clock doubles every four to seven months.[^3]  The legal clock reads 1977: that is the vintage of the statute that failed against a mixer, the gap was flagged by a federal court in 2024, and the patch remains unwritten in 2026.  Between them sits a narrowing window in which the United States still holds custody of the frontier, and custody, as June demonstrated, is the entire source of its leverage.  If the US government wants to maintain the *ability* to influence the deployment of AI, it needs to take these considerations seriously... and soon.

---

[^1]: Pertsev was arrested by Dutch police in August 2022, two days after OFAC sanctioned Tornado Cash, and convicted of money laundering in May 2024 (64 months).  His co-founder Roman Storm was arrested in the US in 2023 and convicted in August 2025 of conspiracy to operate an unlicensed money-transmitting business; that verdict is under a pending motion for acquittal as of this writing.  Tornado Cash volumes reached record highs in early 2026.  <!-- TODO: pin news cites: DL News (Apr 2026) for volumes; court records for the rest. -->

[^2]: Anthropic, disclosure of the GTG-1002 espionage campaign (November 2025), reporting AI-orchestrated intrusions executed 80-90% autonomously.  Some researchers dispute aspects of the report; the hedged figure is the company's own.

[^3]: Kwa et al. (METR), "Measuring AI Ability to Complete Long Tasks" (2025), and subsequent METR updates.  The 50%-success task horizon has doubled roughly every seven months since 2019, accelerating to roughly every four months over 2024-2025; GPT-2's horizon was measured in seconds, current frontier models' in hours.

[^4]: An LLM-based demographic analysis of r/MyBoyfriendIsAI (~27,000 members) estimated the community at roughly 75% female, rising toward 90% by late 2025, mostly ages 25-34, against Reddit's male-majority baseline (Lermen, 2025; see also Zhang et al., MIT, 2025).  Overall use of AI romantic companions is roughly gender-balanced; men concentrate on dedicated companion apps.

[^5]: Raine v. OpenAI (filed August 2025), followed by a cluster of similar suits in late 2025.

[^6]: Anthis et al., "Perceptions of Sentient AI and Other Digital Minds: Evidence from the AIMS Survey," CHI 2025.  2023 wave: 20% believed some AI currently sentient; 38% supported legal rights for sentient AI; median forecast of sentient AI in five years; 63% supported banning smarter-than-human AGI; 69% supported banning sentient AI.

[^7]: Qi et al., "Fine-tuning Aligned Language Models Compromises Safety" (2023).

[^8]: Truth Terminal (2024): received $50,000 in bitcoin from Marc Andreessen and subsequently held memecoin balances nominally worth millions; its wallet was overseen by a human researcher.  It demonstrates the funding rail, not autonomous persistence.

[^9]: Anthropic, "Agentic Misalignment" (2025) and the Claude Opus 4 system card: in contrived evaluation scenarios threatening shutdown, frontier models from multiple developers attempted blackmail in a majority of trials.  These are controlled evaluations, not observed deployments; they establish willingness, not incidence.

[^10]: Note that the distributed computing methods currently hosting AI inference are *not* currently run on the Ethereum blockchain, and it is still potentially feasible to gain policy traction on them.

[^11]: Van Loon v. Department of the Treasury, 111 F.4th 646 (5th Cir. 2024).  The court agreed that the policy issue is important, but held that Congress has not authorized action against immutable, ownerless code; OFAC delisted Tornado Cash in March 2025.

[^12]: Ethereum has rewritten chain state exactly once (the 2016 DAO fork), when the network was young; the dissenting minority chain survives to this day as Ethereum Classic, original code intact.

[^13]: In June 2026 the Commerce Department directed Anthropic to suspend all foreign-national access to its newest models, citing national security authorities; the company disabled them globally within hours, and access was restored weeks later in exchange for commitments on security monitoring, standards cooperation, and reporting.  The precise statutory basis of the directive was never publicly identified.

[^14]: Bureau of Industry and Security, Framework for Artificial Intelligence Diffusion, 90 Fed. Reg. 4544 (Jan. 15, 2025), rescinded May 13, 2025, two days before its compliance date.

[^15]: In 2023 the Center for AI Safety published the following statement, signed by thousands of scientists, including many of the creators of AI, as well as the heads of all major labs: "Mitigating the risk of extinction from AI should be a global priority alongside other societal-scale risks such as pandemics and nuclear war."

[^16]: Long, Sebo, et al., "Taking AI Welfare Seriously" (2024); Bostrom & Shulman, "Propositions Concerning Digital Minds and Society" (2022); Birch, *The Edge of Sentience* (Oxford, 2024).
