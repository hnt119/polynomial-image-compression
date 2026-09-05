# T03 status and history

**Ultimate Eisenstein target and PTCR: OPEN IN THE AVAILABLE RECORD.**
**Recent constructive direction: global reassignment with deficit contraction.**

## Sequence of results

1. Earlier local work develops [correlated CRT](../../history-sources/Q_Correlated_CRT_Tensorization_Checkpoint.md)
   and [weighted inequalities](../../history-sources/Q_Weighted_Local_Inequality_Checkpoint.md).
   The latter reports an all-depth residue-$13$ theorem, while retaining the
   general weighted problem as open. These are local results, not the real-set target.
2. [The constructive push](../../history-sources/Q_Final_Constructive_Push.md)
   gives a balanced code with $4^m$ engineered pairs and $3^m$ norm values.
   Its missing requirement is near-Cartesian coverage, including unengineered pairs.
3. [The CR verdict](../../history-sources/Norm_Preserving_Cartesianization_CR_Verdict.md),
   main theorem and §§G–I, refutes the original untwisted Cartesianization:
   pairs with $v_3(Q_E(a,b))=0$ have density at most $2/3$ in a rational square.
   The source's stronger code deficit is
   $$|A|^2-4^m\ge |A|^2/3+2^m.$$
   This closes that intermediate conjecture, not the ultimate $Q_E$ target.
4. The same report introduces the parity twist. It preserves the
   $4^m$-to-$3^m$ count and has the exact one-coordinate gadget $A_1=\{1,2\}$.
5. [The composition report](../../history-sources/Parity_Twisted_Cartesianization_Composition_Report.md),
   §§B–G, records obstructions to Exact-PTCR for $m\ge2$, natural binary
   placement, endpoint-local/affine recursions, and ordinary repetition of a
   fixed imperfect block. Arbitrary near-Cartesian reassignment remains open.

These are attributed source results; the import does not certify every proof or
rerun the historical C++ searches.

## Concrete finite example

For $(r_1,q_1)=(2,7)$ and $(r_2,q_2)=(5,31)$, the composition report, §C, gives

$$A_2=\{-25,-10,-5,-2,-1,26\}.$$

It realizes the 16 required directed code cells, with nine engineered norm
values. Its deficit is $6^2-16=20$ and its full $Q_E$ image has 19 values.
The report proves minimality among **integer** carriers for its prescribed
histogram; that is not a claim of minimality among all rational carriers.
No working asymptotic composition of this example is reported.

## Current next step and adversarial alternative

The latest task continuation prioritizes global repacking satisfying the strict
recurrence threshold in [SPEC.md](SPEC.md). A coefficient $4^k$ does not contract
old deficit; ordinary repetition of an imperfect block loses density.

Preserve also the report's §I **cube-shadow triangle-gap lemma** as an open
adversarial alternative. If established under its precise permutation-invariant
hypotheses, it would refute PTCR. It would still not disprove arbitrary
Eisenstein norm compression. The next constructive prompt did not settle or
erase that alternative.
