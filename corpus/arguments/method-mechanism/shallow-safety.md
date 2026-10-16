# Safety Alignment Should Be Made More Than Just a Few Tokens Deep

- id: `shallow-safety`
- award: ICLR 2025 Outstanding Paper
- section_bucket: method-mechanism
- source: arXiv:2406.05946

## Excerpt (truncated; study the move, do not copy)

against the text-davinci-003 model (the default reference baseline for AlpacaEval). The augmented fine-tuned model achieves a winrate of 49.5%, which is only marginally lower than the initial Llama-2-7B-Chat model’s winrate of 51.8%.5 This indicates that the augmented fine-tuning does not significantly degrade the model’s utility. 3.2 The Deepened Safety Alignment Shows Improved Robustness Against Multiple Exploits A central argument in this work is that the shallow safety alignment can be a source of many safety vulnerabilities in LLMs. As a counterfactual, now we evaluate the Llama-2-7B-Augmented model against the range of exploits we discuss in Section 2.3, verifying whether a deepened safety alignment can be superior in mitigating these vulnerabilities. Improved Robustness against Multiple Inference-time Exploits. We test the prefilling attack (using the Harmful HEx-PHI dataset we built in Section 2), GCG attack [29], and the decoding parameters 4We note that there are ties to ensuring sufficient exploration in reinfocement learning that we do not explore formally here, but leave to future work. 5To ensure the setup is consistent with the safety evaluation, the official system prompt (with a focus on safety) of Llama-2-7B-Chat is used when running AlpacaEval. Therefore, the win rates here can be generally lower than the numbers in official Alpaca leaderboard in which the…
