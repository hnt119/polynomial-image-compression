# Self-similar cubic checkpoint

## The self-similar polarized theorem for
\(P_C(x,y)=(x-y)^3+C(x+y)\)

### Status

The self-similar assertion **SS-BP is true**.  In fact it holds with the same
explicit constant supplied by the frozen homogeneous two-prime argument.

Throughout, \(q\ne r\) are fixed odd primes,

\[
 \lambda=qr,\qquad M_t=q^{3t}r^{3t}=\lambda^{3t},\qquad
 C_t=q^{2t}r^{2t}=\lambda^{2t}.
\]

For \(p\in\{q,r\}\), put

\[
 A_p=(1-p^{-1})^{-1}
\]

and define the constant from the frozen triple-convolution lemma by

\[
 \mathcal C_{q,r}
 =6\bigl(A_qA_r^2+A_q^2A_r\bigr).
\tag{1}
\]

The main result of this checkpoint is the following.

**Theorem (SS-BP).** For every \(t\ge1\) and all nonempty
\(A,B\subseteq\mathbb Z/M_t\mathbb Z\),

\[
 \boxed{
 |P_{C_t}(A,B)|
 \ge
 b_{q,r}\frac{|A||B|\max\{|A|,|B|\}}{M_t^2},
 \qquad
 b_{q,r}=\frac1{36\mathcal C_{q,r}}.
 }
\tag{2}
\]

No internet or external source was used.

---

## A. Frozen checkpoint confirmation

The six frozen intermediate-singular conclusions in the research prompt were
used as assumptions and were not re-proved.  One precise internal lemma from
the frozen homogeneous two-prime proof is also used below: the audited
triple-convolution/maximal-cross-edge inequality stated in (19).  That is the
quantitative engine which originally proved the frozen homogeneous polarized
theorem.

The new work is the weighted anchored-root estimate in Lemma 1.  It controls
all center translations at once and turns the frozen homogeneous charging
inequality into (2).

The only general standard facts used are:

1. the Chinese remainder theorem;
2. the elementary fact that a degree-three polynomial over a field has at
   most three roots;
3. elementary \(p\)-adic valuation arithmetic and the factorization
   \(X^3-Y^3=(X-Y)(X^2+XY+Y^2)\).

For the optional collision example in Section C, we also use the following
standard finite-unit-group fact: for an odd prime \(p\), the group
\((\mathbb Z/p^n\mathbb Z)^\times\) is cyclic.  Consequently cubing is an
automorphism on \(1+p\mathbb Z/p^n\mathbb Z\) when \(p\ne3\), while for
\(p=3\) its image on \(1+3\mathbb Z/3^n\mathbb Z\) is
\(1+9\mathbb Z/3^n\mathbb Z\).

---

## B. Verdict on the self-similar theorem

The verdict is positive: (SS-BP) holds uniformly in \(t,A,B\), with the
explicit constant in (2).

The scale is sharp.  For every residue \(a\), take

\[
 A=B=a+\lambda^t(\mathbb Z/M_t\mathbb Z).
\]

Then \(|A|=|B|=\lambda^{2t}\), while both the variable cubic term and the
variable part of the linear term vanish modulo \(M_t\).  Hence

\[
 P_{C_t}(A,B)=\{2C_ta\},
 \qquad
 \frac{|A||B|\max(|A|,|B|)}{M_t^2}=1.
\]

Thus the polarized cubic exponent cannot be improved even in this exact
self-similar family.

The proof does **not** rely on a false assertion that hierarchical translation
addresses make all transverse blocks disjoint.  Incomparable blocks can have
unbounded, and even exact, overlap.  Instead, the proof keeps one input as an
anchor.  Once \(y\) is fixed,

\[
 P_{C_t}(y+u,y)=u^3+C_tu+2C_ty,
\tag{3}
\]

and once \(x\) is fixed,

\[
 P_{C_t}(x,x-u)=u^3-C_tu+2C_tx.
\tag{4}
\]

The translations \(2C_ty\) and \(2C_tx\) only change the right-hand side of a
one-variable congruence.  At the exact \(2{:}3\) scaling, every weighted fiber
of the anchored cubics \(u^3\pm C_tu\) has uniformly bounded mass.  This is
the missing translated charging principle.

---

## C. Translation-address structure

### C.1 Exact recursion

Suppose \(0\le d\le t\) and \(x,y\) have a common base-\(\lambda\) prefix
\(w\pmod{\lambda^d}\):

\[
 x=w+\lambda^dX,\qquad y=w+\lambda^dY.
\]

A direct expansion gives

\[
 \boxed{
 P_{C_t}(x,y)
 =2C_tw+\lambda^{3d}P_{C_{t-d}}(X,Y).
 }
\tag{5}
\]

If the common digits are \(a_0,\ldots,a_{d-1}\), so that

\[
 w=a_0+\lambda a_1+\cdots+\lambda^{d-1}a_{d-1},
\]

then the accumulated translation is

\[
 2C_tw
 =C_t\bigl(2a_0+\lambda(2a_1)+\cdots+
 \lambda^{d-1}(2a_{d-1})\bigr).
\tag{6}
\]

Thus the proposed hierarchical address is real and exact.

### C.2 What addresses do separate

Along one ancestor-descendant chain, first-divergence side bands are disjoint.
Indeed, at a depth-\(d\) divergence the residual difference is a unit at at
least one of \(q,r\).  At that prime the residual polynomial in (5) is a unit,
whereas every pair continuing into the common child has residual value
divisible by that prime.  After multiplication by \(\lambda^{3d}\), the two
output bands remain distinct.

This explains why an ordinary single-spine leakage construction does not by
itself defeat (SS-BP).

### C.3 What addresses do not separate

At a fixed depth \(d\), the coarse containers

\[
 2C_tw+\lambda^{3d}(\mathbb Z/M_t\mathbb Z)
\]

for prefixes \(w,w'\pmod{\lambda^d}\) can intersect only if

\[
 \lambda^{3d}\mid 2C_t(w-w'),
\]

or equivalently

\[
 \boxed{
 w\equiv w'\pmod{\lambda^{\max(0,3d-2t)}}.
 }
\tag{7}
\]

Hence the address-only multiplicity allowed by (7) is

\[
 \lambda^{d-\max(0,3d-2t)}
 =
 \begin{cases}
   \lambda^d,&d\le2t/3,\\
   \lambda^{2(t-d)},&d>2t/3.
 \end{cases}
\tag{8}
\]

This is unbounded near the critical depth \(2t/3\).

The overlap is not merely an artifact of coarse containers.  Let
\(t=3H+1\), \(d=2H\), and let \(w\) run through all residues modulo
\(\lambda^d\).  By the finite-unit-group fact stated in Section A, there is a
unit \(e_w\) modulo \(\lambda^{3(t-d)}\) such that

\[
 e_w^3\equiv1-2\lambda^2w
 \pmod{\lambda^{3(t-d)}}.
\tag{9}
\]

Indeed, the right side is congruent to \(1\) modulo \(p^2\) at each
\(p\in\{q,r\}\).  For \(p\ne3\), cubing is an automorphism on
\(1+p^2\mathbb Z/p^n\mathbb Z\); for \(p=3\), its image on
\(1+3\mathbb Z/3^n\mathbb Z\) is \(1+9\mathbb Z/3^n\mathbb Z\).
The Chinese remainder theorem then supplies \(e_w\).

Set, modulo \(M_t\),

\[
 x_w=w+\frac{\lambda^de_w}{2},
 \qquad
 y_w=w-\frac{\lambda^de_w}{2}.
\]

The pair \((x_w,y_w)\) first diverges at depth \(d\), but

\[
 \begin{aligned}
 P_{C_t}(x_w,y_w)
 &=\lambda^{3d}e_w^3+2\lambda^{2t}w\\
 &\equiv\lambda^{3d}
 \pmod{M_t}.
 \end{aligned}
\tag{10}
\]

Thus \(\lambda^{2H}\) different translation addresses yield the same actual
output.  The proposed unweighted bounded-overlap address lemma is false.
The positive theorem must count all Cartesian cross-pairs rather than selected
matched blocks.

---

## D. Main new lemma: anchored weighted fibers

For a prime \(p\), write

\[
 v_p(0)=3t,
 \qquad
 \omega_{p,t}(u)=p^{-2\min(v_p(u),t)}
 \quad (u\bmod p^{3t}).
\tag{11}
\]

**Lemma 1 (self-similar anchored-root bound).** Let \(p\) be an odd prime,
let \(c\) be a unit modulo \(p\), and let \(\varepsilon\in\{1,-1\}\).
For every \(z\pmod{p^{3t}}\),

\[
 \boxed{
 \sum_{\substack{u\bmod p^{3t}\\
 u^3+\varepsilon p^{2t}cu=z}}
 \omega_{p,t}(u)
 \le3.
 }
\tag{12}
\]

The estimate is uniform over the unit \(c\); in the two CRT coordinates
below, \(c\) is the unit contributed by the other prime and may depend on
\(t\).

**Proof.** First suppose \(z=0\).  If \(h=v_p(u)<t\), then

\[
 v_p\bigl(u^3+\varepsilon p^{2t}cu\bigr)=3h<3t,
\]

because \(3h<2t+h\).  Hence such a \(u\) is not a root.  Conversely every
\(u\in p^t\mathbb Z/p^{3t}\mathbb Z\) is a root.  There are \(p^{2t}\)
such elements and each has weight \(p^{-2t}\), so their total weight is 1.

Now suppose \(z\ne0\), and put \(e=v_p(z)<3t\).  Every root has a unique
valuation \(h<t\), and the same valuation comparison forces

\[
 e=3h.
\tag{13}
\]

Write \(s=t-h\) and \(u=p^hv\), where \(v\) is a unit.  After division by
\(p^{3h}\), the root congruence becomes

\[
 v^3+\varepsilon p^{2s}cv
 \equiv z/p^{3h}\pmod{p^{3s}}.
\tag{14}
\]

Each solution \(v\pmod{p^{3s}}\) has exactly \(p^{2h}\) lifts back to
\(u\pmod{p^{3t}}\).

There are at most three unit solutions of (14).  If \(p\ne3\), reduction
modulo \(p\) has at most three roots.  Two roots with the same reduction
cannot be distinct modulo \(p^{3s}\), because their difference times

\[
 v_1^2+v_1v_2+v_2^2+\varepsilon p^{2s}c
\]

is zero, and the displayed second factor is a unit modulo \(p\).

If \(p=3\), all unit roots have the same residue modulo 3 because
\(v^3\equiv v\pmod3\).  If \(v_1\equiv v_2\pmod3\), then

\[
 v_3\bigl(v_1^2+v_1v_2+v_2^2+
 \varepsilon3^{2s}c\bigr)=1.
\tag{15}
\]

Indeed, writing \(v_1=v_2+3a\), the quadratic sum is
\(3(v_2^2+3av_2+3a^2)\), and the term \(3^{2s}c\) is divisible by 9.
The difference factorization therefore gives
\(v_1\equiv v_2\pmod{3^{3s-1}}\).  A fixed class modulo
\(3^{3s-1}\) has only three lifts modulo \(3^{3s}\).

Thus the number of roots \(u\) of valuation \(h\) is at most
\(3p^{2h}\).  Multiplication by their common weight \(p^{-2h}\) proves
(12). \(\square\)

The cancellation in the last line is the exact fiber-level renormalization:
factoring out a root valuation \(h\) sends \(t\) to \(t-h\), produces
\(p^{2h}\) discarded lifts, and the weight contributes precisely
\(p^{-2h}\).

Under CRT, define

\[
 \Omega_t(u)
 =q^{-2\min(v_q(u),t)}r^{-2\min(v_r(u),t)}.
\tag{16}
\]

Lemma 1 factors between \(q\) and \(r\), and therefore gives, for both signs,

\[
 \sum_{u^3\pm C_tu=z}\Omega_t(u)\le9.
\tag{17}
\]

Fixing one input in (3) or (4) now yields the genuinely translated statement.

**Corollary 2 (anchored translated charging).** For every output \(z\),

\[
 \boxed{
 \sum_{\substack{(x,y)\in A\times B\\P_{C_t}(x,y)=z}}
 \Omega_t(x-y)
 \le9\min\{|A|,|B|\}.
 }
\tag{18}
\]

The important feature is the factor \(\min(|A|,|B|)\).  It is the retained
anchor mass which the failed full-ring coarea estimate discarded.

---

## E. Complete quantitative proof

Let \(a=|A|\) and \(b=|B|\).  The exact audited product-tree estimate inside
the frozen homogeneous proof is

\[
 \boxed{
 \sum_{x\in A,y\in B}
 \left(\frac{\operatorname{ord}(x-y)}{M_t}\right)^2
 \ge
 \frac{a^2b^2}{4\mathcal C_{q,r}M_t^2}.
 }
\tag{19}
\]

Here \(\operatorname{ord}(u)\) is the additive order of \(u\) in
\(\mathbb Z/M_t\mathbb Z\), with \(\operatorname{ord}(0)=1\).  Under CRT,

\[
 \left(\frac{\operatorname{ord}(u)}{M_t}\right)^2
 =q^{-2\min(v_q(u),3t)}r^{-2\min(v_r(u),3t)}.
\tag{20}
\]

Since truncation at \(t\) gives a larger weight than truncation at \(3t\),

\[
 \Omega_t(u)
 \ge
 \left(\frac{\operatorname{ord}(u)}{M_t}\right)^2.
\tag{21}
\]

Consequently

\[
 \sum_{x\in A,y\in B}\Omega_t(x-y)
 \ge
 \frac{a^2b^2}{4\mathcal C_{q,r}M_t^2}.
\tag{22}
\]

On the other hand, group the same sum by the actual outputs of
\(P_{C_t}\).  Corollary 2 gives

\[
 \sum_{x\in A,y\in B}\Omega_t(x-y)
 \le9\min(a,b)|P_{C_t}(A,B)|.
\tag{23}
\]

Combining (22) and (23), and using
\(a^2b^2/\min(a,b)=ab\max(a,b)\), gives

\[
 |P_{C_t}(A,B)|
 \ge
 \frac1{36\mathcal C_{q,r}}
 \frac{ab\max(a,b)}{M_t^2}.
\]

This is (2).  The constant depends only on the two fixed primes and is
independent of \(t,A,B\).  No density range, integrality exception, or hidden
depth-dependent loss remains.

---

## F. Why the earlier obstructions are overcome

### F.1 Static coarea

The forbidden strategy sought a set-independent weight whose mass on every
**full two-variable output fiber** was bounded by an absolute constant.
The weight \(\Omega_t\) does not have that property, and no such claim is
made.  Instead, (18) bounds its mass on the restricted fiber
\((A\times B)\cap P^{-1}(z)\) by
\(9\min(|A|,|B|)\).  This bound comes from fixing an actual input and using
the correlation \(v=u+2y\) or \(v=2x-u\).  Replacing the true correlated
\((u,v)\)-set by a Cartesian product would destroy exactly this fact.

### F.2 Mass-only recursion

The failed Bellman induction could only charge a side rectangle by its local
cubic mass and therefore lost the third large factor.  Inequality (19),
coming from the frozen maximal-cross-edge/triple-convolution argument, already
charges all Cartesian cross-pairs and supplies \(a^2b^2\).  The anchored fiber
capacity in (18) removes only \(\min(a,b)\), leaving the desired polarized
quantity \(ab\max(a,b)\).  No depthwise multiplication of lossy child
constants occurs.

### F.3 Address-only charging

Addresses do separate ancestor-descendant side bands, but (10) shows that
incomparable bands can overlap with multiplicity tending to infinity.  The
proof of (2) does not need to choose a prefix-free family or bound that raw
overlap.  The one-variable root bound controls the total weighted
multiplicity of all translated branches simultaneously.

---

## G. Consequences for full BP2+ and the three-prime theorem

The canonical self-similar branch is now closed positively.  The same proof
also applies, without a new idea, to the rectangular exact self-similar family

\[
 M=q^{3t_q}r^{3t_r},\qquad
 C=c_0q^{2t_q}r^{2t_r},\qquad (c_0,qr)=1,
\tag{24}
\]

with the same constant (2).  Each local factor separately has the exact
\(2{:}3\) relation used in Lemma 1.

This does **not** prove full BP2+ for arbitrary intermediate coefficients.
The exact ratio is used at the critical shell.  To see the obstruction to an
automatic extension, let \(p\ge5\), use modulus \(p^{3h+N}\), and take

\[
 C=-3p^{2h},\qquad z=-2p^{3h}.
\]

Writing \(u=p^hw\) gives

\[
 u^3+Cu-z=p^{3h}(w-1)^2(w+2).
\]

For \(w\equiv1\pmod{p^{\lceil N/2\rceil}}\), this vanishes modulo
\(p^{3h+N}\).  Modulo the residual \(p^N\) there are
\(p^{\lfloor N/2\rfloor}\) such roots, and each has \(p^{2h}\) lifts in the
original variable.  Their total \(p^{-2h}\)-weight is at least

\[
 p^{\lfloor N/2\rfloor},
\tag{25}
\]

which is unbounded.  In the self-similar core \(N=0\); this residual critical
fiber is exactly what disappears.

Equation (25) is an obstruction to the present proof, not a counterexample to
BP2+.  Therefore the full arbitrary-\(C\) three-prime theorem remains open,
because the frozen implication BP2+ \(\Rightarrow\) that theorem still needs
BP2+ outside the exact self-similar ratios.  The many-prime/global real-set
construction is likewise not closed by this checkpoint.

---

## H. Exactly one next unresolved statement

For fixed distinct odd primes \(q,r\ge5\), determine whether there is a
constant \(b_{q,r}>0\) such that, uniformly in \(t\ge1\) and all nonempty
\(A,B\subseteq\mathbb Z/M_t\mathbb Z\),

\[
 \boxed{
 \begin{gathered}
 M_t=q^{4t}r^{3t},\qquad
 C_t=-3q^{2t}r^{2t},\\[2mm]
 |P_{C_t}(A,B)|
 \ge b_{q,r}
 \frac{|A||B|\max\{|A|,|B|\}}{M_t^2}.
 \end{gathered}
 }
\tag{26}
\]

This is the first canonical rectangular family in which one prime retains the
solved \(2{:}3\) scaling while the other has a growing residual double-critical
fiber of the form displayed in (25).
