"""An accessibility audit over a rendered tree.

This is the check ``Winged-Swift/ROADMAP.md`` asks for under "Quality" and that
WingedSwift has not shipped:

    a debug-only check for images without `alt`, buttons without a label, iframes
    without a title -- the rules `Iframe` already enforces by construction.

Some of it the signatures already guarantee: :class:`~winged.Img` requires ``alt`` and
:class:`~winged.Iframe` requires ``title``. Both are still reachable through
``Element("img")`` or ``.attr()``, and the remaining rules need a tree walk.

:func:`audit` **returns** findings and never raises: whether a finding is fatal is the
caller's decision, not this module's. It is opt-in, and never runs inside ``render``.
"""

from __future__ import annotations

from dataclasses import dataclass

from .core.element import Element
from .core.node import Fragment, Text
from .document import Document

__all__ = ["A11yIssue", "audit"]


@dataclass(frozen=True, slots=True)
class A11yIssue:
    """One finding. ``path`` locates the node well enough to fix it without a debugger."""

    rule: str
    message: str
    path: str


def _attr(element: Element, key: str) -> str | None:
    for attribute in element._attributes:
        if attribute.key == key:
            return attribute.value if attribute.value is not None else ""
    return None


def _has_text(element: Element) -> bool:
    for child in element._children:
        if isinstance(child, Text) and child.content.strip():
            return True
        if isinstance(child, Element) and _has_text(child):
            return True
    return False


def audit(node: object) -> list[A11yIssue]:
    """Walk a tree and report accessibility problems. Never mutates, never raises."""
    issues: list[A11yIssue] = []
    seen_ids: dict[str, int] = {}
    labelled: set[str] = set()
    heading_level = 0

    def visit(current: object, path: str) -> None:
        nonlocal heading_level

        if isinstance(current, Document):
            if not current.lang.strip():
                issues.append(A11yIssue("html-lang", "<html> has an empty lang", "html"))
            # "html" is the parent path; each child appends its own name.
            visit(current.head, "html")
            visit(current.body, "html")
            return

        if isinstance(current, Fragment):
            for index, child in enumerate(current.children):
                visit(child, f"{path}[{index}]")
            return

        if not isinstance(current, Element):
            return

        name = current.name
        here = f"{path} > {name}" if path else name

        element_id = _attr(current, "id")
        if element_id is not None:
            seen_ids[element_id] = seen_ids.get(element_id, 0) + 1

        if name == "label":
            target = _attr(current, "for")
            if target:
                labelled.add(target)

        if name == "img" and _attr(current, "alt") is None:
            issues.append(A11yIssue("img-alt", "<img> has no alt attribute", here))

        if name == "iframe" and not (_attr(current, "title") or "").strip():
            issues.append(A11yIssue("iframe-title", "<iframe> has no title", here))

        if name == "button" and not (
            _has_text(current) or _attr(current, "aria-label") or _attr(current, "aria-labelledby")
        ):
            issues.append(A11yIssue("button-label", "<button> has no text and no aria-label", here))

        if name == "a" and not _has_text(current):
            images = [c for c in current._children if isinstance(c, Element) and c.name == "img"]
            if images and all(not (_attr(i, "alt") or "").strip() for i in images):
                issues.append(
                    A11yIssue("link-text", "<a> has no text and its image alt is empty", here)
                )

        if len(name) == 2 and name[0] == "h" and name[1].isdigit():
            level = int(name[1])
            if heading_level and level > heading_level + 1:
                issues.append(
                    A11yIssue(
                        "heading-order",
                        f"<{name}> follows <h{heading_level}>, skipping a level",
                        here,
                    )
                )
            heading_level = level

        if name == "input" and (_attr(current, "type") or "") != "hidden":
            input_id = _attr(current, "id")
            if not _attr(current, "aria-label") and (input_id is None or input_id not in labelled):
                issues.append(A11yIssue("form-label", "<input> has no associated label", here))

        for index, child in enumerate(current._children):
            visit(child, f"{here}[{index}]" if index else here)

    visit(node, "")

    issues.extend(
        A11yIssue("duplicate-id", f"id {value!r} is used {count} times", "document")
        for value, count in seen_ids.items()
        if count > 1
    )
    return issues
