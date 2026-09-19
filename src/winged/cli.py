"""The ``winged`` command line interface.

Ports ``Winged-Swift/Sources/WingedCLI/``: ``winged new``, ``winged build`` and
``winged serve [--watch]``.

WingedSwift's own README used to tell people to preview a generated site with
``python3 -m http.server``, which is a slightly funny thing for the Python port to be
replacing -- and a reason to do it properly, with correct MIME types and a server that
cannot be walked out of.

Everything here is stdlib: ``argparse``, ``http.server``. The library has no runtime
dependencies and gains none from shipping a CLI.
"""

from __future__ import annotations

import argparse
import functools
import http.server
import mimetypes
import os
import runpy
import socketserver
import sys
import threading
import time
import webbrowser
from importlib import resources
from pathlib import Path

__all__ = ["main"]

_TEMPLATES = (
    ("site.py.template", "site.py"),
    ("layout.py.template", "layout.py"),
    ("style.css.template", "assets/css/style.css"),
    ("gitignore.template", ".gitignore"),
    ("AGENTS.md.template", "AGENTS.md"),
    ("README.md.template", "README.md"),
)

# mimetypes guesses several of these wrong, or not at all, depending on the platform.
_EXTRA_TYPES = {
    ".css": "text/css",
    ".js": "text/javascript",
    ".mjs": "text/javascript",
    ".svg": "image/svg+xml",
    ".woff2": "font/woff2",
    ".woff": "font/woff",
    ".webmanifest": "application/manifest+json",
    ".json": "application/json",
    ".xml": "application/xml",
}


# -- project root -------------------------------------------------------------------


def find_project_root(start: Path | None = None) -> Path:
    """Walk up from ``start`` looking for ``site.py``.

    Resolving from the project root rather than the current directory is the whole point:
    a generator that uses relative paths passes every unit test and still fails for the
    user. ``scripts/verify.sh`` runs the CLI from ``/`` to keep that honest.
    """
    current = (start or Path.cwd()).resolve()
    for candidate in (current, *current.parents):
        if (candidate / "site.py").is_file():
            return candidate
    raise SystemExit(
        "no site.py found here or in any parent directory — run this inside a project "
        "created with `winged new`"
    )


# -- winged new ---------------------------------------------------------------------


def _read_template(name: str) -> str:
    # importlib.resources, never a path relative to __file__: this has to work from an
    # installed wheel, where the package lives inside site-packages.
    return (resources.files("winged.templates") / name).read_text(encoding="utf-8")


def cmd_new(args: argparse.Namespace) -> int:
    target = Path(args.path or args.name).resolve()
    if target.exists() and any(target.iterdir()):
        print(f"{target} is not empty — refusing to scaffold into it", file=sys.stderr)
        return 1

    for source, destination in _TEMPLATES:
        content = _read_template(source).replace("__NAME__", args.name)
        path = target / destination
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")

    print(f"created {target}")
    print("  next:  cd", target.name, "&&  winged build")
    return 0


# -- winged build -------------------------------------------------------------------


def cmd_build(args: argparse.Namespace) -> int:
    root = find_project_root()
    output = Path(args.output).resolve() if args.output else root / "dist"

    # Run the generator in-process so a traceback survives intact. Swallowing it into a
    # tidy message is its own kind of bug.
    sys.path.insert(0, str(root))
    cwd = Path.cwd()
    try:
        runpy.run_path(str(root / "site.py"), run_name="__main__")
    finally:
        sys.path.remove(str(root))

    if not output.is_dir():
        print(f"{output} was not created by site.py", file=sys.stderr)
        return 1

    total = 0
    for path in sorted(p for p in output.rglob("*") if p.is_file()):
        size = path.stat().st_size
        total += size
        try:
            shown = path.relative_to(cwd)
        except ValueError:
            shown = path
        print(f"  {size:>8,}  {shown}")
    print(f"  {total:>8,}  total")

    if args.check_a11y:
        print("\n--check-a11y: the audit runs inside site.py; see winged.accessibility.audit")
    return 0


# -- winged serve -------------------------------------------------------------------


class _Handler(http.server.SimpleHTTPRequestHandler):
    """A static handler that cannot be walked out of its root."""

    def guess_type(self, path: str | os.PathLike[str]) -> str:
        suffix = Path(path).suffix.lower()
        if suffix in _EXTRA_TYPES:
            return _EXTRA_TYPES[suffix]
        return super().guess_type(path)

    def translate_path(self, path: str) -> str:
        resolved = Path(super().translate_path(path)).resolve()
        root = Path(self.directory).resolve()
        if not resolved.is_relative_to(root):
            # Both "../.." and a symlink pointing out of dist/ land here.
            return str(root / "__forbidden__")
        return str(resolved)

    def log_message(self, format: str, *args: object) -> None:
        sys.stderr.write(f"  {self.address_string()} {format % args}\n")


class _Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


def _watch(root: Path, output: Path, interval: float = 0.4) -> None:
    """Rebuild on change. Debounced, so one editor save is one rebuild."""
    watched = [root / "site.py", root / "layout.py", root / "assets"]

    def snapshot() -> dict[Path, float]:
        stamps: dict[Path, float] = {}
        for entry in watched:
            if entry.is_file():
                stamps[entry] = entry.stat().st_mtime
            elif entry.is_dir():
                for path in entry.rglob("*"):
                    if path.is_file():
                        stamps[path] = path.stat().st_mtime
        return stamps

    previous = snapshot()
    while True:
        time.sleep(interval)
        current = snapshot()
        if current == previous:
            continue
        time.sleep(interval)  # settle, so a burst of saves is one rebuild
        current = snapshot()
        previous = current
        print("\n  change detected — rebuilding")
        try:
            sys.path.insert(0, str(root))
            runpy.run_path(str(root / "site.py"), run_name="__main__")
        except Exception as error:
            print(f"  build failed: {error}", file=sys.stderr)
        finally:
            if str(root) in sys.path:
                sys.path.remove(str(root))


def cmd_serve(args: argparse.Namespace) -> int:
    root = find_project_root()
    output = Path(args.output).resolve() if args.output else root / "dist"
    if not output.is_dir():
        print(f"{output} does not exist — run `winged build` first", file=sys.stderr)
        return 1

    for suffix, kind in _EXTRA_TYPES.items():
        mimetypes.add_type(kind, suffix)

    handler = functools.partial(_Handler, directory=str(output))
    try:
        server = _Server(("127.0.0.1", args.port), handler)
    except OSError as error:
        print(f"cannot bind port {args.port}: {error}", file=sys.stderr)
        return 1

    url = f"http://127.0.0.1:{args.port}/"
    print(f"serving {output} at {url}  (ctrl-c to stop)")

    if args.watch:
        threading.Thread(target=_watch, args=(root, output), daemon=True).start()
        print("  watching for changes — reload the page after a rebuild")
    if args.open:
        webbrowser.open(url)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")
    finally:
        server.server_close()
    return 0


# -- entry point --------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="winged",
        description="Scaffold, build and preview static sites written with Winged-Python.",
    )
    sub = parser.add_subparsers(dest="command")

    new = sub.add_parser("new", help="scaffold a new project")
    new.add_argument("name")
    new.add_argument("--path", help="directory to create (defaults to the name)")
    new.set_defaults(func=cmd_new)

    build = sub.add_parser("build", help="generate the site into dist/")
    build.add_argument("--output", help="output directory (defaults to <project>/dist)")
    build.add_argument("--check-a11y", action="store_true", help="report accessibility findings")
    build.set_defaults(func=cmd_build)

    serve = sub.add_parser("serve", help="preview the generated site")
    serve.add_argument("--port", type=int, default=8000)
    serve.add_argument("--output", help="directory to serve (defaults to <project>/dist)")
    serve.add_argument("--watch", action="store_true", help="rebuild when a source file changes")
    serve.add_argument("--open", action="store_true", help="open a browser")
    serve.set_defaults(func=cmd_serve)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not getattr(args, "func", None):
        # `winged` with no subcommand builds, as WingedSwift's default subcommand does.
        args = parser.parse_args(["build", *(argv or [])])
    func: object = args.func
    assert callable(func)
    return int(func(args))


if __name__ == "__main__":
    raise SystemExit(main())
