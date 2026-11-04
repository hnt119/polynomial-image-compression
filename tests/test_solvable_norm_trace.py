"""Independent small exact checks for the commissioned field experiment."""

from collections import Counter
from itertools import product
import unittest

from experiments.solvable_norm_trace import Budget, FIELDS, Order, image_counts, sign_cube


class SolvableNormTraceTests(unittest.TestCase):
    def test_field_relations_and_traces(self):
        for name, f, unit, inverse in FIELDS:
            with self.subTest(field=name):
                ring = Order(f)
                self.assertEqual(ring.mul(unit, inverse), ring.one)
                self.assertEqual(ring.trace(ring.one), ring.degree)
                self.assertIn(ring.norm(unit), (-1, 1))
                self.assertEqual(ring.norm(tuple(2*v for v in ring.one)), 2 ** ring.degree)
        cubic = Order((-2, 0, 0))
        t = (0, 1, 0)
        self.assertEqual(cubic.mul(cubic.mul(t, t), t), (2, 0, 0))
        self.assertEqual(cubic.trace(t), 0)
        self.assertEqual(cubic.trace((1, 1, 1)), 3)
        self.assertEqual(cubic.norm(t), 2)
        self.assertEqual(cubic.norm((1, 1, 0)), 3)
        self.assertEqual(cubic.norm(cubic.zero), 0)

    def test_rational_oracle_and_all_ordered_pairs(self):
        a = (-2, 0, 1, 3)
        actual = image_counts(Order((0,)), {(x,) for x in a}, Budget())
        for name, linear in (("q", 0), ("q_plus_x", 1)):
            oracle = Counter(x*x + x*y + y*y + linear*x for x in a for y in a)
            self.assertEqual(actual[name]["image_size"], len(oracle))
            self.assertEqual(actual[name]["fiber_histogram"], dict(Counter(oracle.values())))
            self.assertEqual(sum(k*v for k, v in actual[name]["fiber_histogram"].items()), 16)

    def test_sign_cube_against_radical_multiplication(self):
        # Independent dense basis multiplication in Q(sqrt(2),sqrt(3)).
        def mul(x, y):
            out = [0] * 4
            for i in range(4):
                for j in range(4):
                    shared = i & j
                    out[i ^ j] += x[i] * y[j] * (2 if shared & 1 else 1) * (3 if shared & 2 else 1)
            return tuple(out)
        a = [(0, x, y, 0) for x, y in product((-1, 1), repeat=2)]
        q, p = set(), set()
        for x in a:
            for y in a:
                value = tuple(sum(z) for z in zip(mul(x, x), mul(x, y), mul(y, y)))
                q.add(value)
                p.add(tuple(s+t for s, t in zip(value, x)))
        actual = sign_cube((2, 3), Budget())
        self.assertEqual(len(q), 6)
        self.assertEqual(len(p), 16)
        self.assertEqual(actual["q"]["image_size"], len(q))
        self.assertEqual(actual["q_plus_x"]["image_size"], len(p))

    def test_budget_rejects_before_work(self):
        budget = Budget(pairs=7)
        with self.assertRaises(RuntimeError):
            image_counts(Order((0,)), {(1,), (2,)}, budget)
        self.assertEqual(budget.pairs, 0)


if __name__ == "__main__":
    unittest.main()
