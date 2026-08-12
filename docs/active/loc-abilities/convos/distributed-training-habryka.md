# distributed-training-habryka

**Date:** 2026-07-29
**Branch:** loc-abilities
**Surface:** claude.ai

## Summary

Short session. DP was mid-exchange with Oliver Habryka on Twitter, who argued that hardware-level verification is unnecessary because frontier training runs are $10B+ operations in datacenters with a footprint visible from space, already known to intelligence agencies. DP asked to retrieve the distributed-training material from the 2026-07-14 session; the request was a lookup plus a sanity check on whether the retrieved evidence actually rebutted Habryka.

Retrieved Rahman (2026, arXiv 2605.29359) and the 2026-07-14 survey, then worked through where Habryka's argument holds and where it doesn't. The bulk of the session was iterating a two-tweet reply through roughly five drafts.

Nothing new was researched. The one genuinely new analytical item is the tracking-vs-attestation distinction (below), which was not separated in the 7/14 material and probably should have been.

## Topics Explored

- Retrieval of Rahman 2026 + the 7/14 distributed-training survey and its governance-implications section
- Where Habryka's claim survives: frontier runs today are centralised and visible; decentralised proof-of-scale runs remain 1–2 OOM below frontier; a 3x-premium evader is by construction chasing the frontier, never setting it; Heim & Pilz (Transformer, Sep 2025) hold roughly his position in our own library
- Where it doesn't: legal thresholds are fixed FLOP numbers well below "frontier" and get cheaper annually (EU AI Act 10^25 ≈ $31M today per Rahman Table 1); the 10^26 evasion configuration is 4,706 nodes of ≤16 H100-equivalents, which is precisely not a visible $10B facility
- The self-undermining structure of the argument: Rahman rates chip tracking effective and traffic monitoring ineffective, so "we don't need verified chips, we can see the datacenters" bets the regime on the co-location assumption that Decoupled DiLoCo (2604.21428) is engineering away
- Scope objection: Habryka collapses compute governance into covert-run detection, omitting export-control diversion (where chip verification does most of its real work today) and verification of claims by compliant actors (the §112 audited-artifact-provenance thread from `gaaia-analysis`)
- Tweet drafting across ~5 iterations: length constraints, citation formatting, what to cut

## Provisional Findings

- **Tracking and attestation are distinct mechanisms and the 7/14 material conflated them.** *Tracking* is custody — where a unit went, whether the registry matches. That is what Rahman rates effective against threshold evasion and what buys export-control compliance. *Attestation* is proving what executed on the device, which is what buys audit provenance. Tracking alone does not deliver attestation. Habryka's original phrasing ("verified chips") covers both; a reply that says "chip tracking" and then claims audit benefits is answerable.
- Rahman's countermeasure list is broader than chip tracking alone: chip tracking, whistleblower programs, memory-and-compute limits on unregistered hardware, and conventional intelligence work all rated effective. Chip tracking is the strongest of several, not the sole survivor — worth not overclaiming in public.
- Decoupled DiLoCo is a weaker citation than it looks for the covert-run argument, because it is DeepMind coordinating its own multi-datacenter runs — still fully visible to intelligence collection. Its force is as a trend line on the co-location assumption, not as evidence of clandestine capability. The over-the-open-internet citations are Covenant-72B (2603.08163) and Nous Consilience.
- The stronger reframe against Habryka does not depend on distributed training arriving at all: most governance value sits in the compliant case, not the defector case. Satellite imagery cannot establish that the model that was audited is the model that shipped.

## Decisions Made

- Reply shipped as two tweets. Substance: agreement on current runs; DiLoCo trend line; Rahman on traffic monitoring failing and chip tracking being needed; verified chips also buying export-control compliance and audit provenance; closing that this is not the most pressing issue but not the bottom of the list.
- Dropped the explicit "satellite imagery can't do either" clause on DP's call — Habryka will draw the inference unaided, and spelling it out to a fast reader reads as condescension. Held in reserve for the follow-up if he responds.
- Filed under `loc-abilities` rather than a new line, consistent with the 7/14 placement.
- No results file — nothing generated this session that isn't already in the 7/14 survey.

## Open Questions

- **Habryka's likely counter, unresolved:** that auditing is a compliance problem for actors already inside the regime, while his claim was about detecting defectors. He would be half-right. The answer we sketched but did not develop is that most governance value lives in the compliant case *precisely because* the defector case is small and already covered by intelligence work — which inverts his framing rather than conceding the split. Worth developing properly if the exchange continues; it generalises past this thread.
- Does the tracking/attestation split need to be threaded back into the 7/14 survey's governance section, or does it belong in the `gaaia-analysis` §112 provenance material where the attestation half already lives?
- Still open from 7/14: is Robi Rahman DC-local? Unverified. His simulator (`intelligence.org/research/distributed-training-simulator`) could be run under DP's own assumptions before any meeting.
- Still open from 7/14: SparseLoCo compression figures in the survey were cited from memory; verify before external use.
- Still open from 7/14: Krys et al. (2507.07765) not yet ingested to the library.
