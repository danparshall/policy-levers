#!/usr/bin/env python3
"""Pull LessWrong post metadata from the public GraphQL API.

Provenance: docs/active/main/convos/20260730_lw_karma_baseline.md

The endpoint at https://www.lesswrong.com/graphql is public and unauthenticated
(ForumMagnum, shared with the EA Forum).  No key, no Cloudflare challenge; ~500
records per request in under a second.  There is no need to scrape HTML.

IMPORTANT: `filter: "all"` is required.  Without it the "new" view silently drops
roughly 10% of posts, mostly personal blogposts.  Test week 2026-06-01..06-08
returned 107 posts without the filter and 120 with it.

`baseScore` is vote-WEIGHT-summed karma, not an upvote count; `voteCount` is the
number of distinct voters.  Individual votes are not public.

Usage:
    python3 scripts/lw_pull.py --after 2025-08-01 --before 2026-07-30 --out lw.json
"""

import argparse
import datetime as dt
import json
import time
import urllib.request

ENDPOINT = "https://www.lesswrong.com/graphql"
UA = "Mozilla/5.0 (policy-levers research; dan@canaryinstitute.ai)"

POST_FIELDS = (
    "_id title postedAt baseScore voteCount commentCount "
    "frontpageDate curatedDate url user { displayName }"
)


def gq(query, tries=3, backoff=3.0):
    """POST a GraphQL query, with naive retry.  Returns the parsed JSON body."""
    for attempt in range(tries):
        try:
            req = urllib.request.Request(
                ENDPOINT,
                data=json.dumps({"query": query}).encode(),
                headers={"Content-Type": "application/json", "User-Agent": UA},
            )
            return json.load(urllib.request.urlopen(req, timeout=60))
        except Exception:
            if attempt == tries - 1:
                raise
            time.sleep(backoff)


def posts_in_window(after, before, limit=500):
    q = (
        '{ posts(input: {terms: {view: "new", filter: "all", '
        'after: "%s", before: "%s", limit: %d}}) { results { %s } } }'
        % (after, before, limit, POST_FIELDS)
    )
    return gq(q)["data"]["posts"]["results"]


def pull(after, before, step_days=7, pause=0.4):
    """Walk the range in windows.  Windows keep each response under the limit."""
    start = dt.date.fromisoformat(after)
    end = dt.date.fromisoformat(before)
    rows, cursor = [], start
    while cursor < end:
        nxt = min(cursor + dt.timedelta(days=step_days), end)
        batch = posts_in_window(cursor.isoformat(), nxt.isoformat())
        if len(batch) >= 500:
            print("WARN: window %s hit the 500 cap; shorten step_days" % cursor)
        rows.extend(batch)
        cursor = nxt
        time.sleep(pause)
    deduped = {r["_id"]: r for r in rows}
    return list(deduped.values())


def comments_on(post_id, limit=100):
    q = (
        '{ comments(input: {terms: {view: "postCommentsTop", postId: "%s", '
        "limit: %d}}) { results { _id baseScore voteCount postedAt "
        "parentCommentId user { displayName karma } "
        "contents { plaintextMainText } } } }" % (post_id, limit)
    )
    return gq(q)["data"]["comments"]["results"]


def user_posts(user_id, limit=50):
    q = (
        '{ posts(input: {terms: {view: "userPosts", userId: "%s", limit: %d}}) '
        "{ results { %s } } }" % (user_id, limit, POST_FIELDS)
    )
    return gq(q)["data"]["posts"]["results"]


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--after", required=True, help="ISO date, inclusive")
    ap.add_argument("--before", required=True, help="ISO date, exclusive")
    ap.add_argument("--step-days", type=int, default=7)
    ap.add_argument("--out", default="lw_posts.json")
    args = ap.parse_args()

    rows = pull(args.after, args.before, args.step_days)
    with open(args.out, "w") as fh:
        json.dump(rows, fh)
    days = (dt.date.fromisoformat(args.before) - dt.date.fromisoformat(args.after)).days
    print("%d posts, %.1f/day, written to %s" % (len(rows), len(rows) / days, args.out))
