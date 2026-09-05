"""Exact, finite experiments for polynomial images on the same input set.

These computations check finite examples; they do not establish asymptotic
compression results or certify any mathematical proof.
"""

from .core import (
    POLYNOMIALS,
    arithmetic_carrier,
    carrier_image,
    deform,
    evaluate,
    geometric_carrier,
    local_image,
)

__all__ = [
    "POLYNOMIALS",
    "arithmetic_carrier",
    "carrier_image",
    "deform",
    "evaluate",
    "geometric_carrier",
    "local_image",
]
