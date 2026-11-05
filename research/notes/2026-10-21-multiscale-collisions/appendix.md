# Algebra, scales and the finite diagnostic

T01 · 21 October 2026 · companion to [the report](README.md).

## A. MC-L0: exact coefficients, resolution and exceptional differences

**PROVED; checked symbolically by the lead and referee.** With
\(d=a-b\) and \(w=u-v\),
\((d+\rho w)^3=d^3+3d^2\rho w+3d\rho^2w^2+\rho^3w^3\).
Adding \(a+b+\rho(u+v)\), subtracting \(P(a,b)\), and dividing by
\(\rho>0\) gives equation (3) of the report. No term is discarded.
For \(u,v\in[0,1)\), \(|w|\le1\), which proves the remainder bound.
The containing output interval has length at most
\[
\rho\bigl(|1+3d^2|+|1-3d^2|\bigr)
 +2(3|d|\rho^2+\rho^3).
\]
This is a span upper bound, not a distinct-output upper bound.
If the input cluster offsets have diameter \(W\) instead of 1, replace
\(|w|\le1\) by \(|w|\le W\): the nonlinear error is at most
\(3|d|\rho^2W^2+\rho^3W^3\). In the laboratory the fine digit width
is 3 or 7, so the cluster widths are \(3/64\) or \(7/64\), not \(1/64\).

Near \(d=0\), if \(|d|\le\epsilon\), both linear coefficients differ
from 1 by at most \(3\epsilon^2\), and the normalized nonlinear error
is bounded by \(3\epsilon\rho+\rho^2\). At exactly zero its leading
nonlinear term is cubic. Near \(a_*\in\{\pm1/\sqrt3\}\), if
\(|d-a_*|\le\epsilon\), then
\[
|1-3d^2|=3|d-a_*||d+a_*|
 \le(2\sqrt3+3\epsilon)\epsilon,
\]
and the same bound applies to \(|(1+3d^2)-2|\). The normalized quadratic
coefficient has absolute value at most \((\sqrt3+3\epsilon)\rho\).
In these regions projection theorems requiring a uniform nonzero second
coefficient cannot simply be applied without checking their hypotheses.
The exact fiber graph proof needs only \(P_x\ge1\), which is uniform
on all of \(\mathbb R^2\).

More generally the derivative coefficients can grow with \(|d|\).
Translation preserves the polynomial up to adding twice the translation;
scaling does not: \(P(t+\lambda x,t+\lambda y)
=2t+\lambda(x+y+\lambda^2(x-y)^3)\). No fixed-coefficient theorem is
transferred through that normalization without tracking \(\lambda\).

## B. Direct actual-rich-mass transfer

**PROVED — supplement to MC-S3.** Let
\[
\mathcal T_j(K)=\sum_{C\in\mathcal C_j}\sum_z
 r_C(z)\,\mathbf1_{r_C(z)\ge K},\qquad K>0.
\]
For an integer \(k\ge1\), each parent fiber enters at most
\(q_k=2\cdot4^k\) descendant squares at level \(j+k\). This follows
by applying the 1-Lipschitz argument directly to the \(4^k\) fine
\(y\)-intervals, and is sharper than iterating the eight-child bound.
For \(0<\theta<1\),
\[
(1-\theta)\mathcal T_j(K)
 \le\mathcal T_{j+k}\!\left(\frac{\theta K}{q_k}\right),
\qquad \mathcal T_{j+k}(K)\le\mathcal T_j(K).
\]
Indeed, in a parent local fiber of size \(m\ge K\), descendants below
\(\theta K/q_k\) contain in total less than \(\theta K\le\theta m\)
pairs. The rest retain the stated finer local multiplicity. Sum over
the disjoint parent pair populations. The second inequality follows
because descendant local multiplicity is at most its ancestor's.
This transfers actual pair mass, not Shannon entropy or collision energy.
It becomes weak once the finer threshold falls below 1; that loss is real.

## C. Why the two-level test can look small metrically

**PROVED as a specialization of the imported faithful-coefficient
mechanism GS-P4, not a new construction.** For finite real digit sets
\(B,D\), compare formal outputs from \(b+\rho u,c+\rho v\).
Set \(d=b-c\), \(w=u-v\). The coefficients in powers of \(\rho\) are
\[
P(b,c),\quad u+v+3d^2w,\quad 3dw^2,\quad w^3.
\]
If \(w\ne0\), the cubic coefficient determines \(w\), the quadratic
one determines \(d\), the constant one determines \(b+c\), and the
linear one determines \(u+v\). Thus the ordered input labels are
recovered uniquely. If \(w=0\), the linear coefficient determines
\(u=v\), and equality reduces to a base output equality in \(B^2\).

There are finitely many nonzero coefficient-difference polynomials in
\(\rho\); each has finitely many nonzero roots. Consequently there
exists \(\epsilon(B,D)>0\) such that every \(0<\rho<\epsilon(B,D)\)
has no accidental output equality, and the input representation is
injective. For those scales,
\[
|P(B+\rho D,B+\rho D)|
 =|B|^2|D|(|D|-1)+|P(B,B)|\,|D|.
\]
This assertion gives no uniform lower bound for \(\epsilon(B,D)\)
as digits grow. It is a finite root-exclusion argument. For the two
specified sets at \(\rho=1/64\), the exact census verifies this formula;
it is not assumed from a generic-scale argument.

For \(B=\{0,1,3\}\), the base support has seven values:
\(-24,-4,0,2,6,12,30\), with precisely two size-two fibers. Thus the
formula becomes \(9|D|^2-2|D|\). For each fixed \(D\), as \(\rho\)
tends to zero all outputs approach these seven base values. At any fixed
positive covering resolution, sufficiently small \(\rho\) therefore
permits seven covering intervals, while the exact output count remains
\(9|D|^2-2|D|\). This is an exact explanation of why small metric
entropy does not imply large actual fibers; it is not a new unbounded
candidate or an inference from the six finite tests.

## D. Laboratory definitions and full-square accounting

The CP controls are the accepted ladder, not the later two-output TC
attachment. Let \(t\) be the root in \((0,1/12)\) of
\(64t^3-80t^2+28t-1\), \(h=\sqrt t>0\),
\(r=h(4t-2)\), and \(c_i=(2i-1)r\). Then
\[
A_m=\{c_i+h:-1\le i\le m-1\}
\cup\{c_i-h:0\le i\le m\},\quad m=2,3.
\]
The imported source proves real membership, distinctness, \(N=2m+2\),
selected \(Q=4m,Z=m+1\), and actual image at least \(N^2/4\).
The primary audit uses exact rational triples in \(\mathbb Q[t]\)
modulo the cubic; the independent referee uses \(U=4t\) with
\(U^3-5U^2+7U-1=0\), and computes \(4P/h\). The latter polynomial
has no rational root (the only possibilities are \(\pm1\)), hence
is irreducible. Its derivative is positive on \((0,1/3)\), and its
endpoint signs are opposite. This identifies the required real root
and makes coefficient equality an exact equality test. No floating-point
root or comparison is used for the full-square fibers.

For the four rational cases, the tree root is \([0,16)\), with five
four-way generations, terminating at width \(1/64\). Direct checks
confirm scalar separation even at boundary points. Their pair-weighted
branch-event histograms are:

| Set | Zero events | One event | Two events |
|---|---:|---:|---:|
| AP8 | 36 | 8 | 20 |
| AP12 | 96 | 18 | 30 |
| Nonuniform 9 | 69 | 12 | 0 |
| Nonuniform 12 | 128 | 16 | 0 |

The chosen root and scale window are part of these finite data. They
are not asserted to optimize any measure. No metric or tree census was
performed for the algebraic CP controls.

If one treats the entire census as controlled pairs, the reuse ratios
are \(2Q/N=2N\), \(Q/Z=N^2/|P(A,A)|\), and coverage 1. The output
ratio is only a bounded finite number in these data; full enumeration
is not a compressed encoding. The old CP selected ledgers instead have
\((2Q/N,Q/Z,Q/N^2)=(8/3,8/3,2/9)\) and \((3,3,3/16)\).
All excluded-pair counts and safe bounds appear in the main report.

## E. Construction-ledger boundary

This is a necessary-condition theorem plus a finite diagnostic, not a
serious proposed asymptotic construction. The required ledger costs are
therefore explicit as follows. All inputs and both coordinates are
retained: thinning and exceptional-pair losses are zero. Parameter
representations in the tested sets are injective, and the same real set
is used twice. Rational denominators are exactly 64 in the two-level
cases; the input spans and output spans are recorded. The CP computation
uses the fixed degree-three coefficient field above and a common positive
factor \(h\), with no variable field degree, regulator or splitting
argument. There are no local moduli, prime choices, carries, unit counts,
branch inventories or uncontrolled output containers. Metric resolution
is a separate finite observable and earns no exact-image saving. No
asymptotic input exponent, output exponent, or positive net rate is
certified; these entries are **not obtained**, rather than zero cost.
