# TCRC: exact zero-sum triangle accounting and the remaining image-cover requirement

This note works completely offline. It uses the supplied exact adaptive-set and square-class ledgers as frozen input. It does not prove TCRC, a parameter rule for all large levels, or a positive exponent for the actual adaptive family. Its new result is an exact direct-image accounting theorem for the zero-sum-triangle mechanism, together with its evaluation on the certified levels.

## 1. Essential signed labels and completion blocks

Let (V\subset\mathbb R_{>0}) have (r) elements, and put (U=V\cup(-V)). The essential labels for (Q(U,U)) are
\[
\mathscr L(V)=\{(\{a,b\},\epsilon):a,b\in V,\ \epsilon\in\{+,-\}\},
\]
with unordered pairs allowing repetitions. Their output is
\[
q_\epsilon(a,b)=a^2+b^2+\epsilon ab.
\]
Thus (|\mathscr L(V)|=r(r+1)). This counts labels, not distinct output values.

Define
\[
T(V)=\#\{(a,b):a,b\in V,\ a<b,\ a+b\in V\},
\qquad
D(V)=\#\{a\in V:2a\in V\},
\]
and
\[
P(V)=\#\{(a,b)\in V^2:a+b\in V\}=2T(V)+D(V).
\]

**Triangle partition theorem.** The equalities generated solely by completing a zero-sum triple partition the essential labels into:

- (T(V)) blocks of size three;
- (D(V)) blocks of size two;
- (r(r+1)-3T(V)-2D(V)) singleton blocks.

Consequently the exact number of these completion blocks is
\[
\boxed{\mathcal B(V)=r(r+1)-P(V).}
\tag{1}
\]
In particular there is the valid direct upper bound
\[
|Q(U,U)|\le\mathcal B(V).
\tag{2}
\]
Distinct completion blocks can have the same numerical norm. Neither (1) nor (2) is a lower bound for the actual image.

**Proof.** For (a<b) and (c=a+b\in V), the three labels
\[
(\{a,b\},+),\quad(\{a,c\},-),\quad(\{b,c\},-)
\]
have the same value by (Q(x,y)=Q(x,-x-y)=Q(y,-x-y)). For (c=2a\in V), the two distinct labels are
\[
(\{a,a\},+),\quad(\{a,2a\},-).
\]
A plus label fixes its possible third magnitude as (a+b), and a minus label with distinct magnitudes fixes it as (|a-b|). A minus diagonal label has missing third magnitude zero, which is not in (U). Therefore no label lies in two distinct completion blocks. Their displayed sizes give the theorem. ∎

## 2. A sharp limit on this completion certificate

Order (V=\{v_1<\cdots<v_r\}). For a sum equal to (v_j), its first summand has at most (j-1) choices, and the second is then fixed. Therefore
\[
P(V)\le\sum_{j=1}^r(j-1)=\frac{r(r-1)}2.
\]
Together with (1), this gives
\[
\boxed{\mathcal B(V)\ge\frac{r(r+3)}2.}
\tag{3}
\]
The bound on (P(V)) is sharp, attained by (V=\{a,2a,\ldots,ra\}), (a>0). These are its only equality cases. Indeed equality for every target (v_j) forces every smaller (v_i) to have a complement in the smaller prefix. Starting with (v_2=2v_1), induction gives (v_j=jv_1): the complement of (v_1) must be the largest earlier element.

The stronger statement about *uncompleted labels* is
\[
\begin{aligned}
\mathcal U(V)
&=r(r+1)-3T(V)-2D(V)\\
&=r(r+1)-\frac{3P(V)+D(V)}2\\
&\ge\frac{r^2+5r+2}{4},
\end{aligned}
\tag{4}
\]
where (D(V)\le r-1), because the largest positive element has no double in (V).

There is also an exact ordered-pair closure formula:
\[
\#\{(x,y)\in U^2:x+y\in U\}=6P(V)\le3r(r-1).
\tag{5}
\]
For each positive ordered representation of a sum, the two simultaneous signs and the two orientations of each mixed-sign difference give the six contributions; the formula remains valid for equal summands. Hence a finite symmetric nonzero set always misses at least (r^2+3r) of its (4r^2) ordered additive completions.

These results have a precise scope. If the root class has (r=n-o(n)) input indices, a certificate which identifies outputs only by completing zero-sum triples leaves at least ((1/2+o(1))n^2) completion blocks. It therefore cannot by itself establish an (o(n^2)) root image. This does **not** prove an (\Omega(n^2)) lower bound for that image. A successful cover has to identify different completion blocks with one another. Even if every completed-triangle output were somehow compressed to one value, (4) leaves quadratically many uncompleted labels requiring further identifications.

The weaker informal condition “one of the sum or difference is a root” does not handle both signed branches. For example, in (V=\{1,\ldots,r\}), every unequal pair has its positive difference in (V), but a large collection of plus labels still has no completion. Equations (1)–(4) account for this distinction directly.

## 3. Exact bridge from root triangles to old labels

Suppose (C+a=\gamma u_a^2), with (gamma>0), and let three signed roots (u,v,w\in U) satisfy (u+v+w=0). Set
\[
a=\gamma u^2-C,\quad b=\gamma v^2-C,\quad c=\gamma w^2-C,
\qquad S=a+b+c.
\]
The identity (u^2+v^2+w^2=2Q(u,v)) gives
\[
\boxed{\gamma Q(u,v)=\frac{3C+S}{2}.}
\tag{6}
\]
Thus root triangles lead directly to the old-label **triple-sum set**, rather than directly to the old (Q)-image.

More precisely,
\[
(3C+S)^2
=4\big((C+a)(C+b)+(C+a)(C+c)+(C+b)(C+c)\big),
\]
so, with (P=ab+ac+bc),
\[
P=\frac{S^2-2CS-3C^2}{4}.
\]
It follows that
\[
\boxed{
Q(a,b)=\frac34S^2+\frac C2S+\frac34C^2-Sc.
}
\tag{7}
\]
This displays the missing datum: an old pair norm still depends on the chosen third old label (c), not just on the root triangle output (S). In the special case (S=0), every old edge has norm (3C^2/4), exactly the already frozen one-old-fiber transfer situation. Its (O(n)) capacity is not an asymptotic solution.

Let (H_C(B)) be the set of such sums (a+b+c), allowing repeated old labels when the root triangle has a repeated magnitude. The outputs arising from completed triangles are exactly
\[
\frac{3C+H_C(B)}2.
\]
Therefore a direct, correctly scoped upper bound is
\[
\boxed{
|\gamma Q(U,U)|\le |H_C(B)|+\mathcal U(V).
}
\tag{8}
\]
The second term in (8) is unavoidable for this particular certificate; a new cover of the uncompleted labels is essential.

If a fixed positive scale (\lambda) is inserted only in the third root, it does not preserve the triangle identity. In fact
\[
Q(u,-\lambda(u+v))-Q(u,v)
=(\lambda-1)(u+v)(\lambda u+(\lambda+1)v).
\tag{9}
\]
For (u,v,\lambda>0), this vanishes only when (\lambda=1). A scaled-completion mechanism therefore needs a separate image identity; it cannot use zero-sum equality unchanged.

## 4. Certified finite root classes

Use the frozen optimizing parameters at levels (m=1,2,3). The largest input square classes and convenient exact root representatives are:

| (m) | (C_m) | Input class (B) | (gamma) | Positive root set (V) | (P(V)) | Completion blocks | Actual class image size |
|---:|---:|---|---:|---|---:|---:|---:|
| 1 | (5/2) | ({-2,2}) | (1/2) | ({1,3}) | 0 | 6 | 6 |
| 2 | (4) | ({-3,-1,3}) | (1) | ({1,sqrt3,sqrt7}) | 0 | 12 | 11 |
| 3 | (3) | ({-1,1,-sqrt5,sqrt5}) | (1) | ({2,sqrt2,(sqrt{10}-sqrt2)/2,(sqrt{10}+sqrt2)/2}) | 2 | 18 | 17 |

The field membership and maximality of these classes are frozen certified results, not inferred from the displayed roots. Their positive root representatives above are explicitly in the stated input fields.

At (m=2), the root set is literally a subset of (mathcal A_2). Hence this particular class has the exact one-copy cover
\[
Q(U,U)\subseteq Q(\mathcal A_2,\mathcal A_2).
\tag{10}
\]
This is a finite cover with five exceptional input labels out of eight; it supplies no uniform asymptotic exceptional bound. Its non-triangular coincidence is (Q(1,1)=Q(sqrt3,-sqrt3)=3).

At (m=3), write
\[
p=\frac{\sqrt{10}-\sqrt2}{2},\quad q=\sqrt2,
\quad r=\frac{\sqrt{10}+\sqrt2}{2}.
\]
The sole positive additive relation is (p+q=r). There are no others: linear independence of (1,sqrt2,sqrt{10}) excludes participation of the rational root (2), and comparison of the two irrational coefficients lists exactly this relation among (p,q,r). This gives one three-label triangle block. Its norm is
\[
Q(p,q)=Q(p,-r)=Q(q,-r)=4.
\]
The extra coincidence is
\[
Q(2,-2)=4.
\tag{11}
\]
Thus the frozen four-label output component at value (4) consists of one completed triangle block joined to one previously uncompleted diagonal block. This is an exact example of the additional type of identification that triangle closure alone misses.

## 5. Completion accounting on the entire certified adaptive sets

Common positive scaling preserves all additive-completion counts. Applying the same analysis to the full sets gives:

| Actual set | Positive magnitudes (r) | (P(V)) | Completion blocks (r(r+1)-P(V)) | Frozen (Q)-image size | Additional rank between completion blocks |
|---|---:|---:|---:|---:|---:|
| (mathcal A_0) | 1 | 0 | 2 | 2 | 0 |
| (mathcal A_1) | 2 | 1 | 5 | 5 | 0 |
| (mathcal A_2) | 4 | 0 | 20 | 17 | 3 |
| (mathcal A_3) | 8 | 0 | 72 | 68 | 4 |
| (mathcal A_4) | 16 | 2 | 270 | 269 | 1 |

Here are exact checks of the additive counts, independently of any decimal approximations.

- (mathcal A_1={pm1,pm2}) has the unique positive doubling relation (1+1=2).
- The positive magnitudes of (mathcal A_2) are (1,sqrt3,sqrt7,3). Linear independence of (1,sqrt3,sqrt7) over (mathbb Q) excludes every three-term relation except purely rational possibilities, and neither (1+1=2) nor a sum involving (3) gives a magnitude in that list.
- View (mathcal A_3) over (F_2=mathbb Q(sqrt3,sqrt7)). The frozen (4+mathcal A_2) square classes partition its positive roots into ({1,sqrt3,sqrt7}), ({g,h}), and three singletons, where (g=sqrt{4+sqrt7}), (h=sqrt{4-sqrt7}). Roots from different square classes are linearly independent over (F_2). Within the first class, independence of (1,sqrt3,sqrt7) excludes additive triples. In the two-element class a triple would require (g=2h), which after squaring would force (sqrt7=12/5). The singletons cannot contain a positive additive triple. Therefore (P=0).
- Up to one common scaling, (mathcal A_4) has positive roots (sqrt{3+a}), (ainmathcal A_3). The frozen classes have sizes (4,2,2,1,ldots,1). Roots from distinct classes are linearly independent over (F_3), so each three-term additive relation lies in a single class. The size-four class has exactly the relation described in Section 4. A size-two class with radicands (3pm x), for (x=sqrt3) or (sqrt7), would require (3+x=4(3-x)), hence (x=9/5), which is false. Singletons have none. Hence (P=2).

**Assumed standard theorem used in these checks.** For a characteristic-zero field (F), adjoining square roots whose classes span an (s)-dimensional subgroup of (F^	imes/F^{	imes2}) produces a degree-(2^s) extension. The square-root monomials for a basis form an (F)-basis. In particular square roots of distinct square classes are linearly independent over (F), even when the collection of classes is multiplicatively dependent. This exact version is sufficient for the three-term separation above.

No new parameter for (mathcal A_4) is claimed. The last table concerns the already certified set (mathcal A_4), not a fifth adaptive step.

## 6. Consequence for the constructive search

The finite identities (10) and (11) are exact. They do not provide a parameter rule or a root-image coefficient below four uniformly in the adaptive level. Ordinary zero-sum completion, even at its sharp extremum, leaves quadratically many completion blocks and quadratically many uncompleted labels. Thus a successful continuation must control norm values of distinct completion blocks directly.

This missing compression can itself be measured without energy. Define the exact inter-block identification rank
\[
J(V)=\mathcal B(V)-|Q(U,U)|\ge0.
\]
For any proposed coefficient \(\rho<4\) and error \(E\), the desired direct root-image estimate is equivalent to
\[
\boxed{J(V)\ge r(r+1)-P(V)-\rho s-E.}
\tag{12}
\]
In particular it requires
\[
J(V)\ge\frac{r(r+3)}2-\rho s-E.
\tag{13}
\]
If \(r=n-o(n)\), \(s=o(n^2)\), and \(E=o(n^2)\), this is at least \((1/2-o(1))n^2\). The finite ranks in the last table are \(0,0,3,4,1\); no growth law for them is inferred. Equation (12) is an exact quantitative target concerning identifications of distinct triangle blocks, rather than an assertion that a large average collision count is sufficient.

One can permit affine, Möbius, or other fixed single-valued maps of the old output set without altering the elementary cardinality threshold: three everywhere-defined images still have total size at most (3s_m). A Möbius map with a pole is used only on its pole-free old outputs, and its image still has size at most (s_m). What is missing is exact simultaneous coverage, not the choice of notation for the maps. Identity (7) prevents treating the completed-triangle trace as automatically a function of a single old pair norm.

The narrowly unresolved constructive statement from this mechanism is: for actual adaptive inputs, find a legal in-field comparison parameter, a root class with (O(n^{1-delta})) exceptions, and a direct cover of the norms of *all completion blocks*, including the uncompleted singleton blocks, by fewer than four old-image copies up to (O(n^{2-delta})) additional values. Equations (6)–(8) give an exact formulation for its completed-triangle part; (4) quantifies the uncompleted part that cannot be discarded. No such uniform cover, and consequently no positive target exponent, has been proved in this note.
