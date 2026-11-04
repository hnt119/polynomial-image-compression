# Independent referee: actual fibers, refinement, and six exact diagnostics

T01 | 21 October 2026 | version 1 | offline proof and exact-arithmetic audit.

The fixed polynomial is \(P(x,y)=(x-y)^3+x+y\).
For the refinement statements, \(A\subset\mathbb R\) is finite and
\(N=|A|\ge2\); the singleton case is immediate without refinement.
The global graph, branching, and weighted local-transfer statements in
[specialist.md](specialist.md), MC-S1–MC-S3, are **PROVED and independently
audited here**. They are necessary conditions for a small complete image,
not a construction or an unconditional compression theorem.
The six finite counts below are **EXPERIMENTAL: exhaustive and exact for
the explicitly fixed sets**. T01 remains **OPEN**.

## 1. MC-L0 and MC-S1: scaling and fiber geometry

For \(d_0=x_0-y_0\) and \(\delta>0\), direct expansion gives
\[
\begin{aligned}
P(x_0+\delta X,y_0+\delta Y)
={}&P(x_0,y_0)
+\delta[(1+3d_0^2)X+(1-3d_0^2)Y]\\
&+3d_0\delta^2(X-Y)^2+\delta^3(X-Y)^3.
\end{aligned}
\]
This is an exact identity. Discarding its higher-order terms would
replace exact fibers by a different relation.

For fixed \(y\), the map \(x\mapsto P(x,y)\) is strictly increasing,
has derivative \(1+3(x-y)^2\ge1\), and has range \(\mathbb R\).
Hence every exact level \(z\) is a global smooth graph \(x=f_z(y)\).
Putting \(d=f_z(y)-y\) gives
\[
f_z'(y)=\frac{3d^2-1}{3d^2+1},\qquad
d'(y)=-\frac2{3d^2+1},\qquad
f_z''(y)=-\frac{24d}{(3d^2+1)^3}.
\]
Thus \(|f_z'|\le1\), with equality only at \(d=0\), where
\(f_z'=-1\) and \(f_z''=0\). At \(d=\pm1/\sqrt3\),
\(f_z'=0\) and \(f_z''=\mp\sqrt3\).
There is no singular denominator at any of these differences.
The exact cubic remainder in the scaling identity persists when its
quadratic coefficient vanishes.

Take a finite half-open interval \(I_0\) containing \(A\), then refine
it into equal children. This defines a rooted, possibly translated
dyadic grid; it does not assume that the fixed grid with boundary zero
has a single cell containing both positive and negative inputs.
For any interval \(J\) of length \(\delta\), finitely many occupied
\(y\)-coordinates in \(J\) have diameter less than \(\delta\).
Their fiber \(x\)-coordinates have at most that diameter, and therefore
occupy at most two half-open \(x\)-cells of length \(\delta\).
This handles grid-boundary points without generic-position assumptions.

After \(k\) ordinary dyadic refinements of a parent square, a fixed
fiber occupies at most
\[
q_k=\min\{4^k,2^{k+1}\}
\]
child squares. In particular, splitting each scalar interval into
four children, as in MC-S1, permits at most eight occupied child
squares per parent fiber. The equality \(|f_z'|=1\) at one point
does not invalidate this finite-diameter argument.

The fiber coordinates
\[
x_z(d)=\frac{z-d^3+d}{2},\qquad
y_z(d)=\frac{z-d^3-d}{2}
\]
and the bound \(|F_z|\le |A|\) were already recorded in
[CR-P1 and CR-P3](../2026-09-21-cubic-returns/fibers-and-chains.md).
They are identified imports, not new claims of this audit.

## 2. MC-S2: the branch-count implication

Use the four-child scalar refinement and stop at a finite level whose
cell length is below the minimum separation of distinct elements of
\(A\). Each occupied terminal square contains one ordered pair.
For each exact output \(z\), its occupied-square tree has at most eight
children per node. Suppressing unary nodes preserves its leaves and
makes each leaf's depth equal its number of actual branching events.

Label the children of each branching node by distinct symbols from an
eight-symbol alphabet. Leaf words are prefix-free. A leaf at depth at
most \(b\) has at least one extension to length \(b\), and extensions
from different leaves are disjoint. Thus there are at most \(8^b\)
such leaves per output. With \(s=|P(A,A)|\),
\[
\#\{\xi\in A^2:B_L(\xi)\le b\}\le s8^b.
\]
Under the conditional hypothesis \(s\le N^{2-c}\), taking
\(b=\lfloor(c-\gamma)\log_8N\rfloor\), \(0<\gamma<c\), gives
at most \(N^{2-\gamma}\) low-branch pairs.

This proof was checked independently. It concerns branches of one
exact output fiber, not branches of input addresses or nearby output
bins. It does not bound the locations or spacings of branching levels,
or the terminal depth. It supplies no converse support upper bound.

## 3. MC-S3: terminal weights, overlap, and rich-mass transfer

For a square \(C=I\times J\), the exact local capacity is
\[
\operatorname{cap}(C)=\min\{|A\cap J|,3|A\cap I|\}.
\]
The first bound uses one \(x\) per \(y,z\); the second uses the
nonzero cubic equation in \(y\) for fixed \(x,z\).
The orientation and the factor three are correct, including repeated
polynomial roots, which do not increase the count of distinct \(y\)'s.

For a block of refinement levels, let \(M(C)\) be the maximum terminal
capacity inside a coarse square \(C\), and let \(S_C\) be its actual
output set. A terminal node need not have weight one before the
isolating level. The prefix argument gives at most \(8^b\) low-branch
terminal nodes per \(C,z\); multiplying by \(M(C)\) and summing yields
\[
\#\{\text{pairs with at most \(b\) branches in the block}\}
\le8^b\sum_C M(C)|S_C|.
\]
Distinct coarse cells partition the pairs, while a common output may
occur in many cells. Therefore
\[
\Omega=\frac1s\sum_C M(C)|S_C|
\]
correctly charges both terminal populations and cross-cell output
overlap. For \(R>0\), \(s\le N^2/R\) gives low-branch fraction at most
\(8^b\Omega/R\). The equality \(\Omega=1\) at the root requires
one coarse root square and singleton terminal capacities; one coarse
square alone is insufficient. MC-S3 states the required qualification.

There is also a direct rich-mass formulation. At an ordinary dyadic
level \(j\), put
\[
m_z(C)=|F_z\cap C|,\qquad
T_j(K)=\sum_{z,C}m_z(C)\mathbf1_{\{m_z(C)\ge K\}}.
\]
For \(K>0\), \(0<\theta<1\), and \(k\) ordinary dyadic refinements,
\[
(1-\theta)T_j(K)
\le T_{j+k}(\theta K/q_k)
\le T_j(\theta K/q_k),
\qquad T_{j+k}(K)\le T_j(K).
\]
To check the first inequality, a parent of mass \(m\ge K\) has at
most \(q_k\) occupied descendants. Descendants with mass below
\(\theta K/q_k\) have total mass less than \(\theta K\le\theta m\).
The other inequalities follow because each local fiber is contained
in its parent fiber. These are mass-weighted inequalities for actual
fibers, with no selected-pair or quantization substitution.

For the same refinement, let \(E_j=\sum_{z,C}m_z(C)^2\) and let
\(U_j\) count nonempty local fibers \((z,C)\). Then
\[
E_{j+k}\le E_j\le q_k E_{j+k},\qquad
U_j\le U_{j+k}\le q_k U_j.
\]
These follow from summing the elementary identities and inequalities
for a parent's at most \(q_k\) positive child masses.
They quantify refinement loss; they do not turn collision energy
into a small-image certificate.

## 4. MC-S4: prior scope and source applicability

The inspected
[quadratic projection note](../2026-09-21-sublinear-cubic/reuse-and-projections.md)
already treats fixed quadratic coefficient boxes, their real
conjugates, and incompatible external scales. Those scopes do not
automatically cover every nonuniform set \(B+\rho D\).
No previously proved projection result is relabeled here as a new
construction.

The specialist's external-source availability search was not repeated
by this referee. MC-S4 appropriately records its missing-source
limitation and asserts no imported Raz–Zahl theorem. This audit
accepts that separation of source status and theorem applicability;
it does not claim an independent whole-workspace literature search.
The implication from an applicable lower exponent \(\beta\) to a
contradiction with \(N^{2-c}\) indeed requires \(\beta>2-c\), or
appropriate additional constants at equality. Covering numbers and
exact support remain distinct.

## 5. MC-X1: independent exact counts

Only the six predeclared sets were enumerated. Every ordered pair was
evaluated exactly once by this independent verifier.

| Set | \(N\) | \(|P(A,A)|\) | Complete fiber histogram: size → number of outputs |
| --- | ---: | ---: | --- |
| \(\{0,\ldots,7\}\) | 8 | 44 | \(1\to36,\ 3\to4,\ 4\to4\) |
| \(\{0,\ldots,11\}\) | 12 | 108 | \(1\to96,\ 3\to2,\ 4\to8,\ 5\to2\) |
| Accepted CP ladder, \(m=2\) | 6 | 29 | \(1\to24,\ 2\to4,\ 4\to1\) |
| Accepted CP ladder, \(m=3\) | 8 | 52 | \(1\to44,\ 2\to6,\ 4\to2\) |
| \(\{0,1,3\}+\{0,1,3\}/64\) | 9 | 75 | \(1\to69,\ 2\to6\) |
| \(\{0,1,3\}+\{0,1,3,7\}/64\) | 12 | 136 | \(1\to128,\ 2\to8\) |

The [portable referee data](referee-counts.json) contain every scalar
label, every output fiber with its ordered-pair indices, every strict
small-fiber tail, and the complete executed verifier source. The lead
reported agreement with all six independent image sizes and histograms.
Metric covering numbers were not computed by this referee.

### Exact arithmetic and independence

The rational sets use standard-library rational arithmetic. For the
accepted [CP ladder](../2026-10-06-changed-collision-pattern/README.md),
the source uses \(t\) with
\[
64t^3-80t^2+28t-1=0,\qquad 0<t<1/12.
\]
This verifier instead uses \(U=4t\), so
\[
U^3-5U^2+7U-1=0,\qquad h^2=U/4,\qquad r/h=U-2.
\]
The monic cubic has no rational root: its only possible integer
roots are \(1,-1\), and neither vanishes. Thus the basis
\(1,U,U^2\) is faithful for exact equality. The actual scalar labels
are \(h[(2i-1)(U-2)+\sigma]\), with the index ranges in CP-C3.
The common nonzero factor \(h\) causes no equality ambiguity.

For normalized inputs \(X,Y\), the verifier computes the exact key
\[
4P(hX,hY)/h=U(X-Y)^3+4(X+Y).
\]
It reduces this polynomial by companion-operator Horner evaluation:
multiplication by \(U\) sends
\((a,b,c)\) to \((c,a-7c,b+5c)\).
This differs from the prior evaluator's rational \(t\)-basis long
division and fixed \(t\)-power table. The old source was inspected
but not imported or executed.

### Run and provenance

One inline Python 3 standard-library invocation executed the source
embedded in referee-counts.json. Python version: **3.12.7**.
Recorded calculation time: approximately **0.002741 seconds**.
The source SHA-256 is
4b3627a5800dc3b6d0a892419653a0c4ba408836b2106c2da41149e5fd5f7cf4.
Input-source hashes and the exact implementation are stored with the data.

The referee used **six instances, 533 polynomial evaluations, and
39 explicit accounting predicates**. There was no enlargement, rerun,
numerical root finding, package installation, network call, or frame
search. No finite result is used to infer a uniform asymptotic exponent.
The two nonuniform sets are diagnostics, not a successful new carrier.
Only this note and its count file were written by the referee; earlier
artifacts and status/library files were preserved.

## 6. Final saved-document check

The completed README and algebra appendix were read against the accepted
arguments and saved counts. **Accepted: no transcription, constant, or
scope error found.** Their direct refinement loss \(2\cdot4^k\) uses
four-way scalar generations, whereas section 3 above uses ordinary
binary levels. These are consistent.

All six full-image counts and fiber histograms match this referee's
oracle. The CP definitions and selected ledgers concern the earlier
ladder, not the later two-output TC attachment. Metric-cover and
branch-event tables match the lead's saved experiment summary; they
were not recomputed by this referee. That summary also records the
lead's successful comparison of all 533 ordered-pair outputs after
field-basis and input-order conversion.

The checked README SHA-256 is
f47f01566f3dd4b471359a3b37cf29372f4ac211669c71b5f0f43e9bd288f104;
the checked appendix SHA-256 is
75abc4d32ba2e031343f6c47e042ba2108aba7cfae37d6ac0f428ef7c109ef75.
MC-O1 is exactly one proposed OPEN diagnostic question, clearly
separated from the proved necessary conditions and finite observations.
It was not attempted. This final check made no new construction,
enumeration, or mathematical-program run.
