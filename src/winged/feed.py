"""RSS 2.0 feed generation.

Ports ``Winged-Swift/Sources/WingedSwift/feed/RSSGenerator.swift``.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field
from datetime import datetime, timezone
from email.utils import format_datetime

from .core.escape import escape_xml

__all__ = ["RssGenerator", "RssItem", "rfc822"]


def rfc822(moment: datetime) -> str:
    """Format a datetime for ``<pubDate>``.

    RSS wants RFC 822, which is *not* the ISO 8601 that a sitemap's ``lastmod`` uses --
    a difference worth a helper rather than leaving callers to hand-build the string.
    A naive datetime is assumed to be UTC.
    """
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=timezone.utc)
    return format_datetime(moment)


@dataclass(frozen=True, slots=True)
class RssItem:
    """One ``<item>``."""

    title: str
    link: str
    description: str
    pub_date: str | None = None
    guid: str | None = None
    author: str | None = None
    categories: Sequence[str] = field(default_factory=tuple)


class RssGenerator:
    """Renders a list of :class:`RssItem` as an RSS 2.0 document."""

    __slots__ = ("description", "language", "link", "self_url", "title", "webmaster")

    def __init__(
        self,
        *,
        title: str,
        link: str,
        description: str,
        language: str = "en",
        self_url: str | None = None,
        webmaster: str | None = None,
    ) -> None:
        self.title = title
        self.link = link
        self.description = description
        self.language = language
        self.self_url = self_url
        self.webmaster = webmaster

    def generate(self, items: Sequence[RssItem]) -> str:
        out = [
            '<?xml version="1.0" encoding="UTF-8"?>\n',
            '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n',
            "  <channel>\n",
            f"    <title>{escape_xml(self.title)}</title>\n",
            f"    <link>{escape_xml(self.link)}</link>\n",
            f"    <description>{escape_xml(self.description)}</description>\n",
        ]
        if self.self_url is not None:
            out.append(
                f'    <atom:link href="{escape_xml(self.self_url)}" rel="self"'
                ' type="application/rss+xml" />\n'
            )
        out.append(f"    <language>{escape_xml(self.language)}</language>\n")
        if self.webmaster is not None:
            out.append(f"    <webMaster>{escape_xml(self.webmaster)}</webMaster>\n")

        for item in items:
            out.append("    <item>\n")
            out.append(f"      <title>{escape_xml(item.title)}</title>\n")
            out.append(f"      <link>{escape_xml(item.link)}</link>\n")
            out.append(f"      <description>{escape_xml(item.description)}</description>\n")
            if item.pub_date is not None:
                out.append(f"      <pubDate>{escape_xml(item.pub_date)}</pubDate>\n")
            # guid defaults to the link, as a permalink -- WingedSwift does the same.
            guid = item.guid if item.guid is not None else item.link
            out.append(f'      <guid isPermaLink="true">{escape_xml(guid)}</guid>\n')
            if item.author is not None:
                out.append(f"      <author>{escape_xml(item.author)}</author>\n")
            for category in item.categories:
                out.append(f"      <category>{escape_xml(category)}</category>\n")
            out.append("    </item>\n")

        out.append("  </channel>\n")
        out.append("</rss>")
        return "".join(out)
