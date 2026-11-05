"""Small exact oracles for the one released variable-gap motif family.

No analyze/run call: these tests use five P evaluations on one worked motif,
not another complete-square enumeration or an alternative carrier family.
"""
import unittest

from experiments.variable_gap_sharing import (
    Budget, CASES, canonical_partners, endpoints, evaluate, motif_pairs, window,
)


class VariableGapSharingTests(unittest.TestCase):
    def test_worked_output_first_motif(self):
        budget = Budget()
        budget.charge("instances")
        labels = ((1, 1), (-3, -2), (2, 1), (-12, -3), (6, 2))
        expected_pairs = ((1, 0), (0, 2), (2, 1), (0, 3), (3, 1))
        self.assertEqual(tuple(endpoints(*label) for label in labels), expected_pairs)
        self.assertEqual(motif_pairs(1, 0, 2, 3), expected_pairs)
        self.assertEqual(tuple(evaluate(*pair, budget) for pair in expected_pairs),
                         (2, -6, 4, -24, 12))
        for j, u in labels:
            low, high = window(3, u)
            self.assertLessEqual(low, j)
            self.assertLessEqual(j, high)
        self.assertEqual(budget.counts["P_evaluations"], 5)

    def test_boundary_windows_and_canonical_blocks(self):
        self.assertEqual(window(3, -3), (-12, 11))
        self.assertEqual(window(3, 3), (15, 38))
        self.assertEqual(canonical_partners(3, 1, 0), (0, (2, 3)))
        self.assertEqual(canonical_partners(3, 26, 23), (23, (24, 25)))
        self.assertEqual(canonical_partners(5, 124, 123), (119, (119, 120, 121, 122)))

    def test_scope_and_budget(self):
        self.assertEqual(CASES, (3, 4, 5))
        with self.assertRaises(ValueError):
            window(2, 1)
        with self.assertRaises(ValueError):
            window(3, 0)
        with self.assertRaises(ValueError):
            canonical_partners(3, 0, 4)
        budget = Budget()
        budget.limits["P_evaluations"] = 0
        with self.assertRaises(RuntimeError):
            evaluate(1, 0, budget)
        self.assertEqual(budget.counts["P_evaluations"], 0)


if __name__ == "__main__":
    unittest.main()
