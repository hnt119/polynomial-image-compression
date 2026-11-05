# Four tetrahedral closing patterns fail before enumeration

T01 · 20 October 2026 · version 1 · offline, bounded constructive test  
Fixed polynomial: \(P(x,y)=(x-y)^3+x+y\).

**PROVED — TJ-C4.** None of the four registered mixed-role systems has an
admissible real realization. Thus this catalogue supplies no finite seed,
no attachment, and no improvement on the earlier \(N^{4/3}\) prescribed-pair
benchmark. This is a scoped obstruction, not a classification of tetrahedra.
The unrestricted T01 target remains **OPEN**.

[Fixed catalogue](catalogue.md) · [Proof appendix](compatibility.md) ·
[Independent referee](referee-audit.md) · [Verification and source ledger](verification.md)

## 1. Candidate and labelled endpoints

**Meaning.** We prescribed the outputs first and asked whether six frames
could share actual real scalars, including all four slots of the closing
frame. A tetrahedral drawing is only an incidence pattern.

**Statement — TJ-C1, PROVED.** Choose \(a,b>0\) and
\[
(z_0,z_1,z_2,z_3)=(0,a,a+b,D),\qquad D=2a+b.
\]
The symmetric gap rule \((a,b,a)\) is a deliberate restriction; no scaling
or claim of generality is involved. Put
\[
t=D/4,\qquad e=a/4,\qquad \ell=(a+b)/4.
\]
The following are actual scalar endpoints after adding \(t\) to each entry.
The symbols \(q,r,S\) below denote column halfwidths.

| Frame | Row endpoints relative to \(t\) | Column endpoints relative to \(t\) | Lower / upper output |
|---|---|---|---|
| \(01\) | \(-\ell\pm u\) | \(-\ell\pm v\) | \(0,a\) |
| \(23\) | \(\ell\pm u\) | \(\ell\pm v\) | \(a+b,D\) |
| \(02\) | \(-e\pm p\) | \(-e\pm q\) | \(0,a+b\) |
| \(13\) | \(e\pm p\) | \(e\pm q\) | \(a,D\) |
| \(12\) | \(\pm w\) | \(\pm r\) | \(a,a+b\) |
| \(03\), closing | \(\pm H\) | \(\pm S\) | \(0,D\) |

Every halfwidth is positive, each row halfwidth is less than \(1/\sqrt3\),
and the row and column halfwidths in each frame differ. Simultaneously require
\[
3u^2+v^2=3p^2+q^2=3w^2+r^2=3H^2+S^2=1,
\]
\[
C(u)=a,\quad C(p)=a+b,\quad C(w)=b,\quad C(H)=D,
\qquad C(x)=8x(1-2x^2).
\]
The matching branch on \(02/13\) is imposed, not inferred from their equal
gaps. All admissible branches under these equations are retained.

For each \(\epsilon=\pm1\), the opposite-edge identifications are
\[
R_{01}^{\epsilon}=K_{23}^{-},\qquad
R_{23}^{-\epsilon}=K_{01}^{+}
\quad\Longleftrightarrow\quad 2\ell=v+\epsilon u.
\]
Here \(R_{ij}^{\sigma}\) is a row scalar and \(K_{ij}^{\sigma}\) is a column
scalar. We fixed two closing patterns, hence four cases:

| Pattern | Closing row identifications | Closing column identifications | Reduced equations |
|---|---|---|---|
| A | \(R_{03}^{\pm}=K_{12}^{\pm}\) | \(K_{03}^{-}=R_{02}^{-},\ K_{03}^{+}=R_{13}^{+}\) | \(H=r,\ S=e+p\) |
| B | \(R_{03}^{-}=K_{02}^{-},\ R_{03}^{+}=K_{13}^{+}\) | \(K_{03}^{\pm}=R_{12}^{\pm}\) | \(H=e+q,\ S=w\) |

**Proof.** Direct expansion on \(3h^2+s^2=1\) gives
\[
P(q_{ij}\pm h,q_{ij}\pm s)=2q_{ij}\pm C(h)/2,
\]
where the row sign determines the output and the column sign is free.
Subtracting the displayed centers gives every sharing equation above.
Reflection \(x\mapsto D/2-x\) sends outputs to \(D-z\), explaining the
paired signs. It preserves row versus column roles.

**Scope.** The equations involve all four output labels and all six frames.
They would make the closing slots old. They do not, by themselves, connect
the scalar-sharing component \(01/23\) to the other four frames. New pairs
and a third distinct row would still require deduplication on a real seed.
This is not the earlier VO-O1 triangular subsystem.

## 2. Worked obstruction

**Meaning.** The output gaps and the opposite-edge sharing already constrain
the widths enough to contradict each proposed closing pattern.

**Common bounds — TJ-C1, PROVED.** The maximum of \(C\) on the frame domain
is \(C_{\max}=16/(3\sqrt6)\). Since \(2a<D\le C_{\max}\), the short width
is unique and \(0<u<1/6\). With \(v=\sqrt{1-3u^2}\), the opposite-edge rule gives
\[
b=2v+(2\epsilon-8)u+16u^3,\qquad
D=2v+(2\epsilon+8)u-16u^3.
\]
Because \(v>1-3u^2\),
\[
D-2>u(6-6u-16u^2)>0.
\]
On the admissible domain \(C(x)\le2\) for \(x\ge1/2\). Consequently
\[
H<1/2.
\]
These bounds use no selection of a branch for \(p,w,H\).

**Pattern A — TJ-C2, PROVED.** It cannot close for either sign.
Indeed \(H=r<1/2\) implies \(w>1/2\), and the two conics imply
\(S^2=9w^2-2\). Write \(g=C/4=2x-4x^3\).
Since \(e=g(p)-g(w)\) and \(S=e+p\),
\[
p+g(p)=S+g(w).
\]
The left side is \(3p-4p^3\le1\), with its maximum at \(p=1/2\).
For \(w>1/2\), both \(S\) and \(3w-1\) are positive, and
\[
S^2-(3w-1)^2=6w-3>0.
\]
Hence
\[
S+g(w)>5w-4w^3-1>1,
\]
where the last strict inequality follows from
\[
5w-4w^3-2=(2w-1)(2-w-2w^2)>0
\quad(1/2<w<1/\sqrt3).
\]
This contradicts the same quantity being at most one.

**Pattern B — TJ-C3, PROVED.** It cannot close for either sign.
Here \(S=w\), so \(3H^2+w^2=1\) and \(w>1/2\).
On \(1/2<w<1/\sqrt3\), the function
\[
F(w)=3C\!\left(\sqrt{(1-w^2)/3}\right)+C(w)
\]
strictly decreases from \(F(1/2)=8\). Thus \(3D+b<8\).
But the opposite-edge formula gives
\[
3D+b=8\{v+(2+\epsilon)u-4u^3\}
\ge8(v+u-4u^3)>8,
\]
because \(v>1-3u^2\) and
\(u-3u^2-4u^3=u(1-4u)(1+u)>0\).
The derivative and its exact positive factorization are in the appendix.

**Limitation.** Pattern B is excluded already by \(S=w\), without using
\(H=e+q\). Pattern A uses both closing equations. Neither argument assumes
the earlier forbidden triangle or proves that other tetrahedral roles fail.
The boundary \(u=0\) would merge output labels and is not an admissible seed.

## 3. Counts, full-square audit, and attachment disposition

**PROVED — TJ-C4.** There is no actual scalar set \(A\) or pair union \(E\)
satisfying any registered case. Empty feasibility is not an empty-set
construction.

| Cases | \(N,Q,Z,B\) | Full-square fiber distribution | Attachment |
|---|---|---|---|
| \(A,+;\ A,-;\ B,+;\ B,-\) | Not defined: no realization | Not applicable: no seed | Stops at the failed base case |

**PROVED — TJ-C5, accounting only.** For any real finite frame union,
deduplicate \(A\), \(E\), and outputs before using
\[
N=|A|,\quad Q=|E|,\quad Z=|P(E)|,\quad B=N^2-Q,\qquad
|P(A,A)|\le Z+B.
\]
The inequality charges at most one output for each uncovered pair. For a
six-frame tetrahedron \(Q\le24,\ Z=4\); each output receives at most six
selected pairs from at most three distinct first coordinates. The two
opposite-edge identifications and zero-cost closing roles would give
\(N\le18\): five frames have at most twenty scalar slots, and the two
opposite-edge equalities identify two distinct pairs of slots. These are
capacity bounds, not attained counts in this report.

Accordingly, the formal ceilings \(2Q/N\le48/N\), \(Q/Z\le6\) and
\(Q/N^2\le24/N^2\) cannot be reported as measured reuse ratios.
There is no actual image to screen for an injective subgrid. No successful
tetrahedron survives from which to test a growth attachment. No new
unbounded family or rate is obtained, including no improvement over
\(Q\asymp N^{4/3}\).

For context, the earlier \(N=4m,Q=6m-2,Z=m+1\) continuation and its actual
image lower bound \(N^2/16\) are **imported PROVED results** (VO-C3–C4).
They are separate from the present nonexistence argument and were not rerun.
The general requirement of growing rows is unchanged: a fixed row contributes
at most three pairs to a given actual output because the equation in its
second coordinate is a nonzero cubic.

## 4. Exactly one next lemma

**OPEN — TJ-O1; recorded, not tested.** Keep the output rule, conics, all
nondegeneracy conditions and the \(\epsilon=-1\) opposite-edge roles.
Change only pattern A's two closing columns from outward **rows** of
\(02/13\) to their outward **columns**:
\[
H=r,\qquad S=e+q
\quad\text{instead of}\quad H=r,\ S=e+p.
\]
Decide whether this exact system has an admissible real solution for which
the closing frame adds at least two distinct ordered pairs to the other
five frames and gives output \(0\) or \(D\) a third distinct first coordinate.
All closing scalars would still be old.

This is one concrete role change: it removes the \(p+g(p)\le1\) comparison
used in A, while imposing neither B's \(S=w\) nor the frozen VO-O1 roles.
It is not evidence of feasibility or an asymptotic claim. No fifth case or
successor search was executed.

## 5. Evidence status

TJ-C1–C4 were proved by exact symbolic arguments and independently checked
by the lead and referee; TJ-C5 is an elementary counting implication.
The four-case catalogue was fixed before solving its systems. No parameter
enumeration, target-polynomial evaluation run, package installation, network
access, external theorem, or novelty claim was used. The conditional
5,000-unit finite-seed budget was not activated. See the source ledger for
the imported VO checkpoint, formally frozen VO-C6, preservation checks,
and repository validation.
