"""Finite regression checks against the supplied benchmark statements.

A successful run is evidence only for the listed finite instances. It is not
a proof of any universal local-image formula or compression conjecture.
"""

from fractions import Fraction
from math import gcd

from .core import POLYNOMIALS, carrier_image, deform, evaluate, geometric_carrier, local_image


def finite_checks() -> dict:
    checks = []

    def record(name, actual, expected):
        checks.append({"name": name, "passed": actual == expected, "actual": actual, "expected": expected})

    primes = (2, 3, 5, 7, 11, 13)
    for p in primes:
        if p != 2:
            record(f"baseline_original_surjectivity_p{p}", local_image("baseline", p)["image_size"], p)
            for name in ("baseline", "quadratic"):
                record(f"{name}_square_image_p{p}_Q{p}", local_image(name, p, p)["image_size"], (p + 1) // 2)
        record(
            f"quartic_fourth_power_image_p{p}_Q{p}",
            local_image("quartic", p, p)["image_size"],
            1 + (p - 1) // gcd(4, p - 1),
        )
        cubic_expected = 1 if p == 2 else 5 if p == 7 else p
        record(f"mixed_cubic_local_p{p}", local_image("mixed-cubic", p)["image_size"], cubic_expected)

    for base in (3, 4, 5, 10):
        for size in range(9):
            result = carrier_image("mixed-cubic", geometric_carrier(size, base))
            record(f"mixed_cubic_GP_base{base}_N{size}_support", result["image_size"], size * (size + 1) // 2)
            record(f"mixed_cubic_GP_base{base}_N{size}_energy", result["energy"], 2 * size**2 - size)

    for name, metadata in POLYNOMIALS.items():
        for q in (1, 2, 7):
            for x, y in ((-3, 2), (0, 0), (1, -2), (4, 5)):
                expected = q ** metadata["degree"] * evaluate(name, Fraction(x, q), Fraction(y, q))
                record(f"{name}_deformation_Q{q}_x{x}_y{y}", deform(name, x, y, q), expected)

    return {
        "scope": "finite benchmark checks only; not a proof",
        "passed": all(check["passed"] for check in checks),
        "check_count": len(checks),
        "checks": checks,
    }
