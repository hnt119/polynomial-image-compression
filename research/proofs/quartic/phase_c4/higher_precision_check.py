#!/usr/bin/env python3
"""Exact, offline mixed-characteristic check of the critical P4 image.

The ring is (Z/7^m Z)[pi]/(pi^3-7u), u=1,2,4.  No floating point,
randomness, symbolic algebra system, or characteristic-seven surrogate is
used.  The analytic proof is independent of this program.
"""

import argparse
import hashlib
import itertools
import json
from pathlib import Path


class Ring:
    def __init__(self, m, u):
        self.m = m
        self.u = u
        self.mod = 7 ** m

    def add(self, a, b):
        q = self.mod
        return tuple((x + y) % q for x, y in zip(a, b))

    def scale(self, a, c):
        q = self.mod
        return tuple(c * x % q for x in a)

    def mul(self, a, b):
        a0, a1, a2 = a
        b0, b1, b2 = b
        q, t = self.mod, 7 * self.u
        return ((a0*b0 + t*(a1*b2 + a2*b1)) % q,
                (a0*b1 + a1*b0 + t*a2*b2) % q,
                (a0*b2 + a1*b1 + a2*b0) % q)

    def fourth(self, a):
        aa = self.mul(a, a)
        return self.mul(aa, aa)

    def polynomial(self, x, y):
        linear = self.add(x, self.scale(y, 2))
        return self.add(self.fourth(linear),
                        self.add(self.scale(x, 3), self.scale(y, -1)))

    def twice_in_coordinates(self, linear, x):
        return self.add(self.add(self.scale(self.fourth(linear), 2),
                                  self.scale(linear, -1)),
                        self.scale(x, 7))

    def encode(self, a):
        return a[0] + self.mod*a[1] + self.mod*self.mod*a[2]


def fiber(ring, residue):
    q = ring.mod
    for a0 in range(residue % 7, q, 7):
        for a1 in range(q):
            for a2 in range(q):
                yield (a0, a1, a2)


def fourth_ideal_class(a):
    # pi^4 O = 7pi O; its coefficient conditions are
    # c0 divisible by 49 and c1,c2 divisible by 7.
    return (a[0] % 49, a[1] % 7, a[2] % 7)


def check_model(u, a):
    first = Ring(1, u)
    inputs = list(fiber(first, a))
    actual_one = {first.polynomial(x, y) for x in inputs for y in inputs}
    assert len(actual_one) == 4

    second = Ring(2, u)
    representatives = {}
    count_linear = 0
    identity_checks = 0
    for linear in fiber(second, 3*a):
        count_linear += 1
        val = second.twice_in_coordinates(linear, (a, 0, 0))
        representatives.setdefault(fourth_ideal_class(val), linear)
        # Deterministic distinct x choices check the original polynomial
        # separately from the coordinate formula throughout the L sweep.
        if count_linear % 127 == 1:
            x = ((a + 7*(count_linear % 7)) % 49,
                 count_linear % 49, (3*count_linear + 1) % 49)
            y = second.scale(second.add(linear, second.scale(x, -1)),
                             pow(2, -1, 49))
            assert x[0] % 7 == a % 7 == y[0] % 7
            assert second.scale(second.polynomial(x, y), 2) == \
                second.twice_in_coordinates(linear, x)
            identity_checks += 1
    assert count_linear == 7**5
    assert len(representatives) == 22

    precision_rows = []
    for m in (2, 3):
        ring = Ring(m, u)
        q = ring.mod
        actual_outputs = set()
        shifts = list(itertools.product(range(q//49),
                                        range(q//7), range(q//7)))
        for linear in representatives.values():
            base = ring.twice_in_coordinates(linear, (a, 0, 0))
            for t0, t1, t2 in shifts:
                # This is the original image value multiplied by two,
                # using the actual input x=(a+7t0,t1,t2) and
                # y=(L-x)/2.  Two is a unit, so cardinality is unchanged.
                val = ((base[0] + 49*t0) % q,
                       (base[1] + 7*t1) % q,
                       (base[2] + 7*t2) % q)
                actual_outputs.add(ring.encode(val))
        expected = 22 * 7**(3*m-4)
        assert len(actual_outputs) == expected
        precision_rows.append({
            "m": m,
            "constructed_distinct_actual_outputs": len(actual_outputs),
            "number_of_full_pi4_classes": len(representatives),
            "size_per_pi4_class": len(shifts),
            "N_m": expected,
            "upper_bound_basis": (
                "all admissible L enumerated modulo 49; pi4 class "
                "invariance and saturation proved analytically"),
            "cartesian_input_square_enumerated": False,
        })

    serialized_classes = json.dumps(sorted(representatives),
                                    separators=(",", ":")).encode()
    return {
        "u": u,
        "critical_residue_a": a,
        "m1_ordered_pairs_checked": len(inputs)**2,
        "m1_exact_image_count": len(actual_one),
        "m2_admissible_L_values_enumerated": count_linear,
        "original_polynomial_coordinate_identity_checks": identity_checks,
        "pi4_image_classes_for_twice_P": sorted(representatives),
        "pi4_classes_sha256": hashlib.sha256(serialized_classes).hexdigest(),
        "higher_precision": precision_rows,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path("phase_c4/higher_precision_results.json"))
    args = parser.parse_args()
    result = {
        "schema_version": 1,
        "ring_model": "(Z/7^m Z)[pi]/(pi^3-7u)",
        "twists": [1, 2, 4],
        "critical_residues": [3, 5, 6],
        "formula": {"N_1": 4, "N_m_for_m_ge_2": "22*7^(3*m-4)",
                    "N_2": 1078, "N_3": 369754,
                    "higher_to_neutral_scale_ratio": [11, 14],
                    "input_costed_local_factor_m_ge_2": [22, 49]},
        "scope": (
            "m1 exhaustive ordered input pairs; m2 exhaustive L coordinate "
            "plus full pi4-ideal saturation; m3 explicit actual output "
            "construction plus analytic upper bound, not exhaustive pairs"),
        "models": [check_model(u, a) for u in (1, 2, 4)
                   for a in (3, 5, 6)],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"models_checked": len(result["models"]),
                      "N_1": 4, "N_2": 1078, "N_3": 369754,
                      "output": str(args.output)}, sort_keys=True))


if __name__ == "__main__":
    main()
