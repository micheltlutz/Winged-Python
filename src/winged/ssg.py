"""Static site generation.

Ports ``Winged-Swift/Sources/WingedSwift/static/StaticSiteGenerator.swift``.
"""

from __future__ import annotations

import os
import shutil
from collections.abc import Mapping
from pathlib import Path

from .core.render import Node, RenderOptions, render

__all__ = ["StaticSiteGenerator"]

# Directories clean() will never empty, however it was pointed at them.
_FORBIDDEN_ROOTS = frozenset({Path("/"), Path.home()})


class StaticSiteGenerator:
    """Writes rendered pages and assets into an output directory."""

    __slots__ = ("output_directory",)

    def __init__(self, output_directory: str | os.PathLike[str]) -> None:
        self.output_directory = Path(output_directory).resolve()

    # -- writing ----------------------------------------------------------------------

    def _target(self, path: str) -> Path:
        target = (self.output_directory / path).resolve()
        if not target.is_relative_to(self.output_directory):
            raise ValueError(f"{path!r} resolves outside the output directory")
        return target

    def write_file(self, content: str, to: str) -> None:
        """Write text, creating intermediate directories.

        UTF-8 with ``\\n`` line endings on every platform, or the golden fixtures fail on
        Windows.
        """
        target = self._target(to)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8", newline="\n")

    def generate(self, document: Node, to: str, options: RenderOptions | None = None) -> None:
        """Render one page.

        Defaults to pretty output, matching WingedSwift: a static site's HTML is read by
        humans and diffed in git.
        """
        self.write_file(render(document, options or RenderOptions.pretty_()), to)

    def generate_multiple(
        self, pages: Mapping[str, Node], options: RenderOptions | None = None
    ) -> None:
        """Render many pages. Reports the first failure with the path that failed."""
        for path, document in pages.items():
            try:
                self.generate(document, path, options)
            except OSError as error:
                raise OSError(f"failed to write {path!r}: {error}") from error

    def copy_asset(self, source: str | os.PathLike[str], to: str) -> None:
        target = self._target(to)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)

    # -- cleaning ---------------------------------------------------------------------

    def clean(self, *, create_directory: bool = True) -> None:
        """Empty the output directory.

        This is the one method here that deletes, so it refuses the cases where a wrong
        relative path in a config file would become data loss: the filesystem root, the
        user's home directory, and anything reached by following a symlink out of the
        output directory. Paths are resolved before comparison.
        """
        target = self.output_directory
        if target in _FORBIDDEN_ROOTS:
            raise ValueError(f"refusing to clean {target}")
        if target.parent == target:  # a filesystem root on any platform
            raise ValueError(f"refusing to clean the filesystem root {target}")

        if target.exists():
            if target.is_symlink():
                raise ValueError(f"refusing to clean {target}: it is a symlink")
            for entry in target.iterdir():
                if entry.is_dir() and not entry.is_symlink():
                    shutil.rmtree(entry)
                else:
                    entry.unlink()
        if create_directory:
            target.mkdir(parents=True, exist_ok=True)
