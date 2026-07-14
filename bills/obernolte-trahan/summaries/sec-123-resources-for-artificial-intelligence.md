<!--
Section file: bills/obernolte-trahan/sections/sec-123-resources-for-artificial-intelligence.md
Section-by-section: bills/obernolte-trahan/gaaia_section_by_section.txt
Summary written: 2026-07-14
Written by: Claude (Canary Institute automation), YOLO-mode session
-->

# SEC. 123. RESOURCES FOR ARTIFICIAL INTELLIGENCE MODEL DOCUMENTATION — summary

**One-line:** NIST runs a pilot to publish a voluntary, modular model-card / datasheet template plus "objective performance metrics" technical guidelines — no compliance duty on developers, and the template fields are provenance-oriented rather than safety-oriented.

## What it does

Within 180 days of enactment, the NIST Director — in consultation with other agency heads "as appropriate" — must stand up a pilot to build a "structured template and associated technical guidelines for documentation to accompany artificial intelligence models and associated data" (§ 123(a)). NIST publishes the draft in the Federal Register for at least 60 days of public comment (§ 123(c)(2)) and, one year after the pilot begins, reports to House Science and Senate Commerce with an effectiveness assessment and — "if so assessed to be effective" — a plan for permanent implementation (§ 123(d)(1)). Final template and guidelines are posted on the NIST website. Nothing in § 123 requires any AI developer to use, complete, or file the template.

## Key provisions

- **Template fields (§ 123(b)(1)(A)–(H)) are provenance metadata, not safety content:** model name, developer identity, developer's place of incorporation, release date, training-data knowledge cutoff, supported languages, terms of service, plus a Director-discretion catch-all. No risk-assessment, capability-eval, or red-team fields.
- **Modular by mandate (§ 123(b)(2)):** users "flexibly adopt and complete sections" per sector, audience, and use case — partial adoption is expected.
- **"Objective performance metrics" (§ 123(b)(3)):** NIST must publish technical guidelines that "make available objective performance metrics for each component … for a range of artificial intelligence model types, as applicable." No benchmark, standards body, or metric floor is named.
- **Local definition (§ 123(e)(1)):** § 123 defines its own "artificial intelligence model" instead of pulling from § 101 — the bill's operative frontier-developer terms are NOT invoked here.

## Who it affects

- **Regulated parties:** None. Adoption is voluntary and unenforced.
- **Empowered actors:** NIST Director (lead); House Science and Senate Commerce as report recipient.
- **Beneficiaries:** Downstream deployers, procurement officers, and researchers who want a common documentation shape for smaller / non-frontier models.

## Cross-references

- **Paired with § 111:** The mandatory disclosure regime for large frontier developers (>$500M revenue) — pre-deployment reports with risk assessments, mitigations, 15-day critical-incident filings to CAISI, $1M/day penalties — already lives in § 111. § 123 does not overlap with § 111's substantive risk content; the template fields are what a model card looks like *without* any safety disclosures.
- **Institutional note:** § 123 puts the pilot at NIST, not CAISI (§ 102). CAISI is not named as a consultation partner.

## Notable statutory language

> "Produce a structured template designed to enable a user to document information about an artificial intelligence model and associated data, **which may include** the following information …" (§ 123(b)(1), emphasis added)

"May include" plus the modularity requirement plus the absence of any duty-to-file makes the listed fields non-binding even on the pilot's own template design.

## Drafting notes & open questions

- **Voluntary tool with no consumer.** § 123 creates a template but names no party who must produce, receive, or act on completed documentation. Unlike § 111 (CAISI receives, AGs opt in, AG-enforceable), § 123 has no downstream regulatory or contracting hook.
- **"Objective performance metrics" is the substantive fulcrum.** If NIST specifies real benchmark suites tied to template components, § 123 could become the de facto federal model card. If left at the abstraction level of the statute, it is a bibliography.
- **Effectiveness self-assessment is circular.** § 123(d)(1) has NIST evaluate its own pilot with no external metric of adoption or utility.

## Policy conversation angles

- **Innovation / anti-patchwork:** Cleanest angle — a voluntary, industry-collaborated NIST template that preempts nothing and gives smaller developers a reusable artifact.
- **Safety / catastrophic-risk:** Low value on its own terms; § 111 already carries the frontier-developer disclosure that matters. Realistic ask for safety-leaning offices: (a) fund NIST's "objective performance metrics" work to produce concrete benchmarks, or (b) require § 111-covered developers to include the § 123 template fields in their § 111 filings (interop, not new duty).
