# Roadmap

Known gaps and where the library is going. Each item states the problem first — if you
want to contribute, these are the highest-value places to start. See
[CONTRIBUTING.md](CONTRIBUTING.md).

## Shipped in 1.0

Escaping, 93 elements, `RenderOptions`, `Document`, `Fragment` / `RawHtml` / `Comment`,
the varargs DSL, SEO, sitemap, RSS, the static site generator, an accessibility audit, the
`winged` CLI, full typing, and byte-for-byte parity with Winged-Swift's golden fixtures.
See [CHANGELOG.md](CHANGELOG.md).

## 1.x — Tooling

### Incremental builds and cache busting

`StaticSiteGenerator` rewrites every file on every run, and there is no asset
fingerprinting (`style.a1b2c3.css`), which forces short cache TTLs on deployed sites. A
content hash plus a manifest would fix both. Winged-Swift has the same gap.

### Live reload

`winged serve --watch` rebuilds and asks you to refresh. Injecting a small SSE client into
the served HTML would make the page reload itself.

### `winged deploy`

GitHub Pages, Netlify and Vercel deploys are still per-project shell scripts.
`GETTING_STARTED.md` documents them by hand.

## 2.0 — API questions

Open questions, not commitments:

- **Immutable elements.** `Element` is mutable, which is why reusing one instance in two
  places silently shares the node. A frozen tree would remove a class of surprise, at the
  cost of making the chainable helpers return copies.
- **Typed attributes.** `attr("hfre", …)` accepts anything; a typed set for the common
  attributes would catch a typo at check time without closing the door on custom ones.
- **URL policy.** Optionally reject `javascript:` URLs in `A(href=)`, `Img(src=)` and
  `Script(src=)` when the value comes from data. Today the value is escaped, so it cannot
  break out of the attribute, but the scheme is not inspected — see
  [SECURITY.md](SECURITY.md).

## Quality

- **`StaticSiteGenerator` still buffers each page.** `render_into` exists, but `generate`
  renders to a string and writes it in one call, on purpose: a render that raises halfway
  cannot then leave a truncated file on disk. Streaming it needs a write-to-temp-and-move
  step first.
- **The audit has no `color-contrast` or `tabindex` rule**, and cannot have the first one
  — contrast needs the computed CSS, which this library never sees.
- **No Sphinx or API reference site.** The docstrings are there; nothing renders them.
