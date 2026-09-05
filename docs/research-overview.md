# Research overview

This project studies how small the image of a fixed two-variable polynomial can be on a large Cartesian square. Its working targets are a quartic extension of a reported quadratic construction and a separate proposed direction involving nonsingular quadratic forms.

This page retains the initial C0–C2 mechanism overview. The owner's **four recent
directions**, including the two distinct cubic targets and later Eisenstein
Cartesianization work, are now recorded in [the project history](../research/PROJECT_HISTORY.md).

This page organizes the supplied research record. Its main sources are the three phase prompts, the C1 review, and the nonsingular-quadratic conjecture note linked below. It does not report a new proof search or a literature review. The archived phase prompts describe earlier or proposed assignments; their requested deliverables are not evidence that those assignments were completed.

## The question and its quantifiers

For a finite set $A\subset\mathbb R$, write

$$
P(A,A)=\{P(a,b):a,b\in A\}.
$$

For a fixed polynomial $P$, the target is

$$
\exists\varepsilon_P>0\quad\forall N_0\ge1\quad
\exists A\subset\mathbb R\text{ finite}:\quad
|A|\ge N_0,\qquad |P(A,A)|\le |A|^{2-\varepsilon_P}.
$$

The polynomial, its coefficients, and the positive exponent stay fixed as the sets grow. The same set appears in both inputs. An unbounded sequence of cardinalities suffices; the claim does not require every cardinality or every finite set to work. A family statement may allow the exponent to depend on its fixed member.

The motivating search seeks examples beyond the additive and multiplicative special forms $g(u(x)+v(y))$ and $g(u(x)v(y))$, with univariate real polynomials $g,u,v$. Any claimed exclusion from those forms requires its own proof. See the [C0 search specification](../research/prompts/Phase_C0_Conjecture_Proof_Search_Prompt.md).

## Status at a glance

| Claim | Status supported by the archived record |
| --- | --- |
| C0 quadratic family | Reported as established within the supplied source system by the C1 review and later prompts. The original C0 PDF is now recovered; the complete corrected proof is still missing. |
| C1 interval and local-cost results | Reported as sound by the supplied review. Their full underlying C1 proof report is not among those five records. |
| Weak M1-DEFICIT | The review gives an elementary deduction from stated carrier and width estimates. The deficit is insufficient for the desired compression rate. |
| M2-CORR at $p=5,d=2$ | The review supplies a complete elementary proof, reproduced below. |
| Quartic compression and general M2-CORR | Unresolved in the supplied record. |
| C2 hybrid carrier | A proposed structural-lemma investigation; the archived C2 document is a prompt, not a result. |
| Eisenstein norm and broader nonsingular quadratics | Ultimate targets remain conjectural; later Cartesianization results and obstructions are recorded under T03 in the project history. |
| Split-prime generalization report | Additional historical report; its broader quadratic and classification claims have not been independently audited for this repository. |

External novelty and literature status have not been checked. “Unresolved” here describes the supplied project record, not an independently verified statement about the literature.

## C0: reported quadratic baseline

The [C1 prompt](../research/prompts/Phase_C1_Corrections_and_Higher_Degree_Proof_Search_Prompt.md) and [C1 review](../research/notes/Phase_C1_Review_and_Next_Steps.md) report the following family:

$$
P_2(x,y)=(ax+by)^2+cx+ey,
\qquad a,b,c,e\in\mathbb Z,
\qquad \gcd(a,b)=1,\quad ab(ae-bc)\ne0.
$$

For each fixed member, they report a member-dependent fixed power saving with the same-set quantifiers above. Their explicit example is $(x+2y)^2+3x-y$.

The described mechanism uses the deformation

$$
(P_2)_Q(x,y)=(ax+by)^2+Q(cx+ey),
\qquad (P_2)_Q(Qx,Qy)=Q^2P_2(x,y),
$$

square-value restrictions modulo selected split primes, totally real number fields of growing degree, and a uniform count of possible outputs within each residue class. The source dependence matters: selected primes must split in the same field family whose discriminants are controlled. The later prompts distinguish the totally real layers $F_j$ from the complex extensions $F_j(i)$.

This repository should not present that summary as a self-contained proof. Reconstructing the result requires the corrected C0 report, its source manifest and referee record, and the exact field-supply statements they use. The [roadmap](roadmap.md#1-complete-the-source-and-proof-record) tracks that gap.

The archive also includes a [split-prime generalization report](../research/reports/Polynomial_Image_Split_Prime_Generalization.pdf). Treat its conditional counting criterion and broader quadratic claims as historical source material. In particular, a criterion requiring a favorable rate and a compatible split-prime tower does not by itself establish an unconditional polynomial-family theorem. This overview does not independently audit that report's broader quadratic corollary or proper-power classification.

## C1: what the quartic obstruction means

The fixed target is

$$
P_4(x,y)=(x+2y)^4+3x-y.
$$

Its integral deformation is

$$
F_Q(x,y)=(x+2y)^4+Q^3(3x-y),
\qquad F_Q(Qx,Qy)=Q^4P_4(x,y).
$$

The [C1 review](../research/notes/Phase_C1_Review_and_Next_Steps.md) reports that sharpening the continuous output interval, translating input intervals, or allowing unequal coordinate widths still does not make the specified interval-and-residue-class packing certificate prove a saving. The [C2 prompt](../research/prompts/Phase_C2_Hybrid_Carrier_Structural_Lemma_Prompt.md) records a key width bound: for $I=[c-r,c+r]$, $c\in\mathbb R$, $r>0$, and integer $Q\ge5$, if $W_Q(c,r)$ denotes the width of $F_Q(I,I)$, then

$$
W_Q(c,r)+Q\ge Q(2r+1)^2.
$$

This concerns the size of a continuous container used by a counting method. It does not give a lower bound for the number of values actually realized on a finite algebraic carrier. Failure of that certificate neither disproves quartic compression nor rules out a sharper count on the same carrier.

The review also reports a local-cost theorem for a nonempty coordinate input $E\subseteq\mathbb F_p$, for the selected primes $p\equiv1\pmod4$:

$$
\frac{p\,|(E+2E)^4|}{|E|^2}\ge\frac{p+3}{4p},
$$

with equality only for full input $E=\mathbb F_p$. Here $(E+2E)^4=\{(x+2y)^4:x,y\in E\}$. Thus the specified independent coordinate restrictions do not improve the local factor once the input-density loss is charged twice. This does not settle arbitrary correlated restrictions across several coordinates.

## Two elementary corrections in the C1 review

### Weak M1-DEFICIT does not supply a useful rate

The review assumes the established carrier and width estimates and chooses a fixed $r>\max\{Q,\sqrt D\}$, where $D$ bounds the root discriminant. For the dense-center carriers it uses

$$
|C_j|\le(2r+1)^{d_j},\qquad
1+\frac{W_Q(c_{i,j},r)}Q\ge b:=1+\frac{(7r/3)^4}{Q}.
$$

Since $r>Q\ge5$, one has $b>(2r+1)^2$. Set $\eta=\log(b/(2r+1)^2)>0$. For every residue class $\omega+Q\mathcal O_{F_j}$, the trivial pair bound gives

$$
|F_Q(C_j,C_j)\cap(\omega+Q\mathcal O_{F_j})|
\le |C_j|^2
\le e^{-\eta d_j}
\prod_{i=1}^{d_j}\left(1+\frac{W_Q(c_{i,j},r)}Q\right).
$$

This verifies the weak deficit statement from the stated upstream estimates. It only shows that an oversized container is larger than the trivial pair count by an exponential factor. It supplies no saving below $|C_j|^2$. The complete short argument and its dependencies appear in [Correction 1 of the review](../research/notes/Phase_C1_Review_and_Next_Steps.md#correction-1-m1-deficit-is-already-proved-in-its-weak-form).

### M2-CORR at $p=5,d=2$ has a direct proof

Let $G=\mathbb F_5^2$ and let $S\subseteq G$ be nonempty, with $n=|S|$. Define

$$
H_5(S)=\{((x_1+2y_1)^4,(x_2+2y_2)^4):x,y\in S\}.
$$

Then

$$
\frac{25|H_5(S)|}{n^2}\ge\frac4{25},
$$

with equality exactly when $S=G$.

If $n\le12$, the image is nonempty, so the left side is at least $25/144>4/25$. If $n\ge13$, then for every $z\in G$ the two sets $S$ and $z-2S$ each have more than half of the 25 elements of $G$, hence intersect. Therefore $S+2S=G$. Coordinatewise fourth powering maps $G$ onto $\{0,1\}^2$, so $|H_5(S)|=4$. Now $100/n^2\ge4/25$, with equality only at $n=25$. See [Correction 2 of the review](../research/notes/Phase_C1_Review_and_Next_Steps.md#correction-2-m2-corr-at-p--5-d--2-needs-no-exhaustive-search).

This proves that finite case; it does not prove the general correlated finite-field assertion.

## C2: a proposed unit-times-additive carrier

The [C2 prompt](../research/prompts/Phase_C2_Hybrid_Carrier_Structural_Lemma_Prompt.md) proposes carriers $C_j=G_jT_j$ in totally real fields, where $G_j$ is a specified finite set of units and $T_j$ is an additive carrier. Its intended milestone is a proved structural lemma that reduces the count of realized outputs by a quantified amount.

For $u\in G/G$, the prompt defines

$$
G(u)=\{v\in G:uv\in G\},\qquad
\mathcal K_u=\{((ut_1+2t_2)^4,3ut_1-t_2):t_1,t_2\in T\},
$$

$$
\mathcal S_u=\{v^4\alpha+Q^3v\beta:
v\in G(u),\ (\alpha,\beta)\in\mathcal K_u\}.
$$

The proposed analysis uses the exact decomposition $F_Q(C,C)=\bigcup_{u\in G/G}\mathcal S_u$. Displaying this correlation is not itself a cardinality saving. A successful argument must count the entire union, charge the number of ratios and parametrization multiplicity, establish growth of the actual carrier, and account for unit distortion. Simply enclosing $C_j$ in another box returns to the C1 certificate obstruction.

## Proposed nonsingular quadratic direction

The [conjecture note](../research/conjectures/nonsingular_quadratic_compression_conjectures.tex) proposes the Eisenstein norm polynomial

$$
q_E(x,y)=x^2+xy+y^2
$$

as a separate test case with the same fixed-exponent, arbitrarily-large-set target. Its Hessian has determinant $3$, and for $\omega^2+\omega+1=0$,

$$
q_E(x,y)=N_{\mathbb Q(\omega)/\mathbb Q}(x-y\omega).
$$

The note then proposes extensions to nonspecial positive-definite rational binary quadratic forms, and ultimately to nonspecial rational quadratics whose quadratic part satisfies $4ac-b^2\ne0$. These are conjectural directions in this record, not consequences of the reported rank-one C0 family.

The note also contains literature descriptions, an interval-set asymptotic, and local-obstruction claims. Those supporting claims have not been independently verified for this repository and are not used here as proof inputs.

## Full support, collision energy, and the rate

A proof must upper-bound every realized value, including values with small fibers. If

$$
E_P(A)=\#\{(a,b,c,d)\in A^4:P(a,b)=P(c,d)\},
$$

then Cauchy–Schwarz gives

$$
|P(A,A)|\ge\frac{|A|^4}{E_P(A)}.
$$

This is a lower bound on the image. Large collision energy alone does not upper-bound its full support, and a small image on selected pairs does not control $A\times A$.

The shared rate template is: prove

$$
e^{ad-o(d)}\le|C_d|\le e^{Bd+o(d)},\qquad 0<a\le B,
\qquad |F(C_d,C_d)|\le e^{hd+o(d)}.
$$

After all restrictions, fibers, and counting costs are included, a positive $\kappa=2a-h$ gives a normalized saving $e^{-\kappa d+o(d)}$. With a valid same-set transport to the fixed polynomial, every fixed $0<\varepsilon<\kappa/B$ works for sufficiently large degrees. The input **upper** rate $B$ is needed for this conversion. A nonpositive rate rejects the stated bound as a certificate; it does not refute the target.
