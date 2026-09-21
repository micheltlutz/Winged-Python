"""The public surface: what `import winged` and `from winged.prelude import *` give you."""

from __future__ import annotations

import winged


def test_star_import_is_bounded_by_all() -> None:
    namespace: dict[str, object] = {}
    exec("from winged import *", namespace)
    # __version__ is a dunder and is deliberately in __all__, so it must not be filtered.
    exported = set(namespace) - {"__builtins__"}
    assert exported == set(winged.__all__)


def test_prelude_re_exports_the_same_names() -> None:
    from winged import prelude

    assert set(prelude.__all__) == set(winged.__all__)


def test_version_is_a_string() -> None:
    assert isinstance(winged.__version__, str)
    assert winged.__version__


def test_no_sys_path_mutation() -> None:
    # 0.1.0's winged/__init__.py was two lines: `import sys` and `sys.path.insert(0, "")`,
    # which put the current directory on the import path for anyone who imported the
    # library. Assert the effect, not the spelling -- the docstring mentions it.
    import sys

    assert "" not in sys.path[:1]
    source = __import__("pathlib").Path(winged.__file__).read_text()
    assert "sys.path.insert" not in source


def test_core_names_are_exported() -> None:
    for name in ("Document", "RenderOptions", "render", "Fragment", "RawHtml", "escape_text"):
        assert hasattr(winged, name), name
