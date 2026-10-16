# Appendix: Are Emergent Abilities of Large Language Models a Mirage?

- id: `emergent-mirage`
- award: NeurIPS 2023 Outstanding Paper
- arXiv: 2304.15004
- appendix_present: true
- start_page: 12
- appendix_pages: 3
- detection: override
- genres: proofs

## Table of contents

- `A` Appendix (opening) — *proofs* (p.12)

## Excerpts (study the move, do not copy)

### A. Appendix (opening)

- genre: `proofs`
- start_page: 12

A Approximate Behavior of Metrics on Sequential Data How do different metrics behave when used to measure autoregressive model outputs? Precisely answering this question is tricky and possibly analytically unsolvable, so we provide an approximate answer here. Notationally, we consider N test data of length L (here, length is measured in tokens) with tar- gets denoted tn def =(tn1, tn2, ...tnL), the autoregressive model has a true-but-unknown per-token er- ror probability of ϵ ∈[0, 1] and the model outputs prediction ˆtn def =(ˆtn1, ˆtn2, ...ˆtnL). This assumes that the model’s per-token error probability is constant, which is empirically false, but modeling the complex dependencies of errors is beyond our scope. A.1 Per-Token Error Probability is Resolution-Limited Note that because we have N test data, each of length L, our resolution for viewing the per-token error probability ϵ is limited by 1/NL. Here, resolution refers to “the smallest interval measurable by a scientiﬁc instrument; the resolving power.” To explain what resolution means via an example, suppose one wants to measure a coin’s probability of yielding heads. After a single coin ﬂip, only two outcomes are possible…

## Page renders

- `figures/appendix/emergent-mirage/page-12.png`
- `figures/appendix/emergent-mirage/page-13.png`
- `figures/appendix/emergent-mirage/page-14.png`
