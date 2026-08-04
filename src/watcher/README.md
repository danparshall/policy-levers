# watcher — legislative signal digest

Daily-cron-ready Python package that polls congress.gov + a curated set of
committee and member press pages, scores items by AI-policy relevance, and
writes a single markdown digest per run.

**Why this exists** — the Great American AI Act was released 2026-06-04 as a
discussion draft on Rep. Trahan's press page. It never appeared on congress.gov
in that form, and we found out ~1 month later. H.R. 9363's markup and its
suspension-calendar timing were also publicly visible in advance through feeds
we weren't watching. This tool closes both holes: an API poller for introduced
bills, a `docs.house.gov` meeting feed for markups, and a press-page HTML-diff
layer for the drafts that never make it to the API.

**What it doesn't do** — no LLM triage, no email delivery, no cron scheduling.
Every knob is a YAML edit; every run is a single command. Extend before
generalizing.

## Setup

**Python + deps** (uv-managed, per Dan's Python policy):

```
uv venv                    # creates .venv/ if missing (idempotent)
uv sync                    # installs runtime + dev deps
uv run pytest              # 75 tests, should be < 1s
```

**API key** — the congress.gov v3 API is free but rate-limited (5,000 req/hr per
key). Sign up at <https://api.congress.gov/sign-up/>. Store as
`CONGRESS_API_KEY` in `.env.local` at the **main worktree root** (Dan's
convention — this worktree's `.env.local` is a symlink into main).

The CLI loads `.env.local` first, then `.env`, then the process environment; any
of them works.

## Running

```
uv run watcher                       # today, only newly-seen items
uv run watcher --include-backlog 7   # smoke run: surface anything from the last 7d
uv run watcher --sources docs-house-sy00,congress-api-poller   # subset for debug
uv run watcher --today 2026-08-04    # deterministic replay (used by backtest)
uv run watcher --dry-run             # (planned; not implemented in v1)
```

Digests land in `./digests/YYYYMMDD.md` (git-ignored — regenerable). State lives
in `./data/watcher-state/state.json` (also git-ignored). Per-source failure
counts accumulate across runs; three consecutive failures pin a "STALE SOURCE"
warning to the top of the digest.

## Digest layout

Sections in order (empty ones omitted):

```
# Legislative watcher — 2026-08-04
## Tracked bills            ← anything matching keywords.yaml:tracked_bills
## Time-critical            ← markup/floor/hearing items, sorted soonest event first
## New & notable            ← scored items above threshold, high score first
## Source health            ← failures per source since last successful fetch
_Suppressed: N below-threshold items._
```

Each item line: `[score] date · source · title (url)`.

## Adding a source

Every source is one YAML row in `config/sources.yaml`. Four adapter types cover
everything so far:

- **`congress_api`** — congress.gov v3 API. Two modes:
    - `params.mode: poller` — recent-bills sweep, keyword filter happens in the
      scorer.
    - `params.mode: tracked` — one detail-endpoint call per bill listed in
      `keywords.yaml:tracked_bills`.
- **`rss`** — anything with a working RSS feed (committees, member offices).
  Missing `pubDate` falls back to today with an `[pubdate missing]` excerpt tag.
- **`html_diff`** — HTML press listings without RSS. Needs per-source CSS
  selectors `{entry, title, link, date}`. Zero entries from a previously-nonempty
  page raises `SourceError` (selector drift, not "quiet week").
- **`structured`** — schema-specific parsers. `params.subtype`:
    - `meeting_feed` — `docs.house.gov` markup/hearing RSS (event date pulled
      from the description body, not `pubDate`).
    - `floor_lookahead` — Majority Leader / Senate floor pages (`floor` kind).

### The loop

1. Add the row to `config/sources.yaml` (start `enabled: false` if you're
   guessing at selectors).
2. Capture a real payload as a fixture under `tests/fixtures/` (trimmed to the
   relevant structure — under ~50 KB; the branch history becomes main's
   history).
3. Update `tests/fixtures/README.md` with provenance for the new file.
4. Write an adapter test in `tests/adapters/` asserting the *normalized Items
   produced*, not the parsing internals.
5. Green tests → flip `enabled: true` → re-run `uv run watcher
   --include-backlog 7 --sources <your-source-id>` to smoke it.

### Retuning keywords

`config/keywords.yaml` is the entire tuning surface:

- `tracked_bills` — pin to the digest regardless of score; add aliases the
  press-release writers actually use (`"H.R. 9925"`, `"FRONTIER Act"`, etc.).
- `keywords.high/medium/low` — 3/2/1 weight, title-hits × 2. **Case rule** the
  scorer enforces: all-lowercase-free tokens (`AI`, `NIST`) match
  case-sensitively; anything with a lowercase letter (`artificial intelligence`)
  matches case-insensitively. Word boundaries are always required, so `AI`
  never fires on `said`/`aid`/`brain`.
- `kind_boost` — additive **only when there was a keyword hit**. Zero-keyword
  items score 0 no matter their kind, so a road-renaming press release stays
  suppressed.
- `threshold` — non-tracked, non-event items below this get suppressed
  (counted in the digest footer).

Retune YAML first, code second. If the first live week is loud, adjust tiers
and threshold before touching the scorer.

## Fixture discipline

`tests/fixtures/` are **committed** — the branch history is what merges to main,
so keep each fixture under ~50 KB and trimmed to just what the tests need. New
fixtures need a row in `tests/fixtures/README.md` tagging provenance (real
capture vs constructed) and whether they're due for replacement.

## Also do this by hand (out of scope for the watcher)

Polling is second-best for material the source *will* email you. Subscribe by
hand:

- Congress.gov saved-search alerts:
    - <https://www.congress.gov/quick-search/legislation> → save your AI query,
      "Email me when there are new results."
- Committee press email lists (all of these accept plain-email signup at their
  press pages, no RSS gap):
    - Senate Commerce, Judiciary, HELP, HSGAC, Armed Services, Intelligence.
    - House Science, Energy & Commerce, Judiciary.
- Member offices whose press page resists diffing but whose email list is
  public (usually the same page — look for "Newsletter" or "Press releases via
  email"): every senator on the shortlist, plus the GAAIA/FRONTIER cosponsor
  cluster (Obernolte, Trahan, Franklin, Subramanyam, Houchin, Scott Peters
  D-CA-50).
- Axios / Politico Pro AI newsletters — often surface framework rollouts before
  the press page updates (STATUS entry 2026-08-04 credits Axios with the Warner
  scoop).

The watcher is the fallback for when the press-page-first workflow (the GAAIA
failure mode) skips your inbox.

## Layout

```
src/watcher/
├── __init__.py
├── README.md               (this file)
├── adapters/
│   ├── congress_api.py     # /v3/bill/... → Items
│   ├── rss.py              # committee/member RSS → press Items
│   ├── html_diff.py        # press listings with CSS selectors → press Items
│   └── structured.py       # docs.house.gov meetings + floor lookaheads
├── config.py               # sources.yaml + keywords.yaml loaders
├── digest.py               # section rendering + file write
├── models.py               # Item, SourceError, UID helpers
├── run.py                  # CLI + orchestrator (run_watcher + main)
├── scoring.py              # word-boundary keyword scorer + triage
├── sources.py              # Source classes: pair config row → adapter + HTTP fetch
└── state.py                # per-source seen-UIDs + failure counts (atomic save)
```

## Where to go from here

- **v1 → v1.1** — enable the disabled Senate press pages one by one (each is
  one selector-hunting session). Highest-yield rows first: Warner, Blackburn,
  Cruz. Shortlist rationale:
  `docs/active/leg-watcher/results/20260804_ai_legislators_shortlist.md`.
- **v1.1 → v2** — LLM triage layered *after* the deterministic scorer (so it
  can only add signal, never subtract). Cheap model, one call per item that
  scores below threshold with a title that has any keyword hit. Guardrail: cap
  spend per run.
- **v2 → v2.1** — cron / GitHub Action / launchd. Everything is already
  idempotent and non-interactive; just add a scheduler and a delivery hop.
