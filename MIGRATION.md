# Migrating from 0.1.0 to 1.0.0

1.0.0 is a clean break. Nothing from 0.1.0 survives, because most of what it exported was
either broken or a workaround for something that is now handled — and because 0.1.0 does
no output escaping, carrying it forward compatibly would mean carrying an XSS hole.

The good news: the new API is shorter, and the port is mechanical.

## 1. Imports

`winged/HTML/__init__.py` was entirely commented out in 0.1.0, so every import named a
module file directly. Now everything comes from the top level.

```python
# 0.1.0
from winged.HTML.div import Div
from winged.HTML.p import P
from winged.core.attribute import Attribute

# 1.0.0
from winged import Div, P, Attribute
```

## 2. Rendering

`generate()` **printed** the markup and returned `None`, so `print(x.generate())` printed
the page and then printed `None`. `render()` returns the string.

```python
# 0.1.0
div.generate()  # prints
html = div.get_string()  # returns

# 1.0.0
from winged import render, RenderOptions

print(render(div))  # compact — what you ship
print(render(div, RenderOptions.pretty_()))  # indented
```

## 3. Building a tree

```python
# 0.1.0
div = Div(("class", "card"))
div.add(P())
p = P()
p.add(String("Hello"))

# 1.0.0
div = Div(P("Hello"), cls="card")
```

Children are positional, attributes are keyword. Strings are escaped. Iterables are
flattened, so `Ul(Li(x) for x in items)` works; `None` children are dropped, so
`Div(x if cond else None)` is the conditional form.

## 4. Attributes

```python
# 0.1.0 — tuples, with None meaning a bare key
Attribute(("class", "a"), ("required", None))

# 1.0.0 — keywords, with True meaning a bare key
Div(cls="a")
Input(type_="checkbox", checked=True)  # renders `checked`, not checked="true"
Input(type_="text", disabled=False)  # omits the attribute entirely
```

Names that collide with a Python keyword or builtin take a trailing underscore. The
rendered attribute is always the HTML spelling.

| HTML | Python |
| --- | --- |
| `class` | `cls` (or `class_`) |
| `for` | `for_` |
| `type` | `type_` |
| `id` | `id_` |
| `data-user-id` | `data_user_id` |
| `aria-label` | `aria_label` |

## 5. Removed names

| 0.1.0 | 1.0.0 |
| --- | --- |
| `Tag` | `Element` |
| `ElementAbstract` | the `Node` protocol |
| `GenericElement` | `Fragment` |
| `AttributeType` | gone — attributes are keywords |
| `String("x")` | a bare `"x"` child (escaped), or `RawHtml("x")` (not) |
| `H(1, ...)` | `H1(...)` … `H6(...)` |
| `Doctype()` | `Document(head, body, lang=...)` owns it |
| `LinkRel` | `Link` |
| `Center`, `U` | obsolete HTML — use CSS (`text-align`, `text-decoration`) |
| `get_string()` | `render(node)` |
| `generate()` | `print(render(node))` |
| `add(child)` | pass it positionally, or `.child(...)` |
| `add_attributes(...)` | pass keywords, or `.attr(k, v)` |
| `is_container()` | `tag not in winged.VOID_ELEMENTS` |
| `is_form_element()` | gone — it drove nothing |
| `Table.add_row()`, `add_in_row()`, `add_table_headers()` | ordinary composition, below |

## 6. Tables

`Table` had bespoke row-building methods, and `get_string()` mutated state — it appended
its rows into `self.tbody` on every call, so rendering twice duplicated the whole body.
Tables are now ordinary composition.

```python
# 1.0.0
Table(
    Caption("Plans"),
    Thead(Tr(Th("Plan"), Th("Price"))),
    Tbody(*(Tr(Td(name), Td(price)) for name, price in plans)),
)
```

## 7. Pages

```python
# 1.0.0
from winged import Body, Document, H1, Head, Title, render

page = Document(Head(Title("Home")), Body(H1("Hello")), lang="pt-BR")
print(render(page))
```

## Checklist

Run these over your code; each hit is a call site to change.

```bash
grep -rn "from winged.HTML" .          # → from winged import ...
grep -rn "\.get_string()" .            # → render(...)
grep -rn "\.generate()" .              # → print(render(...))
grep -rn "\.add(" .                    # → positional children
grep -rn "String(" .                   # → a bare str, or RawHtml
grep -rn "Doctype\|LinkRel\|Center(" . # → Document, Link, CSS
grep -rn "H(" .                        # → H1 … H6
```
