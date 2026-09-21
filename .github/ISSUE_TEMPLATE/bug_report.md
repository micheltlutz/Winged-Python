---
name: Bug report
about: Markup that is wrong, or an error you did not expect
labels: bug
---

## What happened

<!-- The markup produced, or the traceback. -->

## What you expected

<!-- The markup you expected instead. -->

## Minimal reproduction

```python
from winged import Div, render

print(render(Div("...")))
```

## Environment

- Winged-Python version: <!-- python -c "import winged; print(winged.__version__)" -->
- Python version: <!-- python --version -->
- OS:
