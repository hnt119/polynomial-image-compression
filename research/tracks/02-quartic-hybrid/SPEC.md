# T02 specification: quartic hybrid carrier

Source task: **Create Phase C0 proof prompt**.
Recent checkpoint date: **3 September 2026**. History logged: **5 September 2026**.

## Fixed target

$$P_4(x,y)=(x+2y)^4+3x-y.$$

Find a fixed $\varepsilon_4>0$ and arbitrarily large finite real sets $A$ with
$|P_4(A,A)|\le|A|^{2-\varepsilon_4}$. The polynomial, exponent, and finite
arithmetic parameters stay fixed while carrier size grows. Both inputs use $A$.

## Current proposed construction

The [C2 prompt](../../prompts/Phase_C2_Hybrid_Carrier_Structural_Lemma_Prompt.md),
§§4–7, proposes $C_j=G_jT_j$ in the same totally real field family, where $G_j$
consists of precisely bounded positive units and $T_j$ is a positive additive
carrier. The deformation is

$$F_Q(x,y)=(x+2y)^4+Q^3(3x-y),\qquad F_Q(Qx,Qy)=Q^4P_4(x,y).$$

For $u\in G/G$, retain the dependence in

$$G(u)=\{v\in G:uv\in G\},\quad
\mathcal K_u=\{((ut_1+2t_2)^4,3ut_1-t_2):t_1,t_2\in T\},$$

$$F_Q(C,C)=\bigcup_{u\in G/G}
\{v^4\alpha+Q^3v\beta:v\in G(u),(\alpha,\beta)\in\mathcal K_u\}.$$

The intended milestone is one proved bound for the realized support whose gain
survives the ratio union, unit distortion, sign restrictions, regulator costs,
and multiplicity of $(g,t)\mapsto gt$.

## Acceptance criteria

Prove or explicitly isolate compatible field/unit inputs and the actual carrier
growth. If $e^{ad-o(d)}\le|C_d|\le e^{Bd+o(d)}$ and the full support is at most
$e^{hd+o(d)}$, require $0<a\le B$ and $\kappa=2a-h>0$. Then perform the
same-set transport and error absorption for a fixed $0<\varepsilon_4<\kappa/B$.

A correlated parametrization alone is not a cardinality saving. Returning to the
same full-interval packing estimate does not meet the milestone. See
[STATUS.md](STATUS.md) for the C0/C1 history and source gaps.
