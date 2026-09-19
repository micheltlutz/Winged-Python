# Contributing to Winged-Python

Thanks for wanting to help. This document covers everything from a first clone to a
merged pull request.

## Ways to contribute

- **Fix a bug.** Open an issue first if the fix changes rendered markup.
- **Close a parity gap.** Winged-Swift does something this port does not? There is an
  issue template for it, and [PORTING.md](PORTING.md) lists the differences that are
  deliberate — check there before filing.
- **Take a roadmap item.** [ROADMAP.md](ROADMAP.md) states each as a problem.
- **Improve the docs.** Every code block in this repository is meant to run. If one does
  not, that is a bug.

## Getting started

```bash
git clone https://github.com/micheltlutz/Winged-Python.git
cd Winged-Python
python -m venv .venv && source .venv/bin/activate
pip install -e . pytest pytest-cov ruff mypy build

./scripts/verify.sh
```

If `verify.sh` is green on a fresh clone, your environment is right.

## The development loop

1. **Branch** from `main`: `git checkout -b fix/void-element-children`.
2. **Change** the code. If you are adding an element, follow the five-step contract in
   [AGENTS.md](AGENTS.md#adding-an-element-to-the-library) — it is one row in a table plus
   two generator runs.
3. **Test.** `pytest -q` while you work.
4. **Verify.** `./scripts/verify.sh` before you push. It is a superset of CI, so if it is
   green, CI will be.
5. **Commit** with a typed message (below).
6. **Open a pull request** and fill in the template.

## Commit messages

```
Add: Comment node
Fix: void elements no longer accept children
Change: data_attrs emits in insertion order
Docs: recipes for forms and media
```

Use `Add:`, `Fix:`, `Change:` or `Docs:`. Keep the subject under 72 characters, in the
imperative. If the change affects rendered markup, show before and after in the body.

## Code style

- `ruff format` decides formatting. Do not argue with it; run it.
- `ruff check` and `mypy --strict` are **gating**, in CI and in `verify.sh`.
- 100-column lines, four-space indent.
- A docstring on every public module, class and function.
- Comments explain **why**. If a line encodes a decision, say what the alternative was and
  why it lost. `src/winged/core/escape.py` is the model.
- English throughout.

## Tests

- pytest: plain functions, `parametrize`, `capsys`. No `unittest.TestCase` — 0.1.0's tests
  were written that way and merely run by pytest, which bought nothing and cost a
  hand-rolled, exception-unsafe stdout capture.
- **Assert on rendered strings, never on tree shape or private attributes.** The library's
  entire output is a string; a test reaching into `_children` fails on a refactor that
  changed nothing a user can see.
- A file per feature, named after what it covers. Ported tests name their Winged-Swift
  source in the module docstring.
- Coverage must stay at or above 90%; CI fails below it.

### The golden fixtures

`tests/fixtures/` holds four files copied from Winged-Swift. `tests/test_golden.py`
reproduces them byte for byte — this is what makes "parity" a test rather than a claim.

If your change is *supposed* to change that output:

```bash
WINGED_UPDATE_FIXTURES=1 pytest tests/test_golden.py
```

That rewrites the fixture **and fails the run**, so you have to re-run and read the diff.
A regeneration switch that silently passes is how a golden suite stops meaning anything.
Explain the change in your pull request, and add it to
[PORTING.md](PORTING.md#deliberate-behavioural-differences) if it is a divergence from
Winged-Swift.

## Generated files

Two files are generated and committed:

- `src/winged/elements.py` — from `src/winged/_tagtable.py`
- `docs/tag-catalog.md` — from the same table

Both have a `--check` mode wired into CI, so editing them by hand fails the build. Edit
the table and regenerate.

## Code review

Expect a response within a few days. A reviewer will look for:

- [ ] `./scripts/verify.sh` is green
- [ ] New behaviour has a test that asserts on rendered output
- [ ] Rendered-markup changes are explained, and fixtures updated deliberately
- [ ] Public API has docstrings
- [ ] `CHANGELOG.md` has an entry
- [ ] Nothing new in `dependencies` — this library is stdlib-only, and stays that way

## Good first issues

Issues labelled [`good first issue`](https://github.com/micheltlutz/Winged-Python/labels/good%20first%20issue)
are scoped so you can finish them in an evening. The `link-text` and `heading-order`
limitations in [ROADMAP.md](ROADMAP.md#quality) are good ones: both are small, both have
an obvious test, and both are real.

## Getting help

Open a [discussion](https://github.com/micheltlutz/Winged-Python/discussions). For working
on the library itself, [AGENTS.md](AGENTS.md) is the reference — it is written for coding
agents but works just as well for people.

## Code of conduct

By participating you agree to the [Code of Conduct](CODE_OF_CONDUCT.md).
