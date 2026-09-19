"""Rendering options and the top-level :func:`render` entry point.

Ports ``Winged-Swift/Sources/WingedSwift/core/RenderOptions.swift`` and the buffered
``write(into:options:indentLevel:)`` primitive introduced in WingedSwift 2.0.0.

Options are a value passed into each call, never module-level state, so two callers can
render with different settings at the same time.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Protocol, runtime_checkable

if TYPE_CHECKING:
    from typing import Self

__all__ = ["Node", "RenderOptions", "render"]


@dataclass(frozen=True, slots=True)
class RenderOptions:
    """How a tree is turned into markup."""

    #: Place children on their own lines and indent them.
    pretty: bool = False
    #: One indentation level. Only used when ``pretty`` is true.
    indent: str = "  "
    #: Close void elements as ``<img />`` instead of the HTML5 ``<img>``.
    xhtml_self_closing: bool = False

    @classmethod
    def compact(cls) -> Self:
        """Minified output on a single line — the default, and what you should ship."""
        return cls()

    @classmethod
    def pretty_(cls) -> Self:
        """Indented, human-readable output.

        Named with a trailing underscore because ``pretty`` is already a field.
        """
        return cls(pretty=True)


@runtime_checkable
class Node(Protocol):
    """Anything that can write itself into the output buffer.

    ``write_into`` is the single overridable primitive. WingedSwift 2.0.0 rewrote
    rendering this way to stop building one string per node; keep that property by
    appending into the buffer and joining once.
    """

    def write_into(self, buf: list[str], options: RenderOptions, depth: int) -> None: ...


def render(node: Node, options: RenderOptions | None = None) -> str:
    """Render ``node`` to markup. Compact unless told otherwise."""
    buf: list[str] = []
    node.write_into(buf, options or RenderOptions(), 0)
    return "".join(buf)
