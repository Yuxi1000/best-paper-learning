# Examples

## 1. User: 帮我写 abstract

Do:

1. Classify as `abstract` + guessed paper type from their notes.
2. Pick e.g. `var`, `swin`, `vit-registers` (or analysis trio if it is a science paper).
3. Read those abstracts and paper-notes.
4. Start with `## Studied`.
5. Write an original abstract in the user's claim language.

Do not paste VAR's FID sentence with the numbers swapped.

## 2. User: 给 method 画一张架构图

Do:

1. Task = `figure` / architecture.
2. Open `swin` page-render p.1 and `var` conceptual AR vs VAR notes.
3. Write a figure spec (claim, panels, caption).
4. Then draw a **new** diagram of the user's method, with an old-vs-new panel if possible.

Do not regenerate Swin's window illustration.

## 3. User: 改这段 intro

Do:

1. Task = `review-existing-draft` + `intro`.
2. Pick `uniad` or `never-train-from-scratch` if they are reframing a goal/protocol; `shallow-safety` if they unify failure modes.
3. Quote the user's bottleneck sentence, then rewrite 1–3 paragraphs.
4. List evidence the intro now promises that the rest of the paper must pay.

## 4. User: 帮我写 appendix / 补充实验 / 超参

Do:

1. Task = `appendix`. Read `corpus/arguments/appendix/INDEX.md`.
2. Default trio: `brickgpt` (implementation + limitations), `visprog` (contents list + prompts), `sedd` or `train-for-the-worst` (proofs / extra experiments).
3. Ask which buckets are needed: proofs, extra-experiments, hyperparams, protocol, failures, extra qualitative.
4. Every appendix subsection must be citeable from the main text.

Do not dump uncited hyperparameter sweeps.

## 5. User: 我这篇是分析论文，结论偏负向

Default trio: `emergent-mirage`, `never-train-from-scratch`, `train-for-the-worst`.
Keep the negative claim sharp. Do not dress it up as a new module.
