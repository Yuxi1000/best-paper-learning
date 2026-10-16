# Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution

- id: `sedd`
- award: ICML 2024 Best Paper
- section_bucket: method-mechanism
- source: arXiv:2310.16834

## Excerpt (truncated; study the move, do not copy)

LAMBADA WikiText2 PTB WikiText103 1BW Small GPT-2 45.04 42.43 138.43 41.60 75.20 SEDD Absorb ≤50.92 ≤41.84 ≤114.24 ≤40.62 ≤79.29 SEDD Uniform ≤65.40 ≤50.27 ≤140.12 ≤49.60 ≤101.37 D3PM ≤93.47 ≤77.28 ≤200.82 ≤75.16 ≤138.92 PLAID ≤57.28 ≤51.80 ≤142.60 ≤50.86 ≤91.12 Medium GPT-2 35.66 31.80 123.14 31.39 55.72 SEDD Absorb ≤42.77 ≤31.04 ≤87.12 ≤29.98 ≤61.19 SEDD Uniform ≤51.28 ≤38.93 ≤102.28 ≤36.81 ≤79.12 Table 1: Zero-shot unconditional perplexity (↓) on a variety of datasets. For a fixed size, the best perplexity is bolded. Our SEDD model with absorbing transition beats GPT-2 (Radford et al., 2019) on a majority of the tasks and entirely outperforms prior language diffusion models (Austin et al., 2021; Gulrajani & Hashimoto, 2023). Type BPC (↓) Autoregressive Backbone IAF/SCF 1.88 AR Argmax Flow 1.39 Discrete Flow 1.23 Autoregressive 1.23 Non-autoregressive Mult. Diffusion ≤1.72 MAC ≤1.40 BFN ≤1.41 D3PM Uniform ≤1.61 D3PM Absorb ≤1.45 Ours (NAR) SEDD Uniform ≤1.47 SEDD Absorb ≤1.39 Table 2: Bits Per Character on text8. Our SEDD models achieve second-best overall result (best for nonautoregressive), only being beaten out by the autoregressive model as a backbone) by a small margin. SEDD also substantially improves upon prior the discrete diffusion model D3PM (Austin et al., 2021). incorporates an autoregressive base distribution) (Tran et al., 2019). Furthermore, SEDD substantially…
