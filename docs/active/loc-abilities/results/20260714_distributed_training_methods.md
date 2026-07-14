<!-- Generated during: convos/20260714_distributed_training_survey.md -->

# New methods in distributed training (as of July 2026)

Prepared 2026-07-14. Scope: methods for training LLMs across hardware that is not co-located or not tightly interconnected, plus the demonstration runs that prove them out and the governance-relevant consequences. "Distributed" here means multi-site training by a single coordinating party; "decentralised" means community compute pools without a central coordinator. Krys et al. (arXiv 2507.07765) argue the policy community should keep those terms separate, and the distinction does real work: the methods are shared, the governance implications are not.

## 1. The DiLoCo family: low-communication pretraining goes production

The core move, unchanged since the original DiLoCo paper (Douillard et al. 2023, arXiv 2311.08105), is federated-style two-level optimization: each worker runs an inner optimizer (AdamW) locally for H steps on its own data shard, then workers exchange pseudo-gradients and apply an outer optimizer (Nesterov SGDM). Synchronizing every ~500 steps instead of every step cuts cross-site bandwidth by orders of magnitude. What's new since then is the maturation arc:

- **Scaling laws for DiLoCo** (Charles et al., Mar 2025, arXiv 2503.09799) showed the method scales predictably with model size and, under fixed wall-clock constraints, can match or beat ordinary data-parallel training. This paper moved DiLoCo from "clever trick" to "thing you can budget a frontier run around."
- **Streaming DiLoCo** (Jan 2025, arXiv 2501.18512) synchronizes subsets of parameters on a schedule rather than everything at once, quantizes the exchanged deltas, and overlaps communication with compute. Claimed bandwidth reduction vs. data-parallel: ~2 orders of magnitude beyond base DiLoCo.
- **Eager updates** (Feb 2025, arXiv 2502.12996) further overlap the outer communication with continued inner compute, so workers never idle waiting on the all-reduce.
- **Decoupled DiLoCo** (Apr 2026, arXiv 2604.21428; Douillard through Jeff Dean) is the headline 2026 item. It breaks DiLoCo's remaining lock-step synchrony entirely, moving beyond SPMD: workers proceed asynchronously, coordinated by Pathways, and the system tolerates transient slowdowns and outright hardware failures without stalling the run. DeepMind's framing is goodput maximization for multi-datacenter training; tests with induced failures showed the system isolating bad units, continuing training, and reintegrating recovered units. This is a frontier lab productionizing cross-datacenter pretraining as the default architecture, not a demo.
- **HeLoCo** (May 2026, arXiv 2606.00271) extends the async low-communication approach to heterogeneous data and devices, and its authors explicitly propose composing with Decoupled DiLoCo for larger, more diverse deployments.

The through-line: the constraint that made frontier pretraining a single-building activity (per-step all-reduce over InfiniBand-class fabric) has been engineered away in stages. Bandwidth first (DiLoCo), then latency tolerance (streaming, eager), then synchrony itself (Decoupled).

## 2. Gradient and momentum compression

A parallel thread attacks the size of what gets communicated rather than how often:

- **DeMo / DisTrO** (Nous Research, 2024 onward) decouples momentum across workers and exchanges only the fast-moving frequency components of updates (DCT-based), transmitting just the sign of each amplitude at 1 bit. Nous claims data-transfer reductions of several orders of magnitude vs. all-reduce, sufficient to train over ordinary internet links.
- **SparseLoCo** (Prime Intellect, 2025) combines DiLoCo-style infrequent sync with top-k sparsification plus error feedback and aggressive quantization of the pseudo-gradients, pushing per-sync payloads down another large factor. (Numbers from memory; verify against the paper before quoting.)

Compression composes with the DiLoCo family: infrequent syncs, each of which is itself tiny.

## 3. Proof-of-scale runs in the decentralised (no-central-coordinator) regime

- **INTELLECT-1** (Prime Intellect, Oct 2024): 10B pretrained across three continents; first at that scale.
- **INTELLECT-2** (Apr 2025): 32B trained via globally distributed RL, with verifiable inference (TOPLOC) so untrusted compute contributors can be checked, and two-sided GRPO clipping for stability under staleness.
- **INTELLECT-3** (late 2025): 100B+ Mixture-of-Experts trained on their prime-rl stack, with strong-for-size math/code/reasoning benchmarks. Prime Intellect closed a $130M Series A on July 10, 2026, led by Radical Ventures with NVIDIA Ventures, Intel Capital, and Dell Technologies Capital participating; total funding now exceeds $150M.
- **Nous Psyche** (coordination on Solana): the Consilience 40B pretraining run over ordinary internet bandwidth, ~20T tokens, is the largest internet-distributed pretraining run to date, and Hermes 4.3 (36B) was trained start to finish on the network.
- **Covenant-72B** (arXiv 2603.08163, 2026): 72B pretrained with explicitly trustless peers over the internet, pushing on the adversarial-contributor problem rather than just the bandwidth problem.

Caveat that survives all the press releases: none of these are frontier-competitive models. They are one to two orders of magnitude below frontier training compute, and per-unit-compute efficiency still trails a purpose-built cluster. The trend line matters more than the current position.

## 4. Asynchronous RL: the post-training shift

RL post-training has a structurally different communication profile from pretraining: rollouts are inference-heavy, embarrassingly parallel, and only weights need to flow outward and trajectories back. The 2025-2026 systems literature converged fast on decoupling rollout generation from policy updates:

- **AReaL** (2025, arXiv 2505.24298) fully decouples the two, with staleness-aware PPO objectives; up to 2.77x speedup.
- A wave of successors refines the recipe: ROLL Flash (fine-grained rollout/train decoupling for RLVR and agentic training), AsyncFlow, LlamaRL, PipelineRL, DORA (2026, targeting the skewed-generation problem where one long trajectory blocks the batch), and CoPRIS (concurrency-controlled partial rollouts with importance sampling).
- **NVIDIA ProRL Agent** (Mar 2026) reframes rollouts as a service: agentic environment interaction runs on separate infrastructure from GPU policy updates entirely.
- Algorithmic work addresses the off-policy drift that asynchrony introduces: staleness thresholds, decoupled PPO objectives, variance-controlled off-policy corrections (arXiv 2602.17616), GEPO for heterogeneous/high-latency settings, and "periodic asynchrony" designs that keep strict on-policy correctness by decoupling within an iteration but syncing at iteration boundaries.

The reason this section matters for policy: as the share of total training compute shifts from pretraining to RL post-training, the share that is *easy* to distribute or decentralise grows with it. INTELLECT-2 was possible in 2025 precisely because RL tolerates loose coupling that pretraining historically did not.

## 5. Governance implications

Three items worth reading in full:

- **Krys et al. 2025** (arXiv 2507.07765): the distributed/decentralised taxonomy paper. Flags compute structuring (splitting runs to duck thresholds) and erosion of detectability and shutdownability, while noting genuine benefits (privacy-preserving data access, mitigation of power concentration).
- **Rahman et al. 2026, "Does Distributed Training Undermine Compute Governance?"** (arXiv 2605.29359): simulates whether a Llama-3.1-405B-class model could be trained evasively across distributed hardware. Notes that heterogeneous-hardware methods let evaders supplement tracked new chips with old, unregistered ones, weakening any future compute registry; proposes whistleblower programs (modeled on the Stop Stealing Our Chips Act, Senate-passed as of 2026) as a countermeasure that scales where technical detection doesn't.
- **Heim & Pilz** (via Transformer, Sep 2025): the calibrated skeptic view. For pretraining, decentralisation fears are overstated today because frontier-scale compute is still owned by roughly a dozen entities even when spread across sites, and next-generation runs need an order of magnitude more compute, which is easier to track, not harder. But they concede the RL shift specifically erodes the monitoring assumptions (large single facilities, big fiber buildouts).

One synthesis point, flagged because it cuts against an idea we've used before: the network-fingerprint detection angle (distributed training traffic having a distinguishable signature) is being actively eroded by exactly these methods. DisTrO-style 1-bit compressed exchanges, sub-hourly sync intervals, and rollout-as-a-service RL traffic look progressively less like a classic all-reduce signature and more like ordinary bulk data movement. Detection proposals built on the 2024-era traffic profile need re-validation against the 2026 stack.

## Reference list (primary)

- Douillard et al., Decoupled DiLoCo, arXiv 2604.21428 (Apr 2026)
- Charles et al., Scaling Laws for DiLoCo, arXiv 2503.09799 (Mar 2025)
- Streaming DiLoCo, arXiv 2501.18512 (Jan 2025); Eager Updates, arXiv 2502.12996 (Feb 2025)
- HeLoCo, arXiv 2606.00271 (May 2026)
- AReaL, arXiv 2505.24298 (2025); DORA, arXiv 2604.26256 (2026)
- Covenant-72B, arXiv 2603.08163 (2026)
- Krys et al., arXiv 2507.07765 (Jul 2025); Rahman et al., arXiv 2605.29359 (May 2026)
