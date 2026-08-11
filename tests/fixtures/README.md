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
| `rep-trahan-press.xml` | **REAL** capture of `https://trahan.house.gov/news/rss.aspx`, 2026-08-11, trimmed to 2 items (FRONTIER coalition-praise 7/28 + FRONTIER Act introduction 7/23), descriptions truncated at paragraph boundary with `[fixture-trimmed]` marker | No |
| `rep-franklin-press.xml` | **REAL** capture of `https://franklin.house.gov/news/rss.aspx`, 2026-08-11, trimmed to 2 items (Obernolte-Franklin FRONTIER bill 7/27 + FRONTIER introduction celebration 7/23), same trim discipline | No |
| `sen-hawley-press.xml` | **REAL** capture of `https://www.hawley.senate.gov/rss/`, 2026-08-11, trimmed to 2 items (both 8/6; WordPress feed, `content:encoded` stripped, descriptions truncated) | No |
| `sen-schumer-press.xml` | **REAL** capture of `https://www.democrats.senate.gov/feed/` (Senate Dem caucus newsroom), 2026-08-11, trimmed to 2 items (8/8 floor wrap-up + Pro Forma schedule — the floor-signal content), `content:encoded` stripped | No |
| `rep-obernolte-press.html` | **REAL** entry nodes from `https://obernolte.house.gov/media/press-releases`, 2026-08-11, first 3 `div.media-body` entries (incl. 7/23 FRONTIER introduction), press bodies + scripts stripped, synthetic wrapper | No |
| `sen-blackburn-press.html` | **REAL** entry nodes from `https://www.blackburn.senate.gov/press-releases`, 2026-08-11, first 3 `div.element` entries (8/5 + 8/4 ×2), synthetic wrapper. Exercises `%m/%d/%Y` dates | No |
| `sen-warner-press.html` | **REAL** entry nodes from `https://www.warner.senate.gov/newsroom/press-releases`, 2026-08-11, first 3 `div.ArticleBlock` entries (8/7–8/5), excerpts + scripts stripped, synthetic wrapper. Exercises ordinal-suffix dates | No |
| `rep-houchin-press.html` | **REAL** entry nodes from `https://houchin.house.gov/media/press-releases`, 2026-08-11, first 3 `div.media-body` entries (8/4–7/29), bodies stripped, synthetic wrapper | No |
| `rep-stevens-press.html` | **REAL** entry nodes from `https://stevens.house.gov/media/press-releases`, 2026-08-11, first 3 `div.media-body` entries (7/22–7/21), bodies stripped, synthetic wrapper | No |
| `rep-subramanyam-press.html` | **REAL** entry nodes from `https://subramanyam.house.gov/media/press-releases`, 2026-08-11, first 3 `div.evo-media-object` entries (8/7–7/31), bodies stripped, synthetic wrapper. evo-Drupal h5 title variant | No |
| `sen-cruz-press.html` | **REAL** entry nodes from `https://www.cruz.senate.gov/newsroom/press-releases`, 2026-08-11, first 3 `li.PageList__item` entries (8/10–8/7), excerpts stripped, synthetic wrapper. Exercises dotted `%m.%d.%Y` dates | No |
| `sen-rounds-press.html` | **REAL** entry nodes from `https://www.rounds.senate.gov/newsroom/press-releases`, 2026-08-11, first 3 `li.PageList__item` entries (8/10–8/6), excerpts stripped, synthetic wrapper | No |
| `sen-peters-mi-press.html` | **REAL** entry nodes from `https://www.peters.senate.gov/newsroom/press-releases`, 2026-08-11, first 3 `li.PageList__item` entries (8/6–8/3), excerpts stripped, synthetic wrapper | No |
| `senate-daily-schedule.html` | **REAL** full capture of `https://www.senate.gov/legislative/schedule/floor_schedule.htm`, 2026-08-11, uncut (1.7 KB — server-rendered article pair: next meeting 8/13 pro forma + previous meeting). Exercises `%A, %b %d, %Y` dates and the entry-selector-must-skip-Previous-Meeting contract | No |

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
