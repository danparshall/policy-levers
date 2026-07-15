# GAAIA as partial mitigation for AI-enabled coup risk — seed note

- Date: 2026-07-14
- Origin: Dan, mid-walkthrough of Title I ("many of the issues we worry about, e.g. coups, could be mitigated by this bill")
- Reference: Davidson, Finnveden, Hadshar (Forethought, April 2025), *AI-Enabled Coups: How a Small Group Could Use AI to Seize Power* — https://www.forethought.org/research/ai-enabled-coups-how-a-small-group-could-use-ai-to-seize-power
- Status: SEED. First-pass mapping by Claude below, not yet vetted against a re-read of the paper. Analysis, not descriptive; hence in this line rather than bills/.

## The observation

The Forethought paper's mitigations chapter reads like a wishlist that GAAIA Title I partially enacts, without ever using the words "coup" or "power concentration." Worth developing because (a) it's a genuinely non-partisan frame for why safety-side actors should want the bill improved-and-passed rather than killed, and (b) the gaps between GAAIA and the paper's mitigation list are themselves a ready-made comment-letter agenda.

## Where GAAIA maps onto the paper's mitigations (first pass)

| Forethought mitigation | GAAIA provision | Fit |
|---|---|---|
| Transparency about internal deployments | § 111(a)(2)(J) framework element on internal-use catastrophic risk, incl. model circumventing an oversight mechanism; § 111(f)(1)(B) CAISI risk-report channel explicitly covers internal + internally-deployed models | Strong — internal deployment is the paper's key blind spot and this bill is unusual in reaching it |
| External scrutiny / audits | § 112 IVO regime: semi-annual, unredacted access to materials/personnel/systems, out-of-cycle reports on emergent capabilities (7-day clock), mandatory referral to DOJ + opted-in state AGs on imminent risk | Strong on paper; depends entirely on IVO ecosystem existing (see under-belly note in OVERVIEW) |
| Whistleblower protection | § 113: any federal AI-law violation, internal reporting protected, contractors + former employees covered, anti-waiver incl. mandatory arbitration, AIR21 burdens, no sunset | Strong — arguably the single best coup-relevant provision; insiders are the paper's primary detection channel for secret loyalties |
| Honest reporting of capabilities | § 111(d) false-statements ban re: catastrophic risk, its management, framework compliance | Moderate — securities-law architecture; enforcement-dependent |
| Weight security / no unilateral exfiltration | § 111(a)(2)(G) weight cybersecurity framework element; § 101(7)(A) weight exfil = critical safety incident w/ 15-day report | Moderate |
| Documenting government pressure on AI systems | § 141 jawboning study + mandated redress recommendations | Ironic fit — the MAGA-coded section doubles as an anti-executive-aggrandizement record-builder. Same provision I flagged as in tension with CAISI safety-pressure; both readings are true |

## Where GAAIA does NOT cover the paper's threat models (the comment-letter agenda)

1. **The harm gate excludes bloodless coups.** § 101(6)(A) catastrophic risk requires foreseeable/material risk of 50+ deaths/serious injuries or $1B+ property damage. "Evading control" is a listed *channel* but still must run through that gate. A successful AI-enabled seizure of power could involve zero deaths and zero property damage. Power concentration per se is not a cognizable harm anywhere in the bill. This is THE structural gap.
2. **Secret loyalties are unaudited.** § 112 audits frameworks and compliance, not model internals. Nothing requires testing for hidden objectives, backdoors, or singular loyalty. Interpretability appears only in § 422 grand-challenge priorities. Paper's "no secret loyalties" mitigation has no GAAIA hook.
3. **The federal carve-out points backwards for state-actor risk.** § 101(6)(B) excludes risks from "lawful activity of the Federal Government." The paper's most dangerous actor is a head of state; the buildup phase of an executive coup is mostly lawful activity until it isn't. GAAIA structurally cannot see the government-misuse channel.
4. **Military AI untouched.** No GAAIA provision reaches autonomous-weapons command loops or singular-loyalty risk in military systems (paper ch. on military coups).
5. **No multi-party control requirements** over weights, deployment decisions, or model specs.
6. **The 3-year sunset** may expire before the risk window opens, and coup-relevant capabilities arriving in year 4+ would find no federal regime and (post-lapse) a preemption-scarred state landscape.

## Next steps (unscheduled)

- Re-read the paper properly and check the mapping against its actual mitigation list rather than memory.
- Decide whether "power concentration as cognizable harm" is a realistic comment-window ask or a next-Congress ask. Possible minimal version: add a fourth channel to § 101(6)(A) or drop the death/damage gate for the evading-control channel specifically.
- Connect to loc-abilities line: the § 101(6)(A)(iii) evading-control channel + § 111(a)(2)(J) oversight-circumvention element are statutory LOC hooks; the capability-taxonomy gap analysis there feeds directly into what an IVO would need to test.
