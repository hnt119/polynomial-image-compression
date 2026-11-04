# Exact scouting: complete return distributions

**EXPERIMENTAL, 16 September 2026.** Every ordered pair and every displayed action is enumerated exactly. No fitted asymptotic exponent is used.

## Summary

| Family | H | Depth | n | Full Q image | Actions | Nonzero return histogram R:count | Identity-only % | Median | Geometric mean |
|---|---:|---:|---:|---:|---:|---|---:|---:|---:|
| strata | 1 | 2 | 6 | 12 | 5 | 1:36 | 100.000 | 1 | 1.000000 |
| strata | 1 | 4 | 10 | 30 | 9 | 1:100 | 100.000 | 1 | 1.000000 |
| strata | 1 | 8 | 18 | 90 | 17 | 1:324 | 100.000 | 1 | 1.000000 |
| strata | 2 | 2 | 12 | 39 | 5 | 1:144 | 100.000 | 1 | 1.000000 |
| strata | 2 | 4 | 20 | 105 | 9 | 1:400 | 100.000 | 1 | 1.000000 |
| strata | 2 | 8 | 36 | 333 | 17 | 1:1296 | 100.000 | 1 | 1.000000 |
| strata | 4 | 2 | 24 | 134 | 5 | 1:528, 2:48 | 91.667 | 1 | 1.059463 |
| strata | 4 | 4 | 40 | 382 | 9 | 1:1520, 2:80 | 95.000 | 1 | 1.035265 |
| strata | 4 | 8 | 72 | 1262 | 17 | 1:5040, 2:144 | 97.222 | 1 | 1.019441 |
| strata | 8 | 4 | 70 | 1116 | 9 | 1:4632, 2:244, 3:24 | 94.531 | 1 | 1.040703 |
| strata | 16 | 4 | 140 | 4272 | 9 | 1:18560, 2:920, 3:120 | 94.694 | 1 | 1.040043 |
| orbit_box | 1 | 1 | 13 | 32 | 7 | 1:136, 2:8, 3:24 | 80.952 | 1 | 1.209191 |
| orbit_box | 1 | 2 | 23 | 112 | 11 | 1:480, 2:8, 5:40 | 90.909 | 1 | 1.141598 |
| orbit_box | 1 | 4 | 43 | 422 | 19 | 1:1768, 2:8, 9:72 | 95.671 | 1 | 1.092651 |
| orbit_box | 1 | 8 | 83 | 1642 | 35 | 1:6744, 2:8, 17:136 | 97.909 | 1 | 1.058386 |
| repair | 1 | 0 | 3 | 3 | 1 | 1:8 | 100.000 | 1 | 1.000000 |
| repair | 1 | 1 | 13 | 32 | 7 | 1:136, 2:8, 3:24 | 80.952 | 1 | 1.209191 |
| repair | 1 | 2 | 121 | 2129 | 11 | 1:12180, 2:1972, 3:432, 4:16, 5:40 | 83.197 | 1 | 1.140763 |

Percentages and geometric means are descriptive floating-point summaries of the exact histograms. All medians are exactly 1. The minimum outside the declared zero exception is exactly 1 in every case.

## Exact meaning and zero/stabilizer audit

The action is multiplication by powers of u=(8+5ω)/7 on z=x−ωy. The listed finite exponent windows contain **all returning integer powers for every nonzero pair**, by the proved valuation/height cutoffs. At zero, infinitely many powers return; only the displayed finite family is counted.

For every nonzero pair the action is free: its raw return count equals the number of distinct returned pairs, and its stabilizer within the selected family has size 1. Strata carriers exclude zero. Each orbit-box and repair carrier includes exactly one zero pair; its raw return and stabilizer counts equal the Actions column, but it has exactly one distinct returned pair. These rules together with the table specify the complete raw-return, distinct-return, and stabilizer distributions for every case.

Threshold exceptional sets are defined exactly as E_M={zero, if present}∪{nonzero pairs with R<M}. The compact JSON records their cardinalities, the minimum outside each E_M, and the certified support upper bounds for M=1,2,3,4,8,16,32 and each observed maximum. No constant fraction is treated as a negligible exception.

## Full image multiplicities

Each entry below is fiber size:number of outputs. Summing the counts gives the full image size; summing size×count gives n².

| Family | H | Depth | Full fiber histogram |
|---|---:|---:|---|
| strata | 1 | 2 | 2:6, 4:6 |
| strata | 1 | 4 | 2:10, 4:20 |
| strata | 1 | 8 | 2:18, 4:72 |
| strata | 2 | 2 | 2:9, 4:27, 6:3 |
| strata | 2 | 4 | 2:15, 4:85, 6:5 |
| strata | 2 | 8 | 2:27, 4:297, 6:9 |
| strata | 4 | 2 | 2:18, 4:102, 6:6, 12:8 |
| strata | 4 | 4 | 2:30, 4:328, 6:10, 12:14 |
| strata | 4 | 8 | 2:54, 4:1164, 6:18, 12:26 |
| strata | 8 | 4 | 2:46, 4:990, 6:20, 12:56, 14:4 |
| strata | 16 | 4 | 2:88, 4:3820, 6:36, 8:49, 12:248, 14:12, 16:5, 18:4, 24:10 |
| orbit_box | 1 | 1 | 1:1, 2:5, 4:16, 6:5, 10:1, 12:3, 18:1 |
| orbit_box | 1 | 2 | 1:1, 2:10, 4:82, 6:9, 8:2, 10:2, 12:5, 30:1 |
| orbit_box | 1 | 4 | 1:1, 2:20, 4:364, 6:19, 8:6, 10:1, 12:9, 18:1, 54:1 |
| orbit_box | 1 | 8 | 1:1, 2:40, 4:1528, 6:39, 8:14, 10:1, 12:17, 34:1, 102:1 |
| repair | 1 | 0 | 1:1, 2:1, 6:1 |
| repair | 1 | 1 | 1:1, 2:5, 4:16, 6:5, 10:1, 12:3, 18:1 |
| repair | 1 | 2 | 1:1, 2:43, 4:1328, 6:55, 8:221, 10:7, 12:313, 14:1, 16:76, 18:12, 20:3, 24:56, 28:2, 30:1, 32:2, 36:4, 40:2, 46:1, 48:1 |

## State transitions and structured-pair coverage

Every scalar state is its exact rational 7-adic valuation, with zero separate. Raw JSON records the complete transition count from (v7(x),v7(y)) to the returned pair of valuations, summed over every returning label. These edges are diagnostics, not independent output states or entropy gains.

Orbit-box engineered pair counts at J=1,2,4,8 are 25,41,73,137, in completed squares of size 169,529,1849,6889. Their density decreases. Repair stage sizes are 3,13,121. At depth 2 only 169 of 14,641 pairs belong to the preceding square where the construction directly guarantees u and u⁻¹ returns.

## Reproducibility and finite budget

Command:

```sh
python3 -m experiments.cartesian_returns --output local-only/runs/T03/2026-09-16-high-return/results.json
```

The program refuses an existing output path; choose a fresh path for a rerun. The fixed schedule is 11 strata cases, four orbit-box cases, and three repair stages (18 cases). The common first repair/orbit level is disclosed as the same set, not counted as an independent mechanism.

Runtime: Python 3.12.7. Research run: **863,636 charged evaluations**, **0.468425 CPU seconds**, zero errors. Counts: {'construction_action': 680, 'multiplier_norm': 202, 'polynomial': 58415, 'return_action': 804339}. Budget cap: 2,000,000 evaluations and 600 CPU seconds. The CPU guard is sampled every 256 evaluations and checked at completion; it is not an operating-system hard timeout.

No random seed: the schedule and enumeration are deterministic. No imported archived program, new dependency, floating-point collision test, or numerical field embedding is used. Full input lists, common denominators, input/code/output hashes, transition graphs and exact histograms are in the ignored raw result. A compact portable report is [the example JSON](../../../examples/2026-09-16-cartesian-returns.json); code is [cartesian_returns.py](../../../experiments/cartesian_returns.py). Mathematical regressions and repository checks are separately reported in the main research report.

The finite observations agree with the analytic obstructions. They neither prove those theorems nor exclude other real carriers.
