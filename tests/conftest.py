"""Shared helpers for the watcher test suite.

These tests define the public API contract of src/watcher/ (see
docs/active/leg-watcher/plans/20260804_leg_watcher_v1_plan.md). They are written
before any implementation exists (RED phase).
"""

from pathlib import Path

import pytest

from watcher.models import Item

FIXTURES = Path(__file__).parent / "fixtures"


def load_fixture(name: str) -> bytes:
    return (FIXTURES / name).read_bytes()


def make_item(**overrides) -> Item:
    """Item factory with sane defaults; override any field per test."""
    defaults = {
        "uid": "test-uid-0001",
        "source": "test-source",
        "chamber": "house",
        "kind": "press",
        "title": "A Test Press Release",
        "url": "https://example.house.gov/press/1",
        "date": "2026-08-01",
        "body_excerpt": "",
        "matched_bills": [],
    }
    defaults.update(overrides)
    return Item(**defaults)


@pytest.fixture
def keywords():
    """A small but realistic keyword config used across scoring/digest/orchestrator tests."""
    from watcher.config import Keywords, TrackedBill

    return Keywords(
        tracked_bills=[
            TrackedBill(id="hr9363", aliases=["H.R. 9363", "CAISI"]),
            TrackedBill(id="frontier-act", aliases=["FRONTIER Act"]),
            TrackedBill(id="gaaia", aliases=["Great American AI Act", "GAAIA"]),
        ],
        tiers={
            "high": ["AI", "artificial intelligence", "frontier model"],
            "medium": ["NIST", "algorithmic"],
            "low": ["innovation"],
        },
        kind_boost={"markup": 3, "floor": 3, "bill_intro": 2, "hearing": 2, "press": 1},
        threshold=3,
    )
