# Legislative Watcher v1 Implementation Plan

**Goal:** Build a config-driven legislative watcher that surfaces new AI-relevant bills, discussion drafts, markups, and floor scheduling in a daily markdown digest — so the next GAAIA is discovered on release day, not a month late.

**Originating conversation:** [docs/active/leg-watcher/convos/20260804_leg_watcher_brainstorm.md](../convos/20260804_leg_watcher_brainstorm.md) — which itself executes [issue #3](https://github.com/danparshall/policy-levers/issues/3).

**Context:** GAAIA was a discussion draft (never on congress.gov) discovered ~1 month late; H.R. 9363's markup and suspension-calendar timing were publicly visible in advance through feeds this project wasn't watching. The watcher closes both holes: an API poller for introduced bills, and a press-page diff layer that catches discussion drafts.

**Confidence:** High on architecture (validated section-by-section with Dan 2026-08-04); medium on individual source details (CSS selectors, feed URLs) which can only be settled against the live pages at implementation time.

**Architecture:** Source-registry pipeline. Every source normalizes to a common `Item` record via one of four adapter types (`congress_api`, `rss`, `html_diff`, `structured`). Concrete sources are rows in `config/sources.yaml`. Shared state store (seen-UIDs + parsed-page snapshots), deterministic keyword scorer, single markdown digest emitter. Per-source failure isolation: a broken source degrades the digest, never kills the run.

**Branch:** `leg-watcher` — implement in the existing worktree at `/Users/dan/code/policy-levers-leg-watcher`. Do NOT create a new worktree. Commit and push (`git push -u origin leg-watcher`) at every phase boundary.

**Tech Stack:** Python 3.12, `uv`, `pytest`, `requests`, `feedparser`, `beautifulsoup4`, `PyYAML`, `python-dotenv`. No LLM calls in v1. No cron in v1 (but everything must be idempotent and non-interactive so scheduling is a later flip).

---

## Prerequisites / blockers

1. **congress.gov API key** — free, from https://api.congress.gov/sign-up/. Goes in `.env` as `CONGRESS_API_KEY` (confirm `.env` is gitignored; add if not). All tests use fixtures and run without the key; only the live smoke run (Phase 8) needs it. **If Dan hasn't provided a key by Phase 8, stop and ask — do not sign up on his behalf.**
2. Network access for fixture capture (Phases 4 and 7).
3. The repo has no `pyproject.toml` or `.python-version` yet (verified 2026-08-04); Phase 0 creates them per the Python policy in `~/code/dotfiles/python_environment_policy.md`.

## Testing Plan

I will add unit tests, per-adapter fixture tests, and one backtest integration test. All fixtures are small, committed files under `tests/fixtures/` (parsed-size artifacts, not multi-MB page dumps — trim fixtures to the relevant structure).

- **Unit tests (pure functions):** scorer (word-boundary matching, title-vs-body weighting, kind boosts, tracked-bill alias matching, threshold suppression), state logic (new-item detection, baseline-run behavior, write-after-digest ordering, failure counting), UID stability (same input → same UID across runs), digest rendering (section order, pinning, empty-section omission, suppressed-count footer).
- **Adapter fixture tests:** each adapter is tested against saved real payloads (API JSON, RSS XML, press-page HTML, docs.house.gov XML, floor-lookahead HTML) and asserts on the *normalized Items produced* — correct uid/kind/date/title/url — not on parsing internals. Malformed-input cases included (missing dates, empty lists, changed markup → adapter raises `SourceError`, doesn't return garbage).
- **Orchestration test:** run the full pipeline with two fake sources where one raises — assert the digest contains the healthy source's items plus a source-health warning, and state was updated only for the healthy source.
- **Backtest integration test (the acceptance criterion, from issue #3):** replay June-2026 fixtures through the real pipeline against empty state and assert the digest surfaces (a) GAAIA on release day via the Trahan press layer, (b) H.R. 9363 at introduction via the API poller, (c) the 6/25 House Science markup in advance via docs.house.gov.

Tests assert behavior (items surfaced, digest content, state transitions), never mock-echoes or dataclass field lists. Network is mocked/fixtured everywhere except the Phase 8 manual smoke run.

NOTE: I will write *all* tests before I add any implementation behavior.

*(Practically: all tests for a phase are written and failing before that phase's implementation begins — the strict Nori TDD loop, phase by phase.)*

## Data model (reference for all phases)

```
Item: uid, source, chamber ("house"|"senate"|"joint"), kind ("bill_intro"|"bill_action"|"press"|"hearing"|"markup"|"floor"), title, url, date (ISO event date), body_excerpt (≤500 chars, may be ""), matched_bills (filled by scorer)
```

UID rules: congress_api → `"{bill_id}-{action_code_or_intro}-{action_date}"`; docs.house.gov meeting items → derived from the feed `guid`/EventID (stable across title edits); feed/press/floor → `sha1(url + "|" + title)[:16]`. Content-derived, never fetch-timestamps.

State file `data/watcher-state/state.json` (gitignored): per-source `last_run`, `seen_uids`, `consecutive_failures`; top-level `schema_version: 1`. (No page snapshots: seen-UIDs are the novelty mechanism, and the adapters' zero-entries `SourceError` is the selector-drift tripwire — simplified 2026-08-04 during RED-phase authoring.)

Scoring/triage rules pinned by the test suite (2026-08-04): event kinds (`markup`/`floor`/`hearing`) bypass the score threshold into Time-critical — meeting feeds are already curated by source selection, and a zero-keyword "Full Committee Markup" must still surface. Tracked-bill matching fires on aliases in title/body AND on the bill id embedded in a congress_api uid (official long titles rarely contain "H.R. NNNN").

---

## Phase 0 — Project scaffolding

1. Write `.python-version` containing `3.12`.
2. Write `pyproject.toml`: project `policy-levers`, deps above, dev-deps `pytest` + `ruff`, and `[project.scripts] watcher = "watcher.run:main"`. Package dir: `src/watcher/` (note: `src/` already contains `data/`, `profiles/`, `prioritization/` — do not touch them).
3. Run `uv venv` then `uv sync`; add `.venv/` to `.gitignore` if absent; confirm `.env` and `data/watcher-state/` gitignore coverage (extend `.gitignore` with `data/watcher-state/**` — the existing patterns only cover `data/raw`/`data/processed`).
4. Create empty package skeleton (`src/watcher/__init__.py`, `adapters/__init__.py`) and `tests/` with a trivial import test; run `uv run pytest` to prove the harness works. Commit.

## Phase 1 — Models and config loading

1. Write failing tests: `Item` construction + both UID rules; `load_sources()` parses a minimal `sources.yaml` (fields: `id`, `type`, `chamber`, `url`/`params`, `enabled`, optional `selector`); `load_keywords()` parses `keywords.yaml` (tracked_bills with aliases, high/medium/low lists, kind_boost map); unknown adapter `type` → clear error.
2. Run tests, confirm failures. 3. Implement `models.py` + config loaders minimally. 4. Tests green. 5. Commit.

## Phase 2 — State store

1. Failing tests: fresh state on missing file; `new_items()` filters seen UIDs; baseline behavior (first run of a source marks all seen, returns none as new, unless `include_backlog_days=N` — then items with date within N days are returned); snapshot round-trip; `record_success`/`record_failure` counters; save is atomic (write temp + rename) and **only called by the orchestrator after digest write** — enforce by design (no autosave inside mutators), assert via orchestration test later.
2–5. Fail → implement `state.py` → green → commit.

## Phase 3 — Scorer

1. Failing tests: word-boundary matching (`"AI"` matches "the AI bill", NOT "said" / "aid" / "brain"; case-sensitive for short all-caps terms like `AI`/`CAISI`, case-insensitive for phrases); title hits weigh 2× body hits; high/medium/low = 3/2/1; kind boosts from config; tracked-bill alias hit fills `matched_bills` and marks the item pinned regardless of score; threshold split (`digest_items`, `suppressed_count`).
2–5. Fail → implement `scoring.py` → green → commit.

## Phase 4 — Adapters (repeat the TDD loop per adapter; one commit each)

For each adapter: capture 1–2 real payloads as fixtures FIRST (trimmed), then failing tests asserting normalized Items, then implement. All four share a tiny fetch helper (timeout 30s, retry once, descriptive `User-Agent`, raises `SourceError` on non-200 or parse failure).

1. **`congress_api.py`** — two modes: (a) recent bills via `/v3/bill/119?fromDateTime=...` filtered by keyword set against title (the API has no server-side keyword search worth relying on; filter client-side), (b) latest-action check per tracked bill via `/v3/bill/119/hr/9363` etc. Fixtures: one bill-list response, one bill-detail response. Handle pagination (`pagination.next`) and the `limit=250` cap.
2. **`rss.py`** — `feedparser` over committee/member feeds; entries → `press` Items; tolerate missing `published` (fall back to today, flag in excerpt).
3. **`html_diff.py`** — fetch page, extract entries via per-source CSS selector from `sources.yaml` (selector maps: entry container / title / link / date); return ALL current entries as candidate Items (state layer decides novelty via snapshot diff); zero entries extracted from a page that previously had >0 → `SourceError` (selector drift tripwire, NOT "no news").
4. **`structured.py`** — docs.house.gov committee-repository weekly XML for Science + E&C (markup/hearing notices → `markup`/`hearing` Items, event-dated); Majority Leader weekly lookahead (majorityleader.gov — suspension-calendar tripwire → `floor` Items); Senate floor: Senate executive calendar / daily schedule page → `floor` Items.

## Phase 5 — Digest emitter

1. Failing tests: section order (Tracked bills → Time-critical [markup/floor/hearing sorted soonest-event-first] → New & notable [score-desc] → Source health → suppressed footer); empty sections omitted; item line format `[score] date · source · title (url)`; deterministic output for fixed input (no timestamps of "now" inside the body — date only in filename/H1).
2–5. Fail → implement `digest.py` (writes `digests/YYYYMMDD.md`; if the file exists, merge-append only genuinely new items under a `## Later run` header) → green → commit.

## Phase 6 — Orchestrator (`run.py`)

1. Failing tests (fake in-memory sources): full pipeline happy path; one-source-raises isolation (healthy items digested, warning line present, failed source's state untouched, `consecutive_failures` incremented, exit code 0); 3+ failures → "STALE SOURCE" pinned warning; `--include-backlog N` plumbed through; state saved only after digest written (crash-inject test: digest writer raises → state file unchanged); second identical run produces no new digest content (idempotence).
2–5. Fail → implement (CLI: `uv run watcher [--include-backlog N] [--sources id1,id2] [--dry-run]`) → green → commit.

## Phase 7 — Backtest (acceptance test from issue #3)

1. Capture June-2026 fixtures: Trahan press page including the 2026-06-04 GAAIA release entry (live page or Wayback — cf. the IOSCO precedent, STATUS 2026-07-25: Wayback works when sites block curl); congress.gov API response for H.R. 9363 introduction (6/18); docs.house.gov Science week-of-6/23 XML showing the 6/25 markup.
2. Write the failing backtest: empty state + these fixtures + real `sources.yaml` rows → run pipeline → assert digest contains GAAIA press item (release-day dated), 9363 intro, and the markup listed BEFORE its event date, all correctly sectioned.
3. Make it pass (this should require little new code if Phases 1–6 are honest; treat any gap it exposes as a real bug). 4. Commit.

## Phase 8 — Source registry population + docs + live smoke

1. Populate `config/sources.yaml` with the full v1 registry (verify each URL/feed/selector live as you go; disable-with-comment any office whose page resists diffing rather than burning the session):
   - **House API:** keyword poller + tracked bills (H.R. 9363; FRONTIER Act once numbered; S. 2938; CISA-2015 reauth vehicles).
   - **House committees:** Science maj+min, E&C maj+min (RSS where offered, else html_diff); docs.house.gov for both.
   - **House members (html_diff/rss):** Obernolte, Trahan, Franklin, Subramanyam, Houchin, Lofgren, Foushee, Stevens.
   - **Senate committees:** Commerce maj+min press + hearings; HSGAC maj+min press + hearings.
   - **Senate members:** placeholder rows, `enabled: false` — Dan names the 4–6 offices (candidates: Rounds, Heinrich, Young, Alsobrooks).
   - **Floor:** Majority Leader lookahead; Senate executive calendar/schedule.
2. Write `src/watcher/README.md`: setup (API key signup link), run commands, how to add a source (YAML row + fixture test), and the ticket-mandated list of **free subscriptions Dan should make by hand regardless** (committee/member press email lists, congress.gov saved-search alerts) since inbox delivery beats polling for drafts.
3. Update root `CLAUDE.md`/`README.md` pointers only if trivially appropriate; otherwise leave for the docs pass at merge time.
4. Live smoke run (needs API key): `uv run watcher --include-backlog 7`, eyeball `digests/`, fix selector surprises. Commit digest + any fixes. `ruff check` clean. Push.

---

**Testing Details** Unit tests cover scorer/state/digest as pure behavior (inputs → items/markdown/state transitions). Adapter tests replay committed real-payload fixtures and assert on normalized Items including malformed-input failure modes. Orchestration tests prove failure isolation and crash-safe state ordering with fake sources. The backtest replays the actual June-2026 artifacts end-to-end and is the definition of done — it tests the exact historical failure the tool exists to prevent, not a synthetic scenario.

**Implementation Details**
- Word-boundary keyword matching is mandatory — substring "ai" matching would flood the digest (test explicitly: "said", "aid", "brain").
- `html_diff` returns all current entries; novelty is decided centrally by state snapshots — adapters stay stateless.
- Zero-entries-extracted from a previously-nonempty page is `SourceError` (selector drift), never "quiet day".
- State saves happen once, in the orchestrator, after the digest write — loss-proof ordering; UID dedupe makes re-fetch safe.
- First run of any source is baseline (mark seen, emit nothing) unless `--include-backlog N`.
- Fixtures are trimmed real payloads, committed; keep each under ~50 KB (branch history becomes main history — no blobs).
- 119th Congress is hardcoded-as-config (`congress: 119` in sources.yaml), not scattered in code.
- Timezones: treat all dates as US-Eastern calendar dates; store ISO dates only, no datetimes, to avoid DST noise.
- Same event via two sources (e.g., press release in both RSS and html_diff for one office): prefer one source per office in the registry rather than cross-source dedupe logic (YAGNI).
- Digest lines carry no LLM prose; title + link is the v1 product.

**What could change:** FRONTIER Act referral/numbering will change the tracked-bills block (watch for it — meta). Dan's senator-feed list is pending (placeholder rows ship disabled). If the first weeks are noisy, thresholds/keyword tiers get retuned (YAML-only). A scheduled cloud routine may later replace manual invocation — nothing in v1 may assume a TTY or interactive prompt. LLM triage is an explicit v2 candidate layered after the scorer, not replacing it.

**Questions**
1. Does Dan already hold a congress.gov API key, or should he sign up? (Blocker only for Phase 8.)
2. Which 4–6 Senate offices for the targeted press feeds?
3. Should the daily digest eventually commit to `main` rather than living on `leg-watcher`? (Deferred; v1 commits on the branch.)
4. Is bare "AI" as a high-tier keyword too noisy even with word boundaries (e.g., appropriations boilerplate)? Retune after the first live week if so.

---
