"""Bounded exact tests of local same-set norm-image certificates.

No floating point or heuristic equality is used. Exhaustive results are
finite statements only; they are not an asymptotic construction.
"""

from fractions import Fraction
import json
from pathlib import Path


def image(E, modulus, linear=0):
    return sorted({(x*x + x*y + y*y + linear*x) % modulus
                   for x in E for y in E})


def exhaustive(modulus, linear=0):
    best = None
    minimizers = 0
    sample = None
    for mask in range(1, 1 << modulus):
        E = [i for i in range(modulus) if mask & (1 << i)]
        S = image(E, modulus, linear)
        ratio = Fraction(modulus * len(S), len(E)**2)
        if best is None or ratio < best:
            best, minimizers, sample = ratio, 1, (E, S)
        elif ratio == best:
            minimizers += 1
    E, S = sample
    return {"modulus": modulus, "linear": linear,
            "sets_checked": (1 << modulus)-1,
            "minimum_ratio": str(best), "minimizer_count": minimizers,
            "sample_E": E, "sample_image": S,
            "input_size": len(E), "output_size": len(S)}


def full_norm_power(p, k):
    modulus = p**k
    E = list(range(modulus))
    S = image(E, modulus)
    if p == 3:
        expected_count = (modulus + 1) // 2
    elif p % 3 == 2:
        expected_count = ((p*modulus + 1) // (p+1) if k % 2 == 0
                          else (p*modulus+p) // (p+1))
    else:
        expected_count = modulus
    assert len(S) == expected_count
    return {"prime": p, "depth": k, "modulus": modulus,
            "E": E, "image": S, "input_size": len(E),
            "output_size": len(S), "proven_formula_count": expected_count,
            "density": str(Fraction(len(S), modulus))}


if __name__ == "__main__":
    data = {
        "description": "Exact local tests; no amplification inferred",
        "exhaustive_good_fields": [exhaustive(p, linear)
                                   for p in (5, 7, 11, 13)
                                   for linear in (0, 1)],
        "exhaustive_small_rings": [exhaustive(m) for m in (2, 3, 4, 8, 9, 16)],
        "full_norm_powers": [full_norm_power(p, k)
                             for p, max_k in ((2, 6), (3, 4), (5, 3))
                             for k in range(1, max_k+1)]
    }
    output = Path(__file__).with_name("Norm_Trace_Exact_Experiments.json")
    output.write_text(json.dumps(data, indent=2) + "\n")
    for row in data["exhaustive_good_fields"] + data["exhaustive_small_rings"]:
        print("modulus", row["modulus"], "linear", row["linear"],
              "minimum", row["minimum_ratio"],
              "sizes", row["input_size"], row["output_size"],
              "minimizers", row["minimizer_count"])
    print("Full norm-power formulas verified in", len(data["full_norm_powers"]), "cases.")
    print(output)
