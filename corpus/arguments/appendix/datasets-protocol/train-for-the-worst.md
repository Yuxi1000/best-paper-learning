# Appendix/datasets-protocol: Train for the Worst, Plan for the Best: Understanding Token Ordering in Masked Diffusions

- id: `train-for-the-worst`
- source: arXiv:2502.06768

## D.2. Experimental details on Sudoku and Zebra puzzles

Dataset. For both Sudoku and Zebra puzzles, we use the dataset provided in Shah et al. (2024) to train our model. To evaluate our model on the same difficulty tasks, we use the test dataset proposed in Shah et al. (2024). This dataset is created by filtering the puzzles from (Radcliffe, 2020) that can be solved using a fixed list of 7 strategies. To create a hard dataset to evaluate easy-to-hard generalization, we use the remaining puzzles from (Radcliffe, 2020) as they either require a new strategy unseen during the training and/or require backtracking. The hard dataset contains around 1M Sudoku puzzles. Model, training, and inference. For the training and inference, we use the codebase of (Ye et al., 2024) with keeping most of the hyperparameters default given in the codebase. For the Sudoku dataset, we use 6M GPT-2 model, and for the Zebra dataset, we use 19M model. We set the learning rate to 0.001 with a batch size of 128 to train the model for 300 epochs. For the inference, we use 50 reverse sampling steps using the appropriate strategy. Additionally, we add Gumbel noise with a coefficient of 0.5 to the MDM inference oracle F. 19 Train for the Worst, Plan for the Best:…
