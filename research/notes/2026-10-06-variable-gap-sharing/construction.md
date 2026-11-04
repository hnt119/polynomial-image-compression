# Output-first windows assembled into shared-edge double triangles

2026-10-06, version 1. T01, fixed \(P(x,y)=(x-y)^3+x+y\).
This is the one commissioned variable-gap family. Its labels are chosen
before the scalar endpoints, and exact branch rules assemble them into
directed double triangles. No numerical program, full-square enumeration,
network access, dependency installation, or additional candidate is used
in this appendix. The lead's separately budgeted finite evidence is not a
premise of any proof here.

**PROVED:** this construction has an unbounded partner degree and growing
scalar and output reuse. Its exact counts are
\[
 N=k^3,\qquad Q=2k^4-k(k+1),\qquad Z=2k^3-k,
 \qquad k\ge3.
\tag{C1}
\]
It nevertheless leaves \(N^2-\Theta(N^{4/3})\) ordered pairs uncovered.
Its reconstructed carrier is an integer interval, whose actual full image
is already known to be \(N^2-O(N^{3/2})\). Thus this particular assembled
network does not supply the requested full-support power saving.

## 1. Sources, scope, and selection order

The inherited coordinate formulas and the exact shared-edge equations are
in the current [compatibility companion](compatibility.md). The scalar
accounting follows the [construction template](../../templates/CONSTRUCTION_LEDGER.md).
The relevant earlier comparison is
[GS-P3](../2026-09-21-growing-step-cubic/structure-and-reuse.md),
equations (3.1)–(3.5), dated 2026-09-21: a complete consecutive output-by-difference
rectangle already attains prescribed mass \(\Theta(N^{4/3})\) and
growing coordinate reuse, but has a quadratic complement. The new point
here is the simultaneous double-triangle gluing with every boundary
checked. Neither growing reuse nor the exponent \(4/3\) is claimed as
an improvement on that predecessor.

The actual-image input is
[GS-A4](../2026-09-21-growing-step-cubic/progression-laboratory.md), §4,
equations (A16)–(A18). Its complete proof and the GS-P3 proof were read;
their precise scopes are used below. The earlier fixed-gap triangle
family is closed and is not reintroduced here. No global elliptic group
identity, SH-O1 proof attempt, or unrelated network family is used.

First choose an integer \(k\ge3\) and set \(L=k^3\). Define the fixed
integer-valued functions on \(\mathbb Z\)
\[
 f(u)=\frac{u^3-u}{2},\qquad
 g(u)=\frac{u^3+u}{2}=f(u)+u.
\]
Choose the output/difference labels
\[
 \Lambda_k=\{(j,u):1\le |u|\le k,\ j\in I_u\cap\mathbb Z\},
\]
\[
 I_u=\left[\frac{u^3+|u|}{2},
             L-1+\frac{u^3-|u|}{2}\right].
\tag{C2}
\]
Both endpoints of each window are integers. Only then reconstruct
\[
 x(j,u)=j-f(u),\qquad y(j,u)=j-g(u),\qquad
 P(x(j,u),y(j,u))=2j.
\tag{C3}
\]
Let \(E_k\) be the resulting set of distinct ordered pairs, and let
\(A_k\) be the union of all their scalar endpoints. Write
\(N=|A_k|\), \(Q=|E_k|\), \(Z=|P(E_k)|\).

## 2. VG-C1 — exact reconstruction, pair count, and output support

**PROVED.** The scalar and pair sets derived from (C2) are exactly
\[
 A_k=\{0,1,\ldots,L-1\},
\]
\[
 E_k=\{(a,b)\in A_k^2:1\le |a-b|\le k\}.
\tag{C4}
\]
Each label produces a distinct ordered pair, so formal labels and actual
pairs have the same count. The complete selected output support is
\[
 P(E_k)=\{2j:-f(k)\le j\le L-1+f(k),\ j\in\mathbb Z\}.
\tag{C5}
\]
Consequently \(N=L\), \(Q=2kL-k(k+1)\), and
\(Z=L+k^3-k\), proving (C1) when \(L=k^3\).

**Proof.** Subtracting \(f(u)\) from the endpoints of \(I_u\) shows
that \(x\) runs exactly through
\[
 [\max(u,0),\ L-1+\min(u,0)]\cap\mathbb Z,
\]
while \(y=x-u\). This proves the pair-set equality in (C4) in both
directions. The branches \(u=1\) already use every integer from 0 to
\(L-1\), proving the scalar equality. The label map is injective because
the pair determines \(u=x-y\) and \(j=x+f(u)\). Each positive difference
\(u\) and its negative contribute \(L-u\) pairs; summing gives the
stated \(Q\).

For \(1\le d\le k\), the output-index windows are
\[
 I_d=[g(d),L-1+f(d)],\qquad
 I_{-d}=[-f(d),L-1-g(d)].
\tag{C6}
\]
The windows \(I_1,I_{-1}\) together contain every integer from 0 to
\(L-1\). Successive positive windows overlap or are adjacent if
\[
 L\ge g(d+1)-f(d)=\frac{3d^2+5d+2}{2}.
\]
For \(1\le d<k\), the largest required value is
\((3k^2-k)/2\), and \(L=k^3\) meets it. Reflecting the positive
windows under \(j\mapsto L-1-j\) proves the corresponding statement
for the negative windows. Their union is exactly the integer interval
in (C5). Multiplication by two is injective, so it has
\(L+2f(k)=L+k^3-k\) selected outputs. \(\square\)

The selected fiber at an output \(2j\) has the exact size
\[
 q_j=\#\{u:1\le |u|\le k,\ j\in I_u\},\qquad
 \sum_jq_j=Q,\qquad q_j\le2k.
\tag{C7}
\]
Thus average selected-output reuse is \(Q/Z\sim k\). Each scalar
\(a\in A_k\) has exactly
\[
 d_k(a)=\min(k,a)+\min(k,L-1-a)
\tag{C8}
\]
outgoing selected neighbors and the same number of incoming neighbors.
In particular \(k\le d_k(a)\le2k\). The \(2Q\) coordinate
occurrences have average scalar multiplicity \(2Q/N\sim4k\).
These are actual scalar and output counts, with no formal multiplicity
being credited as a new edge.

## 3. VG-C2 — a finite gluing rule and growing partner degree

**PROVED.** Every edge of \(E_k\) belongs to a directed shared-edge
double triangle whose five edges all lie in \(E_k\). For each base edge
there are at least \(k-1\) distinct choices of a third vertex, and hence
at least \((k-1)(k-2)\) ordered choices of two distinct partners.
The four vertices in each such double triangle are distinct.

The branch formulas are fixed, independent of \(k\). Start with
\((j,u)\in\Lambda_k\) and \((a,b)=(x(j,u),y(j,u))\). For a partner
\(c=b-v\), define the two closing labels
\[
 \Phi_1(j,u,v)=(j-g(u)+f(v),\ v),
\]
\[
 \Phi_2(j,u,v)=(j-f(u)-g(u+v),\ -u-v).
\tag{C9}
\]
They reconstruct exactly \((b,c)\) and \((c,a)\). A second parameter
\(t\), using the same two branches, reconstructs \((b,d),(d,a)\),
where \(d=b-t\). Thus the branches genuinely identify all common
scalars, rather than treating the five edges independently.

**Proof of the global boundary and partner count.** Put
\[
 s=\max\{0,\max(a,b)-k\}.
\tag{C10}
\]
Since \(1\le|a-b|\le k\) and \(L\ge k+1\), the consecutive block
\(\{s,s+1,\ldots,s+k\}\) is contained in \(A_k\) and contains
both \(a,b\). Each of its \(k-1\) other vertices may be chosen as
\(c\). Then \(v=b-c\ne0\), \(u+v=a-c\ne0\), and their absolute
values are at most \(k\). By (C4), both \((b,c)\) and \((c,a)\)
belong to \(E_k\). Equivalently their exact labels (C9) lie in
\(\Lambda_k\), including their specified output windows; no boundary
label has been discarded or assumed admissible. Any two distinct such
vertices \(c,d\) give the five required edges, and \(u\ne0\) ensures
that all four vertices are distinct. Moreover, both cross-partner edges
\((c,d)\) and \((d,c)\) also lie in \(E_k\), since their distance is
at most \(k\). Their outputs are already included in (C5). Thus the
same rule controls local cross-partner pairs as well as the five motif
edges. This proves the count and closure claims. \(\square\)

The complete number of eligible partner vertices for a fixed edge is
\[
 p_k(a,b)=\min\{L-1,\min(a,b)+k\}
          -\max\{0,\max(a,b)-k\}-1.
\tag{C11}
\]
This is the size of the common distance-\(k\) neighborhood after removing
\(a,b\). In particular \(p_k(a,b)\ge k-1\). A network may use any
or all of these double triangles; repeated five-edge motifs do not change
\(Q\). Every pair already counted in (C4) participates, so there are
no orphan boundary edges or independently appended pairs.

Pairwise distinct output labels are not required by this family. The
compatibility equations allow output coincidences, and (C5)–(C7) count
them exactly. There are also motifs with all five outputs distinct:
for \(k=3,L=27\), take \((a,b,c,d)=(1,0,2,3)\). In the order
\((a,b),(b,c),(c,a),(b,d),(d,a)\), the labels are
\[
 (1,1),\ (-3,-2),\ (2,1),\ (-12,-3),\ (6,2),
\]
and the outputs are \(2,-6,4,-24,12\). These identities are direct
hand substitution; no finite run is used as a proof of closure.

## 4. VG-C3 — the complement and cubic-span bottleneck

**PROVED.** With \(N=L=k^3\), the exact number of uncovered pairs is
\[
 B=N^2-Q=k^6-2k^4+k^2+k.
\tag{C12}
\]
Charging one possible extra output for each gives the safe whole-support
certificate
\[
 |P(A_k,A_k)|\le Z+B
 =k^6-2k^4+2k^3+k^2.
\tag{C13}
\]
The selected-output gate holds strongly, \(Z\sim2N\), but the coverage
ratio is
\[
 Q/N^2=2/k^2-(k^2+k)/k^6\longrightarrow0.
\tag{C14}
\]
Hence the growing number of partners, scalar reuse and output reuse does
not supply almost-full coverage. It increases selected mass from linear
to \(\Theta(N^{4/3})\), the scale already present in GS-P3.

The source of the cost is explicit: output windows are centered at the
cubic offsets \(u^3/2\). Their total index span is
\(L+k^3-k\), while a row has only \(L-|u|\) edges. The boundary
correlation in (C2) successfully glues those rows, but the chosen
\(L=k^3\) leaves only \(2k\) possible differences at each scalar
inside an \(L\)-point carrier. No triangle-motif multiplicity removes
the \(L^2-Q\) omitted scalar pairs.

There is also a stronger inherited obstruction for this exact carrier.
By GS-A4 with spacing 1 and
\[
 D_N=\min\{N-1,\lfloor\sqrt{2(N-1)}\rfloor\},
\]
every actual nonsingleton pair has \(|a-b|\le D_N\). Counting the
remaining pairs exactly gives
\[
 |P(A_k,A_k)|\ge(N-D_N)(N-D_N-1)
 =N^2-O(N^{3/2}).
\tag{C15}
\]
Together with the trivial upper bound, this proves actual full-image
density tending to one. Thus incidental pairs and outputs outside the
prescribed network cannot rescue this interval carrier. This is a
precise import of a proved carrier theorem, not a new AP search or a
universal lower bound for other scalar completions.

## 5. Construction and quantitative ledger

| Item | Charged value or explanation | Status |
|---|---|---|
| Order of choices | Integer \(k\ge3\), then \(L=k^3\), then the correlated label windows (C2), then endpoints (C3) | PROVED |
| Actual scalar count | Exactly \(N=L=k^3\); lower and upper counts coincide | PROVED |
| Same-set transport | Every reconstructed endpoint lies in the one real set \(A_k\); all ordered pairs are selected or charged in \(B\) | PROVED |
| Input thinning in both coordinates | None. Selected pair thinning costs exactly \(B=N^2-Q\), rather than changing the input size | PROVED |
| Parameter and pair multiplicity | The label-to-ordered-pair map is injective. Different motifs may use the same pair; those occurrences are counted only once in \(Q\) | PROVED |
| Scalar reuse | Exact degrees (C8), average coordinate multiplicity \(2Q/N\sim4k\) | PROVED |
| Output reuse | Exact fiber formula (C7), \(q_j\le2k\), average \(Q/Z\sim k\) | PROVED |
| Gluing branches and boundaries | Two fixed polynomial label branches (C9), used twice per double triangle; (C10) checks the entire finite boundary | PROVED |
| Partner and motif counts | At least \(k-1\) partners per actual edge. Motif count is not substituted for pair count or image support | PROVED |
| Local splitting, moduli, and per-residue populations | Inapplicable: no sieve, local-density estimate, finite-field model, or arithmetic amplification | PROVED |
| Field degree, discriminant, regulator, units | All scalars are integers in \(\mathbb Q\); no extension, unit selection, or regulator cost | PROVED |
| Denominators and heights | The halves in (C2)–(C3) are integral by parity. Scalar height at most \(L-1\); output-index range exactly (C5). No scaling of the fixed polynomial | PROVED |
| Archimedean distortion | Diameter exactly \(L-1\); projection is literal real inclusion, with no metric or packing gain | PROVED |
| Carries and branch inventory | No digit expansion or carry certificate. Branch count is fixed, but the difference inventory has \(2k\) actual entries | PROVED |
| Uncovered and exceptional outputs | Every omitted ordered pair, including all diagonals and large differences, is charged once in (C12)–(C13) | PROVED |
| Rates | For depth \(d=\log k\), input rate 3, selected pair rate 4, selected support rate 3, and full-image rate 6. The net full-support exponent gap is zero | PROVED |
| Positive fixed power saving | The selected-pair certificate is insufficient, and the actual interval carrier has density-one image by (C15) | PROVED scoped obstruction |

## 6. Evidence, comparison, and retained boundary

VG-C1–VG-C3 concern every integer \(k\ge3\), this fixed polynomial, and
only the displayed label-window family. They are complete symbolic proofs,
dated 2026-10-06, version 1. VG-C2 uses the exact compatibility branches;
VG-C3 uses GS-A4 for the actual-image statement. The earlier GS-P3 rate
is reported as prior work and is not presented as a newly improved rate.
The lead independently audited the complete VG-C1–VG-C3 proofs, including
the window union, exact counts, gluing boundaries, complement, and inherited
image-bound specialization, and found no mathematical correction needed.
The cycle verification record records this internal audit separately from
finite evaluations. No external review, literature comparison, or novelty
is claimed.

The actual construction is an assembled closed motif network, with growing
partner degree at every selected edge. Its exact scalar completion is
nevertheless the interval (C4), so the known image obstruction applies.
Changing only the motif multiplicities or reindexing the same completed
carrier cannot change this conclusion. Any successful modification would
have to change the scalar completion and simultaneously preserve the label
sharing rules; favorable counts alone cannot be assumed.

No new alternative carrier or further lemma is pursued here. The lead
report selects the task's one next obligation, if any. The fixed T01
power-saving target remains **OPEN**.
