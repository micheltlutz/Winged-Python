"""The two tag sets that change how an element renders."""

from __future__ import annotations

__all__ = ["VOID_ELEMENTS", "WHITESPACE_SENSITIVE"]

#: Elements that have no closing tag and take no children.
#:
#: 0.1.0 knew only ``br``, ``hr``, ``img``, ``input``, ``link`` and ``meta``, so it
#: rendered ``<col></col>`` and ``<source></source>``. WingedSwift fixed the same bug in
#: 1.5.0.
VOID_ELEMENTS = frozenset(
    {
        "area",
        "base",
        "br",
        "col",
        "embed",
        "hr",
        "img",
        "input",
        "link",
        "meta",
        "param",
        "source",
        "track",
        "wbr",
    }
)

#: Elements whose content is displayed as written.
#:
#: These render compactly even in pretty mode: indentation injected into a ``<pre>``
#: changes what the browser shows the reader.
WHITESPACE_SENSITIVE = frozenset({"pre", "code", "textarea"})
