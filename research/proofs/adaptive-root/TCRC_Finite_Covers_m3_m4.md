# Exact finite root-cover experiments at the third and fourth certified inputs

All arguments and computations here are offline. The already certified adaptive sets and degree-64 field basis are used as frozen input. There is no claim concerning the optimizing parameter after the fourth input.

## 1. Main finite conclusions

At the actual optimizing pair \((\mathcal A_3,C_3)=(\mathcal A_3,3)\), the largest input square class has four elements. Its 17-element root image requires **exactly five** affine copies of the old 68-element image. Thus the three-affine-cover assertion fails at this particular certified optimizer. This is not a disproof of an eventual TCRC statement, which permits different comparison parameters.

The simple legal comparison parameter \(C=4\) has a larger six-element square class and admits an exact **one-copy inherited-root cover**. It has ten exceptional inputs. Its full next branch image has 271 elements, compared with the optimizer's 269. These finite exceptional counts do not imply a uniform asymptotic statement.

At \(\mathcal A_4\), an explicit legal in-field complementary parameter and an explicit four-input square-class subset are available. This subset has 20 distinct branch values and gives no compression by itself. No full square-class partition at that fourth-level parameter is asserted.

## 2. The exact input field and old image

Write
\[
p=\sqrt2,\quad q=\sqrt5,\quad r=\sqrt3,\quad v=\sqrt7,
\]
\[
\alpha=\sqrt{4+\sqrt3},\quad\beta=\sqrt{4-\sqrt3},
\quad g=\sqrt{4+\sqrt7},\quad h=\sqrt{4-\sqrt7}.
\]
The frozen exact input is
\[
A=\mathcal A_3=\{\pm1,\pm r,\pm q,\pm v,
\pm\alpha,\pm\beta,\pm g,\pm h\}.
\]
Its field is exactly
\[
K=\mathbb Q(\sqrt2,\sqrt3,\sqrt5,\sqrt7,\sqrt{13},\alpha),
\qquad [K:\mathbb Q]=64.
\]
Its old image \(S=Q(A,A)\) has 68 elements. The field basis consists of
\[
(\sqrt2)^{e_1}(\sqrt3)^{e_2}(\sqrt5)^{e_3}
(\sqrt7)^{e_4}(\sqrt{13})^{e_5}\alpha^{e_6},
\qquad e_i\in\{0,1\},
\]
with \(\alpha^2=4+\sqrt3\). The relations
\[
\beta=\frac{\sqrt{13}(4-\sqrt3)\alpha}{13},\quad
 g=\frac{\sqrt{14}+\sqrt2}{2},\quad
 h=\frac{\sqrt{14}-\sqrt2}{2}
\]
provide all input coordinates in this basis.

The only field fact assumed here beyond the frozen certificate is the elementary basis theorem: a finite extension is a vector space over every intermediate field, and multiplication by a nonzero field element is invertible. All finite computations below use rational coefficients in the displayed basis.

## 3. The optimizing parameter \(C=3\): exact root image

The frozen square-class partition of \(3+A\) has sizes
\[
(4,2,2,1,1,1,1,1,1,1,1).
\]
The largest class is
\[
B=\{\pm1,\pm\sqrt5\},\qquad \gamma=1,
\]
with signed root set
\[
U=\left\{\pm2,\;\pm\sqrt2,
\;\pm\frac{\sqrt{10}+\sqrt2}{2},
\;\pm\frac{\sqrt{10}-\sqrt2}{2}\right\}.
\]
All eight roots belong to the actual field \(K\). Direct expansion gives
\[
\begin{aligned}
R:=Q(U,U)
={}&\{2,4,6,8,12\}\\
&\cup\{3\pm q,\;9\pm3q,\;6\pm2q,\;6\pm2p\}\\
&\cup\{7+q\pm(pq+p),\;7-q\pm(pq-p)\}.
\end{aligned}
\]
These are 17 distinct elements, by coefficient comparison in
\(E=\mathbb Q(p,q)\), whose basis is \(1,p,q,pq\).

### 3.1 An explicit five-copy cover

The following affine maps, all with coefficients in \(E\subset K\), cover \(R\):
\[
\begin{aligned}
\ell_1(t)&=-3t+27,\\
\ell_2(t)&=(p-q)t+7-6p+6q-pq,\\
\ell_3(t)&=\left(-2-\frac p2-q-\frac{pq}{2}\right)t
 +13+\frac{5p}{2}+4q+\frac{5pq}{2},\\
\ell_4(t)&=\frac{-1-p+q-pq}{2}\,t
 +\frac{17+p-5q+5pq}{2},\\
\ell_5(t)&=-2t+18.
\end{aligned}
\]
In fact, only the old source values
\[
\{3,5,7,6+q,6-q\}\subset S
\]
are needed. Their membership is explicit:
\(3=Q(1,1)\), \(5=Q(q,-q)\), \(7=Q(v,-v)\), and
\(6\pm q=Q(1,\pm q)\).

| Map | Source values used | Corresponding outputs, in that order |
|---|---|---|
| \(\ell_1\) | \(7,5,6+q,6-q\) | \(6,12,9-3q,9+3q\) |
| \(\ell_2\) | \(7,5,6+q\) | \(7+p-q-pq,7-p+q-pq,2\) |
| \(\ell_3\) | \(3,5,6-q\) | \(7+p+q+pq,3-q,6+2p\) |
| \(\ell_4\) | \(3,6-q,5\) | \(7-p-q+pq,3+q,6-2p\) |
| \(\ell_5\) | \(7,5,3,6+q,6-q\) | \(4,8,12,6-2q,6+2q\) |

The table is verified by multiplication and collection in the basis
\(1,p,q,pq\). It lists all 17 target values; 12 occurs twice. Therefore
\[
R\subseteq\bigcup_{i=1}^5\ell_i(S).
\]

### 3.2 Why three copies, or even four, do not suffice

This is an exact finite exhaustive result, with a small algebraic reduction that makes the enumeration complete.

**Affine-line reduction.** Let \(E\subset K\) be fields and \(R\subset E\). If an affine map \(x\mapsto ax+b\), with \(a\ne0\), sends three distinct source points of \(S\subset K\) into \(R\), those three source points belong to one affine \(E\)-line in \(K\), viewed as a vector space over \(E\):
\[
S\cap(s_0+Ed),\qquad d\ne0.
\]
Indeed, all their differences become elements of \(E\) after multiplication by \(a\), so their ratios of differences belong to \(E\). Conversely, on such a line, write \(s=z+dc\), \(c\in E\). Its intersections with a target \(R\subset E\) are exactly the intersections arising from affine maps \(c\mapsto Ac+B\) with \(A,B\in E\). Once two source coordinates and two distinct target values are matched, \(A,B\) are uniquely determined. Thus enumerating rich source lines and two-point matches considers every affine map having at least three target hits. Maps with at most two hits are covered by allowing every two-element target subset. Constant maps cause no difficulty.

For the present \(S\), rational-coefficient linear algebra in the frozen degree-64 basis gives exactly six affine \(E\)-lines containing at least three source points:

| Direction \(d\) | Intercept \(z\) | Coordinate set \(T\subset E\), with line points \(z+dT\) |
|---|---|---|
| \(1\) | \(0\) | \(\{1,3,5,7,9,11,15,21,6-q,6+q\}\) |
| \(1-v\) | \(9v\) | \(\{8,9,12\}\) |
| \(1+v/2\) | \(-3v\) | \(\{4,8,12\}\) |
| \(1+v\) | \(-9v\) | \(\{8,9,12\}\) |
| \(1-v/2\) | \(3v\) | \(\{4,8,12\}\) |
| \(v\) | \(12\) | \(\{-q,q,-3,3\}\) |

To certify completeness, generate all \(\binom{68}{2}\) source differences. View each difference as a vector over \(E\), divide by its first nonzero \(E\)-coordinate, and subtract its resulting direction times the corresponding coordinate of the source point. Equal normalized direction/intercept pairs are exactly equal affine lines. Counting their source endpoints yields line sizes
\[
10,4,3,3,3,3
\]
for the lines with at least three points. Every other source line has two points.

For each row \(T\) in the table, take every unordered pair of distinct coordinates \(c_1,c_2\in T\), every pair of target values \(r_1,r_2\in R\), and both assignments of those target values. Form exactly
\[
A=\frac{r_2-r_1}{c_2-c_1},\qquad B=r_1-Ac_1,
\]
and collect the hit set \((AT+B)\cap R\). All arithmetic now lies in the four-dimensional field \(E\). This yields **82 distinct hit sets of size at least three**. Adjoin every two-element subset of the 17-element target. Removing hit sets contained in other hit sets leaves 94 maximal masks. Exhaustive union enumeration gives:

| Number of affine copies | Largest possible number of covered target values |
|---:|---:|
| 1 | 7 |
| 2 | 9 |
| 3 | 11 |
| 4 | 14 |
| 5 | 17 |

Each entry is both an upper and a lower bound: all candidate hit sets are enumerated, and the maximizing masks are realizable by the two-point construction. In particular,
\[
\min\left\{j:R\subseteq\bigcup_{i=1}^j(a_iS+b_i),\ a_i,b_i\in K\right\}=5.
\]
The result even allows arbitrary real affine coefficients: any affine map hitting two distinct algebraic source and target points necessarily has its coefficients in \(K\).

The exact certificate files are:

- `output/tcrc_m3_affine_exact.py`: complete source-line enumeration, exact two-point matching, and three-copy union test;
- `output/tcrc_m3_min_cover.py`: exhaustive minimum-cover computation;
- `output/tcrc_m3_affine_exact_results.json`: complete line table, 82 rich hit masks, and verified five-copy witness;
- `output/tcrc_m3_exact_full_data.pkl`: exact intermediate field objects.

The scripts use the frozen rational-arithmetic field implementation in `ardc_a3_exact_certificate.py` and its recursively exact inversion routine in `ardc_a3_squareclass_certificate.py`. The initial data definitions come from the prefix of `tcrc_m3_cover_search.py`; the exhaustive proof scripts perform no floating-point equality tests. A separate floating-point discovery run was not used for any completeness or impossibility claim.

## 4. The comparison parameter \(C=4\): exact one-copy cover

Here \(4>M(A)=\sqrt7\), and \(4\in\mathbb Q\subset K\). The exact square-class partition of \(4+A\) is
\[
(6,1,1,1,1,1,1,1,1,1,1).
\]
Its six-element class is
\[
B^\dagger=\{\pm1,\pm\sqrt3,\pm\sqrt7\},\qquad\gamma=1.
\]
The relevant roots are
\[
U^\dagger=\{\pm\sqrt3,\pm\sqrt5,\pm\alpha,
\pm\beta,\pm g,\pm h\}
=A\setminus\{\pm1,\pm\sqrt7\}.
\]
Each identity follows directly by squaring. Hence
\[
Q(U^\dagger,U^\dagger)\subseteq Q(A,A)=S,
\]
with the single affine map \(\ell(t)=t\). Exact multiplication in the frozen basis gives
\[
|U^\dagger|=12,\qquad |Q(U^\dagger,U^\dagger)|=41.
\]
There are ten exceptional old inputs, rather than twelve at \(C=3\). The 42 branch labels inside the six-element class give 41 outputs. Each of the ten singleton classes gives its two diagonal outputs. All 61 within-field outputs are distinct except for that one identification. By the frozen square-class localization identity,
\[
|\mathcal T_4(A)|
=256-(6^2+10)+61=271.
\]
Equivalently, the exact exceptional-label count is
\[
16\cdot17-6\cdot7=230,
\]
and \(41+230=271\). Thus this comparison parameter realizes a clean exact root inheritance cover but does not beat the actual optimizer's image size 269.

The class partition uses the same exhaustive square test in the actual degree-64 field as the frozen earlier ledger; no field extension is silently inserted. Its positive square roots are displayed above. The remaining 10 labels are singleton classes in that field.

### 4.1 What the inherited-root identity does, and what it does not do

This one-copy identity comes from
\[
B^\dagger=\mathcal A_3\cap\mathcal A_2
\]
and the previous normalized lift parameter \(C_2=4\), whose denominator is one. More generally, if \(A'=\mathcal L_C(A)\), \(d=C-M(A)\), and a subsequent legal comparison parameter is \(\lambda C\), then
\[
B=A'\cap\lambda A,
\quad \gamma=\lambda d
\quad\Longrightarrow\quad
\gamma Q(U,U)\subseteq\gamma Q(A',A'),
\]
where \(u_a=\sqrt{(C+a/\lambda)/d}\in A'\) and both signs are included.
This is an exact sufficient inherited-root construction, for positive \(\lambda\in\mathbb Q(A')\) and legal \(\lambda C>M(A')\). But
\[
|B|\le |A|=|A'|/2.
\]
A single direct parent intersection therefore cannot supply the bounded or power-saving exceptional set required by TCRC. No asymptotic conclusion is inferred from the six-element finite overlap.

## 5. A certified fourth-input comparison test

Set
\[
d_0=3-\sqrt7>0,
\qquad
\mathcal A_4=\left\{\pm\sqrt{\frac{3+a}{d_0}}:a\in\mathcal A_3\right\}.
\]
The frozen degree computation gives \([\mathbb Q(\mathcal A_4):\mathbb Q]=16384\). The parameter
\[
C^\dagger=\sqrt{\frac6{d_0}}=\frac{\sqrt6}{\sqrt{d_0}}
\]
is in the actual field: \(2/\sqrt{d_0}\in\mathcal A_4\), so \(\sqrt{d_0}\) and its reciprocal lie in that field, as does \(\sqrt6\in K\).
It is legal because
\[
M(\mathcal A_4)^2=\frac{3+\sqrt7}{d_0}<\frac6{d_0}.
\]

Every old opposite pair \(\{a,-a\}\) produces four actual inputs
\[
\pm x,\pm y,\qquad
x=\sqrt{\frac{3+a}{d_0}},\quad
 y=\sqrt{\frac{3-a}{d_0}},\quad x^2+y^2=(C^\dagger)^2.
\]
Since \(\sqrt2\) belongs to the actual field, the four radicands
\(C^\dagger\pm x,C^\dagger\pm y\) belong to one square class. Explicitly, with \(\Gamma=C^\dagger+x\), positive normalized roots are
\[
1,\quad
\frac y{C^\dagger+x},\quad
\frac{C^\dagger+x+y}{\sqrt2(C^\dagger+x)},\quad
\frac{C^\dagger+x-y}{\sqrt2(C^\dagger+x)}.
\]
Squaring these expressions gives respectively
\[
1,\quad
\frac{C^\dagger-x}{\Gamma},\quad
\frac{C^\dagger+y}{\Gamma},\quad
\frac{C^\dagger-y}{\Gamma}.
\]
All denominators are positive and nonzero.

For the explicit quartet arising from \(a=1\), take
\[
B_4=\left\{\pm\frac2{\sqrt{d_0}},
\pm\frac{\sqrt2}{\sqrt{d_0}}\right\},
\qquad
\Gamma=\frac{\sqrt6+2}{\sqrt{d_0}}.
\]
The four positive normalized roots are
\[
V=\left\{1,\sqrt3-\sqrt2,
\frac{\sqrt2+\sqrt6-2}{2},
\frac{\sqrt2-\sqrt6+2}{2}\right\}\subset K.
\]
They are positive and pairwise distinct, either by the strictly increasing radicand correspondence or by coefficient comparison. The signed set is \(U_4=V\cup(-V)\), with \(|U_4|=8\). Exact expansion in the basis
\(1,\sqrt2,\sqrt3,\sqrt6\) gives
\[
|Q(U_4,U_4)|=20.
\]
For reproducibility, its 20 coordinate vectors in that basis are
\[
\begin{gathered}
(1,0,0,0),\ (3,0,0,0),\\
(3,-1,1,-1),\ (3,-\tfrac12,1,-\tfrac12),\
(3,\tfrac12,-1,-\tfrac12),\ (3,1,-1,-1),\\
(4,0,0,-1),\\
(5,-\tfrac32,1,-\tfrac32),\ (5,\tfrac32,-1,-\tfrac32),\ (5,0,0,-2),\\
(6,-1,1,-2),\ (6,1,-1,-2),\\
(7,-\tfrac32,1,-\tfrac52),\ (7,\tfrac32,-1,-\tfrac52),\\
(8,0,0,-3),\\
(9,-\tfrac72,3,-\tfrac72),\ (9,-3,3,-3),\
(9,3,-3,-3),\ (9,\tfrac72,-3,-\tfrac72),\\
(15,0,0,-6).
\end{gathered}
\]
There are exactly 20 unordered-positive-root/sign branch labels, so every branch in this quartet is distinct. The actual root contribution is exactly \(\Gamma Q(U_4,U_4)\), also of size 20.

This fourth-level test certifies eight internally coherent quartets, but it does **not** certify that different quartets have the same class. The displayed chosen subset has 28 exceptional inputs. No three-affine cover, full class partition, or full branch-image count at this parameter is claimed. It is a one-step test on the actual fourth input, not a restart of the frozen repeated-complementary continuation.

## 6. Quantitative interpretation

| Actual input | Legal parameter | Certified class/subset size | Exceptional inputs | Root-image size | Certified affine-cover information |
|---|---:|---:|---:|---:|---|
| \(\mathcal A_3\), size 16 | \(3\), optimizing | 4, largest class | 12 | 17 | Exactly five copies are necessary and sufficient |
| \(\mathcal A_3\), size 16 | \(4\), comparison | 6, largest class | 10 | 41 | One identity copy, since \(U\subseteq\mathcal A_3\) |
| \(\mathcal A_4\), size 32 | \(\sqrt{6/(3-\sqrt7)}\) | 4, explicit subset | 28 | 20 | No cover claimed; all 20 branches are distinct |

The optimizer experiment shows that an arbitrary exact affine-cover search does not automatically return three copies even when the root image is much smaller than the old image numerically: 17 is less than 68, yet affine containment requires five copies. This distinguishes cardinality contraction from affine geometric cover.

The comparison experiment shows the useful opposite phenomenon: an exact one-copy cover can hold without a nearly full input class. Its exceptional set is too large to imply a power-saving recurrence. These two finite facts isolate separate requirements; neither proves nor disproves eventual TCRC for the optimizing family.
