# T01 study notes: cubic difference plus sum

[Study index](README.md) · [Shared foundations](00-shared-foundations.md) ·
[Source identities](SOURCES.md)

**Version: 2026-09-14; research cutoff: 2026-09-10.**
The fixed target is **OPEN**:

$$P_+(x,y)=(x-y)^3+x+y,\qquad
\exists c>0\ \forall N_0\ \exists A\subset\mathbb R\text{ finite}:
|A|\ge N_0,\quad |P_+(A,A)|\le|A|^{2-c}.$$

The progress below is source-reported unless explicitly marked as an inspected
argument. No new proof audit or experiment was performed. Source **S-T01**,
§§1–2, fixes this identity; **S-T01-FINAL** concerns a separate quadratic branch.

## SN-T01-1 — The successful model and the cubic difficulty

**PROVED, reported.** The rank-one benchmark
$F_2=(x-y)^2+x+y$ has a same-set power-saving construction. In the supplied
tower, scaling algebraic-integer inputs by a fixed denominator $M$ makes the
cleared output

$$M^2F_2(\alpha/M,\beta/M)
=(\alpha-\beta)^2+M(\alpha+\beta).$$

Modulo each selected split prime dividing $M$, this is a square. Repetition
over the field embeddings supplies many residue restrictions, while uniform
packing counts every allowed output. Source: **S-T01**, §4.1 and (T01.3);
the quadratic checkpoint locator is given there.

**FAILED, specified cubic certificate.** For the cubic, clearing denominators
gives

$$Z_N(U,V)=(U-V)^3+N^2(U+V),\qquad
N^3P_+(U/N,V/N)=Z_N(U,V).$$

Cube residues can be sparse, but the denominator and cubic output width cost
more. For the source's one-prime certificate, $q\equiv1\pmod{12}$,
$q\ge13$, the normalized bound has infimum
$R\delta_{q,2}(2q+1)>8R$, where $R$ is the root discriminant and
$\delta_{q,2}=(q^2-q+3)/(3q^2)$. A base greater than one cannot prove an
exponent saving. This is a failed upper-bound method, not a lower bound on all
sparse cubic images. Source: **S-T01**, §6.1.

**Interpretation.** The source tower survives the adaptation; the favorable
counting balance does not. “More split coordinates” amplifies the loss too.

## SN-T01-2 — Why the literal sum-product transfer stalled

**FAILED, reported parameter-count method.** Substitute two independent
elements $gp,hq$ of a Phase-A carrier into the cubic:

$$P_+(gp,hq)=p^3g^3-3p^2qg^2h+3pq^2gh^2-q^3h^3+pg+qh.$$

For products alone, $gh$ is a useful compressed label. Here the joint labels
$(g^2h,gh^2)$ recover $(g,h)$ over the totally real field. Restricting to one
common scale controls only a $1/|G|$ fraction of pairs. Counting these mixed
labels therefore supplies no full-square saving; it does not prove that every
possible scalar sum of the terms is distinct. Source: **S-T01**, §6.8.

The unit-distance translation route has another clear limitation. For a fixed
difference $d$,

$$P_+(a,a-d)=d^3+2a-d$$

is injective in the anchor $a$. Many selected edges of difference $d$ give
many outputs along that slice. Cross-slice collisions would need a separate
theorem. Source: **S-T01**, §§4.5, 6.7.

## SN-T01-3 — What the negative results actually establish

**PROVED, reported scoped obstructions.** The cubic work replaced several
unsupported hopes with precise boundaries:

| Attempt | Recorded result | Scope retained |
|---|---|---|
| Positive-volume blocks | For bounded Borel $W\subset\mathbb R^m$ of volume $V>0$, the continuous cubic image needs more than $(\sqrt3/\pi)^mV^2$ unit cubes | Rules out the stated volume/covolume plus continuous-cover certificate; does not count arbitrary sparse lattice images |
| Regular digital sets | For fixed base, finite strongly connected right-resolving input graph, fixed start, all states terminal, and growth $\mu>1$, $|Z_{b^n}(D_n,D_n)|\ge c_G|D_n|^2$ eventually | Excludes the proposed all-output automaton with $\lambda^3<\mu^2$ |
| Fixed-prime positive-entropy digits | Fix finite nonempty prime support $S$ and $\alpha>0$. For large $S$-smooth $N$ and $D\subset[0,N)\cap\mathbb Z$, $|D|\ge N^\alpha$ implies $|Z_N(D,D)|\ge\eta(S,\alpha)|D|^2$ | Includes nonregular rules under these hypotheses; does not cover growing prime support or zero entropy |
| One quadratic rich-fiber family | The precisely defined $A_j=\sigma_1(T_j/(2\sqrt{\zeta_j}))$ of §4.4 has exactly $|A_j|^2$ cubic outputs | An actual image theorem for that family, unlike the failed box certificates |

Sources: **S-T01**, §§4.2–4.4, 6; **S-REG**, MC-01 and T01 failure entries.
For the last row, retain the source's largest-fiber construction, translated
box, $\rho_2R\le1/100$, $M\ge64$, and
$X=2\lfloor M/8\rfloor\ge4\sqrt R$; it is not a theorem about arbitrary
quadratic fibers.

**HISTORICAL / SUPERSEDED.** The old SPEC still describes regular digital
witness existence as open. The later obstruction controls the route's status;
the SPEC remains preserved. No narrower supported positive cubic candidate
survives in the frozen record. Sources: **S-T01**, §§13–15; **S-REG**, MC-01.

## SN-T01-4 — Separate norm–trace progress, with its missing witness

**PROVED, argument inspected; CONDITIONAL application.** The 10 September
checkpoint separately studied $P_0=x^2+xy+y^2+x$. Completing its norm gives

$$P_0(x,y)=q(x+2/3,y-1/3)-1/3,\qquad q=x^2+xy+y^2.$$

The shifts differ, so a homogeneous same-set witness does not automatically
work. The checkpoint proves a precise repair. Suppose growing real $C$,
$N=|C|$, satisfy both

$$|q(C,C)|\le K_*N^{2-c_0},\quad |C-C|\le D_*N^{1+\eta},
\quad0<c_0\le1,\quad0\le\eta<c_0/2,$$

with fixed constants. Choose a richest nonzero difference $\delta$, put
$B=C\cap(C-\delta)$ and $A=B/\delta+1/3$. Then

$$|A|\ge\frac{N^{1-\eta}}{2D_*},\qquad
P_0(A,A)\subseteq\delta^{-2}q(C,C)-1/3.$$

The resulting exponent before constant absorption is

$$c_1=\frac{c_0-2\eta}{1-\eta}>0.$$

The $2\eta$ in the numerator pays the thinning in both coordinates. This is
a proved transfer implication with **no supplied witness satisfying both
premises**. It has no established cubic consequence. Source:
**S-T01-FINAL**, §§2.1–2.3; **S-T01**, §12.

**PROVED bound, argument inspected / FAILED power-saving certificate.** The
tested shifted Phase-A family $A_j=\sigma_1(G_j\mathcal P_j)-1/6$ has an
all-pair reflection bound $(N_j^2+N_j)/2$. Its full box estimate has output
rate $g>2h$, where $h$ is the proved input lower rate. Reflection saves a
constant factor, not a fixed power. The actual family is not disproved.
Source: **S-T01-FINAL**, §5, especially (5.4)–(5.6).

**OPEN.** More general solvable extensions supply no demonstrated additional
output gain. The checkpoint completed its bounded study and adopted no new
amplification conjecture. Its arithmetic literature survey predates the freeze;
these notes do not repeat it. Source: **S-T01-FINAL**, §§4, 8.

## Recall check

1. Why does a quadratic theorem not survive replacing the square by a cube?
   **The full output width and denominator costs change; the residue saving
   must be compared with them again.**
2. Which negative result above determines an actual image exactly? **The
   specified rich-fiber family. A failed enclosing bound alone does not.**
3. What is missing from the separate quadratic transfer? **A growing $C$ with
   both small $q(C,C)$ and sufficiently small $C-C$. The implication is proved;
   its application remains conditional.**
