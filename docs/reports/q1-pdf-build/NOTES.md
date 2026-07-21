# Q1 PDF build — MAD about AI

## Context

Application material for **Horizon's Rapid Response AI Fellowship** (announcement: https://horizonpublicservice.org/ai-rapid-response-fellowship/).

Prompt:
> Please write a 400-word recommendation memo on an idea related to AI security (construed broadly) you think a specific actor in the U.S. government should pursue.

## Files

- Source markdown: `essays/mats_chang/q1/Q1_MAD_about_AI.md` (trimmed from ~3000w to ~437w on 2026-07-21)
- Rendered HTML: `Q1_MAD_about_AI.html` (self-contained, CSS embedded)
- Rendered PDF: `Q1_MAD_about_AI.pdf` (one page, Letter, ~0.9" margins)
- Style sheet: `style.css` (Charter/Georgia 10.75pt, justified, 1.32 line-height)

## ⚠️ Genre mismatch — unresolved

The prompt asks for a *recommendation memo* naming *a specific actor* and *an idea they should pursue*.

The current draft is an **analytical essay** critiquing Winter-Levy & Lalwani (2025) in *Foreign Affairs*. It:
- names no specific USG actor
- makes no concrete "X should do Y" ask
- closes with a general observation ("NC3-AI integration is where arms control has to move next, and nobody is negotiating it")

Reviewers screening ~hundreds of applications will likely favor submissions that follow the memo genre literally. Options discussed with Dan:

1. **Submit as-is.** Risk genre ding.
2. **Reshape lightly** — add `TO:` / `FROM:` / `RE:` / `RECOMMENDATION:` block, name an actor (candidates: NSC, State/AVC, DoD CDAO, NIST AISI), rewrite the closing paragraph as a concrete ask. Same substance.
3. **Replace** with a shorter single-lever memo built around one actor + one ask. The corrigibility-as-defective-product turn is the strongest and most memo-shaped insight in the essay — natural fit for a memo to NIST AISI or DoD CDAO recommending a public position on autonomous-response system evaluation.

Dan's plan: clean this up on desktop machine.

## Rebuild

From repo root:

```bash
pandoc essays/mats_chang/q1/Q1_MAD_about_AI.md \
  --standalone --embed-resources \
  --css=docs/reports/q1-pdf-build/style.css \
  --metadata pagetitle="MAD about AI" \
  -o docs/reports/q1-pdf-build/Q1_MAD_about_AI.html

"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=docs/reports/q1-pdf-build/Q1_MAD_about_AI.pdf \
  file://$(pwd)/docs/reports/q1-pdf-build/Q1_MAD_about_AI.html
```

Note: `--metadata pagetitle=` sets the HTML `<title>` (browser tab, PDF metadata) *without* injecting an `<h1>` into the body. Using `--metadata title=` instead causes a duplicated title in the rendered PDF because the markdown source already opens with `# MAD about AI`.
