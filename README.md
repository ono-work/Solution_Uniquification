# Solution Uniquification
## Forcing Sets, Fewest Clues, and Pre-assignment

[日本語](README.ja.md) · Version 0.2 · 2026-11-07 · Working survey

**How much information or modification is needed to leave exactly one solution?**
This repository connects several ways of asking this question. It is designed for students entering the subject and researchers comparing models.

Start with the examples, then distinguish the models before comparing complexity results.

| Read | Purpose | Japanese |
|---|---|---|
| [Models](MODELS.md) | Solution families, clues, fixed versus selectable targets | [モデル](MODELS.ja.md) |
| [Methods](METHODS.md) | Difference sets, hitting sets, uniqueness verification | [共通手法](METHODS.ja.md) |
| [Results](RESULTS.md) | A model-sensitive catalogue of selected results | [主要結果](RESULTS.ja.md) |
| [Reduction sources](REDUCTIONS.md) | Restricted hard cases, budget maps and preserved properties | [日本語](REDUCTIONS.ja.md) |
| [Reading guide](READING.md) | Six seminar sessions, exercises and answers | [読む順序・演習](READING.ja.md) |
| [Questions](QUESTIONS.md) | Literature questions, research prompts, coverage gaps | [研究上の問い](QUESTIONS.ja.md) |
| [Sources](SOURCES.md) | References, versions and evidence levels | 英日共通 |
| [Verification](VERIFICATION.md) | What was and was not checked | 英日併記 |

## A first example

In a triangle with vertices a,b,c, the minimum vertex covers are ab, ac and bc. Requiring a to be in the cover leaves two possibilities. Requiring a and b leaves one. Prohibiting c also leaves just ab. Thus positive and negative clues can have different costs even on a tiny instance.

Do not confuse a *minimum* clue set (smallest size) with a *minimal* one (no clue can be removed). Neither few clues nor a unique answer alone measures human solving difficulty.

## Scope

The core is deterministic, budgeted partial specification: defining/forcing sets, Fewest Clues Problems (FCP), and pre-assignment for optimal solutions. Graph modification is included as a neighboring model. Random isolation and recognition of unique optimality are connections, with no general equivalence asserted.

The research entry point is Horiyama–Kobayashi–Ono–Seto–Suzuki's AAAI 2024 paper [P1](SOURCES.md#p1). The historical background includes matching forcing sets [P2](SOURCES.md#p2), defining sets [P3](SOURCES.md#p3), and FCP [P4](SOURCES.md#p4). This is a thematic map, not a claim that these ideas began in 2004.

## Reproduce the examples

Python 3.10+; no third-party packages:

```bash
python3 examples/exact_examples.py
python3 scripts/check_repository.py
```

The first command checks tiny instances by exhaustive enumeration. These checks do not verify the hardness reductions in the cited papers.

## Status and contributions

This first edition is selective. Results retain their original model and evidence level; “not covered” never means “open.” Some recent leads are deliberately kept outside the confirmed catalogue. No unpublished work is included.

For a correction, identify the row, precise problem model, paper version, theorem and relevant assumption. Update both language versions together. Bibliography: [BIBLIOGRAPHY.bib](BIBLIOGRAPHY.bib).

