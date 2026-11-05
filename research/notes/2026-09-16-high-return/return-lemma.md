# HR-1 — full-image bounds from partial returns

Date/version: **2026-09-16, version 1**. Branch: the newly commissioned
constructive high-return cycle, Stage 1. The fixed benchmark is
$q(x,y)=x^2+xy+y^2$; the combinatorial theorem applies to any one fixed
polynomial $P\in\mathbb R[x,y]$. Neither T03's target nor its actual
adaptive sequence is replaced by this general criterion.

**Status: PROVED**, by the complete internal derivation below. The parent
agent independently inspected the core fiber-partition argument and then
reviewed all written variants in this task. Application
to a growing carrier remains **CONDITIONAL** on every stated hypothesis;
no candidate, positive return rate, or target exponent is established here.

## Scope, provenance, and inherited content

The current user commissioned a constructive high-return cycle. This
Stage-1 subtask proves the return-to-support implication before searching
for a carrier. Budget: symbolic proof only, **zero experiments and zero
network calls**. Previous-cycle files and historical records are immutable.

The basic injective Eisenstein return criterion is inherited. Its source is
`local-only/migration/research_supplement/T03/T03_RESEARCH_RECORD_20260910.zip`,
member `output/Quadratic_Norm_Form_Focused_Offline_Report.md`, §6, Lemma 6.1.
Its coordinate action is summarized in SN-T03-1 of the
[study note](../2026-09-14-study-notes/03-eisenstein.md). The preceding cycle's
[NT-20260916-5](../2026-09-16-solvable-norm-trace/README.md#4-nt-20260916-5--a-zero-safe-multiplier-support-certificate)
independently rederived that criterion, explicitly charged the zero pair,
and required a strict exponent when absorbing constants.

This note derives the extensions to partial transformations, repeated labels,
stabilizers, noninjective scalar input projection, and pointwise reciprocal
counts. These are new derivations in the present task, not claims of
external novelty. No literature or priority assessment was performed.

Startup orientation retained the master handoff, setup/map/audit, migration
conflicts, T03 current-state export, SPEC/STATUS, and the relevant prior
notes. In particular, `local-only/migration/sources/T03_CURRENT_STATE.md`,
§§5.2 and 12–14, distinguishes an available norm-preserving action from
the missing full Cartesian support bound. Its old next-step instructions
are historical; the present Stage-1 assignment comes from the current user.
The unavailable standalone F25 certificate is not used. The proofs below
have no unavailable source dependency.

## 1. Exact setup: labels, returned states, and scalar pairs

Let $A\subset\mathbb R$ be nonempty and finite, $n=|A|$, and put $X=A^2$.
Let $S$ be a nonempty finite set of actual parameter states with a
**surjection**

$$\pi:S\longrightarrow X.$$

Thus every scalar ordered pair is represented. Define the actual scalar
output function

$$F:S\longrightarrow\mathbb R,\qquad F(s)=P(\pi(s)).$$

Here $P((a,b))$ means $P(a,b)$. Surjectivity gives
$F(S)=P(A,A)$. If a candidate instead records an auxiliary invariant $H$,
it must prove an exact identity $F=\chi\circ H$ before preservation of
$H$ can be used. Preservation of an unrelated norm or trace is insufficient.

Let $\mathcal L$ be a finite set of labels. A label may describe the same
transformation as another label. For each $\ell\in\mathcal L$, let
$T_\ell$ be a single-valued partial map from $S$ to an ambient state set
containing $S$. Retain precisely the **legal returns**

$$
\mathcal R(s)=\{\ell\in\mathcal L:
  T_\ell(s)\text{ is defined},\ T_\ell(s)\in S\}.
$$

Assume the scalar identity

$$F(T_\ell(s))=F(s)\qquad(\ell\in\mathcal R(s)).\tag{1}$$

All denominator, field-membership, interval, branch, and Cartesian
membership conditions belong in this definition of a legal return.
No group law, invertibility, or closure of the label set is assumed.

For $s\in S$, define

$$
R(s)=|\mathcal R(s)|,\qquad
\mu(s)=\max_{t\in S}|\{\ell\in\mathcal R(s):T_\ell(s)=t\}|,
\tag{2}
$$

with $\mu(s)=1$ when $R(s)=0$. When $R(s)>0$, $1\le\mu(s)\le R(s)$.
The number of **distinct returned parameter states** is at least
$R(s)/\mu(s)$. Counting labels alone does not give that conclusion with
$\mu=1$.

For scalar projection, write

$$h=\max_{x\in X}|\pi^{-1}(x)|.$$

There are at least $R(s)/(h\mu(s))$ distinct returned scalar pairs. A
sharper bound uses the directly measured scalar multiplicity

$$
\nu(s)=\max_{x\in X}
 |\{\ell\in\mathcal R(s):\pi(T_\ell(s))=x\}|\le h\mu(s),
\tag{3}
$$

where $\nu(s)=1$ for $R(s)=0$.

## 2. Threshold theorem with singular exceptions

**HR-1(a), PROVED.** In the setup above, let $E\subseteq S$, and suppose
that fixed numbers $M>0$ and $\mu_*\ge1$ satisfy

$$R(s)\ge M,\qquad\mu(s)\le\mu_*\qquad(s\in S\setminus E).\tag{4}$$

Then

$$
\boxed{|P(A,A)|\le\frac{|S|\mu_*}{M}+|F(E)|.}\tag{5}
$$

In particular, since $|S|\le hn^2$,

$$|P(A,A)|\le\frac{hn^2\mu_*}{M}+|F(E)|.\tag{6}$$

If the stronger direct bound $\nu(s)\le\nu_*$ is known outside $E$,
then one also has

$$|P(A,A)|\le\frac{n^2\nu_*}{M}+|F(E)|.\tag{7}$$

The exception charge may always be replaced by either $|\pi(E)|$ or
$|E|$, but using $|F(E)|$ can be sharper when many singular states have
one known output.

### Proof

For each $y\in F(S)\setminus F(E)$, choose a state $s$ with $F(s)=y$.
It lies outside $E$. By (1), all its returned states lie in the full fiber
$F^{-1}(y)$. By (2) and (4), that fiber contains at least $M/\mu_*$
distinct states. These fibers are disjoint subsets of $S$. Therefore

$$|F(S)\setminus F(E)|\le |S|\mu_*/M.$$

Adding at most $|F(E)|$ remaining outputs proves (5). Bound (6) follows
from the projection-fiber estimate. For (7), project the returned states:
at most $\nu_*$ return labels produce any one scalar pair, so the
corresponding scalar fiber in $X$ has at least $M/\nu_*$ distinct points.
Disjoint scalar fibers fit inside $X$, whose size is $n^2$. $\square$

Ceilings can sharpen these bounds: replace $M/\mu_*$ or $M/\nu_*$
by its ceiling when counting a nonempty fiber. The displayed forms suffice
for exponent accounting. If $S\setminus E$ is empty, the proof and bounds
remain valid through the exception term.

### Chosen-lift version: no regularity of all parameter lifts is needed

**HR-1(a'), PROVED.** Let $E_{\rm sc}\subseteq A^2$ be a set of exceptional
**scalar pairs**. For each $p\in A^2\setminus E_{\rm sc}$ choose just one
lift $s(p)\in\pi^{-1}(p)$. Fix $h_*,\Lambda\ge1$.
Suppose this chosen lift has at least $M>0$
legal return labels, at most $h_*$ of those labels land at any one target
state, and at most $\Lambda$ distinct returned target states project to any
one scalar pair. These hypotheses are required only for the chosen lifts;
there is no condition on the other elements of $\pi^{-1}(p)$.

Then

$$
\boxed{
|P(A,A)|\le
\frac{n^2}{\lceil M/(h_*\Lambda)\rceil}+|P(E_{\rm sc})|
\le\frac{n^2h_*\Lambda}{M}+|E_{\rm sc}|.
}\tag{7a}
$$

Here $P(E_{\rm sc})=\{P(a,b):(a,b)\in E_{\rm sc}\}$.
The returned-state projection bound $\Lambda$ may be smaller than the
global fiber bound $h$ used earlier. If it is not known separately, take
$\Lambda=h$.

**Proof.** For each chosen lift, removing repeated target states leaves at
least $M/h_*$ states; projection leaves at least $M/(h_*\Lambda)$ scalar
pairs. They have the same actual scalar output by (1). Since their number
is integral, the full scalar output fiber has at least
$\lceil M/(h_*\Lambda)\rceil$ members. Every output outside
$P(E_{\rm sc})$ has such a representative, and its full scalar fiber is
disjoint from those of all other outputs. At most $n^2$ scalar pairs are
available. This proves (7a), including all exceptional outputs. $\square$

If the same chosen lifts satisfy just the raw duplicate bound $h_*$, their
parameter fibers instead give the complementary bound

$$|P(A,A)|\le |S|h_*/M+|P(E_{\rm sc})|.\tag{7b}$$

Indeed, every output outside $P(E_{\rm sc})$ has one chosen lift and hence
at least $M/h_*$ parameter states in its full output fiber. This requires
neither a threshold on all lifts nor an extra factor $\Lambda$ in the
raw-state count. Use the better certified bound; do not charge the same
projection loss in both its numerator and its input-size conversion.

## 3. Pointwise reciprocal variants

No uniform return threshold is needed for the following bounds. They
measure the full distribution of **distinct** returns, including its tail.

Define

$$
\rho(s)=
\begin{cases}
\min\{1,\mu(s)/R(s)\},&R(s)>0,\\
1,&R(s)=0.
\end{cases}
$$

**HR-1(b), PROVED.** For every $E\subseteq S$,

$$
\boxed{|P(A,A)|\le |F(E)|+
       \sum_{s\in S\setminus E}\rho(s).}\tag{8}
$$

In particular, $E=\varnothing$ gives the pointwise reciprocal estimate
$|P(A,A)|\le\sum_{s\in S}\rho(s)$.

### Proof

Put $r_S(y)=|F^{-1}(y)|$. Each nonempty fiber contributes exactly one to

$$|F(S)|=\sum_{s\in S}\frac1{r_S(F(s))}.\tag{9}$$

For every $s$, preservation and duplicate counting imply
$r_S(F(s))\ge\max\{1,R(s)/\mu(s)\}$, with the no-return case treated
by the lower bound one. Hence $1/r_S(F(s))\le\rho(s)$.

For the exception version, split the output set into $F(E)$ and its
complement. Every state above an output in the complement lies outside
$E$, so applying (9) just to those fibers and then enlarging the sum to all
$S\setminus E$ proves (8). The exception term is a count of outputs, not
a replacement of part of a fiber by an unjustified fraction. $\square$

### Direct scalar reciprocal bound

Define $\rho_{\rm sc}(s)$ by replacing $\mu(s)$ with $\nu(s)$ in the
definition of $\rho(s)$; the no-return value is again one. Then

$$
\boxed{
|P(A,A)|\le
\sum_{x\in A^2}\min_{s\in\pi^{-1}(x)}\rho_{\rm sc}(s).
}\tag{10}
$$

Indeed, write $r_X(y)=|\{x\in A^2:P(x)=y\}|$. For every lift $s$ of
$x$, distinct projected returns give
$r_X(P(x))\ge\max\{1,R(s)/\nu(s)\}$. Thus
$1/r_X(P(x))\le\rho_{\rm sc}(s)$ for **each** lift; it remains true
after taking their minimum. Sum the scalar version of (9) over $x\in A^2$.
If only $h\mu(s)$ is known as an upper bound for $\nu(s)$, it gives a
valid, possibly weaker summand.

For the chosen-lift setup, define $\rho_{\rm sec}(p)$ as any proved upper
bound on the reciprocal of its full scalar fiber; for example use
$\min\{1,h_*(p)\Lambda(p)/R(s(p))\}$ when there is a return, and one
when there is none. The same fiber sum gives

$$
|P(A,A)|\le |P(E_{\rm sc})|+
\sum_{p\in A^2\setminus E_{\rm sc}}\rho_{\rm sec}(p).\tag{10a}
$$

To see why the exception-image term is legitimate, apply the exact fiber
sum only to outputs outside $P(E_{\rm sc})$. All pairs above those
outputs lie outside $E_{\rm sc}$, so their chosen-lift bounds are valid.
Enlarging to the full displayed sum only increases the right-hand side.

The minimum in (10) does not assert an efficient algorithm for finding a
good lift. An explicit construction must identify the needed lift or prove
the displayed minimum bound uniformly. Averaging $R(s)$ over the carrier
does not replace (8) or (10): a few very large fibers can coexist with
quadratically many singleton outputs.

## 4. Stabilizers, duplicate transformations, and zero

For a genuine group action on an ambient state set, let labels represent
elements $g_\ell\in G$. Fix $b\ge1$ and suppose at most $b$ labels represent any one group
element. If $H_s=\operatorname{Stab}_G(s)$, the distinct elements sending
$s$ to a specified target lie in one left coset of $H_s$. Consequently

$$
\mu(s)\le b\sup_{g\in G}|\{g_\ell:\ell\in\mathcal L\}\cap gH_s|
\qquad\text{when }R(s)>0.
\tag{11}
$$

In particular, $\mu(s)\le b|H_s|$ when the stabilizer is finite.
Intersecting with the legal-return conditions can only decrease this
multiplicity. If the stabilizer is infinite, a finite coset-intersection
bound for the chosen labels is needed; an infinite bound is no certificate.
For transformations without a group model, definition (2) is the required
replacement. Distinct formulas or parameter words are not a proof of
distinct target states.

### Eisenstein specialization and the inherited zero correction

Let $L\subset\mathbb R$ be a field, $\omega^2+\omega+1=0$, and use
$S=A^2$, $\pi$ the identity. For distinct norm-one elements
$u=r+s\omega\in L(\omega)$, the inherited action is

$$T_u(a,b)=(ra+sb,-sa+(r-s)b).$$

It satisfies $(a'-\omega b')=u(a-\omega b)$ and therefore preserves
$q(a,b)$. At a nonzero pair, $a-\omega b\ne0$ because $L$ is real.
Multiplication by distinct $u$ gives distinct elements of the field, so
$\mu=\nu=1$ there.

At $(0,0)$, every multiplier fixes the pair. If all labels return, then
$R=\mu=|\mathcal L|$ and the effective return count is **one**.
Either retain this correct multiplicity in (8), or place the zero pair
in $E$ and charge its single output in (5). Merely counting its large
$R$ with $\mu=1$ is invalid. The same alternatives apply to any singular
locus with large stabilizers: prove its multiplicity or charge its actual
exceptional outputs. This is why the previous cycle's zero correction is
retained rather than omitted in a generalized theorem.

If every nonzero pair outside a set $E$ has at least $M$ legal returns,
the specialization gives the inherited bound

$$|q(A,A)|\le n^2/M+|q(E)|\le n^2/M+|E|.$$

The first inequality can improve the older presentation when distinct
exceptional pairs are known to have the same output.

## 5. Bounded-fiber scalar input projection: charge it twice

Suppose the parameter carrier is $C$, $N=|C|$, with a surjection
$\varphi:C\to A$ having fibers at most $\kappa$. Use

$$S=C^2,\qquad \pi=\varphi\times\varphi.$$

Then

$$N/\kappa\le n\le N,\qquad |S|=N^2,\qquad h\le\kappa^2.\tag{12}$$

With an exact scalar preservation identity, (5) becomes

$$|P(A,A)|\le N^2\mu_*/M+|F(E)|.\tag{13}$$

The projection loss is paid **twice** when comparing this output count
against $n^2$, through $n\ge N/\kappa$. It must not be silently omitted,
nor should $\kappa^2$ be charged a second time to the raw-state output
term in (13). An equivalent, sometimes coarser scalar form follows from
$N\le\kappa n$:

$$|P(A,A)|\le n^2\kappa^2\mu_*/M+|F(E)|.\tag{14}$$

Field embeddings have $\kappa=1$ and preserve polynomial evaluation.
An arbitrary scalar trace projection need not preserve polynomial
evaluation; bounded fibers alone do not supply (1). For such a projection,
$P(\varphi(c),\varphi(d))$ must be the actual preserved observable.
An output projection, in contrast, can only decrease the number of
already-certified output values: if $F=\chi\circ H$, no upper bound on
fibers of $\chi$ is needed to infer $|F(S)|\le|H(S)|$.

Any thinning from an earlier carrier must occur before defining $C$, $S$,
and the legal returns above. Returns into a discarded part are no longer
legal. If thinning loses a factor in the input count, both coordinates
must pay it; a return bound proved before thinning cannot be reused
without checking survival.

## 6. Uniform signed rates and strict exponent conversion

**HR-1(c), PROVED implication; CONDITIONAL application.** Let $d\to\infty$
be the actual chosen growth parameter, not an unused ambient field degree.
For each $d$, suppose the setup and threshold theorem hold with data
$A_d,S_d,E_d,M_d,\mu_d$. Fix the polynomial and all rate constants before
$d$ grows. Assume

$$
ad-o(d)\le\log n_d\le Bd+o(d),\qquad a>0,
\tag{15}
$$

$$
\log|S_d|\le Cd+o(d),\qquad
\log\mu_d\le\beta d+o(d),\qquad
\log M_d\ge\gamma d-o(d),
\tag{16}
$$

and

$$|F_d(E_d)|\le\exp(ed+o(d)),\qquad e\ge0.\tag{17}$$

An empty exceptional image satisfies (17) with $e=0$; a bounded number of
singular outputs does too. Set

$$g=\max\{C+\beta-\gamma,e\},\qquad\delta=2a-g.$$

Then

$$|P(A_d,A_d)|\le\exp(gd+o(d)).\tag{18}$$

If $\delta>0$, every fixed

$$\boxed{0<c_P<\delta/B}$$

is eventually certified:
$|P(A_d,A_d)|\le|A_d|^{2-c_P}$. This supplies arbitrarily large sets
because $a>0$. No such data are constructed in this note.

### Proof

Insert (16)–(17) into (5); summing two exponential upper bounds gives
(18). From (15),

$$2\log n_d-\log|P(A_d,A_d)|\ge\delta d-o(d).$$

For fixed $c_P<\delta/B$, the upper input bound gives
$c_P\log n_d\le c_PBd+o(d)$, which is eventually less than the
preceding lower bound because $\delta-c_PB>0$. Rearranging proves the
constant-free inequality. Boundary exponents are not supplied by this
argument. $\square$

### Projection ledger in rates

If $S_d=C_d^2$,

$$
\alpha d-o(d)\le\log|C_d|\le B_0d+o(d),\qquad
\kappa_d\le e^{kd+o(d)},
$$

then one may use $a=\alpha-k$, $B=B_0$, $C=2B_0$, provided
$\alpha-k>0$. The net test is

$$
2(\alpha-k)-\max\{2B_0+\beta-\gamma,e\}>0.
\tag{19}
$$

When the parameter-input rate is exact, $\alpha=B_0$, the ordinary
return term requires $\gamma-\beta-2k>0$. This is the duplicate/stabilizer
cost plus the two coordinate-projection costs. There is also the separate
exception test $e<2(\alpha-k)$. Known better scalar input bounds may
improve the final exponent, but unknown fiber or thinning costs are not zero.

Equivalently, directly in terms of the actual scalar size $n\to\infty$,
if

$$
M\ge n^\epsilon,\qquad\mu_*\le n^b,\qquad
\kappa\le n^k,\qquad |F(E)|\le C_0n^{2-\eta},
$$

with fixed constants, $\eta>0$, and $\epsilon-b-2k>0$, then (14)
certifies every

$$0<c_P<\min\{\epsilon-b-2k,\eta\}.$$

A bound on the reciprocal sum in (8) can replace (16): if that sum is
at most $e^{\tau d+o(d)}$, use $g=\max\{\tau,e\}$ instead. This is
an alternative full-support certificate, not an inference from average
returns or collision energy.

## 7. Construction gate and unresolved obligations

| Required quantity | What HR-1 proves; what a carrier must supply |
|---|---|
| Fixed polynomial and same-set inputs | $P$ is fixed and $\pi$ covers every pair in one actual $A^2$. A selected set of engineered pairs does not meet this condition. |
| Actual lower and upper input counts | Required for (15); absent here. Parameter labels must be deduplicated, and input thinning/projection fibers charged twice. |
| Legal partial action | Exact preservation (1) and membership of each counted return are hypotheses, not consequences of a large norm-one family. |
| Duplicate labels and stabilizers | Must bound $\mu$ or the stronger projected multiplicity $\nu$. A singular fixed point may have $R\gg1$ but effective return one. |
| Zero and singular exceptions | Charge $|F(E)|$ if directly known, otherwise $|\pi(E)|$ or $|E|$. Every uncovered output is included. |
| Field degree, discriminant, regulator, units | None is used in the combinatorial implication. A proposed arithmetic construction must prove the effect on input counts and legal-return/exception rates. |
| Heights, denominators, local moduli and splitting | No saving is assumed. All such conditions must enter either the actual carrier count or exact legal-return test, with a quantified bound. |
| Archimedean distortion and branch/ratio counts | Must be included when proving a uniform return or tail bound; unknown costs are not zero. |
| Final signed rate | Must establish (19), or the general $\delta=2a-g>0$, before taking the depth limit. |
| Fixed exponent | Only strict exponents below the proved ratio follow automatically. Finite numerical improvement is not an asymptotic premise. |

**Present conclusion:** HR-1(a)–(c) and the reciprocal/scalar variants are
proved implications. The constructive work remains to produce actual sets
with enough distinct legal returns for essentially all scalar outputs,
pay every input and arithmetic cost, and establish a uniform positive rate.
No carrier search, experiment, or proof of the target is performed here.
