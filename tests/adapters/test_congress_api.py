"""congress.gov API adapter: normalize bill-list payloads to Items (plan Phase 4.1).

Fixtures are REAL /v3/bill responses (captured 2026-08-04, see tests/fixtures/README.md).
Assertions target normalized-Item behavior, not specific bill numbers/titles, so
future re-captures with different real bills don't break the suite.
"""

import json

import pytest

from tests.conftest import load_fixture
from watcher.adapters.congress_api import parse_bill_detail, parse_bill_list
from watcher.models import SourceError


def payload(name):
    return json.loads(load_fixture(name))


def test_bill_list_normalizes_to_bill_intro_items():
    items = parse_bill_list(payload("congress_api_bill_list.json"), source_id="congress-api")
    assert items, "fixture should contain at least one real bill row"
    ai_bill = next(i for i in items if "AI" in i.title or "Artificial Intelligence" in i.title)
    assert ai_bill.kind == "bill_intro"
    assert ai_bill.chamber in ("house", "senate")
    assert ai_bill.date  # ISO date pulled from latestAction.actionDate
    # UID pattern per make_bill_uid: "{bill_id}-{action_code}-{action_date}"
    assert ai_bill.uid.endswith(f"-intro-{ai_bill.date}")
    assert ai_bill.url.startswith("https://")


def test_bill_uid_stable_across_refetch():
    a = parse_bill_list(payload("congress_api_bill_list.json"), source_id="congress-api")
    b = parse_bill_list(payload("congress_api_bill_list.json"), source_id="congress-api")
    assert [i.uid for i in a] == [i.uid for i in b]


def test_latest_action_text_lands_in_body_excerpt():
    items = parse_bill_list(payload("congress_api_hr9363_intro.json"), source_id="congress-api")
    (item,) = items
    assert "Science" in item.body_excerpt  # referral text is the routing signal


def test_malformed_payload_raises_source_error():
    with pytest.raises(SourceError):
        parse_bill_list({"unexpected": "shape"}, source_id="congress-api")


def test_reserved_for_speaker_placeholder_bills_are_skipped():
    """Real quirk in /v3/bill/119: 'Reserved for the Speaker.' placeholder rows
    carry latestAction=null. Real bug hit on the 2026-08-04 smoke run — the adapter
    was raising SourceError on the whole fetch instead of skipping the placeholder."""
    payload = {
        "bills": [
            {
                "congress": 119,
                "latestAction": None,
                "number": "6",
                "originChamberCode": "H",
                "title": "Reserved for the Speaker.",
                "type": "HR",
                "url": "https://api.congress.gov/v3/bill/119/hr/6?format=json",
            },
            {
                "congress": 119,
                "latestAction": {"actionDate": "2026-07-28", "text": "Referred to committee."},
                "number": "999",
                "originChamberCode": "H",
                "title": "Real Bill Act",
                "type": "HR",
                "url": "https://api.congress.gov/v3/bill/119/hr/999?format=json",
            },
        ],
    }
    items = parse_bill_list(payload, source_id="congress-api")
    assert len(items) == 1
    assert items[0].title == "Real Bill Act"


@pytest.mark.parametrize(
    "bad",
    [
        {"unexpected": "shape"},
        {"bill": {"type": "HR", "number": "9363", "title": "no latestAction"}},
        {"bill": {"latestAction": {"actionDate": "2026-06-25"}, "title": "no type/number"}},
    ],
    ids=["wrong-top-level-key", "missing-latestAction", "missing-type-number"],
)
def test_bill_detail_malformed_payload_raises_source_error(bad):
    """Issue #9 (H3): the tracked-bill path is what fires when a watched bill moves;
    a malformed detail payload must be a SourceError, not a KeyError/TypeError."""
    with pytest.raises(SourceError):
        parse_bill_detail(bad, source_id="congress-api")


def _row(**overrides) -> dict:
    row = {
        "type": "HR",
        "number": "1",
        "title": "x",
        "url": "https://api.congress.gov/v3/bill/119/hr/1",
        "latestAction": {"actionDate": "2026-06-25", "text": "Referred."},
    }
    row.update(overrides)
    return row


@pytest.mark.parametrize(
    ("row", "expected"),
    [
        (_row(originChamberCode="H"), "house"),
        (_row(originChamberCode="S"), "senate"),
        (_row(originChamber="House of Representatives"), "house"),
        (_row(originChamber="Senate"), "senate"),
        (_row(), "joint"),
        (_row(originChamberCode="", originChamber=""), "joint"),
    ],
    ids=["code-H", "code-S", "name-house", "name-senate", "absent", "empty"],
)
def test_chamber_resolution_including_joint_fallback(row, expected):
    """Issue #9 (L9): chamber comes from originChamberCode, then originChamber,
    and falls back to 'joint' when neither is present."""
    (item,) = parse_bill_list({"bills": [row]}, source_id="congress-api")
    assert item.chamber == expected


def test_bill_detail_normalizes_latest_action_to_bill_action_item():
    """Tracked-bill mode (b): the /v3/bill/119/hr/9363 detail endpoint returns
    {"bill": {...}}, not {"bills": [...]} — a different parse path."""
    item = parse_bill_detail(payload("congress_api_hr9363_detail.json"), source_id="congress-api")
    assert item.kind == "bill_action"
    assert item.date == "2026-06-25"
    assert item.uid == "hr9363-action-2026-06-25"  # new action date ⇒ new uid ⇒ surfaces once
    assert "Ordered to be Reported" in item.body_excerpt
