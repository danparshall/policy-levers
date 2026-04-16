# Policy Levers

## Project Purpose

Identify and prioritize outreach to U.S. policy makers (Congress, federal agencies, regulatory bodies) on AI economic impact and safety issues. The goal is to build comprehensive profiles and determine whom to inform, in what order, and with what messaging.

Often this repo is documentation and notes, for which you don't need to create a separate worktree.  But if you're doing large-scale tasks programatically, then you should follow standard Nori workflow.  A good rule of thumb is that if you're writing actual code, you should be using TDD on a worktree.

## Scope

- **Congress**: All 535 members (100 senators, 435 representatives). Key data: committee assignments, voting records on tech/AI, public statements, staff contacts, receptiveness.
- **Agencies**: FTC, NIST, OSTP, NSF, DOD, DOE, OMB, and others with AI-relevant mandates.
- **Regulatory bodies**: Bodies with rulemaking authority that intersects AI (SEC, FDA, NHTSA, etc.).

## Related Repositories

These sibling repos contain source material referenced by this project:
- `ai-safety` - AI safety research and analysis
- `econ-impact` - Economic impact analysis of AI
- `general-ai-abilities` - AI capabilities research

## Project Structure

```
policy_levers/
├── src/                   # Python source code
│   ├── data/              # Data ingestion and cleaning
│   ├── profiles/          # Profile generation and management
│   └── prioritization/    # Ranking and ordering logic
├── data/
│   ├── raw/               # Raw ingested data (git-ignored, large files)
│   ├── processed/         # Cleaned/structured data (git-ignored)
│   └── reference/         # Small reference files (committed)
├── notebooks/             # Jupyter notebooks for exploration
├── config/                # Configuration files
└── tests/                 # Tests
```

## Tech Stack

- Python 3.11+
- uv for package management
- pytest for testing
- Jupyter notebooks for exploration

## Conventions

- Use `uv` for dependency management (not pip directly)
- Keep data files out of git (use .gitignore patterns); small reference/lookup tables go in `data/reference/`
- Notebooks are for exploration only; production logic belongs in `src/`

### File and directory naming

- **Default: kebab-case (hyphens)** for all non-code files and directories. Example: `leave-behinds/2026-04-15-canary-leave-behind.pdf`. Rationale: ISO 8601 dates already use hyphens, modern web/Unix tooling has converged on hyphens, and consistency reduces cognitive overhead.
- **Exception: Python source files** (`src/`, `tests/`) use snake_case as required by PEP 8 / Python's import system. Example: `src/data/clean_congress_directory.py`.
- **Exception: SCREAMING_SNAKE for canonical root-level docs.** `README.md`, `CLAUDE.md`, `STATUS.md`, `PAPER_INDEX.md`, `PAPER_SUMMARIES.md` follow the "shouting filename" convention for top-level project docs. Don't add new files in this style; reserve for the existing canonical set.
- **Exception: academic papers in `papers/`** keep their existing `Author_Year_Title.pdf` form. Academic citation convention is recognizable as-is and compound surnames (e.g., `Lopez-Luzuriaga`) already mix separators.

## Research Documentation

Source literature for this project's AI-economic-impact reasoning lives alongside the code:
- `papers/` — source PDFs
- `papers/text/` — extracted text (for search/discussion without re-parsing)
- `PAPER_INDEX.md` — one-line entry per paper
- `PAPER_SUMMARIES.md` — detailed summaries with key findings

For active research lines (as opposed to the core outreach code):
- `docs/active/<branch>/` — research lines in progress, with `convos/`, `plans/`, `results/`, `RESEARCH_LOG.md`
- `docs/historical/<topic>/` — archived lines; do NOT read unless explicitly asked. `STATUS.md` lists what's there.

Epistemic norms: research findings are provisional. Don't treat prior docs as settled truth. Read `RESEARCH_LOG.md` to understand the trajectory of thinking on a research line.

## Startup
At the beginning of every conversation, read these docs:
- README.md
- STATUS.md
- PAPER_INDEX.md
Then confirm that you have read them, and tell me today's date.