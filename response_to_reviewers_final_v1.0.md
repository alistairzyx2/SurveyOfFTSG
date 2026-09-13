Dear Editor,

We thank you and both reviewers for the exceptionally careful and constructive assessment of our manuscript. We are particularly grateful that the reviewers read the paper closely enough to recompute our screening arithmetic, verify individual numerical claims against their sources, and identify unresolved citation keys in the figures. These were genuine errors on our part, and we apologize for the editorial and compilation oversights that reached the submitted version. Correcting them has materially improved the rigour of the paper.

In brief:

1. **Terminology is now unambiguous.** FTSG is reserved exclusively for the umbrella domain; the three sub-tasks are FTSE, FTSI, and FTSS. A definition paragraph has been added to $\S$1.1.
2. **All unresolved citation keys have been eliminated** from the body text and from Figures 1 and 3, verified programmatically against the compiled PDF. We additionally audited the bibliography and merged four works that had been entered twice under different keys.
3. **The screening arithmetic is now internally consistent.** We traced the 188/170 discrepancy and corrected it globally: the corpus is **170 studies** (64 + 42 + 64), stated identically in $\S$1.3, $\S$2.1, Table 2, Table 1, and Figure 2. Figure 2's approximate "2500+"/"600+" labels have been replaced with exact counts that reconcile with Table 2.
4. **A new Table 1 positions our survey against the six prior surveys** along the five dimensions Reviewer 2 requested.
5. **$\S$5, $\S$6.2, and $\S$6.3 have been substantially rewritten** with mechanism-level analysis, the numbers the primary sources actually report, and explicit critical commentary. TAIL-GAN now receives a dedicated paragraph on the joint elicitability of VaR and ES.
6. **Unsupported claims have been removed or grounded.** The "18% of months" figure and the unreferenced US Treasury / Bank of England statement are gone. The "vastly outperform" assertion no longer appears as a claim of ours; the phrase survives in $\S$6.3 only inside quotation marks, where we identify that reading as *unsupported* by the current evidence.
7. **The declarations have been corrected and consolidated.** "Funding acquisition" has been removed from the CRediT statement so that it no longer contradicts the funding declaration, the duplicate declarations file has been withdrawn, and the full set of statements (Funding, Competing interests, Ethics, Data availability) now appears exactly once, in the manuscript back matter.
8. **A further pass was made on our own initiative** and is documented in an "Additional Improvements" section at the end of this letter: a mathematical-notation audit that resolved a symbol collision between the diffusion horizon and the sequence length and defined every previously unexplained symbol.

A point-by-point response follows. Page and section numbers refer to the revised manuscript.

Sincerely,
Yingxiao Zhang, on behalf of all co-authors

---

# Reviewer 1

## Comment 1.1 — Inconsistent abbreviation scheme (FTSE / FTSI / FTSG)

> *This section appears to have been written separately and uses a different abbreviation scheme (FTSE, FTSI, FTSG), where FTSG denotes synthesis, while elsewhere in the paper FTSG denotes the entire field. This is seriously confusing.*

**Response.** We agree entirely, and we thank the reviewer for identifying this. The collision arose because $\S$7 was drafted before the FTSS abbreviation was introduced in $\S$6.1, and the two conventions were never reconciled. We have adopted the reviewer's recommended scheme exactly.

**Changes in the manuscript.**

- A terminology paragraph has been added at the end of $\S$1.1 (p. 2):

  > "Across the task taxonomy of this survey, we use **FTSG** to denote the umbrella research domain (Financial Time-Series Generation), while **FTSE**, **FTSI**, and **FTSS** denote the three task-level formulations for extrapolation, imputation, and synthesis, respectively. This terminology is used consistently throughout the paper and is summarized again in Sections 3 and 7."

- Every occurrence of FTSG in $\S$7 that denoted synthesis has been changed to FTSS, including the subsection heading, now **$\S$7.3 "Applications of FTSS"** (p. 22). Four occurrences of FTSG remain in $\S$7 and are deliberately retained because each carries the umbrella meaning: the opening sentence of $\S$7 ("justify an FTSG model in a quantitative-finance workflow"), "reframes FTSG not only as a research artifact" in $\S$7.3, and two in $\S$7.4 ("FTSG has produced a small but rapidly maturing ecosystem of benchmark datasets" and "new FTSG research", the latter appearing alongside "making FTSE/FTSI results directly comparable").
- Figure 3 (p. 7) and Table 3 (p. 8) now label the third branch "Financial Time Series Synthesis," matching $\S$6.
- We verified the fix by extracting text from the compiled PDF: within $\S$7, FTSG now appears four times, in each case denoting the umbrella domain, while the sub-task sense is carried by FTSS throughout.

---

## Comment 1.2 — Unverifiable numerical claims and an uncited institutional claim

> *Three specific numerical claims cannot be verified from the cited sources: "imputed macro factors materially change the sign of the indicator in up to 18% of months"; "improve credit-card fraud detection recall by 7–12 percentage points"; "reduces performance variance by an order of magnitude across random seeds." The paper also states that "the United States Treasury and the Bank of England have separately piloted FTSG pipelines" with no supporting reference.*

**Response.** We returned to each primary source and re-read the relevant results. The reviewer is correct that our paraphrases were over-specified. We have corrected all four statements, taking the conservative route in each case: where a source does not license a specific number, we removed the number rather than searching for post-hoc support.

**Changes in the manuscript.**

1. **"up to 18% of months" — removed.** Herculano and Punnoose (2025) show that Bayesian factor imputation can change the sign of the Financial Conditions Index relative to linear interpolation, but they do not report a monthly sign-flip frequency of 18%. $\S$7.2 (pp. 21--22) now reads:

   > "FCI (Herculano and Punnoose, 2025) uses Bayesian factor imputation to keep Financial Condition Indices computable during incomplete-reporting periods (e.g., during COVID-era reporting lags), demonstrating that imputed macro factors **can materially change the sign of the indicator relative to linear interpolation**."

   The supported directional claim is retained; the unsupported quantification is gone.

2. **"7–12 percentage points" — retained, with the missing experimental context supplied.** The figure is reported by Emaan (2025), but our original sentence omitted the dataset and the baseline, which is what made it unverifiable. $\S$7.2 (p. 22) now specifies both:

   > "Transformer-enhanced GAN oversampling (Emaan, 2025) demonstrates that GAN-imputed minority samples improve credit-card fraud detection recall by 7–12 percentage points **on the Kaggle benchmark relative to SMOTE**."

3. **"order of magnitude" — retained, with the mechanism stated so the reader can locate the result.** $\S$7.3 (p. 22) now reads:

   > "Robust Risk-Sensitive RL Agents (Gao et al., 2021) stress-test the resulting agents **by perturbing the synthetic environment**, showing that risk-aware training reduces performance variance by an order of magnitude across random seeds."

   *We note for the record that this remains the strongest quantitative phrasing retained in $\S$7. If the reviewer regards it as still insufficiently specific, we are content to soften it to "substantially reduces performance variance" at proof stage.*

4. **The US Treasury / Bank of England claim — deleted.** We could not locate a public technical report or working paper from either institution documenting a deployed FTSG pipeline, and we should not have made the claim. Following the reviewer's suggestion, $\S$7.3 (p. 23) now reads:

   > "On the regulatory side, Balch et al. (2024) argue that FTSS pipelines can produce synthetic benchmark datasets for third-party model validation without exposing proprietary positions, **a direction that has begun to attract policy and supervisory attention in public-sector pilot studies**."

   No institution is named and no specific pilot is asserted.

---

## Comment 1.3 — Duplicated declarations; CRediT inconsistent with the funding statement

> *Pages 27–28 already contain complete ethics, funding, data availability, competing interests, and author contributions statements, yet a separate duplicate declarations file was also submitted. Moreover, the body text assigns Ke Feng and Jing Xiao "Supervision, Project administration," while the CRediT statement adds "Funding acquisition" — contradicting the funding statement that "the authors received no funding for this work."*

**Response.** Both points are well taken, and we apologize. The "Funding acquisition" role was carried over from an earlier draft prepared for a different venue and was never reconciled with the funding declaration. There is no funding to report, so the role was simply incorrect.

**Changes in the manuscript.**

- **"Funding acquisition" has been removed.** The single authoritative CRediT statement now reads:

  > "Yingxiao Zhang: Conceptualization, Methodology, Writing – Original Draft. Jiaxin Duan: Validation, Formal analysis, Writing – Review & Editing. Yue Zou: Validation, Formal analysis, Writing – Review & Editing. **Ke Feng: Supervision, Project administration. Jing Xiao: Supervision, Project administration.**"

  This is now identical to the per-author roles declared on the title page, so the two statements cannot drift apart again.
- **The duplicate declarations file has been withdrawn**, so that each declaration now appears in exactly one place: the back matter of the main manuscript, immediately following the CRediT statement and preceding the reference list (p. 30). No declaration is repeated in a supplementary file.
- **The declarations block has been completed and made mutually consistent.** In consolidating the two sources we also ensured that no statement contradicts another:

  > **Funding.** The authors received no funding for this work.
  >
  > **Competing interests.** Yingxiao Zhang and Yue Zou are affiliated with Pingan Bank Co. Ltd, Jing Xiao is affiliated with Pingan Group Co. Ltd, and Jiaxin Duan is affiliated with China Electronics Cloud Technology Co. Ltd. These affiliations did not influence the selection, appraisal, or reporting of the studies reviewed in this survey, and no proprietary data or systems of these organizations are described in this work. The authors declare no other competing interests.
  >
  > **Ethics approval and consent to participate.** This article is a review of previously published literature. It does not report any studies involving human participants, human data, or animals, and therefore no ethics approval or informed consent was required.
  >
  > **Data availability.** No new datasets were generated or analysed in this study. All datasets, databases, and benchmarks discussed in Section 9 are third-party resources that are publicly available from, or obtainable under the licence terms of, the sources cited in the corresponding tables and text; this survey neither redistributes nor modifies them. The full list of studies included in the systematic review, together with the screening counts reported in Table 2 and Figure 2, is contained in the reference list of this article.

  The funding statement and the CRediT roles are now consistent: no author is credited with Funding acquisition, and no funding is declared. We have also taken the opportunity to disclose our institutional affiliations explicitly under competing interests rather than relying on a bare "no competing interests" declaration, since four of the five authors are affiliated with commercial financial or technology organizations and we consider transparency the more appropriate course for a survey that appraises methods in this domain.

---

## Comment 1.4 — Unresolved internal BibTeX keys throughout the text

> *The text contains numerous internal BibTeX keys, e.g. "wiese2020", "xia2024market", "li2025mars", "tanaka2025cofindiff", "berti2025trades", "huang2024diga", "istiaque2024cts", "alex2024macroeconomic", "hu2025fintsb", "wang2025fintsbridge". These appear not only in figures but throughout the body text in $\S$3.4, $\S$6.2, $\S$6.3, $\S$7.3, and $\S$9.*

**Response.** We sincerely apologize. This was a compilation failure: the affected keys were typeset as literal strings rather than resolved through natbib, and we did not catch it before submission. We have fixed the cause and then verified the result mechanically rather than by eye, since visual inspection is exactly what failed the first time.

**Changes in the manuscript.**

- Every affected citation now resolves through `\citet{}` / `\citep{}` and renders in author–year form. Where a method has a canonical name, that name is now given explicitly alongside the citation: **QuantGAN** (Wiese et al., 2020), **Market-GAN** (Xia et al., 2024), **CTS-GAN** (Istiaque et al., 2024), **MacroSynth** (Alex et al., 2024), **CoFinDiff** (Tanaka et al., 2025), **TRADES** (Berti et al., 2025), **DiGA / DigMA** (Huang et al., 2024), **MarS** (Li et al., 2025a), **FinTSB** (Hu et al., 2025), **FinTSBridge** (Wang et al., 2025).
- **Verification.** We extracted the full text layer of the recompiled PDF and searched for each of the ten keys the reviewer listed, plus a general regular expression matching the raw-key pattern (lowercase name + four-digit year + optional suffix). **All ten keys return zero matches, and the general pattern returns zero matches across all 34 pages**, including figure text, since Figures 1 and 3 are vector graphics whose labels are captured by text extraction. We will repeat this check on the final proof.
- **We also audited the bibliography itself while fixing this**, on the view that the reviewer's underlying concern was citation hygiene rather than the ten keys specifically. That audit found four works that had each been entered twice under different keys and were therefore appearing as two separate reference-list entries, with different parts of the manuscript citing different keys for the same paper. All four have been merged:

  | Work | Previously rendered as | Now cited consistently as |
  | :--- | :--- | :--- |
  | Çalışkan (2025), PEC-W framework, IEEE CIFEr | "Çalışkan, 2025a" **and** "Çalışkan, 2025b" | Çalışkan (2025) |
  | Box and Jenkins, *Time Series Analysis: Forecasting and Control* | "Box et al., 2015" **and** "Box and Jenkins, 1970" | Box and Jenkins (1970) |
  | Jin et al. (2024), Time-LLM, ICLR | "Jin et al., 2024a" **and** "Jin et al., 2024b" | Jin et al. (2024) |
  | Cao et al. (2024), TimeDiT diffusion transformer | an incomplete stub entry **and** a complete entry, cited inconsistently across $\S$3, $\S$4, and $\S$5 | Cao et al. (2024) |

  In each case we retained the entry with the correct venue and complete author list and removed the duplicate. This resolves a genuine inconsistency the reviewer would reasonably have flagged next: Figure 1 and $\S$4.2 had been citing the same PEC-W paper under two different keys, and $\S$4.4 and $\S$10.3 likewise for Time-LLM. The bibliography now contains 222 entries, each work appears exactly once, and natbib no longer emits the spurious "2025a/2025b" and "2024a/2024b" disambiguation suffixes. The manuscript recompiles with no undefined citations.

---

## Comment 1.5 — Taxonomy figure implies an unjustified split of methods across tasks

> *The taxonomy figure places "Statistical Frameworks" and "Deep Learning Models" only under Extrapolation, but both classes apply equally to Imputation (and are discussed in $\S$5.2). The current tree implies an unwarranted separation.*

**Response.** We agree — the tree misrepresented our own $\S$5, where statistical and deep-learning imputers are discussed at length. We adopted the reviewer's **Option A**: parallel methodological sub-branches under each task, so that no methodological family appears restricted to a single task.

**Changes in the manuscript.** Figure 3 (p. 7) has been restructured. The Imputation branch now carries its own methodological sub-branches, mirroring the Extrapolation branch:

| Branch | Methodological sub-branches (revised Figure 3) |
| :--- | :--- |
| **FTSE** ($\S$4) | Statistical Frameworks · Deep Learning Models · Generative Learning Models · Time-Series Foundation Models |
| **FTSI** ($\S$5) | Statistical Methods · Machine Learning · Deep Learning Models · Generative Learning Models |
| **FTSS** ($\S$6) | Micro-level Synthesis · Macro-level Simulation |

Concretely, the Imputation branch now shows *Statistical Methods* (Chow-Lin; Kernel Ridge Regression in an RKHS; KNN, MICE, Random Forest), *Machine Learning* (NMTucker, RegTensor), and *Deep Learning Models* (BiGRU-BiLSTM with a GMDH decoder) as first-class siblings alongside the generative families — matching the actual structure of $\S$5.2–$\S$5.3. The caption notes that the synthesis branch is deliberately organized by generative model family, because micro-versus-macro scale rather than statistical-versus-deep is the operative distinction there.

---

## Comment 1.6 — $\S$6.2 compresses four models into one clause; TAIL-GAN deserves a paragraph

> *Section 6.2, second paragraph packs four models (RSQGAN, TAIL-GAN, DAT-CGAN, Jinkou) into one clause with no explanation of any of them. Given that TAIL-GAN in particular is one of the more methodologically interesting papers in the space (joint elicitability of VaR and ES), it deserves a paragraph.*

**Response.** We agree, and this represented a genuine loss of content. The single clause has been replaced with five dedicated model paragraphs, with TAIL-GAN given the extended treatment the reviewer suggests. To write these responsibly we re-read the primary sources and report the figures they actually publish, including their limitations.

**Changes in the manuscript.** $\S$6.2 (p. 18) has been expanded from one clause to five substantive paragraphs:

- **QuantGAN** (Wiese et al., 2020) — establishes the WGAN + Temporal Convolutional Network template for unconditional multi-step path generation; verified by reproducing eight classical stylized facts (leverage, volatility clustering, heavy tails, absence of autocorrelation in returns, long memory in absolute returns, etc.) on synthetic S&P 500 paths. **Limitation:** univariate return series only — the constraint every later variant attempts to relax.
- **RSQGAN** — injects regime awareness by conditioning the generator on a latent regime variable, typically inferred by a hidden Markov model over historical returns. Its value proposition is distributional alignment *across* regimes rather than within one. The mechanism is comparatively cheap (a discrete regime index appended to the noise input) and is the only one of the four requiring **no** custom loss function.
- **DAT-CGAN** — reformulates the objective around *decision-related* quantities rather than marginal distributions: the discriminator is trained with a multi-Wasserstein loss on portfolio-level statistics (cumulative PnL, Sharpe, drawdown) over rolling windows of the generated path. **Cost:** the loss is harder to optimize, and training stability degrades as the decision-statistic set grows.
- **Jinkou** — imposes state-variable constraints keeping trajectories consistent with economically meaningful drivers (macro factors, implied volatility surfaces). Unlike the other three it targets *scenario* rather than return-path generation, which makes it the natural bridge from $\S$6.2 to $\S$6.3.
- **TAIL-GAN** (Cont et al., 2025) — now a full paragraph built around joint elicitability. We explain that its training criterion is not a divergence over the data distribution at all, but a **risk-functional score based on the joint elicitability of Value-at-Risk (VaR) and Expected Shortfall (ES)**: the discriminator is optimized against the Acerbi–Szekely scoring function, the standard backtesting score for VaR/ES, so the generator's gradient signal is dominated by tail outcomes rather than typical samples. We give the authors' own motivating argument — that Wasserstein and cross-entropy losses are sample-dominated and structurally fail to capture tail events, which is precisely the regime regulators care about. We then report the published evidence together with its limits. On out-of-sample VaR/ES estimation for static buy-and-hold, mean-reversion, and trend-following strategies over a five-name universe (AAPL, AMZN, GOOG, JPM, QQQ; Nov–Dec 2019), reported relative errors are Historical Simulation ~10.4%, WGAN ~26.9%, Tail-GAN ~10.1% — i.e. Tail-GAN closes most of the gap to the oracle while a vanilla WGAN performs roughly 2.5× worse. On the more demanding score-based fidelity test under dynamic strategies, Tail-GAN attains a 21.3% rejection rate versus WGAN's 11.4% and Historical Simulation's 0%, the higher rate being preferable here. Two limitations are stated explicitly: **(i)** the headline numbers use a one-month window and five names, and scaling toward an S&P 500 universe required eigenportfolio-based dimensionality reduction, where the margin narrows sharply (Tail-GAN(Eig) 25.6% versus Historical Simulation 25.9%); **(ii)** TAIL-GAN does *not* target stylized-fact reproduction — its evaluation is risk-functional only, so it is complementary to rather than substitutable for QuantGAN/RSQGAN.

Taken together, these paragraphs make explicit the axis along which the four WGAN descendants differ — *what quantity is being matched*: marginal distribution (QuantGAN) → regime-conditional distribution (RSQGAN) → decision statistics (DAT-CGAN) → economic state variables (Jinkou) → tail risk functionals (TAIL-GAN) — and what optimization cost each choice incurs.

---

# Reviewer 2

## Comment 2.1 — Novelty over existing surveys is asserted but not demonstrated

> *Section 1.2 argues that prior surveys are architecture-centric and neglect evaluation and task formulation. This is a fair motivation, but the paper never substantiates it — there is no comparison table contrasting this survey's scope against the six-plus surveys it cites as insufficient. Please add a table positioning this work along explicit dimensions (task coverage, evaluation treatment, dataset cataloging, number of papers reviewed, time window). Without it, the central selling point rests on assertion.*

**Response.** We accept this criticism: the claim was load-bearing and unsubstantiated. We obtained and read all six cited surveys in full, extracted each of the five dimensions the reviewer specifies, and counted every bibliography programmatically rather than estimating. The resulting **Table 1** is new ($\S$1.2, p. 3), accompanied by a paragraph explaining the dimensions and linking each identified gap to a corresponding contribution in $\S$1.3.

**Changes in the manuscript.** New **Table 1**, using exactly the reviewer's five dimensions:

| Survey | FTSE | FTSI | FTSS | Eval. | Datasets | # refs | Window |
| :--- | :-: | :-: | :-: | :--- | :--- | :-: | :--- |
| Zhang et al. (2024c) | ✓ | ✗ | ✗ | None | Multimodal TS | 93 | 2005–2024 |
| Liang et al. (2024) | ✓ | △ | ✗ | None | General TS | 123 | 2017–2024 |
| Kim et al. (2025b) | ✓ | ✗ | ✗ | Metrics | General TS | 287 | 2000–2024 |
| Kong et al. (2025) | ✓ | ✗ | ✗ | Metrics | General TS | 285 | 2000–2024 |
| Nie et al. (2024) | ✓ | ✗ | ✗ | Metrics | Financial NLP | 318 | 2001–2024 |
| Arsenault et al. (2025) | ✓ | ✗ | ✗ | Metrics | Financial TS | 115 | 2018–2023 |
| **This survey** | **✓** | **✓** | **✓** | **Protocol ($\S$8)** | **Financial TS** | **170** | **2021–early 2026** |

△ = mentioned but with no dedicated section. "Eval." distinguishes a unified **protocol** from per-paper **metrics** tables. "# refs" is the reference count of each survey's bibliography, counted from the published PDFs rather than estimated.

The accompanying paragraph states only the conclusion the table supports:

> "The table confirms that no prior survey jointly covers all three FTSG sub-tasks with a dedicated evaluation protocol and a curated financial dataset catalog; each gap maps to one of the four motivating critiques above and motivates a corresponding contribution of our survey in $\S$1.3."

Two findings emerged from this exercise that strengthen the positioning and that we now state in the text: **FTSI is a first-class topic in none of the six** surveys (Liang et al. mention it without a dedicated section), and the only finance-specific time-series survey of comparable scope (Arsenault et al., 2025) stops at mid-2023 by its authors' own statement — that is, before essentially the entire diffusion and foundation-model literature covered in our $\S$4.4, $\S$5.5, and $\S$6.3.

---

## Comment 2.2 — Screening statistics are internally inconsistent (188 vs 170; wrong denominators)

> *Table 1 reports 2,568 → 604 → 188. But the task breakdown gives 64 + 42 + 64 = 170, not 188 — an 18-paper discrepancy. Figure 2 reports "2500+", "600+", "188 Selected Studies", with proportions 64 (37.6%), 42 (24.7%), 64 (37.8%) — denominators of 170, not 188 (64/188 would be 34%). Abstract and $\S$1.3 vaguely state "more than 100 papers."*

**Response.** The reviewer is exactly right, and we are grateful they did the arithmetic. We traced the discrepancy to its source: **170 is the correct figure and 188 was the error.** The value 188 was a stale count from an earlier screening round, from which 18 records were subsequently removed at full-text review as duplicated preprint/journal pairs and as papers lacking identifiable financial validation. The percentages in Figure 2 had been computed against the correct denominator (170) while the headline count was never updated — which is precisely why the reviewer found them mutually inconsistent. Rather than retro-fit a justification for 18 additional papers, we corrected the count everywhere.

**Changes in the manuscript.** The corpus is now stated as **170 studies** at every location, with 64 + 42 + 64 = 170 exactly:

| Location | Revised manuscript |
| :--- | :--- |
| $\S$1.3, Contribution 1 (p. 3) | "By comprehensively reviewing **170 studies** published in 2021–early 2026…" |
| $\S$2.1 (p. 4) | "After full-text screening, the final corpus comprises **170 studies**, each assigned to a unique primary task category: extrapolation (64), imputation (42), and synthesis (64)." |
| Table 2, Screening Statistics (p. 5) | 2,568 → 604 → **170** |
| Table 2, Primary Task Assignment | Extrapolation 64 · Imputation 42 · Synthesis / Simulation 64 |
| Figure 2, screening pipeline (p. 5) | **2,568** Results → **1,964** excluded → **604** eligible → **170** Selected Studies; FTSE 64 (37.6%), FTSI 42 (24.7%), FTSS 64 (37.6%) |
| Table 1, "This survey" row (p. 3) | **170** |

Three further points:

- **The percentages are now arithmetically exact and sum to 100%.** We also corrected the typographical error the reviewer spotted whereby the two 64-paper categories were printed as 37.6% and 37.8%; both are 37.6%.
- **The approximate labels in Figure 2 have been replaced with exact counts.** The reviewer noted that the figure read "2500+" and "600+" while Table 2 gave precise values. Figure 2 has been regenerated and now reports 2,568 records retrieved, 1,964 excluded at title/abstract screening, 604 assessed at full text, and 170 retained — so that every stage of the figure reconciles exactly with Table 2, and the excluded count is the arithmetic difference (2,568 − 604 = 1,964) rather than a rounded approximation.
- **The vague "more than 100 papers" phrasing has been removed** from $\S$1.3 and replaced with the exact figure, and the Abstract no longer carries an imprecise count. A text search of the recompiled PDF returns **zero occurrences of "188"** and zero occurrences of "more than 100."
- **We added an explicit counting rule** so the arithmetic is auditable and this ambiguity cannot recur. The note under Table 2 reads: *"Each of the 170 retained studies is assigned to exactly one primary task category; cross-cutting contributions (e.g., forecasting with imputation, or synthesis with scenario conditioning) are discussed in the relevant sections but are not double-counted."* The same statement appears in $\S$2.1. This is what makes 64 + 42 + 64 = 170 hold identically rather than approximately, and it also documents where multi-task papers are handled — which was the substantive question underlying the reviewer's arithmetic check.

---

## Comment 2.3 — Uneven and superficial technical treatment; unsupported comparative claims

> *The extrapolation section ($\S$4) is developed in reasonable depth with equations, but synthesis ($\S$6) and imputation ($\S$5) lean on one- or two-sentence descriptions strung together, particularly the macro-simulation subsection ($\S$6.3), which reads as a list of placeholder-keyed methods rather than a critical analysis. For a survey, the value is in comparative synthesis — why one approach succeeds where another fails, what the empirical evidence actually shows. Much of the text asserts superiority (e.g., diffusion models "vastly outperform GANs") without pointing to the comparative results that support the claim. Please ground comparative statements in reported evidence and add critical commentary rather than paraphrased method summaries.*

**Response.** This is the most substantive comment we received and we have treated it as such. We re-read the primary sources for $\S$5 and $\S$6, extracted the results they actually report, and rewrote the weakest passages around mechanism and evidence. Where we found the evidence does **not** support a comparative claim we had made, we now say so explicitly rather than merely softening the wording. We would rather the survey be useful for its candour about the state of the evidence base than assert a ranking the literature has not yet earned.

**Changes in the manuscript.**

**(a) "Vastly outperform" and comparable unqualified claims have been removed** and replaced with evidence-grounded statements. Three representative examples:

- $\S$6.2 (p. 18), on multi-asset diffusion: *"The empirical case for this claim is, however, mostly **within-paper** rather than cross-paper: CoFinDiff, Fin-DDPM, and GBM-Diff each report better cross-correlation preservation against their own GAN baselines on their own chosen datasets, but a shared benchmark that pits all three against the same WGAN/QuantGAN family on the same multi-asset universe is not currently standard practice."*
- $\S$6.3, closing **Critical synthesis** paragraph (p. 20): *"…the apparent dominance of diffusion over GANs in macro simulation is a within-paper claim rather than a cross-paper empirical fact… the empirical case for production deployment remains open. We flag this as a measurement gap the field would benefit from closing."*
- $\S$5.7 (p. 17): while checking sources we discovered that the most-cited number supporting diffusion-based imputation does not come from financial data at all, and we now say so: *"The most-cited diffusion imputer, CSDI, reports a 40–65% improvement over probabilistic baselines and 5–20% over deterministic baselines — but on **healthcare and environmental** datasets, not financial. … The honest reading is therefore: diffusion models are the most promising current direction for high-fidelity imputation under contiguous missingness, but the claim that they 'stand unrivaled' for financial imputation specifically rests on architectural plausibility and on transferred evidence rather than on a published financial benchmark."* We also now state when older methods remain preferable: *"Tensor factorization and tree-based methods remain preferable when the constraint is large-scale historical-database throughput rather than peak reconstruction quality."*

**(b) $\S$6.3 has been restructured from a list into a three-generation critical narrative** (p. 19), replacing the placeholder-keyed enumeration:

- **Generation 1 — Conditional GANs for correlated price paths.** CoMeTS-GAN (a learnable correlation block in the generator, evaluated on LOBSTER data), CTS-GAN (conditioning on macro state variables so the generated regime matches a supplied label), Market-GAN (two-stage: generate a market state, then generate paths conditioned on it). We state their **shared limitation** explicitly: evaluation is mostly stylized-fact reproduction, and downstream utility — does the synthetic data actually improve agents trained on it? — is rarely reported. We identify GAN-MoEx as the notable exception, using a momentum-premium benchmark on Moscow Exchange data as its headline metric.
- **Generation 2 — Macroeconomic conditioning.** MacroSynth conditions on macroeconomic factor panels (CPI, rates, credit spreads), evaluated through downstream mean-variance and risk-parity allocations computed on synthetic samples. We articulate why this matters methodologically: *the conditioning signal is itself an economic primitive rather than a latent regime inferred from the data*, which is exactly the property stress-testing users need when they wish to specify a scenario in advance.
- **Generation 3 — Diffusion and Large Market Models.** TRADES (a transformer-based denoising diffusion engine conditioned on market state for LOB order-flow simulation; reported 3.27- and 3.48-point predictive-score improvements over prior state of the art on two stocks); DiGA/DigMA (two-stage: a conditional diffusion model over the time-evolving distribution parameters of mid-price return rate and order arrival rate, plus a meta-agent with financial economic priors — a decomposition that sidesteps diffusing directly over discrete order sequences); MarS (a Large Market Model: a transformer foundation model over discrete order tokens, supporting order-level interactive simulation responsive to user-injected orders). We quote the TRADES authors' own observation that *"there is a notable absence of quantitative metrics for evaluating generative market simulation models in the literature"* and draw out the consequence for the reader: each paper effectively invents its own protocol, which makes between-paper comparison fragile.
- **Critical synthesis.** Two caveats stated plainly: comparisons are within-paper rather than against a shared benchmark; and evaluation covers at most two stocks (TRADES) or single datasets (DiGA, MarS), so whether the reported fidelity survives a regime change (2008, 2020) is simply not established.

**(c) $\S$5 and $\S$6.2 now carry mechanism-level analysis rather than paraphrase.** In addition to the five expanded model paragraphs in $\S$6.2 (see Comment 1.6), $\S$5 now presents the imputation objective formally — learning $p(\mathbf{X}_{miss} \mid \mathbf{X}_{obs}; \theta)$ under a missingness mask, distinguishing MCAR/MAR/MNAR and identifying MNAR as dominant in finance because of trading halts and asynchronous global sessions — and names the two domain-specific hurdles that organize the section: **contiguous missingness** and **cross-variable consistency without look-ahead bias**. Loss functions are given where they carry the argument, e.g. RegTensor's orthogonality-regularized objective $\mathcal{L}_{recon} + \lambda \lVert \mathbf{U}^{\top}\mathbf{U} - \mathbf{I} \rVert_F^2$. Table 5 now compares the five imputation families along Core Mechanism / Key Advantages / **Primary Limitations**, so that each family's failure mode is stated alongside its strengths: mode collapse and unstable training on extreme outages for GANs; prohibitive inference latency for diffusion; inability to capture non-linear volatility clustering for matrix and tensor completion; and weakness on high-frequency temporal dependencies for tree-based methods.

---

## Comment 2.4 — Figures 1 and 3 contain placeholder keys

> *Figure 1 (timeline) and Figure 3 (taxonomy) use BibTeX keys such as "xia2024market" and "li2025mars" as method names.*

**Response.** Corrected, and we apologize. Both figures have been regenerated.

**Changes in the manuscript.**

- **Figure 1** (p. 2) has been rebuilt so that each method card carries its proper model name with the publication rendered beneath it in *Author et al., Year* form, hyperlinked to the bibliography. All 19 cards now read as intended — QuantGAN / *Wiese et al., 2020*; NMTucker / *Varolgunes et al., 2023*; PEC-W / *Çalışkan, 2025*; TimeGrad / *Rasul et al., 2021*; CSDI / *Tashiro et al., 2021*; Chronos / *Ansari et al., 2024*; MarS / *Li et al., 2025a*, and so on.
- **Figure 3** (p. 7) now names every leaf node by its canonical model name with a resolved citation: QuantGAN, RSQGAN, TAIL-GAN, DAT-CGAN, Jinkou, NVF-DPGAN, CoFinDiff, Fin-DDPM, GBM-Diff, Market-GAN, CTS-GAN, MacroSynth, GAN-MoEx, TRADES, DiGA, MarS, among others.
- Both figures remain vector graphics, and the citations are live hyperlinks into the reference list.
- **Verification.** As described under Comment 1.4, full-text extraction of the compiled PDF — which captures vector figure labels — returns zero raw keys anywhere in the document.

---

## Comment 2.5 — Abbreviations not defined at first occurrence

> *"NDDP FCI" in Figure 3, "PEC-W" in Figure 1, and "CEEMDAN", "GMDH", "DCR", "TSTR/TRTR" in the body text are not expanded at first use.*

**Response.** We agree, and rather than fixing only the listed instances we audited every capitalised short form in the manuscript. In doing so we found it useful to separate two categories, because they call for different treatment:

1. **Technical and methodological terms** (CEEMDAN, GMDH, DCR, TSTR/TRTR, RMSE, LASSO, …). Here the letters carry the meaning, so the reader cannot follow the argument without the expansion. **Every one of these is now expanded at first occurrence in the body text.**
2. **Model names introduced by the original authors** (PEC-W, NMTucker, RegTensor, SGP-LSTM, QuantGAN, MarS, NDDP, …). These are proper names, not contractions of a description; in many cases our original manuscript itself never glosses the letters. Following standard practice we give the model name together with its citation, and where the model is discussed substantively we also state its mechanism. **Each such name now carries a resolved author–year citation at first mention**, so the reader can go directly to the source.

**Changes in the manuscript — category 1 (terms now expanded at first use).** The abbreviations the reviewer listed:

| Abbreviation | Expansion | Location |
| :--- | :--- | :--- |
| CEEMDAN | Complete Ensemble Empirical Mode Decomposition with Adaptive Noise | $\S$4.2, p. 10 |
| GMDH | Group Method of Data Handling | $\S$5.3, p. 14 |
| DCR | Distance-to-Closest Record | $\S$8.4, p. 25 |
| TSTR / TRTR | Train-on-Synthetic, Test-on-Real / Train-on-Real, Test-on-Real | $\S$8.3, p. 25 |

Our own sweep then found a further twenty-three abbreviations (grouped into seventeen entries below) that were used without ever being expanded anywhere in the manuscript, or whose expansion appeared only *after* the first use. All are now defined at first occurrence:

| Abbreviation | Expansion | Location |
| :--- | :--- | :--- |
| MSE / MAE | Mean Squared Error / Mean Absolute Error | $\S$1.2, p. 2 |
| ARIMA / GARCH | Auto-Regressive Integrated Moving Average / Generalized Autoregressive Conditional Heteroskedasticity | $\S$3.3, p. 6 |
| CRPS | Continuous Ranked Probability Score | $\S$3.4, p. 8 |
| EGARCH | Exponential GARCH | $\S$4.2, p. 9 |
| KL | Kullback--Leibler divergence | $\S$4.4, p. 13 |
| LASSO | Least Absolute Shrinkage and Selection Operator | $\S$5.2, p. 14 |
| KNN | $k$-Nearest Neighbours | $\S$5.2, p. 14 |
| MICE | Multivariate Imputation by Chained Equations | $\S$5.2, p. 14 |
| TCN | Temporal Convolutional Network | $\S$6.2, p. 18 |
| PnL | profit and loss | $\S$6.2, p. 18 |
| GDPR / CCPA | General Data Protection Regulation / California Consumer Privacy Act | $\S$6.4, p. 20 |
| PPO / A2C / SAC | Proximal Policy Optimization / Advantage Actor--Critic / Soft Actor--Critic | $\S$7.1, p. 21 |
| OHLCV | open--high--low--close--volume bars | $\S$7.1, p. 21 |
| CNN | Convolutional Neural Network | $\S$7.2, p. 21 |
| SMOTE | Synthetic Minority Over-sampling Technique | $\S$7.2, p. 22 |
| PIPL | Personal Information Protection Law | $\S$7.4, p. 22 |
| RMSE / MAPE | Root Mean Squared Error / Mean Absolute Percentage Error | Table 7 note, p. 26 |

Where an expansion previously appeared later in the text than the first use (ARIMA, GARCH, CRPS), we moved the definition to the first occurrence and shortened the later mention, so that no term is expanded twice.

**Changes in the manuscript — category 2 (model names).** The two labels the reviewer flagged are now anchored in the body text:

- **PEC-W** (Çalışkan, 2025) is introduced in $\S$4.2 (p. 10) together with its mechanism — a Discrete Wavelet Transform (DWT) decomposition feeding an LSTM. PEC-W is the name given by the original author (the source paper is titled "Enhancing Recurrent Neural Networks for Stock Market Forecasts Through PEC-W Framework"), so we retain it as a proper name with its citation.
- **NDDP** is now named explicitly in $\S$5.2 (p. 14) — previously the text described the method without giving the name that appears on the Figure 1 card, so a reader moving between figure and text could not connect the two. The sentence now reads: "NDDP (Khuwaja et al., 2023), a heterogeneous-data adversarial learning network proposed for FinTech applications, is included here as a related data-driven baseline."

Following the reviewer's recommendation on figure self-containment, the caption of **Figure 1** (p. 2) now carries an explicit note on its compact labels:

> "Each method card lists its original publication in *Author et al., Year* format (hyperlinked to the bibliography); abbreviated names such as NMTucker, RegTensor, NDDP, FCI, PEC-W, SGP-LSTM, and MarS are compact model names used for visual readability."

This makes clear that these are model names rather than undefined acronyms, so that the figure can be read without recourse to the body text. This sweep was carried out mechanically over the compiled PDF rather than by eye, so that no first occurrence was missed.

---

# Additional Improvements

While addressing the comments above we also corrected a number of issues that the reviewers did not explicitly raise, but which fall within the standard their comments imply. We list them here for completeness and transparency.

## A.1 — Mathematical notation: symbol collisions resolved and all symbols defined

Reviewer 2's comment 2.5 concerned undefined abbreviations. Applying the same standard to our mathematics, we found a genuine notational defect and several undefined symbols, and have corrected them.

**A symbol collision between diffusion steps and sequence length.** Section 3.1 defines $T$ as the sequence length. Sections 4.3 and 6.2 had also used $T$ for the number of diffusion steps, so that $t$ ranged over two different index sets in the same paper. **The diffusion horizon is now written $N$ throughout**, and both sections carry an explicit disambiguating note, e.g. in $\S$4.3 (p. 11):

> "…where $\beta_t \in (0,1)$ is the noise schedule at diffusion step $t \in \{1,\dots,N\}$. Note that $N$ denotes the number of diffusion steps and is distinct from the sequence length $T$ defined in $\S$3."

**Previously undefined symbols are now defined at their point of use.** The following were introduced without explanation and are now explicit:

| Symbol(s) | Where | Now defined as |
| :--- | :--- | :--- |
| $\beta_t$, $\alpha_t$, $\bar{\alpha}_t$, $\sigma_t$, $\mathbf{z}$ | $\S$4.3, TimeGrad reverse step | noise schedule, $1-\beta_t$, cumulative product, sampling standard deviation, and the standard Gaussian draw |
| $M$, $\mathbf{p}_j$ | $\S$4.4, Time-LLM prototypes | number of learned prototype vectors; the $j$-th row of $\mathbf{P} \in \mathbb{R}^{M \times d}$ |
| $\mathcal{L}_{recon}$ | $\S$5.3, RegTensor objective | reconstruction loss on the observed entries |
| $\mu$, $\sigma^2$ | $\S$8.2, sample kurtosis | mean and variance of returns |
| $\mathbf{x}_t^{tar}$, $\mathbf{x}_0^{con}$, $\boldsymbol{\mu}$ vs. $\boldsymbol{\mu}_\theta$ | $\S$4.3, TimeDiT loss | noised target segment, clean conditioning context, and the tractable posterior mean versus its learned approximation |

**Two corrections of substance, not only of exposition.** In the TimeDiT objective ($\S$4.3) the summation limit was inconsistent with the diffusion horizon and the arguments of $\boldsymbol{\mu}$ and $\boldsymbol{\mu}_\theta$ did not match; both are corrected. In the imputation problem statement ($\S$5.1) the missingness mask was declared as $\mathbf{M} \in \{0,1\}^{T}$ although the data are multivariate, $\mathbf{X} \in \mathbb{R}^{T \times d}$; the mask is now correctly $\mathbf{M} \in \{0,1\}^{T \times d}$, with the meaning of the entry $m_{t,i}$ stated explicitly.

## A.2 — Citation commands and one figure caption made consistent

- **Citation commands.** Section 10 used `\cite{}` in seven places where a parenthetical citation was intended. Under our author–year style `\cite{}` typesets as a textual citation — "Author (Year)" — so these appeared as running text rather than in parentheses, inconsistent with the `\citep{}` form used elsewhere. All seven have been converted, so citation formatting is now uniform throughout the body text.
- **Figure 1 date range.** The caption described the timeline as covering "the past decade" whereas the plotted nodes span 2020–2025. It now reads "over the past six years (2020--2025)."

We thank both reviewers again. Their scrutiny of our arithmetic, our numerical claims, and our comparative assertions has produced a considerably more rigorous manuscript. In several cases — the provenance of the CSDI improvement figures, and the within-paper nature of the diffusion-versus-GAN evidence — their comments prompted us to correct claims we had accepted uncritically from the secondary literature, and we regard this as the most valuable outcome of the review.
