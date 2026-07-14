<!--
Section file: bills/obernolte-trahan/sections/sec-252-detailed-employment-forecasts-for-ai-sensitive-occupations.md
Section-by-section: bills/obernolte-trahan/gaaia_section_by_section.txt
Summary written: 2026-07-14
Written by: Claude (Canary Institute automation), YOLO-mode session
-->

# SEC. 252. DETAILED EMPLOYMENT FORECASTS FOR AI-SENSITIVE OCCUPATIONS — summary

**One-line:** Requires SecLabor to designate at least 15 AI-sensitive 6-digit SOC occupations every 2 years and publish annual 20th-80th percentile prediction-interval employment forecasts at 2-, 4-, and 8-year horizons, with benchmark comparisons, proper-scoring-rule accuracy evaluations, and a machine-readable public archive — funded at $18M over FY2026-2030 and sunsetting after 5 years.

## What it does

Within 240 days of enactment and at least every 2 years thereafter, the Secretary of Labor publishes a Federal Register list of not fewer than 15 occupations at the 6-digit SOC level for which "a deeper analysis of the impact of artificial intelligence" is warranted (§ 252(a)(1)). Six months after the first list and annually thereafter, an "assigned entity" — the BLS Commissioner by default, or the § 243 AI Workforce Research Hub if the Secretary designates it — publishes prediction-interval forecasts for each listed occupation at 2-, 4-, and 8-year horizons (§ 252(b)(1)). Forecasts must be compared against benchmark methods, evaluated within 120 days of ground-truth data release using a proper scoring rule, and archived in a machine-readable public repository (§ 252(b)(6), § 252(c)).

## Key provisions

- **Cadence.** ≥15 occupations every 2 years (§ 252(a)(1)); annual forecast reports (§ 252(b)(1)); accuracy evaluation within 120 days of ground-truth data (§ 252(b)(6)(A)).
- **Selection consultation.** Workforce Information Advisory Council and OSTP, plus § 241 workshop input (§ 252(a)(3)).
- **Prediction interval.** Default 20th–80th percentile range; alternate ranges (including percentage growth) allowed with Secretary approval and a 30-day public justification (§ 252(b)(2)).
- **Scope exclusion.** Forecasts must exclude "future acute shocks unrelated to the economic impacts of artificial intelligence, including recessions, wars, or pandemics" (§ 252(b)(3)).
- **Benchmark forecasts.** Required; may include trend-extrapolation, generative-AI language models, or other methods (§ 252(b)(4)) — notable that LLMs are explicitly named as an eligible forecasting benchmark.
- **Method transparency.** Data sources, assumptions, modeling steps, and prioritized data gaps must be disclosed (§ 252(b)(5)).
- **Proper scoring rule.** Evaluations must score per-forecast accuracy, aggregate calibration, and benchmark comparison (§ 252(b)(6)(B)).
- **Machine-readable archive.** § 508 + WCAG compliant (§ 252(c)).
- **Implementation report at 4 years** (§ 252(d)); **sunset at 5 years** except evaluations continue for 10 (§ 252(e)).
- **Funded.** $18M authorized FY2026-2030 (§ 252(f)).

## Who it affects

- **Regulated parties:** None directly.
- **Empowered actors:** SecLabor (occupation designation); BLS Commissioner or § 243 AI Workforce Research Hub (forecasting + evaluation); OSTP and WIAC (consultation).
- **Beneficiaries:** Workforce researchers, WIOA planners (§ 254, § 256), Rapid AI Adjustment Assistance program design (§ 255), and outside forecasters who can benchmark against a public record.

## Cross-references

- **Defined terms used:** "Artificial intelligence" (assumed § 101). Notably, "AI-sensitive occupation" is not defined in § 101 or elsewhere — § 252(a)(1) originates the concept operationally via the SecLabor designation process.
- **Depends on / paired with:**
  - **§ 241** — workshop input feeds occupation selection (§ 252(a)(3)(B)).
  - **§ 243** — AI Workforce Research Hub is the alternate assigned entity (§ 252(b)(7)(B)).
  - **§ 244** — also requires SecLabor to designate ≥15 occupations every 2 years for a Census-produced worker-flow series; whether the two lists must align is not stated in either section.

## Notable statutory language

> "form a range from the 20th to 80th percentile of forecast projected employment for the occupation" (§ 252(b)(2)(A)(i))

> "Such benchmark forecasts may include— (A) trend-extrapolation models; (B) generative artificial intelligence, such as language models; or (C) other methods the assigned entity determines appropriate" (§ 252(b)(4))

> "an online, public, and machine-readable archive" (§ 252(c))

## Drafting notes & open questions

- **This section has real teeth compared to most of Title II.** Prediction intervals, mandatory proper-scoring-rule accuracy evaluation, benchmark comparisons, and a machine-readable public archive are a genuine measurement commitment — a departure from BLS's default of unqualified point-estimate Employment Projections. The forecasts are also scored *against* alternative methods (including LLM forecasts), which builds in a comparative-performance signal rather than a self-graded output.
- **Horizons are shorter and more granular than BLS's flagship product.** BLS Employment Projections run on a 10-year horizon and refresh biennially; § 252 requires 2/4/8-year horizons refreshed annually. The 2-year horizon in particular allows accuracy evaluation *within* the timescale of any single administration — a real feedback loop that 10-year projections structurally cannot provide.
- **Execution risk is high.** BLS's existing 10-year projections have systematically underestimated AI impact per Mertens et al. (2026) — task-level automation exposure suggests aggregate effects the occupation-level projections do not capture — and METR (2025) documents AI capability doubling every ~7 months, a rate that outpaces any 8-year forecast window's stability. A 20th–80th interval calibrated to historical variance may be too narrow to bracket the actual outcome distribution under rapid capability growth. The proper-scoring-rule evaluation will *detect* this miscalibration; whether it will meaningfully update forecaster methodology within the 5-year sunset is a separate question.
- **Machine-readable archive is required here but not in § 244.** Both sections are produced by the same DOL/BLS ecosystem, often about the same occupations. The § 244 summary flags this asymmetry as likely oversight; § 252's explicit § 508/WCAG-compliant requirement should be replicated in § 244 in markup.
- **Acute-shock exclusion is defensible but load-bearing.** § 252(b)(3) excludes recessions, wars, and pandemics from the forecast scope so that scoring reflects AI-specific accuracy. In early forecast years, however, AI-driven displacement could plausibly present *as* a shock in the data, and the boundary between "AI economic impact" and "AI-adjacent acute event" (e.g., an AI-triggered financial disruption) is undefined.
- **Funded, unlike § 244.** $18M over 5 years (§ 252(f)) is modest but real — enough to staff a small forecasting group at BLS or the § 243 Hub. Contrast § 244(c)'s zero-appropriation clause for the paired worker-flow series.
- **Sunset in 5 years with no reauthorization mechanism.** § 252(e) ends the forecasting obligation 5 years after enactment; only the evaluation-and-archive obligations continue (to 10 years). If AI displacement measurement is a durable policy need — and Canary's working thesis is that it is — the sunset should be revisited in markup.
- **Assigned-entity flexibility is a design choice with tradeoffs.** § 252(b)(7)(B) lets the Secretary route forecasting to the § 243 Hub instead of BLS. This creates capacity for methods BLS doesn't currently use (LLM-based forecasts, prediction markets, etc.) but sidesteps BLS's statutory independence and institutional forecasting practice.

## Policy conversation angles

- **Worker / labor:** This is the strongest measurement provision in Subtitle B and the empirical backbone for § 254 (WIOA targeting), § 255 (Rapid AI Adjustment Assistance), and § 256 (state in-demand lists). Frame positively: annual prediction-interval forecasts with public scoring are a real advance over the status quo of unqualified point estimates on 10-year horizons. Push back on scope: 15 occupations is ~1.7% of the ~867 detailed SOC codes, and the 5-year sunset limits the forecasting series to roughly 4 vintages before authority lapses.
- **Innovation / anti-patchwork:** The section-by-section framing here is workforce, not preemption — this is a federal capacity build, not a state-law override. Industry supporters have little to praise or criticize; it is a government-internal measurement mandate.
- **Safety / catastrophic-risk:** Tangentially relevant. A public archive of prediction-interval forecasts scored against LLM-generated benchmarks is one of the few provisions in the bill that would produce a defensible empirical basis for "how fast is AI actually displacing labor" — a question the risk debate presumes but rarely measures.
