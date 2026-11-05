# Phase C0 candidate ledger

Scores are prioritization scores only. The eight columns are explicitness
(E), local/support gain (L), fixed-polynomial transport (T), archimedean
efficiency (A), field compatibility (F), positive-rate plausibility (R),
substantive extension (S), and proof tractability (P).

| ID | Fixed polynomial / family | E | L | T | A | F | R | S | P | Total | Decision |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C1 | `P=L^2+M`, with primitive two-variable integral `L` and transverse integral `M`; primary member `(x+2y)^2+3x-y` | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 39 | Selected; proved |
| C2 | `(x+2y)^4+3x-y` with deformation `(x+2y)^4+Q^3(3x-y)` | 5 | 4 | 5 | 0 | 5 | 0 | 5 | 4 | 28 | Symmetric-box route failed |
| C3 | `x^2+xy+y^2+3x-y` with uniform quadratic deformation | 5 | 0 | 5 | 5 | 5 | 0 | 4 | 5 | 29 | Rejected: full local image |
| C4 | `x^2+3y^2+x+y` with prime-power modulus `3^k` | 5 | 2 | 5 | 1 | 1 | 0 | 5 | 5 | 24 | Exact local theorem; box route failed |

## C1 - transverse square-leading quadratics

**Conjecture.** For primitive

\[
L(x,y)=ax+by,\qquad M(x,y)=cx+ey,
\]

with `ab != 0` and `ae-bc != 0`, the fixed polynomial

\[
P(x,y)=L(x,y)^2+M(x,y)
\]

has arbitrarily large finite real sets `A` with
`|P(A,A)| <= |A|^(2-epsilon)` for some fixed positive `epsilon`.

**Mechanism.** Use

\[
P_Q=L^2+QM,\qquad P_Q(Qx,Qy)=Q^2P(x,y).
\]

At every selected odd prime dividing `Q`, the reduced image is exactly the
square set. Proposition 3.8 of the supplied unit-distance proof gives enough
completely split primes that the product density beats the root-discriminant
cost. A centered Minkowski box and worst-case class packing bound the full
support.

**Largest initial obligation.** Jointly prove field supply, centered carrier
growth, full class packing, and a strictly positive fixed rate. All are closed
in the consolidated proof.

**Status.** PROVED WITHIN THE OFFLINE SOURCE SYSTEM. The exponent depends on
the fixed family member and the fixed tower parameters; no uniform exponent
over the family is claimed.

## C2 - quartic power mutation

**Conjecture screened.** The fixed polynomial

\[
P^{(4)}=(x+2y)^4+3x-y
\]

might inherit stronger local fourth-power sparsity from

\[
P_Q^{(4)}=(x+2y)^4+Q^3(3x-y),\qquad
P_Q^{(4)}(Qx,Qy)=Q^4P^{(4)}(x,y).
\]

For every supplied split prime `p == 1 (mod 4)`, the exact density is
`(p+3)/(4p)`. On the symmetric box, however,

\[
\Theta_4(X)=D\rho_4\left(162X^2+\frac{8Q^3}{X}+\frac{Q}{X^2}\right)>1
\]

for every `X>0`. The proof is in Role D and the consolidated report.

**Status.** ROUTE FAILED. The compression conjecture itself is not refuted;
a different carrier or packing theorem would be required.

## C3 - full-rank quadratic part

**Conjecture screened.** Let

\[
P_3=x^2+xy+y^2+3x-y,
\qquad
(P_3)_Q=x^2+xy+y^2+Q(3x-y).
\]

The common-scaling identity holds, but modulo every supplied split prime
(`p == 1 (mod 4)`, hence `p != 3`) the nondegenerate quadratic form
`x^2+xy+y^2` is surjective. Thus `rho=1` and the proposed local mechanism
has no gain.

**Status.** LOCAL ROUTE REJECTED, CONJECTURE NOT REFUTED.

## C4 - one-prime, prime-power amplification

For

\[
P_4=x^2+3y^2+x+y,
\qquad (P_4)_R=x^2+3y^2+R(x+y),
\]

one has `(P_4)_R(Rx,Ry)=R^2P_4(x,y)`. The leading form is rank one modulo
`3` and full rank at every other odd prime. Exact valuation analysis proves

\[
\left|\{x^2+3y^2\pmod {3^k}\}\right|=\frac{3^k+1}{2}.
\]

Thus the density tends to `1/2`; it does not become `2^{-k}`. The exact box
ledger is bounded below by `4D`, so the present prime-power route fails. In
addition, the supplied tower does not guarantee complete splitting of the
prescribed prime `3`.

**Status.** ROUTE FAILED, CONJECTURE NOT REFUTED. The prime-power value-set
formula is a proved intermediate result; O4 and O7 would both need new input.
