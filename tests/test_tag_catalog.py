"""Ports Tests/WingedSwiftTests/TagCatalogTests.swift.

Every element in the table is constructed and rendered. 0.1.0 had 49 tag modules and tests
for four of them; this is the test that makes "every tag works" a fact rather than a hope,
and it is why adding a tag without a test is impossible.
"""

from __future__ import annotations

import pytest

import winged
from winged._tagtable import TAGS
from winged.core.render import render
from winged.core.tags import VOID_ELEMENTS, WHITESPACE_SENSITIVE
from winged.elements import Iframe, Img


@pytest.mark.parametrize(("name", "tag"), [(n, t) for n, t, _ in TAGS], ids=[n for n, _, _ in TAGS])
def test_every_element_renders(name: str, tag: str) -> None:
    element_type = getattr(winged, name)
    element = element_type() if tag in VOID_ELEMENTS else element_type("x")
    out = render(element)

    if tag in VOID_ELEMENTS:
        assert out == f"<{tag}>"
    else:
        assert out == f"<{tag}>x</{tag}>"


@pytest.mark.parametrize(("name", "tag"), [(n, t) for n, t, _ in TAGS], ids=[n for n, _, _ in TAGS])
def test_every_element_takes_attributes(name: str, tag: str) -> None:
    element = (
        getattr(winged, name)(**{"cls": "c"})
        if tag in VOID_ELEMENTS
        else getattr(winged, name)(cls="c")
    )
    assert 'class="c"' in render(element)


def test_every_element_is_exported() -> None:
    for name, _, _ in TAGS:
        assert name in winged.__all__, f"{name} is missing from winged.__all__"


def test_the_required_argument_elements() -> None:
    # Img needs alt and Iframe needs title, by construction. That is an accessibility
    # guarantee the signature enforces, as it is in WingedSwift.
    assert render(Img("/a.png", "A photo")) == '<img src="/a.png" alt="A photo">'
    assert render(Iframe("/a", "A map")) == '<iframe src="/a" title="A map"></iframe>'

    with pytest.raises(TypeError):
        Img("/a.png")  # type: ignore[call-arg]
    with pytest.raises(TypeError):
        Iframe("/a")  # type: ignore[call-arg]


def test_the_tag_sets_are_consistent_with_the_table() -> None:
    # "img" and "iframe" live in winged._special, because their signatures require an
    # argument; everything else comes from the table.
    known = {tag for _, tag, _ in TAGS} | {"img", "iframe"}

    # Every void element the renderer knows about is reachable, except <area> and
    # <param>, which WingedSwift does not ship either.
    assert VOID_ELEMENTS - known == {"area", "param"}
    assert known >= WHITESPACE_SENSITIVE
