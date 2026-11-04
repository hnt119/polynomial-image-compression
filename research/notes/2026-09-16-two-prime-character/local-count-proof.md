# TP-L1 — Exact local counts for the correlated character carrier

Date/version: **2026-09-16, version 1**.

## Claim record and scope

| Field | Record |
|---|---|
| Claim ID | **TP-L1** |
| Track/branch | T03, newly commissioned two-prime character-correlation branch |
| Polynomial | $Q(x,y)=x^2+xy+y^2$, evaluated in the explicitly specified finite ring |
| Status | **PROVED**, by the complete elementary argument below |
| Quantifiers | The fixed ring $R=\mathbb F_7\times\mathbb F_{19}$, the exact carrier $D$ and full multiplier group $G$ defined in §1; every ordered pair in $D^2$ |
| Evidence | Internal symbolic derivation, including checkable residue tables; no mathematical program or experiment was executed for this proof |
| Audit | Independently inspected by the lead; the exhaustive matrix computation and split-coordinate oracle both agree, as separately recorded in the cycle report |
| Dependencies | The established Eisenstein action and norm identity; elementary arithmetic in the two finite fields |
| New versus inherited | The correlated carrier's complete local sign counts, return histogram and modular image count are derived here; the norm identity and HR-1 return theorem are inherited |
| Remaining gap | No characteristic-zero realization, real scalar projection, denominator/height bound or positive real construction rate is supplied here |
| Novelty | No external literature assessment or novelty claim; this cycle is strictly offline |

The active assignment is the local attachment
`[private task attachment]`.
Historical T03 scope is recorded in
`local-only/migration/sources/T03_CURRENT_STATE.md`, §§4, 7, 13–15,
and the corresponding frozen T03 archive. The inherited return theorem is
[HR-1](../2026-09-16-high-return/return-lemma.md).
This note does not reopen the different rational denominator carrier from
the completed HR-N1 cycle. It does not change the original real T03 target
or its adaptive RC15/4 obligation.

## 1. The exact finite system

For $p\in\{7,19\}$ let $\chi_p$ be the quadratic character on
$\mathbb F_p^\times$. Put

$$
R=\mathbb F_7\times\mathbb F_{19},\qquad
D=\{(a_7,a_{19})\in R^\times:
             \chi_7(a_7)=\chi_{19}(a_{19})\}.
$$

Each character sign contributes $3\cdot9=27$ scalars, so
$|D|=54$ and $|D^2|=2916$. Here $D^2$ means all ordered pairs of
scalars from the same set $D$.

Let $E_p=\mathbb F_p[\omega]/(\omega^2+\omega+1)$ and let $H_p$
be its full norm-one group. Both primes are $1\pmod3$, so $E_p$
splits as a product of two fields and

$$
H_p=\{(t,t^{-1}):t\in\mathbb F_p^\times\}
       \cong C_{p-1}.
$$

Thus $G=H_7\times H_{19}$ has $6\cdot18=108$ elements.
The established action, for $g=\alpha+\beta\omega\in H_p$, is

$$
T_g(x,y)=(\alpha x+\beta y,-\beta x+(\alpha-\beta)y).
\tag{1}
$$

It preserves $Q$. We use (1), without claiming a new norm identity.
For $z=(x,y)\in D^2$ write $z_p=(x_p,y_p)$ and define

$$
r(z)=\#\{(g_7,g_{19})\in G:
                (T_{g_7}z_7,T_{g_{19}}z_{19})\in D^2\}.
\tag{2}
$$

The target condition in (2) matches the two primes' characters for
the first scalar, and separately matches them for the second scalar.
It does not require the two scalars to have equal characters.

## 2. Orbits and stabilizers, including norm zero

In split coordinates a state has the form $(u,v)$, its norm is $uv$,
and $t\in H_p$ acts by $(u,v)\mapsto(tu,t^{-1}v)$.

* If the norm $N$ is nonzero, its fiber is a single orbit of size
  $p-1$: given $(u,v)$ and $(u',v')$ with the same nonzero product,
  use $t=u'/u$.
* If $N=0$ and the state is nonzero, it lies on one of the two
  punctured coordinate axes in split coordinates. Each axis is one
  orbit of size $p-1$, and the group does not exchange them.
* Every nonzero state has trivial stabilizer. A nonzero split
  coordinate forces $t=1$ whenever the state is fixed.
* The zero vector has stabilizer $H_p$. It is absent here, since
  $x_p$ and $y_p$ are both nonzero for every input in $D^2$.

In particular, isotropic nonzero states do **not** have an extra
stabilizer. Every global input in $D^2$ has stabilizer size one, and
distinct returning labels give distinct scalar pairs in $D^2$.
The passage from $z_p=x_p-\omega y_p$ to the scalar pair is a
bijection, so there is no scalar projection loss in this finite model.

The two isotropic lines have $y=tx$, where $t$ is a root of
$t^2+t+1=0$. These roots are $2,4$ at $7$ and $7,11$ at $19$.
They are squares in their respective fields. Equivalently, their
order is three and $3\mid(p-1)/2$.

## 3. Local sign counts

For a local orbit $\mathcal O$ define

$$
c_p(\varepsilon,\eta;\mathcal O)
=\#\{(x,y)\in\mathcal O:
 x,y\ne0,\ \chi_p(x)=\varepsilon,\ \chi_p(y)=\eta\}.
\tag{3}
$$

Both primes are $3\pmod4$, so $\chi_p(-1)=-1$.
Write the local norm type as $0,+,-$, with $+$ and $-$ denoting
nonzero square and nonsquare norms. We will show that there are
numbers $A_p,B_p$, depending only on this norm type, such that

$$
c_p(+,+)=c_p(-,-)=A_p,\qquad
c_p(+,-)=c_p(-,+)=B_p.
\tag{4}
$$

For norm type zero, (4) refers to **each** of the two punctured
isotropic orbits separately.

### 3.1 Nonzero norm

Set $t=y/x$ and $f(t)=1+t+t^2$. For a fixed nonzero norm $N$,
the equation is $x^2=N/f(t)$. A nonzero $t$ with $f(t)\ne0$ is
admissible precisely when $\chi_p(f(t))=\chi_p(N)$.
For such a $t$, its two possible $x$ values are opposites and
have opposite characters. If $t$ is square, these two states
contribute once each to $(+,+)$ and $(-,-)$; if $t$ is nonsquare,
they contribute once each to $(+,-)$ and $(-,+)$.
Consequently

$$
\begin{aligned}
A_p(N)&=\#\{t\in\mathbb F_p^\times:
                  \chi_p(t)=1,\ \chi_p(f(t))=\chi_p(N)\},\\
B_p(N)&=\#\{t\in\mathbb F_p^\times:
                  \chi_p(t)=-1,\ \chi_p(f(t))=\chi_p(N)\}.
\end{aligned}
\tag{5}
$$

The character conditions in (5) exclude the roots of $f$.
They show directly that the counts depend only on the norm's
character, rather than its particular nonzero value.

Here are complete small tables for the **square** values of $t$;
these determine $A_p$ without enumerating all input pairs.

| $p$ | Square $t$, in listed order | $f(t)\pmod p$, in the same order | Nonzero square $f(t)$ |
|---|---|---|---|
| $7$ | $1,2,4$ | $3,0,0$ | None |
| $19$ | $1,4,5,6,7,9,11,16,17$ | $3,2,12,5,0,15,0,7,3$ | At $t=6,16$ |

All nonzero entries not designated square in the final column are
nonsquares; the listed square sets allow this to be checked directly.
Thus $A_7(+)=0$, $A_7(-)=1$, $A_{19}(+)=2$ and $A_{19}(-)=5$.

To determine $B_p$, the full nonzero-norm orbit has $p-1$ points.
If $N$ is square, exactly four have a zero scalar coordinate:
$(0,\pm\sqrt N)$ and $(\pm\sqrt N,0)$. If $N$ is nonsquare,
none have a zero scalar coordinate. Equation (4) therefore gives

$$
2(A_p(N)+B_p(N))
=p-1-4\mathbf1_{\chi_p(N)=1}.
\tag{6}
$$

This proves all four nonzero-norm rows in the next table.

### 3.2 Norm zero and the resulting table

On either isotropic line, $y=tx$ with square $t$ and
$x\in\mathbb F_p^\times$. Hence $x,y$ have the same character,
and each sign occurs $(p-1)/2$ times. The complete table is

| Prime | Norm type | $A_p=c_p(+,+)=c_p(-,-)$ | $B_p=c_p(+,-)=c_p(-,+)$ | Number of such local orbits |
|---|---|---:|---:|---:|
| $7$ | $0$ | $3$ | $0$ | $2$ |
| $7$ | $+$ | $0$ | $1$ | $3$ |
| $7$ | $-$ | $1$ | $2$ | $3$ |
| $19$ | $0$ | $9$ | $0$ | $2$ |
| $19$ | $+$ | $2$ | $5$ | $9$ |
| $19$ | $-$ | $5$ | $4$ | $9$ |

For each nonzero norm there is one local orbit; each nonzero
character class has $(p-1)/2$ possible norm values. This explains
the final column and keeps the two isotropic orbits separate.

## 4. Exact global returns and histogram

Fix one orbit at each prime. Freeness and transitivity identify
the group elements sending a given state into each sign class
with the states counted by (3). The character correlation
condition in $D$ requires matching sign classes across primes.
It follows that every admissible input in this pair of orbits has

$$
r=\sum_{\varepsilon,\eta\in\{+,-\}}
         c_7(\varepsilon,\eta)c_{19}(\varepsilon,\eta)
  =2(A_7A_{19}+B_7B_{19}).
\tag{7}
$$

The right side also counts how many states of this orbit pair
belong to $D^2$. Let $m_p(\tau)$ be the local orbit multiplicity
in the preceding table. The number of inputs of norm types
$(\tau_7,\tau_{19})$ is therefore
$m_7(\tau_7)m_{19}(\tau_{19})r$.

| Norm type at $7$ | Norm type at $19$ | Orbit pairs $m_7m_{19}$ | Returns $r$ per admissible pair | Input population |
|---|---|---:|---:|---:|
| $0$ | $0$ | $4$ | $54$ | $216$ |
| $0$ | $+$ | $18$ | $12$ | $216$ |
| $0$ | $-$ | $18$ | $30$ | $540$ |
| $+$ | $0$ | $6$ | No admissible input: expression (7) is $0$ | $0$ |
| $+$ | $+$ | $27$ | $10$ | $270$ |
| $+$ | $-$ | $27$ | $8$ | $216$ |
| $-$ | $0$ | $6$ | $18$ | $108$ |
| $-$ | $+$ | $27$ | $24$ | $648$ |
| $-$ | $-$ | $27$ | $26$ | $702$ |

Thus the complete histogram is

| Return count $r$ | Number of ordered pairs |
|---:|---:|
| $8$ | $216$ |
| $10$ | $270$ |
| $12$ | $216$ |
| $18$ | $108$ |
| $24$ | $648$ |
| $26$ | $702$ |
| $30$ | $540$ |
| $54$ | $216$ |
| **Total** | **2916** |

In particular the fraction with $r=1$ is zero, the minimum is
$8$, and the maximum is $54$. The central two observations
are $24$ and $26$, so the usual even-sample median is $25$
(the lower and upper medians are $24$ and $26$).
The arithmetic mean is

$$
\frac{1}{2916}\sum_{z\in D^2}r(z)=\frac{218}{9},
\tag{8}
$$

and the geometric mean has the exact expression

$$
\exp\left(\frac1{2916}\sum_{z\in D^2}\log r(z)\right)
=2^{5/3}3^{7/9}5^{5/18}13^{13/54}.
\tag{9}
$$

All 2916 inputs have stabilizer size one.

There is also a simpler lower bound independent of the table:
the identity and simultaneous negation at both primes give two
distinct returns for every pair. Negation flips both characters
at each prime, preserving their equality across primes. The
stronger bound $r\ge8$ follows from the exact table, not from
crediting repeated labels or nontrivial stabilizers.

## 5. Actual modular fibers and the 130-value image

The orbit distinction at norm zero matters for full polynomial
fibers. For a fixed norm pair $(N_7,N_{19})$, let
$\kappa_p(N_p)=2$ if $N_p=0$ and $1$ otherwise. Each component
of a state in $D^2$ is nonzero, so these are exactly the possible
numbers of local orbits in this polynomial fiber.
Since both isotropic lines have identical sign counts, (7)
gives the full scalar fiber size

$$
\#\{(x,y)\in D^2:Q(x,y)=(N_7,N_{19})\}
=\kappa_7(N_7)\kappa_{19}(N_{19})\,r,
\tag{10}
$$

where the right side is zero for the incompatible type $(+,0)$.
In particular $Q^{-1}(0,0)\cap D^2$ has $4\cdot54=216$
points, even though each of those points has only 54 returns
under $G$. The extra factor four counts different group orbits,
not a stabilizer or projection multiplicity.

| Norm types $(7,19)$ | Number of norm values | Fiber size per norm value |
|---|---:|---:|
| $(0,0)$ | $1$ | $216$ |
| $(0,+)$ | $9$ | $24$ |
| $(0,-)$ | $9$ | $60$ |
| $(+,0)$ | $3$ | $0$ |
| $(+,+)$ | $27$ | $10$ |
| $(+,-)$ | $27$ | $8$ |
| $(-,0)$ | $3$ | $36$ |
| $(-,+)$ | $27$ | $24$ |
| $(-,-)$ | $27$ | $26$ |

Every row except $(+,0)$ has a positive fiber. Consequently

$$
Q(D,D)=R\setminus
\{(N_7,0):N_7\in\mathbb F_7^\times,\ \chi_7(N_7)=1\},
\qquad |Q(D,D)|=133-3=130.
\tag{11}
$$

As a consistency identity, the sum of reciprocal return counts
over all inputs is 154, the number of group orbits meeting
$D^2$. It exceeds 130 because several group orbits share a
zero-coordinate norm value. An action orbit is not always a
complete polynomial fiber.

## 6. What this finite result does and does not supply

The finite local system has positive return entropy: every
return count is at least eight, and its exact mean log return
is the logarithm of (9). Its inputs, transformations and scalar
pairs live in the finite ring $R$, with no projection or
stabilizer cost inside this model.

These statements alone construct no finite subset of
$\mathbb R$ with the requested power saving. Congruent norm
values need not be equal real norm values, and the split
finite-ring action has not been lifted to exact real
Cartesian returns here. Any global construction must separately
justify tensorization, an exact scalar realization, carrier
density in both coordinates, and every arithmetic cost.
No positive real signed rate is asserted by TP-L1.

No mathematical program, experiment, network access or
external verification was used in preparing this proof. The
small tables are displayed as part of its elementary symbolic
argument. Independent exhaustive comparison, if performed,
is corroborating evidence and does not replace this proof.
