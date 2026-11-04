# Cartesian-compatible high-return carriers

**16 September 2026 — constructive research cycle, T03 / full-rank quadratic branch.**

**Outcome: OPEN target; no surviving power-saving construction.** This cycle
proves the required return-to-image theorem and several scoped obstructions.
The strongest new conclusion is an actual-image obstruction for dense
one-prime denominator strata, including growing numerator alphabets. It is
not a general impossibility theorem for real or rational carriers.

The fixed benchmark is

$$Q(x,y)=x^2+xy+y^2.$$

Every construction below uses one scalar set in both coordinates and includes
all ordered pairs. No new witness for $P_0=Q+x$ is obtained. Its inherited
same-set transfer still requires both a homogeneous saving and sufficiently
small difference set; no such premises have been established here.

## 1. Results and proof status

All new proofs are internal derivations, independently inspected within this
task. This is not external review or a novelty claim.

| ID | Status and exact conclusion | Complete proof |
|---|---|---|
| HR-1 | **PROVED:** partial returns imply a full-support bound after duplicate labels, stabilizers, scalar projection fibers and exceptions are charged | [Return lemma](return-lemma.md), §§1–6 |
| HR-2 | **PROVED:** on dense bounded-numerator $7$-adic strata, at most $1+\lfloor\log_7(3H^2)\rfloor$ powers of the specified multiplier return at any nonzero pair, uniformly in denominator depth | [Denominator obstructions](denominator-obstruction.md), HR-2 |
| HR-3 | **PROVED:** a fixed $p$-free numerator alphabet $B$ and arbitrary finite denominator-depth set have full quadratic fibers at most $4|B|+|B|^2$ | Same note, HR-3 |
| HR-4 | **PROVED:** dense one-prime strata have full fibers at most $C_\eta H^\eta$ for every fixed $\eta>0$, uniformly in depth and prime; hence no fixed image saving for this family | Same note, HR-4 |
| HR-5 | **PROVED:** recursive Cartesian repair has only $O(\log n)$ cyclic returns; its polynomial cleared height also excludes actual image power saving | [Carrier screen](carrier-screen.md), HR-5 |
| HR-6 | **PROVED:** the completed orbit of the nine-point seed square has at most $145n^2/M$ nonzero pairs with $M$ cyclic returns | Same note, HR-6 |
| HR-7 | **PROVED**, using the identified **EXTERNAL RESULT** on cyclotomic degree: full cyclotomic digit boxes supply only $n^{o(1)}$ torsion actions | Same note, HR-7 |
| HR-8 | **PROVED:** the specified three compatible integer translates of a coefficient orbit have at most $49n^2/M$ nonzero pairs with $M$ cyclic returns | Same note, HR-8 |
| HR-9 | **EXPERIMENTAL:** exact return and full-image distributions for 18 explicitly bounded finite cases | [Experiments](experiments.md) and [portable data](../../../examples/2026-09-16-cartesian-returns.json) |

Each row belongs to this separate T03 multiplier branch, has fixed polynomial
$Q$, and is dated/versioned in its linked proof. HR-1 is a combinatorial
implication with **CONDITIONAL** applications. HR-2 and HR-5–HR-8 distinguish
failure of an action certificate from a lower bound on the actual image.
HR-3 and HR-4 bound the entire image, independently of a chosen action.
Dependencies and audit scope are detailed below and in the companion notes.

## 2. Return-to-image theorem

Here is the scalar form of HR-1. Let $X=A^2$, $n=|A|$. At each
$p\in X\setminus\mathcal E$, suppose at least $M$ labels give legal,
value-preserving returns to $X$. Suppose at most $D$ labels can produce the
same returned scalar pair. Then

$$
\boxed{|Q(A,A)|\le\frac{n^2}{\lceil M/D\rceil}
                     +|Q(\mathcal E)|
              \le\frac{n^2D}{M}+|\mathcal E|.}
$$

**Proof.** Each output having a nonexceptional representative has at least
$\lceil M/D\rceil$ distinct pairs in its complete fiber. Those fibers are
disjoint subsets of $A^2$. Outputs represented only by exceptional pairs
contribute at most $|Q(\mathcal E)|$. These two classes cover every output.

For a partial action on a decorated carrier, one may choose one lift of each
nonexceptional scalar pair. If at most $h$ return labels land at one decorated
state and at most $\Lambda$ returned states project to one scalar pair,
use $D=h\Lambda$. No regularity of all lifts is required. A group stabilizer
and repeated group labels bound $h$; for an arbitrary relation its duplicate
multiplicity must be proved directly. The raw-state and pointwise reciprocal
versions, including the no-return case, are proved in HR-1. An input
projection with coordinate fibers $\kappa$ costs $\kappa^2$ across the two
inputs. It is not charged again in a raw-state output numerator.

For $z=x-\omega y$, $\omega^2+\omega+1=0$, a norm-one element
$v=r+s\omega$ acts by

$$T_v(x,y)=(rx+sy,-sx+(r-s)y),\qquad Q(T_v(x,y))=Q(x,y).$$

The coefficient map is injective on real pairs. Distinct multipliers act
freely when $z\ne0$, so $D=1$ for the rational experiments. At $(0,0)$,
all multipliers give one returned point: its effective multiplicity is one,
or its one output is charged as an exception. No orbit count at zero is used
as a saving.

If $\log n=ad+o(d)$, the raw return rate is $r$, the total duplicate/projection
loss is $s$, and $|\mathcal E|\le e^{(2a-\delta)d+o(d)}$, the output exponent
is at most

$$\max\{2a-r+s,\ 2a-\delta\}.$$

The net gap is $\min(r-s,\delta)$. It must be strictly positive. Every
$c<\min(r-s,\delta)/a$ then works eventually; endpoint exponents do not
follow automatically. Unequal lower/upper input-rate bounds are treated in
HR-1(c). Large average returns alone do not prove this conclusion.

## 3. Six carrier architectures and the initial return mechanism

Write

$$u=\frac{8+5\omega}{7}=\frac{3+\omega}{2-\omega},\qquad
T=\frac17\begin{pmatrix}8&5\\-5&3\end{pmatrix}.$$

It has norm one and infinite order. The rational architectures use actual
powers of this action. The sixth architecture below changes the action to
a finite cyclotomic group. These are different ways of attempting
Cartesian compatibility, not six choices of coefficients for one finite set.

| Architecture | Exact definition and reason to investigate | Screen and scope |
|---|---|---|
| A. Additive lattice section | $A_N=D^{-1}([-N,N]\cap\mathbb Z)$, with arbitrary common $D>0$. Real ellipses have substantial overlap under rotations, suggesting pair returns if integrality survived. | **FAILED** for actual image saving by the inherited polynomial-height theorem after common scaling. The integral-return index of $u^k$ is $7^{|k|}$, not the squared index of a different archived multiplier family. No new interval search was run. |
| B. Compatible translates | $C_J=\operatorname{coord}\{T^k(1,0):|k|\le J\}$ and $A_J=\{-1,0,1\}+C_J$. Many translated components are intended to absorb partial returns of their centers. | **FAILED cyclic-return certificate**, HR-8: the complete-square mean return is bounded, uniformly in $J$. Translating a norm fiber does not preserve its norm. |
| C. Orbit-thickened Cartesian seed | $P=\{-1,0,1\}$, $Z_J=\bigcup_{|k|\le J}T^k(P^2)$, $A_J=\operatorname{coord}(Z_J)$. The seed itself is Cartesian, and every engineered orbit has many genuine returns. | **FAILED cyclic-return certificate**, HR-6: rich engineered orbits occupy too little of the completed square; at most $145n^2/M$ pairs have $M$ returns. Actual image rate beyond this action remains **OPEN**. |
| D. Denominator states / explicit product-additive hybrid | $A_{H,L,p}=\{bp^{-k}:1\le|b|\le H,\ p\nmid b,\ 0\le k\le L\}$. This is $GP$ with $G=\{p^{-k}\}$ and a dense numerator set. Split-prime multiplier poles can move a pair between denominator states. | **FAILED actual carrier**, HR-4, even when $H$ and $L$ both grow. HR-2 separately bounds every return for $p=7$. The state count alone does not create valuation imbalance. |
| E. Recursive Cartesian repair | $A_0=\{-1,0,1\}$; $A_{j+1}=A_j\cup\operatorname{coord}(T(A_j^2))\cup\operatorname{coord}(T^{-1}(A_j^2))$. Every old Cartesian pair is repaired, not just a selected orbit. | **FAILED actual carrier**, HR-5. The input at least doubles per step, the cleared height stays polynomial in input size, and all cyclic returns remain logarithmic. |
| F. Coefficient module with torsion symmetry | For $3\mid m$, $Z_{m,H}=\{\sum_{i=0}^{m-1}c_i\zeta_m^i:|c_i|\le H\}$; write $z=a-\omega b$ over the real subfield and let $A$ be the signed union of all $a,b$. The digit module is exactly invariant under $\langle\zeta_m\rangle$. | **FAILED supplied-action certificate**, HR-7: $n\ge(2H+1)^{\varphi(m)/2}$ while the group has only $m$ elements. Even perfect Cartesian return has zero limiting return exponent. Sparse variants are outside this theorem. |

The scoped rational lattice theorem was used to reject A without repeating
its completed search. B and F were rejected analytically. C, D and E
received one small, predeclared exact diagnostic run while their independent
obstruction proofs were developed. The diagnostics measure the failure;
they do not designate these families as asymptotic survivors. No broad
optimization, previous 43-case rerun, or further search after these
rejections was performed.

### Why the new denominator obstruction is stronger than a height screen

The carrier has the exact size

$$n=2\bigl(H-\lfloor H/p\rfloor\bigr)(L+1).$$

Clearing denominators gives height $Hp^L$, which can be superpolynomial in
$n$. The old polynomial-height theorem alone therefore does not close this
family. HR-4 does: for every $\eta>0$ there is a constant $C_\eta$ such that

$$\max_t\#\{(x,y)\in A_{H,L,p}^2:Q(x,y)=t\}\le C_\eta H^\eta,$$

uniformly in $L$ and $p$. In particular, since $H\le n$,

$$|Q(A_{H,L,p},A_{H,L,p})|\ge C_\eta^{-1}n^{2-\eta}.$$

The proof separates equal denominator depths, small unequal depth gaps,
and large gaps. Unequal depths are recovered from $v_p(t)$. For a large
gap, reducing the cleared norm modulo $p^{\lfloor\log_p H^2\rfloor+1}$
recovers the deeper numerator square exactly, leaving at most eight ordered
representations. A small gap produces an integer norm at most $3H^6$,
whose representation count is subpolynomial in $H$. Equal depths have only
$O(\log H)$ possible scales and the same small-norm bound. The companion
proof derives the integer norm/divisor estimate directly, so this result
does not depend on an unverified field-tower or class-number claim.

### Orbit thickening: explicit gain versus growth

For C, $|Z_J|=16J+9$ but $2J+3\le n\le36J+3$; hence engineered density
is $O(1/J)$. This observation alone would leave cross-pair returns open.
HR-6 addresses those pairs: unequal rational $7$-adic coordinate valuations
give equal split valuations. Every nonidentity return therefore has its
source or target in the class of equal coordinate valuations, containing
at most $36(n-1)$ pairs. Only $O(J)$ powers can return anywhere. Summing
these edges proves the bounded full-square mean return, and hence the
$145n^2/M$ rich-pair bound. This is a lower bound on the size of the bad
tail, not an image upper bound inferred from collision energy.

## 4. Finite experiments and exception control

**HR-9 — EXPERIMENTAL, exhaustive exact finite cases.** The program counts
the entire image, raw returns, distinct returned pairs, stabilizers, image
fiber sizes, exact threshold exceptional sets, and denominator-state
transition edges. All equality and membership tests use integers or
`Fraction`. Decimal geometric means and percentages are descriptive only.

Selected largest cases:

| Carrier | $n$ | $|Q(A,A)|$ | Nonzero pairs | Identity-only pairs | Largest return count |
|---|---:|---:|---:|---:|---:|
| Strata $H=4,L=8$ | 72 | 1,262 | 5,184 | 5,040 | 2 |
| Strata $H=16,L=4$ | 140 | 4,272 | 19,600 | 18,560 | 3 |
| Orbit box $J=8$ | 83 | 1,642 | 6,888 | 6,744 | 17 |
| Cartesian repair $j=2$ | 121 | 2,129 | 14,640 | 12,180 | 5 |

All 18 cases have median return exactly one and minimum nonzero return
exactly one. The [experiment report](experiments.md) contains every return
and full-image multiplicity histogram, every geometric mean, and exact
rules reconstructing each stabilizer/distinct-point distribution. The
portable JSON records all threshold tails and code/input/output hashes;
the ignored raw result additionally records carriers and transition counts.

For a threshold $M$, the actual exceptional set is zero, if present, plus
all nonzero pairs with fewer than $M$ returns. It is not replaced by the
small selected set where returns are engineered. HR-2 and HR-5 make a
polynomial threshold impossible at every nonzero point eventually. For
HR-6 and HR-8, a polynomial threshold is reached by only a vanishing
fraction of pairs; its exceptional complement has order $n^2$. Thus no
fixed positive exceptional-tail exponent is available from those actions.

## 5. Arithmetic audit and signed rates

The detailed construction ledgers follow the repository template in the
companion proofs. The following summarizes the complete rate gate. Here
$d=\log n$, so the *actual* input rate is $a=1$; this is a size-normalized
ledger, not an assertion of exponential growth in denominator depth or
field degree.

| Candidate | Effective return rate $r-s$ | Exceptional tail | Resulting support information / signed gap |
|---|---|---|---|
| A: lattice interval | Cannot certify positive rate; actual fibers are $n^{o(1)}$ by the inherited fixed-height theorem | Removing pairs does not repair an actual-image obstruction | Actual output exponent $2-o(1)$; no fixed gap |
| B: translates | Any positive threshold is met by at most $49n^2/M$ pairs | Bad tail has exponent 2 | HR-1 offers no positive gap from this action; actual rate **OPEN** |
| C: orbit box | Any positive threshold is met by at most $145n^2/M$ pairs | Bad tail has exponent 2 | Same action-certificate deficit; actual rate **OPEN** |
| D: strata | At $p=7$, $r=0$, since $R\le O(\log n)$; $s=0$ | At $p=7$, no polynomial-return good set for this action | HR-4 gives actual exponent $2-o(1)$ for every prime; no fixed gap |
| E: repair | $r=0$ from $R\le O(\log n)$; $s=0$ | No polynomial-return good set; zero costs one output | Actual exponent $2-o(1)$ from cleared height; no fixed gap |
| F: torsion module | Even maximal raw $r$ is zero after comparison with $n$ | Full Cartesian coverage would not fix this rate deficit | No positive gap from the supplied torsion group; actual rate **OPEN** |

For rational carriers the projection is the identity, nonzero stabilizers
are trivial, and labels are distinct powers: no hidden fiber or stabilizer
gain/loss is present. Sign/swap symmetries may still cause constant-size
polynomial fibers; these are fully counted and do not create a fixed power
saving. No input thinning is used. When considering an earlier-stage
interior, its input fraction is squared: for E, the guaranteed $2r+1$
returns on $A_{j-r}^2$ cover at most approximately $4^{-r}$ of $A_j^2$.

All rational norm actions take place in the same fixed quadratic algebra
$\mathbb Q(\omega)$, of discriminant $-3$. The proofs use explicit
arithmetic, not asymptotic lattice packing, regulator or class-number
estimates; none of those supplies a saving. Split-prime indices, multiplier
poles, common denominators and archimedean bounds are explicitly charged:

- D: input denominator $p^L$, cleared height $Hp^L$; $u^k$ denominator
  divides $7^{|k|}$. Exact valuations replace any assumed uniform residue
  distribution.
- C: denominator $7^J$, real radius 2, cleared height at most $2\cdot7^J$;
  at most 36 scalar points per nonzero denominator state. B has radius
  less than 3 and at most 12 points per such state.
- E: denominator $7^j$, cleared height at most $13^j$, and
  $2^{j+1}+1\le n\le2\cdot13^j+1$. Boundary and state growth are paid by
  the full Cartesian set and the interior-square calculation.
- F: degrees $[K:\mathbb Q]=\varphi(m)$ and $[L:\mathbb Q]=\varphi(m)/2$;
  scalar coefficient recovery divides by $\omega-\bar\omega$. Relations
  among digits are allowed, but an independent basis subcube proves the
  lower input count. A varying discriminant, regulator, class number or
  archimedean distortion cannot repair the already subpolynomial maximum
  action count; no favorable bound for them is assumed. No lattice-volume
  estimate or positive arithmetic rate is claimed.

No carry, branch, ratio or state count is credited twice. The code
deduplicates scalar inputs before forming the square. State transition
graphs count returned edges, not independent scalar outputs. A more
general solvable or nonabelian extension was not added: no concrete new
Cartesian return mechanism survived that would justify its arithmetic cost.

## 6. Failure registry and surviving scope

| Failure ID | Exact hypotheses | What is excluded | What remains outside the proof |
|---|---|---|---|
| HR-F1 | Dense rational interval after one common scaling | Actual fixed saving, inherited height theorem | Superpolynomial cleared height / varying fields |
| HR-F2 | HR-2 carrier, powers of $u$ | Polynomial cyclic returns, for any exponent window | Other numerator patterns or independent prime actions |
| HR-F3 | HR-3 fixed $p$-free alphabet | Actual power saving, any depth set and any action | Growing sparse alphabets not covered by HR-4 |
| HR-F4 | Dense HR-4 alphabet, any $H,L,p$ | Actual power saving, regardless of norm action | Several denominator primes or other sparse numerator architecture |
| HR-F5 | Exactly the recursive repair rule of HR-5 | Actual power saving and polynomial cyclic returns | Other closures with different input/height growth |
| HR-F6 | Exactly the nine-point seed orbit-box of HR-6 | Nearly full polynomial-return tail for its cyclic group | Other seeds, actions or full-image coincidences |
| HR-F7 | Full cyclotomic digit module, displayed torsion action | Fixed positive return exponent from that action | Sparse codes and larger effective actions |
| HR-F8 | Exactly $\{-1,0,1\}+C_J$ | Nearly full polynomial cyclic-return tail | Other translates with growing/correlated populations |

**Best surviving carrier: none.** No candidate is selected for a positive
return proof in Stages 4–6. The rigorous negative endpoint is HR-4 and the
additional scoped action obstructions, not the small finite image ratios.
The objective for arbitrary real sets remains **OPEN**.

## 7. One next proof obligation

**OPEN — HR-N1, untested two-prime return-tail assertion.** This is the
single next obligation, not a claimed survivor or a new experiment in this
cycle. It tests the precise feature absent from the one-prime proof:
independent valuation shifts whose scalar denominator states can interact.

For integers $L\ge1$, define

$$A_L=\{b7^{-k}19^{-\ell}:1\le|b|\le L,\ \gcd(b,133)=1,
                                  \ 0\le k,\ell\le L\},$$
$$v=\frac{21+16\omega}{19}=\frac{5+2\omega}{3-2\omega},\qquad
G_L=\{u^rv^s:|r|,|s|\le8L\}.$$

Both multipliers have norm one. Unique rational valuations give exactly

$$n_L=2\left(L-\lfloor L/7\rfloor-\lfloor L/19\rfloor
                     +\lfloor L/133\rfloor\right)(L+1)^2.$$

**Prove or disprove this one assertion:** there exist fixed
$\varepsilon,\delta>0$ such that, for every sufficiently large $L$,

$$\#\{(x,y)\in A_L^2:R_{A_L,G_L}(x,y)<n_L^\varepsilon\}
                         \le n_L^{2-\delta}.$$

The action and scalar carrier are explicit, projection is injective,
nonzero stabilizers are trivial, and HR-1 would immediately give the
full-support conclusion if the assertion were proved. No favorable return
rate is known. The one-prime HR-4 proof does not apply: clearing a gap at
one prime introduces unbounded powers of the other prime into its numerator.
This is a defined scope gap, not evidence that the assertion is true.

## 8. Authorization, provenance, reproducibility and checks

The current user explicitly commissioned this constructive cycle. Before
research, the announced scope was T03's fixed $Q$, optional justified $P_0$
transfer, six carrier architectures, standard-library exact arithmetic,
**at most 2,000,000 action-pair or polynomial evaluations and 600 CPU
seconds**. Network use was limited to verification of a needed external
theorem. The only mathematical web import was the cyclotomic degree/basis
fact identified in HR-7, checked in the primary MIT notes; this was not a
literature or novelty review.

Controlling context retained and inspected includes setup/map/migration
audit, master handoff, T03 current-state/final TCRC companions, SPEC/STATUS,
the migration-conflict and mechanism/failure/open-lemma registries, the
preceding 16 September norm/trace cycle, and the focused norm report and
new-mechanisms report inside the retained T03 ZIP. The source audit read
the formal lattice and height arguments; source summaries were not treated
as proof. No prior full research schedule was rerun. Existing small unit
regressions, including earlier arithmetic examples, were run for code
verification only.

The fixed field lattice-index correction is local in scope: the older
$7^{2|k|}$ / $25/24$ calculation concerns its squared class-fiber multiplier.
For a primitive split-prime ratio here the index is $7^{|k|}$, and the
two-sided inverse-index sum is $4/3$. Those are ambient lattice densities;
they are not relative probabilities for an arbitrary finite window. The
one-prime proofs here make no such probability assumption.

The unavailable standalone F25 certificate and separate final-checkpoint
designation issue remain recorded in `research/MIGRATION_CONFLICTS.md`.
Neither is a premise of this cycle. The four track targets, old adaptive
RC15/4 obligation, original archives, migration copies and historical
records were preserved.

The single main run completed all 18 cases with **863,636 charged
evaluations**, **0.468425 CPU seconds**, and **zero errors** on Python 3.12.7.
See [the exact run report](experiments.md) for command, schedule, counter
breakdown, guard limitations and output locations. New small independent
`Fraction` oracles check the exact action and full histograms. Their results,
the required repository checks and final hashes are recorded in
[validation](validation.md) and the cycle manifest.

Only new dated notes, one reusable experiment module, its small tests, a
portable example JSON and ignored raw run files belong to this cycle.
Pre-existing tracked and untracked work was retained. No staging, commit,
push, remote change, or archive alteration was performed. All work remains
uncommitted.
