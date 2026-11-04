## 2. Exact target

**OPEN — current target.**
\[
\boxed{\exists c>0\quad\forall N_0\ge1\quad
\exists\text{ finite }A\subset\mathbb R:
|A|\ge N_0,\qquad |Q(A,A)|\le |A|^{2-c}.}
\tag{TARGET}
\]
The same set occurs in both variables; \(c\) is fixed before the sets grow.

**HISTORICAL / SUPERSEDED — original broader question.** For every fixed \(P\in\mathbb R[x,y]\), does there exist \(c_P>0\) and arbitrarily large finite \(A\subset\mathbb R\) with \(|P(A,A)|\le |A|^{2-c_P}\)? The thread selected \(Q\) in the subsequent quadratic-norm prompts. The exact initial calendar date is `UNKNOWN FROM CURRENT THREAD RECORD`. This narrowing selected a difficult benchmark; it did not settle the universal question.

**OPEN — family-specific sufficient target, ARG.** For the actual adaptive family below, establish \(s_m\le K\rho^m\) for fixed \(K<\infty\), \(0<\rho<4\). Failure of ARG would not disprove TARGET for other families.

## 3. Fixed polynomial and notation

| Status | Object | Formula and role |
|---|---|---|
| OPEN target | \(Q\) | \(x^2+xy+y^2\), the sole final polynomial of T03 |
| PROVED identity | Eisenstein norm | \(Q(a,b)=N_{L(\omega)/L}(a-\omega b)\), \(\omega^2+\omega+1=0\) |
| Auxiliary | Radical branches | \(F_C^\pm(a,b)=2C+a+b\pm\sqrt{(C+a)(C+b)}\) |
| Auxiliary | Translated norm | \(Q(a,b)-3C^2/4\) |
| HISTORICAL benchmark | Common-inner additive | \(F(\alpha g(x)+\beta g(y)+\gamma)\) |
| HISTORICAL benchmark | Common-inner multiplicative | \(F(\lambda g(x)^r g(y)^s)\), \(r,s\ge0\) integers, \(r+s>0\) |
| Failed reconstruction benchmark | \(M_{ij}\) | \((i+j)^2\), not the target polynomial |

**PROVED — algebraic scope.** The homogeneous matrix of \(Q\) has determinant \(3/4\) and rank two. It is neither \(F(G(x)+H(y))\) nor \(F(G(x)H(y))\) with nonconstant univariate \(G,H\). In the additive case, outer degree one cannot produce \(xy\); outer degree two forces affine \(G,H\) and a rank-one quadratic part. In the multiplicative case, separate degrees two in both variables force total leading degree four, contrary to \(Q\)'s degree two.

**PROVED — adaptive construction.** For finite nonempty symmetric \(A\subset\mathbb R\), put
\[
n=|A|,\quad M=\max|A|,\quad C>M,\quad d_C=C-M,
\]
\[
\mathcal L_C(A)=\left\{\pm\sqrt{\frac{C+a}{d_C}}:a\in A\right\},
\quad \mathcal T_C(A)=\{F_C^\pm(a,b):a,b\in A\}.
\]
The positive roots are distinct and nonzero, so the lift has \(2n\) elements, and
\[
\boxed{Q(\mathcal L_C(A),\mathcal L_C(A))=d_C^{-1}\mathcal T_C(A).}
\tag{RAD}
\]
There are \(n(n+1)\) essential branch labels: two signs for each unordered old pair, with repetitions allowed.

Start with \(\mathcal A_0=\{\pm1\}\). The exact finite collision algorithm lists all helpful legal parameters, adds \(M+1\), minimizes the next image cardinality, and breaks ties by the least listed parameter. Call it \(C_m\), and let \(\mathcal A_{m+1}=\mathcal L_{C_m}(\mathcal A_m)\). This gives one-step comparison with every legal parameter, not a comparison of alternate descendants.

Write
\[
F_m=\mathbb Q(\mathcal A_m),\quad K_m=F_m(C_m),\quad
n_m=2^{m+1},\quad s_m=|Q(\mathcal A_m,\mathcal A_m)|,\quad p_m=s_m/n_m^2.
\]
For any comparison parameter use exactly \(K=\mathbb Q(A,C)\). Let \(c_j\) be the square-class sizes of \(C+A\) in \(K^\times/K^{\times2}\), \(b=\max c_j/n\), and \(W=|\mathcal T_C(A)\cap K|\). Field degree, normalization \(d_C\), and missing-cell deficit are different quantities.

## 4. Strongest proved results

### 4.1 Exact adaptive values and fields

**PROVED — imported frozen certificates.**

| \(m\) | \(n_m\) | \(s_m\) | Optimizing \(C_m\) |
|---:|---:|---:|---|
| 0 | 2 | 2 | \(5/3\) |
| 1 | 4 | 5 | \(5/2\) |
| 2 | 8 | 17 | \(4\) |
| 3 | 16 | 68 | \(3\) |
| 4 | 32 | 269 | UNKNOWN FROM CURRENT THREAD RECORD |

\[
\mathcal A_1=\{\pm1,\pm2\},\qquad
\mathcal A_2=\{\pm1,\pm\sqrt3,\pm\sqrt7,\pm3\}.
\]
Set
\[
\alpha=\sqrt{4+\sqrt3},\quad\beta=\sqrt{4-\sqrt3},
\quad g=\sqrt{4+\sqrt7},\quad h=\sqrt{4-\sqrt7}.
\]
Then
\[
\mathcal A_3=\{\pm1,\pm\sqrt3,\pm\sqrt5,\pm\sqrt7,
\pm\alpha,\pm\beta,\pm g,\pm h\},\quad M_3=\sqrt7,
\]
\[
\mathcal A_4=\left\{\pm\sqrt{\frac{3+a}{3-\sqrt7}}:a\in\mathcal A_3\right\}.
\]
Exactly
\[
F_3=\mathbb Q(\sqrt2,\sqrt3,\sqrt5,\sqrt7,\sqrt{13},\alpha),
\quad [F_3:\mathbb Q]=64,
\]
\[
[F_4:F_3]=2^8,\qquad [F_4:\mathbb Q]=16384.
\]
Field equality uses \(g-h=\sqrt2\), \(\alpha\beta=\sqrt{13}\),
\(g=(\sqrt{14}+\sqrt2)/2\), \(h=(\sqrt{14}-\sqrt2)/2\), and
\(\beta=\sqrt{13}(4-\sqrt3)\alpha/13\). The next degree is not an optimizer computation or an image bound.

### 4.2 Exact localization, root identity, and parameter restrictions

**PROVED — imported frozen results.** Different shifted square classes contribute individually unique outside-field branches. Hence
\[
\boxed{|\mathcal T_C(A)|=n^2-\sum_jc_j^2+W.}
\tag{SC}
\]
If \(C+a=\gamma_j u_a^2\) on \(B_j\), with positive \(\gamma_j,u_a\in K\), and
\(U_j=\{\pm u_a:a\in B_j\}\), then
\[
\boxed{\mathcal T_C(A)\cap K=\bigcup_j\gamma_jQ(U_j,U_j).}
\tag{ROOT}
\]
Here \(|U_j|=2|B_j|\), and the actual lifted component is
\(\sqrt{\gamma_j/d_C}\,U_j\). The factor \(\sqrt{\gamma_j}\) cannot be dropped.

A parameter of degree at least three over \(F=\mathbb Q(A)\), or transcendental over \(F\), gives all \(n(n+1)\) outputs. A genuinely quadratic parameter gives at least \(n^2+1\). Therefore
\[
|\mathcal T_C(A)|\le n^2\implies C\in F.
\tag{FIELD}
\]
More precisely, for minimal polynomial \(X^2+uX+v\), put
\(A^\dagger=A-u/2\), \(R_0=3(u^2-4v)/16\). If \(r_0\) is its unordered \(R_0\)-fiber size, the image size is \(n(n+1)-(r_0-1)_+\), and \(r_0\le n\). Do not assume an additional, unproved shifted legality condition.

**PROVED — exact collision equation.** For distinct unordered old pairs with sums/products \((s,p),(t,q)\), write \(D=s-t,E=p-q\). If \(D=0\), there is no collision; otherwise a collision parameter satisfies
\[
-3D^2C^2+[2DE-2D^2(s+t)]C+E^2-2D^2(p+q)+D^4=0.
\tag{CP}
\]
Each legal root realizes one sign pair. This supplies the finite optimizer algorithm.

**PROVED — imported field nesting.** For actual inputs containing \(\pm1\),
\(\mathbb Q(A,C)\subseteq\mathbb Q(\mathcal L_C(A))\).
Indeed \(x_1^2-x_{-1}^2=2/d_C\) recovers \(d_C\); the new maximum recovers \(C,M\); then \(a=d_Cx_a^2-C\). The successor extension over \(K_m\) is exactly the multiquadratic extension of the displayed normalized roots.

**PROVED — exact \(m=3,C=3\) ledger.** Shifted classes are
\[
\{\pm1,\pm\sqrt5\},\quad\{\pm\sqrt3\},\quad\{\pm\sqrt7\},
\quad\text{eight separate labels }\pm\alpha,\pm\beta,\pm g,\pm h.
\]
Thus \(b_3=1/4\), \(\sum c_j^2=32\), \(W=17+6+6+16=45\), and
\(224+45=269\). The sole nonsingleton output component has four labels at value \(4\), giving rank three.

**PROVED — exact cross-fiber forest capacity.** If \(r_0\) is the old fiber size at \(3C^2/4\), the maximum rank joining branches of different old norms is
\[
\mathfrak F_C=n+\sum_jc_j^2-W-(r_0-1)_+.
\]
Since \(W\ge n+1\), this is at most \(\sum c_j^2-1\le n\max c_j-1\). One old-fiber transfer gives only \(O(n)\) rank.

### 4.3 Latest cycle: finite root covers and exact affine failures

**PROVED — current exact arithmetic, independently checked.**
Below \(R=\gamma Q(U,U)\), \(S_m=Q(\mathcal A_m,\mathcal A_m)\).

| Input | Legal \(C\) | Largest class \(B\) | \(|B|\) | Exceptions | \(|R|\) | Outcome |
|---|---|---|---:|---:|---:|---|
| \(\mathcal A_1\) | \(5/2\) | \(\{-2,2\}\) | 2 | 2 | 6 | Two affine copies |
| \(\mathcal A_1\) | \(3\) | \(\{-2,1\}\) | 2 | 2 | 5 | Identity copy |
| \(\mathcal A_1\) | \(17/8\) | \(\{-2,-1,1\}\) | 3 | 1 | 12 | Exactly four affine copies |
| \(\mathcal A_2\) | \(4\) | \(\{-3,-1,3\}\) | 3 | 5 | 11 | Identity copy |
| \(\mathcal A_2\) | \(6\) | \(\{-3,1,3\}\) | 3 | 5 | 11 | Identity copy |
| \(\mathcal A_3\) | \(3\) | \(\{\pm1,\pm\sqrt5\}\) | 4 | 12 | 17 | Exactly five affine copies |
| \(\mathcal A_3\) | \(4\) | \(\{\pm1,\pm\sqrt3,\pm\sqrt7\}\) | 6 | 10 | 41 | Identity copy |

These are parameter-specific statements, not a disproof of eventual TCRC.

**PROVED — explicit early covers.** For \(m=1,C=5/2\),
\[
S_1=\{1,3,4,7,12\},\quad \gamma=1/2,\quad U=\{\pm1,\pm3\},
\]
\[
R=\tfrac12\{1,3,7,9,13,27\}
\subseteq(-S_1+15/2)\cup(3S_1-15/2).
\]
The maps hit four and three target values. At \(m=2,C=4\), \(\gamma=1\) and
\(U=\{\pm1,\pm\sqrt3,\pm\sqrt7\}\subset\mathcal A_2\), so the identity map suffices.

**PROVED — affine containment is stronger than the needed cardinality bound.**
At \(m=1,C=17/8\), \(\gamma=1/8\), \(U=\{\pm1,\pm3,\pm5\}\), and
\[
8R=T=\{1,3,7,9,13,19,21,25,27,31,49,75\}.
\]
One, two, and three affine copies of \(S_1\) hit at most \(5,8,11\) elements of \(T\). Four suffice:
\[
T\subseteq(2S_1-5)\cup(6S_1+7)\cup(6S_1+3)\cup\{7\}.
\]
Nevertheless \(|R|=(12/5)|S_1|<3|S_1|\). The full lifted image still has twenty outputs: six outside-field and fourteen inside-field outputs. The exceptional input is not free.

The following exact certificate includes all real affine maps: two distinct rational hits force rational slope/intercept; singleton masks cover maps with at most one hit.

```python
from fractions import Fraction as F
from itertools import permutations
S = [1, 3, 4, 7, 12]
T = [1, 3, 7, 9, 13, 19, 21, 25, 27, 31, 49, 75]
index = {v: i for i, v in enumerate(T)}
masks = set()
for a, b in permutations(T, 2):
    for x, y in permutations(S, 2):
        slope = F(b-a, y-x)
        shift = a-slope*x
        hit = {slope*s+shift for s in S} & set(T)
        masks.add(sum(1 << index[v] for v in hit))
masks.update(1 << i for i in range(len(T)))
pairs = {a | b for a in masks for b in masks}
assert len(masks) == 134 and len(pairs) == 2100
assert max(a.bit_count() for a in masks) == 5
assert max(a.bit_count() for a in pairs) == 8
assert max((a | b).bit_count() for a in pairs for b in masks) == 11
assert set(T) <= ({2*s-5 for s in S} | {6*s+7 for s in S}
                 | {6*s+3 for s in S} | {7})
```

**PROVED — larger finite affine obstruction.** At \(m=3,C=3\),
\[
U=\left\{\pm2,\pm\sqrt2,\pm\frac{\sqrt{10}+\sqrt2}{2},
\pm\frac{\sqrt{10}-\sqrt2}{2}\right\},\quad\gamma=1.
\]
Its seventeen targets lie in \(E=\mathbb Q(\sqrt2,\sqrt5)\). Every map with at least three hits uses old outputs on an affine \(E\)-line in \(F_3\). Exact coefficient enumeration gives six such lines of sizes \(10,4,3,3,3,3\). Matched-pair enumeration on them gives eighty-two hit masks of size at least three; all two-target masks handle the remaining maps. Maximum union coverage with one through five maps is \(7,9,11,14,17\). Five copies are necessary and sufficient. A map with two hits automatically has coefficients in \(F_3\), so unrestricted real coefficients do not evade this certificate. The exact enumeration, line data, and explicit five-map witness are preserved in the supporting record.

**PROVED — concrete \(m=3\) identity cover and its complete ledger.**
For \(C=4\),
\[
B=\{\pm1,\pm\sqrt3,\pm\sqrt7\},\quad\gamma=1,\quad
U=\{\pm\sqrt3,\pm\sqrt5,\pm\alpha,\pm\beta,\pm g,\pm h\}
\subset\mathcal A_3.
\]
Thus \(R\subset S_3\). But there are ten exceptions. The partition is
\((6,1,\ldots,1)\), with ten singletons, \(W=61\), and
\[
|\mathcal T_4(\mathcal A_3)|=256-46+61=271.
\]
Precisely \(16\cdot17-6\cdot7=230\) labels touch exceptions, and \(41+230=271\). The optimizer instead gives \(269\). Root containment without exception control does not improve the full step.

**PROVED — inherited-root cover and its ceiling.** The finite \(C=4\) identity has a general history form. For consecutive actual levels \(A=\mathcal A_{m-1}\), \(A'=\mathcal A_m=\mathcal L_D(A)\), \(D=C_{m-1}\), choose \(\lambda>0\) in the actual field with \(\lambda D>M(A')\), set \(B=A'\cap\lambda A\), and \(\gamma=\lambda(D-M(A))\). For \(a\in B\),
\[
u_a=\sqrt{\frac{D+a/\lambda}{D-M(A)}}\in A',
\quad \lambda D+a=\gamma u_a^2.
\]
Thus \(U=\{\pm u_a:a\in B\}\subset A'\) and
\(\gamma Q(U,U)\subset\gamma Q(A',A')\), one affine output copy. But
\(|B|\le|A|=|A'|/2\). This particular inheritance mechanism necessarily discards at least half the input; it cannot provide the required sublinear exceptions.

### 4.4 Latest cycle: exact history test at the next input

**PROVED — prior-field norm criterion.** Let \(H/F\subset\mathbb R\) be multiquadratic, \(C\in F\), and \(x^2=h,y^2=k\in F^\times\) represent distinct nontrivial classes. If \(C>|x|,|y|\) and \(C+x,C+y\) have the same class in \(H\), then
\[
[C^2-h]\in\{1,[k]\},\qquad[C^2-k]\in\{1,[h]\}
\quad\text{in }F^\times/F^{\times2}.
\tag{HP}
\]
If \(y\in F\), the first quantity must already be square in \(F\).
Indeed square-root descent in \(E=F(x,y)\) writes
\((C+x)(C+y)=e v^2\), \(e\in F^\times,v\in E\). Norm to \(F(y)\) shows that \(C^2-h\) is square there. Its square-root kernel on \(F\) is \(\{1,[k]\}\). This criterion requires \(C\in F\), not just \(C\in H\).

**PROVED — \(m=4,C=4\) comparison obstruction.** Put
\(d_0=3-\sqrt7\), \(h_a=(3+a)/d_0\). Here \(H=F_4\), \(F=F_3\). The candidate \(4\) is legal since \(M_4=(3+\sqrt7)/\sqrt2<4\).
The history buckets of \(\pm\sqrt{h_a}\) have sizes
\[
8,4,4,2,2,2,2,2,2,2,2,
\]
and the bucket from \(a=\pm\sqrt7\) is trivial. Exactly \(140\) degree-64 nonsquare tests show that, for every other parent, \(16-h_a\) and its products with the nine different nontrivial character representatives are nonsquare in \(F_3\). The trivial cases have roots
\[
(3\sqrt2-\sqrt{14})/2,\qquad \sqrt{15}.
\]
By (HP), classes of \(4+\mathcal A_4\) cannot cross history buckets. Hence
\[
c_{\max}\le8,\qquad \sum c_j^2\le128.
\]
The diagonal branches contain \(Z\cup3Z\), \(Z=4+\mathcal A_4>0\), so \(W\ge33\). Therefore
\[
\boxed{|\mathcal T_4(\mathcal A_4)|\ge1024-128+33=929>807=3s_4.}
\]
A single class requires at least twenty-four exceptions. This does not compute \(C_4\), exclude other parameters, or refute finite-stage error terms.

**PROVED — another legal candidate, without a useful cover.**
\[
C_{\rm comp}=\sqrt{\frac6{3-\sqrt7}}
=\frac{\sqrt6}{2}\sqrt{\frac4{3-\sqrt7}}\in F_4
\]
is legal. Complementary quartets merge internally because \(\sqrt2\in F_4\). An explicit four-input class subset gives twenty root outputs, but no dominant class or useful whole-image bound is established. This is a single comparison, not the closed repeated complementary continuation.

### 4.5 Latest cycle: root algebra and pair-template limitation

**PROVED — exact identities.**
If \(C+a=\gamma u^2,C+b=\gamma v^2\), then
\[
Q(a,b)=\gamma^2(u^4+u^2v^2+v^4)-3\gamma C(u^2+v^2)+3C^2.
\]
For \(z_\pm=\gamma Q(u,\pm v)\),
\[
\boxed{(z_+-3C/2)(z_--3C/2)=Q(a,b)-3C^2/4.}
\tag{SP}
\]
For \(h=z-3C/2\ne0\),
\[
a+b=\frac{Q(a,b)-3C^2/4+h^2-Ch}{2h}.
\]
The branch-exchange Möbius map has coefficient \(Q(a,b)-3C^2/4\), depending on the old pair norm; it is not one fixed map of the full old image.

**PROVED — scoped obstruction.** For \(|B|=b\) and a polynomial \(H(X,Y)\) of total degree \(d\), at most \(2\max(d,1)b\) ordered branch labels satisfy \(F_C^\pm(a,b)=H(a,b)\). They are zeros of the nonzero polynomial
\[
(H-2C-X-Y)^2-(C+X)(C+Y).
\]
It is nonzero because a nonconstant linear polynomial cannot be a polynomial square. The elementary grid zero bound is degree times \(b\). Positivity makes the two branch outputs distinct for a fixed pair.

Consequently \(t\) polynomial pair maps of coordinate degree at most \(D\ge1\), followed by affine old-image maps, cover at most \(4Dt b\) labels. Full coverage requires \(b+1\le4Dt\). Three affine-linear pair templates fail once \(b>11\). Rational templates of bounded common-denominator degree have the analogous \((4D+2)t b\) bound on defined pairs. This excludes fixed sign/swap/zero-sum formulas as full certificates, not arbitrary history-dependent assignments to different old pairs.

### 4.6 Latest cycle: zero-sum completion accounting

**PROVED.** For \(U=\pm V\), \(V\subset\mathbb R_{>0}\), \(|V|=r\), let
\(P(V)=|\{(u,v)\in V^2:u+v\in V\}|\).
Identifications generated solely by zero-sum completion partition the \(r(r+1)\) essential labels into
\[
\mathcal B(V)=r(r+1)-P(V)\ge r(r+3)/2
\]
blocks. A nondegenerate completed triangle has three labels; a doubling triangle has two; each label determines its completion. Also \(P(V)\le\sum_{j=1}^r(j-1)\) by ordering positive roots. Equality is attained by \(V=\{a,2a,\ldots,ra\}\), \(a>0\).

This gives an **upper** bound \(|Q(U,U)|\le\mathcal B(V)\). The lower bound on block count is not a lower bound on the actual image. At \(\mathcal A_0,\ldots,\mathcal A_4\), the block counts are \(2,5,20,72,270\), compared with image counts \(2,5,17,68,269\).

For signed roots \(u+v+w=0\), let the corresponding old labels be \(a,b,c\), \(S=a+b+c\). Then
\[
\gamma Q(u,v)=(3C+S)/2,\qquad
Q(a,b)=3S^2/4+CS/2+3C^2/4-Sc.
\]
A triple-sum output is not automatically a function of an old pair norm. \(S=0\) is the already closed single-fiber mechanism. Different completion blocks must still be identified.

### 4.7 Conditional recurrence, exact iteration, and exponent

**CONDITIONAL — TCRC implication, proved.** Suppose for every \(m\ge m_0\) a legal comparison parameter gives a three-copy root-image cover on a class with at most fixed \(L\) exceptions. The exact exceptional label count is
\[
e_m(2n_m-e_m+1)\le L(2n_m+1).
\]
One-step optimizer comparison yields
\[
s_{m+1}\le3s_m+L(2n_m+1).
\tag{REC}
\]
For \(h\ge0\),
\[
s_{m_0+h}\le3^h s_{m_0}
+4L2^{m_0}(3^h-2^h)+\frac L2(3^h-1).
\]
Thus \(s_m=O(3^m)\), with constants depending on \(L,m_0,s_{m_0}\). Every
\(0<c<2-\log_2 3\) follows eventually; a safe conditional choice is
\[
c=\tfrac12\log_2(4/3)\approx0.20751875.
\]

**CONDITIONAL — relaxed recurrence, proved.** Suppose uniformly
\[
e_m\le Hn_m^{1-\delta_e},\qquad
|\gamma_m Q(U_m,U_m)|\le\rho s_m+J n_m^{2-\delta_r},
\]
where \(H,J\ge0\), \(0<\rho<4\), and \(\delta_e,\delta_r>0\) are fixed. With
\(\delta=\min(\delta_e,\delta_r)\),
\[
s_{m+1}\le\rho s_m+(3H+J)n_m^{2-\delta}.
\]
Let \(q=2^{2-\delta}\). The forcing sum over \(h\) steps is
\[
\sum_{j=0}^{h-1}\rho^{h-1-j}q^j
=\frac{\rho^h-q^h}{\rho-q},
\]
or \(h\rho^{h-1}\) when \(\rho=q\). Therefore
\[
s_m=O((m+1)\max\{\rho,2^{2-\delta}\}^m),
\]
and every \(c<\min\{2-\log_2\rho,\delta\}\) works. Strictness absorbs constants and the possible polynomial loss.

**OPEN — missing premise.** No uniform parameter rule, sublinear exception theorem, or \(\rho<4\) root-image bound has been established. No positive exponent in this section is unconditional.


## 5. Construction attempts

Each entry gives the carrier, intended mechanism, required quantitative statement, and outcome. “SURVIVES” means an open possibility, not a positive theorem.

### 5.1 Common-inner benchmark families

**PROVED; outcome: SURVIVES as a solved benchmark, not for \(Q\).** Pull an additive or geometric progression through an injective real branch of \(g\). For a transcendental additive coefficient ratio, a fixed \(k\)-digit box has \(|B|=N^k\) and image at most \(2^{k-1}N^{k+1}\); fix \(k\) before \(N\to\infty\). Algebraic ratios use fixed rational lattices. The common-inner multiplicative family has \(O_P(|A|)\) images. The original report establishes fixed savings for these forms, which exclude \(Q\).

### 5.2 Norm-one actions on number-field boxes

**FAILED for the tested carrier.** For \(K=L(\omega)\), a norm-one element \(r+s\omega\) acts by
\[
(a,b)\mapsto(ra+sb,-sa+(r-s)b).
\]
High-degree arithmetic can produce exponentially many bounded-complexity transformations. The intended carrier was one lattice set \(A\subset L\) with substantial common overlap of \(A^2\) under many matrices. Denominator/integrality indices and the exponentially sparse common stable core defeat that estimate. Exact finite invariance under a non-torsion transformation is impossible. The transformation count does not give an image upper bound.

### 5.3 Full-input norm sieve and CRT boxes

**FAILED for this certificate.** Use integral boxes in totally real fields of degree \(d_j\to\infty\), root discriminant at most fixed \(D\), and local norm restrictions. The historical sufficient criterion required a fixed finite set of rational \(q\equiv2\pmod3\), completely split in every field, and
\[
3D\prod_{q\in S}\frac q{q+1}<1.
\]
The frozen arithmetic inequality gives the product at least \(D^{-1/2}\). Arbitrary decomposition and field-dependent primes within the same packing argument also fail. These are arithmetic-cost obstructions, not universal impossibility for real sets.

### 5.4 Weighted correlated CRT sets

**CONDITIONAL; outcome: SURVIVES only in unresolved regimes.** For a finite factor \(X\), \(|X|=N\), a common rational probability weight \(p\) with
\[
\rho_{\rm loc}=N\sum_t\max_{Q(x,y)=t}p_xp_y<1
\]
would give actual type-class sets \(B_m\subset X^m\). If \(h=-\sum p_x\log p_x\) and the support size is \(s\), at divisible \(m\),
\[
(m+1)^{-s}e^{mh}\le|B_m|\le e^{mh},
\quad
\frac{N^m|Q(B_m,B_m)|}{|B_m|^2}
\le(m+1)^{2s}\rho_{\rm loc}^m.
\]
This is a same-set theorem. No common-weight defect was certified. A defect would additionally need global realization with \(\theta\log(1/\rho_{\rm loc})>\kappa\), where \(m\sim\theta d\) and \(e^{\kappa d}\) is the global cost. The particular depth-one volume model was proved negative; deeper or different global models were not all excluded.

### 5.5 Direct split-divisor-rich integer sets

**PROVED carrier; outcome: FAILED for image saving.** Choose distinct \(q_i\equiv1\pmod3\) recursively, for example from prime divisors of \((3P)^2+3P+1\), where \(P\) is the previous prime product. Let \(A_m\) be least CRT representatives with each coordinate in the three cube roots of unity. Then \(|A_m|=3^m\). At least \(1-e^{-m/18}\) of pairs have at least \(m/2\) selected prime divisors of their norm, giving split-divisor product at least \(2^{m/2}\).

But each local output has four values and factor \(4q_i/9\ge28/9\). The allowed-lift bound \(3M_m4^m\), \(M_m=\prod q_i\), exceeds the trivial \(9^m\). Richness does not ensure enough realized Cartesian fibers. Correlations inside the ternary alphabet do not fix this: its diagonal map \(x\mapsto3x^2\) is injective.

### 5.6 Balanced Eisenstein product code and original CR

**PROVED partial carrier; outcome: original CR FAILED.** For split \(q_i=N\pi_i\equiv1\pmod3\) and inert rational \(r_i\equiv2\pmod3\), use
\[
Z_m=\left\{\prod_{i=1}^m\theta_i:
\theta_i\in\{1,r_i,\pi_i,\bar\pi_i\}\right\}.
\]
Complete the coefficient projections of \(z=a_z-\omega b_z\) to one \(A_m\). There are \(4^m\) distinct engineered pairs and \(3^m\) norm values. A word with \(\ell\) split symbols has exactly \(2^\ell\) realized pairs. Apart from an \(e^{-2\epsilon^2m}\) fraction, \(\ell\ge(1/2-\epsilon)m\).

Only engineered pairs are controlled:
\[
|Q(A_m,A_m)|\le3^m+|A_m|^2-4^m.
\]
CR demanded a near-Cartesian completion after rational norm-one rephasings. It was later disproved by the \(3\)-adic bound \(n^2-4^m\ge n^2/3+2^m\). This does not lower-bound the actual full image of every completion.

**FAILED — distinct cyclic-orbit and full-exponent-box variants.** These failures precede and differ from the later complementary radical continuation.

For non-torsion \(u\in\mathbb Q(\omega)\) of norm one, finite \(C\subset\mathbb Q_{>0}\), and \(K\subset\mathbb Z_{>0}\), use \(Z(C,K)=\{cu^{\pm k}:c\in C,k\in K\}\). Its coefficient completion obeys
\[
|A|\ge\sqrt2\,|K|\sqrt{|C|},\qquad |Z(C,K)|/|A|^2\le1/|K|.
\]
Thus long prescribed norm-one/Chebyshev orbits lose their engineered density. Unrelated cross-pair coincidences are not excluded.

For
\[
Z_{m,h}=\left\{\prod_i\pi_i^{e_i}\bar\pi_i^{f_i}:0\le e_i,f_i\le h\right\},
\]
one has \(|Z|=(h+1)^{2m}\), \(|N(Z)|=(2h+1)^m\), coefficient count at least \((2h+1)^m\), and engineered density at most
\(((h+1)/(2h+1))^{2m}\).

A separate optimistic one-prime invariant-ellipse relaxation yields the multiplier \(9\pi/(8\sqrt{15})=0.912550\ldots<1\). This is only a fractional, one-prime, all-rotations-invariant calculation; it is not a universal no-go for correlated finite windows.

### 5.7 Parity-twisted Cartesianization, PTCR

**PROVED structural modification; outcome: approximate PTCR SURVIVES.** Multiply a word by \(1-\omega\), norm \(3\), when its split-symbol count is even. It changes the obstructed local pattern while preserving \(4^m\) words, \(3^m\) values, and fiber multiplicities.

The remaining requirement is a common rational coefficient set of size \(n\), with injective rephased engineered pairs and
\[
n^2-4^m\le n^{2-\xi},\qquad \xi>0\text{ fixed}.
\]
This would give every \(c<\min(2-\log_2 3,\xi)\). Exact PTCR, \(n=2^m\), is false for every \(m\ge2\), but approximate PTCR remains open.

The \(m=1\) gadget is \(A=\{1,2\}\), table values \(3,7,7,12\). For \(m=2\), markers \(r=(2,5)\), \(q=(7,31)\), the carrier
\[
A=\{-25,-10,-5,-2,-1,26\}
\]
has sixteen engineered cells, nine engineered values, twenty missing cells, and full image nineteen. Its six-point integral minimality is a scoped result. Repeating this imperfect block gives density \((4/9)^j\), not a power-deficit carrier.

### 5.8 Global repacking, DCRC, and mixed-difference coherence

**PROVED combinatorial results; outcome: arithmetic realization OPEN.** The abstract star carrier \(\mathbb F_2^m\cup\{\infty\}\) has \(n=2^m+1\), \(4^m\) engineered cells, and deficit \(2^{m+1}+1\), while preserving code multiplicities and inert cube shadows. It is not a real \(Q\)-table. Formal DCRC with unrestricted complete rebuilding is equivalent to the corresponding progression-PTCR, not a weaker solved recurrence.

A necessary table identity is
\[
\Delta_{11}\Delta_{22}=\Delta_{12}\Delta_{21},
\quad
\Delta_{uv}=M_{x_uy_v}-M_{x_uy_0}-M_{x_0y_v}+M_{x_0y_0}.
\]
For a partial symmetric table over a field of characteristic different from two, with \(d_{\rm miss}\) holes and \(B_{\rm bad}\) violating ordered rectangles, the proved stability theorem gives a potential-product approximation
\(c_i+c_j+\lambda a_i a_j\) within
\[
15n^2\sqrt{B_{\rm bad}/n^6+9d_{\rm miss}/n^2}
\]
edits, with parameters in the same field. Such a table still requires quadratic calibration. Specified-prime MDCO obstructions do not settle arbitrary-prime PTCR.

### 5.9 Direct geometric and radical families

**PROVED; geometric outcome: FAILED for power saving.**
\[
G_k=\{\pm2^j:0\le j<k\},\qquad |G_k|=2k,\qquad
|Q(G_k,G_k)|=k^2+1.
\]
Its exact doubling recurrence is \(s_{2k}=4s_k-3\), preserving positive quadratic density.

**OPEN; adaptive radical outcome: SURVIVES.** RAD changes the actual field and abandons the prescribed code. It doubles set size exactly and has the certified finite values in Section 4. No uniform image-growth saving is proved.

**FAILED; repeated complementary continuation only.** Put \(\kappa=4\arctan(1/2)\), \(N=4\cdot2^h\), and
\[
B_N=\left\{\frac{\cos((2\pi j-\kappa)/N)}{\sin(\kappa/N)}:0\le j<N\right\},
\quad C_N=\csc(\kappa/N).
\]
Then \(|B_N|=N\), \(B_4=\{\pm1,\pm2\}\), and the legal complementary lift gives \(B_{2N}\). Exactly two equal square classes persist, and
\(|Q(B_N,B_N)|\ge N^2/8\) for \(N\ge8\).
This is not the optimizing family.

### 5.10 Dominant square classes and current root covers

**FAILED as a sufficient condition by itself.** The explicit rational construction
\[
t_i=10000^{-5^{i-1}},\quad
u_i=\frac{1-2t_i-t_i^2}{1+t_i^2},\quad
v_i=\frac{1+2t_i-t_i^2}{1+t_i^2},
\]
\[
A_\ell=\{u_i^2-1,v_i^2-1:1\le i\le\ell\},\quad C=1
\]
is symmetric, has \(n=2\ell\), \(M<1\), and every shifted input square in \(\mathbb Q\). Yet all \(n(n+1)\) branch outputs are distinct. This is an auxiliary family, not the optimizer.

**OPEN; current outcome: CONDITIONAL.** TCRC asks for a legal in-field parameter on every sufficiently large actual input, one class with bounded exceptions, and three affine output maps with coefficients in \(F_m\). The maps may vary with \(m\), but are fixed across every pair at that level. The latest finite tests show both genuine covers and precise failures. They support changing the certificate to a direct cardinality bound, but establish no uniform continuation rule.

## 6. Failed / closed routes

Every row is a scoped failure, not a disproof of TARGET.

| Route; status FAILED | Obstruction and type | Exact scope and possible change of hypothesis |
|---|---|---|
| Intervals / ordinary fixed-dimensional digits | No fixed saving for \(Q\); scalar cross terms | Does not exclude other growing algebraic carriers |
| Separate \(A+A\) and \(AA\) bounds | No direct mixed-polynomial image estimate | A genuinely joint image identity is needed |
| Norm-one common-box invariance | Denominator indices, sparse common core, no non-torsion finite invariance | Non-invariant directly counted fibers remain outside the result |
| Fixed complete-splitting sieve | \(\prod q/(q+1)\ge D^{-1/2}\) defeats \(3D\)-criterion | Universal for that criterion, including improved towers or recursive cutting |
| Arbitrary decomposition full-input sieve | \(\liminf\delta_j^{1/d_j}\ge1/(2\sqrt D)\) | Includes ramification, order, depth; same certificate only |
| Field-dependent prime packing | Bounded modulus entropy constrained; unbounded entropy has gain/cost \(\to0\) | Needs a different realization certificate |
| Good split one-place Cartesian restrictions | \(R^k|Q(B,B)|\ge|B|^2\) | All depths, same-set; not automatic correlated CRT tensorization |
| Inert / odd singular Cartesian restrictions | Factors at least \(R/(R+1)\), \(R/[2(R+1)]\) | No depth-dependent gain in these rings |
| Ordinary tensorization inference | Abstract constants can be \((8/9)^{\lfloor t/2\rfloor}\) | Not a counterexample for \(Q\); weighted tensorization differs |
| Weighted defects over residues \(7,13\) | \(\tau=1\) at every depth | Other residues/multilevel weights remain open |
| Optimistic depth-one weighted global ledger | \(\epsilon_{\rm vol}<\log(8/(3e))<0\) | Not all deep prime powers or non-volume realizations |
| Polynomial-height fixed-field sets | Image \(n^{2-o(1)}\) from ideal-divisor bound | Height/house and fixed-field hypotheses essential |
| Ternary split-divisor CRT sets | Normalized factors \(4q_i/9>1\) | Richness is not sufficient Cartesian compression |
| Original un-twisted CR | \(n^2-4^m\ge n^2/3+2^m\) under rational rephasing | Norm-3 parity twist changes the obstructed hypothesis |
| Exact PTCR | Full \(n=2^m\) tables impossible for \(m\ge2\) | Approximate fixed power deficit remains open |
| Imperfect block repetition | Density \((e/h^2)^j\); six-point case \((4/9)^j\) | Complete repacking is a different mechanism |
| Natural / endpoint-local placement | Macroscopic deletions or affine rule \(e\le n^2/2+n\) | Arbitrary nonlinear cell permutation not excluded |
| Scalar digit Cartesianization | Product-algebra coordinatewise \(Q\) does not become scalar \(Q\) | Would need a new exact scalar identity |
| Core-faithful six-point lifts | \(n_{\rm next}\ge4n\), deficit \(\ge16d_{\rm miss}\) | Does not exclude global rebuilding |
| \(O(\sqrt M)\)-label fiber repair | \(M\) directed equal-norm edges need at least \(M/2\) labels | Proposed cheap repair is invalid |
| Code-independent mixed-difference reconstruction | \((i+j)^2\) is coherent but far from every \(Q\)-table | Potential-product structure needs quadratic calibration |
| Deficit recurrence with coefficient \(4\) | Retains early normalized defect | Coefficient strictly below \(4\) with size control would suffice |
| Repeated complementary radicals | Image at least \(N^2/8\) | Particular nonoptimizing family only |
| Dominant class alone | \(b=1\) can coexist with maximal \(n(n+1)\) image | Must also compress the within-class root image |
| Outside-input-field parameters | At least \(n^2+1\), or maximal image | In-field parameters remain open |
| Bounded-degree same-pair cover rules | At most \(4Dt b\) labels | Arbitrary history-dependent cross-pair assignment remains open |
| Triangle completion alone | At least \(r(r+3)/2\) completion blocks | Blocks can still collide; this is not an image lower bound |
| Three-affine cover at tested parameters | Four or five maps are necessary | Eventual TCRC can choose other parameters |
| Repeating \(C=4\) at \(\mathcal A_4\) | At least \(929>3s_4\), largest class at most eight | Does not determine \(C_4\) or rule out finite-error recurrences |

### Quantitative scopes retained from the earlier proofs

**PROVED — global ideal bound.** For \(A\subset\mathcal O_L\), \(L\) totally real, \(K=L(\omega)\), \(t\ne0\),
\[
r_A(t)\le w_{K/L}
\prod_{\substack{\mathfrak p\mid(t)\\\mathfrak p\ {\rm split}}}
(v_{\mathfrak p}(t)+1).
\]
Here \(w_{K/L}\) counts relative norm-one integral units and must be charged. If the image is at most \(n^{2-c}\), at least \(n^2/2\) pairs belong to fibers of size at least \(n^c/2\), and their divisor product is at least \(n^c/(2w_{K/L})\). The argument counts possible ideals by an upper bound, so does not assume a favorable class number. Polynomial-height integer sets, rational sets after polynomial-height common-denominator scaling, and polynomial-house integral sets in one fixed totally real field are excluded. Arbitrary rational sets are not excluded.

**PROVED — decomposition ledger.** Away from \(3\), residue size \(R\equiv1\pmod3\) is split, with full-input density one; \(R\equiv2\pmod3\) is unramified quadratic, with depth-\(k\) density
\[
\frac{R+R^{-2\lfloor k/2\rfloor}}{R+1}.
\]
Only odd residue degree above rational \(q\equiv2\pmod3\) contributes this saving. The ratio of gain \(\log(1+1/R)\) to arithmetic weight \(\log R/(R-1)\) decreases with \(R\). Complete splitting was already optimal per unit cost for that mechanism. The odd/singular Cartesian bound is at least \(R/[2(R+1)]\ge3/8\); the maximal tame ramified case has the stronger \(1/2\) bound.

**PROVED — variable-prime ledger.** Put
\(H_j=d_j^{-1}\log N\mathfrak m_j\) and
\(G_j=-d_j^{-1}\log\delta_j\).
Bounded \(H_j\) remains constrained by the basic inequality. If \(H_j\to\infty\), then \(G_j/H_j\to0\), and the standard packing exponent is at most
\(2G_j/(H_j-G_j)\to0\), when this expression is relevant and positive.

**PROVED — weighted scope.**
\[
\tau(f)=\inf_{\alpha,\beta\ge0}
\frac{|X|\sum_z\max_{f(x,y)=z}\alpha_x\beta_y}
{(\sum\alpha)(\sum\beta)}
\]
uses nonzero weight sums, and \(\tau(f\otimes g)=\tau(f)\tau(g)\). General good split prime powers retain
\[
\frac{R}{R+k(R-1)}\le\tau(Q;\mathcal R_k)\le1.
\]
Residue \(7\) and residue \(13\) are settled at every depth. Correlated split-field products with at most one factor having \(3\) square, and arbitrary ideal-membership-bit correlations, also have constant one. No general common-weight defect or all-ring \(\tau=1\) theorem is recorded.

**PROVED — prescribed-prime MDCO, not arbitrary primes.** With \(r_1=5\), later \(r_j\equiv11\pmod{15}\), and \(q_j\equiv1\pmod{15}\), \(m\ge2\), deficit at most \(10^{-16}n^2\) forces more than \(10^{-16}n^6\) violating rectangles. Another theorem uses two inert markers and
\[
W=3\prod q\prod r_{\rm other}^2,\quad
r^2,s^2>2W,\quad(r^2-2W)(s^2-2W)>4W^2,
\]
and obtains \((4^{-6}-o(1))n^6\) violations when deficit is \(o(n^2)\).
A fixed \(m=3\) star placement with \(r=(2,5,17)\), \(q=(7,31,307)\) is also obstructed. None settles arbitrary prime cancellation.

**EXPERIMENTAL discovery with an exact finite witness.** At the fixed \(m=3\) star domain, a 200000-step heuristic search found a placement with nineteen of 1120 coherent unordered complete rectangles. This is a verified witness, not an optimum or an MDCO counterexample. At \(m=2\), the star domain has no complete \(3\times3\) rectangle; its coherence fraction is \(0/0\), not one.

**PROVED — additional composition restrictions.** Inert cube shadows force
\(2^{m-|S|}\le|X_S|\le\sqrt{4^{m-|S|}+d_{\rm miss}}\).
For \(n_{\rm next}=2n+s\), exactly
\(d_{{\rm miss},{\rm next}}=4d_{\rm miss}+4ns+s^2\).
Near-perfect rational carriers with \(d_{\rm miss}<n^2/3\) have at least \(n-d_{\rm miss}/n\) integral labels. A two-residue reverse-CRT model incurs deficit at least \(c_0^2 4^m/(32m^2)\), with the natural-placement constant \(c_0\); its numerical value is `UNKNOWN FROM CURRENT THREAD RECORD` in this export.

**PROVED — calibration obstruction.** The coherent symmetric table \((i+j)^2\) agrees with any \(Q(b_i,b_j)\) on at most
\(\frac n2(1+\sqrt{8n-7})=\sqrt2\,n^{3/2}+O(n)\) cells.
For nonconstant \(a_i\), \(\lambda\ne0\), the potential-product table
\(c_i+c_j+\lambda a_i a_j\) is exactly \(Q(b_i,b_j)\) iff
\[
\lambda>0,\quad s^2=\lambda,\quad
c_i=\lambda a_i^2+3st a_i+\tfrac32t^2,\quad b_i=sa_i+t
\]
for common real \(s,t\). Rational realization and distinct labels require their own checks.

## 7. Open lemmas

Historical open entries are preserved. **Only T03-O4 is selected as the next constructive obligation.**

| ID; status OPEN | Exact statement | Dependencies and evidence |
|---|---|---|
| T03-O1 | TARGET, Section 2 | No arbitrary-real construction or counterexample |
| T03-O2 | ARG: \(s_m\le K\rho^m\), fixed \(\rho<4\) on actual adaptive levels | Finite counts alone give no rate |
| T03-O3 | Eventual TCRC: in-field legal parameter, bounded exceptions, one shifted class, three affine maps over \(F_m\), allowed to vary with \(m\) but fixed across pairs | Finite failures do not refute the eventual existential statement |
| T03-O4, selected | RC15/4 below | Weaker than TCRC; sufficient for TARGET; thresholds are proposed, not observed rates |
| T03-O5, historical | General BW-Q or a common-weight defect outside settled residues | Weighted tensorization exists; global cost remains separate |
| T03-O6, historical | Approximate PTCR with fixed \(\xi>0\), infinitely many levels | Original CR and exact PTCR are false, approximate PTCR open |
| T03-O7, historical | For every fixed \(\xi>0\) and sufficiently large \(m\), every admissible arbitrary-prime code placement with deficit \(\le n^{2-\xi}\) has at least one complete MD2 violation | Specified-prime results do not settle all cancellations |
| T03-O8, historical | Uniform full-progression DSCR / ARDC inequalities, stated below | Isolated steps and alternate descendants do not support iteration |

**OPEN — inherited progression formulations, retained for precision.** ARDC seeks fixed \(k\ge1\), \(0<\theta<1\) with \(p_{m+k}\le\theta p_m\) on a full progression of sufficiently large actual levels. For the corrected DSCR sufficient formulation, put \(u_m=1-b_m\). Seek fixed \(k,\lambda,H,J,a,\delta,\varepsilon\), with \(0<\lambda<1\), \(a,\delta>0\), \(0<\varepsilon<4^k\), \(H,J\ge0\), such that
\[
u_{m+k}\le\lambda u_m+Hn_m^{-a},\qquad
W_{m+k}\le(4^k-\varepsilon)W_m+Jn_m^{2-\delta}.
\]
Writing \(\mu=1-\varepsilon/4^k\), the proved conditional decay exponent is
\(\min(-\log_2\lambda/k,a,-\log_2\mu/k,\delta)\), with strict exponent loss to absorb constants. The previously proposed DSCR parameters were \(\lambda=e^{-\eta k}\), \(a=1+\eta\). These hypotheses are not known on the required actual progression. They are historical open obligations, not additional selected next tasks.

**OPEN — T03-O4, relaxed actual-root lemma.** There exist fixed \(H<\infty,m_0\) such that for every \(m\ge m_0\) one can explicitly choose
\[
C_m^\dagger\in F_m,\quad C_m^\dagger>M_m,\quad
B_m\subset\mathcal A_m,\quad n_m-|B_m|\le H\sqrt{n_m},
\]
and positive \(\gamma_m,u_a\in F_m\), \(C_m^\dagger+a=\gamma_m u_a^2\), such that for \(U_m=\{\pm u_a:a\in B_m\}\),
\[
\boxed{|\gamma_mQ(U_m,U_m)|\le \frac{15}{4}s_m+Hn_m^{3/2}.}
\tag{RC15/4}
\]
This is a direct bound for the whole signed root image, without requiring affine copies. It cannot be replaced by an energy estimate. No such rule is known here.

**CONDITIONAL — precise consequence.**
\[
s_{m+1}\le\frac{15}{4}s_m+4Hn_m^{3/2}.
\]
Since \(2^{3/2}<15/4<4\), this gives \(s_m=O((15/4)^m)\). Every
\(c<\log_2(16/15)\) works; a safe conditional value is
\[
\boxed{c=\tfrac12\log_2(16/15)\approx0.0465547.}
\]
The constants \(15/4\), \(1/2\) make the unresolved obligation explicit. They are not claimed optimal or empirically established.

