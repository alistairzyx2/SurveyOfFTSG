Dear Dr. Monika Samra and Editorial Team of *npj Artificial Intelligence*,

We sincerely appreciate the editorial team's careful technical review of our manuscript. We have addressed every item in the Technical Check letter and have revised the manuscript and submission materials accordingly. The revised manuscript now follows the required IRDM structure, uses unnumbered headings, contains a single-paragraph abstract of 173 words, uses sequential Nature-style numerical citations, places all declarations in the main manuscript, and provides the requested standalone figure files and PRISMA 2020 checklist.

In brief:

1. **The title page has been corrected.** All affiliations are linked to the authors by sequential superscript numbers and include institution, city, and country; the corresponding authors and their institutional email addresses are clearly identified.
2. **The abstract has been reformatted.** It is a single English paragraph of 173 words, without headings or paragraph breaks.
3. **The manuscript has been reorganized into IRDM format.** It now follows Abstract, Introduction, Results, Discussion, Methods, Declarations, References, Figure Legends and Figures, and Tables; headings are unnumbered throughout.
4. **The requested declarations are complete and placed in the main manuscript.** Data Availability, Code Availability, Acknowledgements, Funding, Author Contributions, and Competing Interests precede the References.
5. **References and figures have been prepared for production.** The bibliography uses sequential Nature numbering, figure legends appear after References, and clean standalone files for Figures 1--6 are available for individual upload.
6. **All supplementary and submission materials have been prepared.** These include clean and marked-up manuscripts, the PRISMA 2020 checklist, the separate figure files, and a cover letter confirming figure originality.

The point-by-point response below reproduces each technical request before describing the corresponding revision. Where the Technical Check requested matching information in SNAPP, the identical final wording has been prepared for entry in the relevant submission-system field.

Sincerely,

Yingxiao Zhang, on behalf of all co-authors

---

# Technical Check

## Point 1 -- Author affiliations and ordering

> *"Please ensure an affiliation, including city and country information, or a URL, is provided on the title page for all authors, including for the corresponding author(s). It should be made clear which affiliation belongs to each author e.g. by using a numbered list or using superscript numbering. Please ensure that all author affiliations appear in the correct sequential order according to their position in the author list. Affiliation 1 must be associated with the first author."*

**Response.** We have revised the title page so that author-affiliation mapping is explicit and sequential. Yingxiao Zhang is listed with affiliations $^{1,2}$; Jiaxin Duan with $^{3}$; Yue Zou with $^{1,2}$; Ke Feng with $^{1,*}$; and Jing Xiao with $^{4,*}$. Affiliation 1 is therefore associated with the first author. The four affiliations are presented in this order:

1. School of Software and Microelectronics, Peking University, Beijing, China.
2. Pingan Bank Co., Ltd., Shenzhen, China.
3. China Electronics Cloud Technology Co., Ltd., Beijing, China.
4. Pingan Group Co., Ltd., Shenzhen, China.

Both corresponding authors are marked with an asterisk, and their institutional email addresses are provided on the title page.

---

## Point 2 -- Abstract formatting and word count

> *"The journal does not permit a structured abstract. The abstract must be a single paragraph with no headings (e.g. Methods, Results, Conclusions) or paragraphs, should be around 150-200 words, and written in the English language. Please also ensure you also update the Abstract in the submission system."*

**Response.** We have condensed and reformatted the abstract as a single English paragraph of **173 words**. It contains no subheadings, bold labels, or paragraph breaks, and is within the requested 150--200-word range. The identical abstract text has been prepared for the submission system.

---

## Point 3 -- Removal of section numbers and cross-references

> *"Please note that section numbers will not be retained during typesetting of the manuscript. Section numbers must be removed from the headings, and reference to section numbers in the main text must be changed to the section headings."*

**Response.** We set `\setcounter{secnumdepth}{0}` in the LaTeX preamble, removing numerical identifiers from all section, subsection, and subsubsection headings. We also audited the main text and replaced references such as "Section 2" or "Section 3--6" with descriptive titles, including the Results subsections, the Methods section, and the Evaluation Protocols subsection.

---

## Point 4 -- Unstructured Introduction

> *"We do not allow a structured Introduction with subheadings. It can only be divided into paragraphs."*

**Response.** All former Introduction subheadings have been removed. The Introduction is now presented as a sequence of coherent paragraphs, with the final paragraph outlining the manuscript's IRDM organization without using a subheading.

---

## Point 5 -- Required IRDM structure

> *"Format of Research Article: IRDM. Please arrange your manuscript according to the below order: Abstract: up to 200 words in length, without subheadings; Introduction: no subheadings permitted; Results: subheadings are compulsory; Discussion: no subheadings permitted; Limitations/Conclusions: not permitted, if present incorporate it into Discussion; Methods: subheadings are compulsory; Declaration statements; References list; Figures, Tables and associated legends; Supplementary information; Mandated checklist: CONSORT/PRISMA/PRISMA-SCR (if applicable, provide as Supplementary Material)."*

**Response.** The manuscript has been reorganized in the required sequence:

- **Abstract:** one unstructured paragraph of 173 words.
- **Introduction:** continuous paragraphs, without subheadings.
- **Results:** seven thematic subsections covering the taxonomy, extrapolation, imputation, synthesis, applications, evaluation, and data resources.
- **Discussion:** a single unstructured section integrating limitations and the concluding outlook.
- **Methods:** placed after Discussion, with subsections for literature retrieval, eligibility criteria, data extraction and coding, and taxonomy synthesis.
- **Declarations:** Data Availability, Code Availability, Acknowledgements, Funding, Author Contributions, and Competing Interests.
- **References, Figure Legends and Figures, and Tables:** placed after the main text and declarations.

The PRISMA 2020 checklist is supplied separately as Supplementary Information.

---

## Point 6 -- Renaming and reorganizing the survey sections

> *"We do not permit 'Methodology of the Survey, Problem Formulation and A Two-Level Taxonomy, Financial Time-Series Extrapolation, Financial Time-Series Imputation, Applications, Financial Time-Series Synthesis, Evaluation Protocols, Data Resources and Benchmarks, Open Challenges and Future Directions' sections. Please rename it to 'Introduction/Methods/Discussion'."*

**Response.** We have replaced the former survey-style top-level organization with the required article structure. The literature-retrieval material is now the **Methods** section. The taxonomy, task-specific technical synthesis, applications, evaluation, and data-resource material are nested as required subsections within **Results**. The former open-challenges material is incorporated into **Discussion**.

---

## Point 7 -- No standalone Conclusions section

> *"We do not permit a Conclusions section. Please rename it to 'Discussion' or incorporate the text into the 'Discussion' section, as applicable."*

**Response.** The standalone Conclusions section has been removed. Its concluding content, together with the former open-challenges discussion and limitations, has been incorporated into the final paragraphs of the unstructured **Discussion** section.

---

## Point 8 -- Acknowledgements and Funding statements

> *"Please supply an Acknowledgements section before the References. If you have no acknowledgements to declare, please state 'Not applicable' under the heading. The Acknowledgements section should be brief and should not include thanks to Editors or referees, effusive comments, or dedications. Please ensure to update the statement on the SNAPP submission system as well. Please supply a Funding section after the Acknowledgements section. Please include all funding information, including the role of the funder(s) in the 'Funding' section. If no funding was granted for the study, please also state this in the Funding Statement."*

**Response.** We have placed both statements before the References in the required order. The Acknowledgements section is limited to one factual sentence thanking colleagues and research-group members for constructive discussions that helped refine the survey's scope and taxonomy; it contains no acknowledgement of editors or reviewers. The Funding statement reads: "The authors declare that no funds, grants, or other financial support were received during the preparation of this manuscript." The same statements are prepared for the corresponding SNAPP fields.

---

## Point 9 -- Competing Interests statement

> *"Authors must disclose and specify any competing interest, using the following statement as applicable. No Competing Interests: If there are no financial or non-financial competing interests, please add the statement: 'The authors declare no competing financial or non-financial interests.' ... The competing interests statement must be included both in the manuscript and in the submission system for full transparency."*

**Response.** The main manuscript now includes the requested statement verbatim under the mandatory heading:

> **Competing Interests.** The authors declare no competing financial or non-financial interests.

The same wording is prepared for the submission-system declaration.

---

## Point 10 -- Nature reference format

> *"Please ensure the references are in the standard Nature format. References should be numbered sequentially as they appear in the text, methods, tables, and figure legends using a 1, 2, 3, format. They should follow the sequence: author list, title of the paper, name of the journal, volume number, initial-final page numbers or article number (year). ... Please either provide a separate BIB/BIBL file, or recompile your LaTeX file to include this information."*

**Response.** We have migrated the citation and bibliography pipeline to sequential Nature-style numerical formatting using `naturemag.bst`. Citations are numbered in first-appearance order across the text, Methods, tables, and figure legends, and the reference list contains **222** sequential entries in the Nature format. The source bibliography (`ultimate_complete.bib`) is available separately, and the LaTeX manuscript has been recompiled to verify that citations and bibliography entries render without unresolved keys or display errors.

---

## Point 11 -- Individual figure files and expanded figure legends

> *"Please provide figure files individually in the system (Figure 1, Figure 2, Figure 3...etc.). Figures 1a-d should be included in Figure 1 file. Add the legends in the main manuscript file after references. Figure titles and legends must be removed from the image file. ... Please remove the figure label (e.g. Figure 1) from the image."*

> *"Begin each figure legend with a concise sentence summarizing the content of the figure; this will serve as the figure title. This should be followed by a detailed description of the figure in the following sentences, up to 350 words, to serve as the legend body. Define all abbreviations, symbols, and color codes used in the figure. Do not use graphical symbols directly, describe them in words ... Present multi-panel figures on a single page, labeled a), b), c), etc., with each panel described individually."*

**Response.** We have completed all figure-related revisions:

1. **Placement and numbering:** Figure Legends and Figures and Tables are now separate sections after the References. In-text figure callouts proceed in order from Figure 1 through Figure 6.
2. **Standalone upload files:** clean high-resolution files for Figures 1--6 have been prepared in `separate_figures/` as `Figure1.pdf`, `Figure2.pdf`, `Figure3.png`, `Figure4.pdf`, `Figure5.pdf`, and `Figure6.png`. They contain no embedded figure title, legend, or Figure-number label.
3. **Legends:** each caption begins with a concise bold summary sentence and then gives a detailed prose description. The legends define abbreviations, panels, line styles, and color coding in words; all are within the requested 350-word limit.
4. **Multi-panel figures:** panels are combined within their corresponding individual figure file and identified and described as **a**, **b**, and **c** where applicable.

---

## Point 12 -- Clean and marked-up manuscript files

> *"Please note that we require both clean and marked-up versions of the manuscript at this stage. In order to ensure that we are able to process your files properly, please provide your clean article file without any red text as a Manuscript file. Please upload the marked-up version of the manuscript to the submission system as a Related manuscript file."*

**Response.** We have prepared the two required versions:

- **Clean manuscript:** `is26.pdf`, without red text or annotations, formatted in IRDM order and ready for production processing.
- **Marked-up manuscript:** `is26_marked.pdf`, with a revision summary and visible indications of the technical changes, prepared for upload as the Related manuscript file.

---

## Point 13 -- Data and Code Availability

> *"The Data Availability information must also be uploaded to system, and the details provided there should match exactly with the statement in the manuscript."*

**Response.** Both statements now appear in the main manuscript. The Data Availability statement explains that no new empirical primary datasets were generated and identifies the public datasets, databases, and APIs reviewed in the survey; it also states that the supporting query logs and extraction coding tables are available from the corresponding authors upon reasonable request. The Code Availability statement explains that the systematic survey generated no custom algorithmic codebase and directs readers to the cited public model and benchmark repositories. The identical wording is prepared for the corresponding submission-system fields.

---

## Point 14 -- Figure originality and copyright confirmation

> *"Please state in your cover letter whether all Figures are your own or taken from another source. If figures and every element of it are taken from another source/created using a tool or software; and if it is under copyright they also state the written permission given to use and adapt it. If the above conditions are not met the image needs to be removed. Please supply proof of permission for its use ... Please ensure the appropriate credit line is present in the relevant figure caption(s)."*

**Response.** The accompanying `Cover_Letter.pdf` confirms that all six figures and all figure elements are original works created by the authors. Figure 1 was prepared using LaTeX TikZ, Figure 2 using LaTeX Forest, and Figures 3--6 using the authors' scientific diagramming tools. No material has been reproduced or adapted from a third-party copyrighted source, so no external permission, licence documentation, or credit line is required.

---

## Point 15 -- Author Contributions consistency

> *"Please note that Author contribution statement provided in manuscript should exactly match with that uploaded in the system."*

**Response.** We have placed a single Author Contributions statement in the main manuscript and prepared the same wording for the submission system. To avoid ambiguity between Yingxiao Zhang and Yue Zou, whose initials would otherwise both be Y. Z., the statement uses the distinct forms **Y. Zhang** and **Y. Zou** throughout.

---

## Point 16 -- PRISMA checklist and declaration placement

> *"Please note that systematic reviews and meta-analyses papers must adhere to the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) or PRISMA-SCR for scoping reviews. It is mandatory to provide a completed PRISMA checklist (or appropriate extension) in the Supplementary Information. Please crosscheck your reporting with the checklist before submitting the revised version of your manuscript. Please note to provide all the declaration in the main manuscript file instead of supplementary file."*

**Response.** We have prepared `Supplementary_Information_PRISMA.pdf`, a single merged supplementary PDF containing a completed PRISMA 2020 checklist for all 27 standard reporting items, with each item mapped to its location in the revised manuscript. All six declarations are placed in the main manuscript before the References rather than in the supplementary file.

We thank the editorial team again for the detailed guidance. We trust that the revised files meet the technical requirements for the manuscript to proceed.