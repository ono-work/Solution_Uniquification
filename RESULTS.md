# Results by problem and input restriction
[日本語](RESULTS.ja.md) · [Home](README.md) · [Reduction-source index](REDUCTIONS.md)

Edition 0.3 · 2026-11-07. **Read each row as one conjunction of hypotheses.** Planar + bipartite + Δ≤3 is stronger than any one condition alone; conditions from different rows cannot be combined. Δ is maximum degree, not regularity. Missing restrictions mean **not recorded**, not an open problem.

Each row separates the underlying problem, allowed clues, target supplied/selected, structural input restrictions, and parameter. S: statement checked in full text; A: primary abstract only; H: reported through another paper; D: elementary consequence explained here. These are access levels, not independent proof certification. [Sources and versions](SOURCES.md). n=|V|, m=|E|, τ is the original vertex-cover number; O* suppresses polynomial factors.

- [Pre-assignment for minimum vertex cover (PAU-VC)](#pau)
- [Vertex deletion to unique minimum vertex cover (MU-VC)](#mu)
- [Perfect matching](#matching)
- [SAT and Boolean defining sets](#sat)
- [Triangle partitions, Latin squares and puzzles](#puzzles)
- [Minimum spanning trees and minimum-weight bases](#mst)
- [Shortest s–t paths](#shortest)
- [Minimum cuts](#cut)
- [Optimal graph coloring](#coloring)
- [Maximum clique and minimum dominating set](#clique-dom)
- [General transfer theorem](#transfer)

<a id="pau"></a>
## Pre-assignment for minimum vertex cover (PAU-VC)

Solutions are the ORIGINAL minimum covers. INCLUDE fixes membership, EXCLUDE fixes non-membership, MIXED permits both. Each row states which models are covered. Planar subcubic and planar bipartite subcubic hardness are separate theorems with different complexity and model scope.

### Hardness

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| VC-H1 | General graphs | INCLUDE / EXCLUDE / MIXED; target selectable | Σ₂^P-complete | [P1](SOURCES.md#p1), Th. 6 | S |
| VC-H2 | Planar graphs, Δ ≤ 3 | All three models; target selectable | Σ₂^P-complete | [P9](SOURCES.md#p9), abstract | A |
| VC-H3 | Bipartite graphs | All three models; target selectable | NP-complete | [P1](SOURCES.md#p1), Ths. 13–14 | S |
| VC-H4 | Planar AND bipartite, Δ ≤ 3 | MIXED as defined in the primary abstract | NP-complete | [P11](SOURCES.md#p11), abstract | A |

### Algorithms

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| VC-A1 | General graphs | All three models | O(2.1996^n) | [P1](SOURCES.md#p1), Th. 15 | S |
| VC-A2 | Parameter τ: original vertex-cover number | All three models | O*(3.6791^τ) | [P1](SOURCES.md#p1), Ths. 16, 18 | S |
| VC-A3 | Bipartite graphs; historical bound | All three models | O(1.9181^n) | [P1](SOURCES.md#p1), §4.3 | S |
| VC-A4 | Bipartite graphs; improved bound | MIXED; do not infer INCLUDE-only applicability from the abstract | O(1.4143^n) | [P11](SOURCES.md#p11), abstract | A |
| VC-A5 | Trees; original bound | All three models | O(1.4143^n) | [P1](SOURCES.md#p1), §4.4 | S |
| VC-A6 | Parameter: clique-width cw | INCLUDE only | FPT; supplied w-expression: 2^{O(2^w)}n² | [P5](SOURCES.md#p5), Th. 1.1; §3.2 | S |
| VC-A7 | Trees | INCLUDE only | Polynomial time (bounded clique-width consequence) | [P5](SOURCES.md#p5), Th. 1.1; §3.1 | D |
| VC-A8 | Split graphs | INCLUDE only | Linear time | [P5](SOURCES.md#p5), Th. 5.1 | S |
| VC-A9 | Unit interval graphs | INCLUDE only | Linear time | [P5](SOURCES.md#p5), Th. 4.1 | S |

### Approximation

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| VC-X1 | Bipartite graphs | INCLUDE; minimum clue cost | No polynomial-time constant-factor approximation unless P=NP | [P5](SOURCES.md#p5), §6 | S |

<a id="mu"></a>
## Vertex deletion to unique minimum vertex cover (MU-VC)

Delete at most k vertices so the remaining graph has a unique minimum cover. No equality with the original optimum is required. Thus the planar degree-5 theorem is NOT a weaker version of the PAU planar degree-3 theorem. Width-expression bounds refer to supplied expressions; constructing a decomposition is a separate step.

### Hardness

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| MU-H1 | Planar graphs, Δ ≤ 5 | Vertex deletion; no original-optimum preservation | Σ₂^P-complete | [P6](SOURCES.md#p6), Th. 7 | S |

### Algorithms

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| MU-A1 | Trees | Vertex deletion | O(n) | [P6](SOURCES.md#p6), Th. 2 | S |
| MU-A2 | Treewidth w | Vertex deletion | XP: n^{O(2^w)} | [P6](SOURCES.md#p6), Th. 3 | S |
| MU-A3 | Treewidth w AND maximum degree Δ | Vertex deletion | FPT: Δ^{O(2^w)}n (decomposition DP) | [P6](SOURCES.md#p6), Th. 4 | S |
| MU-A4 | Supplied clique-width d-expression | Vertex deletion | XP: n^{O(2^d)} | [P6](SOURCES.md#p6), Th. 5; proof | S |
| MU-A5 | Supplied d-expression AND deletion budget k | Vertex deletion | FPT: k^{O(2^d)}n; handle k=0 separately | [P6](SOURCES.md#p6), Th. 6; proof | S |

<a id="matching"></a>
## Perfect matching

Forcing includes edges of the target matching; anti-forcing excludes edges outside it. Given and selectable targets are different problems. The bipartite degree-3 hardness below does NOT include planarity. For a supplied matching on plane bipartite graphs, forcing is polynomial-time. P14 footnote 1 reports that the older selectable-forcing construction claimed degree 4 but actually has degree 5; use its new degree-3 theorem instead.

### Hardness

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| PM-H1 | Bipartite, Δ ≤ 3 | Forcing; perfect matching M supplied | NP-complete | [P2](SOURCES.md#p2), reported in P12 Th. D and P14 §1 | H |
| PM-H2 | Bipartite, Δ ≤ 3 | Anti-forcing; M supplied | NP-complete | [P14](SOURCES.md#p14), Th. 3 | S |
| PM-H3 | Bipartite, Δ ≤ 3 | Forcing; M selectable | NP-complete | [P14](SOURCES.md#p14), Th. 4 | S |
| PM-H4 | Bipartite, Δ ≤ 3 | Anti-forcing; M selectable | NP-complete | [P14](SOURCES.md#p14), Th. 5 | S |

### Historical bounds

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| PM-O1 | Bipartite, Δ ≤ 4; superseded | Anti-forcing; M supplied | NP-complete | [P13](SOURCES.md#p13), abstract | A |
| PM-O2 | Bipartite; paper claims Δ ≤ 4, later correction says Δ ≤ 5 | Forcing; M selectable | Historical NP-completeness; use PM-H3 for Δ ≤ 3 | [P12](SOURCES.md#p12), Th. 7; P14 footnote 1 | H |

### Algorithms

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| PM-A1 | Plane bipartite graph | Forcing; M supplied | Polynomial-time algorithm reported in the literature | [P12](SOURCES.md#p12), Th. C; concluding discussion | H |
| PM-A2 | Graphs of maximum degree ≤ 2 | Forcing / anti-forcing; M given or selectable | Polynomial time; one clue per even-cycle component, if a perfect matching exists | [P14](SOURCES.md#p14), elementary component argument in survey | D |

**Degree-2 consequence (D).** Components are paths and cycles. If a perfect matching exists, each path component has a unique one; each even cycle has exactly two. Every ambiguous cycle needs at least one clue, and one included matching edge or one excluded nonmatching edge suffices. Odd paths/cycles without a perfect matching make the instance infeasible. This proves PM-A2 for all four variants.

<a id="sat"></a>
## SAT and Boolean defining sets

Clues fix variable values. Planar here refers to the formula/incidence-planarity notion used by P4, not a promise about a later graph gadget. Do not append bounded occurrence or monotonicity to these statements. Q1 verifies supplied clues; Q2 finds clues for a supplied solution; Q3 selects the solution too.

### Verification

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| SAT-V1 | 3CNF | Given satisfying assignment AND clue; Q1 | coNP-complete | [P3](SOURCES.md#p3), Th. 3 | S |

### Hardness

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| SAT-H1 | 3CNF | Given satisfying assignment; find clues; Q2 | Σ₂^P-complete | [P3](SOURCES.md#p3), Th. 4 | S |
| SAT-H2 | 3CNF | Target assignment selectable; Q3 | Σ₂^P-complete | [P3](SOURCES.md#p3), Th. 5 | S |
| SAT-H3 | Planar 3SAT (source paper’s planar formula model) | FCP; target selectable | Σ₂^P-complete | [P4](SOURCES.md#p4), Lemma 9 | S |
| SAT-H4 | Planar 1-in-3 SAT | FCP; target selectable; exactly one true literal per clause | Σ₂^P-complete | [P4](SOURCES.md#p4), Lemma 10 | S |
| SAT-H5 | 1-in-3 SAT | FCP; target selectable | Σ₂^P-complete | [P4](SOURCES.md#p4), Lemma 11 | S |
| SAT-H6 | 2CNF | FCP; target selectable | NP-complete | [P4](SOURCES.md#p4), Th. 18 | S |
| SAT-H7 | Positive planar 1-in-3SAT | FCP; choose variable-value clues and target | Σ₂^P-complete | [P7](SOURCES.md#p7), §5.3, Example A | S |
| SAT-H8 | 1-in-3SAT+: exactly three literals per clause | FCP; + denotes exact clause length, NOT positivity | Σ₂^P-complete | [P7](SOURCES.md#p7), §5.3, Example B | S |

### Prescribed variables: unique extension (related problem)

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| NAE-H1 | NAE-3SAT with Boolean constants; no planar/occurrence promise | Prescribed partition X,Y; choose values of X; unique extension to Y | Σ₂^P-hard | [P16](SOURCES.md#p16), §3.10, Th. 3.10.1 | S |
| NAE-H2 | NAE-3SAT without constants; repeated variables allowed | ∃X ∃!Y; X is prescribed, not a budgeted selectable clue set | Σ₂^P-complete (table); theorem proves hardness | [P16](SOURCES.md#p16), §3.10, Th. 3.10.2; survey table §2.1 | S |

**NAE model boundary.** P16 studies a prescribed partition X,Y: ∃x ∃!y φ(x,y). This is not the FCP problem of choosing any ≤k variable positions. The constant-free reduction uses NAE(T,T,F), so distinct variables per clause are not promised. With no constants, complementing every variable preserves solutions, but fixing X can break that symmetry. Do not infer monotone, planar or bounded-occurrence hardness.

<a id="puzzles"></a>
## Triangle partitions, Latin squares and puzzles

Triangle partition means partitioning EDGES into triangles, not vertices. Its tripartite restriction is a separate source case. Sudoku and the other puzzles are generalized input-size families; clue types are problem-specific.

### Hardness

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| PUZ-H1 | Generalized Sudoku; board size part of input | Additional cell-value clues; target selectable | Σ₂^P-complete | [P4](SOURCES.md#p4), Lemma 14 | S |
| PUZ-H2 | Shakashaka | Fix solution-cell states; target selectable | Σ₂^P-complete | [P4](SOURCES.md#p4), Lemma 15 | S |
| PUZ-H3 | Akari | Fix solution-cell states; target selectable | Σ₂^P-complete | [P4](SOURCES.md#p4), Lemma 16 | S |
| PUZ-H4 | Triangle EDGE partition; not vertex partition | Specify triangles in the decomposition | Σ₂^P-complete | [P4](SOURCES.md#p4), Th. 12 | S |
| PUZ-H5 | Tripartite graph; triangle EDGE partition | FCP | Σ₂^P-complete, used in the Latin-square reduction | [P4](SOURCES.md#p4), proof of Th. 13 | S |
| PUZ-H6 | Partial Latin square, variable order | Additional cell entries; target selectable | Σ₂^P-complete | [P4](SOURCES.md#p4), Th. 13 | S |
| PUZ-H7 | Generalized Minesweeper consistency | FCP; place bombs or displayed neighbor counts on undecided cells | Σ₂^P-complete | [P7](SOURCES.md#p7), Th. 6; Cor. 11 | S |

<a id="mst"></a>
## Minimum spanning trees and minimum-weight bases

The graph is undirected; the MST theorem permits weighted multigraphs and negative weights. Forcing includes target edges; anti-forcing excludes other edges. The O(m log n) bound for selectable targets is not automatically the bound for the supplied-target corollary.

### Algorithms

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| MST-A1 | Undirected weighted multigraph; weights may be negative | Forcing / anti-forcing; target selectable | O(m log n) | [P10](SOURCES.md#p10), Th. 1 | S |
| MST-A2 | Weighted matroid, independence-oracle input | Forcing / anti-forcing; target basis selectable | Polynomially many oracle calls and polynomial computation | [P10](SOURCES.md#p10), Th. 2 | S |
| MST-A3 | Same matroid input, minimum-weight basis supplied | Forcing / anti-forcing of that basis | Polynomial time (hence also for a supplied MST) | [P10](SOURCES.md#p10), Cor. 1 | S |

<a id="shortest"></a>
## Shortest s–t paths

Edge lengths are strictly positive. Directed algorithms also apply to undirected inputs as discussed in P10. The hard case already uses unweighted undirected graphs, but no planar or degree bound is recorded. Parameter d counts edges in an ORIGINAL shortest path (maximum over such paths), not weighted distance.

### Algorithms

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| SP-A1 | Directed graph, strictly positive edge lengths | Forcing; shortest path selectable | O(nm) | [P10](SOURCES.md#p10), Th. 3 | S |
| SP-A2 | Same input; undirected case also covered | Forcing; shortest path supplied | O(nm) | [P10](SOURCES.md#p10), Th. 3 and following paragraph | S |
| SP-A3 | Directed, strictly positive edge lengths | Anti-forcing; shortest path supplied | Polynomial time | [P10](SOURCES.md#p10), Th. 5 | S |

### Hardness

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| SP-H1 | Undirected AND unweighted graph | Anti-forcing; shortest path selectable | NP-complete | [P10](SOURCES.md#p10), Th. 4 | S |

### Parameterized algorithms

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| SP-H2 | Same unweighted undirected input | Anti-forcing; parameter d = shortest-path edge length | W[1]-hard in d | [P10](SOURCES.md#p10), Th. 4 | S |
| SP-A4 | Strictly positive lengths; d = maximum edge count of an original shortest path | Anti-forcing; budget k; target selectable | d^k n^{O(1)}; FPT in k+d | [P10](SOURCES.md#p10), Th. 6 | S |
| SP-A5 | Same input and definition of d | Anti-forcing; budget k | (k+1)^d n^{O(1)}; FPT in k+d | [P10](SOURCES.md#p10), Th. 7 | S |
| SP-A6 | Directed; underlying undirected graph has bounded treewidth | Anti-forcing; shortest path selectable | Linear time for each fixed treewidth | [P10](SOURCES.md#p10), Th. 8 | S |

<a id="cut"></a>
## Minimum cuts

All inputs here are UNDIRECTED, with positive integer edge weights for the algorithms. Solutions are edge cutsets, not oriented shore descriptions. Global versus s–t, forcing versus anti-forcing, and supplied versus selectable target give eight cases. A directed residual graph inside an algorithm does not make the input directed.

### Global cuts

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| CUT-A1 | Undirected, positive integer edge weights | Global min cut; forcing; target selectable | O(m polylog n) | [P8](SOURCES.md#p8), Th. 3.1 | S |
| CUT-A2 | Same input | Global min cut; forcing; target cut supplied | O(m polylog n) | [P8](SOURCES.md#p8), Cor. 1 | S |
| CUT-H1 | Unweighted simple undirected graph | Global min cut; anti-forcing; target selectable | NP-complete | [P8](SOURCES.md#p8), Th. 3.3 | S |
| CUT-H2 | Unweighted simple undirected graph | Global min cut; anti-forcing; target supplied | NP-complete | [P8](SOURCES.md#p8), Cor. 2 | S |

### s–t cuts

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| CUT-H3 | Unweighted undirected graph; simple via Lemma 1 | Min s–t cut; forcing; target selectable | NP-complete | [P8](SOURCES.md#p8), Th. 4.3; Lemma 1 | S |
| CUT-H4 | Unweighted undirected graph; simple via Lemma 1 | Min s–t cut; anti-forcing; target selectable | NP-complete | [P8](SOURCES.md#p8), Th. 4.4; Lemma 1 | S |
| CUT-A3 | Undirected, positive integer edge weights | Min s–t cut; forcing; target cut supplied | O(nm) | [P8](SOURCES.md#p8), Th. 4.5 | S |
| CUT-A4 | Undirected, positive integer edge weights | Min s–t cut; anti-forcing; target supplied | O(nm) | [P8](SOURCES.md#p8), Th. 4.6 | S |

<a id="coloring"></a>
## Optimal graph coloring

Clues fix named colors in an optimal coloring. Variable-budget defining-set results differ from fixed-k forcing-chromatic-number results. χ(G)≤3 bounds the chromatic number, NOT maximum degree. A supplied vertex set without its color values is not the same input as supplied partial coloring.

### Input budget k

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| COL-H1 | χ(G)=3; optimal coloring c supplied | Find ≤ k named-color clues for c; k is input | Σ₂^P-complete | [P3](SOURCES.md#p3), Th. 7 | S |
| COL-H2 | χ(G)=3 | Choose an optimal coloring and ≤ k clues; k is input | Σ₂^P-complete | [P3](SOURCES.md#p3), Th. 8 | S |

### Fixed budget k / related verification

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| COL-V1 | General graph; two specified vertices | Ask whether that vertex set forces some optimal coloring | US-complete; values are NOT supplied | [P15](SOURCES.md#p15), Prop. 2.8 | S |
| COL-H3 | Connected graphs; each fixed k ≥ 2 | Does Fχ(G) ≤ k? | US-hard (many-one) | [P15](SOURCES.md#p15), Th. 3.1 | S |
| COL-H4 | χ(G) ≤ 3 AND Fχ(G) ≤ 3; proper 3-coloring supplied | Decide whether Fχ(G) ≤ 2 | coNP-hard under this promise | [P15](SOURCES.md#p15), Th. 4.1 | S |
| COL-A1 | Each fixed k; no planar/degree promise added | Fχ(G) ≤ k | In P_dtt(US); not a many-one completeness statement | [P15](SOURCES.md#p15), Th. 8.2 | S |

<a id="clique-dom"></a>
## Maximum clique and minimum dominating set

These are INCLUDE clues among ORIGINAL optima, with selectable targets. Each k is a fixed constant in these results. US-hardness and P_dtt(US) membership are separate claims; do not combine them into an unsupported completeness statement or an FPT algorithm.

### Maximum clique

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| CLQ-H1 | General graphs; each fixed k ≥ 0 | INCLUDE among maximum cliques; target selectable | US-hard | [P15](SOURCES.md#p15), Th. 7.5 | S |
| CLQ-A1 | Same input | Fω(G) ≤ k | In P_dtt(US) | [P15](SOURCES.md#p15), Th. 8.2 | S |

### Minimum dominating set

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| DOM-H1 | General graphs; each fixed k ≥ 0 | INCLUDE among minimum dominating sets; target selectable | US-hard | [P15](SOURCES.md#p15), Th. 7.5 | S |
| DOM-A1 | Same input | Fγ(G) ≤ k | In P_dtt(US) | [P15](SOURCES.md#p15), Th. 8.2 | S |

<a id="transfer"></a>
## General transfer theorem

This is a model-level theorem, not a structural graph subclass. Parsimoniousness alone is insufficient: coordinate alignment and the full source hypotheses must also be checked. The final full-text Theorem 4 and its checklist have been checked.

### Transfer

| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |
|---|---|---|---|---|---|
| META-1 | Source NP problem with Σ₂^P-complete FCP; aligned parsimonious reduction | FCP transfer; target certificates polynomially checkable | Transfers Σ₂^P-completeness under the formal hypotheses | [P7](SOURCES.md#p7), Th. 4; §3; checklist §5.3 | S |

## Coverage and maintenance

This is a selective catalogue, not a complete classification of every graph class. In particular, no selectable-target planar-matching classification, planar shortest-path hardness, bounded-degree cut hardness, or all-model extension of the P11 abstract is asserted. These are literature-checking gaps, not declarations of open problems.

[Machine-readable records](data/results.json) · [Reduction maps](REDUCTIONS.md) · [Verification](VERIFICATION.md)
