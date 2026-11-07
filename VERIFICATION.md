# Verification record / 確認記録

Edition 0.1 · 2026-11-07 · Selective working survey

## Scope / 対象

- Six paired English/Japanese documents: entry point, models, common methods, selected results, reading guide and questions.
- Eighteen aligned result rows, eleven source records and twelve BibTeX entries (FCP conference and journal versions are separate).
- One historical matching result marked H outside the numbered table.
- Eight exercises with answers, and a Python example enumerator.

英日6組、主要結果18行、出典11件、BibTeX 12件、演習8問を含みます。matchingの歴史的結果は確認範囲Hとして番号付き表と分けています。

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
python3 scripts/check_repository.py
```

The checker validates local documentation links, explicit source anchors, the six language pairs, eighteen matching result IDs and unique bibliography keys. The result IDs and evidence labels were aligned between languages. It does not automatically prove translations equivalent or external URLs permanently reachable.

参照先の版、公刊年と投稿年、モデル制限を点検しました。幅表現が与えられる場合の計算時間と、clique-widthによるFPTという主張を区別しています。一般化されたパズルを、固定サイズのパズルと混同しない表記にしています。

## Limits / 限界

S means the relevant statement was found in accessible full text. A means primary-abstract confirmation only. H means a historical report through another paper. These are evidence-access levels, not peer-review or proof-certification badges.

The reductions and algorithms in the cited papers have not been independently re-proved in this edition. Recent cut results are described at abstract level without inventing a classification matrix. The original 2004 matching proof, precise recent weight assumptions, and full meta-theorem hypotheses remain on the reading queue.

This edition was prepared and checked by the same assistant; no independent reviewer or human approval is claimed. No unpublished research, account information or authentication material is part of the repository.

この版は同じ作成者による確認であり、独立した査読や人間による承認を意味しません。未公開研究・アカウント情報・認証情報は含めません。文献上の問いと、この資料が未調査の事項を区別します。

## Updating / 更新時

For every changed result: preserve its ID or explain a replacement; update both languages; record source version, theorem and assumptions; update its evidence level only after the corresponding check. Re-run the example script if any mathematical example changes. Do not label an unresolved coverage gap an open problem.

