# T03 — Eisenstein norms, Cartesian completion, and adaptive radicals

Prepared 2026-09-14 from the record frozen through 2026-09-10. Target:

\[
Q(x,y)=x^2+xy+y^2.
\]

**OPEN.** The latest frontier is an unproved support bound on the actual
adaptive radical sequence. All computations discussed here are inherited;
none were rerun or expanded for these notes.

## What the two papers contributed

Writing $Q(a,b)=N(a-\omega b)$, where $\omega^2+\omega+1=0$, connects the
target to multiplicative algebra. The unit-distance construction suggests
organizing many representations of a norm. The sum-product construction
suggests combining multiplicative structure with controlled additive sets.
T03 exposes the difficulty of turning these ideas into a Cartesian square:
many engineered pairs with few norms need not cover all pairs of their
coordinate set. Sources: **S-T03**, §§2–7, and [shared foundations](00-shared-foundations.md).

## SN-T03-1 — why a norm identity is only the beginning

**PROVED, reported identities and scoped obstructions; OPEN target.** Sources:
**S-T03**, §§3–7; **S-REG**. Track T03, fixed $Q$ above.

The quadratic form has rank two (matrix determinant $3/4$). It is not the
rank-one square covered by corrected C0. A norm-one Eisenstein multiplier
$r+s\omega$ acts on coordinates by

\[
(a,b)\longmapsto(ra+sb,\;-sa+(r-s)b).
\]

This preserves $Q$ but generally introduces denominators or moves coordinates
outside the proposed input set. The recorded common-box/stable-core strategy
does not recover enough inputs after those costs. This is a failure of that
strategy, not a universal obstruction to norm-one actions.

Likewise, rank-two local norm behavior does not automatically inherit the
rank-one residue saving. The record distinguishes weighted tensorized
inequalities from the ordinary unweighted support bound required here. A
weight is useful only with a charged comparison to an actual same-set input.

## SN-T03-2 — engineered norm pairs versus all coordinate pairs

**PROVED, reported counts and obstructions; EXPERIMENTAL/finite exact examples
as explicitly identified.** Source: **S-T03**, the CR/PTCR and Cartesianization
sections. No archived program or serialized object was executed.

A balanced Eisenstein word construction uses four letters at each of $m$
positions, schematically $\{1,r_i,\pi_i,\bar\pi_i\}$. It supplies $4^m$
engineered pairs and at most $3^m$ engineered norms. If $A$ is the union of
their coordinates and $n=|A|$, a direct bound for the completed Cartesian
image is only

\[
|Q(A,A)|\le3^m+(n^2-4^m).
\]

The second term counts pairs not covered by the engineered construction.
It must itself have a power saving. The recorded untwisted family instead
satisfies $n^2-4^m\ge n^2/3+2^m$.

A parity twist by $1-\omega$, whose norm is three, preserves the useful word
and norm counts. Exact Cartesian closure still fails for the specified PTCR
family when $m\ge2$. An approximate closure question survives historically,
but it is not a proved substitute for the current adaptive-sequence obligation.

The recorded six-point example
$A=\{-25,-10,-5,-2,-1,26\}$ is instructive: 16 engineered ordered pairs have
nine values, whereas the full 36-pair image has 19 values. These are reported
finite exact counts. Repeating this pattern leaves engineered-pair density
$(4/9)^j$ after $j$ repetitions, so its attractive small example does not
establish an asymptotic construction.

## SN-T03-3 — the actual adaptive radical sequence

**PROVED, reported algebraic identities and finite certificates; OPEN uniform
recurrence.** Sources: **S-T03**, §§3–4, 13–15; **S-T03-ZIP**, especially
`TCRC_History_Parameters.md` and `TCRC_Root_Algebra_Pair_Maps.md`.

For finite $A\subset\mathbb R$, put $M=\max|A|$ and choose $C>M$. Define

\[
L_C(A)=\left\{\pm\sqrt{\frac{C+a}{C-M}}:a\in A\right\}.
\]

The positive radicands are distinct, so this doubles the input size exactly.
The recorded sequence starts with $A_0=\{-1,1\}$ and, at each level, chooses
the parameter minimizing the next image among the specified collision-legal
parameters together with $M+1$, with the prescribed least-parameter tie break.
Statements about a different choice at one level describe a different
descendant. They do not automatically establish a recurrence for this sequence.

After removing the common factor $C-M$, the full signed image is

\[
T_C(A)=\{2C+a+b\pm\sqrt{(C+a)(C+b)}:a,b\in A\},
\quad Q(L_C(A),L_C(A))=(C-M)^{-1}T_C(A).
\]

To count it, work over $K=\mathbb Q(A,C)$ and group $C+a$ by their square
classes in $K^*/K^{*2}$. Let their sizes be $c_j$, and let
$W=|T_C(A)\cap K|$. The recorded exact decomposition is

\[
|T_C(A)|=n^2-\sum_jc_j^2+W.
\]

Pairs in different square classes contribute the outside-field part. Within
a class, write $C+a=\gamma_j u_a^2$ with $u_a\in K$ and include both signs
in $U_j$. The remaining support is a union of $\gamma_jQ(U_j,U_j)$.
Thus a dominant square class is useful, but its own signed-root image still
needs a support bound.

The inherited exact levels are:

| Level $m$ | $|A_m|$ | $|Q(A_m,A_m)|$ | Chosen next $C$ |
|---|---:|---:|---:|
| 0 | 2 | 2 | $5/3$ |
| 1 | 4 | 5 | $5/2$ |
| 2 | 8 | 17 | $4$ |
| 3 | 16 | 68 | $3$ |
| 4 | 32 | 269 | Not established in the retained record |

For the level-three choice $C=3$, square-class sizes are $4,2,2$ and eight
singletons. Their squared sizes sum to 32. Therefore 224 values lie outside
the base field; the inside-field support has size 45; the total is 269.
This is an explanation of the recorded certificate, not an extrapolation.
The recorded field degree 16,384 at level four is not a compression exponent:
here the growing input parameter is the iteration depth $m$.

## SN-T03-4 — what the finite cover investigations established

**PROVED, reported finite certificates; OPEN uniform extension.** Source:
**S-T03-ZIP**, all five identified TCRC reports. Their statements were read;
their supporting programs and raw objects were not rerun or loaded.

One tempting approach is to cover the signed-root image by a few affine copies
of the previous image. The retained small cases show why the number and shape of
the copies matter. At level one, $C=17/8$ produces root-image size 12 against
old image size five, but requires four affine copies in the reported cover.
At level three, $C=3$ has root-image size 17 and requires five affine copies.
These examples defeat particular small-cover expectations; they do not
disprove every eventual bounded-cover assertion.

Another level-three choice, $C=4$, has a six-element shifted square-class
core with ten exceptions. Its signed-root image has size 41 and fits the stated one-copy image
cover. But the simple exceptional-pair charge is
$10(2\cdot16-10+1)=230$. The resulting bound is $41+230=271$, already larger
than the actual optimizer's 269. A good core alone has not paid for all pairs.

Repeating $C=4$ at the next actual input gives at least 929 values, exceeding
$3\cdot269=807$. This rejects that repeated parameter as the proposed
factor-three mechanism; it does not determine the next optimizer.

## SN-T03-5 — the missing RC15/4 statement and its conditional payoff

**OPEN premise; CONDITIONAL target conclusion via the reported implication.**
Source: **S-T03**, final adaptive-level obligation and rate ledger.

The required statement concerns every sufficiently large **actual** level.
It asks for fixed $H<\infty$ and $m_0$ such that, for every $m\ge m_0$, there
are $C^\dagger\in F_m=\mathbb Q(A_m)$ with $C^\dagger>M$, a subset
$B\subset A_m$, and a common positive square-class representative $\gamma\in F_m$
satisfying

\[
|A_m\setminus B|\le H\sqrt n,\qquad
C^\dagger+a=\gamma u_a^2\quad(u_a\in F_m,\ a\in B),
\]

and, with $U=\{\pm u_a:a\in B\}$ and $s_m=|Q(A_m,A_m)|$,

\[
|\gamma Q(U,U)|\le\frac{15}{4}s_m+Hn^{3/2}.
\]

The field condition is part of the obligation. It cannot be met by simply
adjoining every desired square root and then ignoring the extension cost.
One must also justify the comparison with the defined optimizer.

Writing $e=|A_m\setminus B|$, the exceptional signed-pair charge is at most
$e(2n-e+1)\le3Hn^{3/2}$. The reported optimizer comparison would then give

\[
s_{m+1}\le\frac{15}{4}s_m+4Hn^{3/2}.
\]

Since $n=2^{m+1}$ and $2^{3/2}<15/4<4$, this yields
$s_m=O((15/4)^m)$ and eventually any target exponent
$0<c<\log_2(16/15)$. The strict inequality absorbs fixed constants.
This is a conditional consequence. No uniform choice of $C^\dagger$, root
core, and support bound is proved in the retained record.

## Recall check

1. Why do $4^m$ pairs with $3^m$ norms not settle the problem? **The
   coordinate set creates additional ordered pairs whose outputs must be counted.**
2. What does the square-class decomposition still leave to control? **The
   actual signed-root support inside the base field.**
3. What is missing beyond the finite levels? **RC15/4 with fixed constants
   on every sufficiently large level of the actual adaptive sequence.**
