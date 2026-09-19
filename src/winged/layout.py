"""The :class:`Layout` protocol.

Ports ``Winged-Swift/Sources/WingedSwift/templates/Layout.swift``.

A layout wraps content in a consistent shell -- header, navigation, footer -- so a page
states only what differs. It is a ``Protocol`` rather than an ABC because structural
typing is the closer analogue of a Swift protocol: a class satisfies it by defining
``render``, with no base class and no registration. (Contrast 0.1.0's
``ElementAbstract``, which inherited nothing and enforced nothing.)
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from .core.node import Fragment
from .core.render import Node

__all__ = ["Layout", "render_many"]


@runtime_checkable
class Layout(Protocol):
    """Wraps content with a page's common structure."""

    def render(self, content: Node) -> Node: ...


def render_many(layout: Layout, contents: Sequence[Node]) -> Node:
    """Wrap a sequence of nodes in one layout.

    The nodes are grouped in a :class:`Fragment`, so no wrapper element is injected and
    pretty-print indentation is preserved.
    """
    return layout.render(Fragment(*contents))
