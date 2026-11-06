# Reproducibility

This document states precisely what can and cannot be reproduced from this repository,
and why. It is the authoritative description; any conflicting claim elsewhere in the
repository is a documentation bug.

## 1. How to run

Requirements: Python 3.10+ (verified on 3.14.4), `pandas`, `scikit-learn`
(`requirements.txt`).

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python scripts/demo.py     # prints measured metrics, writes results/metrics.json
python verify.py           # asserts the measured values; non-zero exit on drift
```

`scripts/demo.py` runs the three workflows in `workflows/` as subprocesses, parses every
`... Accuracy: <float>` line, and writes `results/metrics.json` and
`results/summary.txt`. `verify.py` re-runs the demo, parses the same lines as floats,
prints an expected-vs-actual table, and fails if any delta exceeds 0.01 or if a fixture
row count changed. CI (`.github/workflows/ci.yml`) performs exactly these steps on every
push and pull request.

`scripts/plot_results.py` optionally renders `results/accuracy_bar.png` from
`results/metrics.json`. Images are not committed.

## 2. What is reproducible

- **Pipeline execution.** All three workflows load their CSV, split 80/20 with
  `random_state=42`, fit the classifier, and report accuracy. This runs deterministically.
- **Exact metric values on the committed fixtures.** With the committed data, the demo
  produces:

  | Model | Fixture | Fixture rows | Test samples | Accuracy |
  |---|---|---|---|---|
  | Marketing Random Forest | `data/marketing_sample.csv` | 10 | 2 | 1.00 |
  | HR Decision Tree | `data/hr_sample.csv` | 13 | 3 | 0.33 |
  | Ops SVM | `data/ops_sample.csv` | 10 | 2 | 0.50 |
  | Ops k-NN | `data/ops_sample.csv` | 10 | 2 | 0.50 |

  Raw captured log: [`DEMO_OUTPUT.txt`](DEMO_OUTPUT.txt).
- **Failure on drift.** Changing one test-split label in the marketing fixture moves its
  accuracy from 1.00 to 0.50; `verify.py` then prints `FAIL`, reports delta 0.50, and
  exits 1. The check tests values, not the presence of a label string.

Environment used for the recorded run: Linux 7.0.0-42-generic x86_64, CPython 3.14.4,
pandas 3.0.5, scikit-learn 1.9.0. Because the split is seeded and the fixtures are fixed,
values are stable across runs; they are *not* guaranteed to be stable across every
scikit-learn major version if a default changes, which is exactly what `verify.py` exists
to detect.

## 3. What is NOT reproducible

- **The thesis accuracies: Marketing 94.0% ± 1.2%, HR 77.0% ± 2.0%, Operations
  82.0% ± 1.8%.** These are cited from the thesis, not produced by this code.
- **Derived thesis findings**: Reels +71% engagement, 13.6% inefficient purchases,
  IDR 2.3M/month potential savings. They depend on the full dataset.
- **Thesis figures**: confusion matrix, ROC curve, feature importance, heatmaps.
- **5-fold cross-validation averages.** The scripts implement a single 80/20 split; the
  thesis evaluation averaged five folds.

## 4. Why

1. **The dataset is not in the repository.** `data/*.csv` are synthetic fixtures of 10,
   13 and 10 rows, created to exercise the code path. The institutional data (Instagram
   campaign records, staff performance, procurement transactions) is private: staff
   records were anonymized under an institutional permit and cannot be published.
2. **The evaluation protocol differs.** Even with the real data, these scripts would not
   reproduce the thesis numbers without the same folds, preprocessing and Orange Data
   Mining configuration.
3. **Test sets are 2–3 samples.** On such a split each sample is worth 33–50 percentage
   points, so fixture accuracy is a smoke-test signal, not an estimate of model quality.
   No conclusion about the campus, the thesis, or other institutions follows from it.

## 5. What would make the thesis results reproducible

Publish, or make available under controlled access, (a) the anonymized datasets used for
each domain, (b) the exact preprocessing parameters and fold assignment, and (c) the
exported Orange workflow files. With those, the 5-fold evaluation could be re-run and the
reported means and standard deviations checked. Until then, the thesis numbers remain
cited results with a stated source, and the repository numbers remain fixture smoke tests.

## 6. A note on figures

Earlier revisions shipped `docs/confusion_matrix.png`, `docs/roc_curve.png` and
`results/accuracy_bar.png`. The first two were generated from `make_classification()`
random data unrelated to this study, and the third hard-coded 0.94/0.77/0.82. They have
been removed along with their generators. Any figure in this repository must be produced
from the data actually being discussed; when only the demo fixture is available, the
figure must say so.
