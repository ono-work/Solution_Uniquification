# Choosing a hardness reduction source
[日本語](REDUCTIONS.ja.md) · [Full problem catalogue](RESULTS.md)

## Restricted hard source problems

Each row is a simultaneous restriction. Do not combine properties across rows. A new reduction must separately prove which properties its output preserves.

| Result ID | Source / clue model | Simultaneous restrictions | Hardness |
|---|---|---|---|
| [VC-H2](RESULTS.md#pau) | PAU-VC, INCLUDE / EXCLUDE / MIXED | Planar; Δ≤3 | Σ₂^P-complete |
| [VC-H4](RESULTS.md#pau) | PAU-VC, MIXED | Planar AND bipartite; Δ≤3 | NP-complete |
| [MU-H1](RESULTS.md#mu) | MU-VC, deletion | Planar; Δ≤5 | Σ₂^P-complete |
| [PM-H1–H4](RESULTS.md#matching) | Perfect matching, four variants | Bipartite; Δ≤3; no planar promise | NP-complete |
| [SAT-H3](RESULTS.md#sat) | FCP planar 3SAT | P4 formula-planarity; no occurrence bound recorded | Σ₂^P-complete |
| [SAT-H4](RESULTS.md#sat) | FCP planar 1-in-3SAT | P4 formula-planarity | Σ₂^P-complete |
| [PUZ-H5](RESULTS.md#puzzles) | FCP edge triangle partition | Tripartite | Σ₂^P-complete |
| [SP-H1](RESULTS.md#shortest) | Shortest path, selectable anti-forcing | Unweighted undirected; no planar/degree promise | NP-complete; W[1]-hard in d |
| [CUT-H1–H4](RESULTS.md#cut) | Minimum cut, specified variants | Unweighted simple undirected; no planar/degree promise | NP-complete |
| [COL-H1–H2](RESULTS.md#coloring) | Optimal-coloring defining set | χ(G)=3; NOT Δ≤3 | Σ₂^P-complete |

## Actual reductions and preservation

| Source | Reduction | Budget / preservation | Boundary for reuse |
|---|---|---|---|
| [P14](SOURCES.md#p14), Ths. 1–2; Lemma 6 | Matching forcing → anti-forcing (given → given; selectable → selectable) | Replace each edge by a 3-edge path; same k; perfect-matching bijection; bipartiteness and Δ≥2 preserved | Subdivision also preserves planarity, but the hard source is not proved planar |
| [P14](SOURCES.md#p14), Lemma 10 | Selectable matching forcing, degree 5 → degree 3 | Linear-size vertex gadgets; same k | Bipartite hardness; do not add planarity |
| [P10](SOURCES.md#p10), Th. 4 | Multicolored Biclique → selectable shortest-path anti-forcing | Source parts of size N, parameter q: K=2q(N−1), d=6q−1; unweighted undirected | Many bypass paths; no planar or maximum-degree bound recorded |
| [P8](SOURCES.md#p8), Ths. 4.3–4.4 | Vertex Cover → selectable min s–t cut forcing / anti-forcing | Budget n+k; forcing construction starts with 4-regular VC | 4-regular SOURCE does not imply degree-4 OUTPUT |
| [P8](SOURCES.md#p8), Lemma 1 | Weighted multigraph cuts → unweighted simple graph cuts | Cut correspondence; polynomial construction for polynomially bounded weights | Vertex-replacement cliques do not preserve planarity or bounded degree |
| [P7](SOURCES.md#p7), abstract | General FCP transfer | Parsimonious solution map AND coordinate alignment AND source hypotheses | Abstract only; full formal statement must be checked for a new proof |

## Adding further subclasses

Record the graph class (including intersections), maximum degree versus regularity, weights and direction, target supplied/selected, clue types, budget map and size blow-up together. This index covers checked sources, not every possible subclass. An unlisted case is not declared open.
