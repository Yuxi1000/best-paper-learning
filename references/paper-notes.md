# Paper notes (imitation, not summary)

For each id: the rhetorical bet, abstract move, figure move. Do not paste these sentences into a user paper.

Appendix inventory and excerpts live in `corpus/arguments/appendix/INDEX.md`. Four arXiv PDFs have no appendix (`vggt`, `var`, `swin`, `generative-image-dynamics`).

## vggt

- Bet: 3D reconstruction does not need a per-scene optimizer if a big feed-forward transformer sees enough 3D-annotated views.
- Abstract move: object (`VGGT`) → input cardinality (1 to hundreds) → outputs (camera, depth, points, tracks) → time (<1s) → beats optimization without post-process.
- Figure move: one teaser that shows *all* output heads on real images. The overlay *is* the method.
- Steal: multi-output system papers should list the output tuple in sentence 1, not in page 4.
- Do not steal: DUSt3R-bashing tone; copy their scene photos.

## generative-image-dynamics

- Bet: a still image contains a distribution over plausible motion; generation can be an image-conditioned dynamics model.
- Abstract/intro move: re-define the task (predict motion from one photo) before naming the network.
- Figure move: qualitative loops / future frames as proof that the task exists.
- Steal: when the contribution is a new *task*, lead with phenomena, not architecture.

## richhf

- Bet: scalar human scores are too thin for T2I; region- and word-level feedback is the missing interface.
- Abstract move: enrich the signal (i, ii, iii) → collect 18K → train a predictor → close the loop (filter, inpaint).
- Figure move: annotation overlays (heatmaps + tagged words) teach the reader the label protocol in one glance.
- Steal: dataset papers must show the *schema*, then one downstream use that generalizes to a held-out generator.

## visprog

- Bet: compositional visual reasoning can be a program synthesized from language, using frozen skills, with no training.
- Abstract move: name the interface (visual programs) and the non-claim (without training).
- Figure move: pipeline that is literally code + intermediate images. Transparency is the aesthetic.
- Steal: if you claim “no training”, the figure must show the program, not a new backbone.

## uniad

- Bet: driving stacks should be optimized for planning; perception/prediction exist to serve that goal.
- Abstract move: diagnose accumulative error / poor coordination → “oriented at” the ultimate goal → unified queries.
- Figure move: full-stack architecture with a rightward arrow toward planning, not equal-height module boxes.
- Steal: system papers need a *priority order* among tasks, not “we also do detection”.

## swin

- Bet: Transformers become vision backbones if you restore hierarchy and locality (shifted windows).
- Abstract move: domain mismatch (scale, resolution) → operator → linear complexity → three dense-task numbers with deltas.
- Figure move: **the** architecture teaser: (a) hierarchical windows vs (b) ViT single-scale. Same drawing language.
- Steal: backbone papers live or die on Fig.1 contrast + transfer numbers, not ImageNet-only bragging.

## brickgpt

- Bet: next-token models can emit brick assemblies if training data are physically stable and inference can roll back illegal tokens.
- Abstract move: dataset + autoregressive policy + physics-aware decoding. All three are first-class.
- Figure move: prompt → brick object; plus a failure that rollback catches.
- Steal: constrained generation papers should put the constraint in the *decoder*, visibly.

## var

- Bet: image AR should be next-scale, not next-pixel; then GPT-style models can beat diffusion.
- Abstract move: rename the prediction problem → “for the first time” only after the rename → FID/IS/speed triad → scaling-law r value → zero-shot edits.
- Figure move: sample grid as Fig.1; Fig.2 conceptual AR vs VAR; scaling plot with a validation-FID floor.
- Steal: if you claim a new paradigm, Fig.2 must make the old factorization look wrong.

## vit-registers

- Bet: high-norm background tokens are a real computational artifact; extra register tokens absorb them.
- Abstract move: identify → characterize → hypothesize role → one-line fix → dense-task and qualitative map cleanup.
- Figure move: feature/attention maps before vs after. The “ugly blotches go away” panel is the paper.
- Steal: observe-explain-fix. Do not bury the observation in related work.

## never-train-from-scratch

- Bet: architecture gaps on long-seq benchmarks are inflated by random initialization; self-pretrain on the same data first.
- Abstract move: community protocol named and attacked; then Transformers match S4; then +20 on PathX; then structured SSM params look redundant.
- Figure move: same benchmark, two training recipes. The crossing is the result.
- Steal: if your contribution is a *fair test*, write the test before the model names.

## emergent-mirage

- Bet: “emergent abilities” can be a metric artifact (nonlinear/discontinuous metrics).
- Abstract move: restate the claim → alternative explanation → three independent tests, including *inducing* fake emergence in vision.
- Figure move: two curves, same x, different y-transforms. Inevitable conclusion.
- Steal: adversarial analysis papers should pre-register predictions, then confirm them.

## shallow-safety

- Bet: many LLM jailbreaks are one phenomenon: safety lives in the first few tokens.
- Abstract move: unify disparate attacks under “shallow alignment” → case studies → deepen alignment and constrain finetuning of those tokens.
- Figure/table move: token-index plots; ASR vs position. Mechanism first, defense second.
- Steal: name the shortcut so that several prior papers become special cases.

## llm-finetuning-dynamics

- Bet: finetuning (SFT/DPO) can be read as influence of examples on other examples; this explains hallucinations and DPO squeezing.
- Abstract move: framework → unify known quirks → one extra phenomenon (squeezing) → a simple fix.
- Figure move: influence heat / probability trajectories, not architecture clipart.
- Steal: theory that earns its keep by explaining a known bug, then patching it.

## privacy-auditing

- Bet: you can lower-bound ε from **one** training run by auditing many independent canaries in parallel.
- Abstract move: exploit add/remove parallelism; connect DP to generalization; black-box and white-box; CIFAR number vs theory.
- Figure move: sparse; page renders show lemma/algorithm density. Visual quietness is a feature.
- Steal: put the resource constraint (“one run”) in the title and sentence 1.

## stde

- Bet: high-order multivariate differential operators are expensive because of tensor size and graph size; Taylor-mode tangents fix both.
- Abstract move: write `O(d^k)` and `O(2^{k-1}L)` in the abstract → construction → 1000× and 1M-D in 8 minutes.
- Figure move: complexity schematic or timing vs dimension. The y-axis is log-time.
- Steal: algorithm papers should make the cost the villain.

## sedd

- Bet: discrete diffusion needs a ratio/score-entropy objective, not a naive port of continuous score matching.
- Abstract/method move: derive the estimator, then scale it.
- Figure move: samples plus likelihood/perplexity tables. Theory papers still need one visual of the object being generated.
- Steal: say what quantity you estimate, in the title.

## videopoet

- Bet: a decoder-only LLM over a unified multimodal vocabulary can zero-shot many video tasks.
- Abstract move: one architecture, many tasks (T2V, I2V, in/outpaint, continuation).
- Figure move: task-matrix qualitative; super-res as a separate operator is allowed if labeled.
- Steal: system papers sell the *task set* more than the layer count.

## sd3-rectified-flow

- Bet: scaling rectified-flow transformers (MM-DiT, etc.) is a design-ablation problem at industrial compute.
- Abstract/method move: few architectural bets, then scaling plots and human eval.
- Figure move: architecture block + size/quality Pareto. Clean, not cute.
- Steal: when compute is part of the contribution, show scaling, not a toy CNN diagram.

## llm-debate

- Bet: a weaker judge (human or model) gets more truth if stronger models debate.
- Abstract move: protocol → “more persuasive ⇒ more truthful” as a measured relationship, not a slogan.
- Figure move: debate diagram with information flow; then accuracy vs persuader strength.
- Steal: social/oversight papers must draw the protocol so a skeptic can attack it.

## train-for-the-worst

- Bet: masked diffusion trains on intractable random infills, but adaptive unmasking at test time skips the hard ones.
- Abstract move: train-time exponential hardness vs inference-time order choice; Sudoku <7% → ~90% without retraining.
- Figure move: schematic of random vs confidence order; bar jump so large it needs little decoration.
- Steal: if a one-line inference change is the result, do not hide it inside a new network.
