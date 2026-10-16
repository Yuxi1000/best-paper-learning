---
name: best-paper-style
description: >-
  Studies a local corpus of 20 official CVPR/ICCV/NeurIPS/ICML/ICLR best or
  outstanding papers, then helps write, revise, or design figures for a research
  paper in that style. Use when writing or editing a paper, abstract,
  introduction, related work, method, experiments, limitations, appendix,
  supplementary, rebuttal, or camera-ready text; when designing or critiquing
  figures; or when the user says 写论文, 改论文, 画图, 附录, paper writing, or
  best-paper style.
---

# Best Paper Style

Do not draft, rewrite, or draw until you have studied matching exemplars from this skill's corpus. Imitate **moves**, not sentences or pixels.

Corpus root: `~/.cursor/skills/best-paper-style/corpus/`
Playbooks: `references/writing-playbook.md`, `references/figure-playbook.md`, `references/exemplar-map.md`, `references/paper-notes.md`

## Hard rules

1. **Study first.** Open the files listed below. If you skipped them, you are not done.
2. **Do not copy prose.** No sentence, title clause, or caption may be reused. Transfer structure, claim order, and visual grammar only.
3. **Do not pirate figures.** Do not trace, collage, or regenerate a paper's photos/samples. Redesign a *new* figure that uses the same layout logic.
4. **Cite the source of the pattern** in a short `Studied` block so the user can see what you learned.
5. Match the user's paper language (usually English for the manuscript, Chinese for coaching unless they ask otherwise).
6. If the user's claim is weaker than a best-paper claim, shrink the sentence. Do not inflate.

## Workflow

Copy and track:

```
Paper-style progress:
- [ ] 1. Classify the task and paper type
- [ ] 2. Pick 3-5 exemplars from exemplar-map.md
- [ ] 3. Read those abstracts + paper-notes
- [ ] 4. Read the matching argument excerpts and 2-4 figures
- [ ] 5. State transferable patterns
- [ ] 6. Draft / revise / specify the figure
- [ ] 7. Self-check against the playbook
```

### 1. Classify

Decide both:

- **Task**: `abstract` | `intro` | `related-work` | `method` | `experiments` | `limitations` | `appendix` | `rebuttal` | `full-outline` | `figure` | `caption` | `review-existing-draft`
- **Paper type**: `method-system` | `method-architecture` | `analysis-method` | `empirical-science` | `theory-method` | `dataset-method` | `method-scaling`

If the user pasted a draft, treat it as `review-existing-draft` plus the section they care about.

### 2. Pick exemplars

Read [references/exemplar-map.md](references/exemplar-map.md). Pick **3–5** paper ids. Prefer mix:

- 2 close in *task/type*
- 1 close in *section/figure genre*
- 1 contrast paper (different type) so you do not overfit one voice

### 3. Study (required reads)

For each chosen id `P`:

1. `corpus/abstracts/P.md`
2. The `P` section in [references/paper-notes.md](references/paper-notes.md)
3. One argument file if it exists, matching the task:
   - intro/abstract → `corpus/arguments/problem-framing/P.md` and `claim-contribution/P.md`
   - related work → `corpus/arguments/related-work/P.md`
   - method → `corpus/arguments/method-mechanism/P.md`
   - experiments → `corpus/arguments/experiment-result/P.md`
   - limitations → `corpus/arguments/limitation-scope/P.md`
   - appendix / supplementary / extra ablation / proof / hyperparams / rebuttal dump → `corpus/arguments/appendix/P.md` plus the matching genre file under `corpus/arguments/appendix/{proofs,extra-experiments,hyperparams-implementation,failure-cases,datasets-protocol,qualitative-extra}/P.md` if it exists. Also read `corpus/arguments/appendix/INDEX.md`. Prefer `corpus/figures/appendix/P/` page renders.
4. For figures: prefer `corpus/figures/page-renders/P/` if present; else 2–4 images under `corpus/figures/{teaser,architecture,qualitative,quantitative,analysis-diagram}/` whose filename starts with `P-`. Also skim `corpus/style-cards/P.md` for captions.

Also read the relevant section of [references/writing-playbook.md](references/writing-playbook.md) and, if drawing, [references/figure-playbook.md](references/figure-playbook.md).

Raster crops can be photos embedded inside a figure, not the whole figure. **Page renders and captions are the authority.**

### 4. Emit a Studied block, then work

Always start the user-visible answer with:

```markdown
## Studied
- `id`: one-line lesson
- `id`: one-line lesson

## Patterns to transfer
1. ...
2. ...
3. ...
```

Then produce the draft, revision, figure spec, or critique.

## Output recipes

### Writing or rewriting a section

- Keep the user's scientific claims. Change only structure, emphasis, and wording craft.
- Put the **crux in sentence 1–2**, not after a literature tour.
- Prefer concrete failure of the status quo over “little work has been done”.
- Contributions should be falsifiable and matched later by experiments.
- After drafting, cut 10–15% of adjectives and all “novel/powerful/first” unless the corpus-style evidence is actually in the user's results.

### Reviewing a draft

Return:

1. What the draft is trying to claim
2. Which exemplar has a better move for that claim
3. Line-level rewrite of the 3 weakest paragraphs
4. What evidence is still missing

### Figures

Do not jump to an image. First write a **figure spec**:

- genre: teaser / architecture / qualitative / quantitative / analysis / protocol / appendix-extra
- claim the figure must make in one sentence
- panel list (a, b, c…) with what each panel proves
- labels, units, legend, and the caption
- which exemplar layout you are borrowing

Only then draw (Mermaid, SVG, TikZ-like description, or an image tool). Caption must state the result, not the plot type.

## Quality bar

A best-paper sentence usually does one of:

- names a precise failure of current practice
- defines a new *task interface* or *training protocol*, not just a module
- reports a number that changes the reader's prior
- explains a mechanism, then offers a cheap fix

Reject drafts that only say “we propose an improved network and get higher accuracy”.

## Additional resources

- Corpus index: [corpus/INDEX.md](corpus/INDEX.md)
- Rebuild corpus: `scripts/build_corpus.py` (only if the user asks to refresh papers)
- Rebuild appendix only: `scripts/extract_appendix.py`
