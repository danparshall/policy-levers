"""Core data types for the legislative watcher.

`Item` is the normalized record every adapter must return. UIDs are content-derived
(no fetch-timestamps) so they're stable across runs — the state store dedupes on them.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field


class SourceError(Exception):
    """Raised by an adapter when its source is unreachable or its input is malformed.

    Signaling this (rather than returning `[]`) is what lets the orchestrator
    distinguish "quiet day" from "the selector broke" — see plan §Testing Plan.
    """


@dataclass
class Item:
    uid: str
    source: str
    chamber: str  # "house" | "senate" | "joint"
    kind: str  # "bill_intro" | "bill_action" | "press" | "hearing" | "markup" | "floor"
    title: str
    url: str
    date: str  # ISO event date (YYYY-MM-DD)
    body_excerpt: str = ""
    matched_bills: list[str] = field(default_factory=list)


def make_bill_uid(bill_id: str, action_code: str, action_date: str) -> str:
    """UID for bill items — readable so a human debugging the state file can grep.

    congress_api items use this so tracked-bill matching can fire on the bill_id
    embedded in the uid (official long titles rarely contain "H.R. NNNN").
    """
    return f"{bill_id}-{action_code}-{action_date}"


def make_hash_uid(url: str, title: str) -> str:
    """UID for feed/press/floor items — content-derived, stable across runs."""
    digest = hashlib.sha1(f"{url}|{title}".encode()).hexdigest()
    return digest[:16]
