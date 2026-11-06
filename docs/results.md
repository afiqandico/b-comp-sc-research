# Results

This file reports two separate sets of numbers. Do not conflate them; see
[`REPRODUCIBILITY.md`](REPRODUCIBILITY.md).

## Part A — Reproduced from this repository (demo fixture only)

Source: `python scripts/demo.py`, raw log in [`DEMO_OUTPUT.txt`](DEMO_OUTPUT.txt).
Single 80/20 split, `random_state=42`, on synthetic fixtures of 10/13/10 rows.

| Domain | Model | Fixture rows | Test samples | Accuracy |
|---|---|---|---|---|
| Marketing | Random Forest (n=100) | 10 | 2 | 1.00 |
| HR | Decision Tree (max_depth=3) | 13 | 3 | 0.33 |
| Operations | SVM (linear) | 10 | 2 | 0.50 |
| Operations | k-NN (k=5) | 10 | 2 | 0.50 |

Interpretation: the pipeline executes end to end and produces deterministic values on the
committed fixtures. With two or three test samples, one prediction is worth 33–50
percentage points, so these numbers do **not** measure model quality and must not be
quoted as findings about the campus, the thesis, or any other institution.

## Part B — Thesis results (cited, not reproducible here)

Source: the thesis (abstract and Chapter 4). These were computed on the private
institutional dataset, which is not included in this repository, using 5-fold
cross-validation.

| Domain | Model | Accuracy (thesis) | Key finding (thesis) |
|---|---|---|---|
| Marketing | Random Forest | 94.0% ± 1.2% | Reels content increased engagement by 71% compared to Post |
| HR | Decision Tree | 77.0% ± 2.0% | Absenteeism is the dominant factor affecting staff performance |
| Operations | SVM (linear) + k-NN | 82.0% ± 1.8% | 13.6% of procurement transactions classified inefficient; up to IDR 2.3M/month potential savings |

Implications as argued in the thesis: shift marketing budget toward Reels production,
target training at staff with high absenteeism, and apply the 110%-of-market-price rule to
procurement. These recommendations rest on the thesis dataset, not on the fixture run.

## Visualization

No figure is committed. The two images previously shown here were generated from
`make_classification()` random data and did not represent this study; they were removed.
`scripts/plot_results.py` will render `results/accuracy_bar.png` from the measured
`results/metrics.json`, labelled as fixture output. A confusion matrix or ROC curve for the
thesis results can only be produced once the underlying dataset is available.

## Summary

The repository demonstrates a working three-domain classification pipeline and pins its
fixture-level output with an automated value check. The substantive results of the study
remain the thesis-reported figures in Part B, which this repository cites but cannot
recompute.
