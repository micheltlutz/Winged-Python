"""The :class:`Document` type.

Ports ``Winged-Swift/Sources/WingedSwift/core/Document.swift``, added in WingedSwift 2.0.0.

A document owns the two things every page has and nobody should hand-assemble: the doctype
and the ``lang`` attribute. 0.1.0's answer was a fake ``Doctype`` tag whose ``_tag`` was the
literal string ``"<!DOCTYPE html>"``, so the doctype was a sibling node the user had to
remember to place, and ``lang`` was nobody's job at all.
"""

from __future__ import annotations

from .core.escape import escape_attribute
from .core.render import Buffer, Node, RenderOptions

__all__ = ["Document"]


class Document:
    """A complete HTML page: doctype, ``<html lang>``, head and body."""

    __slots__ = ("body", "head", "lang")

    def __init__(self, head: Node, body: Node, *, lang: str = "en") -> None:
        self.head = head
        self.body = body
        self.lang = lang

    def write_into(self, buf: Buffer, options: RenderOptions, depth: int) -> None:
        # The newline after the doctype is present in compact output too: WingedSwift's
        # own compact fixture starts "<!DOCTYPE html>\n<html ...".
        buf.append("<!DOCTYPE html>\n")
        buf.append(f'<html lang="{escape_attribute(self.lang)}">')

        for child in (self.head, self.body):
            if options.pretty:
                buf.append("\n")
                buf.append(options.indent * (depth + 1))
            child.write_into(buf, options, depth + 1)

        if options.pretty:
            buf.append("\n")
            buf.append(options.indent * depth)
        buf.append("</html>")
