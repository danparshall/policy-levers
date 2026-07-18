<!--
Canary blog draft: GAAIA analysis summary.  2026-07-17, rev 2.
Claude draft rewritten against dotfiles/VOICE.md + docs/reference/llm-writing-tics.md
(contrast-scaffold cluster thinned 6->2, triads broken, labeled devices cut,
provenance claim corrected to "gone through").  Dan still owns seams.
Crosspost: LessWrong (NB: LW AI-writing policy), BlueDot.
-->

# The Best AI Bill Congress Hasn't Introduced Yet

Last month, Representatives Jay Obernolte (R-CA) and Lori Trahan (D-MA) released a [269-page discussion draft](https://trahan.house.gov/uploadedfiles/the_great_american_ai_act_discussion_draft.pdf) called the Great American AI Act, or GAAIA (pronounced like "Gaia", GUY-uh). A discussion draft means the bill hasn't been introduced; it exists to collect feedback before it becomes a real bill, and the sponsors have opened a public inbox for exactly that purpose. Over the past week Fable and I have gone through all 269 pages, section by section (it took a while).

Overall this seems the best-drafted federal AI bill to date, and anyone who is worried about the impacts of AI (whether economic or existential) should be glad that the issue is being taken seriously.  It also looks like it's pulling together all the right pieces to actually make something happen.


## What the bill actually is

The heart of the bill is a straightforward trade with a sunset clause: for three years, states would be barred from enforcing laws that specifically regulate frontier AI development. In exchange, the bill imposes federal transparency requirements on large frontier developers (roughly, labs training models above 10^26 operations *and* with more than $50M in annual revenue): published safety frameworks, incident reporting to a new Center for AI Standards and Innovation (CAISI) at Commerce, semi-annual audits by licensed independent verification organizations, and the strongest whistleblower protections of any provision in the bill. 

This is absolutely a "visibility" bill, not a "control" bill; since currently we have absolutely zero visibility, it's a clear improvement on that front.  But because it's not a control bill, nothing actually PREVENTS deployment. If a developer's audit goes badly, the consequence is disclosure and penalties; the release ships anyway.  Obvious concerns are obvious, but on the other hand, this means it will get less pushback from the pro-business, e/acc end of things. Whether the tradeoff is worth a three-year preemption is, uh, contested (see below). Whether the visibility machinery would actually work as drafted is the technical question, and there I found things worth flagging.


## The bug that makes AI fraud cheaper
First, the small stuff, as a taste of what a 269-page draft inevitably contains. Section 131 raises the maximum fine for mail and wire fraud from $1M to $2M, and adds an enhancement clause for fraud "committed with the assistance of artificial intelligence"... but the AI clause maxes out at $1M. Read literally, using AI to commit wire fraud LOWERS your maximum fine (presumably the AI clause was an earlier addition, and nobody reconciled this).  Elsewhere, a cross-reference points to the definitions section instead of the section it plainly means, and a statutory citation points at an executive order that was rescinded in January 2025. None of this is scandalous. It's what discussion drafts are for, and it's why the sponsors opened an inbox (GAAIA@mail.house.gov, if you'd care to comment on your own). Canary is compiling a technical corrections annex and will file it there.

## The clause that isn't there

The most worrisome issue is that GAAIA contains no severability clause and no inseverability clause; the words don't appear anywhere in the text. Under default doctrine, courts presume severability, meaning a successful challenge to one part of a bill leaves the rest standing.

So what does that do to the core trade? The transparency requirements compel speech from developers, and the compelled-speech playbook that industry ran against state laws in *NetChoice* would be the obvious challenge here. Suppose it succeeds: the transparency and audit sections fall, and the preemption survives alone. Three years of blocked state law, with the federal visibility that justified it struck down in court.  The converse is also possible, in which the preemption falls and the burdens survive.  Different folks might debate whether or not any given trade is worth it, but no one wants half a trade.  This is easy to fix with an inseverability provision linking the transparency, audit, and preemption sections, so that if any one of them falls then they *all* fall, and the deal returns to Congress.  



## Who owes what

Under this regime there are basically 2 categories with required reporting:
- "frontier developers" are labs that trained 10^26 operations (total training, including fine-tuning) _and_ $50M in prior-year annual revenue.
- "large frontier developers" are labs with the same compute _and_ $500M in prior-year revenue; these have a heavier framework

The "large frontier developers" are where most of the action happens.  They need to have published safety frameworks, semi-annual IVO audits, etc.  The smaller developers only need to publish transparency reports concurrent with a release, file critical-safety incidents within 15 days of discovery, and have liability for knowingly false statements.  Not that it matters at this point, basically everyone is either a "large" or nothing.  This actually seems fairly prudent: we don't want to set the threshold too high for the full audit experience, but we want SOME visibility before then.

So this provides a nice easy off-ramp for folks who are small potatoes.  But notice that it *also* allows a nice off-ramp for folks who are BIG potatoes, but don't have any revenue at all yet... I'm lookin' right at Ilya Sutskever's "Safe Superintelligence", which with over $3 billion of funding could easily have produced a model over that 10^26 threshold, and wouldn't have to tell a soul.  So Ilya, what *are* you up to?

For either size, violation is a fine of up to $1M/day, which may not sting if you're pulling in $30B/year: even a full year of stonewalling runs $365M, barely 1% of revenue.  Maybe it should be "greater of $1M or 0.1% of annual revenue, per day".  Otherwise labs could completely ignore this and just call it "cost of doing business".

One fun tidbit is that there's nothing in there saying anything about US creators, so I guess this applies to DeepSeek?  Or at least deploying within the USA?  We'll find out!

## The audit is SOX for AI

The bill doesn't tell developers what their safety practices must be. It requires large frontier developers to write their own "frontier AI framework", publish it (redactions allowed), and then submit to semi-annual audits where the IVO's job is twofold: assess whether the developer actually follows its own plan, and assess whether the plan itself is adequate. Add the required assessment of internal controls and designated senior compliance personnel, and anyone who has lived through Sarbanes-Oxley will recognize the architecture: management defines the controls, the auditor attests to design and operating effectiveness. Same deal here, with catastrophic risk in place of financial reporting.

The structure has real virtues. It doesn't freeze 2026 safety practice into statute, and it scales with whatever labs actually do. It also inherits SOX's known failure mode: adequacy assessments drift toward checkbox unless the standard they certify against has a floor. Here the standard is "acceptable levels of catastrophic risk mitigation", which the bill defines as mitigation adequate to ensure the model's anticipated benefits outweigh its catastrophic risks. That's a cost-benefit judgment, keyed to the developer's own anticipations, with no floor beneath it. The auditor certifies a balancing test, and the developer holds the scale.


## Weights, one-way doors, and paperwork due after the fact

Two findings concern open-weight releases and model identity, and they connect to something [I've written about before](https://canaryinstitute.ai/blog/reversibility-of-coma/).

Releasing model weights is a one-way door: once the files are public no injunction claws them back. GAAIA handles this with a report due "before or concurrent with" deployment.  Technically a lab could release the weights on the same day they release the report, and there's no problem. The natural fix borrows from antitrust: Hart-Scott-Rodino requires merging parties to notify the government and wait a fixed 30-day period before closing, so that if there *is* a potential impact, relevant government agencies have a chance to respond.

The second gap is less obvious. Nothing in the bill establishes that the model anyone's findings describe is the model actually deployed. I went through sections 111 and 112 carefully to confirm this. The IVO doesn't evaluate models; it audits the framework and the developer's compliance with it, while the model-level risk assessments are the developer's own, self-published. The machinery even contemplates findings that "a frontier model is in conformance with its published frontier AI framework", but a model is identified only by its release date, languages, modalities, and intended use; the post-audit report requires the auditor's phone number and no model identifier of any kind. The bill polices *lying* about the model (false-statement liability, whistleblower protections), but it never *identifies* the model. It's a testimony-based regime where a verification-based one costs nothing extra.

The fix is obvious and cheap; register a fingerprint of the evaluated weights, have the auditor certify the artifact hashes match, and require automated, tamper-evident derivation records linking each production serving artifact back to a registered parent. This is pretty standard compliance stuff, and the same provenance stack the government already requires of its software vendors post-SolarWinds; the records are emitted by build systems automatically, so the marginal burden is effectively zero. A frontier serving pipeline that CANNOT produce artifact provenance is a security finding all by itself. (Bonus coherence check: the bill lets the Director order ad hoc audits to "reproduce or validate" prior findings. You can't reproduce a finding about an artifact you can't identify.)



## Two CAISIs, five times apart

One more thing worth watching. While GAAIA sat in draft, the House Science Committee [reported out](https://science.house.gov/2026/6/full-committee-markup-of-h-r-9341-9363-2385-5351-5584-6461-8893-9333-9334-and-9372) a separate bill, [H.R. 9363](https://www.aip.org/fyi/federal-science-bill-tracker/119th/house-of-representatives-9363), authorizing a CAISI at $20M per year with a hiring cap, focused on measurement and voluntary standards. GAAIA's CAISI is authorized at $100M per year, uncapped, with regulatory duties. Both bills are Obernolte's. 

The 5x funding delta is the difference between a measurement shop and a regulator, stated in dollars, and the open question is whether the smaller bill's enacted text leaves room for the larger mission or forecloses it. H.R. 9363 passed committee 29 to 0 and is likely headed for the suspension calendar, so we'll know soon.


## What we're doing about it

Canary is filing technical comments through the sponsors' feedback channel, and I'm available for briefings to congressional staff on any of the machinery above: what the thresholds capture and miss, and how notice-and-wait regimes have worked in other domains. That availability is the point of writing this up. A 269-page bill will be improved by many hands or by none, and the improving is best done now, while it's still a draft and the ink is cheap.

The sponsors say they released it to hear what's wrong with it. I'm taking them at their word.




## The response so far

[Lawfare has argued](https://www.lawfaremedia.org/article/congress-should-do-something--the-case-for-(fixing)-the-great-american-ai-act) the preemption makes the package net-negative as written. The [House Democratic AI commission opposed it](https://rollcall.com/2026/06/04/bipartisan-ai-draft-proposes-three-year-preemption-of-state-laws/) within hours, saying it "does not meet the enormity of the moment". Worth knowing: the commission is drafting its own framework to hand Leader Jeffries for a hoped-for Democratic majority in 2027, so this is partly a rival product talking. Labor went further (the AFL-CIO and AFT's response was, verbatim, "hard no"), the ACLU and Americans for Responsible Innovation opposed the preemption, and the Alliance for Secure AI's Brendan Steinhauser gave the line I expect to stick: a national standard "should protect at least as much as it preempts". Meanwhile, Majority Leader Scalise says he'll look to Energy and Commerce for AI legislation rather than to Obernolte. Squeezed from both leaderships, the draft is unlikely to move as written this year.

Two things temper my pessimism. The three-year sunset means non-renewal is the default: whichever side likes the deal less in 2029 just lets it lapse, and the renegotiation happens with three years of audit reports and incident data on the table instead of vibes. And even a lapsed GAAIA leaves institutional residue: a funded CAISI, a licensed auditor ecosystem, reporting rails that exist. Regulatory regimes rarely spring fully formed; they accrete. This is what the beginning of one looks like.
