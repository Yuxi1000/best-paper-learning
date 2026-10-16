# Stochastic Taylor Derivative Estimator: Efficient Amortization for Arbitrary Differential Operators

- id: `stde`
- award: NeurIPS 2024 Best Paper
- section_bucket: limitation-scope
- source: arXiv:2412.00088

## Excerpt (truncated; study the move, do not copy)

We introduce STDE, a general method for constructing stochastic estimators for arbitrary differential operators that can be evaluated efficiently via Taylor mode AD. We evaluated STDE on PINNs, an instance of the optimization problem where the loss contains differential operators. Amortization with STDE outperforms the baseline methods, and STDE also applies to a wider class of problems as it can be applied to arbitrary differential operators. Applicability Besides PINNs, STDE can be applied to arbitrarily high-order and high-dimensional AD-based PDE solvers. This makes STDE more general than a branch of related methods. STDE is also more applicable than deep ritz method [41], weak adversarial network (WAN) [43], backward SDE-based solvers [3, 34, 10], deep Galerkin method [35], and the recently proposed forward Laplacian [24], which are all restricted to specific forms of second-order PDEs. STDE applies naturally to differential operators in PDEs, but it can also be applied to other problems that require input gradients. For example, adversarial attacks, feature attribution, and meta-learning, to name a few. Limitations Being a general method, STDE forgoes the optimization possibilities that apply to specific operators. Furthermore, we did not consider variance reduction techniques that could be applied, which can be explored in future works. Also, we observed that lowering…
