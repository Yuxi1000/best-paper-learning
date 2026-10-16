# Safety Alignment Should Be Made More Than Just a Few Tokens Deep

- id: `shallow-safety`
- award: ICLR 2025 Outstanding Paper
- section_bucket: problem-framing
- source: arXiv:2406.05946

## Excerpt (truncated; study the move, do not copy)

Safety Alignment Should Be Made More Than Just a Few Tokens Deep Xiangyu Qi Princeton University xiangyuqi@princeton.edu Ashwinee Panda Princeton University ashwinee@princeton.edu Kaifeng Lyu Princeton University klyu@cs.princeton.edu Xiao Ma Google DeepMind xmaa@google.com Subhrajit Roy Google DeepMind subhrajitroy@google.com Ahmad Beirami Google DeepMind beirami@google.com Prateek Mittal Princeton University pmittal@princeton.edu Peter Henderson Princeton University peter.henderson@princeton.edu Abstract The safety alignment of current Large Language Models (LLMs) is vulnerable. Relatively simple attacks, or even benign fine-tuning, can jailbreak aligned models. We argue that many of these vulnerabilities are related to a shared underlying issue: safety alignment can take shortcuts, wherein the alignment adapts a model’s generative distribution primarily over only its very first few output tokens. We refer to this issue as shallow safety alignment. In this paper, we present case studies to explain why shallow safety alignment can exist and provide evidence that current aligned LLMs are subject to this issue. We also show how these findings help explain multiple recently discovered vulnerabilities in LLMs, including the susceptibility to adversarial suffix attacks, prefilling attacks, decoding parameter attacks, and fine-tuning attacks. Importantly, we discuss how this…
