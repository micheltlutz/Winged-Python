"""Report Markdown links that point at a file which is not there.

Only relative links are checked: an `http`, `mailto` or bare-anchor target is somebody
else's problem. Prints one `file -> target` per line and exits 0 either way — the caller
in ``verify.sh`` decides whether an empty report is the pass, which keeps this script
usable by hand while you are editing the documentation.
"""

from __future__ import annotations

import pathlib
import re
import sys

#: Nothing under these is ours to check.
SKIPPED = frozenset(
    {".git", ".venv", ".mypy_cache", ".pytest_cache", "dist", "build", "node_modules"}
)

LINK = re.compile(r"\]\(([^)\s]+)")


def broken_links(root: pathlib.Path) -> list[str]:
    """Every relative Markdown link under ``root`` whose target does not exist."""
    found: list[str] = []
    for path in sorted(root.rglob("*.md")):
        if SKIPPED.intersection(path.parts):
            continue
        for target in LINK.findall(path.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            # Strip the anchor: the file has to exist, the heading we do not verify.
            anchorless = target.split("#", 1)[0]
            if anchorless and not (path.parent / anchorless).exists():
                found.append(f"{path} -> {target}")
    return found


def main() -> int:
    """Print the broken links, one per line."""
    for line in broken_links(pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")):
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
