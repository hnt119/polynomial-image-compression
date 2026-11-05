### 4.3 Digital theorems

**PROVED — regular languages.** Let \(b\ge2\), and let \(G\) be a finite strongly connected right-resolving digit-labelled graph, with a fixed start, every state terminal, and adjacency spectral radius \(\mu>1\). For least-significant-first accepted words, put
\[
D_n=\{[u]_b:u\in L_n(G)\},\quad A_n=b^{-n}D_n.
\]
Then, for fixed \(c_G>0\) and all sufficiently large \(n\),
\[
|Z_{b^n}(D_n,D_n)|\ge c_G|D_n|^2=\Theta_G(\mu^{2n}).
\tag{T01.5}
\]
Reconvergent prefixes supply an eventually injective positive-density continuation rectangle.

**PROVED — stronger positive-entropy theorem.** Fix a nonempty finite prime set \(S\) and \(\alpha>0\). For all sufficiently large \(S\)-smooth \(N\), every \(D\subset[0,N)\cap\mathbb Z\) with \(|D|\ge N^\alpha\) satisfies
\[
|Z_N(D,D)|\ge\eta(S,\alpha)|D|^2.
\tag{T01.6}
\]
Recorded explicit constants: \(s=|S|\), \(R_S=\prod_{p\in S}p\), \(L_S=3^s(1+2R_S)\), \(\beta=1-1/(2s)\), choose \(T\) with \(\beta^T<\alpha\), and take
\[
\eta(S,\alpha)=\frac1{2L_S(2s)^{2T}}.
\]
The proof retains
\[
H_N(d)=\prod_{p^e\parallel N}p^{\min(v_p(d),\lfloor2e/3\rfloor)}
\]
and a fiber bound \(3^s(1+2R_SH_N(d)^2/N)\), together with the exact renormalization
\[
Z_N(r+qX,r+qY)=2rN^2+q^3Z_{N/q}(X,Y),\qquad q\mid N.
\]

