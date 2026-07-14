<!--
Section file: bills/obernolte-trahan/sections/sec-424-liquid-cooling-development-and.md
Section-by-section: bills/obernolte-trahan/gaaia_section_by_section.txt
Summary written: 2026-07-14
Written by: Claude (Canary Institute automation), YOLO-mode session
-->

# SEC. 424. LIQUID COOLING DEVELOPMENT AND SCALABILITY — summary

**One-line:** Directs GAO (with an industry-heavy advisory committee) to study liquid cooling in AI data centers and report to DOE and Congress; DOE then assesses that report and recommends R&D priorities.

## What it does

Not later than 90 days after enactment, the Comptroller General must launch a review of liquid cooling for data centers — the need for R&D, current market/technological/regulatory conditions, and technical characteristics across cooling modalities (§ 424(a)(1)). The review is prepared by a GAO-established advisory committee dominated by industry and technical experts (§ 424(a)(4)), and results in a report to the Secretary of Energy plus the House SST/E&C and Senate ENR committees. Within 180 days of receiving that report, DOE must assess it and send Congress its own report on "the importance of liquid cooling with respect to the United States remaining the global leader in AI" and R&D recommendations for liquid cooling and waste-heat reuse (§ 424(b)).

## Key provisions

- **90-day trigger for GAO review** (§ 424(a)(1)); **180-day follow-on DOE assessment** after GAO submits (§ 424(b)). Total timeline to Congress: ~9 months post-enactment, assuming no slippage.
- **Scope of "liquid cooling" is narrow-and-deep on two modalities.** The section defines and requires cross-density-band comparison of single-phase and two-phase direct-to-chip vs. single-phase and two-phase immersion (§ 424(a)(2)(C), (c)(3), (c)(5), (c)(8)–(9)). **Rear-door heat exchangers are not named** — a notable gap given they are the dominant retrofit path for existing air-cooled halls.
- **Failure-mode analysis required**, including pump failures and fluid leaks, "including with respect to colocation environments" (§ 424(a)(2)(B)(iii)).
- **Energy-adjacent metrics but no water metrics.** The review must quantify "avoided costs of energy, including deferred and avoided new electric transmission and infrastructure upgrades" (§ 424(a)(2)(A)(iv)) and "increased compute capacity as a result of enabling increased utilization of energy for computing workloads" (§ 424(a)(2)(B)(i)). Waste-heat reuse is defined (§ 424(c)(4)) and studied (§ 424(a)(2)(A)(iii); § 424(b)(2)(B)(ii)). **Water consumption / withdrawal is nowhere in the statutory element list** — even though evaporative make-up water is the single loudest community-level complaint about hyperscale AI data centers.
- **Advisory committee tilts private-sector** (§ 424(a)(4)(B)): experts in AI factories, IT equipment, and software; plus representatives of hardware manufacturers, data-center owners/operators, coolant-fluid producers, and AI-factory developers. No labor, no environmental-justice, no ratepayer-advocate slots; National Labs and academia enter only through downstream consultation (§ 424(a)(4)(C)).
- **Deliverables include reference architectures** for rack-, row-, and room-level liquid distribution by density band and cooling process (§ 424(a)(2)(E)) — a de facto federal design-guidance role for GAO, which is unusual.

## Who it affects

- **Regulated parties:** None directly — study only, no enforcement mechanism.
- **Empowered actors:** GAO (lead), Secretary of Energy (follow-on assessor), and the advisory committee.
- **Beneficiaries:** Hyperscalers, colocation operators, and coolant/hardware vendors — who get a GAO-branded reference architecture and a DOE-endorsed R&D wish list. Communities living next to data centers are not beneficiaries under the statute as written.

## Cross-references

- **Defined terms used:** "AI" via NAII Act 2020 § 5002 (15 U.S.C. 9401) (§ 424(c)(1)); "National Laboratory" via Energy Policy Act 2005 § 2 (42 U.S.C. 15801) (§ 424(c)(7)). Section-local defs: direct-to-chip, immersion, single-phase, two-phase, heat-reuse, liquid cooling (§ 424(c)(3)–(9)).
- **Depends on / paired with:** § 421 (Public Data for AI Systems), § 422 (Federal Grand Challenges — energy efficiency is a listed challenge area), § 423 (NAIRR — the federal compute resource whose cooling this section studies). Thematically continuous with § 122 (GAO Report on Regulatory Impediments to AI Innovation), which flags statutes/regulations that "unduly burden AI infrastructure (including energy)" — § 122 is the political vehicle for identifying friction, § 424 is the technical companion identifying what the frictionless infrastructure looks like.

## Notable statutory language

> "Considerations for Congress regarding the importance of liquid cooling with respect to the United States remaining the global leader in AI." (§ 424(b)(2)(A))

The framing is telling: the DOE report is scoped to global-leadership arguments, not to grid impact, community impact, or worker impact. That is the political theory of the case in a sentence — thermal management is being pitched to Congress as a competitiveness question first, and every other framing has to bootstrap off that.

## Drafting notes & open questions

- **Missing water accounting.** Liquid cooling reduces on-site electricity for cooling but often trades that against on-site or upstream water consumption (evaporative towers, adiabatic assists). The statutory review elements enumerate energy avoided but never water consumed. If the point is honest infrastructure accounting, this is a real omission.
- **"AI factories" appears without definition.** The advisory-committee slots (§ 424(a)(4)(B)(i)(I), (B)(ii)(IV)) reference "AI factories or data centers" and "developers of AI factories," but the term is not defined in § 424(c). Presumably it maps to the industry usage popularized by NVIDIA circa 2024, but the statute does not say so.
- **No rear-door heat exchangers.** The comparison in § 424(a)(2)(C) is direct-to-chip vs. immersion. Rear-door and hybrid air-plus-liquid hall retrofits are the near-term deployment path for the installed base and would benefit most from federal reference architectures. Their absence narrows the study's practical usefulness for existing sites.
- **No funding, no mandate to deploy.** § 424 is study + report + more study. The teeth, if any, would have to come from a downstream authorization or from DOE choosing to fund the R&D pipeline the assessment recommends. As written, this is a signal-sending section, not an operative one.

## Policy conversation angles

- **Innovation / anti-patchwork:** Fits cleanly into the "unblock AI infrastructure" story that runs through Title I (§ 122) and Title IV (§§ 421–424). Supporters of federal-preemption framing can point to § 424 as evidence Congress is doing the technical homework before regulating siting or grid interconnect.
- **Worker / labor:** Section as written has no labor angle. The advisory committee has no worker representation, and the failure-mode analysis (pump failures, fluid leaks, colocation environments) does not require any occupational-safety input despite obvious relevance for data-center technicians.
- **Environmental / community:** The most visible gap. Communities pushing back on hyperscale sites cite water withdrawal, aquifer stress, and heat-plume impacts. § 424 studies waste-heat reuse (which is a mitigation) but not water consumption (which is the harm). Amendable in markup by adding a water-accounting element to § 424(a)(2) and an environmental-justice / ratepayer-advocate slot to § 424(a)(4)(B).
