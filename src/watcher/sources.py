"""Live-source wiring (plan Phase 8).

Adapters are pure parse functions (they take a raw payload and return Items). This
module is what the orchestrator actually calls — one Source instance per row in
sources.yaml, each pairing a fetch helper with its adapter parse function.

Design invariants:
- Every fetch has a 30s timeout, one retry on transport errors, and a descriptive
  User-Agent — non-2xx / timeout / connection error → SourceError, which the
  orchestrator turns into a health warning without killing the run.
- No stateful auth: CONGRESS_API_KEY is passed as a query param per row when the
  source calls the congress.gov API. All other sources are unauthenticated.
- Time isn't hardcoded — `today` and `include_backlog_days` are injected so the
  smoke run, backtest, and future cron modes share one code path.
"""

from __future__ import annotations

import time
from datetime import date, timedelta
from typing import TYPE_CHECKING

import requests

from watcher.adapters.congress_api import parse_bill_detail, parse_bill_list
from watcher.adapters.html_diff import extract_entries
from watcher.adapters.rss import parse_feed
from watcher.adapters.structured import parse_floor_lookahead, parse_meeting_feed
from watcher.models import Item, SourceError

if TYPE_CHECKING:
    from watcher.config import Keywords, SourceConfig

USER_AGENT = (
    "policy-levers-watcher/0.1 "
    "(+https://github.com/danparshall/policy-levers; parshall.dan+leg-watcher@gmail.com)"
)
DEFAULT_TIMEOUT = 30  # seconds


def http_get(
    url: str,
    *,
    params: dict | None = None,
    headers: dict | None = None,
    timeout: int = DEFAULT_TIMEOUT,
) -> requests.Response:
    """One-retry GET with a descriptive UA. SourceError on any transport/status fail."""
    final_headers = {"User-Agent": USER_AGENT, "Accept": "*/*"}
    if headers:
        final_headers.update(headers)
    last_exc: Exception | None = None
    for attempt in (1, 2):
        try:
            resp = requests.get(url, params=params, headers=final_headers, timeout=timeout)
        except requests.RequestException as exc:
            last_exc = exc
            if attempt == 1:
                time.sleep(1)
                continue
            raise SourceError(f"transport error fetching {url}: {exc}") from exc
        if resp.status_code >= 400:
            # 4xx often means we're wrong (bad selectors, bad params); don't retry.
            if 400 <= resp.status_code < 500:
                raise SourceError(f"HTTP {resp.status_code} from {url}")
            # 5xx: retry once, then give up
            if attempt == 1:
                time.sleep(1)
                continue
            raise SourceError(f"HTTP {resp.status_code} from {url}")
        return resp
    # Unreachable but keeps the type checker happy.
    raise SourceError(f"exhausted retries fetching {url}: {last_exc}")


class CongressApiPollerSource:
    """Broad recent-bills poller. AI-relevance filtering happens in the scorer."""

    def __init__(
        self,
        cfg: SourceConfig,
        *,
        api_key: str,
        today: str,
        backlog_days: int,
    ) -> None:
        self.id = cfg.id
        self.enabled = cfg.enabled
        self._url = cfg.url.rstrip("/") + "/v3/bill/{congress}"
        self._api_key = api_key
        self._today = today
        self._backlog_days = backlog_days
        self._congress = int(cfg.params.get("congress", 119))
        self._limit = int(cfg.params.get("limit", 250))

    def fetch(self) -> list[Item]:
        # fromDateTime is a UTC timestamp; API accepts YYYY-MM-DDT00:00:00Z form.
        cutoff = date.fromisoformat(self._today) - timedelta(days=self._backlog_days)
        params = {
            "api_key": self._api_key,
            "format": "json",
            "fromDateTime": f"{cutoff.isoformat()}T00:00:00Z",
            "limit": self._limit,
            "sort": "updateDate+desc",
        }
        resp = http_get(self._url.format(congress=self._congress), params=params)
        try:
            payload = resp.json()
        except ValueError as exc:
            raise SourceError(f"{self.id}: non-JSON response") from exc
        return parse_bill_list(payload, source_id=self.id)


class CongressApiTrackedSource:
    """Per-tracked-bill latest-action watcher. One detail call per bill in keywords."""

    def __init__(
        self,
        cfg: SourceConfig,
        *,
        api_key: str,
        keywords: Keywords,
    ) -> None:
        self.id = cfg.id
        self.enabled = cfg.enabled
        self._url = cfg.url.rstrip("/") + "/v3/bill/{congress}/{type}/{number}"
        self._api_key = api_key
        self._congress = int(cfg.params.get("congress", 119))
        self._keywords = keywords

    def _bill_endpoints(self) -> list[tuple[str, str]]:
        """Turn tracked-bill ids like 'hr9925' or 's2938' into (type, number) pairs."""
        endpoints: list[tuple[str, str]] = []
        for bill in self._keywords.tracked_bills:
            slug = bill.id.strip().lower()
            # Split at the first digit: 'hr9925' -> ('hr', '9925'), 's2938' -> ('s', '2938')
            for i, ch in enumerate(slug):
                if ch.isdigit():
                    prefix, number = slug[:i], slug[i:]
                    if prefix and number:
                        endpoints.append((prefix, number))
                    break
        return endpoints

    def fetch(self) -> list[Item]:
        items: list[Item] = []
        errors: list[str] = []
        params = {"api_key": self._api_key, "format": "json"}
        for bill_type, number in self._bill_endpoints():
            url = self._url.format(congress=self._congress, type=bill_type, number=number)
            try:
                resp = http_get(url, params=params)
                payload = resp.json()
                items.append(parse_bill_detail(payload, source_id=self.id))
            except SourceError as exc:
                # A tracked bill that doesn't exist yet (e.g. GAAIA discussion draft
                # never got a number) is expected — skip individually, don't fail the
                # whole source. Aggregate to surface if ALL lookups failed.
                errors.append(f"{bill_type}{number}: {exc}")
                continue
        if not items and errors:
            raise SourceError(
                f"{self.id}: every tracked bill lookup failed ({'; '.join(errors)})"
            )
        return items


class RssSource:
    """Committee/member press feed. Follows the plan's Phase 4.2 shape."""

    def __init__(self, cfg: SourceConfig, *, today: str) -> None:
        self.id = cfg.id
        self.enabled = cfg.enabled
        self._url = cfg.url
        self._chamber = cfg.chamber
        self._today = today

    def fetch(self) -> list[Item]:
        resp = http_get(self._url, headers={"Accept": "application/rss+xml, application/xml"})
        return parse_feed(
            resp.content,
            source_id=self.id,
            chamber=self._chamber,
            today=self._today,
        )


class HtmlDiffSource:
    """Press listing with per-source CSS selectors. Stateless — novelty via state store."""

    def __init__(self, cfg: SourceConfig) -> None:
        self.id = cfg.id
        self.enabled = cfg.enabled
        self._url = cfg.url
        self._chamber = cfg.chamber
        self._selectors = cfg.selectors

    def fetch(self) -> list[Item]:
        resp = http_get(self._url, headers={"Accept": "text/html"})
        return extract_entries(
            resp.text,
            self._selectors,
            source_id=self.id,
            chamber=self._chamber,
            base_url=self._url,
        )


class MeetingFeedSource:
    """docs.house.gov meeting-feed XML (RSS-shaped) → markup/hearing Items."""

    def __init__(self, cfg: SourceConfig) -> None:
        self.id = cfg.id
        self.enabled = cfg.enabled
        self._url = cfg.url
        self._chamber = cfg.chamber

    def fetch(self) -> list[Item]:
        resp = http_get(self._url, headers={"Accept": "application/rss+xml, application/xml"})
        return parse_meeting_feed(resp.content, source_id=self.id, chamber=self._chamber)


class FloorLookaheadSource:
    """Majority Leader / Senate floor page → floor Items via html_diff selectors."""

    def __init__(self, cfg: SourceConfig) -> None:
        self.id = cfg.id
        self.enabled = cfg.enabled
        self._url = cfg.url
        self._chamber = cfg.chamber
        self._selectors = cfg.selectors

    def fetch(self) -> list[Item]:
        resp = http_get(self._url, headers={"Accept": "text/html"})
        return parse_floor_lookahead(
            resp.text,
            selectors=self._selectors,
            source_id=self.id,
            chamber=self._chamber,
            base_url=self._url,
        )


def build_sources(
    source_configs: list[SourceConfig],
    *,
    keywords: Keywords,
    api_key: str,
    today: str,
    backlog_days: int,
) -> list:
    """Pair each config row with the right Source class. Unknown params raise loud."""
    sources: list = []
    for cfg in source_configs:
        if cfg.type == "congress_api":
            mode = cfg.params.get("mode")
            if mode == "poller":
                sources.append(CongressApiPollerSource(
                    cfg, api_key=api_key, today=today, backlog_days=backlog_days,
                ))
            elif mode == "tracked":
                sources.append(CongressApiTrackedSource(
                    cfg, api_key=api_key, keywords=keywords,
                ))
            else:
                raise ValueError(
                    f"congress_api source {cfg.id!r} needs params.mode in "
                    "('poller','tracked'), got {mode!r}"
                )
        elif cfg.type == "rss":
            sources.append(RssSource(cfg, today=today))
        elif cfg.type == "html_diff":
            sources.append(HtmlDiffSource(cfg))
        elif cfg.type == "structured":
            subtype = cfg.params.get("subtype")
            if subtype == "meeting_feed":
                sources.append(MeetingFeedSource(cfg))
            elif subtype == "floor_lookahead":
                sources.append(FloorLookaheadSource(cfg))
            else:
                raise ValueError(
                    f"structured source {cfg.id!r} needs params.subtype in "
                    f"('meeting_feed','floor_lookahead'), got {subtype!r}"
                )
        else:
            # Config loader already validates VALID_ADAPTER_TYPES; belt-and-suspenders.
            raise ValueError(f"source {cfg.id!r} has unknown type {cfg.type!r}")
    return sources
