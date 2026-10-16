# Debating with More Persuasive LLMs Leads to More Truthful Answers

- id: `llm-debate`
- award: ICML 2024 Best Paper
- section_bucket: limitation-scope
- source: arXiv:2402.06782

## Excerpt (truncated; study the move, do not copy)

In this work, we explore debate as a method to elicit more truthful answers from LLMs. We demonstrate that by allowing non-experts to judge a transcript between two experts, we can identify the correct answers to questions. Additionally, we show that this oversight mechanism can be automated with LLM judges. Although the original debate protocol that Irving et al. (2018) propose involves a stricter protocol in which only a sub-component has to be judged to validate the entire debate, our results show that judging over full debate transcripts is already useful for producing expert labels for data using only non-experts and untrustworthy experts. Our findings generalise to different base LLMs for both the expert debaters and non-expert judges, as well as to human judges. This indicates that the debate protocol is robust to variation in judge skill, which is important as models advance. Our work has important limitations. In our setup, the difference between strong and weak is only in access to information. In the future, stronger models may differ in reasoning ability or another skill. Furthermore, we evaluate models that have been fine-tuned with RLHF, which have a propensity for honesty; it is unclear if debate will be a suitable technique for deceptive models (Greenblatt et al., 2023; Hubinger et al., 2024). Finally, our results are limited to setups where the debaters can…
