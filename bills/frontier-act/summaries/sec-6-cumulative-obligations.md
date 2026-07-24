<!--
Section file: bills/frontier-act/sections/sec-6-cumulative-obligations.md
Section-by-section: bills/frontier-act/frontier_act_section_by_section.txt
GAAIA analogue: none (cumulation was implicit in GAAIA's § 101 tier definitions and statutory reference chains)
Summary written: 2026-07-24
Written by: Claude (Canary Institute automation)
-->

# SEC. 6. CUMULATIVE OBLIGATIONS — summary

**One-line:** Confirms that a higher-tier developer complies with every requirement applicable to the tiers below it — a large frontier developer picks up the frontier-developer duties, and a very large frontier developer picks up both.

## What it does

Provides that, "except as otherwise expressly provided," a large frontier developer complies with each Act requirement applicable to a frontier developer, and a very large frontier developer complies with each requirement applicable to both a frontier developer and a large frontier developer (§ 6). Read against the tier structure — frontier developer at $50M gross revenue and 10²⁶ FLOPs (§ 2), large frontier developer at $50M revenue + $1B AI-related expenditures (§ 2), very large at $5B revenue + $10B expenditures (§ 2) — this makes obligations strictly nested: very-large-tier duties sit on top of large-tier duties sit on top of base-tier duties.

## Key provisions

- **Nesting rule (§ 6):** large developer complies with all frontier-developer duties; very large developer complies with all frontier-developer and all large-developer duties.
- **Carve-out language (§ 6):** "Except as otherwise expressly provided" — reserves room for the statute to deviate, but no § 3–§ 9 provision presently disclaims cumulation on its face.

## Who it affects

- **Regulated parties:** Large frontier developers ($50M gross revenue + $1B AI-related expenditures over the preceding 36 months, with affiliates, § 2) and very large frontier developers ($5B revenue + $10B expenditures, same measurement window). Base-tier frontier developers ($50M revenue + one 10²⁶-FLOP model, § 2) are unaffected — nothing tiers *up* from them.
- **Empowered actors:** No new authority. This is a construction rule, not a grant of power.

## Cross-references

- **Defined terms used:** "frontier developer" (§ 2), "large frontier developer" (§ 2), "very large frontier developer" (§ 2).
- **Depends on / paired with:** Interacts with every operative section, but especially:
  - § 4 (transparency and reporting) — triggered on the base "frontier developer" tier (§ 4(d) transparency report, § 4(h) critical-safety-incident report) and the "large frontier developer" tier (§ 4(a) framework, § 4(c) compliance audit, § 4(g)(2) catastrophic-risk report, § 4(k) registration).
  - § 5 (independent verification) — triggered on the "very large frontier developer" tier.
  - § 8 (emergency orders) — runs against "frontier developer" and so reaches every tier.

## Notable statutory language

> "Except as otherwise expressly provided, a large frontier developer shall comply with each requirement of this Act applicable to a frontier developer, and a very large frontier developer shall comply with each requirement of this Act applicable to a frontier developer and to a large frontier developer." (§ 6)

## Drafting notes & open questions

- **The carve-out is currently empty.** § 6 uses "except as otherwise expressly provided," but no other section in the bill contains a "notwithstanding § 6" clause or otherwise disclaims cumulation. The reservation looks like belt-and-suspenders drafting to preserve room for future amendments (or for the Under Secretary's rulemakings under § 3 to expressly deviate).
- **Very-large developers pay for two overlapping third-party engagements.** Under § 6, a very-large developer is subject to *both* the § 4(c) annual independent compliance audit (a large-tier duty) *and* the § 5(b) ongoing IVO assessment (very-large-tier duty). The two reviews target different questions — § 4(c) asks whether the developer complied with its own published framework, § 5 asks whether the framework, governance, risk-monitoring, and mitigations actually "achieve acceptable levels of catastrophic risk mitigation" — so cumulation is coherent rather than redundant, but the compliance cost is doubled at the top of the tier structure. If the drafters intended the IVO assessment to *replace* the compliance audit at the very-large tier, they would need an express carve-out; § 6 as drafted does not read that way.
- **No cumulation-downward.** § 6 only tiers duties *up*. A base-tier frontier developer picks up nothing from the large-tier obligations, and a large-tier developer picks up nothing from very-large-tier obligations. This is standard, but worth flagging for readers who might otherwise assume tier boundaries create bidirectional shared duties.

## Changes vs GAAIA discussion draft (2026-06-04)

GAAIA had no dedicated cumulative-obligations clause. In GAAIA, the tier structure lived in § 101 (definitions) — "frontier developer" at $50M gross revenue (§ 101(12)) and "large frontier developer" at $500M gross revenue (§ 101(15)) — and cumulation was left implicit, to be inferred from statutory reference chains (each downstream section keyed its duties to either "frontier developer" or "large frontier developer" and expected courts to stack them).

FRONTIER makes cumulation express. Two consequences:

- **Closes a litigation vector.** Without an explicit cumulation clause, a very-large-tier developer facing a § 4(c) audit enforcement action could plausibly argue that the § 5(b) IVO assessment is the *exclusive* review regime for its tier (expressio unius reasoning — Congress named one, so it excluded the other). § 6 forecloses that argument.
- **Cleaner drafting under a three-tier structure.** GAAIA had only two tiers (frontier / large frontier); FRONTIER adds a third (very large frontier, § 2). With three tiers, an implicit-cumulation reading gets harder to sustain, so the explicit clause is more load-bearing than it would have been in GAAIA's two-tier world.

## Policy conversation angles

- **Safety / catastrophic-risk:** A CAIS/Bengio-worldview reader will treat § 6 as a floor — the safety architecture is only as strong as the weakest tier's duties, and cumulation ensures the biggest developers can't argue their way out of the base transparency-and-reporting obligations by pointing to their IVO regime.
- **Innovation / anti-patchwork:** Industry critics of overlapping compliance regimes will point to § 6 as the source of the § 4(c) audit + § 5(b) IVO double-review problem at the very-large tier. The counter is that the two reviews answer different questions and the § 9 preemption clause spares them from parallel state-law regimes.
