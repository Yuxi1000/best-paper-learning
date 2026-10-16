# Privacy Auditing with One (1) Training Run

- id: `privacy-auditing`
- award: NeurIPS 2023 Outstanding Paper
- section_bucket: related-work
- source: arXiv:2305.08846

## Excerpt (truncated; study the move, do not copy)

The goal of privacy auditing is to empirically estimate the privacy provided by an algorithm, typically to accompany a formal privacy guarantee. Early work on auditing has often been 4 motivated by trying to identify bugs in the implementations of diﬀerentially private data analysis algorithms [DWWZK18; BGDCTV18]. Techniques for auditing diﬀerentially private machine learning typically rely on conducting some form of membership inference attack [SSSS17];2 these attacks are designed to detect the presence or absence of an individual example in the training set. Essentially, a membership inference attack which achieves some true positive rate (TPR) and false positive rate (FPR) gives a lower bound on the privacy parameter ε ≥loge(TPR/FPR) (after ensuring statistical validity of the TPR and FPR estimates). Jayaraman and Evans [JE19] use standard membership inference attacks to evaluate different privacy analysis algorithms. Jagielski, Ullman, and Oprea [JUO20] consider inferring membership of worst-case “poisoning” examples to conduct stronger membership inference attacks and understand the tightness of privacy analysis. Nasr, Song, Thakurta, Papernot, and Carlini [NSTPC21] measure the tightness of privacy analysis under a variety of threat models, including showing that the DP-SGD analysis is tight in the threat model assumed by the standard DP-SGD analysis. Improvements to…
