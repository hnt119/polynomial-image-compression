"""Exact, bounded all-pair completion scouts and full fiber-coverage diagnostics.

This module runs only when explicitly invoked. It never imports or reruns an
older research grid. All equalities use Fraction, and writers reject overwrites.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations
from math import isqrt, lcm
from pathlib import Path
import hashlib
import json
import platform
import time

LIMITS = {"carriers": 24, "N": 128, "P_evaluations": 200000, "checks": 2000000}
SEEDS = (("third_half", (F(0), F(1, 3), F(1, 2))),
         ("quarter_one", (F(0), F(1, 4), F(1))))
MODES = ("adaptive_linear", "adaptive_quadratic", "mobius_threecycle")


class Budget:
    def __init__(self):
        self.P_evaluations = 0
        self.checks = Counter()

    def charge(self, category, amount=1):
        self.checks[category] += amount
        if sum(self.checks.values()) > LIMITS["checks"]:
            raise RuntimeError("Exact check budget exceeded")

    def polynomial(self, x, y):
        if self.P_evaluations >= LIMITS["P_evaluations"]:
            raise RuntimeError("Polynomial budget exceeded")
        self.P_evaluations += 1
        return (x-y)**3+x+y


def pair_at(u, z):
    u, z = F(u), F(z)
    return ((z-u**3+u)/2, (z-u**3-u)/2)


def build_completion(seed, mode, budget):
    """Three charts on the entire old square; all poles are recorded."""
    seed = tuple(sorted(set(map(F, seed))))
    if mode not in MODES:
        raise ValueError(mode)
    labels = []
    poles = []
    for i, x in enumerate(seed):
        for j, y in enumerate(seed):
            u, z = x-y, budget.polynomial(x, y)
            labels.append((0, i, j, (x, y), z))
            budget.charge("constructor_labels")
            if mode == "mobius_threecycle":
                if u in (0, 1):
                    poles.append((i, j, str(u)))
                    continue
                differences = (1-1/u, 1/(1-u))
            else:
                step = z/2 if mode == "adaptive_linear" else z*z/2
                differences = (u+step, u-step)
            for branch, v in enumerate(differences, 1):
                labels.append((branch, i, j, pair_at(v, z), z))
                budget.charge("constructor_labels")
    return seed, labels, poles


def full_fibers(A, budget):
    A = tuple(sorted(set(map(F, A))))
    if len(A) > LIMITS["N"]:
        raise RuntimeError("Scalar cap exceeded before square enumeration")
    if budget.P_evaluations + len(A)**2 > LIMITS["P_evaluations"]:
        raise RuntimeError("Polynomial cap exceeded before square enumeration")
    fibers = defaultdict(list)
    pair_output = {}
    for x in A:
        for y in A:
            z = budget.polynomial(x, y)
            fibers[z].append((x, y))
            pair_output[(x, y)] = z
    return dict(fibers), pair_output


def coverage_profile(fibers, N):
    """No polynomial evaluations: exact ranked fibers and all cumulative counts."""
    ordered = sorted(fibers, key=lambda z: (-len(fibers[z]), z))
    sizes = [len(fibers[z]) for z in ordered]
    cumulative = [0]
    for r in sizes:
        cumulative.append(cumulative[-1]+r)
    total = N*N
    if cumulative[-1] != total:
        raise ValueError("Incomplete Cartesian square")
    k = min(len(sizes), isqrt(N**3))
    budgets = {
        "floor_N_to_3_over_2": {"k": k, "Q": cumulative[k],
                               "Z": k, "B": total-cumulative[k],
                               "safe_bound": k+total-cumulative[k]}
    }
    targets = {}
    for numerator, denominator in ((1, 2), (9, 10), (99, 100), (1, 1)):
        target = (numerator*total+denominator-1)//denominator
        index = next(i for i, value in enumerate(cumulative) if value >= target)
        targets[f"{numerator}/{denominator}"] = {
            "k": index, "Q": cumulative[index], "B": total-cumulative[index]}
    threshold = isqrt(N)
    if threshold*threshold < N:
        threshold += 1
    tails = {}
    for t in sorted({2, 3, 4, threshold}):
        bad = sum(r for r in sizes if r < t)
        large = sum(r >= t for r in sizes)
        tails[str(t)] = {"B": bad, "Q": total-bad, "Z": large,
                         "safe_bound": bad+large}
    hierarchy = []
    start = 0
    while cumulative[start] < total:
        remaining = total-cumulative[start]
        required = cumulative[start]+(remaining+1)//2
        end = start+1
        while cumulative[end] < required:
            end += 1
        hierarchy.append({
            "stage": len(hierarchy)+1,
            "new_outputs": end-start,
            "new_pairs": cumulative[end]-cumulative[start],
            "cumulative_outputs": end,
            "Q": cumulative[end], "B": total-cumulative[end],
            "safe_bound": end+total-cumulative[end]})
        start = end
    return {
        "ranked_outputs": [str(z) for z in ordered],
        "fiber_sizes": sizes, "cumulative_coverage": cumulative,
        "fiber_histogram": {str(r): count for r, count in sorted(Counter(sizes).items())},
        "output_budgets": budgets, "coverage_targets": targets,
        "threshold_tails": tails, "greedy_half_remainder_hierarchy": hierarchy}


def analyze(seed, mode, budget):
    seed, labels, poles = build_completion(seed, mode, budget)
    E = {entry[3] for entry in labels}
    A = sorted({v for pair in E for v in pair})
    fibers, outputs = full_fibers(A, budget)
    charts = [{entry[3] for entry in labels if entry[0] == branch}
              for branch in range(3)]
    pair_labels = defaultdict(list)
    for branch, i, j, pair, prescribed in labels:
        if outputs[pair] != prescribed:
            raise AssertionError("Output-preservation identity failed")
        pair_labels[pair].append([branch, i, j])
        budget.charge("prescribed_pair_checks")
    selected_outputs = {outputs[pair] for pair in E}
    chart_outputs = [{outputs[pair] for pair in chart} for chart in charts]
    coordinate_labels = Counter(v for entry in labels for v in entry[3])
    coordinate_pairs = Counter(v for pair in E for v in pair)
    profile = coverage_profile(fibers, len(A))
    budget.charge("full_pair_accounting", len(A)**2)
    budget.charge("fiber_profile", len(fibers))
    overlaps = []
    for i, j in combinations(range(3), 2):
        overlaps.append({"charts": [i, j], "pair_overlap": len(charts[i] & charts[j]),
                         "output_overlap": len(chart_outputs[i] & chart_outputs[j])})
        budget.charge("chart_overlap_memberships", len(charts[i])+len(charts[j]))
    occupied = set()
    assigned = []
    for chart in charts:
        assigned.append(chart-occupied)
        occupied |= chart
    assigned_counts = [Counter(outputs[pair] for pair in chart) for chart in assigned]
    D = max((max(c.values(), default=0) for c in assigned_counts), default=0)
    H = sum(len(set(assigned_counts[i]) & set(assigned_counts[j]))
            for i, j in combinations(range(3), 2))
    Q, N, Z = len(E), len(A), len(selected_outputs)
    assert Q*Q <= Z*(D*Q+2*D*D*H)
    assert len(fibers) <= Z+N*N-Q
    assert len(selected_outputs) == len({entry[4] for entry in labels})
    budget.charge("global_accounting_assertions", 3)
    denominator = lcm(*(a.denominator for a in A))
    result = {
        "mode": mode, "seed": [str(a) for a in seed], "seed_N": len(seed),
        "N": N, "Q0": len(labels), "Q": Q, "Z": Z, "B": N*N-Q,
        "full_image": len(fibers), "safe_bound": Z+N*N-Q,
        "coverage_fraction": str(F(Q, N*N)), "capacity_ratio": str(F(Q, Z)),
        "maximum_fiber": max(map(len, fibers.values())), "chart_count": 3,
        "chart_pair_counts": list(map(len, charts)),
        "chart_output_counts": list(map(len, chart_outputs)),
        "chart_overlap": overlaps,
        "assigned_chart_fiber_cap": D, "assigned_output_overlap_sum": H,
        "pair_label_multiplicity_histogram": {
            str(r): c for r, c in sorted(Counter(map(len, pair_labels.values())).items())},
        "mean_actual_coordinate_reuse": str(F(2*Q, N)),
        "mean_label_coordinate_reuse": str(F(2*len(labels), N)),
        "common_denominator": denominator,
        "maximum_reduced_numerator": max(abs(a.numerator) for a in A),
        "maximum_absolute_scalar": str(max(map(abs, A))),
        "excluded_mobius_source_pairs": poles,
        "stop": "Only this first all-pair completion is tested. Its full new-square complement is charged; no sparse recursive expansion.",
        "profile": profile,
    }
    raw = {
        "summary": result, "scalars": [str(a) for a in A],
        "fibers": [{"output": str(z), "pairs": [[str(x), str(y)] for x, y in fibers[z]],
                    "selected_pairs": [[str(x), str(y)] for x, y in fibers[z] if (x, y) in E]}
                   for z in sorted(fibers)],
        "parameter_projection": [{"pair": [str(x), str(y)], "labels": pair_labels[(x, y)]}
                                 for x, y in sorted(pair_labels)],
        "coordinate_projection": [
            {"scalar": str(a), "formal_occurrences": coordinate_labels[a],
             "actual_pair_occurrences": coordinate_pairs[a]} for a in A],
    }
    return result, raw


def write_new(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run():
    run_dir = Path("local-only/runs/T01/2026-09-30-near-complete-charts")
    summary_path = Path("examples/2026-09-30-near-complete-charts.json")
    planned = [(f"{name}_{mode}", seed, mode) for name, seed in SEEDS for mode in MODES]
    if len(planned) > LIMITS["carriers"]:
        raise RuntimeError("Carrier cap")
    # Reject pre-existing outputs before evaluating any candidate.
    destinations = [summary_path, run_dir/"experiment-provenance.json"]
    destinations += [run_dir/f"{name}.json" for name, _, _ in planned]
    if any(path.exists() for path in destinations):
        raise FileExistsError("Existing run artifacts; refusing to rerun/overwrite")
    budget = Budget()
    cpu, wall = time.process_time(), time.perf_counter()
    results = []
    for name, seed, mode in planned:
        summary, raw = analyze(seed, mode, budget)
        path = run_dir/f"{name}.json"
        digest = write_new(path, raw)
        summary = dict(summary, id=name, raw_path=str(path), raw_sha256=digest)
        results.append(summary)
    timing = {"cpu_seconds": time.process_time()-cpu, "wall_seconds": time.perf_counter()-wall}
    portable = {
        "claim_id": "NC-X1", "status": "EXPERIMENTAL", "date": "2026-09-30",
        "polynomial": "(x-y)^3+x+y", "models": results,
        "limits": LIMITS, "errors": [],
        "scope": "Six exact first completions, not an asymptotic family theorem; full cumulative coverage is retained.",
    }
    digest = write_new(summary_path, portable)
    provenance = {
        "command": "python3 -m experiments.near_complete_charts",
        "python": platform.python_version(), "network": "none", "randomness": "none",
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "portable_sha256": digest, "limits": LIMITS, "carriers": len(results),
        "P_evaluations": budget.P_evaluations, "checks": dict(budget.checks),
        "charged_checks": sum(budget.checks.values()), **timing, "errors": [],
        "inspection": "New source inspected before execution; exact fractions, complete scalar square, poles, pair projection and full fiber profile checked.",
    }
    write_new(run_dir/"experiment-provenance.json", provenance)
    print(json.dumps({"models": [{k: row[k] for k in ("id", "N", "Q0", "Q", "Z", "B", "full_image", "maximum_fiber")} for row in results], "provenance": provenance}, indent=2))


if __name__ == "__main__":
    run()
