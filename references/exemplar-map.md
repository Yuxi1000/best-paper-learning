# Exemplar map

Pick 3–5 ids. Read their abstracts and the matching `paper-notes` section before writing.

## By writing task

| Task | Primary ids | Why |
|---|---|---|
| Abstract (method, punchy numbers) | `var`, `vggt`, `swin`, `stde` | Claim in sentence 1; status-quo failure; 1–3 headline numbers |
| Abstract (analysis / science) | `emergent-mirage`, `never-train-from-scratch`, `vit-registers`, `train-for-the-worst` | Alternative explanation; predictions; protocol that changes the conclusion |
| Introduction / problem framing | `uniad`, `never-train-from-scratch`, `shallow-safety`, `visprog` | Reframe the *goal* or the *evaluation*, not just the module |
| Contribution bullets | `videopoet`, `privacy-auditing`, `llm-debate`, `var` | Each bullet is a deliverable plus a testable consequence |
| Related work positioning | `swin`, `sedd`, `uniad`, `sd3-rectified-flow` | Contrast on one axis (bias, objective, task interface) |
| Method mechanism | `vit-registers`, `swin`, `sedd`, `brickgpt` | Simple operator, then why it must work |
| Experiments / results prose | `var`, `never-train-from-scratch`, `llm-debate`, `train-for-the-worst` | Protocol first; number that flips a prior; controls |
| Limitations | `generative-image-dynamics`, `videopoet`, `shallow-safety` | Scope, failure cases, what the mechanism does not imply |
| Appendix / supplementary | `brickgpt`, `visprog`, `sedd`, `uniad`, `train-for-the-worst` | Contents list; proofs; extra ablations; copy-pasteable implementation |
| Appendix proofs | `sedd`, `privacy-auditing`, `train-for-the-worst`, `stde` | Numbered lemmas that the main text already cited |
| Appendix extra experiments | `sedd`, `llm-debate`, `sd3-rectified-flow`, `never-train-from-scratch` | Same claim, new setting; not an uncited sweep |
| Appendix hyperparams / prompts | `brickgpt`, `visprog`, `richhf`, `videopoet` | Prompt templates, grids, token formats, hardware |
| Rebuttal extra tables | `emergent-mirage`, `never-train-from-scratch`, `llm-debate` | One protocol change, one number, what it does to the claim |
| Dataset + method papers | `richhf`, `brickgpt` | Annotation interface, then a model that *uses* the new signal |
| Theory-to-algorithm | `privacy-auditing`, `stde`, `sedd`, `llm-finetuning-dynamics` | Cost/complexity, then a construction that removes it |
| Scaling / industrial method | `sd3-rectified-flow`, `var`, `videopoet` | Design choice → ablation at scale → qualitative |

## By figure genre

| Figure you need | Look at | Borrow this |
|---|---|---|
| Page-1 teaser that states the whole paper | `swin` page-render p.1, `vggt` Fig.1 caption, `var` sample grid, `visprog` pipeline | Side-by-side *old vs new*, or one grid that is the result |
| Architecture | `swin`, `uniad`, `var` Fig.2/4 | Hierarchical blocks; one contrasting baseline drawing |
| Qualitative grid | `var`, `generative-image-dynamics`, `brickgpt`, `videopoet` | Consistent size, aligned rows, failure/edit as extra row |
| Quantitative / scaling | `var` scaling, `emergent-mirage` metric plots, `never-train-from-scratch` | Same axes for rival methods; make the crossing obvious |
| Observe → explain → fix | `vit-registers`, `shallow-safety`, `train-for-the-worst` | Before/after maps or a schematic of the shortcut |
| Protocol / human study | `llm-debate`, `richhf` | Who sees what, in what order |
| Algorithm / complexity | `stde`, `privacy-auditing`, `sedd` | Display the *cost* being killed, not clipart networks |

## By user paper type

| User's paper | Default trio |
|---|---|
| New backbone / architecture | `swin`, `vggt`, `var` |
| New system that unifies modules | `uniad`, `visprog`, `videopoet` |
| Simple fix after an observation | `vit-registers`, `train-for-the-worst`, `never-train-from-scratch` |
| “The community measured it wrong” | `emergent-mirage`, `never-train-from-scratch`, `llm-debate` |
| Generative model | `var`, `sedd`, `sd3-rectified-flow`, `generative-image-dynamics` |
| Safety / alignment | `shallow-safety`, `llm-finetuning-dynamics`, `llm-debate` |
| Dataset release | `richhf`, `brickgpt` |
| Theory with a practical algorithm | `stde`, `privacy-auditing`, `sedd` |

## Contrast ids (always include one)

Use a paper *unlike* the user's draft so you do not clone one venue voice:

- If the user writes a method paper, also read `emergent-mirage` or `never-train-from-scratch`.
- If the user writes an analysis paper, also read `swin` or `var` for how claims are packaged.
- If the user writes a system paper, also read `vit-registers` for how little you can get away with.
