<!-- Generated during: convos/20260730_lw_karma_baseline.md -->

# LessWrong karma & comment baselines (12-month pull)

**Source:** LessWrong public GraphQL endpoint, `https://www.lesswrong.com/graphql`.
Unauthenticated, no API key, no Cloudflare challenge. ~500 records per request in <1s.
**Window pulled:** 2025-08-01 → 2026-07-30. **n = 7,429 posts** (weekly windows, deduped by `_id`).
**Snapshot taken:** 2026-07-30 ~17:50 UTC. All karma figures are as-of that instant.

## Query shape

```graphql
{ posts(input: {terms: {view: "new", filter: "all",
                        after: "YYYY-MM-DD", before: "YYYY-MM-DD", limit: 500}}) {
    results { _id postedAt baseScore voteCount commentCount
              frontpageDate curatedDate url user { displayName } } } }
```

**Gotcha:** omitting `filter: "all"` silently drops ~10% of posts (mostly personal
blogposts). Test week 2026-06-01→06-08: 107 posts without it, 120 with it.

## Posting rate

20.5 posts/day averaged over the 12 months. Monthly range 16.4 (Jan, Aug) to
30.5 (Apr 2026). High month-to-month variance; do not use the annual mean for
short-window comparisons.

## Karma distribution

Two maturity cutoffs, because they differ at the tail and the difference caused a
mid-session confusion (see convo doc):

| cutoff | n | p10 | p25 | p50 | p75 | p90 | p95 | p99 | max |
|---|---|---|---|---|---|---|---|---|---|
| age ≥30d | 6,838 | 1 | 5 | 15 | 38 | 80 | 127 | 264 | 833 |
| age ≥14d | 7,161 | — | — | 15 | — | — | — | — | 1038 |

Median is 15 under either cutoff; percentile ranks near the median are
insensitive to the choice (karma 14 = 48.0th at ≥14d, 48.4th at ≥30d). Only the
extreme tail moves: "Why I Left Google DeepMind" (2026-07-15, 1038) is the
all-time LW #1 and was 15 days old at snapshot, so it falls inside ≥14d and
outside ≥30d.

At the ≥30d cutoff: mean 32.8, 18.8% of posts ≥50 karma, 7.2% ≥100, 2.2% ≥200,
3.8% at ≤0.

**Venue split (age ≥14d):** frontpaged n=4,806, median 20. Personal-blog
n=2,355, median 6. Frontpage promotion is worth roughly 3x at the median.

## Karma vs. post age (cross-sectional)

Assumes a stationary population, which is shaky over a year. Short buckets are thin.

| age | n | p50 | p90 | p99 | max |
|---|---|---|---|---|---|
| 2-7d | 103 | 15 | 92 | 300 | 370 |
| 7-14d | 129 | 16 | 90 | 220 | 239 |
| 14-30d | 323 | 20 | 70 | 304 | 1038 |
| 30-90d | 1,104 | 15 | 79 | 297 | 737 |
| 90-365d | 5,734 | 14 | 80 | 261 | 833 |

**Median is flat past ~3 days.** For an ordinary post (karma 10-50), current
score on a post older than a week is effectively its settled score, so
retrospective single-pull analysis is valid and no prospective snapshotting is
needed. **This does NOT extend to the tail** — a post that escapes LW (Twitter,
HN, newsletters) plausibly accrues for days or weeks, and that accrual shape is
not recoverable after the fact. Studying the tail requires forward snapshots.

## Comment distribution

Mature posts (age ≥14d, n=7,161): median 1, p75 5, p90 15, p99 68, max 419.
**43.0% of posts get zero comments; 52.9% get ≤1.**

Conditioned on karma:

| karma | n | median comments | % zero-comment | median votes |
|---|---|---|---|---|
| 0-5 | 1,514 | 0 | 82.2% | 1 |
| 5-10 | 1,030 | 0 | 65.0% | 3 |
| 10-15 | 779 | 1 | 49.7% | 5 |
| 15-20 | 552 | 1 | 40.2% | 7 |
| 20-30 | 796 | 2 | 30.0% | 10 |
| 30-50 | 917 | 3 | 17.6% | 16 |
| 50-100 | 827 | 7 | 7.6% | 28 |
| 100+ | 516 | 23 | 0.8% | 76 |

## Metric definitions

- `baseScore` — vote-weight-summed karma. A strong upvote from a high-karma user
  is worth substantially more than one from a new account. **Not an upvote count.**
- `voteCount` — number of distinct voters. Individual votes are not public.
- **Comment residual** (proposed, not yet implemented) — observed comments minus
  the karma-bucket median from the table above. Isolates discussion generated
  beyond what reach alone predicts.
