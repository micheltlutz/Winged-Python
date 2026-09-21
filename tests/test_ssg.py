"""Ports Tests/WingedSwiftTests/StaticSiteGeneratorTests.swift."""

from __future__ import annotations

from pathlib import Path

import pytest

from winged import H1, Body, Document, Head
from winged.ssg import StaticSiteGenerator


def page() -> Document:
    return Document(Head(), Body(H1("Hi")))


def test_intermediate_directories_are_created(tmp_path: Path) -> None:
    site = StaticSiteGenerator(tmp_path)
    site.generate(page(), "a/b/c.html")
    assert (tmp_path / "a" / "b" / "c.html").is_file()


def test_output_uses_unix_line_endings(tmp_path: Path) -> None:
    site = StaticSiteGenerator(tmp_path)
    site.generate(page(), "index.html")
    assert b"\r\n" not in (tmp_path / "index.html").read_bytes()


def test_generate_multiple(tmp_path: Path) -> None:
    StaticSiteGenerator(tmp_path).generate_multiple({"a.html": page(), "b.html": page()})
    assert (tmp_path / "a.html").is_file() and (tmp_path / "b.html").is_file()


def test_clean_empties_the_directory(tmp_path: Path) -> None:
    (tmp_path / "old.html").write_text("x")
    (tmp_path / "sub").mkdir()
    StaticSiteGenerator(tmp_path).clean()
    assert list(tmp_path.iterdir()) == []


def test_clean_refuses_the_filesystem_root() -> None:
    with pytest.raises(ValueError, match="refusing to clean"):
        StaticSiteGenerator("/").clean()


def test_clean_refuses_the_home_directory() -> None:
    with pytest.raises(ValueError, match="refusing to clean"):
        StaticSiteGenerator(Path.home()).clean()


def test_writing_outside_the_output_directory_is_refused(tmp_path: Path) -> None:
    site = StaticSiteGenerator(tmp_path / "dist")
    with pytest.raises(ValueError, match="outside the output directory"):
        site.write_file("x", "../escaped.html")


def test_copy_asset(tmp_path: Path) -> None:
    source = tmp_path / "style.css"
    source.write_text("body{}")
    site = StaticSiteGenerator(tmp_path / "dist")
    site.copy_asset(source, "css/style.css")
    assert (tmp_path / "dist" / "css" / "style.css").read_text() == "body{}"
