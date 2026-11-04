# Variable-gap sharing networks: exact gluing, insufficient coverage

T01 · 6 October 2026 · version 1 · offline, internally audited research.
Fixed target: \(P(x,y)=(x-y)^3+x+y\) on one finite real set in both coordinates.

## Verdict

**PROVED — VG-C1–C3.** Variable output gaps permit a compatible network
with growing endpoint reuse, growing selected fibers, and growing numbers
of partners for every selected edge. One explicit output-first family has
\[
N=k^3,\qquad Q=2k^4-k^2-k,\qquad Z=2k^3-k\quad(k\ge3).
\]
It improves on the earlier linear prescribed-pair mechanisms, but **does
not improve the \(N^{4/3}\) rate already attained by GS-P3**. Its scalar
completion is an integer interval, so its actual full image is
\(N^2-O(N^{3/2})\). This family fails the fixed-power-saving target.
The unrestricted T01 target remains **OPEN**.

The new constructive content is explicit simultaneous gluing, including
cross-pairs between triangle partners. The failure concerns distant-block
pairs, not a failure to solve individual sharing equations.

## Compatibility mechanism

**PROVED — VG-G1. Meaning:** one anchor and three differences enforce
the entire shared-edge motif at once. Write its five ordered outputs as
\((z_0,z_1,z_2,z_3,z_4)\), for
\((a,b),(b,c),(c,a),(b,d),(d,a)\). Put
\[
u=a-b,\quad v=b-c,\quad t=b-d,
\]
\[
F(u,s)=s^3-u^3-u-s,\qquad G(u,s)=-(u+s)^3-u^3-s.
\]
**Statement:** necessary and sufficient equations are
\[
z_1-z_0=F(u,v),\quad z_2-z_0=G(u,v),\quad
z_3-z_0=F(u,t),\quad z_4-z_0=G(u,t),
\]
with \(b=(z_0-u^3-u)/2\), \(a=b+u,c=b-v,d=b-t\).
**Proof:** substitution gives all four equations; reconstruction proves
the converse. Four distinct vertices require
\(uvt(u+v)(u+t)(v-t)\ne0\).
**Scope:** these equations enforce sharing; they do not supply density.
The coordinate-template derivation and all endpoint signs are in
[the compatibility appendix](compatibility.md#1-vg-g1--exact-simultaneous-shared-edge-equations).

**PROVED — VG-G2. Meaning:** the tentative uniqueness statement is valid
over the reals for every cycle length. **Statement:** prescribed ordered
outputs determine at most one real directed cycle, allowing repeated
vertices. **Proof:** comparing two cycles gives
\((1+h_i)\alpha_i+(1-h_i)\alpha_{i+1}=0\), where
\(h_i=d_i^2+d_id_i'+(d_i')^2\ge0\). Cyclic absolute-value inequalities
force all \(|\alpha_i|\) equal. A nonzero common value would force every
\(h_i=0\); then both differences vanish, so adjacent displacements are
both equal and opposite, a contradiction. **Scope:** this includes even
cycles, whose degenerate comparison matrix alone would not prove the
claim. It does not restrict freely varying output lists or assert their
existence. [Complete proof](compatibility.md#2-vg-g2--uniqueness-for-every-directed-real-cycle).

## The explicit family and one worked motif

**PROVED — VG-G3/C1/C2. Meaning:** correlated output windows close the
network with actual scalar reuse, rather than naming outputs after choosing
arbitrary vertices. First choose \(k\ge3,L=k^3\), then prescribe
\[
1\le|u|\le k,\qquad z=2j,\qquad
\frac{u^3+|u|}{2}\le j\le L-1+\frac{u^3-|u|}{2},\quad j\in\mathbb Z.
\]
Put \(f(u)=(u^3-u)/2\), \(g(u)=(u^3+u)/2\), and reconstruct
\((x,y)=(j-f(u),j-g(u))\). **Statement:** their scalar union and
distinct prescribed pairs are exactly
\[
A_k=\{0,\ldots,L-1\},\qquad
E_k=\{(x,y)\in A_k^2:1\le|x-y|\le k\}.
\]
For a base label \((j,u)\) and partner difference \(v\), the two exact
gluing labels are
\[
(j-g(u)+f(v),v),\qquad (j-f(u)-g(u+v),-u-v).
\]
Use the same formulas with \(t\) for the second partner.

**Proof:** the window inequalities are equivalent to both reconstructed
endpoints lying in \([0,L-1]\). The two shifts reconstruct precisely
\((b,c),(c,a)\). Every base edge lies in a consecutive block of \(k+1\)
vertices inside \(A_k\); each of the other \(k-1\) vertices is a valid
partner. Any two distinct partners give the requested motif, and both
cross-partner edges also belong to \(E_k\). All shifted labels satisfy
their own windows. Moreover \(E_k\subset E_{k+1}\): old vertices acquire
new partners as the allowed differences grow. No new pair is credited
merely because another motif describes it.

For \(k=3\), choose \((a,b,c,d)=(1,0,2,3)\):

| Edge | Label \((j,u)\) | Output \(2j\) |
|---|---:|---:|
| \((1,0)\) | \((1,1)\) | 2 |
| \((0,2)\) | \((-3,-2)\) | −6 |
| \((2,1)\) | \((2,1)\) | 4 |
| \((0,3)\) | \((-12,-3)\) | −24 |
| \((3,1)\) | \((6,2)\) | 12 |

This motif alone has five outputs. Reuse belongs to the assembled network:
for example, its distinct pairs \((1,0)\) and \((1,2)\) both output 2.
**Scope:** local cross-partner closure does not cover distant blocks.
[Full reconstruction and boundary proof](construction.md).

## Exact ledger and full-square limitation

**PROVED — VG-C1/C3. Statement:** summing \(L-|u|\) pairs per difference
and taking the union of the overlapping output windows gives
\[
\begin{aligned}
N&=k^3,& Q&=2k^4-k^2-k,& Z&=2k^3-k,\\
B&=k^6-2k^4+k^2+k,&
|P(A_k,A_k)|&\le Z+B=k^6-2k^4+2k^3+k^2.
\end{aligned}
\]
In particular \(Q\le NZ\), as required. The three simultaneous ratios are
\[
\frac{2Q}{N}=4k-\frac2k-\frac2{k^2},\qquad
\frac QZ=\frac{2k^4-k^2-k}{2k^3-k}\sim k,\qquad
\frac Q{N^2}=\frac2{k^2}-\frac1{k^4}-\frac1{k^5}\longrightarrow0.
\]
**Proof:** label-to-pair reconstruction is injective; the output-index
union is exactly \([-f(k),L-1+f(k)]\cap\mathbb Z\). Every omitted pair,
including every diagonal, is charged in \(B\). **Scope:** the output gate
\(Z=O(N)\) holds, while \(B=N^2-\Theta(N^{4/3})\) fails every required
subquadratic complement bound. Cubic displacement needs output span
\(L+k^3-k\), but only \(2k\) differences are selected at a scalar.

The stronger actual-image conclusion imports **PROVED GS-A4**, whose proof
was inspected and its spacing-1 specialization independently checked here.
If two integer pairs collide, their differences \(d,e\) satisfy
\(|d^3-e^3|\le2(N-1)\); for distinct integer differences the left side
is at least \(d^2\). Thus all pairs with
\(|d|>D=\min(N-1,\lfloor\sqrt{2(N-1)}\rfloor)\) are singleton fibers,
giving
\[
|P(A_k,A_k)|\ge(N-D)(N-D-1)=N^2-O(N^{3/2}).
\]
This also prevents a different estimate on the same complement from
rescuing this carrier. It is not an obstruction for arbitrary real networks.

**EXPERIMENTAL — VG-X1.** One released exact run enumerated the complete
actual squares at three sizes, after the proofs and source were reviewed:

| \(k\) | \(N\) | \(Q\) | \(Z\) | \(B\) | \(Z+B\) | Actual image |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 27 | 150 | 51 | 579 | 630 | 593 |
| 4 | 64 | 492 | 124 | 3604 | 3728 | 3580 |
| 5 | 125 | 1220 | 245 | 14405 | 14650 | 14185 |

The run used 20,450 exact integer evaluations and 9,349 charged checks.
Complete fiber distributions, all scalar/pair deduplication, and every-edge
motif certificates are in [the exact audit](exact-audit.md) and
[portable data](../../../examples/2026-10-06-variable-gap-sharing.json).
These finite tests are not the asymptotic proof.

## Exactly one next proof obligation

**OPEN — VG-O1: deform the same finite incidence pattern off the interval.**
The smallest change proposed here is to let the real scalar positions and
output values move while preserving the declared output coincidences.
Decide whether there are strictly increasing real numbers
\(x_0<\cdots<x_{26}\), with \(x_0=0\), not forming an arithmetic
progression, and pairwise distinct real \(w_j\), \(-12\le j\le38\), such that
\[
P(x_i,x_\ell)=w_{((i-\ell)^3+i+\ell)/2}
\quad\text{for every }0\le i,\ell\le26,
\quad1\le|i-\ell|\le3.
\]
Produce one exact nonarithmetic realization, or prove this finite pattern
rigid among increasing real embeddings. The known solution is
\(x_i=i,w_j=2j\). This modifies the scalar completion while keeping all
150 prescribed edges and their 51 output classes fixed in advance.
Cycle uniqueness does not answer it because the \(w_j\) vary.
No such deformation has been proved here; even one would still be only
a finite seed, with no implied scaling or full-square saving.

## Provenance and appendices

The accepted [elliptic checkpoint](../2026-09-30-elliptic-geometry/README.md)
and latest [sharing report](../2026-10-06-sharing-compatibility/README.md)
remain unchanged. Their global elliptic and fixed-gap results are imported,
not claimed as new audits. The new shared-edge/cycle proofs and construction
were checked by their authors, the lead, and the exact/referee agent.
The GS-P3 comparison and GS-A4 specialization were read at their formal
proofs. No internet, installation, arithmetic tower, literature assessment,
novelty claim, or unrelated carrier search was used.

Long derivations: [compatibility](compatibility.md);
[construction and complete cost ledger](construction.md);
[exact computation](exact-audit.md);
[proof provenance, budget, and repository checks](verification.md).
