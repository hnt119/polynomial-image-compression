# Phase C1 review and next steps

## Verdict

The main C1 partial theorems appear sound on review. The corrected C0 quadratic family remains established within the supplied source system. C1 does not prove or disprove compression for

\[
P_4(x,y)=(x+2y)^4+3x-y.
\]

C1 makes useful progress by identifying the limits of two explicit counting methods. Its proposed next-step statements need adjustment: the weak M1-DEFICIT assertion is already an elementary consequence of its own bounds, and its proposed M2-CORR test at \(p=5,d=2\) also has a short proof.

This review uses the submitted C1 report, corrected C0 proof, correction log, claim ledger, referee report, source manifest, and computation script. The relevant C1 PDF pages were also inspected. External novelty has not been checked. The uploaded script was inspected; finite experiments are not needed for the deductions below.

## What C1 establishes

1. The corrected C0 proof consistently uses the totally real source fields and retains its fixed-polynomial, same-set conclusion.
2. The quartic's continuous image interval on a centered square is computed exactly. Replacing the earlier loose radius with that interval still leaves the specified certificate above the trivial pair count.
3. The transverse-width lemma holds uniformly over translated intervals. Combining its two slices with norm-separation packing rules out the stated interval-and-class certificate for arbitrary centers and unequal coordinate widths.
4. The local theorem
   \[
   \frac{p\,|(E+2E)^4|}{|E|^2}\ge\frac{p+3}{4p}
   \]
   correctly shows that independent coordinate restrictions do not improve the local factor after charging the input density twice. Equality requires full input in that coordinate.

These are bounds on the performance of specified upper-bound methods. They do not show that the actual polynomial image has quadratic size. In particular, the size of the ambient container is not the number of realized values.

## Correction 1: M1-DEFICIT is already proved in its weak form

The statement in C1 Section 6.6 asks for some fixed common radius \(r\), dense-center carriers \(C_j\), and \(\eta>0\) such that each occupied class contains at most

\[
e^{-\eta d_j}
\prod_{i=1}^{d_j}\left(1+\frac{W_Q(c_{i,j},r)}Q\right)
\]

realized outputs. No threshold relative to the negative compression rate is imposed in that weak statement.

Choose any fixed \(r>\max\{Q,\sqrt D\}\). The dense-center construction in Section 6.2 produces unbounded carriers and gives

\[
|C_j|\le(2r+1)^{d_j}.
\]

The proved width lemma gives, uniformly in the centers,

\[
1+\frac{W_Q(c_{i,j},r)}Q
\ge b:=1+\frac{(7r/3)^4}{Q}.
\]

Since \(r>Q\ge5\),

\[
\frac{(7r/3)^4}{Q}
=\left(\frac73\right)^4\frac{r^2}{Q}\,r^2
>9r^2\ge(2r+1)^2.
\]

Consequently

\[
\eta:=\log\frac{b}{(2r+1)^2}>0.
\]

For every residue class \(\omega\), the trivial pair bound now gives

\[
\begin{aligned}
|F_Q(C_j,C_j)\cap(\omega+Q\mathcal O_{F_j})|
&\le |C_j|^2\\
&\le(2r+1)^{2d_j}\\
&=e^{-\eta d_j}b^{d_j}\\
&\le e^{-\eta d_j}
\prod_i\left(1+\frac{W_Q(c_{i,j},r)}Q\right).
\end{aligned}
\]

This proves precisely the weak existential statement. No explicit tower layers or enumeration are required.

**Recommended status:** `PROVED — elementary consequence of the pair bound; insufficient for compression`. Its proof demonstrates that a positive deficit relative to a very large container is not, by itself, evidence of a useful saving.

## Correction 2: M2-CORR at p = 5, d = 2 needs no exhaustive search

Let \(G=\mathbb F_5^2\), let \(S\subseteq G\) be nonempty, and write \(n=|S|\). The proposed inequality becomes

\[
\frac{25|H_5(S)|}{n^2}\ge\left(\frac25\right)^2=\frac4{25}.
\]

If \(n\le12\), then \(|H_5(S)|\ge1\), so

\[
\frac{25|H_5(S)|}{n^2}\ge\frac{25}{144}>\frac4{25}.
\]

If \(n\ge13\), then for every \(z\in G\), the sets \(S\) and \(z-2S\) each have at least 13 elements in a group of order 25. They intersect. Thus

\[
S+2S=G.
\]

Coordinatewise fourth powering maps \(G\) onto \(\{0,1\}^2\), which has four elements. Therefore

\[
|H_5(S)|=4,
\qquad
\frac{25|H_5(S)|}{n^2}=\frac{100}{n^2}\ge\frac4{25}.
\]

Equality occurs only for \(n=25\), hence only for \(S=G\).

This proves the entire suggested finite test analytically. It does not settle M2-CORR for general \(p,d\). Larger cases must be screened for equally simple arguments before allocating an exhaustive search.

## How to interpret QCLASS-DEFICIT

Section 9 gives a valid sufficient implication: a uniform realized-output deficit stronger than \(\log\Theta_{4,\mathrm{int}}(X)\) would imply the target on the chosen carrier. Its feasibility calculation excludes the elementary contradiction that a nonempty class would be bounded by less than one.

That feasibility condition is not evidence that the estimate holds. The statement contains the main unproved compression claim in a stronger, uniform-per-class form. It is useful as a quantitative target, but does not yet provide a mechanism for reaching it.

A successful total-support estimate need not bound every class equally well. It could bound the sum over classes, separate exceptional classes, or prove an explicit representation of all outputs through a smaller parameter set. Such alternatives still must control the full support.

Also make the quantifiers explicit: a counterexample for one fixed radius and tower can reject a universal version of the deficit claim. It does not rule out the existence of another fixed radius or tower that works.

## Recommended continuation

Preserve the corrected C0 theorem and the main C1 obstruction results. Update the roadmap with the two elementary corollaries above. Do not spend the next run on the weak deficit statement, the \(p=5,d=2\) enumeration, or further optimization of a counting method already covered by the obstruction.

The next research task should specify a source of additional support structure before asking for another deficit estimate. One concrete remaining model from the C1 prompt is

\[
C_j=G_jT_j,
\]

with a precisely defined set of units \(G_j\) and additive carrier \(T_j\). It was not one of the two sustained C1 models. A bounded first task would be to expand

\[
F_Q(g_1t_1,g_2t_2),
\]

identify an exact correlated intermediate support, and calculate whether a stated compression lemma for that support could beat every input, distortion, modulus, and multiplicity cost. This is a proposed test, not a claim that the model is promising or sufficient.

A different selected model is acceptable if it names the additional structure and gives equally explicit counting obligations. A favorable correlated residue pattern alone cannot rescue the unchanged full-interval packing bound: C1 already shows that even one class has excessive ambient capacity. It must be paired with a sharper account of which values are realized.

Use a short stopping rule: require either a proved intermediate lemma that supplies a quantifiable new gain, or a precise explanation of why the chosen model cannot supply it. If neither structural route has a credible rate, reconsider the target polynomial or mechanism instead of producing another reformulation of the desired inequality.
