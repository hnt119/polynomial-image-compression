# Edits for the v6 report editor

Apply these three text changes to a future report revision. Page numbers refer to the printed footer, with the physical PDF page in parentheses. The displayed equations are correct in the supplied report.

| Location | Existing text to replace | Replacement LaTeX |
|---|---|---|
| §4.1, p. 14 (16), immediately after the definition of $A$ | `where $h\ne0$ is a most frequent difference.` | `where $h$ maximizes $\lvert C\cap(C-h)\rvert$ among the nonzero differences in $C-C$.` |
| §4.2, p. 15 (17), final sentence before “To count the returns” | `Many candidates are therefore available even though a lower bound for their actual returns remains unknown.` | `The units $1$ and $-1$ give two distinct returning targets at every nonzero source. An exponential lower bound for the mean number of actual returns remains open.` |
| §4.2, p. 15 (17), immediately after (18) | `For example, three points in an orbit intersection contribute $3(1/3)=1$.` | `Each orbit intersection of size $m$ contributes $m(1/m)=1$ to the sum.` |

Zero has difference multiplicity $|C|$. The proof maximizes over nonzero differences. For the centrally symmetric unit carrier, $-1$ pairs every nonzero source with its distinct negative in the same orbit intersection. All such intersections therefore have even cardinality. The reciprocal-orbit formula and its separate origin term follow as printed. [Proof and locations](norm-and-units.md)

**Bibliography.** Use the [single replacement entry for reference 14](ref14-editor.tex) at the coordinated edit. It adds the locator for the conditional RC15/4 consequence in §7. For reference [15] use the previously published **Sections 1–5** entry. Its §§4–5 contain the exceptional-set bound and image consequence. References [5]–[13] and [16] need no change from the [published bibliography](../../2026-11-05-report-references/bibliography-github.tex). The [cubic owner’s reference 17 fragment](https://github.com/hnt119/polynomial-image-compression/blob/1ebe48fa718b8dbd8b4cbed544daf98854d5f5f7/research/exports/2026-11-05-report-audit/cubic/citation-snippets.tex) retains the published entry. Use that handoff for the combined edit. These changes preserve the existing keys and source-support pin.

**Keep the displayed formulas.** In Appendix C.2, printed pp. 22–23 (24–25), the half factor in the cutoff is present. In Appendix C.6, printed p. 26 (28), both bars in `\bigl|\gamma Q_\omega(U,U)\bigr|` are visible. In §3 the scope of nonspecialness and of compression already differ correctly. The cited quartic width applies to the continuous translated square and was proved at the chosen radius. [Radical check](bff-and-radicals.md) · [Quartic check](quartic.md)
