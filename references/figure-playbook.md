# Figure playbook

Study **layout grammar**. Do not reuse a paper's pixels, samples, or icons.

When raster crops look like random photos, they are usually sub-images inside a composite. Use `corpus/figures/page-renders/` and the caption in `corpus/style-cards/` instead.

## What a best-paper figure is for

Every figure has one job: make a claim inevitable. If the caption could be “illustration of our method”, the figure is not done.

Caption formula: **result + comparison + condition**.

- Swin Fig.1: hierarchical maps with linear cost vs ViT's single-scale quadratic maps.
- VAR Fig.1: samples *are* the claim (AR can look like this).
- ViT registers: artifact maps disappear after adding tokens.
- Emergent-mirage: the same model family looks “emergent” or smooth depending on the metric.

## Genre recipes

### Teaser (page 1)

Two winning templates in this corpus:

1. **Old vs new schematic** (`swin` Fig.1). Same visual language on left and right; the difference *is* the contribution. Tiny annotations: `4× / 8× / 16×`, `linear`, `quadratic`.
2. **Result grid** (`var`). No architecture. Density and alignment do the talking. Optional extra row for zero-shot edits.

Do not put a giant 3D logo over a blurry photo. If you show a scene (`vggt`), overlay the predicted geometry so the overlay is the claim.

### Architecture

- Left-to-right or top-down data flow, not a hairball.
- One contrasting baseline drawn in the same style (`swin` (a) vs (b), `var` AR vs VAR).
- Repeat a small motif (window, query, scale) so the reader can count it.
- Hide training trivia; keep tensor names that appear in equations.

### Qualitative grid

- Same crop size, same background, consistent font inside labels.
- Rows = methods or conditions; columns = examples.
- Put the failure or the *hard* case in a dedicated row (`var` edits, `brickgpt` unstable vs rolled-back).
- Never cherry-pick without a nearby quantitative companion.

### Quantitative / scaling

- Shared axes across methods. Make the crossing or slope the focal point (`var` scaling laws, r ≈ −0.998).
- `emergent-mirage`: two panels, identical x (scale), different y (metric). The figure *is* the argument.
- Annotate the number in the plot, not only in the text.
- Error bars or multiple seeds when the paper's claim is a protocol (`never-train-from-scratch`, `llm-debate`).

### Observe → explain → fix

Use for analysis papers (`vit-registers`, `shallow-safety`, `train-for-the-worst`):

1. Panel of the raw pathology (high-norm tokens, first-token refusal, random unmasking).
2. Schematic of the hypothesized mechanism.
3. After the cheap intervention.

The middle panel is what makes it a paper rather than a bugfix.

### Appendix extras

Appendix figures are denser and less pretty than Fig.1:

- Extra samples: same grid language as the main qualitative figure (`visprog`, `videopoet`)
- Extra ablations: small multiples, not a new architecture drawing (`sedd`, `sd3-rectified-flow`)
- Implementation: prompt box, robot/setup photo, interface screenshot (`brickgpt`, `llm-debate`)

Look at `corpus/figures/appendix/<id>/` page renders. Do not promote appendix clutter onto page 1.

### Protocol

`llm-debate` and `richhf`: draw *who sees what*. Boxes for human, debater, judge; arrows for information hiding. If a control condition exists, give it its own row.

## Color and type

- 2–3 hues plus gray. Color encodes the *variable* (ours vs baseline, scale, metric class), not decoration.
- Colorblind-safe pairs. Do not rely on red/green alone.
- Line weights like a NeurIPS line plot, not a slide gradient.
- Helvetica/Times labels; no clip-art 3D arrows.

## Figure spec template

Fill this before drawing:

```
Claim:
Genre:
Borrowed layout from: <paper id, figure>
Panels:
  (a) proves ...
  (b) proves ...
Labels / units:
What a reader must see in 5 seconds:
Caption:
```

## Agent drawing rules

- Propose the spec in markdown first.
- For architecture, Mermaid or a clean SVG is enough for a draft; say what a designer must keep.
- For qualitative results, ask the user for *their* samples; do not hallucinate other papers' images.
- If using an image generator, generate **schematics and plots**, not fake natural photos presented as experiments.
- After drawing, reread the caption. If it does not mention a comparison or a number, rewrite it.

## Common failures

- Architecture figure that restates the text without a contrast panel
- Teaser that is a collage of unrelated pretty pictures
- Plot with four methods but no visual hierarchy for “ours”
- Caption that starts with “An overview of”
- Inheriting a paper's sample grid into the user's PDF
