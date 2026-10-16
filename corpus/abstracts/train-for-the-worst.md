# Train for the Worst, Plan for the Best: Understanding Token Ordering in Masked Diffusions

- id: `train-for-the-worst`
- award: ICML 2025 Outstanding Paper
- venue: ICML 2025
- arXiv: [2502.06768](https://arxiv.org/abs/2502.06768)
- authors: Jaeyeon Kim, Kulin Shah, Vasilis Kontonis, Sham Kakade, Sitan Chen
- posted: 2025-02-10
- license: see arXiv page
- paper_type: analysis-theory
- use_for: train-test-mismatch, theory-plus-simple-fix, headline-jump

## Abstract

In recent years, masked diffusion models (MDMs) have emerged as a promising alternative approach for generative modeling over discrete domains. Compared to autoregressive models (ARMs), MDMs trade off complexity at training time with flexibility at inference time. At training time, they must learn to solve an exponentially large number of infilling problems, but at inference time, they can decode tokens in essentially arbitrary order. In this work, we closely examine these two competing effects. On the training front, we theoretically and empirically demonstrate that MDMs indeed train on computationally intractable subproblems compared to their autoregressive counterparts. On the inference front, we show that a suitable strategy for adaptively choosing the token decoding order significantly enhances the capabilities of MDMs, allowing them to sidestep hard subproblems. On logic puzzles like Sudoku, we show that adaptive inference can boost solving accuracy in pretrained MDMs from $<7$% to $\approx 90$%, even outperforming ARMs with $7\times$ as many parameters and that were explicitly trained via teacher forcing to learn the right order of decoding.
