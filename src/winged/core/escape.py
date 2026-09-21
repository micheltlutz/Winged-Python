"""HTML and XML escaping.

Ports ``Winged-Swift/Sources/WingedSwift/core/HTMLEscape.swift``.

Winged-Python 0.1.0 had no escaping at all: ``String.get_string()`` returned its text
verbatim and ``Attribute`` interpolated values straight into ``key="value"``. Every value
that reaches the output now passes through one of these three functions.
"""

from __future__ import annotations

__all__ = ["escape_attribute", "escape_text", "escape_xml"]

# "&" is replaced first in every table below. Any other order double-escapes:
# "<" becomes "&lt;" becomes "&amp;lt;".
_TEXT = (
    ("&", "&amp;"),
    ("<", "&lt;"),
    (">", "&gt;"),
    ('"', "&quot;"),
    ("'", "&#x27;"),
)

# Attribute context deliberately leaves "<" and ">" alone. Inside a quoted value they are
# not delimiters, so escaping them only makes the markup noisier.
_ATTRIBUTE = (
    ("&", "&amp;"),
    ('"', "&quot;"),
    ("'", "&#x27;"),
)

_XML = (
    ("&", "&amp;"),
    ("<", "&lt;"),
    (">", "&gt;"),
    ('"', "&quot;"),
    ("'", "&apos;"),
)


def _replace(value: str, table: tuple[tuple[str, str], ...]) -> str:
    for char, entity in table:
        value = value.replace(char, entity)
    return value


def escape_text(text: str, *, escape_slashes: bool = False) -> str:
    """Escape text for an element body.

    ``escape_slashes`` is opt-in. WingedSwift escaped ``/`` unconditionally until 1.5.0,
    which turned every date and path in the output into ``&#x2F;`` soup; ``&``, ``<``,
    ``>``, ``"`` and ``'`` already close the XSS surface without it.
    """
    result = _replace(text, _TEXT)
    if escape_slashes:
        result = result.replace("/", "&#x2F;")
    return result


def escape_attribute(value: str) -> str:
    """Escape a value for use inside a double-quoted attribute."""
    return _replace(value, _ATTRIBUTE)


def escape_xml(text: str) -> str:
    """Escape text for XML output: the sitemap and the RSS feed.

    WingedSwift carries two private, identical copies of this; there is one here.
    """
    return _replace(text, _XML)
