# Recipes

Task-shaped examples. For the full element list see
[tag-catalog.md](tag-catalog.md); for the mistakes see [pitfalls.md](pitfalls.md).

## A new project

```bash
winged new mysite && cd mysite && winged build
```

## A page

```python
from winged import Body, Document, H1, Head, Main, P, Title, render

page = Document(Head(Title("Home")), Body(Main(H1("Home"), P("Hello"))), lang="pt-BR")
print(render(page))
```

## A layout

Any class with `render` satisfies `winged.Layout` — no base class, no registration.

```python
from winged import A, Body, Footer, Header, Li, Nav, P, Ul
from winged.core.render import Node


class SiteLayout:
    def __init__(self, title: str) -> None:
        self.title = title

    def render(self, content: Node) -> Node:
        return Body(
            Header(Nav(A(self.title, href="/", cls="logo"), Ul(Li(A("Home", href="/"))))),
            content,
            Footer(P(f"© 2026 {self.title}")),
        )
```

## A reusable component

A component is a function returning a node.

```python
from winged import A, Div, H3, P
from winged.core.render import Node


def card(title: str, body: str, href: str) -> Node:
    return Div(H3(title), P(body), A("Read more", href=href), cls="card")
```

Returning several nodes? Return a `Fragment`.

## Loops and conditionals

```python
Ul(Li(item.name) for item in items)  # iterables are flattened
Div(banner if logged_in else None)  # None is dropped
Div(*sections)  # so are lists
```

## A table

```python
Table(
    Caption("Plans"),
    Thead(Tr(Th("Plan"), Th("Price"))),
    Tbody(*(Tr(Td(name), Td(price)) for name, price in plans)),
)
```

## A form

```python
Form(
    Fieldset(
        Legend("Newsletter"),
        Label("E-mail", for_="email"),
        Input(type_="email", name="email", id_="email", required=True),
        Button("Subscribe", type_="submit"),
    ),
    action="/subscribe",
    method="post",
)
```

`id_` on the input and `for_` on the label are what make the `form-label` accessibility
rule pass.

## Media

```python
Figure(Img("/img/app.png", "The garage screen"), Figcaption("The garage screen"))
Video(Source(src="/v.mp4", type_="video/mp4"), controls=True, width="640")
Iframe("https://maps.example/embed", "Map of the workshop")
```

`Img` requires `alt` and `Iframe` requires `title`, by signature.

## A code block

```python
Pre(Code("from winged import Div\n\nprint(Div())"))
```

`<pre>` and `<code>` stay compact even in pretty mode.

## Raw markup

```python
Div(RawHtml(markdown_to_html(post.body)), cls="prose")
```

Only for markup you produced. Never for user input.

## An SEO head

```python
from winged.seo import SeoBuilder

Head(
    SeoBuilder(
        title="RideKeeper",
        description="Motorcycle maintenance companion",
        image="https://example.com/og.jpg",
        url="https://example.com",
        keywords=["python", "html"],
        author="Michel Lutz",
        twitter_site="@micheltlutz",
    ).build(),
    Title("RideKeeper — track every service"),
    Link(href="/css/style.css", rel="stylesheet"),
)
```

`SeoBuilder` does not emit `<title>`; place it yourself, where you want it.

## A sitemap and an RSS feed

```python
from datetime import datetime, timezone
from winged.feed import RssGenerator, RssItem, rfc822
from winged.sitemap import SitemapGenerator, SitemapUrl

SitemapGenerator("https://example.com").generate(
    [
        SitemapUrl("/", changefreq="weekly", priority=1.0),
        SitemapUrl("/blog/1", lastmod="2026-09-18", priority=0.7),
    ]
)

RssGenerator(
    title="Blog",
    link="https://example.com",
    description="Notes",
    self_url="https://example.com/feed.xml",
).generate(
    [
        RssItem(
            title="Hello",
            link="https://example.com/blog/1",
            description="First post",
            pub_date=rfc822(datetime.now(timezone.utc)),
            categories=["release"],
        ),
    ]
)
```

`lastmod` is ISO 8601; `pub_date` is RFC 822. They are different formats, which is what
`rfc822()` is for.

## Writing to disk

```python
from winged.ssg import StaticSiteGenerator

site = StaticSiteGenerator("dist")
site.clean()
site.generate(home, "index.html")
site.generate_multiple({f"blog/{p.slug}.html": render_post(p) for p in posts})
site.copy_asset("assets/css/style.css", "css/style.css")
site.write_file(sitemap_xml, "sitemap.xml")
```

## Render options

```python
render(page)  # compact — ship this
render(page, RenderOptions.pretty_())  # indented — read this
render(page, RenderOptions(indent="\t"))
render(page, RenderOptions(xhtml_self_closing=True))  # <img … />
```

## Checking accessibility

```python
from winged.accessibility import audit

issues = audit(page)
if issues:
    for issue in issues:
        print(f"{issue.rule}: {issue.message} at {issue.path}")
    raise SystemExit(1)  # your call, not the library's
```
