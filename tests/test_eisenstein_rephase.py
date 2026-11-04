"""Check that coordinate minimization preserves concrete engineered norm pairs."""

import unittest

from experiments.eisenstein_rephase import RephaseBudget, greedy_rephase
from experiments.eisenstein_solvable import BudgetExceeded, Multiquadratic, construct


class EisensteinRephaseTests(unittest.TestCase):
    def test_nontrivial_move_preserves_norm(self):
        k = Multiquadratic((2,))
        identity = k.one, k.zero
        u = k.multiplier(0)
        result = greedy_rephase(k, {u}, {identity, u, k.conjugate(u)}, RephaseBudget())
        self.assertEqual(len(result["placement"]), 1)
        self.assertEqual(k.q(*result["placement"][0]), k.q(*u))
        self.assertLess(len(result["carrier"]), result["initial_input_size"])
        self.assertTrue(result["single_word_local_optimum"])
        self.assertGreater(sum(row["accepted_moves"] for row in result["trace"]), 0)

    def test_collision_guard_preserves_distinct_f3_words(self):
        k, _, words, multipliers = construct("F3", 1)
        result = greedy_rephase(k, words, multipliers, RephaseBudget())
        self.assertEqual(len(set(result["placement"])), len(words))
        for original, placed in zip(result["original"], result["placement"]):
            self.assertEqual(k.q(*original), k.q(*placed))
        self.assertLessEqual(len(result["carrier"]), result["initial_input_size"])

    def test_candidate_budget(self):
        budget = RephaseBudget(candidate_cap=1)
        budget.candidate(generation=True)
        with self.assertRaises(BudgetExceeded):
            budget.candidate()
        self.assertEqual((budget.generated, budget.scored), (1, 0))


if __name__ == "__main__":
    unittest.main()
