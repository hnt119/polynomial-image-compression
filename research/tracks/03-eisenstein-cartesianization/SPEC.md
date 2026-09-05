# T03 specification: parity-twisted Cartesianization

Source task: **Polynomial 2 · Research Experiment 分支 · Email Progress Update**.
Recent checkpoint date: **3 September 2026**. History logged: **5 September 2026**.

## Fixed target

$$Q_E(x,y)=x^2+xy+y^2.$$

Find a fixed $c_E>0$ and arbitrarily large finite $A\subset\mathbb R$ with
$|Q_E(A,A)|\le|A|^{2-c_E}$. The proposed construction uses rational coefficient
sets, a valid sufficient subclass of real sets.

## Current proposed code

Let $\omega^2+\omega+1=0$, so $N(a-\omega b)=Q_E(a,b)$. Use fresh distinct
split primes $q_i=N(\pi_i)\equiv1\pmod3$ and inert primes
$r_i\equiv2\pmod3$. The balanced code consists of products with local letters
$\{1,r_i,\pi_i,\bar\pi_i\}$.

If $\ell(z)$ is the number of split letters in $z$, set

$$z^\sharp=(1-\omega)^{\epsilon(z)}z,\qquad
\epsilon(z)=\begin{cases}1,&\ell(z)\text{ even},\\0,&\ell(z)\text{ odd}.\end{cases}$$

The frozen code has $4^m$ distinct elements and $3^m$ norm values. PTCR asks
for norm-one multipliers, allowed to depend on the whole codeword, whose
rephased elements are distinct and have both coefficients in a common set
$A_m\subset\mathbb Q$, with

$$d_m=|A_m|^2-4^m\le|A_m|^{2-\xi}$$

for fixed $\xi>0$ and infinitely many $m$.

The all-pairs bound would be
$|Q_E(A_m,A_m)|\le3^m+d_m$. Together with the deficit estimate, this gives
every fixed $0<c_E<\min\{2-\log_2 3,\xi\}$ eventually.

## Current constructive milestone

The recent continuation prioritizes global reassignment with a recurrence

$$d_{m+k}\le\kappa d_m+C|A_m|^{2-\delta},\qquad 0\le\kappa<4^k,$$

for fixed $k,\delta>0$, with an actual admissible construction and controlled
growth $|A_m|=2^{m+o(m)}$. The one-step threshold $\kappa<4$ is derived in the
[composition report, §G.4](../../history-sources/Parity_Twisted_Cartesianization_Composition_Report.md).
The block formulation is the subsequent proposed extension, not a proved
composition algorithm.

Prove norm preservation, distinct codeword placement, one common coefficient
set, the full deficit bound, and all-scale composition. A finite gadget or
arbitrary edge graph alone does not prove the target. See [STATUS.md](STATUS.md).
