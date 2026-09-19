"""The :class:`Element` type — the tree itself.

Ports ``Winged-Swift/Sources/WingedSwift/core/HTMLTag.swift``, plus ``CSSHelpers.swift``
and ``AttributeHelpers.swift``.

Replaces 0.1.0's ``tag.py``, ``generic_element.py`` and ``element_abstract.py``. Three
defects in that code shaped this one: ``ElementAbstract`` declared ``@abstractmethod``
without inheriting ``ABC``, so it enforced nothing; a non-container tag silently discarded
any child added to it; and ``Tag`` held its state in *class* attributes, so it leaked
between instances.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING

from .attribute import Attribute
from .escape import escape_attribute
from .node import Child, Fragment, coerce, flatten
from .render import Node, RenderOptions
from .tags import VOID_ELEMENTS, WHITESPACE_SENSITIVE

if TYPE_CHECKING:
    from typing import Self

__all__ = ["AttrValue", "Element"]

AttrValue = str | bool | int | None

# Keyword names that collide with a Python keyword or builtin. The rendered attribute is
# always the HTML spelling; only the Python argument changes.
_KEYWORD_MAP = {"cls": "class", "class_": "class", "for_": "for", "type_": "type", "id_": "id"}


def attr_name(key: str) -> str:
    """Map a Python keyword argument to its HTML attribute name."""
    if key in _KEYWORD_MAP:
        return _KEYWORD_MAP[key]
    # data_user_id -> data-user-id, aria_label -> aria-label
    if key.startswith(("data_", "aria_")):
        return key.replace("_", "-")
    # A trailing underscore is the general escape from a keyword collision.
    return key.rstrip("_") if key.endswith("_") else key


class Element:
    """An HTML element.

    The tree has reference semantics, as WingedSwift's does: placing one element in two
    parents shares the node rather than copying it.
    """

    __slots__ = ("_attributes", "_children", "_name")

    def __init__(self, name: str, /, *children: Child, **attrs: AttrValue) -> None:
        # `name` is positional-only: <input name="email"> is ordinary HTML, and without
        # the `/` the tag name and the `name` attribute collide in **attrs.
        self._name = name
        self._attributes: list[Attribute] = []
        self._children: list[Node] = []
        for key, value in attrs.items():
            self._set(attr_name(key), value)
        for child in flatten(children):
            self.child(child)  # type: ignore[arg-type]

    # -- construction -----------------------------------------------------------------

    def _set(self, key: str, value: AttrValue) -> None:
        if value is None or value is False:
            return
        if value is True:
            self._attributes.append(Attribute.boolean(key))
            return
        self._attributes.append(Attribute(key, str(value)))

    @property
    def name(self) -> str:
        return self._name

    def add_attribute(self, attribute: Attribute) -> Self:
        self._attributes.append(attribute)
        return self

    def child(self, node: Child) -> Self:
        """Append a child.

        A void element refuses one. 0.1.0 accepted it and dropped it silently, which is
        worse than either rendering it or refusing it.
        """
        if node is None:
            return self
        if self._name in VOID_ELEMENTS:
            raise ValueError(f"<{self._name}> is a void element and cannot have children")
        self._children.append(coerce(node))
        return self

    def text(self, content: str, *, escape: bool = True) -> Self:
        from .node import RawHtml, Text

        return self.child(Text(content) if escape else RawHtml(content))

    # -- chainable helpers ------------------------------------------------------------

    def _existing(self, key: str) -> str | None:
        for attribute in self._attributes:
            if attribute.key == key:
                return attribute.value
        return None

    def _replace(self, key: str, value: str) -> None:
        """Set an already-escaped value, replacing any existing attribute of that name."""
        self._attributes = [a for a in self._attributes if a.key != key]
        self._attributes.append(Attribute.raw(key, value))

    def add_class(self, name: str) -> Self:
        """Append a CSS class, keeping any already set.

        The value is escaped once, here — not again on the next call. WingedSwift 1.5.0
        fixed an injection in this method and had to avoid double-escaping ``&`` while
        doing it.
        """
        current = self._existing("class")
        escaped = escape_attribute(name)
        self._replace("class", f"{current} {escaped}" if current else escaped)
        return self

    def add_classes(self, *names: str) -> Self:
        for name in names:
            self.add_class(name)
        return self

    def set_id(self, value: str) -> Self:
        self._replace("id", escape_attribute(value))
        return self

    def set_style(self, value: str) -> Self:
        self._replace("style", escape_attribute(value))
        return self

    def set_role(self, value: str) -> Self:
        self._replace("role", escape_attribute(value))
        return self

    def attr(self, key: str, value: str) -> Self:
        self._replace(key, escape_attribute(value))
        return self

    def data_attr(self, key: str, value: str) -> Self:
        return self.attr(f"data-{key}", value)

    def data_attrs(self, mapping: Mapping[str, str]) -> Self:
        # Insertion order, deterministically. WingedSwift takes a Dictionary here, so its
        # output order varies between runs, which makes golden files impossible.
        for key, value in mapping.items():
            self.data_attr(key, value)
        return self

    def aria_attr(self, key: str, value: str) -> Self:
        return self.attr(f"aria-{key}", value)

    def aria_attrs(self, mapping: Mapping[str, str]) -> Self:
        for key, value in mapping.items():
            self.aria_attr(key, value)
        return self

    # -- rendering --------------------------------------------------------------------

    def write_into(self, buf: list[str], options: RenderOptions, depth: int) -> None:
        buf.append(f"<{self._name}")
        for attribute in self._attributes:
            buf.append(attribute.render())

        if self._name in VOID_ELEMENTS:
            buf.append(" />" if options.xhtml_self_closing else ">")
            return

        buf.append(">")

        # Two reasons to drop out of pretty mode for this subtree:
        #
        # 1. A whitespace-sensitive element displays its content as written, so injected
        #    indentation changes what the reader sees.
        # 2. An element whose children are all text renders on one line -- WingedSwift
        #    keeps text in a `content` string that it emits inline, and the golden
        #    fixtures depend on `<a href="/">Home</a>` staying a single line.
        blocks = (Element, Fragment)
        inline = not self._children or all(not isinstance(c, blocks) for c in self._children)
        pretty = options.pretty and self._name not in WHITESPACE_SENSITIVE and not inline
        inner = (
            options
            if pretty
            else RenderOptions(indent=options.indent, xhtml_self_closing=options.xhtml_self_closing)
        )

        for child in self._children:
            if pretty:
                buf.append("\n")
                buf.append(options.indent * (depth + 1))
            child.write_into(buf, inner, depth + 1)

        if pretty and self._children:
            buf.append("\n")
            buf.append(options.indent * depth)
        buf.append(f"</{self._name}>")
