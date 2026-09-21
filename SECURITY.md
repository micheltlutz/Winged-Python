# Security Policy

## Reporting a vulnerability

Email <michel_lutz@icloud.com> with a description and, if you can, a minimal reproduction.
Please do not open a public issue for a vulnerability. You can expect an acknowledgement
within a few days.

## Supported versions

| Version | Supported |
| --- | --- |
| 1.0.x | ✅ |
| 0.1.x | ❌ — see below |

**0.1.x performs no output escaping of any kind** and should not be used with data you do
not control. There is no patch path; upgrade to 1.0 (see [MIGRATION.md](MIGRATION.md)).

## What this library does about escaping

Winged-Python builds a string of HTML. Its entire security surface is which characters
reach the output unchanged.

**Escaped by default:**

- Text children. `Div("<script>")` renders `<div>&lt;script&gt;</div>`. A bare `str` child
  becomes a `Text` node, and `Text` escapes `&`, `<`, `>`, `"` and `'`.
- Attribute values, at construction — `Attribute("title", value)` escapes `&`, `"` and
  `'`. Inside a quoted value, `<` and `>` are not delimiters, so they are left readable.
- Every value in the sitemap and RSS generators, via `escape_xml`.
- Values passed to `add_class`, `set_id`, `set_style`, `attr`, `data_attr` and
  `aria_attr`. Escaping happens once, so repeated `add_class` calls do not double-escape.

**Not escaped, by design:**

- `RawHtml(...)`. This is the only way to inject markup verbatim, and it is deliberately
  conspicuous at the call site. **Never pass user input to it.**
- `Attribute.raw(...)`, used internally for meta tag keys such as `og:title`.
- `Element.text(content, escape=False)`.

**What escaping does not protect you from:**

- A `javascript:` URL in `A(href=...)` or `Script(src=...)`. The value is escaped, so it
  cannot break out of the attribute, but the URL scheme is not inspected. Validate URLs
  that come from data. (Winged-Swift's `ROADMAP.md` lists a URL policy for 3.0; the same
  gap exists here.)
- Content inside `<script>` or `<style>`, where HTML escaping is the wrong escaping. Do
  not build either from untrusted data.

## The `winged serve` development server

`winged serve` is a development tool. It binds `127.0.0.1`, refuses paths that resolve
outside the directory it is serving, and does not follow symlinks out of it. It is not
hardened for public exposure — do not put it on a public interface.
