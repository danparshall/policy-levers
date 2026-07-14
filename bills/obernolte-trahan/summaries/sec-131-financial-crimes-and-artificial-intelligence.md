<!--
Section file: bills/obernolte-trahan/sections/sec-131-financial-crimes-and-artificial-intelligence.md
Section-by-section: bills/obernolte-trahan/gaaia_section_by_section.txt
Summary written: 2026-07-14
Written by: Claude (Canary Institute automation), YOLO-mode session
-->

# SEC. 131. FINANCIAL CRIMES AND ARTIFICIAL INTELLIGENCE — summary

**One-line:** Amends five federal financial-crime statutes to raise fine caps and add "committed with the assistance of artificial intelligence" penalty enhancements, defining AI by cross-reference to 15 U.S.C. 9401 (NAII Act 2020).

## What it does

Amends title 18 fraud and money-laundering statutes in three distinct drafting patterns: (1) mail fraud and wire fraud get a base fine raised from $1M to $2M, plus a bolt-on penalty sentence for AI-assisted violations; (2) bank fraud is restructured into subsections and given a new subsection (b) that operates as a **separate AI-assisted offense** at up to $2M/30 years; (3) money laundering gets alternative penalty language inserted into continuation text for each of the three §1956(a) paragraphs. A new AI definition is imported into title 18 chapter 63 (via § 1346, retitled "Definitions") and into § 1956(c)(10), both cross-referencing 15 U.S.C. 9401.

## Key provisions

- Mail fraud (§ 1341): base fine $1M → $2M; AI-assisted violations "fined not more than $1,000,000 or imprisoned not more than 20 years, or both" (§ 131(a)).
- Wire fraud (§ 1343): identical treatment to mail fraud (§ 131(b)).
- Bank fraud (§ 1344): restructured into (a) IN GENERAL and new (b) ARTIFICIAL INTELLIGENCE at up to $2M / 30 years (§ 131(c)). Note: base § 1344(a) fine cap is **not** raised.
- AI defined in § 1346 as 15 U.S.C. 9401 (NAII Act § 5002) (§ 131(d)); chapter 63 heading changed to "Definitions."
- Money laundering (§ 1956): AI-assisted violations in each of (a)(1), (a)(2), (a)(3) get alternative penalty "not more than $1,000,000 or thrice the value... whichever is greater, or imprisoned for not more than 20 years" (§ 131(e)(1)); same AI definition added at § 1956(c)(10).

## Who it affects

- **Regulated parties:** Any defendant charged under §§ 1341, 1343, 1344, or 1956 — no threshold, no covered-entity limit. Individuals and firms alike.
- **Empowered actors:** DOJ (Criminal Division, US Attorneys' offices). No new agency authority — this is prosecutorial toolbox expansion.
- **Beneficiaries:** Fraud victims (higher restitution ceilings track higher fines); federal fisc.

## Cross-references

- **Defined terms used:** "Artificial intelligence" — imported from **15 U.S.C. 9401 (NAII Act 2020 § 5002)**, NOT from GAAIA § 101(3). GAAIA's own § 101(3) definition is similarly broad but is not the operative one here.
- **Depends on / paired with:** § 132 (AI impersonation of federal officials) is the paired offense-side provision in Subtitle D.

## Notable statutory language

> "If the violation is committed with the assistance of artificial intelligence, such person shall be fined not more than $1,000,000 or imprisoned not more than 20 years, or both." (§ 131(a)(2), (b)(2))

> "Whoever commits an offense subsection (a) with the assistance of artificial intelligence shall be fined not more than $2,000,000 or imprisoned not more than 30 years, or both." (§ 131(c)(2), inserting new § 1344(b))

## Drafting notes & open questions

- **"Committed with the assistance of artificial intelligence"** has no mens rea, no materiality gate, and no de minimis carve-out. A defendant need not know AI was involved. Prosecutors could invoke it whenever a phishing email touched a spam classifier, an autocomplete suggested a word, or a translation model rendered text — none of which laypeople call "AI."
- **The NAII 15 U.S.C. 9401 definition is broad** — covers any "machine-based system that can, for a given set of human-defined objectives, make predictions, recommendations, or decisions." Spam filters, ranking models, and OCR all plausibly qualify. Combined with no scienter, this creates equal-protection and vagueness exposure.
- **The section-by-section summary is inaccurate** where it says "increase maximum fines from $1 million to $2 million." Only mail fraud (§ 1341) and wire fraud (§ 1343) get a base fine raise. Bank fraud § 1344(a) base fine is untouched; only new (b) reaches $2M. Money laundering base fines are also untouched — the AI enhancement is an alternative, not a raise to the baseline.
- **Bank fraud (b) is structured as a separate offense**, not a sentencing enhancement. Charging both (a) and (b) for the same conduct risks Blockburger double-jeopardy problems that the mail/wire penalty-clause structure avoids. The three drafting patterns across five statutes are inconsistent.
- **Mail/wire AI penalty is nominally lower than the new baseline**: after § 131(a)(1) raises the base cap to $2M, the AI clause caps at $1M. Read literally, an AI-assisted mail fraud defendant faces a lower maximum fine than a non-AI defendant — likely a drafting error; the AI clause probably intended to be additive, not alternative.
- **Definition imported twice** (into § 1346 and § 1956(c)(10)) rather than once at a shared title-18 location. Fine mechanically, but a future title-18 AI provision will have to import it a third time.

## Policy conversation angles

- **Safety / catastrophic-risk:** Modest relevance — this is downstream deterrence for AI-enabled fraud, not upstream governance. Does not touch frontier developer obligations.
- **Free speech / civil liberties:** Vagueness and lack of mens rea invite selective-prosecution and equal-protection challenges. Defense bar will attack the NAII definition as unconstitutionally broad when applied to routine ML tooling.
- **National security:** Money-laundering enhancement (thrice-value alternative in § 1956) is the most operationally significant piece for sanctions-evasion and cyber-enabled financial crime cases where AI-generated identities or deepfakes are used.
