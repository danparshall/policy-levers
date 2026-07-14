<!--
Section file: bills/obernolte-trahan/sections/sec-311-support-for-designated-critical-opensource-software-maintainers.md
Section-by-section: bills/obernolte-trahan/gaaia_section_by_section.txt
Summary written: 2026-07-14
Written by: Claude (Canary Institute automation), YOLO-mode session
-->

# SEC. 311. SUPPORT FOR DESIGNATED CRITICAL OPEN-SOURCE SOFTWARE MAINTAINERS — summary

**One-line:** Authorizes CISA (with CAISI) to grant funds to maintainers of designated critical open-source software, and requires large frontier developers to provide those maintainers with model access — subject to "reasonable controls" — for cybersecurity work.

## What it does

CISA, in consultation with CAISI, gains two tools to shore up the OSS supply chain: (1) a discretionary grant program for eligible maintainers of "designated critical open-source software," usable for patching, maintenance, and security auditing (§ 311(a)); and (2) a first-of-its-kind private mandate under which any developer of a "covered frontier model" must give eligible maintainers access to that model for cybersecurity purposes (§ 311(b)). CISA must promulgate implementing regulations within 90 days and stand up an outreach program within 180 days. The whole section sunsets 3 years after enactment unless reauthorized (§ 311(f)).

## Key provisions

- Grants may fund "patching, maintenance, and security auditing" (§ 311(a)(3)).
- Eligibility requires (i) wide use per download metrics/surveys/"other means"; (ii) demonstrated need + capacity; (iii) **U.S.-based individual or organization**; and (iv) CISA-with-CAISI criticality determination (§ 311(c)(1)–(4)).
- "Covered frontier model" = a frontier model developed by a large frontier developer *that the CISA Director determines possesses cybersecurity or software engineering capabilities* (§ 311(g)(4)).
- Developer access mandate is qualified by "reasonable controls" (§ 311(b)(2)).
- Regulations must govern application procedure, criticality criteria, grant amount/duration, and reporting (§ 311(d)).
- 3-year sunset (§ 311(f)).

## Who it affects

- **Regulated parties:** Developers of "covered frontier models" — a narrower set than all large frontier developers (§ 101 threshold: >$500M revenue), because CISA must additionally certify the specific model has cyber/SWE capability.
- **Empowered actors:** CISA (lead) and CAISI (consultation) on both designation and grantmaking.
- **Beneficiaries:** U.S.-based maintainers of software CISA designates as critical.

## Cross-references

- **Defined terms used:** "Frontier model" and "large frontier developer" — both § 101 (§ 311(g)(2)–(3)).
- **Depends on / paired with:** § 321 (GAO report on OSS ecosystem security) provides the diagnostic; § 311 is the operational response.

## Drafting notes & open questions

- **Section-by-section vs. bill body:** The Trahan summary says "large frontier developers must also provide AI model access." The bill body is narrower — only *covered* frontier models (a CISA-designated subset) trigger the mandate. The summary elides the CISA gate.
- **No dollar authorization.** Unlike § 102's $100M/yr for CAISI, § 311 sets no funding floor. Grant amount is punted to regulation (§ 311(d)(3)). Program could ship as a $5M or a $500M line without new language.
- **"Reasonable controls" is undefined** (§ 311(b)(2)) — could mean sandbox + rate limits or could mean gated enterprise tier at the developer's discretion. No arbitration mechanism if a maintainer says access is unreasonably throttled.
- **Domestic-presence gate excludes much of the actual attack surface.** XZ (Collin, Finland), curl (Stenberg, Sweden), and large parts of the Linux userspace are maintained abroad. § 311(c)(3) walls them off from grants and model access alike.

## Policy conversation angles

- **National security:** Post-log4j/XZ, the "critical infra runs on volunteers" problem is bipartisan common ground. The mandate on frontier developers to hand out model access to defenders is genuinely novel — a limited private-actor obligation that survives even under a broadly deregulatory reading of the bill.
- **Innovation / anti-patchwork:** The designation authority is the capture surface. If CISA's "critical OSS" list is shaped by incumbent-vendor input, the grant program becomes a channel for subsidizing maintainers of packages the biggest vendors already depend on, rather than the under-resourced hobbyist packages the framing invokes.
- **Safety / catastrophic-risk:** Giving defenders privileged access to cyber-capable frontier models is the mirror image of the offensive-cyber concerns in § 111; whether the "reasonable controls" clause preserves that asymmetry in practice is a regulation-writing question, not a statutory one.
