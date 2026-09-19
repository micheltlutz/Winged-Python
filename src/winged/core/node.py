"""The leaf and grouping nodes.

Ports ``Winged-Swift/Sources/WingedSwift/core/Fragment.swift`` and ``RawHTML.swift``.
:class:`Comment` has no WingedSwift counterpart; winged-rust added one for the same reason.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import TypeAlias

from .escape import escape_text
from .render import Node, RenderOptions

__all__ = ["Child", "Comment", "Fragment", "RawHtml", "Text", "coerce", "flatten"]

#: What may be passed as a child.
#:
#: A bare ``str`` becomes escaped :class:`Text`; ``None`` is dropped, so
#: ``Div(x if cond else None)`` is the conditional form; and an iterable is flattened, so
#: ``Ul(Li(x) for x in items)`` and ``Ul([Li("a"), Li("b")])`` both work. That last case
#: is the job WingedSwift needs ``buildArray`` and a generic ``buildExpression`` for.
Child: TypeAlias = "Node | str | Iterable[Child] | None"


class Text:
    """Escaped text. This is what a bare ``str`` child becomes."""

    __slots__ = ("content",)

    def __init__(self, content: str) -> None:
        self.content = content

    def write_into(self, buf: list[str], options: RenderOptions, depth: int) -> None:
        buf.append(escape_text(self.content))


class RawHtml:
    """Markup injected verbatim.

    The only way to put unescaped markup into the output, and deliberately conspicuous at
    the call site. Unlike :class:`Fragment` it flattens to a raw string, so pretty-print
    indentation is lost inside it.
    """

    __slots__ = ("html",)

    def __init__(self, html: str) -> None:
        self.html = html

    def write_into(self, buf: list[str], options: RenderOptions, depth: int) -> None:
        buf.append(self.html)


class Fragment:
    """A transparent group: renders its children with no wrapper element.

    Keeps the tree, so pretty-print indentation still works. That is the whole difference
    from :class:`RawHtml`, and it is the distinction people get wrong.
    """

    __slots__ = ("children",)

    def __init__(self, *children: Child) -> None:
        self.children: list[Node] = [coerce(c) for c in flatten(children)]

    def write_into(self, buf: list[str], options: RenderOptions, depth: int) -> None:
        for index, child in enumerate(self.children):
            if options.pretty and index:
                buf.append("\n")
                buf.append(options.indent * depth)
            child.write_into(buf, options, depth)


class Comment:
    """An HTML comment."""

    __slots__ = ("text",)

    def __init__(self, text: str) -> None:
        # "--" cannot appear inside an HTML comment: it would close it early.
        if "--" in text:
            raise ValueError("an HTML comment cannot contain '--'")
        self.text = text

    def write_into(self, buf: list[str], options: RenderOptions, depth: int) -> None:
        buf.append(f"<!-- {self.text} -->")


def flatten(children: Iterable[object]) -> list[object]:
    """Flatten nested iterables and drop ``None``.

    This is the work WingedSwift needs ``buildArray`` and a generic ``buildExpression``
    for. ``None`` is dropped so ``Div(x if cond else None)`` is the conditional form.
    """
    out: list[object] = []
    for child in children:
        if child is None:
            continue
        if isinstance(child, str) or not isinstance(child, Iterable):
            out.append(child)
        else:
            out.extend(flatten(child))
    return out


def coerce(child: object) -> Node:
    """Turn a child into a node. A ``str`` is escaped; that is the default."""
    if isinstance(child, str):
        return Text(child)
    if isinstance(child, Node):
        return child
    raise TypeError(f"not a valid child: {child!r} ({type(child).__name__})")
