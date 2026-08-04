# Test fixtures — provenance

| Fixture | Provenance | Replace? |
|---|---|---|
| `docshouse_sy00_live.xml` | **REAL** capture of `https://docs.house.gov/Committee/RSS.ashx?Code=SY00`, 2026-08-04, trimmed to 3 items (one hearing, one markup, one `<guid>0</guid>` empty stub — real quirk observed in live feed, exercises the stub-skip path) | No |
| `docshouse_sy00_june2026.xml` | Constructed in the real SY00 schema (matches live shape); the 6/25 markup event is historically real, guids invented | No further work planned — Wayback CDX search for docs.house.gov RSS attempted 2026-08-04, no archived snapshots. Shape verified against live capture |
| `congress_api_bill_list.json` | **REAL** capture of `/v3/bill/119?fromDateTime=2026-07-01T00:00:00Z&sort=updateDate+desc`, 2026-08-04, curated to 2 real AI-relevant bills (H.R. 7968 Small AI Innovators Empowerment Act; H.R. 9285 Heat Emergency Assessment and Tracking using AI Act). Also exercises the null-latestAction skip path via a separate constructed edge-case test | No |
| `congress_api_hr9363_intro.json` | Constructed to represent hr9363's latestAction at introduction (2026-06-18 referral to Science). The live API only returns the CURRENT latestAction (now the 2026-06-25 markup vote), so this historical snapshot cannot be captured live — kept constructed as the backtest anchor. Schema verified real against `congress_api_bill_list.json` | No — historical snapshot, not fetchable from live API |
| `congress_api_hr9363_detail.json` | **REAL** capture of `/v3/bill/119/hr/9363`, 2026-08-04. Title, latestAction, sponsors, cosponsors count, actions/committees/subjects URLs all live values as of capture | No |
| `member_press.html` | Constructed generic house.gov-style listing (live pages are JS-rendered to curl, verified 2026-08-04 — no real capture possible without a headless browser) | Phase 8+ — needs `requests-html` / Playwright to capture real |
| `trahan_press_june2026.html` | Constructed; GAAIA release entry (2026-06-04) historically real, other entries invented, DOM structure generic. Wayback CDX search 2026-08-04 returned no 2026 captures of the deep press-releases page | No further work planned — no archived source available |
| `committee_rss.xml` | Constructed standard RSS 2.0; second item intentionally lacks `pubDate` | Phase 8+ — capture a real committee feed once one is confirmed to publish RSS |
| `floor_lookahead.html` | Constructed simplified Majority Leader weekly schedule | Phase 8+ — capture real page + selectors when Majority Leader source is enabled |

Rules (from the plan): fixtures are trimmed, committed, each well under 50 KB. When a constructed
fixture is replaced with a real capture, keep assertions on *behavior* (items produced), updating
only selectors/field details that the real payload corrects.

**Real quirks caught during Phase 8 smoke run (2026-08-04) and now exercised by tests:**
- `docs.house.gov` emits `<item><guid>0</guid><title></title>...</item>` empty stubs as section
  separators. The `_is_stub` guard in `parse_meeting_feed` skips them cleanly instead of raising
  SourceError. `docshouse_sy00_live.xml` includes one such stub; `test_empty_stub_items_are_skipped`
  pins the behavior.
- `/v3/bill/{congress}` returns "Reserved for the Speaker." placeholder rows with `latestAction: null`.
  `parse_bill_list` now skips these. `test_reserved_for_speaker_placeholder_bills_are_skipped` pins
  the behavior with an inline constructed payload (the real fixture curates to bills WITH latestAction
  populated so the happy-path assertion stays clean).
