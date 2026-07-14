<!--
Section file: bills/obernolte-trahan/sections/sec-253-forecasting-prize-competition.md
Section-by-section: bills/obernolte-trahan/gaaia_section_by_section.txt
Summary written: 2026-07-14
Written by: Claude (Canary Institute automation), YOLO-mode session
-->

# SEC. 253. FORECASTING PRIZE COMPETITION — summary

**One-line:** Directs NSF to run a recurring (>= every 6 months) prize competition scoring short-horizon forecasts and their rationales on AI labor-market questions, funded at $6M total across FY2026–2030 and sunsetting after 5 years.

## What it does

The NSF Director "shall establish a recurring prize competition to incentivize accurate forecasts and informative rationales for short-horizon questions" bearing on AI's labor-market implications (§ 253(a)). Questions must be released and resolved/scored "not less frequently than every 6 months" (§ 253(d)). Scoring uses a proper scoring rule for accuracy plus a separate/joint rubric for "informativeness or persuasiveness of rationales, models, or other justifications" (§ 253(e)). Eligibility is U.S. citizens/permanent residents or U.S.-incorporated entities; federal employees acting within scope are excluded (§ 253(b)).

## Key provisions

- **Three named question domains** (§ 253(c)): (1) model performance on automation/augmentation benchmarks; (2) AI adoption indicators (e.g., share of firms deploying generative AI); (3) occupation-level employment changes and AI-related mass-layoff reports. Residual "other metrics" category at Director's discretion in consultation with Labor.
- **Consultation partners** (§ 253(f)(1)): Labor, OSTP, and "at least 1 organization that has operated scored crowd elicitation forecasting platforms or contests" — contemplates Metaculus / Good Judgment Inc. / INFER-style involvement without naming them.
- **Public annual summary + 5-year data retention** (§ 253(g)(1)–(2)); consolidated effectiveness report to Congress within 3 years (§ 253(g)(3)).
- **Authorization: $6M total, FY2026–2030** (§ 253(h)); 5-year sunset (§ 253(i)).

## Who it affects

- **Empowered actors:** NSF Director (lead); Labor Secretary and OSTP Director (consult).
- **Beneficiaries:** U.S.-based forecasters, superforecaster networks, academic LLM-forecasting groups, and crowd-forecasting platforms brought in as consultants or administrators.

## Cross-references

- **Defined terms:** "artificial intelligence" via § 101.
- **Paired with:** § 245 (NIST benchmarks) feeds question domain (1); § 252 (BLS occupation forecasts) feeds (3); § 246–§ 247 (voluntary reporting, federal-survey AI questions) feed (2). § 241 workshops surface "best practices for scored crowd-sourced forecasting."
- **Downstream:** § 254 WIOA/apprenticeship report references "forecasts developed under the Act"; whether § 253 output counts is unspecified.

## Notable statutory language

> "The Director shall use evaluation criteria … that include, either jointly or as part of separate prize categories — (1) forecasting accuracy using a proper scoring rule; and (2) informativeness or persuasiveness of rationales, models, or other justifications offered in response to questions." (§ 253(e))

Separating rationale-quality from calibration is unusual in federal prize authorities and echoes recent LLM-forecasting research (Halawi et al., Schoenegger et al.) isolating reasoning quality from Brier score.

## Drafting notes & open questions

- **$6M / 5 yr / semi-annual = ~10 rounds at ~$600k/round gross; after NSF admin, ~$300–500k/round in actual prize dollars.** Metaculus-tournament scale (top prizes $10k–$50k), not ARC-Prize scale ($1M+). Fine for eliciting forecaster attention; too small to move a serious LLM-forecaster research group's roadmap. A pilot, not a durable program.
- **No prize-purse minimum, no minimum participants or questions.** A single question every 6 months with a $100 prize satisfies § 253(a)+(d) as written.
- **"Section 101" reference in § 253(f)(2) reads as a drafting error.** § 101 is Definitions; the referent that fits ("input … about best practices for … scored crowd-sourced forecasting") is § 241, whose RFC (§ 241(a)(3)(C)) and workshops (§ 241(b)(1)(B) invites "scored-forecasting/expert-elicitation practitioners") are the actual mechanism. Flag for markup.
- **"Persuasiveness of rationales" is scoreable but subjective** — no specification of judges (peer? expert panel? LLM?), rubric publication, or handling of disagreement. This is where the program stands or falls.
- **Public vs. private tournament left open.** § 253(g)(1) only requires annual public results; nothing about in-flight tournament visibility, which is core to Metaculus/GJI value.
- **No integration mandate with § 252.** BLS occupation forecasts and prize forecasts are statutorily disconnected.
- **Federal-employee exclusion (§ 253(b)(4))** forecloses growing in-house forecasting capacity through the competition; it would have to be procured.

## Policy conversation angles

- **Worker / labor:** Pairs with § 241, § 244, § 246, § 252. Theory of change: a public tournament produces sharper short-horizon signals on AI adoption and displacement than BLS's slower cycle. Whether $6M funds more than a demonstration is the critical question.
- **Innovation / anti-patchwork:** Prize framing plus contracting-out language (§ 253(f)(1)) is low-regulatory-burden and consistent with Obernolte-side preferences.
- **Safety / catastrophic-risk:** Marginal. Question scope is labor-market; model-benchmark forecasting (§ 253(c)(1)) is scoped to "automation or augmentation benchmarks," not FRA/CBRN evals.
