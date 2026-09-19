"""Ports SitemapGeneratorTests.swift and RSSGeneratorTests.swift."""

from __future__ import annotations

import xml.etree.ElementTree as ET
from datetime import datetime, timezone

import pytest

from winged.feed import RssGenerator, RssItem, rfc822
from winged.sitemap import SitemapGenerator, SitemapUrl


def test_sitemap_escapes_ampersands() -> None:
    out = SitemapGenerator("https://x.example").generate([SitemapUrl("/a?x=1&y=2")])
    assert "&amp;" in out
    assert "?x=1&y=2" not in out


def test_priority_keeps_one_decimal_place() -> None:
    out = SitemapGenerator("https://x.example").generate([SitemapUrl("/", priority=0.8)])
    assert "<priority>0.8</priority>" in out


def test_unset_optionals_emit_no_element() -> None:
    out = SitemapGenerator("https://x.example").generate([SitemapUrl("/")])
    assert "<lastmod>" not in out and "<changefreq>" not in out and "<priority>" not in out


def test_invalid_changefreq_raises_at_construction() -> None:
    with pytest.raises(ValueError, match="changefreq"):
        SitemapUrl("/", changefreq="fortnightly")


def test_invalid_priority_raises() -> None:
    with pytest.raises(ValueError, match="priority"):
        SitemapUrl("/", priority=2.0)


def test_relative_loc_is_resolved_against_the_base() -> None:
    out = SitemapGenerator("https://x.example/").generate([SitemapUrl("/a")])
    assert "<loc>https://x.example/a</loc>" in out


def test_sitemap_is_valid_xml() -> None:
    out = SitemapGenerator("https://x.example").generate([SitemapUrl("/", priority=1.0)])
    ET.fromstring(out)


def test_feed_is_valid_rss() -> None:
    out = RssGenerator(title="T", link="L", description="D").generate(
        [RssItem(title="a", link="b", description="c")]
    )
    root = ET.fromstring(out)
    assert root.tag == "rss" and root.attrib["version"] == "2.0"


def test_guid_defaults_to_the_link() -> None:
    out = RssGenerator(title="T", link="L", description="D").generate(
        [RssItem(title="a", link="https://x.example/p", description="c")]
    )
    assert '<guid isPermaLink="true">https://x.example/p</guid>' in out


def test_markup_in_a_description_round_trips() -> None:
    out = RssGenerator(title="T", link="L", description="D").generate(
        [RssItem(title="a", link="b", description="<b>x</b> & y")]
    )
    item = ET.fromstring(out).find("./channel/item/description")
    assert item is not None and item.text == "<b>x</b> & y"


def test_rfc822_is_not_iso8601() -> None:
    formatted = rfc822(datetime(2026, 8, 11, 10, 0, 0, tzinfo=timezone.utc))
    assert formatted == "Tue, 11 Aug 2026 10:00:00 +0000"


def test_naive_datetimes_are_treated_as_utc() -> None:
    assert rfc822(datetime(2026, 8, 11, 10, 0, 0)).endswith("+0000")
