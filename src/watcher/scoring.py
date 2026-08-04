"""Deterministic keyword scoring + triage (plan Phase 3).

Case rule (both keywords and tracked-bill aliases): if the token contains any
lowercase letter it matches case-insensitively; otherwise it's short/acronym-shaped
(AI, CAISI, GAAIA, H.R.) and matches case-sensitively — so "aid"/"said"/"Ai Weiwei"
don't fire "AI".

Word boundaries are mandatory everywhere — substring "ai" matching would flood the
digest with "said", "aid", "brain".

Weights: high/medium/low = 3/2/1; title hits weigh 2× body hits; kind_boost is added
after the keyword sum. Event kinds (markup/floor/hearing) bypass the score threshold —
committee meeting feeds are already curated by source selection.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from watcher.config import Keywords
    from watcher.models import Item

EVENT_KINDS = {"markup", "floor", "hearing"}
TIER_WEIGHTS = {"high": 3, "medium": 2, "low": 1}


@dataclass
class TriageResult:
    pinned: list[Item] = field(default_factory=list)
    listed: list[tuple[Item, int]] = field(default_factory=list)
    suppressed_count: int = 0


def _compile(term: str) -> re.Pattern:
    """Word-boundary regex; case-sensitive iff `term` has no lowercase letter."""
    flags = re.IGNORECASE if any(c.islower() for c in term) else 0
    return re.compile(r"\b" + re.escape(term) + r"\b", flags)


def _count(term: str, text: str) -> int:
    if not text:
        return 0
    return len(_compile(term).findall(text))


def score_item(item: Item, keywords: Keywords) -> int:
    """Keyword score + (kind_boost IF there was any keyword signal).

    An item with zero keyword hits scores exactly 0, regardless of kind — so a
    press release about a road renaming doesn't get pulled above threshold by
    being "press-kind." Kind_boost is a relevance amplifier, not a base score.
    """
    keyword_score = 0
    for tier, words in keywords.tiers.items():
        weight = TIER_WEIGHTS.get(tier, 0)
        if weight == 0:
            continue
        for kw in words:
            title_hits = _count(kw, item.title)
            body_hits = _count(kw, item.body_excerpt)
            keyword_score += weight * (2 * title_hits + body_hits)
    if keyword_score == 0:
        return 0
    return keyword_score + keywords.kind_boost.get(item.kind, 0)


def match_tracked(item: Item, keywords: Keywords) -> list[str]:
    """Return the ids of tracked bills mentioned in the item.

    Fires on any alias appearing in title or body (word-bounded, per case rule) OR
    on the bill id appearing as a token in the uid (congress_api items encode the
    bill id there — official long titles rarely contain "H.R. NNNN").
    """
    matched: list[str] = []
    uid_tokens = set(item.uid.split("-"))
    for bill in keywords.tracked_bills:
        if bill.id in uid_tokens:
            matched.append(bill.id)
            continue
        for alias in bill.aliases:
            if _count(alias, item.title) or _count(alias, item.body_excerpt):
                matched.append(bill.id)
                break
    return matched


def triage(items: list[Item], keywords: Keywords) -> TriageResult:
    result = TriageResult()
    for item in items:
        matches = match_tracked(item, keywords)
        if matches:
            item.matched_bills = matches
            result.pinned.append(item)
            continue
        score = score_item(item, keywords)
        if item.kind in EVENT_KINDS or score >= keywords.threshold:
            result.listed.append((item, score))
        else:
            result.suppressed_count += 1
    result.listed.sort(key=lambda pair: pair[1], reverse=True)
    return result
