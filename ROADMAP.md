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

- **Streaming render.** `render()` builds one string in memory. Writing directly into a
  file object would keep memory flat for very large pages.
- **The `link-text` a11y rule is shallow.** It only looks at direct `<img>` children of an
  `<a>`; a link wrapping a `<span><img></span>` is not caught.
- **`heading-order` does not track document sections.** It compares against the last
  heading seen anywhere in the tree, so a legitimate `<h3>` opening a new `<section>`
  after an `<h1>` is reported. Scoping it to sectioning elements would fix it.
- **No Sphinx or API reference site.** The docstrings are there; nothing renders them.
