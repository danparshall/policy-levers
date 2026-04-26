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

[remaining sections 04–11 to be added in subsequent passes]
