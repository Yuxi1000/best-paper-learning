# Privacy Auditing with One (1) Training Run

- id: `privacy-auditing`
- award: NeurIPS 2023 Outstanding Paper
- section_bucket: experiment-result
- source: arXiv:2305.08846

## Excerpt (truncated; study the move, do not copy)

Theoretical m=5000 m=1000 m=100 m=50 m=10 Figure 4: Eﬀect of the number of auditing examples (m) in the white-box setting. By increasing the number of the auditing examples we are able to achieve tighter 0 1 2 3 4 5 6 Theoretical Epsilon 0 1 2 3 4 5 6 Theoretical n m = 0 n m = 103 n m = 104 Figure 5: Eﬀect of the number of additional examples (n −m) in the white-box setting. Importantly, adding additional examples does not impact the auditing results in the white-box setting. proposed – the “Dirac canary” approach – which sets all gradients to zero except at a single random index. In our setting where we need to create multiple auditing examples (canaries) we make sure the indices selected in our experiments do not have any repetitions. To compute the score for gradient space attacks, we use the dot product between the gradient update and auditing gradient. When auditing in input space, we leverage two diﬀerent types of injected examples as: 1. Mislabeled example: We select a random subset of the test set and randomly relabel them (ensuring the new label is not the same as the original label). 2. In-distribution example: We select a random subset of the test set. For input space audits, we use the loss of the input example as the score. In our experiments we report the attack with the highest lower bound. In our experiments, we evaluate diﬀerent values of k+ and k−and only…
