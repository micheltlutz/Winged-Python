"""Winged-Python — a dependency-free DSL for writing HTML in Python.

    from winged import Document, Head, Title, Body, H1, P, render

    page = Document(Head(Title("Home")), Body(H1("Winged"), P("Hello")), lang="pt-BR")
    print(render(page))

0.1.0 shipped this file as two lines that mutated ``sys.path`` at import time, and shipped
``winged/HTML/__init__.py`` entirely commented out -- so there was no public API and every
user imported ``from winged.HTML.div import Div``. This module is that fix.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

from .core.attribute import Attribute
from .core.element import Element
from .core.escape import escape_attribute, escape_text, escape_xml
from .core.node import Comment, Fragment, RawHtml, Text
from .core.render import Node, RenderOptions, render
from .core.tags import VOID_ELEMENTS, WHITESPACE_SENSITIVE
from .document import Document
from .elements import *  # noqa: F403
from .elements import __all__ as _ELEMENT_NAMES
from .layout import Layout, render_many

try:
    __version__ = version("winged-python")
except PackageNotFoundError:  # running from a source checkout that was never installed
    __version__ = "0.0.0.dev0"

__all__ = [
    "Attribute",
    "Comment",
    "Document",
    "Element",
    "Fragment",
    "Layout",
    "Node",
    "RawHtml",
    "RenderOptions",
    "Text",
    "VOID_ELEMENTS",
    "WHITESPACE_SENSITIVE",
    "__version__",
    "escape_attribute",
    "escape_text",
    "escape_xml",
    "render",
    "render_many",
    *_ELEMENT_NAMES,
]
