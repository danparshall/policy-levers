"""congress.gov API adapter — normalize bill payloads to Items (plan Phase 4.1).

Two payload shapes:
- List: `{"bills": [{...}, ...]}` from `/v3/bill/{congress}` (keyword-poller mode)
- Detail: `{"bill": {...}}` from `/v3/bill/{congress}/{type}/{number}` (tracked-bill mode)

Uids embed the bill id (hrNNNN, sNNNN, …) so the scorer's `match_tracked` can fire
even when the official long title never mentions the bill number.
"""

from __future__ import annotations

from watcher.models import Item, SourceError, make_bill_uid


def _chamber(row: dict) -> str:
    code = (row.get("originChamberCode") or "").upper()
    if code == "H":
        return "house"
    if code == "S":
        return "senate"
    chamber = (row.get("originChamber") or "").lower()
    if chamber.startswith("house"):
        return "house"
    if chamber.startswith("senate"):
        return "senate"
    return "joint"


def _bill_id(row: dict) -> str:
    bill_type = (row.get("type") or "").lower()
    number = str(row.get("number") or "").strip()
    if not bill_type or not number:
        raise SourceError(f"bill row missing type/number: {row!r}")
    return f"{bill_type}{number}"


def _bill_to_item(row: dict, source_id: str, kind: str, action_code: str) -> Item:
    latest_action = row.get("latestAction") or {}
    action_date = latest_action.get("actionDate")
    action_text = (latest_action.get("text") or "").strip()
    if not action_date:
        raise SourceError(f"bill row missing latestAction.actionDate: {row!r}")
    bill_id = _bill_id(row)
    uid = make_bill_uid(bill_id, action_code, action_date)
    # /v3/bill/{congress} list rows use `url` (api.congress.gov endpoint);
    # /v3/bill/{congress}/{type}/{number} detail returns `legislationUrl`
    # (congress.gov human-facing). Prefer the human-facing URL when available.
    url = (row.get("legislationUrl") or row.get("url") or "").strip()
    return Item(
        uid=uid,
        source=source_id,
        chamber=_chamber(row),
        kind=kind,
        title=(row.get("title") or "").strip(),
        url=url,
        date=action_date,
        body_excerpt=action_text,
    )


def parse_bill_list(payload: dict, *, source_id: str) -> list[Item]:
    if not isinstance(payload, dict) or "bills" not in payload:
        raise SourceError(f"expected {{'bills': [...]}}, got keys {list(payload)!r}")
    bills = payload.get("bills") or []
    if not isinstance(bills, list):
        raise SourceError(f"'bills' must be a list, got {type(bills).__name__}")
    items: list[Item] = []
    for row in bills:
        # Reserved-for-the-Speaker placeholder bills carry `latestAction: null` and
        # have no real content — real quirk observed 2026-08-04 in /v3/bill/119 output.
        # Skip cleanly, not a parse failure.
        if not row.get("latestAction"):
            continue
        items.append(_bill_to_item(row, source_id, "bill_intro", "intro"))
    return items


def parse_bill_detail(payload: dict, *, source_id: str) -> Item:
    if not isinstance(payload, dict) or "bill" not in payload:
        raise SourceError(f"expected {{'bill': {{...}}}}, got keys {list(payload)!r}")
    return _bill_to_item(payload["bill"], source_id, "bill_action", "action")
