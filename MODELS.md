# Models
[日本語](MODELS.ja.md) · [Home](README.md)

## 1. Start with a solution family

Fix an instance I and its representation. Let F(I) be a finite family of distinct solutions. For optimization, let Opt(I) be the family attaining the original optimum. The representation matters: coordinates may be vertices, edges, variable values or cell symbols. Auxiliary variables and symmetry conventions may change what counts as a distinct solution.

For Boolean vectors y in {0,1}^m, a clue is a partial function c:D→{0,1}. Its cost here is |D|. Define

$$F(I;c)=\{y\in F(I): y_i=c(i)\ \text{for all }i\in D\}.$$

A clue succeeds when |F(I;c)|=1, not when this number is at most one. An unsolvable instance cannot be uniquified by merely restricting its solutions.

## 2. Three different questions

| Task | Input beyond I | Question |
|---|---|---|
| Verify a clue | target y and clue c consistent with y | Is y the only compatible solution? |
| Uniquify a fixed target | y and budget k | Can at most k clues identify y? |
| Select and uniquify a target | budget k | Can at most k clues identify some solution? |

These mirror the Q1/Q2/Q3 distinction in [P3](SOURCES.md#p3). Knowing one solution does not necessarily make finding a short defining set easy. See [Results](RESULTS.md).

For a family of subsets of a universe U, clues may be expressed by disjoint sets A,B⊆U:

$$F(I;A,B)=\{S\in F(I): A\subseteq S,\ S\cap B=\varnothing\}.$$

INCLUDE restricts B=∅; EXCLUDE restricts A=∅; MIXED allows both. The budget is |A|+|B|. For a fixed target T, require A⊆T and B⊆U\T. A defining set in the positive set-family sense corresponds to INCLUDE. For assignments represented as sets of (variable,value) pairs, a positive defining set of pairs can express both Boolean values. Thus the word “positive” depends on representation.

## 3. Feasible solutions versus original optimal solutions

For pre-assignment among original optima, success means

$$|\{S\in\operatorname{Opt}(I):A\subseteq S,\ S\cap B=\varnothing\}|=1.$$

This differs from taking all feasible solutions satisfying the clues and then optimizing within that restricted family. The restricted optimum may be worse than the original one.

Example: in the path a-b-c, the unique original minimum cover is {b}. Requiring both a and c yields the unique constrained minimum cover {a,c}, of size 2. No original optimum satisfies those clues. This is a successful constrained reoptimization, but an unsuccessful PAU clue.

For a minimization problem write opt(I;c) for the restricted optimum. The two models coincide for a particular clue if it is feasible and opt(I;c)=opt(I). That equality must be established.

## 4. Deletion versus preservation for vertex cover

For an INCLUDE set A, covers containing A correspond bijectively to covers of G-A by C↦C\A. Consequently

$$\min_{C\text{ cover of }G,\ A\subseteq C}|C|=|A|+\tau(G-A).$$

Therefore INCLUDE succeeds among original minimum covers exactly when BOTH hold:

1. G-A has a unique minimum vertex cover.
2. τ(G-A)=τ(G)-|A|.

Deleting vertices until the remainder has a unique minimum cover only requires the first condition. This is the distinction between the INCLUDE setting and the neighboring MU-VC model [P6](SOURCES.md#p6).

## 5. Vocabulary across subjects

| Term | Working interpretation; check each source |
|---|---|
| Forcing / defining set | A partial specification identifying a target in a specified family |
| Anti-forcing set | Negative specification; in matching, deletion of edges outside a target |
| Fewest clues | Find a smallest partial certificate with one completion |
| PAU | Pre-assignment among original optimal solutions, with model specified |
| Critical set | Commonly a defining partial structure minimal under deletion; conventions vary |
| Global distinguishing set | A single coordinate set separating every pair of solutions |
| Unique-solution recognition | Ask whether there is already exactly one solution |
| Isolation | Restrict or perturb solutions, often probabilistically; budget and success notions differ |

For coloring, decide whether colors are named or color permutations identify the same answer. For cuts, decide whether the solution is an edge set or a vertex bipartition and whether complementary sides are identified. These are mathematical choices, not formatting details.

## 6. Parameters

Distinguish clue budget k, optimum solution size τ, and structural width w. FPT in τ says nothing immediate about FPT in k. FPT means time f(k)L^c for computable f and constant c independent of k. XP permits L^{g(k)}. A supplied width expression is also an input assumption; record it when quoting a quantitative running time.

