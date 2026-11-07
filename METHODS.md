# Common methods
[日本語](METHODS.ja.md) · [Home](README.md)

The elementary derivations below are teaching notes, not claims of new results.

## 1. Every rival must disagree with a chosen clue

Fix a vector solution y and let z range over F(I)\{y}. Define Δ(y,z)={i:y_i≠z_i}. Specifying y on D identifies it exactly when

$$D\cap\Delta(y,z)\ne\varnothing\quad\text{for every rival }z.$$

Proof: a rival survives precisely when it agrees on every chosen coordinate. Negating that condition gives the formula.

Thus fixed-target identification is a hitting-set problem over the difference sets. If the target may be chosen, minimize this hitting-set cost over y∈F(I). The family may have exponentially many rivals; this equivalence alone is not a polynomial-time reduction producing an explicit small hypergraph.

For subset solutions T,S⊆U, INCLUDE must hit T\S with A⊆T; EXCLUDE must hit S\T with B⊆U\T. MIXED can use both types of distinguishing literals. In Opt(I), replace the entire feasible family by the original optima before forming these differences.

## 2. Local and global distinctions

A fixed target y requires hitting Δ(y,z) for its rivals only. A coordinate set distinguishing *every pair* must hit Δ(y,z) for every distinct pair. These objectives need not agree.

For F={000,100,010,001}, identifying target 100 needs only the first coordinate set to 1. Identifying 000 needs all three coordinates set to 0. Distinguishing all four solutions also needs all three coordinates. Hence fixed-target optimum, best-target optimum and global distinguishing optimum are different quantities.

## 3. Verify by searching for a counterexample

For SAT with a known satisfying assignment y and clues c, a second solution exists exactly when

$$F(x)\land c(x)\land\bigvee_{i=1}^m(x_i\ne y_i)$$

is satisfiable. An unsatisfiable formula certifies uniqueness relative to that target and the chosen notion of solution. If the encoding introduces auxiliary variables, blocking all encoded variables and blocking only original variables ask different questions.

For an unweighted graph, first obtain τ(G). A rival minimum cover can be tested by a cover constraint, cardinality τ(G), the clue constraints and C≠T. Guessing a clue does not erase the difficulty of ruling out a rival.

A bounded-certificate relation R(I,y) decidable in polynomial time gives the FCP condition

$$\exists c,y\ \forall z:\ R(I,y)\land c\subseteq y\land
((R(I,z)\land c\subseteq z)\Rightarrow z=y).$$

The polynomially bounded encodings of c,y,z and the budget constraint put this version in Σ₂^P. If R means “globally optimal,” it is generally not polynomial-time decidable; do not apply this argument without an additional optimality check. For scalar polynomial-bit objectives with polynomial-time feasibility and evaluation, a chosen y can instead be required to have no strictly better feasible rival, together with no different tied rival satisfying the clues. This also has an existential–universal formulation.

## 4. Counterexample-guided search

For a fixed target, an implementable exact loop is:

1. Find a minimum-cost clue set hitting the rival differences collected so far.
2. Ask a solver for another compatible solution in the intended family.
3. If none exists, return the clue set; otherwise add its difference set and repeat.

Correctness: every truly identifying clue hits all collected rivals, so the master optimum is a lower bound. If its candidate passes the complete rival oracle, that lower bound is attained. Finite termination follows because every new rival excludes the current candidate. This is an exact method, not a polynomial-time guarantee. For original optima, the oracle must search only at the original optimum, and the target must itself be optimal.

## 5. Counting just enough

For uniqueness, counts can be capped at 2: 0, 1, or at least 2. For disjoint alternatives use min(2,a+b); for independent choices use min(2,ab). These rules are sound only when the decomposition does not count the same complete solution multiple times.

Optimizing a clue set may require remembering many possible count profiles. Recording one cheapest clue for a subgraph can discard information needed after composition. The profile-based PAU algorithm in [P5](SOURCES.md#p5) is a concrete place to study this issue.

## 6. A reduction checklist

Ordinary decision equivalence does not preserve clues. Check:

- Solutions correspond in the required direction, with controlled multiplicity.
- Auxiliary coordinates cannot provide unexpectedly cheap clues.
- Source and target clue budgets are related in both directions.
- Optimality and graph restrictions survive when needed.
- Symmetry and certificate representations match the claimed solution notion.

[P7](SOURCES.md#p7) gives a sufficient FCP transfer framework using aligned certificate coordinates. The existence of one such theorem is not a license to treat every parsimonious reduction as clue-preserving.

