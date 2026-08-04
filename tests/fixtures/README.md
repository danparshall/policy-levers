# Test fixtures — provenance

| Fixture | Provenance | Replace? |
|---|---|---|
| `docshouse_sy00_live.xml` | **REAL** capture of `https://docs.house.gov/Committee/RSS.ashx?Code=SY00`, 2026-08-04, trimmed to 2 items (one hearing, one markup) | No |
| `docshouse_sy00_june2026.xml` | Constructed in the real SY00 schema; the 6/25 markup event is historically real, guids invented | Phase 7 if an archived capture is obtainable |
| `congress_api_bill_list.json` | Constructed from the documented api.congress.gov `/v3/bill/{congress}` schema (no API key held at authoring time) | Phase 7/8 — capture real response once key exists |
| `congress_api_hr9363_intro.json` | Constructed, same schema; H.R. 9363 introduction 2026-06-18 + Science referral are historically real (STATUS.md 2026-07-24); title text approximate | Phase 7 — capture the real bill record (verify title + action text) |
| `congress_api_hr9363_detail.json` | Constructed from the documented `/v3/bill/{congress}/{type}/{number}` detail schema (`{"bill": {...}}`, NOT `{"bills": [...]}`); the 6/25 markup vote is historically real, tally invented | Phase 7/8 — capture real detail response once key exists |
| `member_press.html` | Constructed generic house.gov-style listing (live pages are JS-rendered to curl, verified 2026-08-04) | Phase 8 — capture real page + real selectors per office |
| `trahan_press_june2026.html` | Constructed; GAAIA release entry (2026-06-04) historically real, other entries invented, DOM structure generic | Phase 7 — Wayback capture + live selectors |
| `committee_rss.xml` | Constructed standard RSS 2.0; second item intentionally lacks `pubDate` | Phase 8 — capture a real committee feed |
| `floor_lookahead.html` | Constructed simplified Majority Leader weekly schedule | Phase 8 — capture real page + selectors |

Rules (from the plan): fixtures are trimmed, committed, each well under 50 KB. When a constructed
fixture is replaced with a real capture, keep assertions on *behavior* (items produced), updating
only selectors/field details that the real payload corrects.
