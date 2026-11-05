"""Bounded exact scouts on a cubic coordinate-sharing elliptic curve.

No imported research programs are executed. Standard-library rational arithmetic
is used throughout; saved runs refuse to overwrite any existing artifact.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from math import isqrt, lcm
from pathlib import Path
import hashlib
import json
import platform
import time

COEFFICIENTS = (F(-48), F(-15424))
BASE = (F(40), F(216))
LIMITS = {"candidates": 12, "P_evaluations": 100000, "curve_checks": 20000}
PREFIXES = {"sharing": (2, 4, 6, 8), "x_progression": (4, 8, 12, 16)}


def on_curve(point):
    if point is None:
        return True
    x, y = point
    a, b = COEFFICIENTS
    return y*y == x*x*x+a*x+b


def add(left, right):
    if left is None:
        return right
    if right is None:
        return left
    x, y = left
    u, v = right
    if x == u and y == -v:
        return None
    slope = (3*x*x+COEFFICIENTS[0])/(2*y) if left == right else (v-y)/(u-x)
    result_x = slope*slope-x-u
    return result_x, slope*(x-result_x)-y


def sharing_pairs(point):
    """Inverse birational map to u^3-v^3-u+v=6; exclude its actual pole."""
    x, y = point
    if x == 4:
        raise ValueError("Pole of the sharing inverse")
    d = F(72)/(x-4)
    w = y*d/216
    u, v = (w+d)/2, (w-d)/2
    a = (6-u**3+u)/2
    b = (6-u**3-u)/2
    shared = (-v**3+v)/2
    e = (-v**3-v)/2
    if a != shared or u**3-v**3-u+v != 6:
        raise AssertionError("Sharing identity")
    return (a, b), (a, e)


def evaluate(x, y):
    return (x-y)**3+x+y


def write_new(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(data, stream, indent=2, sort_keys=True)
        stream.write("\n")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run():
    run_dir = Path("local-only/runs/T01/2026-09-30-elliptic-geometry")
    portable_path = Path("examples/2026-09-30-elliptic-geometry.json")
    planned = [(family, m) for family, values in PREFIXES.items() for m in values]
    names = [f"{family}_{m}" for family, m in planned]
    destinations = [portable_path, run_dir/"experiment-provenance.json"]
    destinations += [run_dir/f"{name}.json" for name in names]
    if any(path.exists() for path in destinations):
        raise FileExistsError("Saved run exists; no evaluations performed")
    if len(planned) > LIMITS["candidates"]:
        raise RuntimeError("Candidate budget")
    cpu, wall = time.process_time(), time.perf_counter()
    checks = Counter()
    points = []
    point = None
    for _ in range(max(max(values) for values in PREFIXES.values())):
        point = add(point, BASE)
        checks["group_law_curve_checks"] += 1
        assert point is not None and on_curve(point)
        points.append(point)
    evaluations = 0
    summaries = []
    for (family, m), name in zip(planned, names):
        selected = {}
        labels = []
        if family == "sharing":
            for point in points[:m]:
                first, second = sharing_pairs(point)
                checks["sharing_inverse_checks"] += 2
                labels += [(first, F(6)), (second, F(0))]
            for pair, z in labels:
                if pair in selected and selected[pair] != z:
                    raise AssertionError("Conflicting output labels")
                selected[pair] = z
            A = sorted({x for pair in selected for x in pair})
        else:
            A = sorted({point[0] for point in points[:m]})
        N = len(A)
        if evaluations+N*N > LIMITS["P_evaluations"]:
            raise RuntimeError("Polynomial budget")
        fibers = defaultdict(list)
        for x in A:
            for y in A:
                z = evaluate(x, y)
                evaluations += 1
                fibers[z].append((x, y))
                if (x, y) in selected:
                    checks["prescribed_output_checks"] += 1
                    assert selected[(x, y)] == z
        histogram = Counter(len(pairs) for pairs in fibers.values())
        assert sum(size*count for size, count in histogram.items()) == N*N
        checks["full_square_accounting"] += 1
        threshold = isqrt(N)
        if threshold*threshold < N:
            threshold += 1
        tails = {str(t): sum(r*c for r, c in histogram.items() if r < t)
                 for t in sorted({2, 3, 4, threshold})}
        sizes = sorted((len(pairs) for pairs in fibers.values()), reverse=True)
        coordinate_counts = Counter(x for pair in selected for x in pair)
        denominator = lcm(*(x.denominator for x in A))
        summary = {
            "id": name, "family": family, "m": m, "N": N,
            "full_image": len(fibers), "full_square": N*N,
            "maximum_fiber": max(sizes), "fiber_histogram": dict(sorted(histogram.items())),
            "ranked_fiber_sizes": sizes, "small_fiber_tails": tails,
            "Q_labels": len(labels), "Q": len(selected), "Z": len(set(selected.values())),
            "B": N*N-len(selected), "selected_coverage": str(F(len(selected), N*N)),
            "selected_mean_coordinate_reuse": str(F(2*len(selected), N)),
            "coordinate_occurrence_histogram": dict(sorted(Counter(coordinate_counts.values()).items())),
            "maximum_scalar_numerator_bits": max(abs(x.numerator).bit_length() for x in A),
            "maximum_scalar_denominator_bits": max(x.denominator.bit_length() for x in A),
            "common_denominator_bits": denominator.bit_length(),
            "poles_or_excluded_labels": 0,
        }
        raw = {
            "summary": summary,
            "points": [[str(x), str(y)] for x, y in points[:m]],
            "scalars": [str(x) for x in A],
            "selected_pairs": [{"pair": list(map(str, pair)), "output": str(z)}
                               for pair, z in sorted(selected.items())],
            "fibers": [{"output": str(z), "pairs": [list(map(str, pair)) for pair in pairs]}
                       for z, pairs in sorted(fibers.items())],
        }
        raw_path = run_dir/f"{name}.json"
        digest = write_new(raw_path, raw)
        summaries.append(dict(summary, raw_path=str(raw_path), raw_sha256=digest))
    if sum(checks.values()) > LIMITS["curve_checks"]:
        raise RuntimeError("Curve check budget")
    portable = {
        "claim_id": "EG-X1", "status": "COMPUTATIONAL", "date": "2026-09-30",
        "polynomial": "(x-y)^3+x+y", "curve": "y^2=x^3-48x-15424",
        "base_point": ["40", "216"], "models": summaries,
        "scope": "Eight selected exact prefixes, with exhaustive enumeration of each actual scalar square.",
        "limitations": "No asymptotic inference or rank computation; extra full-square collisions are measured, not predicted.",
    }
    digest = write_new(portable_path, portable)
    provenance = {
        "command": "python3 -m experiments.elliptic_geometry",
        "python": platform.python_version(), "network": "none", "randomness": "none",
        "input": {"coefficients": list(map(str, COEFFICIENTS)), "base": list(map(str, BASE)), "prefixes": PREFIXES},
        "input_sha256": hashlib.sha256(json.dumps({"coefficients": list(map(str, COEFFICIENTS)), "base": list(map(str, BASE)), "prefixes": PREFIXES}, sort_keys=True).encode()).hexdigest(),
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "portable_sha256": digest, "limits": LIMITS,
        "candidates": len(planned), "P_evaluations": evaluations,
        "curve_checks": dict(checks), "charged_curve_checks": sum(checks.values()),
        "cpu_seconds": time.process_time()-cpu, "wall_seconds": time.perf_counter()-wall,
        "errors": [], "arithmetic": "fractions.Fraction; no floating-point equality",
    }
    write_new(run_dir/"experiment-provenance.json", provenance)
    print(json.dumps({"models": [{k: row[k] for k in ("id", "N", "Q", "Z", "B", "full_image", "maximum_fiber", "fiber_histogram", "small_fiber_tails")} for row in summaries], "provenance": provenance}, indent=2))


if __name__ == "__main__":
    run()

