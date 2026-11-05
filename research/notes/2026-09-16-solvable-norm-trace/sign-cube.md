# NT-20260916-3 — exact images of multiquadratic sign cubes

## Identity and provenance

- **Claim ID / version:** NT-20260916-3, 16 September 2026, version 1.
- **Track / branch:** shared solvable-extension investigation, tested on the
  fixed T03 polynomial \(q(x,y)=x^2+xy+y^2\) and the separate T01 norm–trace
  benchmark \(P_0(x,y)=x^2+xy+y^2+x\). The T01 cubic is not replaced.
- **Status:** the exact cardinality theorem below is **PROVED**, with its
  complete argument recorded here and independently audited internally during
  this task. This particular carrier is **FAILED** for fixed power-saving
  compression of either displayed polynomial. Both underlying construction
  problems remain **OPEN**.
- **Authorization / scope:** the user's current solvable-extension and
  norm–trace research request; a bounded audit and write-up of the explicit
  carrier below. This subtask performed no numerical search or experiment,
  used no network, and made no literature or novelty assessment.
- **Proof source:** this file, “Elementary field lemma,” “Exact image theorem,”
  and their proofs, version 1. The parent proposed the carrier and formulas;
  a separate agent checked the coefficient argument, small-depth cases,
  square-class basis justification and fiber counts; the parent then reviewed
  that proof. This is internal review, not external certification.
- **Context inspected:** `local-only/migration/sources/T03_CURRENT_STATE.md`
  §3 and §10, especially its multiquadratic/Kummer dependency statement;
  `research/tracks/03-eisenstein-cartesianization/STATUS.md`;
  `research/MECHANISM_LIBRARY.md`, `research/FAILURE_LIBRARY.md`, and
  `research/MIGRATION_CONFLICTS.md`. No inherited construction theorem is
  needed for the proof below. The field lemma is proved here rather than
  relying on the source's recorded external dependency.
- **Historical relation:** this is a separate sign-cube carrier, not an
  adaptive-radical level or a change to RC15/4. No earlier record is superseded.
  No mathematical source gap is required by this self-contained proof.

## Construction and parameter order

Fix once and for all an infinite sequence of distinct positive primes
\(p_1,p_2,\ldots\), for example the primes in increasing order. Then let the
integer depth \(m\ge1\) grow, and put

\[
K_m=\mathbb Q(\sqrt{p_1},\ldots,\sqrt{p_m}),\qquad
A_m=\left\{\sum_{i=1}^m\varepsilon_i\sqrt{p_i}:
\varepsilon_i\in\{-1,1\}\right\}\subset\mathbb R.
\]

Every square root denotes the positive real root in the displayed embedding.
Both coordinates use exactly \(A_m\). The two polynomials are fixed before
\(m\) grows, and their coefficients do not involve the primes or the depth.

## Elementary field lemma

**PROVED.** For each \(r\ge0\), the field \(K_r\) has degree \(2^r\) over
\(\mathbb Q\), with basis

\[
b_S=\prod_{i\in S}\sqrt{p_i},\qquad S\subseteq\{1,\ldots,r\}.
\]

Moreover, a nonzero rational number \(t\) is a square in \(K_r\) if and only if

\[
t=u^2\prod_{i\in S}p_i
\quad\text{for some }u\in\mathbb Q^\times
\text{ and }S\subseteq\{1,\ldots,r\}.
\tag{1}
\]

**Proof.** Induct simultaneously on the basis assertion and (1). At \(r=0\)
both assertions are the definitions for \(\mathbb Q\). Suppose they hold at
\(r-1\). If \(p_r\) were square in \(K_{r-1}\), (1) would express it as a
rational square times a product of preceding primes. Taking the exponent of
\(p_r\) in numerator minus denominator gives an odd exponent on the left and
an even exponent on the right, a contradiction. Hence adjoining
\(\sqrt{p_r}\) doubles the degree, and adjoining the old basis multiplied by
\(\sqrt{p_r}\) gives precisely the asserted new basis.

For the square criterion, write a prospective square root of
\(t\in\mathbb Q^\times\) uniquely as \(z=u+v\sqrt{p_r}\), where
\(u,v\in K_{r-1}\). In

\[
z^2=u^2+p_rv^2+2uv\sqrt{p_r}=t,
\]

the coefficient of \(\sqrt{p_r}\) over \(K_{r-1}\) is zero. Since this is a
field of characteristic zero, \(u=0\) or \(v=0\). Consequently either \(t\)
or \(t/p_r\) is a square in \(K_{r-1}\). The induction hypothesis gives
(1). Conversely, the displayed expression in (1) has square root
\(u b_S\) in \(K_r\). This completes the induction. \(\square\)

In particular, the elements \(1\), \(\sqrt{p_i}\), and
\(\sqrt{p_ip_j}\), \(i<j\), are linearly independent over \(\mathbb Q\).
Different sign vectors therefore give different real inputs, so

\[
|A_m|=2^m=:n.
\tag{2}
\]

No element of \(A_m\) is zero. The field is totally real, and independent
sign changes of its square roots are automorphisms, as follows directly from
the basis and the relations \((\sqrt{p_i})^2=p_i\). Thus its Galois group is
\((\mathbb Z/2\mathbb Z)^m\), in particular abelian and solvable.

## Exact image theorem

**PROVED — all depths and all ordered pairs.** For every \(m\ge1\),

\[
\boxed{|q(A_m,A_m)|=\frac{n^2}{4}+\frac n2,\qquad
|P_0(A_m,A_m)|=n^2,\qquad n=2^m.}
\tag{3}
\]

### Homogeneous image: coefficient recovery and complete fibers

Write
\(x=\sum_i\varepsilon_i\sqrt{p_i}\) and
\(y=\sum_i\eta_i\sqrt{p_i}\). Expanding gives the constant coefficient

\[
\sum_i p_i(2+\varepsilon_i\eta_i)
\tag{4}
\]

and the coefficient of \(\sqrt{p_ip_j}\), for \(i<j\),

\[
c_{ij}=2\varepsilon_i\varepsilon_j+
\varepsilon_i\eta_j+\eta_i\varepsilon_j+
2\eta_i\eta_j.
\tag{5}
\]

There are no singleton basis terms \(\sqrt{p_i}\). Define the labeled parts

\[
E=\{i:\eta_i=\varepsilon_i\},\qquad
D=\{i:\eta_i=-\varepsilon_i\}.
\]

Then (5) becomes

\[
c_{ij}=\begin{cases}
6\varepsilon_i\varepsilon_j,&i,j\in E,\\
2\varepsilon_i\varepsilon_j,&i,j\in D,\\
0,&\text{one index in each part}.
\end{cases}
\tag{6}
\]

The field lemma permits recovery of each coefficient from the real output.
For \(m\ge3\), coefficients of absolute value six identify the edges inside
any \(E\)-part of size at least two; those of absolute value two identify the
edges inside any \(D\)-part of size at least two. At least one part has size
at least two. If the other part is a singleton, its vertex has zero
coefficient to every other vertex and receives the opposite label. Thus the
labeled partition \((E,D)\) is uniquely recovered, including empty parts.

The small-depth cases also recover that partition. For \(m=2\), a nonzero
mixed coefficient has absolute value six or two and identifies the unique
nonempty part. If the coefficient is zero, both parts are singletons; their
two possible assignments have constants \(3p_1+p_2\) and \(p_1+3p_2\),
which differ because \(p_1\ne p_2\). For \(m=1\), the constants are
\(3p_1\) and \(p_1\), again distinct.

Once the partition is known, (6) determines all pairwise products of the
\(\varepsilon_i\) within each part. In a nonempty part, choose an anchor
index: its sign determines every other sign through these products. Exactly
two choices remain, corresponding to reversing all signs in that part.
This also describes a singleton part, whose one sign is free. The signs
\(\eta_i\) then follow from the part labels. Conversely, reversing the signs
of both \(\varepsilon_i\) and \(\eta_i\) on an entire part preserves
(4)–(6), so all these choices do give the same output.

It follows that the full fiber has size two when one part is empty, precisely
when \(y=x\) or \(y=-x\). It has size four when both parts are nonempty.
The first class contains exactly \(2n\) ordered pairs: its two conditions are
disjoint since \(x\ne0\). No fiber crosses these classes, by the recovered
partition. Therefore every ordered pair is accounted for, and

\[
|q(A_m,A_m)|=\frac{2n}{2}+\frac{n^2-2n}{4}
=\frac{n^2}{4}+\frac n2.
\]

### Linear perturbation: injectivity on the whole Cartesian square

The coefficient of \(\sqrt{p_i}\) in \(P_0(x,y)=q(x,y)+x\) is exactly
\(\varepsilon_i\), because \(q\) has no singleton basis terms. Equality of
two outputs therefore forces equality of the first inputs, say \(x=x'\).
With that input fixed,

\[
q(x,y)-q(x,y')=(y-y')(x+y+y').
\tag{7}
\]

The second factor cannot vanish: in the basis of singleton square roots,
each coefficient of \(x+y+y'\) is a sum of three signs, belonging to
\(\{-3,-1,1,3\}\). Linear independence rules out zero. Hence (7) vanishes
only when \(y=y'\). All \(n^2\) ordered pairs have distinct \(P_0\)-outputs,
proving the second formula in (3). \(\square\)

## Quantitative construction ledger

All logarithms here are natural, and all exponential rates use actual depth
\(m\), not field degree. The rows apply to both polynomials unless stated.

| Gain/cost | Bound, units and reason | Status |
|---|---|---|
| Input count before losses | Exactly \(n=2^m\), by the field lemma and (2) | PROVED |
| Input thinning, both coordinates | None: each coordinate uses all \(2^m\) sign vectors; both losses are zero | PROVED |
| Parameter and real-projection fibers | One sign vector per real input; multiplicity one | PROVED |
| Fixed-polynomial transport | Identity inclusion in the positive-root real embedding; no coordinate change or auxiliary polynomial | PROVED |
| Local sparsity and splitting | No congruence restriction or sieve is used; local saving is zero | Inapplicable mechanism |
| Uniform per-residue population | No residue classes are counted, so no packing estimate is assumed | Inapplicable mechanism |
| Field degree | \([K_m:\mathbb Q]=2^m=n\); input size is linear in degree, not exponential in degree | PROVED |
| Discriminant | Not estimated or assumed bounded; the exact coefficient count uses no lattice-volume or discriminant bound | Inapplicable cost to this proof |
| Regulator and units | No unit carrier or regulator estimate is used | Inapplicable mechanism |
| Heights and fixed coefficients | Input radicands are the first \(m\) terms of the fixed prime sequence; (4)–(6) record their exact effect. Polynomial coefficients stay fixed | PROVED |
| Denominators, normalization and moduli | Inputs are algebraic integers; denominators are one, and no scaling or modulus is introduced | PROVED |
| Archimedean radii and distortion | Put \(S_m=\sum_{i\le m}\sqrt{p_i}\). Every conjugate input satisfies \(\lvert a^\sigma\rvert\le S_m\); outputs satisfy \(\lvert q^\sigma\rvert\le3S_m^2\) and \(\lvert P_0^\sigma\rvert\le3S_m^2+S_m\). No volume count uses these radii | PROVED |
| Branches, ratios, covers and carries | Every sign choice is included. There is no ratio partition, affine cover or carry model. The recovered \((E,D)\) classification yields complete fibers, not a selected branch | PROVED |
| Pair multiplicities | For \(q\), exactly two on \(y=\pm x\) and four otherwise; for \(P_0\), exactly one | PROVED |
| Exceptional or uncovered pairs | None: all \(n^2\) ordered pairs occur in the two complete counts | PROVED |
| Final output rate \(g=c-s\) | For \(q\), \(\log\lvert q(A_m,A_m)\rvert=2m\log2-\log4+\log(1+2^{1-m})\); for \(P_0\), exactly \(2m\log2\). Thus \(g=2\log2\) for both | PROVED, actual image rate |
| Input rates \(a,B\) | \(\log\lvert A_m\rvert=m\log2\), so \(a=B=\log2>0\) | PROVED |
| Net rate \(\delta=2a-g\) | \(\delta=0\); the positive-gap gate is not met | FAILED carrier |
| Fixed exponent below \(\delta/B\) | No positive exponent is certified; (3) directly excludes one on this sequence | FAILED carrier |

The field degree, discriminant and prime heights are not silently assigned
favorable bounded values. Degree is stated exactly, prime sizes enter the
displayed radius, and discriminant/regulator estimates are unnecessary because
the proof counts exact coefficient fibers without using lattice density.

## Evidence and disposition

The theorem is an analytic all-depth calculation, not an inference from finite
counts. This authoring/audit subtask executed no experiment and has no runtime,
seed, sampled range or experimental artifact to report. The parent's separate
finite checks, if recorded elsewhere in this research cycle, are supporting
regressions and are not a premise of (3).

For every fixed \(c>0\),
\[
\frac{|q(A_m,A_m)|}{|A_m|^{2-c}}
\ge\frac14|A_m|^c\longrightarrow\infty,
\qquad
\frac{|P_0(A_m,A_m)|}{|A_m|^{2-c}}=|A_m|^c\longrightarrow\infty.
\]
Thus even allowing a fixed multiplicative constant cannot give a power saving
for this carrier. The constant-factor homogeneous saving does not improve
the exponent; the linear term removes every remaining ordered-pair collision.

There is no remaining gap in these two carrier-specific counts. This result
does not exclude other subsets of these fields, correlated coefficient
carriers, other solvable extensions, or Eisenstein-multiplier constructions.
It does not resolve the fixed T03 target or the separate \(q+x\) benchmark,
and it makes no novelty claim.
