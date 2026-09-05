# T01 specification: cubic difference plus sum

Source task: **cubic polynomial 研究综合与汇报**.
Recent checkpoint date: **3 September 2026**. History logged: **5 September 2026**.

## Fixed target

$$P_+(x,y)=(x-y)^3+x+y.$$

Prove or disprove

$$
\exists c_+>0\quad\forall N_0\ge1\quad\exists A\subset\mathbb R
\text{ finite}:\quad |A|\ge N_0,\quad |P_+(A,A)|\le|A|^{2-c_+}.
$$

Both inputs use the same set. The source calls this polynomial $P_3$ or $F_3$;
this registry uses $P_+$ to distinguish it from T04.

## Current proposed construction

The latest checkpoint proposes a fixed integer base $b\ge2$, a finite strongly
connected right-resolving input graph $G$ with one initial state and growth
$\mu>1$, and a finite deterministic output automaton $H$.
For least-significant-first words, put

$$[u]_b=\sum_{i=0}^{n-1}u_i b^i,\qquad
A_n=b^{-n}\{[u]_b:u\in L_n(G)\}.$$

The exact integer output to encode is

$$Z_n(U,V)=(U-V)^3+b^{2n}(U+V),\qquad
b^{3n}P_+(b^{-n}U,b^{-n}V)=Z_n(U,V).$$

The sufficient condition requires that **every** $Z_n(U,V)$ has a canonical
signed base-$b$ representation accepted by $H$, of length at most $3n+C_0$.
If the number of accepted words of length at most $L$ is bounded by
$C_1L^q\lambda^L$, the required gap is

$$\mu\le\lambda^3<\mu^2.$$

With a complete certificate, the source gives the safe exponent
$c_+=(2\log\mu-3\log\lambda)/(2\log\mu)>0$ after absorbing polynomial factors.
Existence of these graphs and a valid carry invariant is **open in the record**.

## Acceptance criteria

Prove graph/word injectivity, all-depth carry closure, all-pairs output coverage,
growth rates, and fixed parameter order. Finite-depth patterns do not certify a
carry invariant. A one-bit identity before scaling is insufficient.

Source: [finite-block checkpoint, §I](../../history-sources/Concrete_Cubic_Compression_Block_NoGo_Checkpoint.md).
See [STATUS.md](STATUS.md) for the preceding obstruction and current gap.
