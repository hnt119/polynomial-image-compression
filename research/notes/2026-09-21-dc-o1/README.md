# Bottom line

- Four mechanisms were examined: small asymmetric fringes, local return products, balanced state words, and correlated polynomial words with moving return poles.
- The balanced-state and moving-pole constructions have $X=Y$ exactly. This removes the overlap cost but does not supply many genuine returns.
- Independent local rotations cannot generally be multiplied after scalar addition: their cross terms force synchronization on the stated product domains. Balanced state compatibility also remains sparse.
- For the explicit moving-pole family, $|U_d|=3^d$ but $R_{\rm pair}\le27$ everywhere. Thus its effective return exponent is zero; every fixed positive return threshold exponent eventually has a quadratic bad set.
- No positive triple $(\varepsilon,\eta,\delta)$ is established. The transport theorem gives no fixed $c>0$. DC-O1 and the quadratic target remain OPEN.
- The single next obligation is a **correlated DC-O1 return-domain witness**: preserve the scalar cross terms on an almost-full rectangle while realizing polynomially many distinct returning multipliers. Its exact scope is stated at the end.

## RECTANGULAR WITNESS FAIL

$$\boxed{X\approx Y\xrightarrow{\mathrm{PROVED}}
\text{almost-full rectangle}\xrightarrow[\text{tested mechanisms}]{\mathrm{FAILED}}
\text{many returns}\xrightarrow[\text{DC-O1 hypotheses}]{\mathrm{PROVED}}
\text{same-set power saving}.}$$

The last arrow is a proved implication, not an achieved construction.
The many-return step remains OPEN outside the failures proved here.

**DC-O1 research report — 21 September 2026, T03.** Strictly offline;
no external input, literature search or novelty claim. The preceding
[dense-Cartesianization checkpoint](../2026-09-21-dense-cartesianization/README.md)
is retained as frozen context. No completed carrier was rerun with a
minor parameter change. This user-authorized cycle concerns only
$Q(x,y)=x^2+xy+y^2$ and high-overlap rectangular returns.

## 1. Legal return domains and the exact gate

### Statement

For $\omega=(-1+i\sqrt3)/2$, $u=a+b\omega$, $N(u)=a^2-ab+b^2=1$,

$$M_u=\begin{pmatrix}a&b\\-b&a-b\end{pmatrix},\qquad
D_u=(X\times Y)\cap M_u^{-1}(X\times Y).$$

We count distinct target pairs:

$$R(p)=|\{M_up\in X\times Y:u\in U\}|.$$

For a nonzero source this equals $\sum_u1_{D_u}(p)$ when $U$ has
distinct multipliers. At zero every action has the same single target.
All finite scouts require returns into the **oriented rectangle**;
returns merely into $(X\cup Y)^2$ are not silently substituted.

Writing $A=X\cup Y$, $n=|A|$, the established DC-R1 bound is

$$|Q(A,A)|\le n^2/R+|X\setminus Y|^2+|Y\setminus X|^2+2|E|.$$

For $R\ge n^\varepsilon$, $|X\triangle Y|\le Cn^{1-\eta}$ and
$|E|\le C'n^{2-\delta}$, every strict
$c<\min(\varepsilon,2\eta,\delta)$ is certified eventually.

### Meaning

Different actions may have completely different partial-return domains.
The needed estimate is pointwise outside a small exceptional set.
Large summed overlap alone is not used as a lower-tail theorem.

### Consequence

The remaining question is the construction of the three positive
exponents. The cycle examines four routes to those premises, rather
than replacing the fixed target or searching for another global theorem.

## 2. Almost-common cores — capacity of an asymmetric fringe

### Statement

Let $C=X\cap Y$, $F=|X\triangle Y|$, $M=|U|$, and let $K$ be the
largest positive-norm fiber in $C^2$. Put
$H=(X\times Y)\setminus C^2$, $h=|H|\le nF$. If $\ell(p)$ counts
distinct returns from $p\in C^2$ into $H$, then

$$\ell(p)\le2F,\qquad
\sum_{p\in C^2}\ell(p)\le\min(M,K)h.$$

If the rectangular return threshold is $R$ outside $e$ bad pairs,
the same actions return at least $R/2$ pairs into the core outside at most

$$\boxed{e+2\min(M,K)nF/R}.$$

Thus with $M=O(n^\gamma)$ a sufficient core-tail deficit is
$\min(\delta,\eta+\varepsilon-\gamma)>0$. This is a sufficient
condition, not a necessary one. For a weak core with return bound
$L<R$, the number rescued to $R$ by fringe targets is at most
$\min(M,K)nF/(R-L)$.

### Meaning

Each fringe coordinate lies on at most two points of a given norm shell.
Each fringe target has at most $M$ action preimages and at most $K$
equal-norm core preimages. These two exact counts give a bound on
lost or gained returns even when every action has a different domain.

### Consequence

A power-saving fringe cannot rescue almost every pair of a core with
uniformly subpolynomial norm fibers and subpolynomial core returns.
This does not assert that every possible core has small fibers.

A useful distinction is also proved: the rectangular tail itself gives

$$|Q(C,C)|\le |Q(X,Y)|\le |X||Y|/R+e.$$

Thus a successful rectangle would compress its almost-equally-large
core, with every strict saving below $\min(\varepsilon,\delta)$,
even if its original actions leave the core. This is an image inclusion,
not an assertion that those original returns survive intersection. No
rectangle satisfying the premise has been constructed. Full proofs and
the replacement-action accounting are in [CF-1–CF-4](core-fringe.md).

## 3. Local return products — scalar cross terms synchronize actions

### Statement

For nonzero real weights $\theta_i$, local domains $D_i\ni0$ spanning
$\mathbb R^2$, and norm rotations $T_i$, suppose

$$Q\left(\sum_i\theta_iT_iv_i\right)
=Q\left(\sum_i\theta_iv_i\right)
\quad\text{for every }(v_i)\in\prod_iD_i.$$

Then all $T_i$ are the same rotation. Setting all but two coordinates
to zero and cancelling pure terms gives

$$\langle T_iv,T_jw\rangle_Q=\langle v,w\rangle_Q,$$

which forces $T_i=T_j$ on full spans. No faithfulness or independence
of the scalar weights is needed. Without zero, the same result uses
full **difference spans**, by the four-corner subtraction.

For action-dependent full-rank local return domains, the number of
uniformly valid tensor words at a tuple is therefore

$$\left|\bigcap_i L_i(v_i)\right|\quad\text{rather than}\quad
\prod_i|L_i(v_i)|.$$

For fixed zero-containing nonzero rank-one domains, reflections are
also possible, but at most $2\min_i|U_i|$ compatible assembled maps
exist. The companion states the exact hypotheses and examples.

### Meaning

Independent choices preserve the local norms but generally change
the cross terms between different coordinates. A product of local
return counts is consequently not yet a scalar return theorem.

### Consequence

A fixed finite gadget has return exponent zero under these uniform
product-domain certificates. A large-deviation estimate for the
formal product cannot repair this earlier failure of the norm identity.
Correlated restrictions on tuples, with their own exact identity and
coverage proof, are outside this obstruction. See
[DC-T1–DC-T3](tensor-compatibility.md).

## 4. Balanced state words — equality of sets does not balance pairs

### Statement

Take disjoint scalar alphabets $S=\{-1,1\}$, $T=\{-3,3\}$.
For even $d$, let $\mathcal W_d$ consist of words in $(S\cup T)^d$
having exactly $d/2$ letters in $S$. With injective scalar encoding
$\Phi(w)=\sum_{i=0}^{d-1}w_i100^i$, define
$X_d=Y_d=A_d=\Phi(\mathcal W_d)$.

Then, with $L_d=\binom d{d/2}$,

$$n_d=L_d2^d,\qquad |X_d\triangle Y_d|=0.$$

The local rectangular certificate requires complementary states at
every position: one coordinate letter in $S$ and the other in $T$.
Its exactly compatible scalar population is

$$G_{\rm cert}=L_d4^d,\qquad
\boxed{G_{\rm cert}/n_d^2=1/L_d\le(d+1)/2^d}.$$

Input injectivity follows because digit differences have size at most
6 and the leading term dominates at base 100. No quadratic or action
faithfulness is inferred merely from that fact.

### Meaning

Union over balanced state patterns makes the scalar sets exactly equal.
But two independently chosen words usually have noncomplementary state
patterns, so almost all their pairs remain outside the local certificate.

The local swaps are genuine: $u_+=(15+8\omega)/13$ sends $(1,3)$
to $(3,1)$, and $u_-=(3+8\omega)/7$ sends $(1,-3)$ to $(-3,1)$;
their signed source pairs and conjugate actions give the reverse
domains. These are partial transitions between orientations, not
returns into the same local rectangle. The local signs $\pm1$ do
return within that rectangle.

### Consequence

Even granting arbitrarily rich returns to every compatible pair leaves
$B_{\rm cert}=n_d^2-G_{\rm cert}=n_d^2(1-o(1))$. This is a scoped
coverage failure; it is not an actual-image lower bound or a claim that
all other pairs have no returns. The scouts below also measure genuine
scalar returns under the fixed ten actions
$\{\pm1,\pm u_+,\pm\bar u_+,\pm u_-,\pm\bar u_-\}$.
Full combinatorics and costs: [type-balance.md](type-balance.md).

## 5. Correlated polynomial words — moving poles have empty late domains

### Statement

Choose the return actions first:
$v_j(T)=(T-j-\omega)/(T-j-\bar\omega)$, $1\le j\le d$.
Set $B_d=[10(d+2)]^{4d}$ and $u_j=v_j(B_d)$. Define

$$X_d=Y_d=A_d=\left\{\sum_{i=0}^{d-1}a_iB_d^i:
a_i\in\{-1,0,1\},\ \sum_i a_i=0\right\},$$
$$U_d=\{\prod_{j=1}^d u_j^{e_j}:e_j\in\{-1,0,1\}\}.$$

The exact input and action counts satisfy

$$3^d/(2d+1)\le n_d\le3^d,\qquad |U_d|=3^d,$$

but **MP-1 proves**

$$\boxed{R_{\rm pair}(p)\le27\quad\text{for all }p\in A_d^2.}$$

Clearing selected denominators and using the large base turns every
scalar return into the polynomial identity $z'D_e=zN_e$, with
$z=f-\omega g$. A nonzero $z$ has coefficients of magnitude at most
2 and leading coefficient of magnitude at least one, so all its roots
have modulus at most 3. Yet the poles for $j\ge4$ have modulus squared
$j^2-j+1\ge13$. Hence every returning exponent at those indices is
zero; only three width-one exponents can remain.

### Meaning

This carrier has correlated digits and many quadratic coefficient
relations. It falls outside the previous faithful-quadratic digit
theorem. The failure instead comes from the explicitly prescribed
partial divisibility domains: all late poles have no nonzero sources.

### Consequence

For every fixed $\varepsilon>0$, eventually $n_d^\varepsilon>27$,
so $B_\varepsilon=n_d^2$ exactly. One may take any positive $\eta$
because $X=Y$, but no positive return or exceptional-tail exponent
survives. The scalar statement concerns the finite selected power box;
arbitrary integer powers are not covered by its evaluation bound.
The actual image rate is OPEN in this cycle. Complete proof:
[moving-poles.md](moving-poles.md).

## 6. Exact finite scouting

The fixed scout threshold is $n^{1/4}$, implemented as its integer
ceiling. Every ordered rectangular pair and every selected action is
checked, with distinct targets retained. The full union-square image
is computed separately. Equality uses rational arithmetic; the second
oracle uses real/$\sqrt{-3}$ coordinates. No formal tensor return is
counted as an actual multiplier return.

| Construction | $d$ | $|X|$ | $|Y|$ | $n$ | $|X\triangle Y|$ | $|U|$ | Median | Min good | $B_{1/4}$ | Full $|Q(A,A)|$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Local signed rectangle | 1 | 2 | 2 | 4 | 4 | 10 | 2 | 2 | 0 | 6 |
| Balanced states | 2 | 8 | 8 | 8 | 0 | 10 | 2 | 2 | 0 | 20 |
| Balanced states | 4 | 96 | 96 | 96 | 0 | 10 | 2 | — | 9216 | 2352 |
| Moving poles | 3 | 7 | 7 | 7 | 0 | 27 | 1 | — | 49 | 11 |
| Moving poles | 4 | 19 | 19 | 19 | 0 | 81 | 1 | — | 361 | 71 |
| Moving poles | 5 | 51 | 51 | 51 | 0 | 243 | 1 | — | 2601 | 507 |

**Exact return histograms.** The notation $r:c$ counts $c$ source pairs with $r$ distinct returns.

| Construction/depth | $R_{\rm pair}$ | One-return fraction | Geometric mean | Bad fraction at $n^{1/4}$ |
|---|---|---:|---:|---:|
| Local signed rectangle 1 | $2:4$ | $0$ | 2.000000 | $0$ |
| Balanced states 2 | $2:64$ | $0$ | 2.000000 | $0$ |
| Balanced states 4 | $2:9216$ | $0$ | 2.000000 | $1$ |
| Moving poles 3 | $1:49$ | $1$ | 1.000000 | $1$ |
| Moving poles 4 | $1:349, 2:12$ | $349/361$ | 1.023308 | $1$ |
| Moving poles 5 | $1:2565, 2:36$ | $285/289$ | 1.009640 | $1$ |

The moving-pole cases contain zero. Its action count is $|U|$, while its distinct-pair count is one. At every other pair action and pair counts agree. The signed and balanced cases have no zero source and trivial stabilizers.

The balanced-state compatibility counts are 32 of 64 pairs at depth two and 1,536 of 9,216 at depth four. These differ from the actual rich sets in the table. At depth four every scalar pair has exactly two returns under the ten chosen actions, below the threshold four. The three moving-pole cases have thresholds two, three and three.

All complete action-count and image-fiber histograms, individual return-domain sizes, and exact geometric-mean expressions are retained in the frozen JSON. The raw file retains every actual returned pair. Decimal geometric means are display values only.

Small cases meeting this low numerical threshold do not establish an
asymptotic positive exponent. No construction was selected for further
development after its structural gate failed; no additional parameter
search followed the six predetermined cases.

## 7. Signed ledger and exact failure scopes

| Mechanism | Input/overlap | Genuine return rate | Bad-tail cost | Disposition |
|---|---|---|---|---|
| Core/fringe | Conditional $F=O(n^{1-\eta})$ | No witness; rescue limited by $\min(M,K)nF$ | Core transfer costs $2\min(M,K)nF/R$ | Low-fiber fringe repair FAILED in stated scope; general premise OPEN |
| Local product domains | Exponential scalar input growth is a hypothesis | Bounded gadget synchronizes; rate zero in proved scope | Whole rectangle eventually below polynomial certificate threshold | Uniform independent local-product certificate FAILED |
| Balanced states | $n=\binom d{d/2}2^d=e^{d\log4+O(\log d)}$; $\eta$ may be any positive number | Formal returns are not scalar returns; fixed ten-action scout has rate zero | Complementary-state certificate leaves $n^2(1-o(1))$ pairs | State-balancing certificate FAILED |
| Moving poles | $n=e^{d\log3+O(\log d)}$; $X=Y$ | At most 27, so effective $\varepsilon=0$ | $B_\varepsilon=n^2$ eventually for every fixed positive $\varepsilon$ | Explicit selected-action witness FAILED; no positive $\delta$ |

For $X=Y$, choosing $\eta=1$ is a convenient valid convention;
zero asymmetry in fact permits every fixed $\eta>0$. An effective
zero return rate is not a positive DC-O1 exponent. No row supplies
all three positive exponents or an explicit $c>0$.

The two concrete scalar families are integral, using fixed
$\mathbb Q(\omega)$ for their rational multipliers. The field degree
is two and discriminant $-3$. No regulator, class-number, splitting
or ideal-volume estimate is used. The balanced-state actions have
denominators 1, 7 or 13. The moving-pole common denominator divides
$\prod_{j\le d}[(B_d-j)^2+(B_d-j)+1]$, with logarithm
$O(d^2\log d)$; scalar heights have the same logarithmic upper order.
These costs are explicit, not assumed negligible or polynomial in $n$.

The scalar maps are injective where claimed; both input coordinates
pay the word restrictions in the displayed counts. Every target is
tested in the oriented rectangle. Zero, when present, has one distinct
returned point. No unknown field, projection, state or boundary cost
is set to zero. Each proof companion contains the construction ledger
and precise quantified statement required by the repository template.

No new actual-image lower bound is claimed by this cycle. Its scoped
failures do not disprove DC-O1, the quadratic target, ARG, TCRC or
RC15/4. HR-N1 remains separately DISPROVED. The older proof files and
all four fixed track targets are preserved.

## 8. Review and reproducibility

The new claim IDs are CF-1–CF-4, DC-T1–DC-T3, the type-balance claims
identified in their companion, and MP-1. All are dated 21 September
2026, T03/DC-O1, fixed $Q$ on real inputs. They have complete local
proofs and separate internal audits, not external peer review. Source
hashes, corrections, exact executions and repository checks are in
[verification.md](verification.md).

The six-case program is
[rectangular_returns.py](../../../experiments/rectangular_returns.py);
[frozen summary](../../../examples/2026-09-21-dc-o1.json) and local raw
pair data make it reproducible. The standard arithmetic module was
inspected and reused without rerunning its old scout. No external
theorem was needed and no network call was made.

The one fixed scout used **1,535,889 charged evaluations** and **59.575291 measured research CPU seconds**. Including conservatively charged regressions, totals were **1,628,328 charges and 62.694817 CPU seconds**, below the announced 2,000,000 / 600 caps. CPU metadata precedes final data serialization. **61 tests and 159 verification checks passed**; documentation/setup and integrity results are recorded in the verification note.

Historical sources and existing uncommitted changes are retained.
Only new research files and dated status/library addenda belong to
this cycle; nothing is staged or committed. No difference-set, affine
transfer or adaptive RC15/4 search was begun.

## 9. Single next obligation

**OPEN — correlated DC-O1 return-domain witness.** Construct an explicit
high-overlap rectangle whose jointly correlated partial domains preserve
the scalar norm cross terms and give $n^\varepsilon$ distinct genuine
returns outside $O(n^{2-\delta})$ pairs, with
$|X\triangle Y|=O(n^{1-\eta})$ and fixed
$\varepsilon,\eta,\delta>0$. Independent local rotations may not be
credited through a full-product norm identity that the synchronization
theorem forbids. This is the same DC-O1 witness obligation, sharpened by
the proved compatibility constraint; no broad new carrier search is
adopted or started in this handoff.
