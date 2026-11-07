# Reading guide and exercises
[日本語](READING.ja.md) · [Home](README.md)

Prerequisites: sets and graphs, basic SAT, polynomial-time reductions. Learn NP/coNP before Session 3; learn the meaning of Σ₂^P and FPT/XP before Sessions 4–5. No chemical background is required for the entry point through matching.

The six sessions can each take 60–90 minutes; the goal is to explain one definition, one example and one proof idea, not to finish every technical section.

| Session | Preparation | In the meeting |
|---|---|---|
| 1. What is being made unique? | README and Models §§1–3 | Enumerate triangle covers; separate fixed-target and selectable-target questions |
| 2. A common combinatorial view | Methods §§1–2; P3 §1; P2 for context | Prove the difference-set criterion; compare positive and negative clues |
| 3. Verification versus search | Methods §§3–4; P3 §2 | Write a blocking clause; explain Q1 versus Q2 without conflating their quantifiers |
| 4. Puzzle design and FCP | P4 §§2, 4–5 | Specify the certificate coordinates and explain why a clue needs exactly one completion |
| 5. Original optimal solutions | P1 §2.2; P5 §§1, 3 | Prove the deletion identity; locate the model restriction of the width result |
| 6. Extensions and paper review | P6 full text; P7 abstract, then the formal theorem | Compare deletion and preservation; write a result card and mark unverified details |

All paper IDs are resolved in [Sources](SOURCES.md). For an introductory course, stop after Sessions 1–4 and the deletion identity. The later sessions are an entry into research.

## Exercises

1. **Triangle.** Find the minimum INCLUDE, EXCLUDE and MIXED clue costs among minimum covers of K3.
2. **Fixed target.** In F={000,100,010,001}, compute the coordinate-clue cost of each target. What is the cost of separating all pairs?
3. **No solutions.** What should the clue optimum be for F=∅? What about |F|=1?
4. **Preservation.** Prove that INCLUDE A among original minimum covers is equivalent to uniqueness of G-A together with τ(G-A)=τ(G)-|A|.
5. **Restricted reoptimization.** Use the path a-b-c with INCLUDE {a,c} to explain why constrained uniqueness is not original-optimum uniqueness.
6. **Matching.** Given a perfect matching M, prove that D⊆M forces M iff D meets every M-alternating cycle. Can every alternating cycle be switched independently?
7. **Reduction audit.** Encode one source bit x by target bits (x,x). Then encode it by (x,x,x AND z), where z is another source bit. Why is unique extension insufficient to guarantee that a target clue is a clue on only one source coordinate?
8. **Critical versus minimum.** For target 000 and rivals 110 and 101, show that clues {1} and {2,3} are both inclusion-minimal, but only one has minimum size.

## Answers and hints

1. Costs are 2,1,1. A positive clue on one vertex leaves two covers; a negative clue on one vertex fixes the omitted vertex.
2. Costs are 3 for 000, and 1 for each other target. All-pairs separation costs 3.
3. Use +∞ for the empty family and 0 for a singleton. Returning 0 for the empty family confuses uniqueness with at-most-one.
4. Use the bijection C↔C\A and the equality for the minimum size of a cover containing A. Both directions must preserve the original value τ(G).
5. {a,c} is the unique constrained minimum cover of size 2; the sole original minimum cover is {b}, of size 1.
6. A disjoint alternating cycle can be flipped, giving another matching containing D. Conversely, the symmetric difference of two perfect matchings is a disjoint union of alternating cycles, and every such cycle avoids D if both matchings contain D. Overlapping cycles cannot generally be switched independently.
7. The product coordinate depends jointly on x and z. One target clue can impose a condition on two source bits. This explains a potential shortcut; it is not itself a hardness counterexample.
8. The difference sets are {1,2} and {1,3}. Their minimal hitting sets are {1} and {2,3}.

## A result card to submit

Record: exact input; solution representation and symmetry; original versus constrained optimum; target supplied or selectable; permitted clue types and cost; graph restrictions; parameter and decomposition input; conclusion; source version and theorem; proof idea; evidence level; one small example.

A claim that a problem is “open” needs a date and a literature check. An exercise that you cannot solve is not automatically an open problem.

