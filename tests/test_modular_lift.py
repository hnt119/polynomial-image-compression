"""Targeted arithmetic checks, not additional lift search cases."""
import unittest
from experiments.modular_lift import Field, cyclotomic


class ModularLiftArithmeticTests(unittest.TestCase):
    def test_cyclotomic_moduli(self):
        self.assertEqual(cyclotomic(6), [1, -1, 1])
        self.assertEqual(cyclotomic(42), [1, 1, 0, -1, -1, 0, 1, 0, -1, -1, 0, 1, 1])

    def test_integer_scaled_coordinates(self):
        f = Field(6)
        for u in f.powers:
            x, y = f.decode3(u)
            self.assertEqual(f.conj(x), x)
            self.assertEqual(f.conj(y), y)
            self.assertEqual(f.q(x, y), f.scale(f.one, 9))

    def test_wrapped_carry_is_not_real_equality(self):
        n, t = 49, 20
        q = lambda x, y: x*x+x*y+y*y
        self.assertEqual(q(t, n-2*t)-q(t, t), n*(n-3*t))
        self.assertNotEqual(q(t, n-2*t), q(t, t))
