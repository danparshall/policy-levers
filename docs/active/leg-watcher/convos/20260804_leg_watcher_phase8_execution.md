# leg-watcher Phase 8 execution

**Date:** 2026-08-04 (session executed; checkpointed 2026-08-10)
**Branch:** leg-watcher
**Machine:** Dans-MacBook-Air
**Commit:** `b20a034` — "leg-watcher Phase 8 GREEN: config + live wiring + smoke fixes"

## Summary

Executed Phase 8 of the leg-watcher build against the picks from the 2026-08-04
AI-legislator research pass. Populated `config/{sources,keywords}.yaml`, wired
`src/watcher/sources.py` + `run.py:main()` from the previous `NotImplementedError`
stub, shipped `src/watcher/README.md`, and did the live smoke run — which caught
two real docs.house.gov / congress.gov quirks the constructed fixtures had never
exercised. Fixed both with TDD (RED → GREEN → refactor), replaced two constructed
fixtures with real captures, and committed everything as one Phase 8 commit
matching the earlier one-commit-per-phase pattern.

77/77 tests pass, ruff clean, and `uv run watcher --include-backlog 14` produces
a real digest that pins H.R. 9925 (FRONTIER Act) in Tracked bills, surfaces four
markup/hearing events in Time-critical, and scores the K-12 AI Literacy Act at 8
in New & notable. The originating ticket (issue #3) is functionally satisfied —
the tool ships. Reminder #5 (FRONTIER outreach) was skipped this session per the
pre-flight `task-remind` decision.

## Topics Explored

- **Config population from the shortlist.** Translated the 2026-08-04 senator
  ranking (Warner, Blackburn, Cruz, Curtis, Hawley, Rounds, Schumer, Peters D-MI)
  into `config/sources.yaml` rows, plus the House cosponsor cluster (Obernolte,
  Trahan, Scott Peters D-CA-50 — the "Peters" from GAAIA/FRONTIER cosponsorship —
  Franklin, Subramanyam, Houchin, Lofgren, Foushee, Stevens). Enabled at boot: 4
  sources (`congress-api-poller`, `congress-api-tracked`, `docs-house-sy00`,
  `docs-house-if00`). The other 22 shipped `enabled: false` with per-row TODO
  comments, per the plan's explicit "disable-with-comment rather than burning the
  smoke run on markup-drift" instruction.
- **CLI wiring.** Wrote `src/watcher/sources.py` with 6 Source classes (`Congress
  ApiPoller`, `CongressApiTracked`, `Rss`, `HtmlDiff`, `MeetingFeed`, `FloorLook
  ahead`) that pair each config row with the right adapter parse function + an
  HTTP helper (30s timeout, one retry on transport, descriptive UA, SourceError
  on 4xx/5xx/timeout). `build_sources()` dispatches by (type, params.mode/sub
  type). Tracked-bill endpoint splitting at the first digit (`hr9925` →
  `('hr','9925')`) means digit-less ids like `gaaia` are silently skipped —
  intentional since GAAIA never got a bill number.
- **README.** Full setup + run + add-a-source loop + keyword tuning surface +
  fixture discipline + the ticket-mandated "subscribe by hand" list
  (congress.gov saved-search alerts, committee press email lists, Axios/Politico
  Pro), since inbox delivery beats polling for drafts.
- **Real-fixture captures.** Wrote `/tmp/capture_fixtures.py` against the live
  API (using the CONGRESS_API_KEY from `.env.local` — Dan already set it up
  pre-session). First attempt used `sort=updateDate+desc` which returned ancient
  "Reserved for the Speaker." placeholder bills, exposing bug #2 below. Second
  attempt filtered on `fromDateTime=2026-07-01` and curated to 2 real AI-relevant
  bills that satisfy the existing test assertions.
- **Wayback fallback attempt.** Tried Wayback CDX and web.archive.org for
  `trahan.house.gov/media/press-releases` around June 2026 (per the IOSCO
  precedent in STATUS 2026-07-25). No captures exist — deep house.gov press
  pages don't get archived. Documented as "no further work planned" in
  fixtures/README.md.

## Provisional Findings

- **Two real production quirks pinned by tests:**
  1. `docs.house.gov` meeting-feed XML emits `<item><guid>0</guid><title>
     </title><description></description>...</item>` as section separators.
     `parse_meeting_feed` was raising `SourceError` on the empty description —
     killing the entire fetch — instead of skipping the stub. Fixed via
     `_is_stub(title, guid, description)` guard. Live SY00 fetch now surfaces
     the markups it was silently swallowing.
  2. `/v3/bill/{congress}` returns "Reserved for the Speaker." placeholder rows
     (HR 6 and HR 9 in the current 119th Congress) with `latestAction: null`.
     `parse_bill_list` was raising `SourceError` on the whole fetch. Now skips
     those rows.
- **URL fallback for the detail endpoint.** `_bill_to_item` now falls back to
  `legislationUrl` (human-facing, only present in detail responses) when `url`
  (API-endpoint, list responses only) is empty. Tracked-bill digest lines now
  show `https://www.congress.gov/bill/119th-congress/house-bill/9925` instead of
  an empty paren.
- **Real title correction:** H.R. 9363's real title is "AI Security and
  Innovation Act" — not the constructed placeholder we'd been using ("To
  redesignate the National Institute of Standards and Technology's AI Safety
  Institute as the Center for AI Standards and Innovation, and for other
  purposes"). The real title is punchier but matches the same substantive bill.
  Existing test assertions on `date == "2026-06-25"` and body_excerpt containing
  "Ordered to be Reported" survived the swap without rewrite (good test design
  in the RED phase).
- **Keyword noise the live run predicts:** the 30-item second-run "New &
  notable" section on the idempotence-check run pulled in workforce/healthcare/
  labor bills — "workforce" (medium tier) plus "innovation" / "cybersecurity"
  (low tier) are broad enough to catch labor-only bills that only tangentially
  touch AI. Not fixed this session; the plan explicitly says "retune YAML rather
  than code when the first live week is noisy," so leaving it as a follow-up
  after a real week of runs.

## Decisions Made

- **One Phase 8 commit** matching the earlier one-commit-per-phase pattern
  rather than splitting into (a) core wiring + (b) smoke fixes + (c) fixture
  replacements. The bug fixes are entangled with the real-fixture replacements
  (the null-latestAction bug only surfaced when a real fixture was captured), so
  splitting the commit would either duplicate the story or lose the causal
  narrative. `b20a034` message covers all pieces in structured sections.
- **`gaaia` tracked-bill row is intentionally digit-less.** GAAIA never got a
  bill number (it's a discussion draft only), so `_bill_endpoints()` correctly
  skips it — the tool still catches GAAIA via the press-page html_diff layer
  (which is what the backtest verifies).
- **`digests/` added to `.gitignore`.** Rendered output is regenerable and
  branch history becomes main's history — no room for daily digest blobs to
  accumulate.
- **Sizing:** shipped 4 sources enabled at boot rather than trying to hunt live
  selectors for the 8 Senate + 8 House press pages this session. Per the plan,
  each disabled row is a per-row TODO that becomes a follow-up
  selector-verification session (highest yield first: Warner, Blackburn, Cruz).

## Results

The commit `b20a034` is the primary deliverable. New/modified files:

- `config/sources.yaml` (new) — 26 source rows
- `config/keywords.yaml` (new) — tracked bills + tiered keywords + kind_boost
- `src/watcher/sources.py` (new) — 6 Source classes + `build_sources()` + HTTP helper
- `src/watcher/README.md` (new) — setup, run, add-a-source, keyword tuning
- `src/watcher/run.py` (modified) — real `main()` CLI replacing the stub
- `src/watcher/adapters/structured.py` (modified) — empty-stub skip
- `src/watcher/adapters/congress_api.py` (modified) — null-latestAction skip, URL fallback
- `tests/adapters/test_congress_api.py` (modified) — 1 new test, assertions loosened for real data
- `tests/adapters/test_structured.py` (modified) — 1 new test for stub skip
- `tests/fixtures/docshouse_sy00_live.xml` (modified) — added the empty stub
- `tests/fixtures/congress_api_bill_list.json` (modified) — real capture (2 real AI bills)
- `tests/fixtures/congress_api_hr9363_detail.json` (modified) — real API detail response
- `tests/fixtures/README.md` (modified) — provenance table refreshed
- `.gitignore` (modified) — adds `digests/`

Smoke-run digest (not committed — regenerable via `uv run watcher --include-backlog 14`):

```
# Legislative digest — 2026-08-04
## Tracked bills
- 2026-07-23 · congress-api-tracked · To provide for Federal oversight of the
  development and deployment of frontier artificial intelligence in interstate
  and foreign commerce, and for other purposes.
  (https://www.congress.gov/bill/119th-congress/house-bill/9925)
## Time-critical
- [0] 2026-07-21 · docs-house-sy00 · Full Committee Markup
- [0] 2026-07-22 · docs-house-sy00 · Unleashing the Golden Age of Science …
- [0] 2026-07-22 · docs-house-if00 · Legislative Hearing on Protecting Comms …
- [0] 2026-07-22 · docs-house-if00 · Legislative Proposals to Strengthen …
## New & notable
- [8] 2026-07-21 · congress-api-poller · K-12 AI Literacy and Readiness Act of 2026
_7 items suppressed below threshold._
```

## Open Questions

- **When to enable the disabled Senate press pages?** Each is a separate
  selector-hunting session against the live page. Highest yield first: Warner
  (framework rollout workflow), Blackburn (TRUMP AMERICA AI Act discussion-draft
  workflow — the direct GAAIA failure mode), Cruz (Commerce chair markup
  announcements). Dan's call whether to batch or drip.
- **Keyword tuning after a week of real runs.** Second run's 30-item "New &
  notable" section had genuine noise from workforce/healthcare labor bills.
  Options: (a) drop "workforce" from medium tier, (b) bump threshold from 3 →
  4, (c) leave and add a "why is this here" LLM-triage layer in v2. Suggest
  waiting a full week before deciding.
- **Recess-week false positives.** `parse_meeting_feed`'s zero-entries →
  `SourceError` behavior false-positives when Congress is on recess and the feed
  legitimately has nothing. The plan pins this behavior (selector-drift
  tripwire) but real operation shows it's noisy for weeks with no meetings. A
  "seen-nonempty-before" state flag would distinguish "selector broke" from
  "quiet period."
- **Should the daily digest eventually land on main?** Deferred question from
  the plan (Q3). Currently rendered under `digests/` which is `.gitignore`d.
  For versioned digest history, we'd want a separate branch or a scheduled push
  from a runner that has write access.
- **Reminder #5 (FRONTIER outreach)** still open — skipped this session; not
  Phase 8's scope.
- **Doc-hygiene cleanup at merge** (carried from the 2026-08-04 research
  session): STATUS.md's Obernolte "Science chair" vs "R&T subcommittee chair"
  framing is inconsistent; unqualified "Peters" in GAAIA-cosponsor context
  should be "Rep. Scott Peters (D-CA-50)".
