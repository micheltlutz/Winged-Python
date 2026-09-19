"""Ports WingedCLITests/{NewCommandTests,ScaffolderTests,BuildCommandTests,HTTPServerTests}."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

from winged.cli import _Handler, build_parser, find_project_root, main


def scaffold(tmp_path: Path, name: str = "demo") -> Path:
    target = tmp_path / name
    assert main(["new", name, "--path", str(target)]) == 0
    return target


def test_new_scaffolds_every_file(tmp_path: Path) -> None:
    target = scaffold(tmp_path)
    for expected in ("site.py", "layout.py", "assets/css/style.css", ".gitignore", "AGENTS.md"):
        assert (target / expected).is_file(), expected


def test_new_scaffolds_an_agents_file(tmp_path: Path) -> None:
    # WingedSwift's `new` scaffolds one too: a generated project should be workable by a
    # coding agent from its first commit.
    assert "winged build" in (scaffold(tmp_path) / "AGENTS.md").read_text()


def test_new_refuses_a_non_empty_directory(tmp_path: Path) -> None:
    target = tmp_path / "demo"
    target.mkdir()
    (target / "keep.txt").write_text("x")
    assert main(["new", "demo", "--path", str(target)]) == 1


def test_generated_project_builds_from_the_filesystem_root(tmp_path: Path) -> None:
    # The failure this guards against: a generator that resolves paths from the current
    # directory passes every unit test and still fails for the user.
    target = scaffold(tmp_path)
    result = subprocess.run(
        [sys.executable, str(target / "site.py")],
        cwd="/",
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert (target / "dist" / "index.html").is_file()
    assert (target / "dist" / "css" / "style.css").is_file()
    assert (target / "dist" / "sitemap.xml").is_file()


def test_find_project_root_walks_up(tmp_path: Path) -> None:
    target = scaffold(tmp_path)
    nested = target / "a" / "b"
    nested.mkdir(parents=True)
    assert find_project_root(nested) == target.resolve()


def test_find_project_root_without_a_project(tmp_path: Path) -> None:
    with pytest.raises(SystemExit, match=r"no site\.py"):
        find_project_root(tmp_path)


@pytest.mark.parametrize(
    ("suffix", "expected"),
    [(".css", "text/css"), (".woff2", "font/woff2"), (".svg", "image/svg+xml")],
)
def test_mime_types(suffix: str, expected: str) -> None:
    # mimetypes guesses several of these wrong, or not at all, depending on the platform.
    handler = _Handler.__new__(_Handler)
    assert handler.guess_type(f"x{suffix}") == expected


@pytest.mark.parametrize(
    "attack", ["/../secret.txt", "/..%2fsecret.txt", "/a/../../secret.txt", "/./../secret.txt"]
)
def test_dot_dot_never_escapes_the_served_directory(tmp_path: Path, attack: str) -> None:
    root = tmp_path / "dist"
    root.mkdir()
    (tmp_path / "secret.txt").write_text("nope")

    handler = _Handler.__new__(_Handler)
    handler.directory = str(root)
    translated = Path(handler.translate_path(attack)).resolve()

    assert translated.is_relative_to(root.resolve())
    assert not translated.exists()  # so the request 404s rather than serving anything


def test_a_symlink_out_of_the_served_directory_is_not_followed(tmp_path: Path) -> None:
    root = tmp_path / "dist"
    root.mkdir()
    secret = tmp_path / "secret.txt"
    secret.write_text("nope")
    (root / "link.txt").symlink_to(secret)

    handler = _Handler.__new__(_Handler)
    handler.directory = str(root)
    translated = Path(handler.translate_path("/link.txt"))

    assert translated.name == "__forbidden__"
    assert not translated.exists()


def test_parser_exposes_the_three_commands() -> None:
    parser = build_parser()
    for command in ("new", "build", "serve"):
        assert parser.parse_args([command] if command != "new" else [command, "x"])


def test_build_writes_dist_and_reports_files(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    target = scaffold(tmp_path)
    monkeypatch.chdir(target)
    assert main(["build"]) == 0

    out = capsys.readouterr().out
    assert "index.html" in out and "total" in out
    assert (target / "dist" / "index.html").is_file()


def test_build_from_a_subdirectory_writes_to_the_project_dist(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    target = scaffold(tmp_path)
    nested = target / "a" / "b"
    nested.mkdir(parents=True)
    monkeypatch.chdir(nested)

    assert main(["build"]) == 0
    assert (target / "dist" / "index.html").is_file()
    assert not (nested / "dist").exists()


def test_build_with_the_a11y_flag(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    target = scaffold(tmp_path)
    monkeypatch.chdir(target)
    assert main(["build", "--check-a11y"]) == 0
    assert "check-a11y" in capsys.readouterr().out


def test_no_subcommand_builds(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    # WingedSwift makes `build` the default subcommand; so does this.
    target = scaffold(tmp_path)
    monkeypatch.chdir(target)
    assert main([]) == 0
    assert (target / "dist" / "index.html").is_file()


def test_serve_without_a_build_fails_clearly(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    target = scaffold(tmp_path)
    monkeypatch.chdir(target)
    assert main(["serve"]) == 1
    assert "winged build" in capsys.readouterr().err


def test_serve_reports_an_occupied_port(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    import socket

    target = scaffold(tmp_path)
    monkeypatch.chdir(target)
    main(["build"])

    holder = socket.socket()
    holder.bind(("127.0.0.1", 0))
    holder.listen(1)
    port = holder.getsockname()[1]
    try:
        assert main(["serve", "--port", str(port)]) == 1
        assert f"cannot bind port {port}" in capsys.readouterr().err
    finally:
        holder.close()
