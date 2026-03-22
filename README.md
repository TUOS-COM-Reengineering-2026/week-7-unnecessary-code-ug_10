[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/VDzEbIbf)
# Code Clones and Unnecessary Code

NOTE: Do **not** modify any files in the `tests` directory for all tasks.

## Setup

```bash
pip install -r requirements.txt
```

## Part 1: Code Clones

### Task 1.1: Find Code Clones using Jaccard Similarity (5 points)

Update the `compute_jaccard_similarity()` function in `code_clones.py` to compute the Jaccard similarity between two code snippets.
If correctly implemented, the following command should return OK (2 PASSED):

```bash
pytest tests/test_jaccard.py -v
```

- Open Question: What is the threshold value for Jaccard similarity that you would consider two code snippets to be clones?

### Task 1.2: Visualise Code Clones using Dot Plots (10 points)

Update the `visualise_dot_plot()` function in `code_clones.py` to visualise code clones using dot plots.
If correctly implemented, the following command should return OK (2 PASSED):

```bash
pytest tests/test_dot_plots.py -v
```

## Part 2: Unnecessary Code

### Task 2.1: Remove Dead Code (5 points)

Remove dead code from the `example_function()` function in `dead_code.py`.
If correctly removed, the following command should return OK (1 PASSED):

```bash
pytest tests/test_dead_code.py -v
```

## Part 3: (Advanced Topic) Program Debloating

Can you automatically remove dead code from the `example_function()` function in `dead_code.py`?

HINT: Try to transform the problem into an optimisation problem and use random search to find the optimal solution (see Week 6 lecture slides). 

See the Reading List on Blackboard for more advanced techniques.