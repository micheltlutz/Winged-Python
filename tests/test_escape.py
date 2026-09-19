"""Ports Tests/WingedSwiftTests/HTMLEscapeTests.swift."""

from __future__ import annotations

import pytest

from winged import escape_attribute, escape_text, escape_xml


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("<script>alert('XSS')</script>", "&lt;script&gt;alert(&#x27;XSS&#x27;)&lt;/script&gt;"),
        ("a & b", "a &amp; b"),
        ('say "hi"', "say &quot;hi&quot;"),
        ("", ""),
        ("plain", "plain"),
    ],
)
def test_escape_text(raw: str, expected: str) -> None:
    assert escape_text(raw) == expected


def test_ampersand_is_escaped_first() -> None:
    # Any other order produces "&amp;lt;".
    assert escape_text("<") == "&lt;"
    assert escape_text("&lt;") == "&amp;lt;"


def test_slashes_are_left_alone_by_default() -> None:
    # WingedSwift escaped these unconditionally until 1.5.0, turning every date into soup.
    assert escape_text("2026/09/18") == "2026/09/18"
    assert escape_text("a/b", escape_slashes=True) == "a&#x2F;b"


def test_attribute_context_keeps_angle_brackets() -> None:
    escaped = escape_attribute('a "quoted" & <tagged> value')
    assert escaped == "a &quot;quoted&quot; &amp; <tagged> value"


def test_escape_xml() -> None:
    assert escape_xml("a & b <c> 'd'") == "a &amp; b &lt;c&gt; &apos;d&apos;"
