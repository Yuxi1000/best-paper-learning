# Writing playbook

Patterns distilled from the 20 award papers. Use them as checks, not as a Mad Libs template.

## Abstract

Best-paper abstracts are closer to a proof sketch than to marketing.

**Default shape (method):**

1. Name the object you introduce in clause 1 (`We present VAR, a …`).
2. One precise defect of the status quo (raster-scan AR, modular driving stack, train-from-scratch protocol).
3. The move, in operational language (next-scale prediction, planning-oriented queries, registers, physics rollback).
4. Evidence: 2–4 numbers *or* a qualitative regime change.
5. Optional: what this implies for the field (scaling laws, backbone-ness, “do not train from scratch”).

**Default shape (analysis/science):**

1. Quote the community claim in neutral language.
2. Offer an alternative mechanism.
3. List the tests you will run (usually 2–3 complementary ones).
4. State the conclusion as a restriction on what the old claim may still mean.

Steal from:

- `var`: rename the learning problem, then dump FID/IS/speed.
- `swin`: domain mismatch (language vs vision) → inductive bias → three downstream numbers.
- `stde`: complexity diagnosis `O(d^k)` → construction → 1000× / 1M-D PDE.
- `emergent-mirage`: “alternative explanation”, then three tests.
- `never-train-from-scratch`: the protocol *is* the contribution; the number (PathX +20) is a corollary.
- `vit-registers`: observation → cheap fix → dense-prediction SOTA, but the real headline is cleaner maps.

Avoid: “to the best of our knowledge”, stacked citations, “extensive experiments demonstrate superiority”.

## Introduction

Open with a **decision the field is making badly**, not with 2017 Transformers lore.

Good openings in this corpus:

- `uniad`: the stack is perception→prediction→planning, so we should optimize for planning.
- `never-train-from-scratch`: random init is not a fair architecture test.
- `shallow-safety`: many jailbreaks share one shortcut (first tokens).
- `visprog`: compositional visual reasoning can be a program, not a trained monolith.
- `train-for-the-worst`: MDM trains on an exponential set of infills; inference can pick the easy ones.

Contribution lists that work:

- Each bullet starts with a verb: introduce / show / prove / release.
- Each bullet names an object (dataset, estimator, protocol) *and* a measurable consequence.
- Do not split “we propose X” and “X gets good numbers” into two bullets; fuse them.

Last intro paragraph: one-sentence paper map, not a teaser trailer.

## Related work

Position on **one axis** the method actually changes:

| Axis | Exemplar |
|---|---|
| Inductive bias / compute pattern | `swin` vs global ViT |
| Training protocol | `never-train-from-scratch` vs LRA-from-scratch |
| Generative factorization | `var` vs raster AR vs diffusion |
| Objective | `sedd` score-entropy vs continuous score matching |
| Task interface | `uniad` planning-first vs separate heads |
| Supervision richness | `richhf` vs scalar RLHF scores |

Do not write a survey. Write 3–5 contrastive paragraphs. End each with what remains unsolved *that this paper takes*.

## Method

Best method sections explain an *operator*, not a zoo of modules.

- `vit-registers`: add tokens; they absorb high-norm artifacts.
- `swin`: non-overlapping windows + shift; linear vs quadratic.
- `brickgpt`: next-brick tokens + physics rollback.
- `sedd`: ratio/score of discrete distributions; then the loss.
- `llm-finetuning-dynamics`: decompose how one example moves another; then DPO squeezing.

Recipe:

1. Setup (input, output, what is *not* assumed).
2. The one equation or algorithm block that is the paper.
3. Why a naive alternative fails (global attention, first-token refusal, random mask order).
4. Training / inference details only after the idea is inspectable.

If you need a large system (`uniad`, `videopoet`, `vggt`), still lead with the *interface* (unified queries, unified vocabulary, feed-forward 3D attributes), then modules.

## Experiments

Write results as **answers to the intro's bets**.

- Name the protocol before the table (`never-train-from-scratch`, `llm-debate`).
- Put the prior-flipping number in prose, not only in a table (`var` FID 18.65→1.73; Sudoku <7%→~90%).
- Include the obvious attack on your claim (different metric, different init, stronger baseline, on-policy vs off-policy).
- Ablations should kill *components of the story*, not random knobs.

`emergent-mirage` is the gold standard for “show the same data under two analyses”.

## Limitations and scope

Good limitations restrict the *mechanism*:

- where the shortcut could return
- which tasks the protocol does not cover
- compute that a follower would need
- what a negative result would look like

Bad limitations: “we did not try ImageNet-21K because of GPUs” as the only note.

## Appendix / supplementary

The appendix is where best papers **pay implementation debts** without clogging the main argument. It is not a junk drawer.

Typical appendix inventory in this corpus (see `corpus/arguments/appendix/INDEX.md`):

| Bucket | What belongs | Exemplars |
|---|---|---|
| Proofs / derivations | Lemmas that the main text cites by number | `sedd`, `privacy-auditing`, `train-for-the-worst`, `stde` |
| Extra experiments | Same claim, new setting / extra ablation | `sedd` D, `llm-debate` extra matches, `never-train-from-scratch` |
| Hyperparams / implementation | Prompt templates, optimizers, hardware, token formats | `brickgpt` A, `visprog` A.1–A.2, `sd3-rectified-flow` |
| Datasets / protocol | Filtering, annotation, human-study interface | `richhf`, `llm-debate` D, `uniad` F.1 |
| Failure / ethics / scope | Cases the main qualitative grid omitted | `brickgpt` D, `videopoet` fairness, `richhf` ethics |
| Extra qualitative | More samples, visual rationales | `visprog`, `videopoet` |

Moves that work:

- Open with a **contents list** of what the appendix contains (`visprog`, `uniad`).
- Every appendix subsection should be **cited from the main text** (“see App. D.3”). If it is not cited, cut it or cite it.
- Implementation details are copy-pasteable: full prompt, grid size, brick vocabulary, learning rate (`brickgpt`).
- Extra experiments answer an objection, they do not dump every sweep.
- Proofs start from the numbered claim in the main paper, not from a new story.
- 4 papers in the corpus have **no appendix in the arXiv PDF** (`vggt`, `var`, `swin`, `generative-image-dynamics`). Do not invent one for them; VAR ships a separate supplemental zip of extra samples.

When the user is writing a rebuttal, treat extra tables as appendix-style: short setup, one number, what it would have done to the paper if it were negative.

## Sentence craft

From this corpus, prefer:

- Short subject, concrete verb, measurable object.
- Contrast markers: `Instead`, `In stark contrast`, `This diverges from`.
- Numbers adjacent to the claim they support.
- One idea per paragraph; the last sentence is the takeaway.

Cut:

- `powerful`, `novel`, `facilitate`, `leverage` used as decoration
- `first to` unless you actually checked
- stacked hedges (`may potentially help enable`)

## Revision checklist

- [ ] Sentence 1 of abstract still true if you delete the rest?
- [ ] Status-quo failure is operational, not moral
- [ ] Each contribution maps to a figure or table
- [ ] Related work argues, it does not list
- [ ] Method can be reimplemented from the text without the figure
- [ ] Result paragraph states what would have refuted you
- [ ] No copied clause from an exemplar abstract
