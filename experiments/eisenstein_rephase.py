"""F4: bounded greedy norm-one rephasing of the finite F3 word carrier.

Each original word has the FIXED candidate set w*U_m. Rephasing never expands
that exponent window. The search minimizes the signed coordinate union while
preserving distinct engineered pairs; it does not minimize the full Q image.
Only strict coordinate-count reductions are applied, with deterministic ties.

Run: python3 -m experiments.eisenstein_rephase --output NEW_PATH
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import sys
import time

from .eisenstein_solvable import (
    Budget, BudgetExceeded, construct, digest, full_image, integerize,
)


CANDIDATE_CAP = 100_000
PAIR_CAP = 100_000
CPU_CAP = 90.0
SWEEP_CAP = 10


class RephaseBudget(Budget):
    def __init__(self, cpu_cap=CPU_CAP, candidate_cap=CANDIDATE_CAP):
        super().__init__(pair_cap=PAIR_CAP, action_cap=0, cpu_cap=cpu_cap)
        self.candidate_cap = candidate_cap
        self.generated = 0
        self.scored = 0

    def candidate(self, generation=False):
        if self.generated + self.scored >= self.candidate_cap:
            raise BudgetExceeded("candidate generation/scoring cap exhausted")
        if generation:
            self.generated += 1
        else:
            self.scored += 1
        if (self.generated + self.scored) % 64 == 0:
            self.check()


def signed_coordinates(arithmetic, pair):
    return frozenset(coordinate for x in pair for coordinate in (x, arithmetic.neg(x)))


def rational_pair_payload(pair):
    return [[[Fraction(x).numerator, Fraction(x).denominator] for x in coordinate]
            for coordinate in pair]


def greedy_rephase(arithmetic, words, multipliers, budget, max_sweeps=SWEEP_CAP):
    """Coordinate descent over fixed finite candidate lists, not global optimization."""
    if not 1 <= max_sweeps <= SWEEP_CAP:
        raise ValueError("sweep count must lie between 1 and 10")
    original = sorted(words)
    current = list(original)
    occupied = set(current)
    if len(current) != len(occupied):
        raise ValueError("original engineered pairs must be distinct")
    candidates = []
    for word in original:
        options = set()
        for multiplier in sorted(multipliers):
            budget.candidate(generation=True)
            options.add(arithmetic.eisenstein_mul(word, multiplier))
        if word not in options:
            raise ValueError("candidate multiplier set must contain identity")
        candidates.append(sorted(options))
    counts = Counter(coordinate for word in current
                     for coordinate in signed_coordinates(arithmetic, word))
    original_size = len(counts)
    trace = []
    stable = False
    for sweep in range(1, max_sweeps + 1):
        moves = 0
        before = len(counts)
        for index, old in enumerate(current):
            old_coordinates = signed_coordinates(arithmetic, old)
            # Temporarily remove precisely this word's incidence, including zero once.
            for coordinate in old_coordinates:
                counts[coordinate] -= 1
                if counts[coordinate] == 0:
                    del counts[coordinate]
            base_size = len(counts)
            best = old
            best_size = base_size + sum(coordinate not in counts for coordinate in old_coordinates)
            for candidate in candidates[index]:
                budget.candidate()
                if candidate != old and candidate in occupied:
                    continue
                coordinates = signed_coordinates(arithmetic, candidate)
                size = base_size + sum(coordinate not in counts for coordinate in coordinates)
                # Iteration is lexical: the first strict minimum handles all ties.
                if size < best_size:
                    best, best_size = candidate, size
            if best != old:
                occupied.remove(old)
                occupied.add(best)
                current[index] = best
                moves += 1
            for coordinate in signed_coordinates(arithmetic, best):
                counts[coordinate] += 1
        trace.append({"sweep": sweep, "accepted_moves": moves,
                      "input_size_before": before, "input_size_after": len(counts)})
        budget.check()
        if moves == 0:
            stable = True
            break
    # Verify algebraic invariants directly on the final correspondence.
    if len(set(current)) != len(original):
        raise ArithmeticError("rephasing lost distinct engineered pairs")
    for old, new in zip(original, current):
        budget.pair()
        old_norm = arithmetic.q(*old)
        budget.pair()
        if old_norm != arithmetic.q(*new):
            raise ArithmeticError("rephasing changed an engineered norm")
    independently_rebuilt = {coordinate for pair in current
                             for coordinate in signed_coordinates(arithmetic, pair)}
    if independently_rebuilt != set(counts):
        raise ArithmeticError("coordinate incidence bookkeeping mismatch")
    if len(counts) > original_size:
        raise ArithmeticError("coordinate objective increased")
    return {"original": original, "placement": current,
            "carrier": independently_rebuilt,
            "initial_input_size": original_size,
            "trace": trace, "single_word_local_optimum": stable,
            "candidate_options_per_word": [len(options) for options in candidates]}


def case(m, budget):
    if m not in (1, 2, 3):
        raise ValueError("only levels 1, 2, 3 are authorized")
    started = time.process_time()
    old_pairs, old_generated, old_scored = budget.pairs, budget.generated, budget.scored
    arithmetic, _, words, multipliers = construct("F3", m, budget)
    search = greedy_rephase(arithmetic, words, multipliers, budget)
    denominator, carrier = integerize(sorted(search["carrier"]))
    carrier = sorted(set(carrier))
    images = full_image(arithmetic, carrier, budget)
    encoded_pairs = [(tuple(int(x * denominator) for x in a),
                      tuple(int(x * denominator) for x in b))
                     for a, b in search["placement"]]
    norms = set()
    for pair in encoded_pairs:
        budget.pair()
        norms.add(arithmetic.q(*pair))
    if not norms <= set(images):
        raise ArithmeticError("rephased engineered norm is absent from full Q image")
    input_payload = {"primes": arithmetic.primes, "denominator": denominator,
                     "carrier": carrier, "engineered_pairs": sorted(encoded_pairs)}
    output_payload = {"primes": arithmetic.primes,
                      "denominator": denominator * denominator,
                      "output_fibers": sorted(images.items())}
    correspondence = [[rational_pair_payload(old), rational_pair_payload(new)]
                      for old, new in zip(search["original"], search["placement"])]
    return {
        "family": "F4", "source_family": "F3", "m": m,
        "primes": arithmetic.primes, "field_degree": arithmetic.dimension,
        "initial_input_size": search["initial_input_size"],
        "input_size": len(carrier), "full_image_size": len(images),
        "engineered_pairs": len(encoded_pairs), "engineered_norms": len(norms),
        "ordered_pairs": len(carrier) ** 2,
        "unengineered_ordered_pairs": len(carrier) ** 2 - len(encoded_pairs),
        "multiplier_candidate_count": len(multipliers),
        "candidate_options_per_word": search["candidate_options_per_word"],
        "single_word_local_optimum": search["single_word_local_optimum"],
        "global_optimum_claimed": False,
        "trace": search["trace"],
        "output_fibers_by_multiplicity": dict(sorted(Counter(images.values()).items())),
        "input_common_denominator": denominator,
        "max_abs_scaled_coefficient": max(abs(x) for a in carrier for x in a),
        "input_sha256": digest(input_payload), "output_sha256": digest(output_payload),
        "correspondence_sha256": digest(correspondence),
        "carrier_scaled_integer_coefficients": carrier,
        "engineered_pairs_scaled_integer_coefficients": encoded_pairs,
        "norm_preserving_correspondence": correspondence,
        "pair_output_evaluations": budget.pairs - old_pairs,
        "candidate_generations": budget.generated - old_generated,
        "candidate_score_evaluations": budget.scored - old_scored,
        "cpu_seconds": time.process_time() - started,
    }


def run(cpu_cap=CPU_CAP):
    if not 0 < cpu_cap <= CPU_CAP:
        raise ValueError("CPU budget must be positive and at most 90 seconds")
    budget = RephaseBudget(cpu_cap=cpu_cap)
    wall_started = time.monotonic()
    from . import eisenstein_solvable
    result = {
        "experiment": "F4 bounded greedy Eisenstein rephasing",
        "status": "EXPERIMENTAL; finite greedy search and exhaustive final full-image counts",
        "branch": "T03 separate multiplier construction; not adaptive RC15/4",
        "polynomial": "x^2+xy+y^2",
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version, "platform": platform.platform(),
        "command": [sys.executable, "-m", "experiments.eisenstein_rephase", *sys.argv[1:]],
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "arithmetic_module_sha256": hashlib.sha256(Path(eisenstein_solvable.__file__).read_bytes()).hexdigest(),
        "budget": {"candidate_generation_and_scoring_cap": CANDIDATE_CAP,
                   "pair_output_cap": PAIR_CAP, "cpu_seconds_cap": cpu_cap,
                   "maximum_sweeps_per_level": SWEEP_CAP},
        "parameters": {"levels": [1, 2, 3], "primes": [2, 3, 5],
                       "candidate_exponents": [-1, 0, 1],
                       "candidate_rule": "original word times U_m; fixed through every sweep",
                       "input_rule": "one signed union of both coefficient projections",
                       "word_order": "lexical exact rational coefficient tuples",
                       "update_rule": "strict signed-input-cardinality improvement, lexical candidate tie"},
        "limitations": ["Only single-word strict descent over the specified candidate lists is tested.",
                        "Stopping without moves proves a coordinatewise local optimum in that finite list only.",
                        "The search objective is coordinate count, not image size; full image is counted afterward.",
                        "Finite improvements do not prove an asymptotic rate or advance RC15/4."],
        "results": [], "errors": [],
    }
    try:
        for m in (1, 2, 3):
            result["results"].append(case(m, budget))
        budget.check()
    except BudgetExceeded as error:
        result["errors"].append(str(error))
    result.update(completed=len(result["results"]) == 3 and not result["errors"],
                  pair_output_evaluations=budget.pairs,
                  candidate_generations=budget.generated,
                  candidate_score_evaluations=budget.scored,
                  cpu_seconds=time.process_time() - budget.started,
                  wall_seconds=time.monotonic() - wall_started)
    result["results_sha256"] = digest(result["results"])
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="new JSON output file, never overwritten")
    parser.add_argument("--cpu-seconds", type=float, default=CPU_CAP)
    args = parser.parse_args(argv)
    if args.output is not None and args.output.exists():
        parser.error("output already exists; choose a new run path")
    try:
        result = run(args.cpu_seconds)
    except ValueError as error:
        parser.error(str(error))
    rendered = json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n"
    if args.output is None:
        print(rendered, end="")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x") as stream:
            stream.write(rendered)
        print(json.dumps({"output": str(args.output.resolve()), "completed": result["completed"],
                          "cases": len(result["results"]), "cpu_seconds": result["cpu_seconds"],
                          "pair_output_evaluations": result["pair_output_evaluations"],
                          "candidate_generations": result["candidate_generations"],
                          "candidate_score_evaluations": result["candidate_score_evaluations"],
                          "errors": result["errors"]}))
    return 0 if result["completed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
