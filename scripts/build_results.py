from pathlib import Path
import json
r=Path(__file__).resolve().parents[1]
sections=[
('pau','Pre-assignment for minimum vertex cover (PAU-VC)','最小頂点被覆のpre-assignment（PAU-VC）',
 'Solutions are the ORIGINAL minimum covers. INCLUDE fixes membership, EXCLUDE fixes non-membership, MIXED permits both. Each row states which models are covered. Planar subcubic and planar bipartite subcubic hardness are separate theorems with different complexity and model scope.',
 '解集合は元のグラフの最小頂点被覆です。INCLUDEは含める指定、EXCLUDEは含めない指定、MIXEDは両方です。平面・最大次数3の結果と、平面・二部・最大次数3の結果を分けます。後者を三モデルすべての結果として扱いません。'),
('mu','Vertex deletion to unique minimum vertex cover (MU-VC)','頂点削除による最小頂点被覆の一意化（MU-VC）',
 'Delete at most k vertices so the remaining graph has a unique minimum cover. No equality with the original optimum is required. Thus the planar degree-5 theorem is NOT a weaker version of the PAU planar degree-3 theorem. Width-expression bounds refer to supplied expressions; constructing a decomposition is a separate step.',
 'k頂点以下を削除し、残ったグラフの最小被覆を一意にします。元の最適値の保存は要求しません。平面・最大次数5の定理は、PAUの平面・最大次数3の定理とは別問題です。幅表現を入力とする計算量と、分解を求める処理も区別します。'),
('matching','Perfect matching','完全マッチング',
 'Forcing includes edges of the target matching; anti-forcing excludes edges outside it. Given and selectable targets are different problems. The bipartite degree-3 hardness below does NOT include planarity. For a supplied matching on plane bipartite graphs, forcing is polynomial-time. P14 footnote 1 reports that the older selectable-forcing construction claimed degree 4 but actually has degree 5; use its new degree-3 theorem instead.',
 'forcingは目標マッチングの辺を含め、anti-forcingは目標外の辺を除外する指定です。目標入力／選択の四通りを分けます。以下の二部・最大次数3の困難性には平面性は含まれません。平面二部グラフの目標入力forcingには多項式時間の結果があります。P14脚注1は、古い目標選択forcingの構成について、原論文の次数4という記述に対し実際は次数5と指摘しています。次数3の帰着元には新しい定理を使います。'),
('sat','SAT and Boolean defining sets','SAT・Boolean defining set',
 'Clues fix variable values. Planar here refers to the formula/incidence-planarity notion used by P4, not a promise about a later graph gadget. Do not append bounded occurrence or monotonicity to these statements. Q1 verifies supplied clues; Q2 finds clues for a supplied solution; Q3 selects the solution too.',
 '指定は変数の値です。planarはP4で使う式の平面性の定義であり、別のグラフへの帰着後にも平面になるという意味ではありません。出現回数制限や単調性は追加していません。Q1は指定の検証、Q2は入力解への指定探索、Q3は解も選ぶ問題です。'),
('puzzles','Triangle partitions, Latin squares and puzzles','三角形分割・Latin square・パズル',
 'Triangle partition means partitioning EDGES into triangles, not vertices. Its tripartite restriction is a separate source case. Sudoku and the other puzzles are generalized input-size families; clue types are problem-specific.',
 '三角形分割は辺集合を三角形へ分割する問題です。頂点分割と混同しないでください。三部グラフに制限した結果も別行にします。Sudokuなどは入力サイズが増える一般化版です。指定対象は各問題に依存します。'),
('mst','Minimum spanning trees and minimum-weight bases','最小全域木・最小重み基底',
 'The graph is undirected; the MST theorem permits weighted multigraphs and negative weights. Forcing includes target edges; anti-forcing excludes other edges. The O(m log n) bound for selectable targets is not automatically the bound for the supplied-target corollary.',
 '無向グラフで、MSTの定理は重み付き多重グラフ・負の重みも許します。forcing／anti-forcingを分けます。目標選択のO(m log n)を、目標入力の系にもそのまま付けません。'),
('shortest','Shortest s–t paths','最短s–t路',
 'Edge lengths are strictly positive. Directed algorithms also apply to undirected inputs as discussed in P10. The hard case already uses unweighted undirected graphs, but no planar or degree bound is recorded. Parameter d counts edges in an ORIGINAL shortest path (maximum over such paths), not weighted distance.',
 '辺長はすべて正です。P10の有向版のアルゴリズムは同論文で無向入力にも適用されます。困難性は重みなし無向でも成り立ちますが、平面性や次数制限は付けません。dは元の最短路に含まれる辺数の最大値であり、重み付き距離ではありません。'),
('cut','Minimum cuts','最小カット',
 'All inputs here are UNDIRECTED, with positive integer edge weights for the algorithms. Solutions are edge cutsets, not oriented shore descriptions. Global versus s–t, forcing versus anti-forcing, and supplied versus selectable target give eight cases. A directed residual graph inside an algorithm does not make the input directed.',
 '入力はすべて無向です。アルゴリズムの重み条件は正整数です。解はcutの辺集合であり、岸の向きを区別した表現ではありません。global／s–t、forcing／anti-forcing、目標入力／選択の八通りを分けます。計算途中の有向残余グラフを有向入力の結果と読み替えません。'),
('coloring','Optimal graph coloring','最適グラフ彩色',
 'Clues fix named colors in an optimal coloring. Variable-budget defining-set results differ from fixed-k forcing-chromatic-number results. χ(G)≤3 bounds the chromatic number, NOT maximum degree. A supplied vertex set without its color values is not the same input as supplied partial coloring.',
 '最適彩色に対し、色名付きの指定を行います。予算kが入力のdefining setと、kを固定したforcing chromatic numberを分けます。χ(G)≤3は彩色数の制限であり、最大次数3の意味ではありません。頂点集合のみが入力の問題と、部分彩色が入力の問題も異なります。'),
('clique-dom','Maximum clique and minimum dominating set','最大クリーク・最小支配集合',
 'These are INCLUDE clues among ORIGINAL optima, with selectable targets. Each k is a fixed constant in these results. US-hardness and P_dtt(US) membership are separate claims; do not combine them into an unsupported completeness statement or an FPT algorithm.',
 '元の最適解に対するINCLUDE指定で、目標解を選択します。ここでkは各固定定数です。US困難性とP_dtt(US)所属は別々の主張であり、完全性やFPTアルゴリズムと読み替えません。'),
('transfer','General transfer theorem','一般的な移送定理',
 'This is a model-level theorem, not a structural graph subclass. Parsimoniousness alone is insufficient: coordinate alignment and the full source hypotheses must also be checked. Only the final abstract has been checked here.',
 'グラフクラスの定理ではなく、モデル間の移送定理です。parsimoniousであるだけでは不十分で、指定座標の整列条件など正式な仮定の確認が必要です。ここは最終版要旨の確認にとどまります。')]
# Save the reproducible renderer in the repository, with only public survey content.
header={
'en':'# Results by problem and input restriction\n[日本語](RESULTS.ja.md) · [Home](README.md) · [Reduction-source index](REDUCTIONS.md)\n\nEdition 0.2 · 2026-11-07. **Read each row as one conjunction of hypotheses.** Planar + bipartite + Δ≤3 is stronger than any one condition alone; conditions from different rows cannot be combined. Δ is maximum degree, not regularity. Missing restrictions mean **not recorded**, not an open problem.\n\nEach row separates the underlying problem, allowed clues, target supplied/selected, structural input restrictions, and parameter. S: statement checked in full text; A: primary abstract only; H: reported through another paper; D: elementary consequence explained here. These are access levels, not independent proof certification. [Sources and versions](SOURCES.md). n=|V|, m=|E|, τ is the original vertex-cover number; O* suppresses polynomial factors.\n\n',
'ja':'# 問題別・入力制限別の結果\n[English](RESULTS.md) · [入口](README.ja.md) · [帰着元索引](REDUCTIONS.ja.md)\n\n第0.2版 · 2026-11-07。**一行の条件は同時に満たすものとして読みます。** 平面・二部・最大次数3以下という結果と、それぞれ単独の結果を区別します。異なる行の制限を合成してはいけません。Δは最大次数であり正則性ではありません。条件の未記載は「未収録」であり「未解決」ではありません。\n\n問題、指定モデル、目標解の入力／選択、構造制限、パラメータを分けて示します。S＝本文で主張確認、A＝一次要旨のみ、H＝別論文での報告、D＝ここで説明する初等的帰結です。確認範囲は証明の独立検証を意味しません。[出典・参照版](SOURCES.md)。n=|V|、m=|E|、τは元の最小頂点被覆数、O*は多項式因子を省略します。\n\n'}
groups={'hard':('Hardness','困難性'),'algorithm':('Algorithms','アルゴリズム'),'approximation':('Approximation','近似'),'historical':('Historical bounds','歴史的結果'),'verification':('Verification','検証'),'parameterized':('Parameterized algorithms','パラメータ化アルゴリズム'),'global':('Global cuts','global cut'),'st':('s–t cuts','s–t cut'),'variable':('Input budget k','予算kが入力'),'fixed':('Fixed budget k / related verification','固定予算k・関連する検証'),'clique':('Maximum clique','最大クリーク'),'domination':('Minimum dominating set','最小支配集合'),'general':('Transfer','移送')}
data=json.loads((r/'data/results.json').read_text())['results']
for lang in ('en','ja'):
 t=header[lang]+''.join(f'- [{s[1 if lang=="en" else 2]}](#{s[0]})\n' for s in sections)+'\n'
 for key,en,ja,ei,ji in sections:
  t+=f'<a id="{key}"></a>\n## {en if lang=="en" else ja}\n\n{ei if lang=="en" else ji}\n\n'
  rr=[a for a in data if a['family']==key]
  for group in dict.fromkeys(a['group'] for a in rr):
   t+='### '+groups[group][lang=='ja']+'\n\n'
   t+=('| ID | Input / simultaneous restrictions | Model / target | Result | Source / location | Evidence |\n' if lang=='en' else '| ID | 入力・同時に課す制限 | 指定モデル・目標解 | 結果 | 出典・位置 | 確認 |\n')+'|---|---|---|---|---|---|\n'
   for a in rr:
    if a['group']!=group:continue
    t+='| '+' | '.join([a['id'],a['domain'][lang],a['model'][lang],a['result'][lang],f'[{a["source"]}](SOURCES.md#{a["source"].lower()}), {a["locator"]}',a['evidence']])+' |\n'
   t+='\n'
  if key=='matching':
   t+=('**Degree-2 consequence (D).** Components are paths and cycles. If a perfect matching exists, each path component has a unique one; each even cycle has exactly two. Every ambiguous cycle needs at least one clue, and one included matching edge or one excluded nonmatching edge suffices. Odd paths/cycles without a perfect matching make the instance infeasible. This proves PM-A2 for all four variants.\n\n' if lang=='en' else '**次数2の帰結（D）。** 成分は道と閉路です。完全マッチングが存在すれば、道成分では一意、偶閉路成分では二通りです。各偶閉路で少なくとも一指定が必要で、マッチング辺を一つ含めるか、外の辺を一つ除外すれば十分です。完全マッチングがない成分があれば実行不可能です。これによりPM-A2の四通りが従います。\n\n')
 t+=('## Coverage and maintenance\n\nThis is a selective catalogue, not a complete classification of every graph class. In particular, no selectable-target planar-matching classification, planar shortest-path hardness, bounded-degree cut hardness, or all-model extension of the P11 abstract is asserted. These are literature-checking gaps, not declarations of open problems.\n\n' if lang=='en' else '## 収録範囲と更新\n\nすべてのグラフクラスを網羅した分類表ではありません。特に、目標選択matchingの平面版、最短路の平面版の困難性、cutの次数制限付き困難性、P11要旨の三モデルへの拡張は、この版では主張していません。これらは文献調査の未収録箇所であり、未解決問題の宣言ではありません。\n\n')
 t+=('[Machine-readable records](data/results.json) · [Reduction maps](REDUCTIONS.md) · [Verification](VERIFICATION.md)\n' if lang=='en' else '[機械可読データ](data/results.json) · [帰着の対応](REDUCTIONS.ja.md) · [確認記録](VERIFICATION.md)\n')
 (r/('RESULTS.md' if lang=='en' else 'RESULTS.ja.md')).write_text(t)
