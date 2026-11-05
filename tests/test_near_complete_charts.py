"""Independent tiny exact oracles; no research grid is executed."""
from fractions import Fraction as F
from itertools import combinations
import unittest
from experiments.near_complete_charts import (
    Budget, LIMITS, build_completion, coverage_profile, full_fibers, pair_at)


class NearCompleteTests(unittest.TestCase):
    def test_full_square_and_exact_budget_optimum(self):
        budget = Budget()
        fibers, outputs = full_fibers([0, 1], budget)
        self.assertEqual(fibers, {F(0): [(F(0), F(0)), (F(0), F(1))],
                                  F(2): [(F(1), F(0)), (F(1), F(1))]})
        profile = coverage_profile(fibers, 2)
        self.assertEqual(profile["cumulative_coverage"], [0, 2, 4])
        self.assertEqual(profile["threshold_tails"]["3"]["B"], 4)
        pairs = list(outputs)
        for k in range(3):
            scores = []
            coverages = []
            for count in range(5):
                for subset in combinations(pairs, count):
                    Z = len({outputs[pair] for pair in subset})
                    if Z <= k:
                        scores.append(Z+4-count)
                        coverages.append(count)
            self.assertEqual(min(scores), k+4-profile["cumulative_coverage"][k])
            self.assertEqual(max(coverages), profile["cumulative_coverage"][k])
        self.assertEqual(budget.P_evaluations, 4)

    def test_rational_threecycle_and_pole_exclusion(self):
        u, z = F(2), F(3)
        seen = []
        for _ in range(3):
            x, y = pair_at(u, z)
            self.assertEqual((x-y)*(x-y)*(x-y)+x+y, z)
            seen.append(u)
            u = 1-1/u
        self.assertEqual(seen, [F(2), F(1, 2), F(-1)])
        self.assertEqual(u, F(2))
        seed, labels, poles = build_completion([0, 1], "mobius_threecycle", Budget())
        self.assertEqual(len(poles), 3)  # Both diagonal sources and u=1.
        self.assertEqual(len(labels), 6)
        for _, _, _, (x, y), target in labels:
            self.assertEqual((x-y)*(x-y)*(x-y)+x+y, target)

    def test_adaptive_completion_exact_pairs(self):
        budget = Budget()
        seed, labels, poles = build_completion([0, F(1, 2)], "adaptive_linear", budget)
        self.assertFalse(poles)
        self.assertEqual(len(labels), 12)
        self.assertEqual(budget.P_evaluations, 4)
        for branch, i, j, (x, y), target in labels:
            source_x, source_y = seed[i], seed[j]
            source_output = (source_x-source_y)**3+source_x+source_y
            self.assertEqual(target, source_output)
            self.assertEqual((x-y)**3+x+y, source_output)
            expected_step = 0 if branch == 0 else source_output/2*(1 if branch == 1 else -1)
            self.assertEqual(x-y, source_x-source_y+expected_step)

    def test_preflight_rejects_before_square(self):
        budget = Budget()
        with self.assertRaises(RuntimeError):
            full_fibers(range(LIMITS["N"]+1), budget)
        self.assertEqual(budget.P_evaluations, 0)
        budget.P_evaluations = LIMITS["P_evaluations"]
        with self.assertRaises(RuntimeError):
            full_fibers([0], budget)
        self.assertEqual(budget.P_evaluations, LIMITS["P_evaluations"])


if __name__ == "__main__":
    unittest.main()

