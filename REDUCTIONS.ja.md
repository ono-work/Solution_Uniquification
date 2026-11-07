# 帰着元を選ぶための索引
[English](REDUCTIONS.md) · [問題別の全結果](RESULTS.ja.md)

## 制限付きの困難性

以下は、その行の制限を同時に満たす帰着元です。別行の平面性・二部性・次数制限を合成しないでください。目標問題への帰着で保存する性質は別途証明が必要です。

| 結果ID | 帰着元・指定モデル | 同時に成り立つ制限 | 困難性 |
|---|---|---|---|
| [VC-H2](RESULTS.ja.md#pau) | PAU-VC, INCLUDE / EXCLUDE / MIXED | 平面・Δ≤3 | Σ₂^P-complete |
| [VC-H4](RESULTS.ja.md#pau) | PAU-VC, MIXED | 平面かつ二部・Δ≤3 | NP-complete |
| [MU-H1](RESULTS.ja.md#mu) | MU-VC・頂点削除 | 平面・Δ≤5 | Σ₂^P-complete |
| [PM-H1–H4](RESULTS.ja.md#matching) | 完全マッチング・四変種 | 二部・Δ≤3。平面性の保証なし | NP-complete |
| [SAT-H3](RESULTS.ja.md#sat) | FCP planar 3SAT | P4の式の平面性。出現回数制限は未記録 | Σ₂^P-complete |
| [SAT-H4](RESULTS.ja.md#sat) | FCP planar 1-in-3SAT | P4の式の平面性 | Σ₂^P-complete |
| [PUZ-H5](RESULTS.ja.md#puzzles) | FCP・辺の三角形分割 | 三部グラフ | Σ₂^P-complete |
| [SP-H1](RESULTS.ja.md#shortest) | 最短路・目標選択anti-forcing | 重みなし無向。平面・次数保証なし | NP-complete; W[1]-hard in d |
| [CUT-H1–H4](RESULTS.ja.md#cut) | 最小cut・表の該当変種 | 重みなし単純無向。平面・次数保証なし | NP-complete |
| [COL-H1–H2](RESULTS.ja.md#coloring) | 最適彩色のdefining set | χ(G)=3。Δ≤3ではない | Σ₂^P-complete |

## 実際の帰着と保存条件

| 出典 | 帰着 | 予算・保存性 | 適用時の境界 |
|---|---|---|---|
| [P14](SOURCES.md#p14), Ths. 1–2; Lemma 6 | matching forcing→anti-forcing（目標入力同士・目標選択同士） | 各辺を3辺の道へ置換。同じk・完全マッチングの全単射・二部性とΔ≥2を保存 | 細分は平面性も保存するが、帰着元の困難例が平面とは示されていない |
| [P14](SOURCES.md#p14), Lemma 10 | 目標選択matching forcing・次数5→次数3 | 線形サイズの頂点ガジェット・同じk | 二部での困難性。平面性を追加しない |
| [P10](SOURCES.md#p10), Th. 4 | Multicolored Biclique→目標選択最短路anti-forcing | 元の各部の大きさN・パラメータqに対しK=2q(N−1)、d=6q−1。重みなし無向 | 多数の迂回路。平面・最大次数の保証は未記録 |
| [P8](SOURCES.md#p8), Ths. 4.3–4.4 | Vertex Cover→目標選択min s–t cut forcing／anti-forcing | 予算n+k。forcing側は4正則VCからの構成 | 帰着元が4正則でも、帰着後が次数4とは限らない |
| [P8](SOURCES.md#p8), Lemma 1 | 重み付き多重グラフcut→重みなし単純グラフcut | cutの対応。重みが多項式有界なら構成は多項式時間 | 頂点をクリークで置換するため平面性・次数制限は保存されない |
| [P7](SOURCES.md#p7), abstract | 一般のFCP移送 | 解のparsimonious対応に加え、座標整列と帰着元の仮定 | 要旨のみ。新しい証明への適用時は正式な定理を確認 |

## 今後の追加単位

新しいグラフクラスを追加する際は、一般・平面・二部・平面二部、最大次数と正則性、重み・向き、目標解の入力／選択、指定の種類、予算とサイズ増加を一組として記録します。今回の索引は、収録した論文から確認できた帰着元の整理です。未記載のクラスを未解決とは扱いません。
