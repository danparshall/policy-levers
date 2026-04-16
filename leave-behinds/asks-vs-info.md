# Asks vs. Info Log

Tracks, per date, the ratio of "asks made" to "total info provided" during outreach activities. Purpose: stay clear of the 20% cap on lobbying time.

A meeting/interaction is "lobbying" when it contains a direct ask for a specific legislative/regulatory action. Pure information-sharing (briefings, educational content, answering questions) does not count toward the cap.

## Convention

For each leave-behind / interaction, log:
- **Asks made**: count of distinct direct legislative/regulatory action requests
- **Info-only sections**: count of distinct educational/analytical content blocks
- **Lobbying share (by document area)**: rough % of document space devoted to direct asks
- **Counts toward cap?**: yes/no/N/A. Pre-Canary distributions are N/A.

## Log

| Date | Context | Asks made | Info-only sections | Lobbying share | Counts toward cap? | Notes |
|------|---------|-----------|--------------------|----------------|--------------------|-------|
| 2026-02-27 | Hill day — Pentagon/Anthropic crisis (10 offices) | 4 | 6 (situation, 4 "why this matters" subsections, pull-quote) | ~25% | **No** — pre-Canary, individual constituent | See `2026-02-27-pentagon-anthropic-one-pager-content.md` |
| 2026-04-15 | Hill day — AIRE Act (20 offices) | 3 (oppose preemption, support S.2938, sign Dear Colleague to Cruz) | ~7 (polling, capability trajectory, economic reach, Brookings, chart, CEO statements, "grown not programmed") | ~12% | **No** — Canary not yet incorporated | See `2026-04-15-canary-leave-behind-content.md` |

## Trend / calibration notes

- The Feb 27 one-pager was 25% asks by area — that's high. The April 15 two-pager dropped to ~12%. Intentional or not, the trajectory is moving in the right direction.
- Once Canary is incorporated and 501(h) is elected, the cap applies to *expenditures*, not document area. The ratio above is a proxy: the more lobbying-coded a document is, the more its production/distribution costs count against the cap.
- "A line or two on a larger doc" target → roughly 5-10% by area. April 15 is at the upper end; Feb 27 was over.
