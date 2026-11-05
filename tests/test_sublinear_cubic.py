"""Independent small projection/coordinate oracles for the new grid."""

from collections import Counter
from fractions import Fraction as Q
import unittest

from experiments import sublinear_cubic as grid


class SublinearCubicTests(unittest.TestCase):
    work = Counter()

    def test_declared_input_only_preflight(self):
        preflight = grid.structural_preflight(list(grid.definitions()))
        self.assertEqual((preflight["carriers"], preflight["graphs"], preflight["maximum_N"]), (36,216,60))
        self.assertEqual(preflight["exact_P_evaluations"], 37243)

    def test_nonfaithful_projection_oracle(self):
        candidate = next(c for c in grid.definitions() if c["id"]=="projection_q2_near")
        self.assertEqual(candidate["values"], [Q(j,4) for j in (0,2,3,4,5,6,7,8,9,10,11,12,13,15)])
        multiplicities = Counter(x for x,_ in candidate["records"])
        self.assertEqual(dict(Counter(multiplicities.values())), {1:12,2:2})
        self.assertEqual(multiplicities[Q(3,2)], 2)
        self.assertEqual(multiplicities[Q(9,4)], 2)
        self.assertEqual(grid.common_inventory([Q(1,2),Q(3,4)],5), (Q(1,2),Q(3,4),Q(1),Q(3,2),Q(9,4)))

    def test_correlated_coordinate_reuse_oracle(self):
        candidate = next(c for c in grid.definitions() if c["id"]=="correlated_q4_H2")
        first = {Q(-1,8),Q(-3,32),Q(0),Q(5,32),Q(3,8),Q(21,32),Q(1)}
        self.assertEqual(set(candidate["values"]), first | {x+1 for x in first})
        self.assertEqual((len(candidate["values"]),len(candidate["records"]),len(candidate["prescribed"])), (13,36,18))

    def test_shared_anchor_full_pair_oracle(self):
        candidate = next(c for c in grid.definitions() if c["id"]=="reverse_q3_H2")
        budget = grid.Budget()
        carrier = grid.graph.enumerate_fibers(candidate["values"],budget)
        metrics = grid.carrier_metrics(candidate,carrier,budget)
        case = grid.graph.graph_case(carrier,"oracle",[Q(1,3),Q(2,3)],budget,direct_oracle=True)
        zero_index = next(i for i,f in enumerate(carrier["fibers"]) if f["output"]=="0")
        zero_vertices = carrier["fibers"][zero_index]["vertices"]
        self.assertTrue({Q(-1,3),Q(0),Q(1,3),Q(2,3),Q(1),Q(4,3)} <= set(map(Q,carrier["fibers"][zero_index]["differences"])))
        self.assertEqual((carrier["N"],metrics["distinct_prescribed_pairs"]), (24,24))
        self.assertEqual(metrics["parameter_to_scalar_reuse"], "2")
        self.assertTrue(any(len(set(c)&set(zero_vertices))>=6 for c in case["components"]))
        self.assertEqual(case["direct_motion_oracle"],"PASS")
        type(self).work.update(budget.checks)

    def test_engine_guards_restore_on_failure(self):
        before = (grid.graph.MAX_CARRIERS,grid.graph.MAX_CASES,grid.graph.MAX_INPUTS)
        with self.assertRaisesRegex(RuntimeError,"deliberate"):
            with grid.engine_limits():
                self.assertEqual(grid.graph.MAX_CASES,288)
                raise RuntimeError("deliberate")
        self.assertEqual((grid.graph.MAX_CARRIERS,grid.graph.MAX_CASES,grid.graph.MAX_INPUTS),before)


if __name__=="__main__":
    unittest.main()
