# Best-paper style corpus

Study these files before writing or drawing. Copy patterns, not sentences.

| id | award | type | abstract | style card | use for |
|---|---|---|---|---|---|
| `vggt` | CVPR 2025 Best Paper | method-system | [abstract](abstracts/vggt.md) | [card](style-cards/vggt.md) | architecture-figure, system-method, strong-abstract |
| `generative-image-dynamics` | CVPR 2024 Best Paper | method-system | [abstract](abstracts/generative-image-dynamics.md) | [card](style-cards/generative-image-dynamics.md) | teaser, qualitative-grid, problem-reframing |
| `richhf` | CVPR 2024 Best Paper | dataset-method | [abstract](abstracts/richhf.md) | [card](style-cards/richhf.md) | dataset-paper, annotation-figure, application-loop |
| `visprog` | CVPR 2023 Best Paper | method-system | [abstract](abstracts/visprog.md) | [card](style-cards/visprog.md) | intuitive-method, pipeline-figure, no-training-claim |
| `uniad` | CVPR 2023 Best Paper | method-system | [abstract](abstracts/uniad.md) | [card](style-cards/uniad.md) | task-reframing, system-architecture, metric-story |
| `swin` | ICCV 2021 Best Paper (Marr Prize) | method-architecture | [abstract](abstracts/swin.md) | [card](style-cards/swin.md) | architecture-figure, inductive-bias-argument, backbone-paper |
| `brickgpt` | ICCV 2025 Best Paper (Marr Prize) | method-system | [abstract](abstracts/brickgpt.md) | [card](style-cards/brickgpt.md) | constraint-in-decoding, qualitative, dataset-plus-method |
| `var` | NeurIPS 2024 Best Paper | method-generative | [abstract](abstracts/var.md) | [card](style-cards/var.md) | paradigm-shift-claim, scaling-plot, headline-numbers |
| `vit-registers` | ICLR 2024 Outstanding Paper | analysis-method | [abstract](abstracts/vit-registers.md) | [card](style-cards/vit-registers.md) | observe-explain-fix, feature-map-figure, short-elegant-paper |
| `never-train-from-scratch` | ICLR 2024 Outstanding Paper | empirical-science | [abstract](abstracts/never-train-from-scratch.md) | [card](style-cards/never-train-from-scratch.md) | experimental-protocol, negative-result-plus-fix, fair-comparison |
| `emergent-mirage` | NeurIPS 2023 Outstanding Paper | empirical-science | [abstract](abstracts/emergent-mirage.md) | [card](style-cards/emergent-mirage.md) | metric-critique, reanalysis-figure, claim-dismantling |
| `shallow-safety` | ICLR 2025 Outstanding Paper | analysis-method | [abstract](abstracts/shallow-safety.md) | [card](style-cards/shallow-safety.md) | unifying-explanation, case-study-structure, mitigation-from-diagnosis |
| `llm-finetuning-dynamics` | ICLR 2025 Outstanding Paper | analysis-theory | [abstract](abstracts/llm-finetuning-dynamics.md) | [card](style-cards/llm-finetuning-dynamics.md) | mechanism-explanation, theory-to-fix, influence-analysis |
| `privacy-auditing` | NeurIPS 2023 Outstanding Paper | theory-method | [abstract](abstracts/privacy-auditing.md) | [card](style-cards/privacy-auditing.md) | tight-problem-setup, theory-to-algorithm, practical-bound |
| `stde` | NeurIPS 2024 Best Paper | theory-algorithm | [abstract](abstracts/stde.md) | [card](style-cards/stde.md) | complexity-argument, algorithm-paper, headline-speedup |
| `sedd` | ICML 2024 Best Paper | method-theory | [abstract](abstracts/sedd.md) | [card](style-cards/sedd.md) | objective-derivation, discrete-generative, theory-plus-scale |
| `videopoet` | ICML 2024 Best Paper | method-system | [abstract](abstracts/videopoet.md) | [card](style-cards/videopoet.md) | system-paper, task-unification, qualitative-video |
| `sd3-rectified-flow` | ICML 2024 Best Paper | method-scaling | [abstract](abstracts/sd3-rectified-flow.md) | [card](style-cards/sd3-rectified-flow.md) | scaling-study, architecture-ablation, industrial-scale-writing |
| `llm-debate` | ICML 2024 Best Paper | empirical-science | [abstract](abstracts/llm-debate.md) | [card](style-cards/llm-debate.md) | protocol-paper, human-study, claim-with-controls |
| `train-for-the-worst` | ICML 2025 Outstanding Paper | analysis-theory | [abstract](abstracts/train-for-the-worst.md) | [card](style-cards/train-for-the-worst.md) | train-test-mismatch, theory-plus-simple-fix, headline-jump |

## Folder map

- `abstracts/` — one file per paper, official arXiv abstract
- `arguments/` — truncated section excerpts by rhetorical move
- `figures/` — extracted figures by visual genre (raster crops; can be sub-images)
- `figures/page-renders/` — full PDF pages for papers whose figures are mostly vectors
- `style-cards/` — figure inventory and captions
- `pdfs/` — source PDFs from arXiv
- `NOTICE.md` — study-only / no-copy policy

For writing style, prefer `../references/paper-notes.md` over the generic style-card boilerplate.

## Argument buckets

- `arguments/problem-framing/`
- `arguments/claim-contribution/`
- `arguments/related-work/`
- `arguments/method-mechanism/`
- `arguments/experiment-result/`
- `arguments/limitation-scope/`
- `arguments/appendix/` — supplementary TOC + excerpts; genre subfolders; see `arguments/appendix/INDEX.md`

## Figure buckets

- `figures/teaser/`
- `figures/architecture/`
- `figures/qualitative/`
- `figures/quantitative/`
- `figures/ablation/`
- `figures/analysis-diagram/`
- `figures/appendix/<id>/` — rendered appendix pages
