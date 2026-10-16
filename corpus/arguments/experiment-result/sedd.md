# Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution

- id: `sedd`
- award: ICML 2024 Best Paper
- section_bucket: experiment-result
- source: arXiv:2310.16834

## Excerpt (truncated; study the move, do not copy)

Mean Prediction. Instead of directly parameterizing the ratios pt(y) pt(x), Austin et al. (2021); Campbell et al. (2022) instead follow a strategy of Ho et al. (2020) to learn the reverse density p0|t. This actually recovers the ratios pt(y) pt(x) in a roundabout way (as shown in our Theorem 4.2), but comes with several drawbacks. First, learning p0|t is inherently harder since it is a density (as opposed to a general value). Furthermore, the objective breaks down in continuous time and must be approximated (Campbell et al., 2022). As a Ratio Matching. Originally introduced in Hyv¨arinen (2007) and augmented in Sun et al. (2023), ratio matching learns the marginal probabilities of each dimension with maximum likelihood training. However, the resulting setup departs from standard score matching and requires specialized and expensive network architectures (Chen & Duvenaud, 2019). As such, this tends to perform worse than mean prediction. Concrete Score Matching. Meng et al. (2022) generalizes the standard Fisher divergence in score matching, learning sθ(x, t) ≈ h pt(y) pt(x) i y̸=x with concrete score matching: LCSM = 1 2Ex∼pt  X y̸=x  sθ(xt, t)y −pt(y) pt(x) 2   (4) Unfortunately, the ℓ2 loss is incompatible with the fact that pt(y) pt(x) must be positive. In particular, this does not sufficiently penalize negative or zero values, leading to divergent behavior. Although…
