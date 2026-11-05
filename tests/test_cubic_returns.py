"""Exact conjugacy, return-formula and graph-coverage oracles."""

from fractions import Fraction as Q
import unittest

from experiments.cubic_returns import Budget, analyze, fixed_candidates, inverse_coordinates, motion, polynomial


class CubicReturnTests(unittest.TestCase):
    def test_conjugacy_and_composition(self):
        for x, y in ((Q(0), Q(1)), (Q(2, 3), Q(-5, 7)), (Q(4), Q(9))):
            u, z = x - y, polynomial(x, y)
            self.assertEqual(inverse_coordinates(u, z), (x, y))
            for tau in (Q(1), Q(-2), Q(2, 3)):
                pair = motion(x, y, tau)
                self.assertEqual(pair, inverse_coordinates(u + tau, z))
                self.assertEqual(polynomial(*pair), z)
                self.assertEqual(motion(*pair, Q(1, 3)), motion(x, y, tau + Q(1, 3)))

    def test_two_point_graph_complete_oracle(self):
        data = analyze([0, 1], Budget())
        self.assertEqual((data["E1"], data["E1_from_fibers"], data["E1_from_slices"]), (2, 2, 2))
        self.assertEqual(data["components"], 2)
        self.assertEqual(data["path_vertex_size_distribution"], {"2": 2})
        self.assertEqual(data["paths"], [[1, 0], [3, 2]])
        self.assertEqual(data["image_size"], 2)
        self.assertEqual(data["maximum_actual_fiber"], 2)
        self.assertEqual(data["vertex_weighted_mean_forward_steps"], "1/2")

    def test_six_point_known_image_and_path_inequality(self):
        data = analyze([Q(i, 3) for i in range(6)], Budget())
        self.assertEqual(data["image_size"], 22)
        self.assertEqual(data["E1"], 14)
        self.assertEqual(data["components"], 22)
        self.assertEqual(data["path_vertex_size_distribution"], {"1": 8, "2": 14})
        self.assertEqual(sum(map(len, data["paths"])), 36)
        self.assertEqual(sum(f["size"] for f in data["fibers"]), 36)

    def test_fixed_inventory_and_preflight(self):
        candidates = list(fixed_candidates())
        self.assertEqual(len(candidates), 97)
        self.assertLessEqual(max(len(a) for _, _, a, _ in candidates), 256)
        budget = Budget()
        with self.assertRaises(RuntimeError):
            budget.reserve(257)
        self.assertEqual(budget.pair_checks, 0)


if __name__ == "__main__":
    unittest.main()
