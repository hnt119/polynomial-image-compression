# C4 signed rate ledger — extraction from the accepted record

Date: 2026-09-10. This is a documentation extraction from `Phase_C4_Higher_Ramified_Precision.md`, Sections 5-6, and `agents/higher_rate.md`, Section 2. No new rate optimization or computation was performed.

All logarithms are natural. Set

\[
a=\log X-\tfrac13\log7-\tfrac12\log D,\quad
X=2\,7^{1/3}\sqrt D,\quad a=\log2,
\]
\[
W=81(X+1)^4+\tfrac32X+\tfrac{27}{16},\qquad C_*=(22/49)^{1/3}.
\]

These use the fixed critical-coset carrier, the actual fixed source root discriminant `D`, and a fixed radius before the tower degree tends to infinity.

## Rational-prime precision

\[
U_m=N_m^{d/3}(1+W/7^m)^d=e^{c_md},\qquad \kappa_m=2a-c_m.
\]

| Precision | Occupied classes per cubic factor | Exact signed rate | Uniform negative upper bound |
|---|---|---|---|
| `m=1` | `4` | \(\log[X^2/(D(4/7)^{1/3}(W+7))]\) | \(-\log[18\sqrt7D(4/7)^{1/3}]\) |
| `m>=2` | \(22\,7^{3m-4}\) | \(\log[X^2/(DC_*(W+7^m))]\) | \(-\log[18DC_*7^{m/2}]\) |

For `m>=2`,

\[
c_m=\tfrac13\log22-\tfrac43\log7+\log(W+7^m).
\]

The signed contributions are `+2 log X` for two input windows, `-(2/3) log 7` for both ideal restrictions, `-log D` for discriminant, `-(1/3) log Nm` for occupied classes, and `-log(1+W/7^m)` for per-class packing. Translation is included in `W`. No unit, regulator, sign-selection, multiplicity, or exceptional-output loss is hidden.

The exact difference is

\[
\kappa_2-\kappa_1=\tfrac13\log(14/11)+\log\frac{W+7}{W+49}.
\]

This is positive in the chosen growth range, but both rates remain negative. At fixed `X,D,W`, the rates strictly decrease for `m>=2`.

## Existing illustrative numerical table

The following values are copied from `agents/higher_rate.md`, Section 2. They use **only an illustrative floor** `D=7^(2/3)`, with the prescribed radius and `W=387884.61286169...`. No tower attaining this discriminant floor is asserted. The local checking script and JSON concern levels 1-3 and do not verify this numerical rate table; levels 4-6 here are existing formula/table entries.

| `m` | Exact local count `Nm` | Illustrative certificate rate |
|---:|---:|---:|
| 1 | 4 | -9.9983748415 |
| 2 | 1078 | -9.9180957610 |
| 3 | 369754 | -9.9188533356 |
| 4 | 126825622 | -9.9241403487 |
| 5 | 43501188346 | -9.9603868642 |
| 6 | 14920907602678 | -10.1828760674 |

## Sharper local-support covers

| Cover | Envelope / rate | Accepted obstruction |
|---|---|---|
| Saturation ideal \(\mathfrak I^4\) | \(U=22^{d/3}(1+W/7^{4/3})^d\) | \(\kappa\le-\log(18\,22^{1/3}D)<0\) |
| Exact mixed-depth cover, \(n=d/3\) | \(U_{\rm mix}=\sum_{k=0}^n\binom nk3^{n-k}(1+W/7^{1+k/d})^d\) | \(2a-c_{\rm mix}\le-\log[18\sqrt7D(3/7)^{1/3}]<0\) |
| Any finite 7-supported integral-ideal coset cover of the entire local product support | \(U_{\rm cover}=\sum_\ell(1+W/N(J_\ell)^{1/d})^d\) | For nontrivial equal-radius critical-coset carriers, \(U_{\rm cover}/\lvert C\rvert^2\ge[81\,22^{1/3}/64]^d>3.54^d\) |

For the same actual-population comparison, the exact mixed-depth envelope has ratio greater than `3.85^d`, and direct saturation-ideal packing has ratio greater than `4.24^d`. These are lower bounds on numerical envelopes, not lower bounds on the actual polynomial image.

**PROVED:** the displayed inequalities and their stated hypotheses, as established in the accepted reports. **FAILED:** these full-local-support/full-continuous-interval uniform-packing certificates as a route to a positive saving. **OPEN:** the actual same-input quartic compression target.
