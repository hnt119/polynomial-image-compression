# Independent audit of the HR-N1 separated-depth obstruction

**Date/version:** 16 September 2026, version 1.

**Disposition: PASS.** The proposed obstruction is valid. On every level
\(L=10m\), \(m\ge2\), a class containing at least \(|A_L|^2/200\)
ordered pairs has exactly one return, the identity, even under the entire
group \(\{u^rv^s:r,s\in\mathbb Z\}\). This disproves the frozen HR-N1
return-tail assertion. It does not establish an actual-image lower bound
for the two-prime carrier or disprove the underlying T03 target.

## Audit scope, sources and offline boundary

The parent proposed the separated-depth class and proof outline. A separate
agent independently checked the argument, including its local valuation
claims, signs, denominator recovery, both coordinate orderings, size bounds,
and quantifiers. The complete audit is recorded below. This is internal
proof review, not external certification or a novelty assessment.

The current user's full local request and the frozen question in
[`2026-09-16-high-return/README.md`, §7](../2026-09-16-high-return/README.md#7-one-next-proof-obligation)
were read. The relevant inherited complete arguments inspected are
[HR-1](../2026-09-16-high-return/return-lemma.md), especially §2, and the
elementary split-valuation argument in
[HR-2–HR-4](../2026-09-16-high-return/denominator-obstruction.md). HR-4's
one-prime full-image obstruction is not applied to the two-prime carrier.
The following proof checks the two primes together.

**Strictly offline:** only local file reads and this new Markdown write were
performed. There were no web, browser, connector, external API, download,
installation or remote Git calls. No mathematical diagnostic, enumeration,
oracle or research program was run. This subtask used zero charged
computational evaluations and zero experimental CPU time. Symbolic
inequalities below are proof steps, not finite experimental evidence.

## 1. Frozen objects, counts and generator independence

Throughout,

\[
Q(x,y)=x^2+xy+y^2,\qquad \omega^2+\omega+1=0,
\]
\[
B_L=\{b\in\mathbb Z:1\le|b|\le L,\ \gcd(b,133)=1\},
\qquad
A_L=\{b7^{-k}19^{-\ell}:b\in B_L,\ 0\le k,\ell\le L\}.
\]

The rational valuations \(v_7\) and \(v_{19}\) recover \(-k\) and
\(-\ell\), respectively, and then recover the numerator. Thus every scalar
input has exactly one displayed representation. If \(b_L=|B_L|\), then

\[
b_L=2\left(L-\lfloor L/7\rfloor-\lfloor L/19\rfloor
+\lfloor L/133\rfloor\right),\qquad n_L=b_L(L+1)^2.
\tag{1}
\]

Put

\[
\pi_7=3+\omega,\quad \bar\pi_7=2-\omega,\qquad
\pi_{19}=5+2\omega,\quad \bar\pi_{19}=3-2\omega.
\]

Their products with their conjugates are 7 and 19. The frozen generators are

\[
u=\pi_7/\bar\pi_7=(8+5\omega)/7,\qquad
v=\pi_{19}/\bar\pi_{19}=(21+16\omega)/19.
\tag{2}
\]

Both have norm one. For \(g=a+b\omega\), multiplication of
\(z=x-\omega y\) gives

\[
gz=(ax+by)-\omega\bigl(-bx+(a-b)y\bigr).
\tag{3}
\]

This checks exactly the user's action convention and proves
\(Q(T_g(x,y))=Q(x,y)\) for the generators and all their integer powers.

### Local facts at both primes, including scalar recovery

For clarity, these facts require no global factorization theorem. In
\(\mathbb Z[\omega]\), divisibility by the conjugate factors at 7 is
equivalent to evaluation at the two roots 4 and 2 modulo 7, as proved in
the cited HR-2 companion. At 19, direct division gives

\[
\frac{a+b\omega}{\pi_{19}}
=\frac{(3a+2b)+(-2a+5b)\omega}{19},\qquad
\frac{a+b\omega}{\bar\pi_{19}}
=\frac{(5a-2b)+(2a+3b)\omega}{19}.
\]

Hence the corresponding divisibility tests are

\[
\pi_{19}\mid a+b\omega\iff a+7b\equiv0\pmod{19},\qquad
\bar\pi_{19}\mid a+b\omega\iff a+11b\equiv0\pmod{19}.
\tag{4}
\]

Evaluation at these roots maps onto the relevant prime field, so each
divisibility kernel is prime. Division lowers the positive integer norm by
7 or 19, proving that the largest divisible power of a factor exists for
every nonzero integral element. Primality gives additivity of those orders;
subtracting numerator and denominator orders extends them to
\(\mathbb Q(\omega)^\times\). Factoring out the smaller order proves that
the valuation of a sum equals the smaller valuation when the summands have
different valuations. These are exactly the elementary steps in HR-2,
now with the explicit 19-kernels (4).

Write \(\nu_p,\bar\nu_p\) for the two resulting valuations over
\(p\in\{7,19\}\). On rational numbers both equal the ordinary \(v_p\).
Conjugation interchanges the two, and the generator valuation vectors are

\[
\begin{array}{c|rrrr}
 &\nu_7&\bar\nu_7&\nu_{19}&\bar\nu_{19}\\ \hline
u&1&-1&0&0\\
v&0&0&1&-1.
\end{array}
\tag{5}
\]

The zero entries in (5) are essential: an integral factor of norm 7 cannot
be divisible by a factor of norm 19, or conversely, because divisibility
would force divisibility of their positive integer norms. Thus there is no
unrecorded valuation cost from the other generator.

In particular, the labels \((r,s)\) give distinct elements \(u^rv^s\).
Cancellation shows that these distinct multipliers send a nonzero
\(z\) to distinct points. The frozen action window therefore has exactly
\((16L+1)^2\) multipliers; scalar and nonzero stabilizer multiplicities
are both one.

For a rational pair and \(z=x-\omega y\), the scalar coordinates are
recovered by

\[
x=\frac{\omega\bar z-\bar\omega z}{\omega-\bar\omega},\qquad
y=\frac{\bar z-z}{\omega-\bar\omega}.
\tag{6}
\]

Both \(\omega\) and \(\bar\omega\) have norm one, and
\(N(\omega-\bar\omega)=3\), so every coefficient and the denominator
in (6) is a unit at the factors over 7 and 19. Consequently:

- If \((\nu_p(z),\bar\nu_p(z))=(\alpha,\beta)\) with
  \(\alpha\ne\beta\), then \(v_p(x)=v_p(y)=\min(\alpha,\beta)\).
  Both numerators in (6) have two terms of distinct valuations.
- If \(\alpha=\beta=-D\), then \(v_p(x),v_p(y)\ge-D\), and at least
  one equals \(-D\). Otherwise the identity \(z=x-\omega y\) would
  have valuation greater than \(-D\). For legal carrier coordinates,
  their maximum denominator depth at \(p\) is therefore exactly \(D\).

These statements justify the scalar depth deductions below; split
valuations are not silently identified with separate coordinate depths.

## 2. The separated-depth class and its density

Fix \(m\ge2\), set \(L=10m\), and consider all pairs

\[
x=b7^{-k}19^{-\ell},\qquad y=c7^{-h}19^{-j},
\tag{7}
\]

where \(b,c\in B_L\), \(0\le k,h\le L\), \(k\ne h\), and

\[
0\le\ell\le m,\qquad 9m\le j\le10m.
\tag{8}
\]

Define

\[
K=\max(k,h),\quad M=j,\quad e=j-\ell\ge8m,
\quad a=K-k,\quad d=K-h.
\tag{9}
\]

The two values \(a,d\) are nonnegative, and exactly one is zero.
Normalizing \(z=x-\omega y\) by \(7^K19^M\) gives coordinates

\[
X=b7^a19^e,\qquad Y=c7^d.
\tag{10}
\]

Because the two rational coordinate valuations are unequal at each prime,
the split valuations of \(z\) are initially balanced:

\[
(\nu_7(z),\bar\nu_7(z))=(-K,-K),\qquad
(\nu_{19}(z),\bar\nu_{19}(z))=(-M,-M).
\tag{11}
\]

The gap has the following strict archimedean dominance:

\[
19^e>4L^2 7^L.
\tag{12}
\]

Indeed \(19^2=361>343=7^3\), hence \(19^4>7^6\), and therefore

\[
\frac{19^{8m}}{7^{10m}}
=\left(\frac{19^4}{7^5}\right)^{2m}>49^m>400m^2=4L^2.
\]

For the final inequality the base case is \(49^2=2401>1600\); induction
uses \(49m^2>(m+1)^2\) for \(m\ge2\). This is a uniform inequality,
not a finite numerical test.

Unique scalar representations make the class size exactly

\[
b_L^2 L(L+1)(m+1)^2.
\]

Its fraction of \(A_L^2\) is

\[
\frac{L(m+1)^2}{(L+1)^3}
\ge\frac{L}{100(L+1)}\ge\frac1{200},
\tag{13}
\]

because \(m+1\ge(L+1)/10\) and \(L\ge1\). Thus the restrictions have
been charged on the full ordered Cartesian square, not only on one input.

## 3. A nonzero 19-exponent cannot return

Suppose \(g=u^rv^s\), with arbitrary integers \(r,s\), sends a pair from
(7)–(8) to \((x',y')\in A_L^2\). By (5) and (11), its split valuations
at 19 are \((-M+s,-M-s)\). If \(s\ne0\), scalar recovery (6) forces
both returned coordinates to have 19-depth \(M+|s|\).

Their 7-depths are nonnegative and their numerator magnitudes are at most
\(L\), so

\[
|x'|,|y'|\le L19^{-M-|s|}.
\tag{14}
\]

Meanwhile \(|x|\ge7^{-L}19^{-\ell}=7^{-L}19^{e-M}\). For every real
pair, \(Q(x,y)\ge3x^2/4\), whereas
\(Q(x',y')\le3\max(|x'|,|y'|)^2\). Norm preservation and (14) give

\[
19^e\le2L7^L19^{-|s|}\le2L7^L,
\]

contradicting (12). This argument does not assume any sign relation
between coordinates and is independent of \(r\). Hence every legal
return must have \(s=0\).

## 4. A nonzero 7-exponent cannot return either

Suppose now \(s=0\) and \(r\ne0\), and put \(t=|r|\ge1\).
Equations (5), (6) and (11) force both returned coordinates to have the
same 7-depth \(K+t\). Legality gives

\[
t\le L-K,\qquad d+t\le L-h\le L.
\tag{15}
\]

The split valuations at 19 are unchanged, still \((-M,-M)\), so the
largest returned 19-depth is exactly \(M\). After swapping the two
returned coordinates if necessary, their normalized pair has the form
\((b'19^f,c')\), where \(b',c'\in B_L\) and \(f\ge0\). Symmetry of
\(Q\) permits this swap; it does not change the norm equation. Clearing
the actual common denominator gives exactly

\[
Q(b'19^f,c')=7^{2t}Q(b7^a19^e,c7^d).
\tag{16}
\]

There is no assumption about which original coordinate had the larger
7-depth. Both possibilities are included in the values of \(a,d\).

The left side of (16) is at most \(3L^2 19^{2f}\), while the right side
is at least \((3/4)7^{2t}19^{2e}\), since \(|b7^a|\ge1\). Hence

\[
19^f\ge\frac{7^t19^e}{2L},\qquad
19^{\min(e,f)}\ge\frac{19^e}{2L}>2L7^L.
\tag{17}
\]

In particular \(w=\min(e,f)\) is a positive integer; the case \(f=0\)
is automatically impossible. Reducing (16) modulo \(19^w\) yields

\[
c'^2\equiv c^2 7^{2(d+t)}\pmod{19^w}.
\tag{18}
\]

The two factors \(c'-c7^{d+t}\) and \(c'+c7^{d+t}\) cannot both be
divisible by 19: their difference \(2c7^{d+t}\) is a 19-unit. Equation
(18) therefore forces one entire factor to be divisible by \(19^w\).
By (15), each factor has magnitude at most

\[
|c'|+|c|7^{d+t}\le L+L7^L\le2L7^L<19^w.
\]

An integer divisible by \(19^w\) and strictly smaller in absolute value
must be zero. Thus \(c'=\pm c7^{d+t}\). But \(d+t\ge1\), so the
right side is divisible by 7, whereas \(c'\in B_L\) is not. This final
contradiction proves \(r=0\).

All powers returning from the class are therefore \(u^0v^0=1\). The
identity returns every carrier pair, and lies in the prescribed window,
so the return count is exactly one for every pair in (7)–(8).

## 5. Quantifiers, rate consequence and scope

For every fixed \(\varepsilon,\delta>0\), every pair in the class has
return count \(1<n_L^\varepsilon\), so it is in the proposed bad tail.
Along \(L=10m\), \(m\ge2\), (13) gives

\[
\#\{(x,y)\in A_L^2:R_{A_L,G_L}(x,y)<n_L^\varepsilon\}
\ge\frac{n_L^2}{200}.
\tag{19}
\]

Since \(n_L\ge2(L+1)^2\to\infty\), eventually
\(n_L^\delta>200\), and the right side of (19) is strictly larger than
\(n_L^{2-\delta}\). The unbounded subsequence contradicts the frozen
assertion's requirement for every sufficiently large \(L\). It refutes
all fixed positive exponent pairs, not merely a selected numerical pair.

### Audit ledger

| Item | Verified charge or scope |
|---|---|
| Fixed polynomial, primes and carrier | Exactly the frozen \(Q,A_L,7,19\); no enlarged family or field |
| Scalar input multiplicity | One; both rational prime valuations and then the numerator are recovered |
| Multiplier multiplicity | One; valuation vector (5) recovers both exponents |
| Stabilizers and zero | All inputs are nonzero; every nonzero pair has trivial multiplier stabilizer |
| Exceptional class size | Exactly the count preceding (13), at least \(n_L^2/200\); all ordered choices are included |
| Denominator costs | Both returned prime depths are recovered using (6); the essential bound \(d+t\le L\) is (15) |
| Cross-prime effects | Opposite-prime valuations of each generator are zero; real size and the 19-congruence are applied jointly |
| Archimedean loss | Explicit factors \(2L\) and \(4L^2 7^L\), dominated uniformly by the imposed 19-gap |
| Norm coincidences | Used only for exclusion of returns; no inference about the full fiber outside this multiplier group |
| Return-window coverage | The proof excludes every nonidentity integer power pair, hence all labels in the specified finite window |
| Rate outcome | On a fixed positive fraction of pairs, returns have exponent zero; the bad tail has exponent two |
| Computational evidence | None required or executed; the proof is uniform over \(m\ge2\) |

**No mathematical gap was found in this obstruction.** The only conclusion
promoted from OPEN to FAILED by this audit is the exact HR-N1 action-tail
assertion. An actual-image obstruction for the two-prime carrier, an
exceptional-output bound, an alternative subsequence construction, and the
general real-set compression target are not settled here. No previous
report or archive was edited by this subtask.
