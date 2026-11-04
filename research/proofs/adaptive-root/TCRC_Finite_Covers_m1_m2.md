# Exact finite root covers at the first two certified inputs

This note works offline. It uses the frozen adaptive-family identities and square-class localization theorem. Its finite computations use rational arithmetic only. It establishes finite root-cover identities, not the asymptotic TCRC conjecture.

## 1. Results and quantitative ledger

Write (S=Q(A,A)), choose the largest square class (B\subset A) of the shifted radicands (C+a), and write (C+a=\gamma u_a^2), with (U=\{\pm u_a:a\in B\}). Put (R=\gamma Q(U,U)).

| Input | Legal (C\in\mathbb Q(A)) | Largest (B) | (n-|B|) | \(\gamma\) | Positive roots (u_a) | \(|R|/|S|\) | Exact affine cover of (R) | \(|\mathcal T_C(A)|\) |
|---|---:|---|---:|---:|---|---:|---|---:|
| \(A_1=\{\pm1,\pm2\}\) | \(5/2\), optimizer | \(\{-2,2\}\) | 2 | \(1/2\) | \(1,3\) | \(6/5\) | 2 copies | 17 |
| \(A_1\) | \(3\) | \(\{-2,1\}\) | 2 | 1 | \(1,2\) | 1 | identity copy | 19 |
| \(A_1\) | \(17/8\) | \(\{-2,-1,1\}\) | 1 | \(1/8\) | \(1,3,5\) | \(12/5\) | exactly 4 copies; 3 cover at most 11 of 12 values | 20 |
| \(A_2=\{\pm1,\pm\sqrt3,\pm\sqrt7,\pm3\}\) | \(4\), optimizer | \(\{-3,-1,3\}\) | 5 | 1 | \(1,\sqrt3,\sqrt7\) | \(11/17\) | identity copy | 68 |
| \(A_2\) | \(6\) | \(\{-3,1,3\}\) | 5 | 1 | \(\sqrt3,\sqrt7,3\) | \(11/17\) | identity copy | 71 |

The (C=17/8) comparison is a concrete reason to prefer a direct image-cardinality bound over an exact three-affine-cover formulation: the latter fails here, although 

\[
|R|=\frac{12}{5}|S|<3|S|.
\]

It is not a disproof of TCRC, which can choose another parameter and concerns all sufficiently large actual levels. The fixed finite exception counts in this table give no uniform asymptotic exceptional-set estimate.

## 2. The certified (m=1) optimizer has a non-vacuous two-copy cover

The old image is

\[
S_1=\{1,3,4,7,12\}.
\]

At (C=5/2), the shifted radicands are (1/2,3/2,7/2,9/2). Their square classes in the correct field (F_1=\mathbb Q) have sizes (2,1,1). The unique largest class has input labels (B=\{-2,2\}), representative (\gamma=1/2), and root set (U=\{\pm1,\pm3\}). Direct evaluation gives

\[
R=\tfrac12\{1,3,7,9,13,27\}.
\]

Define two affine maps, fixed for the entire image,

\[
\ell_1(t)=-t+\frac{15}{2},\qquad
\ell_2(t)=3t-\frac{15}{2}.
\]

Their exact intersections with (R) are

\[
\ell_1(S_1)\cap R=\tfrac12\{1,7,9,13\},
\qquad
\ell_2(S_1)\cap R=\tfrac12\{3,9,27\}.
\]

Thus (R\subseteq\ell_1(S_1)\cup\ell_2(S_1)). Both maps cover at least three target values, and one covers four; the certificate does not consist of fitting two arbitrary target points per map. No single affine image can cover six values because it has at most five values. The attached exact matched-pair search additionally certifies that the largest single-map intersection has size four.

The singleton radicand (3/2) contributes only (3/2,9/2\in R). The singleton (7/2) contributes (7/2\in R) and (21/2\notin R). Hence the within-field image has size seven. Frozen localization then gives

\[
|\mathcal T_{5/2}(A_1)|=4^2-(2^2+1^2+1^2)+7=17.
\]

## 3. A legal comparison parameter with an exact root-set return

At (C=3), the shifted radicands of (A_1) are (1,2,4,5). Their square classes in (\mathbb Q) have sizes (2,1,1), with largest class (B=\{-2,1\}). Taking (\gamma=1) gives

\[
U=\{\pm1,\pm2\}=A_1,
\qquad R=S_1.
\]

This is an exact one-copy root-cover mechanism. The exceptional labels are (\{-1,2\}). Their diagonal outputs are (2,6,5,15), all distinct and outside (S_1). Consequently the within-field image has size nine, and

\[
|\mathcal T_3(A_1)|=16-6+9=19.
\]

The cover is structurally stronger than the optimizing parameter's two-copy cover, but the total image is larger because the exceptional labels contribute too much.

## 4. Three affine copies fail at (C=17/8), even though the direct factor is (12/5)

Here (C>2=M(A_1)), and

\[
C+A_1=\tfrac18\{1,9,25,33\}.
\]

Thus there is a unique largest class of size three, labeled (B=\{-2,-1,1\}), with (\gamma=1/8), and

\[
U=\{\pm1,\pm3,\pm5\}.
\]

Its root image is

\[
R=\tfrac18T,\qquad
T=\{1,3,7,9,13,19,21,25,27,31,49,75\}.
\]

The exact minimum number of affine copies of (S_1) needed to cover (T), equivalently (R), is four. This holds even if the affine coefficients are allowed to be arbitrary real numbers.

Four explicit maps covering (T) are

\[
t,\qquad 6t+3,\qquad 6t+7,\qquad 3t-2.
\]

Indeed, their relevant hit sets are respectively

\[
\{1,3,7\},\quad
\{9,21,27,75\},\quad
\{13,25,31,49\},\quad
\{1,7,19\}.
\]

Divide all four maps by eight to cover (R). The first three cover exactly (T\setminus\{19\}).

### Exact exhaustiveness certificate

Suppose a nonconstant affine map meets (T) in two distinct points (t_1,t_2), at distinct source points (s_1,s_2\in S_1). Necessarily

\[
\alpha=\frac{t_2-t_1}{s_2-s_1},\qquad
\beta=t_1-\alpha s_1.
\]

These coefficients are rational. Every map meeting (T) in at least two points therefore appears in the enumeration over unordered distinct source pairs and ordered distinct target pairs. Its hit set is computed exactly using rational arithmetic.

A map meeting (T) in exactly one point can be replaced by an enumerated map whose hit set contains that point and one further target point. This includes zero-slope maps. A map meeting no target points is irrelevant. Thus no real affine map omitted from the enumeration can improve an optimal cover.

The enumeration yields 122 distinct hit sets. Removing hit sets properly contained in another leaves 51 maximal hit sets. Exhaustive unions give the following exact maxima:

| Number of affine copies | Largest number of covered elements of (T) |
|---:|---:|
| 1 | 5 |
| 2 | 8 |
| 3 | 11 |

The standard-library program `tcrc_finite_covers_m1_m2.py` reconstructs all these sets and checks every union using integer bit masks. No numerical tolerances, optimization solver, or unverified root matching is used. This is a finite exact computational certificate of the lower bound of four copies.

The singleton radicand (33/8) contributes (33/8,99/8), neither in (R). Hence the within-field image has 14 values, and

\[
|\mathcal T_{17/8}(A_1)|=16-(3^2+1^2)+14=20.
\]

The sole exceptional label already prevents this particular comparison parameter from beating the optimizer. No claim about a large-level recurrence follows.

## 5. The certified (m=2) optimizer has an exact identity cover

Work in exactly

\[
F_2=\mathbb Q(\sqrt3,\sqrt7).
\]

The required standard algebra fact is the following precise multiquadratic theorem: if the rational square classes of (d_1,\ldots,d_r) are independent, then adjoining their square roots gives a degree (2^r) extension with the square-root monomials as a basis, and a rational number becomes a square in that extension precisely when its rational square class is in the subgroup generated by the (d_i). Here (3,7) are independent by their prime valuations. In particular, (1,\sqrt3,\sqrt7,\sqrt{21}) is a basis, and the rational classes becoming squares are (1,3,7,21).

At (C=4), the frozen exact partition of the shifted radicands is

\[
\{1,3,7\},\quad
\{4-\sqrt7,4+\sqrt7\},\quad
\{5\},\quad\{4-\sqrt3\},\quad\{4+\sqrt3\}.
\]

Thus the unique largest class has labels (B=\{-3,-1,3\}) and size three. The missing label (+1) has shifted radicand (5); its square root is not in (F_2). Choosing (\gamma=1) gives the exact root set

\[
U=\{\pm1,\pm\sqrt3,\pm\sqrt7\}\subset A_2.
\]

Therefore

\[
R=Q(U,U)\subseteq Q(A_2,A_2)=S_2
\]

with the identity affine map. More explicitly,

\[
R=\{1,3,7,9,21,\ 4\pm\sqrt3,\ 8\pm\sqrt7,\ 10\pm\sqrt{21}\}.
\]

These are eleven distinct values. The entire old image is

\[
S_2=R\cup\{13,27,\ 12\pm3\sqrt3,\ 16\pm3\sqrt7\},
\]

and has 17 distinct values. The field basis proves distinctness directly.

The second class has representative (\gamma=1/2) and positive roots (\sqrt7-1,\sqrt7+1), because

\[
4\pm\sqrt7=\frac{(\sqrt7\pm1)^2}{2}.
\]

Its six outputs are (5,11,4\pm\sqrt7,12\pm3\sqrt7). The singleton (5) adds only 15, and the two remaining singleton classes add only (12\pm3\sqrt3). Thus the within-field image has (11+6+1+2=20) values. The exact full image is

\[
|\mathcal T_4(A_2)|=64-(3^2+2^2+1+1+1)+20=68.
\]

The root cover has no loss at all; the obstruction at this finite input is the five exceptional input labels, not the cost of covering the dominant-class image.

## 6. A second identity cover at (m=2)

At (C=6>3=M(A_2)), the rational shifted radicands (3,7,9) are squares in (F_2), corresponding to labels (B=\{-3,1,3\}). Taking (\gamma=1),

\[
U=\{\pm\sqrt3,\pm\sqrt7,\pm3\}\subset A_2,
\qquad R\subset S_2.
\]

Here

\[
R=\{3,7,9,21,27,\ 10\pm\sqrt{21},\ 12\pm3\sqrt3,\ 16\pm3\sqrt7\},
\]

again of size eleven.

For completeness, this is the unique largest class. The remaining five radicands (5,6\pm\sqrt3,6\pm\sqrt7) occupy five distinct nontrivial square classes. The rational class (5) remains nonsquare in (F_2). For (x=6\pm\sqrt3\in\mathbb Q(\sqrt3)), if (x) or a rational multiple of (x) became a square in (F_2), then (x) or seven times (x), up to a rational square-class factor, would be square in \(\mathbb Q(\sqrt3)\); its rational norm has nonsquare class (33), which is impossible. The analogous norm for (6\pm\sqrt7) is 29. Opposite signs cannot merge because their products are respectively 33 and 29, neither a square in (F_2). Finally, a ratio between (x=6\pm\sqrt3) and (y=6\pm\sqrt7) has norm to \(\mathbb Q(\sqrt3)\) equal to (x^2/29), which cannot be a square there because 29 is not a square in \(\mathbb Q(\sqrt3)\). These observations also separate them from the rational classes.

All ten diagonal outputs from the five singleton classes are distinct and lie outside the displayed (R). This is checked directly in the field basis. The within-field image therefore has 21 values, and

\[
|\mathcal T_6(A_2)|=64-(3^2+1+1+1+1+1)+21=71.
\]

## 7. Scope and constructive implication

The exact root-set return at (m=1,C=3), and the two root-subset returns at (m=2,C=4,6), show that the proposed image-level mechanism already occurs at actual inputs. These examples do not show that it occurs on (n-O(1)) labels at arbitrarily large levels. No denominator or field enlargement is hidden: all parameters, representatives, roots and affine coefficients lie in the stated actual input field.

The (C=17/8) example gives a strict separation between two constructive goals on an actual input: its best affine cover requires four copies, whereas its exact image cardinality is only (12/5) times the old image size. Thus a proof of a direct fixed-factor estimate with factor below four need not provide a three-affine-copy cover. Any asymptotic use must still prove a sublinear exceptional-set bound; the finite ledger does not supply one.

The verifier is reproducible by running:

```bash
python output/tcrc_finite_covers_m1_m2.py
```

It checks the stated affine hit sets, exhaustive cover maxima, exact root identities, image cardinalities and field-basis arithmetic. The frozen square-class localization theorem is the only collision-counting theorem used to pass from the within-field ledger to the total branch images.
