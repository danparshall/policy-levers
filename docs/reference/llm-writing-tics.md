<!-- Generated during: docs/active/main/convos/20260716_canary_lw_essay_adaptations.md -->

# LLM writing tics — research summary and VOICE.md delta

Compiled 2026-07-16 (session: general-audience rewrite of MAD about AI).  Web research
by subagent; cross-referenced against `~/code/dotfiles/VOICE.md`.  Purpose: a reusable
checklist for de-AI-ifying prose, plus candidate additions to VOICE.md.

## Anchor sources

- [Wikipedia:Signs of AI writing (WP:AITELLS)](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) — most comprehensive practitioner catalog, built from thousands of flagged submissions.
- [Kobak et al., Science Advances 2025, "Delving into LLM-assisted writing in biomedical publications through excess vocabulary"](https://www.science.org/doi/10.1126/sciadv.adt3813) ([arXiv full text](https://arxiv.org/html/2406.07016v1)) — "excess mortality"-style analysis of 15M PubMed abstracts; ≥13.5% of 2024 abstracts show LLM processing.  2024's excess vocabulary is almost entirely STYLE words (66% verbs, 18% adjectives): "delves" ~25x expected frequency, "showcasing" ~9.2x, "underscores" ~9.1x.
- [blader/humanizer SKILL.md](https://github.com/blader/humanizer/blob/main/SKILL.md) — densest practical fix-it checklist (33 patterns with repairs).
- [refsmmat.com LLM-style notebook](https://www.refsmmat.com/notebooks/llm-style.html) — aggregates the stylometry literature (Mizumoto 2024, Jiang & Hyland 2025, Siler 2026).
- [Jasmine Sun, "Why LLMs Are Bad Writers But Good Editors"](https://jasmi.news/p/ai-writing) — editor's perspective on voice laundering.

Two calibration warnings from the sources, both worth keeping in mind:
(1) single markers prove nothing; it's CLUSTER DENSITY that signals AI — em-dashes and
contrast framing are legitimate human devices; (2) humans detect AI text at roughly
chance when going on gut feel, so checklist editing beats vibes.

## The catalog

### Lexical red flags (subtract on sight)

Tier 1, empirically quantified (Kobak; Liang et al. peer-review corpus): delve,
underscore(s), showcase/showcasing, crucial, pivotal, intricate, meticulous(ly),
notable/notably, realm, comprehensive, commendable, "the potential for," "valuable
insights," enhance/enhancing.

Tier 2, WP:AITELLS vocabulary list: tapestry, testament ("stands as a testament"),
landscape ("evolving landscape"), interplay, robust, vibrant, fostering, garner,
boasts, "enduring legacy," bolstered, "align with," "plays a key/vital/pivotal role,"
Additionally/Moreover/Furthermore as paragraph openers, trailing
highlighting/emphasizing/underscoring clauses.

Tier 3, stock phrases: "It's important to note," "In today's fast-paced world,"
"rich cultural heritage," "nestled," "in the heart of," "marks a pivotal moment,"
"setting the stage for," "In conclusion / In summary / Overall" as closers, vague
authority ("Experts argue," "Observers have cited"), filler frames ("in order to,"
"due to the fact that," "has the ability to").

### Structural patterns

1. Negative parallelism / contrast scaffolding: "It's not just X, it's Y."  The
   single most-cited structural tell.  Circulating mechanistic explanation: RLHF
   raters upvote contrast framing as "insightful," so it got reward-hacked into
   house style.
2. Rule of three, everywhere ("clear, concise, and compelling").
3. Copula avoidance: "serves as," "functions as," "represents" instead of "is."
4. Trailing "-ing" significance clauses: "…, highlighting the importance of X."
5. Inflated-significance paragraph closers ("underscores its enduring relevance").
6. Restating summary paragraphs ("In conclusion…").
7. Bolded-phrase-colon bullet lists ("**Scalability:** The system…").
8. Formulaic section templates ("Challenges and Future Directions").
9. Uniform sentence/paragraph length (low burstiness); corroborated empirically
   by Jiang & Hyland 2025 (rigid formulaic lexical bundles).
10. Synonym cycling / elegant variation (artifact of repetition penalties): "the
    company… the firm… the organization… the enterprise."
11. False ranges: "from X to Y" where X and Y aren't on a real scale.
12. Rhetorical questions as transitions; fake-candid openers ("Honestly?").
13. Signposting inflation ("Let's dive in," header restated in first sentence).
14. Staccato punchline drama ("No fluff.  No guessing.  Just results.").
15. Aphorism formulas: "X is the Y of Z"; "X is more than a Y — it's a Z."

### Tonal patterns

- Grandiosity/puffery in neutral contexts (press-release cadence).
- False balance: symmetric "however, critics argue" regardless of evidence.
- Hedging paradox: LLM text has FEWER genuine epistemic-stance markers than human
  academic prose (impersonal expository tone), yet stacks decorative qualifiers
  ("could potentially possibly").  Human hedging is asymmetric and specific.
- Artificial comprehensiveness: every facet at equal depth; no salience gradient.
- No first-person stakes, no lived detail, no defended idiosyncratic choices.
- Abstract nouns where a human names a person, a number, a place, a Tuesday.

### Formatting

Em-dash density (not isolated use), curly-quote paste artifacts, Title Case
Headers, emoji headers, mechanical boldface, markdown residue in non-markdown
surfaces, uniform hyphenation in predicate position ("the report is high-quality").

### Repair techniques (the "add back" half)

Removing tells only gets to neutral; human texture must be ADDED:
- Replace abstractions with named, dated, countable specifics.
- Insert first-person stakes and opinions with conceded tradeoffs.
- Replace decorative hedging with real epistemic position (flat where confident,
  specific where not).
- Vary rhythm deliberately; allow slack sentences; at most one punchline per passage.
- Let structure be asymmetric: three paragraphs on what you know, one clause on
  what you don't.
- Signals AI can't fake: hard-to-fabricate detail, unresolved tension, era-bound
  references, self-corrections, defended idiosyncratic choices.
- Don't over-correct into a new tell (zero em-dashes + zero contrast in persuasive
  prose is itself unnatural; judge by cluster density).

## Cross-reference against VOICE.md

Already covered there (no action): em-dashes (A12), bold/markdown scaffolding
(Inv 7, A17), corporate transitions (A5), texture phrases (A3), hedge stacks (A2),
false balance (A7), press-release register (A16), engineered epigrams (A19),
argument narration (A18), sentence-length variance + double-space (anti-detection
overlay), uniform-density failure (M5/M6 slack-sentence guidance), vague authority
(Inv 8 named targets), abstract-instead-of-specific (Inv 3).

Candidate NEW additions to VOICE.md (not currently explicit there):
1. Trailing "-ing" significance clauses ("…, highlighting the importance of X") —
   A18-adjacent but distinct; extremely common and easy to grep.
2. Copula avoidance ("serves as," "functions as," "represents" for "is").
3. Synonym cycling / elegant variation; A20 already endorses loose repeated short
   names, but the inverse tell isn't named.
4. Rule-of-three audit: cut to two, extend to four, or keep the strongest item.
5. False ranges ("from X to Y" without a real scale).
6. Inflated-significance paragraph closers as a named tell (every paragraph ending
   by asserting the fact matters).
7. Lexical greplist (delve/crucial/pivotal/landscape/tapestry/robust/testament/
   underscore/showcase/realm/foster/garner/boast) as a mechanical final pass.

## Practical editing order (for any draft)

1. Grep the lexical lists; replace with plain words or delete the clause.
2. Structural pass: break contrast scaffolds, audit triads, restore plain copulas,
   delete trailing "-ing" clauses and restating closers.
3. Tonal pass: add specifics, stakes, and asymmetry; state confidence flatly.
4. Formatting pass: em-dash count, header case, unbold, quote style.
5. Read aloud for rhythm; confirm slack sentences survived.
