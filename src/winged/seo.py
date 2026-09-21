"""SEO meta tags: Open Graph, Twitter Cards and the common head set.

Ports ``Winged-Swift/Sources/WingedSwift/seo/SEOHelpers.swift``.

Every helper returns a :class:`~winged.core.node.Fragment`, so the result drops straight
into a ``Head(...)`` with no wrapper element and keeps pretty-print indentation.

Tag *order* is part of the contract here, not an implementation detail: the golden
fixtures in ``tests/fixtures`` are compared byte for byte, so these emit in exactly the
order WingedSwift does.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .core.attribute import Attribute
from .core.element import Element
from .core.node import Fragment

__all__ = [
    "SeoBuilder",
    "common",
    "open_graph",
    "open_graph_article",
    "twitter_card",
]


def _meta(key: str, name: str, content: str) -> Element:
    """One ``<meta>``.

    ``key`` is ``name`` or ``property``: Open Graph keys go on ``property``, Twitter keys
    on ``name``. The spec makes that distinction and it is easy to get wrong.

    The key itself is inserted raw, matching WingedSwift's ``Meta``; the *content* is
    escaped like any other attribute value.
    """
    element = Element("meta")
    element.add_attribute(Attribute.raw(key, name))
    element.add_attribute(Attribute("content", content))
    return element


def common(
    *,
    title: str,
    description: str,
    keywords: Sequence[str] = (),
    author: str | None = None,
    viewport: str = "width=device-width, initial-scale=1.0",
    robots: str = "index, follow",
    charset: str = "UTF-8",
) -> Fragment:
    """Charset, viewport, description, robots, and optionally keywords and author.

    Deliberately does **not** emit ``<title>``, matching WingedSwift: a page places its
    title where it wants it, and a meta helper that injects an element into the middle of
    the head makes ordering surprising. ``title`` is taken because
    :class:`SeoBuilder` passes it through to the Open Graph and Twitter sets.
    """
    tags: list[Element] = [
        Element("meta", charset=charset),
        _meta("name", "viewport", viewport),
        _meta("name", "description", description),
        _meta("name", "robots", robots),
    ]
    if keywords:
        tags.append(_meta("name", "keywords", ", ".join(keywords)))
    if author is not None:
        tags.append(_meta("name", "author", author))
    return Fragment(*tags)


def open_graph(
    *,
    title: str,
    description: str,
    image: str,
    url: str,
    type_: str = "website",
    site_name: str | None = None,
    locale: str | None = None,
) -> Fragment:
    """The Open Graph set. Keys go on ``property``."""
    tags = [
        _meta("property", "og:title", title),
        _meta("property", "og:description", description),
        _meta("property", "og:image", image),
        _meta("property", "og:url", url),
        _meta("property", "og:type", type_),
    ]
    if site_name is not None:
        tags.append(_meta("property", "og:site_name", site_name))
    if locale is not None:
        tags.append(_meta("property", "og:locale", locale))
    return Fragment(*tags)


def open_graph_article(
    *,
    published_time: str | None = None,
    modified_time: str | None = None,
    author: str | None = None,
    section: str | None = None,
    tags: Sequence[str] = (),
) -> Fragment:
    """The ``article:`` Open Graph extension. One ``article:tag`` per entry, in order."""
    out: list[Element] = []
    if published_time is not None:
        out.append(_meta("property", "article:published_time", published_time))
    if modified_time is not None:
        out.append(_meta("property", "article:modified_time", modified_time))
    if author is not None:
        out.append(_meta("property", "article:author", author))
    if section is not None:
        out.append(_meta("property", "article:section", section))
    out.extend(_meta("property", "article:tag", tag) for tag in tags)
    return Fragment(*out)


def twitter_card(
    *,
    title: str,
    description: str,
    image: str,
    card: str = "summary_large_image",
    site: str | None = None,
    creator: str | None = None,
) -> Fragment:
    """The Twitter Card set. Keys go on ``name``, not ``property``."""
    tags = [
        _meta("name", "twitter:card", card),
        _meta("name", "twitter:title", title),
        _meta("name", "twitter:description", description),
        _meta("name", "twitter:image", image),
    ]
    if site is not None:
        tags.append(_meta("name", "twitter:site", site))
    if creator is not None:
        tags.append(_meta("name", "twitter:creator", creator))
    return Fragment(*tags)


@dataclass(slots=True)
class SeoBuilder:
    """The whole head set in one place.

    Covers WingedSwift's ``SEO.complete(...)``, whose argument list is long enough that
    keyword-by-keyword construction reads better than one call.
    """

    title: str
    description: str
    image: str
    url: str
    keywords: Sequence[str] = field(default_factory=tuple)
    author: str | None = None
    twitter_site: str | None = None
    twitter_creator: str | None = None
    site_name: str | None = None
    locale: str | None = None

    def build(self) -> Fragment:
        """Common + Open Graph + Twitter, in that order."""
        return Fragment(
            common(
                title=self.title,
                description=self.description,
                keywords=self.keywords,
                author=self.author,
            ),
            open_graph(
                title=self.title,
                description=self.description,
                image=self.image,
                url=self.url,
                site_name=self.site_name,
                locale=self.locale,
            ),
            twitter_card(
                title=self.title,
                description=self.description,
                image=self.image,
                site=self.twitter_site,
                creator=self.twitter_creator,
            ),
        )
