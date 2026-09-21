"""Ports Tests/WingedSwiftTests/HTMLTagTests.swift and HTML14FeaturesTests.swift."""

from __future__ import annotations

from winged import Attribute


def test_value_is_escaped_at_construction() -> None:
    assert Attribute("title", 'a "q" & <t> v').value == "a &quot;q&quot; &amp; <t> v"


def test_boolean_renders_as_a_bare_key() -> None:
    assert Attribute.boolean("required").render() == " required"
    assert Attribute.boolean("required").value is None


def test_raw_does_not_escape() -> None:
    assert Attribute.raw("property", "og:title").value == "og:title"


def test_rendering_twice_does_not_escape_twice() -> None:
    attribute = Attribute("x", "a & b")
    assert attribute.render() == attribute.render() == ' x="a &amp; b"'


def test_attribute_is_frozen() -> None:
    import pytest

    attribute = Attribute("x", "y")
    with pytest.raises(Exception):  # noqa: B017 -- dataclass raises FrozenInstanceError
        attribute.key = "z"  # type: ignore[misc]
