# 合并上传说明文档 · 索引与执行摘要

> **用途**：把 `SurveyOfFTSG-main0913/`（今日修订成果，下称 **WS**）合并、提交到
> `github.com/alistairzyx2/SurveyOfFTSG` 的 `main` 分支。
> **生成时间**：2026-09-13
> **⚠️ 合并基准**：`e7fa6b0`（`fix(Figure 2): 根节点标题溢出框架，改为两行显示`）
> —— 侦察时为 `aa33670`，写文档期间仓库被推送了新提交，见 §3.4。
> `aa33670` 仍是**回滚目标**与**redline 默认基准**。
> **文档目录**：`SurveyOfFTSG-main0913/merge_docs/`

---

## 0. 文档清单

| 文件 | 内容 | 何时读 |
|---|---|---|
| `00_README_索引与执行摘要.md` | 本文件。全局结论、风险、决策记录 | **先读这个** |
| `01_仓库拓扑与血缘证明.md` | 仓库三份并存稿件的关系；`strip()` 血缘证明 | 想理解"为什么要这么改" |
| `02_变更文件清单.md` | 逐文件 before/after 与改动理由 | 做 code review |
| `03_Bib差异分类.md` | 102 条删除 / 3 条新增，分类为「别名重复」与「虚构」 | 审文献改动 |
| `04_合并操作命令.md` | **可直接复制粘贴的执行脚本** | **实际动手时** |
| `05_Redline生成指南.md` | 用 latexdiff 生成新一轮标记稿 | 做标记稿时 |
| `06_提交与推送指南.md` | commit message 模板 + 人工推送步骤 | 提交时 |
| `07_风险与回滚.md` | 已知风险、待决问题、完整回滚流程 | **动手前必读** |
| `08_冲突裁决_Figure2根节点.md` | ✅ **已决**：仓库 `e7fa6b0` 与 WS 对同一问题的两种改法 → **方案 A 已实施** | **记录 + 复核方法** |
| `09_被删条目正文处理审计.md` | 🆕 **22 篇被删文献的 26 个引用点逐处审计**：换挂 14 / 去具名 10 / 删文 2 | **答审稿人"是否丢内容"** |
| `_data/` | 机器可读的中间产物（JSON、diff） | 排查用 |
| `scripts/` | **5 个可执行脚本**，见 §0.1 | **实际动手时** |

### 0.1 脚本清单（`merge_docs/scripts/`）

全部已 `chmod +x`，`bash -n` 语法检查通过。

| 脚本 | 大小 | 作用 | 关键参数 |
|---|---:|---|---|
| `merge.sh` | 9.6 KB | 备份 + 成对替换 `sections/`+`bib` + 复制图片到两处 | `--dry-run`（默认）/ `--apply` |
| `verify.sh` | 6.1 KB | 双树重建 + 断言（errors/bibitems/`[?]`/页数） | `[root\|clean\|all]` |
| `redline.sh` | 9.1 KB | 从 git 历史用 latexdiff 生成新标记稿 | `[--no-build] [基准提交]` |
| `commit.sh` | 7.1 KB | 6 项预检 + 内嵌中文 commit message + 提交 | `--check-only` / `--amend` / `--push` |
| `rollback.sh` | 4.5 KB | 列回滚点 / 还原文件 / `git reset` | `--list` / `--files` / `--git` / `--all` |
| `audit_deleted_prose.sh` | 🆕 8 KB | 审计 22 篇被删文献的正文引用点如何改写（输出新旧句对照） | `[基准提交]`，默认 `e7fa6b0` |

> `audit_deleted_prose.sh` 输出「旧正文引用点合计 26 / 新正文残留 0」，
> 并按 key 打印【旧】/【新】句子对与相似度。**相似度 < 0.45 需人工判读**
> ——去具名改写会让比值掉到 0.3~0.5，不代表句子被删。

---

## 1. 执行摘要（TL;DR）

今天的修订**可以安全合并**，因为：

1. **血缘干净** —— 把仓库根目录 `sections/` 的修订宏剥掉后，**15 个文件里 13 个与
   `SurveyOfFTSG-main_clean/sections/` 逐字符完全相同**（见 `01`）。
   这说明 `main_clean/` 就是根目录的"无标记快照"，而 WS 是 `main_clean/` 的后代。
   **合并基础是干净的，不存在两套平行演化的历史。**

2. **改动量小** —— 11 个 `sections/` 文件、共 `+44 / -42` 行、43 个 hunk。
   其中 8 个文件只有 1–2 行改动。

3. **正文与文献库自洽** —— WS 引用 199 个 key，WS bib 含 204 条（199 被引用 +
   5 条仅出现在标记稿的删除标记里），`undefined` 计数为 **0**。

但**必须成对替换 `sections/` 与 `ultimate_complete.bib`** —— 见下。

---

## 2. 四项架构决策（已确认）

| # | 决策点 | 选择 |
|---|---|---|
| 1 | **落点** | 两份都更新：根目录 `sections/`+`bib`+`图` + 同步刷新 `main_clean/` |
| 2 | **标记稿** | 用 latexdiff 从 git 历史自动生成新一轮 redline |
| 3 | **bib 简并** | 是，`sections/` 与 `ultimate_complete.bib` **成对整体替换** |
| 4 | **推送方式** | **先 commit，不 push** —— 用户检查完 PDF 后自行推送 |

---

## 3. ⚠️ 三个必须先知道的事实

### 3.1 成对替换不是偏好，是硬约束（证据充分）

WS 与仓库的 bib key 命名体系不同。仓库用**别名 key**（`ARIMA`、`ImputeGAN`、
`CoFinDiff`、`MarS`、`Qlib`、`SD3`…），WS 用 **author-year key**
（`box2015time`、`qin2023imputegan`、`tanaka2025cofindiff`、`li2025mars`…）。
WS 正文里的 `\citep{}` 已全部改写为新体系。

**如果只换 bib 不换 `sections/`**：

```
### IF you copy repo prose but KEEP-GRAFT WS bib -> undefined keys: 27
GIFT-EVAL, Time-LLM, aksu2024gifteval, bamford2023, box1970, cai2025, chen2023b,
du2024, gao2024, gholamrezaei2023conditioning, lozano2023dual, miao2025, nater2025,
oppel2025, qian2024, qin2025, qiu2024tfb, shan2021, shankar2025, tao2024,
wang2021bigru, wang2024c, wi2023, zhang2023imputation, zhang2024spatial,
zhang2025a, zhou2024cross
```

→ 正文会出现 **27 个 `[?]`**。

**如果只换 `sections/` 不换 bib**：同样会因 `box2015time`、`li2025mars`、
`berti2025trades`、`wang2024mtsisurvey` 等 key 缺失而报错。

✅ **唯一正确做法：两者同时替换。** `04_合并操作命令.md` 里的脚本已把这两步绑成
一个原子操作。

### 3.2 Table 1 的 `# refs` 列 —— 已确认 `199` 正确，**不需要改回 131**

上游（根目录 / `main_clean/`）该单元格是 `131`，WS 是 `199`。曾怀疑是语义冲突，
**现已查清 `199` 是对的**：

| 证据 | 说明 |
|---|---|
| 表 1 caption 原文 | "\textbf{\# refs} is the count of **references cited** in each survey" |
| 同列其他行的口径 | `318`（Nie et al.）、`115`（Arsenault et al.）—— 都是**被引文献数**，不是语料规模 |
| WS 实际被引数 | `is26.bbl` = **199** 条 ✅ |
| WS 的 Window 列 | `1950--2026` —— WS bib 最早年份确为 **1950**，与 `199` 同源 ✅ |
| 上游的 `131` | 是**语料规模**（`修改内容清单_20260913.md` 里"语料 131 篇"），语义与该列不符 ❌ |

**结论**：WS 的 `199` 修正了上游一处口径错误。而且 WS **已经**同步把 caption 扩写了
一句说明 Window 为何向前延伸：

> `...\textbf{Window} is the publication-year range of each survey's references;
> for this survey it extends before the 2021--early 2026 search window because
> foundational statistical and econometric references are retained.`

✅ **此项无需任何额外操作**，直接采用 WS 版本。

### 3.3 根目录的 802 处 `\revadd`/`\revdel` 标记会被"压平"

根目录 `sections/` 目前带自制修订宏（`\revadd`/`\revdel`/`\revaddblock`/
`\revdelblock`/`\revnote`/`\markadd`/`\markdel`/`\citebox`，共 802 处），
用于构建 `is26_marked.pdf`（59 页红色标记稿）。

今日改动是**在无标记文本上**做的，因此：

- 覆盖根目录 `sections/` 后，`\revadd` 历史标记 **全部消失**
- `is26_marked.pdf` 将退化为与 `is26.pdf` 内容一致
- **这是决策 #1 与 #2 的必然结果** —— 用 `latexdiff` 从 git 历史重新生成标记稿来替代
  （见 `05_Redline生成指南.md`）

> 💡 若你希望**保留**历史 `\revadd` 标记链，请在执行前告知，改走
> `05_Redline生成指南.md` §7 的"替代方案"。

### 3.4 🆕 仓库已被推送到 `e7fa6b0`，产生 Figure 2 冲突

侦察时 HEAD 是 `aa33670`；写文档期间你推送了 `e7fa6b0`，
**独立修复了 Figure 2 根节点的同一个溢出问题，但改法不同**。

| | 根节点写法 | 渲染为 |
|---|---|---|
| 仓库 `e7fa6b0` | `[{Financial Time Series\\Generation}, …]` | `Financial Time Series` / `Generation` |
| WS | `[Financial Time\\Series Generation, …]` | `Financial Time` / `Series Generation` |

**实测**：两版**都能编译、都无溢出、页面尺寸都是 `623.62 × 467.72 pt`**，
仅换行位置不同。

⚠️ **但文件级差异有 7 行**，其中 **6 行是 WS 独有的语义修订**
（新增 `Controllable & Multimodal Models` 分支、`WaveGAN`→`Wavelet-based GAN`、
扩散模型清单更新等）。**绝不能整体采用仓库文件**（会丢失这 6 行）。

➡️ **已按方案 A 处理完毕**：保留 WS 全部 6 行语义修订，根节点采用仓库换行形式。
`standalone_fig2.tex` 与 `separate_figures/Figure2.pdf` 均已更新（详见 `08` §7）。

**验证结果**：页面 623.62 × 467.72 pt、0 errors、右溢出 **−16.69 pt**（仓库版 −17.06 pt），
**无溢出**。详见 `08_冲突裁决_Figure2根节点.md` §7.2。

**连带发现**：`main_clean/separate_figures/Figure2.pdf`（125,037 B）
**没有**跟上 `e7fa6b0`（根目录 125,047 B），已经开始脱节 —— 本轮合并顺带修复。

---

## 4. 变更规模一览

### 4.1 `sections/` 逐文件改动（`main_clean/` → WS）

| 文件 | +行 | −行 | hunk 数 |
|---|---:|---:|---:|
| `01_introduction.tex` | 1 | 1 | 1 |
| `02_methodology.tex` | 1 | 1 | 1 |
| `03_problem_taxonomy.tex` | 2 | 2 | 2 |
| `04_extrapolation.tex` | 5 | 5 | 5 |
| `05_imputation.tex` | 11 | 11 | 11 |
| `06_synthesis.tex` | 5 | 5 | 5 |
| `07_applications.tex` | 9 | 7 | 3 |
| `09_data_resources.tex` | 1 | 1 | 1 |
| `10_challenges.tex` | 1 | 1 | 1 |
| `13_figures.tex` | 2 | 2 | 2 |
| `14_tables.tex` | 6 | 6 | 5 |
| **合计** | **44** | **42** | **37** |
| `00_abstract` / `08_evaluation` / `12_declarations` | — | — | 0（未改动） |

> 注：`diff -r` 报告的 hunk 数（43）略高于逐文件合计（37），差异来自跨文件
> `--unified` 上下文合并计数，属正常。

### 4.2 文献库

| 指标 | 仓库（`main_clean/`） | WS | 变化 |
|---|---:|---:|---|
| bib 条目数 | 303 | **204** | −99 |
| 被引用 key 数 | 221 | **199** | −22 |
| **孤儿条目**（未被引用） | **82** | **5** | **−77** ✅ |
| `is26.bbl` 渲染条目 | 222 | **199** | −23 |
| 最早 / 最新年份 | 1950 / 2026 | 1950 / 2026 | — |

> **孤儿从 82 降到 5** 是本轮最大的文献学成果 —— 直接回应审稿人"重复参考文献"意见。

**97 条删除的四象限分解**（详见 `03_Bib差异分类.md`）：

```
                        被仓库正文引用      未被引用（孤儿）
                       ┌──────────────────┬──────────────────┐
   别名风格 (40)       │        0         │       40   ✅安全 │
                       ├──────────────────┼──────────────────┤
   author-year (57)    │       22 ⚠️       │       35   ✅安全 │
                       └──────────────────┴──────────────────┘
```

- **40 个别名 key 引用次数为 0** —— 纯孤儿（这正是审稿人说的"重复参考文献"）
  其中 **15 个**已用标题匹配证明与 author-year key 是同文异键：
  `AttnWGAIN`=`wang2025attn`、`CTS-GAN`=`istiaque2024cts`、`CWGAIN-GP`=`wang2024cwgain`、
  `DDPM-based`=`takahashi2024generation`、`DiGA`=`huang2024diga`、`ETT`=`zhou2021informer`、
  `FinTSBridge`=`wang2025fintsbridge`、`GBMDiff`=`kim2025gbm`、`ImputeGAN`=`qin2023imputegan`、
  `MC-TE-GAN`=`alex2024macroeconomic`、`MarS`=`li2025mars`、`N-BEATS-GAN`=`dai2026nbeats`、
  `OneFitsAll`=`zhou2023onefitsall`、`TRADES`=`berti2025trades`、`QuantGAN`=`wiese2020`
- **只有 22 个**被删 key 需要正文改写（已全部完成），清单见 `_data/cited_removed.json`
- 其余 **75 条删除是零风险**（无任何正文引用）

### 4.3 图片

| 文件 | 仓库 | WS | 说明 |
|---|---:|---:|---|
| `separate_figures/Figure1.pdf` | 55,569 B | **55,786 B** | 重新生成 |
| `separate_figures/Figure2.pdf` | 125,037 B | **126,429 B** | 重新生成 |

---

## 5. 五条命令搞定（完整脚本见 `04`）

```bash
# ---- 前置：一律先设置 PATH ----
export PATH="/Library/TeX/texbin:$PATH"
cd "/Volumes/FunkDisk/Study/PHD/论文发表/论文一：金融数据合成综述"

# 1) 干跑（dry-run）：只打印将要做什么，不落盘
bash SurveyOfFTSG-main0913/merge_docs/scripts/merge.sh --dry-run

# 2) 真正执行：成对替换 sections + bib，同步两份，复制图片
bash SurveyOfFTSG-main0913/merge_docs/scripts/merge.sh --apply

# 3) 编译校验（两个 build tree 各自编译）
bash SurveyOfFTSG-main0913/merge_docs/scripts/verify.sh

# 4) 生成新一轮 redline
bash SurveyOfFTSG-main0913/merge_docs/scripts/redline.sh

# 5) 提交（不推送）
bash SurveyOfFTSG-main0913/merge_docs/scripts/commit.sh
```

---

## 6. 提交前检查清单

- [ ] `merge.sh --dry-run` 输出与本文件 §4 的规模相符
- [ ] `verify.sh` 报告 `errors: 0` / `undefined: 0` / `bibitems: 199`
- [ ] `is26.pdf` 页数与预期一致（54 页左右）
- [ ] Table 1 渲染为 `... & 199 & 1950--2026 \\`
- [ ] 全文搜索 `[?]` 结果为 0
- [ ] 11 个已删虚构文献 key 在 `is26.pdf` 中**不出现**
- [ ] `git status` 显示的改动文件列表符合预期
- [ ] **确认没有 push**（本轮只 commit）

---

## 7. 待你决策的事项

| # | 事项 | 建议 | 状态 | 详见 |
|---|---|---|---|---|
| **E** | **Figure 2 根节点：方案 A / B** | **方案 A** | ✅ **已决并已实施**（`Figure2.pdf` 已重生成） | `08` §7 |
| A | 根目录 802 处 `\revadd` 标记压平后，`is26_marked.pdf` 如何处理 | 用 latexdiff 新标记稿替换 | ✅ 决策 #2 已定 | `05` |
| B | 回复信/清单里的 **222** 条 vs 稿件的 **199** 条 | 需同步改口径 | ⚠️ **推送前必须处理** | `06` §6、`07` §4 |
| C | 是否继续跟踪 LaTeX 编译中间产物（`.aux/.bbl/.log` 等） | 建议本轮不动，后续单独提交 | 可延后 | `06` §7、`07` §7 |
| D | `sections/11_conclusion.tex`（仅根目录有，未被任何 master 引用） | 建议保留不动 | 已纳入脚本保护 | `02` §5 |

---

## 8. 环境准备（一次性）

```bash
export PATH="/Library/TeX/texbin:/opt/homebrew/bin:$PATH"
brew install latexdiff          # 仅在需要生成标记稿时
```

> ⚠️ `latexmk` **未安装且不需要**，构建走 `pdflatex → bibtex → pdflatex ×2`。
> ⚠️ `tlmgr install latexdiff` **会失败**（TeX Live 装在只读的 `/usr/local/texlive`）。
> ⚠️ 首次 `brew` 可能触发一次性的 `brew vendor-install ruby` 引导，**较慢**，等它跑完。

---

## 9. 一键回滚

```bash
cd "/Volumes/FunkDisk/Study/PHD/论文发表/论文一：金融数据合成综述/SurveyOfFTSG-main0913/merge_docs/scripts"
./rollback.sh --list      # 看回滚点
./rollback.sh --files     # 文件级还原（保留提交历史）
./rollback.sh --git       # git reset --hard aa33670（丢弃提交）
```

手动版：
```bash
cd "/Volumes/FunkDisk/Study/PHD/论文发表/论文一：金融数据合成综述/SurveyOfFTSG"
git reset --hard aa33670        # 提交之前的出发点
git clean -fd                   # 清理未跟踪文件
```

详见 `07_风险与回滚.md` §8。

---

## 10. 最短路径（TL;DR）

```bash
export PATH="/Library/TeX/texbin:/opt/homebrew/bin:$PATH"
cd "/Volumes/FunkDisk/Study/PHD/论文发表/论文一：金融数据合成综述/SurveyOfFTSG-main0913/merge_docs/scripts"

# ⛔ 先在 08 选好 Figure 2 方案（A / B）

./merge.sh --dry-run     # 1. 预演
./merge.sh --apply       # 2. 执行
./verify.sh              # 3. 双树编译 + 断言
brew install latexdiff   # 4. 装 latexdiff（一次性）
./redline.sh             # 5. 生成标记稿
./commit.sh              # 6. 提交（不推送）

# 7. 人工复核三个 PDF，处理回信 222→199（见 06 §6）
cd "../.." && git -C ../SurveyOfFTSG push origin main
```

---

## 11. 📌 执行记录（2026-09-13 实际执行结果）

本节记录**真实执行**留下的数据与踩到的坑，供复核与下一次修订复用。

### 11.0 ✅ 最终结果

| 项 | 值 |
|---|---|
| **提交** | **`037101e`** — `fix(文献审计): 合并今日修订 —— 引用去伪存真、孤儿清理、图表同步` |
| 远端状态 | **未推送**（按决策 #4，你复核 PDF 后自行 `git push origin main`） |
| 领先远端 | **1 个提交** |
| 工作区 | **完全干净**（`git status` 无输出） |
| 提交规模 | 42 个文件，+2,079 / −5,386 行 |

### 11.1 执行结果一览

| 步骤 | 命令 | 结果 |
|---|---|---|
| 1 | `./merge.sh --dry-run` | ✓ 全部检查通过，Figure2.pdf 126,422 B 被正确拾取 |
| 2 | `./merge.sh --apply` | ✓ 两树各覆盖 14 个 `.tex`；bib → 204；4 张图复制完成 |
| 3 | `./verify.sh all` | ✓ **exit=0，全部断言通过** |
| 4 | `./redline.sh` | ✓ 55 页 / 199 bibitems / 0 error |
| 5 | `./commit.sh` | ✓ 提交 `037101e`（未推送） |

**备份位置**：`merge_docs/.merge_backup_20260913_211243/`
**回滚基准**：提交 `aa33670`（`e7fa6b0` 之前一个提交）

### 11.2 合并后实测（`verify.sh all` 原文）

```
══ 根目录  ·  .../SurveyOfFTSG ══            ══ main_clean ══
  ✓ LaTeX errors        0                      ✓ 0
  ✓ bibtex warnings     0                      ✓ 0
  ✓ bibitem count       199  (期望 199)        ✓ 199
  ✓ undefined citations 0                      ✓ 0
  ✓ page count          54                     ✓ 54
  · overfull hbox       3 个，最大 4.82483pt   · 同
  ✓ PDF 内 '[?]'        0 次                   ✓ 0

══ 交叉断言 ══
  根目录 199 / main_clean 199 / 工作区 199
  三处 ultimate_complete.bib 均为 204 条
```

两棵树产出的 `is26.pdf` 均为 **5,146,843 B / 54 页**，字节级一致。

### 11.3 标记稿（redline）实测

以 `aa33670` 为基准，用 `latexdiff --type=UNDERLINE` 自动生成：

| 指标 | 值 |
|---|---:|
| `is26_redline.tex` | 159,749 B / 1,215 行 |
| `is26_redline.pdf` | 55 页 |
| `DIFadd` / `DIFdel` | 237 / 263 |
| `\DIFaddbegin` / `\DIFdelbegin` | 80 / 80 |
| 蓝色新增字符 | 6,703 |
| 红色删除字符 | 2,253 |
| LaTeX errors | 0 |
| overfull hbox | 10（latexdiff 固有，非缺陷） |

### 11.4 ⚠️ 本轮修正的四个脚本缺陷（均已修复并注释）

这四个坑都会**静默出错**（不报错但结果错误），值得记录：

1. **`--show-preamble` 会让 latexdiff 只输出 preamble 就退出**
   —— 输出从 1215 行 / 159 KB 塌缩到 89 行 / 5 KB，正文全丢，编译报 2 个 error。
   脚本后处理阶段本就改用镜像自己的 preamble，**该选项必须永不启用**。

2. **`--add-to-config` 必须写成 `varenv=pattern`**
   —— 裸写该 flag 会把下一个参数（文件名）当作赋值目标吞掉，报
   `Illegal assignment \documentclass[11pt,a4paper]{article} in configuration list`。

3. **`$(grep -c PAT FILE || echo 0)` 会得到两行 `"0\n0"`**
   —— `grep -c` 零匹配时既打印 `0` 又返回退出码 1，导致 `|| echo 0` 也执行。
   已统一改为 `cnt()` 助手（`head -1` + 兜底）。

4. **shell 变量名 `B`/`R`/`G`/`Y`/`N` 与 ANSI 颜色码冲突**
   —— `verify.sh` 用 `B` 存 bibitem 计数，`rollback.sh` 用 `B` 存备份路径，
   与青色变量撞车，输出出现 `199══ 总结 ══` 这类粘连。
   已重命名为 `BIB_R`/`BIB_C`/`BIB_W` 与 `BK`。

### 11.5 已顺手清理的仓库卫生问题

- `commit.sh` 首轮提交时误纳入 11 个构建中间产物
  （`main_clean/is26.aux`、`verify_build.log` 等），已 `git rm --cached` 并新增
  `.gitignore` 规则阻止复发。
- **已跟踪**的产物（`is26.pdf`、`is26.bbl`、`is26_redline.pdf`、`Figure*.pdf`）
  不受 `.gitignore` 影响，仍正常提交 —— 这是有意的，见 `06` §7。
- 误删的 `is26.fdb_latexmk` / `is26.fls` 已用 `git checkout --` 还原。

### 11.6 ⏭️ 推送前仍需你处理的唯一事项

**回信里的参考文献数字与实际不符**（详见 `06` §6）：

| 位置 | 现值 | 应为 |
|---|---|---|
| `response_to_reviewers_final.md` | 4× `131`、2× `222` | `199` |
| `response_to_technical_check_final.md` | 1× `222` | `199` |
| `修改内容清单_20260913.md` | 12× `131`、9× `222`、6× `130` 等 | 统一为 `131`（语料）/ `199`（引用） |

`d90bd4d` 曾把回信数字统一改成 `222`，但最终稿实际编译结果是 **199**
（`131` 是语料规模，`222` 是旧 bib 时代的引用数）。**这项未自动修改**，
因为它属于对外文书，需你确认口径后手动改。见 `06_提交与推送指南.md` §6。
