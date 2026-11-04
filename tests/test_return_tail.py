"""Small arithmetic checks; these do not rerun the scout cases."""
import unittest
from experiments.return_tail import (key, conjugate, multiply, add, scale, trace,
                                    complex_pair, target_times_three,
                                    matrix_coefficients_times_three,
                                    matrix_target_times_three)


class ReturnTailTests(unittest.TestCase):
    def test_cyclotomic_relation_and_nonzero_monomial(self):
        p = 11
        self.assertEqual(key({i: (1, 0) for i in range(p)}, p), key({}, p))
        self.assertNotEqual(key({p-1: (1, 0)}, p), key({}, p))

    def test_conjugation_is_involutive_and_trace_real(self):
        p = 11
        u = {3: (0, 1)}
        self.assertEqual(key(conjugate(conjugate(u, p), p), p), key(u, p))
        self.assertEqual(key(conjugate(trace(u, p), p), p), key(trace(u, p), p))
        self.assertEqual(key(multiply(u, conjugate(u, p), p), p), key({0: (1, 0)}, p))

    def test_three_scaled_oracles_on_distinct_input_traces(self):
        p = 11
        x, y = trace({2: (1, 0)}, p), trace({4: (0, 1)}, p)
        z = complex_pair(x, y)
        for u in ({0: (1, 0)}, {0: (-1, 0)}, {3: (0, 1)}):
            actual = target_times_three(u, z, p)
            other = matrix_target_times_three(matrix_coefficients_times_three(u, p), x, y, p)
            self.assertEqual(actual, other)
        self.assertEqual(target_times_three({0: (1, 0)}, z, p),
                         (key(scale(x, (3, 0)), p), key(scale(y, (3, 0)), p)))


if __name__ == '__main__':
    unittest.main()
