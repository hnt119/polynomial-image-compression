# Phase C2 claim ledger

## Status key

- **SOURCE INPUT:** stated in an inspected supplied source.
- **PROVED:** proved in the Phase C2 report from stated hypotheses.
- **PROVED ALGEBRAIC REFINEMENT:** exact new relation, but without a positive
  final-output rate.
- **USEFUL STRUCTURAL LEMMA PROVED:** a quantified, full-support improvement
  is proved, although it need not close the final target rate.
- **SCOPED OBSTRUCTION:** a specified counting route cannot certify a saving;
  this is not an image lower bound.
- **CONDITIONAL RATE SCREEN:** a proved implication whose unproved hypothesis
  is not counted as a milestone.
- **CONJECTURAL:** a proposed general assertion not proved here.
- **UNRESOLVED:** not proved or disproved.

## Claims

| ID | Claim | Hypotheses and dependencies | Locator | Status |
|---|---|---|---|---|
| C2-01 | The corrected Phase C0 quadratic family theorem retains its existing same-input, fixed-polynomial scope | Corrected C0 proof and C1 referee report | Main report Section 1 | PROVED WITHIN THE OFFLINE SOURCE SYSTEM; PRESERVED |
| C2-02 | The C1 continuous quartic range, transverse-width theorem, and two stated certificate obstructions retain their scopes | C1 main report and referee report | Main report Sections 1 and 5.1 | PROVED / SCOPED CERTIFICATE OBSTRUCTIONS; PRESERVED |
| C2-03 | Weak M1-DEFICIT follows from the trivial pair bound for fixed \(r>\max\{Q,\sqrt{D}\}\) | C1 carrier upper bound and width theorem | `C1_STATUS_ADDENDUM.md`, Section 1 | PROVED - INSUFFICIENT FOR THE REQUIRED RATE |
| C2-04 | M2-CORR holds for \(p=5,d=2\), with equality only for the full set | Nonemptiness for \(|S|\le12\); intersection argument for \(|S|\ge13\) | `C1_STATUS_ADDENDUM.md`, Section 2 | PROVED FOR THIS FINITE CASE |
| C2-05 | General M2-CORR | C2-04 proves only the case \(p=5,d=2\) | Addendum Section 2 | CONJECTURAL |
| C2-06 | The source base \(F\) is cyclic cubic, its conductor includes 7, and the maximal unramified pro-3 group has the stated generator/relation bounds | Unit-distance proof, Propositions 3.2-3.5 and proof of Proposition 3.8 | Main report Sections 2-2.1 | SOURCE INPUT |
| C2-07 | Killing one Frobenius above 7 in addition to the source's \(3t\) Frattini Frobenii leaves an infinite pro-3 quotient for sufficiently large \(\ell\) | One-generator loss, one-relation cost, standard pro-\(p\) primitive-generator elimination in the non-Frattini case, explicit Golod-Shafarevich inequality | Main report Section 2.1 | PROVED |
| C2-08 | In the refined layers, the source-selected \(q_b\) and the unique base prime above 7 split completely relative to \(F\); the layers remain totally real with fixed root discriminant | C2-07 and the source tower extraction | Main report Section 2.1 | PROVED |
| C2-09 | \(7\mathcal O_{F_j}=\prod_{k=1}^{d_j/3}\mathfrak P_{j,k}^3\), with residue field \(\mathbb F_7\) at every factor | Total ramification in the cubic base and complete relative splitting | Main report Section 2.1 | PROVED |
| C2-10 | Phase A's additive count, unit count, separation lemma, distortion bounds, and \(R_F\le\Delta_F\) apply field-locally to the same refined \(F_j\) | Totally real \(F_j\), \(d_j\ge2\) | Main report Sections 2-3 | SOURCE INPUT APPLIED WITH VERIFIED HYPOTHESES |
| C2-11 | For \(G_j=\{h^2:h\in B_{F_j}^\times(Y/2)\}\), the square map has fibers exactly two, every element of \(G_j\) is totally positive, and the displayed unit/product/quotient bounds hold | \(Y\ge2\); Phase A unit count | Main report Sections 3.1-3.2 | PROVED |
| C2-12 | The additive carrier \(T_j=X+B_{F_j}^+(\tau X)\) is totally positive and has the displayed centered-box count | \(0<\tau<1\), \(\tau X\ge1\) | Main report Sections 3.1-3.2 | PROVED FROM SOURCE INPUT |
| C2-13 | \(G_j\times T_j\to C_j\) is injective, so \(\mu_j=1\), \(|C_j|=|G_j||T_j|\), and the lower/upper rates are \(a,B\) | \(\tau<\sqrt{5}-2\); unit separation | Main report Section 3.3 | PROVED |
| C2-14 | The seven-monomial expansion of \(F_Q(g_1t_1,g_2t_2)\) is exact | Binomial theorem | Main report Section 4 | PROVED |
| C2-15 | The ratio change of variables preserves admissibility, satisfies \(\sum_u|G(u)|=|G|^2\), and gives the exact union \(F_Q(C,C)=\bigcup_u\mathcal S_u\) | Definitions and exact substitution | Main report Section 4.1 | PROVED |
| C2-16 | The map \(T^2\to\mathcal K_u\) is injective for totally positive \(u,T\), hence \(|\mathcal K_u|=|T|^2\) | Determinant \(-7u\ne0\), positivity, total reality | Theorem C2.1 | PROVED |
| C2-17 | For fixed \((\alpha,\beta)\in\mathcal K_u\), common-action fibers have size at most four, so the image over \(G(u)\) has size at least \(|G(u)|/4\) | \(\alpha\ne0\) | Theorem C2.1 | PROVED; LOWER-BOUND DIAGNOSTIC ONLY |
| C2-18 | Elementary parameter counting on the exact ratio decomposition yields exactly \(|C|^2\) and no strict exponential gain | C2-13, C2-15, C2-16 | Theorem C2.1 | SCOPED OBSTRUCTION |
| C2-19 | Multiplying the marginal supports \((C+2C)^4\) and \(3C-C\) cannot certify a saving because their product is at least \(|C|^2\) | Total positivity and determinant \(-7\) | Main report Section 5.2 | SCOPED OBSTRUCTION |
| C2-20 | The integral image of \((t_1,t_2)\mapsto(ut_1+2t_2,3ut_1-t_2)\) is exactly \(a+2b\in7\mathcal O\), and outputs satisfy \(F_Q\equiv2z^4+Q^3z\pmod7\) | \(u\in\mathcal O^\times\) | Lemma C2.2 | PROVED ALGEBRAIC REFINEMENT |
| C2-21 | On \(\mathbb F_7[\pi]/(\pi^3)\), each map \(2z^4\pm z\) has exactly 208 values | Taylor expansion, four regular and three critical residue branches | Theorem C2.3 | PROVED |
| C2-22 | The complete quartic image occupies at most \(208^{d_j/3}(\rho_4Q)^{d_j}\) residue classes modulo \(7Q\mathcal O_{F_j}\); this is a bound on their total number | C2-08, C2-09, C2-20, C2-21, CRT, split-prime fourth powers | Main report Section 5.3 | PROVED FULL-SUPPORT CLASS BOUND |
| C2-23 | The determinant-seven restriction supplies the positive per-degree gain \(s_7=\frac13\log(343/208)\) | C2-21 and C2-22 | Main report Section 5.3 | USEFUL STRUCTURAL LEMMA PROVED |
| C2-24 | Modulus 7 alone, and separately the combined modulus \(7Q\), remain worse than the pair budget under full continuous-interval packing | C1 width theorem and \(|C_j|\le(2r+1)^{d_j}\) | Main report Section 6.1 | SCOPED CERTIFICATE OBSTRUCTION |
| C2-25 | The squared-unit quotient rate \(\Lambda_G=\log[Y^2/(4D^2(5Y+1))]\) is positive above the displayed exact threshold | C2-10, C2-11 | Main report Section 6.2 | PROVED |
| C2-26 | A uniform estimate \(|\mathcal S_u|\le e^{\chi d+o(d)}|G(u)|^\theta|T|^2\) would have net rate at least \((1-\theta)\Lambda_G-\chi-2m\) | Concavity and C2-15 | Main report Section 6.2 | CONDITIONAL RATE SCREEN |
| C2-27 | The elementary ratio estimates give \(\theta=1,\chi=0,m=0\); the elementary ratio certificate proves no positive gain, so set \(\kappa_{\mathrm{cert}}=0\) | C2-13, C2-16, C2-18; this does not determine the actual image exponent | Main report Section 6.2 | PROVED NO-GAIN CALCULATION FOR THIS CERTIFICATE |
| C2-28 | Status of the fixed-quartic compression target | The local gain is insufficient for interval packing, and no sharper full-support overlap theorem was proved | Main report Section 8 | UNRESOLVED |

## Interpretation rule

Claims C2-18, C2-19, and C2-24 concern specified upper-bound methods. They do
not assert that the actual image has quadratic size. In particular, C2-18
does not rule out overlaps across distinct points of \(\mathcal K_u\), or
across different ratios. Claim C2-22 bounds the total number of occupied
residue classes; it does not bound the population of an individual class
and asserts neither equidistribution nor carrier surjectivity. Claim C2-26
is a rate test, not a proved support estimate.

External novelty and literature status have not been checked.
