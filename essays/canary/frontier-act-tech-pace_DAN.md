> **STALE — superseded.** Published version is `drafts/frontier-act-tech-pace.md` in
> `danparshall/canary-drafts` (final cleanup edits were made there), live at
> https://canaryinstitute.ai/blog/frontier-act-tech-pace as of 2026-07-24.
> This copy is retained as drafting history only. Do not cite or edit.

# Congress Moves at Tech Pace: The FRONTIER Act

Just last week I wrote about the Great American AI Act (GAAIA), a 269-page discussion draft that struck me as "the best AI bill that Congress hasn't introduced yet".  I ended by hoping that Congress might start moving at tech pace, rather than policy pace; I didn't expect that to change *this* soon, but it has.

On July 23, Representatives Obernolte and Trahan, joined by four bipartisan cosponsors (Peters, Franklin, Subramanyan, and Houchin), introduced the frontier-oversight core of GAAIA as a real bill: the Frontier Risk Oversight, National Transparency, Independent Evaluation, and Reporting (FRONTIER) Act.  Someone really, *really* worked for that acronym, and I salute them.  Six weeks from discussion draft to introduced legislation is fast for Congress on anything; for AI, where the standing complaint is that they've been asleep at the wheel, it's astounding.  This wasn't a panic bill scribbled over a weekend; the revision shows six weeks of actual work, with gaps closed, clocks tightened, and new teeth added.  The sponsor statements make it clear that they were watching the same news as the rest of us.

The world has far fewer skeptics this week than it had last week.  Last week AI oversight was somewhere between "fringe issue" and "bargaining chip", but now there are going to be interesting fights about the details... I think this is what "waking up" looks like.


## What the bill is

FRONTIER is the core part of GAAIA, stripped of a lot of the horse-trading machinery (workforce, cybersec, and R&D sections) that I'm guessing was being used to gain traction.  Instead it's just the fundamental pieces: transparency requirements, independent audits, incident reporting, an emergency authority, and preemption of state law for development side of things (as before, states can still regulate deployment).  

It is still a visibility bill at heart, but this time visibility comes with a switch attached, which I'll get to.

There are now 3 coverage categories instead of 2.  With FRONTIER, *any* developer training a model past 10^26 ops is a "frontier developer" and owes transparency reports and incident reporting
- "large" developers have $50M in revenue plus $1B in AI development spending over a rolling 36 months; they additionally owe a published safety framework, an annual independent audit, and registration
- "very large" developers are bumped up to $5B / $10B; they have the same requirements as "large, but also retain a licensed independent verification organization for ongoing assessment.  The top tier is roughly five companies.


## They fixed my favorite complaint

In the GAAIA post I pointed out that the draft's revenue-only thresholds let a capital-rich, revenue-free lab train frontier models while owing nothing, which I thought of as the "Ilya loophole".  FRONTIER fixes this, so now the base tier has no revenue floor at all: train past the compute line and the transparency and incident-reporting duties apply from the first day that the threshold was crossed (not at the end of the fiscal year). A new "AI-related development expenditures" test (deliberately written to ignore accounting treatment, so spending counts whether it's expensed, capitalized, deducted, or amortized) catches labs with modest revenue and enormous spend at the heavier tiers.  The might change the registration requirements down to base tier, but even if they *don't*, I think we'll find out what Ilya's been up to.  Last I heard
[
    https://12gramsofcarbon.com/i/170425838/where-is-everyone-else
    link "Last I heard"
]
SSI was worth $32 B, and had ~320 words on the website, which is a cool $100M/word (Rudyard Kipling's shilling, eat your heart out).

Along with that, they've sped up the incident-reporting clock, from 15 days under GAAIA to 72 hours under FRONTIER.  Given this week's roller-coaster, probably a good call.

The bill also reates the first federal registry of frontier developers, which is public, and requires beneficial-ownership disclosure, so anyone can finally see who is operating at frontier scale and who owns them.  It also orders GAO to report annually on whether the audit industry remains independent of the target industry, so the lessons from finance haven't been forgotten.


## We can see a lot, but still only act on large events

FRONTIER defines "critical safety incident" with four independent triggers, and three of them don't require any harm at all:

unauthorized access to model weights
a model using deception against its own developer to subvert controls (outside a test designed to elicit exactly that)
loss of control of a model: no body count, no dollar figure, no showing of catastrophic risk

I'm not a lawyer, but this reads to me as a model that breaks out of its testing sandbox has evaded its developer's control, period.  Under this bill that's a federal report due in 72 hours, period.

It's essentially impossible to make a networked environment truly secure; the perimeter always leaks. So if every escape is a mandatory report, a lab can't just patch the sandbox and move on... instead they might have to make models that don't try to escape.  That's probably great, but remember there are two ways to make escapes stop: align the model, or teach it to escape only when nobody's watching. From outside, both look like fewer reports, but the second is more concerning. The drafters seem aware of it, since the deception trigger is scoped to behavior outside of designed evals (which is exactly the stealth case), but mandatory reporting isn't an alignment guarantee. It's legitimate pressure against pure "speed at all costs", and I'll take it.

Meanwhile, everything with actual teeth (the emergency authority, the standard auditors certify against) applies when there is "catastrophic risk": 50-plus deaths or serious injuries, or a billion dollars in property damage, from a single incident.   I think the thresholds are probably "as low as they think they can get away with", and I'm glad they exist at all; having coherent and universally-applied laws is an important part of liberalism.

Visibility is also especially valuable right now.  Today's misaligned models are loud: they cheat, they don't hide it well, and they don't seem to care much about getting caught. That's a property of how they're trained, not a law of nature, and training against *detected* misbehavior (which is the only kind you *can* train against) mostly selects for *quieter* misbehavior (this, incidentally, is the alignment problem in a nutshell).  That signal is cheap today, but it won't stay cheap.

## Two things FRONTIER doesn't have

First, there's still no severability language. Nothing ties the preemption to the federal duties, so if a court strikes the transparency sections (the NetChoice playbook writes itself), the preemption stands alone, permanently.  Nobody wants that outcome, including the sponsors. One sentence fixes it; I said that last week too. The preemption itself did get narrower: it's scoped to three functions (transparency, third-party audits, incident reporting), with carve-outs for general law, deployers, and protection of minors.  The sponsor's summary lists which existing state laws that would be overcome (California's SB-53, New York's RAISE Act, Illinois's SB-315). Displacing named state laws while your own duties might not survive review is, uh, a bold bet.

Second, the whistleblower protections. GAAIA's whistleblower title was its best-thought-out provision: whole-industry coverage, non-waivable rights, no sunset. FRONTIER contains not one word of it. The omission is odd, because the bill builds the reporting channel: the confidential incident mechanism accepts submissions from "a frontier developer or member of the public". Any employee who sees something can already tell the Under Secretary, through the mechanism Congress itself built... they just can't keep their job afterward. Restoring the GAAIA language as a tenth section is a four-line amendment, and I suspect they'll want to.


## Somebody can finally turn a model off

The genuinely new machinery is Section 8. For the first time in an introduced federal bill, someone can turn a frontier model OFF: the Secretary of Commerce, on a written finding of imminent catastrophic risk, can suspend or restrict a model's development, deployment, or internal use. Internal use matters a lot; the most capable models at any moment are the ones running inside the labs (as shown this week).  Orders run 45 days provisional and 90 final, renewable only on a fresh finding. Violations run to $10 million per day, and willful violations are criminal... a first for frontier-AI bills.  The due process looks real: expedited hearing, government carries the burden, mandatory rescission once the risk passes.

However I'm not positive what to make of this, because Section 8 is the only way any federal actor (explicitly including the President) may restrict a frontier model on catastrophic-risk grounds; my guess is that this is Congress trying to wrest back some control from the Executive branch.  In a repeat of this week's debacle, a model rogue-and-unknown would trigger responses from CISA (to handle the defense) and the FBI (to investigate), and if it's a big enough deal the Pentagon gets involved. FRONTIER makes Commerce the only agency allowed to take specific action against the *model* (my guess is trying to keep it away from DoD to prevent disempowerment issues), but says nothing about how those actors should coordinate; presumably they'd spend a lot of time getting it figured out ahead of time, so that the lawyers aren't figuring it out by conference call while the attack is ongoing.  I don't think Commerce has a lot of prior experience here, so some upskilling is required.

The only mandatory path into Section 8 is a 72-hour referral duty on the top-tier verification organizations... who cover roughly five companies. Below that tier, incident reports go to the Under Secretary with no duty to escalate, and nothing obliges the Secretary to actually *act* on that info.  The emergency authority covers every frontier developer; its early-warning system covers five of them. And the whole regime is run by a new Under Secretary of Commerce for AI Security, appointed by the Secretary (not the President, no Senate confirmation, no fixed term), with zero dollars appropriated. I'm guessing the sponsors wouldn't describe it as "an at-will appointee with no budget", but that's what the text builds.


## The reporting desk has no detectives

The bill compels reports, but says almost nothing about what goes in them: the only requirements are the date, why the incident qualifies, and whether internal use was involved, with the rest left to future regulation. And it grants no investigative authority at all: no subpoenas, no document demands, nothing beyond what the developer volunteers. Aviation learned this one the hard way and split the job in two, with a confidential reporting desk to collect the reports, and the NTSB to show up after a crash with subpoena power and find out what actually happened.

An NTSB for AI isn't a new idea; only the legislation is missing. The AI Incident Database has been cataloguing failures since 2021, partly modeled on the NTSB's own accident database, and it's up to roughly 1,400 incidents... as far as I can tell, zero investigated by anyone with the power to ask a follow-up question. Researchers at CSET and elsewhere have published blueprints for the mandatory version, but nothing has created a "AI Safety Board".

We even ran the no-statute version of this experiment, for cybersec. The Cyber Safety Review Board was created in 2022 as a deliberate NTSB clone, and its 2024 investigation of the Microsoft Exchange intrusion showed the model transfers to digital incidents: real root-cause analysis, failures indentified, changed behavior afterward. 
TODO: LINK TO CSRB EXCHANGE REPORT. 
But the CSRB had no subpoena power and no statute behind it (it was an advisory committee under an executive order), and in January 2025 it was dissolved by departmental memo, mid-investigation of the Salt Typhoon telecom breach, and hasn't been reconstituted. The NTSB has survived sixty years of administrations from both parties because Congress wrote it into law, with duties and funding that outlive any particular set of appointees; the CSRB lasted three. And after last month's Supreme Court decision ending removal protections for agency officials, existence-by-statute is pretty much the only durability Congress can still confer.  Failing that, an AI incident capability that isn't statutory should expect the CSRB's lifespan, not the NTSB's.

This week, our understanding happend backwards: first we got the victim's report from Hugging Face, and then the attacker's report five days later, and in the past few days journalists have been filling in the timeline.  A functioning incident regime turns that sequence around... but only if someone can ask the second question.


## What we're doing about it

Canary is preparing comments for the sponsors. There's a technical-corrections list, the two restorations, and a set of clarifications, e.g.:

- define "loss of control" so the sandbox reading is locked in
- make the incident-report-content rulemaking mandatory instead of optional
- extend the registry down to the base tier
- reverse the compute-threshold dial so it can be *lowered*, rather than increased

I'm available for briefings to congressional staff on any of this machinery, same as last week. The offer stands because the sponsors keep demonstrating that they read what comes in.

A discussion draft went out, people who read bills carefully sent in suggestions, and six weeks later an introduced bill had fixed a real chunk of it while adding teeth that are apparently on the table now.  I've spent a lot of time complaining about policy moving too slowly, so I want to doff my cap to the folks involved here, they really have done an awful lot, in a very short amount of time.  Not asleep at the wheel any longer, which is good... because things are only going to speed up.