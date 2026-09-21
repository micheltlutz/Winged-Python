"""Everything, for a generator script.

    from winged.prelude import *

Mirrors winged-rust's ``prelude`` module. Bounded by :data:`winged.__all__`, so this is a
safe star-import rather than a wildcard over the whole package.
"""

from __future__ import annotations

from winged import *  # noqa: F403
from winged import __all__ as __all__
