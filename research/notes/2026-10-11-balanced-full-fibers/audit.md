# Independent full-fiber and counting audit

11 October 2026 · T03 · fixed polynomial
\(Q(x,y)=x^2+xy+y^2\) · version 4.

## 1. Authorization, carrier, and evidence boundary

The current authorized cycle studies unrestricted full fibers of the
**unchanged balanced-factor carrier** from
[the 6 October checkpoint](../2026-10-06-cross-block-amplification/README.md).
The lead commissions exact full-square scouts only at depths r=0,1 and
one separate symbolic coupled phase/switch mechanism. This specialist
audits counting, equality, proof scope, and rates. It does not create
another candidate, run mathematical programs, use the network, or delegate
to further agents. Its allocated mathematical evaluation and program-CPU
budgets are both zero; the lead owns the shared 2,000,000-evaluation,
600-CPU-second cap and 20% reserve.

The frozen carrier is
\[
q=7^r,\quad \xi=e^{2\pi i/q},\quad
c_{h,\mathbf i}=h\prod_{\ell<r}(2-\xi^{i_\ell7^\ell}),
\quad 1\le h\le8,\quad i_\ell\in\{-3,\ldots,3\}.
\]
With \(\omega=e^{2\pi i/3}\), \(\Delta=1+2\omega\), put
\[
Z_r=\bigcup_{h,\mathbf i}c_{h,\mathbf i}\mu_{6q},\qquad
X(z)=\frac{\omega\bar z-\omega^2z}{\Delta},\quad
Y(z)=\frac{\bar z-z}{\Delta},\quad A_r=X(Z_r)=Y(Z_r).
\]
The inherited AMP-A1–A3 proofs establish \(A_r=-A_r\),
\(0\in A_r\), \(A_0=\{-8,\ldots,8\}\), and
\(8q^2\le|A_r|\le48q^2\) for r≥1. Their exact encoded norm
counts are not full-square norm counts.

The inherited AMP-R1–R3 theorem concerns a specified certificate of
independent factor switches, sign/swap, encoded edges, and finite
iterations. Its bounded certificate counts are **not upper bounds on
full fibers**. Both the previous theorem and that limitation are retained.
Only the new authorized task investigates full fibers of this fixed
carrier. A finite histogram cannot prove a uniform asymptotic exponent.

Current startup inspection covered the inherited Git state/diff summary,
setup and source map, T03 state and specification, the relevant migration
limitations and library entries, and the complete controlling checkpoint.
The companion proofs were independently audited in the prior cycle;
their provenance is retained rather than described as a new full proof
audit solely because their summaries were reread.

## 2. BFF-C1 — exact sign/swap representatives and weights

**PROVED; independently derived for this counting audit.** Let
\(A=-A\subset\mathbb R\) be finite with \(0\in A\), and write
\(n=|A|=2s+1\). Consider the four maps
\[
(x,y),\quad(-x,-y),\quad(y,x),\quad(-y,-x).
\tag{1}
\]
They preserve Q and A². The orbit size \(w(x,y)\) is exactly
\[
w(x,y)=
\begin{cases}
1,&x=y=0,\\
2,&x=y\ne0\text{ or }x=-y\ne0,\\
4,&\text{otherwise}.
\end{cases}
\tag{2}
\]
In particular, a nonzero axis pair has weight four, not two.

Choose one representative \(b_i\) from each nonzero sign pair
\(\{a,-a\}\), and put these representatives in any fixed total
order, indexed \(1,\ldots,s\). They need not be the positive real
elements. An exact algebraic coefficient-key order suffices and avoids
numerical comparisons of algebraic real numbers. The following list has
exactly one representative of every orbit in (1):
\[
(0,0),\qquad (b_i,0)\ (1\le i\le s),\qquad
(b_i,b_j),\ (b_i,-b_j)\ (1\le j\le i\le s).
\tag{3}
\]
The first representative has weight one; the axis representatives have
weight four; the two representatives with i=j each have weight two; and
all i>j representatives have weight four.

**Proof of uniqueness and completeness.** A pair with one nonzero
coordinate has a unique sign class, and swap plus simultaneous sign moves
it to its unique listed axis representative. If both coordinates are
nonzero, order their two sign-class indices so i≥j by swap, then use
simultaneous sign to make the first coordinate \(b_i\). The second
coordinate is uniquely \(b_j\) or \(-b_j\). When i=j these give
the diagonal and antidiagonal orbits separately. When i>j their two relative
sign choices remain different orbits. The origin is separate. This proves
(3); direct inspection of the four maps gives (2).

Consequently there are
\[
1+s+2\sum_{i=1}^s i=(s+1)^2=\frac{(n+1)^2}{4}
\tag{4}
\]
representatives. Their weight counts are
\[
N_1=1,\qquad N_2=2s=n-1,\qquad N_4=s^2,
\qquad \sum w=1+4s+4s^2=n^2.
\tag{5}
\]
This is an exact exhaustive enumeration of A² modulo proved symmetries,
not a sample. Its implementation still must deduplicate actual A first,
verify negation closure and zero, and use exact canonical equality keys.
It must not infer equality from floating-point embeddings.

## 3. Recovering full fibers and pair-weighted statistics

For an actual output t define
\[
f_t=\#\{(x,y)\in A^2:Q(x,y)=t\}.
\]
An exact output counter over the representatives (3), adding w rather
than one at each representative, satisfies
\[
f_t=\sum_{p\text{ in (3)}} w(p)\,\mathbf1_{Q(p)=t}.
\tag{6}
\]
Every orbit lies in one Q-fiber, and the orbits partition A², proving
(6). Different sign/swap orbits may have the same output and must be
merged into that same counter entry. In particular w is an initial
guaranteed orbit size, not the claimed final fiber size.

Distinguish the output-weighted and pair-weighted histograms:
\[
K_f=\#\{t:f_t=f\},\qquad
H_f=\#\{p\in A^2:F_A(p)=f\}=fK_f,
\quad F_A(p)=f_{Q(p)}.
\tag{7}
\]
Required exact cross-checks are
\[
\sum_f K_f=|Q(A,A)|,\qquad
\sum_f fK_f=\sum_f H_f=n^2,\qquad
\sum_f\frac{H_f}{f}=|Q(A,A)|.
\tag{8}
\]
The last sum is integral because each H_f is a multiple of f.
The pair-weighted mean full fiber and the collision energy agree as
\[
\frac1{n^2}\sum_f fH_f
=\frac1{n^2}\sum_f f^2K_f.
\tag{9}
\]
They do not imply an upper bound on the image beyond any separately
proved support estimate. A pair-weighted median must use H, whereas an
output-weighted median uses K; these generally differ. Here n² is odd,
so the pair-weighted median is the first f whose cumulative H reaches
\((n^2+1)/2\). Any other quantile convention must be named explicitly.

Positive definiteness gives the exact zero fiber \(f_0=1\), supplied
only by (0,0). Every nonzero full fiber is even because simultaneous
negation has no nonzero fixed point. Every representative must satisfy
\(f_{Q(p)}\ge w(p)\); these are further exact checks.

### Strict quarter-power tail

For the strict threshold in this cycle, no floating-point fourth root
or rounded cutoff is necessary:
\[
F_A(p)<n^{1/4}\quad\Longleftrightarrow\quad F_A(p)^4<n.
\tag{10}
\]
Hence its exact pair count is
\(\sum_{f^4<n}H_f\). Equality \(f^4=n\) is excluded.
Using \(F\le\lfloor n^{1/4}\rfloor\) would be wrong when n
is a fourth power. The equivalent integer cutoff is
\(F<\lceil n^{1/4}\rceil\), if the ceiling itself is obtained
exactly.

### Measuring returns beyond the symmetry baseline

For a representative p, its source orbit contributes w(p) points to
the full fiber. The number of additional targets is exactly
\(f_{Q(p)}-w(p)\). Thus the pair-weighted number of sources with
any target beyond their own sign/swap orbit is
\[
\sum_{p\text{ in (3)}}w(p)
\mathbf1_{f_{Q(p)}>w(p)}.
\tag{11}
\]
Testing only \(F_A(p)>4\) would miss genuine extra targets at
diagonal or antidiagonal sources with baseline two. Conversely, labeling
every source with fiber four as nontrivially rich would incorrectly
include generic sources explained entirely by (1).

## 4. Sharper scalar-size identity: independent symbolic check

The complete [algebra.md](algebra.md), BFF-A1–BFF-A4, was read and
independently checked. In particular, the new exact identity on the
unchanged carrier is valid. Let
\[
H=\mathbb Q(\xi),\quad
B=\{h\xi^aP_{\mathbf i}:1\le h\le8,\ a\bmod q\},\quad
D_B=\{\bar b-b:b\in B\}.
\]
Inherited coset disjointness gives \(|B|=8q^2\),
\(\bar B=B\), and \(B\cap(-B)=\varnothing\). Directly,
\(X(\bar b)=X(b)+Y(b)\) and
\(Y(b)=X(\bar b-b)\). Therefore
\[
A=X\bigl(B\cup(-B)\cup D_B\bigr).
\tag{12}
\]
The three sets inside this union are disjoint. The elements of D_B are
purely imaginary, whereas B contains no nonzero purely imaginary element:
such a b would have \(\bar b=-b\in B\cap(-B)\). The same applies
to −B, and 0 is in neither. Since X is injective on H,
\[
n=16q^2+|D_B|,
\qquad 16q^2+1\le n\le24q^2-7.
\tag{13}
\]
For the upper bound the eight distinct elements b=h all map to zero in
D_B; hence \(|D_B|\le|B|-7\). This argument also works at q=1,
where D_B={0} and n=17. It does not require classifying other collisions
of the map \(b\mapsto\bar b-b\).

For completeness the proposed exact multiplication formula was checked:
\[
X(v)X(w)=X\left(\frac{2vw+v\bar w+\bar v w-\bar v\bar w}{3}\right)
\qquad(v,w\in H).
\tag{14}
\]
Indeed write v=s+a and w=t+b with s,t fixed and a,b negated by complex
conjugation. Then \(X(v)=s+a/\Delta\), while the argument of X
on the right is \(st-ab/3+sb+at\). Equation (14) follows from
\(\Delta^2=-3\). This is an arithmetic identity, not a projection
count or image bound.

The companion's full-output component test was also checked. Writing
v=s+a and w=t+b as above,
\[
Q(X(v),X(w))
=s^2+st+t^2-(a^2+ab+b^2)/3
 +(2sa+sb+ta+2tb)/\Delta.
\tag{14a}
\]
Its first component lies in \(F=H\cap\mathbb R\) and its numerator
in the second component is imaginary in H. The components are independent
because \(\Delta\notin H\). For v∈B∪(−B) and w∈D_B, the
imaginary numerator is s(2a+w) with s≠0. Thus the output lies in F
exactly when \(w=\bar v-v\), giving the encoded pair
\((X(v),Y(v))\). For D_B×D_B every output lies in F. These exact
interfaces leave the remaining full-fiber collisions unclassified;
the companion states that limitation correctly.

## 5. Pre-execution implementation inspection

The lead's local-only file
`local-only/runs/T03/2026-10-11-balanced-full-fibers/scout.py`
was read before its first execution, together with its budget definition
and the reused `Field` arithmetic in `experiments/modular_lift.py`.
This specialist did not execute them.

The mathematical implementation passed the following source inspection:

- Only r=0,1 occur. The build deduplicates actual coordinates of every
  amplitude and every phase. It stores 3A to keep exact integer coefficient
  keys. The subsequent output is Q(3A,3A)=9Q(A,A), so image cardinalities,
  full fibers, and symmetry baselines are unchanged.
- In the primary traversal, negation reverses lexicographically sorted
  coefficient tuples. The ranges \(0\le i\le(n-1)/2\),
  \(i\le j<n-i\) are another exact orbit transversal for (1).
  The orbit size is calculated from its four actual index pairs, including
  diagonal, antidiagonal, axis and zero stabilizers.
- The output counter adds that orbit size. The pair-weighted histogram,
  median and strict fourth-power test match (6)–(10).
- The baseline-exceeding count first includes all sources with full fiber
  above four, then adds precisely the smaller-orbit sources with
  \(w<F\le4\). This equals (11) without duplication.
- Verification uses the distinct transversal (3) and the norm product
  \((a-\omega b)(a-\omega^2b)\), compared with the primary expanded
  quadratic. The seed also has a separate complete integer ordered-square
  oracle. Both cyclotomic passes share the same canonical field reduction;
  they are independent formulas and traversals, not independent field
  libraries.
- The whole output distribution is digested in sorted canonical form.
  An equality of reported histograms alone would not be enough, but the
  proposed verifier compares the full value-to-fiber distribution digest.
  No sampled subset or approximate equality is used.

Two operational issues were reported before execution: the initial
`Budget.finish` lacked a final CPU guard after the last charged query,
and its counter definition included explicit scalar/field checks that
were not all charged in the initial source. A no-overwrite guard for raw
artifacts was also requested. The final executed source was reread: it
contains the CPU guard, no-overwrite guard, charges for reality, zero,
negation and canonical-selection checks, and updated forecasts. Its
verified SHA-256 is
`5e6adfbfad4e7e5ab04786c8d1c4a91f0057c925aa156332f45ba28ce42fbdff`.
All three execution records name that same hash. The shared Field source
hash is
`0be8b14d111991ec4df96141702e9f4ef156088fc70c3517abd377240b0f6f14`.
These were administrative hash checks, not mathematical program reruns.

One minor accounting omission was reported after reading the executed
source: its explicit seed-carrier comparison covered 17 scalar identities
without a separate charge. The lead recorded those already-performed
checks as a 17-evaluation discovery-budget correction, with zero new CPU
because they were timed in the original build. No mathematical rerun was
performed. The exact executed bytes are preserved as `scout-executed.py`
with the hash above. The reproduction `scout.py` now charges the checks
inline and has SHA-256
`2d39ec1d787e6772d45fc5fd67304952219aaed8888a90115f73cabc6765418b`.
Both hashes and the explicit correction record were read and checked.
The correction changes neither the finite mathematical data nor the
identity of the code that actually generated them.

## 6. Saved finite evidence: inspected, not rerun

The saved `scout-results.json` and `verification-results.json` were read.
The latter records a PASS for the complete norm distribution in both
predeclared cases, including the independent raw integer seed square.
Their verified SHA-256 values are, respectively,
`26af21bfb86e74ea3900ce165274c08514527b54d13705cddebc5bb945f8c309`
and
`d37ddc5277e51b8c7b3cc8019ac38772cc410ee4d70a40b180305a616f3d2792`.

**EXPERIMENTAL — complete exact enumeration at r=0,1 only.**

| r | n | Ordered pairs | Image size | Pair median F | Pairs with F⁴<n | Pairs exceeding their own sign/swap orbit | Maximum F |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0 | 17 | 289 | 44 | 12 | 9 | 216 | 18 |
| 1 | 1079 | 1,164,241 | 286,664 | 4 | 1,135,967 | 28,274 | 84 |

The displayed output and pair histograms satisfy (7)–(8). At r=0,
the pair masses at F=1,2,4,6,12,18 are respectively
1,8,64,66,132,18. Their cumulative mass before F=12 is 139,
so the median is 12; the strict quarter-power tail is 1+8=9.
At r=1 the masses at F=1,2,4 total 1,135,967, and all remaining
masses sum to 28,274. Since \(4^4<1079<6^4\), this is precisely
the reported strict tail. The output histogram sums to 286,664, whereas
its pair-weighted version sums to 1,164,241. The two weighting conventions
are not conflated.

There are 81 primary representatives at r=0 and 291,600 at r=1.
The alternate oracle covers the same complete square with a different
transversal and exact norm formula. Its saved PASS is execution evidence
from the lead, not a claim that this specialist reran the oracle. The
reported baseline statistic is computed by the correct source-orbit
formula inspected in §5; it is not inferred solely from the output
histogram.

The fiber-audit subtotal is **598,542 charged evaluations and
22.089862 research-program CPU seconds**, including the administrative
seed-check correction described above. No count was obtained by sampling,
and no depth beyond r=1 was executed by this specialist or inferred from
these records. These two depths do not establish an asymptotic full-fiber
bound, a positive saving, or a full-image obstruction.

### Packaging addendum: required existing regressions

Version 4 adds only administrative inspection of the lead's saved
repository-validation wrapper, results, log, and budget. The mathematical
proofs and the fiber-audit subtotal above are unchanged. This specialist
did not execute or rerun any regression.

The inspected wrapper is
`local-only/runs/T03/2026-10-11-balanced-full-fibers/check_regressions.py`,
with verified SHA-256
`bc459fc17b79dcc16c3bcee924801b880cce1e6aa803bf9e8257e814cd5377b1`.
It runs in-process equivalents of the required existing commands
`python3 -m unittest discover -s tests -v` and
`python3 -m experiments verify`. Its separate metering category charges
executed source-line events in the repository's experiments and tests,
including arithmetic internals, instead of reusing the scout's query
boundary counter. This is recorded as a conservative validation charge,
not as 373,301 new balanced-carrier pair evaluations.

The budget's predeclared validation policy transfers up to 1,000,000
unused discovery charges to repository verification after research stops,
with a 90-CPU-second additional limit. The overall 2,000,000-charge and
600-CPU-second caps remain unchanged. The wrapper has live line/CPU guards,
records final CPU, records any guard or error, and checks the shared totals.
Its log is opened exclusively, protecting an existing validation log.

Saved evidence confirms:

- Both commands exited 0; the regression summary has no error or guard.
- `regressions.log` reports **100 unit tests: OK** and **159 finite
  benchmark checks: passed**. These are existing regression cases, not
  additional balanced-carrier depths or an asymptotic proof.
- Additional accounting is **373,301 conservative line charges and
  0.907295 CPU seconds**. The final shared totals are therefore
  **971,843 charged units and 22.997157 program CPU seconds**.
- The log retains a nonfatal `runpy` RuntimeWarning that
  `experiments.__main__` was already present in `sys.modules` before
  the second command. Both result records still report successful
  completion. No rerun or claim of a warning-free log is made.

The independently checked saved result hash is
`bcb0728fe6a99a95c6dabc03b48e83737d6ee292b2e47c0a13689ef991fa4d08`
for `regression-results.json`; the saved log hash is
`02a5f7d9b132f113bc504f07feb5f6b6927488626a736695925b1fafabb7db0d`.
These source/result identity checks are administrative. They do not
constitute another proof audit or mathematical research run.

## 7. Scope of the proposed final full-fiber obligation

The lead's proposed next statement is a direct full-fiber question on this
same carrier, not an accepted theorem. Put
\(V=B\cup(-B)\cup D_B\), so X is a bijection V→A. If
\[
M(v,w)=2vw+v\bar w+\bar v w-\bar v\bar w,\qquad
K(v,w)=M(v,v)+M(v,w)+M(w,w),
\tag{15}
\]
then (14) gives
\(Q(X(v),X(w))=X(K(v,w)/3)\). Consequently equality of full
Q-values is exactly equality of K-values, by injectivity of X on H.

**OPEN premise; PROVED consequence only.** Suppose there are fixed
C and r₀ such that for every r≥r₀, at least \(32q^4\) sources
\((v,w)\in B^2\) have at most \((r+1)^C\) solutions
\((s,t)\in V^2\) to
\(K(s,t)=K(v,w)\). Because the target range is all of V², this
would be their full Cartesian fiber bound, not a selected return bound.
Counting these sources by their complete fibers would give
\[
|Q(A,A)|\ge\frac{32q^4}{(r+1)^C}
\ge\frac{n^2}{18(r+1)^C},
\tag{16}
\]
using n≤24q². Since n≥16·49ʳ, the denominator is \(n^{o(1)}\).
Thus the premise would retire this fixed carrier as a source of any fixed
positive compression exponent. The premise has not been proved by this
audit, the finite data, or the old certificate obstruction. No search for
it was performed here.

## 8. Final written audit of the sole coupled mechanism

**BFF-P1–BFF-P2 / PROVED in their stated certificate scope; independent
internal audit PASS.** The entire [coupled.md](coupled.md) was read,
including its full norm expansion, degenerate branches, count, closure,
and construction ledger. This was the only new mechanism submitted to
this audit, and it did not change A.

Its precise source and proposed target are
\[
p=(X(c\alpha),Y(d\beta)),\qquad
p'=(X(\kappa c'\beta),Y(\lambda d'\alpha)),
\tag{17}
\]
where c′ and d′ are independently switched bare amplitudes,
\(\alpha,\beta\in\mu_{6q}\), and
\(\kappa,\lambda\in\mu_6\). All scalar representations are
allowed. Membership is automatic; norm equality is imposed separately.
The bounded correction group \(\mu_6\) is part of the theorem's
hypotheses and is not silently replaced by arbitrary \(\mu_{6q}\)
corrections.

For fixed data except β, the complete norm defect is a Laurent polynomial
of degree at most two in each direction. Its β² coefficient after
multiplication by \(\Delta^2\) is
\[
\omega\kappa^2(c')^2-d^2.
\tag{18}
\]
The mixed scalar terms have degrees only −1 and 1 and cannot cancel it.
All five coefficients of the companion's displayed expansion were
checked. If (18) is nonzero, the resulting nonzero quartic has at most
four second phases.

If (18) vanishes, its equality in H and \(\omega\notin H\) force
\(\kappa=\tau\omega\), \(\tau=\pm1\). Bare-coset
disjointness then forces c′=d. The new first coordinate is τy, and,
with t the new second coordinate, the exact defect becomes
\[
Q(\tau y,t)-Q(x,y)=(t-\tau x)(t+\tau x+\tau y).
\tag{19}
\]
The first branch is merely ±swap. The second branch fixes Y(dβ), hence
has at most two phases; its resulting whole-pair map is
\(\tau(y,-x-y)\), with its domain still determined by (17).
The written example \((0,1)\mapsto(1,-1)\) is correct and already
belongs to the encoded set. It is not credited as generic amplification.

The complete source-label bound for a target outside the source's
four-point sign/swap orbit is
\[
(8q)^2\,4^r\,(6q)\,36\,4
=55296q^3 4^r.
\tag{20}
\]
This counts independent switch masks, both correction units and all
source representations. The refined input lower bound n≥16q² gives
the fraction \(216(4/7)^r\), correctly stated in the companion.

Reversal uses the same masks and correction pair
\((\lambda^{-1},\kappa^{-1})\). Coordinate swap uses the source
phases \((\omega\beta,\omega^2\alpha)\) and correction pair
\((\omega^2\lambda,\omega\kappa)\). These formulas stay inside
\(\mu_6\), and simultaneous sign is obtained by negating both source
phases. They prove the exact symmetry invariance needed for the iteration
argument, rather than assuming it from a count.

After adjoining the old coordinate-switch certificate, all sign/swap
edges, and every equal-norm edge inside Γ, the exceptional union has
size at most
\[
56832q^3 4^r+48q^2,
\qquad
\frac{|E|}{n^2}\le222(4/7)^r+\frac{3}{16q^2}=o(1).
\tag{21}
\]
Outside this symmetry-invariant union, each allowed edge remains in the
same four-point orbit; induction gives at most four targets under any
finite path. Thus this enlarged certificate fails a polynomial return
lower tail, even allowing fixed constants in its exceptional-set bound.
The inequality remains \(R_*(p)\le F_A(p)\). Nothing here permits
turning the certificate upper bound into an unrestricted full-fiber
upper bound.

## 9. Final inspection register and unresolved claims

| Claim or evidence | Audit performed | Exact remaining limit |
|---|---|---|
| BFF-C1 / BFF-A4 symmetry enumeration | Independent derivation and written/code inspection | Counts complete squares by exact weights; not an asymptotic fiber theorem |
| BFF-A1–BFF-A3 scalar algebra | Complete written proof independently checked | No full-image bound follows solely from the scalar count or component test |
| r=0,1 full histograms | Code inspected; saved full-validation PASS and source hashes checked; no rerun by this specialist | EXPERIMENTAL over these two fixed depths only |
| Required repository regressions | Wrapper, successful saved results, budget and hashes inspected administratively | 100 tests and 159 finite checks; no proof status changes or rerun by this specialist |
| BFF-P1–BFF-P2 | Complete written proof independently checked, including refined constants and finite-path closure | Failure only for the precisely defined phase-transposed/enriched certificate |
| Proposed full-fiber lemma in §7 | Consequence and constants checked, premise not searched | OPEN; no positive-density subpolynomial-fiber theorem is asserted |

Only this new audit companion was edited by this specialist. The final
shared lead budget is recorded in §6; this specialist used zero
mathematical evaluations and zero research-program CPU. File reads and
hash checks were administrative. No network, nested agent, additional
finite case, carrier change, or extra mechanism was used.

Unrestricted asymptotic full-fiber growth, a power-saving lower tail,
and an entire-image upper bound for this carrier remain **OPEN**.
The frozen selected-certificate obstruction is retained in its original
scope. The single proposed full-fiber obligation is distinct from that
closed certificate; its proof would have the explicit consequence (16),
but it is not an implication of the saved finite data.
