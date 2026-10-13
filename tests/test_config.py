"""Config loading behavior: sources.yaml and keywords.yaml (plan Phase 1)."""

from pathlib import Path

import pytest
import yaml

from watcher.config import load_keywords, load_sources

SOURCES_YAML = """\
congress: 119
sources:
  - id: trahan-press
    type: html_diff
    chamber: house
    url: https://trahan.house.gov/media/press-releases
    selectors:
      entry: "li.press-item"
      title: "a"
      link: "a"
      date: "span.date"
  - id: senate-commerce-press
    type: rss
    chamber: senate
    url: https://www.commerce.senate.gov/rss
    enabled: false
"""

KEYWORDS_YAML = """\
tracked_bills:
  - id: hr9363
    aliases: ["H.R. 9363", "CAISI"]
keywords:
  high: [artificial intelligence, AI]
  medium: [NIST]
  low: [innovation]
kind_boost:
  markup: 3
  press: 1
threshold: 3
"""


def write(tmp_path, name, text):
    p = tmp_path / name
    p.write_text(text)
    return p


def test_load_sources_parses_fields(tmp_path):
    cfgs = load_sources(write(tmp_path, "sources.yaml", SOURCES_YAML))
    assert len(cfgs) == 2
    trahan = cfgs[0]
    assert trahan.id == "trahan-press"
    assert trahan.type == "html_diff"
    assert trahan.chamber == "house"
    assert trahan.selectors["entry"] == "li.press-item"


def test_load_sources_enabled_defaults_true(tmp_path):
    cfgs = load_sources(write(tmp_path, "sources.yaml", SOURCES_YAML))
    assert cfgs[0].enabled is True
    assert cfgs[1].enabled is False


def test_load_sources_rejects_unknown_adapter_type(tmp_path):
    bad = SOURCES_YAML.replace("type: rss", "type: telepathy")
    with pytest.raises(ValueError, match="telepathy"):
        load_sources(write(tmp_path, "sources.yaml", bad))


def test_load_keywords_parses_tracked_bills_and_tiers(tmp_path):
    kw = load_keywords(write(tmp_path, "keywords.yaml", KEYWORDS_YAML))
    assert kw.tracked_bills[0].id == "hr9363"
    assert "CAISI" in kw.tracked_bills[0].aliases
    assert "artificial intelligence" in kw.tiers["high"]
    assert kw.kind_boost["markup"] == 3
    assert kw.threshold == 3


REAL_SOURCES_YAML = Path(__file__).resolve().parents[1] / "config" / "sources.yaml"


def test_real_sources_yaml_has_explicit_enabled_on_every_row():
    """Config discipline (issue #9): no bare `enabled` — a quick `grep 'enabled: true'`
    must equal the number of live sources."""
    doc = yaml.safe_load(REAL_SOURCES_YAML.read_text())
    bare = [row["id"] for row in doc["sources"] if "enabled" not in row]
    assert bare == [], f"rows missing an explicit enabled flag: {bare}"


def test_real_sources_yaml_probed_dead_rows_are_disabled():
    """`disposition: probed-dead` tags endpoints that were probed and don't exist;
    such a row must never be enabled."""
    doc = yaml.safe_load(REAL_SOURCES_YAML.read_text())
    dead = [row for row in doc["sources"] if row.get("disposition") == "probed-dead"]
    assert dead, "expected at least one probed-dead row"
    assert all(row["enabled"] is False for row in dead)


def test_load_keywords_threshold_defaults_when_absent(tmp_path):
    text = KEYWORDS_YAML.replace("threshold: 3\n", "")
    kw = load_keywords(write(tmp_path, "keywords.yaml", text))
    assert kw.threshold == 3
