# Appendix/proofs: Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution

- id: `sedd`
- source: arXiv:2310.16834

## A. Proof of Main Results

Proof of Prop 3.2. Given infinite samples, the loss becomes equivalent to minimizing min θ X x,y̸=x p(x)wxy  sθ(x)y −p(y) p(x) log sθ(x)y  (23) where we have removed constants not depending on θ. This is minimized when sθ(x)y −p(y) p(x) log sθ(x)y (24) is minimized for all x, y. Taking a derivative with respect to s and setting to 0, we see that this occurs when sθ(x)y = p(y) p(x), which can be easily checked to be optimal as the function is convex as a function of s. One can check that the loss is 0 at the minimum. Proof of Prop 3.3. The trick is the categorical equivalent of the divergence theorem. In particular, we have Ex∼p X y̸=x p(y) p(x)f(x, y) = X x,y:x̸=y p(y) p(x)p(x)f(x, y) = X x,y:x̸=y p(y)f(x, y) = Ey∼p X x̸=y f(x, y) = Ex∼p X y̸=x f(y, x) for abitrary f. By setting f(x, y) = wxy log sθ(x)y, we get that Ex∼p  X y̸=x wxy  sθ(x)y −p(y) p(x) log sθ(x)y + K p(y) p(x)   = Ex∼p  X y̸=x wxysθ(x)y −wyx log sθ(y)x + wxyK p(y) p(x)   which is the desired equivalent (as the last term does not depend on θ). Proof of Thm 3.4. This is similar to the same denoising variant for concrete score matching. We just need to show that the log sθ(xt)y pt(y) pt(x) marginalizes…
