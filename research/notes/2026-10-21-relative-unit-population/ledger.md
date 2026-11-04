# MS-O1 construction and signed-rate ledger

21 October 2026 · version 1. Uses the repository
[construction ledger template](../../templates/CONSTRUCTION_LEDGER.md).

## Identity, hypotheses and evidence

- **Track / polynomial:** T03, \(Q(x,y)=x^2+xy+y^2\), the unchanged
  mixed-signature C0 lattice carrier.
- **Scope:** the commissioned relative order-unit population gate, with
  a required distortion audit; no field, seed or scalar-window mutation.
- **Mode / cap:** strictly offline; shared 2,000,000 charged exact
  evaluations and 600 program CPU seconds; 20% reserved for verification.
  No mathematical program was executed.
- **Quantifier order:** accept the C0 tower and its fixed \(D_0\);
  define \(D_*,D_E,B_0,J_0,K_R\) as in the report; fix \(T_*\);
  then let the original index \(j\) grow. No parameter depends on \(j\)
  except the original fields and their actual degree.
- **Dependencies:** 20 October MS-F1–F6 and MS-C1–C2; the accepted
  C0 field input; Dirichlet's lattice theorem, ideal factorization,
  discriminant identities, and the elementary Minkowski/Blichfeldt
  argument with the stated normalizations.
- **Evidence:** complete new symbolic proofs MSU-A1–A3, MSU-G1–G3
  and MSU-R1; arithmetic proof independently checked by the specialist
  auditor and lead. No experiment or novelty claim.
- **Status supersession:** the earlier MS-O1 OPEN entry is historical.
  The uniform population assertion is now PROVED. All earlier failure
  results retain their exact scope.

## Exact construction and coverage

Use \(K_j=F_j(s)\), \(E_j=K_j(\omega)\) and
\(R_j=\mathcal O_{K_j}[\omega]\). The only scalar parameter selection
is the fixed admissible radius
\[
T_*=\max\{2\sqrt{D_*},e^{2K_R/3}\}.
\]
Retain every algebraic integer satisfying all real interval and complex
disk constraints at radius \(T_*\), then take its injective chosen real
embedding. This gives one scalar set \(A_j\), not two rectangular sides.
The group consists of actual order units of relative norm one; the
finite inventory is the complete \(\ell^1\) height window of radius
\(d_jL(T_*)\).

The group preserves \(Q\) and the whole arithmetic lattice, but need not
preserve its finite window. No return is credited without both scalar
target constraints. On nonzero pairs the action has multiplicity one;
at zero, all labels give the same single target. The full-support lemma
counts every ordered pair and charges uncovered outputs to bad pairs.

## Quantitative ledger

Write \(d=d_j\), \(T=T_*\), \(L=L(T)\), and \(C_R=\log K_R\).

| Gain or cost | Bound and units | Status / explanation |
|---|---|---|
| Actual input lower rate | \(a(T)=\log((\pi/2)T^3/D_*^{3/2})>0\), \(n\ge e^{a(T)d}\) | PROVED, inherited MS-C1 |
| Actual input upper rate | \(B(T)=3\log(2T+1)\), \(n\le e^{B(T)d}\) | PROVED; no input-growth limit assumed |
| Input thinning, both coordinates | Zero | No scalar deleted; any later bad-pair set must be charged separately |
| Parameter / real projection fibers | One | Injective field embedding; actual cardinalities, not multiset weights |
| Local sparsity / splitting | No gain asserted | No residue sieve; C0 splitting data not transferred |
| Uniform per-residue populations | Inapplicable | No residue classes used |
| Field degrees | \(3d,6d\) | Unchanged fields |
| Root discriminants | \(D_*,D_E\) | Paid in scalar lower rate and \(B_0=2\sqrt{D_E}\) |
| Ideal labels | At most \(B_0^{12d}2^{6d}\) | PROVED by convergent positive ideal series; no class-number estimate |
| Exact norm-element labels | At most \((2B_0^2+1)^{3d}\) | PROVED by norm separation |
| Relative log error | Radius \(3d\log B_0\) | PROVED, includes all complex places |
| Relative maximal-order covolume | \(\mathcal R_E\le K_E^d\) | PROVED MSU-A2 |
| Relative order covolume | \(\mathcal R_R\le K_R^d\), \(K_R=27K_E\) | PROVED; the factor \(27^d\) is charged once |
| Additive order index | At most \(3^{3d/2}\) | Inherited; not an additional loss in the unit count |
| Regulator normalization | Ordinary Euclidean \(\ell_i=\log\lvert\nu_i^+u\rvert\) | No absolute-regulator substitution or hidden factor of two |
| Unit population | \(\lvert U_j(T_*)\rvert\ge2^d\); sharper rate \(1+\log L-C_R\) | PROVED; no short-generator or lattice-shape premise needed |
| Torsion | \(6\le w_j\le8d^2\) | Zero exponential rate; exactly \(w_j\) preimages per log point |
| Denominators | No action coefficient denominators | Same ideal yields maximal-order units; order conversion is separately paid |
| Height / conjugate size | \(h(u)\le L/3\), house \(\le e^{dL}\) | PROVED; no uniform coordinatewise smallness |
| Continuous distortion | \(w(u)=e^{-2\sum_i(\lvert\ell_i\rvert-\log2)_+}\) | An upper overlap diagnostic only |
| Weighted lattice shape | \(e^{\pm2S_j}/\mathcal R_{R,j}\) in weighted comparison | Unknown tower shape retained, not set to zero |
| Discrete overlap comparison | Prefactor \([4D_*^3(2+1/T)^6/\pi^2]^d\) and strip inflation \(+1\) | PROVED upper bound MSU-G3; cannot be read as a lower return estimate |
| Branches / covers / carries / states | No scalar states or digit carries; \(J_0^d\) auxiliary log-cover labels | Cover labels already included in \(K_E\), not a second loss |
| Stabilizers / repeated targets | Free at nonzero sources; one target at zero | PROVED; no unit-label overcount |
| Exceptional outputs | At most one per bad ordered source | PROVED support implication; no small bad-source bound yet |
| Actual output rate | Only \(\lvert Q(A,A)\rvert\le n^2\) claimed unconditionally here | OPEN positive gap; no new lower-image obstruction |
| Conditional return and exception rates | MS-O2 would give \(\kappa,\eta>0\) | OPEN; not supplied by action population |
| Conditional final fixed exponent | Every \(c<\min(\kappa,\eta)/B(T)\) | PROVED implication MSU-R1, not an unconditional result |

## Signed rate and exact deficit

The action rate is now positive:
\[
\alpha\ge\log2,\qquad
\liminf d_j^{-1}\log|U_j(T_*)|\ge1+\log L(T_*)-C_R.
\]
It is **not a return gain** in a full-output ledger. The unknown gain is
how many units simultaneously satisfy both scalar window constraints for
almost every source. Thus neither a strictly positive full-output gap
nor a fixed \(c>0\) is certified.

Using only the cutoff and the new population bound gives the crude
weighted lower rate
\[
1+\log L-C_R-2L\le-C_R-\log2.
\]
This fails to prove a positive weighted lower rate. It neither bounds
the actual weighted sum above nor refutes a return tail. Even a positive
weighted lower rate would concern upper continuous-overlap bounds and
would still not establish the required discrete lower tail.

Conditional on the one stated MS-O2 incidence lemma, the exact support
bound is
\[
2n^2e^{-\kappa d}+4(n^2-1)e^{-\eta d}+1.
\]
Converting with the actual upper input bound, rather than positing an
input-growth limit, gives the strict exponent range above. Constant
prefactors and the origin are absorbed by strictness. This rate
conversion uses every ordered source and does not count any local saving
twice.

## Disposition

**MS-O1 PROVED.** Full-rank useful returns and the actual image remain
**OPEN**. The sole next obligation is
[MS-O2, the stated actual-domain incidence concentration lemma](README.md#5-full-support-status-and-one-next-lemma).
It is a stronger sufficient condition, not a necessary characterization
or a claim of feasibility. No further proof search is performed here.
