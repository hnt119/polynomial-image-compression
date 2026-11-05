"""Meaningful exact-arithmetic and all-pairs checks for the multiplier diagnostics."""

from collections import Counter
from fractions import Fraction
import unittest

from experiments.eisenstein_solvable import (
    Budget, BudgetExceeded, Multiquadratic, case, construct, full_image,
    integerize, return_tail, run,
)


class EisensteinSolvableTests(unittest.TestCase):
    def test_multiquadratic_independent_product(self):
        k = Multiquadratic((2, 3))
        a = (1, 1, 1, 0)  # 1 + sqrt(2) + sqrt(3)
        self.assertEqual(k.mul(a, a), (6, 2, 2, 2))
        self.assertEqual(k.mul((0, 0, 0, 1), (0, 0, 0, 1)), (6, 0, 0, 0))

    def test_norm_preserved_and_inverse_returns(self):
        k = Multiquadratic((2, 3, 5))
        z = (k.add(k.one, k.root(2)), k.sub(k.root(0), k.root(1)))
        for i in range(3):
            u = k.multiplier(i)
            w = k.eisenstein_mul(u, z)
            self.assertEqual(k.q(*w), k.q(*z))
            self.assertEqual(k.eisenstein_mul(k.conjugate(u), w), z)

    def test_denominator_clear_is_exact(self):
        values = [(Fraction(1, 3), Fraction(1, 2)), (Fraction(-2, 5), 0)]
        denominator, integers = integerize(values)
        self.assertEqual(denominator, 30)
        self.assertEqual(integers, [(10, 15), (-12, 0)])

    def test_full_image_against_scalar_oracle(self):
        k = Multiquadratic((2,))
        raw = (-2, -1, 0, 1, 2)
        carrier = [k.constant(a) for a in raw]
        budget = Budget()
        got = full_image(k, carrier, budget)
        expected = Counter((a*a + a*b + b*b, 0) for a in raw for b in raw)
        self.assertEqual(got, expected)
        self.assertEqual(budget.pairs, 25)

    def test_fraction_oracle_for_returns_and_zero(self):
        k, rational, _, multipliers = construct("F1", 1)
        denominator, integers = integerize(sorted(rational))
        got = return_tail(k, integers, multipliers, Budget())
        expected = Counter()
        for a in rational:
            for b in rational:
                if (a, b) == (k.zero, k.zero):
                    continue
                # Independent Fraction coefficient evaluation, without denominator divisibility.
                count = sum(1 for u in multipliers
                            if all(c in rational for c in k.eisenstein_mul(u, (a, b))))
                expected[count] += 1
        self.assertEqual(got["nonzero_pairs_by_return_count"], dict(sorted(expected.items())))
        self.assertEqual(got["zero_pairs_charged_as_exception"], 1)
        self.assertGreater(denominator, 1)

    def test_case_counts_match_rational_oracle(self):
        k, rational, _, _ = construct("F3", 1)
        expected = Counter(k.q(a, b) for a in rational for b in rational)
        result = case("F3", 1, Budget())
        self.assertEqual(result["full_image_size"], len(expected))
        self.assertEqual(result["output_fibers_by_multiplicity"],
                         dict(sorted(Counter(expected.values()).items())))
        self.assertEqual(result["ordered_pairs"], len(rational) ** 2)

    def test_pair_and_action_budget_reject_before_extra_work(self):
        budget = Budget(pair_cap=1, action_cap=1)
        budget.pair()
        budget.action()
        with self.assertRaises(BudgetExceeded):
            budget.pair()
        with self.assertRaises(BudgetExceeded):
            budget.action()
        self.assertEqual((budget.pairs, budget.actions), (1, 1))

    def test_out_of_scope_family_rejected(self):
        with self.assertRaises(ValueError):
            construct("F1", 4)
        with self.assertRaises(ValueError):
            construct("F2", 3)
        with self.assertRaises(ValueError):
            run(cpu_cap=float("nan"))
        budget = Budget()
        construct("F1", 2, budget)
        self.assertEqual(budget.pairs, 2)


if __name__ == "__main__":
    unittest.main()
