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
