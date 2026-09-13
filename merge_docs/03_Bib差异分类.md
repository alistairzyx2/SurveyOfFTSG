# 03 · Bib 差异分类（97 条删除 / 3 条新增）

> **核心结论先说**：97 条被删的 key 中，**只有 22 条需要改动正文**，
> 其余 75 条**本来就是无人引用的孤儿条目**，删除它们是零风险的清灰。
> 而 40 个"厂商名风格"的别名 key **全部**是孤儿 —— 它们正是审稿人所说"重复参考文献"的来源。
>
> 数据文件：`_data/bib_delta.json`、`_data/alias_map.json`、`_data/cited_removed.json`

---

## 1. 总量对照

| 指标 | 仓库（`main_clean/`） | WS 原有（`.bak`） | WS 现行 |
|---|---:|---:|---:|
| bib 条目数 | **303** | 298 | **204** |
| 被正文引用的 key | 221 | — | **199** |
| **孤儿条目**（无引用） | **82** | — | **5** |
| `is26.bbl` 渲染条目 | 222 | — | **199** |

**集合关系**（关键）：
```
WS原有(298) ⊂ 仓库(303)          ← 仓库完全是 WS 的超集，0 个 WS 独有 key
仓库独有(5)  = Time-LLM, WaveletGAN, aksu2024gifteval, box1970, qiu2024tfb
WS 新增(3)   = frino2018macroeconomic, richter2024survey, wang2024mtsisurvey
```

---

## 2. 97 条删除项的四象限分解

```
                    被仓库正文引用      未被引用（孤儿）
                   ┌──────────────────┬──────────────────┐
   别名风格 (40)   │        0         │       40   ✅安全 │
                   ├──────────────────┼──────────────────┤
   author-year(57) │       22 ⚠️       │       35   ✅安全 │
                   └──────────────────┴──────────────────┘
                              ↑
                    只有这 22 条需要"动正文"
```

| 类别 | 数量 | 说明 |
|---|---:|---|
| **A. 别名 key · 孤儿** | **40** | 厂商/模型名 key，无人引用 → 纯垃圾，直接删 |
| **B. author-year · 孤儿** | **35** | 其他遗留孤儿 → 直接删 |
| **C. author-year · 被引用** | **22** | **必须改写正文**（本轮的核心外科手术） |
| 合计 | **97** | |

> ✅ **75 条（A+B）删除对正文零影响** —— 已用 `strip()` 解析仓库根目录全部 15 个
> `sections/` 文件后统计 `\cite*{}` 调用验证。

---

## 3. A 类：40 个别名 key（全部是孤儿）

这些 key 用**模型名 / 厂商名 / 缩写**命名，正是"重复参考文献"问题的来源。

### 3.1 已用标题匹配证实的别名（15 个，相似度 = 1.00）

| 仓库别名 key | → WS author-year key | 标题相似度 |
|---|---|---:|
| `AttnWGAIN` | `wang2025attn` | **1.00** |
| `CTS-GAN` | `istiaque2024cts` | **1.00** |
| `CWGAIN-GP` | `wang2024cwgain` | **1.00** |
| `DDPM-based` | `takahashi2024generation` | **1.00** |
| `DiGA` | `huang2024diga` | **1.00** |
| `ETT` | `zhou2021informer` | **1.00** |
| `FinTSBridge` | `wang2025fintsbridge` | **1.00** |
| `GBMDiff` | `kim2025gbm` | **1.00** |
| `ImputeGAN` | `qin2023imputegan` | **1.00** |
| `MC-TE-GAN` | `alex2024macroeconomic` | **1.00** |
| `MarS` | `li2025mars` | **1.00** |
| `N-BEATS-GAN` | `dai2026nbeats` | **1.00** |
| `OneFitsAll` | `zhou2023onefitsall` | **1.00** |
| `TRADES` | `berti2025trades` | **1.00** |
| `QuantGAN` | `wiese2020` | 0.99 |

> 相似度 1.00 表示 **title 字段逐字符相同** —— 同一篇文献被登记了两遍，铁证。

### 3.2 标题较短、无法自动匹配的其余 25 个

这些 key 的 `title` 字段过短（如 `ARIMA`、`VAR`、`GARCH`、`Qlib`、`MIMIC`、
`PixArt`、`SD3`、`LDM`）导致自动相似度匹配不可靠，但**已确认它们在仓库正文中
引用次数为 0**，属纯孤儿：

```
ARIMA, BSM-DRL, BiLSTM-ARIMA, CFTNet, CoFinDiff, FLLM, FinTSB, Fraud, FunctionalVAR,
FuseDiT, GARCH, LASSO-SMLR-PCA, LDM, LVQ-CBR, MIMIC, Market-GAN, PixArt, QWGAN-GP,
Qlib, RMT-Net, SD3, TimeGAN-3D-CNN, VAE-GRU-MCMC, VAR, WGAN-BiLSTM
```

> 注：`CoFinDiff` / `Qlib` / `MIMIC` / `SD3` / `LDM` 这类名字在 WS 里都有对应的
> author-year key（`tanaka2025cofindiff` 等），因此也是重复登记。

---

## 4. C 类：22 条必须动正文的 key

**这是唯一需要外科手术的部分。**

```
bamford2023      cai2025        chen2023b       du2024         gao2024
gholamrezaei2023conditioning   lozano2023dual  miao2025       nater2025
oppel2025        qian2024       qin2025         shan2021       shankar2025
tao2024          wang2021bigru  wang2024c       wi2023         zhang2023imputation
zhang2024spatial zhang2025a     zhou2024cross
```

### 4.1 处置方式一览

| key | 处置 | 详见 |
|---|---|---|
| `bamford2023` | **去具名** → "have been proposed" | `02` §4 |
| `cai2025` | **去具名** → TGN 归属改挂 `rossi2020temporal` | `02` §4 |
| `chen2023b` | 去具名/删除 | `02` §4 |
| `du2024` | **替换** → `wang2024mtsisurvey,richter2024survey` | `02` §4 |
| `gao2024` | **去具名** → `wang2024mtsisurvey` | `02` §4 |
| `gholamrezaei2023conditioning` | **替换** → `wang2024mtsisurvey` | `02` §4 |
| `lozano2023dual` | **去具名** → "dual-sourced diffusion networks" | `02` §4 |
| `miao2025` | 去具名 | `02` §4 |
| `nater2025` | **去具名** → "are being developed" + `richter2024survey` | `02` §4 |
| `oppel2025` | **去具名** → "conditional generators are now being embedded" | `02` §4 |
| `qian2024` | 去具名 → `wang2024mtsisurvey` | `02` §4 |
| `qin2025` | **整段删除** | `02` §4 |
| `shan2021` | **替换** → `wang2024mtsisurvey,richter2024survey` | `02` §4 |
| `shankar2025` | 去具名 | `02` §4 |
| `tao2024` | **去具名** → "Distillation techniques … have been introduced" | `02` §4 |
| `wang2021bigru` | **去具名** → "bidirectional GRU--LSTM frameworks" | `02` §4 |
| `wang2024c` | 去具名 | `02` §4 |
| `wi2023` | **去具名** → 改写为祈使陈述句 | `02` §4 |
| `zhang2023imputation` | 去具名 | `02` §4 |
| `zhang2024spatial` | **去具名** → "horizons," | `02` §4 |
| `zhang2025a` | 去具名 | `02` §4 |
| `zhou2024cross` | **去具名** → "across boundaries." | `02` §4 |

### 4.2 处置原则

> **保留技术论断，去掉具名归属。**

审稿意见指出部分具名归属无法核实。本轮的处理**不是**删掉技术内容，而是：
1. 把 "Xxx et al.~\citep{fake}" 改成无主语的被动/陈述句
2. 尽可能补挂一个**可核实的真实文献**（本轮主要用 `wang2024mtsisurvey` /
   `richter2024survey` / `rossi2020temporal` / `lobench2025` / `frino2018macroeconomic`）
3. 技术论断本身（小波域对抗学习、蒸馏加速、diagonal-masked attention 等）**全部保留**

---

## 5. 3 条新增条目（替换虚构引用）

| key | 文献 | DOI | 用途 |
|---|---|---|---|
| `wang2024mtsisurvey` | IJCAI 2024 多模态时序综述 | `10.24963/ijcai.2024/1187` | 替换 5 处虚构具名 |
| `richter2024survey` | IEEE Access 12:148167–148189 | `10.1109/access.2024.3473540` | 替换 2 处虚构综述 |
| `frino2018macroeconomic` | J. Futures Markets 38(7):775–787 | `10.1002/fut.21908` | 补挂 look-ahead bias 论断 |

> 三条均已通过 Crossref / DOI 解析验证存在。

---

## 6. 5 个"仓库独有"key 的去向

这 5 个 key 存在于仓库但不在 WS 原点（`.bak`）中：

| key | 仓库中是否被引用 | WS 中的处置 |
|---|---|---|
| `Time-LLM` | ✅ 引用 | → `jin2024timellm`（author-year 化） |
| `aksu2024gifteval` | ✅ 引用 | → `GIFT-Eval`（保留原 key） |
| `box1970` | ✅ 引用 | → `box2015time`（更正到实际版本） |
| `qiu2024tfb` | ✅ 引用 | → `TFB`（保留原 key） |
| `WaveletGAN` | ❌ 孤儿 | 删除 |

> ⚠️ **注意方向**：`GIFT-Eval` 与 `TFB` 在 WS 里是**被保留**的原始 key，
> 而 `aksu2024gifteval` / `qiu2024tfb` 才是被删的重复项。这与直觉相反，**不是笔误**。

---

## 7. 孤儿清理的收益

| | 仓库 | WS | 变化 |
|---|---:|---:|---:|
| 孤儿条目 | **82** | **5** | **−77（−94%）** |
| 孤儿占库比 | 27.1% | 2.5% | — |

**剩下 5 条孤儿**（有意保留）：

```
jiang2025multimodaltimeseriesanalysis
style-facts
tsa1
tsa2
zhao2025timeseriesscientistgeneralpurposeaiagent
```

这 5 条只出现在 `is26_redline.bbl`（latexdiff 的删除标记里），均为**真实论文**，
保留是为了让标记稿的删除标记仍能正确渲染。参考计数恒等式：

$$204\ (\text{库内条目}) = 199\ (\text{正式稿引用}) + 5\ (\text{仅存在于删除标记})$$

---

## 8. ⚠️ 为什么必须成对替换（量化证据）

WS 正文的 `\citep{}` 已全部改用 author-year 体系。

### 场景 1：换 bib 但不换 `sections/`
仓库正文仍调用已删除的 key → **27 个 `[?]`**：
```
GIFT-EVAL, Time-LLM, aksu2024gifteval, bamford2023, box1970, cai2025, chen2023b,
du2024, gao2024, gholamrezaei2023conditioning, lozano2023dual, miao2025, nater2025,
oppel2025, qian2024, qin2025, qiu2024tfb, shan2021, shankar2025, tao2024,
wang2021bigru, wang2024c, wi2023, zhang2023imputation, zhang2024spatial,
zhang2025a, zhou2024cross
```

### 场景 2：换 `sections/` 但不换 bib
WS 正文调用 `box2015time`、`li2025mars`、`berti2025trades`、`wang2024mtsisurvey`
等仓库 bib 中不存在的 key → **同样报错**。

### ✅ 正确做法
两者作为一个原子操作同时替换。`04_合并操作命令.md` 的脚本已把 `sections/` +
`ultimate_complete.bib` 绑定为同一事务。

---

## 9. ⚠️ 关于"Crossref 相似度扫描"的警告

Phase 1 曾用 Crossref 标题相似度做批量筛查，输出了一份 **58 条 `sim < 0.72`**
的候选删除名单，**该名单不能直接使用**。原因：Crossref 检索对经典论文存在大量
**假阴性**：

| 假阳性案例 | Crossref 相似度 | 实际 |
|---|---:|---|
| `ho2020ddpm` | 0.88 | ✅ 真实（DDPM 原文） |
| `arjovsky2017wgan` | 0.91 | ✅ 真实（WGAN 原文） |
| `brown2020language` | 1.00 | ✅ 真实（GPT-3） |
| `esteban2017real` | 0.44 | ✅ 真实（RCGAN） |

> **只有经过人工逐条复核的那 22 + 若干条才是可信的删除清单。**
> 若后续有人重跑扫描脚本，**务必不要**把原始输出当作删除依据。

### arXiv 论文的可靠存在性检验

对 arXiv 论文，Crossref **经常查不到**。应改用 **DataCite**：

```
https://api.datacite.org/dois/10.48550/arXiv.<arXivID>
```

本轮用此法纠正了 8 处 arXiv ID 错配：

| key | 错误 ID | 正确 ID |
|---|---|---|
| `lobench2025` | `2412.01802` | `2505.02139` |
| `finmaster2025` | `2412.18025` | `2505.13533` |
| `tsrbench2026` | `2502.13840` | `2601.18744` |
| `tao2024` | — | 虚构，已删除 |

---

## 10. 复核命令

```bash
cd "/Volumes/FunkDisk/Study/PHD/论文发表/论文一：金融数据合成综述"

# 条目数对照
for f in SurveyOfFTSG/SurveyOfFTSG-main_clean/ultimate_complete.bib \
         SurveyOfFTSG-main0913/ultimate_complete.bib; do
  printf "%-60s %s\n" "$f" "$(grep -cE '^@' "$f")"
done

# 完整差异清单
python3 -c "
import json
d=json.load(open('SurveyOfFTSG-main0913/merge_docs/_data/bib_delta.json'))
print('删除',len(d['removed']),'新增',len(d['added']))
print('别名(孤儿)',len(d['alias']))
print('author-year',len(d['lower']))
"
```

更详细的逐条核实记录见工作区根的
`MARKOUT_unverifiable_refs.md`（679 行，§0–§12）。
