# Pitfalls

The mistakes people actually make with this library, and why each one happens.

## 1. Pre-escaping

```python
Div("Tom &amp; Jerry")  # renders Tom &amp;amp; Jerry
Div("Tom & Jerry")  # renders Tom &amp; Jerry  ✅
```

Text children and attribute values are escaped for you. Attribute values are escaped **at
construction**, which is why rendering the same tree twice is byte-identical.

## 2. Reaching for `RawHtml` too early

`RawHtml` exists for markup you produced yourself — a rendered Markdown body, an embedded
SVG. It is the one place the escaping stops. If the string came from a form, a database,
or an API, it does not go in here.

## 3. `Fragment` vs `RawHtml`

Both put several things where one was expected. They are not interchangeable:

| | keeps the tree | keeps pretty-print indentation | escapes |
| --- | --- | --- | --- |
| `Fragment(P("a"), P("b"))` | ✅ | ✅ | ✅ |
| `RawHtml("<p>a</p><p>b</p>")` | ❌ | ❌ | ❌ |

Use `Fragment` to return several nodes from a function. Use `RawHtml` only for a string of
markup you already have.

## 4. Giving a void element children

```python
Br(P("x"))  # raises
Img("/a.png", "alt", P("x"))  # raises
```

This is deliberate. Winged-Swift ignores the child and 0.1.0 of this library dropped it
silently — both of which make content disappear from the page with no error.

## 5. Expecting `render()` to print

0.1.0's `generate()` printed and returned `None`. `render()` returns the string:

```python
print(render(page))  # ✅
print(page.generate())  # gone in 1.0 — it printed, then printed None
```

## 6. Reusing one element in two places

The tree has reference semantics. This puts the *same* node in both lists:

```python
shared = Li("Home")
Ul(shared, shared)  # one node, rendered twice — mutating it changes both
Ul(Li("Home"), Li("Home"))  # two nodes  ✅
```

It renders the way you expect; it is mutation that surprises you.

## 7. Forgetting the trailing underscore

`class`, `for`, `type` and `id` are a Python keyword or builtin. Write `cls`, `for_`,
`type_`, `id_`. The rendered attribute is the HTML spelling either way.

```python
Label("E-mail", for_="email")  # <label for="email">E-mail</label>
```

## 8. `"true"` instead of `True`

```python
Input(type_="checkbox", checked="true")  # <input type="checkbox" checked="true">
Input(type_="checkbox", checked=True)  # <input type="checkbox" checked>   ✅
```

`False` and `None` omit the attribute entirely, so `disabled=is_locked` does the right
thing without a conditional.

## 9. Writing the doctype by hand

`Document` owns `<!DOCTYPE html>` and `<html lang>`. Adding your own produces two.

## 10. Expecting pretty mode inside `<pre>`

`<pre>`, `<code>` and `<textarea>` render compactly even under
`RenderOptions.pretty_()`, because indentation inside them is content the browser shows.

## 11. Expecting every element to indent in pretty mode

An element whose children are **all** text renders on one line — `<a href="/">Home</a>`.
Only elements with element children get indented. This matches Winged-Swift's fixtures.

## 12. Looking for 0.1.0's names

`Tag`, `String`, `GenericElement`, `Doctype`, `H(1, …)`, `LinkRel`, `get_string()`,
`add()` — all gone.
[MIGRATION.md](https://github.com/micheltlutz/Winged-Python/blob/main/MIGRATION.md)
maps each one.

## 13. Assuming a URL is validated

Escaping prevents a value breaking out of its attribute. It does not inspect the scheme:
`A("x", href="javascript:alert(1)")` renders that href. Validate URLs from data yourself.
