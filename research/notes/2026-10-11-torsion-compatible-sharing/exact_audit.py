"""One frozen offline audit: two compatible CP loci and orders 2,3,4.

No imported research implementation, root search, torsion enumeration or
parameter sweep. Scalar inputs are H*K and elliptic points are (X,H*V),
with exact rational arithmetic in one fixed degree-three or degree-four K.
Run only after the saved compatibility proof and this source are reviewed.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
import platform
import time


HERE = Path(__file__).resolve().parent
ORDERS = (2, 3, 4)
LIMITS = {"cases": 6, "exact_checks": 20000, "P_evaluations": 5000}
OUTPUT = HERE / "exact-results.json"


class Budget:
    def __init__(self):
        self.counts = Counter()
        self.check_categories = Counter()
        self.P_methods = Counter()

    def charge(self, kind, amount=1):
        if self.counts[kind] + amount > LIMITS[kind]:
            raise RuntimeError(f"Frozen budget exceeded: {kind}")
        self.counts[kind] += amount

    def check(self, condition, category):
        self.charge("exact_checks")
        self.check_categories[category] += 1
        if not condition:
            raise AssertionError(category)

    def polynomial(self, method):
        self.charge("P_evaluations")
        self.P_methods[method] += 1


class Field:
    """Q[T]/f. Irreducibility and real embedding are proof prerequisites."""
    def __init__(self, modulus, budget):
        self.modulus = tuple(map(F, modulus))
        self.degree = len(modulus)-1
        self.monic = tuple(a/self.modulus[-1] for a in self.modulus)
        self.budget = budget
        self.zero = (F(0),)*self.degree
        self.one = (F(1),)+(F(0),)*(self.degree-1)
        self.variable = (F(0), F(1))+(F(0),)*(self.degree-2)
        # Independent fixed-power table: multiply a vector by T by shifting.
        self.powers = [self.one]
        for _ in range(4*(self.degree-1)):
            old = self.powers[-1]
            high = old[-1]
            self.powers.append(tuple((old[j-1] if j else F(0))
                                     -high*self.monic[j]
                                     for j in range(self.degree)))

    def constant(self, value):
        return (F(value),)+(F(0),)*(self.degree-1)

    def add(self, a, b):
        return tuple(x+y for x, y in zip(a, b))

    def scale(self, a, scalar):
        return tuple(F(scalar)*x for x in a)

    def sub(self, a, b):
        return self.add(a, self.scale(b, -1))

    def reduce(self, polynomial):
        out = list(map(F, polynomial))
        out.extend([F(0)]*max(0, self.degree-len(out)))
        for power in range(len(out)-1, self.degree-1, -1):
            factor = out[power]
            for j in range(self.degree):
                out[power-self.degree+j] -= factor*self.monic[j]
            out[power] = F(0)
        return tuple(out[:self.degree])

    def mul(self, a, b):
        out = [F(0)]*(len(a)+len(b)-1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i+j] += x*y
        return self.reduce(out)

    def square(self, a):
        return self.mul(a, a)

    def cube(self, a):
        return self.mul(self.square(a), a)

    def inv(self, value):
        if value == self.zero:
            raise ZeroDivisionError("Zero field denominator")
        n = self.degree
        columns = []
        for j in range(n):
            basis = tuple(F(i == j) for i in range(n))
            columns.append(self.mul(value, basis))
        rows = [[columns[j][i] for j in range(n)]+[F(i == 0)]
                for i in range(n)]
        for j in range(n):
            pivot = next(i for i in range(j, n) if rows[i][j])
            rows[j], rows[pivot] = rows[pivot], rows[j]
            factor = rows[j][j]
            rows[j] = [a/factor for a in rows[j]]
            for i in range(n):
                if i != j:
                    factor = rows[i][j]
                    rows[i] = [a-factor*b for a, b in zip(rows[i], rows[j])]
        result = tuple(rows[i][-1] for i in range(n))
        self.budget.check(self.mul(value, result) == self.one, "field_inverse_identity")
        return result

    def div(self, a, b):
        return self.mul(a, self.inv(b))


def encoded(value):
    return [str(a) for a in value]


def point_encoded(point):
    return {"point": "O"} if point is None else {
        "X_coefficients": encoded(point[0]), "Y_over_H_coefficients": encoded(point[1])}


class Group:
    def __init__(self, field, H_squared, c_over_H):
        self.f = field
        self.lam = H_squared
        self.c = c_over_H
        self.B = field.sub(field.constant(-128),
                           field.scale(field.mul(H_squared, field.square(c_over_H)), 432))
        self.cache = {}

    def on_curve(self, point):
        if point is None:
            return True
        f, (x, v) = self.f, point
        return f.mul(self.lam, f.square(v)) == f.add(
            f.sub(f.cube(x), f.scale(x, 48)), self.B)

    def negative(self, point):
        return None if point is None else (point[0], self.f.scale(point[1], -1))

    def add(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        f = self.f
        f.budget.check(self.on_curve(left), "group_input_on_curve")
        f.budget.check(self.on_curve(right), "group_input_on_curve")
        x, v = left
        xx, vv = right
        if x == xx:
            if v == f.scale(vv, -1):
                return None
            f.budget.check(v == vv, "equal_X_same_or_opposite_Y")
            slope_over_H = f.div(f.sub(f.scale(f.square(x), 3), f.constant(48)),
                                 f.scale(f.mul(self.lam, v), 2))
        else:
            slope_over_H = f.div(f.sub(vv, v), f.sub(xx, x))
        result_x = f.sub(f.sub(f.mul(self.lam, f.square(slope_over_H)), x), xx)
        result_v = f.sub(f.mul(slope_over_H, f.sub(x, result_x)), v)
        result = (result_x, result_v)
        f.budget.check(self.on_curve(result), "group_result_on_curve")
        return result

    def multiple(self, n, point):
        if n < 0:
            return self.multiple(-n, self.negative(point))
        key = (n, point)
        if key in self.cache:
            return self.cache[key]
        result, summand, remaining = None, point, n
        while remaining:
            if remaining & 1:
                result = self.add(result, summand)
            remaining //= 2
            if remaining:
                summand = self.add(summand, summand)
        self.cache[key] = result
        return result


def primary_P(f, lam, x, y):
    f.budget.polynomial("difference_cube_generic_reduction")
    return f.add(f.mul(lam, f.cube(f.sub(x, y))), f.add(x, y))


def independent_P(f, lam, x, y):
    """Unreduced expanded cube; no Field.mul/cube/reduce call."""
    f.budget.polynomial("expanded_cube_fixed_power_table")
    n = f.degree
    cubic = [F(0)]*(3*n-2)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                cubic[i+j+k] += (x[i]*x[j]*x[k]-3*x[i]*x[j]*y[k]
                                  +3*x[i]*y[j]*y[k]-y[i]*y[j]*y[k])
    polynomial = [F(0)]*(4*n-3)
    for i, coefficient in enumerate(cubic):
        for j, scale_coefficient in enumerate(lam):
            polynomial[i+j] += coefficient*scale_coefficient
    for i in range(n):
        polynomial[i] += x[i]+y[i]
    return tuple(sum(coefficient*f.powers[j][i]
                     for j, coefficient in enumerate(polynomial)) for i in range(n))


def prepare_cases(budget):
    first = Field([-1, 28, -80, 64], budget)
    t = first.variable
    s = first.sub(first.constant(5), first.scale(t, 8))
    c = first.scale(first.sub(first.one, first.scale(t, 2)), 8)
    q = first.scale(c, F(1, 4))
    case1 = {"id": "original_CP_bridge", "field": first, "H_squared": t,
             "root_interval": ["1/32", "1/24"], "c_over_H": c,
             "widths": [(first.one, s)],
             "frames": [(q, first.one, s), (first.scale(q, -1), first.one, s)],
             "expected_Z": 3, "expected_locus_size": 2}
    second = Field([-23, 0, 6, 0, 1], budget)
    w = second.variable
    rt2 = second.scale(second.add(second.square(w), second.constant(3)), F(1, 4))
    k = second.sub(rt2, second.one)
    lam = second.scale(second.add(second.constant(3), rt2), F(1, 14))
    c2 = second.scale(second.mul(k, second.sub(second.one,
                       second.scale(second.mul(lam, second.square(k)), 2))), 8)
    q2 = second.scale(c2, F(1, 4))
    case2 = {"id": "forced_two_width_frame", "field": second, "H_squared": lam,
             "root_interval": ["3/2", "7/4"], "c_over_H": c2,
             "widths": [(k, w), (second.one, k)],
             "frames": [(q2, k, w), (q2, second.one, k)],
             "expected_Z": 2, "expected_locus_size": 4}
    return [case1, case2]


def chart_point(case, width, column_width):
    f, lam = case["field"], case["H_squared"]
    squared_width = f.mul(lam, f.square(width))
    return (f.sub(f.constant(44), f.scale(squared_width, 96)),
            f.scale(f.mul(column_width, f.sub(f.one, f.scale(squared_width, 2))), 288))


def slots(case, point, z, lower_output):
    f, lam, c = case["field"], case["H_squared"], case["c_over_H"]
    denominator = f.add(point[0], f.constant(4))
    d = f.div(f.scale(c, 12), denominator)
    total = f.div(point[1], f.scale(denominator, 3))
    u, v = f.scale(f.add(total, d), F(1, 2)), f.scale(f.sub(total, d), F(1, 2))
    A = f.scale(f.add(f.sub(z, f.mul(lam, f.cube(u))), u), F(1, 2))
    B = f.scale(f.add(f.sub(lower_output, f.mul(lam, f.cube(v))), v), F(1, 2))
    D = f.sub(A, u)
    f.budget.check(D == f.sub(B, v), "shared_second_coordinate")
    return A, B, D


def audit_case(case, budget):
    f, lam, c = case["field"], case["H_squared"], case["c_over_H"]
    group = Group(f, lam, c)
    locus = {}
    for i, (width, column_width) in enumerate(case["widths"], 1):
        budget.check(f.mul(lam, f.add(f.scale(f.square(width), 3),
                                      f.square(column_width))) == f.one,
                     "frame_conic_compatibility")
        point = chart_point(case, width, column_width)
        budget.check(group.on_curve(point), "basepoint_on_curve")
        locus[f"R{i}+"] = point
        locus[f"R{i}-"] = group.negative(point)
    budget.check(len(set(locus.values())) == case["expected_locus_size"],
                 "complete_admissible_locus_distinctness")
    base = locus["R1+"]
    translations = {name: group.add(point, group.negative(base))
                    for name, point in locus.items()}
    order_results = []
    for n in ORDERS:
        budget.charge("cases")
        divided, transported = [], []
        details = []
        for name, point in locus.items():
            multiple = group.multiple(n, point)
            shift = translations[name]
            shift_multiple = group.multiple(n, shift)
            proper = {d: group.multiple(d, shift) for d in range(1, n) if n % d == 0}
            exact_order = shift_multiple is None and all(p is not None for p in proper.values())
            if multiple == base:
                divided.append(name)
            if exact_order:
                transported.append(name)
            budget.check(group.add(base, shift) == point, "translation_recovers_destination")
            details.append({"destination": name, "n_times_destination": point_encoded(multiple),
                            "translation": point_encoded(shift),
                            "n_times_translation": point_encoded(shift_multiple),
                            "proper_divisor_multiples": {str(d): point_encoded(p) for d, p in proper.items()},
                            "division_hit": multiple == base, "translation_exact_order_n": exact_order})
        order_results.append({"n": n, "division_intersection": divided,
                              "exact_order_translation_destinations": transported,
                              "complete_locus_tests": details})
    base_multiples = {str(k): point_encoded(group.multiple(k, base))
                      for k in (1, 2, 3, 4, 5, 6, 8)}
    # Construct only the two pre-agreed six-point carriers from all frame slots.
    scalar_set, selected, frame_records = set(), {}, []
    for frame_id, (center, width, column_width) in enumerate(case["frames"]):
        half_gap = f.scale(f.mul(width, f.sub(f.one,
                        f.scale(f.mul(lam, f.square(width)), 2))), 4)
        z, lower_output = f.add(f.scale(center, 2), half_gap), f.sub(f.scale(center, 2), half_gap)
        budget.check(f.sub(z, lower_output) == c, "same_ordered_output_difference")
        base_point = chart_point(case, width, column_width)
        rows = [f.add(center, width), f.sub(center, width)]
        columns = [f.sub(center, column_width), f.add(center, column_width)]
        for sign, point in ((1, base_point), (-1, group.negative(base_point))):
            A, B, D = slots(case, point, z, lower_output)
            expected_column = columns[0 if sign > 0 else 1]
            budget.check((A, B, D) == (rows[0], rows[1], expected_column),
                         "actual_chart_endpoint_recovery")
            for row, output in ((A, z), (B, lower_output)):
                pair = (row, D)
                budget.check(pair not in selected, "distinct_prescribed_pair")
                selected[pair] = output
                scalar_set.update(pair)
        frame_records.append({"frame": frame_id, "center": encoded(center),
                              "source_halfwidth": encoded(width), "target_halfwidth": encoded(column_width),
                              "upper_output": encoded(z), "lower_output": encoded(lower_output)})
    scalars = sorted(scalar_set)  # Canonical coefficient order, not real order.
    indices = {x: i for i, x in enumerate(scalars)}
    budget.check((len(scalars), len(selected), len(set(selected.values()))) ==
                 (6, 8, case["expected_Z"]), "N_Q_Z_counts")
    fibers, values = defaultdict(list), {}
    for i, x in enumerate(scalars):
        for j, y in enumerate(scalars):
            a = primary_P(f, lam, x, y)
            b = independent_P(f, lam, x, y)
            budget.check(a == b, "independent_complete_square_P_agreement")
            values[(x, y)] = a
            fibers[a].append([i, j])
    for pair, expected in selected.items():
        budget.check(values[pair] == expected, "prescribed_output_in_complete_square")
    histogram = Counter(len(pairs) for pairs in fibers.values())
    budget.check(sum(size*count for size, count in histogram.items()) == 36,
                 "complete_square_mass")
    summary = {"case": case["id"], "N": 6, "Q": 8, "Z": case["expected_Z"], "B": 28,
               "safe_support_upper_bound": 28+case["expected_Z"], "full_image": len(fibers),
               "two_Q_over_N": "8/3", "Q_over_Z": str(F(8, case["expected_Z"])),
               "Q_over_N_squared": "2/9", "full_fiber_histogram": dict(sorted(histogram.items())),
               "strict_small_fiber_tails": {str(k): sum(size*count for size, count in histogram.items() if size < k)
                                            for k in range(1, 8)},
               "division_intersections": {str(row["n"]): row["division_intersection"] for row in order_results},
               "translation_destinations": {str(row["n"]): row["exact_order_translation_destinations"] for row in order_results}}
    return {"summary": summary, "field_modulus": encoded(f.modulus),
            "root_interval": case["root_interval"], "H_squared": encoded(lam),
            "c_over_H": encoded(c), "curve_B": encoded(group.B),
            "admissible_locus": {name: point_encoded(p) for name, p in locus.items()},
            "basepoint_multiples": base_multiples, "order_audit": order_results, "frames": frame_records,
            "scalar_encoding": "H times polynomial coefficients; canonical coefficient order, not real order",
            "scalars": [encoded(x) for x in scalars],
            "selected_pairs": [{"pair": [indices[x], indices[y]], "output": encoded(z)}
                               for (x, y), z in sorted(selected.items())],
            "complete_fibers": [{"output": encoded(z), "pairs": pairs} for z, pairs in sorted(fibers.items())]}


def audit_saved_certificates(path, field):
    """Multiply the five saved identities; no solver or old code is imported."""
    saved = json.loads(path.read_text())
    f, t = field, field.variable
    one, zero = f.one, f.zero
    a = f.sub(one, f.scale(t, 4))
    b = f.sub(f.constant(3), f.scale(t, 4))
    d = f.sub(f.constant(7), f.scale(t, 12))
    choices = {"minus_d": f.scale(d, -1), "minus_b": f.scale(b, -1),
               "minus_a": f.scale(a, -1), "plus_b": b, "plus_d": d}
    f.budget.check({row["reused_other_row"] for row in saved["cases"]} == set(choices)
                   and len(saved["cases"]) == 5, "all_five_attachment_certificates_present")
    audited = []
    for row in saved["cases"]:
        f.budget.check(row["endpoint"] == "plus_a", "certificate_endpoint")
        A = choices[row["reused_other_row"]]
        difference = f.sub(a, A)
        cubic = [f.scale(A, -1), f.constant(-3), zero, f.scale(t, 4)]
        quadratic = [f.sub(f.mul(t, f.square(difference)), one),
                     f.scale(f.mul(t, difference), -2), f.scale(t, 4)]
        U = [tuple(map(F, coeffs)) for coeffs in row["bezout_cubic"]]
        V = [tuple(map(F, coeffs)) for coeffs in row["bezout_quadratic"]]
        f.budget.check(all(len(item) == f.degree for item in U+V), "certificate_coefficient_dimension")
        result = [zero]*max(len(U)+len(cubic)-1, len(V)+len(quadratic)-1)
        for first, second in ((U, cubic), (V, quadratic)):
            for i, x in enumerate(first):
                for j, y in enumerate(second):
                    result[i+j] = f.add(result[i+j], f.mul(x, y))
        for power, coefficient in enumerate(result):
            expected = one if power == 0 else zero
            for index in range(f.degree):
                f.budget.check(coefficient[index] == expected[index], "Bezout_coefficient_identity")
        audited.append({"reused_other_row": row["reused_other_row"],
                        "verified_product_coefficients": [encoded(x) for x in result]})
    return audited


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(proof, certificates):
    proof, certificates = Path(proof), Path(certificates)
    if not proof.is_file() or not certificates.is_file():
        raise FileNotFoundError("Saved reviewed geometry and existing certificates required")
    if OUTPUT.exists():
        raise FileExistsError("No overwrite and no new evaluation performed")
    started_cpu, started_wall = time.process_time(), time.perf_counter()
    budget = Budget()
    cases = prepare_cases(budget)
    certificate_audit = audit_saved_certificates(certificates, cases[0]["field"])
    results = [audit_case(case, budget) for case in cases]
    payload = {"status": "EXPERIMENTAL exact finite audit; symbolic geometry is a separate proof",
               "date": "2026-10-11", "scope": "Two frozen families times three orders; complete admissible-locus intersections, not full division-point enumeration",
               "orders": ORDERS, "limits": LIMITS,
               "counts": dict(budget.counts), "check_categories": dict(budget.check_categories),
               "P_methods": dict(budget.P_methods), "certificate_audit": certificate_audit,
               "cases": results,
               "provenance": {"python": platform.python_version(), "network": "none", "randomness": "none",
                   "source_sha256": sha(Path(__file__)),
                   "compatibility_proof": {"path": str(proof), "sha256": sha(proof)},
                   "saved_certificates": {"path": str(certificates), "sha256": sha(certificates)},
                   "command": f"python3 {Path(__file__).relative_to(Path.cwd())} --compatibility-proof {proof} --attachment-certificates {certificates}",
                   "cpu_seconds": time.process_time()-started_cpu,
                   "wall_seconds": time.perf_counter()-started_wall, "errors": []}}
    with OUTPUT.open("x", encoding="utf-8") as stream:
        json.dump(payload, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps({"summaries": [r["summary"] for r in results], "counts": dict(budget.counts),
                      "output": str(OUTPUT), "output_sha256": sha(OUTPUT),
                      "provenance": payload["provenance"]}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compatibility-proof", required=True)
    parser.add_argument("--attachment-certificates", required=True)
    arguments = parser.parse_args()
    run(arguments.compatibility_proof, arguments.attachment_certificates)
