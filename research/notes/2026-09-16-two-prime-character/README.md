# Full-Rank C0 Extension — First Cartesian Norm-Symmetry Cycle

**16 September 2026, version 1. T03, separate two-prime character branch.**

## Bottom line

- **Verdict: LOCAL GO / GLOBAL FAIL.** The selected correlated residue carrier has uniformly many returns, but its exact product-group action cannot retain exponential return multiplicity on real scalar pairs.
- We tested the 54-element set of units modulo $133$ whose quadratic characters at $7$ and $19$ agree, using all 108 norm-one multipliers.
- Both primes split the Eisenstein algebra and have the same character behavior for $-1$ and $3$. Their common quadratic-character quotient gives a natural correlation between the primes.
- **PROVED:** every local ordered pair has between 8 and 54 distinct returns. The median is 25 and the geometric mean is about 21.6342; no pair has only the identity return.
- **PROVED:** coordinatewise products have $R_d=\prod_i r_i\ge8^d$ with no exceptions. A stronger explicit tail has fewer than $18^d$ returns on at most $2772^d$ of the $2916^d$ ordered pairs.
- These are finite-ring statements. Any group-compatible realization by real norm-one multipliers has at most 18 distinct actions, regardless of $d$. Projected duplicate actions consume the exponential return gain. The normalized CRT factor is also adverse: $(8645/1458)^d>1$.
- The real signed rate is not positive. No full-rank C0 extension or affine transfer is obtained; no difference-set search is run. HR-N1 remains closed, and the real quadratic target and RC15/4 remain OPEN.
- **One next obligation:** retain T03-O4/RC15/4's existing whole-signed-root-image bound, stated in §10. This cycle does not begin that obligation or adopt a replacement return conjecture.

## 1. Scope, prerequisites and model selection

The current attachment commissioned one $7,19$ correlation experiment,
an exact one-block distribution, and a rigorous product/realization audit.
The network policy was fixed as **strictly offline**. The announced shared
ceiling was **2,000,000 charged evaluations and 600 CPU seconds**, including
oracles, validation and reruns. Only one new finite carrier case was run.

The existing norm identity and [HR-1 return-to-image theorem](../2026-09-16-high-return/return-lemma.md)
are used, not rederived as new mechanisms. Corrected C0 remains the reported
rank-one theorem from the local corrected source; its complete-splitting
and density accounting does not automatically extend to $Q$.

The [frozen HR-N1 result](../2026-09-16-hr-n1-final-freeze/README.md)
is later project context than the initial high-return proposal. Its rational
denominator carrier is **FAILED / DISPROVED** for the specified tail and
is not reopened here. The 18 previous rational finite cases, one-prime
families, orbit-thickening, repair and cyclotomic digit searches were not
rerun as research cases.

### 1.1 Theoretical comparison before computation

| $7,19$ model | Decision |
|---|---|
| The independent unit product $\mathbb F_7^\times\times\mathbb F_{19}^\times$ | Natural control, but it has no cross-prime correlation; not selected or enumerated |
| Equal quadratic characters | Selected: the simplest nontrivial subgroup coupling the two canonical sign quotients |
| Opposite quadratic characters | A scalar dilation of the selected set; commuting with the action gives the same return distribution, so no separate experiment |
| HR-N1 rational denominator box | Already closed by its positive-density identity-only theorem; not a candidate for this cycle |

The opposite-character assertion follows by choosing a unit $c$ with
$\chi_7(c_7)\ne\chi_{19}(c_{19})$: its coset is $cD$, and linearity gives
$T_g(cx,cy)=cT_g(x,y)$, so both membership conditions and return counts
are transported bijectively. This comparison creates no additional search.

**Important inherited restriction.** The selected residue model was not in
the previous finite return schedule, but it lies within a known local
CRT obstruction. The [correlated-CRT checkpoint, §C, Theorem 1](../../history-sources/Q_Correlated_CRT_Tensorization_Checkpoint.md)
proves $|Q(B,B)|\ge|B|$ for every correlated subset of products of split
fields in which $3$ is nonsquare. This includes both primes and their
repeated products. The present work is a new exact **return-distribution
and scalar-realization audit**, not a claim that this normalized CRT regime
was previously open. That theorem's elementary sign-cube proof was inspected.

### 1.2 Claim and evidence map

| Claim | Status and exact scope | Controlling proof |
|---|---|---|
| TP-L1 | PROVED: exact one-block counts, all ordered inputs, modular image and stabilizers | [local-count-proof.md](local-count-proof.md), §§1–5 |
| TP-P1 | PROVED: exact product return law and positive local tails for every $d\ge1$ | §4 below and [product-realization.md](product-realization.md) |
| TP-G1 | PROVED: bounded real action image for homomorphic realizations of this product group | §6.2 and product-realization companion |
| TP-C1 | PROVED: exact adverse normalized local factor for this carrier; inherited CRT scope retained | §6.3, TP-L1 and the cited checkpoint |
| TP-X1 | EXPERIMENTAL: exhaustive exact corroboration of the fixed one-block model | [data](../../../examples/2026-09-16-two-prime-character.json), [code](../../../experiments/two_prime_character.py), §8 |

All claims use the fixed polynomial $Q=x^2+xy+y^2$; every modular statement
specifies its ring. The lead inspected both written proofs; independent
reviews and file identities are recorded in [verification.md](verification.md)
and [manifest.json](manifest.json). No external review or novelty is claimed.
TP-G1 in this report is the theorem labeled TP-R1 in the companion;
TP-R2 is its separate, explicitly zero-preserving projection obstruction.

## 2. Exact carrier, action and arithmetic reason for the primes

Let $\chi_p$ be the quadratic character, with $\chi_p(0)=0$. Set

$$R=\mathbb F_7\times\mathbb F_{19}\cong\mathbb Z/133\mathbb Z,$$
$$D=\{(a_7,a_{19})\in R^\times:
                    \chi_7(a_7)=\chi_{19}(a_{19})\}.
\tag{1}$$

There are $3\cdot9$ scalars for each common sign, so $|D|=54$ and
$|D^2|=2916$. This is a genuine correlation: the two residue projections
are individually surjective onto the units, but half their combinations
are excluded. Each of the two input scalars must lie in the same $D$;
their signs need not agree with each other.

Both primes are $1\pmod3$, so the Eisenstein algebra splits. More
specifically they are $7\pmod{12}$; $-1$ and $3$ are nonsquares at both.
Thus the same canonical character quotient can couple them, and simultaneous
negation preserves $D$. This explains the arithmetic selection, while the
known no-defect theorem explains its limitation.

The roots of $X^2+X+1$ are $(2,4)$ at $7$ and $(7,11)$ at $19$.
For either prime write them $(\zeta_p,\bar\zeta_p)$. In
$E_p=\mathbb F_p[\omega]/(\omega^2+\omega+1)$, all norm-one elements
are parametrized by

$$g_p(t_p)\longleftrightarrow(t_p,t_p^{-1}),\qquad
t_p\in\mathbb F_p^\times.
\tag{2}$$

The coordinates here are evaluation at the two roots, and their product
is the norm. Explicitly, $g_p=\alpha_p+\beta_p\omega$, where

$$\beta_p=\frac{t_p-t_p^{-1}}{\zeta_p-\bar\zeta_p},\qquad
\alpha_p=t_p-\beta_p\zeta_p.$$

The denominators are nonzero in their finite fields. The full group is

$$G=H_7\times H_{19}\cong C_6\times C_{18},\qquad |G|=108.
\tag{3}$$

For $x,y\in D$ act at each prime by the established norm action

$$T_{\alpha+\beta\omega}(x,y)
=(\alpha x+\beta y,-\beta x+(\alpha-\beta)y).
\tag{4}$$

All arithmetic in (4) is in $R$. Define the exact return count by

$$r(x,y)=\#\{g\in G:T_g(x,y)\in D^2\}.
\tag{5}$$

Both transformed scalar coordinates must have nonzero residues at both
primes and satisfy (1). We never count mere return to the ambient ring.

### Stabilizers and projection

The split state coordinates are
$(x_p-\zeta_py_p,x_p-\bar\zeta_py_p)$. Their transformation is diagonal
with multipliers $(t_p,t_p^{-1})$. At least one state coordinate is nonzero
because $x_p,y_p\ne0$ and the roots differ. A fixing multiplier must
therefore have $t_p=1$. All local and product stabilizers on the carrier
are trivial, including nonzero isotropic states.

Split-coordinate recovery and the CRT map are bijections **inside the finite
model**, so every counted return gives a distinct modular scalar pair.
Neither map is asserted to preserve $Q$ as an equality of real numbers.
No real scalar carrier is silently substituted for $D$.

## 3. Complete one-block return distribution

**PROVED by TP-L1; independently corroborated by exact enumeration.**

| Returns $r$ | Ordered pairs |
|---:|---:|
| 8 | 216 |
| 10 | 270 |
| 12 | 216 |
| 18 | 108 |
| 24 | 648 |
| 26 | 702 |
| 30 | 540 |
| 54 | 216 |
| **Total** | **2916** |

| Statistic | Exact value or stated approximation |
|---|---|
| Number of scalar inputs / actions | $54$ / $108$ |
| Fraction with $r=1$ | $0$ |
| Minimum / maximum | $8$ / $54$ |
| Median | $25$; lower and upper central values are $24,26$ |
| Mean | $218/9$ |
| Geometric mean | $2^{5/3}3^{7/9}5^{5/18}13^{13/54}\approx21.63420053$ |
| Mean logarithmic return $\mu$ | $(5/3)\log2+(7/9)\log3+(5/18)\log5+(13/54)\log13\approx3.07427542$ |
| Stabilizer distribution | Size one on all 2916 pairs |
| Distinct returned-pair distribution | Exactly the return histogram above |
| Full modular image | $130$ values |
| Reciprocal return sum | $\sum_{D^2}1/r=154$ |

Only the displayed decimal summaries use floating point. All membership,
equality, histograms, fractions and return sets were checked exactly.

### 3.1 Why these counts hold

For a local norm orbit, let $A_p$ count each equal-sign class $(+,+)$ or
$(-,-)$ and $B_p$ count each opposite-sign class $(+,-)$ or $(-,+)$.
Classify a norm as $0,+,-$ according to zero, nonzero square, or nonsquare.
The complete local table is

| Prime | Norm type | $A_p$ | $B_p$ | Number of such orbits |
|---|---|---:|---:|---:|
| 7 | 0 | 3 | 0 | 2 |
| 7 | + | 0 | 1 | 3 |
| 7 | − | 1 | 2 | 3 |
| 19 | 0 | 9 | 0 | 2 |
| 19 | + | 2 | 5 | 9 |
| 19 | − | 5 | 4 | 9 |

For nonzero norm $N$, put $t=y/x$. The equation is
$x^2=N/(1+t+t^2)$. Each admissible slope has two opposite roots of
opposite character, since $-1$ is nonsquare. Among square slopes at $7$,
$t=1$ gives nonsquare $1+t+t^2$ and $t=2,4$ give zero. Among square
slopes at $19$, the nonzero polynomial values are squares exactly at
$t=6,16$. This determines $A_p$. The orbit contains $p-1$ points;
four axis points must be deleted precisely when $N$ is square, giving
$2(A_p+B_p)=p-1-4\mathbf1_{\chi_p(N)=1}$. Each isotropic line instead
has $A_p=(p-1)/2$, $B_p=0$. The companion displays every residue used.

Matching both scalar character signs across the primes now gives

$$r=2(A_7A_{19}+B_7B_{19}).
\tag{6}$$

For each pair of prime orbits, (6) is both its number of admissible input
pairs and the return count of every such pair. Multiplying by the orbit
counts gives the histogram. This counts the correlation directly; it does
not multiply unrelated marginal return probabilities.

### 3.2 Full fibers, zeros, and returns are different counts

The modular image consists of all of $R$ except the three values
$(N_7,0)$ with $N_7$ a nonzero square. Its fiber distribution is

| Fiber size | Number of outputs |
|---:|---:|
| 8 | 27 |
| 10 | 27 |
| 24 | 36 |
| 26 | 27 |
| 36 | 3 |
| 60 | 9 |
| 216 | 1 |

The zero-norm fiber has 216 inputs in four distinct multiplier orbits,
each with 54 returns. These are nonzero vectors with trivial stabilizer;
they are not the fixed zero pair. This explains why the 154 occupied
action orbits give an upper bound larger than the 130 polynomial values.

Negation alone already gives two returns on every pair. The exact bound
$r\ge8$ is stronger: even after identifying returning labels up to the
common sign, there are at least four classes. Still, neither this fact nor
the positive mean log return claims a benefit exclusive to two-prime
correlation; the independent control was not enumerated.

## 4. Product theorem and exceptional-pair tails

For every $d\ge1$, define the formal block system

$$\mathscr R_d=R^d,\qquad \mathcal D_d=D^d,\qquad G_d=G^d,$$
$$Q_d(\mathbf x,\mathbf y)
=(Q(x_1,y_1),\ldots,Q(x_d,y_d)).
\tag{7}$$

Then $|\mathcal D_d|=54^d=e^{ad}$, with $a=\log54$, and there are
$2916^d=e^{2ad}$ ordered pairs. These elements are finite-ring vectors,
not real numbers.

**TP-P1 — PROVED.** The legal returning label set is exactly the product
of the one-block returning label sets. Hence

$$R_d(\mathbf x,\mathbf y)=\prod_{i=1}^d r(x_i,y_i),
\qquad 8^d\le R_d(\mathbf x,\mathbf y)\le54^d.
\tag{8}$$

Membership in $D^d$ is equivalent to membership in $D$ in every block,
so both directions of the factorization follow. Distinct tuples of
multipliers remain distinct in $G^d$, and stabilizers remain trivial.
No multiplication of all block labels into a single scalar multiplier is
part of this theorem. There is no additional global product-norm constraint:
the entire vector $Q_d$ is preserved.

The strongest uniform lower bound supplied here is $8^d$, attained by
choosing a minimum-return pair in each block. It has **zero exceptional
pairs**. In the requested exponential notation one can take
$r_* =\log8$ and, for example, $\delta=1$ for this modular theorem.

### 4.1 Exact law and typical exponent

Let $h_k$ be the histogram in §3. A choice of block counts $m_k\ge0$,
$\sum m_k=d$, contributes

$$\frac{d!}{\prod_k m_k!}\prod_k h_k^{m_k}
\quad\text{pairs with return count }\prod_k k^{m_k}.
\tag{9}$$

If several count vectors yield the same integer return count, their
populations are added. Formula (9) is an exact distribution for every $d$.
Uniform pairs in $(D^d)^2$ are precisely independent uniform choices from
$D^2$ at each block; this proves the independence used here without removing
the two-prime correlation within any block.

For $\theta>0$ put

$$M(\theta)=\frac1{2916}\sum_k h_k k^{-\theta}.$$

Multiplying the finite sums gives
$\mathbb E(R_d^{-\theta})=M(\theta)^d$, and the elementary inequality
$\mathbf1_{R_d<e^{rd}}\le e^{\theta rd}R_d^{-\theta}$ gives

$$\#\{R_d<e^{rd}\}\le
\exp\bigl((2a+\theta r+\log M(\theta))d\bigr).
\tag{10}$$

Since $(\log M)'(0)=-\mu$, every fixed $r<\mu$ has a sufficiently
small positive $\theta$ with a positive deficit
$\delta_r=-\theta r-\log M(\theta)>0$. The analogous positive moment
bounds the upper tail for $r>\mu$. Thus $d^{-1}\log R_d$ concentrates
at the exact $\mu$ in §3, with exponential tails at every fixed distance.
This is a counting theorem, not an extrapolation from small $d$.

An explicit stronger-than-minimum tail needs no limiting choice:

$$M(1)=\frac{77}{1458},\qquad
\#\{R_d<18^d\}\le2916^d\left(\frac{77}{81}\right)^d=2772^d.
\tag{11}$$

Thus $r_* =\log18$ and $\delta=\log(81/77)>0$ work locally.
The exceptional set consists exactly of the block tuples whose sum of log
returns is below $d\log18$. Equation (11) is an upper bound on its size;
(9) gives its exact count if desired.
No product carrier was enumerated and no larger finite schedule was needed.

## 5. Applying the existing return-to-image theorem

HR-1 is a finite-fiber counting statement. It applies to the observable
$Q_d$ just as to a real-valued observable: one may encode its finite output
labels injectively as real numbers without changing its fibers. That
encoding does **not** turn the observable into scalar $Q$ on real inputs.

There is no stabilizer or scalar-projection loss inside the modular model.
Using (8) in HR-1 gives the local bound

$$|Q_d(\mathcal D_d,\mathcal D_d)|
\le\frac{54^{2d}}{8^d}.
\tag{12}$$

The already proved reciprocal version gives the stronger certificate

$$|Q_d(\mathcal D_d,\mathcal D_d)|
\le\sum_{\mathcal D_d^2}\frac1{R_d}
=\left(\sum_{D^2}\frac1r\right)^d=154^d.
\tag{13}$$

All-support coverage is explicit: every ordered pair is included and the
exception set for (12)–(13) is empty. The actual image is even smaller,
exactly $130^d$, because the coordinatewise image in (7) is the product
of the one-block images. In contrast, (11) would give the valid but weaker
threshold bound $162^d+2772^d$.

These are **PROVED modular support bounds**. No bound on
$|Q(A_d,A_d)|$ for an exponentially growing real scalar set is established.
The missing real equality is addressed next, not assumed.

## 6. Why the local gain fails in the audited global realizations

### 6.1 CRT representatives do not preserve real norm values

Writing each residue as an integer in $[0,132]$ is injective as a set map,
but only preserves $Q$ modulo $133$. For example $1,132\in D$ and

$$Q(1,1)=3,\qquad Q(132,132)=52272=3+393\cdot133.
\tag{14}$$

The modular multiplier $-1$ relates these pairs, whereas their real norms
differ. Thus taking representatives does not prove scalar return legality.
Likewise $R^d$ is not the ring $\mathbb Z/133^d\mathbb Z$; digit carries
and cross terms prevent treating those two structures as identical.

### 6.2 TP-G1: every group-compatible real realization has bounded action image

State the realization hypothesis explicitly. Suppose a scalar map
$f:D^d\to A_d\subseteq\mathbb R$ is used in **both** coordinates and a
group homomorphism

$$\rho:G^d\longrightarrow
\{\alpha+\beta\omega:\alpha,\beta\in\mathbb R,
                          \ \alpha^2-\alpha\beta+\beta^2=1\}
\tag{15}$$

intertwines every counted local return with the corresponding real action:

$$T_g(\mathbf x,\mathbf y)=(\mathbf x',\mathbf y')\in(D^d)^2
\quad\Longrightarrow\quad
T_{\rho(g)}(f(\mathbf x),f(\mathbf y))
=(f(\mathbf x'),f(\mathbf y')).
\tag{16}$$

This is the natural exact realization that would preserve the product
action theorem. It is an explicit hypothesis, not a claim about all possible
nonhomomorphic or state-dependent lifts.

Every $g\in G^d$ satisfies $g^{18}=1$. Hence $\rho(g)^{18}=1$.
In $\mathbb C$, the polynomial $Z^{18}-1$ has at most 18 roots. Therefore

$$|\rho(G^d)|\le18.
\tag{17}$$

The conclusion is independent of the number or degrees of auxiliary fields,
and it holds even if the scalar map is not injective. Every real pair has
at most 18 distinct returns supplied by (15); at $(0,0)$ it has just one.

If $M$ local labels return a parameter pair, at least $\lceil M/18\rceil$
of them project to the same scalar returned pair. Thus the duplicate-label
factor $\nu$ in HR-1 satisfies

$$\nu\ge M/18,\qquad M/\nu\le18.
\tag{18}$$

For a typical local $M=e^{\mu d+o(d)}$, the necessary logarithmic duplicate
loss is at least $\mu d-O(1)$. It consumes the whole raw return rate.
Using a global maximum projection multiplicity in HR-1 cannot improve this
pointwise bound. An injective same-set realization is impossible once
$8^d>18$, since it would project all $8^d$ distinct returned pairs
injectively into at most 18 targets; in particular this already fails for
$d\ge2$.

This is a **PROVED scoped obstruction to group-compatible realization**,
not an image lower bound for every real lift. Lifts that break the finite
group law are outside (15); they cannot inherit (8) without a new exact
Cartesian return argument. None is constructed or conjectured here.

### 6.3 TP-C1: normalized CRT costs are adverse too

Relative to the entire residue ring, the scalar input density is
$(54/133)^d$ and the output density is $(130/133)^d$. Input thinning
must be paid in both coordinates. Their normalized ratio is

$$\frac{(130/133)^d}{(54/133)^{2d}}
=\left(\frac{133\cdot130}{54^2}\right)^d
=\left(\frac{8645}{1458}\right)^d>1.
\tag{19}$$

Thus the normalized local contribution to the standard CRT packing rate
is

$$\Delta_{\rm CRT}
=2\log(54/133)-\log(130/133)
=\log(1458/8645)<0.
\tag{20}$$

Equation (20) is already unfavorable before any further height, modulus,
discriminant or packing cost. The inherited theorem actually precludes a
normalized defect for arbitrary correlations in these depth-one factors;
we have not discovered a loophole by conditioning characters.
This statement concerns that normalized certificate, not all possible
realizations or the size of an arbitrary real polynomial image.

The product-realization companion also records a separate zero-preserving
norm-projection obstruction with its additional hypothesis. It is not needed
for (17)–(20), and we do not turn modular zero-norm states into uncharged
real exceptions.

## 7. Fully charged signed-rate ledger

This ledger follows the [construction template](../../templates/CONSTRUCTION_LEDGER.md).
Fix the primes, carrier and group first; only the block number $d$ grows.

| Gain or cost | Exact rate/accounting | Status |
|---|---|---|
| Modular input lower and upper counts | Both exactly $54^d$; $a=B=\log54$ | PROVED |
| Relative carrier density | $(54/133)^d$; squared loss for the input pair | PROVED |
| Raw return gain | Uniform $\log8$; typical $\mu$ in §3 | PROVED in the finite product |
| Exceptional pairs | None for threshold $8^d$; at most $2772^d$ for $18^d$; deficit $\log(81/77)$ | PROVED in the finite product |
| Local stabilizers / projections | Stabilizer and projection fibers one; every coordinate is a unit | PROVED |
| Local full support | Reciprocal HR-1 bound $154^d$; actual modular image $130^d$ | PROVED |
| Real action duplicates | At least $M/18$ for $M$ returning local labels; effective real return count at most 18 | PROVED under (15)–(16) |
| Net real return rate | Raw rate minus necessary duplicate loss is at most zero | FAILED positive-rate gate for compatible lifts |
| Normalized CRT rate | $\log(1458/8645)<0$ per block, with input density charged twice | FAILED normalized CRT gain |
| Real scalar input count | No compatible injective realization for $d\ge2$; no alternative growing real carrier constructed | OPEN outside the stated realization |
| Field degree/discriminant/regulator/class number | No growing number field is used locally. An alternative arithmetic realization would need its own bounds; none is set to zero | Not supplied; no favorable rate inferred |
| Denominators and integrality | Local inverses exist in the fields; they do not supply rational or algebraic-integer denominators of a real lift | No free lift assumed |
| Archimedean and coefficient heights | Absent from the finite ring, unpaid for another real lift; norm equality already fails for canonical representatives (14) | No favorable bound inferred |
| CRT repeats, branches and carries | Formal factors are independent blocks; repeated prime powers and scalar digits are different structures | No automatic scalar tensorization |
| Input thinning, both coordinates | Charged explicitly in (19); no hidden replacement of the full modular square by selected pairs | PROVED |
| Real output exponent and valid $c>0$ | None follows from this architecture; a constant effective return bound cannot give a fixed positive exponent | FAILED certificate, target OPEN |
| Difference set / affine transfer | Not investigated because the homogeneous real gate failed | GATED, not an additive obstruction |

The modular image exponent $\log130<2\log54$ is genuine in the finite
product but is not a real exponent. Unknown realization costs are not zero.
The two failures above are alternative audits: do not subtract both as if
they were two losses in one already constructed real carrier.

## 8. Exact computation and reproducibility

The one-block diagnostic was frozen before execution. It enumerates all
$133^2$ coefficient candidates for the norm-one group, all 2916 input pairs,
and all 108 actions for each pair. A separate oracle works in the four split
field coordinates, diagonalizes the action, and reconstructs both returned
coordinates. For every input it agrees on the complete returned-pair set
(via canonical set hashes), return count and norm. No smaller action window
or sampled pair set is used.

Reproduction command, using new output filenames because overwrites are refused:

```bash
python3 -m experiments.two_prime_character \
  --output NEW_SUMMARY.json \
  --pairs-output NEW_PAIRS.json
```

The actual summary is [examples/2026-09-16-two-prime-character.json](../../../examples/2026-09-16-two-prime-character.json).
All per-pair counts, norms, stabilizers, distinct-return counts and returned
set hashes are retained locally in
`local-only/runs/T03/2026-09-16-two-prime-character/pairs.json`.
The summary also contains every strict threshold tail from 1 through 109,
full image multiplicities, exact mean and geometric-mean expression, runtime,
source hash and parameter definitions. No random seed is used.

| Diagnostic charge | Count |
|---|---:|
| Main norm-one coefficient candidates | 17,689 |
| Main polynomial evaluations | 2,916 |
| Main action–pair tests | 314,928 |
| Oracle local norm candidates | 410 |
| Oracle ring-polynomial evaluations | 2,916 |
| Oracle action–pair tests | 314,928 |
| **Exact diagnostic total** | **653,787** |

The oracle's two component norms constitute one evaluation of $Q$ in $R$.
The run used Python 3.12.7 and **0.691836 research CPU seconds**. It was run
once. The analytic table was derived independently before that run; its
agreement corroborates the proof rather than establishing an asymptotic
claim by fitting finite data.

Required code regressions subsequently passed: **42 tests and 159 finite
baseline checks**. They are validation, not new carrier searches. A local
guard conservatively charged every project Python function call, including
helper calls and generator resumptions, for these regressions. Including a
retained failed wrapper import attempt, this added **82,570 charges**.
Total cycle usage is therefore **736,357 charges and 3.607404 CPU seconds**,
below both caps. The first wrapper attempt omitted the repository from its
import path; it ran no mathematical test, was fixed locally, and its six
charged import calls and CPU time remain included. The diagnostic itself
had no failed run or rerun.

Local repository/reference checks, full code-inspection scope, errors,
preservation hashes and validation commands are recorded in
[verification.md](verification.md). No network access, download, package
installation, imported historical program or literature search was attempted.

## 9. Final disposition and exact failure scope

$$\boxed{\text{LOCAL GO / GLOBAL FAIL.}}$$

There is positive **modular** typical return entropy, even a uniform lower
bound. The exact tensor theorem holds in the finite product. It does not
produce exponentially many distinct genuine real Cartesian returns under
a realization preserving this finite group action: (17) bounds them by 18.
The conventional normalized CRT contribution is separately negative.

The failure registry therefore closes this specified **finite-residue
product plus group-compatible scalar realization** as a power-saving return
certificate. It does not rule out other norm-symmetry actions, nonhomomorphic
lifts with independently proved returns, other scalar carriers, or the
underlying full-rank quadratic target. HR-N1's earlier, different obstruction
is preserved rather than reused as evidence for TP-G1.

No homogeneous real saving survived, so there is no difference-set exponent
to report and no attempt to transfer to $P_0=Q+x$. This is a failure at the
norm-return realization gate, not a statement that the additive structure
is bad. No full-rank extension of corrected C0 is claimed.

## 10. One next proof obligation only

Retain the already selected **T03-O4 / RC15/4**, not a repair of this model.
On every sufficiently large actual adaptive level $\mathcal A_m$, with
$F_m=\mathbb Q(\mathcal A_m)$, $n_m=2^{m+1}$,
$s_m=|Q(\mathcal A_m,\mathcal A_m)|$ and $M_m=\max|\mathcal A_m|$,
seek fixed $H,m_0$ and explicit choices

$$C_m^\dagger\in F_m,\quad C_m^\dagger>M_m,\quad
B_m\subseteq\mathcal A_m,\quad n_m-|B_m|\le H\sqrt{n_m},$$
$$C_m^\dagger+a=\gamma_m u_a^2,
\quad \gamma_m,u_a\in F_m\text{ positive},\quad
U_m=\{\pm u_a:a\in B_m\},$$

with the whole signed-root bound

$$|\gamma_mQ(U_m,U_m)|\le\frac{15}{4}s_m+Hn_m^{3/2}.$$

This is the existing OPEN obligation from T03 current state §§7, 13–14;
it has not been pursued during this cycle. The real quadratic target, ARG,
TCRC and RC15/4 remain OPEN. No second next conjecture or new research
program is adopted here.
