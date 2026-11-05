# Direct iteration and separated copies of the six-point gadget

Date/version: 2026-09-16, v1. Track T01; throughout
\(P(x,y)=(x-y)^3+x+y\). This is a new, authorized, offline analytic
continuation of the [finite-gadget report](../2026-09-16-three-branch-lift/README.md).
No experiment, network access, external theorem, or arithmetic tower is used.
The complete proofs below are internal; no novelty claim is made.

## 1. What happens if shared input points are allowed?

The three copies keep adding new points, but they increasingly share old
ones. The resulting set grows by a factor approaching two, not three.
More decisively, its cubic image eventually contains almost as many values
as there are ordered input pairs. Thus allowing branch overlap repairs
unbounded input growth but does not produce a power saving.

### TC-D1 — exact input set and input growth

**PROVED internally.** Start at the six-point gadget
\[
A_0=G=\{0,1,2,3,4,5\}/3,
\qquad
A_{m+1}=\bigcup_{r=0}^2(A_m/2+r/3).
\]
For every integer \(m\ge0\), put \(q=2^m\). Then
\[
\boxed{A_m=\{0,1,\ldots,4q+1\}/(3q),\quad
n_m=|A_m|=4q+2,\quad n_{m+1}=2n_m-2.}\tag{1}
\]
In particular \(n_{m+1}/n_m\to2\). Starting instead from the original
two-point seed \(\{0,2\}\) only shifts the stage index by one.

**Proof.** The formula is correct at \(m=0\). Express the three images
at the next stage using their common denominator \(6q\). Their integer
numerator sets are the intervals
\[
[0,4q+1],\quad[2q,6q+1],\quad[4q,8q+1].
\]
Their union is every integer from 0 to \(8q+1\), proving induction.
The two adjacent intersections each contain \(2q+2\) points; the first
and third intersection and the triple intersection each contain two points.
Inclusion–exclusion therefore gives
\[
3(4q+2)-(2q+2)-(2q+2)-2+2=8q+2.
\]
The branch maps are individually injective, but their total overcount is
\(3n_m-n_{m+1}=n_m+2\). This loss has been charged in (1). ∎

The conclusion is limited to the displayed literal maps. It says nothing
yet about stage-dependent scales or translations.

## 2. Almost every ordered pair can be distinguished exactly

Although the points become closely spaced in a bounded real interval,
their exact cubic outputs are usually different. Clearing the denominator
reveals the reason: most differences can be recovered from the output
modulo a large power of two. Once the difference is known, the sum is also
known, and therefore the original ordered pair is known.

### TC-D2 — actual image is asymptotically quadratic

**PROVED internally.** For the sets in (1), write
\(s_m=|P(A_m,A_m)|\). For \(m\ge4\), define
\[
q=2^m,\quad T=\lfloor m/2\rfloor-1,\quad Q=2^T,\quad n=4q+2.
\]
Then
\[
\boxed{
n^2\left(1-\frac1Q\right)-2+\frac4Q
\le s_m\le n^2.
}\tag{2}
\]
Consequently
\[
\frac{s_m}{n_m^2}\longrightarrow1,
\qquad
\frac{s_{m+1}}{s_m}\longrightarrow4.
\tag{3}
\]
In particular there is no fixed \(c>0\) with
\(s_m\le n_m^{2-c}\) for arbitrarily large \(m\).

**Proof.** Write \(x=i/(3q)\), \(y=j/(3q)\), where
\(0\le i,j\le4q+1\). The exactly cleared output is
\[
(3q)^3P(x,y)=W(i,j):=(i-j)^3+9q^2(i+j).
\tag{4}
\]
We prove that all ordered pairs satisfying \(Q\nmid i-j\) have different
outputs from one another. This does not assert that their outputs avoid
every omitted pair; injectivity on the selected pairs alone is enough for
a support lower bound.

Suppose two selected pairs have equal outputs, and set
\(d=i-j\), \(d'=i'-j'\). Equation (4) implies
\[
d^3\equiv(d')^3\pmod {q^2},\qquad q^2=2^{2m}.
\tag{5}
\]
Both differences are nonzero. Let \(t\) be the largest power-of-two
exponent dividing \(d\), and similarly let \(t'\) correspond to \(d'\).
The selection gives \(0\le t,t'<T\). If \(t\ne t'\), the largest
power of two dividing \(d^3-(d')^3\) has exponent
\(3\min(t,t')<2m\), contradicting (5). Thus \(t=t'\).

Write \(d=2^ta\), \(d'=2^tb\) with \(a,b\) odd integers. The integer
\(a^2+ab+b^2\) is odd, so
\[
d^3-(d')^3=(d-d')(d^2+dd'+(d')^2)
\]
shows from (5) that
\[
2^{2m-2t}\mid d-d'.
\tag{6}
\]
But \(t\le T-1=\lfloor m/2\rfloor-2\), whence
\[
2^{2m-2t}\ge2^{m+4}=16q>8q+2\ge|d-d'|.
\]
Therefore \(d=d'\). Returning to the equality of (4) gives
\(i+j=i'+j'\), and hence \((i,j)=(i',j')\).

It remains to count the omitted pairs. Put \(a=4q/Q\), an integer.
Among the \(n=4q+2\) consecutive indices, two residue classes modulo
\(Q\) have \(a+1\) members and the other \(Q-2\) classes have \(a\)
members. The number of ordered pairs with equal residues is exactly
\[
2(a+1)^2+(Q-2)a^2
=\frac{n^2}{Q}+2-\frac4Q.
\]
The remaining pairs are injective by the argument above. This proves (2).
Since \(Q\to\infty\), the first limit in (3) follows. The second follows
by multiplying that first limit at consecutive stages by
\((n_{m+1}/n_m)^2\to4\). Finally, for large \(m\), (2) gives
\(s_m\ge n_m^2/2\), which exceeds \(n_m^{2-c}\) once
\(n_m^c>2\). ∎

The proof also gives \(s_m=n_m^2-O(n_m^{3/2})\), because
\(Q\) is bounded above and below by fixed multiples of \(\sqrt q\).
No limit formula is asserted for every individual output multiplicity.

### TC-D3 — the corrected rate test fails

**PROVED internally.** For literal iteration, the actual growth rates are
\[
\lambda=2,\qquad\rho=4,\qquad\rho=\lambda^2.
\]
Thus the apparent improvement from an output factor near nine to a factor
near four is completely paid for by the slower input growth. There is no
remaining exponent gain.

More precisely, for any fixed \(\rho_0<4\), \(\delta>0\), and finite
constant \(C\), an eventual recurrence
\[
s_{m+1}\le\rho_0s_m+C n_m^{2-\delta}
\]
is impossible. Divide by \(n_m^2\) and use (1)–(3): the left side tends
to 4, while the right side tends to \(\rho_0\). This is an actual-image
obstruction, not failure of one proposed output estimate.

## 3. Widely separating the copies repairs the inputs but loses the collisions

There is another simple repair: retain the whole previous set and place
three copies far apart. This does make the inputs triple. However, outputs
from different copies then remember both endpoints. The cross-copy part
alone has quadratic size.

### TC-D4 — exact separated-copy support count

**PROVED internally.** Let \(C\subset\mathbb R\) be any fixed nonempty
finite set, \(n=|C|\), \(s=|P(C,C)|\), and put
\[
B_H=C\cup(C+H)\cup(C+2H).
\]
For all sufficiently large positive real \(H\),
\[
\boxed{|B_H|=3n,\qquad |P(B_H,B_H)|=6n^2+3s.}\tag{7}
\]
Indeed this holds for every \(H\) outside a finite set, provided the three
input copies are disjoint.

**Proof.** For branch indices \(r,t\in\{0,1,2\}\), \(x,y\in C\), write
\(k=r-t\), \(d=x-y\). The output is a polynomial in the separation:
\[
\begin{aligned}
P(x+rH,y+tH)
={}&k^3H^3+3k^2dH^2\\
&+(3kd^2+r+t)H+d^3+x+y.
\end{aligned}\tag{8}
\]
If \(k\ne0\), the coefficients of this polynomial recover, in order,
\(k\), \(d\), \(r+t\), and \(x+y\). These recover \(r,t,x,y\).
Thus all \(6n^2\) cross-copy ordered pairs give different polynomials.
Each has degree three, so none equals a same-copy output polynomial.

The same-copy polynomials are \(2rH+z\), where \(z\in P(C,C)\).
There are exactly \(3s\) distinct such polynomials. Altogether there are
\(6n^2+3s\) distinct output polynomials. Each pair of distinct polynomials
can agree at only finitely many real \(H\). Their union is a finite
exceptional set. For all larger \(H\), every distinct polynomial gives a
distinct value. Also \(H>\max C-\min C\) makes the input copies disjoint.
This proves (7), and the stated finite-exception version. ∎

For the six-point gadget \(G\), this yields exactly
\[
|B_H|=18,\quad |P(B_H,B_H)|=6\cdot36+3\cdot22=282
\]
for all sufficiently large \(H\). Its output growth factor is
\(282/22=141/11>9\). In general (7) gives
\[
\frac{|P(B_H,B_H)|}{9s}
=\frac13+\frac23\frac{n^2}{s}\ge1.
\]
So merely separating unscaled copies never retains a strict sub-nine step
at such separations.

### TC-D5 — common scaling does not rescue sufficiently separated copies

**PROVED internally.** Fix any nonzero real \(a\) before choosing \(H\).
Replacing \(C\) by \(aC\) in (7) proves
\[
|P(aC+\{0,H,2H\},aC+\{0,H,2H\})|
=6n^2+3|P(aC,aC)|
\tag{9}
\]
for all sufficiently large positive \(H\), with \(3n\) distinct inputs.
Here \(aC+\{0,H,2H\}\) means the union of the three translated copies.

The universal lower bound \(|P(aC,aC)|\ge n\) follows by fixing one
second coordinate and using \(\partial_xP=1+3(x-y)^2>0\). Therefore any
fixed common scale applied to \(G\), followed by sufficiently separated
copies, gives at least \(216+18=234>9\cdot22\) outputs. More generally
the six cross-copy blocks already contribute
\[
6n^2=\tfrac23(3n)^2.
\]
Thus no infinite construction that uses (9) at each stage can have a fixed
power saving, even if \(a\) and the adequately large \(H\) change with
the stage.

**Limits of TC-D4/TC-D5.** The previous set and its common scale are fixed
first; then the separation avoids the finite collision values in the proof
(in particular it may exceed them all). We do not rule out deliberately
chosen exceptional separations, parameters varying together to preserve
collisions, unequal branch scales, or overlapping copies. No uniform bound
for the needed separation in terms of \(n\) alone is asserted. These are
exact support theorems for their stated class, not a claim that every
visually separated configuration has the same count.

## 4. Source compatibility and the full count ledger

Literal iteration falls into a fixed-prime rational setting. A prefix of
\(A_m\) is precisely
\[
\{0,\ldots,N-1\}/N,\qquad N=3\cdot2^m.
\]
It has fixed prime support \(\{2,3\}\) and positive entropy. Thus the
reported fixed-prime theorem in T01 current state §4.3, T01.6 would also
give a constant-fraction quadratic lower bound for the whole \(A_m\).
Its named full proof is unavailable in the supplied tree, as documented in
the preceding cycle's [source audit](../2026-09-16-three-branch-lift/source-scope.md).
TC-D2 is an independent, complete elementary proof for this particular
family, and yields the stronger asymptotic ratio 1. No missing proof is
silently imported.

TC-D4/TC-D5 use no prime-support or digital hypothesis; real parameters are
allowed. All statements concern the same input set in both coordinates.
They use no continuous-volume count, cube-residue density certificate,
\(GP\), norm-one trace, or rich-quadratic-fiber construction. Towers are
not considered because neither continuation leaves a positive scalar rate.

| Entry | Literal iteration | Sufficiently separated copies |
|---|---|---|
| Actual input count, lower and upper | Exactly \(4\cdot2^m+2\); factor tends to 2 | Exactly \(3n\) at each admitted step |
| Branch/parameter fibers | Individual branches injective; overlap loses exactly \(n+2\) of the naive \(3n\) count | Three copies disjoint; input encoding injective |
| Input thinning | None; repeated input points are identified and counted once | None |
| Entire image | (2) bounds the entire image between an injective-pair lower count and \(n^2\) | Exact (7), or exact (9) after scaling; all nine blocks counted |
| Exceptional pairs | Exactly \(n^2/Q+2-4/Q\) omitted only from the lower-bound injection argument; they remain in the complete image and cannot weaken the lower bound | No uncovered pairs; finitely many exceptional separation values excluded in the theorem's hypotheses |
| Denominators/coefficient heights | Actual denominator \(3\cdot2^m\); (4) keeps the full factor \(9q^2\); all equalities exact | Parameters may be real; polynomial coefficients are explicit in (8); no bound suppresses a coefficient or mixed term |
| Archimedean size | \(A_m\subset[0,5/3]\); no volume estimate used | Separation grows as needed; no output packing estimate hides this cost |
| Field, discriminant, regulator, classes | Inputs rational, field degree 1; no number-field counting step | No number-field construction, norm, or ideal-class count |
| Moduli/carries | Congruence modulo \(q^2\) only proves injectivity; no residue saving or omitted carry | Not used |
| Direct-iteration rates | \(\log n_m=m\log2+O(1)\), \(\log s_m=2m\log2+O(1)\); net gap zero | Whole image at least \(\tfrac23|A_{m+1}|^2\); no positive exponent |
| Real projection | Identity; exact rational equality in TC-D1/TC-D2 | Identity on the specified real sets |

## 5. Claim and verification record

All claims have track T01, branch “three-branch continuation,” polynomial
\((x-y)^3+x+y\), and version/date at the top of this file. Each proof is
self-contained at its stated section. They are **PROVED internally**;
the literal and sufficiently separated continuation mechanisms are
**FAILED** as power-saving constructions in their precise scopes.

| Claim | Quantifiers and dependency | Evidence / locator | Retained gap |
|---|---|---|---|
| TC-D1 | Every integer \(m\ge0\), the displayed fixed maps and seed | Exact interval induction, §1 | Other branch rules |
| TC-D2 | Every \(m\ge4\), the exact TC-D1 sets | Congruence injection and complete omitted-pair count, §2 | Other denominators/carriers |
| TC-D3 | TC-D1 sets; every fixed proposed \(\rho_0<4,\delta>0,C<\infty\) | Actual asymptotic image and recurrence contradiction, §2 | Adaptive rules |
| TC-D4 | Every fixed nonempty finite real \(C\), all sufficiently large \(H\) | Exact polynomial separation, §3 | Exceptional separations |
| TC-D5 | Every such \(C\), every nonzero real common scale fixed before separation | TC-D4 plus monotonicity, §3 | Coupled exceptional parameters or unequal scales |

This subtask inspected the initial Git status/diff summary, the new request,
and the prior report. Mandatory project/source orientation had already been
read in the preceding phase of this same task. It changed only this new
note. No original source, historical report, canonical JSON, or SPEC was
edited. No finite search, code execution for mathematical evidence, or
network access occurred. Repository verification and independent proof
review are coordinated by the lead report task; this note makes no claim
that a file-integrity check proves a mathematical theorem.
