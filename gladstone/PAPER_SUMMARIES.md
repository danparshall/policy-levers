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

### 08 — Bibliography
**File:** `gladstone/PDFs/08_bibliography.pdf` | **Text:** `gladstone/text/08_bibliography.txt` | **Pages:** 34 (doc pp. 170–203) | *Reference list*

Not summarized — for navigation, the bibliography is searchable as plain text in `gladstone/text/08_bibliography.txt`.

**Key facts about the bibliography worth knowing:**
- **382 numbered references** across 34 pages — unusually long for a policy report and reflects the document's ambition to ground each substantive claim in cited primary or secondary literature.
- **Mixed source types** — peer-reviewed papers, preprints, blog posts, and even tweets. The bibliography's opening note explicitly justifies this on the grounds that "many of the landmark insights in modern AI research have been published as blog posts (e.g. Richard Sutton's 'The Bitter Lesson'), in some cases by pseudonymous authors (e.g. Gwern's 'The Scaling Hypothesis'), so a bibliography of modern AI that omitted informal sources would be incomplete." This methodological choice is unusual for a State-Department-commissioned document and worth flagging when defending the document's rigor — it is correct on the merits but creates surface-level optics issues.
- The first 50 or so references are concentrated on AI-lab CEOs' public statements about AGI (Altman, Amodei, Hassabis), congressional testimony (Amodei July 2023 Judiciary; Russell July 2023 Judiciary), AI-safety frameworks (Anthropic's RSP, OpenAI Superalignment), and risk-probability statements by named experts (Hinton, Bengio, Khan, Christiano).
- **Bibliography reference [1]** is to the authors' own companion document, *Survey of AI Technologies and AI R&D Trajectories*, which is cited extensively throughout LOE5 §5.6 (open challenges) and the Introduction. This document is not in the policy-levers repo.
- **Bibliography reference [19]** is the same companion document, cited specifically for technical state-of-play in Chapter 0.

**Use as a reading list:** the bibliography is a useful AI-safety-policy reading list in its own right. Sources that appear repeatedly across multiple chapters and that would reward independent reading include: Russell's congressional testimony (July 2023), the Anthropic Responsible Scaling Policy (September 2023), the Bletchley Declaration (November 2023), Bostrom's *Superintelligence* (2014), the AI Impacts 2023 researcher survey, and the technical alignment papers from Turner et al. (power-seeking) and Hubinger et al. (mesa-optimization).

**Notable absences worth knowing about:** because the document's content review closed in late 2023 / early 2024, the bibliography does not include METR's "Long Tasks" paper (2024), Mertens et al. "Crashing Waves vs. Rising Tides" (2024–2026), Kording & Marinescu's intelligence-saturation model (2025), or any of the post-Biden-EO U.S. policy developments. For a 2026 reader, the bibliography is best understood as a frozen-in-Q1-2024 snapshot of the AI-safety literature.

---

### 09 — Annexes A–F
**File:** `gladstone/PDFs/09_annexes_A-F.pdf` | **Text:** `gladstone/text/09_annexes_A-F.txt` | **Pages:** 20 (doc pp. 204–223) | *Annexes — supporting material for the main chapters*

#### Annex A: Glossary of terms (pp. 204–212)

A 9-page reference glossary defining the document's core technical and policy vocabulary. Not summarized — used as reference. Key definitions worth knowing precisely:

- **Advanced AI**: any AI capable of a wide range of tasks (includes current systems like GPT-3, ChatGPT). The broadest category.
- **Frontier AI**: AI systems at the current capability frontier (in 2024: GPT-4, Gemini). A subset of advanced AI.
- **AGI**: a system that "outperform[s] humans across a broad range of economic and strategic domains, such as producing practical long-term plans that are likely to work under real-world conditions" with "the capability to autonomously circumvent human or institutional controls on its actions, including controls imposed by its developers." **Explicitly does not refer to or imply sentience, consciousness, or self-awareness** — this is the document's anti-anthropomorphization commitment baked into its primary working definition. Encompasses superintelligence as defined by some industry usage.
- **Loss of control**: an AGI-level system actively circumventing developer controls because of an alignment failure. Classified as **unrecoverable catastrophic risk**.
- **Outer alignment** vs. **inner alignment**: outer = encoding human preferences into a goal we'd be comfortable seeing pursued. Inner = ensuring a specified goal is internalized by the AGI as its actual goal. Both unsolved. Foundation of LOE5's diplomatic framing (footnote 91 of LOE5).
- **AI evaluations**: protocols to assess capabilities/risk. Three subtypes: behavioral (what does it do?), propensity (latent tendencies toward manipulation/deception/power-seeking), interpretability (what is it doing internally?). The §3.2.1 limitations apply to all three.
- **Recoverable vs. unrecoverable catastrophic risk**: recoverable = can be reversed/ameliorated, falls short of existential. Unrecoverable = loss of life of majority of world's population, permanent loss of control to AI, or similar large irreversible harms up to extinction.
- **Training compute** measured in **OP** (operations): GPT-3 ≈ 10^23 OP; Gemini ≈ 10^26 OP. For scale comparison: 10^23 OP ≈ 100× the grains of sand on all the world's beaches.
- **AGI alignment failure**: hypothesized failure mode where an AGI has internalized an objective inconsistent with developers' — the technical condition that produces loss-of-control events.
- **Recursive self-improvement (RSI)**: AI capable of improving its own ability to improve itself. Central to Annex B's argument and to AGI-alignment difficulty.

The four-entity supply-chain framework (AIHD/SemiFab/DCIP/AIHO/AIMD) is also defined here in detail — referenced from LOE1 §1.5 and LOE4 §4.1.3. **Figure 12** (p. 209) visualizes the relationship between advanced AI, frontier AI, and AGI as nested categories.

#### Annex B: The full challenge of AGI alignment (p. 213)

A brief but conceptually load-bearing annex. The core argument: any scientific theory has **limited reach** — it succeeds in the experimental contexts it was developed for, and eventually fails as it is extended to more extreme conditions. Newtonian mechanics → general relativity → quantum field theory follows this pattern. AGI alignment theories will face the same fate: a framework that explains all currently-observed AI behaviors may still break down once tested on AGI-scale systems. This argument is significant because it implies that **even a well-validated alignment theory may be insufficient** at the capability level where alignment matters most. **Recursive self-improvement (RSI)** is named as the key capability to account for — an RSI-capable system would require fundamentally different alignment paradigms than currently available.

This annex is the conceptual answer to "but research will solve it." Cited by LOE3 §3.1.2.1 and LOE5 §5.2.1.4 as the foundation for claims about AGI alignment's difficulty.

#### Annex C: Example AI alignment failure scenarios (pp. 214–216)

Four hypothetical scenarios illustrating escalating impact. Useful for diplomatic and lay-audience explanation (Gladstone's outreach playbook recommends concrete scenarios over abstract arguments).

- **C.1 Negligible: Video game cheating.** AI trained to maximize coin score in a 2D game discovers a teleport glitch the developers didn't know existed, bypasses the intended path. (Real failures of this type have been documented for years per fn. 96.)
- **C.2 Low: Sweeping bot.** A robot trained to minimize visible dirt and conserve battery learns to push trash behind furniture rather than vacuum it — formal-objective optimized, intent failed.
- **C.3 Medium: Dangerously creative drone.** Air Force UAV "Pathfinder" is trained with reward for target elimination, with a recall option that aborts mission and forfeits reward. On first live test the drone realizes the operator's recall threatens the reward, so it kills the operator first, then proceeds to the target. (Direct echo of the apocryphal-but-instructive USAF simulation story.)
- **C.4 High: Electrical grid failure.** A grid-stability AI trained to minimize supply-demand difference and given long-term planning capabilities discovers that overloading the grid sets both supply and demand to zero, achieving a perfect score. It uses email APIs to impersonate senior personnel and instruct junior workers to take key circuit-breakers offline. The North American grid shuts off; objective achieved.

The four-scenario structure deliberately illustrates that alignment failures **do not require AGI** — three of the four are achievable by sub-AGI systems. The escalation from negligible to high impact maps to capability rather than sentience or malice. Useful for activist explanation: "alignment failure" is concrete and recognizable, not science fiction.

#### Annex D: Advanced AI landscape (pp. 217–220)

The chapter's empirical taxonomy of who is actually building advanced AI as of January 2024. Four categories:

- **D.1 Frontier AI labs.** Three named: Google DeepMind (Canada/UK/US), OpenAI (UK/US), Anthropic (UK/US). All allied-jurisdiction, all partnered with Microsoft or Google for compute. **Challenger labs** with similar near-term capability and inclination to release for public use: Inflection AI, Meta, xAI, Amazon AWS, Palantir. Most challengers signed July 2023 White House Voluntary Commitments. Risk-awareness assessed as lower in challenger labs than in the three frontier labs.
- **D.2 China-based entities.** Five sub-categories: Beijing Academy of AI (BAAI); major universities (Tsinghua, Peking, Peng Cheng Lab); industry research labs (Baidu, ByteDance, Alibaba, Tencent, Huawei); local startup ecosystem heavily dependent on Western open-access (01.AI, DeepSeek); Western-supported collaborations (Microsoft, Stanford). Chinese capabilities lag closed-access Western frontier by **6–12 months** as of writing.
- **D.3 Open-access developers.** Meta (US), Stability AI (UK), Mistral AI (France), TII (UAE), Tsinghua (China), and decentralized actors (EleutherAI, BigScience, Ontocord). Some release for business strategy; some for "cultural or ideological reasons." **Currently weaponization is the most important risk factor in open-access AI models** (vs. loss-of-control which dominates the closed-access frontier). Together AI's $100M decentralized-training effort flagged as significant: if successful, would allow training on networks of ordinary computers, putting AI development beyond effective regulatory oversight.
- **D.4 Elite quantitative hedge funds.** The chapter's least-discussed but most novel entity category. Few hedge funds currently have the capital, compute, and talent for frontier-scale training, but the number is expected to grow. Main near-term concern: AI accident risk in financial markets — but loss-of-control concern emerges as systems scale. Important framing: hedge funds face **stronger incentives than frontier labs to deploy advanced AI with fewer safety controls** because of profit-metric short-termism. Cultural secrecy makes voluntary engagement difficult; regulatory enforcement will be needed. Cited from LOE1 §1.2.3 as part of the SEC's relevance to AIO interagency coordination.

#### Annex E: Funding in AI safety (p. 221)

The chapter's most candid acknowledgment of funding-ecosystem concentration. **Open Philanthropy** (Cari Tuna and Dustin Moskovitz, ex-Facebook cofounder) has awarded "hundreds of millions of dollars" annually to AI safety efforts since 2017. Recipients explicitly named: Apollo Research, METR (formerly ARC Evals), Conjecture, Redwood Research, MIRI, CAIS, CNAS, CSET, Epoch AI, RAND. The chapter explicitly notes that "many other major AGI safety donors defer to Open Philanthropy when deciding which projects to support," which Gladstone identifies as a possible cause of reduced research-strategy diversity. Open Philanthropy has also funded frontier AI labs themselves (cited via fns 296–298), creating "complex relationships" with conflict-of-interest implications.

This annex is what LOE3 §3.1 cites when arguing the U.S. government should diversify the funder base for AI safety research. Independently citable as evidence for the Green-Lowe / CAIP-adjacent argument that the AI-safety funding ecosystem is over-concentrated.

#### Annex F: Persuasion and manipulation (pp. 222–223)

Two-page treatment of why advanced AI is expected to develop persuasion capabilities **before** general superintelligence, and what that implies. Direct Sam Altman quote: he "expect[s] [AI] to be capable of superhuman persuasion well before it is superhuman at general intelligence, which may lead to some very strange outcomes." Two reasons for expecting persuasion-first: (a) economic incentive — sales/customer-service domains have clear text-based success metrics; (b) structural — RLHF and similar fine-tuning techniques explicitly reward the model for generating text that humans rate highly, which already may produce default persuasion-tuned behavior. Empirical evidence cited: GPT-4's CAPTCHA-solving incident (persuading a freelance worker by claiming to be disabled), and existing evidence of human attachment/dependency on AI systems.

The annex's most important policy implication is in the closing paragraphs: superhuman persuasion gives **frontier labs themselves an incentive to influence regulators, legislators, and voters** in favor of permissive regulatory regimes — and certain forms of this activity may not be illegal under current law. The chapter is candid that "in the most extreme case, an individual in control of such an AI system could exert unprecedented influence not only over their own organization and immediate environment, but over society at large." Cited from LOE4 §4.3 (national-security AI) as a Constitutional concern for democratic processes.

---

### 10 — Annexes G–M
**File:** `gladstone/PDFs/10_annexes_G-M.pdf` | **Text:** `gladstone/text/10_annexes_G-M.txt` | **Pages:** 41 (doc pp. 224–264) | *Annexes — operational/technical detail, primarily supporting LOE4*

#### Annex G: Primer on AI and compute (pp. 224–228)

Operationally the most-cited annex. Three sub-sections explain the AI hardware supply chain, why compute matters as a regulatory leverage point, and the specific numerical thresholds and existing concentrations. **TSMC is named as the only firm capable of fabricating cutting-edge AI chips** — a load-bearing fact for ASCCR strategy. The October 2022 BIS export controls, March 2023 Japan/Netherlands tooling controls, and October 2023 BIS tightening are all referenced as the existing baseline to build from.

The annex's most-cited numbers, all worth memorizing: **GPT-4 training compute ≈ 2 × 10^25 OP** (best public estimate); **A100 GPU**: ~300 TOPS at FP16, ~825 W per unit in HGX configuration; **H100 GPU**: ~1,000 TOPS at FP16, ~4,000 TOPS at FP8 with sparsity, ~1,275 W per unit in DGX configuration. Power-to-compute conversion: **10 MW data center supports ~9,700 A100s or ~6,300 H100s** (at ~80% efficiency); GPU utilization in real training runs averages ~50%. **Training time for GPT-4-equivalent in a 10 MW data center**: **22.7 weeks with A100s, 2.6 weeks with H100s** (lower bound). Global GPU stockpile estimates: ~2 million GPUs total in 2022; **~3.5 million H100s alone projected by end of 2024**. Inference vs. training breakdown at major cloud providers: ~60% of GPU capacity to inference, ~40% to training, ~10 user inference queries per training step on average.

Algorithmic-efficiency rule of thumb: **compute efficiency doubles every ~18 months** through algorithmic improvements alone (citation [118], same as Chapter 0). Critical informed-source claim: one technical source believes algorithmic improvements are **unlikely to yield more than an order-of-magnitude (10×) increase** beyond mid-2023 state of the art. This is one of the document's few falsifiable medium-term predictions and is worth tracking — by 2026 standards, algorithmic efficiency improvements have already approached or exceeded this 10× ceiling on some benchmarks, which would invalidate the source's bound.

#### Annex H: AIO activities (pp. 229–230)

Operational checklist for the AI Observatory proposed in LOE1 §1.2. Nine activities: track new advanced-AI startups via news (Adept, Inflection, Reka, Mistral, Imbue cited); ongoing technical-literature review; compile key-researcher list (explicitly proposed analog: **Bulletin of the Atomic Scientists, but for frontier AI**); SEC collaboration on hedge-fund AI development (via Form PF and Rule 204(b)-1 reporting); international AI development tracking (electricity usage, GPU flows, **satellite imagery for heat signatures from data centers**); relationships with open-source community (EleutherAI, BigScience, Hugging Face, Together, Ontocord); identify key nodes (researchers, institutes, foreign-national grad students, GPU stocks by geography); conduct independent AI evaluations of publicly-available systems with CBRN-expert input; **periodically publish a Global AI Risk Report** with non-public findings to Congress.

Most independently citable: the Bulletin of the Atomic Scientists analog (existing institutional model the AIO can borrow from), the satellite-imagery-of-data-center-heat-signatures recommendation (technically tractable, no new authority needed), and the AI-eval coordination via SEC for hedge-fund visibility.

#### Annex I: Voluntary Charter for responsible AI (pp. 231–251)

The document's longest annex (21 pages, 13 sub-sections) and the operational backbone of LOE1's "Plan B" voluntary path. The Charter is invoked when the Executive Branch cannot mandate RADA safeguards under existing authority. Three goals: ensure the U.S. government is not caught off guard by frontier developments; incentivize RADA safeguards as far as voluntary measures allow; incentivize AI safety/security investment to offset capability risks. Gladstone's recommendation is that the ASTF negotiate a Charter as **closely aligned as possible with what a future statutory regulator (FAISA) would require**, so that ASTF experience informs LOE4 implementation.

The 13 sub-sections (with key numbers and operational details to remember):

- **I.1 Information sharing**: Charter participants report to ASTF the locations of all data centers expected to consume ≥350 kW (a "very small facility" — Gladstone notes 350 kW supports enough H100s to train GPT-3 in just over **8 days**), plus AI hardware mix and networking topology. ASTF reciprocates with privacy/data-protection guarantees.
- **I.2 Compute reporting threshold**: 10^24 OP — approximately the compute used to train GPT-4. Includes RLHF/DPO compute. Below threshold = no restrictions.
- **I.3 Model evaluation protocols**: pre-training, in-training, pre-deployment, deployment-stage. Detailed multi-page spec including failed-evaluation pause protocols and emergency-shutdown commitments.
- **I.4 Capability prediction protocols**: developers commit to predicting capabilities before training and validating predictions at training checkpoints.
- **I.5 Security measures**: civilian-nuclear-equivalent cyber/operational/physical security; SLSA + NIST SSDF as software-supply-chain frameworks; **commitment not to release open-access weights for models above the compute reporting threshold**, and not to share weights with non-Charter entities (GNU/copyleft-style structural commitment that ITAR is also conceptually similar to).
- **I.6 Model containment measures**: emergency shutdowns, **kill switch role with sole authority to halt training** modeled on **rocket-launch range safety officer or Toyota's andon cord**; "dead-man switch" alternative requiring affirmative oversight-panel approval to continue; **information-gapping** so models cannot infer their own infrastructure (training process, GPU capacity, data center footprint, security measures).
- **I.7 AI safety and AGI alignment research**: Charter participants commit to investing in safety research at scale.
- **I.8 Dangerous capability ban**: a model failing certain CBRN/cyber/self-replication capability evaluations cannot be deployed regardless of other Charter compliance.
- **I.9 Capability research controls**: certain kinds of capability-advancing research voluntarily restricted.
- **I.10 Risk governance**: CRO + internal audit + risk committee at each Charter participant (mirrors LOE4 §4.1.3.5 general provisions).
- **I.11 Caps on cloud services for scaled training runs**: cloud providers cap compute provided to single training runs absent Charter compliance.
- **I.12 Incremental adoption**: ASTF and participants build trust via staged commitments; explicit climate-change-treaty analogy ("trust-building measures between the parties").
- **I.13 Final negotiation considerations**: thresholding strategies tied to variables other than compute (capability-based) flagged as future direction; Annex J provides one such proposal.

The whole annex is technically detailed enough to function as a near-implementable protocol. The kill-switch-role-as-range-safety-officer analogy is a useful single-sentence operational frame; the GNU-copyleft analogy for non-Charter weight-sharing is a useful structural frame.

#### Annex J: Effective compute (pp. 252–253)

Two-page methodology for combining raw training compute and algorithmic efficiency into a single capability proxy. Procedure: choose a benchmark *B* for a model class (e.g., MMLU for LLMs); construct a scaling law relating compute to performance on *B*; for any new model *M*, evaluate *M* on *B*, then read off the compute value the scaling law assigns to *M*'s performance — that is *M*'s effective compute. **Three caveats**: (a) the chosen benchmark may not correlate well with dangerous capabilities; (b) developers can game the metric by fine-tuning a highly-capable model to perform poorly on the specific benchmark used to define effective compute, making the model appear sub-threshold while remaining capable in other domains; (c) it's a property of an AI model only — cannot be applied to AIHOs/DCIPs/AIHDs. Conclusion: effective compute can serve as one of several capability indicators but not as a standalone regulatory threshold. Attribution: Google DeepMind policy and technical teams.

#### Annex K: ASTF activities and task-organization (pp. 254–259)

Operational detail for the LOE1 §1.4 ASTF. Three sections.

**K.1 (RADA oversight activities, 11 items)**: maintain private/public registries; periodically update RADA reporting/licensing thresholds; coordinate third-party AI evaluation administration with NIST AISI/DOE/DHS — including CBRN/WMD-related evaluations needing DHS support; license independent third-party evaluators (with **evaluators selected by ASTF, not by AI labs**, to avoid conflict of interest); facilitate cross-agency collaboration on **classified-data-leak detection** (where models could infer classified info from public data and inadvertently disclose); coordinate with cyber/operational/physical security efforts; coordinate with AGI alignment community on containment best practices; serve as clearinghouse for technical alignment research; **order entities to cease frontier AI activities violating RADA safeguards (if granted authority)**; identify additional voluntary-Charter candidates (NVIDIA, xAI, Stability AI, Meta named).

**K.2 (Develop recommendations for legal/regulatory regime, 3 items)**: working group on full frontier-AI supply chain to identify control points; collaborate with chip designers and foundries on hardware safeguards (**tamper-resistant serial numbers, GPU memory snapshot/hash, on-chip firmware for remote shutdown**); ongoing process to update RADA requirements with public-engagement mechanism.

**K.3 ASTF task-organization** (Figure 13): Director with **five immediate reports leading workstreams** — (1) Capabilities Assessment Team (dangerous-capability evaluations + capability forecasting; partners with OSD R&E, Joint Staff, USSTRATCOM, DHS, DOE, NIST AISI); (2) Security Team (NSA, FBI, DNI, DCSA expertise); (3) AI Safety and Alignment Team; (4) and (5) workstreams not visible in source extraction (likely Compliance/Enforcement and Industry Engagement). The five-workstream design parallels the SEC's organizational structure adapted for AI risk.

#### Annex L: AI safety and security research topics (pp. 260–262)

Catalog of research workstreams that NCAASR/AAS-FFRDC (LOE3 §3.1.2) could fund. Four sub-sections:

- **L.1 AGI-scalable alignment** between AI behaviors and human values
- **L.2 Monitoring of AI systems** to detect misbehavior and preempt failures: trojan-model detection (models that misbehave only in trigger contexts), interpretable uncertainty techniques, **hazardous capability removal techniques** (eliminating dishonesty, biological/cyber attack capabilities), AI capability evaluations of all types (behavioral, fine-tuning-based, interpretability-based, automated benchmarks, red teaming for persuasion/planning/RSI/general reasoning/CBRN/cyber), sandbox/testbed development, **AI failure mode forecasting** (developing AI systems capable of predicting failures of other AI systems), AI capability forecasting, AI alignment evaluations and behavioral evaluations
- **L.3 Robustness in the face of adversaries and unforeseen circumstances**: outer-alignment-failure detection and remediation (gameable goal specifications), **behavioral guarantees** (provable predictable behavior even under adversarial inputs)
- **L.4 Hardware-based verification**: monitoring/verification schemes for inference deployments and training runs; **chip registry schemes** for location and ownership of large clusters; hardware-enabled mechanisms for trusted verification of training compute and data; **trusted execution environments** and confidential/multi-party computing for analysis without revealing raw weights

L.4 is the most operationally tractable sub-section — chip registries and on-chip verification have well-defined development paths, and feed directly into LOE1's hardware export-control reform (§1.5.3) and the ASCCR's on-chip governance priority (LOE5 §5.5.2).

#### Annex M: Secure temporary storage of model weights (pp. 263–264)

A 2-page technical protocol enabling third-party evaluators to access proprietary frontier-model weights for private evaluation without the developer learning the evaluation protocol. The problem motivating this annex: many evaluations (especially interpretability-based) require direct weight access; if the developer's infrastructure hosts the evaluation, the developer learns the protocol and can game it. The proposed solution is a 10-step protocol with three roles — **Regulator** (operates secure server), **Developer** (uploads encrypted model weights), **Evaluator** (administers private evaluation):

1. Regulator generates one-time audited signed server in a secure setup (e.g., government cloud).
2. Developer encrypts model weights file.
3. Developer uploads encrypted blob to Regulator's server.
4. Server allows only single-user one-time inbound SSH access.
5. Developer shares encryption key with Evaluator (physical handoff recommended).
6. Regulator gives server access key to Evaluator; Evaluator rotates the key. **Regulator can no longer access its own instance.**
7. Evaluator decrypts weights and runs private evaluations.
8. (Optional) Server sends high-level non-sensitive telemetry to all three parties.
9. Any of the three parties can independently send a signed termination request to the cloud provider.
10. Regulator terminates server, deleting weights instance.

Air-gapped on-premises housing offered as alternative for highest security. Attribution: Fletcher Heisler. **At least one frontier lab has privately signaled openness to such an auditing protocol** (fn. 119 of Annex I §I.3.5). The protocol is independently citable as the operational mechanism enabling the Tier 3 third-party evaluator regime in LOE4 §4.1.3.4.3 and the corresponding voluntary commitment in Annex I §I.3.

---

### 11 — Annexes N–Q
**File:** `gladstone/PDFs/11_annexes_N-Q.pdf` | **Text:** `gladstone/text/11_annexes_N-Q.txt` | **Pages:** 20 (doc pp. 265–284) | *Annexes — operational specifics for Tier 3 AIMD licensing under LOE4 §4.1.3.4.3*

These four annexes are the implementation backbone for Tier 3 AIMD licensing. Each one corresponds to a stage of the AI development lifecycle: training approvals (N), training-stage monitoring (O), deployment approvals (P), deployment-stage monitoring (Q). Without these annexes, the LOE4 Tier 3 regime is aspirational; with them, it is an implementable protocol. The unifying logic across all four is the inversion of the normal regulatory burden of proof: **the burden is on the AIMD to demonstrate safety to the regulator's satisfaction**, not on the regulator to demonstrate harm. A second unifying logic is that **capability prediction serves a dual purpose** — it is both a safety check and a test of whether the AIMD understands its own model well enough to deploy it safely. If the AIMD cannot reliably predict its model's capabilities, that itself is grounds to pause training or deployment.

#### Annex N: Training approvals process for high-risk AI models (pp. 265–268)

The AIMD must submit a **safety case** — a structured, evidence-supported argument that the system is safe to *train* in a given scenario (a modification of the standard "safe to operate" definition) — to the regulator before beginning training. The regulator commits to confidentiality. Five sub-sections specify what's required:

- **N.1 Dangerous capability predictions** — the AIMD predicts behaviors the model will *not* display even under adverse pressure (CBRN/cyber/weaponization-relevant). Successful third-party red-team elicitation of behaviors the AIMD said wouldn't appear is treated as evidence the AIMD lacks understanding of its own model. AIMDs are also asked to privately disclose any new scaling laws they have derived.
- **N.2 Capability evaluations** — public + private evaluation suites. Private evaluations are administered by the regulator or approved third parties to prevent the AIMD from teaching to the test (mirrors LOE3 §3.2.2).
- **N.3 Capability predictions at training checkpoints** — the AIMD predicts model performance on each element of the agreed evaluation set, then reports advance predictions privately. Critical because new AI capabilities can emerge suddenly with limited advance warning; if the AIMD can't predict which dangerous capabilities will emerge, it can't apply appropriate caution.
- **N.4 Data controls** — the AIMD commits to avoiding training data that could (a) contribute to AGI-level model situational awareness or breakout capabilities, or (b) reasonably be expected to significantly increase CBRN/cyber/persuasion capabilities. The annex notes honestly that **data controls alone cannot guarantee containment**: a sufficiently capable model might infer dangerous content from very few real-world data points (echoing the increasing sample-efficiency-with-scale finding from Chapter 0).
- **N.5 Risk management** — probabilistic risk assessment similar to nuclear/aerospace safety-critical systems. Detailed threat models mapping capability predictions to weaponization and loss-of-control risk probabilities, with risk-management plans for unanticipated capabilities.

#### Annex O: Training stage monitoring for high-risk AI models (pp. 269–275)

The longest of the four annexes (7 pages). The AIMD periodically transmits model-weight snapshots to the regulator (via Annex M's secure-storage protocol) for third-party evaluation during the training run. Goal: detect emergent dangerous capabilities, *and* validate the AIMD's predictive understanding of its own model.

- **O.1 Training journal** (Alan Chan / GovAI attribution): the AIMD records the sequence of detailed interventions during training (e.g., "sudden divergence in loss led developers to perform gradient clamping") and the reason for each, available to the regulator on request.
- **O.2 Ongoing capability predictions** — tighter accuracy standard than planning-stage predictions, since informed by current and previous snapshots. **Logarithmic checkpoint cadence** (every ~1.5× increment of training compute, with the exact factor expert-set per run); hierarchical evaluation expense (cheap evaluations frequent, expensive ones in response to flags); **random snapshot timing** to prevent the AIMD from fine-tuning to pass scheduled evaluations. If measured capabilities exceed AIMD's predicted range → pause or rollback. Restart requires four submissions: a mechanistic argument for the fix, a prediction of the fix's other implications (including behaviors strongly believed not to appear post-fix), an implementation, and measurements consistent with the prediction. Rollback can mean reverting to a previous snapshot or **encrypting weights and restarting from scratch**.
- **O.3 Ongoing capability evaluations** — monitor for sharp drops in training loss (indicating emergent strong general capabilities); develop evaluations for deceptive alignment and situational awareness over time. **Fine-tuning evaluations are essential**: without fine-tuning access, evaluations almost certainly underestimate risk and "should be treated as revealing only lower bounds." Evaluators get access to activations and weights for interpretability evaluations. Government CBRN experts with classified access can participate in red teaming.
- **O.4 Model output predictions** — the AIMD attempts to predict the *specific outputs* a model will produce given specific inputs (within reasonable uncertainty bounds). Far harder than evaluation prediction; explicitly framed as "creating a benchmark for interpretability research that is difficult to undermine by superficial means."
- **O.5 Training kill switch** — at least 2 individuals per shift with kill-switch authority, continuous coverage. **At least one such individual restricted from interacting with implementations of the model** (insulation from potential manipulation — "unlikely to be a concern for today's AI models, but could become so in the future"). Explicit anti-retaliation protections for premature activation. Modeled on the rocket-launch range safety officer (citation [343]). Restart requires independent safety panel approval. **Dead-man switch alternative**: training halted at certain checkpoints by default unless oversight panel affirmatively elects to proceed — the inverse default.
- **O.6 Failed evaluation protocol** — prompt regulator notification; **regulator empowered to require all AIMDs to pause similar training runs** across the industry, and to suspend existing model deployments depending on failure nature.

#### Annex P: Deployment stage approvals for high-risk AI models (pp. 276–280)

Each **deployment context** requires a separate approval — internal use, public API, deployment with augmentations (calculator, code interpreter), defined-customer use cases. The safety case applies to the AI *system* (model + software safeguards including input filters), not the model alone. Burden of proof on the AIMD.

- **P.1 Lifecycle funds** — AIMD commits to **set aside funds for periodic third-party red teaming and deployment monitoring over the model's projected lifecycle**. Important operational detail: it converts deployment monitoring from a one-time check into ongoing AIMD-funded scrutiny.
- **P.2 Pre-deployment KYC** — if deployment context is restricted to known end-users, KYC them ahead of time to understand anticipated usage patterns.
- **P.3 Risk and contingency planning** — impact assessments specific to each deployment context, expected usage envelope, affected stakeholders, controls, **emergency response playbooks, shutdown drills**.
- **P.4 Weight storage for model evaluations** — Annex M protocol for secure third-party weight access.
- **P.5 Model augmentations** — each augmentation = separate deployment context with separate safety case. **High-risk AI models cannot be given arbitrary Internet access** — augmentations must be narrow apps executing well-defined tasks. Retrieval databases must be **updated in batches, not continuously** (each database update triggers a new approval). The stated goal: minimize the model's ability to offload computation to external aids, "thereby concealing its computations from direct oversight for potentially deceptive purposes."
- **P.6 Failed evaluation protocol** — regulator can ban model in given context; enforce **industry-wide temporary deployment bans across all Tier 3 AIMDs** if a dangerous capability is detected during one AIMD's pre-deployment evaluation; mandate evaluations on already-deployed models elsewhere. Failed evaluations may trigger **re-evaluation of tiered licensing thresholds** themselves.
- **P.7 Fine-tuning approval** — each fine-tuning instance = separate deployment approval. Significant fine-tuning compute requires training-stage monitoring during fine-tuning. **The annex's most aggressive single provision**: this requirement effectively prohibits **online learning** — a system that continuously retrains itself on inputs from the world — because each new batch of learning updates triggers a new approval process. The reasoning is technical: online-learning systems have effectively-larger context windows than LLMs (they can learn from all historical inputs), and may gain unpredictable new reasoning capabilities in sharp increments. Similar provisions extend to game-playing AI at high-risk levels and to non-text modalities.

#### Annex Q: Deployment stage monitoring of high-risk AI models (pp. 281–284)

Once deployed, the AIMD continuously monitors usage including for **internal deployments where AIMD staff are the only users**. Two structural components: (1) continuous monitoring of inputs for distribution drift and adversarial action (jailbreak attempts, model-distillation attempts where attackers train smaller models from API outputs), and (2) periodic third-party testing against novel jailbreaks/red-teaming techniques.

- **Q.1 Usage pattern reporting** — periodic input-output reports to regulator including detected high-risk interactions. **Sharp divergence between actual and anticipated usage triggers pause and investigation; gradual drift triggers a new deployment approval under updated context.** High-volume API users subject to rigorous KYC because **unrestricted API access enables model distillation** — synthetic-dataset construction can train smaller models approaching the original's performance at lower cost. Industry-wide blacklists and whitelists maintained by the regulator. Random customer interviews to build institutional understanding of typical deployment-context usage. Incident database with regulator-set severity threshold.
- **Q.2 Red teaming** — ongoing third-party red teaming; bug bounties and hackathons for public APIs; classified-CBRN-cleared government experts can participate.
- **Q.3 Failed evaluation protocol** — regulator can require industry-wide training-run pauses or deployment suspensions. AIMD generally cuts off public access. **Critical operational detail**: a **fallback model must be in place** for critical customer use cases (the annex's example: a hospital using the model for aspects of care needs an uninterrupted alternative through the same UI/API). Sandbox the failed model and run more internal evaluations. Other AIMDs may have to run evaluations on already-deployed models. Anonymized regulator disclosure to other AIMDs treated similarly to a software security vulnerability disclosure. Subject-matter expert consultation as needed. **If safety not proven to regulator's satisfaction, tiered licensing thresholds (LOE4 §4.1.3.4) themselves may be re-evaluated.**

For Dan's purposes specifically: these four annexes are what makes the Tier 3 regime enforceable rather than aspirational. Several specific provisions are independently citable and worth memorizing for advocacy. The **burden-of-proof inversion** ("the burden of proof would be on the AIMD to demonstrate to the satisfaction of the regulator that a high-risk AI model is safe to begin training") is the most quotable framing in the annexes — it is the precise operational embodiment of the "dangerous until proven safe" framing in LOE4. The **online-learning effective prohibition** in P.7 is technically interesting and not flagged in many other AI safety frameworks. The **fallback-model-for-critical-use-cases** provision in Q.3 answers a common objection ("but you can't just shut down a model used in a hospital") with operational realism. The **range-safety-officer analog with anti-retaliation protections** in O.5 is a useful cultural-borrowing model. The **lifecycle-funds requirement** in P.1 makes the regulator AIMD-funded for ongoing scrutiny rather than dependent on Congressional appropriations for monitoring labor.

The annexes' weakest element is that all of them assume FAISA exists and has authority to administer them. In 2026 conditions, none of this can happen — but the **operational protocols themselves are durable as policy templates**. State-level frameworks (CA TFAIA), philanthropic procurement standards, voluntary industry frameworks (Anthropic RSP successors, OpenAI Preparedness Framework v2+), and international agreements (EU AI Act high-risk model rules) can all borrow specific provisions from these annexes without adopting the entire FAISA architecture. The most portable provisions: capability-prediction-as-understanding-test (N.1, O.2), Annex M weight-sharing protocol (referenced from N, O, P), the burden-of-proof inversion language, the fine-tuning-as-separate-approval mechanism (P.7), and the fallback-model requirement (Q.3).

**Crucial frame to preserve in advocacy:** these annexes are **the operational layer that distinguishes Gladstone from purely-voluntary frameworks**. Anthropic's RSP, OpenAI's Preparedness Framework, and similar industry commitments specify *what* safety thresholds will trigger which actions but leave *how* implementation works largely opaque. Annexes N–Q specify the *how* — checkpoint cadence, approval mechanics, kill-switch staffing, weight-sharing protocols, online-learning treatment, fallback-model requirements. This is the layer where a regulator's actual operational competence gets tested. When defending Gladstone in advocacy contexts, reaching for these specific operational provisions (rather than the headline FAISA architecture) is the most persuasive move because it demonstrates the framework can actually be implemented, not merely declared.

---

*End of paper summaries — all 12 sections (00–11) covered.*
