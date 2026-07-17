<!--
Canary blog draft: GAAIA analysis summary.  2026-07-17, rev 2.
Claude draft rewritten against dotfiles/VOICE.md + docs/reference/llm-writing-tics.md
(contrast-scaffold cluster thinned 6->2, triads broken, labeled devices cut,
provenance claim corrected to "gone through").  Dan still owns seams.
Crosspost: LessWrong (NB: LW AI-writing policy), BlueDot.
-->

# The Best AI Bill Congress Hasn't Introduced Yet

In June, Representatives Jay Obernolte (R-CA) and Lori Trahan (D-MA) released a [269-page discussion draft](https://trahan.house.gov/uploadedfiles/the_great_american_ai_act_discussion_draft.pdf) called the Great American AI Act, or GAAIA. A discussion draft means the bill hasn't been introduced; it exists to collect feedback before it becomes a real bill, and the sponsors have opened a public inbox for exactly that purpose. Over the past week I've gone through all 269 pages, section by section. It took a while. Most of the coverage so far has focused on a single provision, and the machinery underneath is more interesting than the headline.

My verdict: this is the best-drafted federal AI bill to date. I don't mean it's a good bill, or that it should pass as written; I mean somebody did the work. Most AI legislation is either a messaging document or a grab-bag of studies. GAAIA has real teeth in specific places, its parts are wired together deliberately, and its compromises are legible. You can hate the trade it makes and still respect the drafting.

## What the bill actually is

The provision getting all the attention is the preemption: for three years, states would be barred from enforcing laws that specifically regulate frontier AI development. In exchange, the bill imposes federal transparency requirements on large frontier developers (roughly, labs training models above 10^26 operations with more than $50M in annual revenue): published safety frameworks, incident reporting to a new Center for AI Standards and Innovation (CAISI) at Commerce, semi-annual audits by licensed independent verification organizations, and the strongest whistleblower protections of any provision in the bill. [Lawfare has already argued](https://www.lawfaremedia.org/article/congress-should-do-something--the-case-for-(fixing)-the-great-american-ai-act) that the preemption makes the package net-negative as written; the [House Democratic AI commission opposed it](https://rollcall.com/2026/06/04/bipartisan-ai-draft-proposes-three-year-preemption-of-state-laws/) within hours of release. I'm not going to relitigate that trade here. Canary's comparative advantage is the technical layer, so that's where this post lives.

The right genre label for GAAIA is a visibility bill, not a control bill. Nothing in it gates deployment. If a developer's audit goes badly, the consequence is disclosure and penalties; the release ships anyway. What the bill buys is that the federal government would, for the first time, be entitled to know what frontier developers are doing, with third-party verification and protected insiders. Right now it is entitled to none of that. Whether visibility without control is worth a three-year preemption is the political question, and plenty of people are already fighting about it. Whether the visibility machinery would actually work as drafted is the technical question, and there I found things worth flagging.

## The bug that makes AI fraud cheaper

First, the small stuff, as a taste of what a 269-page draft inevitably contains. Section 131 raises the maximum fine for mail and wire fraud from $1M to $2M, and adds an enhancement clause for fraud "committed with the assistance of artificial intelligence." The AI clause caps at $1M. Read literally, using AI to commit wire fraud LOWERS your maximum fine. The intent is obviously the opposite; the AI clause presumably predates the base-fine change and nobody reconciled them. Elsewhere, a cross-reference points to the definitions section instead of the section it plainly means, and a statutory citation points at an executive order that was rescinded in January 2025. None of this is scandalous. It's what discussion drafts are for, and it's why the sponsors opened an inbox. Canary is compiling a technical corrections annex and will file it there.

## The clause that isn't there

The finding I'd rank highest is about a missing sentence. GAAIA contains no severability clause and no inseverability clause; the words don't appear anywhere in the text. Under default doctrine, courts presume severability, meaning a successful challenge to one part of a bill leaves the rest standing.

Now trace what that does to the core trade. The transparency requirements compel speech from developers, and the compelled-speech playbook that industry ran against state laws in *NetChoice* would be the obvious challenge here. Suppose it succeeds: the transparency and audit sections fall, and the preemption survives alone. Three years of blocked state law, with the federal visibility that justified it struck down in court. The mirror scenario is also live, with the preemption falling and the burdens surviving. Either way, litigation can hand one side of the bargain its winnings while voiding the other side's.

The fix is one sentence: an inseverability provision linking the transparency, audit, and preemption sections, so that if any falls, all fall, and the deal returns to Congress. What I like about this ask is that it cuts the same way no matter which side you're on. If you support the trade, inseverability protects it. If you oppose the preemption, inseverability guarantees it can't survive as a free-floating gift to industry. As far as I can tell from the comments filed publicly, nobody has asked for it.

## Who owes nothing

The frontier duties trigger on compute AND revenue: 10^26 operations and $50M in prior-year annual revenue. The conjunction is the problem. A capital-rich lab with no revenue, and there is at least one prominent lab organized exactly this way, can train frontier models while owing nothing under the transparency and audit sections. Meanwhile the preemption still bars states from touching it. So the bill's most demanding obligations attach to the labs with products and customers, and skip the labs that answer to nobody. If the concern is frontier capability, the trigger should be capability; a disjunct with capital raised or compute expenditure would close the gap.

## Weights, one-way doors, and paperwork due after the fact

Two findings concern open-weight releases and model identity, and they connect to something [I've written about before](https://canaryinstitute.ai/blog/reversibility-of-coma/).

Releasing model weights is a one-way door: once the files are public and mirrored, no injunction claws them back. GAAIA handles this with a report due "before or concurrent with" deployment. Concurrent. The remedial chain for the irreversible act is a late-filing penalty of roughly $1M per day for however few days it takes to paper over, which a frontier lab experiences as a rounding error. The natural fix borrows from antitrust: Hart-Scott-Rodino requires merging parties to notify the government and wait a fixed period before closing, without granting anyone approval authority. The same structure fits here. A notice period for weight release above the compute threshold, on the order of weeks, doesn't restrict anyone's right to release; it means the government sees the pipeline forming rather than reading about it afterward. To be clear about what that buys with finite evaluation capacity: a tripwire and a queue, not a review guarantee. But a tripwire beats a press release.

The second gap is quieter. Nothing in the bill establishes that the model an auditor evaluated is the model actually deployed. The audit regime never cryptographically identifies its own artifact, so its conclusions attach to a rumor. The fix is boring and cheap: register a fingerprint of the evaluated weights, have the auditor certify the artifact hashes match, and require automated, tamper-evident derivation records linking each production serving artifact back to a registered parent. This is the same provenance stack the government already requires of its software vendors post-SolarWinds; the records are emitted by build systems automatically, so the marginal burden rounds to zero. A frontier serving pipeline that CANNOT produce artifact provenance is a security finding all by itself.

## Two CAISIs, five times apart

One more thing worth watching. While GAAIA sat in draft, the House Science Committee [reported out](https://science.house.gov/2026/6/full-committee-markup-of-h-r-9341-9363-2385-5351-5584-6461-8893-9333-9334-and-9372) a separate bill, [H.R. 9363](https://www.aip.org/fyi/federal-science-bill-tracker/119th/house-of-representatives-9363), authorizing a CAISI at $20M per year with a hiring cap, focused on measurement and voluntary standards. GAAIA's CAISI is authorized at $100M per year, uncapped, with regulatory duties. Both bills are Obernolte's. The 5x funding delta is the difference between a measurement shop and a regulator, stated in dollars, and the open question is whether the smaller bill's enacted text leaves room for the larger mission or forecloses it. H.R. 9363 passed committee 29 to 0 and is likely headed for the suspension calendar, so we'll know soon.

## What we're doing about it

Canary is filing technical comments through the sponsors' feedback channel, and I'm available for briefings to congressional staff on any of the machinery above: what the thresholds capture and miss, and how notice-and-wait regimes have worked in other domains. That availability is the point of writing this up. A 269-page bill will be improved by many hands or by none, and the improving is best done now, while it's still a draft and the ink is cheap.

The sponsors say they released it to hear what's wrong with it. I'm taking them at their word.
