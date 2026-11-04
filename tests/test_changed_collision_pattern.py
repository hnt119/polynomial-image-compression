"""Small exact arithmetic checks for the already frozen conic-frame ladder.

The four seed row/column pairs use eight P evaluations across two methods.
This adds one repeated seed instance, not another carrier or a square rerun.
The lead runs these once with the repository suite; the research scout does not.
"""
import unittest
from fractions import Fraction as F

from experiments.changed_collision_pattern import (
    Budget, CASES, ONE, T, ZERO, add, constants, multiply,
    p_difference, p_expanded, reduce_polynomial, scale,
)


class ChangedCollisionPatternTests(unittest.TestCase):
    def test_faithful_modulus_reduction_and_power_table(self):
        self.assertEqual(reduce_polynomial([-1, 28, -80, 64]), ZERO)
        t3 = (F(1, 64), F(-7, 16), F(5, 4))
        self.assertEqual(multiply(multiply(T, T), T), t3)
        self.assertEqual(multiply(T, t3), (F(5, 256), F(-17, 32), F(9, 8)))
        self.assertEqual([(a**3+a*a+a+2) % 3 for a in range(3)], [2, 2, 1])

    def test_four_prescribed_seed_pairs_two_methods(self):
        budget = Budget()
        budget.charge("instances")
        r_over_h, s_over_h = constants()
        center = scale(r_over_h, -1)
        for row_sign in (-1, 1):
            x = add(center, scale(ONE, row_sign))
            expected = ZERO if row_sign < 0 else scale(r_over_h, -4)
            for column_sign in (-1, 1):
                y = add(center, scale(s_over_h, column_sign))
                primary = p_difference(x, y, budget)
                oracle = p_expanded(x, y, budget)
                budget.check(primary == oracle == expected, "seed_two_oracles_and_label")
        self.assertEqual(budget.counts["P_evaluations"], 8)
        self.assertEqual(budget.counts["compatibility_checks"], 4)

    def test_frozen_three_lengths(self):
        self.assertEqual(CASES, (1, 2, 3))


if __name__ == "__main__":
    unittest.main()
