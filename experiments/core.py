"""Small standard-library computations using integers and exact fractions."""

from collections import Counter
from fractions import Fraction
from math import isqrt
from typing import Iterable


POLYNOMIALS = {
    "baseline": {"degree": 2, "expression": "(x-y)^2+x+y"},
    "quadratic": {"degree": 2, "expression": "(x+2y)^2+3x-y"},
    "quartic": {"degree": 4, "expression": "(x+2y)^4+3x-y"},
    "mixed-cubic": {"degree": 3, "expression": "xy(x+y)"},
    "eisenstein": {"degree": 2, "expression": "x^2+xy+y^2"},
}


def _integer(value: int, label: str) -> int:
    if type(value) is not int:
        raise ValueError(f"{label} must be an integer")
    return value


def _polynomial(name: str) -> None:
    if name not in POLYNOMIALS:
        raise ValueError(f"unknown polynomial: {name!r}")


def _positive_q(q: int) -> int:
    _integer(q, "q")
    if q < 1:
        raise ValueError("q must be positive")
    return q


def evaluate(name: str, x: int | Fraction, y: int | Fraction) -> int | Fraction:
    """Evaluate a fixed polynomial exactly; floats and booleans are rejected."""
    _polynomial(name)
    if any(type(value) not in (int, Fraction) for value in (x, y)):
        raise ValueError("coordinates must be integers or fractions")
    if name == "baseline":
        return (x - y) ** 2 + x + y
    if name == "quadratic":
        return (x + 2 * y) ** 2 + 3 * x - y
    if name == "quartic":
        return (x + 2 * y) ** 4 + 3 * x - y
    if name == "mixed-cubic":
        return x * y * (x + y)
    return x * x + x * y + y * y


def deform(name: str, x: int, y: int, q: int = 1) -> int:
    """Compute F_Q(x,y) = Q^m P(x/Q,y/Q) by integer expressions.

    Here m is the total degree. The homogeneous mixed cubic and Eisenstein
    quadratic are unchanged. No divisions or floating-point operations occur.
    """
    _polynomial(name)
    _integer(x, "x")
    _integer(y, "y")
    _positive_q(q)
    if name == "baseline":
        return (x - y) ** 2 + q * (x + y)
    if name == "quadratic":
        return (x + 2 * y) ** 2 + q * (3 * x - y)
    if name == "quartic":
        return (x + 2 * y) ** 4 + q**3 * (3 * x - y)
    return evaluate(name, x, y)


def is_prime(p: int) -> bool:
    """Trial division suffices for the deliberately small CLI inputs."""
    if type(p) is not int or p < 2:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    return all(p % divisor for divisor in range(3, isqrt(p) + 1, 2))


def local_image(name: str, p: int, q: int = 1) -> dict:
    """Enumerate the full image of F_Q on F_p x F_p.

    Density means |image|/p, not |image|/p^2. Returned fractions are exact
    Fraction instances; the CLI encodes them as numerator/denominator objects.
    """
    _polynomial(name)
    _positive_q(q)
    if not is_prime(p):
        raise ValueError("p must be prime")
    residues = sorted({deform(name, x, y, q) % p for x in range(p) for y in range(p)})
    return {
        "polynomial": name,
        "degree": POLYNOMIALS[name]["degree"],
        "prime": p,
        "q": q,
        "input_count": p**2,
        "image_size": len(residues),
        "density": Fraction(len(residues), p),
        "image": residues,
    }


def arithmetic_carrier(size: int, start: int = 0, step: int = 1) -> tuple[int, ...]:
    """Return a set represented as a tuple: start + step*i, 0 <= i < size."""
    _integer(size, "size")
    _integer(start, "start")
    _integer(step, "step")
    if size < 0:
        raise ValueError("size must be nonnegative")
    if step == 0:
        raise ValueError("step must be nonzero")
    return tuple(start + step * i for i in range(size))


def geometric_carrier(size: int, base: int = 3) -> tuple[int, ...]:
    """Return (1, base, ..., base^(size-1)); size=0 returns the empty set.

    Bases >=2 give distinct positive powers. The mixed-cubic benchmark in the
    supplied research reference assumes base >=3.
    """
    _integer(size, "size")
    _integer(base, "base")
    if size < 0:
        raise ValueError("size must be nonnegative")
    if base < 2:
        raise ValueError("base must be at least 2")
    return tuple(base**i for i in range(size))


def carrier_image(name: str, values: Iterable[int], q: int = 1) -> dict:
    """Enumerate F_Q(A,A), preserving the same set in both input coordinates.

    Repeated elements in values are deduplicated, as A is a set. E is the
    number of ordered collisions, sum_t r(t)^2. The Cauchy-Schwarz lower bound
    n^4/E and the normalized support |F_Q(A,A)|/n^2 are returned as fractions.
    For A empty, both ratios are None (undefined), and support and energy are 0.
    """
    _polynomial(name)
    _positive_q(q)
    checked = [_integer(value, "carrier element") for value in values]
    carrier = sorted(set(checked))
    counts = Counter(deform(name, x, y, q) for x in carrier for y in carrier)
    size = len(carrier)
    energy = sum(count**2 for count in counts.values())
    return {
        "polynomial": name,
        "q": q,
        "carrier_size": size,
        "input_count": size**2,
        "image_size": len(counts),
        "energy": energy,
        "image_lower_bound": Fraction(size**4, energy) if energy else None,
        "normalized_support_ratio": Fraction(len(counts), size**2) if size else None,
    }
