# Summary template — GAAIA section summaries

Each per-section summary in this folder is written to help Canary Institute
staff / Hill visitors understand what the section does at a glance, without
losing the option to drill into exact statutory language for a citation.

## Format

Use this structure. Skip a heading if it's genuinely N/A for the section.
Target 250–500 words total. Trivial sections (2–5 lines of statutory text)
can be shorter.

```markdown
# SEC. NNN. TITLE — summary

**One-line:** [one-sentence what-this-section-does]

## What it does

[2–4 sentence prose explanation of the operative mechanism — who acts, on
whom, on what timeline, with what consequence.]

## Key provisions

- [Precise bullet — e.g. "Fine of up to $1M/day for violations (§ 111(f)(2))"]
- [Precise bullet with citation]

## Who it affects

- **Regulated parties:** [e.g. "Large frontier developers" — always name
  the threshold: revenue, compute, model class, whichever applies here.]
- **Empowered actors:** [agencies + AGs that gain new authority]
- **Beneficiaries:** [workers, states, researchers, etc.]

## Cross-references

- **Defined terms used:** [terms defined in § 101 that this section relies
  on. Always cite § 101(N) for each.]
- **Depends on / paired with:** [other sections that must fire for this
  one to have teeth — e.g. § 112 needs § 111 for anything to audit]

## Notable statutory language

> [Direct quote of a subsection whose exact wording matters for policy
> interpretation. Cite as § NNN(a)(1)(A). Use sparingly — quote only when
> the wording itself carries the policy load.]

## Drafting notes & open questions

- [Ambiguities, forward references to sections that don't exist yet,
  numeric thresholds that seem miscalibrated, definitions that don't
  quite fit, tension with adjacent sections. Be direct.]

## Policy conversation angles

Include only angles this section actually loads. Skip the rest.

- **Innovation / anti-patchwork:** [how supporters of federal-preemption
  framing would use this section]
- **Safety / catastrophic-risk:** [how the CAIS/Bengio worldview reads
  this section]
- **Worker / labor:** [WARN, labor market data, forecasting]
- **National security:** [cyber, adversary tech transfer, export]
- **Free speech / civil liberties:** [Sec 141 territory + adjacent]
- **State AG / enforcement:** [what state AGs can and can't do here]
```

## Style rules

- **Cite precisely.** Every quoted phrase gets a `§ NNN(a)(1)(A)` citation.
  When paraphrasing, make it clear you're paraphrasing.
- **Numeric thresholds are load-bearing.** Always surface dollar amounts,
  percentages, headcounts, timelines. Don't wave them off with "large" or
  "significant."
- **Compare bill body to section-by-section summary.** The section-by-section
  from Trahan's office (`../gaaia_section_by_section.txt`) is authoritative
  intent but sometimes elides mechanism. Flag mismatches — e.g. the summary
  says X, the bill body actually does Y.
- **Push back if the mechanism is weak.** If the section is a study/report
  with no teeth, say so. If it's a definition that carves out most of the
  regulated population, say so. This repo's CLAUDE.md norm: intellectual
  honesty > sycophancy.
- **Don't editorialize on the whole bill.** Stay in the lane of the specific
  section you're summarizing. Cross-section synthesis will happen at a
  higher level.

## Provenance

Each summary file starts with a short YAML-ish header:

```
<!--
Section file: bills/obernolte-trahan/sections/sec-NNN-slug.md
Section-by-section: bills/obernolte-trahan/gaaia_section_by_section.txt
Summary written: 2026-07-14
Written by: Claude (Canary Institute automation), YOLO-mode session
-->
```
