# T04 specification: direct cubic slice overlap

Source task: **Polynomial 1 · Research Experiment 分支 · Email Progress Update**.
Recent checkpoint date: **3 September 2026**. History logged: **5 September 2026**.

## Fixed target

$$P_-(x,y)=(x-y)^3-3(x+y).$$

Find a fixed $c_->0$ and arbitrarily large finite $A\subset\mathbb R$ with
$|P_-(A,A)|\le|A|^{2-c_-}$. The source calls this CPSI and labels its polynomial
$P_3$; this registry uses $P_-$ to distinguish it from T01.

## Benchmark and exact bridge

The quadratic seed is $R(x,y)=(x-y)^2+5(x+y)$. With $u=x-y$,

$$5P_-(x,y)=5u^3+3u^2-3R(x,y).$$

The seed's reported small-image theorem is a benchmark. Its success does not
automatically transfer to the cubic on the same witness.

## Current proposed construction

Put $H_3(u)=u^3-3u$ and $A_u=A\cap(A-u)$, so $y\in A_u$ means that both
$y$ and $y+u$ belong to $A$. Then

$$P_-(A,A)=\bigcup_{u\in A-A}\left(H_3(u)-6A_u\right),
\qquad\sum_u|A_u|=|A|^2.$$

The desired step is a direct construction forcing enough overlap across these
slices to bound the **whole union** below $|A|^{2-c_-}$. The overlap equation is

$$6(y-y')=(u-u')(u^2+uu'+u'^2-3).$$

## Acceptance criteria

Define one growing family of sets and a fixed exponent. Prove all-pairs coverage
and a full-support upper bound, accounting for exceptional or lightly represented
outputs. A large collision-energy estimate alone has the wrong direction for
that conclusion. A successful proof must introduce a gain beyond the two
specified narrow-window quadratic-transfer regimes closed in the recent record.

Sources: [positive-polynomial checkpoint, §§C, I](../../history-sources/positive_polynomial_phase_checkpoint.md)
and [complementary-prime obstruction, §H](../../history-sources/complementary_prime_transfer_obstruction.md).
See [STATUS.md](STATUS.md) for the exact scope of those obstructions.
