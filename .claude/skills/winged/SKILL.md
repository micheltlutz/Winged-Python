---
name: winged
description: Write or extend Winged-Python, a dependency-free Python DSL that builds HTML strings. Use when working with winged, Winged-Python, `from winged import`, Element/Document/Fragment/RawHtml/RenderOptions, the `winged` CLI (new/build/serve), or any task that generates HTML, a static site, a sitemap, or an RSS feed with this library.
---

# Winged-Python

A DSL that builds an HTML **string**. No DOM, no browser, no server, no runtime
dependencies.

## Which workflow are you in?

**A. Using the library** — building pages, a site, a feed. Read the rules below, then
`references/recipes.md` for the shape you need.

**B. Extending the library** — changing `src/winged/`. Read `AGENTS.md` at the repository
root; it has the element-adding contract and the "before you say you are done" gate.

## Rules

1. **Children are positional, attributes are keyword.** `Div(P("a"), cls="card")`.
2. **Text is escaped.** Pass a plain `str`. Never pre-escape — you get `&amp;lt;`.
3. **`RawHtml` is the only opt-out**, and never for anything from data.
4. **Void elements take no children** and raise if given one: `Br`, `Img`, `Input`,
   `Link`, `Meta`, `Hr`, `Col`, `Source`, `Track`, `Wbr`, `Base`, `Embed`.
5. **`Fragment` groups; `RawHtml` injects.** `Fragment` keeps the tree and its
   indentation, `RawHtml` loses both.
6. **Boolean attributes are `True`**, not `"true"`. `False`/`None` omit the attribute.
7. **Names that collide take a trailing underscore**: `cls`, `for_`, `type_`, `id_`.
   The rendered attribute keeps the HTML spelling.
8. **`Document` owns the doctype and `lang`.** Never write `<!DOCTYPE html>` by hand.
9. **`render(node, options)` is a function and returns the string.** It does not print.
   Options are a value; there is no global.
10. **Iterables are flattened and `None` children are dropped** — that is how loops and
    conditionals work: `Ul(Li(x) for x in items)`, `Div(x if cond else None)`.
11. **`Img` requires `alt`; `Iframe` requires `title`.** Deliberate. Do not work around it.
12. **Never invent an element name.** Check `references/tag-catalog.md`.

## Read it when

| File | Read it when |
| --- | --- |
| `references/tag-catalog.md` | You need an element name or its signature. **Generated from the source, so it cannot drift.** |
| `references/recipes.md` | You need the shape for a page, layout, component, table, form, media, SEO head, sitemap, feed, or writing to disk. |
| `references/pitfalls.md` | Output is wrong, something is double-escaped, or a 0.1.0 name is missing. |

## Minimal example

```python
from winged import Body, Document, H1, Head, P, Title, render

page = Document(Head(Title("Home")), Body(H1("Hi"), P("<ok>")), lang="pt-BR")
print(render(page))
# <!DOCTYPE html>
# <html lang="pt-BR"><head><title>Home</title></head><body><h1>Hi</h1><p>&lt;ok&gt;</p></body></html>
```
