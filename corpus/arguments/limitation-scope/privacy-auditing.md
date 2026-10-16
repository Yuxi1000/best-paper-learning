# Privacy Auditing with One (1) Training Run

- id: `privacy-auditing`
- award: NeurIPS 2023 Outstanding Paper
- section_bucket: limitation-scope
- source: arXiv:2305.08846

## Excerpt (truncated; study the move, do not copy)

Our main contribution is showing that we can audit the diﬀerential privacy guarantees of an algorithm with a single run. In contrast, prior methods require hundreds – if not thousands – of runs, which is computationally prohibitive for all but the simplest algorithms. Our experimental results demonstrate that in practical settings our methods are able to give meaningful lower bounds on the privacy parameter ε. However, while we win on computational eﬃciency, we lose on tightness of our lower bounds. We now illustrate the limitations of our approach and discuss the extent to which this is inherent, and what lessons we can learn. But, ﬁrst, we illustrate that our method can give tight lower bounds. In Figure 10, we consider an idealized setting where the number of guesses changes and the fraction that are correct is ﬁxed at eε eε+1 for ε = 4 – i.e., 98.2% of guesses are correct.4 This is the maximum expected fraction of correct guesses compatible with (4, 0)-DP. In this setting the lower 4The number of correct guesses is rounded down to an integer (which results in the lines being jagged). 27 1 2 3 4 5 6 7 8 Theoretical Epsilon 0 1 2 3 4 5 6 7…
