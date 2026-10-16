# Appendix/proofs: Privacy Auditing with One (1) Training Run

- id: `privacy-auditing`
- source: arXiv:2305.08846

## A. Appendix (opening)

where f(v) := P ˇ W←Binomial(r, eε eε+1)  ˇW ≥v  . Now we delve into the proof of Theorem 5.2. We use a decomposition result of Kairouz, Oh, and Viswanath [KOV15] (see also [MV15] & [Ste22, Corollary 24]). Lemma 5.5. Let P and Q be probability distributions over Y. Fix ε, δ ≥0. Suppose that, for all measurable S ⊂Y, we have P(S) ≤eε · Q(S) + δ and Q(S) ≤eεP(S) + δ. Then there exist δ′ ∈[0, δ] and distributions P ′, Q′, P ′′, and Q′′ over Y such that the following three properties are all satisﬁed. First, we can express P and Q as convex combi- nations: P = (1 −δ′)P ′ + δ′P ′′, Q = (1 −δ′)Q′ + δ′Q′′. Second, for all measurable S ⊂Y, we have e−εP ′(S) ≤Q′(S) ≤eεP ′(S). Third, there exist measurable S, T ⊂Y such that P ′′(S) = 1, Q′′(T) = 1, ∀S′ ⊂S P(S′) ≥Q(S′), and ∀T ′ ⊂T Q(T ′) ≥P(T ′). Proof. This proof follows that of Steinke [Ste22]. We begin with some formalities: Fix some base measure such that P and Q are absolutely continuous with respect to the base measure. (If P and Q are discrete distributions, this can be the counting measure. If they are continuous distributions, this can be the Lebesgue measure. In general, P + Q serves as such a measure.) For y ∈Y, let P(y) and…
