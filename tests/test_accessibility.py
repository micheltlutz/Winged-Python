"""The audit ROADMAP.md asks for. Each rule has a test that fires it and one that does not."""

from __future__ import annotations

from winged import (
    H1,
    H3,
    A,
    Body,
    Button,
    Div,
    Document,
    Element,
    Form,
    Head,
    Iframe,
    Img,
    Input,
    Label,
    P,
    render,
)
from winged.accessibility import audit


def rules(node: object) -> set[str]:
    return {issue.rule for issue in audit(node)}


def test_a_clean_page_reports_nothing() -> None:
    assert audit(Document(Head(), Body(H1("a"), P("b")))) == []


def test_img_alt() -> None:
    assert "img-alt" in rules(Element("img", src="x"))
    assert "img-alt" not in rules(Img("x", "a photo"))


def test_iframe_title() -> None:
    assert "iframe-title" in rules(Element("iframe", src="x"))
    assert "iframe-title" not in rules(Iframe("x", "a map"))


def test_button_label() -> None:
    assert "button-label" in rules(Button())
    assert "button-label" not in rules(Button("Send"))
    assert "button-label" not in rules(Button(aria_label="Send"))


def test_link_text() -> None:
    assert "link-text" in rules(A(Img("x", ""), href="/"))
    assert "link-text" not in rules(A(Img("x", "Home"), href="/"))


def test_heading_order() -> None:
    assert "heading-order" in rules(Div(H1("a"), H3("b")))
    assert "heading-order" not in rules(Div(H1("a"), P("b")))


def test_html_lang() -> None:
    assert "html-lang" in rules(Document(Head(), Body(), lang=""))
    assert "html-lang" not in rules(Document(Head(), Body(), lang="pt-BR"))


def test_form_label() -> None:
    assert "form-label" in rules(Form(Input(type_="text", id_="a")))
    assert "form-label" not in rules(Form(Label("A", for_="a"), Input(type_="text", id_="a")))
    assert "form-label" not in rules(Form(Input(type_="hidden")))


def test_duplicate_id() -> None:
    assert "duplicate-id" in rules(Div(Div(id_="x"), Div(id_="x")))
    assert "duplicate-id" not in rules(Div(Div(id_="x"), Div(id_="y")))


def test_audit_never_mutates_the_tree() -> None:
    tree = Div(H1("a"), Img("x", "y"))
    before = render(tree)
    audit(tree)
    assert render(tree) == before


def test_issues_carry_a_path() -> None:
    issues = audit(Div(Button()))
    assert issues and "button" in issues[0].path
