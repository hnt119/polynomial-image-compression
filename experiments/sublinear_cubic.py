"""One bounded exact grid of new sublinear-inventory cubic carriers.

Uses the inspected growing-step graph engine, with isolated run limits.
This module never launches that engine's historical carrier grid.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from contextlib import contextmanager
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from math import gcd
from pathlib import Path
import platform
import sys
import time

from experiments import growing_step_cubic as graph

MAX_CARRIERS, MAX_GRAPHS, MAX_INPUTS = 48, 288, 160
MAX_P_EVALUATIONS, MAX_CHECKS, MAX_CPU = 1_500_000, 8_000_000, 60


class Budget(graph.Budget):
    def reserve(self, category, count):
        self.time_check()
        if sum(self.checks.values()) + count > MAX_CHECKS:
            raise RuntimeError("New-grid check budget exhausted before batch")
        if category == "scalar_pair_evaluations" and self.checks[category] + count > MAX_P_EVALUATIONS:
            raise RuntimeError("New-grid polynomial budget exhausted before batch")
        self.checks[category] += count

    def time_check(self):
        if time.process_time() - self.start_cpu > MAX_CPU:
            raise RuntimeError("New-grid research CPU budget exhausted")


@contextmanager
def engine_limits():
    """Configure only the imported engine's guards, restoring them afterwards."""
    names = ("MAX_CARRIERS", "MAX_CASES", "MAX_INPUTS")
    previous = tuple(getattr(graph, name) for name in names)
    try:
        for name, value in zip(names, (MAX_CARRIERS, MAX_GRAPHS, MAX_INPUTS)):
            setattr(graph, name, value)
        yield
    finally:
        for name, value in zip(names, previous):
            setattr(graph, name, value)


def candidate(identifier, family, records, steps, parameters, escape, prescribed=()):
    return {"id": identifier, "family": family, "records": records,
            "values": sorted({x for x, _ in records}), "basic_steps": list(steps),
            "parameters": parameters, "escape": escape, "prescribed": list(prescribed)}


def definitions():
    for q in (4, 8, 12):
        yield candidate(f"multiscale_q{q}", "multiscale", [(Q(i, q) + Q(j, q*q+1), [i, j]) for i, j in product(range(q), range(3))],
                        [Q(1, q), Q(1, q*q+1)], {"q": q, "short_side": 3},
                        "Shrinking and unequal rational scales; no fixed mesh or faithful cubic coefficient projection.")
    for n in (8, 16, 24):
        yield candidate(f"reciprocal_n{n}", "nonuniform_mesh", [(Q(1, j), [j]) for j in range(1, n+1)],
                        [Q(1, n), Q(1, n*(n-1))], {"n": n},
                        "Nonuniform reciprocal gaps and a changing common denominator.")
    for q in (2, 3, 4):
        for kind, a in (("near", q+1), ("wide", 2*q-1)):
            yield candidate(f"projection_q{q}_{kind}", "nonfaithful_rational_projection",
                            [(Q(q*i+a*j, q*q), [i, j]) for i, j in product(range(2*q), repeat=2)],
                            [Q(1, q), Q(a, q*q)], {"q": q, "a": a, "side": 2*q},
                            "A rational rank-one scalar projection of a two-parameter box; the kernel identifies parameters and coefficients. It is not a rank-two number field.")
    for q, h in product((4, 8, 12), (2, 3)):
        records, prescribed = [], []
        for r, j in product(range(h), range(-q, q+1)):
            u = Q(j, q)
            ell = 2*r + u*u
            z = u**3 + ell
            prescribed.append((z, u, [r, j]))
            records.extend((((ell+u)/2, [r, j, "x"]), ((ell-u)/2, [r, j, "y"])))
        yield candidate(f"correlated_q{q}_H{h}", "correlated_u_L", records, [Q(1, q), Q(2, q)],
                        {"q": q, "H": h, "L_formula": "2r+u^2", "u_indices": [-q, q]},
                        "Correlated quadratic sum coordinate with growing denominators; fixed rational completion and independent U-by-L products are not used.", prescribed)
    for n in (4, 8, 16):
        for kind, c in (("near", 1), ("far", n)):
            records = []
            for j in range(n):
                records.extend(((Q(j, n), [0, j]), (c+Q(j, n*n+1), [1, j]), (-c+Q(j, n**3), [2, j])))
            yield candidate(f"unequal_n{n}_{kind}", "unequal_scale_union", records,
                            [Q(1, n), Q(1, n*n+1), Q(1, n**3)], {"n": n, "offset": c},
                            "Three unequal shrinking meshes; no fixed-spacing or moderate-width assumption is imposed.")
    for rule, sequence in (("fresh", (Q(1,3), Q(1,5), Q(1,7))), ("powers", (Q(1,2), Q(1,9), Q(1,125)))):
        records = [(Q(0), [0]), (Q(1), [1])]
        for level, tau in enumerate(sequence, 1):
            shifts = (Q(0), (tau-tau**3)/2, -(tau+tau**3)/2)
            records = [(x+shift, word+[i]) for (x, word), (i, shift) in product(records, enumerate(shifts))]
            yield candidate(f"changing_{rule}_level{level}", "changing_scale_completion", records,
                            list(sequence[:level]), {"rule": rule, "level": level, "steps_so_far": list(map(str, sequence[:level]))},
                            "The rational shift list changes with depth; only three declared levels are tested. This is not iteration of one fixed completion set.")
    for q, h in product((3, 5, 7), (2, 3)):
        records, prescribed = [], []
        for k, j, e in product(range(h), range(4), (-1, 0, 1)):
            anchor, u = Q(k, q), Q(j, q)
            z = u**3-u+2*anchor
            v = u+Q(e, q)
            prescribed.append((z, v, [k, j, e]))
            x, y = graph.orbit_coordinates(z, v)
            records.extend(((x, [k, j, e, "x"]), (y, [k, j, e, "y"])))
        yield candidate(f"reverse_q{q}_H{h}", "shared_anchor_reverse_fibers", records, [Q(1,q), Q(2,q)],
                        {"q": q, "H": h, "base_u_indices": [0, 3], "offset_indices": [-1, 1]},
                        "Outputs are correlated with anchor and base difference; every central pair reuses its anchor. Mesh changes with q and the output-by-difference prescription is not a full rectangular grid.", prescribed)


def structural_preflight(candidates):
    sizes = [len(c["values"]) for c in candidates]
    work = {"carriers": len(candidates), "graphs": 6*len(candidates), "maximum_N": max(sizes),
            "exact_P_evaluations": sum(n*n for n in sizes),
            "construction_record_checks": sum(len(c["records"])+len(c["prescribed"]) for c in candidates),
            "sizes": {c["id"]: len(c["values"]) for c in candidates}}
    if work["carriers"] > MAX_CARRIERS or work["graphs"] > MAX_GRAPHS or max(sizes) > MAX_INPUTS or work["exact_P_evaluations"] > MAX_P_EVALUATIONS:
        raise RuntimeError("Declared new-grid preflight exceeds allocation")
    return work


def common_inventory(basic_steps, cap):
    steps = []
    multiplier = 1
    while len(steps) < cap:
        for base in basic_steps:
            value = multiplier*abs(base)
            if value and value not in steps:
                steps.append(value)
                if len(steps) == cap:
                    break
        multiplier += 1
    return tuple(sorted(steps))


def inventories(carrier, basic_steps):
    n = carrier["N"]
    small, medium, large = graph.ceil_root(n, 6), graph.ceil_root(n, 2), graph.ceil_root(n*n, 3)
    ranked = sorted(carrier["edges_by_step"], key=lambda s: (-len(carrier["edges_by_step"][s]), s))
    return [("construction_small", common_inventory(basic_steps, small)),
            ("construction_sqrt", common_inventory(basic_steps, medium)),
            ("construction_two_thirds", common_inventory(basic_steps, large)),
            ("frequent_small", tuple(sorted(ranked[:small]))),
            ("frequent_sqrt", tuple(sorted(ranked[:medium]))),
            ("all_useful_diagnostic", tuple(sorted(ranked)))]


def carrier_metrics(candidate_record, carrier, budget):
    values, n = carrier["values"], carrier["N"]
    budget.reserve("difference_pair_checks", n*n)
    differences = sorted({x-y for x, y in product(values, repeat=2)})
    budget.reserve("difference_gap_checks", len(differences)-1)
    projection = defaultdict(list)
    for value, label in candidate_record["records"]:
        projection[str(value)].append(label)
    prescribed = defaultdict(list)
    for z, u, label in candidate_record["prescribed"]:
        prescribed[str(z)+"|"+str(u)].append(label)
    budget.reserve("prescribed_membership_checks", len(candidate_record["prescribed"]))
    indices = {x:i for i,x in enumerate(values)}
    for z, u, _ in candidate_record["prescribed"]:
        x, y = graph.orbit_coordinates(z, u)
        if x not in indices or y not in indices:
            raise AssertionError("Prescribed pair escaped the actual scalar carrier")
        output_index = carrier["output_of_vertex"][indices[x]*n+indices[y]]
        if carrier["fibers"][output_index]["output"] != str(z):
            raise AssertionError("Prescribed output does not match the full exact enumeration")
    denominator = 1
    for x in values:
        denominator = denominator*x.denominator//gcd(denominator, x.denominator)
    translated_numerators = [int((x-values[0])*denominator) for x in values]
    divisor = 0
    for x in translated_numerators:
        divisor = gcd(divisor, x)
    mesh = Q(divisor, denominator)
    diameter = values[-1]-values[0]
    sizes = [f["size"] for f in carrier["fibers"]]
    return {"diameter": str(diameter), "minimum_scalar_gap": str(min(b-a for a,b in zip(values, values[1:]))),
            "difference_set_size": len(differences), "difference_set_minimum_gap": str(min(b-a for a,b in zip(differences,differences[1:]))),
            "common_denominator": str(denominator), "largest_affine_lattice_mesh": str(mesh),
            "lattice_width_ratio_D_over_h3N2": str(diameter/(mesh**3*n*n)),
            "scalar_maximum_numerator_bits": max(abs(x.numerator).bit_length() for x in values),
            "scalar_maximum_denominator_bits": max(x.denominator.bit_length() for x in values),
            "parameter_occurrences": len(candidate_record["records"]), "parameter_to_scalar_reuse": str(Q(len(candidate_record["records"]),n)),
            "scalar_projection_multiplicity_distribution": dict(sorted(Counter(map(len, projection.values())).items())),
            "scalar_projection_fibers": dict(projection), "prescribed_pair_parameter_fibers": dict(prescribed),
            "distinct_prescribed_pairs": len(prescribed), "prescribed_pair_fraction": str(Q(len(prescribed), n*n)),
            "prescribed_pairs_per_scalar": str(Q(len(prescribed),n)),
            "maximum_actual_fiber": max(sizes), "average_actual_fiber": str(Q(n*n,len(sizes))),
            "actual_nonsingleton_mass": sum(s for s in sizes if s>1),
            "actual_fiber_size_distribution": dict(sorted(Counter(sizes).items()))}


def step_reuse(carrier, steps, budget):
    budget.reserve("step_output_reuse_checks", sum(len(carrier["edges_by_step"].get(s,())) for s in steps))
    return {str(s): {"edge_count": len(carrier["edges_by_step"].get(s,())),
                     "distinct_outputs": len({carrier["output_of_vertex"][v] for v,w in carrier["edges_by_step"].get(s,())})}
            for s in steps}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_new(path, data):
    if path.exists():
        raise RuntimeError(f"Refusing to overwrite {path}")
    graph.write_json(path, data)


def run(directory, portable):
    budget = Budget()
    wall = time.perf_counter()
    if (directory/"provenance.json").exists() or portable.exists():
        raise RuntimeError("Refusing to overwrite an existing new-grid artifact")
    candidates = list(definitions())
    preflight = structural_preflight(candidates)
    budget.reserve("construction_record_checks", preflight["construction_record_checks"])
    directory.mkdir(parents=True, exist_ok=True)
    records, cases, errors = [], [], []
    try:
        with engine_limits():
            for candidate_record in candidates:
                carrier = graph.enumerate_fibers(candidate_record["values"], budget)
                metrics = carrier_metrics(candidate_record, carrier, budget)
                record = {"id": candidate_record["id"], "family": candidate_record["family"],
                          "parameters": candidate_record["parameters"], "scope_escape": candidate_record["escape"],
                          "basic_steps": list(map(str,candidate_record["basic_steps"])),
                          "inputs": list(map(str,carrier["values"])), "N":carrier["N"], "image_size":carrier["image_size"],
                          "fibers":carrier["fibers"], "pair_output_index":carrier["output_of_vertex"],
                          "all_useful_step_counts": {str(s):len(e) for s,e in sorted(carrier["edges_by_step"].items())}, **metrics}
                path = directory/(record["id"]+"-carrier.json")
                write_new(path, record)
                record.update(raw_path=str(path), raw_sha256=sha(path))
                records.append({k:v for k,v in record.items() if k not in {"fibers","pair_output_index","scalar_projection_fibers","prescribed_pair_parameter_fibers"}})
                for label, steps in inventories(carrier, candidate_record["basic_steps"]):
                    oracle = label=="construction_small" and record["id"] in {"projection_q2_near","reverse_q3_H2","changing_fresh_level1"}
                    case = graph.graph_case(carrier, label, steps, budget, direct_oracle=oracle)
                    case.update(carrier_id=record["id"], step_output_reuse=step_reuse(carrier, steps, budget),
                                inventory_source="actual-fiber diagnostic" if label.startswith("frequent") or label.startswith("all_") else "declared construction list")
                    path = directory/(record["id"]+"-"+label+".json")
                    write_new(path, case)
                    case.update(raw_path=str(path), raw_sha256=sha(path))
                    cases.append({k:v for k,v in case.items() if k not in {"components","component_output_indices","edges","components_per_output"}})
                    budget.time_check()
    except Exception as error:
        errors.append({"type":type(error).__name__,"message":str(error),"completed_carriers":len(records),"completed_graphs":len(cases)})
    result = {"date":"2026-09-21", "claim_id":"SL-X1", "status":"EXPERIMENTAL exact finite new-grid evidence", "polynomial":"(x-y)^3+x+y",
              "preflight":preflight,"carriers":records,"cases":cases,"errors":errors,
              "warning":"All-useful graphs reproduce full fibers by construction. Frequent-step lists use exact fiber information and are diagnostic. No asymptotic statement is inferred; rational two-parameter projections are not rank-two number fields."}
    write_new(portable,result)
    provenance={"date":"2026-09-21","command":"python3 -m experiments.sublinear_cubic","python":sys.version,"implementation":platform.python_implementation(),
                "network":"none","randomness":"none","source_sha256":sha(Path(__file__)),"graph_engine_sha256":sha(Path(graph.__file__)),"portable_sha256":sha(portable),
                "preflight":preflight,"limits":{"carriers":MAX_CARRIERS,"graphs":MAX_GRAPHS,"N":MAX_INPUTS,"P_evaluations":MAX_P_EVALUATIONS,"checks":MAX_CHECKS,"research_cpu_seconds":MAX_CPU},
                "actual":{"carriers":budget.carriers,"graphs":budget.cases,"checks_by_category":dict(budget.checks),"charged_checks":sum(budget.checks.values()),"cpu_seconds":time.process_time()-budget.start_cpu,"wall_seconds":time.perf_counter()-wall},
                "errors":errors,"inspection":"New code and graph-engine enumeration/union-find/counting functions read before execution; no historical grid invoked."}
    write_new(directory/"provenance.json",provenance)
    print(json.dumps({"actual":provenance["actual"],"errors":errors},indent=2))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preflight",action="store_true")
    parser.add_argument("--directory",type=Path,default=Path("local-only/runs/T01/2026-09-21-sublinear-cubic"))
    parser.add_argument("--portable",type=Path,default=Path("examples/2026-09-21-sublinear-cubic.json"))
    args=parser.parse_args()
    if args.preflight:
        start=time.process_time()
        result=structural_preflight(list(definitions()))
        result["preflight_cpu_seconds"]=time.process_time()-start
        print(json.dumps(result,indent=2))
    else:
        run(args.directory,args.portable)


if __name__=="__main__":
    main()
