"""Independent exact chart and full-complement oracles."""

from collections import Counter
from fractions import Fraction as Q
import unittest

from experiments import nonlinear_reuse as nr


class NonlinearReuseTests(unittest.TestCase):
    work=Counter()

    def test_input_only_preflight_and_stops(self):
        charts=list(nr.definitions())
        result=nr.preflight(charts)
        self.assertEqual((result["model_records"],result["distinct_normalized_carriers"],result["maximum_N"]),(16,12,18))
        self.assertEqual(result["cached_full_square_P_evaluations"],924)
        self.assertTrue(all(c["stop"] for c in charts))
        self.assertEqual(next(c for c in charts if c["id"]=="signed_square_m3")["values"],(Q(0),Q(1),Q(4),Q(9)))
        type(self).work["constructor_record_checks"]+=result["formal_label_construction_checks"]

    def test_conic_independent_rational_oracle(self):
        u,v=nr.conic(Q(1,2))
        self.assertEqual((u,v),(Q(3,7),Q(5,7)))
        self.assertEqual(u*u+u*v+v*v,1)
        first,second=nr.coordinates(Q(0),u),nr.coordinates(Q(0),v)
        self.assertEqual(first,(Q(60,343),Q(-87,343)))
        self.assertEqual(second,(Q(60,343),Q(-185,343)))
        self.assertEqual([nr.normalized_polynomial(*p) for p in (first,second)],[0,0])
        type(self).work["identity_P_evaluations"]+=2

    def test_nodal_independent_scaled_oracle(self):
        self.assertEqual(nr.nodal(0),(Q(-2),Q(-1)))
        first=nr.coordinates(Q(0),Q(-2),Q(1,3))
        second=nr.coordinates(Q(4,3),Q(-1),Q(1,3))
        self.assertEqual(first,(Q(1,3),Q(7,3)))
        self.assertEqual(second,(Q(1,3),Q(4,3)))
        self.assertEqual([nr.normalized_polynomial(*p,Q(1,3)) for p in (first,second)],[0,Q(4,3)])
        with self.assertRaises(ValueError):
            nr.nodal(1)
        type(self).work["identity_P_evaluations"]+=2

    def test_duplicate_labels_and_full_completion_oracle(self):
        chart=nr.model("oracle","oracle",[(Q(0),Q(1),[j],Q(2,3)) for j in range(3)],Q(1,3))
        budget=nr.Budget()
        carrier=nr.enumerate_carrier(chart,budget)
        self.assertEqual([z for z,_ in carrier["fibers"]],[Q(0),Q(2,3),Q(4,3),Q(2)])
        partial=nr.audit_chart(chart,carrier,budget)
        self.assertEqual((partial["N"],partial["Q0"],partial["Q"],partial["selected_image_size"],partial["uncovered_pairs"]),(2,3,1,1,3))
        self.assertEqual(partial["formal_pair_projection_multiplicity_distribution"],{3:1})
        self.assertEqual((partial["new_outputs_outside_selected"],partial["safe_full_image_upper_bound"]),(3,4))
        completion=nr.augmented(chart,"full_completion")
        self.assertEqual(nr.cache_key(completion),nr.cache_key(chart))
        full=nr.audit_chart(completion,carrier,budget)
        self.assertEqual((full["Q0"],full["Q"],full["selected_image_size"],full["full_image_size"],full["uncovered_pairs"]),(6,4,4,4,0))
        self.assertEqual(full["formal_pair_projection_multiplicity_distribution"],{1:3,3:1})
        type(self).work.update(budget.checks)


if __name__=="__main__":
    unittest.main()
