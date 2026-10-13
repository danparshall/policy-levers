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


# ── http_get: retry / status handling (issue #9, H1) ─────────────────────────
# The HTTP boundary is faked at `requests.get` (the one call http_get makes);
# everything above it — retry decisions, status-code branching, SourceError
# wrapping, Retry-After handling — is the real code under test.


class _StatusResponse:
    def __init__(self, status_code: int, headers: dict | None = None, text: str = "") -> None:
        self.status_code = status_code
        self.headers = headers or {}
        self.text = text
        self.content = text.encode()


class _FakeHttp:
    """Scripted stand-in for requests.get: each call pops the next outcome.

    An outcome is either a response object or an exception instance to raise.
    """

    def __init__(self, *outcomes) -> None:
        self._outcomes = list(outcomes)
        self.calls: list[tuple[str, dict]] = []

    def __call__(self, url, **kwargs):
        self.calls.append((url, kwargs))
        outcome = self._outcomes.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome


@pytest.fixture
def no_sleep(monkeypatch):
    slept: list[float] = []
    monkeypatch.setattr(sources.time, "sleep", slept.append)
    return slept


def _install(monkeypatch, *outcomes) -> _FakeHttp:
    fake = _FakeHttp(*outcomes)
    monkeypatch.setattr(sources.requests, "get", fake)
    return fake


def test_http_get_200_passes_response_through(monkeypatch, no_sleep):
    ok = _StatusResponse(200, text="<rss/>")
    fake = _install(monkeypatch, ok)
    resp = sources.http_get("https://example.gov/feed")
    assert resp is ok
    assert len(fake.calls) == 1
    assert "policy-levers-watcher" in fake.calls[0][1]["headers"]["User-Agent"]


def test_http_get_404_raises_without_retry(monkeypatch, no_sleep):
    fake = _install(monkeypatch, _StatusResponse(404))
    with pytest.raises(sources.SourceError, match="404"):
        sources.http_get("https://example.gov/missing")
    assert len(fake.calls) == 1
    assert no_sleep == []


def test_http_get_500_retries_once_then_succeeds(monkeypatch, no_sleep):
    ok = _StatusResponse(200)
    fake = _install(monkeypatch, _StatusResponse(503), ok)
    assert sources.http_get("https://example.gov/flaky") is ok
    assert len(fake.calls) == 2


def test_http_get_500_twice_raises_source_error(monkeypatch, no_sleep):
    fake = _install(monkeypatch, _StatusResponse(502), _StatusResponse(502))
    with pytest.raises(sources.SourceError, match="502"):
        sources.http_get("https://example.gov/down")
    assert len(fake.calls) == 2


def test_http_get_transport_error_retries_once_then_succeeds(monkeypatch, no_sleep):
    import requests

    ok = _StatusResponse(200)
    fake = _install(monkeypatch, requests.ConnectionError("reset by peer"), ok)
    assert sources.http_get("https://example.gov/blip") is ok
    assert len(fake.calls) == 2


def test_http_get_persistent_transport_error_wraps_as_source_error(monkeypatch, no_sleep):
    import requests

    _install(monkeypatch, requests.Timeout("slow"), requests.Timeout("slow"))
    with pytest.raises(sources.SourceError, match="transport error"):
        sources.http_get("https://example.gov/slow")


def test_http_get_429_honors_retry_after_then_succeeds(monkeypatch, no_sleep):
    """Congress.gov v3 returns 429 + Retry-After once the hourly budget is hit.
    Back off for the advertised interval and retry rather than treating it as a
    'we're wrong' 4xx."""
    ok = _StatusResponse(200)
    fake = _install(monkeypatch, _StatusResponse(429, headers={"Retry-After": "2"}), ok)
    assert sources.http_get("https://api.congress.gov/v3/bill/119") is ok
    assert len(fake.calls) == 2
    assert no_sleep == [2.0]


def test_http_get_429_twice_names_rate_limit_in_error(monkeypatch, no_sleep):
    limited = _StatusResponse(429, headers={"Retry-After": "1"})
    _install(monkeypatch, limited, limited)
    with pytest.raises(sources.SourceError) as exc_info:
        sources.http_get("https://api.congress.gov/v3/bill/119")
    msg = str(exc_info.value).lower()
    assert "rate" in msg and "limit" in msg, f"operator must see 'rate-limited', got: {msg}"
    assert "retry-after" in msg


def test_http_get_429_with_huge_retry_after_fails_fast(monkeypatch, no_sleep):
    """A Retry-After beyond the backoff cap must not stall the cron run for an hour —
    surface the header and give up."""
    _install(monkeypatch, _StatusResponse(429, headers={"Retry-After": "3600"}))
    with pytest.raises(sources.SourceError, match="3600"):
        sources.http_get("https://api.congress.gov/v3/bill/119")
    assert no_sleep == []


# ── build_sources dispatch ───────────────────────────────────────────────────


def _cfg(**overrides) -> SourceConfig:
    base = {
        "id": "src",
        "type": "rss",
        "chamber": "house",
        "url": "https://example.gov/feed",
        "params": {},
        "selectors": {},
    }
    base.update(overrides)
    return SourceConfig(**base)


def _build(cfgs):
    return sources.build_sources(
        cfgs, keywords=Keywords(), api_key="k", today="2026-08-11", backlog_days=7
    )


@pytest.mark.parametrize(
    ("cfg", "expected_cls"),
    [
        (_cfg(type="rss"), sources.RssSource),
        (_cfg(type="html_diff"), sources.HtmlDiffSource),
        (_cfg(type="structured", params={"subtype": "meeting_feed"}), sources.MeetingFeedSource),
        (
            _cfg(type="structured", params={"subtype": "floor_lookahead"}),
            sources.FloorLookaheadSource,
        ),
        (
            _cfg(type="congress_api", params={"mode": "poller"}),
            sources.CongressApiPollerSource,
        ),
        (
            _cfg(type="congress_api", params={"mode": "tracked"}),
            sources.CongressApiTrackedSource,
        ),
    ],
)
def test_build_sources_dispatches_each_type(cfg, expected_cls):
    (src,) = _build([cfg])
    assert isinstance(src, expected_cls)
    assert src.id == "src"


def test_build_sources_unknown_structured_subtype_raises():
    with pytest.raises(ValueError, match="'nope'"):
        _build([_cfg(type="structured", params={"subtype": "nope"})])


def test_build_sources_unknown_type_raises():
    with pytest.raises(ValueError, match="telepathy"):
        _build([_cfg(type="telepathy")])


# ── tracked-bill id → endpoint mapping (issue #9) ────────────────────────────


def _tracked_with(*bill_ids) -> sources.CongressApiTrackedSource:
    cfg = SourceConfig(
        id="congress-api-tracked",
        type="congress_api",
        chamber="joint",
        url="https://api.congress.gov",
        params={"mode": "tracked", "congress": 119},
    )
    keywords = Keywords(tracked_bills=[TrackedBill(id=b) for b in bill_ids])
    return sources.CongressApiTrackedSource(cfg, api_key="k", keywords=keywords)


def _detail(bill_type: str, number: str) -> dict:
    return {
        "bill": {
            "type": bill_type.upper(),
            "number": number,
            "originChamberCode": "H",
            "title": "x",
            "latestAction": {"actionDate": "2026-06-25", "text": "Referred."},
        }
    }


def test_tracked_source_builds_urls_for_resolution_types(monkeypatch):
    """hjres/sjres/hres/sres/hconres/sconres ids must map to their own URL segment,
    not be mangled by a naive split-on-first-digit."""
    calls: list[str] = []

    def fake_http_get(url: str, **_):
        calls.append(url)
        bill_type, number = url.rsplit("/", 2)[-2:]
        return _FakeResponse(payload=_detail(bill_type, number))

    monkeypatch.setattr(sources, "http_get", fake_http_get)
    src = _tracked_with("hr9925", "s2938", "hjres45", "sconres7", "HRes100")
    src.fetch()
    assert calls == [
        "https://api.congress.gov/v3/bill/119/hr/9925",
        "https://api.congress.gov/v3/bill/119/s/2938",
        "https://api.congress.gov/v3/bill/119/hjres/45",
        "https://api.congress.gov/v3/bill/119/sconres/7",
        "https://api.congress.gov/v3/bill/119/hres/100",
    ]


def test_tracked_source_skips_ids_that_are_not_bill_slugs(monkeypatch):
    """Alias-only tracked entries (e.g. an unnumbered discussion draft) have no
    congress.gov endpoint — skip them rather than fabricating a URL."""
    calls: list[str] = []

    def fake_http_get(url: str, **_):
        calls.append(url)
        return _FakeResponse(payload=_detail("hr", "1"))

    monkeypatch.setattr(sources, "http_get", fake_http_get)
    src = _tracked_with("gaaia", "frontier-act", "hr1", "xyz123")
    src.fetch()
    assert calls == ["https://api.congress.gov/v3/bill/119/hr/1"]
