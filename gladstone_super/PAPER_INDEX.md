# Gladstone "America's Superintelligence Project" — Section Index

Full title: *America's Superintelligence Project [Redacted]*
Authors: Jeremie Harris, Edouard Harris · Gladstone AI Inc.
Published: 22 April 2025 · 62 pp. · Public/redacted version
Source URL: https://superintelligence.gladstone.ai/

Source: `gladstone_super/America's Superintelligence Project [Redacted].pdf` (full PDF). Split sections in `gladstone_super/PDFs/`. Cleaned text in `gladstone_super/text/`. Reformatted navigation TOC in `gladstone_super/TOC.md`. Per-section summaries in `gladstone_super/PAPER_SUMMARIES.md`.

## What this document is — and isn't

This is **not** a v2 of the 2024 *Defense in Depth* Action Plan (`gladstone/`). The Action Plan's frame was: *frontier AI is being built privately and needs to be regulated*. This document's frame is: *the U.S. government should run a national superintelligence project, and here is the operational design*. The upstream commitment ("the U.S. should pursue ASI") is assumed, not argued. Treating this as Action Plan v2 will lead readers wrong — the audience, the political theory, the recommended posture, and the recommended counterparties are all different.

The pivot is partly political (between February 2024 and April 2025 the Overton window on USG-led AI projects moved dramatically — Aschenbrenner's *Situational Awareness*, the USCC "Manhattan Project for AGI" recommendation, Stargate, the second Trump administration's deregulatory turn) and partly the authors' own fieldwork — they spent the year between the two reports embedded with special-forces operators evaluating data-center physical security, which gives this document its tactical-operator voice and its empirical center of gravity around supply-chain and physical-attack vulnerability rather than regulatory architecture.

| # | Section | Doc pages | Description | File (split PDF) |
|---|---------|----------:|-------------|------------------|
| 0 | Title & Table of Contents | 1–2 | Front matter | `00_TOC.pdf` |
| 1 | Executive Summary | 3–5 | 5 challenge categories: supply chain, model developer, loss of control, oversight | `01_executive_summary.pdf` |
| 2 | Introduction | 6–11 | Frames the CCP-penetration claim; argues U.S. has no real lead until labs are secured; defines scope (not whether to nationalize but how a USG-backed project would have to be structured) | `02_introduction.pdf` |
| 3 | Ch. — Data center security | 12–29 | Physical, hardware supply chain, side-channel, software supply chain, energy, export controls, AI hardware. The longest chapter; the operational core | `03_data_center_security.pdf` |
| 4 | Ch. — AI model developer security | 30–37 | Personnel security (incl. ethnic-Chinese targeting framing), cyber, emissions/TEMPEST | `04_ai_model_developer_security.pdf` |
| 5 | Ch. — AI control | 38–44 | Loss-of-control framing, control-vs-security inseparability, current-game-plan critique, AI-control ombudsman | `05_ai_control.pdf` |
| 6 | Ch. — The chain of command | 45–49 | Concentration-of-power problem; nuclear-chain-of-command analogy; oversight design questions | `06_chain_of_command.pdf` |
| 7 | Conclusion | 50–62 | Three-pillar strategy (delay CCP / secure labs / advance R&D); project ownership (DOE); funding; offensive counterintelligence necessity | `07_conclusion.pdf` |

## Quick navigation — common lookup targets

- **The "all labs CCP-penetrated" claim** (load-bearing for the entire document): pp. 3–4 (exec summary), 6–9 (introduction), 32 (model developer chapter)
- **$20–30K attack on $2B data center** (most cited single fact): pp. 12–14
- **ASPEED BMC concentration** (70% Taiwan, soft underbelly): pp. 17–18
- **CCP $275B PPP investment in AI infrastructure**: pp. 16, 47, 51
- **MSS targeting of ethnic Chinese (incl. U.S. citizens)**: pp. 31–32
- **OpenAI security-vulnerability whistleblower account** (anonymous lab researcher; almost certainly o1-era): pp. 34–35
- **10–80% loss-of-control estimate range** from 12 lab researchers: p. 39
- **o1-preview Docker container breakout**: p. 38
- **"Pathological liar … sociopath" CEO passage** (unnamed but identifiable): pp. 45–46
- **DOE as project owner**: p. 56
- **Three-pillar strategy** (delay CCP / secure labs / advance R&D): pp. 53–54
- **"No version of a national superintelligence project that isn't integrated with active, offensive operations"**: p. 59

## Center of gravity

The Data Center Security chapter (18 pp) is the document's empirical core — it is where the 12 months of fieldwork show up most concretely, and where the most independently citable facts live (supply-chain concentrations, attack costs, BMC vulnerability, packaging dependence on Taiwan). The AI Control chapter is the document's intellectual core — it makes a case that control problems and security problems are inseparable, which is the document's most interesting structural argument. The Chain of Command chapter is the document's underdiscussed center — it is the only place in the Gladstone corpus where the *concentration-of-power problem* is treated as a first-class concern rather than as a downstream consequence of weaponization or loss-of-control, and is the chapter most useful to advocates whose framing differs from Gladstone's.

## How this document differs from the 2024 Action Plan

| | 2024 Action Plan | 2025 Superintelligence Project |
|---|---|---|
| **Premise** | Frontier AI is being built privately; it needs regulation | The U.S. government should run a national ASI project; here is the operational design |
| **Audience** | State Department (commissioning agency); Congress; regulators | National-security executive branch; intelligence community; project planners |
| **Posture** | Defense-in-depth, multilateral, treaty-anchored | Offensive counterintelligence from day one; unilateral; allies as a secondary layer |
| **Counterparty** | Private frontier labs (regulated) | Private frontier labs (security-vetted contractors in a USG-owned project) |
| **Theory of CCP** | A peer competitor whose progress lags 6–12 months | A peer competitor that has already operationally compromised U.S. labs and is racing |
| **Structural unit** | Regulatory tier (FAISA's 4 levels) | Physical site (a new gigawatt data-center build) |
| **Time horizon** | 1–4 year regulatory rollout | "Break ground within months" |
| **Funder model** | Federal appropriation, FAISA fees | Private investor returns + DOE direct funding for security/control/oversight |
| **What's left out** | Operational physical security; offensive ops; chain-of-command design | Multilateral coordination; legal-liability framework; standards-development |

The two documents are complementary in principle — one is the regulatory architecture, the other is the operational architecture — but they were written for political environments that increasingly diverge. By mid-2026, the political environment has moved further toward the *Superintelligence Project*'s framing on the racing question, but further away from the project on the *security* question (the December 2025 EO on federal preemption of state AI safety laws cuts against both Gladstone documents).
