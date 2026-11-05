"""Exact small oracles; run only after compatibility release.

The successful run performs 25 charged P evaluations (9+16), two compatibility
triples and two inverse checks outside analyze. Internal checks are counted
by Budget; the eight additional geometric checks are charged in the report.
No saved artifacts or unrequested strip lengths are created.
"""
from fractions import Fraction as F
import unittest

from experiments.sharing_compatibility import (
    Budget, CASES, analyze, endpoints, p_coefficient, triangle_compatibility,
)


class SharingCompatibilityTests(unittest.TestCase):
    def test_m1_complete_hand_table(self):
        budget = Budget()
        budget.charge("instances")
        expected = ((0, 2, -2), (4, 6, 8), (14, 10, 12))
        actual = tuple(tuple(3*p_coefficient(a, b, budget) for b in range(3))
                       for a in range(3))
        self.assertEqual(actual, expected)
        self.assertEqual(budget.counts["P_evaluations"], 9)

    def test_m2_full_square_and_deduplication(self):
        budget = Budget()
        summary, raw = analyze(2, budget)
        expected = [["0", "2", "-2", "-18"], ["4", "6", "8", "4"],
                    ["14", "10", "12", "14"], ["36", "20", "16", "18"]]
        self.assertEqual(raw["worked_matrix_3P_over_r"], expected)
        self.assertEqual([summary[k] for k in ("N", "Q", "Z", "B", "full_image")],
                         [4, 5, 4, 11, 14])
        self.assertEqual(summary["fiber_histogram"], {1: 12, 2: 2})
        self.assertEqual(summary["strict_small_fiber_tails"],
                         {"1": 0, "2": 12, "3": 16, "4": 16, "5": 16})
        self.assertEqual(summary["Q_distinct_labels"], 5)
        self.assertEqual(summary["raw_triangle_labels"], 6)
        self.assertEqual(summary["safe_support_upper_bound"], 15)
        self.assertEqual(budget.counts["P_evaluations"], 16)

    def test_exact_inverse_and_compatibility(self):
        self.assertEqual(endpoints(F(2, 3), -1), (F(0), F(1)))
        self.assertEqual(endpoints(F(14, 3), 2), (F(2), F(0)))
        self.assertEqual(triangle_compatibility(-1, -1, 2), (True, True, True))
        self.assertNotEqual(triangle_compatibility(-1, -1, 1), (True, True, True))

    def test_scope_and_budget_fail_before_polynomial_evaluation(self):
        self.assertEqual(CASES, (1, 2, 3, 4, 8, 16, 32, 64))
        budget = Budget()
        with self.assertRaises(ValueError):
            analyze(5, budget)
        self.assertEqual(sum(budget.counts.values()), 0)
        budget.limits["P_evaluations"] = 0
        with self.assertRaises(RuntimeError):
            p_coefficient(0, 1, budget)
        self.assertEqual(budget.counts["P_evaluations"], 0)


if __name__ == "__main__":
    unittest.main()
