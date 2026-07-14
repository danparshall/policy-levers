<!--
Section file: bills/obernolte-trahan/sections/sec-423-national-artificial-intelligence-research.md
Section-by-section: bills/obernolte-trahan/gaaia_section_by_section.txt
Summary written: 2026-07-14
Written by: Claude (Canary Institute automation), YOLO-mode session
-->

# SEC. 423. NATIONAL ARTIFICIAL INTELLIGENCE RESEARCH RESOURCE — summary

**One-line:** Codifies NAIRR in statute — governance (Steering Subcommittee at OSTP + Program Management Office at NSF + nongovernmental Operating Entity), resource categories (compute, data, training, testbeds), eligibility (US researchers, non-profits, agencies, FFRDCs, and small/young private firms — foreign-adversary-nationals excluded, large frontier developers not eligible), and a safety/security priority for a "significant percentage" of compute — but authorizes **zero appropriated dollars**, relying entirely on donated cash and in-kind contributions.

## What it does

Section 423 turns the NAIRR pilot (running under NSF since January 2024) into standing statute. It does this in two moves: (a) amends § 5103 of the FY2021 NDAA (15 U.S.C. 9413) to insert a new **NAIRR Steering Subcommittee** inside the existing Interagency Committee, chaired by the OSTP Director; and (b) amends the National AI Initiative Act of 2020 (15 U.S.C. 9401 et seq.) by adding a new **Title LVI** with five sections: § 5601 definitions, § 5602 establishment/governance, § 5603 resources, § 5604 processes and procedures, § 5605 funding. NSF must stand up NAIRR within one year of enactment (§ 5602(a)); a Program Management Office at NSF (≥3 FTE) issues an RFP and selects a nongovernmental Operating Entity through a "competitive and transparent process" (§ 5602(b)(3)(A)(ii)).

## Key provisions

- **Three-layer governance:** OSTP-chaired NAIRR Steering Subcommittee (§ 5103(e)) → NSF-housed Program Management Office (§ 5602(b)) → nongovernmental Operating Entity (§ 5602(b)(3)(A)(ii)) — may be an FFRDC or consortium.
- **Resource categories** (§ 5603(b)): (1) mixed compute — on-prem, cloud, hybrid, benchmarking, open-source software environment, an **API providing "structured access to artificial intelligence models"** (§ 5603(b)(1)(E)); (2) data — interoperability standards, curated datasets, an **"artificial intelligence open data commons"** (§ 5603(b)(2)(D)), federal statistical data via the 44 U.S.C. § 3583(a) SAP; (3) educational tools and STEM outreach; (4) AI testbeds coordinated with NIST.
- **Eligible users** (§ 5604(a)(2)(B)): US-based institutions of higher ed; nonprofits; executive agencies; FFRDCs; **private-sector entities that are both <7 years old and <500 employees** (§ 5604(a)(2)(B)(v)); startups/emerging-tech companies designated by Commerce, SBA, or NIST; consortia of the above.
- **Excluded users** (§ 5604(a)(3)): individuals employed by or acting for countries listed at 10 U.S.C. § 4872(f)(2) (currently PRC, Russia, DPRK, Iran).
- **Safety priority** (§ 5604(b)(3)(B)): "a significant percentage of the annual allotment" of compute must go to projects primarily focused on "the safety and security of artificial intelligence systems, or other topics that demonstrate the project at issue is in the public interest." Ranked priority when demand exceeds supply (§ 5604(b)(3)(C)).
- **Fee schedule** (§ 5604(e)): must include a free tier (§ 5604(e)(2)); may cost-recover beyond it.
- **Funding** (§ 5605): "the NAIRR is authorized to accept and utilize donations of cash, services, and personal property from private sector entities." That is the entire funding section. No appropriation authorized, no in-kind mechanism from federal agencies (though § 5103(e)(7) and § 5602(b)(3)(A)(ix) contemplate agency contributions of resources or funding).

## Who it affects

- **Regulated parties:** None. NAIRR is capacity, not obligation.
- **Empowered actors:** OSTP Director (chairs Steering Subcommittee); NSF Director (establishes NAIRR, runs PMO, enforces eligibility); the Operating Entity (day-to-day operations, portal, training, security tiering); NIST (testbeds, cybersecurity framework baseline); CISA + OMB (co-consult on security tiers, § 5604(d)); designated statistical agencies + Chief Statistician (audit federal statistical data resources, § 5604(b)(1)(B)).
- **Beneficiaries:** Academic AI researchers, students, HBCUs and MSIs (through the outreach mandate § 5603(b)(3)(C)), FFRDCs, small/young AI startups (<500 FTE, <7 years), federal AI staff (§ 5602(b)(3)(B)(x) — resources available to Congress and agencies for AI education). Frontier developers (OpenAI, Anthropic, Google DeepMind, Meta, xAI) are **not eligible** — all exceed the size and age thresholds.

## Cross-references

- **Defined terms used:** "Artificial intelligence" per § 101; "AI testbed" defined at § 5601(2) by reference to NIST Act § 22A(g) (15 U.S.C. § 278h-1(g)); "NAIRR" defined at § 5601(5) by reference to NAII Act § 5106(g) (not amended here).
- **Depends on / paired with:**
  - **§ 421 (public data / federal data)** — the "open data commons" and federal-statistical-data intake at § 5603(b)(2)(D)–(E) is where § 421-cleared data would land for research use.
  - **§ 422 (grand challenges)** — challenge participants are a natural consumer of NAIRR compute and datasets.
  - **§ 102 (CAISI)** — NIST's testbed authority (§ 5603(b)(4)) sits alongside CAISI's evaluation mission; the two must be reconciled operationally.
  - **§ 431 (research security)** and NSPM-33 conformance is explicitly required (§ 5604(f)).
  - **§ 5605 funding** vs. **§ 123** (resources for AI regulation) and any anticipated NSF authorization — § 423 does none of that work itself.

## Notable statutory language

> "To carry out this title, the NAIRR is authorized to accept and utilize donations of cash, services, and personal property from private sector entities." (§ 5605)

That one sentence is the entire funding authority. Compare the NAIRR Task Force final report (NSF, Jan 2023), which estimated **$2.6 billion over six years** to stand up a full-scale NAIRR. The pilot has run since Jan 2024 on ~$30–50M/year in NSF direct + several hundred million in donated cloud credits and hardware.

> "Ensure a significant percentage of the annual allotment of such computational resources is provided to projects the primary focus of which is related to any of the topics referred to in subparagraph (A)." (§ 5604(b)(3)(B))

"Subparagraph (A)" is safety, security, and "other topics that demonstrate the project at issue is in the public interest." The safety carve-out is real but "significant percentage" is undefined — the Operating Entity gets to set it.

## Drafting notes & open questions

- **Funding is the fatal ambiguity.** § 5605 authorizes donations only. There is no "authorization of appropriations" line — compare § 411 (no appropriation, but the section imposes no compute costs), § 231–232 (scholarships with explicit dollar authorizations), or the pending Senate NAIRR bill (S. 2714 in the 118th Congress) which authorized $2.6B. Codifying NAIRR without an appropriation is a **hollow codification**: the Steering Subcommittee, PMO, Operating Entity, and portal all exist on paper, but the compute that makes NAIRR real depends entirely on cloud providers continuing to donate credits and NSF finding money in its base. If AWS/Azure/GCP wind down credit programs, NAIRR winds down with them. Hill visits should press for an appropriation authorization inserted into § 5605.
- **Eligibility carves out the frontier.** § 5604(a)(2)(B)(v)'s "<7 years old and <500 employees" bar is written for startups; it excludes every US frontier developer. That is defensible policy (public compute for public-interest research, not subsidy for private capex), but the mismatch with § 111 (which regulates the same frontier developers) is worth noting — GAAIA gives frontier developers duties without any NAIRR-mediated benefit they might otherwise use to offset compliance cost. The startup/emerging-tech designation path at § 5604(a)(2)(B)(vi) is a discretionary backdoor for firms that Commerce/SBA/NIST want to include.
- **Safety-priority mechanism is soft.** "Significant percentage" and "public interest" are Operating-Entity-set. The pilot's actual allocation to alignment/interpretability work has been modest; whether § 5604(b)(3) tightens that depends on advisory-committee composition and steering-subcommittee direction — neither of which the statute pins down.
- **Advisory committee is FACA-exempt.** § 5602(c) excludes the NAIRR advisory committee from Chapter 10 of Title 5 (former FACA). This is a substantive transparency reduction — no chartering, no open-meeting requirement, no public membership balancing.
- **Foreign-nationals exclusion is via 10 U.S.C. § 4872(f)(2), not the § 101 "foreign adversary" definition.** These lists overlap but are not identical. Should be reconciled or one should reference the other.
- **§ 5106(g) NAIRR definition is unamended.** § 5601(5) points to it as the operative definition, but the actual definition text sits in the pre-existing NAII Act. Anyone drafting technical amendments should verify the § 5106(g) language still fits.
- **NDAA § 5103(e) grafting is clean but load-bearing.** The Steering Subcommittee is chartered inside the existing Interagency Committee. This preserves the OSTP-led coordination architecture but means Steering Subcommittee authority is downstream of whatever the Interagency Committee's charter allows — worth checking against § 5103(a)–(d).

## Policy conversation angles

- **Innovation / anti-patchwork:** NAIRR-as-national-capacity is the affirmative side of the "US wins the AI race" argument — democratizing access to compute for university and startup research is the compute-side analog of the coalition-standards push in § 411. But the funding gap makes this rhetorical rather than operational.
- **Safety / catastrophic-risk:** § 5604(b)(3)(B) is the CAIS/Bengio-worldview hook — public compute earmarked for alignment, interpretability, evaluation, and safety research. Operationalizing "significant percentage" is where the leverage is. Advocacy target: push for a floor (e.g., 25% or 40%) written into the statute or into the PMO's founding operating plan.
- **National security:** § 5604(a)(3) foreign-nationals exclusion and § 5604(d) tiered security (co-set with CISA and NIST) are the security surface. § 5604(f)'s NSPM-33 conformance is where any research-security friction (openness/reciprocity/transparency vs. classified data access) will surface.
- **Beneficiaries / equity:** Small and young firms, HBCUs/MSIs via STEM outreach (§ 5603(b)(3)(C)), and federal-workforce AI education (§ 5602(b)(3)(B)(x)) are the named beneficiaries. Frontier developers explicitly are not.
