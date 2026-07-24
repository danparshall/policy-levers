# Summary template — FRONTIER Act section summaries

Each per-section summary in this folder is written to help Canary Institute
staff / Hill visitors understand what the section does at a glance, without
losing the option to drill into exact statutory language for a citation.

## Format

Use this structure. Skip a heading if it's genuinely N/A for the section.
Target 250–500 words total. Trivial sections (2–5 lines of statutory text)
can be shorter.

```markdown
# SEC. N. TITLE — summary

**One-line:** [one-sentence what-this-section-does]

## What it does

[2–4 sentence prose explanation of the operative mechanism — who acts, on
whom, on what timeline, with what consequence.]

## Key provisions

- [Precise bullet — e.g. "Fine of up to $1M/day for violations (§ 4(f)(2))"]
- [Precise bullet with citation]

## Who it affects

- **Regulated parties:** [e.g. "Large frontier developers" — always name
  the threshold: revenue, compute, expenditure, model class, whichever applies here.]
- **Empowered actors:** [Under Secretary + AGs that gain new authority]
- **Beneficiaries:** [workers, states, researchers, etc.]

## Cross-references

- **Defined terms used:** [terms defined in § 2 that this section relies
  on. Always cite § 2(N) for each.]
- **Depends on / paired with:** [other sections that must fire for this
  one to have teeth — e.g. § 5 needs § 4 for anything to audit]

## Notable statutory language

> [Direct quote of a subsection whose exact wording matters for policy
> interpretation. Cite as § N(a)(1)(A). Use sparingly — quote only when
> the wording itself carries the policy load.]

## Drafting notes & open questions

- [Ambiguities, forward references to sections that don't exist yet,
  numeric thresholds that seem miscalibrated, definitions that don't
  quite fit, tension with adjacent sections. Be direct.]

## Changes vs GAAIA discussion draft (2026-06-04)

The FRONTIER Act was carved out of the broader Great American AI Act
(GAAIA) discussion draft — specifically the frontier-oversight slice
(GAAIA Title I §§ 101, 102, 111, 112, 113, 121). If this section has a
GAAIA analogue, note the drift here (definitions changed, thresholds
moved, new authority, provisions dropped, etc.). Be precise — cite the
GAAIA section number and quote wording changes when the wording carries
policy load. If genuinely new (e.g. § 8 emergency orders) or genuinely
absent from GAAIA, say so.

GAAIA reference material lives at `../obernolte-trahan/` in this repo:
- Bill body: `bills/obernolte-trahan/gaaia_full_text.txt`
- Per-section summaries: `bills/obernolte-trahan/summaries/`
- Overview: `bills/obernolte-trahan/OVERVIEW.md`

## Policy conversation angles

Include only angles this section actually loads. Skip the rest.

- **Innovation / anti-patchwork:** [how supporters of federal-preemption
  framing would use this section]
- **Safety / catastrophic-risk:** [how the CAIS/Bengio worldview reads
  this section]
- **National security:** [cyber, adversary tech transfer, export]
- **Free speech / civil liberties:** [pre-emption edges, jawboning]
- **State AG / enforcement:** [what state AGs can and can't do here]
```

## Style rules

- **Cite precisely.** Every quoted phrase gets a `§ N(a)(1)(A)` citation.
  When paraphrasing, make it clear you're paraphrasing.
- **Numeric thresholds are load-bearing.** Always surface dollar amounts,
  percentages, headcounts, timelines. Don't wave them off with "large" or
  "significant."
- **Compare bill body to section-by-section summary.** The section-by-section
  (`../frontier_act_section_by_section.txt`) is authoritative intent but
  sometimes elides mechanism. Flag mismatches — e.g. the summary says X,
  the bill body actually does Y.
- **Push back if the mechanism is weak.** If the section is a study/report
  with no teeth, say so. If it's a definition that carves out most of the
  regulated population, say so. Repo norm: intellectual honesty > sycophancy.
- **Don't editorialize on the whole bill.** Stay in the lane of the specific
  section you're summarizing. Cross-section synthesis will happen at a
  higher level (`OVERVIEW.md`, `FRONTIER_VS_GAAIA.md`).

## Provenance

Each summary file starts with a short YAML-ish header:

```
<!--
Section file: bills/frontier-act/sections/sec-N-slug.md
Section-by-section: bills/frontier-act/frontier_act_section_by_section.txt
GAAIA analogue: bills/obernolte-trahan/sections/sec-XXX-slug.md (if any)
Summary written: 2026-07-24
Written by: Claude (Canary Institute automation)
-->
```
