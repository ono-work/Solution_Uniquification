# Selected results
[日本語](RESULTS.ja.md) · [Home](README.md)

These are results reported by the cited authors, not new claims of this survey. “S” means a statement was located in accessible full text, not that its proof was independently validated. “A” means the primary abstract was checked. “H” is historical reporting through another paper. See [Sources](SOURCES.md). This is not a table of best known bounds for every model.

Let n=|V(G)|, τ=τ(G), and L be encoded input length. O* suppresses polynomial factors. Each row has its own scope.

| ID | Problem / solution family | Target and clues | Result | Source / locator | Evidence |
|---|---|---|---|---|---|
| R01 | 3SAT satisfying assignments | Given target and clue; verification (Q1) | coNP-complete | [P3](SOURCES.md#p3), Theorem 3 | S |
| R02 | 3SAT satisfying assignments | Given target; choose variable values (Q2) | Σ₂^P-complete | P3, Theorem 4 | S |
| R03 | 3SAT satisfying assignments | Target selectable; choose variable values (Q3) | Σ₂^P-complete | P3, Theorem 5 | S |
| R04 | FCP: generalized Sudoku, Shakashaka, Akari | Target selectable; puzzle-specific certificate coordinates | Σ₂^P-complete | [P4](SOURCES.md#p4), §4 | S |
| R05 | FCP 2SAT | Target selectable; variable-value clues | NP-complete | P4, Theorem 18 | S |
| R06 | PAU-VC, general graphs, original minimum covers | Target selectable; INCLUDE / EXCLUDE / MIXED | Σ₂^P-complete | [P1](SOURCES.md#p1), Theorem 6 | S |
| R07 | PAU-VC, bipartite graphs | Same three models | NP-complete | P1, Theorems 13–14 | S |
| R08 | PAU-VC, general graphs | Same three models | O(2.1996^n); O*(3.6791^τ) | P1, §4 | S |
| R09 | PAU-VC, bipartite graphs | Same three models | Historical O(1.9181^n) bound | P1, §1.1 and §4 | S |
| R10 | Min PAU-VC | INCLUDE only | FPT in clique-width | [P5](SOURCES.md#p5), Theorem 1.1 | S |
| R11 | Min PAU-VC, split / unit interval graphs | INCLUDE only | Linear time | P5, Theorem 1.2 | S |
| R12 | MU-VC: delete vertices to obtain a unique minimum cover | Deleted vertices; no original-optimum preservation condition | Σ₂^P-complete, even planar maximum degree 5 | [P6](SOURCES.md#p6), abstract | A |
| R13 | MU-VC | Same deletion model | Linear on trees; FPT in treewidth + maximum degree; XP in clique-width, FPT in clique-width + deletion budget | P6, abstract | A |
| R14 | FCP transfer theorem | Certificate-aligned parsimonious reductions, plus hypotheses on the source | Transfers Σ₂^P-completeness | [P7](SOURCES.md#p7), abstract | A |

| R15 | PAU-VC, planar maximum degree 3 | Target selectable; all three models | Σ₂^P-complete | [P9](SOURCES.md#p9), abstract | A |
| R16 | PAU-VC, bipartite graphs | MIXED as formulated in the abstract | O(1.4143^n); NP-complete even planar maximum degree 3 | [P11](SOURCES.md#p11), abstract | A |
| R17 | Minimum-weight spanning tree | Target selectable; forcing / anti-forcing | Polynomial-time algorithms | [P10](SOURCES.md#p10), v4 abstract | A |
| R18 | Shortest s–t path | Target selectable; forcing versus anti-forcing | Forcing polynomial; anti-forcing decision NP-complete | P10, v4 abstract; detailed weight assumptions require full text | A |

The tree question in the 2024 PAU paper has a positive answer for INCLUDE via R10, since trees have bounded clique-width. Do not use R10 to infer the same statement for EXCLUDE or MIXED. R09 is retained to show the original result, not advertised as the current best bound.

For R10, the full-text proof gives 2^{O(2^w)}n² time with a supplied clique-width w-expression (§3.2). The FPT assertion also accounts for finding an approximate expression. Do not replace w by the optimum clique-width in that displayed expression-dependent bound.

## Recent minimum-cut work

[P8](SOURCES.md#p8) studies forcing and anti-forcing for global and s–t minimum cuts, with both supplied and selectable optimal targets. Its primary indexed abstract reports polynomial-time algorithms or NP-completeness for every variant. The exact per-variant classification is not reproduced here until the full text is checked.

R16 confirms an improvement over historical R09 for the stated MIXED setting. R17–R18 quote the current v4 abstract; do not silently attribute the expanded author list to the earlier conference paper. Check the full text before applying their algorithms to a particular weight model.

## Historical matching entry

| Problem | Target | Reported result | Status |
|---|---|---|---|
| Minimum forcing set for a perfect matching | Matching supplied; require selected matching edges | NP-complete | [P2](SOURCES.md#p2), reported in P3 §1; original proof not inspected here (H) |

This separates a long-established result from the present edition's limited evidence access. Do not promote a restricted-degree version without locating its original theorem.

## Interpretation

R01 versus R02 separates verifying a clue from finding one. R06 versus R12 compares different models, not two bounds for the same problem. R07 and R05 show that easy underlying optimization or feasibility does not by itself make minimum clues easy. R10 resolves one historical tree case, not every pre-assignment model.

The catalogue does not infer approximation ratios, ETH bounds or complexity-class collapses from these entries.

