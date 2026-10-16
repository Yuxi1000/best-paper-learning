# Train for the Worst, Plan for the Best: Understanding Token Ordering in Masked Diffusions

- id: `train-for-the-worst`
- award: ICML 2025 Outstanding Paper
- section_bucket: experiment-result
- source: arXiv:2502.06768

## Excerpt (truncated; study the move, do not copy)

from Section 3.2. Since we do not have access to the Bayes-optimal predictor, we use the metric Ex0∼pdata hPL−1 i=0 log pθ  xπ(i) 0 x0[π{i, . . . , L −1}] i . This captures the accumulation of error across subproblems pθ  xπ(i) 0 x0[π{i, . . . , L −1}]  , since pθ(x0|x0[M]) = pdata(x0|x0[M]) minimizes this metric. Fig. 2 shows a clear gap between different subproblems. The theoretical and empirical evidence demonstrates that MDMs perform better in estimating pθ(x0|x0[M]) for some subproblems M than for others. We therefore want to avoid encountering hard subproblems M at inference time. In the next section, we show that while vanilla MDM inference can run into such subproblems, simple modifications at the inference stage can effectively circumvent these issues, resulting in dramatic, training-free performance improvements. 4. MDMs can plan around hard problems We previously argued that due to the complex nature of masking subproblems, MDM must perform poorly on certain ones pθ(xi|xt). Therefore, during vanilla MDM inference, MDM inevitably encounters such difficult subproblems at Step (b). While this might suggest that we need to fundamentally revisit how MDMs are trained, in this section we show that, surprisingly, simple modifications at the inference stage—without any further training—can sidestep these issues and lead to significant performance improvements. MDM offers…
