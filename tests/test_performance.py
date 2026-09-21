"""A regression guard, not a benchmark.

Ports ``Winged-Swift/Tests/WingedSwiftTests/RenderPerformanceTests.swift``.

What it guards against is a return to per-node string concatenation, which is quadratic
and is exactly what 0.1.0's ``get_string()`` did -- every node built a new string from its
children's strings. The bound is generous on purpose: CI runners vary, and a flaky
performance test gets disabled, which is worse than not having one.
"""

from __future__ import annotations

import time

from winged import RenderOptions, Table, Tbody, Td, Tr, render


def big_table(rows: int = 1500) -> Table:
    return Table(Tbody(*(Tr(Td(str(n)), Td("x"), Td("y"), Td("z")) for n in range(rows))))


def test_rendering_a_large_tree_stays_linear() -> None:
    tree = big_table()
    start = time.perf_counter()
    out = render(tree)
    elapsed = time.perf_counter() - start

    assert elapsed < 2.0, f"rendering took {elapsed:.2f}s"
    # A render that got fast by producing less is not a pass.
    assert out.startswith("<table><tbody><tr><td>0</td>")
    assert out.endswith("</tr></tbody></table>")
    assert len(out) > 70_000


def test_pretty_rendering_also_completes() -> None:
    start = time.perf_counter()
    out = render(big_table(500), RenderOptions.pretty_())
    assert time.perf_counter() - start < 2.0
    assert out.count("<td>") == 2000
