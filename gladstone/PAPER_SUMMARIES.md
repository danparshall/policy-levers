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

[remaining sections 03–11 to be added in subsequent passes]
