# Local return products and scalar norm compatibility

Date: **21 September 2026**. Track: **T03 / DC-O1**. Sole polynomial:
$Q(x,y)=x^2+xy+y^2$ on real inputs.

## Identity, sources and evidence

This is a bounded symbolic subtask of the newly authorized, strictly
offline DC-O1 cycle. It analyzes coordinatewise rotations followed by
real linear scalar assembly. **No program runs, mathematical evaluation
budget, network access, external results or novelty claims are used.**
Only this new note is authored; historical files are unchanged.

The complete local arguments below establish the following claims. Their
status is **PROVED by internal derivation and independently audited in
this task**. The separately assigned source/proof auditor inspected
DC-T1–DC-T3, the two reflection examples, arbitrary weight relations,
action-dependent full-rank return domains, zero, noninjective assembly
and the certificate-only conclusion, and reported PASS with no
substantive issue. This was an internal symbolic audit, not external
review or a program run; the lead's cycle record supplies its provenance.

| ID | Quantified scope | Proof location |
|---|---|---|
| DC-T1 | Any finite number of nonzero real assembly weights, local norm rotations, and zero-containing local domains: uniform preservation of the assembled $Q$ forces preservation of every cross inner product; one two-dimensional local span forces all nonzero local factors to use the same rotation | §1 |
| DC-T2 | Without zero, the same cross constraint holds on difference spans; one full difference span synchronizes all factors having nonzero variation. Linear span alone does not suffice | §2 |
| DC-T3 | Fixed zero-containing nonzero local domains and finite action alphabets: at most $2\min_i|U_i|$ uniformly norm-compatible assembled maps, improved to the diagonal intersection when one local span is two-dimensional; full-rank local return domains give intersection, not product, return labels | §3 |

Source history and exact use:

- [Current dense-Cartesianization checkpoint](../2026-09-21-dense-cartesianization/README.md),
  §§2, 5–6, 12: the coefficient action, the earlier faithful-product
  results, proved rectangular transport, and the OPEN DC-O1 witness.
- [DC-M2–M5](../2026-09-21-dense-cartesianization/matrix-product.md),
  §§3–5.1: earlier action-faithful overlap and quadratic-faithful image
  bounds. They are context, **not premises** of the proofs below. Here
  the weights may have arbitrary real linear and quadratic relations.
- [DC-R1](../2026-09-21-dense-cartesianization/block-rectangle.md), §4,
  and [HR-1](../2026-09-16-high-return/return-lemma.md): genuine distinct
  returned pairs and power-saving exceptions are required for the
  full-support conclusion. No such positive tail is asserted here.
- Private sources `local-only/migration/sources/00_MASTER_HANDOFF.md`,
  §§1, 5, 13, and `local-only/migration/sources/T03_CURRENT_STATE.md`,
  §§1–3: fixed same-set target, support-versus-energy distinction and
  historical scope. The current branch checkpoint controls this newer
  assignment; T03-O4/RC15/4 is not attempted.
- `research/MIGRATION_CONFLICTS.md`, MC-03/MC-05/MC-06, and the dated
  dense-Cartesianization entries of `research/MECHANISM_LIBRARY.md`,
  `research/FAILURE_LIBRARY.md`, `research/OPEN_LEMMAS.md`: retained
  source and failure scopes. The absent F25/arithmetic originals are
  not needed for this elementary proof.

The new distinction is between **independent local rotations** and one
genuine scalar norm action. The earlier faithful-digit theorem instead
studied the digit behavior of an already fixed scalar action. Neither
statement supersedes the other.

## 1. DC-T1 — zero-containing local domains

### Statement

Put

$$B((x,y),(s,t))=xs+(xt+ys)/2+yt,$$

so $B(v,v)=Q(v)$ and $Q(x,y)=(x+y/2)^2+3y^2/4$ is positive definite.
Identify $\mathbb R^2$ with $\mathbb C$ by
$\phi(x,y)=x-\omega y$, $\omega=(-1+i\sqrt3)/2$. For $|u|=1$,
let $T_u$ be multiplication by $u$ in these real coordinates:

$$T_{a+b\omega}=
\begin{pmatrix}a&b\\-b&a-b\end{pmatrix},\qquad
a^2-ab+b^2=1.$$

Fix $d\ge1$, weights $\theta_i\in\mathbb R\setminus\{0\}$,
sets $D_i\subseteq\mathbb R^2$ containing zero, and rotations
$T_i=T_{u_i}$ with $|u_i|=1$. Write

$$S(v)=\sum_{i=1}^d\theta_i v_i,\qquad
S_T(v)=\sum_{i=1}^d\theta_i T_i v_i.$$

Assume the uniform scalar identity

$$Q(S_T(v))=Q(S(v))\qquad
\text{for every }v\in\prod_iD_i.\tag{1}$$

Then, with $V_i=\operatorname{span}_{\mathbb R}D_i$,

$$B(T_i v,T_j w)=B(v,w)
\quad(i\ne j,\ v\in V_i,\ w\in V_j).\tag{2}$$

There is a single $Q$-orthogonal linear map $O$ on $\mathbb R^2$
such that $T_i|_{V_i}=O|_{V_i}$ for all $i$. Therefore

$$S_T(v)=O S(v)\quad\text{on the entire product domain}.\tag{3}$$

If some $V_i=\mathbb R^2$, then $O=T_i$ is a rotation and every
index $j$ with $V_j\ne\{0\}$ satisfies $T_j=T_i$. In particular,
if all $D_i$ span $\mathbb R^2$, (1) holds **if and only if**

$$u_1=u_2=\cdots=u_d.\tag{4}$$

No injectivity, rational independence, quadratic faithfulness, separation
or height hypothesis on the weights is required.

#### Proof

For distinct $i,j$, put every other coordinate equal to zero in (1).
Since $T_i,T_j$ each preserve $Q$, the pure terms cancel, leaving

$$2\theta_i\theta_j
\bigl[B(T_i v,T_j w)-B(v,w)\bigr]=0
\quad(v\in D_i,w\in D_j).$$

Both weights are nonzero. Bilinearity extends the resulting equality
to $V_i\times V_j$, proving (2). The same inner-product identity holds
within each individual $V_i$ because $T_i$ is a rotation.

Define a map on $V=\sum_iV_i$ by the proposed rule

$$O\left(\sum_i v_i\right)=\sum_iT_i v_i,\qquad v_i\in V_i.$$

It is well defined: if $\sum_i v_i=0$, all the within-block and
cross-block inner products just established give

$$Q\left(\sum_iT_i v_i\right)=Q\left(\sum_i v_i\right)=0,$$

so positivity makes the transformed sum zero. The same expansion
shows that this linear map preserves $B$. If $V=\mathbb R^2$, it is
already a $Q$-orthogonal map. If $V$ is a line, extend a normalized
vector of that line and its image to $B$-orthonormal bases and map
one basis to the other. If $V=\{0\}$, take the identity. This proves
the stated extension and (3).

If $V_i=\mathbb R^2$, the restrictions give $O=T_i$. For any other
$V_j\ne\{0\}$, select $w\ne0$ in $V_j$. Then $T_jw=T_iw$.
In complex coordinates $u_j\phi(w)=u_i\phi(w)$, and $\phi(w)\ne0$,
so $u_j=u_i$. The converse in (4) follows immediately by applying
one common rotation to $S(v)$. $\square$

### Meaning

Preserving each local norm is not enough to preserve the norm of the
sum. The cross terms compare different coordinates. Independent choices
of rotations can only be combined uniformly if those cross comparisons
agree. Algebraic relations between scalar weights do not remove this
test: zero isolates each two-coordinate comparison before any global
coefficient recovery is needed.

### Consequence

This obstructs a **uniform tensor norm certificate**, not the actual
image of every assembled set. It does not address tuples on which an
otherwise incompatible word happens to preserve $Q$. Such a restricted
domain needs its own exact identity and coverage proof.

## 2. DC-T2 — difference spans, rank-one exceptions and missing zero

### Statement

Allow arbitrary nonempty $D_i$, possibly without zero, and retain (1).
Let $H_i=\operatorname{span}_{\mathbb R}(D_i-D_i)$. Then

$$B(T_i h,T_j k)=B(h,k)
\quad(i\ne j,\ h\in H_i,k\in H_j).\tag{5}$$

If one $H_i=\mathbb R^2$, all factors with $H_j\ne\{0\}$ use
the same rotation. In particular, full affine span for every local
domain implies (4), even when none contains zero. Singleton domains
have zero variation; this conclusion does not constrain their factors.

For the more general rank-one case, put $H=\sum_iH_i$. If
$H=\mathbb R^2$, there is one $Q$-orthogonal map $O$ with

$$S_T(v)=O S(v)\quad\text{on }\prod_iD_i.\tag{6}$$

This $O$ can have determinant $-1$, in which case it is a reflection
in the complex model and need not equal any fixed norm multiplier.

#### Proof

Fix all coordinates other than $i,j$, and choose two values in each
of those two domains. Take the alternating sum of (1) over the four
corners. Every term involving at most one varied coordinate cancels.
The remainder is

$$2\theta_i\theta_j
\{B(T_i(v_i-v_i'),T_j(v_j-v_j'))
-B(v_i-v_i',v_j-v_j')\}=0.$$

Bilinearity gives (5). If $H_i=\mathbb R^2$ and $0\ne k\in H_j$,
orthogonality of $T_i$ rewrites (5) as
$B(h,(T_i^{-1}T_j-I)k)=0$ for every $h\in\mathbb R^2$.
Nondegeneracy and complex cancellation give $T_i=T_j$.

For the final assertion, the Gram argument of §1 on the spaces $H_i$
gives $O|_{H_i}=T_i|_{H_i}$. Choose base points $b_i\in D_i$.
Every product tuple then satisfies

$$S_T(v)=O S(v)+c,\qquad
c=\sum_i\theta_i(T_i-O)b_i.$$

Using (1) and orthogonality of $O$ gives
$2B(OS(v),c)+Q(c)=0$ on the product. Subtraction between two tuples
forces $B(O(S(v)-S(v')),c)=0$. Such differences span
$\sum_i\theta_iH_i=H=\mathbb R^2$, so $c=0$. This proves (6).
$\square$

### Meaning — exact exceptions to synchronization

**Rank-one domains really permit a reflection.** In complex coordinates,
take $d=2$, weights one, $D_1=\{0,1\}$, $D_2=\{0,i\}$,
$u_1=1$, $u_2=-1$. For all $s,t\in\{0,1\}$,

$$u_1s+u_2(it)=s-it=\overline{s+it}.$$

Thus global norms agree despite $u_1\ne u_2$. These are legitimate
real pair domains through $\phi^{-1}$. Their local spans have rank
one, while their combined span has rank two. No fixed multiplier
implements this reflection on the whole assembled set: the input
points $1$ and $i$ require multiplier $1$ and $-1$, respectively.

**Without zero, full linear span is insufficient.** Take $d=3$,
weights one, and complex domains

$$D_1=\{i,1+i\},\qquad
D_2=\{-1,-1+i\},\qquad
D_3=\{2,3+i\},$$

with $u_1=1$, $u_2=-1$, $u_3=-i$. Every $D_i$ has real linear span
two but affine span one. For $s,t,r\in\{0,1\}$, the assembled input is

$$S=1+i+s+it+(1+i)r,$$

and the assembled output is

$$S_T=1-i+s-it+(1-i)r=\overline S.$$

The three rotations are different, yet (1) holds. This verifies why
difference spans, rather than linear spans, are the correct assumption
when zero is absent. The example is a scope test, not a growing
rectangular witness.

### Consequence

A reflection preserves $Q$, and at each nonzero input $z$ its returned
point can be written as $uz$ with $u=O(z)/z$ of norm one. This quotient
usually depends on the input. Therefore a reflection cannot silently be
identified with one fixed scalar multiplier; conversely it should not
be called an invalid returned pair. Distinct pairs, actual action labels
and their input dependence must be counted separately. The following
bound shows why fixed rank-one local gadgets still do not yield a
product-sized family of assembled returns in the stated uniform scope.

## 3. DC-T3 — count the compatible maps before using a product rate

### Statement

First fix zero-containing domains $D_i$ with $V_i\ne\{0\}$ and
finite sets $U_i$ of distinct norm-one multipliers. Call a word
$\mathbf u\in\prod_iU_i$ compatible if it satisfies (1) on the
**entire fixed product** $\prod_iD_i$.

There are at most

$$2\min_i|U_i|\tag{7}$$

compatible words, and hence at most that many assembled maps and
returned pairs at any input. If some $V_i=\mathbb R^2$, the compatible
words are exactly

$$\{(u,\ldots,u):u\in\bigcap_iU_i\}.\tag{8}$$

Zero-only domains may be omitted; their freely chosen labels do not
change the assembled input or output and must be treated as duplicates.

#### Proof

Choose an index $i$ and $v\ne0$ in $V_i$. By DC-T1 every compatible
word is represented on its assembled domain by a $Q$-orthogonal map
$O$ with $Ov=T_uv$ for some $u\in U_i$. For each fixed nonzero
source and target of the same norm there are exactly two orthogonal
maps in dimension two: their actions on a normalized orthogonal
complement have the two possible signs. Thus there are at most
$2|U_i|$ possible $O$.

For each such $O$ and each $j$, there is at most one norm rotation
$T_{u_j}$ agreeing with $O$ on $V_j$: agreement on one nonzero vector
determines its complex multiplier. Hence the number of compatible
words is at most $2|U_i|$. Minimize over $i$. If one local span has
rank two, DC-T1 gives precisely the diagonal words (8). $\square$

Now let local finite rectangular carriers be $K_i=X_i\times Y_i$,
with $0\in X_i\cap Y_i$, and use local action sets $U_i$. Define
the action-dependent return domain

$$D_i(u)=K_i\cap T_u^{-1}K_i.$$

Assume every $D_i(u)$ under consideration spans $\mathbb R^2$.
It automatically contains zero. Assemble the two scalar sets by the
same weights:

$$X=\left\{\sum_i\theta_i x_i:x_i\in X_i\right\},\qquad
Y=\left\{\sum_i\theta_i y_i:y_i\in Y_i\right\}.$$

At a fixed tuple $v_i\in K_i$, write

$$L_i(v_i)=\{u\in U_i:T_uv_i\in K_i\},\qquad
r_i(v_i)=|L_i(v_i)|.$$

There are $\prod_i r_i(v_i)$ formal coordinatewise return words.
Among words that preserve the scalar norm on their full product
$\prod_iD_i(u_i)$, the exact count is only

$$\left|\bigcap_iL_i(v_i)\right|\le\min_i r_i(v_i).\tag{9}$$

Indeed, DC-T1 applied separately to each word's product domain makes
it diagonal. Every diagonal word does preserve the assembled norm and
returns each coordinate into its local carrier, proving both directions.
For a nonzero assembled pair these diagonal multipliers give distinct
returned scalar pairs. At an assembled zero pair there is at most one
distinct returned pair, irrespective of the number of words.

### Meaning

Local choices multiply as formal words. They need not multiply as
global norm-preserving operations. For this certificate the local
return sets must intersect in a common multiplier; they cannot be
selected independently. This conclusion does not require scalar input
injectivity or faithful recovery of quadratic coefficients.

### Consequence and rate

For a fixed finite local gadget, $|U_i|\le m$ with fixed $m$,
the certified return count in (9) is at most $m$ at every tuple.
If $\log n_d=ad+o(d)$ with $a>0$, this gives return exponent zero,
even when the formal local product has positive logarithmic rate.
Allowing all rank-one possibilities in the fixed-domain version only
changes the bound to $2m$ by (7), still exponent zero.

More generally, a subexponential minimum local action count gives
only a subexponential number of compatible assembled maps. A positive
return exponent would require a correspondingly large paid local action
inventory or a mechanism outside these uniform product hypotheses.

For the full-rank return-domain certificate, all actual multipliers
used by compatible words lie in $\bigcap_iU_i$, across all tuple
representations. Thus noninjective scalar assembly does not create
additional certified actions by choosing another representation.
If $|X\triangle Y|=o(n)$ for $n=|X\cup Y|$, then
$|X||Y|=n^2(1-o(1))$. At every threshold $n^\varepsilon>m$,
the **certificate** bad set is the whole rectangle. This is not a
lower bound on the actual low-return set under other actions or under
word restrictions for which a separate norm identity is proved.

## 4. Construction and quantitative ledger

This is a scoped obstruction to uniform local-product certificates.
It supplies no new carrier with positive DC-O1 exponents and no
actual-image lower bound. The ledger follows
`research/templates/CONSTRUCTION_LEDGER.md`.

| Gain or cost | Exact accounting and status |
|---|---|
| Fixed polynomial and growing parameter | $Q$ fixed; arbitrary finite depth $d$, with all weights/domains/action sets specified before testing (1) |
| Scalar construction | Real linear assembly in §§1–3; rectangular input assembly is explicit in §3 |
| Input lower and upper counts | Without extra projection hypotheses, only $|X|\le\prod_i|X_i|$, $|Y|\le\prod_i|Y_i|$ are automatic; positive exponential lower input growth is a stated conditional rate hypothesis, not proved here |
| Projection and parameter fibers | May be arbitrary. No unit fiber is assumed. Compatibility obstruction is independent of their size; positive constructions must still pay them |
| Formal branch count | $\prod_i r_i(v_i)$ counts words, not scalar returns |
| Compatible action/map count | Intersection bound (9) in the full-rank return setting; $2\min_i|U_i|$ in the fixed zero-containing domain setting |
| Zero and inactive labels | Zero has at most one returned point. Zero-only factors contribute duplicate labels, not extra actions |
| Same-set balance | No new bound on $|X\triangle Y|$ is proved. Even if it is $o(n)$, a bounded compatible action inventory has certificate bad mass $n^2(1-o(1))$ |
| Input thinning twice | None performed. Deleting tuples to escape the full-product identity is outside the theorem and requires a fresh two-coordinate coverage/fiber charge |
| All ordered pairs and exceptions | No full high-return theorem. The full product identity is explicitly quantified; incidental norm equalities outside its certificate are not discarded or counted as impossible |
| Denominators, heights, moduli, carries | No arithmetic count or no-carry premise is used. Arbitrary real weights are allowed; these costs remain to be proved for any positive arithmetic carrier |
| Field degree, discriminant, regulator, splitting | Inapplicable to this real linear-algebra proof; no gain is claimed from them and no field construction is supplied |
| Archimedean distortion | Each local rotation preserves $Q$ exactly. Cross terms, rather than an unproved box or sum invariance, are evaluated explicitly |
| Final input rate | Conditional $\log n_d=ad+o(d)$, $a>0$; unknown without further carrier data |
| Final return rate | Zero for fixed or subexponential local inventories within the stated uniform compatibility scopes |
| Full output exponent | OPEN for a general scalar carrier. Failure of this certificate is not a lower bound for $|Q(A,A)|$ |
| DC-O1 exponents and strict $c$ | No positive $\varepsilon$ is obtained in the bounded-gadget uniform certificate, so no $c>0$ follows from DC-R1. No numerical $\eta$ or $\delta$ is asserted |

## 5. Scope retained at handoff

The proved failure concerns independent local rotations whose scalar
norm identity is required on their full product return domains. It
does **not** prohibit correlated tuple restrictions, pair-dependent
choices justified by a different exact identity, growing local action
inventories, nonlinear scalar encodings, or different arithmetic
realizations. Missing-zero domains must be measured by their difference
spans; rank-one domains have the reflection exception proved above.

The single active branch obligation remains DC-O1 in the current-cycle
report. This note does not create a second research objective or begin
a broader carrier search. No experiment or validation suite was run by
this symbolic subtask; repository validation is left to the lead's
centrally budgeted completion checks.
