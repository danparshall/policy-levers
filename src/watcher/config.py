"""Config loading for sources.yaml and keywords.yaml (plan Phase 1).

Both files stay small enough to be reviewed by hand; the parser rejects unknown
adapter types up-front so a typo can't degrade quietly to "no source."
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

VALID_ADAPTER_TYPES = {"congress_api", "rss", "html_diff", "structured"}
DEFAULT_THRESHOLD = 3


@dataclass
class SourceConfig:
    id: str
    type: str
    chamber: str
    url: str = ""
    params: dict = field(default_factory=dict)
    selectors: dict = field(default_factory=dict)
    enabled: bool = True


@dataclass
class TrackedBill:
    id: str
    aliases: list[str] = field(default_factory=list)


@dataclass
class Keywords:
    tracked_bills: list[TrackedBill] = field(default_factory=list)
    tiers: dict[str, list[str]] = field(default_factory=dict)
    kind_boost: dict[str, int] = field(default_factory=dict)
    threshold: int = DEFAULT_THRESHOLD


def load_sources(path: str | Path) -> list[SourceConfig]:
    doc = yaml.safe_load(Path(path).read_text()) or {}
    rows = doc.get("sources", [])
    out: list[SourceConfig] = []
    for row in rows:
        adapter_type = row.get("type")
        if adapter_type not in VALID_ADAPTER_TYPES:
            raise ValueError(
                f"unknown adapter type: {adapter_type!r} (source id={row.get('id')!r})"
            )
        out.append(
            SourceConfig(
                id=row["id"],
                type=adapter_type,
                chamber=row.get("chamber", "house"),
                url=row.get("url", ""),
                params=row.get("params", {}) or {},
                selectors=row.get("selectors", {}) or {},
                enabled=row.get("enabled", True),
            )
        )
    return out


def load_keywords(path: str | Path) -> Keywords:
    doc = yaml.safe_load(Path(path).read_text()) or {}
    tracked = [
        TrackedBill(id=tb["id"], aliases=list(tb.get("aliases", [])))
        for tb in doc.get("tracked_bills", [])
    ]
    tiers = {tier: list(words) for tier, words in (doc.get("keywords", {}) or {}).items()}
    kind_boost = dict(doc.get("kind_boost", {}) or {})
    threshold = int(doc.get("threshold", DEFAULT_THRESHOLD))
    return Keywords(tracked_bills=tracked, tiers=tiers, kind_boost=kind_boost, threshold=threshold)
