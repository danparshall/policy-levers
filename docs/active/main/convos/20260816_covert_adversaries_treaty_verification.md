# Covert Adversaries — Treaty Verification Framing

**Date:** 2026-08-16
**Branch:** main
**Machine:** Dans-MacBook-Air

## Summary

Dan dropped the Aumann–Lindell 2010 J. Crypt. paper *Security Against Covert Adversaries: Efficient Protocols for Realistic Adversaries* (`Aumann_Lindell__Covert_Adversaries__s00145-009-9040-7.pdf`) into the repo root and asked this session to (a) check whether either author has been publishing on AI verification / treaty topics, and (b) sketch the paper's outline. A parallel agent ran the `add-paper` skill against the same PDF, so paper integration (rename to `AumannY_LindellY__2007--security_against_covert_adversaries.pdf`, text extraction, `PAPER_INDEX.md` entry, `PAPER_SUMMARIES.md` writeup) is that agent's commit, not this one's — this session's contribution is analytical only.

The session then extended into two follow-ups from Dan: a clarifying question about whether *this* Aumann is the Aumann Agreement Theorem's Aumann (answer: no — Yonatan Aumann at Bar-Ilan CS, son of Robert Aumann the game theorist / Nobelist; different person, related family), and a substantive modeling walkthrough of how the covert-adversary framework maps onto AI-treaty verification. Handoff at the end: Dan will have a web agent walk him through the paper in detail.

## Topics Explored

- Whether Yehuda Lindell or Yonatan Aumann have published on AI treaty verification / governance in 2023–2026 (checked Lindell's publications page, searched for Yonatan Aumann's recent work).
- Structure of the 63-page Aumann–Lindell paper: three definitional variants of covert security (failed-simulation, explicit-cheat, strong explicit-cheat), OT protocol from homomorphic encryption, general 2PC via cut-and-choose + input splitting on Yao's garbled circuits, composition theorems.
- Simulator-vs-adversary distinction in the ideal/real simulation paradigm (Dan asked directly — this is often blurred).
- Mapping the covert-adversary model onto AI-treaty verification: what plays 𝒜, what plays F_treaty, what plays 𝒮, what "the simulator cheating" means operationally, and how the three definitional variants translate to three regulatory regime designs (soft detection / hard detection with allowed benefit / hard detection with forfeit).

## Provisional Findings

- **Neither author currently publishes directly on AI verification / treaty topics.** Yehuda Lindell's 2023–2024 output is pure crypto (Fischlin's transform, Exponent-VRFs, Feldman VSS for dishonest majority); as Coinbase's Chief Cryptographer his focus is production MPC. Yonatan Aumann at Bar-Ilan's Multi-Agent AI Group works on mechanism design, truthful auctions, coalition games, and (recently) LLMs instructing multiple interacting agents — thematically much closer to treaty verification's game-theoretic structure than Lindell's work, but not on treaties by name.
- **The covert-adversary framing is being re-derived, uncredited, in the current AI-verification-of-treaties literature.** MIRI's Nov 2024 "Mechanisms to Verify International Agreements About AI Development" (arxiv 2506.15867), Baker et al.'s "Verifying International Agreements on AI: Six Layers" (2507.15916), Scher et al.'s "Verification methods for international AI agreements" (2408.16074), and "Hardware-Level Governance of AI Compute" (2604.04712) all frame the threat model as *a state actor willing to spend billions to cheat but sensitive to being caught* — which is the covert-adversary model with a large ε-deterrent. None cite Aumann–Lindell 2010. This is a citation gap worth flagging.
- **Yonatan Aumann ≠ Robert Aumann.** Yonatan (Bar-Ilan CS) is Robert Aumann's son. Different person; the Aumann Agreement Theorem belongs to Robert. Worth knowing for anyone Googling.
- **The covert-adversary framework's definitional insight transfers cleanly to AI-treaty verification; the technical machinery does not, quite.** The clean move — *any cheating attempt is caught with probability ≥ ε, tune ε to social/reputational cost of getting caught* — maps directly. The formal ideal/real simulation apparatus strains at three points: F_treaty (the ideal functionality) isn't well-specified in compute-trace terms; there aren't "honest inputs" in a MPC-shaped sense (treaty verification is unilateral observation, not joint computation); and "cheating = not simulatable" needs relaxation because the verification "protocol" is a heterogeneous mix of attestation + inspections + audits + intel, not a single cryptographic protocol.
- **Strong explicit-cheat definition (§3.5) maps to "detection interrupts payoff" regimes** — escrowed weights, kill-switches on illicit training runs, forfeited compute leases — where getting caught means not just political sanction but that the forbidden artifact wasn't produced. Aumann–Lindell's own line: *"there is less deterrence to not rob a bank if when you are caught you are allowed to keep the stolen money."* Read as a design constraint on treaty apparatus, not just a cryptographic distinction.

## Decisions Made

- No plan doc created — this was research/discussion, not something ready to implement.
- Paper integration is the parallel agent's commit; this session commits only convo + log entries.
- Next-agent handoff: Dan will run a web agent through the paper in detail; this convo doc + the `PAPER_SUMMARIES.md` writeup are the context anchors for that handoff.

## Results

None saved to `results/` this session — the outputs are the analytical text in this convo doc and the framing points above. If the "citation-gap" observation becomes a public writeup, a `results/YYYYMMDD_covert_adversary_treaty_citation_gap.md` would be the place.

## Open Questions

- Has anyone in the crypto community written the formal bridge — a paper defining covert-adversary security for the *unilateral observation* setting that treaty verification actually is? If not, it's a paper-shaped gap, not just a policy-brief-shaped gap.
- Would it be worth reaching out to Yonatan Aumann? His multi-agent + mechanism-design work + the family game-theory pedigree + his father's diplomatic-negotiation applications work suggest he'd have opinions on the modeling question. Lindell is deep in Coinbase execution; probably lower-leverage contact.
- Reframe worth pushing on policymakers: *"confirm they aren't training X"* is impossible; *"make undetected training expected-loss-negative"* is the frame that admits mathematical shape. IAEA doesn't prove nobody's enriching — they make undetected enrichment probabilistically expensive. The covert-adversary framework is the vocabulary for making that shift precise. Whether/how to build this into a talking-points asset is a Dan call.

## Reading Order for the Next Agent

If a downstream agent is walking Dan through the paper:
1. Abstract + §1.2 "Our Work — Covert Adversaries" (pp. 283–286) — the definitional sketch and the two efficiency theorems.
2. §1.3 Related Work (pp. 287–288) — disambiguates from Franklin–Yung t-detectability, Canetti–Ostrovsky "honest-looking," and (importantly) Chandran et al.'s "covert MPC" which is a *different* notion (covert computation, not covert adversarial behavior).
3. §3 (definitional formalism) — the three variants form a strict hierarchy and each has different policy analogs.
4. §6.3 Non-halting detection accuracy — the "cheat by aborting" loophole and how it's closed, which has a very direct treaty analog (adversary can always "abort" a compliant computation, so detection has to survive that).
5. Skim §5 and §6 for the mechanics if the audience is cryptographic; skip if the audience is policy.
