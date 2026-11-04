## 2. Algebra audit

### 2.1 General quadratic and split cases

**PROVED.** Let \(K\) be a characteristic-zero field,
\[
P=ax^2+bxy+cy^2+dx+ey+r,\qquad \Delta=b^2-4ac\ne0.
\]
For \(a\ne0\), take the quadratic étale algebra
\[
E=K[T]/(T^2-\Delta),\quad \bar T=-T,\quad
\alpha=\frac{-b+T}{2a}.
\]
When \(\Delta\) is nonsquare this is a field; when it is square, \(E\cong K\times K\), with the two factors exchanged by the involution. Retaining both factors is essential.

Since \(\alpha+\bar\alpha=-b/a\) and \(\alpha\bar\alpha=c/a\),
\[
q(x,y):=ax^2+bxy+cy^2=aN_{E/K}(x-\alpha y).
\]
The unique solution of the trace equations in the prompt is
\[
\boxed{\beta=\frac d2+\frac{bd-2ae}{2\Delta}T.}
\tag{2.1}
\]
Indeed, for \(\beta=u+vT\), those equations are \(2u=d\) and \(bu-v\Delta=ae\). With \(z=x-\alpha y\),
\[
P=aN(z)+\operatorname{Tr}(\beta z)+r.
\]
Expanding \(N(z+w)=N(z)+\operatorname{Tr}(z\bar w)+N(w)\), with \(w=\bar\beta/a\), proves
\[
\boxed{P=aN\left(z+\frac{\bar\beta}{a}\right)+r-\frac{N(\beta)}a.}
\tag{2.2}
\]
Equivalently, put
\[
s=\frac{be-2cd}{\Delta},\qquad
t=\frac{bd-2ae}{\Delta}.
\]
Then
\[
P(x,y)=q(x+s,y+t)+r-q(s,t),\qquad
q(s,t)=\frac{bde-cd^2-ae^2}{\Delta}.
\tag{2.3}
\]
The trace is therefore not an additional independent output operation. Its construction issue is the translated Cartesian input.

**PROVED, \(a=0\) case.** Here \(b\ne0\). In \(E=K\times K\), set
\[
z=(y,bx+cy),\qquad \beta=(e-cd/b,d/b).
\]
Then \(P=N(z)+\operatorname{Tr}(\beta z)+r=N(z+\bar\beta)+r-N(\beta)\). The input remains the correlated set \(\{(y,bx+cy):x,y\in A\}\), not the unrestricted product \(A\times(bA+cA)\). Swapping the variables preserves \(A^2\); general linear mixing need not.

### 2.2 Benchmark and same-set issue

**PROVED.** Write \(q(x,y)=x^2+xy+y^2\),
\[
\alpha=\frac{-1+\sqrt{-3}}2,\qquad
\beta=\frac12-\frac{\sqrt{-3}}6.
\]
Then \(\operatorname{Tr}\beta=1\), \(\operatorname{Tr}(\beta\alpha)=0\), \(N\beta=1/3\), and
\[
\boxed{P_0(x,y)=q(x+2/3,y-1/3)-1/3.}
\tag{2.4}
\]
For totally real \(K_j\), all norms and traces here are relative \(E_j/K_j\), where \(E_j=K_j(\sqrt{-3})\). Their values lie in \(K_j\). Inputs use a real embedding of \(K_j\); the extending embeddings of \(E_j\) are complex.

Writing \(B=A-1/3\) gives exactly
\[
P_0(A,A)=q(B+1,B)-1/3.
\tag{2.5}
\]
An arbitrary homogeneous witness \(C\) does not automatically contain both required shifts. Also, the target norm–trace image uses the **same** \(z\) in its two terms; replacing it by \(N(Z)+\operatorname{Tr}(\beta Z)\) loses correlation. A freely chosen \(Z=GB\subset E_j\) does not define a real input set without full containment of the corresponding \(A-\alpha A\).

### 2.3 A proved same-set transfer lemma

**PROVED.** Suppose a finite \(C\subset\mathbb R\), \(|C|=N\ge2\), satisfies
\[
|q(C,C)|\le K_*N^{2-c_0},\qquad
|C-C|\le D_*N^{1+\eta},
\]
where \(K_*,D_*\) are fixed, \(0<c_0\le1\), and \(0\le\eta<c_0/2\). There is an explicitly selected set \(A\) with
\[
|A|\ge(2D_*)^{-1}N^{1-\eta},\qquad
|P_0(A,A)|\le K_*(2D_*)^{2-c_1}|A|^{2-c_1},
\]
\[
\boxed{c_1=\frac{c_0-2\eta}{1-\eta}>0.}
\tag{2.6}
\]

**Proof.** Choose a nonzero difference \(\delta\in C-C\) maximizing \(|B|\), where \(B=C\cap(C-\delta)\); use increasing real order to break ties. The identity
\[
\sum_{\delta\ne0}|C\cap(C-\delta)|=N(N-1)
\]
gives \(|B|\ge N^{1-\eta}/(2D_*)\). Set \(A=B/\delta+1/3\). Then for all pairs,
\[
P_0(A,A)=\delta^{-2}q(B+\delta,B)-1/3
\subseteq\delta^{-2}q(C,C)-1/3.
\]
Using \(N\le(2D_*|A|)^{1/(1-\eta)}\) proves (2.6). Thus growing examples follow if its two hypotheses hold along a growing sequence. This is a transfer theorem, not evidence that its homogeneous witnesses exist. No such witness is established by the supplied constructions.

