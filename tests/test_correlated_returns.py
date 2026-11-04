"""Small correctness tests, not additional carrier scouting."""
import unittest
from fractions import Fraction as F
from experiments.correlated_returns import crt_carrier, factor_divides, diagonal_product


class CorrelatedReturnsTests(unittest.TestCase):
    def test_centered_crt_has_exact_residue_product(self):
        carrier, modulus = crt_carrier(((7, (2, -1)), (13, (3, -1))))
        self.assertEqual((len(carrier), modulus), (9, 91))
        self.assertEqual(len({(int(x) % 7, int(x) % 13) for x in carrier}), 9)
        self.assertTrue(all(-45 <= x <= 45 and x != 0 for x in carrier))
        self.assertTrue(all(pow(int(x), 3, p) == 1 for x in carrier for p in (7, 13)))

    def test_divisibility_orientation(self):
        alpha = (F(2), F(-1))
        conjugate_alpha = (F(3), F(1))
        self.assertTrue(factor_divides(alpha, F(2), F(1)))
        self.assertFalse(factor_divides(conjugate_alpha, F(2), F(1)))
        self.assertFalse(factor_divides(alpha, F(1), F(1)))

    def test_diagonal_uses_simultaneous_residues(self):
        blocks = ((7, (2, -1)), (13, (3, -1)))
        self.assertEqual(diagonal_product(blocks, F(1), F(8)), (7, 1))
        self.assertEqual(diagonal_product(blocks, F(1), F(92)), (91, 2))


if __name__ == '__main__':
    unittest.main()
