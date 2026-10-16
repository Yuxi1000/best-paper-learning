# Stochastic Taylor Derivative Estimator: Efficient Amortization for Arbitrary Differential Operators

- id: `stde`
- award: NeurIPS 2024 Best Paper
- section_bucket: method-mechanism
- source: arXiv:2412.00088

## Excerpt (truncated; study the move, do not copy)

From the previous discussion, it is clear that the exponential scaling in k for the problem described in Eq. 1 cannot be mitigated by amortization alone. Although high-order AD methods like Taylor mode AD [6] can address this scaling issue, it is only defined for univariate functions. In this section, we describe a method that addresses the scaling issue in k and d simultaneously when amortizing Eq. 1 by seeing univariate Taylor mode AD as contractions of multivariate derivative tensor. 4.1 Univariate Taylor mode AD as contractions of multivariate derivative tensor dF projects the Jacobian of F to Rd′ with a 1-jet Jg(t). Similarly, dkF contracts a set of derivative tensors to Rd′ with a k-jet Jk g . We can expand ∂k ∂tk F ◦g with Eq. 43 to see the form of the contractions. For example, ∂F is JVP, and ∂2F contains a quadratic form of the Hessian D2 F : ∂2F(a)(v(1), v(2)) = ∂2 ∂t2 [F ◦g](t) = DF (a)v(2) + D2 F (a)d′,d1,d2v(1) d1 v(1) d2 . (9) From Eq. 43, one can always find a Jl g with large enough l ≥k such that there exists k ≤l′ ≤l with ∂l′F(Jl′ g ) = Dk F (a) · ⊗k i=1v(vi) where vi ∈[1, k], by setting some tangents v(vi) to the zero vector. That is, arbitrary derivative tensor contraction is contained within a Fréchet derivative of high-order, which can be efficiently evaluated through Taylor mode AD. How large l should be depends on how off-diagonal the operator is. If the…
