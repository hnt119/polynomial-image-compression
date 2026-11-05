# Can the six-point cubic gadget be made asymptotic?

**2026-09-16, continuation v1 · T01 · \(P(x,y)=(x-y)^3+x+y\).**
Authorized offline research. Immediate starting source:
[the preceding finite-gadget report](../2026-09-16-three-branch-lift/README.md).
Its proofs, code and data are preserved. No internet, package installation,
external novelty assessment, or arithmetic-tower construction occurred.

## 1. Short verdict

**No positive asymptotic rate was obtained. The original target remains OPEN.**
The finite 22-output result is correct, but its present overlap mechanism
does not survive the tested repairs in the way a power saving requires.

Three conclusions are proved, rather than inferred from experiments:

- **Allow the copies to overlap:** the literal maps still give exponentially
  many inputs, but their actual growth factor tends to 2. Almost every
  ordered pair eventually has a different output, so the image growth
  factor tends to 4. The gate is \(4<2^2\), which fails by equality.
- **Separate the copies sufficiently:** inputs triple, but every cross-copy
  pair becomes distinguishable. The exact output count is \(6n^2+3s\)
  for unscaled copies, so separation loses the desired sub-nine gain.
- **Reuse only the gadget's translated-slice rules:** these give only
  \(O(N)\) identifications on an \(N\)-point set. A fixed fractional
  reduction in the full \(N^2\) pair budget cannot come from that bounded
  list alone, even if the list's parameters change at every stage.

There is also **EXPERIMENTAL exact** evidence from nine stage-dependent
affine rules over three successive levels. Every rule triples the inputs
through \(6,18,54,162\), but none gives three successive normalized gains.
One alternating rule gains at level two and loses the gain at level three.
The tests are finite evidence, not a theorem against every adaptive affine
system. The proved negative statements have the narrower scopes above.

## 2. Why the six-point gadget works

The scale \(1/2\) turns the old seed gap 2 into a gap of 1 inside each
branch. The shifts \(0,1/3,2/3\) interleave those pairs into a short
progression:
\[
A=\{0,2\},\qquad F_r(x)=x/2+r/3,\qquad
G=\{0,1/3,2/3,1,4/3,5/3\}.
\]
On this short progression, a few difference slices account for a large
part of the entire square. Their cubic terms cancel against anchor shifts.

**TC-A1 — exact identities and exhaustive classification.** All fourteen
savings from 36 pairs to 22 outputs follow from
\[
\begin{aligned}
P(t,t\pm1)&=P(t,t)=2t,\\
P(t+1/3,t)&=P(t,t+2/3)=2t+10/27,\\
P(t-1/3,t)&=P(t,t-2/3)=2t-10/27.
\end{aligned}\tag{2.1}
\]
Each is a polynomial identity in the one variable \(t\). Its application
requires every endpoint shown to lie in the finite set.

The table classifies **every overlap between distinct blocks**. Write
\(I_+\), \(I_-\) for the last two identities. Values in the middle column
are multiplied by 27 only to display integers.

| Intersecting blocks | All common values, times 27 | Explanation and legal anchors |
|---|---|---|
| 01, 12 | \(\{62\}\) | \(I_-(4/3)\) |
| 01, 20 | \(\{44\}\) | \(I_-(1)\) |
| 02, 10 | \(\{10,64\}\) | \(I_+(0),I_+(1)\) |
| 02, 21 | \(\{46\}\) | \(I_+(2/3)\) |
| 10, 21 | \(\{28\}\) | \(I_+(1/3)\) |
| 12, 20 | \(\{26,80\}\) | \(I_-(2/3),I_-(5/3)\) |

There are no other nonempty intersections and no triple block intersections.
The eight listed equalities form the two whole-slice containments
\(S_{-2}\subset S_1\), \(S_2\subset S_{-1}\), where the index is
three times the real difference. The six internal duplicates in diagonal
blocks come from \(P(t,t\pm1)=P(t,t)\) and give
\(S_{\pm3}\subset S_0\).

**Proof.** Substitution in (2.1), together with endpoint membership in
\(G\), gives the displayed values. The preceding report's complete block
table has block-size sum 30 and exactly eight repeated values between
different blocks. Inside the diagonal blocks six pair duplicates reduce
36 to 30. Equivalently, the full image has fourteen fibers of size two
and eight fibers of size one: \(14\cdot2+8=36\), \(14+8=22\).
The [affine companion, §1](affine-mechanism.md#1-all-eight-interblock-overlaps-come-from-two-identities)
lists all ordered-pair witnesses, so this classification is exhaustive. ∎

In the requested vocabulary these are **exact one-variable polynomial
identities** that produce **whole-slice containments on the chosen seed**.
There is no whole-block containment between distinct blocks, no identity
in two independently varying seed variables, and no unexplained accidental
collision in \(G\). The seed supplies the endpoints; the identities supply
the equality. Residues modulo 3 identify branch labels, but no modular
reduction proves these real equalities.

## 3. Why shrinking or changing the branches is delicate

The cubic term scales differently from the linear term. Consequently,
shrinking a gadget preserves its shape but usually destroys its exact
output coincidences. A new scale can create other coincidences, which
must be proved separately.

**TC-A2 — preservation of old collisions.** If two different ordered pairs
have the same output, put \(u=a-b\), \(v=c-d\). Then \(u\ne v\), and
\[
P(ha+t,hb+t)-P(hc+t,hd+t)
=h(h^2-1)(u^3-v^3).\tag{3.1}
\]
For nonzero real \(h\), that old equality survives exactly when
\(h=1\) or \(h=-1\).

**Proof.** The old equality gives
\((a+b)-(c+d)=-(u^3-v^3)\). Expanding the rescaled outputs gives (3.1).
Equal differences and equal sums would recover the same pair, so the
remaining factor is nonzero. ∎

For the same interleaved two-point pattern, let the seed gap be \(H\),
common branch scale \(a\), and shift step \(q\). Interleaving requires
\(aH=3q\), while
\[
P(t+q,t)=P(t,t+2q)\quad\Longleftrightarrow\quad q(9q^2-1)=0.
\]
Distinct branches force \(q=\pm1/3\) and \(aH=\pm1\). Thus changing
the seed gap and compensating by scaling gives the same small gadget up
to translation or reflection, not an unbounded family of larger gadgets.

**TC-A3 — unequal slopes do not retain an entire translated-slice identity.**
If
\[
P(\alpha t+a,\beta t+b)=P(\gamma t+c,\delta t+d)
\]
for all real \(t\), either the ordered input lines are identical or all
four slopes are equal. In the latter case the constant terms agree:
\((a-b)^3+a+b=(c-d)^3+c+d\).

**Proof.** The cubic coefficient fixes \(\alpha-\beta=\gamma-\delta\).
If this common value is nonzero, comparison of the quadratic, linear and
constant coefficients successively recovers the coordinate differences,
slope sums and coordinate sums, so the lines coincide. If it is zero,
both sides are linear and their slopes must agree. ∎

This rules out unequal slopes as a way of preserving these whole-line
identities. It does not rule out seed-specific collisions or a different
complete support mechanism. In particular it is not a no-go for every
adaptive affine system.

The exact formulas keep track of what must survive. For arbitrary affine
branches \(F_r(x)=a_rx+t_r\), the entire \((r,s)\) block is
\[
\{(a_rx-a_sy+t_r-t_s)^3+a_rx+a_sy+t_r+t_s:x,y\in A\}.
\tag{3.2}
\]
For any finite carrier, define \(A_u=A\cap(A-u)\). Then
\[
P(A,A)=\bigcup_{u\in A-A}(u^3+u+2A_u),\qquad
a-b=\frac{(v-u)(u^2+uv+v^2+1)}2
\tag{3.3}
\]
is the exact collision condition between anchors \(a\in A_u\) and
\(b\in A_v\). These follow by substituting the pair \((a+u,a)\).
Each individual slice is injective in its anchor.

With common branch scale \(\ell\ne0\), compare the old slices
\((z+u,z)\) and \((z+\eta+v,z+\eta)\) in blocks \((r,s)\)
and \((p,q)\). Put \(U=\ell u+t_r-t_s\) and
\(V=\ell v+t_p-t_q\). Substitution in (3.2) gives an identity precisely when
\[
2\ell\eta=U^3+U-V^3-V+2(t_s-t_q).
\tag{3.4}
\]
To obtain an actual containment, all four old endpoints
\(z,z+u,z+\eta,z+\eta+v\) must lie in \(A\) for every claimed
anchor. Solving (3.4) does not supply that endpoint condition or its density.

## 4. Direct iteration: growth survives, the gain does not

The copies need not be disjoint for the input set to keep growing. For the
literal maps, however, the loss is substantial: almost one third of the
naive input labels are duplicates. Their smaller image growth must be
compared with the square of that smaller input growth.

**TC-D1–D3 — complete result for literal repetition.** Starting at \(A_0=G\),
let \(A_{m+1}=\bigcup_{r=0}^2(A_m/2+r/3)\). For \(q=2^m\),
\[
A_m=\frac1{3q}\{0,1,\ldots,4q+1\},\quad
n_m=4q+2,\quad n_{m+1}=2n_m-2.\tag{4.1}
\]
Writing \(s_m=|P(A_m,A_m)|\), one has
\[
s_m=n_m^2-O(n_m^{3/2}),\qquad
\lambda=\lim\frac{n_{m+1}}{n_m}=2,\quad
\rho=\lim\frac{s_{m+1}}{s_m}=4.\tag{4.2}
\]
Therefore \(\rho=\lambda^2\), with no strict saving.

**Proof idea, with exact bounds.** At the next level, the common-denominator
numerator intervals are \([0,4q+1]\), \([2q,6q+1]\), and
\([4q,8q+1]\), proving (4.1). For inputs \(i/(3q),j/(3q)\), clear the
denominator:
\[
27q^3P=(i-j)^3+9q^2(i+j).
\]
For \(m\ge4\), put \(Q=2^{\lfloor m/2\rfloor-1}\). Among pairs with
\(Q\nmid i-j\), equality modulo \(q^2\) recovers the exact difference;
the displayed output then recovers the sum. These pairs are injective.
Exactly \(n_m^2/Q+2-4/Q\) pairs were left out, so
\[
n_m^2(1-1/Q)-2+4/Q\le s_m\le n_m^2.
\tag{4.3}
\]
Since \(Q\) is comparable to \(\sqrt{n_m}\), this proves (4.2).
The complete elementary congruence proof and intersection counts are in
[direct-iteration.md, §§1–2](direct-iteration.md). ∎

This is an actual-image lower bound, independent of the missing full
historical digital proof. It closes these literal maps even when overlaps
are allowed. It leaves other stage-dependent rules outside its scope.

## 5. More separation fixes disjointness but exposes cross-copy pairs

Moving intact copies farther apart keeps their internal collisions.
It also makes an output from two different copies record which copies
and which two old inputs were used. Those six cross-copy blocks then
dominate the count.

**TC-D4–D5 — exact sufficiently separated-copy theorem.** Fix a nonempty
finite real set \(C\), \(n=|C|\), \(s=|P(C,C)|\). For every separation
\(H\) outside a finite exceptional set, with disjoint copies,
\[
B=C\sqcup(C+H)\sqcup(C+2H),\qquad
|P(B,B)|=6n^2+3s.\tag{5.1}
\]
In particular this holds for all sufficiently large \(H\). A common
nonzero scale \(a\), fixed before \(H\) is chosen, changes the formula to
\(6n^2+3|P(aC,aC)|\), still at least \(\tfrac23|B|^2\).

**Proof.** For \(k=r-s\), \(u=x-y\), the block output is
\[
k^3H^3+3k^2uH^2+(3ku^2+r+s)H+u^3+x+y.
\]
When \(k\ne0\), its coefficients recover \(k,u,r+s,x+y\), hence the
block and ordered pair. Thus all \(6n^2\) cross-copy output polynomials
are distinct. Same-copy outputs are the \(3s\) distinct linear
polynomials \(2rH+z\). Nonidentical polynomials agree at finitely many
\(H\), proving (5.1). ∎

For \(C=G\), this gives 282 outputs on 18 inputs:
\(\rho=282/22=141/11>9\). If such unscaled separation is repeated,
\[
\frac{s_{m+1}}{n_{m+1}^2}
=\frac13\frac{s_m}{n_m^2}+\frac23,
\]
so the output density tends to 1. Allowing stage-dependent common scales
does not remove the quadratic lower bound at adequately separated stages.

This theorem does not reject deliberately chosen exceptional separations,
or all visually separated configurations. The set and scale are fixed
first, and the separation must meet the stated finite-exception condition.

## 6. What block composition inherits, and what it still has to prove

The good collisions inside a six-point copy are a small part of all pairs
in a union of many copies. Even trying to transfer each old equality into
every cross-copy block works at only a few differences between centers.

**TC-A6 — exact survival equation.** Suppose
\(C=\bigsqcup_{t\in T}(t+hG)\), \(|T|=m\), so \(N=6m\).
For an old nontrivial equality between pairs with differences \(u,v\),
the same matching in copies whose centers differ by \(D\) survives iff
\[
3D^2+3hD(u+v)+(h^2-1)(u^2+uv+v^2)=0.\tag{6.1}
\]
Each old equality permits at most two center differences. All fourteen
old equalities therefore supply at most \(28m\) equality edges among
\(36m^2\) pairs.

**Proof.** The cross-copy output is
\((D+hu)^3+t+s+h(a+b)\). Subtract the corresponding old matching and
use its old equality. The difference is \(h(u-v)\) times (6.1).
The prefactor is nonzero, and each root \(D\) can occur for at most
\(m\) ordered center pairs. ∎

For the two interblock identity families, (6.1) becomes
\[
9D^2-3hD+h^2-1=0,
\qquad 9D^2+3hD+h^2-1=0.
\]
Both survive in the same copy pair only when \(D=0,h^2=1\).
This shows explicitly why internally good blocks do not automatically
compose. The count concerns inherited matchings only; unlisted new
cross-copy collisions could still exist. It is a failed certificate,
not an actual-image lower bound for every union of copies.

## 7. A broad obstruction to using only finitely many slice rules

Changing the constants at each level is not enough if the construction
still uses only a short list of the same kinds of equalities. Each rule
works at at most two differences, and each difference has at most \(N\)
ordered pairs. Most of the square remains unaccounted for.

**TC-A4–A5 — PROVED.** On any \(N\)-point real carrier:

- \(L\) selected differences cover at most \(LN\) pairs. Covering all
  but \(O(N^{2-\delta})\) pairs this way requires
  \(L\ge N-O(N^{1-\delta})\).
- \(M\) nonzero fixed pair displacements \((h,k)\), even chosen after
  seeing the carrier, generate at most \(2MN\) equality edges. The
  equality classes obtained using only those edges number at least
  \(N^2-2MN\).

**Proof.** A fixed difference determines the first coordinate from the
second. For a displacement, putting \(u=x-y\) gives
\[
P(x+h,y+k)-P(x,y)
=3(h-k)u^2+3(h-k)^2u+(h-k)^3+h+k.
\]
For a nonzero displacement this vanishes at at most two real differences
(or at none if \(h=k\)). There are at most \(N\) source pairs at each
difference. Each equality edge reduces the number of labels by at most one. ∎

In fact the entire original gadget uses only two displacements:
\[
(x,y)\mapsto(x,y+1),\qquad
(x,y)\mapsto(x-1/3,y+2/3).
\]
They work respectively at differences \(0,1\) and \(1/3,2/3\), and
supply at most \(4N\) edges on any carrier.

This is a **scoped obstruction to the stated overlap certificate**, even
for adaptive affine systems retaining that bounded inventory of rules.
If those rules generate every actual output fiber, it becomes an actual
quadratic image lower bound. Without that additional hypothesis, other
collisions remain possible. We do not replace a missing support upper
bound by an unjustified assertion that every uncovered pair is distinct.

## 8. Exact continuation experiments

The preceding 980-gadget search was not repeated. These tests ask a new
question: what happens over three successive continuations of \(G\)?
Known literal and fixed-spacing progression failures were stopped
analytically and were not deepened numerically.

Nine explicit rules were fixed before execution. The announced limits were
16 rules, 120 evaluated steps, 162 distinct inputs per level, three million
exact polynomial evaluations, and 90 research CPU seconds. Actual use:
**9 rules, 27 steps, 265,392 evaluations, 7.432394 CPU seconds**, using
CPython 3.12.7 and exact rational arithmetic. No randomized search or
floating-point collision test was used.

### Rules and input growth

**TC-E2 — exact tripling and growing prime support.**
Let \(D=\max A-\min A\). Rules 1–8 use
\(F_r(x)=ax+r(q+1/p)\). At each level, \(p\ge5\) is the smallest prime
larger than the preceding prime and absent from every denominator of
\(aA\), \(a\), and \(q\). Thus the left side of a possible branch
collision is integral at \(p\), while the nonzero \((r-s)/p\) term is not;
the copies are disjoint. This argument proves tripling at every stage,
not only the tested stages. Zero persists under branch zero, so each new
set contains \(q+1/p\) from branch one and fresh denominator primes really
occur. Rule 9 uses a different disjointness proof.

| Rule | Scale \(a\) | Base shift \(q\) | Purpose |
|---|---|---|---|
| 1. Intact, near gap | 1 | \(D\) | Retain internal gadget while separating copies |
| 2. Intact, wider gap | 1 | \(D+1\) | Increase separation |
| 3. Half scale, near gap | \(1/2\) | \(D/2\) | Shrink, then separate |
| 4. Intact, perturbed thirds | 1 | \(1/3\) | Keep old identities internally; perturb interleaving |
| 5. Half scale, perturbed thirds | \(1/2\) | \(1/3\) | Repair the literal map's disjointness |
| 6. Alternating scale | 2 at odd levels, \(1/2\) at even levels | \(1/3\) | Test recovery after alternating sizes |
| 7. Stage-dependent shrink | \(1/(m+1)\) at level \(m\ge1\) | \(1/3\) | Vary scales rather than repeat one contraction |
| 8. Diameter reset | \((5/3)/D\) | \(1/3\) | Restore the old diameter before shifting |
| 9. Exact thirds | \(1/p\) | Exact shifts \(r/3\), no perturbation | Keep the shifts; choose fresh \(p>3D\), making each copy shorter than \(1/3\) |

For rule 9, \(p\) is also larger than the previous prime and absent from
the old denominators. The point obtained by repeatedly taking branch zero
from the initial \(1/3\) retains every new prime in its denominator.
All nine rules therefore have unbounded denominator-prime support if
continued. They escape that hypothesis of the historical fixed-prime
theorem. Escaping an obstruction is not evidence of output compression.

### Full image counts and the rate test

Every row below starts from \(n_0=6,s_0=22\). Every rule gives
\(n_1=18,n_2=54,n_3=162\), so each effective \(\lambda_m=3\).

| Rules | \(s_1\) | \(s_2\) | \(s_3\) | \(\rho_1/9\) | \(\rho_2/9\) | \(\rho_3/9\) |
|---|---|---|---|---|---|---|
| 1, 2, 4 | 282 | 2790 | 25866 | \(47/33\) | \(155/141\) | \(479/465\) |
| 3, 5, 7 | 312 | 2916 | 26244 | \(52/33\) | \(27/26\) | 1 |
| 6 | 324 | 2790 | 26226 | \(18/11\) | \(155/162\) | \(47/45\) |
| 8 | 282 | 2916 | 26244 | \(47/33\) | \(54/47\) | 1 |
| 9 | 288 | 2880 | 26136 | \(16/11\) | \(10/9\) | \(121/120\) |

These are **complete scalar support counts**. The nine block images,
pairwise intersections, all higher intersection masks, every difference
slice, and multiplicities of every actual ordered pair are retained in
the exact data. Overlapping branch labels, if present, are never counted
as distinct scalar pairs. Here the branch copies were disjoint at every
tested step.

Using the two old identity templates gives the following total savings
from \(n_m^2\); the last column lists further savings not explained by
those templates:

| Rules | Old-template savings at levels 1,2,3 | Additional savings |
|---|---|---|
| 1, 2, 4 | \((42,126,378)\) | \((0,0,0)\) |
| 3, 5, 7 | \((12,0,0)\) | \((0,0,0)\) |
| 6 | \((0,126,0)\) | \((0,0,18)\) |
| 8 | \((42,0,0)\) | \((0,0,0)\) |
| 9 | \((12,36,108)\) | \((24,0,0)\) |

“Additional” does not mean accidental. For example, rule 9 at level one
contains instances of the exact translated identity
\[
P(t,t+3/7)=P(t,t+5/7)=2t+120/343.
\]
It follows because \((3/7)^2+(3/7)(5/7)+(5/7)^2=1\).
The alternating rule's eighteen extra equalities at level three all use
\[
P(t+26/21,t)=P(t+34/21,t+8/3),
\]
another translated-slice identity. Such new finite coincidences are real,
but none supplies a tested repeated positive rate.

Full portable counts, exact parameters and raw-file hashes:
[the continuation JSON](../../../examples/2026-09-16-three-branch-continuation.json).
The 27 lossless certificates are in
`local-only/runs/T01/2026-09-16-three-branch-continuation/` and must travel
separately in a local handoff. The reusable implementation is
[three_branch_continuation.py](../../../experiments/three_branch_continuation.py).
No new infinite claim is inferred from three levels.

## 9. The rigorous rate calculation with input losses

The required inequality is \(\rho<\lambda^2\). Small relative losses
at each step can accumulate, so an input ratio tending to \(\lambda\)
gives \(n_m=\lambda^{m+o(m)}\), not necessarily
\(n_m\asymp\lambda^m\). For instance \(\lfloor3^m/(m+1)\rfloor\)
almost triples but is not comparable to \(3^m\) by fixed constants.
The strict exponent conclusion still follows.

**TC-R1–R3 — PROVED implication.** If \(n_m\to\infty\),
\[
\liminf n_{m+1}/n_m\ge\lambda>1,\quad
s_{m+1}\le\rho s_m+C n_m^{2-\delta},\quad
1\le\rho<\lambda^2,
\]
with fixed \(C,\delta>0\), then every
\[
0<c<\min\{2-\log_\lambda\rho,\delta\}
\]
gives \(s_m\le n_m^{2-c}\) eventually.

**Proof.** Choose \(p<2-c\) but larger than
\(\log_\lambda\rho\) and \(2-\delta\), and slightly decrease
\(\lambda\) to \(\lambda_0>1\) with \(\rho<\lambda_0^p\).
Eventually the inputs grow by at least \(\lambda_0\). Induction on
\(s_m\le Dn_m^p\) absorbs the smaller-order error into
\(D(\lambda_0^p-\rho)n_m^p\). The remaining strict gap absorbs the
fixed \(D\). Full details are in [rates-and-fiber-maps.md](rates-and-fiber-maps.md). ∎

For finite steps there is an especially simple diagnostic:
\[
\frac{\rho_m}{\lambda_m^2}
=\frac{s_{m+1}/n_{m+1}^2}{s_m/n_m^2}.
\]
A good step lowers output density. It does not show that density continues
to fall at a fixed exponential rate. No current candidate meets the
all-level hypotheses of the rate implication.

## 10. One nonlinear extension, and its missing Cartesian property

After the affine identity analysis, one natural extension was examined
symbolically. Instead of specifying a constant shift for each input
separately, move a pair to a neighboring difference slice and adjust both
coordinates together to preserve the output.

**TC-Q1–Q2 — PROVED algebra, OPEN construction.** With \(u=x-y\), define
\[
H_\tau(u)=3\tau u^2+3\tau^2u+\tau^3,\qquad
T_\tau(x,y)=\left(x+\frac{\tau-H_\tau(u)}2,
y-\frac{\tau+H_\tau(u)}2\right).
\]
Then \(P(T_\tau(x,y))=P(x,y)\) and
\(T_\sigma T_\tau=T_{\sigma+\tau}\).

**Proof.** The new difference is \(u+\tau\) and the new sum is
\(x+y+u^3-(u+\tau)^3\). The cubic terms cancel exactly. Successive
increments add, proving the composition law. For \(\tau\ne0\), however,
the map cannot send a whole nonempty finite square \(A^2\) into itself:
it moves its largest or smallest difference outside \(A-A\). ∎

The original identity with differences \(1/3,-2/3\) is one instance of
\(T_{-1}\). This extension is tied to the gadget, but it is a map of
**pairs**, not three one-variable branches. A useful large set of partial
returns to \(A^2\) has not been constructed. No nonlinear numerical search
or second unrelated family was launched.

## 11. Gain-versus-cost ledger and previous no-go compatibility

This ledger instantiates the project's
[construction template](../../templates/CONSTRUCTION_LEDGER.md).
Each carrier uses the same real set in both coordinates. Rates use actual
depth and actual scalar input counts.

| Cost or gain | Literal iteration | Separated copies / finite-rule continuation |
|---|---|---|
| Input lower and upper count | Exactly \(4\cdot2^m+2\) | Exactly \(3n\) under disjointness; all nine tested rules have this property |
| Branch multiplicity and thinning, charged twice | Individual branches injective; exactly \(n+2\) duplicate labels lost each step; squared comparison uses actual \(2n-2\) | No thinning in tested rules; actual scalar pairs counted once; general overlapping models require a fresh count |
| Real projection | Identity, no fibers | Identity on exact rationals or specified real parameters |
| Full support | \(n^2-O(n^{3/2})\le s\le n^2\) | Sufficient separation: exact \(6n^2+3s_a\); tests: complete stored nine-block unions |
| Difference/move inventory | All pairs included in true image; congruence discards some pairs only from a lower-bound injection | \(L\) differences cover at most \(LN\) pairs; \(M\) allowed moves save at most \(2MN\) labels; unknown extra collisions are not free |
| Exceptional and uncovered pairs | Exactly \(n^2/Q+2-4/Q\) omitted from lower-bound injection, never from complete support | Zero uncovered pairs in exact counts; bounded-rule certificate leaves a quadratic pair tail |
| Denominators and coefficient heights | Actual \(3\cdot2^m\) denominator, all terms retained after clearing | Exact growing rational denominators recorded at every tested level; no bounded-height assumption |
| Archimedean size and scale distortion | Inputs bounded, but exact image still quadratic | Old collisions change by (3.1); large centers enter every mixed term; profiles stored, no volume saving claimed |
| Local moduli and splitting | Powers of two prove injectivity, not sparsity | Fresh primes ensure disjoint inputs; they are not claimed to save outputs; no field splitting invoked |
| Field degree, discriminant, regulator, class number | Rational field degree 1; no unit/ideal/tower construction | Rational experiments or purely real lemmas; number-field costs inapplicable here, unknown for any later proposed tower |
| Carries, block counts, ratio counts | Full cubic denominator formula used | All nine blocks and intersections included; no ignored mixed terms or formal-state substitution |
| Input/output rate | \(a=B=\log2\), \(b=2\log2\); gap \(2a-b=0\) | Sufficiently separated stages have output at least \(\tfrac23 N^2\); other tested rules have no proved favorable asymptotic \(b\) |
| Certified power-saving exponent | None | None |

Literal iteration contains the normalized prefix
\(\{0,\ldots,3\cdot2^m-1\}/(3\cdot2^m)\), so it also meets the
reported fixed-prime positive-entropy obstruction's hypotheses. That route
was stopped; the new self-contained proof is stronger for this particular
family. The old named digital and rich-fiber full checkpoints remain
**MISSING SOURCE / PROVENANCE FILE**, as recorded in the prior source audit;
we do not claim to have recertified them.

The new rational rules introduce genuinely growing prime support. The
old fixed-prime theorem therefore does not apply to those rules as stated.
They still face the exact identity and complete-image counts above.
No positive-volume window, cube-residue/uniform-lift certificate, literal
\(GP\), norm-one trace, or rejected rich-quadratic-fiber carrier is used.

**Arithmetic amplification was not started.** There is no reusable local
scalar mechanism with a positive rate to amplify. Chebotarev or tower
existence would not fill that gap. No absent external theorem or constant
was reconstructed from memory, and no primary arithmetic paper was invoked.

## 12. Claim ledger, provenance, and verification

Every new claim below has track T01, branch “three-branch continuation,”
the fixed plus-sign cubic, and version/date 2026-09-16 continuation v1.
Quantifiers and hypotheses are stated in the cited section/companion.
Dependencies are elementary algebra, counting and the preserved prior
gadget table; no external research theorem is used in the new proofs.

| Claim | Status and exact evidence | Audit and retained gap |
|---|---|---|
| TC-A1 | **PROVED**, all fourteen gadget savings; affine companion §1, full witness table | Lead checked identities against prior complete data; finite only |
| TC-A2–A3 | **PROVED**, common-scale preservation and all affine-line identities; companion §§2–3 | Coefficient proofs internally audited; other finite coincidences not excluded |
| TC-A4–A6 | **PROVED scoped bounds**, difference/move inventories and inherited block matchings; companion §§4–5 | Certificate bounds distinguished from actual-image bounds; unlisted relations OPEN |
| TC-D1–D3 | **PROVED / FAILED family**, exact literal inputs and asymptotically quadratic actual image; direct companion §§1–2 | Complete congruence/count proof independently audited; adaptive families outside scope |
| TC-D4–D5 | **PROVED / FAILED class**, all finite carriers with sufficiently separated copies, including common scales; companion §3 | Finite-exception condition essential; deliberately exceptional parameters not excluded |
| TC-E1 | **EXPERIMENTAL exact**, nine predetermined rules, three levels each; JSON and code | Complete pair/block/slice data; no infinite inference |
| TC-E2 | **PROVED**, all nine explicitly specified rules triple the input at every level and have unbounded denominator-prime support; §8 | Prime-integrality or interval disjointness, and surviving-point proofs inspected; output rate still OPEN |
| TC-R1–R3 | **PROVED implications**, corrected input growth and strict-exponent gate; rates companion §§1–3 | Application CONDITIONAL on actual uniform rates, not currently supplied |
| TC-Q1–Q2 | **PROVED algebra / OPEN construction**, one quadratic pair-map family; rates companion §§4–5 | Output preservation and global finite-square obstruction audited; useful partial returns unproved |
| TC-O1 | **OPEN**, fixed positive exponent for arbitrarily large real inputs | No current positive construction; no universal impossibility asserted |

New files comprise this report and its three proof companions, a reusable
experiment module, tests, portable finite counts, and ignored raw output.
Only dated T01 navigation addenda are appended to existing status records.
Earlier reports, archives, SPECs, canonical JSON and inherited changes are
preserved. Commands, hashes, finite budgets, source availability and final
check results are in [verification.md](verification.md). Internal audit
does not mean external review or established novelty.

## 13. Exactly one next proof obligation

**Determine whether one fixed quadratic slice motion can have a positive
proportion of Cartesian returns.** Use the explicitly defined \(T_1\)
above, which is the inverse direction of the gadget's main slice matching.
For \(N\ge1\), set
\[
R_1(N)=\sup_{A\subset\mathbb R,\ |A|=N}
\frac{|\{(x,y)\in A^2:T_1(x,y)\in A^2\}|}{N^2}.
\]
Decide whether \(\limsup_{N\to\infty}R_1(N)>0\), by an explicit
growing carrier, or prove \(R_1(N)\to0\). This asks a concrete question
about the first nonlinear extension of the actual gadget identity. A
positive answer would provide repeated partial slice overlap, but would
still not establish a power saving without further multiplicity and full
support control. No positive answer is conjectured, and no further cycle
is launched by this recommendation.
