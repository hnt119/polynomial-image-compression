# Residual double-critical cubic fiber: constructive checkpoint

## Executive conclusion

Fix distinct primes \(q,r\ge 5\), and put

\[
R_t=\mathbb Z/M_t\mathbb Z,
\qquad M_t=q^{4t}r^{3t},
\qquad C_t=-3q^{2t}r^{2t}.
\]

For

\[
P_{C_t}(x,y)=(x-y)^3+C_t(x+y),
\qquad
\mathcal R_t(A,B)
=\frac{M_t^2|P_{C_t}(A,B)|}
{|A||B|\max(|A|,|B|)},
\]

the residual critical point does create an exponentially large unary fiber, but
it does **not** create a Cartesian compression in any of the critical-cell,
aligned-ball, finite multibranch, graph, or silent-CRT constructions that were
tested rigorously.

The sharpest explicit critical construction found has a singleton image, yet

\[
\mathcal R_t=q^{2\lceil t/2\rceil}\ge q^t;
\]

it is exponentially worse than the cubic threshold.  More strongly, if both
inputs lie in one residual critical cell, then

\[
\boxed{\mathcal R_t(A,B)\ge 1.}
\]

For completely arbitrary \(A,B\subseteq R_t\), the weighted product-tree
argument gives the rigorous depth-dependent lower bound

\[
\boxed{
\mathcal R_t(A,B)
\ge \frac{1}{60\mathcal C_{q,r}}q^{-t/2},
}
\tag{0.1}
\]

where

\[
\mathcal C_{q,r}
=6\left(A_qA_r^2+A_q^2A_r\right),
\qquad A_p=(1-p^{-1})^{-1}.
\]

No construction with \(\mathcal R_t\to0\) was found.  However, (0.1) is not
a uniform BP2+ estimate: an arbitrary recursively correlated family spread
over exponentially many critical cells remains unresolved.  Thus this
checkpoint closes the **residual-fiber construction**, not the full arbitrary
two-prime polarized problem.

No internet search or external verification was used.

---

## A. Sub-agent assignments and independent conclusions

The common target given to all agents was to maximize the actual decay exponent

\[
-\frac1t\log \mathcal R_t,
\]

not collision energy or unary multiplicity.

1. **Critical \(q\)-adic geometry.** This branch computed the exact image and
   fibers of \(u^3-3q^{2t}u\pmod{q^{4t}}\). The largest critical fiber is
   explicit and has \(q^{\lfloor t/2\rfloor}\) residual pieces, but those
   pieces merely partition one flat ball.
2. **Cartesian realization.** This branch realized critical differences by
   sets \(A\times B\), while charging \(x+y\). The best singleton-image
   realization has \(\mathcal R_t=q^{2\lceil t/2\rceil}\); every pair of
   inputs in one critical cell has \(\mathcal R_t\ge1\).
3. **Correlated CRT encoding.** This branch used the \(r\)-coordinate to tag
   \(q\)-critical branches. A silent \(r\)-tag is exactly removable by
   saturation; non-silent transverse tags create full output cells. No graph
   or hierarchical code produced decay.
4. **Adversarial audit.** This branch searched for missing output digits and a
   family-wide floor. It found (0.1), and verified that the apparent
   \(q^{t/2}\) gain is exactly the worst loss in the existing anchored-root
   estimate.
5. **Structured offline computation.** This branch tested balls, cell unions,
   digit masks, and CRT graphs at small parameters. It found no decreasing
   pattern. These experiments were used only to reject conjectures; no theorem
   below relies on them.

The assignments were non-overlapping: unary geometry, Cartesian realization,
CRT correlation, adversarial proof, and structured experimentation were kept
separate.

---

## B. Best constructive candidate

Write

\[
L=q^tr^t,
\qquad C_t=-3L^2,
\qquad M_t=q^tL^3,
\qquad s=\left\lceil\frac t2\right\rceil.
\]

Let ideals and cosets be taken in \(R_t\), and define

\[
\boxed{
A_t=L+q^{t+s}r^tR_t,
\qquad
B_t=q^{2t}r^tR_t.
}
\tag{B.1}
\]

Their exact sizes are

\[
\boxed{
|A_t|=q^{3t-s}r^{2t},
\qquad
|B_t|=q^{2t}r^{2t}.
}
\tag{B.2}
\]

This is the strongest direct use of the flat double root: it makes the entire
Cartesian image a singleton.  It nevertheless fails badly after the two input
densities and the third mass factor are charged.

For comparison, the whole residual critical cell

\[
H=LR_t
\]

has

\[
|H|=q^{3t}r^{2t},
\qquad |P_{C_t}(H,H)|=q^t,
\qquad \mathcal R_t(H,H)=1.
\tag{B.3}
\]

Thus the best proved asymptotic exponent among the surviving explicit
Cartesian candidates is zero, not positive.

---

## C. Exact critical-fiber calculation

First normalize away the \(q\)-adic unit contributed by \(r^t\), and consider

\[
f_t(u)=u^3-3q^{2t}u
\pmod{q^{4t}}.
\]

For \(\varepsilon\in\{\pm1\}\), \(j\ge1\), and

\[
B_{\varepsilon,j}
=\varepsilon q^t+q^{t+j}\mathbb Z/q^{4t}\mathbb Z,
\]

one has the exact expansion

\[
f_t(\varepsilon q^t+q^{t+j}v)
=-2\varepsilon q^{3t}
+q^{3t+2j}v^2(3\varepsilon+q^jv).
\tag{C.1}
\]

Hence, before the modulus depth is reached,

\[
v_q\bigl(f_t(\varepsilon q^t+q^{t+j}v)
-f_t(\varepsilon q^t)\bigr)
=3t+2j+2v_q(v).
\tag{C.2}
\]

This is the promised quadratic flatness: there is no term linear in the
perturbation.

### The standard lifting fact used

For an odd prime \(p\), every element of \(1+p\mathbb Z_p\) has a unique square
root in \(1+p\mathbb Z_p\).  Consequently, if a polynomial or convergent
\(p\)-adic analytic map is congruent to the identity modulo \(p\) and has unit
derivative, then it induces a bijection modulo every \(p^n\).  This is the
ordinary unique-lifting form of Hensel's lemma.

Apply it to

\[
v\longmapsto
v\sqrt{1+\frac{q^jv}{3\varepsilon}}.
\]

If \(n=t-2j>0\), (C.1) therefore gives the exact image

\[
\boxed{
f_t(B_{\varepsilon,j})
=-2\varepsilon q^{3t}
+3\varepsilon q^{3t+2j}
\operatorname{Sq}(\mathbb Z/q^n\mathbb Z).
}
\tag{C.3}
\]

If \(n\le0\), the image is the singleton
\(\{-2\varepsilon q^{3t}\}\).

The number of square residues modulo \(q^n\) is

\[
S_q(n)
=1+\frac{q-1}{2}
\sum_{a=0}^{\lfloor(n-1)/2\rfloor}q^{n-2a-1},
\tag{C.4}
\]

or, equivalently,

\[
S_q(n)=
\begin{cases}
1+\dfrac{q(q^n-1)}{2(q+1)},& n\text{ even},\\[6pt]
1+\dfrac{q^{n+1}-1}{2(q+1)},& n\text{ odd}.
\end{cases}
\tag{C.5}
\]

Thus

\[
|B_{\varepsilon,j}|=q^{3t-j},
\qquad
|f_t(B_{\varepsilon,j})|
=\begin{cases}
S_q(t-2j),&2j<t,\\
1,&2j\ge t.
\end{cases}
\tag{C.6}
\]

The largest constant ball is

\[
K_{\varepsilon,t}
=\varepsilon q^t+q^{t+\lceil t/2\rceil}
\mathbb Z/q^{4t}\mathbb Z,
\qquad
|K_{\varepsilon,t}|=q^{\lfloor5t/2\rfloor}.
\tag{C.7}
\]

The complete critical fiber follows from

\[
f_t(u)+2q^{3t}=(u-q^t)^2(u+2q^t):
\]

\[
\boxed{
f_t^{-1}(-2q^{3t})
=\left(q^t+q^{\lceil3t/2\rceil}R_q\right)
\cup
\left(-2q^t+q^{2t}R_q\right),
}
\tag{C.8}
\]

where \(R_q=\mathbb Z/q^{4t}\mathbb Z\).  It has size

\[
q^{\lfloor5t/2\rfloor}+q^{2t}.
\tag{C.9}
\]

The first ball in (C.8) splits into \(q^{\lfloor t/2\rfloor}\) balls of
depth \(2t\), all with the same output.  They are not independent branches:
they are exactly a partition of the one ball (C.7).  The two critical signs
have disjoint images because their centers differ by \(4q^{3t}\), whereas
every local variation is divisible by \(q^{3t+2}\).

The unary ledgers expose the trap.  For the largest critical fiber \(U_t\),

\[
\frac{q^{4t}|f_t(U_t)|}{|U_t|^2}\asymp_q q^{-t},
\qquad
\frac{q^{8t}|f_t(U_t)|}{|U_t|^3}\asymp_q q^{t/2}.
\tag{C.10}
\]

The first quantity looks constructively attractive; the second is the actual
cubic/BP ledger and loses.

---

## D. Exact image-size estimate for the Cartesian candidate

Take \(x=L+a\in A_t\) and \(y=b\in B_t\), and put \(h=a-b\).  Since

\[
P_{C_t}(x,y)=f(h+L)+2C_tb,
\qquad
f(u)=u^3-3L^2u,
\]

the critical expansion is

\[
f(L+h)-f(L)=3Lh^2+h^3.
\tag{D.1}
\]

Here

\[
v_q(h)\ge t+s,
\qquad v_r(h)\ge t.
\]

Therefore

\[
v_q(3Lh^2)\ge3t+2s\ge4t,
\qquad
v_r(3Lh^2)\ge3t,
\]

and the cubic term is at least as divisible.  Also

\[
2C_tb\equiv0\pmod{q^{4t}r^{3t}}.
\]

Since \(f(L)=-2L^3\), this proves the exact, not energetic, estimate

\[
\boxed{
P_{C_t}(A_t,B_t)=\{-2L^3\},
\qquad |P_{C_t}(A_t,B_t)|=1.
}
\tag{D.2}
\]

### Why all restrictions inside one critical cell fail

Let

\[
H=LR_t,
\]

fix a coset \(c+H\), and take arbitrary \(A,B\subseteq c+H\).  Write

\[
x=c+L\xi,
\qquad y=c+L\eta.
\]

Then

\[
P_{C_t}(x,y)
=-6L^2c+L^3\bigl((\xi-\eta)^3-3(\xi+\eta)\bigr).
\tag{D.3}
\]

The bracket matters only modulo \(q^t\).  Define

\[
\pi(c+L\xi)=\xi\pmod{q^t},
\qquad X=\pi(A),\quad Y=\pi(B).
\]

Each \(\pi\)-fiber has \(L^2=q^{2t}r^{2t}\) elements, and multiplication by
\(L^3\) injects \(\mathbb Z/q^t\mathbb Z\) into \(R_t\).  Hence

\[
\boxed{
|P_{C_t}(A,B)|=|P_{-3}(X,Y)|,
\qquad
|A|\le L^2|X|,\qquad |B|\le L^2|Y|.
}
\tag{D.4}
\]

For the unit-coefficient map \(P_{-3}\) modulo \(q^t\), the change
\((x,y)\leftrightarrow(u=x-y,v=x+y)\) is invertible.  Once an output and \(u\)
are fixed, \(v\) is unique because \(-3\) is a unit.  Thus every full-ring
fiber has exactly \(q^t\) points, and

\[
|P_{-3}(X,Y)|\ge\frac{|X||Y|}{q^t}.
\tag{D.5}
\]

Combining (D.4) and (D.5) yields

\[
\boxed{
\mathcal R_t(A,B)
\ge\frac{q^t}{\max(|X|,|Y|)}\ge1.
}
\tag{D.6}
\]

This is a complete no-go theorem for arbitrary sparse digits, progressions,
Cantor restrictions, and unions of fine balls contained in one residual
critical cell.

### A universal bound for arbitrary cells

The following proposition records exactly what remains of the old weighted
argument after the residual double root appears.

**Proposition.** For all nonempty \(A,B\subseteq R_t\),

\[
|P_{C_t}(A,B)|
\ge
\frac{q^{-t/2}}{60\mathcal C_{q,r}}
\frac{|A||B|\max(|A|,|B|)}{M_t^2}.
\tag{D.7}
\]

**Proof.** Invoke the arbitrary-exponent form of the exact product-tree
difference estimate from the supplied sum-product construction. It holds for
\(M=q^\ell r^m\), and hence for \((\ell,m)=(4t,3t)\):

\[
\sum_{x\in A,y\in B}
\left(\frac{\operatorname{ord}(x-y)}{M_t}\right)^2
\ge
\frac{|A|^2|B|^2}{4\mathcal C_{q,r}M_t^2}.
\tag{D.8}
\]

Here \(\operatorname{ord}(u)\) is the additive order of \(u\), with
\(\operatorname{ord}(0)=1\), and we set \(v_p(0)=+\infty\). Define

\[
\Omega_t(u)
=q^{-2\min(v_q(u),t)}r^{-2\min(v_r(u),t)}.
\]

Because this truncation is shallower than the exponents in \(M_t\),
\(\Omega_t(u)\ge(\operatorname{ord}(u)/M_t)^2\). Therefore

\[
\sum_{A\times B}\Omega_t(x-y)
\ge
\sum_{A\times B}
\left(\frac{\operatorname{ord}(x-y)}{M_t}\right)^2
\ge
\frac{|A|^2|B|^2}{4\mathcal C_{q,r}M_t^2}.
\tag{D.8a}
\]

For the \(r\)-adic anchored cubic modulo \(r^{3t}\), the frozen exact
\(2{:}3\) root calculation gives weighted root mass at most \(3\), for either
sign of the linear term. At the \(q\)-place, split roots of

\[
u^3\mathbin{\pm}3q^{2t}c^2u=w
\pmod{q^{4t}},
\qquad q\nmid c,
\]

according to \(h=v_q(u)\):

1. If \(h<t\), the cubic term dominates.  There are at most \(3q^{2h}\)
   lifted roots, and their total weight is at most \(3\).
2. If \(h>t\), the linear term is transverse after scaling.  The discarded
   \(q^{2t}\) lifts cancel the weight \(q^{-2t}\), contributing at most \(1\).
3. If \(h=t\), divide by \(q^{3t}\). One obtains
   \(v^3\mathbin{\pm}3c^2v=a\pmod{q^t}\). If critical residue classes exist,
   their critical values are distinct, so at most one critical class can occur
   for a fixed \(a\). In that class, the same analytic change used in (C.3)
   reduces the equation to a square congruence, which has at most
   \(2q^{\lfloor t/2\rfloor}\) roots. If a critical class occurs, there is at
   most one other simple class; if no critical class occurs, there can be at
   most three simple classes. Every solution \(v\pmod{q^t}\) has \(q^{2t}\)
   lifts in the original scaled variable, and the factor \(q^{-2t}\) in
   \(\Omega_t\) cancels those lifts.

Consequently the \(q\)-adic weighted root mass is at most

\[
2q^{\lfloor t/2\rfloor}+5
\le5q^{t/2}.
\]

CRT makes the two local sums multiply, so every anchored global root fiber has
weighted mass at most \(15q^{t/2}\). Fixing \(y\) gives

\[
u^3+C_tu=z-2C_ty,
\]

while fixing \(x\) gives

\[
u^3-C_tu=z-2C_tx.
\]

The preceding estimate covers both signs. Anchoring in these two ways shows
that every output \(z\) satisfies

\[
\sum_{\substack{(x,y)\in A\times B\\P_{C_t}(x,y)=z}}
\Omega_t(x-y)
\le15q^{t/2}\min(|A|,|B|).
\tag{D.9}
\]

Group the total weighted pair mass by outputs, combine (D.8) and (D.9), and
use

\[
\frac{|A|^2|B|^2}{\min(|A|,|B|)}
=|A||B|\max(|A|,|B|).
\]

This proves (D.7). \(\square\)

The factor \(q^{t/2}\) in (D.9) is precisely the residual critical
multiplicity.  The proposition proves that no construction in this family can
decay faster than \(q^{-t/2}\), but it does not rule out decay at that scale.

---

## E. Normalized compression ledger

For the singleton candidate (B.1), \(|A_t|\ge|B_t|\), so (B.2) and (D.2)
give

\[
\boxed{
\mathcal R_t(A_t,B_t)
=\frac{q^{8t}r^{6t}}
{(q^{3t-s}r^{2t})^2(q^{2t}r^{2t})}
=q^{2s}=q^{2\lceil t/2\rceil}.
}
\tag{E.1}
\]

Thus

\[
-\frac1t\log\mathcal R_t(A_t,B_t)
=-\frac{2\lceil t/2\rceil}{t}\log q
\longrightarrow-\log q.
\]

It loses exponentially.  The main candidates rank as follows.

1. The unary full critical fiber has \(Q_2\asymp q^{-t}\), but its cubic
   ledger is \(Q_3\asymp q^{t/2}\); it is not Cartesian.
2. The singleton Cartesian pair (B.1) has
   \(\mathcal R_t=q^{2\lceil t/2\rceil}\) and decay exponent
   \(-\log q+o(1)\).
3. The whole critical cell \((H,H)\) has \(\mathcal R_t=1\), hence exponent
   zero.
4. Every pair inside one common \(H\)-cell has \(\mathcal R_t\ge1\).
5. An arbitrary pair in the full ring obeys
   \(\mathcal R_t\ge(60\mathcal C_{q,r})^{-1}q^{-t/2}\), which caps any
   possible decay exponent at \(\tfrac12\log q+o(1)\).

No explicit candidate has a positive decay exponent.

---

## F. Same-set conversion

The asymmetric singleton construction does not survive union into one set.
Let

\[
S_t=A_t\cup B_t.
\]

Since \(|S_t|\le2|A_t|\) and

\[
P_{C_t}(x,x)=2C_tx,
\]

the diagonal block gives

\[
|P_{C_t}(S_t,S_t)|
\ge|2C_tA_t|=q^{t-s}.
\]

Consequently

\[
\boxed{
\frac{M_t^2|P_{C_t}(S_t,S_t)|}{|S_t|^3}
\ge\frac18q^{2s}\ge\frac18q^t.
}
\tag{F.1}
\]

There is also a general same-set obstruction.  Multiplication by \(2C_t\)
has kernel size

\[
g=\gcd(C_t,M_t)=L^2.
\]

Therefore every \(S\subseteq R_t\) satisfies

\[
|P_{C_t}(S,S)|\ge\frac{|S|}{L^2},
\]

and hence

\[
\boxed{
\mathcal R_t(S,S)
\ge
\left(\frac{|H|}{|S|}\right)^2.
}
\tag{F.2}
\]

If \(S\) occupies at most \(J\) cosets of \(H\), then
\(\mathcal R_t(S,S)\ge J^{-2}\).  Any exponentially compressive same set
would therefore have to occupy exponentially many critical cells and control
all off-diagonal cross-pairs.

Even perfect control of four blocks at a very sparse scale does not help.  Put

\[
T=q^{2t}r^tR_t,
\qquad S=T\cup(L+T).
\]

The four blocks have exactly the outputs

\[
0,\qquad -2L^3,\qquad -4L^3,\qquad -6L^3,
\]

so \(|S|=2L^2\) and \(|P_{C_t}(S,S)|=4\), but

\[
\mathcal R_t(S,S)=\frac12q^{2t}.
\tag{F.3}
\]

---

## G. Global amplification test

No exponential local compression was proved.  The best explicit local gain
parameter is therefore

\[
\eta=0.
\]

Accordingly, an amplification condition

\[
\eta\theta>\kappa_{\mathrm{global}}
\]

cannot hold for any positive archimedean/root-discriminant cost
\(\kappa_{\mathrm{global}}\).  There is no justified number-field ledger and
no candidate real exponent \(c>0\) to derive from this family.

The lower bound (D.7) says only that a hypothetical construction could gain at
most \(\tfrac12\log q\) per unit of \(t\).  A lower bound is not a construction
and cannot be entered on the gain side of the global ledger.

---

## H. Verdict toward the ultimate theorem

**Selected verdict: 3. No constructive gain.**

The rigorous scope of that verdict is important:

\[
\boxed{
\text{The residual double-critical fiber mechanism is closed, but full BP2+
for arbitrary cross-cell }A,B\text{ is not yet proved.}
}
\]

Thus "BP2+ survives" here means that it remains unrefuted and is proved on the
entire critical cell plus all tested structured families.  It is **not** a
claim of a uniform family-wide theorem.  Closing the entire cubic local stream
would currently overstate the mathematics.

The exact missing configuration is a recursively nontransverse, sparse
prefix-code spread over a growing number of \(H\)-cells.  Mass-only
tensorization does not control it, and none of the present constructions makes
it compress.

---

## I. Exactly one next mathematical target

Prove or disprove the following full-cell translated charging statement.

Let \(H=q^tr^tR_t\), let \(K=|H|=q^{3t}r^{2t}\), and let
\(X,Y\subseteq R_t/H\).  Is there a constant \(b_{q,r}>0\), independent of
\(t,X,Y\), such that

\[
\boxed{
|P_{C_t}(X+H,Y+H)|
\ge
b_{q,r}K
\frac{|X||Y|\max(|X|,|Y|)}{(q^tr^t)^2}?
}
\tag{I.1}
\]

This removes all within-cell sparsity while retaining the unresolved
translation and cross-cell overlap.  It is the smallest clean statement that
tests whether exponentially many residual-cell addresses can cooperate.

---

## Frozen-input and theorem-use ledger

The exact \(2{:}3\) no-compression theorem and its anchored weighted root
estimate were treated as frozen and were not re-proved.  The only substantial
general tools invoked above were:

1. the Chinese remainder theorem;
2. the unique-lifting form of Hensel's lemma stated in Section C;
3. the exact product-tree difference inequality (D.8) from the supplied
   sum-product construction.

All remaining arguments are explicit congruence, valuation, fiber, and
cardinality calculations contained in this note.
