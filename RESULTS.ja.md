# 問題別・入力制限別の結果
[English](RESULTS.md) · [入口](README.ja.md) · [帰着元索引](REDUCTIONS.ja.md)

第0.2版 · 2026-11-07。**一行の条件は同時に満たすものとして読みます。** 平面・二部・最大次数3以下という結果と、それぞれ単独の結果を区別します。異なる行の制限を合成してはいけません。Δは最大次数であり正則性ではありません。条件の未記載は「未収録」であり「未解決」ではありません。

問題、指定モデル、目標解の入力／選択、構造制限、パラメータを分けて示します。S＝本文で主張確認、A＝一次要旨のみ、H＝別論文での報告、D＝ここで説明する初等的帰結です。確認範囲は証明の独立検証を意味しません。[出典・参照版](SOURCES.md)。n=|V|、m=|E|、τは元の最小頂点被覆数、O*は多項式因子を省略します。

- [最小頂点被覆のpre-assignment（PAU-VC）](#pau)
- [頂点削除による最小頂点被覆の一意化（MU-VC）](#mu)
- [完全マッチング](#matching)
- [SAT・Boolean defining set](#sat)
- [三角形分割・Latin square・パズル](#puzzles)
- [最小全域木・最小重み基底](#mst)
- [最短s–t路](#shortest)
- [最小カット](#cut)
- [最適グラフ彩色](#coloring)
- [最大クリーク・最小支配集合](#clique-dom)
- [一般的な移送定理](#transfer)

<a id="pau"></a>
## 最小頂点被覆のpre-assignment（PAU-VC）

解集合は元のグラフの最小頂点被覆です。INCLUDEは含める指定、EXCLUDEは含めない指定、MIXEDは両方です。平面・最大次数3の結果と、平面・二部・最大次数3の結果を分けます。後者を三モデルすべての結果として扱いません。

### 困難性

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| VC-H1 | 一般グラフ | 三モデルすべて・目標解を選択 | Σ₂^P完全 | [P1](SOURCES.md#p1), Th. 6 | S |
| VC-H2 | 平面グラフかつ最大次数3以下 | 三モデルすべて・目標解を選択 | Σ₂^P完全 | [P9](SOURCES.md#p9), abstract | A |
| VC-H3 | 二部グラフ | 三モデルすべて・目標解を選択 | NP完全 | [P1](SOURCES.md#p1), Ths. 13–14 | S |
| VC-H4 | 平面かつ二部、最大次数3以下 | 一次要旨で定義されたMIXED | NP完全 | [P11](SOURCES.md#p11), abstract | A |

### アルゴリズム

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| VC-A1 | 一般グラフ | 三モデルすべて | O(2.1996^n) | [P1](SOURCES.md#p1), Th. 15 | S |
| VC-A2 | 元の最小被覆数τでパラメータ化 | 三モデルすべて | O*(3.6791^τ) | [P1](SOURCES.md#p1), Ths. 16, 18 | S |
| VC-A3 | 二部グラフ・当初の上界 | 三モデルすべて | O(1.9181^n) | [P1](SOURCES.md#p1), §4.3 | S |
| VC-A4 | 二部グラフ・改善後の上界 | MIXED。要旨だけでINCLUDEへの適用を推測しない | O(1.4143^n) | [P11](SOURCES.md#p11), abstract | A |
| VC-A5 | 木・当初の上界 | 三モデルすべて | O(1.4143^n) | [P1](SOURCES.md#p1), §4.4 | S |
| VC-A6 | clique-width cwでパラメータ化 | INCLUDEのみ | FPT。幅wの表現が入力なら2^{O(2^w)}n² | [P5](SOURCES.md#p5), Th. 1.1; §3.2 | S |
| VC-A7 | 木 | INCLUDEのみ | 多項式時間（clique-width有界からの帰結） | [P5](SOURCES.md#p5), Th. 1.1; §3.1 | D |
| VC-A8 | split graph | INCLUDEのみ | 線形時間 | [P5](SOURCES.md#p5), Th. 5.1 | S |
| VC-A9 | unit interval graph | INCLUDEのみ | 線形時間 | [P5](SOURCES.md#p5), Th. 4.1 | S |

### 近似

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| VC-X1 | 二部グラフ | INCLUDE・最小指定数 | P≠NPなら多項式時間定数近似なし | [P5](SOURCES.md#p5), §6 | S |

<a id="mu"></a>
## 頂点削除による最小頂点被覆の一意化（MU-VC）

k頂点以下を削除し、残ったグラフの最小被覆を一意にします。元の最適値の保存は要求しません。平面・最大次数5の定理は、PAUの平面・最大次数3の定理とは別問題です。幅表現を入力とする計算量と、分解を求める処理も区別します。

### 困難性

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| MU-H1 | 平面グラフかつ最大次数5以下 | 頂点削除・元の最適値の保存を要求しない | Σ₂^P完全 | [P6](SOURCES.md#p6), Th. 7 | S |

### アルゴリズム

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| MU-A1 | 木 | 頂点削除 | O(n) | [P6](SOURCES.md#p6), Th. 2 | S |
| MU-A2 | treewidth w | 頂点削除 | XP：n^{O(2^w)} | [P6](SOURCES.md#p6), Th. 3 | S |
| MU-A3 | treewidth wと最大次数Δ | 頂点削除 | FPT：Δ^{O(2^w)}n（分解上のDP） | [P6](SOURCES.md#p6), Th. 4 | S |
| MU-A4 | clique-width d-expressionを入力 | 頂点削除 | XP：n^{O(2^d)} | [P6](SOURCES.md#p6), Th. 5; proof | S |
| MU-A5 | 幅dの表現と削除予算k | 頂点削除 | FPT：k^{O(2^d)}n。k=0は別処理 | [P6](SOURCES.md#p6), Th. 6; proof | S |

<a id="matching"></a>
## 完全マッチング

forcingは目標マッチングの辺を含め、anti-forcingは目標外の辺を除外する指定です。目標入力／選択の四通りを分けます。以下の二部・最大次数3の困難性には平面性は含まれません。平面二部グラフの目標入力forcingには多項式時間の結果があります。P14脚注1は、古い目標選択forcingの構成について、原論文の次数4という記述に対し実際は次数5と指摘しています。次数3の帰着元には新しい定理を使います。

### 困難性

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| PM-H1 | 二部グラフかつ最大次数3以下 | forcing・完全マッチングMが入力 | NP完全 | [P2](SOURCES.md#p2), reported in P12 Th. D and P14 §1 | H |
| PM-H2 | 二部グラフかつ最大次数3以下 | anti-forcing・Mが入力 | NP完全 | [P14](SOURCES.md#p14), Th. 3 | S |
| PM-H3 | 二部グラフかつ最大次数3以下 | forcing・Mを選択 | NP完全 | [P14](SOURCES.md#p14), Th. 4 | S |
| PM-H4 | 二部グラフかつ最大次数3以下 | anti-forcing・Mを選択 | NP完全 | [P14](SOURCES.md#p14), Th. 5 | S |

### 歴史的結果

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| PM-O1 | 二部グラフ・最大次数4以下。後続結果あり | anti-forcing・Mが入力 | NP完全 | [P13](SOURCES.md#p13), abstract | A |
| PM-O2 | 二部グラフ。原論文はΔ≤4と主張、後続論文は構成のΔ≤5を指摘 | forcing・Mを選択 | 歴史的NP完全性。Δ≤3にはPM-H3を使用 | [P12](SOURCES.md#p12), Th. 7; P14 footnote 1 | H |

### アルゴリズム

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| PM-A1 | 平面埋込み付き二部グラフ | forcing・Mが入力 | 文献で多項式時間アルゴリズムが報告 | [P12](SOURCES.md#p12), Th. C; concluding discussion | H |
| PM-A2 | 最大次数2以下 | forcing／anti-forcing・M入力／選択の4通り | 多項式時間。完全マッチングがあれば偶閉路成分ごとに1指定 | [P14](SOURCES.md#p14), elementary component argument in survey | D |

**次数2の帰結（D）。** 成分は道と閉路です。完全マッチングが存在すれば、道成分では一意、偶閉路成分では二通りです。各偶閉路で少なくとも一指定が必要で、マッチング辺を一つ含めるか、外の辺を一つ除外すれば十分です。完全マッチングがない成分があれば実行不可能です。これによりPM-A2の四通りが従います。

<a id="sat"></a>
## SAT・Boolean defining set

指定は変数の値です。planarはP4で使う式の平面性の定義であり、別のグラフへの帰着後にも平面になるという意味ではありません。出現回数制限や単調性は追加していません。Q1は指定の検証、Q2は入力解への指定探索、Q3は解も選ぶ問題です。

### 検証

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| SAT-V1 | 3CNF | 充足割当てと指定が入力・Q1 | coNP完全 | [P3](SOURCES.md#p3), Th. 3 | S |

### 困難性

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| SAT-H1 | 3CNF | 充足割当てが入力・指定を探すQ2 | Σ₂^P完全 | [P3](SOURCES.md#p3), Th. 4 | S |
| SAT-H2 | 3CNF | 目標割当てを選択・Q3 | Σ₂^P完全 | [P3](SOURCES.md#p3), Th. 5 | S |
| SAT-H3 | Planar 3SAT（原論文の平面式モデル） | FCP・目標割当てを選択 | Σ₂^P完全 | [P4](SOURCES.md#p4), Lemma 9 | S |
| SAT-H4 | Planar 1-in-3 SAT | FCP・目標を選択・各節で真のリテラルがちょうど1個 | Σ₂^P完全 | [P4](SOURCES.md#p4), Lemma 10 | S |
| SAT-H5 | 1-in-3 SAT | FCP・目標を選択 | Σ₂^P完全 | [P4](SOURCES.md#p4), Lemma 11 | S |
| SAT-H6 | 2CNF | FCP・目標を選択 | NP完全 | [P4](SOURCES.md#p4), Th. 18 | S |

<a id="puzzles"></a>
## 三角形分割・Latin square・パズル

三角形分割は辺集合を三角形へ分割する問題です。頂点分割と混同しないでください。三部グラフに制限した結果も別行にします。Sudokuなどは入力サイズが増える一般化版です。指定対象は各問題に依存します。

### 困難性

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| PUZ-H1 | 一般化Sudoku・盤面サイズも入力 | 追加のマス値を指定・目標解を選択 | Σ₂^P完全 | [P4](SOURCES.md#p4), Lemma 14 | S |
| PUZ-H2 | Shakashaka | 完成形のマス状態を指定・目標解を選択 | Σ₂^P完全 | [P4](SOURCES.md#p4), Lemma 15 | S |
| PUZ-H3 | Akari | 完成形のマス状態を指定・目標解を選択 | Σ₂^P完全 | [P4](SOURCES.md#p4), Lemma 16 | S |
| PUZ-H4 | 辺集合を三角形に分割。頂点分割ではない | 分解に含める三角形を指定 | Σ₂^P完全 | [P4](SOURCES.md#p4), Th. 12 | S |
| PUZ-H5 | 三部グラフ上の三角形辺分割 | FCP | Σ₂^P完全。Latin squareへの帰着で使用 | [P4](SOURCES.md#p4), proof of Th. 13 | S |
| PUZ-H6 | 位数が入力の部分Latin square | 追加のマス値を指定・目標完成形を選択 | Σ₂^P完全 | [P4](SOURCES.md#p4), Th. 13 | S |

<a id="mst"></a>
## 最小全域木・最小重み基底

無向グラフで、MSTの定理は重み付き多重グラフ・負の重みも許します。forcing／anti-forcingを分けます。目標選択のO(m log n)を、目標入力の系にもそのまま付けません。

### アルゴリズム

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| MST-A1 | 無向重み付き多重グラフ・負の重みも許す | forcing／anti-forcing・目標木を選択 | O(m log n) | [P10](SOURCES.md#p10), Th. 1 | S |
| MST-A2 | 重み付きmatroid・独立性オラクル入力 | forcing／anti-forcing・目標基を選択 | 多項式回のオラクル呼出しと多項式計算 | [P10](SOURCES.md#p10), Th. 2 | S |
| MST-A3 | 同じmatroid入力・最小重み基が入力 | 指定された基のforcing／anti-forcing | 多項式時間。指定MSTにも適用 | [P10](SOURCES.md#p10), Cor. 1 | S |

<a id="shortest"></a>
## 最短s–t路

辺長はすべて正です。P10の有向版のアルゴリズムは同論文で無向入力にも適用されます。困難性は重みなし無向でも成り立ちますが、平面性や次数制限は付けません。dは元の最短路に含まれる辺数の最大値であり、重み付き距離ではありません。

### アルゴリズム

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| SP-A1 | 有向グラフ・辺長はすべて正 | forcing・最短路を選択 | O(nm) | [P10](SOURCES.md#p10), Th. 3 | S |
| SP-A2 | 同じ入力条件。無向の場合も適用 | forcing・最短路が入力 | O(nm) | [P10](SOURCES.md#p10), Th. 3 and following paragraph | S |
| SP-A3 | 有向・辺長はすべて正 | anti-forcing・最短路が入力 | 多項式時間 | [P10](SOURCES.md#p10), Th. 5 | S |

### 困難性

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| SP-H1 | 無向かつ重みなしグラフ | anti-forcing・最短路を選択 | NP完全 | [P10](SOURCES.md#p10), Th. 4 | S |

### パラメータ化アルゴリズム

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| SP-H2 | 同じ重みなし無向入力 | anti-forcing・パラメータdは最短路の辺数 | dに関してW[1]困難 | [P10](SOURCES.md#p10), Th. 4 | S |
| SP-A4 | 辺長は正。dは元の最短路が持つ辺数の最大値 | anti-forcing・予算k・目標路を選択 | d^k n^{O(1)}。k+dでFPT | [P10](SOURCES.md#p10), Th. 6 | S |
| SP-A5 | 同じ入力条件とdの定義 | anti-forcing・予算k | (k+1)^d n^{O(1)}。k+dでFPT | [P10](SOURCES.md#p10), Th. 7 | S |
| SP-A6 | 有向。基礎無向グラフのtreewidthが有界 | anti-forcing・最短路を選択 | treewidthを固定すると線形時間 | [P10](SOURCES.md#p10), Th. 8 | S |

<a id="cut"></a>
## 最小カット

入力はすべて無向です。アルゴリズムの重み条件は正整数です。解はcutの辺集合であり、岸の向きを区別した表現ではありません。global／s–t、forcing／anti-forcing、目標入力／選択の八通りを分けます。計算途中の有向残余グラフを有向入力の結果と読み替えません。

### global cut

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| CUT-A1 | 無向・辺重みは正整数 | global min cut・forcing・目標cutを選択 | O(m polylog n) | [P8](SOURCES.md#p8), Th. 3.1 | S |
| CUT-A2 | 同じ入力条件 | global min cut・forcing・目標cutが入力 | O(m polylog n) | [P8](SOURCES.md#p8), Cor. 1 | S |
| CUT-H1 | 重みなし単純無向グラフ | global min cut・anti-forcing・目標cutを選択 | NP完全 | [P8](SOURCES.md#p8), Th. 3.3 | S |
| CUT-H2 | 重みなし単純無向グラフ | global min cut・anti-forcing・目標cutが入力 | NP完全 | [P8](SOURCES.md#p8), Cor. 2 | S |

### s–t cut

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| CUT-H3 | 重みなし無向グラフ。Lemma 1で単純化 | min s–t cut・forcing・目標cutを選択 | NP完全 | [P8](SOURCES.md#p8), Th. 4.3; Lemma 1 | S |
| CUT-H4 | 重みなし無向グラフ。Lemma 1で単純化 | min s–t cut・anti-forcing・目標cutを選択 | NP完全 | [P8](SOURCES.md#p8), Th. 4.4; Lemma 1 | S |
| CUT-A3 | 無向・辺重みは正整数 | min s–t cut・forcing・目標cutが入力 | O(nm) | [P8](SOURCES.md#p8), Th. 4.5 | S |
| CUT-A4 | 無向・辺重みは正整数 | min s–t cut・anti-forcing・目標cutが入力 | O(nm) | [P8](SOURCES.md#p8), Th. 4.6 | S |

<a id="coloring"></a>
## 最適グラフ彩色

最適彩色に対し、色名付きの指定を行います。予算kが入力のdefining setと、kを固定したforcing chromatic numberを分けます。χ(G)≤3は彩色数の制限であり、最大次数3の意味ではありません。頂点集合のみが入力の問題と、部分彩色が入力の問題も異なります。

### 予算kが入力

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| COL-H1 | χ(G)=3・最適彩色cが入力 | cを確定するk個以下の色指定を探索・kは入力 | Σ₂^P完全 | [P3](SOURCES.md#p3), Th. 7 | S |
| COL-H2 | χ(G)=3 | 最適彩色とk個以下の指定を選択・kは入力 | Σ₂^P完全 | [P3](SOURCES.md#p3), Th. 8 | S |

### 固定予算k・関連する検証

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| COL-V1 | 一般グラフと指定された二頂点 | その頂点集合がいずれかの最適彩色をforceするか | US完全。色の値は入力ではない | [P15](SOURCES.md#p15), Prop. 2.8 | S |
| COL-H3 | 連結グラフ・各固定定数k≥2 | Fχ(G)≤kの判定 | US困難（many-one帰着） | [P15](SOURCES.md#p15), Th. 3.1 | S |
| COL-H4 | χ(G)≤3かつFχ(G)≤3・適正3彩色が入力 | Fχ(G)≤2かの判定 | このpromise下でcoNP困難 | [P15](SOURCES.md#p15), Th. 4.1 | S |
| COL-A1 | 各固定定数k。平面性や次数条件を加えない | Fχ(G)≤k | P_dtt(US)に所属。many-one完全性の主張ではない | [P15](SOURCES.md#p15), Th. 8.2 | S |

<a id="clique-dom"></a>
## 最大クリーク・最小支配集合

元の最適解に対するINCLUDE指定で、目標解を選択します。ここでkは各固定定数です。US困難性とP_dtt(US)所属は別々の主張であり、完全性やFPTアルゴリズムと読み替えません。

### 最大クリーク

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| CLQ-H1 | 一般グラフ・各固定定数k≥0 | 最大クリークに対するINCLUDE・目標を選択 | US困難 | [P15](SOURCES.md#p15), Th. 7.5 | S |
| CLQ-A1 | 同じ入力条件 | Fω(G)≤k | P_dtt(US)に所属 | [P15](SOURCES.md#p15), Th. 8.2 | S |

### 最小支配集合

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| DOM-H1 | 一般グラフ・各固定定数k≥0 | 最小支配集合に対するINCLUDE・目標を選択 | US困難 | [P15](SOURCES.md#p15), Th. 7.5 | S |
| DOM-A1 | 同じ入力条件 | Fγ(G)≤k | P_dtt(US)に所属 | [P15](SOURCES.md#p15), Th. 8.2 | S |

<a id="transfer"></a>
## 一般的な移送定理

グラフクラスの定理ではなく、モデル間の移送定理です。parsimoniousであるだけでは不十分で、指定座標の整列条件など正式な仮定の確認が必要です。ここは最終版要旨の確認にとどまります。

### 移送

| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |
|---|---|---|---|---|---|
| META-1 | 帰着元NP問題のFCPがΣ₂^P完全・座標整列したparsimonious帰着 | FCPの移送・帰着先の証明書は多項式時間判定可能 | 正式な仮定の下でΣ₂^P完全性を移送 | [P7](SOURCES.md#p7), final abstract | A |

## 収録範囲と更新

すべてのグラフクラスを網羅した分類表ではありません。特に、目標選択matchingの平面版、最短路の平面版の困難性、cutの次数制限付き困難性、P11要旨の三モデルへの拡張は、この版では主張していません。これらは文献調査の未収録箇所であり、未解決問題の宣言ではありません。

[機械可読データ](data/results.json) · [帰着の対応](REDUCTIONS.ja.md) · [確認記録](VERIFICATION.md)
