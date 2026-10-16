# Privacy Auditing with One (1) Training Run

- id: `privacy-auditing`
- award: NeurIPS 2023 Outstanding Paper
- section_bucket: claim-contribution
- source: arXiv:2305.08846

## Excerpt (truncated; study the move, do not copy)

Our approach (§2): The DP deﬁnition (1) considers adding or removing a single person’s data to or from the dataset. We consider multiple people’s data and the dataset independently includes or excludes each person’s data point. Our analysis exploits the parallelism of multiple independent data points in a single run of the algorithm in lieu of multiple independent runs. Our auditing procedure operates as follows. We identify m data points (i.e., training examples or “canaries”) to either include or exclude and we ﬂip m independent unbiased coins to decide which of them to include or exclude. We then run the algorithm on the randomly selected dataset. Based on the output of the algorithm, the auditor “guesses” whether or not each data point was included or excluded (or it can abstain from guessing for some data points). We obtain a lower bound on the privacy parameters from the fraction of guesses that were correct. Intuitively, if the algorithm is (ε, 0)-DP, then the auditor can correctly guess each inclusion/exclusion coin ﬂip with probability at most eε eε+1. Thus DP implies a high-probability upper bound on the fraction of correct guesses and, conversely, a large fraction of correct guesses implies a high-probability lower bound on the privacy parameters. Our analysis (§5): Na¨ıvely, analyzing the addition or removal of multiple data elements would rely on group privacy;…
