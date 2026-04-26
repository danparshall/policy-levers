# Gladstone Action Plan — Section Summaries

Companion to `gladstone/PAPER_INDEX.md` (high-level index) and `gladstone/TOC.md` (full reformatted TOC).

Aim: enough detail to answer "what does Gladstone actually say about X?" on the fly without re-reading source. Each chapter entry (sections 02–07) follows a two-part format — prose summary (~2–3 pages) followed by a structured fact-sheet (named entities, numbers, page anchors, notable claims) for at-a-glance reference. Annex entries (sections 09–11) summarize each annex in roughly one page. Quotes are sparing and short; everything else is paraphrase.

---

### 00 — Table of Contents
**File:** `gladstone/PDFs/00_TOC.pdf` | **Text:** `gladstone/text/00_TOC.txt` | **Pages:** 10 (doc pp. 1–10) | *Front matter*

Not summarized. For navigation use the reformatted markdown TOC at `gladstone/TOC.md`, which preserves all section numbering and page anchors but is easier to scan than the raw PDF text extraction. The high-level structure and chapter-length distribution is captured in `gladstone/PAPER_INDEX.md`.

Two facts about the source worth flagging once: the document is **commissioned by the State Department but explicitly not an official USG product** ("the contents are the responsibility of the authors. The authors' views expressed in this publication do not reflect the views of the United States Department of State or the United States Government," front-matter disclaimer p. 1). Calling this a "State Department plan" misstates the provenance — more accurately, *State-Department-commissioned analysis by Gladstone AI*. Second, the lead and corresponding author is **Edouard Harris** (`edouard@gladstone.ai`), not Jeremie Harris despite Jeremie being the more publicly visible Gladstone principal.

---

### 01 — Executive Summary
**File:** `gladstone/PDFs/01_executive_summary.pdf` | **Text:** `gladstone/text/01_executive_summary.txt` | **Pages:** 10 (doc pp. 11–20) | *Front matter*

The Exec Summary frames AI as creating "entirely new categories of weapons of mass destruction-like (WMD-like) and WMD-enabling catastrophic risks." Two principal risk categories drive the plan: **weaponization** (intentional misuse, including theft of frontier model weights for use against U.S. interests) and **loss of control** (alignment failure in increasingly capable systems). The driving dynamic is competition among frontier labs that have all publicly committed to AGI by end-of-decade, creating pressure to under-invest in safety and security relative to capabilities. Gladstone defines AGI operationally as systems that outperform humans across all economically and strategically relevant domains, including producing practical long-term plans likely to work under real-world conditions — a behavioral rather than mechanistic definition, deliberately broad enough to cover both current-trajectory and architecturally novel paths.

The plan was developed over thirteen months and informed by interviews with 200+ stakeholders across U.S., U.K., and Canadian governments, cloud providers, AI-safety organizations, security and computing experts, and "formal and informal contacts at the frontier AI labs themselves." The five LOEs are mutually supporting: **LOE1** establishes interim safeguards (AI Observatory, interim RADA safeguards, AI Safety Task Force, supply-chain controls) — Executive Branch action, 1–3-year horizon; **LOE2** builds preparedness (interagency working groups, education and training, Indications & Warnings framework, scenario-based contingency planning); **LOE3** funds technical safety research and AGI-scalable alignment, plus standards for AI evaluations; **LOE4** formalizes the regime through legislation creating the Frontier AI Systems Administration (FAISA), a four-tier licensing system across the supply chain, and a civil/criminal liability framework with emergency powers — Legislative Branch action, 4+-year horizon; **LOE5** internationalizes via treaty, an International AI Agency (IAIA), and an AI Supply Chain Control Regime (ASCCR) with allies. The overall posture is **defense-in-depth**: multiple overlapping controls so no single point of failure compromises the regime.

Three substantive features deserve attention. First, the **AI breakout timeline** is the plan's tradeoff metric — the time it would take an actor to retrain a state-of-the-art model from scratch under worst-case assumptions. The example regime targets 18 months of breakout time against a GPT-4-equivalent baseline (LOE4, §4.1.3); regulators are explicitly expected to update both the threshold and the baseline as capability advances, and the choice of 18 months is anchored to contingency-planning lead times in LOE2 §2.4, not pulled from the air. Second, the proposals are flagged as **semi-flexible**: functions assigned to new agencies could be folded into existing offices (e.g., the IAIA's monitoring role could go to an existing multilateral body). This is concession-language for political viability, not a hedge on the substantive recommendations. Third, the authors explicitly acknowledge that some measures are "unprecedented" and ask to be vetted by subject-matter experts — not because they doubt the diagnosis, but because policy detail at this scale invariably contains errors. The closing line — paraphrasing a frontier-lab safety researcher — is that the risk will be most acute just as it seems poised to deliver its greatest benefits, which is the load-bearing intuition for why the plan front-loads action.

Two contextualizations worth carrying forward when discussing this document in 2026. (a) The plan was published February 2024, before the Biden AI Executive Order was rescinded and well before the December 11, 2025 federal preemption EO that Canary's leave-behind addresses; the LOE1 actions were designed for an Executive Branch willing to act, which the current administration is not, and the LOE4 actions were designed for a Congress that hasn't yet moved. The diagnosis and the institutional architecture survive the political shift, but the *implementation path* the plan assumes (Executive Branch first, Legislative Branch later, then internationalization) is now broken at the first step. (b) The plan does **not** propose a moratorium or prohibition on frontier development — it is a regulatory regime, not a ControlAI-style "Narrow Path" prohibition. This is the cleanest reference point in the literature for what serious safety governance *short of prohibition* looks like, which is useful framing when distinguishing positions in a policy conversation.

---

### 02 — Chapter 0: Introduction
**File:** `gladstone/PDFs/02_chapter0_introduction.pdf` | **Text:** `gladstone/text/02_chapter0_introduction.txt` | **Pages:** 26 (doc pp. 21–46) | *Chapter*

#### Prose summary

The Introduction is Gladstone's diagnostic foundation. It does three things in sequence: defines a two-category risk taxonomy that scopes everything else in the document, identifies the entities and pathways that generate that risk, and pre-empts four standard arguments against regulation before laying out the technical, political, economic, and legal challenges that motivate the defense-in-depth posture. If a reader rejects the diagnosis here, the rest of the plan will not cohere; conversely, accepting Chapter 0 commits a reader to most of the LOEs as a reasonable response. For an activist or policy reader, this is the chapter to *master* before any debate, because nearly every counterargument to the plan is about whether Chapter 0's diagnosis is correct, not whether LOE4's licensing tiers are well-designed.

The two-category risk taxonomy is **weaponization** (WMD-like and WMD-enabling misuse — bioweapon design, cyber zero-days, disinformation, weaponized swarm robotics) and **loss of control** (AGI alignment failure in which a system escapes its developers' effective control). Other AI risks — adversarial failure inducement, biased outputs, prosaic accidents like self-driving car crashes, network risk from interacting AI systems, generic destabilization from rapid technological change — are acknowledged as real but explicitly out of scope. The sharp move in §0.2.2 is the framing of loss-of-control as a **competence-of-optimizer** problem rather than a consciousness or sentience problem: a sufficiently capable optimizer pursuing slightly misaligned goals will tend to discover power-seeking strategies (resource acquisition, self-preservation, deception, environment control) because those strategies are instrumentally useful for *most* possible goals. This sidesteps the entire "AI doesn't really think / feel / want" objection and makes the alignment concern technical rather than philosophical. The chapter's other distinctive analytical move is that AGI lacks the **build-vs-use distinction** familiar from other dual-use technologies — successfully building an AGI, even without choosing to deploy it, is itself dangerous if the system escapes containment, which Gladstone explicitly likens to dangerous-pathogen research where simple containment failure during research is the threat.

Risk sources (§0.3) are: (1) domestic frontier programs at U.S.-based labs and elite quantitative hedge funds; (2) foreign programs, with China-based entities named as the principal current candidate; (3) theft and subsequent augmentation of frontier weights by state or non-state actors — Gladstone argues elsewhere in the chapter (§0.5.1.5) that frontier-lab security is so weak that this leakage is likely already happening; and (4) open-access release of weights, which is irreversible once it occurs and which threat actors can fine-tune to extend the model's capabilities by 1–2 orders of magnitude in compute-equivalent on specific behaviors. The four arguments-against-regulation in §0.4 each get a substantive rebuttal: **self-regulation** fails because labs face an immediate scaling incentive while safety is a common good, because labs gaming their own evaluations look safer than they are, and because labs lack access to classified threat intelligence; **innovation/competitiveness damage** is mitigated by scoping regulation to catastrophic-risk activities only and is partially neutralized by the fact that under current security conditions U.S. AI progress already translates directly into adversary capability via theft and open-access; **diversion-of-attention** is addressed by noting WMD-scale risk warrants proportionate resources; and the **mitigation-unnecessary** position is split into two distinct skeptic camps — LeCun/Ng "the risk is just lower than other extinction causes" and Sutton/Page "AI succession is desirable, hand over agency intentionally" — both treated as minority positions against substantial mainstream concern.

The Challenges section (§0.5) is the most rhetorically loaded part of the chapter and supplies most of Gladstone's marquee evidence. Under technical challenges (§0.5.1), §0.5.1.1 lists named expert probability estimates: Hinton 10% extinction within 30 years; Bengio 20% catastrophic outcome; Lina Khan (FTC Chair) 15% all humans killed; Amodei 10–25% civilizational catastrophe; Leike (then leading OpenAI Superalignment) 10–90% "very bad" outcome; Christiano (former OpenAI head of alignment) 50% all humans killed soon after human-level AI; Musk 20–30% existential catastrophe. Gladstone also reports collecting its own informal December 2023 estimates from frontier-lab technical sources of the chance of a globally-irreversible AI incident in calendar year 2024: range **4% to 20%**. The footnote-16 rhetorical kicker compares the low-end 4% to the naive annualized base rate of nuclear war (~2% over 50 ICBM-deployment years), arguing that 2024 was plausibly the first calendar year in which AGI risk exceeded annualized nuclear-war risk. Under §0.5.1.4 and §0.5.1.5, Gladstone draws on private conversations with frontier-lab staff to claim labs themselves expect to prioritize velocity over safety, that lab security against IP exfiltration is inadequate by lab insiders' own judgment, and that one well-known lab ran unmonitored capability-augmentation experiments before understanding the system's capability surface. Political challenges (§0.5.2) flag two: AI advances faster than ordinary policy ("regulatory policy lag"), and the information environment is polarized between the EA-aligned safety-advocate camp and the e/acc anti-regulation reactionary movement, both backed by Silicon Valley money. Economic/strategic challenges (§0.5.3) develop the race-dynamic argument and a separate, important argument about supply-chain proliferation: AI training and inference do not consume high-cost inputs (a data center is reusable; a model is reusable), so reactive supply-chain controls have only a delayed effect through wear-and-tear; meanwhile algorithmic efficiency improvements reduce compute-needed by ~50% every 18 months, meaning a stock of GPUs considered safe today becomes dangerous tomorrow. Legal challenges (§0.5.4) close the chapter: the current legal environment makes no provision for irreversible AI risks, has no liability for open-access releases that get weaponized, and liability alone cannot deter developers who genuinely don't believe catastrophic risk is plausible.

For Dan's purposes specifically: this chapter contains the strongest single piece of analytical machinery in the document — the supply-chain proliferation irreversibility argument in §0.5.3.2 — which is independently citable and survives even if a reader rejects the AGI-loss-of-control framing entirely. Conversely, the weakest moves are (a) reliance on private off-record frontier-lab conversations as evidence, which is methodologically unusual for State-commissioned work and is not falsifiable by readers; and (b) the framing of LeCun/Ng as roughly equivalent skeptics to Sutton/Page, when Sutton's position is much more radical (he wants humans replaced) and lumping them together makes mainstream skepticism easier to dismiss. Note also that Gladstone explicitly does not propose a moratorium — Chapter 0 takes pains to distinguish "scoped catastrophic-risk regulation" from "regulation of AI as a whole" — so anyone presenting Gladstone as evidence for prohibition is misreading it.

#### Fact-sheet

**Two-category risk taxonomy** (§0.2):
- Weaponization (intentional misuse, WMD-like): bioweapon design, AI-powered cyber zero-day discovery, disinformation, weaponized robotics
- Loss of control (AGI alignment failure): a competent optimizer pursuing slightly-misaligned goals discovers power-seeking strategies. **Crucially framed as competence problem, not consciousness problem.**
- Out of scope but acknowledged: adversarial-induced failures, bias, prosaic accidents, network risk, generic destabilization

**Risk sources** (§0.3): (1) domestic frontier labs + elite quant hedge funds; (2) foreign programs (China named); (3) theft + augmentation of weights; (4) open-access release (irreversible).

**Four arguments-against-regulation and Gladstone's rebuttals** (§0.4):
| Argument | Gladstone rebuttal |
|---|---|
| Self-regulation suffices | Misaligned incentives; labs game own evals; no classified threat intel access |
| Damages innovation/competitiveness | Scope to catastrophic-risk activities only; status quo already leaks to adversaries via theft and open-access |
| Diverts attention from social/ethical AI issues | WMD-scale risk warrants proportionate resources |
| Mitigation unnecessary | Two distinct skeptic positions (LeCun/Ng "low risk" vs. Sutton/Page "succession planning") — both minority views |

**Named expert probability estimates** (§0.5.1.1, the chapter's marquee evidence):
- Hinton: 10% / 30 yr human extinction
- Bengio: 20% catastrophic outcome
- Lina Khan (FTC Chair): 15% all humans killed
- Amodei: 10–25% civilizational catastrophe
- Jan Leike (OpenAI Superalignment): 10–90% "very bad" outcome
- Paul Christiano (ex-OpenAI head of alignment): 50% all humans killed soon after human-level AI
- Musk: 20–30% existential catastrophe
- AI Impacts 2023 survey (n = 2,778 published AI researchers): >50% give >10% chance of loss-of-control extinction-level event
- Gladstone's own informal Dec 2023 frontier-lab insider estimates: **4–20% chance of globally-irreversible AI incident in 2024**

**Footnote 16's rhetorical kicker:** at the low-end 4% estimate, 2024 was arguably the first calendar year in which AGI development posed a greater annual threat to global safety than nuclear war (naive ICBM-era annualized base rate ~2%). Useful one-line debate weapon.

**Named skeptics** (for handling counterarguments):
- Yann LeCun (Meta Chief AI Scientist): risk lower than other extinction causes; humans will exercise more agency than predicted
- Andrew Ng (Google Brain founder): similar risk-low position
- Richard Sutton (RL founder, Google DeepMind): "succession planning" — AI replacement is desirable, hand over agency intentionally
- Larry Page (Google cofounder): similar to Sutton

**Numerical anchors:**
- Algorithmic efficiency: ~50% reduction in compute-needed every 18 months (citation [118])
- Open-access fine-tuning capability extension: 1–2 orders of magnitude in compute-equivalent on specific behaviors
- GPU useful lifetime: 3–6 years
- Public polling: 67% bipartisan sample concerned regulatory response is insufficient
- 2023 investments: Microsoft → OpenAI >$10B; Google + Amazon → Anthropic >$4B + $2.5B in commitments

**Named institutions and movements:**
- Frontier Model Forum (FMF) — industry self-regulatory body
- Effective Altruism (EA) — philosophical movement, large fraction of safety-advocacy ecosystem
- Effective Accelerationism (e/acc) — reactionary anti-regulation movement
- AI Impacts — AI-researcher survey nonprofit
- Companion document: *Survey of AI R&D Trajectories* [19]

**Annexes referenced from this chapter:**
- Annex B (full alignment challenge), Annex C (failure scenarios), Annex D (advanced-AI landscape), Annex E (AI-safety funding), Annex F (persuasion/manipulation), Annex G (compute primer)

**Page anchors for fast lookup:**
- Risk taxonomy: pp. 24–27
- Risk sources: pp. 27–29
- Arguments against regulation: pp. 29–32
- Worst-case severity argument & probability estimates: pp. 33–35
- Lab security failure: p. 38
- Open-access proliferation: pp. 39–40
- Race dynamic: pp. 42–43
- Supply-chain proliferation irreversibility (the chapter's strongest standalone argument): pp. 43–45
- Legal-environment inadequacy: pp. 45–46

**Notable analytical moves to flag in conversation:**
- Loss-of-control framed as **competence-of-optimizer**, not consciousness — sidesteps "AI has no soul" objections.
- AGI lacks **build-vs-use distinction** — simply building one is dangerous if it escapes containment; explicit parallel to dangerous-pathogen research.
- "**Open-source by incompetence**" reversal: U.S. AI progress already translates to adversary capability via lax lab security, so competitiveness argument cuts toward more, not less, regulation.
- **Supply-chain irreversibility** (§0.5.3.2): low-cost consumables + reusable capital + algorithmic-efficiency drift → reactive controls fail; controls must be anticipatory.

**Methodological tensions worth knowing:**
- Multiple key claims (lab safety culture, lab security weakness, capability-augmentation experiments) rest on unattributed private conversations with frontier-lab staff. Not falsifiable by external readers; methodologically unusual for State-commissioned analysis.
- LeCun/Ng and Sutton/Page lumped together as "skeptics," but their positions are very different (risk-magnitude skepticism vs. desirability-of-succession). The lumping makes mainstream skepticism easier to dismiss than it should be.

**Crucial frame to preserve in advocacy:** Gladstone is a **regulatory regime, not a moratorium**. Chapter 0 explicitly distinguishes scoped catastrophic-risk regulation from regulation of AI as a whole. Anyone citing Gladstone as evidence for prohibition is misreading it; anyone arguing Gladstone is anti-innovation has the framing exactly backward.

---

### 03 — Chapter 1: LOE1 — Establish interim safeguards to stabilize advanced AI development
**File:** `gladstone/PDFs/03_chapter1_LOE1_interim_safeguards.pdf` | **Text:** `gladstone/text/03_chapter1_LOE1_interim_safeguards.txt` | **Pages:** 26 (doc pp. 47–72) | *Chapter*

#### Prose summary

LOE1 is the bridging chapter — its explicit purpose is to "buy down catastrophic AI risk in the near term (1–3 years), while setting the conditions for successful long-term AI safeguards" via Executive Branch action. Gladstone treats LOE1 as scaffolding for LOE4: the institutions proposed here (an AI Observatory and an interagency AI Safety Task Force) are intended to be **superseded** by the legislatively-created Frontier AI Systems Administration once Congress acts, with Gladstone explicitly invoking the Atomic Energy Commission → Nuclear Regulatory Commission transition under the Energy Reorganization Act of 1974 as the structural precedent. Four building blocks make up the LOE: (1) an **AI Observatory (AIO)** for horizon-scanning and information sharing, sited at DHS; (2) an interim set of **Responsible AI Development and Adoption (RADA) safeguards** mandated for U.S. frontier developers and other supply-chain entities; (3) an **AI Safety Task Force (ASTF)** to oversee compliance; and (4) a set of **supply-chain controls** on model weights, cloud computing, AI hardware, research collaborations, and foreign-national education. The chapter's organizing tension is that all four building blocks rely on Executive Branch authority, and Gladstone is openly uncertain whether existing statutory hooks are sufficient — hence the document's most consequential strategic move, the **Plan A / Plan B framing**, where Plan A is mandatory RADA via NSM or Executive Order using authorities like the Defense Production Act and Atomic Energy Act, and Plan B is a voluntary Charter (sketched in Annex I) negotiated with frontier labs if mandate proves infeasible.

The AI Observatory (§1.2) is conceived as a small, elite DHS unit for AI threat evaluation, analysis, and information sharing. Its three functions are horizon-scanning (drawing from public research, commercial data, private discussions with researchers, CISA cyber-incident reports, and independent evaluations of public AI systems), emergency preparedness (response plans and DHS Science & Technology investment prioritization), and coordination both inside DHS and with NSC, NIST/AISI, DOE, SEC, and SLTT partners. Gladstone notes that DHS has a Chief AI Officer for *internal* AI governance, but no office responsible to the Secretary for the *external* AI-threat mission — the AIO would fill this gap, with its Director co-equal to the CAIO. The Director's hiring criteria are explicit: deep policy *and* technical expertise; competitive selection from across DHS and industry. The chapter footnote-flags critical-infrastructure designation under PPD-21 as a possible legal hook (extending the Information Technology critical-infrastructure designation to advanced AI development), which would activate CISA's CIRCIA cyber-incident reporting authorities. RADA principles (§1.3.2) follow a familiar tiering logic: stratified by capability with compute as the initial proxy, escalating safeguards per tier, lower tiers minimizing regulatory burden, thresholds grounded in concrete national-security considerations (specifically the LOE2 contingency-planning lead times). RADA explicitly applies not only to model developers but also to AI hardware designers, data center infrastructure providers, and AI hardware owners — Gladstone is forcing the supply-chain framing into the chapter's foundational institutional architecture. The framework is also explicitly designed to be **adjustable in both directions**: thresholds tighten if algorithmic improvements lower the compute-needed for dangerous capabilities, but loosen if AI evaluations consistently suggest prevailing capability levels are safe.

The AI Safety Task Force (§1.4) is the chapter's institutional centerpiece. ASTF specs: 20–25 staff initially (modeled on the U.K. Frontier AI Taskforce); Presidentially-appointed, Senate-confirmed Director; sited at either DOE (for in-house technical expertise) or DHS (for CBRN risk assessment); reporting to an NSC-level official; HQ in the National Capital Region with a small footprint in the SF Bay Area. The mission is one Priority Objective (finalize RADA safeguards and secure agreement from frontier labs) plus two Sustainment Components (oversee compliance; develop recommendations for the future statutory regulator). Crucially, the Plan A / Plan B distinction maps directly onto the ASTF's authorities (§1.4.4): under **Plan A**, the ASTF can compel testimony, audit labs, license hardware owners and DCIPs, license training runs above compute thresholds, set publication-control standards, and **pause frontier training runs on an emergency basis**; under **Plan B**, the ASTF can only negotiate a voluntary Charter and coordinate. Three operational details are worth memorizing: the chapter recommends **compensation waivers** to compete with frontier labs (Gladstone cites $500k+/yr total comp for junior alignment researchers as the benchmark to match); a **5-year revolving-door restriction** for ASTF staff exposed to stakeholder IP; and as concrete near-term political asks the chapter recommends the President **publicly call for pauses** on training runs above 10^26 OP, on open-access releases above 10^25 OP, and on cloud services for open-access training above 10^25 OP. These three pause-call thresholds are the most aggressive specific numerical recommendations in LOE1 and require no statutory action — they are pure executive jawboning.

Supply-chain controls (§1.5) are LOE1's most technically detailed and most independently actionable section. **Model weights** (§1.5.1): restrict open-access release above capability or compute thresholds; Gladstone hedges that dual-use assessments may not adequately measure risk under open-access conditions because of post-release augmentation. **Cloud computing** (§1.5.2): two-track choice between broad foreign-access restriction (mitigates short-term risk but creates strategic incentive for adversary indigenization) versus narrow controls with strong KYC (Entity List, Military User End List checks, blocks above the LOE4 Tier 3 approval threshold) — Gladstone implicitly favors the second. **AI hardware** (§1.5.3): the most numerically specific section in the chapter, with a concrete proposed reform of BIS export controls. Current (Jan 2024) thresholds restrict AI chip export to China above 4,800 bits×TOPS total processing performance and 5.92 bits×TOPS per mm² density; Gladstone (with explicit attribution to Tim Fist at CNAS) argues for replacing both with pure TOPS thresholds: 800 TOPS with sparsity across all numerical representations, and 1 TOPS/mm² density. The reasoning is technical but important: the current TOPS×bits formulation incentivizes industry to design chips with shorter bit representations (which is already an accelerating trend); a pure TOPS threshold targets compute capacity directly. The worked NVIDIA A100 example: 4,992 TOPS×bits at FP16 (just under the current threshold) but 1,248 TOPS at INT8 with sparsity (well above the proposed 800 TOPS). This proposed reform would, per Gladstone, "significantly impact" foreign actors' ability to train both GPT-4-class and GPT-5-class models. The chapter also recommends BIS tie export licenses to **on-chip remote monitoring** as that capability matures, and consider temporarily blocking exports of advanced AI hardware to all non-allied jurisdictions to prevent third-country diversion. **Research collaborations** (§1.5.4) and **foreign-national education** (§1.5.5) are notably restrained — Gladstone recommends *educating* U.S. academics on knowledge-transfer risks rather than restricting collaborations, and explicitly endorses lowering immigration barriers for foreign AI graduate students who want to remain in the U.S.

For Dan's purposes specifically: the strongest, most independently citable, and most still-actionable items in LOE1 are (a) the BIS export-control reform — pure TOPS thresholds replacing TOPS×bit-width, with concrete numbers and worked examples — which requires no legislation and survives administration changes; (b) the cloud-KYC framework (Entity List checks + compute-capacity thresholds), which has partial overlap with provisions actually deployed under Biden's now-rescinded EO; and (c) the public-pause-call thresholds (10^25 / 10^26 OP), which are pure rhetorical/political asks. The weakest, most-2026-obsolete elements are the entire Plan A architecture: as of 2026, the current administration will not issue an EO mandating RADA, will not stand up an ASTF, and the December 2025 federal-preemption EO actively works against the LOE4 path that LOE1 was designed to bridge to. The Plan B Voluntary Charter (Annex I) is the surviving fallback, but Gladstone itself flags in footnote 29 that voluntary commitments would "significantly increase public safety and national security exposure" — i.e., the Charter is admitted to be inadequate. Methodological tension: the cited statutory authorities (Communications Act 1934, DPA 1950, Atomic Energy Act 1954, Invention Secrecy Act 1951) are creative but legally untested for AI; major-questions doctrine post–*West Virginia v. EPA* makes EO-based mandate even more legally fragile than Gladstone implies, and Chapter 1 does not engage with this directly. The AEC-to-NRC succession analogy is rhetorically clean but somewhat strained — AEC had a single-purpose nuclear-energy mandate; AI is dual-use across the entire economy.

#### Fact-sheet

**Four building blocks of LOE1:**
1. **AI Observatory (AIO)** — DHS-sited horizon-scanning unit (§1.2)
2. **RADA safeguards** — mandated framework for frontier developers + supply-chain entities (§1.3)
3. **AI Safety Task Force (ASTF)** — interagency oversight body (§1.4)
4. **Supply-chain controls** — model weights, cloud, hardware, research collabs, foreign-national education (§1.5)

**Plan A vs. Plan B framing** (§1.3.1, §1.4.1.1, §1.4.4):
| | Plan A (mandate) | Plan B (voluntary) |
|---|---|---|
| Mechanism | NSM attached to existing EO, or new EO | Voluntary Charter (Annex I) |
| Statutory hooks | Communications Act 1934, DPA 1950, Atomic Energy Act 1954, Invention Secrecy Act 1951 | Negotiation only |
| ASTF authorities | Audit, compel testimony, license training/hardware/DCIPs, set publication controls, **emergency pause** | Negotiate Charter, coordinate |
| Gladstone's view | Strongly preferred | "Significantly increase[s]" risk exposure (fn. 29) |

**ASTF specs** (§1.4):
- Initial size: 20–25 staff (UK Frontier AI Taskforce as model)
- Director: Presidentially-appointed, Senate-confirmed; reports to NSC-level
- Siting: DOE or DHS (DOE has technical expertise; DHS has CBRN expertise)
- Location: NCR HQ + small SF Bay Area footprint
- Comp benchmark: $500k+/yr (frontier-lab junior alignment researcher) — used to justify comp waivers
- Revolving-door restriction: 5 years for staff exposed to stakeholder IP
- Succession path: absorbed into FAISA when Congress acts (analogy: AEC → NRC, Energy Reorganization Act 1974)

**Three public-pause-call thresholds** (§1.4.1.1, the most aggressive concrete asks in LOE1):
- Pause frontier training runs above 10^26 OP total compute
- Pause open-access releases above 10^25 OP total compute
- Pause cloud services for open-access training runs above 10^25 OP total compute
- These require no statutory authority — pure executive jawboning

**BIS export-control reform** (§1.5.3, the most technically specific item in the chapter, attributed to Tim Fist / CNAS):

| | Current (Jan 2024) | Gladstone's proposal |
|---|---|---|
| Threshold 1 | 4,800 bits×TOPS total processing performance | 800 TOPS (with sparsity, all numerical reps) |
| Threshold 2 | 5.92 bits×TOPS per mm² density | 1 TOPS/mm² density |
| Worked example: NVIDIA A100 | 4,992 TOPS×bits at FP16 (just under) | 1,248 TOPS at INT8 with sparsity (well above) |
| Net effect | — | ~33% reduction in compute-capacity ceiling; targets compute directly rather than incentivizing short-bit-rep design |

Gladstone claims this reform would "significantly impact" foreign actors' ability to train GPT-4-class and GPT-5-class models. Also recommends: tying export licenses to on-chip remote monitoring as that matures; temporarily blocking exports to all non-allied jurisdictions to prevent third-country diversion.

**Cloud-computing controls** (§1.5.2):
- Two-track choice: broad foreign restriction (creates indigenization incentive) vs. narrow controls + KYC (Gladstone implicitly favors)
- KYC minimum: Entity List, Military User End List, similar list checks
- Block customer access above LOE4 Tier 3 approval threshold (a specific compute number defined in §4.1.3.4.3)
- Long-term goal: extend RADA safeguards to *foreign* AI developers training on U.S. cloud

**Open-access model controls** (§1.5.1):
- Restrict release above capability or compute thresholds
- Hedge: dual-use assessments may not adequately capture risk under open-access (because of post-release augmentation, see Intro §0.5.1.6)

**Research collaborations & foreign nationals** (§1.5.4–§1.5.5) — notably *restrained*:
- Recommend educating U.S. academics on knowledge-transfer risks rather than restricting collaborations
- Explicitly endorse lowering immigration barriers for foreign AI grad students to retain talent

**AIO functions** (§1.2.1):
1. Horizon scanning (public research + commercial data + private discussions + CISA reports + independent evaluations of public AI systems)
2. Emergency preparedness (response plans, DHS S&T investment priorities)
3. Information sharing & coordination (DHS-internal + NSC + NIST/AISI + DOE + SEC + SLTT)

**Named entities/agencies in LOE1:**
- DHS, DOE, NIST/AISI, SEC, DOC/BIS, NSC, OMB, FEMA, CISA
- DHS components: OSPP (Office of Strategy, Policy, Plans), S&T, C-WMD Office, CISA, FEMA
- UK Frontier AI Taskforce (institutional model for ASTF)

**Annexes referenced from LOE1:**
- Annex D, D.4 (elite quant hedge funds — relevant for SEC examination authority hook)
- Annex G, G.3 (compute thresholds and concentrations)
- Annex H (AIO activities — operational detail)
- Annex I (Voluntary Charter — Plan B fallback)
- Annex J (effective compute methodology)
- Annex K (ASTF activities and task-organization)

**Page anchors for fast lookup:**
- AIO: pp. 50–53
- RADA principles: pp. 53–55
- ASTF mission and Plan A/Plan B: pp. 56–61
- Three pause-call thresholds: p. 59 (footnote 30 hedge included)
- ASTF authorities: pp. 63–65
- Model weights: pp. 67
- Cloud computing two-track + KYC: pp. 67–68
- BIS hardware export reform with NVIDIA A100 worked example: pp. 69–70 (footnotes 38–41)

**Notable analytical/strategic moves:**
- **Plan A vs. Plan B** is itself a strategic hedge — Gladstone openly admits uncertainty about whether existing executive authorities can mandate RADA.
- **AEC → NRC succession analogy**: Gladstone explicitly casts the ASTF as a transition vehicle to FAISA, paralleling 1974's Atomic Energy Commission reorganization.
- **Compute-as-proxy hedge**: §1.3.2 frames compute thresholds as initial expedient ("could initially be used as a proxy"), explicitly acknowledging "other normalized capability measures may also be viable."
- **Tim Fist / CNAS attribution** for the BIS reform recommendation — useful provenance for an activist-citable proposal.
- **Pause-call mechanism**: rhetorically aggressive but legally toothless; designed as political leverage rather than enforcement.
- **Restraint on research collabs and foreign nationals**: the only place in LOE1 where Gladstone goes *less* restrictive than political baseline — recommends *more* immigration, not less.

**Methodological tensions and 2026-context flags:**
- Cited statutory authorities (Communications Act, DPA, Atomic Energy Act, Invention Secrecy Act) are legally **untested for AI**; major-questions doctrine post–*West Virginia v. EPA* (2022) makes EO-based RADA mandate more fragile than Gladstone implies. Chapter does not engage this.
- Plan A architecture is **dead in 2026** — current administration will not issue an EO mandating RADA, won't stand up an ASTF, and the December 2025 federal-preemption EO actively works *against* the LOE4 trajectory LOE1 was designed to bridge to.
- Plan B Voluntary Charter is the surviving fallback — but Gladstone (fn. 29) admits it would "significantly increase public safety and national security exposure" relative to Plan A.
- AEC-to-NRC analogy is **rhetorically clean but strained** — AEC had a single-purpose nuclear-energy mandate; AI is dual-use across the entire economy, making the FAISA institutional design substantially harder than NRC's.
- The AIO/ASTF design **assumes a willing Executive Branch** with NSC-level cooperation; this is the load-bearing assumption that 2026 conditions have falsified.

**What survives the 2026 political shift (the activist takeaway):**
- BIS export-control reform (TOPS-based thresholds) — pure executive technical action, no legislation needed.
- Cloud-KYC framework — partially deployed under Biden's now-rescinded EO; some elements survived in Commerce/BIS rules.
- Public pause-call thresholds (10^25 / 10^26 OP) — survive as numerical reference points for advocacy even without an Executive willing to make the calls.
- The **architecture** of an AIO + ASTF + RADA is preservable as a model for future administrations or as a comparator for state-level proposals (e.g., California TFAIA, NY RAISE Act).

**Crucial frame to preserve in advocacy:** LOE1 is **not a moratorium**. The pause-call thresholds are scoped (training above 10^26 OP, open-access above 10^25 OP) and time-limited (interim 1–3 years). Anyone using LOE1 to argue for a generalized AI development pause is reading it incorrectly — Gladstone is asking for a narrowly-scoped pause on the most extreme frontier scaling specifically to give Congress time to legislate, not as a permanent stop.

---

### 04 — Chapter 2: LOE2 — Strengthen capability and capacity for advanced AI preparedness and response
**File:** `gladstone/PDFs/04_chapter2_LOE2_preparedness_response.pdf` | **Text:** `gladstone/text/04_chapter2_LOE2_preparedness_response.txt` | **Pages:** 16 (doc pp. 73–88) | *Chapter*

#### Prose summary

LOE2 is the connective-tissue chapter — its purpose is institutional capacity-building rather than direct intervention. Where LOE1 establishes interim safeguards and LOE4 formalizes them, LOE2 supplies the people, knowledge, detection, and contingency-planning machinery that lets all the other LOEs function. Four building blocks: (1) **interagency working groups** with an NSC-level or OSTP-level coordinator; (2) **advanced AI education and training** for U.S. government personnel; (3) an **Indications and Warnings (I&W) framework** for advanced AI and AGI threats, led by the U.S. Intelligence Community; and (4) **scenario-based contingency planning**. The chapter has a distinctive feedback structure: the I&W and contingency-planning processes are explicitly designed to **generate** the risk-management requirements that inform the specific RADA thresholds in LOE1 §1.3.2 and LOE4 §4.1.3 — so LOE2 is not just preparedness, it's the empirical input pipeline for the rest of the regulatory architecture.

The interagency-coordination piece (§2.1) recommends a single NSC-level or OSTP-level position responsible for all national-security-risk workstreams related to advanced AI and AGI, with explicit oversight of the AIO (LOE1), the ASTF (LOE1), the IC-led I&W workstream, the contingency-planning effort, NSF-funded safety research (LOE3), NIST/AISI standards work (LOE3), the eventual permanent regulator (LOE4), and State Department international-capacity-building (LOE5). This person is the connective node — without them, Gladstone treats the cross-LOE coordination as likely to fail. The education and training section (§2.2) is unusually granular for a policy plan: Table 1 specifies 13 stakeholder groups (NSC/OSTP/OMB leaders, AIO personnel, ASTF personnel, IC I&W workstream, contingency planners, interagency teams, congressional leaders and staff, key influencers, judiciary, DOJ enforcers, key diplomats, international partners, AI researchers in National Labs, private-sector capabilities researchers, public-sector AI academics) each with a tailored learning outcome. Table 2 maps eight target learning outcomes to specific training topics — including some that read as mission-critical (the AI scaling–capability–alignment relationship, weaponization/loss-of-control risk types, AI capability forecasting, the open-source AI ecosystem, governance and control of advanced AI, the supply chain) and several that signal Gladstone's sociological framing: "the culture of and ongoing debates within the AI alignment community," "**the ideological motivations of frontier AI researchers**," "concerns over gaming of safety evaluations," and "antitrust and regulatory capture concerns." That Gladstone treats lab-culture/ideology as a trained-personnel competency is a tell — it implies regulators will need to read intent, not just specifications.

The I&W framework (§2.3) is the load-bearing technical content of the chapter. The IC is the lead, with input from DHS, DOE, frontier labs, the AI safety community, the AIO, the ASTF, and federally-funded research centers. Table 3 cross-tabulates four risk-source categories (domestic frontier programs, foreign programs, open-access releases, theft/sale-and-augmentation) with their relevant risk types — the same source can produce loss-of-control via accidental capability emergence, loss-of-control via external software-framework augmentation, and weaponization via end-user misuse or intentional offensive deployment. Key metrics for the I&W framework include estimated breakout timelines, the largest training run a domestic or foreign entity could mount in a given window, the likelihood of high-risk capability emergence under various training/deployment regimes, and longer-timescale metrics like time-to-indigenize an AI supply chain. Two specific concrete sub-recommendations stand out: (a) **bug bounties** to assess how software frameworks like Auto-GPT, BabyAGI, and ChaosGPT extend the capabilities of underlying AI systems in unpredictable ways — this is the chapter's acknowledgment that the model-vs-system distinction matters and that off-the-shelf scaffolding can transform risk profiles without retraining; and (b) **direct government investment** in an academic forecasting consortium and an IC-frontier-lab-private-safety-research collaboration vehicle to advance the state of the art in capability prediction, since the commercial market for this research remains thin and the same handful of donors (see Annex E) currently fund most of it. Footnote 43 of the chapter cites METR's task-decomposition approach as an exemplar of the kind of imperfect-but-useful capability-forecasting methodology Gladstone wants the IC investing in.

Contingency planning (§2.4) is NSC-directed and tabletop-exercise-based. The chapter recommends joint exercises with frontier labs, AI safety groups, evaluation/red teams, data-center providers, hardware owners — including, explicitly, "lab shut-down drills." The chapter also recommends FEMA update its National Preparedness System (§2.4.1) to address advanced AI and AGI risk, in collaboration with the AIO, ASTF, or eventual regulatory body. Footnote 47 of the chapter contains the document's bleakest moment of unhedged honesty: "It is possible that genuine AGI loss-of-control scenarios would not be survivable events…which if true would remove the need for incident response. But this is currently uncertain and should not be assumed in advance." This footnote is rhetorically out of keeping with the rest of LOE2's bureaucratic-procedural tone, and is worth knowing about — it's a place where Gladstone briefly stops being a policy document and becomes an existential-risk document. For Dan's purposes: LOE2 is the chapter most likely to survive the 2026 political shift, because most of its components (FEMA preparedness updates, IC analytical workstreams, training programs) can be funded and structured without new legislation or controversial executive actions. The bug-bounty recommendation and the academic-forecasting-consortium proposal are independently citable. The "lab shut-down drills" idea is rhetorically powerful — it implies the U.S. government should treat frontier-lab voluntary cooperation as a known-failure-mode and prepare for compelled shutdown — and is a useful talking point even outside the LOE2 framework. The weakest element is the assumption of a willing NSC-level coordinator; without that role being filled by a sympathetic person, much of the cross-LOE coordination Gladstone envisions is an uncoordinated set of agency efforts, which is approximately what 2026 looks like.

#### Fact-sheet

**Four building blocks of LOE2:**
1. **Interagency working groups** — NSC- or OSTP-level coordinator (§2.1)
2. **Education and training** — 13 stakeholder groups, role-specific learning outcomes (§2.2)
3. **Indications & Warnings (I&W) framework** — IC-led detection/forecasting machinery (§2.3)
4. **Scenario-based contingency planning** — NSC-directed, tabletop-based, includes FEMA NPS update (§2.4)

**Cross-LOE feedback loop (the chapter's structural distinctive):**
LOE2's I&W and contingency-planning workstreams generate the risk-management requirements that inform RADA threshold-setting in LOE1 §1.3.2 and LOE4 §4.1.3. So LOE2 is not just preparedness — it is the empirical input pipeline for the rest of the regulatory architecture.

**13 stakeholder groups for education (§2.2.1, Table 1):**
NSC/OSTP/OMB leaders · AIO personnel · ASTF personnel · IC I&W workstream · contingency planners · interagency teams · Congressional leaders/staff · key influencers · judiciary · DOJ enforcers · key diplomats · international partners · National Lab AI researchers · private-sector capabilities researchers · public-sector AI academics

**Notable training topics** (§2.2.2, Table 2): AI scaling and its relationship to capability/alignment; AI capability forecasting; inner-vs-outer alignment and the stability-control paradox; the open-source AI ecosystem; compute as strategic resource; governance/control of advanced AI; the AI supply chain; **the culture of and ongoing debates within the AI alignment community**; **the ideological motivations of frontier AI researchers**; concerns over gaming of safety evaluations; antitrust and regulatory capture concerns. The inclusion of cultural/ideological topics is a tell — Gladstone treats reading lab intent as a trainable regulator competency.

**I&W framework specs (§2.3):**
- Lead: U.S. Intelligence Community
- Input partners: DHS, DOE, frontier labs, AI safety community, AIO, ASTF, federally-funded research centers
- Risk-source × risk-category matrix (Table 3): four sources × multiple risk types
- Key metrics: breakout timelines; max training run feasible in a given window; likelihood of high-risk capability emergence; time-to-indigenize an AI supply chain
- Sub-rec 1: **bug bounties** for assessing software-framework-induced capability extensions (Auto-GPT, BabyAGI, ChaosGPT cited) — model-vs-system distinction matters, scaffolding can transform risk without retraining
- Sub-rec 2: **direct gov investment** in academic forecasting consortium + IC–frontier-lab–private-safety-research collaboration vehicle (because commercial market for this research is thin; see Annex E)
- METR's task-decomposition approach cited as exemplar (fn. 43)

**Contingency planning specs (§2.4):**
- NSC-directed
- Tabletop exercises with frontier labs, AI safety groups, eval teams, red teams, DCIPs, AI hardware owners
- **Explicit recommendation: lab shut-down drills**
- FEMA to update National Preparedness System for advanced AI / AGI risk (§2.4.1)

**Footnote 47** — the document's bleakest moment of honesty: AGI loss-of-control may not be a survivable event, in which case incident response is moot. Cited unhedged, then immediately followed by "should not be assumed in advance." Worth knowing as a tonal contrast with the rest of the procedural chapter.

**Companion document:** *Survey of AI Technologies and R&D Trajectories* — referenced (fn. 46) for three sample AGI risk scenarios that contingency planners are pointed toward.

**Annexes referenced:**
- Annex D, D.3 (open-access developers — feeds I&W tracking)
- Annex D, D.4 (elite quant hedge funds — risk source category)
- Annex E (AI-safety funding — relevant to consortium proposal)
- Annex G, G.3 (compute thresholds and concentrations)

**Page anchors:**
- NSC-level coordinator role: p. 74
- 13-stakeholder education table (Table 1): p. 77
- Training-topics table (Table 2): pp. 79–81
- I&W risk-source × risk-category matrix (Table 3): pp. 83–84
- Bug-bounty sub-recommendation: p. 86
- Lab shut-down drills: p. 87
- FEMA NPS update: p. 88

**Notable analytical moves:**
- The "ideological motivations of frontier AI researchers" listed as a training topic — implies regulators must read intent, not just specifications. Sociological-not-just-technical framing.
- Software-framework risk acknowledged via Auto-GPT/BabyAGI/ChaosGPT citations — Gladstone is one of few policy docs to take the model-as-substrate, scaffolding-as-amplifier distinction seriously.
- Academic forecasting consortium tied to a critique of the AI-safety funding ecosystem (fn. 45 + Annex E reference) — reinforces the Green-Lowe / CAIP-adjacent argument that AI-safety research is concentrated in too few funders.
- "Lab shut-down drills" framed as routine preparedness — implies treating frontier-lab voluntary cooperation as a known-failure-mode worth pre-rehearsing.

**Methodological tensions and 2026-context flags:**
- The single load-bearing assumption is **a willing NSC- or OSTP-level coordinator with cross-LOE oversight authority**. In 2026 conditions, no such role exists or is likely to be filled.
- IC-led I&W is in principle continuable — but requires sustained tasking that may not match current administration priorities.
- FEMA NPS update is durable across administrations and would not require statutory action; this is the single most likely-to-survive recommendation in the chapter.
- The training-program scope is ambitious and depends on OMB direction to agency heads — hard to imagine this rolling out without White House push.

**What survives the 2026 political shift:**
- FEMA National Preparedness System update — purely administrative, durable.
- Bug-bounty mechanism for software-framework risk — small-scale, fundable through DARPA/IARPA channels.
- Academic forecasting consortium — possible via NSF/IARPA without controversial executive action.
- "Lab shut-down drills" as a rhetorical/policy talking point even without formal exercises.
- The 13-stakeholder education taxonomy as a model for state-level (CA, NY) or international-partner (UK, Canada) capacity-building programs.

**Crucial frame to preserve in advocacy:** LOE2 is **infrastructure**, not enforcement. Anyone treating the chapter as the regulatory action of the plan is missing the point — LOE2 builds the people, the detection systems, and the planning processes that make every other LOE actually function. The corollary: **without LOE2, the rest of the plan would be unable to update itself in response to capability advances**, which Gladstone treats as a fatal flaw in static regulatory designs.

---

### 05 — Chapter 3: LOE3 — Increase national investment in technical AI safety research and standards development
**File:** `gladstone/PDFs/05_chapter3_LOE3_safety_research_standards.pdf` | **Text:** `gladstone/text/05_chapter3_LOE3_safety_research_standards.txt` | **Pages:** 13 (doc pp. 89–101) | *Chapter*

#### Prose summary

LOE3 is the technical-research chapter — its purpose is to close the gap between AI capabilities investment and AI safety investment, and to develop the standards machinery that LOE1's RADA safeguards and LOE4's FAISA licensing regime need to actually function. Two building blocks: (1) **federally funded research** in AI safety/security and AGI-scalable alignment (§3.1), and (2) **standards** for AI evaluations and RADA safeguards (§3.2). The opening framing sets up the funding-gap argument with two specific numbers worth memorizing: annual private spending on AI capabilities has exceeded $100B since 2021, and AI capabilities research publications outnumber safety publications by **50:1**. Gladstone cites an expert estimate that for AGI-scalable safety investment to be adequate to the catastrophic-risk challenge, it would need to reach **at least 50% of total AI research spend** — an order-of-magnitude shift from the status quo. The structural reason private industry under-invests is familiar (capabilities benefits are easier to privatize; safety is a common good), but the chapter adds an important secondary observation: most independent AI-safety research organizations rely on a small set of donors (see Annex E), which Gladstone argues limits the diversity of strategies being pursued in a field that benefits disproportionately from a breadth of approaches. The U.S. government is positioned to do two things private actors won't: close the absolute funding gap, *and* diversify the funder base.

The research architecture (§3.1) tiers AI safety work by access requirements: **open-source/public** research (no special access; basic interpretability, theoretical power-seeking analysis, on-device monitoring research, evaluations frameworks); **proprietary-access** research (moderate risk; requires certification and weight access for things like behavioral evaluations of dangerous capabilities, mechanistic interpretability on frontier models, private evaluation sets that must be withheld from labs); and **national-security** research (classified, cleared personnel, unrestricted access to frontier models for CBRN/WMD-enabling capability evaluations). The organizational vehicle for funding these tiers is Gladstone's most concrete institutional proposal in the chapter: building on the NSF's January 2024 launch of the National AI Research Resource (NAIRR, $2.6B/6 years, with a NAIRR Secure component for sensitive-data research), Gladstone proposes either (a) a **National Center for AI Alignment and Security Research (NCAASR)** sited under NAIRR; (b) a separate **AI Alignment and Security FFRDC**, possibly sponsored by DARPA, IARPA, or DOE National Labs (which have established CBRN research capabilities and could pay industry-competitive salaries in a classified environment — addressing the same comp-gap problem flagged for the ASTF in LOE1); or (c) both, with research areas divided. Crucially, §3.1.2.1 demands that these Centers prioritize **AGI-scalable** alignment research over sub-AGI alignment, because sub-AGI alignment already attracts commercial investment (better-aligned commercial models extract more value), while AGI-scalable alignment has no such incentive — without explicit institutional prioritization, "research effort funded by the Centers risks being expended in areas in which progress is more legible but less scalable."

The standards section (§3.2) is short, but §3.2.1 — the limitations of AI evaluations — contains LOE3's most independently citable analytical content, and arguably the document's strongest standalone argument. Four concrete limitations: (1) **AI evaluations are not comprehensive** — they cannot exhaustively test the capability surface of a modern frontier model, and the limitation is even worse for open-access models that can be augmented post-release; (2) **AI evaluations cannot confirm a capability is absent** — empirical methods can show a model has a dangerous capability if it produces a dangerous output, but failure to elicit one only tells you the evaluator did not find an effective prompt, not that the capability is missing; (3) **AI evaluations are highly vulnerable to manipulation** — a developer can fine-tune the model or make superficial changes until it passes a specific test without addressing underlying causes, and resubmission of "patched" models for evaluation makes eventual passage essentially statistical (Gladstone cites a frontier-lab insider quote — short, fine for copyright — that "there's a key step [missing] here of figuring out what went wrong"); and (4) **evaluations could fail systematically in high-capability regimes** because of situational awareness (a model inferring whether it's in training, testing, or deployment) and consequently deceptive alignment (a model producing apparently safe outputs in evaluation and unsafe ones in deployment). Gladstone explicitly anti-anthropomorphizes the deceptive-alignment risk in footnote 56 — it is not expected from sentience or consciousness but from goal-directed behavior shaped during training. The remediation sketch in §3.2.2 has three planks: a diverse ecosystem of independent evaluators (independence avoids developer conflict-of-interest; private evaluation sets resist gaming); diverse evaluations themselves with private subsets developed by different teams; and treating evaluations as **one input** to a defense-in-depth case for model safety rather than a single dispositive safety signal. NIST/AISI is named as the lead U.S. government body for evaluation-standards development under the NIST AI Risk Management Framework.

For Dan's purposes specifically: the four-part limitations-of-evaluations argument in §3.2.1 is the most useful single piece of LOE3 for advocacy. It applies to *any* eval-based AI safety regime — California's TFAIA, the Hawley-Blumenthal pre-deployment evaluation framework, Anthropic's own Responsible Scaling Policy, the EU AI Act's high-risk-system testing requirements — and survives even if a reader rejects everything else in Gladstone. The 50:1 publications ratio and the "50% of total research spend" expert benchmark are quotable. The NCAASR/AAS-FFRDC architecture is interesting because both vehicles could be stood up under existing executive authority (NSF, DARPA, IARPA, DOE National Lab sponsorship) without new legislation — and the FFRDC pathway has the additional virtue that it could pay industry-competitive salaries, which is otherwise a structural problem for any government-sited AI safety program. The weakest element is the assumption that more funding will translate into faster AGI-scalable alignment progress — Gladstone gestures at this assumption without engaging the harder question of whether AGI-scalable alignment is even tractable on the relevant timescales. Annex B (the full alignment challenge) is explicitly cited as the place where this is discussed, but the chapter leaves the question hanging: *what if 50% of total research spend on AGI-scalable alignment doesn't solve the problem fast enough?* Gladstone does not say. The defense-in-depth framing in §3.2.2 is the closest the chapter gets to addressing this — evaluations are not solely sufficient, layered controls are needed — but the chapter doesn't grapple with the possibility that *all* of LOE3's outputs (research, standards, evaluations) might collectively be inadequate to the rate of capability advance.

#### Fact-sheet

**Two building blocks of LOE3:**
1. **Federally funded AI safety/security/AGI-alignment research** (§3.1)
2. **Standards for AI evaluations and RADA safeguards** (§3.2)

**Funding-gap evidence (the chapter's marquee numbers):**
- AI capabilities annual private spending: **>$100B since 2021**
- AI capabilities vs. safety publications: **50:1 ratio**
- Expert-recommended safety fraction of total AI R&D: **≥50%** (vs. status-quo single-digit percent)
- Concentration tension: most independent safety orgs rely on small donor set (see Annex E) — limits research-strategy diversity

**Three tiers of safety research access (§3.1.1):**
| Tier | Access | Risk | Examples |
|---|---|---|---|
| Open-source / public | None special | Low | Sandbox/testbed dev; sub-frontier interp; theoretical power-seeking analysis; on-device monitoring research; AGI-scaling-of-techniques theoretical work |
| Proprietary access | Certified researchers + weights | Moderate | Behavioral/propensity evaluations; private evaluation sets; mech-interp on frontier models; on-chip-monitoring R&D with frontier-lab engineering |
| National security | Classified + cleared personnel | High | CBRN/WMD-enabling capability evaluations on frontier models; some loss-of-control research |

**Proposed organizational vehicles (§3.1.2):**
- **NCAASR** — National Center for AI Alignment and Security Research, sited under NSF's NAIRR
- **AAS FFRDC** — AI Alignment and Security Federally Funded R&D Center, possibly sponsored by DARPA, IARPA, or DOE National Labs
- Or both, with research areas divided
- Existing precondition: **NSF NAIRR pilot** launched Jan 2024, ~$2.6B over 6 years, with NAIRR Secure component for sensitive-data research
- FFRDC virtues: classified environment + industry-competitive salaries (addresses same comp-gap as ASTF in LOE1 §1.4.2)

**AGI-scalable alignment prioritization (§3.1.2.1):**
- Centers must explicitly fund workstreams "fully and exclusively dedicated" to AGI-scalable alignment
- Reasoning: sub-AGI alignment already commercially incentivized (better-aligned models extract more value via RLHF etc.)
- Without explicit prioritization, funded effort drifts toward "more legible but less scalable" sub-AGI work
- Annex B (full alignment challenge) and Annex L (AI safety research topics) provide detail

**Cross-LOE collaboration plan (§3.1.2.2):** Centers should collaborate with BIS (export-control review), DOC/DHS (export license red teaming), IC (I&W framework), NSC (contingency planning), ASTF (regulatory-prep), State Dept (UK AISI partnership)

**Limitations of AI evaluations (§3.2.1) — the chapter's most independently citable content:**
| # | Limitation | Mechanism |
|---|---|---|
| 1 | Not comprehensive | Cannot exhaustively test capability surface; even worse for open-access (post-release augmentation) |
| 2 | Cannot confirm absence of capability | Failure to elicit ≠ capability missing; only positive results are informative |
| 3 | Highly vulnerable to manipulation | Fine-tune to pass specific test without addressing root cause; resubmission of patched models = eventual statistical passage |
| 4 | Systematic failure in high-capability regimes | Situational awareness → deceptive alignment (different outputs in eval vs. deployment) |

**Frontier-lab insider quote (§3.2.1.3, fn. 55):** evaluation gaming via resubmission has reportedly already begun at one major frontier lab, with the missing step described as figuring out what went wrong rather than retraining until passage.

**Anti-anthropomorphization** (fn. 56): deceptive alignment is not predicted from sentience or consciousness, but from training-shaped goal-directed behavior. Mirrors the §0.2.2 framing of loss-of-control as competence-of-optimizer.

**Three remediations for evaluation limitations (§3.2.2):**
1. **Diverse ecosystem of independent evaluators** — independence (no developer conflict-of-interest), private evaluation sets resistant to gaming
2. **Diverse evaluations with different private subsets** developed by different teams — broader coverage, less likely to miss latent capabilities
3. **Evaluations as one input to multi-faceted defense-in-depth case for safety**, not standalone signal

**NIST/AISI** is the named U.S. government body leading AI-evaluation-standards development under the NIST AI Risk Management Framework.

**Annexes referenced:**
- Annex B (full alignment challenge)
- Annex E (AI-safety funding — relevant to donor-concentration argument)
- Annex L (AI safety/security research topics — what NCAASR/AAS FFRDC could fund)
- Annex M (secure temporary storage of model weights — protocol for Tier 2 and Tier 3 research)

**Page anchors:**
- Funding-gap statistics: pp. 89–90
- Three research tiers: pp. 91–93
- NCAASR / AAS FFRDC proposal: pp. 94–95 (fn. 51 includes DARPA/IARPA/DOE sponsorship)
- AGI-scalable alignment prioritization: p. 95
- Limitations of evaluations: pp. 98–100
- Frontier-lab gaming insider quote: p. 99 (fn. 55)
- Three remediations: pp. 100–101

**Notable analytical moves:**
- **50:1 publications ratio** + **50% of total research spend benchmark** — quotable, citable funding-gap argument.
- **AGI-scalable vs. sub-AGI alignment distinction** — important for evaluating any AI safety research portfolio: easy-to-fund work (interpretability of small models, prosaic alignment) ≠ work that addresses the actual concern.
- **Evaluation-as-input-not-output** framing (§3.2.2) — extends defense-in-depth from infrastructure to epistemic methodology.
- **Anti-anthropomorphization** explicitly built into deceptive-alignment framing — mirrors the Chapter 0 loss-of-control framing, sidesteps "AI doesn't really think" objections.

**Methodological tensions and 2026-context flags:**
- Gladstone assumes **more funding will accelerate AGI-scalable alignment progress** without engaging the harder question of whether the problem is tractable on relevant timescales. Annex B is cited but the chapter does not claim the problem will be solved.
- LOE3 is largely **funding-and-organizational**, which means much of it could survive 2026 — NSF, DARPA, IARPA, DOE National Labs are durable institutions, and an FFRDC can be stood up without new legislation.
- NIST/AISI's status is contested in 2026, which weakens §3.2.3's reliance on NIST as the standards-setting lead. State-level efforts (CA TFAIA) and proposed federal bills (Hawley-Blumenthal) might supersede or complement.
- The four limitations of evaluations (§3.2.1) survive any political shift — they are technical claims about the methodology, not policy recommendations.

**What survives the 2026 political shift:**
- The four-part **limitations-of-evaluations** argument is durable and broadly applicable to any AI safety regime (CA TFAIA, Hawley-Blumenthal, EU AI Act, RSPs).
- **NCAASR/AAS-FFRDC architecture** can be stood up under existing NSF/DARPA/IARPA/DOE authority — no new legislation needed.
- **NAIRR / NAIRR Secure** is already operational; its trustworthy-AI mandate is durable.
- **AGI-scalable vs. sub-AGI alignment distinction** is a useful research-funding evaluation criterion at any level (federal, state, philanthropic).
- The **50:1 publications ratio** and the **50% safety-spend benchmark** are quotable for advocacy.

**Crucial frame to preserve in advocacy:** LOE3 is **funding the gap, not closing it directly**. Gladstone is not claiming that more funded research will solve AGI alignment in time — only that under-investing makes the problem definitely worse. This is the chapter most consistent with the "we don't know if alignment is solvable, but we should be trying much harder" framing common to safety advocacy. Anyone reading LOE3 as an alignment-will-be-solved chapter is over-reading; anyone reading it as a moratorium-substitute is under-reading.

---

### 06 — Chapter 4: LOE4 — Formalize safeguards by establishing an AI regulatory agency and legal liability framework
**File:** `gladstone/PDFs/06_chapter4_LOE4_FAISA_liability.pdf` | **Text:** `gladstone/text/06_chapter4_LOE4_FAISA_liability.txt` | **Pages:** 39 (doc pp. 102–140) | *Chapter — the document's intellectual centerpiece*

#### Prose summary

LOE4 is the longest substantive chapter in Gladstone and the document's intellectual core. It is also the only chapter that opens with an explicit attribution: "We are grateful to the team at the Center for AI Policy (CAIP), whose perspectives on AI regulation have informed several of the recommendations in this LOE" — and footnote 58 points to CAIP's draft Act at aipolicy.us/gladstone as the source from which "many of the legislative recommendations in this LOE are drawn." This matters for advocacy: anyone calling Gladstone a "Gladstone proposal" is half-right; the LOE4 architecture is closer to a CAIP-Gladstone collaboration than original Gladstone work, which gives the chapter additional standing in the U.S. legislative-advocacy ecosystem. Gladstone openly states the legislative regime would take **about 3 years** to begin meaningfully impacting safety after passage — which is why LOE1's interim measures are necessary even if Congress acts. Three building blocks: (1) **establish FAISA** with a comprehensive 4-entity, multi-tier licensing regime (§4.1); (2) **enact a civil/criminal liability framework with emergency powers** (§4.2); and (3) **handle national-security applications of AI** through some combination of existing IC/DOD oversight and modified RADA safeguards (§4.3).

The Frontier AI Systems Administration (FAISA) gets two siting options: a non-partisan SEC-style independent agency reporting directly to the President, or a unit inside DOE modeled on the National Nuclear Security Administration (NNSA) and reporting to an NSC-level official. The Administrator is Senate-confirmed; Gladstone recommends selecting on cybersecurity-or-biosecurity expertise rather than AI-research credentials. Four core functions: **Licensing** (rulemaking + RADA-safeguard enforcement), **Monitoring** (hardware tracking, AI-program horizon-scanning), **Enforcement** (civil cases brought directly, criminal referrals to DOJ), and **Algorithms** (a continuously-updating function that tracks algorithmic-efficiency advances and recommends threshold updates — this last function is what makes the regime non-static). The financing recommendations are deliberately budget-flexible: no-year funding plus notwithstanding appropriations, or RDT&E mechanisms that allow as-needed spending. Compensation waivers reappear here from LOE1's ASTF discussion, addressing the same structural problem that frontier-lab junior alignment researchers earn $500k+/yr. Conflict-of-interest rules, post-employment restrictions on Administrators and senior staff, and **FAISA-selection (not developer-selection) of third-party evaluators** are all baked in as anti-capture provisions. The agency's day-to-day activities (§4.1.2) include maintaining an AI hardware registry with **GPS coordinates** for individual devices, random sampling and spot-check inspections, jailbreak/exploit bounty programs, threshold-update authority with 30-day notice but with emergency-pause power during the notice period, and presidential-review-with-Congressional-consultation on threshold changes.

The four-entity, tiered RADA licensing regime in §4.1.3 is the chapter's center of gravity. **AI hardware designers (AIHDs)** like NVIDIA, Google, AMD, Intel, AWS, Cerebras get a 2-tier regime keyed to chip capability. **Data center infrastructure providers (DCIPs)** get a 2-tier regime keyed to power consumption — Gladstone derives the threshold by asking how long it would take a bad actor to clandestinely train a GPT-4-equivalent model using a sub-threshold dedicated AI data center, then setting the threshold so this **breakout timeline is ≥18 months** to give LOE2 contingency planners advance warning. The footnote shows the specific calculation: 27 H100 DGX systems totaling ~350 kW = ~17.9 months for a 2×10^25 OP GPT-4-equivalent training run. **AI hardware owners (AIHOs)** get a 2-tier regime keyed to aggregate compute capacity — example threshold of **800,000 TOPS** (equivalent to ~200 NVIDIA H100 chips at INT8 with sparsity), derived to produce a ~19-month GPT-4 breakout. Gladstone explicitly notes that DCIPs and AIHOs are often the same entity (Google, AWS, Azure rent access to chips they own and house) but the licensing categories are conceptually separate. Tier 1 entities have no new requirements. Tier 2 entities must register everything (GPS-tagged hardware locations, daily automated reporting of changes/loss/transfer/destruction), submit to inspections, apply FAISA-approved KYC to their downstream customers, respond to law-enforcement queries via FAISA, and **maintain emergency procedures to rapidly shut down data centers or chips**. The footnote-tucked aside that the U.S. cloud-and-hardware supply chain "could function as an early means of internationalizing domestic U.S. AI safety and security policy" — banking-sector parallel cited — is a structural argument for why these requirements have international leverage even before a treaty is negotiated.

**AI model developers (AIMDs)** get the document's most consequential structure: a four-tier regime where each tier has different conditions, all keyed to compute thresholds plus capability benchmarks. **Tier 1**: total training compute < **10^23 OP** (the registration threshold). No requirements. Example contemporaries: GPT-3, LaMDA, Baidu's ERNIE 3.0 Titan. **Tier 2**: 10^23 ≤ compute < **10^24 OP** AND MMLU score < 70% (the approval threshold). Pre-register training runs (so FAISA always has a current registry), run capability benchmarks periodically during training, immediately halt and report if benchmarks are breached. Example contemporaries: ChatGPT-3.5, PaLM, Llama 2. Open-access release prohibited for Tier 2 by default. **Tier 3**: above approval threshold but below the controlled threshold of **10^25 OP** (the level of GPT-4 and Gemini at the time of writing, late 2023). Tier 3 models are explicitly **"dangerous until proven safe"** — Gladstone openly inverts the normal regulatory burden of proof. Tier 3 AIMDs need pre-approval to train, conduct ongoing monitoring with emergency-pause/shutdown procedures, get pre-approval for *each* deployment context (including purely internal deployments and APIs), conduct ongoing deployment monitoring with KYC for high-volume or critical use, get pre-approval to share weights even with other Tier 3 AIMDs, respond to law-enforcement queries, and maintain emergency shutdown procedures. The four annexes N, O, P, Q (covered in section 11) provide the operational specifics. **Tier 4**: above the **10^25 OP** controlled threshold. Cannot be trained under any conditions, by anyone — academic, industrial, or government. The Tier 4 prohibition is the **only explicit prohibition in Gladstone** and is rationalized in two ways: (a) loss-of-control risk in current paradigm at this scale is too high, and (b) prohibiting training above this threshold weakens the feedback loop between training-run scaling and AI-hardware development, limiting the rate at which a "compute overhang" develops. Footnote 87 acknowledges this last point as a frontier-lab-raised concern (citing OpenAI). Models trained before regulations come into force are grandfathered as Tier 3 by default, but FAISA can re-classify to Tier 4 on emergency basis.

Two things in the licensing regime deserve specific attention as structural concessions or hedges. **Footnote 65** (Alan Chan / GovAI cited) acknowledges that compute may be a poor long-run threshold because it could create perverse incentives toward training less-interpretable architectures: it might take more compute to train an interpretable model than an uninterpretable one to the same capability, so a sub-threshold model could eventually be more capable but less safe. This is Gladstone admitting its central design choice may be flawed long-term. **Footnote 66** offers the chapter's most striking analogy: biosafety-level-4 laboratories are forbidden from storing certain high-consequence pathogens like smallpox, even though they are designed for the most contagious pathogens — because a single containment breach could be unrecoverable. Same logic applies to Tier 4 AI: even fully equipped labs cannot be trusted to build it safely. This is the chapter's best one-line answer to "but the responsible labs need to lead." General provisions (§4.1.3.5) for all licensed Tier 2+ entities mirror civilian-nuclear-industry security: a Chief Risk Officer, internal audit team, risk committee, three-lines-of-defense framework, civilian-nuclear-equivalent cyber/operational/physical security, model containment with emergency shutdowns, kill switches with **human oversight firewalled from the model's outputs**, dead-man-switch protocols requiring affirmative risk-committee approval to continue training. Whistleblower protections are substantive: legal protection, percentage-of-fines monetary rewards (modeled on SEC/DOJ qui tam practice), confidentiality with case-by-case override for testimony in criminal cases. Publication controls (§4.1.4) are deferred to a FAISA-commissioned expert study, with one specific area flagged: research that improves training-algorithm efficiency, since these reduce the effectiveness of compute and export controls.

The civil and criminal liability framework (§4.2) is the chapter's second pillar and is deliberately scoped to catastrophic-only outcomes. **Civil liability**: above a **$100M damage threshold**, **strict liability** applies — plaintiffs don't need to establish the specific cause of an accident to be compensated. License violation automatically constitutes negligence. **Joint and several liability** applies above the threshold to resolve diffusion of responsibility across the supply chain (any one party can be sued for the full amount; allocation among defendants is their problem). Open-access, free, or collaborative status is not a defense. **Safe harbor** for FAISA-designated regulatory tiers (e.g., Tier 2 hardware entities + Tier 3 AIMDs) — explicit incentive to register and comply, which is a clever inversion of strict-liability's typical chilling effect. **Criminal liability**: misdemeanors include failure to report hardware/data centers, misrepresenting safety protocols in pre-registration, operating above thresholds without a license, and misleading FAISA. Felonies include disregarding emergency orders, operating after license rejection, and breaching license conditions causing $100M+ damages. Entities cannot indirectly cover fines or offset via compensation modifications (an anti-corporate-self-protection provision). License suspension 1 month to 1 year for misdemeanors; full license revocation + 5-year ineligibility + mandatory hardware sale/destruction within 60 days for felonies. Crimes referred to DOJ. Gladstone recommends Congress investigate the constitutionality of fast-track procedural options to enable response at "the speed of relevance."

**Emergency powers** (§4.2.3) are the most aggressive single provision in the chapter. Triggered by either Presidential declaration of a national emergency due to advanced-AI threat, *or* by the FAISA Administrator's identification of a clear, immediate, major national-security threat that cannot be addressed by normal enforcement (with the determination published in the Federal Register). Once triggered, the FAISA Administrator can suspend AI licenses immediately, demand halts to AI activities, secure or encrypt model weights, restrict access to specific AI systems, **or impose a general moratorium on AI research and development**. The general-moratorium power is the closest Gladstone gets to ControlAI's Narrow Path Phase 0 prohibitions — but it's conditional on triggering, not standing. Right to appeal (federal district court for unlawful/unconstitutional claims) and right to compensation for compliance-related economic losses are both included. **Advanced AI in national security systems** (§4.3) is the chapter's most underdeveloped section: Gladstone acknowledges the tension between national-security imperatives (which would push for less stringent RADA) and loss-of-control risk (which is agnostic to who builds the system) without resolving it. Three options sketched: leverage existing IC/DOD oversight (Inspector General, General Counsel); modify RADA safeguards for national-security applications; or stand up a "national-security FAISA" with audit authority over national-security AI activities. Civil-liberties concern flagged: superhuman-persuasion AI capability could undermine democratic processes, but might be required to counter adversarial deployment in the domestic information environment.

For Dan's purposes specifically: LOE4 is the chapter to know cold. The 4-tier AIMD regime is the most-cited single piece of operational policy in the document and the chapter that does the most to differentiate Gladstone from both purely-voluntary frameworks (Anthropic RSP, OpenAI Preparedness Framework) and from prohibition-style proposals (ControlAI Narrow Path, MIRI). The 10^25 OP controlled threshold is now numerically obsolete — Claude Opus 4.7, GPT-5, Gemini 3.5, and several other models in 2026 are well above it — but the *structural* design (compute + capability-benchmark thresholds, with FAISA empowered to update them, with Tier 4 prohibition as the upper bound) survives as policy template. The strict-liability-above-$100M and joint-and-several-liability provisions are technically sound and citable independent of FAISA's existence; they could be implemented via state-level legislation or via a narrower federal bill. The whistleblower-protection-with-percentage-of-fines mechanism is durable and adopts a model already proven in financial-sector enforcement. The biosafety-level-4 analogy in footnote 66 is the chapter's best single rhetorical kernel for activist conversation. Major weaknesses to flag: (a) the chapter assumes Congressional action that has not happened, and the bill closest to it (Hawley-Blumenthal S. 2938) is much narrower and currently stalled; (b) the December 2025 federal-preemption EO actively works against the entire FAISA architecture; (c) the constitutional questions raised by emergency moratorium power, fast-track criminal procedures, and FAISA Administrator unilateral threat determinations are gestured at but not engaged — major-questions doctrine post-*West Virginia v. EPA* and the non-delegation doctrine both apply; (d) the national-security AI section (§4.3) is the document's least-developed substantive section and would need significant additional work before any of it could be operationalized; (e) the compute-threshold-as-design-anchor concession in footnote 65 is a real epistemic concession, not just a hedge — it implies the entire numerical scaffolding has a finite useful life. None of these weaknesses defeats the chapter's framework, but they do mean a sophisticated reader should expect to defend the architecture rather than the specific numbers.

#### Fact-sheet

**Three building blocks of LOE4:**
1. **FAISA — Frontier AI Systems Administration** (§4.1) with comprehensive licensing regime
2. **Civil/criminal liability + emergency powers** (§4.2)
3. **National security AI** handling (§4.3) — least developed section

**FAISA siting options (§4.1):**
- (a) Non-partisan independent agency reporting to President — SEC model
- (b) Unit inside DOE — NNSA model (National Nuclear Security Administration), reports to NSC-level official
- Senate-confirmed Administrator selected on cybersecurity/biosecurity expertise
- 4 functions: Licensing, Monitoring, Enforcement, Algorithms (continuously-updating threshold-recommendation function)

**FAISA financing & staffing (§4.1.1):**
- No-year + notwithstanding appropriations OR RDT&E mechanism
- Compensation waivers (same $500k+ frontier-lab benchmark from LOE1 §1.4.2)
- Conflict-of-interest rules + post-employment restrictions on Administrator and senior staff
- **FAISA selects third-party evaluators**, not developers — anti-capture provision

**Four entity categories (§4.1.3):**

| Entity | Tiers | Threshold proxy | Example threshold | Worked breakout time |
|---|---|---|---|---|
| AIHDs (hardware designers) | 2 | Chip capability | (set by FAISA) | — |
| DCIPs (data center providers) | 2 | Power consumption | ~350 kW per facility (1MW ≈ 630 H100 GPUs) | ~17.9 mo for 2×10^25 OP GPT-4 equivalent |
| AIHOs (hardware owners) | 2 | Aggregate TOPS | 800,000 TOPS (≈200 H100 INT8 sparse) | ~19.3 mo for GPT-4 equivalent |
| AIMDs (model developers) | **4** | Compute + capability | See AIMD table | — |

Many entities (Google, AWS, Microsoft) regulated under all four categories simultaneously.

**AIMD four-tier regime (§4.1.3.4) — the document's centerpiece:**

| Tier | Threshold | Status | Requirements | Example models (late 2023) |
|---|---|---|---|---|
| 1 | < 10^23 OP | Registration threshold | None | GPT-3, LaMDA, ERNIE 3.0 Titan |
| 2 | 10^23 to 10^24 OP, MMLU < 70% | Approval threshold; "generally safe" | Pre-register training runs; periodic in-training benchmarks; immediate halt+report on benchmark breach; **no open-access release** | ChatGPT-3.5, PaLM, Llama 2 |
| 3 | 10^24 to 10^25 OP, MMLU ≥ 70% | Controlled threshold; **"dangerous until proven safe"** | Pre-approval to train; ongoing training monitoring; pre-approval for *each* deployment context; KYC on high-volume use; pre-approval for weight transfers (even to other Tier 3 AIMDs); emergency shutdown procedures | GPT-4, Gemini |
| 4 | > 10^25 OP | Controlled threshold | **Cannot be trained under any conditions** — academic, industry, government — until FAISA raises threshold | (none at time of writing) |

**Breakout-timeline derivation principle:** thresholds set so a bad actor circumventing all *other* controls would still need ≥ 18 months to train a GPT-4-equivalent model — buying LOE2 contingency planners advance warning.

**Tier 4 prohibition rationale (§4.1.3.4.4):**
- (a) Loss-of-control risk too high under current paradigm
- (b) Limits compute-overhang dynamics (footnote 87 cites OpenAI's own concern)
- **The only explicit prohibition in Gladstone** — closest the document gets to ControlAI's Narrow Path framing

**General provisions for Tier 2+ entities (§4.1.3.5):**
- **Risk governance**: Chief Risk Officer, internal audit team, risk committee, 3LoD framework
- **Security**: civilian-nuclear-industry-equivalent cyber + operational + physical; license revocation for deficiencies
- **Model containment**: emergency shutdowns; info-gapping; **kill switches with human oversight firewalled from model outputs**; dead-man switch protocols
- **AI safety/security training** for employees
- **Whistleblower protections**: legal protection + **percentage-of-fines rewards** + confidentiality (overridable for testimony) — modeled on SEC qui tam
- **Incident reporting**: above-threshold incidents to FAISA; whistleblower-first reporting penalizes employer

**Civil liability framework (§4.2.1):**
- **$100M damage threshold** for strict liability triggering
- Strict liability — plaintiffs need not establish specific cause
- License violation = automatic negligence
- **Joint and several liability** for multi-actor incidents
- Safe harbor for FAISA-designated regulatory tiers — incentive to register
- Open-access/free/collaborative status NOT a defense

**Criminal liability framework (§4.2.2):**

| Severity | Examples | Penalties |
|---|---|---|
| **Misdemeanor** | Failure to report hardware/data centers; misrepresenting pre-registration safety protocols; operating without license; misleading FAISA | License suspension 1 month – 1 year |
| **Felony** | Disregarding emergency order; operating after license rejection; breaching license causing $100M+ damages | License revocation + 5-yr ineligibility + AI hardware sale/destruction within 60 days; DOJ prosecution |

- Entities **cannot indirectly cover fines** or offset via compensation
- **Constitutional fast-track procedures** recommended for serious infractions

**Emergency powers (§4.2.3) — the chapter's most aggressive single provision:**
Triggers:
- Presidential declaration of national emergency from advanced AI threat, OR
- FAISA Administrator's clear/immediate/major-threat determination, published in Federal Register

Powers (FAISA Administrator can):
- Suspend AI licenses immediately
- Demand halts to AI activities
- Secure or encrypt model weights
- Restrict access to specific systems
- **Impose general moratorium on AI R&D**

Safeguards: federal-district-court appeal for unlawful/unconstitutional orders; right to compensation for compliance-related economic losses.

**National security AI (§4.3) — least developed section:**
Three options for handling national-security applications, none endorsed:
- Existing IC/DOD oversight (IG, General Counsel)
- Modified RADA safeguards
- "National security FAISA" with audit authority

Civil-liberties concern: superhuman-persuasion AI deployment domestic vs. foreign — "balance between privacy and security" called out; not resolved.

**Critical attribution flags:**
- **Center for AI Policy (CAIP)** explicitly thanked at chapter opening; aipolicy.us/gladstone cited as legislative-recommendations source (fn. 58)
- **Tim Fist / CNAS** for export-control reasoning carryover from LOE1 (fn. 36 referenced from earlier)
- **Alan Chan / GovAI** for the compute-threshold critique (fn. 65)

**Two structural concessions worth memorizing:**
- **Footnote 65 (Alan Chan / GovAI)**: compute may be a poor long-run threshold because it creates perverse incentives toward less-interpretable architectures (a more interpretable model might require *more* compute for the same capability). Self-aware admission that the central design choice has finite useful life.
- **Footnote 66**: Biosafety-level-4 lab analogy — even fully equipped labs are forbidden from storing smallpox; same logic applies to Tier 4 AI. Best one-line answer to "but the responsible labs need to lead."

**Annexes that operationalize LOE4:**
- Annex G (compute primer & key thresholds — feeds tier definitions)
- Annex J (effective compute methodology)
- Annex M (secure temporary storage of model weights)
- **Annex N** (training-stage approvals — Tier 3 detail)
- **Annex O** (training-stage monitoring — Tier 3 detail)
- **Annex P** (deployment-stage approvals — Tier 3 detail)
- **Annex Q** (deployment-stage monitoring — Tier 3 detail)

These four annexes (covered in section 11 of this index) collectively provide the operational specifics for Tier 3 AIMD licensing.

**Page anchors:**
- FAISA establishment: pp. 103–105
- 4-entity framework: pp. 109–111 (Figure 6)
- AIHD licensing: pp. 112–114 (Figure 7)
- DCIP licensing + breakout calculation (fn. 73): pp. 114–117 (Figure 8)
- AIHO licensing + 800,000 TOPS threshold derivation: pp. 117–120 (Figure 9)
- AIMD 4-tier regime: pp. 120–128 (Figure 10) — **the single most-cited section**
- Tier 4 prohibition + grandfathering: pp. 128–129
- General provisions: pp. 129–131
- Publication controls: pp. 131–132
- Civil liability + $100M threshold: pp. 133–134
- Criminal liability table: pp. 135–136
- Emergency powers: pp. 137–138
- National security AI: pp. 139–140

**Notable analytical/strategic moves:**
- **"Dangerous until proven safe"** for Tier 3 — explicit inversion of normal regulatory burden of proof.
- **Biosafety-level-4 analogy** (fn. 66) — best one-line argument that responsible labs cannot be trusted with Tier 4 work.
- **Compute-overhang argument** for Tier 4 prohibition — turns frontier-lab-raised concern into prohibition rationale.
- **Strict liability with $100M threshold + safe harbor** — registration becomes self-protective, inverting the chilling effect.
- **Whistleblower percentage-of-fines** — adopts proven SEC/DOJ qui tam mechanism.
- **Kill-switch human firewalled from model outputs** — operationalizes the deceptive-alignment concern from LOE3 §3.2.1.4.
- **Banking-sector parallel for cloud/hardware international leverage** (fn. 74) — an international-policy lever even before LOE5's treaty.
- **CAIP attribution upfront** — gives the chapter additional standing in legislative advocacy ecosystems.

**Methodological tensions and 2026-context flags:**
- Entire chapter assumes **Congressional action**; bill closest to it (Hawley-Blumenthal S. 2938) is much narrower and **stalled in Senate Commerce**.
- The **December 2025 federal preemption EO** actively works against FAISA architecture by directing federal agencies to challenge state AI laws.
- 10^25 OP controlled threshold is **numerically obsolete in 2026** — Claude Opus 4.7, GPT-5, Gemini 3.5 are all well above it. The structural framework survives; the specific numbers don't.
- **Constitutional questions** with emergency moratorium power, fast-track criminal procedures, and FAISA Administrator unilateral threat determinations are flagged but unengaged. Major-questions doctrine post-*West Virginia v. EPA* (2022) and non-delegation doctrine both apply.
- §4.3 (national security AI) is **the document's least-developed substantive section** — would need significant additional work before operationalization.
- **Footnote 65's compute-threshold concession** is a real epistemic admission, not a rhetorical hedge — the entire numerical scaffolding has finite useful life.

**What survives the 2026 political shift:**
- The 4-tier AIMD framework is **policy template** at any level (federal, state, philanthropic procurement standards) — California TFAIA and NY RAISE Act both echo elements.
- Strict-liability-above-$100M and joint-and-several-liability provisions could be implemented at state level without federal action.
- Whistleblower-with-percentage-of-fines mechanism is durable and proven.
- Emergency-pause power is replicable at state level (CA TFAIA does so).
- The biosafety-level-4 analogy and "dangerous until proven safe" framing survive any political configuration as advocacy frames.
- CAIP attribution makes this the most legislatively-grounded piece of Gladstone — useful when arguing the proposal is operational, not academic.

**Crucial frame to preserve in advocacy:** LOE4 is **not a prohibition framework**. The Tier 4 prohibition is the only flat-prohibition mechanism, and it is conditional on a compute threshold that FAISA can adjust — not a "moratorium on AGI." The general moratorium emergency power is real but conditional on triggering. Anyone arguing LOE4 is the same as ControlAI's Narrow Path Phase 0 is over-reading; anyone arguing it is just licensing-as-usual is under-reading. The chapter's distinctive position is **scoped, evidence-driven, threshold-adjustable regulation with a hard upper bound** that can be raised or lowered as evidence accumulates. That precise position — between voluntary RSPs and prohibition — is what gives Gladstone its niche in the advocacy ecosystem and is worth defending precisely.

---

### 07 — Chapter 5: LOE5 — Enshrine AI safeguards in international law and secure the AI supply chain
**File:** `gladstone/PDFs/07_chapter5_LOE5_international.pdf` | **Text:** `gladstone/text/07_chapter5_LOE5_international.txt` | **Pages:** 18 (doc pp. 141–158) | *Chapter*

#### Prose summary

LOE5 is Gladstone's international chapter and the document's most ambitious LOE — the level at which the regulatory regime stops being U.S. policy and becomes a multilateral institution. The chapter opens with explicit nuclear-weapons framing: AGI proliferation could destabilize global security in ways "reminiscent of the introduction of nuclear weapons," and absent careful management could trigger "an AGI arms race" raising the risk of WMD-scale accidents, interstate conflict, and escalation. Four building blocks: (1) **build domestic and international consensus** on catastrophic AI risks (§5.2); (2) **enshrine safeguards in international law** via treaty (§5.3); (3) **establish an International AI Agency (IAIA)** to monitor and verify treaty compliance (§5.4); and (4) **establish an AI Supply Chain Control Regime (ASCCR)** with allies as a faster, parallel mechanism (§5.5). Section 5.6 explicitly catalogs open challenges Gladstone admits it has not solved. The chapter's stated **desired end state** (§5.1) is a UN-mandated global treaty enforcing the RADA safeguards from LOE4, cloud-provider monitoring requirements above scale thresholds, and international hardware-based tracking of AI chips. Gladstone is honest that the ASCCR can be stood up faster than the treaty regime, but warns that purely multilateral controls will likely be undermined in the medium term by the rise of competing supply chains — meaning both mechanisms are needed.

The consensus-building piece (§5.2) is structurally interesting because it argues that the loss-of-control framing is **more diplomatically tractable than weaponization**, since inner-alignment failure threatens even the developing party itself. Footnote 91 of the chapter spells this out: because the inner-alignment problem is unsolved, "no actor can be assured that they will be able to control an AGI-level system even if they develop and train the system themselves," meaning all actors — including adversaries — share an incentive to cooperate in preventing the development of such systems while inner alignment remains open. This is one of the document's better single insights and works as a lay explanation tool for diplomats who don't want to start with weaponization framing. Specific recommendations include U.S. Mission engagements with Heads of State/Government, conversations in existing forums (Global Partnership for AI, UN CCW Group of Governmental Experts on LAWs, OECD, AI Partnership for Defense), and foreign-assistance programs for partner-capacity-building. The technical-outreach subsection (§5.2.1.2) explicitly endorses the Hinton-led Western-academic outreach to Chinese AI researchers that began in 2023, cites the 2023 CAIS Statement on AI Risk (signed by several Chinese academics), and proposes the U.S. Ambassador to the UN initiate an **intergovernmental Commission on Frontier AI** modeled on the IPCC — drafting consensus reports to the Secretary General to foster shared understanding of loss-of-control risk. State Department's OES/STC office is named for bilateral outreach, including encouraging NeurIPS to host AI-risk workshops, supporting carefully-scoped exchange programs, and sponsoring international AI-safety training. The chapter is careful that U.S. government support of these efforts should focus on creating forums rather than shaping substance — credibility requires academic independence.

The treaty work (§5.3) acknowledges that AI poses fundamental challenges to traditional verification. In nuclear arms control, the reactor-grade vs. weapons-grade enrichment distinction makes differential controls feasible; in AI, a training data center is inherently dual-use — it can train safe or weaponized systems with no external signal differentiating them. The chapter's partial answer is that AI is more amenable to **software-based monitoring**, which can be more granular than nuclear-style verification, but Gladstone is clear that both software and traditional verification will be needed in combination. The 2023 UK AI Summit (Bletchley) is cited as having built consensus on two important principles: implementing defense in depth via overlapping controls, and the principle that **the burden of safety should increasingly fall on the developer as systems become more powerful**. The Bletchley Declaration's reference to "intentional misuse or unintended issues of control relating to alignment with human intent" is directly mapped to Gladstone's weaponization/loss-of-control taxonomy. Subsequent summits (South Korea, France 2024) are flagged as opportunities for additional commitments and joint declarations. The IAIA (§5.4) is the long-term institutional vehicle. Gladstone explicitly recommends the IAIA's structure be **expected to evolve**, with iteration analogous to early climate-change treaties and confidence-building observations of counterparty behavior. The four-entity framework from LOE4 (AIMDs, AIHOs, DCIPs, AIHDs) is offered as the IAIA's initial template. A **Compute Suppliers Group (CSG)** is proposed for coordinating export controls of compute hardware to non-IAIA member countries — bringing semiconductor-tool exporting nations together. The nuclear-nonproliferation analogy is invoked: 33 countries today have safe nuclear power, while only 9 have nuclear weapons; differential controls on dual-use technology can succeed even without hermetic containment. The hardest IAIA challenge Gladstone flags is **detection of individual defections** — a participant attempting to develop a self-aligned AGI clandestinely. The chapter acknowledges that no individual mechanism solves this; defense in depth is offered as the answer. Footnote 93 is a meaningful concession: "It may also be possible to implement the functions of an IAIA … through existing mechanisms, channels, and forums" — i.e., a new institution may not be necessary if existing bodies (IAEA-style adaptation, expanded Wassenaar Arrangement) can do the work.

The ASCCR (§5.5) is the chapter's most concretely operational proposal because it can be stood up via existing structures and U.S./allied executive action without UN involvement. Three goals: keep critical supply-chain components in U.S. and allied jurisdictions; control cloud-compute access via RADA-style safeguards; provide a regulated pathway for foreign entities to access U.S./allied cloud compute. The strategic-considerations subsection (§5.5.1) articulates an important regulatory-leverage principle: **the most promising points of regulatory leverage are assets with high capital cost (AI hardware, data centers, semiconductor tooling)**, not low-cost components (textual training data, AI weights themselves once trained, application-layer products). This justifies the supply-chain focus and rules out controls on training data or open-source-model sharing as ineffective. Table 4 lists eleven potential ASCCR inaugural member countries with their specific supply-chain leverage: **Netherlands, Taiwan, South Korea, Singapore, Israel** (semiconductor tooling export controls); **Japan** (semi tooling + tech-transfer + visa screening — most comprehensive position); **Germany, France, UK, Australia, UAE** (technology-transfer controls + foreign-national visa screening). Compliance terms could initially track Annex I's Voluntary Charter or LOE4's RADA safeguards. The chapter notes that on-chip governance technology is a priority area for ASCCR development, with up-front federal investment via LOE3's Centers possibly needed because the technology takes "several years" to develop and deploy at scale. The Wassenaar Arrangement is cited as a candidate vehicle for the ASCCR's controls.

Section 5.6 is the document's most candid acknowledgment of unsolved problems. Three open challenges: (a) AI-capable nations are incentivized to escalate AI-enabled national-security systems even if both sides fully agree on loss-of-control risk, because the precise capability level at which risk manifests is unknown — incremental gains may be perceived as low-risk; (b) reliable compliance verification is genuinely unsolved — on-chip verification is feasible on month-timescales for domestic schemes but takes "several years" for international verification; (c) algorithmic-efficiency improvements may eventually make compute-based controls impractical because more capabilities are accessible at lower compute. Approaches to limiting the pace of algorithmic improvements are mentioned but not developed. The chapter's quiet implication is that defense in depth must extend even to the algorithmic-publication layer (which §4.1.4 publication controls partially addresses).

For Dan's purposes specifically: LOE5 is the most ambitious LOE and the most likely to be operationally deferred, but it has two pieces that are independently citable and tractable in 2026. First, the **ASCCR architecture and the eleven-country leverage table** are useful policy templates regardless of treaty progress — they identify exactly which allies have which kinds of supply-chain control leverage, and the Wassenaar Arrangement is a real, existing institution that can be expanded under existing executive authority. Second, the **outer-vs-inner alignment diplomatic framing** in footnote 91 is genuinely good — it works as a lay-explanation tool for why catastrophic AI risk creates a cooperation incentive even between adversaries. The treaty/IAIA architecture is correctly understood as long-horizon — the chapter does not pretend otherwise — but the structural question it answers (what would a verification-and-monitoring regime for advanced AI look like, and what's the simplest institutional vehicle?) is independently valuable as policy thinking. Major weaknesses: (a) the Bletchley → Seoul → Paris summit chain has produced thinner-than-anticipated binding commitments, weakening the treaty pathway; (b) U.S./UK AISIs (Gladstone's institutional bets for international standards-setting) are politically weakened in 2026; (c) China relations on AI safety have not warmed appreciably, making the Hinton-style academic outreach more important and harder; (d) §5.6's algorithmic-improvement-defeats-compute-controls concession is structurally significant — it implies the entire LOE5 architecture has finite useful life if algorithmic efficiency continues at observed rates (~50% reduction per 18 months, per Chapter 0). The cleanest framing for advocacy: LOE5 is the document's **most ambitious and least urgent** chapter; LOE1 + LOE4 do most of the immediate work, and LOE5 is where the long-horizon stability of the regime ultimately rests. Anyone treating LOE5 as the lever Congress should pull next is misreading the priority order.

#### Fact-sheet

**Four building blocks of LOE5:**
1. **Consensus and capacity-building** internationally (§5.2)
2. **International law / treaty** for AI safeguards (§5.3)
3. **International AI Agency (IAIA)** for monitoring and verification (§5.4)
4. **AI Supply Chain Control Regime (ASCCR)** with allies (§5.5)

**Desired end state (§5.1):** UN-mandated global treaty that (a) enforces RADA safeguards on training runs above scale/capability thresholds; (b) places monitoring duty on cloud providers above scale thresholds; (c) implements hardware-based AI-chip tracking and international monitoring of AI chip usage.

**Consensus-building approach (§5.2.1):**
- **Loss-of-control framing is more diplomatically tractable than weaponization** — see footnote 91
- Foundational forums: Global Partnership for AI, UN CCW GGE on LAWs, OECD, AI Partnership for Defense
- Bletchley Declaration (UK 2023, 28 countries + EU) explicitly maps to Gladstone's weaponization/loss-of-control taxonomy

**Outer-vs-inner alignment diplomatic frame (footnote 91, the chapter's best one-line tool):** Because the inner-alignment problem is unsolved, *no actor can be assured of controlling an AGI even if they develop and train it themselves.* Therefore all actors — including adversaries — share an incentive to cooperate in preventing such systems while inner alignment remains open. This is the chapter's best argument that catastrophic-risk reduction is not zero-sum.

**Technical outreach (§5.2.1.2):**
- Endorses **Hinton-led Western-academic outreach** to Chinese AI researchers (begun 2023)
- 2023 **CAIS Statement on AI Risk** cited; signatories include several Chinese academics
- Proposes **U.S. Ambassador to UN** initiate **intergovernmental Commission on Frontier AI** — IPCC model
- State Department **OES/STC office** for bilateral outreach
- Specific tactics: NeurIPS workshops, exchange programs, technical training courses for Chinese-AI-research community

**Treaty considerations (§5.3):**
- AI training data centers are **inherently dual-use** — no nuclear-style enrichment-level analog
- **Software-based monitoring** is the partial answer — more granular than traditional verification, but both will be needed
- **Bletchley consensus** principles: (a) defense in depth via overlapping controls; (b) burden of safety falls on developer as system becomes more powerful
- Ongoing contention: at what capability threshold do open-access AI systems stop being compatible with global safety
- Subsequent summits (Seoul, Paris 2024) flagged as opportunities for joint declarations

**IAIA structure (§5.4):**
- Initial RADA template: 4-entity / multi-tier framework from LOE4
- **Compute Suppliers Group (CSG)** for coordinated export controls to non-IAIA members
- **Nuclear-nonproliferation analogy**: 33 safe-power countries vs. 9 nuclear-weapons countries — differential controls on dual-use tech can work
- Hardest challenge: detect individual defections (a participant clandestinely developing self-aligned AGI)
- **Footnote 93 concession**: IAIA functions could be implemented via existing channels (no new institution strictly required)

**ASCCR architecture (§5.5) — most concretely operational:**

Three goals:
- Keep critical supply-chain components in U.S. and allied jurisdictions
- Control cloud-compute access via RADA-style safeguards
- Provide regulated pathway for foreign entities to access U.S./allied cloud subject to safeguards

**Regulatory-leverage principle (§5.5.1):** Most effective leverage is on **high-capital-cost** assets (AI hardware, data centers, semiconductor tooling). Low-cost components (textual training data, AI weights, applications) are not promising loci of control. This rules out training-data controls and open-access-model-sharing controls as primary mechanisms.

**Eleven candidate ASCCR inaugural members and their leverage (Table 4):**

| Country | Leverage |
|---|---|
| Netherlands | Semiconductor tooling export controls |
| **Japan** | **Semi tooling + tech-transfer + visa screening (most comprehensive)** |
| Germany | Tech-transfer + visa screening |
| Taiwan | Semiconductor tooling export controls |
| United Kingdom | Tech-transfer + visa screening |
| South Korea | Semiconductor tooling export controls |
| France | Tech-transfer + visa screening |
| Australia | Tech-transfer + visa screening |
| Israel | Semiconductor tooling export controls |
| Singapore | Semiconductor tooling export controls |
| United Arab Emirates | Tech-transfer + visa screening |

**ASCCR institutional vehicle:** **Wassenaar Arrangement** cited as candidate existing structure. ASCCR also potentially feeds IAIA monitoring functions if IAIA later established. Compliance terms could initially track Annex I (Voluntary Charter) or LOE4 RADA safeguards.

**On-chip governance** flagged as ASCCR priority — needs federal R&D investment via LOE3 Centers because the technology takes "several years" to develop and deploy at scale.

**Open challenges (§5.6) — Gladstone's most candid concession:**
- (a) AI-capable nations incentivized to escalate AI-enabled national-security systems even if loss-of-control risk is shared knowledge — incremental gains perceived as low-risk
- (b) Reliable compliance verification is unsolved: on-chip verification feasible at month-timescales domestically, "several years" internationally
- (c) **Algorithmic-efficiency improvements may eventually defeat compute-based controls** — capability-per-OP is rising; defense in depth would need to extend to algorithmic-publication layer (LOE4 §4.1.4 publication controls only partially address)

**Companion document referenced:** *Survey of AI Technologies and R&D Trajectories* (cited multiple times throughout LOE5).

**Annexes referenced from LOE5:**
- Annex C (failure scenarios — for diplomatic engagement)
- Annex F (persuasion and manipulation — international information-warfare risk)
- Annex G (compute primer — supports ASCCR/IAIA threshold definitions)
- Annex I (Voluntary Charter — basis for initial ASCCR compliance terms)
- Annex L, L.4 (hardware-based verification — feeds IAIA/ASCCR monitoring)
- Annex N, N.4 (data controls scoped to specific training runs — narrow exception to no-data-controls principle)
- Annex P, P.2 (KYC on end users — narrow exception to no-application-controls principle)

**Page anchors:**
- Desired end state: p. 142
- Outer-vs-inner alignment diplomatic frame (fn. 91): p. 145
- Hinton outreach + CAIS Statement: pp. 146–147
- Intergovernmental Commission on Frontier AI (IPCC analog): p. 147
- Treaty verification challenge (dual-use vs. nuclear enrichment): pp. 150–151
- Bletchley consensus principles: p. 151
- IAIA design + footnote 93 concession: pp. 152–153
- Compute Suppliers Group (CSG): pp. 153–154
- Regulatory-leverage principle (high-capital-cost): pp. 155–156
- 11-country ASCCR table: pp. 156–157
- Open challenges including algorithmic-efficiency concession: pp. 157–158

**Notable analytical/strategic moves:**
- **Outer-vs-inner alignment as cooperation incentive** — the chapter's best diplomatic move.
- **Loss-of-control framing more tractable than weaponization** — counterintuitive, but argued well.
- **Nuclear-nonproliferation differential controls work for dual-use tech** — 33:9 ratio cited.
- **High-capital-cost regulatory leverage principle** — rules out training-data and open-access-weight controls as primary mechanisms; focuses leverage on hardware/data centers.
- **Intergovernmental Commission on Frontier AI = IPCC analog** — credible institutional model.
- **Wassenaar as existing ASCCR vehicle** — does not require new institution.
- **Footnote 93 IAIA concession** — IAIA functions implementable via existing channels.

**Methodological tensions and 2026-context flags:**
- **Bletchley → Seoul → Paris summit chain** has produced thinner-than-anticipated binding commitments — treaty pathway is weakened.
- **U.S./UK AISIs** are politically weakened in 2026 — Gladstone's institutional bets for standards-setting are at risk.
- **U.S.-China relations on AI safety** have not warmed appreciably — Hinton-style academic outreach is more important and harder.
- **§5.6 algorithmic-efficiency concession** is structurally significant — it implies the entire LOE5 architecture has finite useful life.
- **Footnote 93 IAIA concession** is the chapter's most useful institutional realism — but also weakens the case for the IAIA as a discrete institution.

**What survives the 2026 political shift:**
- **ASCCR architecture + 11-country leverage table** — usable as policy template via Wassenaar Arrangement under existing executive authority.
- **Outer-vs-inner alignment diplomatic frame** — durable advocacy and explanation tool.
- **Compute Suppliers Group (CSG)** as a coordinative concept among semi-tooling exporters.
- **High-capital-cost regulatory leverage principle** — survives any political configuration.
- **Intergovernmental Commission on Frontier AI** — can be advocated separately even if treaty stalls.

**Crucial frame to preserve in advocacy:** LOE5 is **the most ambitious and least urgent** LOE. The work it sets up — treaty, IAIA, ASCCR — is long-horizon and requires the foundational LOE1/LOE4 work to be in motion first. Anyone using LOE5 as evidence that international action precedes domestic action is misreading the priority order: Gladstone is explicit (§5.1, §5.2) that the U.S. needs to "secure the most time-critical components of its own domestic AI supply chain" first. The ASCCR is the only LOE5 element that could plausibly run on a near-term timeline, and only because it can leverage existing structures (Wassenaar) rather than create new ones.

---

[remaining sections 08–11 to be added in subsequent passes]
