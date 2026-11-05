# T01 tetrahedral junction: fixed four-case catalogue

**2026-10-20; selection record, before solving these four systems.**
This is the bounded catalogue chosen for the current authorized offline task.
No claim of exhaustive classification of tetrahedral endpoint roles is made.
The polynomial is always \(P(x,y)=(x-y)^3+x+y\).

## Output rule and all branches

Choose \(a,b>0\), put \(D=2a+b\), and prescribe the outputs
\((z_0,z_1,z_2,z_3)=(0,a,a+b,D)\).
This reflection-symmetric gap rule is a restriction, not a normalization
available for arbitrary four outputs. No scaling is used.

Write \(t=D/4,\ e=a/4,\ \ell=(a+b)/4\). The table lists scalar
coordinates relative to \(t\); add \(t\) to every displayed endpoint.

| Edge | Center relative to \(t\) | Row widths | Column widths |
|---|---:|---:|---:|
| 01 | \(-\ell\) | \(u\) | \(v\) |
| 23 | \(\ell\) | \(u\) | \(v\) |
| 02 | \(-e\) | \(p\) | \(q\) |
| 13 | \(e\) | \(p\) | \(q\) |
| 12 | \(0\) | \(w\) | \(r\) |
| 03 | \(0\) | \(H\) | \(S\) |

Here \(q\) is a column width, distinct from the frame-center notation
\(q_{ij}\). Require
\[
3u^2+v^2=3p^2+q^2=3w^2+r^2=3H^2+S^2=1,
\]
\[
C(u)=a,\quad C(p)=a+b,\quad C(w)=b,\quad C(H)=D,
\qquad C(x)=8x(1-2x^2).
\]
All eight widths are positive; each row width is less than \(1/\sqrt3\);
exclude \(u=v,\ p=q,\ w=r,\ H=S\).
The equal widths on 02 and 13 are imposed as part of this catalogue;
equal output gaps alone need not force equal branches.
All admissible width branches subject to these equations are retained.

## Opposite-edge roles

For each \(\epsilon\in\{-1,1\}\) impose
\[
R_{01}^{\epsilon}=K_{23}^{-},\qquad
R_{23}^{-\epsilon}=K_{01}^{+}.
\]
Here \(R_{ij}^{\sigma}=q_{ij}+\sigma h_{ij}\) is a row scalar and
\(K_{ij}^{\sigma}=q_{ij}+\sigma s_{ij}\) is a column scalar.
Both equations reduce to
\[
2\ell=v+\epsilon u.
\]
These are genuine mixed-role identifications between opposite edges.

## Two closing patterns, four cases total

| Pattern | Closing rows reused from | Closing columns reused from | Width equations |
|---|---|---|---|
| A | \(R_{03}^{\pm}=K_{12}^{\pm}\) | \(K_{03}^-=R_{02}^-,\ K_{03}^+=R_{13}^+\) | \(H=r,\ S=e+p\) |
| B | \(R_{03}^-=K_{02}^-,\ R_{03}^+=K_{13}^+\) | \(K_{03}^{\pm}=R_{12}^{\pm}\) | \(H=e+q,\ S=w\) |

The four cases are \((+,A),(-,A),(+,B),(-,B)\).
Each gives zero new scalar slots for 03 if the simultaneous system is
realizable. New ordered pairs, distinct rows, and all other coincidences
must still be checked on any actual seed. The prescribed sharing equations
do not themselves force the opposite-edge pair 01/23 to share a scalar with
the other four frames; the output-label graph is connected.

## Order of work and finite budget

First prove compatibility or nonexistence analytically for these systems.
Only if exact real seeds survive, enumerate their actual scalar and pair
unions and full-square fibers, within a total budget of **5,000 polynomial
evaluations and checked predicates combined**. No floating-point equality
test is evidence. No additional role catalogue, external search, or package
installation is authorized by this record.

The two specialist roles are `/root/finite_gadgets` (construction) and
`/root/symbolic_obstruction` (independent referee), coordinated by `/root`.
If no seed survives, stop the proposed extension at its failed base case.
