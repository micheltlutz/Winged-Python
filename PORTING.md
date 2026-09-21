# Porting from Winged-Swift

A map from `Winged-Swift` 2.0.0 to `Winged-Python` 1.0.0, and an honest list of everywhere
the two behave differently.

Markup parity is not a claim here — it is a test. `tests/test_golden.py` reproduces all
four of Winged-Swift's golden fixtures byte for byte. Everything below is either a rename,
or a difference that shows up somewhere those four files do not reach.

## Type and function mapping

| Winged-Swift | Winged-Python | notes |
| --- | --- | --- |
| `HTMLTag` (class) | `Element` | |
| `HTMLTag.write(into:options:indentLevel:)` | `Node.write_into` | the overridable primitive in both |
| `HTMLTag.render(_:)` | `render(node, options)` | a free function, not a method |
| `HTMLTag.render()` | `render(node)` | compact in both |
| `RenderOptions` | `RenderOptions` | `pretty`, `indent`, `xhtml_self_closing` |
| `RenderOptions.compact` / `.pretty` | `RenderOptions.compact()` / `.pretty_()` | trailing `_`: `pretty` is already a field |
| `Attribute(key:value:)` | `Attribute(key, value)` | |
| `Attribute.boolean(_:)` | `Attribute.boolean` | |
| `HTMLEscape.escape(_:)` | `escape_text` | |
| `HTMLEscape.escapeAttribute(_:)` | `escape_attribute` | |
| private `escapeXML` ×2 | `escape_xml` | Swift has two identical copies |
| `Fragment` (subclass) | `Fragment` | |
| `RawHTML` (subclass) | `RawHtml` | |
| — | `Comment` | **new** |
| — | `Text` | **new** — Swift keeps text in a `content` string on the tag |
| `Document` | `Document` | |
| `Layout` (protocol) | `Layout` (`typing.Protocol`) | structural in both |
| `Layout.render(contents:)` | `render_many(layout, contents)` | a free function |
| `SEO.openGraph(…)` | `seo.open_graph` | |
| `SEO.openGraphArticle(…)` | `seo.open_graph_article` | |
| `SEO.twitterCard(…)` | `seo.twitter_card` | |
| `SEO.common(…)` | `seo.common` | |
| `SEO.complete(…)` | `seo.SeoBuilder.build` | |
| `SitemapURL` / `SitemapGenerator` | `sitemap.SitemapUrl` / `SitemapGenerator` | |
| `RSSItem` / `RSSGenerator` | `feed.RssItem` / `RssGenerator` | |
| `StaticSiteGenerator` | `ssg.StaticSiteGenerator` | |
| `@HTMLBuilder` / `@HTMLFragmentBuilder` | varargs children | see below |
| `html { … }` | `Document(head, body)` | |
| `fragment { … }` | `Fragment(…)` | |
| — | `accessibility.audit` | **new** — Swift's `ROADMAP.md` asks for it |
| — | the `winged` CLI's Python equivalent | Swift ships `winged` too |

### Builder methods

| Winged-Swift | Winged-Python |
| --- | --- |
| `addClass(_:)` | `add_class` |
| `addClasses(_:)` | `add_classes` |
| `setId(_:)` | `set_id` |
| `setStyle(_:)` | `set_style` |
| `setRole(_:)` | `set_role` |
| `setAttribute(key:value:)` | `attr` |
| `dataAttribute(key:value:)` | `data_attr` |
| `dataAttributes(_:)` | `data_attrs` |
| `ariaAttribute(key:value:)` | `aria_attr` |
| `ariaAttributes(_:)` | `aria_attrs` |
| `addAttribute(_:)` | `add_attribute` |
| `addChild(_:)` | `child` |
| `setContent(_:escape:)` | `text` |

### Renamed elements and attributes

| Winged-Swift | Winged-Python | why |
| --- | --- | --- |
| `MainTag` | `Main` | Swift needs the suffix; Python does not |
| `VarTag` | `Var` | same |
| `Label(for:)` | `Label(for_=…)` | `for` *is* a Python keyword. The rendered attribute is still `for`. |
| `Input(type:)` | `Input(type_=…)` | `type` shadows a builtin |
| `HTMLTag(_:attributes:)` with a `class` | `cls=` | `class` is a keyword |
| `Img(src:alt:)` | `Img(src, alt)` | `alt` required in both |
| `Iframe(src:title:)` | `Iframe(src, title)` | `title` required in both |

`A` and `I` keep their one-letter names. Renaming them to satisfy a linter would make the
DSL lie about the markup it produces; Winged-Swift sets SwiftLint's `type_name.min_length`
to 1 for exactly this reason, and `pyproject.toml` disables ruff's `E742` on the generated
module.

## The DSL

Swift's result builders have no Python equivalent, so children are varargs:

```python
Document(
    Head(Title("Home"), Meta(charset="UTF-8")),
    Body(Main(P("Hello ", Strong("world")), Ul(*(Li(x) for x in items)))),
    lang="pt-BR",
)
```

Three behaviours replace what Swift needs `buildBlock`, `buildArray` and a generic
`buildExpression<Tag: HTMLTag>([Tag])` for:

- an **iterable** child is flattened, so `Ul(Li(x) for x in items)` and `Ul([Li("a")])`
  both work — this is the case that made Swift's builder ambiguous until 2.0.0;
- a **`None`** child is dropped, so `Div(x if cond else None)` is the `if` form;
- a **`str`** child becomes escaped `Text`.

## Deliberate behavioural differences

Each of these is a decision, not an accident.

### 1. `data_attrs` and `aria_attrs` output is deterministic

Swift's `dataAttributes(_:)` and `ariaAttributes(_:)` take a `Dictionary`, so the order in
which the attributes render varies between runs. That makes output diffs noisy and golden
files impossible for any page that uses them. Python dicts preserve insertion order, so
matching Swift here would cost effort and buy nothing.

### 2. Void elements raise on a child

Swift ignores a child added to `<br>`. 0.1.0 of this library did too. Both are worse than
refusing it: the child silently disappears from the page. `Element("br", P("x"))` raises.

### 3. Text is a node, not a string on the tag

Swift's `HTMLTag` carries an optional `content: String?` alongside its children, which is
why its 2.0.0 release notes mention pretty printing having dropped the text when both were
set. Here text is an ordinary `Text` node in the child list, so the case cannot arise.

The visible consequence: an element whose children are **all** text renders inline in
pretty mode (`<a href="/">Home</a>`), matching Swift's fixtures; an element with any
element child puts each child on its own line.

### 4. `render` is a function, not a method

`render(node)` rather than `node.render()`. It keeps `Node` a one-method protocol, so a
custom node needs only `write_into`.

### 5. `Comment` refuses `--`

A body containing `--` would close the comment early. Swift has no `Comment` type.

### 6. `clean()` refuses dangerous targets

`StaticSiteGenerator.clean()` will not empty the filesystem root or the home directory,
and will not follow a symlink out of the output directory. Swift's does not check.

### 7. An accessibility audit exists

`accessibility.audit` implements the debug check Winged-Swift's `ROADMAP.md` describes
under "Quality" and has not shipped.
