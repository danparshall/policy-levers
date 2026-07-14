<!--
Section file: bills/obernolte-trahan/sections/sec-244-modernizing-access-to-artificial-intelligence-related-labor-market-data.md
Section-by-section: bills/obernolte-trahan/gaaia_section_by_section.txt
Summary written: 2026-07-14
Written by: Claude (Canary Institute automation), YOLO-mode session
-->

# SEC. 244. MODERNIZING ACCESS TO AI-RELATED LABOR MARKET DATA — summary

**One-line:** Directs the Census Bureau to run a 4-year pilot producing a recurring job-to-job worker-flow series for at least 15 Labor-designated AI-sensitive occupations, and to assess (but not build) secure remote researcher access to underlying microdata — all with no new money.

## What it does

The Secretary of Commerce, acting through the Census Bureau Director and in consultation with the Secretary of Labor and the Chief Statistician of the United States, must publish a statistical series on flows of workers between occupations — modeled on Census's existing J2J Explorer but at a more detailed SOC level — restricted to a Labor-designated list of AI-sensitive occupations (§ 244(a)(2)). Separately, BLS's Commissioner must assess proposals to give researchers secure remote access to individual-level records so that academic work on AI's workforce impact can proceed (§ 244(b)). No new appropriations are authorized (§ 244(c)).

## Key provisions

- **Designation.** Secretary of Labor publishes an initial list within 240 days of enactment and re-designates at least every 2 years; list must contain "not fewer than 15" occupations at the 6-digit or 4-digit SOC level, or a similar scheme if more feasible (§ 244(a)(3)(A)).
- **Designation factors.** Degree of AI-driven dislocation or shortage, analytical value for evaluating AI-workforce assumptions, feasibility of collecting transitions data, and insufficiency of existing data (§ 244(a)(3)(B)).
- **First series in 18 months**, then at least 1 quarter per fiscal year thereafter (§ 244(a)(5)).
- **Data sources.** Federal surveys, administrative records, interagency data linkages; voluntary private partnerships including payroll data; small-scale state/local pilots that could collect enhanced wage-record elements such as job titles or occupation codes (§ 244(a)(4)).
- **Escape hatch.** If the Director determines the series is impracticable or its cost substantially exceeds its value, he/she publishes a barriers-and-cost-benefit report instead of the series (§ 244(a)(6)).
- **Sunset.** Subsection (a) obligations terminate 4 years after enactment (§ 244(a)(7)).
- **Secure remote access.** BLS Commissioner, with Chief Statistician and Census Director, must publish within 1 year a report assessing proposals to give researchers unit-record access — potentially through NSF's National Secure Data Service demonstration project (§ 244(b)).
- **Zero-dollar mandate.** "No additional amounts are authorized to be appropriated to carry out this section" (§ 244(c)).

## Who it affects

- **Regulated parties:** None directly. Implementation burden falls on Census, BLS, and DOL.
- **Empowered actors:** Secretary of Labor (occupation designation), Census Director (series production or escape-hatch report), BLS Commissioner (secure-access assessment). NSF potentially indirectly, via NSDS.
- **Beneficiaries:** Workforce researchers, WIOA planners, adjustment-assistance program designers, and — eventually — displaced workers whom better transition data would help route into targeted retraining.

## Cross-references

- **Defined terms used:** "Artificial intelligence" (assumed § 101, not separately re-defined here). Note: § 244 does not itself define "AI-sensitive occupation" — the phrase appears in § 252's section-by-section but not in § 244's operative text, which uses "occupations impacted by artificial intelligence."
- **Depends on / paired with:**
  - **§ 241** — public comment and expert workshops feed the (a)(6) practicability determination and (b) secure-access assessment.
  - **§ 243** — AI Workforce Research Hub would be a natural consumer of the series.
  - **§ 252** — also requires Secretary of Labor to designate "at least 15 AI-sensitive occupations every two years." Whether § 252 and § 244 lists are the same list is not stated; drafters likely intend alignment but the bill is silent.
  - **§ 248** — standardized data elements for workforce reporting.

## Notable statutory language

> "The list shall include not fewer than 15 occupations designated at the 6-digit or 4-digit Standard Occupational Classification code level, or according to a similar occupation code scheme if the Secretary of Labor determines that designation in accordance with that scheme would be more feasible or valuable." (§ 244(a)(3)(A))

> "No additional amounts are authorized to be appropriated to carry out this section." (§ 244(c))

## Drafting notes & open questions

- **15 occupations is a very narrow window into a broad phenomenon.** SOC 2018 has ~867 detailed (6-digit) occupations; 15 is ~1.7% of the taxonomy. If Mertens-style aggregate productivity effects and the diffuse cross-occupation task-shift patterns METR and Parshall / Lopez-Luzuriaga document are real, a 15-occupation panel will catch obvious targets (paralegals, translators, software developers, radiologists) but is structurally blind to the broad, low-per-occupation displacement pattern that is the actual policy concern. The "not fewer than" floor gives DOL room to expand, but the § 244(c) zero-appropriation clause is a hard budget lid that pushes toward the floor, not the ceiling.
- **Machine-readability is not required here.** § 252 mandates a "public, machine-readable archive"; § 244 does not. Given both are produced by the same agency ecosystem and often about the same occupations, this asymmetry is probably an oversight worth fixing in markup.
- **Statistical disclosure limitation (SDL) is not addressed.** The section allows administrative records, payroll data, and enhanced wage records — all high-reidentification-risk sources — without an explicit SDL requirement. Presumably CIPSEA and Title 13 govern by default, but explicit language would harden the privacy posture, especially at 6-digit SOC × geography intersections where cell sizes get small fast.
- **Escape hatch is broad.** § 244(a)(6) lets the Director substitute a report if the series is "not practicable" or if cost "substantially" exceeds value — undefined thresholds, no Congressional signoff required. Combined with (c)'s zero-appropriation clause, this is a plausible off-ramp for the whole pilot.
- **4-year sunset with no reauthorization mechanism.** (a)(7) ends the obligation after 4 years; nothing in the section directs Congress or the agencies to evaluate whether to continue. Given a first release at 18 months and at most quarterly-per-year cadence thereafter, the pilot generates ~3 statistical vintages before the authority lapses.
- **§ 244 vs § 252 designation lists.** Both require SecLabor to designate ≥15 occupations every 2 years; neither section explicitly says they are the same list. Aligning them (via cross-reference) would reduce implementation burden and force consistency between the forecasts (§ 252) and the observed transition data (§ 244) used to evaluate them.

## Policy conversation angles

- **Worker / labor:** This is the operative section for empirically observing AI-driven job-to-job transitions — a prerequisite for evidence-based adjustment assistance (§ 255), state in-demand list updates (§ 256), and WIOA targeting (§ 254). Worth flagging that the mechanism is a small, unfunded, 4-year pilot with a broad off-ramp; the "at least 15" floor and no-new-money constraint together mean the data infrastructure needed to actually verify displacement claims may not materialize at usable scale.
- **Innovation / anti-patchwork:** Voluntary private partnerships for payroll data (§ 244(a)(4)(B)) provide a light-touch alternative to mandatory reporting. Industry supporters can point to this as evidence the bill favors cooperation over compulsion for labor-market data.
- **Safety / catastrophic-risk:** Tangentially relevant. Reliable transition data would help distinguish "AI transformed this occupation" from "AI eliminated this occupation" — an empirical question the broader risk debate presumes rather than measures.
