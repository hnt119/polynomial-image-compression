### 4.5 The quadratic-to-cubic transfer was closed

**PROVED — exact bridge.** With \(u=x-y\),
\[
5P_3(x,y)=5u^3+3u^2-3R(x,y).
\]
The map \((x,y)\mapsto(u,R(x,y))\) is injective. Inside every exact quadratic fiber, the cubic projection on the specified witness is injective; a transfer saving would have to come from cross-fiber overlap.

**PROVED — both specified prime choices fail.** For the centered witness \(A=\sigma_0(B_K(Q/8))/Q\):

- If all selected split primes satisfy \(q\equiv5\pmod{12}\), then \(|P_3(A,A)|=|A|^2\). Cubing recovers the difference modulo \(Q\); the narrow window and norm integrality give its unique lift.
- If all satisfy \(q\equiv1\pmod{12}\), let \(t\) be their number and
  \[
  \delta=\tfrac12\log Q-t\log4-\log(32\sqrt D).
  \]
  For \(\delta>0\),
  \[
  |P_3(A,A)|\ge\frac{|A|^2}{1+e^{-\delta d}}.
  \]
  The successful quadratic condition \(\Theta_R<1\) forces \(t\ge8\) and permits
  \[
  \delta\ge\delta_*(t)=\tfrac12\log\frac{41t!}{256(8/3)^t}>0.
  \]

Thus the gain rate \(d^{-1}\log(|A|^2/|P_3(A,A)|)\) tends to zero. **FAILED:** CRO for this exact complementary-prime architecture. Other radii, altered arithmetic carriers, and CPSI itself are not excluded by this statement.

### 4.7 Exact coverage criterion and a rich-fiber counterexample to an inference

**PROVED — full-image accounting.** For \(f:X^2\to Y\), \(n=|X|\), and output multiplicity \(m(z)\),
\[
|f(X,X)|=\sum_{(x,y)\in X^2}\frac1{m(f(x,y))}.
\]
If at most \(Cn^{2-\kappa}\) pairs lie in fibers smaller than \(n^\varepsilon\), then
\[
|f(X,X)|\le(C+1)n^{2-\min(\varepsilon,\kappa)}.
\]
Conversely, \(|f(X,X)|\le Cn^{2-c}\) implies at most \(Cn^{2-c/2}\) pairs lie in fibers smaller than \(n^{c/2}\).

**FAILED — fixed positive-density coverage inference.** Covering only a fixed fraction \(\delta<1\) by \(n^\varepsilon\)-rich fibers gives merely
\[
(1-\delta)n^2+\delta n^{2-\varepsilon}.
\]
It does not give CPSI on that witness.

**PROVED — explicit failed rich-fiber construction.** The checkpoint selects increasing integers \(i_j\) by finite avoidance/CRT conditions and sets
\[
A_N=\{36i_j^3+3i_j+2,\ 36i_j^3-3i_j+2:1\le j\le N\}.
\]
Then \(|A_N|=2N\), output \(-12\) has multiplicity \(N\), every other output has multiplicity one, and
\[
|P_3(A_N,A_N)|=4N^2-N+1.
\]
The Chebyshev lift uses \(h(x)=(\sqrt{x+2}+\sqrt{x-2})/2\), gives \(|H_N|=4N\) and a totally real field of degree \(16^N\) excluding \(\sqrt3\). Its root discriminant is not bounded. The actual exponent gap is zero.

