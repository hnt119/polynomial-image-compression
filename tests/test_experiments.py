from contextlib import redirect_stderr, redirect_stdout
from fractions import Fraction
import io
import json
import unittest

from experiments.__main__ import main
from experiments.core import (
    POLYNOMIALS, arithmetic_carrier, carrier_image, deform, evaluate,
    geometric_carrier, is_prime, local_image,
)
from experiments.verification import finite_checks


class PolynomialTests(unittest.TestCase):
    def test_manual_integer_values(self):
        expected = {"baseline": 4, "quadratic": 26, "quartic": 626, "mixed-cubic": 6, "eisenstein": 7}
        for name, value in expected.items():
            with self.subTest(name=name):
                self.assertEqual(evaluate(name, 1, 2), value)
                self.assertIs(type(evaluate(name, 1, 2)), int)

    def test_manual_deformations(self):
        self.assertEqual(deform("baseline", 1, 2, 3), 10)
        self.assertEqual(deform("quadratic", 1, 2, 3), 28)
        self.assertEqual(deform("quartic", 1, 2, 3), 652)

    def test_rational_deformation_identity(self):
        for name, metadata in POLYNOMIALS.items():
            for q in (1, 2, 3, 11):
                for x, y in ((-5, 4), (0, -2), (3, 7)):
                    with self.subTest(name=name, q=q, x=x, y=y):
                        scaled = q ** metadata["degree"] * evaluate(name, Fraction(x, q), Fraction(y, q))
                        self.assertEqual(deform(name, x, y, q), scaled)
                        self.assertEqual(deform(name, q*x, q*y, q), q**metadata["degree"] * evaluate(name, x, y))

    def test_invalid_evaluations(self):
        with self.assertRaises(ValueError):
            evaluate("unknown", 1, 2)
        for value in (1.0, True, "1"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                evaluate("baseline", value, 1)
        for q in (0, -1, 1.0, True):
            with self.subTest(q=q), self.assertRaises(ValueError):
                deform("baseline", 1, 2, q)
        with self.assertRaises(ValueError):
            deform("baseline", Fraction(1, 2), 2, 1)


class LocalImageTests(unittest.TestCase):
    def test_manual_cubic_mod_two(self):
        # 00, 01, 10, 11 all give xy(x+y) = 0 modulo 2.
        result = local_image("mixed-cubic", 2)
        self.assertEqual(result["input_count"], 4)
        self.assertEqual(result["image"], [0])
        self.assertEqual(result["density"], Fraction(1, 2))

    def test_manual_square_mod_five(self):
        result = local_image("baseline", 5, 5)
        self.assertEqual(result["input_count"], 25)
        self.assertEqual(result["image"], [0, 1, 4])
        self.assertEqual(result["density"], Fraction(3, 5))

    def test_manual_fourth_powers(self):
        self.assertEqual(local_image("quartic", 5, 5)["image"], [0, 1])

    def test_prime_validation(self):
        for value in (-7, 0, 1, 4, 9, 25, 49, 121, 561, 3.0, True):
            with self.subTest(value=value):
                self.assertFalse(is_prime(value))
                with self.assertRaises(ValueError):
                    local_image("baseline", value)
        for value in (2, 3, 7, 97, 1009):
            self.assertTrue(is_prime(value))


class CarrierTests(unittest.TestCase):
    def test_progressions(self):
        self.assertEqual(arithmetic_carrier(3, -1, 2), (-1, 1, 3))
        self.assertEqual(arithmetic_carrier(3, 4, -2), (4, 2, 0))
        self.assertEqual(geometric_carrier(4), (1, 3, 9, 27))
        self.assertEqual(arithmetic_carrier(0), ())
        self.assertEqual(geometric_carrier(0), ())

    def test_invalid_progressions(self):
        cases = ((arithmetic_carrier, (-1,)), (arithmetic_carrier, (3, 0, 0)),
                 (arithmetic_carrier, (3.0,)), (geometric_carrier, (-1,)),
                 (geometric_carrier, (3, 1)), (geometric_carrier, (3, True)))
        for function, arguments in cases:
            with self.subTest(function=function.__name__, arguments=arguments), self.assertRaises(ValueError):
                function(*arguments)
        with self.assertRaises(ValueError):
            carrier_image("baseline", [0, 1.0])

    def test_empty_set_has_undefined_ratios(self):
        result = carrier_image("mixed-cubic", [])
        for field in ("carrier_size", "input_count", "image_size", "energy"):
            self.assertEqual(result[field], 0)
        self.assertIsNone(result["image_lower_bound"])
        self.assertIsNone(result["normalized_support_ratio"])

    def test_singleton(self):
        result = carrier_image("baseline", [9])
        self.assertEqual(result["image_size"], 1)
        self.assertEqual(result["energy"], 1)
        self.assertEqual(result["image_lower_bound"], Fraction(1))

    def test_manual_same_set_cubic(self):
        # A={0,1}: values 0,0,0,2; multiplicities 3 and 1.
        result = carrier_image("mixed-cubic", [0, 1])
        self.assertEqual(result["input_count"], 4)
        self.assertEqual(result["image_size"], 2)
        self.assertEqual(result["energy"], 10)
        self.assertEqual(result["image_lower_bound"], Fraction(8, 5))
        self.assertEqual(result["normalized_support_ratio"], Fraction(1, 2))

    def test_manual_geometric_cubic(self):
        # A={1,3}: values 2,12,12,54; multiplicities 1,2,1.
        result = carrier_image("mixed-cubic", geometric_carrier(2))
        self.assertEqual(result["image_size"], 3)
        self.assertEqual(result["energy"], 6)
        self.assertEqual(result["image_lower_bound"], Fraction(8, 3))

    def test_duplicates_are_set_elements(self):
        self.assertEqual(carrier_image("quartic", [1, 2, 1]), carrier_image("quartic", [2, 1]))

    def test_energy_is_lower_bound(self):
        for name in POLYNOMIALS:
            for values in (arithmetic_carrier(7, -3), geometric_carrier(6)):
                result = carrier_image(name, values)
                self.assertLessEqual(result["image_lower_bound"], result["image_size"])
                self.assertLessEqual(result["normalized_support_ratio"], 1)


class VerificationAndCliTests(unittest.TestCase):
    def invoke(self, *arguments):
        output = io.StringIO()
        with redirect_stdout(output):
            status = main(list(arguments))
        return status, output.getvalue()

    def test_all_finite_benchmarks(self):
        result = finite_checks()
        self.assertTrue(result["passed"], [check for check in result["checks"] if not check["passed"]])
        self.assertGreater(result["check_count"], 100)

    def test_cli_exact_stable_json(self):
        args = ("local-images", "--polynomial", "baseline", "--primes", "5", "--q", "5")
        status, output = self.invoke(*args)
        self.assertEqual(status, 0)
        self.assertEqual(output, self.invoke(*args)[1])
        result = json.loads(output)["results"][0]
        self.assertEqual(result["density"], {"numerator": 3, "denominator": 5})
        self.assertNotIn("3.0", output)

    def test_cli_empty_geometric_carrier(self):
        status, output = self.invoke("carriers", "--carrier", "geometric", "--size", "0")
        self.assertEqual(status, 0)
        for result in json.loads(output)["results"]:
            self.assertEqual(result["image_size"], 0)
            self.assertIsNone(result["image_lower_bound"])

    def test_cli_invalid_inputs(self):
        cases = (("local-images", "--primes", "9"),
                 ("local-images", "--primes", "1013"),
                 ("local-images", "--q", "0"),
                 ("carriers", "--step", "0"),
                 ("carriers", "--size", "129"),
                 ("carriers", "--base", "1"))
        for args in cases:
            with self.subTest(args=args), redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
                main(list(args))
            self.assertEqual(error.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
