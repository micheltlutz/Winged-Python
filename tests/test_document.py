"""Ports DocumentTests.swift, LayoutTests.swift and RenderOptionsTests.swift."""

from __future__ import annotations

from winged import (
    H1,
    Body,
    Document,
    Head,
    Layout,
    Main,
    P,
    RenderOptions,
    Title,
    render,
    render_many,
)
from winged.core.render import Node


def test_document_owns_the_doctype() -> None:
    assert render(Document(Head(), Body())).startswith('<!DOCTYPE html>\n<html lang="en">')


def test_lang_is_on_the_html_element() -> None:
    out = render(Document(Head(), Body(), lang="pt-BR"))
    assert '<html lang="pt-BR">' in out
    assert out.count("<!DOCTYPE") == 1


def test_document_pretty() -> None:
    out = render(Document(Head(Title("Home")), Body(H1("Hi"))), RenderOptions.pretty_())
    assert out == (
        '<!DOCTYPE html>\n<html lang="en">\n  <head>\n    <title>Home</title>\n  </head>\n'
        "  <body>\n    <h1>Hi</h1>\n  </body>\n</html>"
    )


class _Layout:
    def render(self, content: Node) -> Node:
        return Main(content)


def test_a_plain_class_satisfies_the_protocol() -> None:
    assert isinstance(_Layout(), Layout)


def test_render_many_injects_no_wrapper() -> None:
    assert render(render_many(_Layout(), [P("a"), P("b")])) == "<main><p>a</p><p>b</p></main>"


def test_render_options_are_values() -> None:
    assert RenderOptions.compact().pretty is False
    assert RenderOptions.pretty_().pretty is True
    assert RenderOptions(indent="\t").indent == "\t"
