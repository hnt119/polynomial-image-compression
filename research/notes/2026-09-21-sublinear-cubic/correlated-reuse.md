# Correlation, coordinate reuse, and growing denominators

T01 / sublinear cubic symmetry cycle, 2026-09-21 v1.
Throughout, \(P(x,y)=(x-y)^3+x+y\). All claims below are elementary
proofs developed in this cycle, with no external theorem or novelty claim.

## SC-R1 — The exact correlated domain and the reuse cost

**Meaning.** Difference and sum are correlated coordinates. Selecting them
independently invents pairs that need not belong to the scalar square.

**Statement — PROVED.** For a finite real set \(A\), define

\[
\Omega_A=\{(u,L):(L+u)/2\in A, (L-u)/2\in A\}.
\]

The map \(A^2\to\Omega_A\), \((x,y)\mapsto(x-y,x+y)\), is a
bijection, and the full output is exactly

\[
P(A,A)=\{u^3+L:(u,L)\in\Omega_A\}.
\tag{1}
\]

For an arbitrary finite set \(F\subset\mathbb R^2\) of distinct labels
\((z,u)\), put

\[
c_+(z,u)=(z-u^3+u)/2,\quad c_-(z,u)=(z-u^3-u)/2,
\quad A_F=c_+(F)\cup c_-(F),\quad N=|A_F|,\quad Q=|F|.
\]

These labels prescribe exactly \(Q\) distinct ordered pairs of \(A_F^2\).
Writing \(m(a)\) for the number of coordinate occurrences equal to \(a\),
including both positions even when they agree, gives

\[
\sum_{a\in A_F}m(a)=2Q,\qquad \frac1N\sum_a m(a)=\frac{2Q}{N}.
\tag{2}
\]

In particular, a prescribed-pair certificate covering
\(Q\ge N^2-B\) requires average scalar reuse at least \(2N-2B/N\).
If every output section of \(F\) is partitioned into actual paths or
connected sets of size at least \(K\) under a common inventory, then

\[
|P(A_F,A_F)|\le Q/K+(N^2-Q).
\tag{3}
\]

The \(N^2-Q\) unprescribed pairs each cost one possible output. If sections
have small components too, their total vertex mass must also be charged.

**Proof.** Both coordinate transformations have the displayed inverse.
The map from \((z,u)\) to its ordered scalar pair is injective, since that
pair recovers its difference and output. Counting the two scalar slots
proves (2). Each prescribed connected set gives one output, while the
unprescribed complement has at most its cardinality many outputs. This
proves (3) without any assertion about incidental collisions.

**Why it matters.** Long planted fibers are useful only if scalar reuse
is linear in \(N\) on average. A large number of formal parameter labels
does not supply this reuse; duplicates must first be removed from \(F\)
and from the scalar set separately.

**Scope.** This is an exact accounting reduction and sufficient certificate,
not an existence theorem. In particular, \(u\in A-A\) and \(L\in A+A\)
do not imply \((u,L)\in\Omega_A\). For \(A=\{0,1\}\), the separate
choices \(u=1,L=0\) pass those two tests but give scalars \(1/2,-1/2\).

## SC-R2 — Affine matching between different fiber templates is sparse

**Meaning.** Copying one difference template to several output fibers does
not make the scalar coordinates agree at many corresponding positions.

**Statement — PROVED.** Let \(s,t\in\{+1,-1\}\) and
\(c_s(z,u)=(z-u^3+su)/2\). Fix \(z,w,\alpha,\beta\in\mathbb R\).
The identity

\[
c_s(z,u)=c_t(w,\alpha u+\beta)
\tag{4}
\]

holds for at most three distinct real \(u\), unless

\[
\alpha=1,\quad\beta=0,\quad s=t,\quad z=w,
\]

in which case it holds identically. If \(\alpha=1,\beta\ne0\), there
are at most two solutions. If \(\alpha=1,\beta=0,s\ne t\), there is
exactly one solution.

**Proof.** Multiplying (4) by two and moving terms produces

\[
(\alpha u+\beta)^3-u^3+su-t(\alpha u+\beta)+z-w=0.
\]

It is a polynomial of degree at most three. For it to vanish identically,
its leading coefficient gives \(\alpha^3=1\), hence \(\alpha=1\) over
the reals. The quadratic coefficient then gives \(3\beta=0\), the linear
coefficient gives \(s=t\), and the constant gives \(z=w\). For a nonzero
translation, the quadratic coefficient is \(3\beta\ne0\); for zero
translation and opposite signs, the linear coefficient is nonzero.

**Why it matters.** An affine relabeling cannot provide repeated whole
coordinate blocks shared by distinct fibers. Reuse, if it succeeds, must
come from nonmatching indices, nonlinear relabelings, or varying correlated
subsets, whose multiplicities remain to be counted.

**Scope.** This does not bound all intersections between two scalar images:
the other parameter may be chosen nonlinearly. It is a statement about
specified affine matching, not a universal obstruction to coordinate reuse.

## SC-R3 — Two fibers can share at most one translated second-coordinate edge

**Meaning.** Even when one scalar coordinate is reused freely, matching both
ends of a fixed-step edge imposes an additional cubic restriction.

**Statement — PROVED.** Fix distinct outputs \(z\ne w\) and a nonzero
step \(\tau\). There is at most one ordered pair \((u,v)\in\mathbb R^2\)
such that

\[
y_z(u)=y_w(v),\qquad y_z(u+\tau)=y_w(v+\tau).
\tag{5}
\]

In fact there is exactly one such real pair, before imposing membership
in any scalar carrier. It satisfies \(v=-u-\tau\).

**Proof.** Write \(g(u)=u^3+u\). Subtracting the two equations gives

\[
g(u+\tau)-g(u)=g(v+\tau)-g(v).
\]

The difference factors as \(3\tau(u-v)(u+v+\tau)=0\).
The option \(u=v\) would force \(z=w\), so \(v=-u-\tau\).
The first equation then becomes

\[
w-z=-g(u+\tau)-g(u).
\]

Its right side is a strictly decreasing bijection of the real line, since
its derivative is \(-3(u+\tau)^2-3u^2-2<0\). This proves uniqueness
and existence.

**Why it matters.** Coordinate reuse at one vertex does not automatically
propagate to a reusable common-step path. This is an exact extra constraint
using both second-coordinate memberships of the edge.

**Scope.** Shared edges may occur at different indices in many fibers.
The assertion alone does not improve the universal \(N^{1/6}\) inventory
threshold. No incidence bound with a stronger exponent is inferred from it.

## SC-D1 — A growing prime denominator can force almost all pairs to be unique

**Meaning.** Very fine rational meshes can escape the earlier real-width
obstruction, but congruences at their changing denominator can still prevent
cubic collisions. The argument applies to arbitrary nonuniform subsets.

**Statement — PROVED.** Let \(p\ge5\) be a prime with \(p\equiv2\pmod3\),
let \(B\subset\mathbb Z\) be finite with \(N=|B|\), diameter
\(W=\max B-\min B\), and assume \(2W<p^2\). For any real \(a\), put
\(A=a+B/p\). Let \(n_r=|\{b\in B:b\equiv r\pmod p\}|\) and
\(H=\sum_{r\bmod p}n_r^2\). Every pair in a nonsingleton actual
\(P\)-fiber has its two indices congruent modulo \(p\). Consequently,
for every step inventory and every integer \(K\ge2\),

\[
\#\{\text{vertices in components of size at least }K\}\le H,
\qquad |P(A,A)|\ge N^2-H.
\tag{6}
\]

If \(max_r n_r\le R\), then \(H\le NR\). Thus \(R=O(N^{1-\kappa})\)
with fixed \(\kappa>0\) gives at most \(O(N^{2-\kappa})\) nonsingleton
vertices and an actual image \(N^2-O(N^{2-\kappa})\). If all residues
are distinct, the polynomial is completely injective on \(A^2\).

**Proof.** Translation adds the constant \(2a\) to every output and changes
no equality. If \((i,j)\) and \((k,l)\in B^2\) have equal outputs, put
\(d=i-j,e=k-l\). Clearing denominators gives

\[
d^3+p^2(i+j)=e^3+p^2(k+l),\qquad d^3\equiv e^3\pmod{p^2}.
\tag{7}
\]

Cubing is injective modulo \(p\): a nontrivial cube root of one in the
nonzero residue group would have order three, which is impossible because
\(3\nmid(p-1)\). Thus \(d\equiv e\pmod p\). If \(p\nmid d\), the factor
\(d^2+de+e^2\equiv3d^2\pmod p\) is nonzero. Factoring \(d^3-e^3\)
therefore gives \(p^2\mid(d-e)\). Since \(|d-e|\le2W<p^2\), we have
\(d=e\). Equation (7) then gives equal sums as well, so \(i=k,j=l\).
Every distinct collision must therefore have \(p\mid d\) and \(p\mid e\).
Exactly \(H\) ordered pairs have this property. All other pairs are singleton
fibers, which proves (6), including all inventories. The inequality
\(H\le N\max n_r\) is immediate. If all residues are distinct, the only
eligible pairs are diagonal. Their outputs \(2a+2i/p\) are distinct and
cannot meet a nondiagonal output by the same congruence argument.

**Why it matters.** This supplies a new necessary arithmetic concentration
condition on fine-mesh candidates. For almost-full component coverage in
this class one needs \(H=N^2-o(N^2)\), hence a residue class containing
\(N-o(N)\) inputs, because \(\max n_r\ge H/N\). Adding many steps cannot
rescue a residue-dispersed carrier.

**Scope.** The prime changes with the set; this is not a restart of fixed
rational additive completion or a fixed-prime digital search. It proves
neither a theorem for all rational denominators nor one for arbitrary real
sets. When \(2W\ge p^2\), the argument no longer forces \(d=e\).
When a residue class dominates, the quantitative exceptional bound may be
vacuous. No distribution theorem for primes is needed: the statement is
conditional on any prime satisfying its explicit elementary hypotheses.

### A nonuniform, tiny-gap family inside the theorem

**PROVED consequence.** For each prime \(p\ge5\), \(p\equiv2\pmod3\),
take

\[
B_p=\{j+p\lfloor j/3\rfloor:0\le j<p\},\qquad A_p=B_p/p.
\]

Here \(N=p\), all residues are distinct, and
\(W=(p-1)+p\lfloor(p-1)/3\rfloor<p^2/2\). Therefore
\(|P(A_p,A_p)|=p^2\) exactly, with no nontrivial components for any inventory.
The scalar gaps take the values \(1/p\) and \(1+1/p\), in a repeating small, small, large pattern up to end
truncation, and \(D=W/p=\Theta(p)\). The previous common-lattice hypothesis
\(D=o(h^3N^2)\), for \(h=1/p\), fails by a factor \(Theta(p^2)\).
This is a scoped negative family, not a proposed positive construction.

There are arbitrarily large such primes by the elementary Euclid argument:
if their finite product were \(Q\) \(including 2\), the integer \(3Q-1\)
has a prime factor \(2\pmod3\) absent from \(Q\), a contradiction.
No prime density or external result is used.

## SC-D2 — Exact descent to residue-class squares

**Meaning.** All collisions in the fine mesh are confined to separate
integer-mesh subcarriers. Their output sets do not overlap, so every
residue class can be charged at once without losing its square of inputs.

**Statement — PROVED.** Retain SC-D1's hypotheses, and put

\[
A_r=\{a+b/p:b\in B,\ b\equiv r\pmod p\},\quad D=W/p,
\quad F(D)=1+2\left\lfloor D^{1/3}+\sqrt{2D/3}\right\rfloor.
\]

The sets \(P(A_r,A_r)\) for occupied residues are pairwise disjoint.
They are also disjoint from the outputs of every off-residue pair, all of
which are singleton fibers. Thus

\[
|P(A,A)|=N^2-\sum_r n_r^2+\sum_r|P(A_r,A_r)|.
\tag{8}
\]

If \(V\) is the total mass of nonsingleton actual fibers, then

\[
V\le\sum_r n_r\min\{n_r,F(D)\}\le NF(D),
\qquad |P(A,A)|\ge N^2-NF(D).
\tag{9}
\]

For every inventory and every integer \(K\ge2\), the mass in components
of size at least \(K\) is at most \(NF(D)\). In particular,
\(W/p=o(N^2)\) forces an actual image \(N^2-o(N^2)\) and leaves
\(N^2-o(N^2)\) singleton graph vertices for *every* inventory.
The sufficient special regime \(p=o(N^2)\) follows from \(2W<p^2\).
If \(W/p=O(N^{2-\gamma})\), \(0<\gamma\le2\), the nonsingleton
mass is \(O(N^{2-\gamma/2}+N)\).

**Proof.** SC-D1 proves that a nontrivial collision has
\(i\equiv j\equiv r\pmod p\) and
\(k\equiv l\equiv s\pmod p\). Write \(d=pd_1,e=pe_1\)
in (7) and divide by \(p^2\). This gives

\[
p(d_1^3-e_1^3)+(i+j)-(k+l)=0.
\]

Reduction modulo \(p\) yields \(2r=2s\), so \(r=s\).
The same reduction handles equality of any two outputs from different
residue squares; hence those images are disjoint. Off-residue pairs
are globally singleton by SC-D1. This proves the exact decomposition (8).
Each actual subcarrier \(A_r\subset a+r/p+\mathbb Z\) has diameter
at most \(D\). The frozen GS-U3 theorem bounds its nonsingleton fiber
mass by \(n_r\min\{n_r,F(D)\}\). No other class can join any of these
fibers, so the bounds add exactly, proving (9). Any nontrivial graph
component lies in a nonsingleton actual fiber. Finally,
\(F(D)=O(1+D^{1/2})\), which proves the stated rates.

**Why it matters.** This closes an entire changing-prime, nonuniform
fine-mesh regime, including carriers with highly concentrated residues.
The old common-lattice test on the *whole* carrier would involve
\(W p^2/N^2\); the new sufficient test involves \(W/(pN^2)\), subject
to the explicit congruence and width hypotheses. The factor \(p^3\)
difference comes from proved fiber confinement, not a free rescaling.

**Scope.** This is a combination of a new arithmetic fiber decomposition
and frozen GS-U3 on its exact scalar subcarriers. It is not a new proof of
GS-U3 or a fixed rational completion search. When \(2W\ge p^2\),
off-residue collisions are no longer ruled out by this argument. When
\(W/p\) is not \(o(N^2)\), (9) may be vacuous. Neither limitation is
positive evidence for a construction. Arbitrary denominators and arbitrary
real carriers remain outside this theorem.

## Claim metadata

All IDs SC-R1/R2/R3/D1/D2 have track T01, the plus-sign cubic, date/version
2026-09-21 v1, universal quantifiers and hypotheses stated in their sections.
Evidence type: full symbolic proof above. Dependencies: only the frozen
inverse fiber identity; SC-D1 additionally uses elementary integer
divisibility and the finite-group order argument explicitly given above.
SC-D2 additionally uses frozen GS-U3 on every displayed same-set residue
subcarrier; the exact partition charges all subcarrier squares and cross-pairs.
Audit and computation records are in `verification.md`. No missing
historical digital checkpoint is a proof dependency. The construction
witness for sublinear-inventory almost-full coverage remains **OPEN**.
