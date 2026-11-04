# Power savings for quadratic images

Professor brief · Research evidence through 5 November 2026

## One theorem and one open problem

A set of $n$ real numbers gives $n^2$ ordered pairs. How few distinct numbers can a fixed polynomial produce from those pairs? A **power saving** means a bound of $n^{2-c}$ for a fixed $c>0$, on sets of unbounded size. The same set must fill both input positions. Saving a constant fraction of the square does not meet this target.

**Proved for C0.** Fix any four integers $a,b,c,e$. There are arbitrarily large finite real sets $A$ and an exponent $\epsilon_P>0$, depending only on the fixed polynomial, for which
$$
P(x,y)=(ax+by)^2+cx+ey,\qquad |P(A,A)|\le |A|^{2-\epsilon_P}.
$$

The theorem includes zero coefficients and nonprimitive pairs. When the squared form is nonzero, its quadratic part has rank one: all quadratic variation comes from a single linear expression. The extra condition $ab(ae-bc)\ne0$ identifies a nonspecial subfamily; it is not a compression hypothesis.

**Why the proof works.** Replace the linear term temporarily by a fixed multiple. At many selected primes the multiple disappears, leaving a square. Roughly half of the local residues are excluded at each split coordinate. A lattice bound caps the population of every permitted class. A single common scaling then returns to the original polynomial and preserves every cardinality. The output estimate covers even the least frequent outputs.

**Open benchmark.** The quadratic part of the following form has determinant $3/4$ and rank two:
$$
Q(x,y)=x^2+xy+y^2.
$$

It has a different useful identity. If $\omega$ is a primitive cube root of unity, then $Q(x,y)=(x-\omega y)(x-\omega^2y)$. Multiplication by an element of relative norm one preserves this value. To use that symmetry for compression, the resulting pair must still have both coordinates in $A$.

Sources: [C0 v5, Theorem 1 and its proof](../../proofs/c0-v5/theorem-and-proof.tex); [T03, fixed benchmark and scope](../../tracks/03-eisenstein-cartesianization/STATUS.md)

<!-- page -->

## When many symmetries are too few

**A rich orbit can miss the square.** One construction has an orbit of $3^d$ points with at least $2^d$ norm-preserving returns at every point. Projecting to the coordinates produces $n=2\cdot3^d$ distinct scalars. But its engineered pairs occupy just $3^d$ of the $n^2$ positions. Pairing a coordinate from one point with a coordinate from another creates inputs for which the original return count says nothing.

**What the retirements establish.** Two later multiscale packings reuse coordinates by exact trigonometric identities. Even after allowing all equal-value targets, their images remain of quadratic size. A separate balanced-factor construction also has a fixed $M$ such that, at every sufficiently large depth,
$$
\frac{n^2}{18M}\le |Q(A,A)|\le n^2.
$$

This last statement counts complete fibers, meaning all pairs with the same output. It rules out every positive saving exponent on that specific family. The earlier observation that certain rotations failed would not have established this lower bound.

**A different carrier.** Start instead with all algebraic integers in a field whose conjugates fit one fixed window: intervals at real places, disks at complex places. Use one real embedding to read the integers as a finite set $A$. For a growing sequence of degrees, its size grows exponentially. There is no discarded coordinate or privileged list of source pairs.

At tower level $j$, write $d_j$ for the degree of the initial totally real field. An arithmetic covering argument (MS-O1) gives at least $2^{d_j}$ distinct integral norm-one actions in one fixed logarithmic cutoff. Every possible nonzero order-unit return is included. What is not known is how many of these actions return a given pair to the window: a multiplier that expands one complex direction may send a coordinate outside its disk. Its phases at different places belong to one global algebraic number.

Sources: [Exponent construction, UE-P2–P3](../../notes/2026-09-16-unit-exponent/primary-proof.md); [Multiscale full fibers, XB-F1–F2](../../notes/2026-10-06-cross-block-returns/README.md); [Balanced retirement, BFF-O1 §§1–4](../../notes/2026-10-11-bff-o1/README.md); [Order-unit population, MSU-A1–A3](../../notes/2026-10-21-relative-unit-population/arithmetic.md)

<!-- page -->

## The count that would settle this route

For a nonzero source pair $p=(x,y)$ write $z=x-\omega y$. Its label consists of two arithmetic objects: the actual principal ideal $z\mathcal{R}_j$ in the chosen order, and the exact relative norm $z\tau(z)=Q(x,y)$. Here $\tau$ fixes the coefficient field and interchanges $\omega$ and $\omega^2$. Two sources have the same label precisely when one is obtained from the other by an order unit of relative norm one.

![How source pairs give occupied labels and then quadratic outputs](figures/orbit-labels.png)

Let $n_j=|A_j|$, let $N_j=n_j^2-1$, and choose $p$ uniformly from the nonzero pairs. Write $r_j(p)$ for its number of distinct returning targets, and $\nu_j$ for the number of occupied labels. In a class of size $m$, each of the $m$ sources contributes $1/m$. Each class counts once:
$$
N_j\,\mathbb{E}[1/r_j]=\nu_j,\qquad |Q(A_j,A_j)|\le 1+\nu_j .
$$

The extra output is zero. Different occupied labels may have the same norm, so replacing the inequality by an equality would lose the distinction between an orbit and a complete output fiber.

**Open estimate (MS-O2-I).** Find constants $\gamma>0$ and $C_1<\infty$ such that, at every sufficiently large tower level,
$$
\nu_j\le C_1 N_j e^{-\gamma d_j}.
$$

**Conditional consequence.** The input bound is $\log n_j\le B_*d_j$ for a fixed $B_*>0$. Substitution would give an eventual same-set saving for every fixed $0<c<\gamma/B_*$. The strict inequality absorbs the constant and the zero output. No positive $\gamma$ is currently proved. A negative answer about these labels alone would still leave open savings from collisions between different labels.

Sources: [Orbit partition and labels, MSR-I1–I3](../../notes/2026-10-21-typical-unit-returns/incidences.md); [Open estimate and conditional exponent, §§5–6](../../notes/2026-10-21-typical-unit-returns/README.md)
