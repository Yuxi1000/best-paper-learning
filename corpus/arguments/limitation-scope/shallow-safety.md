# Safety Alignment Should Be Made More Than Just a Few Tokens Deep

- id: `shallow-safety`
- award: ICLR 2025 Outstanding Paper
- section_bucket: limitation-scope
- source: arXiv:2406.05946

## Excerpt (truncated; study the move, do not copy)

Our work identifies a shortcut that current safety alignment strategies appear to exploit: that alignment only needs to change the generative distribution of the first few tokens. We show that this may be a key component of many downstream vulnerabilities. We then provide two initial strategies to address this: (1) a data augmentation approach that can increase depth of alignment; (2) a constrained optimization objective that can help mitigate finetuning attacks by constraining updates on initial tokens. Future work can explore additional approaches grounded in control theory and safe reinforcement learning. The methods we describe here may not be a perfect defense and may be subject to some future adaptive attacks, but they are an initial step for improving robustness and further demonstrate how much improvement there can be over current approaches. Fundamentally, our results are primarily to support our argument that future safety alignment should be made more than just a few tokens deep. Broader Impacts and Ethics Statement Our work explicitly ties failure modes of safety alignment to potential shortcuts that can be taken by alignment methods and advocates for, and provides a path forward for, deeper alignment approaches that will improve safety more broadly. While a deeper understanding of the failures of alignment may result in increased ability to jailbreak models, we…
