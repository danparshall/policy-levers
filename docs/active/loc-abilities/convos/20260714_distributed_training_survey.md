# 20260714_distributed_training_survey

**Date:** 2026-07-14
**Branch:** loc-abilities
**Surface:** claude.ai

## Summary

DP requested a survey of new methods in distributed training. Produced a report covering four converging threads: the DiLoCo family's maturation from bandwidth reduction (2023) through scaling laws (2503.09799) to Decoupled DiLoCo (2604.21428, April 2026), which breaks lock-step synchrony entirely and is DeepMind productionizing multi-datacenter pretraining; gradient/momentum compression (Nous DisTrO at 1-bit, SparseLoCo); decentralised proof-of-scale runs (INTELLECT-1/2/3, Nous Consilience 40B at 20T tokens over the internet, Covenant-72B with trustless peers, plus Prime Intellect's $130M Series A on 2026-07-10 as a money signal); and asynchronous RL systems (AReaL, DORA, ProRL Agent), which matter because RL's loose coupling makes post-training the naturally decentralisable phase.

The survey surfaced Rahman (2026, arXiv 2605.29359), "Does Distributed Training Undermine Compute Governance?", which DP had ingested to the main paper library via the paper-processing-academic skill (commit f7a78bd on `main`). Solo-authored by Robi Rahman, now affiliated with MIRI, formerly Epoch AI. DP initially read the affiliation change as a DC-to-SF move; we noted the paper gives affiliation only, MIRI is Berkeley-based with remote staff, so his location is unverified and worth checking directly if a meeting is wanted.

The session's standing correction: the network-fingerprint detection idea from earlier conversations (distributed training traffic having a distinguishable signature) should be treated as undercut by the 2026 stack. Replica divergence, not communication volume, is the binding efficiency penalty in Rahman's model, and 1-bit compressed sub-hourly syncs no longer look like an all-reduce. Rahman rates traffic monitoring and bandwidth caps ineffective as countermeasures; chip tracking and whistleblower programs effective.

## Topics Explored

- DiLoCo lineage: original, scaling laws, Streaming, Eager updates, Decoupled DiLoCo, HeLoCo
- Compression: DeMo/DisTrO, SparseLoCo (numbers flagged for verification)
- Decentralised demonstration runs and their scale gap to frontier (1-2 OOM below)
- Async RL systems wave and its policy significance
- Governance literature: Krys et al. 2507.07765 (distributed vs decentralised taxonomy), Rahman 2605.29359, Heim & Pilz skeptic position (Transformer, Sep 2025)
- Rahman paper deep read: threat model, efficiency decomposition, results table, countermeasures

## Provisional Findings

- Evasion economics per Rahman: Scher 10^24 / EU AI Act 10^25 / SB 53 10^26 thresholds evadable with $1.6M / $31M / $3.8B of sub-monitoring hardware at ~3x cost premium over centralized; latency irrelevant
- Rahman's simulator had to revise its compression default from 16x to 150x after Covenant-72B published, evidence the enforcement gap is outrunning its own modelers
- The share of training compute that is easy to distribute grows as compute shifts from pretraining to RL post-training; Heim & Pilz concede this erodes their "overstated for now" position
- Detection-vs-custody rhyme with MacDonald (2021, 2025): identifying a node does not prove it is part of a training run

## Decisions Made

- Survey filed under loc-abilities (DP's call) rather than a new line; connection is the erosion of detectability/shutdownability assumptions behind capability-threshold governance
- Rahman paper lives in the root library on `main`, not branch-local
- No plan doc; survey session, nothing ready to implement

## Results

- `results/20260714_distributed_training_methods.md` (the survey report)
- Rahman 2026 ingest on `main` (f7a78bd): PDF + text in `papers/`, index row, Protocol A summary in `PAPER_SUMMARIES.md`

## Open Questions

- SparseLoCo compression figures cited from memory in the survey; verify against the paper before external use
- Is Robi Rahman still DC-local? If so, a direct conversation beats correspondence; his simulator (intelligence.org/research/distributed-training-simulator) could be run under DP's own assumptions beforehand
- Krys et al. 2507.07765 not yet ingested to the library; candidate for a future add-paper pass
- Does the LOC/capability-taxonomy work in this line need a detectability axis, given that threshold governance assumes observable training runs?

---

## Addendum (written 2026-10-28; content from 2026-07-14, post-wrap)

The session continued after finish-convo ran. Four items from that continuation were never committed; the 2026-07-29 Habryka session already drew on the first one from chat memory, so they belong in the record.

### Strongest doubt on Rahman 2026: the Charles et al. extrapolation

No published rebuttal existed as of mid-July; the strongest doubt is internal to Rahman's citation chain. His dominant efficiency penalty, replica divergence (η_rep, 0.15–0.90), is calibrated "based on Charles et al. (2025)" (arXiv 2503.09799) — but that paper's empirical envelope is 9 model sizes from 35M to 2.4B parameters (extrapolation tested at 4B/10B) and single-digit replica counts. Rahman's headline configurations need M = 625 (Llama-405B case) and M = 4,706 (10^26 case): a simultaneous ~2-OOM extrapolation in replica count and ~2 more in model size, in his largest and least-anchored penalty term, in the unfavorable direction (Charles et al. measured loss degrading with M at fixed compute; "improves with model size" is a trend fit at small M). If η_rep at M = 625 is 0.05 rather than 0.15, the ~3x premium becomes ~10x and $441M becomes >$1B. The qualitative conclusion (thresholds gameable, input-side countermeasures) survives; the dollar figures should be cited as "even if off by 3–5x, the structure holds." Rahman half-acknowledges this (hardware requirements "increase sharply" at high replica counts; PP groups reduce effective M), and every penalty revision since 2023 has moved in the evader's favor (his own compression default went 16x → 150x after Covenant-72B).

Runners-up: Pilz/Heim/Brown-style significance attack (why spend $441M and two covert years to reach a capability level that open-weight releases hand you free, 1–2 years behind frontier — fails only against evaders who specifically want unmonitored, mitigation-free models); and arXiv 2606.19262 (zero-overhead telemetry detecting hidden training), whose threat model is cloud tenants disguising workloads from providers, not Rahman's own-hardware core case.

### Possible vs. detectable — the clean statement

Charles et al. and Rahman are both pro-feasibility; they differ in role (measurement vs. extrapolation), and the open question is whether the efficiency numbers survive the trip between their scales. On detection Rahman argues the training run is largely *invisible* in transit (traffic shapeable into arbitrary patterns at no performance cost, VPN-routable; traffic monitoring and bandwidth caps rated ineffective), which is why his effective countermeasures all target inputs and people: chip tracking, forensic accounting, memory/compute limits on unregistered hardware, whistleblowers (distributed evasion is more personnel-intensive than centralized — the humans are the attack surface when the packets aren't).

### China and trailing-edge chips

Distributed training does not reduce the total FLOP bill (it raises it ~3x); what it relaxes is co-location and interconnect quality — and China's weaknesses concentrate in exactly those two. Three mechanisms: (1) the interconnect requirement collapses, and interconnect was literally a US export-control parameter (the Oct 2022 rules' bandwidth threshold produced the A800/H800); low-communication training is the algorithmic bypass of that control philosophy. (2) Heterogeneous pooling — Rahman's simulator includes Huawei Ascend 910B/910C pod presets, and he cites Ryabinin 2023 / Douillard 2026 for mixing hardware types — makes China's fragmented fleet (Ascend variants, legacy A100/V100, smuggled H100s in sub-detectable batches) federatable into one effective run; this also undercuts smuggling interdiction's assumption that smuggled chips must concentrate in one detectable cluster to matter. (3) It converts the competition into quantity × energy, China's friendliest framing (trailing-node fab volume, power buildout, cheap electricity) — CloudMatrix 384 was already this bet at rack scale. Brakes: per-chip FLOP/W and FLOP/$ penalties multiply with the distributed premium and overtraining penalty (bearable for a subsidizing state, ruinous otherwise), and for domestic Chinese training the covert framing is irrelevant — it's open engineering, not evasion; evasion bites only under a future verification treaty and in the smuggled-chip dispersal point. Policy punchline: the algorithmic trend converts export controls from a quality game to a volume game; thresholds keyed to chip performance, interconnect, or cluster density age badly, and the durable levers are unit counts, fab capacity, and HBM supply.

### ACX comment (Scott Alexander, "AI Chip Regulation Is Not A Dystopian Surveillance State," 2026-07-15)

Dan drafted a comment correcting the post's decentralized-training paragraph: it defends the wrong margin (phones/laptops rather than sub-threshold clusters of trailing-edge datacenter chips), its latency claim is wrong (DiLoCo syncs every ~30–38 min; transmission dominates RTT), and its "0.1% of frontier scale" is a true snapshot of a closing gap (Sevilla, Scott's own citation: ~20x/yr vs frontier 5x/yr). Framed to support Scott's conclusion while correcting the mechanism: Rahman's finding that run-detection fails and input-side measures work *is* the case for the registry/KYC architecture Plan A proposes. Final text cited SWARM (2301.11913) for heterogeneity rather than the scaling-laws paper. Whether the comment was posted is not recorded here.

### Open questions (addendum)

- Did the ACX comment go up, and did it draw a response worth capturing?
- η_rep at large M remains the live empirical question for Rahman's Table 1; any late-2026 publication measuring DiLoCo-family efficiency at M > 50 would resolve it and should trigger a re-read.
