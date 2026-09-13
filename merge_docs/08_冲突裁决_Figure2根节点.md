# 08 · ✅ 冲突裁决：Figure 2 根节点（已决：方案 A）

> **✅ 本冲突已裁决并修复完毕（方案 A）。** 保留本文档以记录决策依据与复核方法。
> 侦察时（HEAD = `aa33670`）没有这个冲突。写文档过程中发现仓库已被推送到
> **`e7fa6b0`**，该提交独立修复了 Figure 2 根节点的同一个溢出问题，
> 但**改法与工作区不同**。

---

## 1. 发生了什么

| | 时间 | 内容 |
|---|---|---|
| 工作区 `standalone_fig2.tex` | 09-13 **20:14** | 你今天的版本：语义修订 + 根节点换行 |
| 仓库 `e7fa6b0` | 09-13 **20:50** | 另一次提交：**只**改根节点换行 |

`e7fa6b0` 的提交说明：

> 问题：根节点 "Financial Time Series Generation" 单行渲染宽 126.94pt，
> 而节点框仅 101.69pt（由 text width=4.5cm 决定），右侧溢出 27.98pt。
>
> 方案对比：
>   - 加宽至 6.0cm：消除溢出，但整图文字被缩小 5.4%（x0.9464）
>   - **手动换行（采用）**：右溢出 -17.06pt，全局缩放 x1.0000，零副作用

---

## 2. 两侧改法不同

**仓库 `e7fa6b0`**（换行点在 Series 之后，且加了 `{}` 成组）：
```latex
[{Financial Time Series\\Generation}, root, text width=4.5cm, align=center
```
渲染为：`Financial Time Series` / `Generation`

**工作区**（换行点在 Time 之后，无 `{}`）：
```latex
[Financial Time\\Series Generation, root, text width=4.5cm, align=center
```
渲染为：`Financial Time` / `Series Generation`

---

## 3. 实测结果：两版都能编译，都无溢出

```
$ pdflatex repo.tex / ws.tex
repo   errors=0  pdf=125047 bytes   page=623.6 x 467.7 pt
ws     errors=0  pdf=126429 bytes   page=623.6 x 467.7 pt
```

| 指标 | 仓库版 | 工作区版 |
|---|---|---|
| LaTeX errors | 0 | 0 |
| 页面尺寸 | 623.62 × 467.72 pt | 623.62 × 467.72 pt |
| 根节点行数 | 2 行 | 2 行 |
| 文字块总数 | 35 | 35 |
| 溢出 | 无 | 无 |
| 行宽平衡 | `Financial Time Series`(21) / `Generation`(10) | `Financial Time`(14) / `Series Generation`(17) |
| 左边界 | x=35.6 | x=40.4 |

**结论：两者视觉上均正确，仅换行位置不同。** 工作区版的换行更均衡（14/17 vs 21/10）。

---

## 4. 真正的问题：文件级差异远不止根节点

`diff -u` 显示两版有 **7 处**不同，其中 **6 处**是工作区的语义修订，
且这些修订**只存在于工作区**：

| # | 位置 | 仓库 `e7fa6b0` | 工作区 | 性质 |
|---|---|---|---|---|
| 1 | 根节点 | `{Financial Time Series\\Generation}` | `Financial Time\\Series Generation` | ⚠️ 冲突 |
| 2 | 外推/GAN | `GAN, WaveGAN, N-BEATS-GAN, WGAN-GP` | `GAN, Wavelet-based GAN, N-BEATS-GAN, WGAN-GP` | ✅ 工作区对 |
| 3 | 外推 | 无 `Controllable & Multimodal Models` 分支 | **新增该分支**（TimeWeaver, T2S） | ✅ 工作区对 |
| 4 | 插补/扩散 | `CSDI, Score-CDM, SSSD, TimeDiT, LSCD` | `CSDI, LSSDM, Score-CDM, SaSDim, SPDM, TimeDiT, LSCD` | ✅ 工作区对 |
| 5 | 插补/高级框架 | `Foundation Models & Dual Graph: … Dual-Bipartite Graph Network` | `Foundation Models & Graph-Augmented: LLM-Forest, MTabGen` | ✅ 工作区对 |
| 6 | 合成/经典 | `SDEs (GBM, Heston Model)` | `SDEs with GBM priors` | ✅ 工作区对 |
| 7 | 合成/扩散 | `TimeGrad, SGM, CoFinDiff, FinDiff` | `TimeGrad, CoFinDiff, Fin-DDPM, GBM-Diff, Fin-Denoiser` | ✅ 工作区对 |

> **关键判断**：`e7fa6b0` 只动了第 1 行（根节点），其提交说明亦自述
> "文字差异仅根节点换行一行，其余 45 行完全一致"。
> 第 2–7 行的语义修订**来自工作区，是今天的成果**，必须保留。

---

## 5. 三个可选方案

| 方案 | 做法 | 结果 | 风险 |
|---|---|---|---|
| **A（推荐）** | 用工作区文件，但把根节点改回仓库的 `{Financial Time Series\\Generation}` | 保留全部语义修订 + 与已推送的 `e7fa6b0` 视觉一致 | 换行略不均衡 |
| **B** | 纯用工作区文件（含其自己的根节点换行） | 保留全部语义修订 + 更均衡换行 | 与 `e7fa6b0` 的根节点渲染**不同**（`)` 说明里说已修复，但表现变了） |
| **C** | 纯用仓库文件 | — | ❌ **丢失第 2–7 行全部语义修订**，不可接受 |

### 方案 A 的具体操作

```bash
cd "/Volumes/FunkDisk/Study/PHD/论文发表/论文一：金融数据合成综述/SurveyOfFTSG-main0913"
python3 - <<'PY'
p='standalone_fig2.tex'
s=open(p,encoding='utf-8').read()
old='  [Financial Time\\\\Series Generation, root, text width=4.5cm, align=center\n'
new='  [{Financial Time Series\\\\Generation}, root, text width=4.5cm, align=center\n'
assert s.count(old)==1, "found %d"%s.count(old)
open(p,'w',encoding='utf-8').write(s.replace(old,new))
print("根节点已改为仓库形式")
PY
# 重新生成 Figure2.pdf
export PATH="/Library/TeX/texbin:$PATH"
pdflatex -interaction=nonstopmode standalone_fig2.tex >/dev/null 2>&1
cp -f standalone_fig2.pdf ../SurveyOfFTSG-main0913/separate_figures/Figure2.pdf
```

> ⚠️ 注意：`standalone_fig2.tex` 生成的是 **一页整图**，
> 需要与 `separate_figures/Figure2.pdf` 的页面尺寸一致（623.62 × 467.72 pt）。
> 若 `standalone_fig2.pdf` 的页面尺寸不同，需用 `pdfcrop` 或直接调整
> `standalone_fig2.tex` 的 `geometry`。

---

## 6. ⚠️ 另一个连带问题：`main_clean/` 的图也过期了

| 位置 | Figure2.pdf 大小 | md5 |
|---|---:|---|
| 仓库 **根目录** | 125,047 B | `b409beea…` |
| **`main_clean/`** | 125,037 B | `695d3ec3…` |
| 工作区 | 126,429 B | `06e5eabe…` |

`main_clean/separate_figures/Figure2.pdf` 最后一次变更是 **`aa33670`**，
**没有**跟上 `e7fa6b0` 的根节点修复 —— 说明 `main_clean/` 已经开始与根目录脱节。

> 本轮合并会把三处统一到同一个文件，顺带修好这个脱节。

---

## 7. 决策记录

> ### ✅ 已决：**方案 A** —— 工作区语义 + 仓库根节点换行
>
> **决定已执行**，`standalone_fig2.tex` 与 `separate_figures/Figure2.pdf` 均已更新。
> 详见下方 §7.2 验证结果。

```
[x] 方案 A —— 工作区语义 + 仓库根节点换行（推荐）   ← 采纳
[ ] 方案 B —— 纯工作区文件
[ ] 其他：________________________________

决定人：alistairzyx2      日期：2026-09-13
```

### 7.1 已执行的操作

```bash
# 1) 备份原工作区版本
cp standalone_fig2.tex /tmp/fig2_ws_backup.tex

# 2) 根节点改为仓库形式（Python 精确替换，assert s.count(old)==1 通过）
#    旧：  [Financial Time\\Series Generation, root, text width=4.5cm, align=center
#    新：  [{Financial Time Series\\Generation}, root, text width=4.5cm, align=center

# 3) 重新生成并安装到 separate_figures/
pdflatex -interaction=nonstopmode standalone_fig2.tex
cp standalone_fig2.pdf separate_figures/Figure2.pdf
```

### 7.2 修复后实测（用 PyMuPDF 逐 span 测量，非目测）

| 指标 | 工作区修复前 | **工作区（方案 A）** | 仓库 `e7fa6b0` |
|---|---:|---:|---:|
| LaTeX errors | 0 | **0** | 0 |
| 页面尺寸 | 623.62 × 467.72 pt | **623.62 × 467.72 pt** ✅ | 623.62 × 467.72 pt |
| PDF 字节 | 126,429 | **126,422** | 125,047 |
| 根节点框宽 | 99.48 pt | **99.48 pt** | 101.69 pt |
| 根节点文字宽 | 65.68 pt | **80.12 pt** | 81.90 pt |
| 右溢出 | −31.13 pt | **−16.69 pt** ✅ | −17.06 pt |
| 判定 | 无溢出 | **无溢出** ✅ | 无溢出 |

> **结论**：方案 A 的根节点右溢出为 **−16.69 pt**，与仓库 `e7fa6b0` 的 −17.06 pt
> 几乎一致（差 0.37 pt），页面尺寸完全相同，**无溢出**。

### 7.3 复核命令

```bash
BASE="/Volumes/FunkDisk/Study/PHD/论文发表/论文一：金融数据合成综述"
WS="$BASE/SurveyOfFTSG-main0913"

# 1) 根节点确实已改为仓库形式
grep -n 'root, text width=4.5cm' "$WS/standalone_fig2.tex"
#   -> 42:  [{Financial Time Series\\Generation}, root, text width=4.5cm, align=center

# 2) 与仓库的差异应只剩 6 处「工作区语义修订」+ 1 处 Conditional GANs，共 17 行 +/- 差异
diff "$BASE/SurveyOfFTSG/standalone_fig2.tex" "$WS/standalone_fig2.tex" | grep -cE '^[<>]'
#   -> 17

# 3) 页面尺寸与溢出（逐 span 测量）
python3 - <<'PY'
import pymupdf
p = pymupdf.open("separate_figures/Figure2.pdf")[0]
spans = [(pymupdf.Rect(s['bbox']), s['text'])
         for b in p.get_text('dict')['blocks'] for l in b.get('lines', [])
         for s in l['spans'] if s['text'].strip()]
boxes = [d['rect'] for d in p.get_drawings()
         if 20 < d['rect'].width < 420 and 8 < d['rect'].height < 60]
r = [b for b in sorted(boxes, key=lambda q: q.x0)
     if sum(1 for sr, _ in spans if b.contains(sr)) >= 2][0]
tb = None
for sr, _ in spans:
    if r.contains(sr): tb = sr if tb is None else tb | sr
print("页面   " + str(tuple(round(x, 2) for x in p.rect)))
print("根节点框 x %.2f..%.2f" % (r.x0, r.x1))
print("根节点文字 x %.2f..%.2f" % (tb.x0, tb.x1))
print("右溢出 %+.2f pt  %s" % (tb.x1 - r.x1, "OK" if tb.x1 <= r.x1 else "FAIL"))
PY
```

---

## 8. 复核命令

```bash
BASE="/Volumes/FunkDisk/Study/PHD/论文发表/论文一：金融数据合成综述"

# 1. 看两版差异
diff -u "$BASE/SurveyOfFTSG/standalone_fig2.tex" \
        "$BASE/SurveyOfFTSG-main0913/standalone_fig2.tex"

# 2. 确认 e7fa6b0 只改了根节点
git -C "$BASE/SurveyOfFTSG" show e7fa6b0 -- standalone_fig2.tex

# 3. 三处 Figure2.pdf 是否一致
for f in "$BASE/SurveyOfFTSG/separate_figures/Figure2.pdf" \
         "$BASE/SurveyOfFTSG/SurveyOfFTSG-main_clean/separate_figures/Figure2.pdf" \
         "$BASE/SurveyOfFTSG-main0913/separate_figures/Figure2.pdf"; do
  printf "%-78s %8s B  %s\n" "${f#$BASE/}" "$(stat -f%z "$f")" "$(md5 -q "$f" | cut -c1-8)"
done
```
