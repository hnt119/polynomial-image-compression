"""Released output-first label windows and their shared-edge double triangles.

One fixed family, k in (3,4,5), L=k^3. All scalar and P arithmetic is integral.
No carrier search, floating-point equality, old scout, or package is used.
The command requires both saved proof companions and refuses existing outputs.
"""
import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
import hashlib
import json
from math import isqrt
from pathlib import Path
import platform
import time


CASES = (3, 4, 5)
LIMITS = {"instances": 12, "P_evaluations": 50000,
          "compatibility_checks": 10000}
RUN_DIR = Path("local-only/runs/T01/2026-10-06-variable-gap-sharing")
PORTABLE = Path("examples/2026-10-06-variable-gap-sharing.json")


@dataclass
class Budget:
    limits: dict = field(default_factory=lambda: dict(LIMITS))
    counts: Counter = field(default_factory=Counter)
    categories: Counter = field(default_factory=Counter)

    def charge(self, category, amount=1):
        if amount < 0 or self.counts[category]+amount > self.limits[category]:
            raise RuntimeError(f"Budget exceeded: {category}")
        self.counts[category] += amount

    def check(self, condition, category):
        self.charge("compatibility_checks")
        self.categories[category] += 1
        if not condition:
            raise AssertionError(category)


def evaluate(x, y, budget):
    budget.charge("P_evaluations")
    return (x-y)**3+x+y


def window(k, u):
    """The output labels are prescribed before scalar reconstruction."""
    if k not in CASES or not 1 <= abs(u) <= k:
        raise ValueError("Only the prescribed nonzero-difference windows")
    length = k**3
    return (u**3+abs(u))//2, length-1+(u**3-abs(u))//2


def endpoints(j, u):
    return j-(u**3-u)//2, j-(u**3+u)//2


def canonical_partners(k, a, b):
    """A k+1 vertex block containing the given nonzero controlled edge."""
    length = k**3
    if k not in CASES or not (0 <= a < length and 0 <= b < length
                              and 1 <= abs(a-b) <= k):
        raise ValueError("Not an edge of the declared family")
    start = max(0, max(a, b)-k)
    partners = tuple(c for c in range(start, start+k+1) if c not in (a, b))
    return start, partners


def motif_pairs(a, b, c, d):
    return ((a, b), (b, c), (c, a), (b, d), (d, a))


def analyze(k, budget):
    if k not in CASES:
        raise ValueError("Only k=3,4,5 are released")
    budget.charge("instances")
    length = k**3
    labels, pair_labels, windows = {}, {}, []
    for u in tuple(range(-k, 0))+tuple(range(1, k+1)):
        low, high = window(k, u)
        windows.append({"u": u, "j_min": low, "j_max": high})
        for j in range(low, high+1):
            pair = endpoints(j, u)
            labels[(j, u)] = pair
            pair_labels[pair] = (j, u)
    expected_q = 2*k*length-k*(k+1)
    scalars = sorted({a for pair in pair_labels for a in pair})
    budget.check(scalars == list(range(length)), "actual_scalar_union")
    budget.check(len(labels) == expected_q, "expected_label_count")
    budget.check(len(pair_labels) == len(labels), "no_pair_multiplicity")
    budget.check(set(pair_labels) == set(labels.values()), "label_pair_bijection")
    budget.check(all(1 <= abs(a-b) <= k for a, b in pair_labels), "band_containment")
    # The band has exactly expected_q pairs, so containment and cardinality
    # already prove equality with the full band without a second enumeration.
    prescribed_outputs = {2*j for j, _ in labels}
    expected_z = length+k**3-k
    budget.check(len(prescribed_outputs) == expected_z, "expected_Z")
    output_j = {j for j, _ in labels}
    budget.check(output_j == set(range(-(k**3-k)//2,
                                       length+(k**3-k)//2)), "output_interval")

    # Certify one genuine double triangle on EVERY controlled base edge.
    # All other motif labels are retrieved from the predeclared grid.
    motifs = []
    for a, b in sorted(pair_labels):
        start, partners = canonical_partners(k, a, b)
        c, d = partners[:2]
        pairs = motif_pairs(a, b, c, d)
        for pair in pairs[1:]:
            budget.check(pair in pair_labels, "glued_motif_edge_membership")
        motifs.append({"vertices": [a, b, c, d],
                       "base_label": list(pair_labels[(a, b)]),
                       "block": [start, start+k],
                       "all_block_partners": list(partners),
                       "edge_labels": [list(pair_labels[pair]) for pair in pairs]})
    budget.check(all(len(set(row["vertices"])) == 4 for row in motifs),
                 "all_motifs_nondegenerate")
    budget.check(all(len(row["all_block_partners"]) == k-1 for row in motifs),
                 "uniform_partner_count")
    budget.check(len(motifs) == expected_q, "every_base_edge_has_motif")

    n = len(scalars)
    if budget.counts["P_evaluations"]+n*n > budget.limits["P_evaluations"]:
        raise RuntimeError("Insufficient budget for the complete scalar square")
    fibers, values = defaultdict(list), {}
    for x in scalars:
        for y in scalars:
            z = evaluate(x, y, budget)
            values[(x, y)] = z
            fibers[z].append((x, y))
    for pair, (j, u) in pair_labels.items():
        budget.check(values[pair] == 2*j and pair[0]-pair[1] == u,
                     "prescribed_label_evaluation")
    histogram = Counter(map(len, fibers.values()))
    q, z = len(pair_labels), len(prescribed_outputs)
    budget.check(sum(size*count for size, count in histogram.items()) == n*n,
                 "full_square_pair_mass")
    budget.check(sum(histogram.values()) == len(fibers), "full_image_count")
    budget.check(n == length and q == expected_q and z == expected_z,
                 "N_Q_Z_accounting")
    tails = {str(t): sum(size*count for size, count in histogram.items() if size < t)
             for t in range(1, n+2)}
    sqrt_threshold = isqrt(n)
    if sqrt_threshold**2 < n:
        sqrt_threshold += 1
    selected_sizes = Counter(2*j for j, _ in pair_labels.values())
    endpoint_uses = Counter(a for pair in pair_labels for a in pair)
    summary = {
        "id": f"windows_k{k}", "k": k, "L": length, "N": n,
        "Q": q, "Q_distinct_labels": len(labels), "Z": z, "B": n*n-q,
        "two_Q_over_N": str(Fraction(2*q, n)),
        "Q_over_Z": str(Fraction(q, z)),
        "Q_over_N_squared": str(Fraction(q, n*n)),
        "safe_support_upper_bound": z+n*n-q,
        "full_square": n*n, "full_image": len(fibers),
        "maximum_fiber": max(histogram),
        "fiber_histogram": dict(sorted(histogram.items())),
        "selected_fiber_histogram": dict(sorted(Counter(selected_sizes.values()).items())),
        "strict_small_fiber_tails": tails,
        "sqrt_tail_threshold": sqrt_threshold,
        "sqrt_tail_pair_mass": tails[str(sqrt_threshold)],
        "ranked_fiber_sizes": sorted(map(len, fibers.values()), reverse=True),
        "canonical_double_triangles": len(motifs),
        "minimum_certified_partners_per_base_edge": k-1,
        "canonical_motif_edge_occurrences": 5*len(motifs),
        "canonical_motif_union_pairs": q,
        "endpoint_occurrence_histogram": dict(sorted(Counter(endpoint_uses.values()).items())),
        "poles_or_excluded_pairs": 0,
        "output_label_interval": [min(output_j), max(output_j)],
    }
    worked = motif_pairs(1, 0, 2, 3)
    raw = {
        "summary": summary, "prescribed_windows": windows, "actual_scalars": scalars,
        "labels": [{"j": j, "u": u, "pair": list(pair)}
                   for (j, u), pair in sorted(labels.items())],
        "canonical_double_triangles": motifs,
        "full_fibers": [{"output": output, "pairs": [list(pair) for pair in pairs]}
                        for output, pairs in sorted(fibers.items())],
        "worked_motif": [{"pair": list(pair), "label": list(pair_labels[pair]),
                          "output": values[pair]} for pair in worked],
    }
    return summary, raw


def write_new(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(data, stream, sort_keys=True, indent=2)
        stream.write("\n")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(proof_paths):
    proof_paths = [Path(path) for path in proof_paths]
    if len(proof_paths) != 2 or any(not path.is_file() for path in proof_paths):
        raise FileNotFoundError("Both saved and reviewed proof companions are required")
    destinations = [PORTABLE, RUN_DIR/"experiment-provenance.json"]
    destinations += [RUN_DIR/f"windows_k{k}.json" for k in CASES]
    if any(path.exists() for path in destinations):
        raise FileExistsError("Saved artifact exists; no evaluation performed")
    if sum(k**6 for k in CASES) > LIMITS["P_evaluations"]:
        raise RuntimeError("Planned full squares exceed the fixed budget")
    cpu, wall = time.process_time(), time.perf_counter()
    budget, summaries = Budget(), []
    for k in CASES:
        summary, raw = analyze(k, budget)
        raw_path = RUN_DIR/f"windows_k{k}.json"
        digest = write_new(raw_path, raw)
        summaries.append(dict(summary, raw_path=str(raw_path), raw_sha256=digest))
    inputs = {"k": CASES, "L": "k^3", "u": "integers 1<=abs(u)<=k",
              "j_min": "(u^3+abs(u))/2", "j_max": "L-1+(u^3-abs(u))/2",
              "fixed_polynomial": "(x-y)^3+x+y"}
    portable = {
        "claim_id": "VG-X1", "status": "EXPERIMENTAL", "date": "2026-10-06",
        "inputs": inputs, "models": summaries,
        "scope": "Three prescribed windows in one output-first family; complete actual scalar squares.",
        "limitations": "No new asymptotic inference, exponent improvement, carrier search, or alternative family.",
        "arithmetic": "Exact integers; fractions used only to report ratios.",
    }
    portable_hash = write_new(PORTABLE, portable)
    provenance = {
        "command": "python3 -m experiments.variable_gap_sharing --proofs "+" ".join(map(str, proof_paths)),
        "python": platform.python_version(), "network": "none", "randomness": "none",
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "test_sha256": hashlib.sha256(Path("tests/test_variable_gap_sharing.py").read_bytes()).hexdigest(),
        "input_sha256": hashlib.sha256(json.dumps(inputs, sort_keys=True).encode()).hexdigest(),
        "proofs": [{"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
                   for path in proof_paths],
        "portable_sha256": portable_hash, "limits": LIMITS,
        "charged_counts": dict(budget.counts), "check_categories": dict(budget.categories),
        "cpu_seconds": time.process_time()-cpu, "wall_seconds": time.perf_counter()-wall,
        "errors": [], "scope": "One released run; tests are recorded separately.",
    }
    write_new(RUN_DIR/"experiment-provenance.json", provenance)
    print(json.dumps({"models": [{key: row[key] for key in
          ("k", "N", "Q", "Z", "B", "two_Q_over_N", "Q_over_Z", "Q_over_N_squared",
           "full_image", "fiber_histogram", "sqrt_tail_pair_mass")} for row in summaries],
          "provenance": provenance}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proofs", nargs=2, required=True,
                        help="Saved geometry and construction proofs, reviewed before release")
    arguments = parser.parse_args()
    run(arguments.proofs)
