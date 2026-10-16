# Appendix/datasets-protocol: Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution

- id: `sedd`
- source: arXiv:2310.16834

## C.6. Likelihood Evaluation Details

We randomly sample with 1000 timesteps to Monte Carlo estimate our likelihoods. We use invertible tokenizers, as is customary for GPT-2 experiments. We report results on the test set for all datasets besides WikiText02, where we report on the train set since WikiText02 and WikiText103 share the same test set.
