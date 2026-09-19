## What changed

<!-- One or two sentences. What does this do that the previous code did not? -->

## Why

<!-- The problem, not the patch. Link the issue if there is one: Closes #123 -->

## Markup impact

<!-- If rendered output changes, paste before and after. If it does not, say "none". -->

## Checklist

- [ ] `./scripts/verify.sh` passes
- [ ] Tests cover the change, and assert on rendered strings rather than tree shape
- [ ] `CHANGELOG.md` has an entry under `## [Unreleased]`
- [ ] If an element was added: a row in `winged/_tagtable.py`, and both generators re-run
