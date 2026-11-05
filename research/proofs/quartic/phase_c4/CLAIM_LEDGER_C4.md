# Phase C4 claim ledger

All section references are to `Phase_C4_Higher_Ramified_Precision.md`.
The target is the fixed \(P_4(x,y)=(x+2y)^4+3x-y\).

| ID | Claim | Status and evidence |
|---|---|---|
| S1 | Actual source local cubic has e=3, f=1; the refined tower preserves its completions | Source input, from corrected C2 and frozen C3 tower arguments; Section 1 |
| S2 | Critical-coset input lower count and exact continuous width | Accepted C3 theorem, reused in Section 5 |
| L1 | Independent Cartesian coordinates and image saturation by \(\mathfrak p^4\) | PROVED support equality, Section 2; no characteristic-seven substitution at higher precision |
| L2 | Exactly 22 classes modulo \(\mathfrak p^4\) | PROVED analytically by actual DVR expansion, Section 3 |
| L3 | Exact support: three complete \(\mathfrak p^3\)-cosets and one complete \(\mathfrak p^4\)-coset | PROVED equality, including every cross-pair; Section 3 |
| L4 | \(N_1=4\), \(N_m=22\cdot7^{3m-4}\) for m>=2 | PROVED for all fixed m and all three full critical inverse-image families; Sections 3-4 |
| L5 | Local cost becomes 22/49, extra gain log(14/11)/3 | Exact two-input normalization; Section 4 |
| C1 | Exact integer checks in nine local twist/fiber combinations | COMPUTATIONAL CORROBORATION; code and results; Section 7 |
| C2 | Independent rerun gives byte-identical JSON | VERIFIED REPRODUCTION by independent referee; not a premise of L4 |
| G1 | Explicit growing carrier has a=log2 at fixed X | PROVED using S2; no fixed-box equidistribution assumption |
| G2 | \(\kappa_m=\log[X^2/(D(22/49)^{1/3}(W+7^m))]<0\) for m>=2 | SIGNED CERTIFICATE OBSTRUCTION; Section 5 |
| G3 | m2 is best among m>=2; improves the negative m1 estimate in the stated growth range | PROVED from exact formulas; Section 5 |
| G4 | Packing at the natural saturation ideal \(\mathfrak I^4\) still has negative rate | SCOPED OBSTRUCTION; Section 6.1 |
| G5 | The exact mixed-depth maximal-ball envelope has negative rate | SCOPED OBSTRUCTION including every branch; Section 6.2 |
| G6 | Volume-budget and actual-population comparisons are distinct | Explicitly separated in Section 6.3; actual-population claims require nontrivial equal-radius critical-coset carriers |
| G7 | Any 7-supported ideal-coset cover of the entire local product support fails full-interval uniform packing against actual population | PROVED SCOPED OBSTRUCTION; Section 6.4; full local support hypothesis essential |
| U1 | Optimal higher-level cost over arbitrary E_m subsets | NOT CLAIMED; the theorem concerns the requested full inverse images |
| U2 | Smaller finite realized residues or smaller real support within classes | UNRESOLVED; not excluded by G2-G7 |
| U3 | Fixed-quartic subquadratic same-input image | UNRESOLVED here; no actual-image lower bound proved |
| U4 | External novelty and literature priority | UNCHECKED; research was offline |

The universal modulus-7 theorem and its equality and second-minimum
classifications are frozen unchanged. The C2 wording corrections affect
precision and status labels, not their accepted mathematical results.

Retirement applies to the evaluated full-local-support/full-interval
uniform-packing route. No universal impossibility theorem for P4 is claimed.
