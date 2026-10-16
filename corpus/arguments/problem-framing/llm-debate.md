# Debating with More Persuasive LLMs Leads to More Truthful Answers

- id: `llm-debate`
- award: ICML 2024 Best Paper
- section_bucket: problem-framing
- source: arXiv:2402.06782

## Excerpt (truncated; study the move, do not copy)

Debating with More Persuasive LLMs Leads to More Truthful Answers Akbir Khan * 1 John Hughes * 2 3 Dan Valentine * 3 Laura Ruis 1 Kshitij Sachan 4 5 Ansh Radhakrishnan 4 Edward Grefenstette 1 Samuel R. Bowman 4 Tim Rockt¨aschel 1 Ethan Perez 4 6 Abstract Common methods for aligning large language models (LLMs) with desired behaviour heavily rely on human-labelled data. However, as models grow increasingly sophisticated, they will surpass human expertise, and the role of human evaluation will evolve into non-experts overseeing experts. In anticipation of this, we ask: can weaker models assess the correctness of stronger models? We investigate this question in an analogous setting, where stronger models (experts) possess the necessary information to answer questions and weaker models (non-experts) lack this information but are otherwise as capable. The method we evaluate is debate, where two LLM experts each argue for a different answer, and a non-expert selects the answer. On the QuALITY comprehension task, we find that debate consistently helps both non-expert models and humans answer questions, achieving 76% and 88% accuracy respectively (naive baselines obtain 48% and 60%). Furthermore, optimising expert debaters for persuasiveness in an unsupervised manner improves non-expert ability to identify the truth in debates. Our results provide encouraging empirical evidence for…
