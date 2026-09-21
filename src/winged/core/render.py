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

__all__ = ["Buffer", "Node", "RenderOptions", "Sink", "render", "render_into"]


@runtime_checkable
class Buffer(Protocol):
    """Where a node writes its output.

    ``list[str]`` is the one :func:`render` uses, and the one to reach for. The protocol
    exists so :func:`render_into` can pass an adapter that forwards straight to a file
    instead, without every ``write_into`` having to know which it got.
    """

    def append(self, chunk: str, /) -> None: ...


@runtime_checkable
class Sink(Protocol):
    """The part of a text file object :func:`render_into` needs."""

    def write(self, chunk: str, /) -> int | None: ...


class _SinkBuffer:
    """A :class:`Buffer` that forwards each chunk to a file rather than keeping it.

    This is the whole of streaming: every node already appends small pieces, so sending
    them onwards one at a time keeps memory flat no matter how large the page is.
    """

    __slots__ = ("_sink",)

    def __init__(self, sink: Sink) -> None:
        self._sink = sink

    def append(self, chunk: str, /) -> None:
        self._sink.write(chunk)


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

    def write_into(self, buf: Buffer, options: RenderOptions, depth: int) -> None: ...


def render(node: Node, options: RenderOptions | None = None) -> str:
    """Render ``node`` to markup. Compact unless told otherwise."""
    buf: list[str] = []
    node.write_into(buf, options or RenderOptions(), 0)
    return "".join(buf)


def render_into(node: Node, sink: Sink, options: RenderOptions | None = None) -> None:
    """Render ``node`` straight into a text file object, holding no full copy in memory.

    ``render(page)`` builds the whole string first, which for a large generated page --
    a sitemap index, a catalogue -- means holding the markup twice: once in the pieces,
    once joined. Writing as it goes is the same output, in constant memory.

        with open("index.html", "w", encoding="utf-8") as handle:
            render_into(page, handle)
    """
    node.write_into(_SinkBuffer(sink), options or RenderOptions(), 0)
