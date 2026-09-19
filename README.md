# Winged-Python

[![CI](https://github.com/micheltlutz/Winged-Python/actions/workflows/ci.yml/badge.svg)](https://github.com/micheltlutz/Winged-Python/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/micheltlutz/Winged-Python/branch/main/graph/badge.svg)](https://codecov.io/gh/micheltlutz/Winged-Python)
[![PyPI](https://img.shields.io/pypi/v/winged-python.svg)](https://pypi.org/project/winged-python/)
[![Python](https://img.shields.io/pypi/pyversions/winged-python.svg)](https://pypi.org/project/winged-python/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Write HTML in Python. No templates, no template language, no runtime dependencies — just
functions that compose into a tree and render to a string.

```python
from winged import Body, Document, H1, Head, Li, P, Title, Ul, render

page = Document(
    Head(Title("Home")),
    Body(
        H1("Winged"),
        P("Hello ", "<world>"),
        Ul(*(Li(name) for name in ["one", "two"])),
    ),
    lang="pt-BR",
)

print(render(page))
```

```html
<!DOCTYPE html>
<html lang="pt-BR"><head><title>Home</title></head><body><h1>Winged</h1><p>Hello &lt;world&gt;</p><ul><li>one</li><li>two</li></ul></body></html>
```

Note `&lt;world&gt;`: **text is escaped by default.** That is the one thing a library
which builds HTML from data has to get right.

This is the Python sibling of [Winged-Swift](https://github.com/micheltlutz/Winged-Swift),
and 1.0.0 is at parity with Winged-Swift 2.0.0 — a parity that is
[tested](tests/test_golden.py) against Winged-Swift's own golden fixtures, not asserted.

## Contents

- [Install](#install)
- [Quick start](#quick-start)
- [The CLI](#the-cli)
- [Writing markup](#writing-markup)
- [Pages and layouts](#pages-and-layouts)
- [SEO, sitemap and RSS](#seo-sitemap-and-rss)
- [Static sites](#static-sites)
- [Accessibility](#accessibility)
- [Escaping](#escaping)
- [Documentation](#documentation)
- [Contributing](#contributing)

## Install

```bash
pip install winged-python
```

Python 3.10 or newer. No runtime dependencies.

## Quick start

```bash
winged new mysite && cd mysite
winged build          # writes dist/
winged serve --watch  # http://127.0.0.1:8000, rebuilding on change
```

## The CLI

| Command | What it does |
| --- | --- |
| `winged new <name>` | Scaffold a project: `site.py`, `layout.py`, assets, and its own `AGENTS.md` |
| `winged build` | Run the generator into `dist/` and report what was written |
| `winged serve [--watch] [--open]` | Preview on `127.0.0.1`, rebuilding on change |

`build` and `serve` find the project by walking up for `site.py`, so they work from any
subdirectory.

## Writing markup

Children are positional; attributes are keyword.

```python
from winged import A, Div, Img, Input, Label, P, Span, render

Div(P("Body"), cls="card")  # <div class="card"><p>Body</p></div>
A("Home", href="/")  # <a href="/">Home</a>
Img("/a.png", "A screenshot")  # alt is required, by signature
Input(type_="checkbox", checked=True)  # <input type="checkbox" checked>
Input(type_="text", disabled=False)  # the attribute is omitted
Label("E-mail", for_="email")  # for_ renders as for
Div(data_user_id="7", aria_label="Card")  # data-user-id, aria-label
```

Names that collide with a Python keyword or builtin take a trailing underscore — `cls`,
`for_`, `type_`, `id_`. The rendered attribute is always the HTML spelling.

Three shapes keep loops and conditionals readable:

```python
Ul(Li(x) for x in items)  # iterables are flattened
Div(banner if logged_in else None)  # None children are dropped
Div(*sections)  # so are lists
```

Helpers chain, and each returns the element:

```python
Div().add_class("card").add_class("wide").set_id("main").set_role("region")
```

### Pretty or compact

```python
from winged import RenderOptions, render

render(page)  # one line — what you ship
render(page, RenderOptions.pretty_())  # indented — what you read
render(page, RenderOptions(indent="\t", xhtml_self_closing=True))
```

Options are a value passed per call, never global state, so two callers can render
differently at the same time. `<pre>`, `<code>` and `<textarea>` stay compact even in
pretty mode, because indentation inside them changes what the browser displays.

### Fragments, raw markup and comments

```python
from winged import Comment, Fragment, RawHtml

Fragment(P("a"), P("b"))  # no wrapper element, indentation preserved
RawHtml("<p>a</p>")  # verbatim — never pass user input here
Comment("build 42")  # <!-- build 42 -->
```

## Pages and layouts

`Document` owns the doctype and `lang`, so a page cannot be assembled without them:

```python
Document(Head(Title("Home")), Body(H1("Hi")), lang="pt-BR")
```

A layout is any class with a `render` method — it satisfies `winged.Layout` structurally,
with no base class and no registration:

```python
from winged import Body, Footer, Header, Nav, P, render_many
from winged.core.render import Node


class SiteLayout:
    def render(self, content: Node) -> Node:
        return Body(Header(Nav(...)), content, Footer(P("© 2026")))
```

## SEO, sitemap and RSS

```python
from winged.seo import SeoBuilder
from winged.sitemap import SitemapGenerator, SitemapUrl
from winged.feed import RssGenerator, RssItem, rfc822

head = Head(
    SeoBuilder(
        title="RideKeeper",
        description="Motorcycle maintenance companion",
        image="https://example.com/og.jpg",
        url="https://example.com",
        keywords=["python", "html"],
        twitter_site="@micheltlutz",
    ).build(),
    Title("RideKeeper"),
)

SitemapGenerator("https://example.com").generate(
    [
        SitemapUrl("/", changefreq="weekly", priority=1.0),
    ]
)

RssGenerator(title="Blog", link="https://example.com", description="Notes").generate(
    [
        RssItem(
            title="Hello",
            link="https://example.com/1",
            description="First post",
            pub_date=rfc822(datetime.now(timezone.utc)),
        ),
    ]
)
```

Open Graph keys go on `property`, Twitter keys on `name` — a distinction the spec makes
and that is easy to get wrong. `pub_date` is RFC 822, which is *not* the ISO 8601 a
sitemap's `lastmod` uses, which is why `rfc822()` exists.

## Static sites

```python
from winged.ssg import StaticSiteGenerator

site = StaticSiteGenerator("dist")
site.clean()
site.generate(page, "index.html")
site.generate_multiple({"about.html": about, "blog/1.html": post})
site.copy_asset("assets/css/style.css", "css/style.css")
```

Intermediate directories are created for you. `clean()` refuses the filesystem root, your
home directory, and anything reached through a symlink out of the output directory.

## Accessibility

```python
from winged.accessibility import audit

for issue in audit(page):
    print(f"{issue.rule}: {issue.message} at {issue.path}")
```

Eight rules: `img-alt`, `button-label`, `iframe-title`, `link-text`, `heading-order`,
`html-lang`, `form-label`, `duplicate-id`. `audit` returns findings and never raises —
whether a finding should fail your build is your decision. Two of the rules are already
unreachable through the normal constructors, because `Img` requires `alt` and `Iframe`
requires `title`.

## Escaping

| What | Escaped? |
| --- | --- |
| A `str` child | ✅ |
| Attribute values | ✅ — at construction, so never twice |
| `add_class`, `set_id`, `set_style`, `attr`, `data_attr`, `aria_attr` | ✅ |
| Sitemap and RSS values | ✅ |
| `RawHtml(...)` | ❌ — that is what it is for |
| `Element.text(x, escape=False)` | ❌ |

URL *schemes* are not inspected: a `javascript:` URL in `href` is escaped but not
rejected. Validate URLs that come from data. See [SECURITY.md](SECURITY.md).

## Documentation

| Document | What is in it |
| --- | --- |
| [GETTING_STARTED.md](GETTING_STARTED.md) | Four ways in, then deployment |
| [docs/tag-catalog.md](docs/tag-catalog.md) | All 93 elements — generated from the source |
| [docs/recipes.md](docs/recipes.md) | Task-shaped examples |
| [docs/pitfalls.md](docs/pitfalls.md) | The mistakes, and why they happen |
| [MIGRATION.md](MIGRATION.md) | 0.1.0 → 1.0.0, name by name |
| [PORTING.md](PORTING.md) | Winged-Swift → Winged-Python, and the deliberate differences |
| [ROADMAP.md](ROADMAP.md) | What is missing, stated as problems |
| [AGENTS.md](AGENTS.md) | Working on this repository, including with a coding agent |

## Contributing

```bash
git clone https://github.com/micheltlutz/Winged-Python.git
cd Winged-Python
python -m venv .venv && source .venv/bin/activate
pip install -e . pytest pytest-cov ruff mypy build

./scripts/verify.sh      # build, test, lint, types, generated files, parity, end-to-end
```

`verify.sh` is a superset of CI. Run it before opening a pull request — and if you are a
coding agent, run it before reporting that you are done. See
[CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md).

## License

MIT. See [LICENSE](LICENSE).
