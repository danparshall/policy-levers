# 2026-08-16 — Covert adversaries paper walkthrough (web session)

Suggested chat title: "Covert adversaries paper walkthrough"

Follow-on to the local agent's 20260816_covert_adversaries_treaty_verification.md. Reading Aumann & Lindell (J. Cryptology 2010) per its suggested order.

## Covered so far
1. ~1050-word summary delivered (abstract, §1, §3, §6.3). Key structure: ε-deterrent (catch prob ≥ ε·p), detection accuracy as definitional requirement, three variants (failed-simulation / explicit-cheat / strong explicit-cheat), §6.3 non-halting fix via 1-out-of-ℓ OT.
2. Simulation paradigm unpacked. Dan's misparse corrected: ideal world is NOT "everyone honest" — adversary exists there with powers stripped to the unavoidable minimum; simulator = proof artifact running a captive copy of the real adversary. Diagram rendered in chat. Coins (random tapes) and distributions-vs-single-execution explained; §3.1 coin-toss example.
3. Why A-L reject distributional difference as the standard, vs Dan's (correct) point that statistical bounds still cap cheating. Landed formulation: randomness in WHICH items you check, determinism in WHAT a check means. Connected to Cankaya's LW system overview (fetched; not yet in paper library — only arxiv 2606.00279 cited in academic-recruitment log) and its attribution-problem section.
4. Two-layer bound sketched (the "lemma", provenance: Dan's seed claim + Claude's formalization, novelty UNVERIFIED):
   - Layer A (aggregate flow statistic, noise floor θ): salami-proof fails, G ≤ Tθ grows linearly.
   - Layer S (attributable per-item sampling, fraction f, item capacity c): survival e^(−fK), K ≥ B/c; concentration fails if c is small.
   - Combined: G_max ≈ min(Tθ, c/f). Corollaries: granularity c as design lever (answers Cankaya's Question #1; back-of-envelope with his numbers: c/f ≈ 10^20 FLOPs ≪ frontier); per-check FPR ≈ 0 is what bit-exact replay buys (enables large f without drowning attribution); layers must be co-tuned; ALL conditional on coverage of the item universe (chip tracking is the separate fight).
   - IAEA analog: material accountancy (flow, noise floor ~1 SQ/yr at large reprocessing plants) + containment/surveillance (discrete attributable events, seals/cameras).
   - PVC tie-in (already in academic-recruitment log): transferable cheating certificates = strengthened attribution layer for multilateral settings.
5. Advanced-research run suggested to Dan (button offered) for prior art: Dresher 1962; Avenhaus & Canty 1996 (protracted-vs-abrupt diversion likely = salami-vs-concentration already); Avenhaus–von Stengel–Zamir Handbook chapter 2002; IAEA stats literature (Jaech, MUF-D, CUSUM, timely-detection games). Questions: (1) duality as formal result? (2) combined aggregate+attributable game/bound? (3) granularity as design variable? (4) does AI-verification canon cite any of it? Dan expects it's been done; wants underpinnings either way.

## Open threads
- Dangling comprehension check: in strong explicit-cheat ideal world, whose coin decides detected/undetected (trusted party's, not adversary's — v2's fix over v1 is lodging the cheat decision before seeing honest inputs). Dan hasn't answered yet.
- §3 walkthrough proper not yet started; then §6.3 wrinkle in detail.
- Research-run results to fold back here when/if Dan launches it.
- Possible add-paper: Cankaya LW system overview and/or arxiv 2606.00279.
- Style note from Dan mid-session: spell out acronyms on first use (C/S–MA slip).
- Authorship/provenance question for any writeup: parked (cart-before-horse); revisit only if lemma survives prior-art check.
