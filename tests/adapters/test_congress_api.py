"""congress.gov API adapter: normalize bill-list payloads to Items (plan Phase 4.1).

Fixtures are constructed from the documented /v3/bill schema (no API key at authoring
time — see tests/fixtures/README.md). Assertions target normalized Items, not parsing
internals, so swapping in real captures later must not require assertion rewrites.
"""

import json

import pytest
from watcher.adapters.congress_api import parse_bill_detail, parse_bill_list
from watcher.models import SourceError

from tests.conftest import load_fixture


def payload(name):
    return json.loads(load_fixture(name))


def test_bill_list_normalizes_to_bill_intro_items():
    items = parse_bill_list(payload("congress_api_bill_list.json"), source_id="congress-api")
    assert len(items) == 2
    ai_bill = next(i for i in items if "Artificial Intelligence" in i.title)
    assert ai_bill.kind == "bill_intro"
    assert ai_bill.chamber == "house"
    assert ai_bill.date == "2026-07-28"
    assert "hr9901" in ai_bill.uid
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


def test_bill_detail_normalizes_latest_action_to_bill_action_item():
    """Tracked-bill mode (b): the /v3/bill/119/hr/9363 detail endpoint returns
    {"bill": {...}}, not {"bills": [...]} — a different parse path."""
    item = parse_bill_detail(payload("congress_api_hr9363_detail.json"), source_id="congress-api")
    assert item.kind == "bill_action"
    assert item.date == "2026-06-25"
    assert item.uid == "hr9363-action-2026-06-25"  # new action date ⇒ new uid ⇒ surfaces once
    assert "Ordered to be Reported" in item.body_excerpt
