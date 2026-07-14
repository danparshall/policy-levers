<!--
Section file: bills/obernolte-trahan/sections/sec-245-support-for-evaluation-of-artificial-intelligence-automation.md
Section-by-section: bills/obernolte-trahan/gaaia_section_by_section.txt
Summary written: 2026-07-14
Written by: Claude (Canary Institute automation), YOLO-mode session
-->

# SEC. 245. SUPPORT FOR EVALUATION OF ARTIFICIAL INTELLIGENCE AUTOMATION — summary

**One-line:** Directs NIST to run at least one Stevenson-Wydler prize competition, plus optional companion grants, for reproducible benchmarks measuring AI's ability to automate or augment tasks/occupations, with a $7M authorization spread across FY2026–2030.

## What it does

Within 270 days of enactment, the NIST Director must commence at least one prize competition under section 24 of the Stevenson-Wydler Technology Innovation Act of 1980 (15 U.S.C. 3719) "to develop benchmarks or similar reproducible methods to quantitatively measure the ability of artificial intelligence to automate or augment tasks or occupations" (§ 245(a)). The stated primary purpose is improving forecasts of AI's impact on workers and their retraining needs. NIST may separately award grants or cooperative agreements to support benchmark construction, validation, and maintenance (§ 245(d)), and may contract out design/administration to for-profits, nonprofits, or state/local/Tribal agencies (§ 245(e)).

## Key provisions

- Deadline: prize competition commences within 270 days of enactment (§ 245(a)).
- Consultation with Commerce, Labor, BLS, and NSF Director (§ 245(b)).
- Competition may be scoped by occupation impacted or AI capability domain (§ 245(c)(2)); may be multi-phase, e.g., design + prototype (§ 245(c)(4)).
- Category-selection criteria include informativeness re labor-market impacts, quality of submissions, complementarity with existing benchmarks, and whether benchmarks are "underfunded by private contributions relative to the public value" (§ 245(c)(3)(A)–(D)).
- Evaluation-design guardrails: NIST "shall, to the extent practicable, seek to avoid or mitigate" training-data contamination and "rapid loss of discriminatory value over time due to a metric having a low ceiling for performance" (§ 245(c)(5)(A)–(B)). This is direct acknowledgment of the saturation problem plaguing existing AI benchmarks.
- Companion-grant support items: data collection/labeling, evaluator training and rubric development, third-party replication and inter-rater reliability testing (§ 245(d)(1)–(3)).
- **Authorization: $7,000,000 total, FY2026–2030** — roughly $1.4M/year across prizes, grants, and administration (§ 245(f)).

## Who it affects

- **Empowered actors:** NIST Director (lead), Secretary of Commerce (nominal).
- **Beneficiaries:** Benchmark developers (academic labs, evaluation NGOs like METR/Apollo/Anthropic evals teams, econ groups doing O*NET-style task decomposition), and — indirectly — labor forecasters at BLS.

## Cross-references

- **Depends on / paired with:** § 241 (public workshops feed category selection via § 245(c)(3)(E)); § 101 input feeds evaluation criteria (§ 245(c)(5)(C)); § 252 employment forecasts and § 253 forecasting competition share the "improve labor forecasts" thesis but neither statutorily requires § 245 benchmarks as input.
- **Downstream hooks — weak.** § 254 is a *report* on how benchmarks/forecasts "will be incorporated" into WIOA and apprenticeship grant criteria; § 256 requires state WIOA boards to "consider" AI-related data. Neither mandates use. § 244 (AI-sensitive occupations) and § 255 (rapid adjustment study) don't cite § 245 output at all.

## Notable statutory language

> "benchmarks or similar reproducible methods to quantitatively measure the ability of artificial intelligence to automate or augment tasks or occupations, with the primary purpose of improving forecasts of the impacts that artificial intelligence may have on workers and the retraining needs of workers." (§ 245(a))

The "automate or augment" pairing is doing real work — it captures both full-replacement and productivity-assistance regimes, aligning with the METR long-tasks framing (capability-side) and Mertens/Acemoglu-style O*NET task decomposition (economics-side).

## Drafting notes & open questions

- **The $7M / 5-year authorization is small for what's asked.** ARC Prize alone runs ~$1M/year in prize money; METR's HCAST evaluations reportedly cost seven figures to build once. $1.4M/year across prizes + grants + NIST administration funds maybe one credible occupation-scale benchmark, not a portfolio.
- **"Reproducible methods" is undefined.** No requirement for open code, open data, published methodology, or contamination-audit protocols — just an aspiration in (c)(5) to "avoid or mitigate" contamination. A benchmark that ships as a private test set held by the prize winner would arguably satisfy the text.
- **Who can compete is deferred to Stevenson-Wydler § 24** — generally U.S. citizens/entities, but NIST retains structural discretion. No prize dollar amount specified.
- **No downstream teeth.** This is the load-bearing critique. The value of an AI-automation benchmark is whether policy attaches to it. Nothing in the bill *requires* § 252 forecasts, § 244 occupation designations, § 255 adjustment-program design, or § 256 state in-demand-lists to use the § 245 output. § 254 is only a report on future use. The bill funds the measurement without wiring it into any decision.
- **Task-level vs. occupation-level is left to NIST.** § 245(c)(2) permits scoping "by the occupation impacted or the capability domain" — either or both, at Director's discretion.

## Policy conversation angles

- **Worker / labor:** This is the clearest place in Subtitle B where the bill tries to institutionalize AI-labor measurement as a permanent federal capability rather than a one-off study. Supporters can frame it as the missing empirical foundation for BLS forecasts. Skeptics should press on whether $7M funds anything more than a demonstration.
- **Innovation / anti-patchwork:** Prize-competition structure and NIST-led framing align with the "light-touch, industry-partnered" federal role that Obernolte-side supporters prefer. State/local/Tribal admin partners (§ 245(e)) broaden the constituency without adding regulatory burden.
- **Safety / catastrophic-risk:** Marginal. The benchmarks are scoped to labor-market impact, not dangerous-capability evaluation. CAISI (§ 102) is the venue for the latter.
