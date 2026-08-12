# LW karma baseline

**Date:** 2026-07-30 (session held open; wrapped 2026-08-12)
**Branch:** main (misc / cross-line)
**Surface:** claude.ai

## Summary

Dan asked whether tools exist to report LessWrong posting rates and karma
distributions, and how scrapeable LW is if one had to be built. Neither question
needed much investigation: LW runs on ForumMagnum and exposes a public,
unauthenticated GraphQL endpoint at `https://www.lesswrong.com/graphql`. No key,
no Cloudflare challenge, ~500 records per request in under a second. Scraping is
not required. No maintained public dashboard for these statistics was found, so
the tool would be new, but it is a thin wrapper rather than a scraping project.

Pulled 12 months (2025-08-01 → 2026-07-30, n=7,429) and computed posting rate,
karma distribution, a karma-vs-age curve, and comment distributions conditioned
on karma. Then ranked Dan's own five substantive posts against those baselines.
Headline: his median post sits at the 48th percentile sitewide, i.e. median
performance rather than top-half. The engagement picture is more interesting than
the karma picture — the April economists post drew 5 comments against a
karma-predicted 1, including an actual academic economist (Jakub Growiec), while
the FRONTIER/bill posts drew zero.

Two of my own errors got caught and corrected mid-session, both worth recording
because they are the kind that would have propagated into a built tool. See
Corrections below.

## Topics Explored

- Whether off-the-shelf LW analytics tools exist (none found for this purpose)
- LW GraphQL API: endpoint behaviour, query shape, rate tolerance, field semantics
- Posting-rate and karma-distribution baselines over a 12-month window
- Karma accrual as a function of post age, and whether retrospective analysis is valid
- Comment-count baselines conditioned on karma bucket
- Dan's own posts ranked against all three baselines
- What LW is actually for in the Canary portfolio (raised, not resolved)

## Provisional Findings

- **LW does not need scraping.** Public GraphQL endpoint, unauthenticated,
  fast. ~52 requests for a 12-month pull with no rate limiting encountered.
- **`filter: "all"` is mandatory.** Without it the `new` view silently drops
  ~10% of posts, mostly personal blogposts (107 vs 120 on a test week).
- **Posting rate:** 20.5/day over 12 months, monthly range 16.4 to 30.5.
- **Karma:** median 15, p90 80, p99 264. 3.8% of posts end at ≤0.
  Frontpage median 20 vs personal-blog median 6 — roughly 3x for promotion.
- **`baseScore` is not upvotes.** It is vote-weight-summed; a strong upvote from
  a high-karma account is worth much more than one from a new account. Dan's
  posts at 11-30 karma have only 4-9 distinct voters.
- **Median karma is flat past ~3 days**, so retrospective single-pull analysis is
  valid for ordinary posts and no prospective snapshotting is needed. This does
  not extend to the tail (see Corrections).
- **43% of mature LW posts get zero comments**; median comment count is 1.
  Conditioned on karma, the zero-comment rate runs 50% at 10-15 karma and 30% at
  20-30 karma.
- **Dan's posts:** median 14 karma = 48.0th percentile sitewide (57.6th against
  low-frequency authors). Not top-half. n=5 with single-digit voter counts, so
  the noise swamps the 40th-vs-60th distinction.
- **The economists post is the engagement outlier** (+4 comment residual). Two of
  three commenters engaged the same specific number ("less than a dozen
  economists"). Working hypothesis: a bounded contestable claim gives readers a
  place to plant a flag; accurate bill summaries do not. Confounded — n=1, only
  post with a named foil, only post on a topic with a resident LW expert
  population, three months older, and frontpaged.
- **The two bill posts were not frontpaged.** Given the ~3x frontpage median that
  is plausibly costing more reach than any content variable measured here.

## Corrections (Claude errors caught in-session)

1. **Undeclared denominator switch.** The headline karma table used a ≥30-day
   maturity cutoff (max 833); the percentile table in the next message used ≥14
   days (max 1038) without flagging the change. Dan caught it via "Why I Left
   Google DeepMind" (2026-07-15, 1038, all-time LW #1), which sits inside one
   cutoff and outside the other. The pull was NOT lossy — the post was present in
   the raw data — and percentile ranks near the median are insensitive to the
   choice (48.0th vs 48.4th). Fix for any built tool: state the maturity cutoff
   with every distribution figure.

2. **Over-generalized the flat-accrual result.** "Current score on a post older
   than a week IS the two-week number" was asserted as universal from a median
   result. A post that escapes LW plausibly accrues for days or weeks; that
   accrual shape is not recoverable retrospectively and would need forward
   snapshots.

3. **Alarmist claim without a baseline.** Told Dan that zero comments on his last
   four posts was "worse news than the karma" before checking the comment
   baseline. 43% of LW posts get zero comments, and at his karma levels the
   zero-comment rate is 30-50%, so most of those posts are unremarkable. Only
   proof-of-retention (30 karma, 0 comments, ~18% bucket) is genuinely anomalous.

## Decisions Made

- No research line cut. Filed under `docs/active/main/` per existing precedent
  for misc/cross-line sessions. Promoting to a line later is cheap.
- Puller saved as `scripts/lw_pull.py` (post windows, per-post comments, user
  posts) so the baselines are reproducible rather than one-off.
- No tool built this session. Dan's closing position is that "delivering accurate
  summaries is not a bad place to be," which reframes the whole measurement
  question — see Open Questions.

## Results

- `results/20260730_lw_karma_comment_baselines.md` — sitewide distributions,
  query shape, metric definitions
- `results/20260730_lw_dan_post_performance.md` — Dan's posts vs. baseline,
  commenter detail on the economists post
- `scripts/lw_pull.py` — reusable API client

## Open Questions

- **What is LW for in the portfolio?** If it is a credibility artifact and a
  citable landing page for staffers searching "FRONTIER Act analysis," then karma
  and comments both measure the wrong thing and the tool as scoped is
  mis-targeted; the relevant signals would be referral traffic, inbound links,
  and citation by staffers or reporters. If it is standing with the AI-safety
  research community (MATS, coalition work), engagement matters more. Not
  resolved.
- **Tag-conditioned baseline not built.** `ai-governance` / `ai-risk` posts
  specifically, which is the denominator that would say whether bill analysis
  lands with people who read bill analysis. Offered, not run.
- **Comment residual** (observed minus karma-bucket median) proposed as the
  headline engagement metric; not implemented.
- **Is the contestable-claim hypothesis testable?** Adding a defensible
  contestable claim to a bill post and watching comment residual is the obvious
  experiment, but n accumulates at roughly one post per week.
- **Frontpage promotion as a lever.** Unknown whether the bill posts were
  declined or never submitted for frontpage; worth checking, since it may
  dominate everything else measured.
- **Claude's standing objection:** accurate bill summaries commoditize fast, and
  the judgment layer in the repo (which of the 31 tiered asks matter, what
  Obernolte's office will accept, severability and the NetChoice playbook) is
  largely absent from the posts. Dan has not responded to this.
