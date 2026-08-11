"""Regression tests for src/watcher/sources.py — Source classes and build_sources().

Focused on the two bug fixes from the pre-merge code review; broader HTTP-layer
coverage (retry, 4xx-vs-5xx, transport error) is tracked in the follow-up issue
opened at merge time.
"""

from __future__ import annotations

import pytest

from watcher import sources
from watcher.config import Keywords, SourceConfig, TrackedBill


class _FakeResponse:
    """Minimal requests.Response stand-in for the fetch tests."""

    def __init__(self, *, payload=None, text: str = "") -> None:
        self._payload = payload
        self.text = text
        self.content = text.encode("utf-8")
        self.status_code = 200

    def json(self):
        if self._payload is None:
            raise ValueError("no JSON payload")
        return self._payload


def _tracked_source(**cfg_overrides) -> sources.CongressApiTrackedSource:
    cfg = SourceConfig(
        id=cfg_overrides.pop("id", "congress-api-tracked"),
        type="congress_api",
        chamber="house",
        url=cfg_overrides.pop("url", "https://api.congress.gov"),
        params={"mode": "tracked", "congress": 119, **cfg_overrides.pop("params", {})},
    )
    keywords = Keywords(
        tracked_bills=[
            TrackedBill(id="hr9925"),
            TrackedBill(id="hr9363"),
        ],
    )
    return sources.CongressApiTrackedSource(cfg, api_key="fake-key", keywords=keywords)


def test_tracked_source_skips_bill_with_malformed_json_and_continues(monkeypatch):
    """Bug fix (code-review 2026-08-11): CongressApiTrackedSource.fetch() previously
    let a ValueError from resp.json() propagate up, killing the whole tracked-bills
    fetch on a single bad detail response. Now each bill's non-JSON response is
    converted to SourceError inside the per-bill try, so the loop continues."""
    good_detail = {
        "bill": {
            "type": "HR",
            "number": "9363",
            "congress": 119,
            "originChamberCode": "H",
            "title": "Good Bill Act",
            "url": "https://api.congress.gov/v3/bill/119/hr/9363?format=json",
            "latestAction": {"actionDate": "2026-06-25", "text": "Ordered to be Reported."},
        }
    }
    calls: list[str] = []

    def fake_http_get(url: str, **_):
        calls.append(url)
        # First bill (hr9925) returns non-JSON garbage; second bill (hr9363) is real.
        # Note: URL shape is /v3/bill/119/hr/9925 — the slug is split with a slash.
        if "/hr/9925" in url:
            return _FakeResponse(text="<html>internal server error page</html>")
        return _FakeResponse(payload=good_detail)

    monkeypatch.setattr(sources, "http_get", fake_http_get)
    src = _tracked_source()
    items = src.fetch()
    assert len(calls) == 2, "loop should continue past the malformed bill"
    assert len(items) == 1, "one good bill should still surface"
    assert items[0].uid.startswith("hr9363-")


def test_tracked_source_raises_when_every_bill_lookup_fails(monkeypatch):
    """Complements the fix above: if EVERY tracked-bill lookup fails, the source
    still surfaces as failed (aggregated SourceError) so the operator sees the
    outage in the digest's source-health section instead of silently returning []."""

    def always_bad_json(url: str, **_):
        return _FakeResponse(text="<html>oops</html>")

    monkeypatch.setattr(sources, "http_get", always_bad_json)
    src = _tracked_source()
    with pytest.raises(sources.SourceError) as exc_info:
        src.fetch()
    msg = str(exc_info.value)
    assert "every tracked bill lookup failed" in msg
    assert "hr9925" in msg and "hr9363" in msg  # aggregated diagnostic


def test_build_sources_bad_mode_error_message_includes_actual_value():
    """Bug fix (code-review 2026-08-11): the ValueError raised for an unknown
    congress_api mode was implicit-concatenating a non-f-string, so {mode!r}
    printed literally instead of the offending value. Pin the actual formatting."""
    cfg = SourceConfig(
        id="broken-source",
        type="congress_api",
        chamber="house",
        url="https://api.congress.gov",
        params={"mode": "typo-here"},
    )
    with pytest.raises(ValueError) as exc_info:
        sources.build_sources(
            [cfg],
            keywords=Keywords(),
            api_key="fake-key",
            today="2026-08-11",
            backlog_days=7,
        )
    msg = str(exc_info.value)
    assert "'broken-source'" in msg
    assert "'typo-here'" in msg, f"actual mode value should be in message; got: {msg}"
    assert "{mode!r}" not in msg, "literal placeholder leaked through — f-prefix missing"
