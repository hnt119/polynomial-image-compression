"""Exact invariants of the bounded T01 rational gadget certificate."""

from fractions import Fraction as Q
import unittest

from experiments.three_branch_lift import analyze, grid, image, polynomial


class ThreeBranchLiftTests(unittest.TestCase):
    def test_predeclared_budget(self):
        trials = list(grid())
        self.assertEqual(len(trials), 980)
        self.assertLessEqual(max(len(seed) for _, seed, _ in trials), 6)
        self.assertEqual(len({identifier for identifier, _, _ in trials}), 980)

    def test_two_point_row_collapse(self):
        self.assertEqual(image([Q(0), Q(1)]), {Q(0), Q(2)})
        for x in (Q(0), Q(1)):
            for y in (Q(0), Q(1)):
                self.assertEqual(polynomial(x, y), 2 * x)

    def test_complete_blocks_and_intersections(self):
        record = analyze([Q(0), Q(1, 2)], [(2, 0), (2, 2), (2, 4)], "ap6")
        self.assertTrue(record["accepted"])
        self.assertEqual((record["s"], record["s_prime"]), (4, 24))
        blocks = [set(map(Q, block)) for block in record["block_images"]]
        all_values = set().union(*blocks)
        self.assertEqual(all_values, image(list(map(Q, range(6)))))
        for value, mask in record["membership_masks"]:
            self.assertEqual(mask, sum(1 << j for j in range(9) if Q(value) in blocks[j]))
        for mask in range(1, 512):
            selected = [blocks[j] for j in range(9) if mask & (1 << j)]
            direct = set.intersection(*selected)
            encoded = {Q(z) for z, bits in record["membership_masks"] if bits & mask == mask}
            self.assertEqual(direct, encoded)

    def test_rejects_overlapping_branches(self):
        record = analyze(range(3), [(1, 0), (1, 1), (1, 2)], "overlap")
        self.assertFalse(record["accepted"])
        self.assertFalse(record["branch_disjoint"])
        self.assertNotIn("s_prime", record)

    def test_best_gadget_independent_exact_oracle(self):
        record = analyze([0, 2], [(Q(1, 2), Q(r, 3)) for r in range(3)], "best")
        self.assertEqual((record["s"], record["s_prime"]), (4, 22))
        self.assertEqual(set(map(Q, record["old_image"])), set(map(Q, (-6, 0, 4, 10))))
        # Derived separately from the integer slice identity
        # 27 P(i/3,j/3) = (i-j)^3 + 9(i+j).
        numerators = [-80, -28, -10, 0, 8, 10, 18, 26, 28, 36, 44,
                      46, 54, 62, 64, 72, 80, 82, 90, 100, 118, 170]
        masks = [4, 2, 32, 1, 2, 12, 16, 96, 136, 256, 66,
                 132, 1, 34, 12, 16, 96, 128, 256, 8, 128, 64]
        self.assertEqual(list(map(Q, record["complete_image"])),
                         [Q(n, 27) for n in numerators])
        self.assertEqual(record["membership_masks"],
                         [[str(Q(n, 27)), mask] for n, mask in zip(numerators, masks)])
        self.assertEqual(record["sum_block_sizes"], 30)
        self.assertEqual(record["overlap_saving"], 8)

    def test_difference_collision_formula(self):
        # A known pair of distinct difference slices of the AP6 gadget.
        x, y, u, v = map(Q, (2, 0, 5, 4))
        d, e = x - y, u - v
        self.assertEqual(polynomial(x, y), polynomial(u, v))
        self.assertEqual(y - v, (e - d) * (d * d + d * e + e * e + 1) / 2)


if __name__ == "__main__":
    unittest.main()
