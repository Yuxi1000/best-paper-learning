# Safety Alignment Should Be Made More Than Just a Few Tokens Deep

- id: `shallow-safety`
- award: ICLR 2025 Outstanding Paper
- section_bucket: related-work
- source: arXiv:2406.05946

## Excerpt (truncated; study the move, do not copy)

Safety & Alignment. A large body of work has examined improved methods for alignment [16, 39, 19, 45, 14, 5, 31]. While we tie alignment approaches to potential downstream jailbreaks, we do so mainly be examining aligned artifacts which go through more rigorous alignment procedures than most other open source models. We rely on the Gemma [31] and Llama-2 [5] base and aligned models throughout this work, as the safety alignment built in these two models are closest to the technology applied in frontier proprietary models. Jailbreaking Methods. A large body of work has examined methods for jailbreaking aligned LLMs, including leveraging finetuning, decoding strategies, prefilling strategies, optimization strategies, and even persuasion [21, 29, 22, 24, 46, 23, 47, 48, 30, 17]. Many approaches try to handle jailbreaking through a systems approach by monitoring inputs and outputs with machine learning models [49], but this is only as good as the monitoring mechanism (which can also be jailbroken) [50]. Superficial Alignment Hypothesis and Per-token Effects of Alignment Fine-tuning. Our work is closely related to the Superficial Alignment Hypothesis (SAH) [28], which posits that the alignment process for current LLMs only superficially changes the formats of inputs and outputs to be used for interacting with the users. Besides, there are also some earlier works noting asymmetries…
