# Appendix/other: Stochastic Taylor Derivative Estimator: Efficient Amortization for Arbitrary Differential Operators

- id: `stde`
- source: arXiv:2412.00088

## f. and its Jacobian Jf is closed under composition:

(f, Jf) ◦(g, Jg) = (f ◦g, Jf◦g), Jf◦g(t) = Jf(g(t))Jg(t) (26) where ◦denotes both function composition and the composition of the tuple (f, Jf). If we have the analytical formula of the Jacobian Jf for every f ∈L, then we can calculate the Jacobian of any composition of functions from L using the above composition rule for the tuple (f, Jf). The set L of functions are usually called the primitives. B.3 Fréchet derivative and linearization Given normed vector spaces V, W, the Fréchet derivative ∂f of a function f : V →W is a map from V to the space of all bounded linear operators from V to W, denoted as L(V, W), that is ∂f : V →L(V, W), (27) such that at a point a ∈V it gives the best linear approximation ∂f(a)(·) of f, in the sense that lim ∥h∥→0 ∥f(a + h) −f(a) −∂f(a)(h)∥W ∥h∥V = 0 (28) Therefore, it is also called the linearization of f at point a. Concretely, consider a function in Euclidean spaces f : Rn →Rm. At any point a ∈Rn, the Fréchet derivative ∂f can be seen as the directional derivative of f: ∂f : Rn →L(Rn, Rm), ∂f(a)(v) = Jf(a)v (29) where Jf(a) ∈Rm×n denote the Jacobian of f at point a called the primal, and v ∈Rn, also called the tangent is a vector representing…
