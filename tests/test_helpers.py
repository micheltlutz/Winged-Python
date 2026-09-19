"""Ports CSSHelpersTests.swift and AttributeHelpersTests.swift."""

from __future__ import annotations

from winged import Div, render


def test_add_class_appends() -> None:
    assert render(Div().add_class("a").add_class("b")) == '<div class="a b"></div>'


def test_add_classes() -> None:
    assert render(Div().add_classes("a", "b", "c")) == '<div class="a b c"></div>'


def test_class_values_cannot_escape_the_attribute() -> None:
    # WingedSwift 1.5.0 fixed this injection: the value used to be written verbatim, so a
    # quote in dynamic data closed the attribute and opened a new one.
    out = render(Div().add_class('x" onclick="evil()'))
    assert out == '<div class="x&quot; onclick=&quot;evil()"></div>'
    # The quotes are entities, so there is exactly one attribute on the element.
    assert out.count('="') == 1


def test_no_double_escaping_on_repeated_add_class() -> None:
    assert render(Div().add_class("a & b").add_class("c")) == '<div class="a &amp; b c"></div>'


def test_set_id_style_role() -> None:
    element = Div().set_id("x").set_style("color: red").set_role("banner")
    assert render(element) == '<div id="x" style="color: red" role="banner"></div>'


def test_data_and_aria_attrs_are_deterministic() -> None:
    # WingedSwift takes a Dictionary here, so its order varies between runs. Insertion
    # order here, which is what makes golden files possible.
    element = Div().data_attrs({"b": "2", "a": "1"}).aria_attrs({"label": "x"})
    assert render(element) == '<div data-b="2" data-a="1" aria-label="x"></div>'
