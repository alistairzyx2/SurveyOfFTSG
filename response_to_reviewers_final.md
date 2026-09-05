Dear Editor,

We thank you and both reviewers for the exceptionally careful and constructive assessment of our manuscript. We are particularly grateful that the reviewers examined the screening arithmetic, checked numerical statements against their sources, and identified unresolved citation keys and ambiguities in the figures. These were genuine weaknesses in the submitted version, and we apologize for the editorial and compilation oversights. Addressing them has materially improved the rigour, traceability, and presentation of the survey.

The present letter responds only to the peer-review comments. The manuscript has subsequently been reformatted into the journal's required IRDM structure with unnumbered headings and sequential Nature-style citations. Accordingly, the reviewer quotations below retain the original section and figure references from the reviewed version, while our responses identify the relevant current heading, figure, or table.

In brief:

1. **Terminology is now unambiguous.** FTSG is reserved for the umbrella field, while FTSE, FTSI, and FTSS identify extrapolation, imputation, and synthesis, respectively.
2. **All unresolved citation keys have been eliminated.** The compiled manuscript uses sequential Nature-style numerical citations and a 130-entry bibliography generated from the source bibliography file.
3. **The screening arithmetic is internally consistent.** The final corpus is **130 studies**: 54 extrapolation, 29 imputation, and 47 synthesis studies. Table 8 and Figure 6 now report the corresponding retrieval and screening counts.
4. **Table 1 now positions this survey against six prior surveys** across task coverage, evaluation, dataset cataloguing, reference count, and publication window.
5. **The imputation and synthesis discussion has been strengthened** with mechanism-level explanation, reported empirical evidence, and explicit limitations rather than unqualified comparative claims.
6. **Unsupported claims have been removed or qualified.** The unverified 18-percent claim and the named public-institution claim have been removed; other results are attributed to their original studies and described only within their reported settings.
7. **Declarations have been consolidated and made internally consistent.** All required statements occur once in the main manuscript before References, and the author-contribution statement no longer assigns Funding acquisition while the Funding statement reports no external support.
8. **Figures and terminology have been audited.** The timeline and taxonomy graphics were regenerated with resolved model labels, and domain abbreviations are expanded or contextualized at first use.

A point-by-point response follows.

Sincerely,

Yingxiao Zhang, on behalf of all co-authors

---

# Reviewer 1

## Comment 1.1 -- Inconsistent abbreviation scheme (FTSE / FTSI / FTSG)

> *This section appears to have been written separately and uses a different abbreviation scheme (FTSE, FTSI, FTSG), where FTSG denotes synthesis, while elsewhere in the paper FTSG denotes the entire field. This is seriously confusing.*

**Response.** We agree entirely. The collision arose because different draft sections had used FTSG both as an umbrella term and as the label for synthesis. We have standardized the terminology across the revised manuscript.

**Changes in the manuscript.** In the current Results subsection, *Problem Formulation and A Two-Level Taxonomy*, Financial Time-Series Generation (FTSG) is defined as the umbrella domain. The three task-level formulations are consistently labelled Financial Time-Series Extrapolation (FTSE), Financial Time-Series Imputation (FTSI), and Financial Time-Series Synthesis (FTSS). The same usage is carried through the Applications subsection, Figure 2 (the taxonomy), Figure 3 (the task comparison), and the task-technique mapping table. FTSG is no longer used to mean synthesis alone.

---

## Comment 1.2 -- Unverifiable numerical claims and an uncited institutional claim

> *Three specific numerical claims cannot be verified from the cited sources: 'imputed macro factors materially change the sign of the indicator in up to 18% of months'; 'improve credit-card fraud detection recall by 7-12 percentage points'; 'reduces performance variance by an order of magnitude across random seeds.' The paper also states that 'the United States Treasury and the Bank of England have separately piloted FTSG pipelines' with no supporting reference.*

**Response.** We returned to the cited primary studies and agree that several of our original paraphrases were over-specific. We revised the affected passages conservatively: unsupported quantification and unsupported institutional attribution have been removed, while any retained result is tied to its original study and setting.

**Changes in the manuscript.**

1. The claim that Bayesian factor imputation changes an indicator's sign in up to 18 percent of months has been removed. The Applications subsection now states only the supportable directional conclusion from the cited Financial Conditions Index study: imputed macro factors can materially change the indicator relative to linear interpolation.
2. The specific 7-12-percentage-point fraud-recall range has been replaced by a qualified account of reported downstream recall gains for GAN-based minority-class synthesis on standard credit-card transaction benchmarks, relative to heuristic baselines such as SMOTE.
3. The order-of-magnitude variance result is retained only as the reported outcome of the cited Robust Risk-Sensitive RL study, which perturbs the synthetic environment during its stress tests; it is no longer presented as a general claim about FTSG methods.
4. The named United States Treasury and Bank of England assertion has been deleted. The revised text refers only to the cited literature's discussion of regulatory and supervisory interest in privacy-preserving synthetic-data validation, without claiming a particular institution has deployed an FTSG pipeline.

---

## Comment 1.3 -- Duplicated declarations; CRediT inconsistent with the funding statement

> *Pages 27-28 already contain complete ethics, funding, data availability, competing interests, and author contributions statements, yet a separate duplicate declarations file was also submitted. Moreover, the body text assigns Ke Feng and Jing Xiao 'Supervision, Project administration,' while the CRediT statement adds 'Funding acquisition' -- contradicting the funding statement that 'the authors received no funding for this work.'*

**Response.** Both points are well taken. The separate duplicate declarations file has been withdrawn, and the declarations have been consolidated in one location in the main manuscript. We also removed the inconsistent Funding acquisition role.

**Changes in the manuscript.** The mandatory declarations now appear once, immediately before the References, in this order: Data Availability, Code Availability, Acknowledgements, Funding, Author Contributions, and Competing Interests. The Funding statement reports that no funds, grants, or other financial support were received during preparation of the manuscript. The Author Contributions statement now identifies Ke Feng and Jing Xiao only with *Supervision* and *Project administration*, and distinguishes **Y. Zhang** from **Y. Zou** to prevent abbreviation ambiguity. The same consolidated wording is prepared for the submission system.

---

## Comment 1.4 -- Unresolved internal BibTeX keys throughout the text

> *The text contains numerous internal BibTeX keys, e.g. 'wiese2020', 'xia2024market', 'li2025mars', 'tanaka2025cofindiff', 'berti2025trades', 'huang2024diga', 'istiaque2024cts', 'alex2024macroeconomic', 'hu2025fintsb', 'wang2025fintsbridge'. These appear not only in figures but throughout the body text.*

**Response.** We sincerely apologize. The affected strings were a compilation failure that was not detected before submission. We corrected the citation pipeline and checked the compiled text rather than relying on visual inspection alone.

**Changes in the manuscript.** All citations now render in sequential Nature numerical format, including citations in figures, tables, and legends. The bibliography is generated from `ultimate_complete.bib` using `naturemag.bst` and contains 130 entries. The canonical method names -- including QuantGAN, Market-GAN, CTS-GAN, MacroSynth, CoFinDiff, TRADES, DiGA, MarS, FinTSB, and FinTSBridge -- are written as reader-facing labels; no raw BibTeX key remains in the compiled manuscript. We also recompiled the source and checked the output text for the raw keys identified by the reviewer.

---

## Comment 1.5 -- Taxonomy figure implies an unjustified split of methods across tasks

> *The taxonomy figure places 'Statistical Frameworks' and 'Deep Learning Models' only under Extrapolation, but both classes apply equally to Imputation. The current tree implies an unwarranted separation.*

**Response.** We agree. The original graphic did not sufficiently distinguish task taxonomy from technique taxonomy and could imply that statistical and deep-learning approaches are exclusive to extrapolation.

**Changes in the manuscript.** The taxonomy has been regenerated as **Figure 2** in the current layout. It separates the three task formulations from the relevant algorithmic families and gives the Imputation branch its own temporal-disaggregation, tensor-factorization, recurrent/deep, adversarial, diffusion, and graph/transformer methods. The accompanying Results text and the task-technique mapping table make clear that method families are not exclusive to one task; Figure 3 separately visualizes the different conditioning and output structures of FTSE, FTSI, and FTSS.

---

## Comment 1.6 -- TAIL-GAN deserves a substantive explanation

> *The synthesis discussion packs RSQGAN, TAIL-GAN, DAT-CGAN, and Jinkou into one clause with no explanation of any of them. Given that TAIL-GAN in particular is one of the more methodologically interesting papers in the space (joint elicitability of VaR and ES), it deserves a paragraph.*

**Response.** We agree, and the previous one-clause treatment did not provide sufficient technical context. The synthesis discussion now gives each of these methods a dedicated explanation, with an expanded discussion of TAIL-GAN.

**Changes in the manuscript.** In the Results subsection *Financial Time-Series Synthesis*, the revised text contrasts the quantities matched by QuantGAN, RSQGAN, DAT-CGAN, Jinkou, and TAIL-GAN. The TAIL-GAN paragraph explains its risk-functional objective based on the joint elicitability of Value-at-Risk and Expected Shortfall, identifies the Acerbi-Szekely scoring-function basis of the training signal, reports the original study's five-asset, one-month evaluation setting, and states the limits of its evidence, including its restricted scale and its focus on risk functionals rather than stylized-fact reproduction.

---

# Reviewer 2

## Comment 2.1 -- Novelty over existing surveys is asserted but not demonstrated

> *The paper argues that prior surveys are architecture-centric and neglect evaluation and task formulation. This is a fair motivation, but the paper never substantiates it -- there is no comparison table contrasting this survey's scope against the six-plus surveys it cites as insufficient. Please add a table positioning this work along explicit dimensions: task coverage, evaluation treatment, dataset cataloging, number of papers reviewed, and time window. Without it, the central selling point rests on assertion.*

**Response.** We accept this criticism. The novelty claim required direct comparative evidence rather than assertion, so we constructed a new comparison table from the six cited surveys.

**Changes in the manuscript.** **Table 1** now compares this survey with the six prior surveys across FTSE, FTSI, and FTSS coverage; treatment of evaluation; financial dataset cataloguing; bibliography size; and publication window. The table shows that this review covers all three task formulations, provides a unified evaluation protocol, catalogs financial datasets and benchmark suites, and reviews 130 studies from 2021 to early 2026. The surrounding Introduction text limits its conclusion to what the table supports: the prior surveys do not jointly provide all of those elements.

---

## Comment 2.2 -- Screening statistics are internally inconsistent

> *The screening table and figure report different selected-study totals, while the task breakdown uses a different denominator. The Abstract and Introduction also state the corpus imprecisely. Please reconcile the screening flow, task totals, and all manuscript references to the final corpus.*

**Response.** The reviewer was right to request a full reconciliation. We re-audited the retrieval and screening record, chose one final corpus definition, and applied it consistently throughout the manuscript.

**Changes in the manuscript.** The final corpus is **130 studies**, with 54 extrapolation, 29 imputation, and 47 synthesis studies. **Table 8** and **Figure 6** now report 2,568 records retrieved, 604 records retained after title/abstract screening for full-text review, and 130 studies retained after full-text review. The Methods section states the same counting rule: each retained study is assigned one primary task category, while cross-cutting work is discussed where relevant but not double-counted. The Abstract, Introduction, Results, Discussion, and Table 1 now use the same final total.

---

## Comment 2.3 -- Uneven technical treatment and unsupported comparative claims

> *The extrapolation discussion is developed in reasonable depth, but synthesis and imputation lean on short descriptions, particularly the macro-simulation material, which reads as a list of methods rather than a critical analysis. For a survey, the value is in comparative synthesis: why one approach succeeds where another fails, and what the empirical evidence actually shows. Much of the text asserts superiority without pointing to comparative results that support the claim. Please ground comparative statements in reported evidence and add critical commentary rather than paraphrased method summaries.*

**Response.** This was the most substantive comment we received, and we have treated it accordingly. We re-read the primary sources for the imputation and synthesis sections, strengthened the mechanism-level analysis, and explicitly marked where the available evidence is limited to an individual study rather than a shared benchmark.

**Changes in the manuscript.**

1. The imputation discussion now formalizes the conditional reconstruction problem, distinguishes missingness mechanisms, and compares matrix/tensor, tree-based, GAN, diffusion, and foundation-model approaches by mechanism, strengths, and limitations. It explicitly notes that widely cited diffusion-imputation evidence often originates outside finance and should not be generalized without a financial benchmark.
2. The synthesis discussion now develops a critical narrative from conditional GANs through macroeconomic conditioning to diffusion and large-market models. It explains the relevant conditioning mechanisms, reported evaluation protocols, and failure modes rather than listing model names.
3. Claims that diffusion models categorically outperform GANs have been replaced by evidence-qualified language. The revised text explains that many reported improvements are within-paper comparisons against a paper's own baselines; a common cross-paper benchmark remains unavailable.
4. The Applications subsection now limits downstream statements to the conditions documented by the cited studies and explicitly removes or qualifies claims for which the original sources do not support a general conclusion.

---

## Comment 2.4 -- Figures contain placeholder citation keys

> *The timeline and taxonomy figures use BibTeX keys such as 'xia2024market' and 'li2025mars' as method names.*

**Response.** Corrected, and we apologize. The affected graphics were regenerated as production-ready standalone figure files.

**Changes in the manuscript.** The current **Figure 1** timeline uses proper model names and resolved publication references instead of internal keys. The current **Figure 2** taxonomy uses canonical method labels, including QuantGAN, RSQGAN, TAIL-GAN, DAT-CGAN, CoFinDiff, Market-GAN, CTS-GAN, MacroSynth, TRADES, DiGA, and MarS. The expanded figure legends define compact labels in prose, while the separate upload files omit embedded titles and legends as required by the journal. A compiled-PDF text check confirmed that the raw-key strings cited by the reviewer no longer appear.

---

## Comment 2.5 -- Abbreviations not defined at first occurrence

> *'NDDP' and 'FCI' in the figures, 'PEC-W' in the timeline, and technical terms such as CEEMDAN, GMDH, DCR, and TSTR/TRTR in the body text are not expanded at first use.*

**Response.** We agree. Rather than correcting only the listed examples, we audited technical abbreviations and compact model labels throughout the manuscript and figure legends.

**Changes in the manuscript.** Technical terms are expanded at their first substantive occurrence, including CEEMDAN (Complete Ensemble Empirical Mode Decomposition with Adaptive Noise), GMDH (Group Method of Data Handling), DCR (Distance-to-Closest Record), and TSTR/TRTR (Train-on-Synthetic, Test-on-Real / Train-on-Real, Test-on-Real). Figure legends now expand FCI (Financial Conditions Index) and NDDP (Nonlinear Diffusion Drift Process). Model labels such as PEC-W, RegTensor, and MarS are introduced with their cited source and an explanatory mechanism where they are discussed. This makes the figures self-contained without treating every original model name as an unexplained abbreviation.

We thank both reviewers again. Their scrutiny of our terminology, arithmetic, technical synthesis, and evidence base has substantially improved the revised manuscript.