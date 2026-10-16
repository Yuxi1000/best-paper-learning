# Are Emergent Abilities of Large Language Models a Mirage?

- id: `emergent-mirage`
- award: NeurIPS 2023 Outstanding Paper
- section_bucket: method-mechanism
- source: arXiv:2304.15004

## Excerpt (truncated; study the move, do not copy)

0.0 0.2 0.4 0.6 0.8 1.0 Multiple Choice Grade Num. Choices 2 D 109 1010 1011 0.3 0.4 0.5 0.6 0.7 Multiple Choice Grade Published Emergent Ability 109 1010 1011 0.0 0.2 0.4 0.6 0.8 1.0 Accuracy Target Str Len 5 109 1010 1011 0.0 0.2 0.4 0.6 0.8 1.0 Accuracy Published Emergent Ability C 109 1010 1011 10 1 100 CE (Per-Token) A 109 1010 1011 0.0 0.2 0.4 0.6 0.8 1.0 Prob Correct (Per-Token) B Emergent Abilities No Emergent Abilities Discontinuously score LLM outputs 109 1010 1011 4 3 2 1 0 - Number of Incorrect Tokens Target Str Len 5 E Nonlinearly score LLM outputs Continuously score LLM outputs Linearly score LLM outputs 109 1010 1011 0.8 0.6 0.4 0.2 0.0 - Brier Score Num. Choices 2 F Figure 2: Emergent abilities of large language models are created by the researcher’s chosen metrics, not unpredictable changes in model behavior with scale. (A) Suppose the per-token cross-entropy loss decreases monotonically with model scale, e.g., LCE scales as a power law. (B) The per-token probability of selecting the correct token asymptotes towards 1. (C) If the researcher scores models’ outputs using a nonlinear metric such as Accuracy (which requires a sequence of tokens to all be correct), the metric choice nonlinearly scales performance, causing performance to change sharply and unpredictably in a manner that qualitatively matches published emergent abilities (inset). (D) If the…
