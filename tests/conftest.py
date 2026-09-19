"""Shared fixtures.

0.1.0's tests defined the same ``MockElement`` helper in four files and captured output by
swapping ``sys.stdout`` for a ``StringIO`` by hand -- which is not exception-safe, so a
failing assertion between the two assignments left stdout redirected for the rest of the
session. Neither is needed now: ``render`` returns the string.
"""

from __future__ import annotations

from pathlib import Path

import pytest

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def fixture() -> object:
    def read(name: str) -> str:
        return (FIXTURES / name).read_text(encoding="utf-8")

    return read
