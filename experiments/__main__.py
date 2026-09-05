"""Command line entry point: python -m experiments --help."""

import argparse
from fractions import Fraction
import json

from .core import POLYNOMIALS, arithmetic_carrier, carrier_image, geometric_carrier, local_image
from .verification import finite_checks


def bounded_integer(low: int, high: int):
    def parse(value: str) -> int:
        try:
            number = int(value)
        except ValueError as error:
            raise argparse.ArgumentTypeError("must be an integer") from error
        if not low <= number <= high:
            raise argparse.ArgumentTypeError(f"must be between {low} and {high}")
        return number
    return parse


def encode_fraction(value):
    if isinstance(value, Fraction):
        return {"numerator": value.numerator, "denominator": value.denominator}
    raise TypeError(f"cannot serialize {type(value).__name__}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Exact finite polynomial-image experiments; these checks are not proofs.")
    commands = parser.add_subparsers(dest="command", required=True)

    local = commands.add_parser("local-images", help="enumerate all pairs in F_p x F_p")
    local.add_argument("--primes", type=bounded_integer(2, 1009), nargs="+", default=[2, 3, 5, 7, 11, 13], help="prime moduli, each <=1009 (at most 16)")

    carriers = commands.add_parser("carriers", help="enumerate images and ordered collision energy on A x A")
    carriers.add_argument("--carrier", choices=("arithmetic", "geometric"), default="arithmetic")
    carriers.add_argument("--size", type=bounded_integer(0, 128), default=8)
    carriers.add_argument("--start", type=bounded_integer(-1000000, 1000000), default=0, help="arithmetic progression start")
    carriers.add_argument("--step", type=bounded_integer(-1000000, 1000000), default=1, help="nonzero arithmetic progression step")
    carriers.add_argument("--base", type=bounded_integer(2, 100), default=3, help="geometric progression base; benchmark formulas assume >=3")

    for command in (local, carriers):
        command.add_argument("--polynomial", choices=(*POLYNOMIALS, "all"), default="all")
        command.add_argument("--q", type=bounded_integer(1, 1000000000), default=1, help="deformation parameter Q; Q=1 is the original polynomial")

    commands.add_parser("verify", help="check finite benchmark cases and exact deformation identities")
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "verify":
            result = finite_checks()
        else:
            names = list(POLYNOMIALS) if args.polynomial == "all" else [args.polynomial]
            if args.command == "local-images":
                if len(args.primes) > 16:
                    raise ValueError("at most 16 primes may be supplied")
                result = {
                    "experiment": "local-images",
                    "scope": "full finite-field enumeration; not an asymptotic proof",
                    "results": [local_image(name, p, args.q) for name in names for p in sorted(set(args.primes))],
                }
            else:
                if args.carrier == "arithmetic":
                    carrier = arithmetic_carrier(args.size, args.start, args.step)
                    parameters = {"kind": args.carrier, "size": args.size, "start": args.start, "step": args.step}
                else:
                    carrier = geometric_carrier(args.size, args.base)
                    parameters = {"kind": args.carrier, "size": args.size, "base": args.base}
                result = {
                    "experiment": "carriers",
                    "scope": "finite same-set enumeration; energy gives a lower bound on support",
                    "carrier": parameters,
                    "results": [carrier_image(name, carrier, args.q) for name in names],
                }
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2, sort_keys=True, default=encode_fraction, allow_nan=False))
    return 1 if args.command == "verify" and not result["passed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
