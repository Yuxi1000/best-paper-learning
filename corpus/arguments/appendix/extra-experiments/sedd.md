# Appendix/extra-experiments: Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution

- id: `sedd`
- source: arXiv:2310.16834

## D.1. Ablation of Concrete Score Matching

We also ablated the concrete score matching objective from (Meng et al., 2021) for the GPT-2 scale experiments. This was done by simply replacing the score entropy term with the corresponding ℓ2 based loss (in particular keeping the scaling by Qt(x, y)). In general, we found that this did not train well, resulting in 3 −4× higher likelihood loss, which corresponds to 10,000× higher perplexity. Similarly, 17 Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution
