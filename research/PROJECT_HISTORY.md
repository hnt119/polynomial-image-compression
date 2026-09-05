# Project history: four research tracks

Logged on **5 September 2026**, from the recent parts of the four research tasks
identified by the project owner. Dates below identify discussion or checkpoint
dates; they are not claims about first discovery or publication priority.

The common target is a fixed polynomial $P$, a fixed $c_P>0$, and arbitrarily
large finite real sets $A$ satisfying $|P(A,A)|\le|A|^{2-c_P}$. Each track keeps
its own polynomial and construction. Historical proof claims are attributed to
their checkpoints; this history import is not a new independent proof audit.

## The four directions

| ID | Source task, with its original title | Recent direction | Current recorded outcome |
| --- | --- | --- | --- |
| T01 | cubic polynomial 研究综合与汇报 | $(x-y)^3+x+y$: exact digital carries after the positive-volume block obstruction | Target open; digital automaton criterion proposed |
| T02 | Create Phase C0 proof prompt | $(x+2y)^4+3x-y$: a unit-times-additive carrier after C0/C1 | Target open; C2 structural-lemma prompt prepared |
| T03 | Polynomial 2 · Research Experiment 分支 · Email Progress Update | $x^2+xy+y^2$: global reassignment of a parity-twisted norm code | PTCR open; exact Cartesianization and several composition methods obstructed |
| T04 | Polynomial 1 · Research Experiment 分支 · Email Progress Update | $(x-y)^3-3(x+y)$: direct overlapping slices after testing quadratic witness transfer | Target open; both specified $T=Q/8$ transfer regimes closed in the source record |

Each direction has a [specification and status record](tracks/README.md).
“Unit Distance and Sum-Product” is shared background, not a fifth track in this log.

## Recent chronology

| Date | Track | Checkpoint or decision | Consequence |
| --- | --- | --- | --- |
| 2026-09-02 | T02 | Original C0 report reviewed: transverse rank-one quadratics $L^2+M$ have a reported fixed power saving | Preserve the family result; correct radius wording and the scope of the quartic conclusion |
| 2026-09-02 | T01 | Cubic difference-plus-sum checkpoint reduces a proposed construction to a finite covering block | This was a conditional implication, requiring a favorable block inequality |
| 2026-09-03 | T01 | Subsequent block checkpoint rules out that positive-volume certificate | Keep the implication as history, but close its proposed block hypothesis for the specified tower |
| 2026-09-03 | T01 | Recent continuation proposes regular digital inputs and an exact output automaton | A fixed carry invariant and a spectral gap remain to be constructed |
| 2026-09-03 | T02 | C1 reviewed; weak M1 deficit and the $p=5,d=2$ test receive elementary corrections | Neither correction proves the quartic target |
| 2026-09-03 | T02 | C2 prompt prepared around $C_j=G_jT_j$ | Require a new bound on realized support that pays unit, ratio, and multiplicity costs |
| 2026-09-03 | T03 | Original norm-preserving Cartesianization (CR) is rejected by a 3-adic density obstruction | Move to the parity-twisted code, preserving the $4^m$-to-$3^m$ profile |
| 2026-09-03 | T03 | Composition report supplies a six-point $m=2$ example and obstructions to exact or naive recursive placement | A finite gadget is available; a construction at arbitrarily large scales is not |
| 2026-09-03 | T03 | Recent continuation prioritizes global reassignment with deficit contraction | A block recursion must have coefficient strictly below $4^k$, with all construction and growth hypotheses verified |
| 2026-09-03 | T04 | Positive-polynomial checkpoint establishes inheritance from the quadratic seed, as a source result | The companion even-degree family does not solve the fixed cubic |
| 2026-09-03 | T04 | $q\equiv5\pmod{12}$ quadratic witness is reported exactly injective for the cubic | That particular transfer cannot compress the cubic |
| 2026-09-03 | T04 | Complementary $q\equiv1\pmod{12}$ witness is reported asymptotically injective | Close the two analyzed narrow-window transfer regimes; study direct slice overlap |
| 2026-09-05 | All | Four tracks logged; 33 checkpoint/reference attachments recovered and preserved | The repository now retains the recent research state and supporting artifacts |

## What the recent directions require

- **T01 — digital carry control.** Find a fixed input graph with growth $\mu>1$
  and a fixed output automaton with growth bound $\lambda$, prove coverage of
  every output, and establish $\lambda^3<\mu^2$. The numerator after scaling is
  $(U-V)^3+b^{2n}(U+V)$; ignoring the scale-dependent term changes the problem.
- **T02 — realized quartic support.** Prove a quantitative support lemma for
  $C_j=G_jT_j$. Displaying seven correlated terms or putting the carrier into a
  larger box does not provide the required gain.
- **T03 — Cartesian deficit.** Place the parity-twisted norm code in one rational
  set $A_m$ with $d_m=|A_m|^2-4^m\le|A_m|^{2-\xi}$. Global reassignment is the
  latest constructive direction. The composition report also preserves an open
  triangle-gap lemma as an adversarial route to refuting PTCR.
- **T04 — cubic slice overlap.** Construct one set whose slices
  $H_3(u)-6(A\cap(A-u))$, where $H_3(u)=u^3-3u$, have a rigorously small total
  union. Large collisions on selected slices are insufficient.

## Boundaries that must survive future updates

The two cubic tracks have different linear terms and remain separate. Neither
is the mixed cubic $xy(x+y)$ in the initial experiment suite. T02's quartic is
also different from the inherited companion $R^2+R$ in T04.

An obstruction to a specified certificate is not a disproof of its ultimate
polynomial target. A disproved intermediate conjecture, such as original CR, is
recorded with its scope. A proposed continuation is not logged as an executed
research run.

The initial repository's finite tests cover its five implemented polynomials;
they do not automatically validate these recovered reports or the two new cubic
specifications. External novelty has not been reverified for this release.

See [the source recovery record](HISTORY_SOURCES.md) for inspected sections,
remaining missing inputs, and links to the preserved files.
