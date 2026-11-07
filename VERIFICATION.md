# Verification record / 確認記録

Edition 0.2 · 2026-11-07 · Selective working survey

## Scope / 対象

- Seven paired English/Japanese documents, including the new reduction-source index.
- 71 aligned result records across 11 problem families/sections, 15 source records and 16 BibTeX entries.
- One machine-readable catalogue (`data/results.json`) generates both result pages using `scripts/build_results.py`.
- Eight exercises with answers and a Python example enumerator remain available.

英日7組、問題別11節・結果71項目、出典15件、BibTeX16件です。平面性・二部性・最大次数の同時条件、モデル、目標解、重み、パラメータを分けました。旧R01–R18は問題別IDへ置換し、分割・拡充しています。旧版はGit履歴に残ります。

## Mathematical checks / 数学的な確認

Elementary explanations were checked directly: rival difference sets; fixed versus selectable targets; global distinction; the INCLUDE/deletion equivalence with original-optimum preservation; and the existential–universal formulation with an explicit polynomial-time relation.

The example enumerator checked all **76 labeled simple graphs on 0–4 vertices**. For each graph it checked:

1. For selectable targets, minimum EXCLUDE cost equals minimum MIXED cost and is at most minimum INCLUDE cost.
2. For every INCLUDE set A, uniqueness among original minimum covers agrees with uniqueness of the residual minimum cover AND the optimum-value equality.
3. The coordinate difference-set hitting criterion for every original optimum and coordinate subset.

It also checked the K3, K5, C4 and P3 examples, target-dependent clue costs, the empty/singleton conventions, and the constrained-reoptimization counterexample.

小グラフの全列挙は、説明した等式・同値性の具体例を確かめるものです。一般定理の証明や、引用論文の帰着の検証の代わりにはなりません。

## Documentation checks / 文書の確認

Run from the repository root:

```bash
python3 examples/exact_examples.py
python3 scripts/build_results.py
python3 scripts/check_repository.py
```

The checker validates local documentation links, explicit source anchors, seven language pairs, all 71 result IDs against the shared data, unique bibliography keys, and critical structural restrictions. The result pages are generated reproducibly from the same data. The result IDs and evidence labels were aligned between languages. It does not automatically prove translations equivalent or external URLs permanently reachable.

参照先の版、公刊年と投稿年、モデル制限を点検しました。幅表現が与えられる場合の計算時間と、clique-widthによるFPTという主張を区別しています。一般化されたパズルを、固定サイズのパズルと混同しない表記にしています。

## Limits / 限界

S means the relevant statement was found in accessible full text. A means primary-abstract confirmation only. H means a historical report through another paper. These are evidence-access levels, not peer-review or proof-certification badges.

The reductions and algorithms in the cited papers have not been independently re-proved in this edition. P6, P8 and P10 have now been checked in full text; the cut matrix and weight assumptions are recorded. P9/P11 restricted PAU results and P13 remain abstract-level. The original 2004 matching proof and full P7 meta-theorem hypotheses remain on the reading queue. P14 footnote 1 reports the correction of the earlier degree-4 matching claim; this discrepancy is retained explicitly. D labels elementary derivations, not source theorems.

This edition was prepared and checked by the same assistant; no independent reviewer or human approval is claimed. No unpublished research, account information or authentication material is part of the repository.

この版は同じ作成者による確認であり、独立した査読や人間による承認を意味しません。未公開研究・アカウント情報・認証情報は含めません。文献上の問いと、この資料が未調査の事項を区別します。

## Updating / 更新時

For every changed result: preserve its ID or explain a replacement; update both languages; record source version, theorem and assumptions; update its evidence level only after the corresponding check. Re-run the example script if any mathematical example changes. Do not label an unresolved coverage gap an open problem.

