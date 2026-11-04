# HR-2–HR-4 — denominator-depth carriers and Eisenstein returns

## Claim identities, authorization and scope

- **Version/date:** 2, 16 September 2026. The HR-4 addendum below strengthens
  the full-image conclusion for the dense numerator family; HR-2 and HR-3
  retain their original statements and proofs.
- **Track:** T03, a separate high-return Cartesian carrier branch. The fixed
  polynomial throughout is \(q(x,y)=x^2+xy+y^2\). No adaptive-radical parameter
  or RC15/4 assertion is changed.
- **HR-2 — PROVED:** on the dense denominator-depth carrier below at the
  prime 7, every nonzero point has at most
  \(1+\lfloor\log_7(3H^2)\rfloor\) returns under distinct powers of the
  specified Eisenstein multiplier. This is a **FAILED cyclic-action
  certificate** in the scope stated below, not an actual-image obstruction
  when the numerator alphabet grows.
- **HR-3 — PROVED:** for every prime and every fixed finite alphabet of
  nonzero integer numerators not divisible by that prime, every \(q\)-fiber
  has at most \(4|B|+|B|^2\) ordered pairs, independently of the denominator
  depth set. This is an **actual-image lower bound** and excludes power saving
  for that fixed-alphabet family.
- **HR-4 — PROVED, added in version 2:** for every \(\varepsilon>0\), a
  constant \(C_\varepsilon\) bounds every full \(q\)-fiber on
  \(A_{H,L,p}^2\) by \(C_\varepsilon H^\varepsilon\), uniformly over
  all primes \(p\), \(H\ge1\) and \(L\ge0\). Consequently the dense family
  has actual image size \(n^{2-o(1)}\) along every sequence with
  \(n\to\infty\). This entire dense family **FAILS** the power-saving target.
- **Task boundary:** the current user commissioned the high-return carrier
  cycle. This independent subtask proves and documents these two proposed
  scoped obstructions, including the subsequently proposed HR-4 strengthening.
  Finite computation budget: zero mathematical
  experiments. Network policy: offline; no literature or novelty assessment.
- **Proof/evidence source:** this file, the elementary valuation argument and
  the HR-2/HR-3 proofs from version 1, and the HR-4 addendum in version 2.
  The parent proposed the statements and a
  valuation outline; a separate agent independently checked and supplied the
  complete proofs here. This is internal proof work and review, not external
  certification. No computation or imported theorem on ideal factorization,
  class groups, or unique factorization is a premise. The HR-4 addendum proves
  the elementary factorization and divisor bounds it needs.
- **Context:** prior setup and T03 sources were inspected in the preceding
  solvable-extension cycle. The norm convention agrees with
  `research/notes/2026-09-14-study-notes/03-eisenstein.md`, SN-T03-1. Neither
  prior finite multiplier experiments nor their sign-cube obstruction is
  used as proof here. The T03 construction target remains **OPEN**.

## Common construction and notation

Fix a prime \(p\), integers \(H\ge1\), \(L\ge0\), and put

\[
A_{H,L,p}=\{b p^{-k}:b\in\mathbb Z,
1\le |b|\le H,\ p\nmid b,\ 0\le k\le L\}.
\tag{1}
\]

The representation in (1) is unique: the rational \(p\)-adic valuation of
\(b p^{-k}\) is \(-k\), which recovers the depth, and then recovers \(b\).
Consequently the same set in both coordinates has exactly

\[
n=|A_{H,L,p}|=2\bigl(H-\lfloor H/p\rfloor\bigr)(L+1)
\tag{2}
\]

distinct nonzero real elements. Both \(H\) and \(L\) may vary in HR-2; the
prime and the multiplier are fixed before they vary.

Let \(\omega=(-1+\sqrt{-3})/2\), so \(\omega^2+\omega+1=0\), and identify
the pair \((x,y)\) with \(z=x-\omega y\). Complex conjugation gives

\[
N(z)=z\bar z=q(x,y).
\tag{3}
\]

For the remainder of HR-2 only, fix

\[
p=7,\quad \pi=3+\omega,\quad \bar\pi=2-\omega,\quad
\pi\bar\pi=7,
\]
\[
u=\frac{\pi}{\bar\pi}=\frac{8+5\omega}{7},\qquad N(u)=1.
\tag{4}
\]

Multiplication of \(x-\omega y\) by \(u\) corresponds exactly to

\[
T_u(x,y)=\left(\frac{8x+5y}{7},\frac{-5x+3y}{7}\right).
\tag{5}
\]

Thus all integer powers of this real linear map preserve \(q\).

## Elementary split valuations at 7

This section supplies the local facts needed for HR-2 directly. Write
\(R=\mathbb Z[\omega]\), which is a subring of \(\mathbb C\) and hence an
integral domain. For \(a,b\in\mathbb Z\), explicit division gives

\[
\frac{a+b\omega}{\pi}
=\frac{(2a+b)+(-a+3b)\omega}{7},
\qquad
\frac{a+b\omega}{\bar\pi}
=\frac{(3a-b)+(a+2b)\omega}{7}.
\]

Therefore

\[
\pi\mid a+b\omega\iff a+4b\equiv0\pmod7,
\qquad
\bar\pi\mid a+b\omega\iff a+2b\equiv0\pmod7.
\tag{6}
\]

Evaluation at \(\omega=4\) and at \(\omega=2\) defines surjective ring maps
\(R\to\mathbb F_7\), since both residues satisfy
\(t^2+t+1=0\pmod7\). By (6) their kernels are precisely \(\pi R\) and
\(\bar\pi R\). Each kernel is prime because its quotient is a field.
Also \(\pi\) does not divide \(\bar\pi\), or conversely: their residues in
the opposite quotients are nonzero.

For \(0\ne w\in R\), define \(v_\pi(w)\) to be the largest integer
\(r\ge0\) such that \(\pi^r\) divides \(w\) in \(R\), and similarly for
\(v_{\bar\pi}\). These maxima exist. Indeed,
\(N(a+b\omega)=a^2-ab+b^2\) is a positive integer for nonzero \(a+b\omega\);
division by either prime factor divides this norm by 7, so cannot continue
indefinitely.

Primality from (6) shows that these valuations are additive on products.
Factoring out the maximal powers leaves two factors with nonzero residues
in the corresponding field, whose product still has nonzero residue.
Consequently one extends the valuations consistently to
\(\mathbb Q(\omega)^\times\) by subtracting numerator and denominator
valuations. Factoring the smaller power in a sum also proves

\[
v_\pi(w+w')\ge\min\{v_\pi(w),v_\pi(w')\},
\]

with equality when the two valuations differ; the same assertion holds for
\(v_{\bar\pi}\). In the unequal case the residual sum has one nonzero and
one zero residue, proving equality. This argument extends to fractions by
clearing a common denominator.

Since \(7=\pi\bar\pi\), and integers prime to 7 have nonzero residues in
both quotients, for every \(r\in\mathbb Q^\times\),

\[
v_\pi(r)=v_{\bar\pi}(r)=v_7(r).
\tag{7}
\]

Conjugation interchanges the two prime factors, so
\(v_\pi(\bar z)=v_{\bar\pi}(z)\). Combining this with (3) and (7) gives

\[
v_7(N(z))=v_\pi(z)+v_{\bar\pi}(z).
\tag{8}
\]

Finally (4) and nondivisibility of the opposite factors give

\[
v_\pi(u)=1,\qquad v_{\bar\pi}(u)=-1.
\tag{9}
\]

In particular \(u\) has infinite order. Distinct powers of \(u\) send any
nonzero \(z\) to distinct points; cancellation in the field proves this.

## HR-2 — logarithmic bound for all cyclic returns

**Theorem HR-2 — PROVED.** Set

\[
C_H=\lfloor\log_7(3H^2)\rfloor.
\]

For every \(H\ge1\), \(L\ge0\), every nonzero real pair \((x,y)\), and
every finite set of distinct integers \(J\subset\mathbb Z\),

\[
\#\{j\in J:T_u^j(x,y)\in A_{H,L,7}^{\,2}\}\le C_H+1.
\tag{10}
\]

In particular the bound applies to every initial pair in the carrier square,
is independent of \(L\) and of the exponent window, and is \(O(\log n)\)
uniformly over \(H,L\).

**Proof.** First take any pair in the carrier square and write

\[
x=b7^{-k},\qquad y=c7^{-\ell},\qquad
\alpha=v_\pi(x-\omega y),\quad
\beta=v_{\bar\pi}(x-\omega y).
\]

Both \(b,c\) are nonzero integers prime to 7. The element \(\omega\) is
a unit in both residue fields. If \(k\ne\ell\), (7) and the unequal-sum
valuation rule give

\[
\alpha=\beta=-\max\{k,\ell\}.
\tag{11}
\]

If \(k=\ell\), write \(x-\omega y=7^{-k}(b-\omega c)\). Both prime
valuations of \(b-\omega c\) are nonnegative, and they cannot both be
positive. Otherwise (6) would imply both
\(b-4c\equiv0\pmod7\) and \(b-2c\equiv0\pmod7\); subtracting gives
\(2c\equiv0\pmod7\), contrary to \(7\nmid c\). Thus

\[
\min\{\alpha,\beta\}=-k,
\qquad
\alpha+\beta=v_7(q(b,c))-2k.
\tag{12}
\]

As \(0<q(b,c)\le3H^2\) is an integer, its 7-adic valuation is at most
\(C_H\). Equations (11) and (12) therefore prove the uniform carrier
constraint

\[
|\alpha-\beta|\le C_H.
\tag{13}
\]

Now start with any nonzero rational pair, identified with
\(z\in\mathbb Q(\omega)^\times\), and put
\(\alpha_0=v_\pi(z)\), \(\beta_0=v_{\bar\pi}(z)\),
\(s=\alpha_0+\beta_0\). By (9), the valuations at exponent \(j\) are
\((\alpha_0+j,\beta_0-j)\), with their sum unchanged. If this exponent
returns to the Cartesian square, (13) forces

\[
\frac{s-C_H}{2}\le\alpha_0+j\le\frac{s+C_H}{2}.
\tag{14}
\]

This closed interval has length \(C_H\) and hence contains at most
\(C_H+1\) integers. Different integers \(j\) give different integers
\(\alpha_0+j\), proving (10) in this case.

For an arbitrary nonzero real pair, there is nothing to prove if no exponent
returns. Otherwise choose one returning exponent \(j_0\). Its pair is
rational, and the inverse map \(T_u^{-j_0}\) has rational coefficients by
(5). The original pair is therefore rational as well, reducing to the case
just proved.

Finally (2) at \(p=7\) implies \(H\le n\). Thus
\(C_H+1\le1+\lfloor\log_7(3n^2)\rfloor=O(\log n)\), with an absolute
constant independent of \(H,L,J\). \(\square\)

### Exact failure scope of HR-2

The theorem excludes polynomially many returns per point from any selected
finite subset of this cyclic action, even if its exponent window grows
arbitrarily. For every fixed \(\varepsilon>0\), the maximum return count is
\(o(n^\varepsilon)\). Thus this action cannot supply a threshold
\(M\ge n^\varepsilon\) for almost all pairs in a high-return support
certificate on these carriers.

This is not a bound on the entire \(q\)-fiber: equal-norm pairs need not lie
in one orbit of the cyclic group generated by \(u\). HR-2 does not prove an
actual-image lower bound for growing \(H\), rule out additional independent
multipliers, or rule out other numerator sets. Its logarithmic statement
must not be promoted to any of those conclusions.

## HR-3 — bounded full fibers for fixed numerator alphabets

**Theorem HR-3 — PROVED.** Fix any prime \(p\) and a finite nonempty set
\(B\subset\mathbb Z\setminus\{0\}\) such that \(p\nmid b\) for every
\(b\in B\). For every finite nonempty
\(K\subseteq\mathbb Z_{\ge0}\), put

\[
A_{B,K,p}=\{b p^{-k}:b\in B,\ k\in K\}.
\tag{15}
\]

Then \(n=|A_{B,K,p}|=|B||K|\), and every real output \(t\) has at most

\[
F_B=4|B|+|B|^2
\tag{16}
\]

ordered representations \(t=q(x,y)\) with \((x,y)\in A_{B,K,p}^2\).
Consequently

\[
\boxed{|q(A_{B,K,p},A_{B,K,p})|\ge\frac{n^2}{4|B|+|B|^2}.}
\tag{17}
\]

**Proof.** The input representation is unique by rational \(p\)-adic
valuation, giving the input count. Outputs are positive rationals because
\(q(x,y)=(x+y/2)^2+3y^2/4>0\) on this square. Outputs not positive rational
have no representations, so fix a positive rational \(t\).

First consider representations with unequal depths, say
\(x=b p^{-k},y=c p^{-\ell}\) and \(k>\ell\). Then

\[
t=p^{-2k}\bigl(b^2+bc p^{k-\ell}+c^2p^{2(k-\ell)}\bigr).
\tag{18}
\]

The expression in parentheses is congruent to \(b^2\not\equiv0\pmod p\).
Thus \(v_p(t)=-2k\): the output determines the deepest depth \(k\).
Choose the numerator \(b\) of that deeper coordinate, with at most \(|B|\)
choices. This fixes \(x\). The equation

\[
y^2+xy+x^2-t=0
\]

has at most two real solutions for \(y\), hence at most two allowed inputs.
This gives at most \(2|B|\) representations with the first coordinate
deeper. Interchanging the coordinates gives at most another \(2|B|\).
These two cases are disjoint and include every unequal-depth pair.

For equal depths, a choice of ordered numerators \((b,c)\in B^2\) gives

\[
t=p^{-2k}q(b,c).
\tag{19}
\]

The positive factor \(q(b,c)\) is fixed, and the powers \(p^{-2k}\) are
distinct. Thus (19) determines at most one allowed \(k\) for that ordered
numerator pair. There are at most \(|B|^2\) equal-depth representations.
Adding the two disjoint depth cases proves (16). Summing these fiber sizes
over all outputs counts exactly \(n^2\) ordered pairs, which proves (17).
\(\square\)

### Exact failure scope of HR-3

When \(p\) and \(B\) are fixed before \(|K|\) grows, \(F_B\) is a fixed
constant. For every fixed \(c>0\), (17) eventually exceeds
\(n^{2-c}\), and even exceeds any fixed constant times \(n^{2-c}\).
This fixed-alphabet family therefore **FAILS** the power-saving target.
The conclusion uses the entire image and does not depend on which multiplier
actions are considered.

The pointwise bound (17) is also true when an alphabet is chosen separately
at each size, but its constant then grows with \(|B|\). In particular it
does not by itself exclude every sequence with \(H\to\infty\) in (1).

## Construction and quantitative ledger

This ledger applies to the explicit carriers, not to all rational sets.
No unknown quantity below is assigned a zero cost.

| Gain/cost | Exact bound or applicability | Status |
|---|---|---|
| Fixed choices and growth order | HR-2 fixes \(p=7,u\) before arbitrary \(H,L\); HR-3 fixes \(p,B\) before arbitrary finite depth sets \(K\) grow | PROVED scope |
| Input counts, both lower and upper | HR-2 has exactly (2); HR-3 has exactly \(n=\lvert B\rvert\lvert K\rvert\) | PROVED |
| Input thinning in both coordinates | No points are removed after the stated numerator restriction. Its full cost is included exactly in (2); both coordinates use the same resulting set | PROVED |
| Parameter and projection fibers | Multiplicity one, recovered by rational \(p\)-adic valuation and the numerator | PROVED |
| Field degree and real projection | Inputs lie in \(\mathbb Q\), degree one; the norm algebra is the fixed quadratic field \(\mathbb Q(\omega)\). No growing-field input rate is assumed | PROVED |
| Discriminant, regulator and units | No lattice-volume, discriminant or regulator estimate occurs. The action is the explicit fractional norm-one element (4), not an uncharged family of integral units | Inapplicable estimates |
| Denominators and fixed-polynomial transport | The common input denominator divides \(p^L\), or \(p^{\max K}\) in HR-3. Clearing it is injective and scales every \(q\)-output by its square | PROVED |
| Multiplier denominators and ratio counts | \(u^{\pm j}\) has coefficients with denominator dividing \(7^{\lvert j\rvert}\); arbitrary distinct exponents are included in (10). Their exact valuation displacement is charged by (14) | PROVED |
| Local splitting | The only split-prime input is the explicit factorization \(7=(3+\omega)(2-\omega)\), with prime kernels proved in (6). HR-3 needs no splitting assumption | PROVED |
| Local density and residue packing | No local saving is multiplied by global volume; no packing or independence assertion is used | Inapplicable mechanisms |
| Coefficient heights and archimedean radii | In HR-2, \(\lvert x\rvert\le H\) and \(0<q(x,y)\le3H^2\); after denominator clearing, the bounds multiply by \(7^L\) and \(7^{2L}\). HR-3 uses \(\max_{b\in B}\lvert b\rvert\) and \(p^{\max K}\) analogously | PROVED |
| Branches and equality | HR-2 includes every returning exponent in the interval (14); HR-3 separates all pairs into two unequal-depth orientations and the equal-depth case | PROVED |
| Exceptional or uncovered pairs | None in either theorem. Inputs are nonzero, so there is no zero pair requiring a separate orbit charge | PROVED |
| HR-2 quantitative outcome | Every cyclic return count is at most \(1+\lfloor\log_7(3H^2)\rfloor=O(\log n)\). HR-2 alone does not determine the entire image rate for growing \(H\); HR-4 below supplies a separate full-fiber argument | PROVED action bound |
| HR-3 quantitative outcome | \(n^2/F_B\le\lvert q(A,A)\rvert\le n^2\), with \(F_B=4\lvert B\rvert+\lvert B\rvert^2\) fixed | PROVED actual image bounds |
| HR-3 rate and net gap | Using size parameter \(d=\log n\), input rates are \(a=B_{\mathrm{rate}}=1\), output rate \(g=2\), and \(\delta=2a-g=0\). Along \(K=\{0,\ldots,L\}\), input growth is only linear in depth \(L\), not exponential | FAILED fixed-alphabet carrier |
| Fixed positive saving | HR-2 excludes polynomial-return certification by this cyclic group; HR-3 excludes every fixed positive image saving for a fixed alphabet | Distinct scoped failures |

## Evidence limits and disposition

Both theorems are complete analytic statements over their displayed ranges.
No finite experiment, random seed, floating-point equality test or external
result is a premise, and no research program was run in this subtask.
No original or historical file is superseded. HR-2 restricts one cyclic action
on the dense denominator family. HR-3 restricts the full image only when the
numerator alphabet is fixed. Neither proves a general impossibility for the
T03 polynomial, which remains **OPEN**.

## HR-4 addendum — full-image obstruction for the dense family

**Added 16 September 2026, version 2.** This is a stronger, separate argument
for the actual image of (1), not a promotion of the cyclic-return count to
a full-fiber count. It removes the fixed-numerator-alphabet restriction for
this dense family. The parent supplied the small-gap/large-gap proof outline;
the author independently checked it and supplies the full argument, including
its elementary arithmetic dependencies, below. No experiment or network
access was used. No novelty or external-review claim is made.

### HR-4A — an elementary integer norm representation bound

For an integer \(N\ge1\), let

\[
R_q(N)=\#\{(a,b)\in\mathbb Z^2:a^2+ab+b^2=N\},
\qquad
\tau(N)=\#\{d\in\mathbb Z_{\ge1}:d\mid N\}.
\]

**Lemma HR-4A — PROVED here.** For every \(N\ge1\),

\[
R_q(N)\le6\tau(N).
\tag{20}
\]

**Proof.** The map \((a,b)\mapsto a-\omega b\) is a bijection from
\(\mathbb Z^2\) to \(R=\mathbb Z[\omega]\), with norm
\(N(a-\omega b)=q(a,b)\). We first give the needed factorization argument
in \(R\).

For \(z,w\in R\), \(w\ne0\), express \(z/w=\alpha+\beta\omega\) with
\(\alpha,\beta\in\mathbb Q\). Choose nearest integers \(a,b\), so
\(\delta=\alpha-a\) and \(\eta=\beta-b\) lie in \([-1/2,1/2]\). Then

\[
N\bigl(\delta+\eta\omega\bigr)
=\delta^2-\delta\eta+\eta^2\le\frac34<1.
\]

Consequently \(r=z-(a+b\omega)w\in R\) has either zero norm, meaning
\(r=0\), or integer norm strictly smaller than \(N(w)\). This is a
Euclidean division algorithm for the positive integer norm. Iteration and
back substitution give a greatest common divisor expressed as an \(R\)-linear
combination of the two inputs.

An irreducible \(\rho\) is therefore prime: if \(\rho\nmid z\), its
greatest common divisor with \(z\) is a unit, and a Bezout identity
\(a\rho+bz=1\) implies \(\rho\mid w\) whenever \(\rho\mid zw\).
Every nonzero nonunit has a factorization into irreducibles by induction on
its integer norm; a proper nonunit factor has smaller norm. Primality then
gives uniqueness up to units and order by cancellation. Thus the required
unique factorization assertion has been established directly.

The units are exactly the elements of norm one. The equation
\(a^2-ab+b^2=(a-b/2)^2+3b^2/4=1\) has exactly six integer solutions: two
for each of \(b=-1,0,1\). Therefore there are exactly six units.

Now fix a rational prime \(\ell\). If \(\ell\) is irreducible in \(R\),
its norm is \(\ell^2\). If it is reducible, factorization and
\(N(\ell)=\ell^2\) show that it has exactly two irreducible factors,
counting multiplicity, each of norm \(\ell\). Choose one, \(\rho\).
The identity \(\rho\bar\rho=N(\rho)=\ell\) shows that the other is
associated to \(\bar\rho\). These two factors are either associated or
nonassociated. This proves the three factorization possibilities needed
without any congruence classification of rational primes.

Write the ordinary integer factorization as \(N=\prod_\ell\ell^{e_\ell}\).
If \(z\in R\) has norm \(N\), then \(z\bar z=N\). Every irreducible
factor of \(z\) is consequently associated to a factor of one of these
rational primes. Factors arising from different rational primes cannot be
associated, since their norms are powers of different primes.

For an irreducible rational prime \(\ell\), its exponent in \(z\) must be
\(e_\ell/2\), giving at most one choice. For two associated factors of norm
\(\ell\), the exponent of their unique associate class must be
\(e_\ell\), again at most one choice. For two nonassociated factors of norm
\(\ell\), their two exponents must sum to \(e_\ell\), giving exactly
\(e_\ell+1\) possibilities before any further restrictions. Thus in all
cases there are at most \(e_\ell+1\) choices. Unique factorization and the
six possible units give at most

\[
6\prod_\ell(e_\ell+1)=6\tau(N)
\]

elements of norm \(N\), proving (20). \(\square\)

### HR-4B — the divisor bound used, with its constant

**Lemma HR-4B — PROVED here.** For every \(\theta>0\), there is a finite
constant \(D_\theta\), depending only on \(\theta\), such that

\[
\tau(N)\le D_\theta N^\theta\qquad(N\ge1).
\tag{21}
\]

**Proof.** For \(e\ge0\), \(e+1\le2^e\). Hence if a prime
\(\ell\ge2^{1/\theta}\), then \(e+1\le\ell^{\theta e}\). There are
only finitely many smaller primes. For each such prime, the sequence
\((e+1)\ell^{-\theta e}\), \(e\ge0\), has a finite supremum: its
successive ratio tends to \(\ell^{-\theta}<1\). Let \(D_\theta\) be the
product of those finitely many suprema, with the empty product interpreted
as one. Multiplying the inequalities over the prime factorization of \(N\)
gives (21). \(\square\)

### HR-4 — the uniform full-fiber theorem

**Theorem HR-4 — PROVED.** For every \(\varepsilon>0\), there is a finite
constant \(C_\varepsilon\), depending only on \(\varepsilon\), such that
for every prime \(p\), every integer \(H\ge1\), \(L\ge0\), and every
real number \(t\),

\[
\#\{(x,y)\in A_{H,L,p}^2:q(x,y)=t\}
\le C_\varepsilon H^\varepsilon.
\tag{22}
\]

In particular the bound is uniform in denominator depth, and even in the
choice of the prime. With \(n\) as in (2),

\[
\boxed{|q(A_{H,L,p},A_{H,L,p})|
\ge C_\varepsilon^{-1}n^{2-\varepsilon}.}
\tag{23}
\]

**Proof.** Nonpositive or irrational outputs have no representations, so
fix a positive rational output \(t\). Set

\[
r_0=\lfloor\log_p(H^2)\rfloor+1,
\qquad p^{r_0}>H^2.
\tag{24}
\]

First consider unequal depths. As proved in (18), the deeper depth is
uniquely determined by \(k=-v_p(t)/2\). If any such representation exists,
then \(k\) is a nonnegative integer and

\[
N=t p^{2k}
\tag{25}
\]

is one fixed positive integer not divisible by \(p\). When the first
coordinate is deeper, write the gap as \(r=k-\ell\ge1\); the norm equation
is exactly

\[
N=b^2+bc p^r+c^2p^{2r}=q(b,c p^r),
\qquad 1\le |b|,|c|\le H,\quad p\nmid bc.
\tag{26}
\]

**Large gaps, \(r\ge r_0\).** Equation (26) gives
\(N\equiv b^2\pmod{p^{r_0}}\). Since
\(1\le b^2\le H^2<p^{r_0}\), the residue of the fixed integer \(N\)
determines the integer \(b^2\) exactly, or gives no possible square.
There are at most two signed possibilities for \(b\). Together with the
fixed depth \(k\), these give at most two possibilities for the deeper
coordinate. For each, the equation \(q(x,y)=t\) is a quadratic in the other
coordinate and has at most two real roots. Thus there are at most four
large-gap representations with the first coordinate deeper and at most four
with the second deeper: at most eight in total, regardless of \(L\).

**Small gaps, \(1\le r<r_0\).** Now \(p^r\le H^2\), and (26) gives

\[
0<N\le3H^2p^{2r}\le3H^6.
\tag{27}
\]

The map from a representation to the integer pair \((b,c p^r)\) is
injective within the first-deeper orientation. Indeed \(r\) is the ordinary
\(p\)-adic valuation of the second integer, because \(p\nmid c\);
then \(c\), the fixed \(k\), and \(\ell=k-r\) are recovered. All small
gaps in that orientation therefore contribute at most \(R_q(N)\), not a
separate multiple of that bound for every gap. The other orientation
contributes at most another \(R_q(N)\). If no small-gap representation
exists this contribution is zero; otherwise (20), (21), and (27) bound it by

\[
2R_q(N)\le12D_\theta(3H^6)^\theta.
\tag{28}
\]

**Equal depths.** Write \(x=b p^{-k}\), \(y=c p^{-k}\). Then
\(t=p^{-2k}q(b,c)\), with \(q(b,c)\) a positive integer at most
\(3H^2\). Consequently

\[
v_p(t)+2k=v_p(q(b,c))
\in\{0,1,\ldots,\lfloor\log_p(3H^2)\rfloor\}.
\tag{29}
\]

The left side determines at most one depth \(k\) for each listed integer,
so there are at most \(1+\lfloor\log_p(3H^2)\rfloor\) possible depths,
independently of \(L\). For each such depth actually represented,
\(N_k=t p^{2k}\) is a positive integer at most \(3H^2\). The map from
the pair \((x,y)\) to its integer numerators \((b,c)\) is injective at fixed
\(k\). Equations (20) and (21) thus bound the entire equal-depth
contribution by

\[
6\bigl(1+\lfloor\log_p(3H^2)\rfloor\bigr)
D_\theta(3H^2)^\theta.
\tag{30}
\]

These three cases are disjoint and exhaust all ordered pairs. Adding their
bounds, the full fiber is at most

\[
8+12D_\theta 3^\theta H^{6\theta}
+6D_\theta3^\theta
\bigl(1+\lfloor\log_p(3H^2)\rfloor\bigr)H^{2\theta}.
\tag{31}
\]

Choose \(\theta=\varepsilon/12\). Uniformly for every prime \(p\ge2\),
\(1+\lfloor\log_p(3H^2)\rfloor\le1+\log_2(3H^2)\), and this is at
most a constant depending only on \(\varepsilon\) times
\(H^{\varepsilon/2}\), for \(H\ge1\). Thus the powers of \(H\) in
the second and third terms of (31) are at most \(\varepsilon/2\) and
\(2\varepsilon/3\), respectively. Absorbing their constants and the first
term gives (22), with \(C_\varepsilon\) independent of \(p,H,L\).

Finally, (2) and \(p\ge2\) imply \(H\le n\). Summing the full fibers
over all outputs counts exactly \(n^2\) ordered pairs, so (22) gives

\[
|q(A,A)|\ge\frac{n^2}{C_\varepsilon H^\varepsilon}
\ge C_\varepsilon^{-1}n^{2-\varepsilon},
\]

as claimed. \(\square\)

### HR-4 construction ledger and disposition

The exact input representation, denominator charges, fixed polynomial and
coverage rows in the preceding ledger continue to apply. The new argument
replaces the growing \(|B|^2\) loss of HR-3 by a subpower full-fiber bound
for the specific dense alphabet in (1).

| Gain/cost | Bound and reason | Status |
|---|---|---|
| Choices and quantifiers | Choose the desired \(\varepsilon>0\) first; \(C_\varepsilon\) is then fixed. The bound holds for all primes and all \(H,L\); no selected subsequence or favorable depth is assumed | PROVED |
| All-pair split | Every pair has equal depths, small unequal gap, or large unequal gap; both unequal orientations are included | PROVED |
| Large-gap fibers | At most eight, by the exact residue of the fixed normalized norm and the two roots of a quadratic | PROVED |
| Small-gap fibers | At most \(2R_q(N)\), with \(N\le3H^6\); numerator coprimality makes the norm-pair encoding injective across every small gap | PROVED |
| Equal-depth fibers | At most \(1+\lfloor\log_p(3H^2)\rfloor\) candidate depths, each with norm at most \(3H^2\) | PROVED |
| Arithmetic multiplicities | Exactly six possible units and at most \(\tau(N)\) factor-exponent allocations, proved in HR-4A; no class-group or regulator estimate is omitted | PROVED |
| Divisor bound and constants | \(\tau(N)\le D_\theta N^\theta\) for fixed \(\theta=\varepsilon/12\); constants depend only on the chosen exponent, not the carrier size | PROVED |
| Denominators | The potentially large \(p^{2k}\) in (25) is handled without a height estimate in the large-gap case. Only in the small-gap case is the resulting norm bounded polynomially in \(H\) | PROVED |
| Exceptional or uncovered outputs | None; (31) bounds the actual entire fiber for every output | PROVED |
| Actual image rate | For every \(\varepsilon>0\), \(C_\varepsilon^{-1}n^{2-\varepsilon}\le\lvert q(A,A)\rvert\le n^2\). Equivalently the logarithmic image exponent tends to 2 along every growing sequence in this family | PROVED |
| Positive power-saving gate | No fixed \(c>0\) is possible on this family: choose \(\varepsilon=c/2\) in (23) and absorb the fixed constant as \(n\to\infty\) | FAILED dense carrier family |

Thus the dense denominator-depth family has image size \(n^{2-o(1)}\)
uniformly over its parameters. HR-4 is stronger than the two preceding scoped
failures for this family: it bounds full fibers and so cannot be evaded merely
by choosing more norm-one actions on the same carrier. It does not exclude
other rational carriers with different numerator/denominator relations,
growing number-field carriers, or the general real T03 target. Those broader
construction questions remain **OPEN**.
