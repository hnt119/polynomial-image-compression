# Quadratic projections: exact reuse and actual-fiber obstructions

T01 / sublinear-step cubic cycle, 2026-09-21 v1.
The fixed polynomial is \(P(x,y)=(x-y)^3+x+y\).
These are new internal elementary proofs for the authorized offline cycle.
No experiment, network source, or arithmetic amplification is used.

The projection considered here is deliberately not faithful on cubic
coefficient polynomials: \((\sqrt D)^2=D\). This escapes the hypothesis
of GS-P4 in the preceding growing-step report. The argument below
instead uses the second real substitution \(\sqrt D\mapsto-\sqrt D\).
Its product gives an integer that cannot be arbitrarily small.
This is a diagnostic identity in one fixed quadratic field, not a
norm/trace construction, extension tower, or amplification scheme.

## 1. SC-Q1 — every collision is confined to a thin quadratic band

### Meaning

After a quadratic projection, different formal cubic coefficients can
indeed merge. But an exact equality must remain true after changing the
sign of the square root. These two real equalities sharply restrict the
difference of the original inputs. For fixed scales, only a vanishing
fraction of the Cartesian square passes this restriction.

### Statement

**PROVED.** Fix a positive nonsquare integer \(D\). Write
\(\mathcal K=\mathbb Q(\sqrt D)\), and use subscripts \(+\) and \(-\)
for the substitutions \(\sqrt D\mapsto\sqrt D\) and
\(\sqrt D\mapsto-\sqrt D\).
Let integers \(L,K\ge1\), \(h>0\), and \(t\in\mathbb R\) be given, with
\(\lambda=h^2\in\mathcal K\). Define
\[
A=t+h\{a+b\sqrt D:0\le a<L,\ 0\le b<K\},\qquad N=LK,
\tag{Q1}
\]
\[
\beta=\sqrt{|\lambda_+\lambda_-|}>0,\qquad
W=L-1+\sqrt D(K-1),\qquad R=\frac{8W}{3\beta}.
\]
If an ordered pair belongs to a nonsingleton actual cubic output fiber,
its unscaled difference \(p+q\sqrt D\) satisfies
\[
|p|<L,\quad |q|<K,\qquad |p^2-Dq^2|\le R.
\tag{Q2}
\]
Let \(\mathcal B_{L,K}(R)\) count the integer vectors satisfying (Q2).
The actual nonsingleton pair mass is at most
\[
\min\{N^2,N\mathcal B_{L,K}(R)\}.
\tag{Q3}
\]
In particular the entire image is at least \(N^2-N\mathcal B_{L,K}(R)\).
This lower bound comes from actual singleton outputs; it is not a
component-count certificate.

An explicit band estimate is
\[
\begin{aligned}
\mathcal B_{L,K}(R)\le\min\{&
(2L-1)(2K-1),\\
&(2K-1)(2\sqrt{2R}+2),\\
&(2L-1)(2\sqrt{2R/D}+2)\}.
\end{aligned}
\tag{Q4}
\]
Writing \(T=\max\{L,K\}\), \(m=\min\{L,K\}\), this gives
\[
\text{nonsingleton mass}
\le \min\{N^2,C_DNm(1+\sqrt{T/\beta})\}.
\tag{Q5}
\]
Thus whenever \(T\to\infty\) and \(\beta T\to\infty\), the actual
image is \(N^2-o(N^2)\), for arbitrary step inventories.

For the balanced unscaled box \(L=K\), \(h=1\), the sharper estimate is
\[
\text{nonsingleton mass}=O_D(L^3\log(2L))
 =O_D(N^{3/2}\log(2N)),
\tag{Q6}
\]
and hence
\[
|P(A,A)|=N^2-O_D(N^{3/2}\log(2N)).
\tag{Q7}
\]
The same conclusion holds for bounded-aspect rectangles and scales
with \(\beta\) bounded below by a fixed positive constant; in that
extension the implicit constant also depends on the fixed aspect bound
and the chosen positive lower bound for \(\beta\).

### Proof

Irrationality of \(\sqrt D\) makes the two input coefficients unique,
so \(N=LK\) exactly. Common translation only adds \(2t\) to an output.
Suppose distinct pairs have equal output. Write their unscaled
differences as \(\xi=p+q\sqrt D\) and \(\nu=p'+q'\sqrt D\), and
their unscaled sums as \(\Sigma,\Sigma'\). Dividing output equality
by \(h\) gives an identity in \(\mathcal K\):
\[
\lambda(\xi^3-\nu^3)=\Sigma'-\Sigma.
\tag{Q8}
\]
If \(\xi=\nu\), the sums also agree and the ordered pairs are identical.
Thus \(\Delta=\xi-\nu\ne0\). Its coefficients are integers, and
\[
|\Delta_+\Delta_-|
=|(p-p')^2-D(q-q')^2|\ge1.
\tag{Q9}
\]
The integer is nonzero because \(D\) is nonsquare.

At either substitution, \(|(\Sigma'-\Sigma)_\pm|\le2W\).
For all real \(a,b\),
\[
a^2+ab+b^2=(b+a/2)^2+3a^2/4\ge3a^2/4.
\]
Factoring the cubes in (Q8) therefore gives
\[
|\lambda_\pm|\,|\Delta_\pm|\,\frac34|\xi_\pm|^2\le2W.
\tag{Q10}
\]
Multiply the two inequalities and use (Q9). The result is
\[
\frac9{16}\beta^2|\xi_+\xi_-|^2\le4W^2,
\]
which is (Q2). A fixed difference vector has
\((L-|p|)(K-|q|)\le LK=N\) actual anchors. This proves (Q3).

For fixed \(q\), the admissible real \(p\)'s in
\(|p^2-Dq^2|\le R\) lie in at most two intervals of total length
at most \(2\sqrt{2R}\). They contain at most \(2\sqrt{2R}+2\)
integers. Interchanging the two coordinates gives the analogous bound
with \(R/D\). This proves (Q4), hence (Q5).
After division by \(N^2=(mT)^2\), its bound is
\[
C_D\left(T^{-1}+(\beta T)^{-1/2}\right),
\]
which tends to zero under the stated conditions.

For (Q6), \(R\le C_DL\). The range \(|q|\le C'_D\sqrt L\)
has \(O_D(\sqrt L)\) possible \(p\)'s for each \(q\), contributing
\(O_D(L)\) vectors. For larger \(|q|\), enlarge \(C'_D\) so that
\(Dq^2\ge2R\). The positive interval of possible \(p\)'s has length
\[
\sqrt{Dq^2+R}-\sqrt{Dq^2-R}
 =\frac{2R}{\sqrt{Dq^2+R}+\sqrt{Dq^2-R}}
 =O_D(L/|q|).
\]
The negative interval has the same length. Thus each \(q\) contributes
\(O_D(1+L/|q|)\) integer values. Summing to \(L\) gives
\(O_D(L\log(2L))\) difference vectors. Multiplying by at most \(L^2\)
anchors proves (Q6). Bounded-aspect rectangles with \(\beta\) bounded
below have the same argument, with all ranges \(O(L)\) and \(R=O(L)\).
\(\square\)

### Why it matters

This is an all-step theorem about actual fibers after a nonfaithful
projection. For unscaled rectangles of any aspect ratio, (Q5) also gives
the convenient uniform bound \(O_D(N^{7/4})\), since \(T\ge\sqrt N\).
For rational \(h^2\), one has \(\beta=h^2\), so the near-injectivity
criterion is \(h\sqrt T\to\infty\).
For general \(\lambda\in\mathcal K\), the two substitutions can have
very different magnitudes; their product, not the chosen real scale alone,
controls this obstruction.

### Scope

The field and its two real substitutions are fixed. The input is the
displayed coefficient rectangle; no statement about arbitrary subsets
with unrelated coefficient ranges is implicit. Neither (Q5) nor (Q6)
is a claim that every individual fiber is small. They bound the total
mass in nonsingleton actual fibers and therefore apply to every graph
inventory, including inventories of unrestricted size.
The regime \(\beta T\not\to\infty\) is not resolved by this bound.

## 2. SC-Q2 — at the critical shrinking scale, a quadratic image persists

### Meaning

At scale \(h\) of order \(L^{-1/2}\), the preceding thin-band estimate
can become inconclusive. Nevertheless, a positive fraction of source
pairs have large differences in both real substitutions. An equal-output
partner must then have almost the same two integer coefficients. Only
a bounded number of partners are possible, so the actual image is still
of quadratic order.

### Statement

**PROVED.** In (Q1), take \(K=L\ge8\) and assume \(h^2\in\mathbb Q\).
Put \(N=L^2\),
\[
\gamma_D=\frac7{2048\sqrt D},\qquad
C_D=\frac{512(1+\sqrt D)}{27}.
\]
Then
\[
|P(A,A)|\ge
\frac{\gamma_D N^2}{\left(1+2C_D/(h^2L)\right)^2}.
\tag{Q11}
\]
For every fixed \(\kappa>0\), if \(h^2L\ge\kappa\), this is
\[
|P(A,A)|\ge c_{D,\kappa}N^2,
\qquad
c_{D,\kappa}=\frac{\gamma_D}{(1+2C_D/\kappa)^2}>0.
\tag{Q12}
\]
Moreover at least \(\gamma_DN^2\) pair vertices then belong to actual
fibers of size at most \((1+2C_D/\kappa)^2\). No step inventory can
place these vertices in components of polynomially growing size.

### Proof

Select source difference indices satisfying
\[
L/2\le p\le3L/4,\qquad
|q|\le L/(8\sqrt D).
\tag{Q13}
\]
There are at least \(L/8\) choices of integer \(p\) when \(L\ge8\),
and at least \(L/(8\sqrt D)\) integer choices of \(q\).
Each difference has at least
\[
(L-|p|)(L-|q|)\ge (L/4)(7L/8)=7L^2/32
\]
anchors. These differences therefore supply at least
\(\gamma_D L^4=\gamma_DN^2\) distinct source pairs.
Both of their conjugate differences satisfy
\[
3L/8\le\xi_\pm\le7L/8.
\]

For any pair anywhere in the entire same output fiber, (Q10), now with
\(\lambda_+=\lambda_-=h^2\), gives
\[
|\Delta_\pm|
\le\frac{8(L-1)(1+\sqrt D)}{3h^2(3L/8)^2}
\le\frac{C_D}{h^2L}.
\tag{Q14}
\]
Writing \(\Delta=r+s\sqrt D\), with integers \(r,s\), gives
\[
|r|\le C_D/(h^2L),\qquad
|s|\le C_D/(\sqrt D\,h^2L).
\]
There are at most \((1+2C_D/(h^2L))^2\) such integer vectors.
For a fixed output and fixed difference, the original ordered pair is
uniquely determined by the inverse coordinate formulas. Hence this
bounds the whole actual fiber, not merely its selected subset.

Divide the selected pair mass by that fiber-size bound to obtain
(Q11). The final component assertion follows because a component lies
inside its actual fiber. \(\square\)

### Why it matters

The changing-scale boxes cannot yield a fixed power saving while
\(h^2L\) stays bounded below. This includes the critical scale
\(h\asymp L^{-1/2}=N^{-1/4}\), beyond the near-injectivity conclusion
of SC-Q1.

### Scope

The critical-scale statement uses rational \(h^2\), so that its value is
the same under both substitutions. The general algebraic-scale version
of SC-Q1 uses the explicitly charged product \(\beta\) instead.
The regime \(h^2L\to0\) remains outside (Q12); this is an unclosed
regime, not positive evidence for a carrier.

## 3. SC-Q3 — an exact many-to-one scalar projection still fails

### Meaning

The user-requested many-to-one projection can be made completely explicit.
A three-dimensional box collapses to only order \(L^2\) real scalars,
with average multiplicity of order \(L\). This is substantial parameter
reuse, but it does not produce the needed cubic output reuse.

### Statement

**PROVED.** Fix the same \(D\), and let \(L\ge D\). Project
\[
(a,b,c)\in\{0,\ldots,L-1\}^3
\quad\longmapsto\quad
a+b\sqrt D+c(\sqrt D)^2.
\]
Its scalar image is exactly
\[
A_L=\{r+b\sqrt D:
0\le r\le(D+1)(L-1),\quad 0\le b<L\}.
\tag{Q15}
\]
Therefore
\[
N=|A_L|=((D+1)(L-1)+1)L.
\tag{Q16}
\]
For a given scalar \(r+b\sqrt D\), the exact parameter multiplicity is
\[
\mu(r)=
\left(
\min\{L-1,\lfloor r/D\rfloor\}
-\max\{0,\lceil(r-L+1)/D\rceil\}+1
\right)_+.
\tag{Q17}
\]
In particular \(\mu(r)\le\lceil L/D\rceil\), and its average over the
actual scalar set is \(L^3/N\sim L/(D+1)\).
Nevertheless
\[
|P(A_L,A_L)|
=N^2-O_D(N^{3/2}\log(2N)),
\tag{Q18}
\]
with only \(O_D(N^{3/2}\log(2N))\) vertices in nonsingleton actual
fibers, for every step inventory.

### Proof

The scalar is \((a+Dc)+b\sqrt D\), so its two displayed coefficients
are unique. For successive \(c\), the intervals of possible first
coefficients are
\([Dc,Dc+L-1]\cap\mathbb Z\).
They overlap or are adjacent because \(L\ge D\). Their union is
exactly the interval in (Q15), proving (Q16).
For fixed \(r\), the equation \(a=r-Dc\) requires
\[
\max\{0,\lceil(r-L+1)/D\rceil\}
\le c\le
\min\{L-1,\lfloor r/D\rfloor\}.
\]
Counting these integers gives (Q17). Their interval has length at most
\((L-1)/D\), giving the maximum bound; averaging counts all \(L^3\)
parameter points once.

The actual image (Q15) is a bounded-aspect coefficient rectangle, with
aspect ratio tending to \(D+1\). Apply the bounded-aspect conclusion
of SC-Q1 to obtain (Q18). No parameter multiplicity is counted as an
extra scalar or as an output collision. \(\square\)

### Why it matters

This tests a genuinely nonfaithful scalar projection, not just a
projection nonfaithful on output coefficients. Its \(L^3\) descriptions
yield only \(N\asymp L^2\) scalars, but the true Cartesian square still
has almost \(N^2\) distinct outputs. Parameter reuse by itself is
insufficient.

### Scope

The projection and \(D\) are fixed before \(L\) grows. Its exact
multiplicity and all cross-pairs are charged. This is not a theorem
about arbitrary algebraic relations, growing field degree, or
correlated subsets of the three-dimensional parameter box.

## 4. SC-Q4 — a generic external scale eliminates every collision

### Meaning

Scaling does not automatically create more collisions. If the square
of the scale lies outside the coefficient field, any purported
collision would express that scale as a quotient of field elements.

### Statement

**PROVED.** For any finite \(B\subset\mathcal K\), \(t\in\mathbb R\),
and \(h>0\) with \(h^2\notin\mathcal K\), the polynomial \(P\) is
injective on \((t+hB)^2\). Thus every actual fiber is a singleton and
no nonzero step has a return.

### Proof

Equal outputs give \(h^2(\xi^3-\nu^3)=\Sigma'-\Sigma\) with all
\(\xi,\nu,\Sigma,\Sigma'\in\mathcal K\). If \(\xi=\nu\), the sums
also agree, so the pairs are identical. Otherwise real cube
injectivity gives \(\xi^3-\nu^3\ne0\), and the equality forces
\[
h^2=\frac{\Sigma'-\Sigma}{\xi^3-\nu^3}\in\mathcal K,
\]
a contradiction. \(\square\)

### Why it matters and scope

Within this coefficient model, useful scales must respect a precise
algebraic restriction. This is a necessary condition only; SC-Q1–Q3
show that many scales inside the field also fail. No search over
algebraic extensions is proposed.

## 5. Full accounting, provenance, and retained boundary

The preceding cycle's GS-P3 and GS-P4 are used only to identify which
old hypotheses are escaped. Here \((\sqrt D)^2=D\) destroys formal
coefficient faithfulness, and the irrational two-coordinate carrier
is not contained in a fixed real lattice. The new proofs do not invoke
the missing historical regular-digital or rich-fiber originals, any
finite experiment, or an external theorem. The only algebraic fact
beyond displayed arithmetic is that \(1,\sqrt D\) are linearly
independent over \(\mathbb Q\).

The scalar input counts are exact: \(LK\) for (Q1), and (Q16) for
the three-parameter projection. There is no thinning; both coordinates
use the same actual scalar set. Projection multiplicity is one for
the two-coordinate basis and exactly (Q17) for the three-parameter
construction. Every ordered pair is included. Actual singleton-fiber
mass supplies the image lower bounds in SC-Q1/Q3, while an explicitly
counted positive fraction with uniformly bounded actual fibers supplies
SC-Q2. No energy-to-support inference is used.

The field degree is fixed at two and \(D\) is fixed; no regulator,
splitting condition, local prime, extension tower, or arithmetic rate
is used. The scale is charged through \(\beta\) in SC-Q1 and \(h^2L\)
in SC-Q2. Coefficient widths, possible anisotropy, and real
archimedean distortion are explicit in \(W,T\) and the displayed
conjugate inequalities. If scales vary, no unspecified height or
denominator cost is declared zero. There is no positive construction
whose denominator cost must be absorbed: these direct real equalities
and inequalities hold at each stated scale. Step inventories may be
arbitrarily large in every obstruction, so no inventory cost is hidden.

| ID | Status and exact scope | Evidence locator and dependencies | Remaining boundary |
|---|---|---|---|
| SC-Q1 | PROVED; fixed nonsquare \(D\), every coefficient rectangle and scale \(h^2\in\mathcal K\) | §1, two real substitutions and integer product | Thin-band conclusion may be weak when \(\beta T\) is small |
| SC-Q2 | PROVED; balanced boxes, rational \(h^2\), critical scale \(h^2L\ge\kappa>0\) | §2, explicit positive pair mass and full-fiber bound | \(h^2L\to0\) not settled |
| SC-Q3 | PROVED; fixed quadratic relation and all \(L\ge D\) | §3, exact projection fibers and SC-Q1 | No general claim about correlated parameter subsets |
| SC-Q4 | PROVED; any finite \(B\subset\mathcal K\), scale square outside \(\mathcal K\) | §4, exact collision identity | Scales inside the field need separate analysis |

All claims are T01, the fixed plus-sign cubic, version 1 dated
2026-09-21. Evidence consists of the complete internal arguments above.
Two independent internal reviews, by the coordinating agent and the
parallel obstruction agent, checked SC-Q1–Q4 without finding a
mathematical gap. The latter review clarified the constant dependencies
in the bounded-aspect extension; that clarification is incorporated above.
No external review or novelty claim is made. The original cubic
power-saving target and the commissioned sublinear-inventory witness
remain OPEN; no positive asymptotic witness is supplied by these models.
