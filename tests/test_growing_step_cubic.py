"""Whole-fiber and finite-induced-graph oracles, including a subgroup trap."""

from fractions import Fraction as Q
from itertools import product
import unittest

from experiments.growing_step_cubic import Budget, carrier_definitions, enumerate_fibers, graph_case, inventories


class GrowingStepTests(unittest.TestCase):
    def test_carrier_inventory_preflight(self):
        carriers = list(carrier_definitions())
        self.assertEqual(len(carriers), 32)
        self.assertLessEqual(max(len(a) for _, _, a, _ in carriers), 128)

    def test_subgroup_coset_does_not_imply_connectedness(self):
        budget = Budget()
        carrier = enumerate_fibers([-5, -3, 0], budget)
        zero = next(i for i, f in enumerate(carrier["fibers"]) if f["output"] == "0")
        self.assertEqual(carrier["fibers"][zero]["differences"], ["0", "2"])
        one = graph_case(carrier, "one", [1], budget, direct_oracle=True)
        two = graph_case(carrier, "two", [2], budget, direct_oracle=True)
        self.assertEqual(one["components_per_output"][zero], 2)
        self.assertEqual(two["components_per_output"][zero], 1)
        self.assertEqual(one["component_count"], 9)
        self.assertEqual(two["component_count"], 8)

    def test_gadget_exact_full_fibers_and_edge_direction(self):
        budget = Budget()
        carrier = enumerate_fibers([Q(j, 3) for j in range(6)], budget)
        case = graph_case(carrier, "one", [1], budget, direct_oracle=True)
        self.assertEqual(carrier["image_size"], 22)
        self.assertEqual(case["distinct_undirected_edges"], 14)
        self.assertEqual(case["directed_edge_count"], 14)
        self.assertEqual(case["nonisolated_vertices"], 28)
        self.assertEqual(case["component_size_distribution"], {"1": 8, "2": 14})

    def test_all_useful_graph_recovers_actual_fibers(self):
        budget = Budget()
        carrier = enumerate_fibers([0, 1, 2, 3], budget)
        label, steps = inventories(carrier)[-1]
        case = graph_case(carrier, label, steps, budget, direct_oracle=True)
        self.assertEqual(case["component_count"], carrier["image_size"])
        self.assertEqual(case["component_excess_over_image"], 0)
        self.assertEqual(case["missing_within_fiber_connections"], 0)
        self.assertTrue(case["diagnostic_only"])

    def test_faithful_boxes_independent_numeric_oracles(self):
        # These independently supplied exact counts test the new slice theorem;
        # they are not calculated by its E_1 formula inside the test.
        for rank, length, image, mass, maximum in ((2, 3, 69, 21, 3), (3, 2, 56, 16, 2)):
            with self.subTest(rank=rank, length=length):
                base = 100 * (length + 1) ** 3
                weights = [1] + [base ** (4 ** (i - 1)) for i in range(1, rank)]
                values = [sum(a * w for a, w in zip(digits, weights))
                          for digits in product(range(length), repeat=rank)]
                budget = Budget()
                carrier = enumerate_fibers(values, budget)
                case = graph_case(carrier, "one", [1], budget, direct_oracle=True)
                self.assertEqual(carrier["N"], length ** rank)
                self.assertEqual(carrier["image_size"], image)
                self.assertEqual(case["component_count"], image)
                self.assertEqual(case["nonisolated_vertices"], mass)
                self.assertEqual(case["largest_component"], maximum)


if __name__ == "__main__":
    unittest.main()
