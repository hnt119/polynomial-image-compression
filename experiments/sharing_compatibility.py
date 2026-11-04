"""One released directed-triangle strip family, using exact Q*r coefficients.

r = 1/sqrt(3), so P(a*r,b*r)/r = (a-b)^3/3+a+b.  No floats, root
searches, random choices, imported research programs, or additional families.
The command requires a saved compatibility proof and never overwrites data.
"""
import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from fractions import Fraction as F
import hashlib
import json
from math import isqrt
from pathlib import Path
import platform
import time


CASES = (1, 2, 3, 4, 8, 16, 32, 64)
LIMITS = {"instances": 12, "P_evaluations": 50000,
          "compatibility_checks": 10000}
RUN_DIR = Path("local-only/runs/T01/2026-10-06-sharing-compatibility")
PORTABLE_PATH = Path("examples/2026-10-06-sharing-compatibility.json")


@dataclass
class Budget:
    limits: dict = field(default_factory=lambda: dict(LIMITS))
    counts: Counter = field(default_factory=Counter)
    compatibility_categories: Counter = field(default_factory=Counter)

    def charge(self, category, amount=1):
        if amount < 0 or self.counts[category]+amount > self.limits[category]:
            raise RuntimeError(f"Budget exceeded: {category}")
        self.counts[category] += amount

    def check(self, condition, category):
        self.charge("compatibility_checks")
        self.compatibility_categories[category] += 1
        if not condition:
            raise AssertionError(category)


def p_coefficient(a, b, budget):
    """Return the exact coefficient of r, charging before evaluating P."""
    budget.charge("P_evaluations")
    a, b = F(a), F(b)
    return (a-b)**3/3+a+b


def endpoints(z, u):
    """Inverse (z,u) label, with both z and u expressed in units of r."""
    z, u = F(z), F(u)
    total = z-u**3/3
    return (total+u)/2, (total-u)/2


def triangle_compatibility(u, v, w):
    """Three coefficient-form equations for the sole fixed gap h=2*r."""
    u, v, w = F(u), F(v), F(w)
    return (u+v+w == 0,
            (v**3-u**3)/3-u-v == 2,
            2*u+v-v*(u*u+u*v+v*v) == 0)


def strip(m, budget):
    """Deduplicate actual scalar endpoints, pairs and (output,difference) labels."""
    if m not in CASES:
        raise ValueError("Only the eight prescribed strip lengths are allowed")
    selected, labels, triangles = {}, {}, []
    for j in range(1, m+1):
        vertices = (F(j-1), F(j), F(j+1))
        pairs = tuple(zip(vertices, vertices[1:]+vertices[:1]))
        z0 = 2*j-F(4, 3)
        outputs = tuple(z0+2*i for i in range(3))
        differences = tuple(a-b for a, b in pairs)
        for condition in triangle_compatibility(*differences):
            budget.check(condition, "triangle_equations")
        for pair, z, u in zip(pairs, outputs, differences):
            label = (z, u)
            budget.check(endpoints(*label) == pair, "label_inverse")
            budget.check(pair not in selected or selected[pair] == z,
                         "pair_overlap_consistency")
            budget.check(label not in labels or labels[label] == pair,
                         "label_overlap_consistency")
            selected[pair] = z
            labels[label] = pair
        triangles.append({"j": j, "vertices": list(map(str, vertices)),
                          "outputs": list(map(str, outputs)),
                          "differences": list(map(str, differences))})
    scalars = sorted({x for pair in selected for x in pair})
    budget.check(len(scalars) == m+2, "expected_N")
    budget.check(len(selected) == 2*m+1, "expected_Q")
    budget.check(len(set(selected.values())) == m+2, "expected_Z")
    budget.check(len(labels) == len(selected), "label_pair_bijection")
    budget.check(set(labels.values()) == set(selected), "same_labeled_pairs")
    budget.check(all(a-b in (F(-1), F(2)) for a, b in selected),
                 "allowed_directed_differences")
    budget.check(len(selected) == 2*len(scalars)-3, "sharp_linear_coverage")
    return scalars, selected, labels, triangles


def analyze(m, budget):
    if m not in CASES:
        raise ValueError("Only the eight prescribed strip lengths are allowed")
    budget.charge("instances")
    scalars, selected, labels, triangles = strip(m, budget)
    n = len(scalars)
    if budget.counts["P_evaluations"]+n*n > budget.limits["P_evaluations"]:
        raise RuntimeError("Insufficient budget for the entire scalar square")
    fibers = defaultdict(list)
    full_values = {}
    for a in scalars:
        for b in scalars:
            z = p_coefficient(a, b, budget)
            fibers[z].append((a, b))
            full_values[(a, b)] = z
    for pair, z in selected.items():
        budget.check(full_values[pair] == z, "prescribed_outputs")
    histogram = Counter(map(len, fibers.values()))
    budget.check(sum(size*count for size, count in histogram.items()) == n*n,
                 "full_square_pair_mass")
    budget.check(sum(histogram.values()) == len(fibers), "full_image_histogram")
    budget.check(len(full_values) == n*n, "full_square_unique_pairs")
    budget.check(n*n-len(selected) == (m+2)**2-(2*m+1), "expected_B")
    band = min(n-1, isqrt(6*(n-1)))
    for pairs in fibers.values():
        if len(pairs) > 1:
            for a, b in pairs:
                budget.check(abs(a-b) <= band, "nonsingleton_difference_band")
    guaranteed_singletons = (n-band)*(n-band-1)
    budget.check(histogram[1] >= guaranteed_singletons, "singleton_lower_bound")
    # Strict tails B_A(t)=sum_{r(z)<t} r(z), for every integer t in range.
    tails = {str(t): sum(size*count for size, count in histogram.items() if size < t)
             for t in range(1, n+2)}
    sqrt_threshold = isqrt(n)
    if sqrt_threshold**2 < n:
        sqrt_threshold += 1
    coordinate_occurrences = Counter(x for pair in selected for x in pair)
    selected_histogram = Counter(Counter(selected.values()).values())
    summary = {
        "id": f"strip_m{m}", "m": m, "N": n,
        "raw_triangle_labels": 3*m, "Q_distinct_labels": len(labels),
        "Q": len(selected), "Z": len(set(selected.values())),
        "B": n*n-len(selected), "full_square": n*n,
        "safe_support_upper_bound": len(set(selected.values()))+n*n-len(selected),
        "full_image": len(fibers), "maximum_fiber": max(histogram),
        "fiber_histogram": dict(sorted(histogram.items())),
        "selected_fiber_histogram": dict(sorted(selected_histogram.items())),
        "ranked_fiber_sizes": sorted(map(len, fibers.values()), reverse=True),
        "strict_small_fiber_tails": tails,
        "sqrt_tail_threshold": sqrt_threshold,
        "sqrt_tail_pair_mass": tails[str(sqrt_threshold)],
        "nonsingleton_difference_band": band,
        "guaranteed_singleton_pairs": guaranteed_singletons,
        "nonsingleton_pair_mass": sum(size*count for size, count in histogram.items() if size > 1),
        "selected_coverage": str(F(len(selected), n*n)),
        "mean_selected_coordinate_occurrences": str(F(2*len(selected), n)),
        "coordinate_occurrence_histogram": dict(sorted(Counter(coordinate_occurrences.values()).items())),
        "poles_or_excluded_labels": 0,
        "coefficient_interval": ["0", str(m+1)],
    }
    raw = {
        "summary": summary, "scalars_in_units_r": list(map(str, scalars)),
        "triangles": triangles,
        "distinct_labels": [{"z": str(z), "u": str(u),
                             "pair": list(map(str, pair))}
                            for (z, u), pair in sorted(labels.items())],
        "selected_pairs": [{"pair": list(map(str, pair)), "output": str(z)}
                           for pair, z in sorted(selected.items())],
        "fibers": [{"output": str(z), "pairs": [list(map(str, pair)) for pair in pairs]}
                   for z, pairs in sorted(fibers.items())],
    }
    if m <= 2:
        raw["worked_matrix_3P_over_r"] = [
            [str(3*full_values[(a, b)]) for b in scalars] for a in scalars]
    return summary, raw


def write_new(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(data, stream, sort_keys=True, indent=2)
        stream.write("\n")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(proof_path):
    """Call only after the lead releases the saved compatibility proof."""
    proof_path = Path(proof_path)
    if not proof_path.is_file():
        raise FileNotFoundError("A saved, reviewed compatibility proof is required")
    destinations = [PORTABLE_PATH, RUN_DIR/"experiment-provenance.json"]
    destinations += [RUN_DIR/f"strip_m{m}.json" for m in CASES]
    if any(path.exists() for path in destinations):
        raise FileExistsError("Existing saved artifact; no evaluations performed")
    if len(CASES) > LIMITS["instances"] or sum((m+2)**2 for m in CASES) > LIMITS["P_evaluations"]:
        raise RuntimeError("Planned run exceeds the fixed budget")
    cpu, wall = time.process_time(), time.perf_counter()
    budget, summaries = Budget(), []
    for m in CASES:
        summary, raw = analyze(m, budget)
        raw_path = RUN_DIR/f"strip_m{m}.json"
        digest = write_new(raw_path, raw)
        summaries.append(dict(summary, raw_path=str(raw_path), raw_sha256=digest))
    inputs = {"cases": CASES, "r_squared": "1/3", "gap_in_units_r": "2",
              "triangle": "(j-1,j,j+1), j=1,...,m; coordinates in units r"}
    portable = {
        "claim_id": "SH-X1", "status": "EXPERIMENTAL", "date": "2026-10-06",
        "polynomial": "(x-y)^3+x+y", "inputs": inputs,
        "arithmetic": "Exact rational coefficients of r=1/sqrt(3), with r^3=r/3",
        "models": summaries,
        "scope": "Exactly eight prescribed lengths of one strip family; exhaustive actual A^2 for each.",
        "limitations": "Finite checks do not prove an asymptotic image or fiber-tail theorem.",
    }
    portable_digest = write_new(PORTABLE_PATH, portable)
    provenance = {
        "command": f"python3 -m experiments.sharing_compatibility --compatibility-proof {proof_path}",
        "python": platform.python_version(), "network": "none", "randomness": "none",
        "input_sha256": hashlib.sha256(json.dumps(inputs, sort_keys=True).encode()).hexdigest(),
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "test_sha256": hashlib.sha256(Path("tests/test_sharing_compatibility.py").read_bytes()).hexdigest(),
        "compatibility_proof_path": str(proof_path),
        "compatibility_proof_sha256": hashlib.sha256(proof_path.read_bytes()).hexdigest(),
        "portable_sha256": portable_digest, "limits": LIMITS,
        "charged_counts": dict(budget.counts),
        "compatibility_categories": dict(budget.compatibility_categories),
        "cpu_seconds": time.process_time()-cpu, "wall_seconds": time.perf_counter()-wall,
        "errors": [], "arithmetic": "fractions.Fraction; no floating-point equality",
        "regression_scope": "The new unit tests are charged separately; no hidden test run occurs here.",
    }
    write_new(RUN_DIR/"experiment-provenance.json", provenance)
    print(json.dumps({"models": [{k: row[k] for k in
          ("m", "N", "Q", "Z", "B", "full_image", "maximum_fiber", "fiber_histogram")}
          for row in summaries], "provenance": provenance}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compatibility-proof", required=True,
                        help="Saved proof file, independently reviewed before execution")
    arguments = parser.parse_args()
    run(arguments.compatibility_proof)
