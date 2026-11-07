# Questions and coverage
[日本語](QUESTIONS.ja.md) · [Home](README.md)

## Questions explicitly raised in a checked source

[P5](SOURCES.md#p5), arXiv v3, §1 asks whether INCLUDE Min PAU-VC is polynomial-time solvable on chordal graphs. This is a question in that version, not a certification that no later paper answers it. Recheck the literature before presenting it as currently open.

## Research prompts, not novelty claims

- When can fixed-target clue optimization be reduced to a compact hitting-set instance? What structure bounds the number or type of essential rivals?
- For a graph class, which transformations relate INCLUDE, EXCLUDE and MIXED without increasing the budget? A relation for selectable targets may fail to preserve a supplied target.
- Can an efficient optimization algorithm expose its whole optimal solution family sufficiently to support efficient minimum clues?
- Which boundary information must a DP keep to optimize clues and preserve uniqueness simultaneously?
- Under what assumptions does a clue-preserving reduction also preserve approximation ratios or structural parameters?

Each prompt requires a prior-work check. This repository does not assert any of them is new or unresolved.

## Queue for the next edition

| Topic / lead | Action before adding precise results |
|---|---|
| Matching forcing / anti-forcing | Read the original 2004 theorem and degree restrictions; add alternating-cycle and planar special cases with primary citations |
| PAU-VC follow-ups on restricted graphs | Read P9 and P11 beyond their abstracts; check all three models separately |
| Forcing and anti-forcing minimum cuts | Read P8 full text and extract the per-variant classification; the primary indexed abstract is now recorded |
| FCP transfer theorem | Read the final P7 PDF; verify all alignment and source hypotheses, and theorem numbers |
| MU-VC | Check P6 v2 full text against the conference version; add exact theorem locators |
| Defining sets in domination / coloring / Latin squares | Build separate cards, including symmetry and fixed-target assumptions |
| Isolation and uniqueness recognition | Add primary sources and explain their relation without identifying them with budgeted clues |

A missing row is a coverage gap, not evidence of tractability, hardness or an open problem.

## Benchmark generation

A useful experiment should output the original instance, original optimum, clue cost, target, modified instance if any, and a checkable account of why no rival remains. Store solver versions and random seeds. A unique answer does not imply the generated instance is difficult, and a planted answer alone does not establish uniqueness.

