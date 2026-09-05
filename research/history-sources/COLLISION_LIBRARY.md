# COLLISION_LIBRARY

Let \(N=|A|\) and \(E_F(A)=\#\{(a,b,c,d)\in A^4:F(a,b)=F(c,d)\}\).

## 1. \(F(x,y)=x+y\)

- **Normal form:** native addition.
- **Collision equation:** \(a+b=c+d\).
- **Local residue behavior:** \(F(\mathbb F_p,\mathbb F_p)=\mathbb F_p\); density \(1\).
- **Global support mechanism:** small additive doubling.
- **Obstruction:** no local residue saving on a full residue-field carrier.

## 2. \(F(x,y)=xy\)

- **Normal form:** native multiplication.
- **Collision equation:** \(ab=cd\).
- **Local residue behavior:** \(F(\mathbb F_p,\mathbb F_p)=\mathbb F_p\); density \(1\).
- **Global support mechanism:** small multiplicative doubling or exact Phase-A hybrid factorization.
- **Obstruction:** no local residue saving.

## 3. \(F(x,y)=x+y+xy\)

- **Normal form:** \(F(x,y)=(x+1)(y+1)-1\).
- **Collision equation:** \((a+1)(b+1)=(c+1)(d+1)\).
- **Local residue behavior:** surjective over every \(\mathbb F_p\), since \(F(0,y)=y\).
- **Global support mechanism:** multiplicative structure of \(A+1\).
- **Obstruction:** local compression is absent because the global exceptional form already explains compression.

## 4. \(F(x,y)=x^2+y^2\)

- **Normal form:** addition on \(A^2\).
- **Collision equation:** \(a^2+b^2=c^2+d^2\).
- **Local residue behavior:** over every odd \(\mathbb F_p\), every element is a sum of two squares; density \(1\).
- **Global support mechanism:** additive structure of \(A^2\).
- **Obstruction:** the structure must be built in the transformed carrier.

## 5. \(h(x,y)=xy(x+y)\)

- **Normal forms:** \(x^2y+xy^2\) and \(h(tx,ty)=t^3h(x,y)\).
- **Collision equation:** \(ab(a+b)=cd(c+d)\).
- **Global stress test:** on \(A=\{q^0,\ldots,q^{N-1}\}\), \(q\ge3\),
  \[
  |h(A,A)|=N(N+1)/2,
  \qquad
  E_h(A)=2N^2-N.
  \]
- **Local residue behavior:**
  \[
  |h(\mathbb F_p,\mathbb F_p)|=
  \begin{cases}
  1,&p=2,\\
  5,&p=7,\\
  p,&\text{every other prime }p.
  \end{cases}
  \]
  Thus the density is \(5/7\) only at the exceptional odd prime \(7\), and is \(1\) at every other odd prime.
- **Global support mechanism:** none validated. Complete splitting of \(7\) would formally repeat a \((5/7)^d\) restriction, but Pohoata's tower theorem does not state that \(7\) belongs to its split set, and the degree-three archimedean cost defeats the generic one-prime ledger.
- **Obstruction:** global rank-two mixing and almost everywhere full local image.

## 6. \(f_Q(x,y)=Q(x+y)+(x-y)^2\)

- **Normal form:** a quadratic polynomial deliberately containing a lower-degree coefficient divisible by \(Q\).
- **Collision equation:**
  \[
  Q(a+b-c-d)+(a-b)^2-(c-d)^2=0.
  \]
- **Local residue behavior:** for every odd \(p\mid Q\),
  \[
  f_Q(x,y)\equiv(x-y)^2\pmod p,
  \]
  so its reduced image has exactly \((p+1)/2\) values and density \((p+1)/(2p)\).
- **Global support mechanism:** complete splitting, Chinese remainder theorem, Minkowski output box, and uniform packing inside each residue class.
- **Obstruction:** \(Q\), coefficient height, and output radius must be absorbed before \(d\to\infty\).

## 7. \(f(x,y)=x+y+(x-y)^2\)

- **Normal form:** fixed quadratic obtained from \(f_Q\) by scaling.
- **Collision equation:**
  \[
  a+b-c-d+(a-b)^2-(c-d)^2=0.
  \]
- **Local residue behavior:** surjective over every odd \(\mathbb F_p\), since \(f(x,x)=2x\).
- **Global support mechanism:** not a direct sparse local image of \(f\). Instead use
  \[
  f_Q(Qx,Qy)=Q^2f(x,y)
  \]
  and scale the carrier by \(Q^{-1}\).
- **Obstruction:** any future use of an auxiliary deformation must pass the same fixed-polynomial rescaling audit.
