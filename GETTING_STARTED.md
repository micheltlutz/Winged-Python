# Getting started

Four ways in, from least to most setup. All you need is Python 3.10 or newer.

## Method 0 — the CLI

The fastest path. Scaffolds a working site, builds it, and previews it.

```bash
pip install winged-python
winged new mysite
cd mysite
winged build
winged serve --watch
```

Open <http://127.0.0.1:8000>. Edit `site.py`, save, and `--watch` rebuilds; refresh the
page to see it.

What you got:

```
mysite/
  site.py              the generator — every page is a function returning a Document
  layout.py            the shared shell: header, footer, nav
  assets/css/style.css copied into dist/ verbatim
  AGENTS.md            so a coding agent knows the rules from the first commit
  .gitignore           dist/ is generated
```

## Method 1 — minimal, no project

```bash
pip install winged-python
```

```python
# page.py
from winged import Body, Document, H1, Head, P, Title, render

page = Document(Head(Title("Home")), Body(H1("Hello"), P("From Winged-Python.")))

with open("index.html", "w") as out:
    out.write(render(page))
```

```bash
python page.py && open index.html
```

## Method 2 — a real site, with CSS and SEO

```python
# site.py
from pathlib import Path

from winged import Body, Document, H1, Head, Link, Main, P, Title
from winged.seo import SeoBuilder
from winged.sitemap import SitemapGenerator, SitemapUrl
from winged.ssg import StaticSiteGenerator

# Resolved from this file, not the current directory. See "Common issues" below.
ROOT = Path(__file__).resolve().parent
SITE_URL = "https://example.com"


def page(title: str, *content: object) -> Document:
    head = Head(
        SeoBuilder(
            title=title,
            description="A site built with Winged-Python.",
            image=f"{SITE_URL}/og.jpg",
            url=SITE_URL,
        ).build(),
        Title(title),
        Link(href="/css/style.css", rel="stylesheet"),
    )
    return Document(head, Body(Main(*content)), lang="pt-BR")


def main() -> None:
    site = StaticSiteGenerator(ROOT / "dist")
    site.clean()
    site.generate(page("Home", H1("Home"), P("Hello.")), "index.html")
    site.generate(page("About", H1("About")), "about.html")
    site.copy_asset(ROOT / "assets" / "css" / "style.css", "css/style.css")
    site.write_file(
        SitemapGenerator(SITE_URL).generate(
            [SitemapUrl("/", priority=1.0), SitemapUrl("/about", priority=0.5)]
        ),
        "sitemap.xml",
    )


if __name__ == "__main__":
    main()
```

## Method 3 — live preview while you work

```bash
winged serve --watch --open
```

`--watch` rebuilds when `site.py`, `layout.py` or anything under `assets/` changes,
debounced so one save is one rebuild. The page does not reload itself yet — that is on the
[roadmap](ROADMAP.md).

## Checking your pages

```python
from winged.accessibility import audit

for issue in audit(page):
    print(f"{issue.rule}: {issue.message} at {issue.path}")
```

Eight rules, including images without `alt`, buttons with no accessible name, inputs with
no label, and skipped heading levels.

## Deployment

`dist/` is a directory of static files. Anything that serves static files will do.

### GitHub Pages

```yaml
# .github/workflows/deploy.yml
name: Deploy
on:
  push:
    branches: [main]
permissions:
  contents: read
  pages: write
  id-token: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install winged-python
      - run: python site.py
      - uses: actions/upload-pages-artifact@v3
        with:
          path: dist
      - uses: actions/deploy-pages@v4
```

### Netlify

`netlify.toml`:

```toml
[build]
  command = "pip install winged-python && python site.py"
  publish = "dist"
```

### Vercel

`vercel.json`:

```json
{ "buildCommand": "pip install winged-python && python site.py", "outputDirectory": "dist" }
```

## Common issues

### My assets are missing when I build from another directory

Resolve paths from the file, not the process:

```python
ROOT = Path(__file__).resolve().parent  # ✅
site = StaticSiteGenerator(ROOT / "dist")

site = StaticSiteGenerator("dist")  # ❌ depends on where you ran it
```

This is the failure `scripts/verify.sh` guards against by running the CLI from `/`.

### My text shows up as `&amp;amp;`

You escaped it before passing it in. Don't — text children and attribute values are
escaped for you.

### My markup is being escaped and I wanted it raw

Wrap it in `RawHtml(...)`. Only do that for markup you produced yourself, never for
anything that came from a user or an API.

### `<br>` says it cannot have children

It cannot. Void elements take attributes only. See
[docs/tag-catalog.md](docs/tag-catalog.md) for which are which.

### I upgraded from 0.1.0 and nothing imports

1.0.0 is a clean break. See [MIGRATION.md](MIGRATION.md) — it maps every removed name and
ends with a grep checklist.

## Where next

- [docs/recipes.md](docs/recipes.md) — task-shaped examples
- [docs/pitfalls.md](docs/pitfalls.md) — the mistakes, and why they happen
- [docs/tag-catalog.md](docs/tag-catalog.md) — every element
- [AGENTS.md](AGENTS.md) — working on the library itself
