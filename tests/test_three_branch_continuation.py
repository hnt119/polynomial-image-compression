"""Independent finite oracles and accounting invariants for continuation data."""

from fractions import Fraction as Q
import unittest

from experiments.three_branch_continuation import (
    Budget, GADGET, analyze_level, choose_maps, initial_certificate,
)


class ContinuationTests(unittest.TestCase):
    def test_initial_exact_support_and_template_completeness(self):
        budget = Budget()
        data = initial_certificate(budget)
        numerators = [-80, -28, -10, 0, 8, 10, 18, 26, 28, 36, 44,
                      46, 54, 62, 64, 72, 80, 82, 90, 100, 118, 170]
        self.assertEqual(list(map(Q, data["outputs"])), [Q(n, 27) for n in numerators])
        self.assertEqual(data["template_savings"], 14)
        self.assertEqual(data["extra_savings"], 0)
        self.assertEqual(sum(data["output_multiplicities"]), 36)
        self.assertEqual(sum(d["mass"] for d in data["difference_slices"]), 36)
        self.assertEqual(budget.evaluations, 36)

    def test_overlapping_branches_do_not_multiply_scalar_fibers(self):
        budget = Budget()
        data = analyze_level(GADGET, 22, [(Q(1), Q(0))] * 3, budget)
        self.assertEqual((data["n"], data["s"]), (6, 22))
        self.assertEqual(data["polynomial_evaluations"], 324)
        self.assertEqual(data["unique_pair_count"], 36)
        self.assertEqual(data["repeated_branch_pair_evaluations"], 288)
        self.assertEqual(sum(data["output_multiplicities"]), 36)
        self.assertEqual(set(data["block_membership_masks"]), {511})
        self.assertEqual(data["normalized_ratio"], "1")

    def test_prime_translation_rule_and_exact_separation_rule(self):
        maps, p = choose_maps("intact_third_shift", GADGET, 1, 3)
        self.assertEqual(p, 5)
        self.assertEqual(maps, [(Q(1), Q(r) * Q(8, 15)) for r in range(3)])
        maps, p = choose_maps("exact_third_translations", GADGET, 1, 3)
        self.assertEqual(p, 7)
        self.assertEqual(maps, [(Q(1, 7), Q(r, 3)) for r in range(3)])
        self.assertLess((max(GADGET) - min(GADGET)) / p, Q(1, 3))

    def test_preflight_rejects_before_evaluation(self):
        budget = Budget()
        with self.assertRaises(RuntimeError):
            budget.preflight(1, 163)
        self.assertEqual(budget.evaluations, 0)
        self.assertEqual(budget.steps, 0)


if __name__ == "__main__":
    unittest.main()
