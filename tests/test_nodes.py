"""Ports Tests/WingedSwiftTests/FragmentTests.swift."""

from __future__ import annotations

import pytest

from winged import Comment, Div, Fragment, P, RawHtml, RenderOptions, render

PRETTY = RenderOptions.pretty_()


def test_fragment_is_transparent() -> None:
    assert render(Div(Fragment(P("a"), P("b")))) == render(Div(P("a"), P("b")))


def test_fragment_keeps_indentation_and_raw_html_does_not() -> None:
    assert render(Div(Fragment(P("a"), P("b"))), PRETTY) == render(Div(P("a"), P("b")), PRETTY)
    assert render(Div(RawHtml("<p>a</p><p>b</p>")), PRETTY) == "<div><p>a</p><p>b</p></div>"


def test_bare_strings_are_escaped_and_raw_html_is_not() -> None:
    assert render(Div("<b>x</b>")) == "<div>&lt;b&gt;x&lt;/b&gt;</div>"
    assert render(Div(RawHtml("<b>x</b>"))) == "<div><b>x</b></div>"


def test_comment() -> None:
    assert render(Comment("note")) == "<!-- note -->"


def test_comment_rejects_a_double_hyphen() -> None:
    with pytest.raises(ValueError, match=r"--"):
        Comment("a -- b")


def test_none_children_are_dropped() -> None:
    assert render(Div(None, P("x"))) == "<div><p>x</p></div>"


def test_iterables_are_flattened() -> None:
    assert render(Div([P("a"), P("b")])) == "<div><p>a</p><p>b</p></div>"
    assert render(Div(P(str(n)) for n in range(2))) == "<div><p>0</p><p>1</p></div>"
