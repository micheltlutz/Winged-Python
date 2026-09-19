"""Sitemap 0.9 generation.

Ports ``Winged-Swift/Sources/WingedSwift/seo/SitemapGenerator.swift``.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from urllib.parse import urljoin

from .core.escape import escape_xml

__all__ = ["CHANGE_FREQUENCIES", "SitemapGenerator", "SitemapUrl"]

#: The enumeration the sitemap protocol defines. Anything else is a typo.
CHANGE_FREQUENCIES = frozenset(
    {"always", "hourly", "daily", "weekly", "monthly", "yearly", "never"}
)


@dataclass(frozen=True, slots=True)
class SitemapUrl:
    """One ``<url>`` entry. An unset optional emits no element at all."""

    loc: str
    lastmod: str | None = None
    changefreq: str | None = None
    priority: float | None = None

    def __post_init__(self) -> None:
        if self.changefreq is not None and self.changefreq not in CHANGE_FREQUENCIES:
            raise ValueError(
                f"changefreq must be one of {sorted(CHANGE_FREQUENCIES)}, got {self.changefreq!r}"
            )
        if self.priority is not None and not 0.0 <= self.priority <= 1.0:
            raise ValueError(f"priority must be between 0.0 and 1.0, got {self.priority}")


class SitemapGenerator:
    """Renders a list of :class:`SitemapUrl` as a sitemap document."""

    __slots__ = ("base_url",)

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def generate(self, urls: Sequence[SitemapUrl]) -> str:
        out = [
            '<?xml version="1.0" encoding="UTF-8"?>\n',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n',
        ]
        for url in urls:
            loc = urljoin(self.base_url, url.loc)
            out.append("  <url>\n")
            out.append(f"    <loc>{escape_xml(loc)}</loc>\n")
            if url.lastmod is not None:
                out.append(f"    <lastmod>{escape_xml(url.lastmod)}</lastmod>\n")
            if url.changefreq is not None:
                out.append(f"    <changefreq>{url.changefreq}</changefreq>\n")
            if url.priority is not None:
                # One decimal place, matching WingedSwift: the golden fixture is compared
                # byte for byte, and "1.0" is not "1".
                out.append(f"    <priority>{url.priority:.1f}</priority>\n")
            out.append("  </url>\n")
        out.append("</urlset>")
        return "".join(out)
