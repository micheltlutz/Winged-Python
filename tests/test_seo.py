"""Ports Tests/WingedSwiftTests/SEOTests.swift."""

from __future__ import annotations

from winged import render
from winged.seo import SeoBuilder, common, open_graph, open_graph_article, twitter_card


def test_open_graph_uses_property() -> None:
    out = render(open_graph(title="T", description="D", image="I", url="U"))
    assert '<meta property="og:title" content="T">' in out
    assert 'name="og:title"' not in out


def test_twitter_uses_name() -> None:
    out = render(twitter_card(title="T", description="D", image="I"))
    assert '<meta name="twitter:card" content="summary_large_image">' in out


def test_unset_optionals_emit_nothing() -> None:
    out = render(open_graph(title="T", description="D", image="I", url="U"))
    assert "og:site_name" not in out
    assert 'content=""' not in out


def test_common_does_not_emit_a_title() -> None:
    # Matching WingedSwift: a page places its own <title>, so a meta helper injecting one
    # into the middle of the head would make ordering surprising.
    assert "<title>" not in render(common(title="T", description="D"))


def test_values_are_escaped() -> None:
    out = render(common(title="T", description='a "quoted" & <tagged> value'))
    assert "&quot;quoted&quot; &amp;" in out


def test_article_tags_render_in_order() -> None:
    out = render(open_graph_article(tags=["a", "b"]))
    assert out.index('content="a"') < out.index('content="b"')


def test_builder_order_is_common_then_og_then_twitter() -> None:
    out = render(SeoBuilder(title="T", description="D", image="I", url="U").build())
    assert out.index("charset") < out.index("og:title") < out.index("twitter:card")


def test_optional_open_graph_fields() -> None:
    out = render(
        open_graph(
            title="T",
            description="D",
            image="I",
            url="U",
            site_name="S",
            locale="pt_BR",
            type_="article",
        )
    )
    assert 'property="og:site_name" content="S"' in out
    assert 'property="og:locale" content="pt_BR"' in out
    assert 'property="og:type" content="article"' in out


def test_optional_twitter_fields() -> None:
    out = render(twitter_card(title="T", description="D", image="I", site="@s", creator="@c"))
    assert 'name="twitter:site" content="@s"' in out
    assert 'name="twitter:creator" content="@c"' in out


def test_common_optional_fields() -> None:
    out = render(common(title="T", description="D", keywords=["a", "b"], author="Me"))
    assert 'content="a, b"' in out
    assert 'name="author" content="Me"' in out


def test_article_metadata() -> None:
    out = render(
        open_graph_article(
            published_time="2026-01-01",
            modified_time="2026-02-01",
            author="Me",
            section="Tech",
        )
    )
    for key in ("published_time", "modified_time", "author", "section"):
        assert f"article:{key}" in out
