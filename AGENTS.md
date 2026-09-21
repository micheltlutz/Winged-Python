# AGENTS.md — working with Winged-Python

Instructions for anyone changing this repository, human or coding agent.

## What Winged-Python is

A dependency-free DSL that builds an HTML **string**. No DOM, no browser, no server. You
compose elements into a tree and render it to text.

Three things follow from that, and most mistakes come from forgetting one of them:

1. **The output is a string**, so tests assert on rendered strings — never on tree shape.
2. **Escaping is the whole security surface.** Text and attribute values are escaped by
   default; `RawHtml` is the only opt-out and must never receive user input.
3. **The tree has reference semantics.** Putting one element in two parents shares the
   node; it is not copied.

```python
from winged import Body, Document, H1, Head, P, Title, render

page = Document(Head(Title("Home")), Body(H1("Hi"), P("<ok>")), lang="pt-BR")
render(page)
# <!DOCTYPE html>
# <html lang="pt-BR"><head><title>Home</title></head><body><h1>Hi</h1><p>&lt;ok&gt;</p></body></html>
```

## Commands

| Task | Command |
| --- | --- |
| Everything, before you say you are done | `./scripts/verify.sh` |
| Tests | `pytest` |
| One test file | `pytest tests/test_element.py -q` |
| Lint and format | `ruff check . && ruff format .` |
| Types | `mypy` |
| Regenerate the elements | `python scripts/generate_elements.py` |
| Regenerate the tag catalogue | `python scripts/generate_tag_catalog.py` |
| Regenerate the golden fixtures | `WINGED_UPDATE_FIXTURES=1 pytest tests/test_golden.py` |

## Repository map

```
src/winged/
  core/
    escape.py      escape_text / escape_attribute / escape_xml — the security surface
    attribute.py   Attribute, and the boolean-attribute set
    element.py     Element: the tree, the chainable helpers, the pretty printer
    node.py        Text, RawHtml, Fragment, Comment, and child coercion
    render.py      RenderOptions, the Node protocol, render()
    tags.py        VOID_ELEMENTS and WHITESPACE_SENSITIVE
  _tagtable.py     the one declarative table every element is generated from
  elements.py      GENERATED — do not edit
  _special.py      Img and Iframe, whose signatures require an argument
  document.py      Document: doctype and <html lang>
  layout.py        the Layout protocol
  seo.py           Open Graph, Twitter Cards, SeoBuilder
  sitemap.py       sitemap 0.9
  feed.py          RSS 2.0
  ssg.py           StaticSiteGenerator
  accessibility.py the audit
  cli.py           winged new / build / serve
  templates/       what `winged new` scaffolds
scripts/           the two generators, the Markdown link check, and verify.sh
tests/fixtures/    Winged-Swift's golden files, copied
docs/              tag-catalog.md is generated; recipes and pitfalls are not
```

## Rules

1. **Prefer the varargs form.** `Div(P("a"), cls="x")`, not `Div().child(P("a"))`. The
   chainable helpers are for the cases where the value is computed.
2. **Never invent an element name.** Check `docs/tag-catalog.md`. If it is not there, add
   a row to `_tagtable.py` and regenerate — see the contract below.
3. **Content and attributes are escaped for you.** Never pre-escape; you will get
   `&amp;lt;`.
4. **`RawHtml` is the only way in for markup**, and never for anything from data.
5. **Void elements take no children.** `Br`, `Img`, `Input`, `Link`, `Meta`, `Hr`, `Col`,
   `Source`, `Track`, `Wbr`, `Base`, `Embed`. Passing one a child raises.
6. **`Fragment` groups, `RawHtml` injects.** `Fragment` keeps the tree and its
   indentation; `RawHtml` flattens to a string and loses both.
7. **Boolean attributes are `True`**, not `"true"`. `False` and `None` omit the attribute.
8. **`Document` owns the doctype.** Never write `<!DOCTYPE html>` by hand.
9. **Rendering is configured by value.** Pass `RenderOptions`; never add a global.
10. **Names that collide take a trailing underscore** — `cls`, `for_`, `type_`, `id_`.
    The rendered attribute keeps the HTML spelling.
11. **`Img` requires `alt` and `Iframe` requires `title`.** That is deliberate; do not
    add defaults.

## Recipes

### A full page written to disk

```python
from winged import Body, Document, H1, Head, Link, Main, Title
from winged.seo import SeoBuilder
from winged.ssg import StaticSiteGenerator

head = Head(
    SeoBuilder(title="Home", description="…", image="…", url="…").build(),
    Title("Home"),
    Link(href="/css/style.css", rel="stylesheet"),
)
page = Document(head, Body(Main(H1("Home"))), lang="pt-BR")

site = StaticSiteGenerator("dist")
site.clean()
site.generate(page, "index.html")
```

### A reusable component

A component is a function returning a node. There is no base class to inherit.

```python
from winged import A, Div, H3, P
from winged.core.render import Node


def card(title: str, body: str, href: str) -> Node:
    return Div(H3(title), P(body), A("Read more", href=href), cls="card")
```

## Adding an element to the library

1. Add a row to `src/winged/_tagtable.py`: `("Name", "tag", "Group")`.
2. If it is void, add the tag to `VOID_ELEMENTS` in `src/winged/core/tags.py`. If its
   content is whitespace-sensitive, add it to `WHITESPACE_SENSITIVE`.
3. Run `python scripts/generate_elements.py` and
   `python scripts/generate_tag_catalog.py`. Commit both generated files.
4. `tests/test_tag_catalog.py` picks the element up automatically — confirm it passes.
5. Add a `CHANGELOG.md` entry under `## [Unreleased]`.

An element whose signature must require an argument (like `Img`) goes in `_special.py`
instead, and gets a row in the generator's `names` list.

## Conventions

- Four-space indent, 100-column lines, `ruff format`.
- A docstring on every public module, class and function.
- Comments explain **why**, not what. If a line encodes a decision, say what the
  alternative was and why it lost.
- Tests are pytest: plain functions, `parametrize`, `capsys`. No `unittest.TestCase`.
- Assert on rendered strings, never on private attributes.
- Commit messages: `Add:`, `Fix:`, `Change:`, `Docs:`.
- English, in code and comments — the Swift sibling is in English too.

## Before you say you are done

```bash
./scripts/verify.sh
```

It builds, tests, lints, type-checks, verifies both generated files are current and that
`.claude/skills/winged/references/` is still symlinked into `docs/`, resolves every
relative link in the Markdown, checks byte-for-byte parity against Winged-Swift's fixtures, installs the
package into a throwaway venv and renders a page with it, then runs `winged new` and
`winged build` **from `/`** — because a generator that resolves paths from the current
directory passes every unit test and still fails for the user.
