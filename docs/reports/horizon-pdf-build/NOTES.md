# Horizon memo PDF build — Keep AI out-of-the-loop

## Context

Application material for **Horizon's Rapid Response AI Fellowship** (https://horizonpublicservice.org/ai-rapid-response-fellowship/).

Prompt:
> Please write a 400-word recommendation memo on an idea related to AI security (construed broadly) you think a specific actor in the U.S. government should pursue.

Successor to `docs/reports/q1-pdf-build/` (the first, essay-genre attempt; its genre-mismatch flag is resolved by this version). Memo genre: recommendation-first, third person, no TO/FROM block — actor is State's Bureau of Arms Control, Nonproliferation, and Stability; ask is codifying the Nov 2024 Biden–Xi human-control affirmation into a U.S.–China NC3-AI framework, then P5.

Word count 2026-07-21: 421 above the separator. Dan's ruling: 400 is not a hard cap; the cap is "fits on one page." Current render is one page with ~40% whitespace remaining.

## Files

- Source markdown: `essays/horizon/Horizon__Keep_AI_out_of_the_loop.md` — memo is the text ABOVE the first `====` line; below it is retained scratch material (earlier draft language), excluded from the render.
- Rendered HTML: `Horizon__Keep_AI_out_of_the_loop.html` (self-contained, CSS embedded)
- Rendered PDF: `Horizon__Keep_AI_out_of_the_loop.pdf` (one page, Letter)
- Style sheet: `style.css` (copied from q1-pdf-build: Charter/Georgia 10.75pt, justified, 1.32 line-height)

## Rebuild

From repo root:

```bash
awk '/^=+$/{exit} {print}' essays/horizon/Horizon__Keep_AI_out_of_the_loop.md > /tmp/horizon_memo_build.md

pandoc /tmp/horizon_memo_build.md \
  --standalone --embed-resources \
  --css=docs/reports/horizon-pdf-build/style.css \
  --metadata pagetitle="Keep AI out-of-the-loop" \
  -o docs/reports/horizon-pdf-build/Horizon__Keep_AI_out_of_the_loop.html

"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=docs/reports/horizon-pdf-build/Horizon__Keep_AI_out_of_the_loop.pdf \
  file://$(pwd)/docs/reports/horizon-pdf-build/Horizon__Keep_AI_out_of_the_loop.html
```

Notes:
- The `awk` step strips everything from the first all-`=` line onward, so scratch sections never reach the PDF.
- `--metadata pagetitle=` sets the HTML `<title>` without injecting a duplicate `<h1>` (the markdown already opens with `# Keep AI out-of-the-loop`).
- Chrome's `CVDisplayLinkCreateWithCGDisplay` stderr errors are benign headless noise on this Mac.
