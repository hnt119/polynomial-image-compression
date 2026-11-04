"""Tiny invariant/exception checks; the four carrier scouts are not rerun."""

from fractions import Fraction as F
import unittest

from experiments.dense_cartesianization import measure
from experiments.unit_exponent import Budget


class DenseReturnAccountingTests(unittest.TestCase):
    def test_origin_counts_one_pair_despite_all_action_labels(self):
        units = {0: (F(1), F(0)), 1: (F(0), F(1))}
        summary, raw = measure([0], units, {(F(0), F(0))}, 1, Budget(cap=20))
        self.assertEqual(summary["R_action"]["maximum"], 2)
        self.assertEqual(summary["R_pair"]["maximum"], 1)
        self.assertEqual(summary["controlled_G"], 0)
        self.assertEqual(summary["stabilizer_histogram"], {2: 1})
        self.assertEqual(raw["pairs"][0]["returned_pairs"], [(0, 0)])

    def test_mixed_root_rotation_has_seven_returns_on_ternary_square(self):
        units = {0: (F(1), F(0)), 1: (F(0), F(1))}
        summary, raw = measure([-1, 0, 1], units, set(), 1, Budget(cap=100))
        self.assertEqual(sum(1 in row["returning_action_indices"] for row in raw["pairs"]), 7)
        self.assertEqual(summary["controlled_G"], 6)
        self.assertEqual(summary["bad_B"], 3)
        self.assertEqual(summary["full_Q_image_size"], 3)
        self.assertEqual(summary["image_fiber_histogram"], {1: 1, 2: 1, 6: 1})


if __name__ == "__main__":
    unittest.main()
