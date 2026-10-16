# Stochastic Taylor Derivative Estimator: Efficient Amortization for Arbitrary Differential Operators

- id: `stde`
- award: NeurIPS 2024 Best Paper
- section_bucket: problem-framing
- source: arXiv:2412.00088

## Excerpt (truncated; study the move, do not copy)

Stochastic Taylor Derivative Estimator: Efficient amortization for arbitrary differential operators Zekun Shi National University of Singapore Sea AI Lab shizk@sea.com, Zheyuan Hu National University of Singapore e0792494@u.nus.edu, Min Lin Sea AI Lab linmin@sea.com, Kenji Kawaguchi National University of Singapore kenji@nus.edu.sg Abstract Optimizing neural networks with loss that contain high-dimensional and high-order differential operators is expensive to evaluate with back-propagation due to O(dk) scaling of the derivative tensor size and the O(2k−1L) scaling in the computation graph, where d is the dimension of the domain, L is the number of ops in the forward computation graph, and k is the derivative order. In previous works, the polynomial scaling in d was addressed by amortizing the computation over the optimization process via randomization. Separately, the exponential scaling in k for univariate functions (d = 1) was addressed with high-order auto-differentiation (AD). In this work, we show how to efficiently perform arbitrary contraction of the derivative tensor of arbitrary order for multivariate functions, by properly constructing the input tangents to univariate high-order AD, which can be used to efficiently randomize any differential operator. When applied to Physics-Informed Neural Networks (PINNs), our method provides >1000× speed-up and >30× memory…
