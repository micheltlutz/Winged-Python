"""Ports HTMLTagTests, HTML5TagsTests, WhitespaceTests and PrettyPrintTests."""

from __future__ import annotations

import pytest

from winged import Br, Code, Col, Div, Element, Img, Input, P, Pre, RenderOptions, Strong, render

PRETTY = RenderOptions.pretty_()


def test_void_elements_have_no_closing_tag() -> None:
    # 0.1.0 rendered <col></col> and <source></source>.
    assert render(Br()) == "<br>"
    assert render(Col()) == "<col>"


def test_void_element_refuses_a_child() -> None:
    # 0.1.0 accepted the child and silently discarded it.
    with pytest.raises(ValueError, match="void element"):
        Element("br", P("x"))


def test_xhtml_self_closing() -> None:
    xhtml = RenderOptions(xhtml_self_closing=True)
    assert render(Img("x", "y"), xhtml) == '<img src="x" alt="y" />'


def test_state_is_per_instance() -> None:
    # 0.1.0 held _tag, _attributes and _children as class attributes.
    first, second = Div(), Div()
    first.child(P("x"))
    assert render(second) == "<div></div>"


def test_rendering_is_idempotent() -> None:
    # 0.1.0's Table.get_string() appended its rows on every call.
    tree = Div(P("x"))
    assert render(tree) == render(tree) == "<div><p>x</p></div>"


def test_keyword_attributes() -> None:
    assert render(Div(cls="a", data_user_id="7", hidden=True)) == (
        '<div class="a" data-user-id="7" hidden></div>'
    )


def test_false_and_none_attributes_are_omitted() -> None:
    assert render(Input(type_="text", disabled=False, placeholder=None)) == '<input type="text">'


def test_name_attribute_does_not_collide_with_the_tag_name() -> None:
    assert render(Input(type_="email", name="email")) == '<input type="email" name="email">'


def test_text_children_render_inline_in_pretty_mode() -> None:
    assert render(P("Fuel & chain"), PRETTY) == "<p>Fuel &amp; chain</p>"


def test_element_children_are_indented() -> None:
    assert render(Div(P("a"), P("b")), PRETTY) == "<div>\n  <p>a</p>\n  <p>b</p>\n</div>"


def test_whitespace_sensitive_subtrees_stay_compact() -> None:
    # Indentation injected into <pre> changes what the browser displays.
    assert render(Pre(Code("  two\n  lines")), PRETTY) == "<pre><code>  two\n  lines</code></pre>"


def test_mixed_content() -> None:
    assert render(P("Hello ", Strong("world"))) == "<p>Hello <strong>world</strong></p>"
