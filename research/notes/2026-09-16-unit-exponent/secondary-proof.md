# UE-S1–UE-S2 — the secondary valuation-exponent carrier

## Identity, scope and evidence

- **Date/version:** 16 September 2026, version 1.
- **Track/branch:** T03, the one authorized secondary mutation in the
  unit-exponent / Følner cycle.
- **Fixed polynomial:** \(Q(x,y)=x^2+xy+y^2\), on the same finite rational
  set in both coordinates, viewed in the fixed embedding into \(\mathbb R\).
- **UE-S1 — PROVED:** the generators below give multiplicatively independent
  actual norm-one actions, but every ordered Cartesian pair has exactly one
  return under their entire integer-exponent group: the identity.
- **UE-S2 — PROVED:** the entire image has exactly
  \(n_d^2/4+n_d/2\) elements. This is an actual image calculation, separate
  from the action obstruction in UE-S1.
- **Quantifiers:** fix any integer \(L\ge1\) first; define the infinite
  generator sequence below; then both theorems hold for every \(d\ge1\).
  The identity-only conclusion includes arbitrary positive and negative
  integer exponents of all of the first \(d\) generators.
- **Proof source:** this file, §§1–6. The elementary Euclidean-factorization
  fact used in §2 is also proved in
  [HR-4A](../2026-09-16-high-return/denominator-obstruction.md#hr-4a--an-elementary-integer-norm-representation-bound);
  that proof was inspected locally, and the needed argument is repeated here.
- **Audit performed:** an independent internal agent checked the lead's
  proposed valuation and specialization arguments and supplied the full
  proofs here. This is an internal mathematical audit, not external review.
- **Computation/network:** symbolic proof only; zero research evaluations,
  no mathematical program or finite experiment executed by this author,
  and no network, external lookup or literature/novelty claim.
- **Disposition:** **ACTION GO / CARTESIAN FAIL** for this specified secondary
  carrier. Neither theorem is a universal obstruction to norm-one methods,
  other valuation boxes, or the real T03 target.

## Mathematical statement

Fix \(L\ge1\), and recursively define positive integers

\[
P_0=1,\qquad t_i=3P_{i-1}^{2L+1},\qquad
q_i=t_i^2+t_i+1,\qquad P_i=P_{i-1}q_i.
\tag{1}
\]

Let \(\omega^2+\omega+1=0\), with
\(\omega=(-1+i\sqrt3)/2\), and put

\[
\alpha_i=t_i-\omega,\qquad
u_i=\frac{\alpha_i}{\overline\alpha_i},\qquad
\Gamma_d=\left\{\prod_{i=1}^d u_i^{h_i}:h\in\mathbb Z^d\right\}.
\tag{2}
\]

The scalar carrier is

\[
A_d=\left\{\sigma\prod_{i=1}^d q_i^{e_i}:
\sigma\in\{1,-1\},\quad e\in\{-L,\ldots,L\}^d\right\}.
\tag{3}
\]

Write \(M_d=(2L+1)^d\) and \(n_d=2M_d\). Then:

1. \(|A_d|=n_d\), and the map \(h\mapsto\prod u_i^{h_i}\) is injective
   on all of \(\mathbb Z^d\).
2. For every \((x,y)\in A_d^2\) and \(h\in\mathbb Z^d\),
   \[
   \left(\prod_i u_i^{h_i}\right)(x-\omega y)=x'-\omega y',
   \qquad (x',y')\in A_d^2
   \quad\Longrightarrow\quad h=0,
   \quad (x',y')=(x,y).
   \tag{4}
   \]
3. Every \(Q\)-fiber has size two or four, and
   \[
   |Q(A_d,A_d)|=M_d^2+M_d
   =\frac{n_d^2}{4}+\frac{n_d}{2}.
   \tag{5}
   \]
   Precisely \(2M_d\) outputs have fibers of size two and
   \(M_d(M_d-1)\) outputs have fibers of size four.

### What it means

The action box has exponentially many genuinely different transformations.
Nevertheless, none of its nonidentity elements returns even one pair of
this Cartesian square. All collisions in the full quadratic image come
from swapping the two coordinates and changing their signs simultaneously.

### Why it matters

The proposed valuation translation succeeds as an action construction and
fails completely as a Cartesian return construction. The full-image formula
also rules out a fixed power saving for this carrier: its factor of about
four is constant, while a power saving requires a factor growing with
\(n_d\). This conclusion uses no assertion about untested families.

## 1. Arithmetic separation and exact input count

For \(j>i\), \(q_i\mid P_{j-1}\), so
\(t_j\equiv0\pmod{q_i}\) and

\[
q_j\equiv1\pmod{q_i}.
\tag{6}
\]

Thus the \(q_i\) are pairwise coprime. Every \(q_i>1\), and
\(q_i\equiv1\pmod3\), since \(3\mid t_i\). They are odd, since
\(t_i(t_i+1)\) is even. No assertion that the \(q_i\) themselves are
prime is made or needed.

For later use, if \(P=P_{i-1}\ge1\), then

\[
q_i=9P^{4L+2}+3P^{2L+1}+1
>6P^{4L}>3P^{4L}.
\tag{7}
\]

If two expressions in (3) agree, positivity of the \(q_i\) recovers the
sign. For any rational prime \(p\mid q_i\), its rational valuation then
recovers the exponent as

\[
e_i=\frac{v_p(|x|)}{v_p(q_i)}.
\tag{8}
\]

Here all other \(q_j\) are \(p\)-units. The parameterization is therefore
injective and \(|A_d|=2(2L+1)^d\), both an upper and a lower count.
Every input is nonzero, and every ordered pair in \(A_d^2\) is included.

## 2. The actual prime valuations of the action

Work in \(\mathcal O=\mathbb Z[\omega]\), inside the fixed quadratic
field \(K=\mathbb Q(\omega)\). The norm is
\(N(a+b\omega)=a^2-ab+b^2\), so

\[
N(\alpha_i)=q_i,\qquad N(u_i)=1.
\tag{9}
\]

We use prime-factor valuations on \(K^\times\); equivalently, these are
the prime-ideal valuations at the corresponding principal prime ideals.
The following paragraph supplies the required factorization facts without
an outside theorem or a factorization computation.

For \(z,w\in\mathcal O\), \(w\ne0\), write
\(z/w=a+b\omega\) with rational \(a,b\) and round both to nearest
integers. The rounding error \(\delta+\eta\omega\) has
\(|\delta|,|\eta|\le1/2\) and norm at most \(3/4<1\).
This gives Euclidean division for the positive integer norm. The Euclidean
algorithm gives Bezout identities; an irreducible is consequently prime.
Induction on the norm gives factorization into irreducibles, and primality
gives uniqueness up to units. In particular, if a rational prime \(p\)
is reducible in \(\mathcal O\), its two irreducible factors have norm
\(p\) and are conjugates up to units, since their norm product is \(p^2\).

The elements \(\alpha_i\) and \(\overline\alpha_i\) are coprime in
\(\mathcal O\). Indeed, a common irreducible would divide
\(\omega-\overline\omega\), whose norm is 3, and would also have norm
dividing \(q_i\); this contradicts \(3\nmid q_i\).

Fix a rational prime \(p\mid q_i\), and write \(k=v_p(q_i)\ge1\).
The prime \(p\) cannot be irreducible in \(\mathcal O\): from
\(p\mid\alpha_i\overline\alpha_i\), primality would imply
\(p\mid\alpha_i\) or \(p\mid\overline\alpha_i\), which is impossible
by the coefficient of \(\omega\), namely \(-1\) or \(+1\).
Therefore

\[
p=\pi\overline\pi,
\qquad N(\pi)=p,
\tag{10}
\]

after choosing a representative. The two factors are not associated:
otherwise conjugation would make any factor above \(p\) dividing one
of \(\alpha_i,\overline\alpha_i\) divide both, contradicting their
coprimality. Orient the pair so that \(\pi\mid\alpha_i\). Unique
factorization now gives

\[
v_\pi(\alpha_i)=k,\quad
v_{\overline\pi}(\alpha_i)=0,\quad
v_\pi(u_i)=k,\quad
v_{\overline\pi}(u_i)=-k.
\tag{11}
\]

For \(j\ne i\), both valuations of \(u_j\) are zero, because their
rational norm supports are disjoint. For rational \(r\ne0\),
\(v_\pi(r)=v_{\overline\pi}(r)=v_p(r)\). For \(z\ne0\) in \(K\),
conjugation interchanges the factors and gives

\[
v_p(N(z))=v_\pi(z)+v_{\overline\pi}(z).
\tag{12}
\]

These formulas include negative valuations, by extending valuations from
\(\mathcal O\) to its fraction field by subtraction.

If \(\prod_i u_i^{h_i}=1\), (11) at any \(p\mid q_i\) implies
\(kh_i=0\), hence \(h_i=0\), for every \(i\). This proves global
multiplicative independence. It also excludes every nontrivial torsion
relation, because a root of unity has all prime valuations zero.

The fixed complex embedding is injective, so these algebraically different
elements give different actual real-linear transformations of coefficient
pairs. More explicitly, if \(u=a+b\omega\) with rational \(a,b\), then

\[
u(x-\omega y)=(ax+by)-\omega\bigl(-bx+(a-b)y\bigr).
\tag{13}
\]

Thus multiplication corresponds to a genuine transformation of \(\mathbb R^2\)
preserving \(Q\), not a modular or formal action. At any nonzero
\(x-\omega y\), multiplication has trivial stabilizer. In particular,
the box \(|h_i|\le H\), for any fixed integer \(H\ge1\), contains
exactly \((2H+1)^d\) different actions.

## 3. Every norm determines the minimum exponents

Take an arbitrary ordered pair from (3):

\[
x=\sigma\prod_i q_i^{e_i},\qquad
y=\tau\prod_i q_i^{f_i},\qquad
m_i=\min(e_i,f_i).
\]

Define the rational common factor and integral residual coordinates

\[
S=\prod_i q_i^{m_i},\qquad
X=x/S=\sigma\prod_i q_i^{e_i-m_i},\qquad
Y=y/S=\tau\prod_i q_i^{f_i-m_i}.
\tag{14}
\]

All residual exponents lie in \([0,2L]\), and for each block at least
one residual exponent is zero. In particular, \(X,Y\) are nonzero
integers. This normalization is valid even if some or all original
exponents are negative; no rational denominator is left in \(X,Y\).

For a positive rational number \(T\), define

\[
w_i(T)=\min_{p\mid q_i}
\left\lfloor\frac{v_p(T)}{v_p(q_i)}\right\rfloor.
\tag{15}
\]

We claim that

\[
\boxed{w_i(Q(x,y))=2m_i\quad\text{for every }i.}
\tag{16}
\]

Because \(Q(x,y)=S^2Q(X,Y)\), it suffices to show
\(q_i\nmid Q(X,Y)\). Indeed, all valuations of the positive integer
\(Q(X,Y)\) are nonnegative, and nondivisibility by \(q_i\) says that
at least one \(p\mid q_i\) has

\[
0\le v_p(Q(X,Y))<v_p(q_i).
\tag{17}
\]

If \(e_i\ne f_i\), one of \(X,Y\) is divisible by \(q_i\) and the
other is coprime to \(q_i\). Reduction of \(Q\) modulo any \(p\mid q_i\)
is the square of that unit, so in fact every such residual valuation is
zero.

If \(e_i=f_i\), both residual exponents at \(i\) are zero. By (6),
later blocks reduce to 1 modulo \(q_i\), so

\[
Q(X,Y)\equiv Q(X_0,Y_0)\pmod{q_i},
\quad
X_0=\sigma\prod_{j<i}q_j^{e_j-m_j},\quad
Y_0=\tau\prod_{j<i}q_j^{f_j-m_j}.
\tag{18}
\]

Both \(|X_0|\) and \(|Y_0|\) are at most \(P_{i-1}^{2L}\). The
positive-definite identity

\[
Q(a,b)=(a+b/2)^2+3b^2/4
\]

therefore yields

\[
0<Q(X_0,Y_0)\le3P_{i-1}^{4L}<q_i.
\tag{19}
\]

This includes both sign choices and the first block \(P_0=1\).
The residue in (18) is nonzero modulo the entire integer \(q_i\),
which proves (17) and hence (16). Notice that it need not be nonzero
modulo every prime divisor: the proof requires and supplies at least one
prime with valuation strictly below its multiplicity in \(q_i\).

## 4. UE-S1: identity-only returns on the entire Cartesian square

Suppose (4) holds. Norm preservation and (16) give

\[
\min(e_i',f_i')=\min(e_i,f_i)=m_i\quad\text{for every }i.
\tag{20}
\]

Thus the same rational \(S\) from (14) normalizes the returned
coordinates to nonzero integers \(X'=x'/S\), \(Y'=y'/S\). Dividing
(4) by \(S\), we get an equality in the field

\[
\left(\prod_i u_i^{h_i}\right)(X-\omega Y)
=X'-\omega Y'\in\mathcal O.
\tag{21}
\]

Fix \(i\), choose \(p\mid q_i\) satisfying (17), and use the two
prime valuations oriented as in (11), with \(k=v_p(q_i)\). Put

\[
A=v_\pi(X-\omega Y),\qquad
B=v_{\overline\pi}(X-\omega Y).
\]

Integrality and (12), (17) give

\[
A\ge0,\qquad B\ge0,\qquad A+B<k.
\tag{22}
\]

In particular both \(A<k\) and \(B<k\). On the left of (21), the two
valuations are exactly

\[
A+kh_i,\qquad B-kh_i,
\tag{23}
\]

since all other generators are units at these primes. If \(h_i\ge1\),
the second is negative; if \(h_i\le-1\), the first is negative.
Either case contradicts the integrality of the right side of (21).
Consequently \(h_i=0\). Doing this separately at every block gives
\(h=0\); linear independence of \(1,\omega\) over \(\mathbb Q\)
then gives \(x'=x,y'=y\). This proves UE-S1.

There are no exceptional pairs, boundary exclusions, zero inputs or
uncontrolled tails. For any action window containing the identity,

\[
R_{\rm label}(x,y)=R_{\rm action}(x,y)=R_{\rm pair}(x,y)=1
\quad\text{on all of }A_d^2.
\tag{24}
\]

Here the three return counts refer to the eligible returning exponent
vectors, their actual actions, and their resulting Cartesian pairs,
respectively. The total available action box may be exponential even
though its returning part consists of one element. For every fixed
positive threshold exponent, all \(n_d^2\) pairs eventually lie below
that threshold. The requested exponentially small exceptional set is
therefore impossible for this carrier/action pair.

## 5. A finite-term specialization lemma

This lemma is about the same generator sequence; it introduces no further
carrier. Suppose an integer polynomial \(F(T_1,\ldots,T_d)\) has degree
at most \(4L\) in each variable and coefficient \(\ell^1\)-norm at
most 6. Then

\[
F(q_1,\ldots,q_d)=0\quad\Longrightarrow\quad F=0.
\tag{25}
\]

**Proof.** Induct on \(d\), the case \(d=0\) being immediate. Write
\(F=\sum_{r=0}^{4L}F_r(T_1,\ldots,T_{d-1})T_d^r\). Each integer
\(c_r=F_r(q_1,\ldots,q_{d-1})\) satisfies

\[
|c_r|\le6P_{d-1}^{4L}<q_d,
\tag{26}
\]

because every evaluated monomial is at most \(P_{d-1}^{4L}\).
The equality \(\sum_r c_rq_d^r=0\), reduced modulo \(q_d\), forces
\(c_0=0\). Divide by \(q_d\), repeat, and get every \(c_r=0\).
Each \(F_r\) satisfies the inductive degree and coefficient bounds, so
each is the zero polynomial. This proves (25). Signed coefficients cause
no difficulty: an integer strictly between \(-q_d\) and \(q_d\)
and divisible by \(q_d\) is zero. \(\square\)

## 6. UE-S2: exact full image and every fiber

Let \(D=P_d^L\). Multiplying a scalar input in (3) by \(D\) gives

\[
Dx=\sigma\prod_i q_i^{E_i},\qquad E_i=e_i+L\in\{0,\ldots,2L\}.
\tag{27}
\]

Thus clearing an equality of two \(Q\)-values by \(D^2\) gives an
integer polynomial equality at \((q_1,\ldots,q_d)\). Its difference
has at most six signed monomial terms, coefficient \(\ell^1\)-norm
at most 6 even after collecting terms, and coordinate degrees at most
\(4L\). By (25), the evaluated values agree exactly when their formal
polynomials agree.

For exponent vectors \(E,F\in\{0,\ldots,2L\}^d\), write
\(T^E=\prod_iT_i^{E_i}\). The formal output is

\[
Q(\sigma T^E,\tau T^F)
=T^{2E}+\sigma\tau T^{E+F}+T^{2F}.
\tag{28}
\]

If \(E\ne F\), the three exponent vectors in (28) are distinct.
Their support determines its unique midpoint and the unordered pair of
endpoints, hence determines \(\{E,F\}\). To see uniqueness directly,
any midpoint of a three-point arithmetic progression is one third of
the sum of its three points; division by 3 is unique in \(\mathbb Q^d\).
The coefficient at the midpoint then determines \(\sigma\tau\).
Consequently the only equalities among these outputs come from swapping
the two inputs and changing both signs.

If \(E=F\), (28) is the single monomial
\((2+\sigma\tau)T^{2E}\), with coefficient 3 or 1. These two
possibilities are distinct, and equality determines both \(E\) and
\(\sigma\tau\). A one-term output cannot equal one of the three-term
outputs with unequal exponent vectors. This includes all degeneracies.

There are \(M_d\) unsigned monomials. Each of their \(\binom{M_d}{2}\)
unordered distinct pairs gives two relative-sign outputs, each with
exactly four ordered signed representations. Each of the \(M_d\)
equal pairs gives two outputs, each with exactly two representations.
Therefore

\[
|Q(A_d,A_d)|=2\binom{M_d}{2}+2M_d=M_d^2+M_d,
\]

and the fiber distribution is the one stated in (5). As a check on
complete coverage, the representation counts sum symbolically to
\(4M_d(M_d-1)+2(2M_d)=4M_d^2=n_d^2\). This is an identity, not
a finite computational test.

UE-S2 also clarifies the scope of UE-S1: the swap/common-sign collisions
are real norm collisions, but their nonidentity multipliers are outside
the selected free subgroup \(\Gamma_d\). Identity-only returns for
that subgroup do not mean that a quadratic fiber has size one.

## 7. Why the old dense one-prime theorem is not this proof

The earlier [HR-4 theorem](../2026-09-16-high-return/denominator-obstruction.md#hr-4--the-uniform-full-fiber-theorem)
treats the dense carrier
\(\{bp^{-k}:1\le|b|\le H,\ p\nmid b,\ 0\le k\le K\}\) for a
single denominator prime, with all eligible numerators up to \(H\).
Here the number of pairwise disjoint rational-prime support blocks grows
with \(d\), the scalar coordinates are sparse multiplicative monomials,
and valuations at different prime divisors of one \(q_i\) are tied to
the same exponent. It is not that dense family.

After a common scaling, any such finite set can be contained in a large
integer interval. Applying a bound in terms of that interval's height
does not produce a bound in terms of this sparse set's cardinality.
Indeed (1) gives

\[
9P_{i-1}^{4L+3}\le P_i\le13P_{i-1}^{4L+3},
\qquad
\log P_d=\Theta_L((4L+3)^d),
\tag{29}
\]

whereas \(\log n_d=d\log(2L+1)+O(1)\). Its heights are far beyond
a polynomial in \(n_d\). Thus old dense-carrier or polynomial-height
conclusions cannot simply be substituted for §§3–6. Those sections give
a separate proof for this exact sparse carrier. Being outside an old
theorem is not evidence of success.

No HR-N1 denominator-box test or proof search was rerun. The present
carrier, arbitrary-integer-power conclusion, and exact image formula
stand on the new arguments above. No affine \(Q+x\) or difference-set
analysis is undertaken.

## 8. Construction and rate ledger

| Item | Exact bound or treatment | Status/source |
|---|---|---|
| Parameter order | Fix \(L\ge1\), then define all \(q_i,u_i\) recursively, then grow the actual depth \(d\). A finite action window \(H\ge1\), if used, is also fixed before \(d\). | PROVED definitions (1)–(3) |
| Input lower and upper counts | Both equal \(n_d=2(2L+1)^d\). | PROVED §1 |
| Input thinning in both coordinates | None: all exponent vectors and both signs are included; all \(n_d^2\) ordered pairs are covered. | PROVED §§1, 4, 6 |
| Parameter and real-projection fibers | Exactly one, by sign and rational valuations. Real projection is the ordinary embedding \(\mathbb Q\subset\mathbb R\). | PROVED (8) |
| Total actual actions | \((2H+1)^d\) in \([-H,H]^d\); no multiplicative relation, torsion identification, embedding identification or denominator equivalence. | PROVED §2 |
| Returning labels/actions/pairs | Each equals 1 on every pair, even if all integer powers are permitted. The available exponential action growth contributes no return exponent. | PROVED UE-S1 |
| Stabilizers and repeated actions | Trivial stabilizers at every input norm element; action labels are injective. The failure is Cartesian legality, not duplicate labels. | PROVED §2 |
| Prime factors and splitting | Every prime dividing a \(q_i\) has two distinct conjugate factors in \(\mathcal O\); their exact valuations are \(\pm v_p(q_i)\). No factorization algorithm or density-of-primes input is required. | PROVED §2 |
| Local moduli and population | Growing coprime \(q_i\) are used only for exact congruences and valuations. There is no local-density or per-residue packing estimate to charge as a saving. | PROVED §§3–5 |
| Denominators and integrality | A common scalar denominator is \(D=P_d^L\); \(DA_d\subset\mathbb Z\), with absolute values at most \(P_d^{2L}\). For source/target comparison the equal minimum exponents give the same exact rational factor \(S\), and both residual coordinates are integral. | PROVED (14), (20), (27) |
| Multiplier denominators | \(u_i=\alpha_i^2/q_i\), so a common coefficient denominator for \(\prod u_i^{h_i}\) divides \(\prod q_i^{|h_i|}\). The proof admits all such exponents and charges their exact prime-valuation displacement. | PROVED (9), (11), (23) |
| Coefficient heights and archimedean radius | \(\max_{a\in A_d}|a|=P_d^L\), \(Q(a,b)\le3P_d^{2L}\); (29) records their growth. These radii are not converted into a volume count. | PROVED definitions and (29) |
| Field degree, discriminant and regulator | The action field is the fixed quadratic \(\mathbb Q(\omega)\), with discriminant \(-3\). Scalar inputs are rational. No growing field, class-number estimate, regulator estimate or lattice volume is used. The \(u_i\) are fractional norm-one elements, not asserted to be integral units. | PROVED §2; inapplicable estimates |
| Branches, ratios, carries and states | Two signs per scalar input; one carrier state. Every exponent vector is distinct. The at-most-six-term specialization proof accounts for possible arithmetic equalities; no unproved carry-free encoding is assumed. | PROVED §§1, 5–6 |
| Exceptional/uncovered pairs | Zero exceptions in both exact theorems. Conversely every pair fails any eventually growing return threshold. | PROVED §4 |
| Entire image and fibers | \(M_d^2+M_d\) outputs, all fibers of size 2 or 4, with the exact multiplicities in (5). | PROVED UE-S2 |
| Input rates | \(a=B=\log(2L+1)>0\), since \(\log n_d=ad+O(1)\). | PROVED exact input count |
| Output rate | \(\log|Q(A_d,A_d)|=2ad+o(d)\). In a gain/cost ledger one may take \(c-s=2a\), without double counting the constant symmetry factor. | PROVED exact image count |
| Net gap | \(\delta=2a-(c-s)=0\); no strictly positive power-saving exponent is certified or true along this carrier. | PROVED (5) |

For every fixed \(c_0>0\), (5) gives
\(|Q(A_d,A_d)|>n_d^{2-c_0}\) once \(n_d^{c_0}>4\).
This is a full-image obstruction for the carrier, stronger in scope than
the identity-only action theorem, but still not an obstruction to other
finite real sets.

## 9. Evidence and disposition

All equalities, congruences, counts and rates above are analytic statements
for all depths, not extrapolations from finite data. No coefficient
enumeration, prime factorization, action enumeration or runtime experiment
was performed for this proof. Repository-wide integrity checks and any
separately authorized diagnostics are recorded by the lead in the cycle's
verification record; they are not mathematical premises of UE-S1 or UE-S2.

The secondary mutation passes the distinct-action gate and fails the
Cartesian-return gate on every pair. Its actual quadratic image is also
quadratic in size. The branch is **FAILED in this stated scope**. The
general real target, unrelated carriers and the prior T03 obligations
remain **OPEN**; this note launches no further mutation or next task.
