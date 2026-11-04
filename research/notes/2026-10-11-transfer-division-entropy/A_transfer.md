# A: quadratic baseline and a charged transfer gate

T01 / auxiliary rank-one quadratic baseline; 2026-10-11, version 1.
The target remains P(x,y)=(x-y)^3+x+y. F2 below is a different polynomial.
Status **PROVED relative to an identified EXTERNAL RESULT** means the counting
argument below was reconstructed and internally audited in this cycle, with
the supplied tower theorem retained as an external input. No novelty claim.

## A1. Source boundary and parameter order

The requested Pohoata, *Split primes and the Elekes–Ronyai problem*,
arXiv:2606.13619v2, Proposition 3.1 and Section 4, was **unavailable in the
searched local cache**. No statement or proof is attributed to those sections
as if inspected. This is an availability limitation, not a disproof.

The actual input inspected is
`local-only/migration/research_supplement/shared/03-unit-distance-proof.pdf`,
Proposition 3.8(P1)–(P4), pp. 12–14, and Remark 3.9.
Its version is identified by the source hash in README. The corrected
secondary use is `local-only/migration/research_supplement/shared/Phase_C0_Corrected.md`,
§§5–6; the 2026-09-10 T01 export §4.1 uses a different translated-box constant.
Those arguments are compatible; their constants must not be conflated.

**EXTERNAL RESULT — A-EXT.** For sufficiently large fixed ell, the supplied
theorem gives t=floor((ell-1)^2/100) distinct primes p_i=1 mod 4 and totally
real fields K_j, with d_j=[K_j:Q] tending to infinity, root discriminant
D=rd(K_j) independent of j, log D=O(ell log ell), and every p_i completely
split in every K_j. Its CM companions K_j(i) are not the input fields.

The source proof first chooses primes by Chebotarev in a finite extension,
then kills their Frobenius elements in an infinite pro-3 quotient, using a
Golod–Shafarevich relation bound. The latter step supplies simultaneous
splitting throughout the tower. Chebotarev alone does not. The source selects
its own primes, avoiding 3 and its ramified conductor primes. Arbitrary
preassigned primes or a newly constructed tower are not being asserted.
We inspected this assembly and statement, not independent proofs of all its
class-field, relation-rank and Golod–Shafarevich inputs.

Fix ell large enough that 13D(3/5)^t<1. Then fix the source primes and set

    M = product p_i,    rho = product (p_i+1)/(2p_i),
    theta = 13 D rho < 1.

Choose X >= max(M,2 sqrt(D),1), fixed before j varies. Only then let d_j
grow. The dependence of D on ell is paid before ell is fixed: t is quadratic
in ell whereas log D is O(ell log ell). No bound on the sizes of the selected
primes is needed for existence of a fixed positive exponent; their possibly
large product M increases the fixed X and reduces that exponent.

## A2. Complete counting proof

**PROVED — A-Q.** Let

    B_j = {alpha in O_(K_j): |sigma_i(alpha)| <= X for every real embedding},
    A_j = sigma_1(B_j)/M,    F2(x,y)=(x-y)^2+x+y.

The Minkowski lattice has covolume D^(d_j/2). Averaging translates of the
half-open cube [-X/2,X/2)^(d_j) supplies at least (X/sqrt(D))^(d_j)
lattice points in some translate. Subtract one such point. The resulting
distinct points lie in the centered cube defining B_j. Thus

    (X/sqrt(D))^d <= n=|A_j|=|B_j| <= (2X+1)^d.             (A.1)

For the upper bound, the difference of distinct algebraic integers has
nonzero integral norm, so one conjugate difference is at least 1 in
absolute value. Disjoint open cubes of side 1 centered on their Minkowski
images fit in a cube of side 2X+1. Boundary touching does not affect volume.
In particular n>=2^d tends to infinity. A single real field embedding and
division by fixed M are injective; there is no input projection loss.

For every ordered pair alpha,beta in B_j, form the algebraic integer

    G(alpha,beta)=(alpha-beta)^2+M(alpha+beta).

Exactly,

    M^2 F2(sigma_1(alpha)/M,sigma_1(beta)/M)=sigma_1(G(alpha,beta)).

Every conjugate of G has absolute value at most
S=4X^2+2MX. Modulo each selected odd split prime p,

    O_K/p O_K = F_p^d,    G = (alpha-beta)^2,
    O_K/M O_K = product_i F_(p_i)^d.

In one F_p coordinate the full possible square set, including zero, has
(p+1)/2 elements. Thus at most (M rho)^d residue classes can contain
outputs. This is exact finite-ring product factorization, not independence
of random residues, and it does not require B_j to fill these classes.
Prime 2 gives no square-density saving and is excluded. Ramified or
incompletely split primes cannot be treated as d copies of F_p; none is used.

For **each** class modulo M O_K, distinct representatives differ by M gamma
with gamma a nonzero algebraic integer. They are M-separated in sup norm.
Packing cubes of side M in [-S-M/2,S+M/2]^d bounds the population of every
class by

    (2S/M+1)^d.                                           (A.2)

It follows, without equidistribution or an average-class estimate, that

    |G(B_j,B_j)| <= [rho(2S+M)]^d
                 = [rho(8X^2+4MX+M)]^d
                 <= (13 rho X^2)^d <= theta^d n^2.        (A.3)

The last coarse constant uses M<=X and M<=X^2. The sharper signed output
interval could improve 13; it is not needed. All ordered pairs have been
covered by this container. There are no exceptional outputs.

Set c=-log(theta)/log(2X+1)>0. Equation (A.1) gives
d>=log n/log(2X+1), so theta^d<=n^(-c). Therefore

    |F2(A_j,A_j)| <= n^(2-c).                              (A.4)

Here the boundary exponent is valid because (A.1)–(A.3) are exact
inequalities with no subexponential errors. This verifies the requested
constant 13 and rescaling, conditional only on A-EXT as an external input.
It does not verify the unavailable Pohoata version or solve T01.

## A3. Reusable rate gate

**PROVED — A-GATE.** Suppose actual same-set inputs and their entire image
satisfy, for an increasing parameter d,

    ad-o(d) <= log n_d <= Bd+o(d),
    log |P(A_d,A_d)| <= bd+o(d),    a>0, B>0, b<2a.

Then every fixed 0<c<(2a-b)/B gives |P(A_d,A_d)|<=n_d^(2-c)
eventually. Indeed log(|image|/n_d^2)<=-(2a-b)d+o(d), and the upper
input bound converts this to a negative multiple of log n_d. A prefactor
may instead be retained in the target. Unknown costs cannot be assigned zero.

If an initial parameter count has rate a0, input thinning costs eta and
parameter-to-scalar fibers cost phi, use a=a0-eta-phi; the pair budget loses
2eta+2phi. If output classes have rate l and worst-case population has
rate u, their contribution is b=l+u. Separately bounded exceptional outputs
of rate e change this to max(l+u,e), with finite sums absorbed in o(d).
Growing chart inventories, covering degrees and carries belong in l or u,
not in an uncharged label count. If any rate is unproved, the application
is **CONDITIONAL**, even though this implication is proved.

For a finite ring R, E subset R and the actual reduced map F, record

    kappa(R,E,F) = |R| |F(E,E)| / |E|^2.                   (A.5)

This is output density divided by the square of input density. For a
genuinely proved product of coordinate restrictions, these factors multiply.
For correlated restrictions use the actual entire product ring and subset
in (A.5). Neither tensorization, a faithful real realization, nor the
appropriate lattice lower input count follows from (A.5) alone.

## A4. Imported cubic failure and the amount a replacement must save

**FAILED certificate / reported, formula locally checked.** The 2026-09-02
`research/history-sources/Cubic_Difference_Sum_Research_Checkpoint.md`,
executive verdict and §C, and 2026-09-10 T01 export §§6.1–6.3, retain this
specific cube-residue/full-interval population certificate:

    beta_p(X)=D delta_(p,2)[2 max(X,p^2/X)+p^2/X^2],
    delta_(p,2)=(p^2-p+3)/(3p^2),
    inf beta_p=D delta_(p,2)(2p+1).

For the selected good primes p=1 mod 12, p>=13, the last expression is
at least 1431D/169>8D. The bracket decreases to X=p from the left;
to the right its derivative is 2-2p^2/X^3>0. The displayed density
times (2p+1) increases for p>=13. These elementary minimizations were
checked here; the historical general prime-power/anisotropic proofs were
not rerun or broadened. The recorded CRT, correlated-code, algebraic-
denominator and exceptional-prime failures have the scopes in export §6,
not the scope of arbitrary sparse real carriers. A failed upper certificate
is not an actual-image lower bound.

Concretely, at the optimized one-prime setting, a new output improvement
g^d combined with an input loss exp(-eta d) needs

    g < exp(-2eta)/beta_p(p).

Equivalently its new saving rate must exceed log beta_p(p)+2eta. Reducing
the packing factor by that same amount is another way to meet the gate.
For p=13 and no thinning the multiplicative output improvement must be
strictly greater than 1431D/169 in reciprocal terms. This specifies the
additional gain needed within this ledger; no candidate producing it was
found or assumed. No prime sweep or tower construction ran.

## A5. Fully charged construction ledger

| Gain or cost | Quadratic baseline charge | Cubic transfer requirement |
|---|---|---|
| Input counts | a=log(X/sqrt D), B=log(2X+1) | Prove both for actual scalars |
| Input thinning, twice | 0: no thinning | Subtract twice its rate |
| Parameter fibers | 1: embedding and scaling injective | Prove and charge |
| Discriminant and degree | n lower count pays D^(d/2); d varies last | Never discard discriminant cost |
| Units, regulator, class number | Inapplicable: no unit carrier or ideal-class selection | Charge if used |
| Moduli and denominator | Fixed M; present in S and residue packing; scaling exact | Cubic clearing uses M^3 P(U/M,V/M)=(U-V)^3+M^2(U+V) |
| Heights and distortion | Coefficients 1; all embeddings bounded by X | Actual entire output bounds required |
| Local sparsity | rho^d, supplied complete splitting | New proved gain above failure base |
| Per-class population | (2S/M+1)^d, uniform | Must improve or pay full cost |
| Branches, ratios, carries | One container; no hidden branch/ratio/carry count | Count all labels and multiplicities |
| Exceptional pairs/outputs | 0: every pair lies in the container | Any exception contributes to b |
| Final output rate | b=log(13 rho X^2) | Must satisfy b<2a |
| Net gap | 2a-b=-log theta>0 | Unknown is not positive |

Claim record: A-EXT (external input inspected as stated), A-Q and A-GATE
(proved and separately checked internally), A4 (scoped historical failure
with minimization checked). All are version 1, 2026-10-11; the precise
quantifiers, hypotheses, locators, dependencies and remaining availability
gap are stated above. There is no external proof audit or literature claim.
