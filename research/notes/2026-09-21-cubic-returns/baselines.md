# Elementary Cartesian-return baselines

2026-09-21, v1. T01, \(P(x,y)=(x-y)^3+x+y\).
This is an analytic companion to the explicitly authorized offline
Cartesian-return cycle. No numerical experiment, network source, or
arithmetic amplification is used. All new proofs below are internal.

The starting identity is TC-Q1 in
../2026-09-16-three-branch-continuation/rates-and-fiber-maps.md, §4:
in coordinates \(u=x-y,\ z=P(x,y)\), the map \(T_1\) sends
\((u,z)\) to \((u+1,z)\). Put
\[
c(u)=\frac{3u^2+3u+2}{2}
=\frac32\left(u+\frac12\right)^2+\frac58.
\]
A return with anchor \(y\) requires all four scalars
\[
y,\quad y+u,\quad y-c(u),\quad y-c(u)+u+1
\tag{B0}
\]
to lie in the same set \(A\). We count these ordered returning pairs by
\(E_1(A)\). A path's size below means its number of pair vertices; its
number of edges is one less.

## 1. CR-B1 — integer intervals have order \(N^{3/2}\) returns

**Plain-language meaning.** Every usable difference can have order \(N\)
anchors, but the downward shift has size comparable to the square of the
difference. Only order \(\sqrt N\) differences fit. Translation and
centering do not change this count.

**PROVED.** For \(I_N=\{0,\ldots,N-1\}\), \(N\ge1\), let
\[
M=\left\lfloor\frac{\sqrt{24N+1}-5}{6}\right\rfloor.
\]
Then
\[
\begin{aligned}
E_1(I_N)
&=2\sum_{v=0}^{M}
\left(N-1-\frac{3v^2+5v}{2}\right)\\
&=(M+1)(2N-2-M^2-3M)\\
&=\frac43\sqrt{\frac23}\,N^{3/2}+O(N).
\end{aligned}
\tag{B1}
\]
The same formula holds for every translate \(t+I_N\), including a
symmetric integer progression with \(N\) terms.

**Proof.** For \(u=v\ge0\), the four offsets in (B0), relative to \(y\),
are \(0,v,-c(v),v+1-c(v)\). Their minimum is \(-c(v)\) and their
maximum is \(v\), since \(c(v)\ge1\). Thus exactly
\[
\bigl(N-v-c(v)\bigr)_+
=\left(N-1-\frac{3v^2+5v}{2}\right)_+
\]
integer anchors work, where \(r_+=\max\{r,0\}\).
For \(u=-v-1\), \(v\ge0\), one has \(c(u)=c(v)\), and the extreme
offsets are \(-c(v)-v\) and \(0\). The anchor count is the same.
These two cases partition all integer differences. The displayed
cutoff is exactly the nonnegative root cutoff; including a zero last
summand makes no difference. Summing \(v\) and \(v^2\) gives (B1).
Since \(M=\sqrt{2N/3}+O(1)\), the asymptotic follows.

Adding a common real \(t\) to all four scalars preserves (B0), proving
translation invariance. \(\square\)

**Scope.** This gives the explicit lower bound
\[
R_1(N)\ge
\left(\frac43\sqrt{\frac23}+o(1)\right)N^{-1/2}.
\tag{B2}
\]
It gives no positive limiting return density and no upper bound for the
complete cubic image.

## 2. CR-B2 — fixed-step arithmetic progressions

**Plain-language meaning.** A unit move in the difference must fit the
progression's spacing. If it fits, the quadratic shift still limits the
usable differences to order \(\sqrt N\). Symmetric progressions have
exactly the same behavior as their translates.

**PROVED.** Fix \(h>0\), and allow any real center \(t\). For
\(A=t+h\{0,\ldots,N-1\}\):

- if \(1/h\notin\mathbb Z\), then \(E_1(A)=0\);
- if \(h=1/q\), \(q\) a fixed positive integer, then
  \(E_1(A)=\Theta_q(N^{3/2})\) as \(N\to\infty\).

In the second case there is also the exact finite formula below. For
\(d\in\mathbb Z\), put
\[
b_q(d)=\frac{3d^2+3qd+2q^2}{2q},\qquad
\mathcal O_q(d)=\{0,d,-b_q(d),d+q-b_q(d)\},
\]
and \(w_q(d)=\max\mathcal O_q(d)-\min\mathcal O_q(d)\). Then
\[
E_1(A)=
\sum_{\substack{d\in\mathbb Z\\2q\mid3d(d+q)}}
\bigl(N-w_q(d)\bigr)_+.
\tag{B3}
\]
Only finitely many summands are nonzero.

**Proof.** Both the original difference \(u\) and the new difference
\(u+1\) must belong to \(h\mathbb Z\). Therefore \(1\in h\mathbb Z\)
is necessary. If \(h=1/q\), write \(u=d/q\).
The shift \(c(u)\), in units of \(h\), is \(b_q(d)\), and all four
offsets in (B0), in those same units, are precisely
\(\mathcal O_q(d)\). They are integral exactly when
\(2q\mid3d(d+q)\). An integral list of offsets of span \(w\) fits into
\(\{0,\ldots,N-1\}\) at exactly \((N-w)_+\) anchors. This proves (B3).

For an upper bound, \(y,y-c(u)\in A\) implies
\(c(u)\le (N-1)/q\). Thus there are only \(O_q(\sqrt N)\)
possible integer \(d\), each with at most \(N\) anchors.
For a lower bound, choose nonnegative \(d\) divisible by \(2q\).
These always satisfy the divisibility condition, and for \(d\ge0\)
\[
w_q(d)=d+b_q(d)=\frac{3d^2}{2q}+\frac52d+q.
\]
For a sufficiently small fixed \(\gamma_q>0\), all such
\(d\le\gamma_q\sqrt N\) have \(w_q(d)\le N/2\), for all sufficiently
large \(N\). There are \(\gg_q\sqrt N\) of them, each with at least
\(N/2\) anchors. \(\square\)

**Scope.** The step is fixed before \(N\) grows. In particular, constants
in this statement are not uniform for denominators \(q\to\infty\).
Centers may depend on \(N\), because common translation changes nothing.
The zero-return case is a statement about this fixed \(T_1\), not a
statement about all \(T_\tau\) or all cubic collisions.

**A stronger explicit lower constant.** The step \(h=1/3\) has no
divisibility loss in (B3), since
\(b_3(d)=(d^2+3d+6)/2\) is integral for every integer \(d\). Put
\[
K=\left\lfloor\frac{\sqrt{8N+1}-5}{2}\right\rfloor\ge-1.
\]
An empty sum when \(K=-1\) is zero. Then
\[
\begin{aligned}
E_1\bigl(\{j/3:0\le j<N\}\bigr)
&=2(N-2)_+
 +2\sum_{d=0}^{K}\left(N-\frac{d^2+5d+6}{2}\right)\\
&=\frac{4\sqrt2}{3}N^{3/2}+O(N).
\end{aligned}
\tag{B3a}
\]
Indeed, \(d\ge0\) has span \((d^2+5d+6)/2\), its partner
\(-d-3\) has the same span, and the two remaining differences
\(d=-1,-2\) each have span two. Since \(K=\sqrt{2N}+O(1)\), summing
the quadratic gives the displayed asymptotic. Consequently the
strongest explicit lower bound established in this note is
\[
R_1(N)\ge\left(\frac{4\sqrt2}{3}+o(1)\right)N^{-1/2}.
\tag{B3b}
\]
No optimization over every fixed step is claimed.

## 3. CR-B3 — bounded unions of progressions, even far apart

**Plain-language meaning.** Separating a bounded number of progression
blocks does not defeat the quadratic-shift restriction. For each anchor,
the possible downward shifts lie in a bounded number of intervals of
length order \(N\). Pulling these intervals back through \(c(u)\) leaves
only order \(\sqrt N\) candidate locations in each progression.

**PROVED.** Fix \(k\ge1\) and \(0<h_-\le h_+<\infty\). Let
\[
A=\bigcup_{j=1}^k
\{t_j+h_jr:0\le r<n_j,\ r\in\mathbb Z\},
\qquad h_-\le h_j\le h_+,
\tag{B4}
\]
and let \(N=|A|\). Empty blocks can be omitted. Then
\[
E_1(A)=O_{k,h_-,h_+}(N^{3/2}).
\tag{B5}
\]
The estimate is uniform in all centers \(t_j\), including centers which
separate arbitrarily rapidly with \(N\). The steps need not be rational
or commensurable. Overlaps among the blocks are allowed.

**Proof.** Each block has \(n_j\le N\), so its interval hull has length
at most \(h_+N\). Hence \(A-A\) is contained in a union of \(k^2\)
closed intervals, each of length at most \(2h_+N\).
For any interval \(J\) of length \(W\), the inverse image
\(c^{-1}(J)\) has at most two interval components, with total length
at most \(2\sqrt{2W/3}\). This follows from the displayed completed
square for \(c\) and
\(\sqrt b-\sqrt a\le\sqrt{b-a}\), \(0\le a\le b\).
Consequently all return differences belong to a union \(S\) of at most
\(2k^2\) intervals, with total length
at most \(4k^2\sqrt{h_+N/3}\).

Fix the anchor \(y\in A\). On any one progression of step at least
\(h_-\), the possible values \(x=y+u\), \(u\in S\), number at most
\[
\frac{4k^2}{h_-}\sqrt{\frac{h_+N}{3}}+2k^2.
\]
Sum this bound over the \(k\) blocks and then the \(N\) anchors.
This counts a superset of the actual returns and proves (B5). \(\square\)

**Differences and anchors.** With a common step, the differences lie in
a bounded number of lattice translates, and only \(O(\sqrt N)\)
distinct differences can contribute. For incommensurable steps, that
global difference count is not asserted: the proof instead bounds the
number of useful differences separately at each anchor.

**Scope.** This includes bounded unions of integer intervals, symmetric
progressions, and widely separated fixed-step blocks. It does not cover
a growing number of blocks or steps tending to zero without charging
their growing constants.

## 4. CR-B4 — maximum orbit lengths in these progression families

**Plain-language meaning.** Long paths do occur in intervals. Their
length is only order \(N^{1/3}\), and they occupy a vanishing fraction
of the Cartesian square. Moving a bounded number of blocks far apart
does not increase this order.

**PROVED.** If a finite real set \(A\) has diameter \(D\), every
\(T_1\)-path has at most \(2D^{1/3}+1\) vertices. More generally, if
\(A\) has the form (B4), every path has at most
\[
2k^2(h_+N)^{1/3}+k^2
\tag{B6}
\]
vertices, uniformly in the centers. For the single progression
\(t+q^{-1}\{0,\ldots,N-1\}\), fixed positive integer \(q\), the maximum
path size is \(\Theta_q(N^{1/3})\).

**Proof.** A path fixes one output \(z\) and has successive differences
\(u,u+1,\ldots\). Since \(u^3=z-(x+y)\), a set of diameter \(D\)
confines all these cubes to an interval of length \(2D\).
For real \(a\ge b\),
\[
a^3-b^3=3\left(\frac{a+b}{2}\right)^2(a-b)
 +\frac{(a-b)^3}{4}\ge\frac{(a-b)^3}{4}.
\]
Thus an interval of cube values of length \(W\) pulls back to an
interval of length at most \((4W)^{1/3}\). A unit-spaced run in it
has at most that length plus one vertices. This proves the first bound.

For (B4), all sums \(x+y\) lie in \(k^2\) interval hulls, each of length
at most \(2h_+N\). Their inverse cube images have total length at most
\(2k^2(h_+N)^{1/3}\) and at most \(k^2\) interval components.
Each path lies in one translate of \(\mathbb Z\), giving (B6).

For the lower bound in the reciprocal-step progression, choose an
interior grid point \(a\) within one grid step of the midpoint. At output
\(z=2a\), the pairs at integer differences \(r\) have coordinates
\[
x_r=a-\frac{r^3-r}{2},\qquad
y_r=a-\frac{r^3+r}{2}.
\tag{B7}
\]
Both offsets are integers and hence multiples of \(1/q\).
For every \(|r|\le\gamma_q N^{1/3}\), with \(\gamma_q>0\) sufficiently
small and \(N\) sufficiently large, both coordinates remain inside the
progression. These pairs give a path with \(\gg_q N^{1/3}\) vertices.
\(\square\)

**Coverage and average.** A nontrivial path with \(v\ge2\) vertices has
\(v-1\) edges and \(v\le2(v-1)\). Therefore at most \(2E_1(A)\)
pair vertices belong to nontrivial paths. For (B4) this is
\(O(N^{3/2})=o(N^2)\). In particular, no long-path coverage of almost
all \(A^2\) can come from these families.

If \(L_A(x,y)\) counts forward edges, as in the active request, a path
of \(v\) vertices contributes \(v(v-1)/2\) to the sum of \(L_A\).
Combining (B5) and (B6) gives
\[
\frac1{N^2}\sum_{(x,y)\in A^2}L_A(x,y)=O(N^{-1/6}).
\tag{B8}
\]
This upper bound is sufficient here; no sharp average is claimed.

## 5. CR-B5 — two exact quadratic examples

**Plain-language meaning.** Placing the quadratic shift itself into the
set does not make the four-point relation automatic. Squares have gaps
large enough to drop a transformed endpoint out of the carrier. The
shift sequence has an even simpler obstruction: all its values are
congruent to one modulo three.

**PROVED.** For \(N\ge2\),
\[
E_1(\{0^2,1^2,\ldots,(N-1)^2\})=2.
\tag{B9}
\]
The only edges are
\[
(1,1)\longrightarrow(1,0),\qquad
(0,1)\longrightarrow(0,0).
\]
Thus maximum path size is two. For every \(N\ge1\),
\[
E_1(\{1^2,\ldots,N^2\})=0,\qquad
E_1(\{c(0),\ldots,c(N-1)\})=0.
\tag{B10}
\]
These conclusions also hold after any common real translation.

**Proof for squares.** Write \(y=b^2\). If \(x=a^2>y\), then
\(u\ge2b+1\), and \(c(u)>b^2\); the scalar \(y-c(u)\) is negative.
If \(x<y\) and \(b\ge2\), write \(u=-d\), where \(d\ge2b-1\).
Since \(c(-d)\) is increasing for integers \(d\ge1\),
\[
c(u)\ge c(-(2b-1))=6b^2-9b+4>b^2.
\]
Here the last difference is \((5b-4)(b-1)>0\).
If \(x<y\) and \(b=1\), the only case is \((x,y)=(0,1)\),
which gives the second displayed edge. If \(u=0\), a return requires
both \(b^2\) and \(b^2-1\) to be nonnegative squares, which happens only
at \(b=1\). This gives the first edge. Removing zero removes both edges.

**Proof for the shift sequence.** For every integer \(j\),
\[
c(j)=1+3\frac{j(j+1)}2\equiv1\pmod3.
\]
Thus \(A-A\subset3\mathbb Z\), whereas a return would require both
\(u\) and \(u+1\) to belong to \(A-A\). This is impossible. \(\square\)

**Scope.** These are exact statements for the displayed sets, not for
all quadratic sequences or symmetric unions of positive and negative
squares. Such broader fixed polynomial families have the next bounds.

## 6. CR-B6 — fixed polynomial sequences are sparse return carriers

**Plain-language meaning.** A polynomial sequence has increasingly large
gaps. The return condition forces the two original inputs to be fairly
close, and only a small number of pairs in these sequences can be that
close. This argument does not depend on arithmetical divisibility.

**PROVED.** Fix finitely many real polynomials \(p_1,\ldots,p_k\), all
of the same degree \(d\ge2\), with nonzero leading coefficients. Fix all
their coefficients before \(n\) grows. Let
\[
A_n=\bigcup_{j=1}^k\{p_j(r):0\le r<n,\ r\in\mathbb Z\},
\qquad N=|A_n|.
\tag{B11}
\]
Then \(N\asymp_{p_1,\ldots,p_k}n\), and
\[
E_1(A_n)=
\begin{cases}
O_{p_1,\ldots,p_k}(N\log(2N)),&d=2,\\
O_{p_1,\ldots,p_k}(N),&d\ge3.
\end{cases}
\tag{B12}
\]

**Proof.** Each polynomial takes any scalar value at at most \(d\)
real arguments. Thus \(n/d\le N\le kn\), even if the displayed
parametrizations overlap. Their fixed coefficients give
\(\operatorname{diam}(A_n)=O(n^d)\).
Every return has \(c(u)\le\operatorname{diam}(A_n)\), hence
\[
|x-y|=|u|\le C n^{d/2}.
\tag{B13}
\]
It suffices to count all parameter pairs satisfying this necessary
condition; counting a scalar pair more than once only enlarges the
upper bound.

Fix two of the polynomials \(p,q\), put \(W=Cn^{d/2}\), and count
\(|p(i)-q(j)|\le W\), \(0\le i,j<n\). There is a fixed threshold
past which each polynomial is monotone, has magnitude comparable to
the \(d\)-th power of its argument, and has derivative magnitude
bounded below by a positive constant times the \((d-1)\)-st power.
The finitely many earlier indices contribute \(O(n)\) pairs, which
is harmless.

If their leading coefficients have opposite signs, all sufficiently
large qualifying indices satisfy \(i,j=O(\sqrt n)\): the two
magnitudes add, and their sum is at most \(W\).
This gives \(O(n)\) pairs. If their leading coefficients have the same
sign, multiply both polynomials by \(-1\) if necessary.
For \(j\le C_0\sqrt n\), condition (B13) forces
\(i=O(\sqrt n)\), again giving \(O(n)\) pairs.
Choose the fixed \(C_0\) sufficiently large. For
\(j>C_0\sqrt n\), condition (B13) forces \(i\) between two fixed
positive multiples of \(j\), because \(q(j)\) dominates \(W\).
The allowed values of \(p(i)\) lie in an interval of length \(2W\),
and successive values there have gaps at least \(c j^{d-1}\).
There are consequently at most
\[
1+\frac{C'W}{j^{d-1}}
\]
possible integers \(i\). Summing over \(j>C_0\sqrt n\) gives
\(O(n\log(2n))\) for \(d=2\), and \(O(n)\) for \(d\ge3\).
For the latter case use
\(\sum_{j>\sqrt n}j^{-(d-1)}=O(n^{-(d-2)/2})\).
Summing over the fixed \(k^2\) polynomial pairs proves (B12).
\(\square\)

**Differences and anchors.** The contributing differences satisfy
\(|u|=O(n^{d/2})\). We do not assert that all these differences return
or count their anchors as if they were freely selectable: the proof
counts the actual available source pairs satisfying this necessary
restriction. For a fixed anchor from an index \(j>C_0\sqrt n\), it
allows at most \(O(1+n^{d/2}/j^{d-1})\) partners from each comparable
polynomial sequence. This is already enough to rule out quadratic
return counts in the stated class.

**Shift-adapted examples.** The quadratic carrier \(c(j)\), ordinary
quadratic sequences, and fixed symmetric unions such as
\(\{\pm j^2:0\le j<n\}\) fall within the degree-two statement.
The discrete antiderivative
\[
g(r)=\frac{r^3+r}{2},\qquad g(r+1)-g(r)=c(r),
\tag{B14}
\]
is a natural cubic carrier, but \(\{g(r):0\le r<n\}\) still has only
\(O(N)\) returns by (B12). The same estimate covers a fixed finite
collection of the cubic coordinate polynomials of fixed output fibers.
It is compatible with one long path of length order \(N\): one such
path still uses only order \(N\) of the \(N^2\) pair vertices.

**Orbit consequences.** At most \(2E_1(A_n)\) pair vertices lie in
nontrivial paths. Thus these occupy at most \(O(N\log(2N))\) vertices
in degree two and \(O(N)\) in higher degrees. CR-B4 and the diameter
bound give maximum path size \(O(N^{d/3}+1)\). Also every fixed-output
fiber has at most \(N\) points, since its second coordinate
\[
y(u)=\frac{z-u^3-u}{2}
\]
is strictly decreasing in \(u\), and takes values in the \(N\)-point
set \(A_n\). Together these give maximum path size
\(O(\min\{N,N^{d/3}\})\). No matching lower bound for an arbitrary
fixed polynomial family is asserted.

**Scope.** Degrees must match, and the number of sequences and their
coefficients are fixed before \(n\) grows. No uniform bound is claimed
for coefficients varying with \(n\), a growing number of output
fibers, mixed-degree unions, or arbitrary two-parameter scalar
carriers. These bounds do not preclude cubic collisions between
different \(T_1\)-paths.

## 7. Source scope and construction accounting

These proofs use the displayed TC-Q1 identity and elementary real
algebra only. They do not use the unavailable original regular-digital
or rich-fiber checkpoint proofs. The 2026-09-20 T01 recovery addendum
and manifest report recovered originals elsewhere, but the local intake
contains those two Markdown records rather than the original proof
bytes. Their availability status is not upgraded here. None of the
present claims depends on the older reported digital no-go statements.

All results concern the fixed plus-sign T01 cubic and the single
unit-step map. No T04 sign convention or separate quadratic target is
imported. The shift sequence in CR-B5 has a direct mod-\(3\)
obstruction, but no finite-field collapse or local-density theorem is
used to infer any of the other real return bounds.

For the construction ledger: the scalar sets and their actual sizes
are explicit above. Progressions have exactly the displayed number of
distinct points; unions use \(N=|A|\), not the sum of block lengths.
For polynomial carriers, parameter fibers are charged by the bound
\(d\), giving \(n/d\le N\le kn\). There is no input thinning,
additional real projection, field extension, splitting
condition, discriminant, regulator, carry process, or exceptional-output
deletion. Fixed steps, fixed polynomial coefficients, and fixed block
counts are explicit hypotheses; growing versions of those parameters
are not assigned zero cost. Reciprocal-step denominators are fixed in
CR-B2; CR-B3 assumes direct real scalar sets and needs no rational
representation. The only modular calculation is the fixed mod-\(3\)
obstruction in CR-B5, not a construction or a multiplicative saving.
Arbitrary centers in CR-B3 and CR-B4 are
handled uniformly by direct real estimates, so no height bound on the
centers is required for these conclusions. Every return is included
in an exact count or an upper bound. No whole-image upper bound is
claimed, and no return estimate is substituted for one.

## 8. Claim record

Every entry is T01, \(P=(x-y)^3+x+y\), v1 dated 2026-09-21,
with complete internal proof in the indicated section. The proofs were
derived and checked algebraically in this task without numerical
execution; this is not an external review or a novelty claim.

| ID | Status and exact scope | Source and dependencies | Remaining limit |
|---|---|---|---|
| CR-B1 | PROVED exact and asymptotic interval count for all \(N\ge1\) | §1, TC-Q1 and (B0) | Does not bound general \(R_1\) from above |
| CR-B2 | PROVED fixed-step AP zero/Theta alternatives and exact sum | §2, (B0), fixed \(h\) | Constants not uniform as step shrinks |
| CR-B3 | PROVED \(O(N^{3/2})\) for fixed bounded AP unions with steps in a fixed positive compact interval | §3, quadratic inverse-image estimate | Growing number of blocks or shrinking steps excluded |
| CR-B4 | PROVED progression path bounds, reciprocal-step lower construction, and negligible covered mass | §4, TC-Q1, CR-B3 | No complete image conclusion |
| CR-B5 | PROVED exact square and shift-sequence return counts | §5, (B0) | Only the explicitly displayed sets |
| CR-B6 | PROVED polynomial-family bounds for fixed same-degree polynomials | §6, diameter bound and elementary gap count | Varying coefficients or growing families excluded |

The global Cartesian-return question and the original cubic
power-saving target are not resolved by these baseline results.
