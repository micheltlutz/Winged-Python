"""The :class:`Attribute` value type.

Ports ``Winged-Swift/Sources/WingedSwift/core/Attribute.swift``.

Replaces 0.1.0's ``winged/core/attribute.py``, which defined the identical ``class
Attribute`` body twice in the same file, and ``attribute_type.py``, whose entire content
was one ``Tuple[str, Optional[str]]`` alias.
"""

from __future__ import annotations

from dataclasses import dataclass

from .escape import escape_attribute

__all__ = ["BOOLEAN_ATTRIBUTES", "Attribute"]

#: Attributes whose presence is the value. They render as a bare key.
BOOLEAN_ATTRIBUTES = frozenset(
    {
        "async",
        "autofocus",
        "autoplay",
        "checked",
        "controls",
        "default",
        "defer",
        "disabled",
        "hidden",
        "ismap",
        "loop",
        "multiple",
        "muted",
        "novalidate",
        "open",
        "playsinline",
        "readonly",
        "required",
        "reversed",
        "selected",
    }
)


@dataclass(frozen=True, slots=True)
class Attribute:
    """One rendered attribute.

    Frozen on purpose: an attribute is a value, and sharing one between two elements must
    never let a mutation on one reach the other.

    The value is escaped **at construction**, not at render time, so rendering the same
    tree twice cannot escape it twice.
    """

    key: str
    value: str | None

    def __init__(self, key: str, value: str, *, escape: bool = True) -> None:
        object.__setattr__(self, "key", key)
        object.__setattr__(self, "value", escape_attribute(value) if escape else value)

    @classmethod
    def boolean(cls, key: str) -> Attribute:
        """An attribute that renders as a bare key: ``required``, not ``required="true"``."""
        attribute = cls.__new__(cls)
        object.__setattr__(attribute, "key", key)
        object.__setattr__(attribute, "value", None)
        return attribute

    @classmethod
    def raw(cls, key: str, value: str) -> Attribute:
        """An unescaped attribute.

        The documented escape hatch, never a default. WingedSwift's ``Meta`` needs it to
        insert its ``name`` / ``property`` / ``charset`` / ``http-equiv`` keys verbatim.
        """
        return cls(key, value, escape=False)

    def render(self) -> str:
        if self.value is None:
            return f" {self.key}"
        return f' {self.key}="{self.value}"'
