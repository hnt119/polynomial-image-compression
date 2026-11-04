# Phase C0 claim ledger

| ID | Claim | Hypotheses / dependencies | Proof or source | Status | Referee resolution |
|---|---|---|---|---|---|
| CL1 | Tower with `d_j -> infinity`, `t=floor((ell-1)^2/100)` fixed split primes, and `log D=O(ell log ell)` | Fixed sufficiently large `ell` | Supplied unit-distance proof, Proposition 3.8, PDF pp. 12-14 | PROVED FROM SUPPLIED SOURCES | Passed; no prescribed-prime strengthening used |
| CL2 | Unique common-scaling quadratic deformation `P_2+Q P_1+Q^2 P_0` | Quadratic `P`, nonzero `Q` | Report Lemma 4.1; Role A A1 | PROVED HERE | Passed |
| CL3 | For primitive `L`, `L^2+QM mod p` has exactly `(p+1)/2` values at every odd `p|Q` | `gcd(a,b)=1` | Report Lemma 4.3; Role B B2-B3 | PROVED HERE | Passed, zero and `p=2` handled |
| CL4 | Rank-one binary quadratics have half-density; rank-two forms are surjective | Odd finite field | Report Lemma 4.2; Roles A/B | PROVED HERE | Passed |
| CL5 | CRT gives at most `(rho Q)^d` allowed classes | Squarefree `Q`; every factor completely split | Report Section 6, Step 1 | STANDARD FACT + PROVED HERE | Passed; no probabilistic independence |
| CL6 | Centered carrier bounds `(X/sqrt D)^d <= |B_K(X)| <= (2X+1)^d` | Totally real `K`, root discriminant at most `D` | Report Lemma 5.2; frozen Phase A Section 4.1 | PROVED HERE FROM STANDARD FACTS | Passed; translated-half-box correction explicit |
| CL7 | Every class mod `Q O_K` has at most `(2M/Q+1)^d` points in `B_K(M)` | Integral modulus `Q` | Report Lemma 5.3 | PROVED HERE | Passed; worst-case class bound |
| CL8 | Explicit output radius `M=9X^2+4QX` | Explicit `P_Q`, centered carrier | Report Section 6, Step 2 | PROVED HERE | Passed at every conjugate |
| CL9 | Full support is at most `[rho(2M+Q)]^d` | CL5, CL7, CL8 | Report Section 6, Step 3 | PROVED HERE | Passed; covers light fibers |
| CL10 | One fixed `ell` makes `27D rho<1` | CL1 and selected primes `p_i == 1 mod 4` | Report Lemma 5.1; Roles C/D | PROVED HERE | Passed; joint `D(ell)` dependence charged |
| CL11 | Same-set transport preserves cardinalities | `P_Q(Qx,Qy)=Q^2P`, injective real embedding | Report Section 6, Step 4 | PROVED HERE | Passed; one map in both inputs, fibers one |
| CL12 | `epsilon=-log theta/log(2X+1)` gives the exact target | `theta<1`, carrier upper bound | Report Section 6, Step 5 | PROVED HERE | Passed; upper bound used in correct direction |
| CL13 | `P_*` is outside additive and multiplicative forms | Both square-direction coefficients nonzero; transverse linear part | Report Lemma 4.4 | PROVED HERE | Passed after complete degree split |
| CL14 | `P_*` is not the supplied example under same-input affine transport, output affine map, or swap | Specified equivalence only | Report Section 1; Role A A4b | PROVED HERE | Passed with scope limitation |
| CL15 | Theorem C1 for all primitive transverse `L^2+M` with `ab != 0` | CL1-CL13; fixed member | Report Theorem C1 and Section 6 | PROVED WITHIN OFFLINE SOURCE SYSTEM | Passed; exponent member-dependent |
| CL16 | Quartic symmetric-box factor exceeds one for all `X>0` | C2 deformation and supplied split primes | Report Section 10; Role D Section 7 | PROVED HERE - ROUTE FAILED | Passed; conjecture not refuted |
| CL17 | `|{x^2+3y^2 mod 3^k}|=(3^k+1)/2` | `k>=1` | Report Section 10; Role A Lemma A5 | PROVED HERE | Passed as partial local theorem; global route fails |

No load-bearing claim remains assumed or open in Theorem C1.
