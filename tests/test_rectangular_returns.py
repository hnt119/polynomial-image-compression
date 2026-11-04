"""Small tests of rectangle membership, zero, and the prescribed threshold."""
from fractions import Fraction as F
import unittest

from experiments.rectangular_returns import fourth_root_ceiling, measure
from experiments.unit_exponent import Budget


class RectangularReturnsTests(unittest.TestCase):
    def test_return_must_stay_in_oriented_rectangle(self):
        U = [(F(1), F(0)), (F(-1), F(0)), (F(15, 13), F(8, 13))]
        report, raw = measure([-1, 1], [-3, 3], U, Budget(cap=100))
        self.assertEqual(report['R_pair']['histogram'], {2: 4})
        self.assertEqual(report['return_domain_sizes'], [4, 4, 0])
        self.assertEqual(report['symmetric_difference'], 4)
        self.assertEqual(report['rectangular_Q_image'], 2)

    def test_zero_has_one_target(self):
        report, raw = measure([0], [0], [(F(1), F(0)), (F(-1), F(0))], Budget(cap=10))
        self.assertEqual(report['R_pair']['histogram'], {1: 1})
        self.assertEqual(report['R_action']['histogram'], {2: 1})

    def test_integer_threshold_includes_exact_fourth_powers(self):
        self.assertEqual([fourth_root_ceiling(n) for n in (1, 8, 16, 17, 81, 96)], [1, 2, 2, 3, 3, 4])


if __name__ == '__main__':
    unittest.main()
