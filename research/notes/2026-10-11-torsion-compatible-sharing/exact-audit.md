# Exact arithmetic audit of the two fixed compatible loci

T01, 11 October 2026, version 1. Fixed polynomial
\(P(x,y)=(x-y)^3+x+y\). **TC-X1 — EXPERIMENTAL, exact and exhaustive
in the finite scope below.** The full symbolic compatibility statements
are [TC-G1–TC-G6](geometry.md); they were derived before computation.
Neither the finite counts nor absence of the tested torsion relations is
an asymptotic compression theorem.

## 1. Frozen scope and review before execution

There are two fixed algebraic examples and three orders \(n=2,3,4\),
giving six ordered `(example, n)` tests. Compatibility determines each
example's complete finite paired-row locus before the program runs.
The program does not enumerate the \(n^2\) complex division points,
or even the entire \(n\)-point real division fiber. It checks the
intersection of that fiber with the already classified admissible locus.

The proof/computation referee independently inspected the saved original
CP construction, the exact elliptic coordinate model in EG-C1, the
new TC-G1–TC-G6 proof, and B-CP's exhaustive attachment reduction.
The sign change from first-coordinate to second-coordinate sharing was
checked explicitly. The lead independently read the complete new evaluator
before releasing one run. The construction specialist separately reviewed
the same unchanged source; both independent source reviews are complete.
No previous research implementation is imported or executed.

The source is [exact_audit.py](exact_audit.py), and all exact data are in
[exact-results.json](exact-results.json). No subsequent parameter, order,
curve, division basepoint or carrier was added after the result. The old
\(c=6\) division scout was not repeated. There was no network access,
package installation, numerical root search, arithmetic tower, randomness,
or execution of the earlier certificate-generating scripts.

The independent geometry audit checked these points in full:

- The correct curve is
  \(Y^2=X^3-48X-128-432c^2\), for same-second-coordinate sharing.
  Its inverse denominator is \(X+4\). Replacing these by the
  first-coordinate model would test the wrong mechanism.
- The actual slots have complex degree nine, but the real common-column
  slot is injective. Fixing both source rows gives at most two points,
  related by negation; the conic-frame condition reduces to the finite
  locus in TC-G2.
- The general one-row completion needs the stated double cover with
  six simple branch points, genus four and slot degree eighteen. Its
  isogeny pullback has genus \(1+3e\). This is a global chart limitation,
  not a ban on finite algebraic matches.
- The second example is uniquely forced, up to exchanging the widths,
  by the declared same-center, equal-output, two-reused-endpoint conditions.
  It is not selected by a parameter search.

## 2. Exact fields, real embeddings and scaled arithmetic

All scalar inputs and outputs in each example are represented as
\(H\) times a rational coefficient vector in a fixed field \(K\),
with \(H>0\) and \(H^2=\lambda\in K\). Therefore equality of those
vectors is exactly equality of the actual real scalars. It is not
necessary to assume \(H\in K\) or to determine its minimal polynomial.
No rescaling changes the target polynomial: the program uses the identity
\[
\frac{P(HA,HB)}H=\lambda(A-B)^3+A+B.                       \tag{A1}
\]

### Original CP bridge

Take
\[
K_1=\mathbb Q[t]/(64t^3-80t^2+28t-1),\qquad
1/32<t<1/24,
\]
\[
H=\sqrt t,\qquad h_1=H,\qquad s_1=H(5-8t),\qquad
c=8H(1-2t),\qquad q=c/4.
\]
The cubic is primitive; modulo 3 it is \(T^3+T^2+T+2\), with
values \(2,2,1\) at the three elements of \(\mathbb F_3\).
It is irreducible. The root interval follows from the monotonicity and
signs already checked in TC-G3. This gives a faithful degree-three
coefficient basis \(1,t,t^2\).

The actual carrier is the old six-point bridge, constructed using the two
centers \(q,-q\). Their output pairs are respectively \((c,0)\)
and \((0,-c)\); both have the same difference \(c\). They use
the same two marked parameter points \(R_1^+,R_1^-\). Thus the
second output translate is charged explicitly, rather than being counted
as a new elliptic parameter point.

### Forced same-center two-width example

Let \(W\) denote the positive root
\[
W^4+6W^2-23=0,\qquad 3/2<W<7/4,
\]
and put
\[
\sqrt2=\frac{W^2+3}{4},\quad k=\frac{W^2-1}{4}=\sqrt2-1,
\quad \lambda=H^2=\frac{3+\sqrt2}{14}.
\]
The quartic is irreducible. Indeed \(W^2=4\sqrt2-3\) lies in the
quadratic field \(\mathbb Q(\sqrt2)\) and has norm \(-23\).
It cannot be a square there, because the norm of a square is a rational
square and cannot be negative. Conversely \(\sqrt2=(W^2+3)/4\)
belongs to \(\mathbb Q(W)\), so that field has degree four.
The positive root interval specifies its real embedding. The coefficient
basis \(1,W,W^2,W^3\) is consequently faithful.

Choose
\[
h_1=kH,\quad h_2=H,\quad s_1=HW,\quad s_2=kH,
\]
\[
c=8h_1(1-2h_1^2)=8H(1-2H^2),\qquad q=c/4.
\]
The two conic frames have the same center and outputs \((c,0)\).
Their scalar union is exactly
\[
A=\{q\pm h_1,q\pm H,q\pm s_1\}.
\]
The two coefficient fields have degrees three and four. The corresponding
full scalar fields \(K_i(H)\) have degrees at most six and eight.
No assertion that these upper bounds are attained is needed. There is
no growing degree, discriminant, regulator or density gain in this finite
audit; every denominator is handled by exact rational arithmetic.

### Elliptic group arithmetic

An elliptic point is stored as \((X,V)\), meaning the actual point
\((X,HV)\), on
\[
\lambda V^2=X^3-48X-128-432\lambda(c/H)^2.
\]
For a chord whose actual slope is \(HL\), the exact formulas are
\[
L=\frac{V_2-V_1}{X_2-X_1},\quad
X_3=\lambda L^2-X_1-X_2,\quad
V_3=L(X_1-X_3)-V_1.                                     \tag{A2}
\]
For doubling,
\[
L=\frac{3X_1^2-48}{2\lambda V_1}.
\]
The program explicitly handles the identity, opposite points and vertical
lines. Each nontrivial field inverse is checked by multiplication; group
inputs and results are checked against the curve equation. This uses no
extension arithmetic beyond the stated coefficient fields.

The two target-polynomial evaluators are separate. One cubes the
difference using generic field multiplication and long division. The
other expands \(A^3-3A^2B+3AB^2-B^3\) as an unreduced polynomial,
multiplies by \(\lambda\), and uses an independently generated fixed
power table. It calls none of the first evaluator's multiplication, cube
or reduction routines. Both calls are charged as evaluations of \(P\).

## 3. All six division and translation tests

Let \(\mathcal L\) denote the complete admissible paired-row locus,
and choose the positive marked point \(R_1=R_1^+\) as basepoint.
The tested quantities are
\[
M_n=\bigl|[n]^{-1}(R_1)\cap\mathcal L\bigr|,
\]
and the set of marked destinations \(S\in\mathcal L\) for which
the unique translation \(T=S-R_1\) has exact order \(n\).
Exact order requires \([n]T=O\) and \([d]T\ne O\) for every
proper positive divisor \(d\mid n\). In particular the zero
translation is never called order two, three or four.

| Example | Complete marked locus | Actual fixed-output frames | \(n\) | Whole real division-fiber size | \(M_n\) | Exact-order translation destinations |
|---|---|---:|---:|---:|---:|---|
| Original seed | \(\{R_1,-R_1\}\) | 1 | 2 | 2 | 0 | none |
| Original seed | same | 1 | 3 | 3 | 0 | none |
| Original seed | same | 1 | 4 | 4 | 0 | none |
| Two-width seed | \(\{R_1,-R_1,R_2,-R_2\}\) | 2 | 2 | 2 | 0 | none |
| Two-width seed | same | 2 | 3 | 3 | 0 | none |
| Two-width seed | same | 2 | 4 | 4 | 0 | none |

The whole real division-fiber sizes in this table are the proved TC-G6
counts, not points enumerated by this program. The finite computation
checks every point in \(\mathcal L\), which is sufficient for the
intersection because TC-G2–TC-G5 prove that the displayed loci are
complete. Complex \(n^2\) counts are never credited as usable real
parameters.

For the first example the nontrivial transport is \(-2R_1\); it would
only swap columns of the existing frame. The division tests reduce to
\([n-1]R_1\ne O\) and \([n+1]R_1\ne O\), and transport is
excluded by \([2n]R_1\ne O\) for the selected orders. For the
second example the nonzero translations tested are exactly
\[
-2R_1,\qquad R_2-R_1,\qquad -R_2-R_1.
\]
All have been checked at the three orders; no assertion about their higher
orders or infinite-order status is made.

The raw JSON retains actual rational coordinates for every tested
\([n]S\), \(T\), \([n]T\) and proper-divisor multiple, including
identity markers when applicable. It also retains
\([j]R_1\) for \(j=1,2,3,4,5,6,8\). Thus the result is not a
list of unbacked boolean flags. As compact examples, the doubled basepoints
are stored as:
\[
\begin{array}{c|c|c}
 &X(2R_1)&Y(2R_1)/H\\ \hline
K_1& (696-2112t+2304t^2)/49
   &(39328-244672t+270336t^2)/343\\
K_2& (246+18W^2)/23
   &(-2092W+19692W^3)/3703
\end{array}
\]
These agree with the symbolic doubled-X formula in TC-G6. Field
faithfulness makes each saved nonzero coordinate vector genuinely nonzero
at the prescribed real embedding.

## 4. Complete scalar-square ledgers

The program reconstructs all scalar endpoints from the actual inverse
elliptic chart and the two approved frames. It compares these slots with
their expected center/width formulas, deduplicates actual field elements
and ordered pairs, and then evaluates every ordered pair of the resulting
same scalar set. No pole, complex parameter or repeated formal label is
counted as an extra scalar. No diagonal, reverse or unprescribed pair is
discarded.

Here \(N=|A|\), \(Q=|E|\), \(Z=|P(E)|\), \(B=N^2-Q\).
The matrix has 36 cells in each example. A histogram \(r:n_r\) means
\(n_r\) complete output fibers each have \(r\) ordered pairs.

| Example | \(N\) | \(Q\) | \(Z\) | \(B\) | Safe upper \(Z+B\) | Actual full image | Complete histogram |
|---|---:|---:|---:|---:|---:|---:|---|
| Original CP bridge | 6 | 8 | 3 | 28 | 31 | 29 | \(1:24,2:4,4:1\) |
| Forced two-width seed | 6 | 8 | 2 | 28 | 30 | 30 | \(1:28,4:2\) |

For both examples \(2Q/N=8/3\) and \(Q/N^2=2/9\).
The ratios \(Q/Z\) are respectively \(8/3\) and 4. The new
attachment reuses endpoints and has smaller prescribed support, but its
actual full image is one larger than the original bridge's. This finite
comparison is not promoted to an all-size theorem or a new compression
exponent.

For the two-width seed the complete nonsingleton fibers are precisely
the prescribed ones:

| Output | Ordered-pair representatives |
|---|---|
| \(c\) | \((q+h_1,q-s_1),(q+h_1,q+s_1),(q+H,q-h_1),(q+H,q+h_1)\) |
| \(0\) | \((q-h_1,q-s_1),(q-h_1,q+s_1),(q-H,q-h_1),(q-H,q+h_1)\) |

The remaining 28 pairs have 28 distinct singleton outputs. All coefficients
and pair representatives, including these singletons, are retained in the
JSON. Its scalar indices follow canonical coefficient order only; that
order is not asserted to be the real numerical order.

For the strict small-fiber pair mass
\(T(K)=\sum_{z:r(z)<K}r(z)\), the saved thresholds are \(1\le K\le7\):

| Example | \(T(1)\) | \(T(2)\) | \(T(3)=T(4)\) | \(T(5)=T(6)=T(7)\) |
|---|---:|---:|---:|---:|
| Original CP bridge | 0 | 24 | 32 | 36 |
| Forced two-width seed | 0 | 28 | 28 | 36 |

These are actual full-square tails, not just tails of a selected-edge
graph. They illustrate the missing near-complete coverage in these two
fixed examples; they do not resolve the unbounded tail obligation.

## 5. Independent audit of the earlier attachment proof

The imported B-CP proof in
[B_division.md](../2026-10-11-transfer-division-entropy/B_division.md)
reduces the original CP-O1 to five polynomial systems. The referee checked
the reduction separately: the zero row cannot be a permitted reused old
scalar, monotonicity restricts reused columns to \(\pm a\), and both
cannot occur. One reused column and the other source row exhaust all
possible roles. After simultaneous negation, the reused column is \(a\)
and the other source row is one of \(-d,-b,-a,b,d\).

With bars denoting normalization by \(h=\sqrt t\), let
\(W_0\) be the new signed width divided by \(h\). The two equations
are exactly
\[
C_A(W_0)=4tW_0^3-3W_0-\bar A,
\]
\[
Q_A(W_0)=4tW_0^2-2t(\bar a-\bar A)W_0
                  +t(\bar a-\bar A)^2-1.
\]
The current program loads only the saved rational coefficient arrays
from `attachments_results.json`. It imports no solver, field class or
certificate-generation routine from the earlier cycle. It directly
multiplies each saved \(U_AC_A+V_AQ_A\) in the independently implemented
field \(K_1[W_0]\).

Every product is exactly the coefficient sequence \((1,0,0,0,0)\),
where each entry is itself a degree-three field vector. All 75 rational
coefficient checks passed. Together with the inspected exhaustive role
reduction, this supplies an independent internal audit of B-CP's complete
proof, rather than a sampled failure to locate a root. It uses zero
target-polynomial evaluations and changes none of the earlier files.
Its scope remains precisely CP-O1's seed, zero row and two-old-endpoint
requirements; it does not exclude the distinct new seed in TC-G5.

## 6. Command, budget, hashes and claim limits

After compatibility and source review, the lead released this command,
which was run exactly once from the repository root:

```text
python3 research/notes/2026-10-11-torsion-compatible-sharing/exact_audit.py --compatibility-proof research/notes/2026-10-11-torsion-compatible-sharing/geometry.md --attachment-certificates research/notes/2026-10-11-transfer-division-entropy/attachments_results.json
```

It exited with code 0 under Python 3.12.7, with no failed assertion or
error. The recorded process CPU time was 0.114311 seconds, and wall time
0.114381 seconds. There was no rerun. Subsequent JSON inspection and
hashing evaluated no new polynomial or group operation.

| Item | Declared ceiling | Actual use |
|---|---:|---:|
| `(example, order)` cases | 6 | 6, from two fixed examples |
| Exact compatibility/arithmetic checks | 20,000 | 652 |
| Target \(P\) evaluations | 5,000 | 144 |

The 144 evaluations are the 72 distinct square cells times two evaluators;
the methods agreed on every cell. The 652 checks include 75 certificate
coefficient equalities, 100 inverse identities, 172 group-input and 84
group-result curve equations, 56 equal-X case checks, 72 target-oracle
agreements and the remaining explicit frame, projection, pair and ledger
checks. Their full category counts are saved in the JSON. These are
explicit mathematical predicates, not a claim to count every elementary
rational addition or multiplication performed inside them.

| Released artifact/input | SHA-256 |
|---|---|
| `geometry.md` at release | `0a6adbd799a08dc43c8a5063a9a46b8dadd09af3fd67ad753e4ce0e6238e0a7a` |
| New evaluator, including all frozen parameter definitions | `cc8347ebe0b74ae867c4ef35c676328b4ab233b38255bd525b26ddc326e3f819` |
| Saved five-certificate input JSON | `76072f08356684b59fbbadb864d51c8a4c6f80b1930383b504d300e57b863000` |
| Complete `exact-results.json` | `17069d583d612d7f949b191e39164124a872c46ceb5f42ef6593d4aa3fbc3cc4` |

The parameter inputs are fixed in the hashed evaluator and specified in
the hashed release proof; there is no external candidate input stream.
The result JSON repeats the exact moduli, root intervals, scalar scale,
curve coefficient, basepoints, frames, all tested group coordinates and
all full fibers. It refuses to overwrite an existing result. Later proof
metadata or finite-result annotations do not alter the proof-at-release
hash recorded here. Repository checks are performed once by the lead and
recorded separately in [verification.md](verification.md); this referee
did not rerun the software suite or the research program.

| Claim-record item | Exact scope |
|---|---|
| ID, track, polynomial | TC-X1; T01; \((x-y)^3+x+y\) |
| Date/version | 2026-10-11 / 1 |
| Quantifiers | Two specified algebraic examples; orders exactly 2,3,4; every marked admissible destination; both complete six-scalar squares |
| Dependencies | TC-G1–TC-G6 for complete compatible loci and exact maps; the stated irreducible coefficient fields; saved B-CP certificates and inspected role reduction |
| Evidence | Exact finite arithmetic, exhaustive in the declared finite scope; 652 checked predicates and two independent target evaluators |
| Internal audit | Lead inspected the new code before release; specialist separately inspected the same unchanged source. Referee inspected saved geometry, certificate products, exact coordinate examples, full counts and nonsingleton fibers |
| Retained gaps | No higher-order torsion classification, arbitrary division network, variable-output growth construction or asymptotic actual-image saving |

The new finite attachment is compatible, but none of the selected torsion
or division operations produces it from the marked basepoint. The fixed
paired-row loci cannot grow on those fixed curves. These conclusions
leave the unrestricted same-set T01 target and the existing actual
fiber-tail obligation **OPEN**. This appendix adopts no additional next
obligation.
