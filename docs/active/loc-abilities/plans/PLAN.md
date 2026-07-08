# Plan: LOC-Relevant Capability Taxonomies vs. General-Intelligence Decomposition

- **Author:** Daniel Parshall, Canary Institute
- **Started:** 2026-07-07
- **Status:** planning
- **Immediate parent use:** MATS Benjamin Chang track essay on AGI/ASI terminology (2026-07 deadline)
- **Estimated write time:** 15-25 hours over ~2 weeks

## Purpose

Map the landscape of capability taxonomies used for loss-of-control (LOC) risk assessment, and compare them to general-intelligence decomposition frameworks (specifically ADeLe / Zhou et al. 2025). Output is a Canary-branded reference document for policy audiences; the immediate use is grounding the MATS essay's argument that "AGI" as a scalar has outlived its policy usefulness.

## Motivation

Two literatures, no bridge.

1. The safety community has multiple partial taxonomies (Shevlane et al. 2023, the three frontier lab RSPs, Bengio 2026 IAISR, Hubinger 2019, Ngo 2022, Carlsmith 2021). None are canonical. IAISR 2026 explicitly notes "no widely accepted taxonomy for capabilities."
2. The general-intelligence-decomposition community (ADeLe, Burnell, Ruan) offers dimensional evaluation but doesn't map onto safety-relevant capability categories. Nobody has done the crosswalk.

That gap is a policy problem: policymakers reading either literature miss the other. The report bridges them and takes a position on which axes need their own dedicated instruments regardless of what ADeLe-style frameworks cover.

## Taxonomies to summarize

Each gets a 200-400 word section: origin, category list, current status, and what it doesn't cover.

**Safety / LOC-relevant:**

- Shevlane et al. 2023 (DeepMind), "Model evaluation for extreme risks." Nine dangerous-capability categories. Predates and largely predicts the lab RSPs.
- Anthropic Responsible Scaling Policy. ASL threshold framework. Verify current version at ship time.
- OpenAI Preparedness Framework. Cybersecurity, CBRN, Persuasion, Model Autonomy.
- Google DeepMind Frontier Safety Framework. Critical Capability Levels across autonomy, biosecurity, cybersecurity, ML R&D.
- Bengio et al. 2025/2026 (International AI Safety Report). Three-way LOC taxonomy: intentional-active, unintentional-active, passive. Multilateral scientific consensus, highest-authority document in the field.
- Shah et al. 2025 (DeepMind), "An Approach to Technical AGI Safety and Security." Explicitly declines to treat LOC as its own category, splits mitigations across misuse/misalignment/structural. Independent convergence with IAISR's decomposition.
- Frontier Model Forum, "Preliminary Taxonomy of Pre-Deployment Frontier AI Safety Evaluations" (Jan 2025). Industry-consensus taxonomy. Contents TBD, need to read.
- METR long-task horizon (Kinniment et al. 2023 and followup). Specific empirical instrument, currently the best proxy for autonomous agency.
- Hubinger et al. 2019, "Risks from Learned Optimization." Foundational theoretical decomposition of mesa-optimization and deceptive-alignment prerequisites.
- Carlsmith 2021, "Is Power-Seeking AI an Existential Risk?" Six necessary conditions for LOC. Not a capability taxonomy per se, but the property decomposition is directly comparable.
- Ngo, Chan, Mindermann 2022, "The Alignment Problem from a Deep Learning Perspective." Names situational awareness as a distinct property.
- Berglund et al. 2023 / Laine et al. 2024. Situational awareness as measurable construct.

**General-intelligence decomposition:**

- Zhou et al. 2025 (ADeLe). 11 primordial + 5 knowledge + 2 extraneous demand rubrics, plus UG as a non-demand extraneous dimension.
- Burnell et al. 2023, "Revealing the structure of language model capabilities." Factor-analytic decomposition.
- Ruan et al. 2024, "Observational Scaling Laws." Related decomposition angle.
- Tolan et al. 2019 (source of ADeLe's primordial dimensions). Human cognitive taxonomy from cognitive-psychology / animal-cognition / AI-domains synthesis.

## Crosswalk approach

For each ADeLe primordial dimension, identify:

1. Which safety-relevant capabilities it directly measures (e.g., MS → theory of mind, directly relevant to deception).
2. Which safety-relevant capabilities it enables but doesn't measure on its own (e.g., QLl → prerequisite for scheming plans).
3. Which safety-relevant capabilities are absent from ADeLe entirely (e.g., persuasion, autonomous horizon, deployment-aware situational awareness, self-proliferation).

Present as a crosswalk matrix. Rows = ADeLe dimensions (including knowledge and extraneous, for completeness). Columns = Shevlane categories + additional LOC-relevant capabilities not in Shevlane. Cells = direct / enabler / absent.

## Output structure

Rough sketch, revisable:

1. Introduction: two literatures, no bridge, why policymakers pay the cost of the gap.
2. LOC-taxonomy landscape (summaries of the safety-side taxonomies).
3. General-intelligence-decomposition landscape (ADeLe and neighbors).
4. Crosswalk matrix + narrative interpretation.
5. Gaps: capabilities absent from both traditions, or covered by one but not the other.
6. Proposal: what a policy-relevant unified taxonomy would need.

Target length: 6-10 pages dense. Not a paper. Reference document.

## Open questions

- Does the report argue for a specific proposal (the essay's capability-profile + autonomous-horizon split), or descriptively map the field? Decide before §6.
- Do we treat propensity/goals as part of the capability taxonomy (Carlsmith's misaligned-goals and power-seeking-incentives categories bundle these), or as orthogonal? The lab RSPs and Shevlane treat capabilities separately from propensities; Hubinger and Carlsmith bundle them. Choice affects the matrix's row structure.
- Scope on cyber and bio uplift: how deep? The RAND biosecurity work and various cyber-eval taxonomies each have their own subtaxonomies. Summary treatment or full inclusion?
- Where does "autonomous replication and adaptation" (ARA) sit? METR treats it as a specific eval, Anthropic RSP as a threshold, Shevlane as "self-proliferation." Same construct, three names. Report should pick one and be consistent.

## Dependencies / TODOs

- Read FMF Jan 2025 taxonomy directly (haven't yet).
- Verify current versions of the three lab RSPs at ship time. All three update frequently.
- Cross-check IAISR 2026 §2.5 for the LOC decomposition graphic and cite exactly.
- Pull Shevlane 2023 for exact category list.
- Confirm METR's most recent horizon-doubling numbers and note whether the trend has held.
- Check whether Anthropic's model welfare and interpretability work overlaps (probably not for this report, but flag).

## Immediate next steps

1. Ingest FMF taxonomy and Shevlane 2023 into `policy-levers/papers/` with the standard naming convention.
2. Draft the crosswalk matrix on paper before writing prose.
3. Circulate the matrix internally at Canary before drafting §5-§6.
4. Loop back to the MATS essay draft once §4 is stable enough to cite.
