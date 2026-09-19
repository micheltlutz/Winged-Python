"""Elements whose signature enforces something.

WingedSwift makes ``alt`` and ``title`` required by construction on these two, and the
requirement is an accessibility guarantee rather than a convenience: the ``img-alt`` and
``iframe-title`` rules in :mod:`winged.accessibility` cannot fire for an element built
through these constructors.
"""

from __future__ import annotations

from .core.element import AttrValue, Element

__all__ = ["Iframe", "Img"]


class Img(Element):
    """``<img>``. ``alt`` is required — pass ``""`` for a decorative image."""

    def __init__(self, src: str, alt: str, **attrs: AttrValue) -> None:
        super().__init__("img", src=src, alt=alt, **attrs)


class Iframe(Element):
    """``<iframe>``. ``title`` is required: a frame without one is unusable by a screen reader."""

    def __init__(self, src: str, title: str, **attrs: AttrValue) -> None:
        super().__init__("iframe", src=src, title=title, **attrs)
