# leg-watcher v1.1: enable member press pages (the discussion-draft catcher)

**Goal:** Wire the disabled member/committee press-page sources in `config/sources.yaml` so the tool actually catches discussion drafts (the GAAIA failure mode) instead of only numbered bills. Also fix two smoke-run polish items (congress.gov API pagination; recess-week false positive) so the tool works when Congress is in session.

**Originating conversation:** [docs/active/leg-watcher/convos/20260804_leg_watcher_phase8_execution.md](../convos/20260804_leg_watcher_phase8_execution.md) — Phase 8 shipped the pipeline but ~22 of 26 configured sources are disabled with per-row TODOs. This plan enables the highest-value ones.

**Context:** The tool as it stands today catches new numbered bills at introduction, but not discussion drafts released via member press pages. GAAIA was released 2026-06-04 as a discussion draft on Trahan's press page; H.R. 9363's markup slipped through docs.house.gov coverage the tool DOES have but the tracked-bill catch didn't fire until later. The June-2026 backtest passes because it feeds the pipeline the Trahan press-page HTML directly as a fixture — but on the live wire, that source is currently `enabled: false`. Live probes 2026-08-11 (see convo file) confirm the earlier "everything is JS-rendered" pessimism was overbroad: Warner returns real static HTML, Blackburn returns real static HTML (different CMS), and — decisively — **Trahan has an RSS feed at `/news/rss.aspx`** that publishes press releases immediately (verified: FRONTIER Act coalition-praise release 2026-07-28 present, DocumentID URLs live). Since Trahan uses the Fireside/ASP.NET CMS common to many .house.gov offices, RSS is very likely available across the House cluster.

**Confidence:** High on architecture — the pipeline already handles all four adapter types, this plan just enables config rows. Medium on per-office selectors and RSS availability, which can only be settled against live pages one at a time. High on the two polish items (well-understood limits observed in the Phase 8 smoke run).

**Architecture:** No new code paths for the primary work — this is config + fixture-capture + per-office adapter tests + a `.enabled` flip. The two polish items add small features to existing modules (pagination loop in `sources.py:CongressApiPollerSource.fetch`; new `nonempty_last_seen` flag in `state.py` gated by `parse_meeting_feed`).

**Branch:** `leg-watcher` — continue in `/Users/dan/code/policy-levers-leg-watcher` (existing worktree). Commit per phase (RSS-enable, html_diff-enable, floor, polish). Push at each phase boundary.

**Tech Stack:** No new dependencies. Everything uses the existing `requests` / `feedparser` / `beautifulsoup4` stack.

---

## Prerequisites

1. Fresh session should have run the standard Nori pre-flight (STATUS.md, README.md, `docs/active/leg-watcher/RESEARCH_LOG.md`, and this plan's originating convo).
2. `.env.local` symlink is live (existed at Phase 8 ship time; symlink into main worktree — see convo). No new secrets needed.
3. Congress is on recess through ~2026-09-01. That means: docs.house.gov feeds will be quiet (relevant to Priority 3 polish item), and member/committee press activity is lighter but not zero (Trahan RSS still shows July 28 content). Live-run signal is thinner during recess but selector work can proceed.

## Testing Plan

I will add per-source adapter tests using real captured fixtures, one commit per enabled source. All fixtures are trimmed real payloads, committed, each under 50 KB. New tests assert on *normalized Items produced* (correct uid/kind/date/title/url), never on parsing internals or mock echoes.

- **RSS-source tests (per office):** capture a real `/news/rss.aspx` fixture trimmed to 2-3 items, assert `Item.kind == "press"`, correct chamber, ISO date, url matches href, title matches, body_excerpt contains description text.
- **html_diff-source tests (per office):** capture a real HTML fixture trimmed to 2-3 entries, assert same normalized-Item behavior for the CSS selectors chosen. Include one adversarial case per test: title selector missing, link href empty, date unparseable → SourceError raised.
- **Committee RSS confirmation:** live-fetch each candidate feed URL (Judiciary, House Science, House E&C) with a probe; if 200 + non-empty entries, capture a fixture and write the same-shaped test as member RSS.
- **Floor lookahead:** capture real Majority Leader page HTML, add selector set, write test asserting `Item.kind == "floor"` with correct date.
- **Pagination (polish 1):** unit test for `CongressApiPollerSource.fetch` — mock two consecutive API responses where the first includes `pagination.next` and the second doesn't; assert the returned Items include both pages' bills and `http_get` was called twice.
- **Recess-week nonempty flag (polish 2):** unit test for `parse_meeting_feed`: when passed a feed that legitimately has zero entries AND the state layer signals the source has never seen non-empty content, do NOT raise SourceError (return `[]`). When the source has seen non-empty content before and now sees zero, DO raise (real selector-drift signal). This requires threading a small flag through to the adapter or into the orchestrator's fetch loop — see plan step 4 for the architectural decision.

**Live smoke run** after each phase's commits: `uv run watcher --include-backlog 14 --sources <the-new-source-ids>` to confirm the new source produces items on the wire. Delete `data/watcher-state/state.json` between smoke runs so the backlog window fires. Eyeball a digest sample; commit the fix and a short "smoke-verified" note if any selector needed adjustment.

Full-registry smoke run after all phases: `uv run watcher --include-backlog 14` (no `--sources` filter) — the whole digest should surface press-release activity from every enabled office plus the API/meeting layer already live.

NOTE: I will write *all* tests before I add any implementation behavior.

---

## Phase 1 — RSS discovery pass (cheap, high-value)

**Goal:** Find every configured office that has an RSS feed, since RSS is more reliable than html_diff and needs zero selector work.

1. Write a small one-shot probe script `/tmp/rss_probe.py` (do not commit) that curls candidate RSS URLs for each disabled member/committee source in `config/sources.yaml` and logs `(source_id, url, status, entry_count)`. Candidate URL patterns:
   - House: `{base}/news/rss.aspx` (Fireside/ASP.NET — confirmed live for Trahan)
   - House alt: `{base}/rss/`, `{base}/rss/press-releases.xml`
   - Senate: `{base}/rss/`, `{base}/services/rss.aspx`, `{base}/feed/`, `{base}/newsroom.rss`
2. Run the probe against every disabled source's URL host. Save the result as a working notes file `/tmp/rss_probe_results.md` (do not commit — feed into config edits).
3. For every 200 + non-empty-entries result: replace the html_diff row in `config/sources.yaml` with an `rss` row (chamber preserved, url updated, `enabled: false` still until Phase 2 tests pass).
4. Commit the config-only refactor: `config: switch <N> sources from html_diff to rss (per Phase 1 discovery)`.

## Phase 2 — Enable RSS sources (test + flip enabled: true, one commit per source)

For each source flipped from html_diff → rss in Phase 1, plus the committee RSS candidates that were shipped as best-guess URLs:

1. Fetch the live feed with the app's UA (`policy-levers-watcher/0.1 (+https://github.com/...)`), save trimmed to `tests/fixtures/<source_id>.xml` — keep 2-3 items, drop channel-level bloat, no `<content:encoded>` if trimmable.
2. Update `tests/fixtures/README.md` with a new row for the fixture (provenance = "REAL capture of {url}, {date}").
3. Add a failing test in `tests/adapters/test_rss.py` (or a new `test_rss_<source_id>.py` if the file gets crowded) asserting normalized-Item shape as described in Testing Plan.
4. Run, confirm RED. Implement — usually zero code since `parse_feed` handles it; if it doesn't, that's the real bug and TDD is telling you.
5. Confirm GREEN. Ruff clean.
6. Flip the source `enabled: true` in `config/sources.yaml`.
7. Live smoke: `uv run watcher --include-backlog 14 --sources <this-source-id>` from a clean state, eyeball 3-5 items, confirm they're press releases (title + href look right, date is recent, `kind == "press"`).
8. Commit: `leg-watcher: enable <source_id> RSS (real fixture + selector test)`. Push.

**Order (highest signal first, so partial completion still helps):**
1. **`rep-trahan-press`** — the literal GAAIA-catcher; RSS confirmed live 2026-08-11. Enabling this alone means the tool would have caught GAAIA on release day.
2. **`rep-obernolte-press`** — GAAIA + FRONTIER lead sponsor, same release workflow.
3. **`rep-scott-peters-ca-press`** — FRONTIER cosponsor. Also disambiguates from Gary Peters (already tracked separately).
4. **`rep-subramanyam-press`** — "four-alarm fire" quote history, active in this space.
5. **`rep-houchin-press`** — sponsor quote directly cited concurrent AI incidents.
6. **`rep-franklin-press`, `rep-lofgren-press`, `rep-foushee-press`, `rep-stevens-press`** — cluster fill.
7. **Senate committee RSS candidates:** `senate-judiciary`, `senate-hsgac`, `senate-commerce-{majority,minority}` — best-guess URLs need confirmation. If probe returned 200, enable one at a time; if 404, mark `enabled: false` with a permanent comment and stop trying.
8. **House committee RSS:** `house-science-majority`, `house-energy-commerce-majority` — same pattern.

## Phase 3 — Enable html_diff sources (only for offices without RSS)

For each Senate-member row where Phase 1 found no RSS feed:

1. Fetch the live page: `curl -sL -H "User-Agent: policy-levers-watcher/0.1" "<url>" -o /tmp/<source_id>.html`. Verify HTTP 200 and the file contains real press-listing markup (grep for `<article`, `<time`, class names like `press-`).
2. Inspect DOM (Read the HTML file, or paste a snippet). Identify: entry container, title selector, link selector, date selector.
3. Save trimmed fixture to `tests/fixtures/<source_id>.html` — keep 2-3 entries, drop `<script>` and `<style>` blocks and asset preloads to stay under ~10 KB.
4. Update `tests/fixtures/README.md`.
5. Add a failing adapter test in `tests/adapters/test_html_diff.py` (or per-source file) asserting normalized Items using the chosen selectors. Include an adversarial variant (selectors missing → SourceError).
6. Run, confirm RED. In `config/sources.yaml`, update the row's `selectors` dict with the real selectors, keep `enabled: false` until…
7. Confirm test GREEN with the new selectors (may require iterating selectors 2-3 times). Ruff clean.
8. Flip `enabled: true`.
9. Live smoke as in Phase 2 step 7.
10. Commit: `leg-watcher: enable <source_id> html_diff (real fixture + selectors)`. Push.

**Order (highest signal first):**
1. **`sen-blackburn-press`** — released TRUMP AMERICA AI Act as a discussion draft in March 2026, exact GAAIA analog. HTML confirmed static 2026-08-11.
2. **`sen-warner-press`** — 4-bill Framework for America's AI Future rollout July 21-22. HTML confirmed static.
3. **`sen-cruz-press`** — Commerce chair; markup announcements route through here.
4. **`sen-curtis-press`, `sen-hawley-press`, `sen-rounds-press`, `sen-schumer-press`, `sen-peters-mi-press`** — remainder of the shortlist.

**Guardrail:** if a page turns out to be JS-rendered after all (grep for empty `<article>` shells or `data-react-root` attributes, or if the visible titles from a browser aren't in the curl output), stop trying to selector-hunt. Add a permanent comment `# JS-rendered — needs headless-browser adapter (v2)` and move on. Do not add Playwright as a dependency in v1.1.

## Phase 4 — Floor lookahead + suspension-calendar catcher

1. Fetch `https://www.majorityleader.gov/content/weekly-house-schedule` live; inspect DOM structure. Same fixture + selector + adapter-test loop as Phase 3.
2. Enable `majority-leader-lookahead`.
3. Fetch `https://www.senate.gov/legislative/schedule/floor_schedule.htm` live; may be table-heavy — inspect and either write selectors or mark permanent-disabled with a comment.
4. If Senate schedule is workable, enable `senate-daily-schedule`; if not, leave disabled.
5. Live smoke: `uv run watcher --include-backlog 14 --sources majority-leader-lookahead`. Eyeball at least one week's floor items.
6. Commit + push.

## Phase 5 — Polish 1: congress.gov API pagination

**Why:** `CongressApiPollerSource.fetch` currently makes one API call at `limit=250`. When Congress is in session, ~500 bills/week can be introduced — the second half gets dropped silently. Real limit that will bite once recess ends.

1. Add failing test in `tests/adapters/test_congress_api.py`: patch `http_get` to return a first response with `{"bills": [...50 items], "pagination": {"next": "https://.../v3/bill/119?offset=250&format=json"}}` and a second response with `{"bills": [...30 items], "pagination": {"count": 30}}` (no `next`). Assert `parse_bill_list` receives both payloads eventually and returns 80 items total. This will require the pagination loop to live in the *Source* class, not the parser, since the parser is a pure function.
2. Confirm RED (test needs the Source to loop).
3. Add the loop to `sources.py:CongressApiPollerSource.fetch`: after each `http_get`, check `payload["pagination"].get("next")`; if present, follow it (append `&api_key=...` — the `next` URL from the API doesn't carry auth). Cap at 10 iterations as a safety valve (2,500 bills would already be a suspicious week). Test asserts the cap.
4. Confirm GREEN. Ruff clean.
5. Live smoke: `uv run watcher --include-backlog 30 --sources congress-api-poller` — should now report substantially more items during in-session weeks. Confirm we're not over-limit-ing the API (5,000 req/hr free tier).
6. Commit + push.

## Phase 6 — Polish 2: recess-week false positive on `parse_meeting_feed`

**Why:** During recess, docs.house.gov meeting feeds legitimately return zero-item XML. The current `parse_meeting_feed` raises `SourceError` on zero entries (spec'd as "selector drift, not a quiet week"), which triggers the source-health warning inappropriately. Real bug once the tool runs daily during a recess.

**Design decision (surface in the plan for the next agent):** two viable approaches, pick one:

- **Approach A (state-aware adapter):** add a new `nonempty_last_seen: bool` field to `_SourceState` in `state.py`. Orchestrator threads it into the adapter's fetch via a `source_context` param. Adapter raises `SourceError` on zero entries only if `nonempty_last_seen == True`; else returns `[]`. Con: adapter is no longer purely a parser, breaks the "adapters are stateless" invariant.
- **Approach B (orchestrator-level catch):** adapter still raises `SourceError` on zero entries; orchestrator catches it, checks state's `nonempty_last_seen` flag, and either records the failure (drift) or silently swallows (recess-quiet). Con: exception-for-control-flow.

**Recommendation:** Approach B. Keeps adapters stateless; state layer knows whether a source has ever been non-empty. Add a new exception subclass `EmptyFeed(SourceError)` in `models.py` so orchestrator can distinguish "genuinely empty" from "genuinely broken."

1. Add `EmptyFeed(SourceError)` to `models.py`. Update `parse_meeting_feed` to raise `EmptyFeed` (not bare `SourceError`) on zero entries.
2. Add `nonempty_last_seen` tracking in `_SourceState` (defaults `False`). `record_success` sets it to `True` iff items list is non-empty. Save/load handles the new field.
3. Orchestrator: on `EmptyFeed`, if `state.nonempty_last_seen(source_id) == True`, treat as failure (record_failure, health warning). Else, treat as normal (record_success with `[]`).
4. Tests: (a) parse_meeting_feed zero-entries raises `EmptyFeed`; (b) state records nonempty_last_seen correctly on transition; (c) orchestrator swallows first-ever empty; (d) orchestrator surfaces empty-after-nonempty as a failure.
5. Confirm GREEN. Ruff clean.
6. Live smoke: expected `docs-house-sy00` and `docs-house-if00` should no longer appear in the source-health section during the current recess. Confirm.
7. Commit + push.

## Phase 7 — Keyword retune (do LAST, only after 1-2 weeks of real digests)

Do NOT do this in the same session as Phases 1-6. This is a data-driven retune, not a design change; it needs real corpus data.

1. Read at least 3 daily digests plus one `--include-backlog 14` run against the fully-enabled registry.
2. Enumerate the false-positive items in "New & notable" — bills that shouldn't be there (labor bills, healthcare bills, unrelated workforce items).
3. Trace each false positive: which keyword + tier caused it? "Workforce" (medium) is the primary suspect from the Phase 8 smoke run's 30-item second run.
4. Options in priority order: (a) drop broad terms from tiers (e.g., "workforce" → drop from medium, keep in low or drop entirely); (b) require multi-keyword co-occurrence for medium/low; (c) bump `threshold` from 3 to 4. All are YAML edits to `config/keywords.yaml`, no code changes.
5. Re-run the same 3 digests against the new YAML, count false positives, count true positives that got suppressed by the change. Iterate.
6. Commit: `config: keyword retune (drop workforce, threshold 3→4, N false positives eliminated, M true positives preserved)`.

---

**Testing Details** Each enable-a-source phase adds one adapter test asserting normalized-Item behavior (uid/kind/date/title/url), never mock echoes or dataclass field lists. Adversarial cases (missing selector, empty href, unparseable date) are included per source and raise `SourceError`. The pagination test patches `http_get` to return staged responses and asserts both call count and item accumulation. The recess-week test drives orchestrator behavior through the state layer — no mocking of adapter internals.

**Implementation Details**
- Every fixture stays under 50 KB (branch history becomes main history — no blobs). Trim aggressively.
- Every fixture gets a row in `tests/fixtures/README.md` with provenance line matching Phase 8's format ("REAL capture of {url}, {date}, trimmed to N items").
- Live smoke runs happen from a clean `data/watcher-state/state.json` (`rm -f` before each) so the backlog window fires and items surface.
- Per-source enable commits reference the source id in the message so `git log --grep=<source-id>` traces the source's history.
- Do NOT add Playwright/requests-html as a dependency in v1.1. If JS-rendering blocks a source, mark it permanently disabled with a comment and move on — that's a v2 architecture question.
- If a fixture capture surfaces a new adapter bug (as the Phase 8 SY00 empty-stub and null-latestAction bugs did), fix it with the same RED→GREEN loop before enabling the source. Do NOT skip the failing case with a `# TODO: real bug`.
- `.env.local` is symlinked into the worktree from main — do not create a new .env.local in the worktree, do not commit either.
- Ruff must be clean at every commit (`uv run ruff check src/watcher tests`).

**What could change:**
- **JS-rendering discovery.** If more offices than expected turn out to be JS-rendered, the v1.1 scope shrinks and Phase 3 gets shorter, but the plan holds — the offices that DO work still get enabled. Worst case: only Trahan RSS enables, but that alone is the primary GAAIA-catcher.
- **RSS URL patterns.** The `/news/rss.aspx` pattern may not generalize — some offices use different CMSes. Phase 1's probe determines this; the plan's ordering absorbs whatever the probe finds.
- **Congress-in-session pagination volume.** If the API returns >2500 bills in a 30-day window during high activity, the pagination cap needs raising or we need date-window sharding. Not blocking; measurement question.
- **Recess-week nonempty logic.** Approach B (orchestrator-level `EmptyFeed`) is the recommendation but Approach A (state-aware adapter) is defensible if the implementing agent prefers keeping error semantics simple. Either is fine; document the choice in the commit.
- **Committee RSS availability.** Best-guess URLs in `config/sources.yaml` may 404. If a committee has no RSS and no clean html_diff option (many committee sites are complex ASP.NET), mark permanent-disabled and note it — coverage of committee press is nice-to-have, docs.house.gov meeting feeds already cover the markup/hearing signal.

**Questions**
1. **Stop after Phase 4 (usefulness), or push through Phase 6 (usefulness + robustness)?** Phases 1-4 make the tool actually catch discussion drafts. Phases 5-6 make it robust for daily cron runs. If time-boxed, Phase 4 is the "useful tool" line; 5-6 are for when the tool moves from manual to scheduled.
2. **Any office Dan does NOT want enabled?** Schumer is on the shortlist as a Minority Leader signal; if the volume is workforce/healthcare noise not AI-signal, dropping him from the enable list saves per-office work.
3. **When to open follow-up issues?** Phase 7 (keyword retune) and any permanent-disabled sources should probably become tracked issues on GitHub with a `task` label so they don't get forgotten. Do this at commit time or defer until Dan reviews the plan?
4. **Merge to main after Phase 4?** The originating ticket (#3) is "build legislative watcher." If Phases 1-4 land, the tool actually does what the ticket promised. Phase 5-6 could be either same-branch continuation or a v1.1 branch off main after merge. Dan's call.

---
