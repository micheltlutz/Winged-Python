# Changelog

All notable changes to Winged-Python are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- **The workflow actions moved to the Node 24 runtime** — `actions/checkout` v4 to v7,
  `actions/setup-python` v5 to v7, `softprops/action-gh-release` v2 to v3,
  `codecov/codecov-action` v5 to v7. Every run was printing a deprecation notice and
  being forced onto Node 24 anyway. Nothing here uses what the new majors dropped:
  `checkout` v7 only restricts forked-PR checkout under `pull_request_target`, and
  `setup-python` v7 removed the `pip-install` input.

## [1.0.0] - 2026-09-21

Parity with [Winged-Swift](https://github.com/micheltlutz/Winged-Swift) 2.0.0, demonstrated
rather than claimed: `tests/test_golden.py` reproduces all four of Winged-Swift's golden
fixtures byte for byte.

**This release is a clean break from 0.1.0.** Nothing from the old API survives. See
[MIGRATION.md](MIGRATION.md) for the replacement of every removed name, and
[PORTING.md](PORTING.md) for the map from Winged-Swift.

### Added

- **HTML escaping** — `escape_text`, `escape_attribute` and `escape_xml`. 0.1.0 escaped
  nothing at all: `String.get_string()` returned its text verbatim and attribute values
  were interpolated straight into `key="value"`. Text children are escaped by default and
  `RawHtml` is the only opt-out.
- **93 elements**, up from 49, generated from one table in `winged/_tagtable.py`.
  `docs/tag-catalog.md` is generated from the same table.
- **`RenderOptions`** — `pretty`, `indent`, `xhtml_self_closing`, passed per call rather
  than held as global state. 0.1.0 had no pretty printing; its README showed indented
  output the library could not produce.
- **`render` and `render_into`** — `render` returns the markup as a string; `render_into`
  writes it straight into a text file object, so memory stays flat on a page large enough
  that you would rather not hold it twice. What a node writes into is the `Buffer`
  protocol, which is what makes a list and a file interchangeable without any
  `write_into` knowing which it got.
- **`Document`** — owns `<!DOCTYPE html>` and `<html lang>`.
- **`Fragment`, `RawHtml`, `Comment`, `Text`** — a transparent group, an explicit raw
  injection, a comment that refuses `--`, and escaped text.
- **The varargs API** — `Div(H1("x"), P("y"), cls="box")`. Iterables are flattened, so
  `Ul(Li(x) for x in items)` works; `None` children are dropped, so
  `Div(x if cond else None)` is the conditional form.
- **Chainable helpers** — `add_class`, `add_classes`, `set_id`, `set_style`, `set_role`,
  `attr`, `data_attr(s)`, `aria_attr(s)`, each returning `Self`.
- **`seo`** — Open Graph, Open Graph Article, Twitter Cards, the common head set, and
  `SeoBuilder`.
- **`sitemap`** and **`feed`** — sitemap 0.9 and RSS 2.0 generators.
- **`ssg.StaticSiteGenerator`** — writes pages and assets. `clean()` refuses the
  filesystem root, the home directory, and anything reached through a symlink out of the
  output directory.
- **`accessibility.audit`** — eight rules (`img-alt`, `button-label`, `iframe-title`,
  `link-text`, `heading-order`, `html-lang`, `form-label`, `duplicate-id`). This is the
  check Winged-Swift's `ROADMAP.md` asks for and has not shipped. Three of them are
  deliberately not naive: `link-text` looks at every `<img>` under the link rather than
  its direct children, so the ordinary `<a><span><img></span></a>` icon link is checked;
  `heading-order` treats `<section>`, `<article>`, `<aside>` and `<nav>` as opening a new
  heading context, so an `<h3>` starting a section after an `<h1>` is not a finding; and
  `form-label` reads the whole tree before it judges, so a `<label for=…>` placed after
  its input — what a CSS sibling selector needs — still counts.
- **The `winged` CLI** — `winged new`, `winged build`, `winged serve [--watch]`.
  Stdlib only; the dev server refuses to serve outside its root and binds `127.0.0.1`.
- **`Layout`** — a `typing.Protocol`, satisfied by defining `render` with no base class.
- **Typing** — the package ships `py.typed` and passes `mypy --strict`.
- **`pyproject.toml`**, a `src/` layout, ruff, a five-version CI matrix that runs on pull
  requests, `scripts/verify.sh`, and release to PyPI via trusted publishing.
- **Docs** — `GETTING_STARTED.md`, `MIGRATION.md`, `PORTING.md`, `ROADMAP.md`,
  `AGENTS.md`, `docs/tag-catalog.md`, `docs/recipes.md`, `docs/pitfalls.md`.

### Changed

- **Rendering writes into one buffer.** `write_into(buf, options, depth)` is the single
  overridable primitive. 0.1.0's `get_string()` built a new string per node, which is
  quadratic; `tests/test_performance.py` guards against a return to it.
- **`render()` returns the markup.** 0.1.0's `generate()` printed it and returned `None`,
  so `print(x.generate())` printed the page and then printed `None`.
- **Void elements refuse children** instead of silently discarding them, and render
  without a closing tag. 0.1.0 emitted `<col></col>` and `<source></source>`.
- **`<pre>`, `<code>` and `<textarea>` render compactly** even in pretty mode.
- **Element state is per instance.** 0.1.0 held `_tag`, `_attributes` and `_container` as
  class attributes.
- **`data_attrs` and `aria_attrs` emit in insertion order.** Winged-Swift takes a
  `Dictionary`, so its order varies between runs — which makes golden files impossible.
- **`Img` requires `alt` and `Iframe` requires `title`**, by signature.

### Removed

`Tag`, `ElementAbstract`, `GenericElement`, `AttributeType`, `String`, `H(level)`,
`Doctype`, `LinkRel`, `Center`, `U`, `get_string()`, `generate()`, `add()`,
`add_attributes()`, `is_container()`, `is_form_element()`, `Table.add_row()`,
`Table.add_in_row()`, `Table.add_table_headers()`, tuple-form attributes, `setup.py`,
`requirements.txt`, `pytest.ini`, `import_maker.py` and `demo.py`.

### Fixed

- **`winged/HTML/__init__.py` was entirely commented out**, so `from winged.HTML import
  Div` did not work and every user imported `from winged.HTML.div import Div`.
- **`winged/__init__.py` mutated `sys.path`** at import time.
- **`Attribute` was defined twice in the same file**, the second silently shadowing the
  first.
- **`Table.get_string()` mutated state** — it appended its rows into `self.tbody` on every
  call, so rendering twice duplicated the whole table body.
- **`Table.__init__` accepted no attributes**, unlike every other tag.
- **`ElementAbstract` declared `@abstractmethod` without inheriting `ABC`**, so it
  instantiated fine and enforced nothing.
- **CI never ran on pull requests** and used actions two majors out of date.

## [0.1.0] - 2023-11-30

First public release: a `Tag` base class, 49 hand-written element modules, `Attribute`,
`GenericElement` and a PyPI package.
