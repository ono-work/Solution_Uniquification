# Solution Uniquification
## 解の一意化：Forcing Set・Fewest Clues・Pre-assignment

[English](README.md) · 第0.2版 · 2026-11-07 · 継続更新するサーベイ

**どれだけ少ない情報の指定や変更で、解をちょうど一つにできるか。**
この問いを、異なる分野のモデルを比較しながら学ぶための資料です。学生が研究に入るための導入と、研究者が既知結果を比較するための一覧を用意します。

まず具体例を読み、モデルの違いを理解してから計算量の結果へ進んでください。

| 資料 | 内容 | 英語 |
|---|---|---|
| [モデル](MODELS.ja.md) | 解集合、部分指定、指定解と選択可能な解 | [Models](MODELS.md) |
| [共通手法](METHODS.ja.md) | 差分集合、hitting set、一意性の検証 | [Methods](METHODS.md) |
| [主要結果](RESULTS.ja.md) | モデルの適用範囲を明示した結果表 | [Results](RESULTS.md) |
| [帰着元索引](REDUCTIONS.ja.md) | 平面・二部・次数制限付きの困難性、予算・保存性 | [Reduction sources](REDUCTIONS.md) |
| [読む順序・演習](READING.ja.md) | 全6回の輪講案、演習と解答 | [Reading guide](READING.md) |
| [研究上の問い](QUESTIONS.ja.md) | 文献の問い、考察課題、未調査項目 | [Questions](QUESTIONS.md) |
| [出典](SOURCES.md) | 書誌情報、参照版、確認の深さ | 英日共通 |
| [確認記録](VERIFICATION.md) | 今回確認したこと・未確認のこと | 英日併記 |

## 最初の例

頂点a,b,cからなる三角形の最小頂点被覆は、ab・ac・bcの三つです。「aを含める」だけでは二つ残ります。「aとbを含める」と一つになります。一方「cを含めない」だけでもabに確定します。したがって、含める指定と含めない指定では必要な指定数が異なります。

「指定を一つも取り除けない」という**極小**と、「指定数が最も少ない」という**最小**を区別します。また、手がかりの少なさや解の一意性だけから、人間にとって解きにくいとは結論できません。

## 対象範囲

中心は、指定数を制限して解を一意にする決定的な部分指定です。defining／forcing set、Fewest Clues Problem（FCP）、最適解のpre-assignmentを扱います。グラフ変更による一意化は隣接するモデルとして含めます。乱択isolationや最適解の一意性判定は関連事項とし、一般に同じ問題とは扱いません。

研究の入口は、堀山・小林・小野・瀬戸・鈴木によるAAAI 2024論文[P1](SOURCES.md#p1)です。歴史的背景として、matchingのforcing set [P2](SOURCES.md#p2)、defining set [P3](SOURCES.md#p3)、FCP [P4](SOURCES.md#p4)を接続します。2004年を分野全体の起源とするものではありません。

## 例の再現

Python 3.10以降、追加ライブラリ不要です。

```bash
python3 examples/exact_examples.py
python3 scripts/check_repository.py
```

小さい例の全列挙による確認です。引用論文の困難性証明を検証するものではありません。

## この版の位置づけ

第0.2版は、問題別・入力制限別の71項目と帰着元索引を備えた選択的サーベイです。結果にはモデルと確認の深さを付けます。「未収録」は「未解決」を意味しません。最近の文献候補は、定理を確認する前に確定結果表へ混ぜません。未公開研究は含めません。

修正時は、該当する行、モデル、論文の版、定理、仮定を明記し、英日を同時に更新します。[BibTeX](BIBLIOGRAPHY.bib)も利用できます。

