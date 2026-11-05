"""Small independent Fraction oracles for the high-return finite scout.

The schedules below are fixed regression cases, not a carrier search.
No test calls the module's main research schedule.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
import unittest

from experiments.cartesian_returns import (
    BACKWARD,
    FORWARD,
    IDENTITY,
    Budget,
    BudgetExceeded,
    apply_rational,
    compose,
    construct,
    digest,
    powers,
    run_case,
)


def oracle_action(exponent, x, y):
    """Repeated rational action, independent of integer matrix powering."""
    x, y = Fraction(x), Fraction(y)
    for _ in range(abs(exponent)):
        if exponent > 0:
            x, y = (8*x + 5*y)/7, (-5*x + 3*y)/7
        else:
            x, y = (3*x - 5*y)/7, (5*x + 8*y)/7
    return x, y


def oracle_q(x, y):
    return x*x + x*y + y*y


def decode_histogram(values):
    return Counter({int(key): value for key, value in values.items()})


class CartesianReturnTests(unittest.TestCase):
    def test_power_actions_against_fraction_recurrence(self):
        self.assertEqual(compose(FORWARD, BACKWARD), IDENTITY)
        self.assertEqual(compose(BACKWARD, FORWARD), IDENTITY)
        self.assertEqual(apply_rational(FORWARD, 1, -3), (-1, -2))
        points = ((0, 1), (Fraction(-2, 7), Fraction(3, 7)), (1, -3))
        for exponent, matrix in powers(3):
            self.assertGreater(matrix[-1], 0)
            for x, y in points:
                with self.subTest(exponent=exponent, point=(x, y)):
                    actual = apply_rational(matrix, x, y)
                    self.assertEqual(actual, oracle_action(exponent, x, y))
                    self.assertEqual(oracle_q(*actual), oracle_q(x, y))

    def test_small_full_pair_counts_projection_and_zero_tail(self):
        cases = (
            (('strata', 1, 1),
             {Fraction(-1), Fraction(-1, 7), Fraction(1, 7), Fraction(1)}),
            (('strata', 4, 0),
             {Fraction(i) for i in range(-4, 5) if i}),
            (('orbit_box', 1, 0),
             {Fraction(-1), Fraction(0), Fraction(1)}),
        )
        for spec, expected_input in cases:
            with self.subTest(spec=spec):
                budget = Budget(cap=5000)
                result = run_case(spec, budget)
                carrier = {Fraction(num, den) for num, den in result['carrier']}
                self.assertEqual(carrier, expected_input)
                n = len(carrier)
                denominator = result['common_denominator']
                self.assertTrue(all((x*denominator).denominator == 1 for x in carrier))
                exponents = result['action_exponents']
                self.assertIn(0, exponents)

                images = Counter()
                raw, effective, nonzero, stabilizers = (Counter() for _ in range(4))
                for x, y in product(carrier, repeat=2):
                    images[oracle_q(x, y)] += 1
                    returned = [oracle_action(j, x, y) for j in exponents]
                    returned = [(u, v) for u, v in returned if u in carrier and v in carrier]
                    raw[len(returned)] += 1
                    effective[len(set(returned))] += 1
                    stabilizers[sum(pair == (x, y) for pair in returned)] += 1
                    if x or y:
                        nonzero[len(returned)] += 1

                self.assertEqual(result['input_size'], n)
                self.assertEqual(result['ordered_pairs'], n*n)
                self.assertEqual(result['full_image_size'], len(images))
                self.assertEqual(
                    decode_histogram(result['image_multiplicity_distribution']),
                    Counter(images.values()),
                )
                cleared_images = sorted(
                    (int(value*denominator*denominator), count)
                    for value, count in images.items()
                )
                self.assertEqual(result['output_fibers_sha256'], digest(cleared_images))

                for field, expected in (
                    ('raw_return_distribution_all_pairs', raw),
                    ('distinct_returned_pair_distribution', effective),
                    ('return_distribution_nonzero', nonzero),
                ):
                    self.assertEqual(decode_histogram(result[field]['histogram']), expected)
                    self.assertEqual(result[field]['population'], sum(expected.values()))
                    self.assertEqual(result[field]['sum'], sum(k*v for k, v in expected.items()))
                self.assertEqual(
                    decode_histogram(result['stabilizer_distribution_all_pairs']), stabilizers,
                )
                self.assertEqual(sum(row[-1] for row in result['state_transition_counts']),
                                 sum(k*v for k, v in raw.items()))

                zero = int(Fraction(0) in carrier)
                self.assertEqual(result['zero_exception_count'], zero)
                for item in result['return_tail']:
                    threshold = item['threshold']
                    exceptional = zero + sum(v for k, v in nonzero.items() if k < threshold)
                    bound = Fraction(n*n, threshold) + exceptional
                    self.assertEqual(item['exceptional_pair_count'], exceptional)
                    self.assertEqual(item['support_bound_exact'],
                                     [bound.numerator, bound.denominator])
                    self.assertEqual(item['minimum_outside_exception'],
                                     min((k for k in nonzero if k >= threshold), default=None))
                    self.assertLessEqual(len(images), bound)

                self.assertEqual(result['evaluations']['polynomial'], n*n)
                self.assertEqual(result['evaluations']['return_action'], n*n*len(exponents))
                self.assertEqual(result['evaluations']['multiplier_norm'], len(exponents))
                self.assertEqual(budget.total, sum(result['evaluations'].values()))

    def test_one_repair_step_is_full_cartesian_completion(self):
        budget = Budget(cap=100)
        carrier, group, engineered, metadata = construct('repair', 1, 1, budget)
        seed = {Fraction(-1), Fraction(0), Fraction(1)}
        expected = set(seed)
        for exponent in (-1, 1):
            for x, y in product(seed, repeat=2):
                expected.update(oracle_action(exponent, x, y))
        self.assertEqual(set(carrier), expected)
        self.assertEqual(metadata['stage_sizes'], [3, 13])
        self.assertEqual(metadata['previous_square_count'], 9)
        self.assertEqual([j for j, _ in group], list(range(-3, 4)))
        self.assertEqual(engineered, set())
        self.assertEqual(budget.counts, Counter(construction_action=18))

    def test_preflight_and_budget_do_not_overspend(self):
        budget = Budget(cap=1)
        with self.assertRaises(BudgetExceeded):
            run_case(('strata', 1, 1), budget)
        self.assertEqual(budget.total, 0)
        self.assertEqual(budget.counts, Counter())
        budget = Budget(cap=2)
        budget.charge('regression')
        budget.charge('regression')
        with self.assertRaises(BudgetExceeded):
            budget.charge('regression')
        self.assertEqual(budget.total, 2)


if __name__ == '__main__':
    unittest.main()
