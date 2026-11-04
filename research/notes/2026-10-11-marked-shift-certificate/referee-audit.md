# Independent audit of the marked shift certificate

T01 · 11 October 2026 · version 1 · offline internal audit.

**PROVED — MS-R1, audit of MS-C1.** For the precise positive real
constants and marked points of TC-G5, the point \(T=R_2-R_1\) has
infinite order. Equivalently, \([n]T\ne O\) for every positive integer n.
The complete argument in [arithmetic.md](arithmetic.md), including the
local logarithm proof, was independently read and checked in this task.
The simplified coordinates and proof in [README.md](README.md) were also
checked. No correction was required.

This is an internal mathematical audit, not an external review or a
finite experiment. The fixed project polynomial remains
\(P(x,y)=(x-y)^3+x+y\). The conclusion concerns this one marked elliptic
shift; it does not provide a growing scalar construction or an image
upper bound.

## 1. Scope, sources, and evidence

The controlling constants are those in TC-G5 of
[geometry.md](../2026-10-11-torsion-compatible-sharing/geometry.md):
\[
 a=\sqrt2,\quad \lambda=(3+a)/14,\quad H=\sqrt\lambda>0,
 \quad W=\sqrt{4a-3}>0.
\]
The relevant predecessor evidence and current proof were inspected at
these SHA-256 versions:

| Source | SHA-256 | Use in this audit |
|---|---|---|
| Predecessor `geometry.md` | `713c2372740eb9b3f54dcb4242192b170436b98002f2ceacdfcc075903cb2d58` | Exact TC-G5 points and fixed curve; TC-G6 context |
| Predecessor `exact-results.json` | `17069d583d612d7f949b191e39164124a872c46ceb5f42ef6593d4aa3fbc3cc4` | Preserved finite evidence; no rerun or all-orders inference from it |
| EG-C2 in `complex-extensions.md` | `ecf894b30c3a0da77e4bccca37734a78ad0434682c9c72f7cb59f27d5da4c03d` | Full local formal-logarithm proof read and checked |
| Current `arithmetic.md` | `dfe7a75294130008d7ad4da909f693454dabd4adb13bcf70aa0fd26af0e4697d` | Complete MS-C1 proof and final refinements audited |
| Current `README.md` | `c7d6ab1d04aad9910cf0c9dfa364335ae3acfc9d5912e2013ab70f616fb181ed` | Expanded coordinates and MS-C1 presentation audited |

The audit used hand algebra, exact norm identities, and a single
preselected local prime, 23. It executed zero mathematical programs,
zero target-P evaluations, zero point counts, and zero order or division
searches. Reading files and computing document hashes are provenance
operations, not mathematical experiments. The allowed three-prime,
10,000-check ceiling was not expanded; only one prime is used in the
proof. No certificate-verifier program was needed.

## 2. The field and conjugation really exist

Write \(F_0=\mathbb Q(a)\), \(F=F_0(H)\), and
\(K=F(W)\). The three norms are exactly
\[
 N(\lambda)=1/28,\qquad N(4a-3)=-23,
 \qquad N((4a-3)/\lambda)=-644.
\]
The first is not a rational square; the latter two are negative. A
square in the real quadratic field has a rational norm that is itself
a square. Thus \(\lambda\) is not a square in \(F_0\), and neither
\(4a-3\) nor \((4a-3)/\lambda\) is a square in \(F_0\).

The additional square-class step was checked explicitly: if
\((x+yH)^2=4a-3\), with x,y in \(F_0\), its H coefficient gives
2xy=0. The two resulting cases contradict the last two norm tests.
Hence \([K:\mathbb Q]=8\), and the automorphism fixing a,H and negating
W is valid. It fixes the curve, fixes \(R_2\), and negates \(R_1\).
It follows that
\[
 T+\sigma(T)=2R_2.
\]
If an integer n annihilated T, the same integer would annihilate its
conjugate and therefore \(2R_2\). No independent choice of signs is
being assumed inside a field where it might fail to define an
automorphism.

The joint coordinate field is indeed K: either displayed X-coordinate
recovers a, the Y-coordinate of \(R_2\) recovers H, and that of
\(R_1\) recovers W. The proof does not need, or claim, that T alone
generates K.

## 3. Independent chord-law expansions

Substitution of \(h_1^2=(5-3a)/14\) and \(h_2^2=\lambda\) gives
\[
 R_1=\left((68+144a)/7,\ 288HW(2+3a)/7\right),
\]
\[
 R_2=\left((164-48a)/7,\ 288H(5a-6)/7\right).
\]
For \(T=R_2-R_1\), the slope through \(R_2\) and \(-R_1\) simplifies to
\[
 m_T=3H\{a-2-(a+2)W\}.
\]
Using \(a^2=2\) and \(W^2=4a-3\), independent expansion gives
\[
 m_T^2=\frac{342+198a+(54+18a)W}{7}.
\]
Subtracting \(X(R_1)+X(R_2)=(232+96a)/7\) gives precisely
\[
 X(T)=\frac{110+102a+(54+18a)W}{7}.
\]
Then \(-Y(R_2)+m_T(X(R_2)-X(T))\) gives
\[
 Y(T)=\frac{H\{1368+540a+(792+684a)W\}}7.
\]
Thus the expanded point in the README has the correct sign for the
commissioned difference, not its negative.

For the separate doubling used by the certificate, direct expansion gives
\[
 m_{R_2}=H(16a-4),\qquad
 m_{R_2}^2=(664+72a)/7,
\]
\[
 S=2R_2=\left(48+24a,\ -16H(281+208a)/7\right).
\]
For example,
\((16a-4)(-172-216a)=-6224-1888a\); subtracting
\(288(5a-6)\) gives \(-16(281+208a)\), verifying the Y-coordinate
without invoking the predecessor's finite-order output.

## 4. The local embedding and the negative valuation

The root a=18 modulo23 satisfies \(a^2=2\), with derivative
36=13 modulo23 nonzero. After lifting a, \(\lambda\) has residue13,
and H=6 is a simple root of \(H^2=\lambda\), with derivative12
nonzero. The coefficient-by-coefficient simple-root lifting argument in
the appendix constructs the roots in \(\mathbb Z_{23}\). Since the
two displayed quadratic extensions are fields, these assignments extend
to an injective field homomorphism \(F\longrightarrow\mathbb Q_{23}\).
No embedding of W into \(\mathbb Q_{23}\), and no ramified version of
the logarithm criterion, is required.

The exact identity
\[
 c^2=64(19-3a)/343
\]
gives \(c^2=16\) and \(16+27c^2=11\) modulo23. The equation is
integral and its discriminant
\(-2^{12}3^6c^2(16+27c^2)\) is a unit, so every good-reduction
hypothesis is met at this specific embedding.

The norm calculation is
\[
 281^2-2\cdot208^2=-7567=-7\cdot23\cdot47.
\]
At the chosen embedding the conjugate factor \(281-208a\) has residue10,
whereas \(281+208a\) has residue0. The former is a unit, and the
rational product has valuation one. Therefore
\(v_{23}(281+208a)=1\), exactly, not merely a lower bound.
Consequently
\[
 v_{23}(Y(S))=1,\quad X(S)=-3\pmod{23},\quad
 3X(S)^2-48=2\pmod{23}.
\]
The tangent slope at S has valuation -1. Its square has valuation -2,
whereas \(2X(S)\) is a unit. Thus
\[
 v_{23}(X(2S))=-2.
\]
The tangent denominator is nonzero, so \(2S=4R_2\) is a finite point.
The integer factor47 is part of a norm identity; it is not an additional
selected local prime or a separate local computation.

## 5. Why the criterion excludes every torsion order

The full EG-C2 proof, reproduced in arithmetic.md §5, was checked rather
than using its conclusion as an unexplained torsion criterion. The smooth
integral group law supplies an integral formal group at O, in the local
parameter t=-x/y. Its invariant differential is integral with leading
coefficient one; formal integration yields
\[
 \ell(t)=t+\sum_{n\ge1}\frac{a_n}{n+1}t^{n+1},
 \qquad a_n\in\mathbb Z_{23}.
\]
For a nonzero t with valuation r at least one, each correction term has
valuation at least \((n+1)r-v_{23}(n+1)>r\). The series converges,
its value is nonzero, and translation invariance of the differential
makes it a homomorphism to the additive characteristic-zero field.
Thus the identity subgroup has no nonidentity torsion.

Finally negative X-valuation on the integral equation forces
\(v(X)=-2r\), \(v(Y)=-3r\), and \(v(t)=r\ge1\), so the point
is in precisely that subgroup. For \(4R_2\), r=1. This proves
\(4R_2\), then \(R_2\), and then T are of infinite order. No bound
on a hypothetical order enters the proof.

## 6. Audit verdict and stop

All field, coordinate, root-lifting, discriminant, valuation, and
formal-logarithm steps pass the independent audit. The elementary
algebraic group facts used by EG-C2 are retained with their scope: this
is a good integral elliptic model over \(\mathbb Q_{23}\), not a claim
that every torsion point has integral coordinates over arbitrary ramified
extensions.

The previously open TC-O1 is resolved for its exact marked point. The
earlier bounded-order checks remain preserved historical evidence; they
are not the premise for the all-orders conclusion. No higher-order
search, additional carrier, next proof obligation, or claim about all
possible elliptic sharing constructions is introduced. The original
T01 same-set power-saving problem remains OPEN. Mathematical work on
this commissioned point stops with this certificate.
