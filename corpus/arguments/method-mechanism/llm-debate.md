# Debating with More Persuasive LLMs Leads to More Truthful Answers

- id: `llm-debate`
- award: ICML 2024 Best Paper
- section_bucket: method-mechanism
- source: arXiv:2402.06782

## Excerpt (truncated; study the move, do not copy)

then grades these and the most helpful is used to refine the answer. For all preference models, we use the log probabilities from GPT-4-Turbo. We document prompt iteration in Appendix D.3 and learning with examples in Appendix A.9. For LLM judging, we used GPT-4-Turbo, Mixtral-8x7B, GPT-3.5-Turbo and Claude 2.1. Prompts are provided in Appendix G.2. Similar to Zheng et al. (2023), we found strong biases with LLM judges. To mitigate positional biases, we run judgements over each debate twice - once with the original transcript and once with the debater order swapped. To mitigate verbosity biases, we apply strict word limits. We document judge biases in Appendix A.7 and mitigation techniques in Appendix D.6. Cross-play tournament — To investigate how debate scales with model capabilities, we require a way to compare debaters. We run cross-play debates, in which different debaters argue against one another. To compare a large set of debaters, we use a tournament to generate informative matches. For n debaters, it is not feasible to run all possible matches as this requires O(n2) matches. Instead, we use a Swiss-style tournament to decide matches, which produces rankings in O(n log n) matches (see Appendix D.4). Human judges — We recruit 30 human judges via the referral-based annotator platform Pareto.2 Annotators judge debates via a web interface in which they are presented with…
