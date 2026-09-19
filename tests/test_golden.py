"""Byte-for-byte parity with Winged-Swift's frozen fixtures.

This is what makes "parity with Winged-Swift" a test rather than a claim. The four files
in ``tests/fixtures`` are copies of ``Winged-Swift/Tests/WingedSwiftTests/Fixtures``, so
the suite runs on a clone with no Swift checkout.

``WINGED_UPDATE_FIXTURES=1 pytest`` rewrites a fixture **and fails the run**, saying to
re-run and compare. A regeneration switch that silently passes is how a golden suite stops
meaning anything.
"""

from __future__ import annotations

import os
from datetime import datetime, timezone
from pathlib import Path

import pytest

from tests.marketing import marketing_page
from winged import RenderOptions, render
from winged.feed import RssGenerator, RssItem, rfc822
from winged.sitemap import SitemapGenerator, SitemapUrl

FIXTURES = Path(__file__).parent / "fixtures"


def check(name: str, produced: str) -> None:
    path = FIXTURES / name
    if os.environ.get("WINGED_UPDATE_FIXTURES"):
        path.write_text(produced, encoding="utf-8", newline="\n")
        pytest.fail(f"wrote {name} — re-run the tests to compare against it")
    assert produced == path.read_text(encoding="utf-8")


def test_marketing_compact() -> None:
    check("marketing-compact.html", render(marketing_page()))


def test_marketing_pretty() -> None:
    check("marketing-pretty.html", render(marketing_page(), RenderOptions.pretty_()))


def test_sitemap() -> None:
    generator = SitemapGenerator("https://ridekeeper.example")
    produced = generator.generate(
        [
            SitemapUrl("https://ridekeeper.example/", changefreq="weekly", priority=1.0),
            SitemapUrl(
                "https://ridekeeper.example/pricing?plan=pro&billing=year",
                lastmod="2026-08-11",
                changefreq="monthly",
                priority=0.7,
            ),
        ]
    )
    check("sitemap.xml", produced)


def test_feed() -> None:
    generator = RssGenerator(
        title="RideKeeper",
        link="https://ridekeeper.example",
        description="Release notes",
        language="pt-BR",
        self_url="https://ridekeeper.example/feed.xml",
    )
    produced = generator.generate(
        [
            RssItem(
                title="1.2 — tyres & chain",
                link="https://ridekeeper.example/blog/1-2",
                description="Tyre pressure log <and> chain reminders",
                pub_date=rfc822(datetime(2026, 8, 11, 10, 0, 0, tzinfo=timezone.utc)),
                categories=["release"],
            )
        ]
    )
    check("feed.xml", produced)
