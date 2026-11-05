"""Independent small arithmetic oracles for the elliptic scout."""
from fractions import Fraction as F
from collections import Counter
import unittest
from experiments.elliptic_geometry import BASE, add, on_curve, sharing_pairs, evaluate


class EllipticGeometryTests(unittest.TestCase):
    def test_group_law_known_points_and_inverse(self):
        self.assertTrue(on_curve(BASE))
        doubled = add(BASE, BASE)
        self.assertEqual(doubled, (F(41), F(-227)))
        fourth = add(doubled, doubled)
        self.assertTrue(on_curve(fourth))
        self.assertEqual(fourth[0], F(8048513, 206116))
        self.assertIsNone(add(BASE, (BASE[0], -BASE[1])))
        self.assertEqual(add(None, BASE), BASE)

    def test_inverse_map_and_full_small_square(self):
        points = [BASE, add(BASE, BASE)]
        labels = [pair for point in points for pair in sharing_pairs(point)]
        self.assertEqual(labels[:2], [(F(0), F(-2)), (F(0), F(0))])
        self.assertEqual(labels[2][0]-labels[2][1], F(-11, 222))
        self.assertEqual(labels[3][0]-labels[3][1], F(-443, 222))
        A = {x for pair in labels for x in pair}
        self.assertEqual(len(A), 5)
        self.assertEqual([evaluate(*pair) for pair in labels], [6, 0, 6, 0])
        fibers = Counter(evaluate(x, y) for x in A for y in A)
        self.assertEqual(Counter(fibers.values()), {1: 21, 2: 2})


if __name__ == "__main__":
    unittest.main()
