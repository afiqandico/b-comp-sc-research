# B.Comp.Sc. Research — Campus Management Optimization via Data Science Classification (ITB STIKOM Bali)

> B.Comp.Sc. (Bachelor of Computer Science) thesis research, Information Systems, ITB STIKOM
> Bali (2025). This repository documents the study and ships a small, runnable version of
> its classification pipeline. It does **not** ship the institutional dataset, so the
> thesis accuracy figures cannot be regenerated here. Both kinds of numbers are labelled
> separately below.

## 📋 Research Details

| Item | Detail |
|---|---|
| Degree | Bachelor of Computer Science (B.Comp.Sc. / S.Kom) |
| Study Program | S1 Information Systems |
| Institution | Institute of Technology and Business (ITB) STIKOM Bali — Abiansemal Campus |
| Author | Afiq Andico Pangimpian (Student ID 190030591) |
| Year | 2025 — final exam 03 September 2025 |
| Supervisors | Indrianto, S.Kom., M.Kom. (main supervisor) · Muhamad Samsudin, SE., MM.Kom. |
| Domain | Marketing (Instagram), Human Resources (staff performance), Operations (procurement) |
| Method | Data science classification (K-Nearest Neighbors, Random Forest, Decision Tree, SVM) on Orange Data Mining; 5-fold cross-validation |
| Thesis-reported results | Marketing 94% acc (Reels engagement uplift 71%) · HR 77% · Operations 82% (13.6% purchases inefficient, up to IDR 2.3M/month savings) — **reported in the thesis, not reproducible from this repository** |
| Documentation | `docs/abstract.md`, `docs/methodology.md`, `docs/results.md`, `docs/REPRODUCIBILITY.md`, `docs/full_text.txt` |

<div align="center">

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![Orange](https://img.shields.io/badge/Orange_Data_Mining-F78400?style=for-the-badge&logo=orange&logoColor=white)]()
[![License](https://img.shields.io/badge/License-MIT-89b4fa?style=for-the-badge&labelColor=1e1e2e)](LICENSE)

</div>

---

## ⚠️ Read this before quoting any number

This repository contains **two different sets of results**, and they must not be mixed:

| | What it is | Reproducible here? |
|---|---|---|
| **(A) Demo pipeline results** | Accuracy measured by `scripts/demo.py` on the three tiny synthetic fixtures in `data/` (10, 13 and 10 rows) | **Yes** — regenerated on every run and asserted by `verify.py` |
| **(B) Thesis results** | Accuracy reported in the thesis (Marketing 94%, HR 77%, Operations 82%), computed on the full institutional dataset | **No** — that dataset is not in this repository |

The demo fixture is a smoke test for the pipeline. Its test splits contain **2–3 samples**,
so a "100%" or "33%" there says nothing about model quality, the thesis, or campus
management in general. No claim in this repository generalizes beyond these fixtures.

### (A) What this repository actually reproduces

Measured on 2026-11-06 with Python 3.14.4, pandas 3.0.5, scikit-learn 1.9.0; raw log in
[`docs/DEMO_OUTPUT.txt`](docs/DEMO_OUTPUT.txt). Single 80/20 split, `random_state=42`.

| Domain | Model | Fixture rows | Test samples | Accuracy (measured) |
|---|---|---|---|---|
| Marketing | Random Forest (n=100) | 10 | 2 | **1.00** |
| HR | Decision Tree (depth=3) | 13 | 3 | **0.33** |
| Operations | SVM (linear) | 10 | 2 | **0.50** |
| Operations | k-NN (k=5) | 10 | 2 | **0.50** |

These are the values `verify.py` asserts (tolerance ±0.01). They describe only how the
code behaves on a 10–13 row synthetic fixture.

### (B) What the thesis reports — not reproducible from this repository

Source: thesis abstract and Chapter 4, mirrored in `docs/abstract.md`,
`docs/methodology.md` and `docs/results.md`. These figures come from the private
institutional dataset (Instagram campaign records, anonymized staff performance,
procurement transactions), which is **not included** in this repository. No script here
can regenerate them.

| Domain | Model | Accuracy (thesis) | Key finding (thesis) |
|---|---|---|---|
| Marketing | Random Forest | 94.0% ± 1.2% | Reels content associated with 71% higher engagement than Post |
| HR | Decision Tree | 77.0% ± 2.0% | Absenteeism is the dominant performance factor |
| Operations | SVM (linear) + k-NN | 82.0% ± 1.8% | 13.6% of purchases classified inefficient; up to IDR 2.3M/month potential savings |

Why they cannot be reproduced: the raw data is private and was never published (privacy
and institutional permission), and the original evaluation used 5-fold cross-validation
on the full dataset rather than the single 80/20 split implemented here. See
[`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md).

---

## 🎯 Pipeline

```text
Data collection → Cleaning → Feature engineering → Classification → Insight reporting
```

The Python workflows mirror the Orange Data Mining design: cleaning, label encoding,
an 80/20 split, then Random Forest / Decision Tree / SVM + k-NN. They are a readable
re-implementation for demonstration, not a byte-for-byte export of the Orange workflow,
and they do not implement the 5-fold cross-validation described in the thesis.

---

## 📂 Project Structure

```text
b-comp-sc-research/
├── data/                     # Synthetic fixtures (10/13/10 rows) — smoke test only
│   ├── marketing_sample.csv
│   ├── hr_sample.csv
│   └── ops_sample.csv
├── workflows/                # Classifier implementations
│   ├── marketing_reels.py    # Random Forest — engagement prediction (Reels vs Post)
│   ├── hr_decision_tree.py   # Decision Tree — staff performance classification
│   └── ops_svm_knn.py        # SVM + k-NN — inefficient purchase detection
├── scripts/
│   ├── demo.py               # Run all workflows, print + save measured metrics
│   └── plot_results.py       # Plot measured metrics from results/metrics.json
├── docs/
│   ├── abstract.md           # Thesis abstract (thesis-reported figures)
│   ├── methodology.md        # Data sources, preprocessing, modelling, evaluation
│   ├── results.md            # Thesis results + reproduced demo results, labelled
│   ├── REPRODUCIBILITY.md    # What runs, what cannot be reproduced, and why
│   ├── DEMO_OUTPUT.txt       # Raw captured output of scripts/demo.py
│   └── full_text.txt         # Thesis front matter + TOC
├── results/                  # metrics.json + summary.txt (generated numerically)
├── PROJECT_REPORT.md         # Narrative project report
├── verify.py                 # Asserts measured accuracies (float, ±0.01)
└── README.md
```

> **Note:** `data/` holds synthetic/anonymized samples for pipeline demonstration. The real
> institutional dataset is private and stays outside the repository.

---

## 🚀 Quick Start

```bash
git clone git@github.com:afiqandico/b-comp-sc-research.git
cd b-comp-sc-research

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

pip install -r requirements.txt
python scripts/demo.py            # prints measured metrics, writes results/
python verify.py                  # exits non-zero if any value drifts
```

`verify.py` runs the demo, parses each accuracy as a float, prints an expected-vs-actual
table, and fails on a difference greater than 0.01 or on a changed fixture row count. It
checks the fixture values in table (A), not the thesis values in table (B).

Expected output (values only; see `docs/DEMO_OUTPUT.txt` for the full log):

```text
Marketing Random Forest Accuracy: 1.00
HR Decision Tree Accuracy: 0.33
Ops SVM Accuracy: 0.50
Ops k-NN Accuracy: 0.50
Verification PASSED
```

Visualizations are not committed. `scripts/plot_results.py` builds
`results/accuracy_bar.png` from the measured `results/metrics.json` and labels it as
fixture output. Confusion-matrix / ROC images from the thesis cannot be regenerated here
because the full dataset is absent; any such figure must be produced from real data, and
no placeholder or synthetic image is shipped.

---

## ⚠️ Research Limitations

- **Data privacy**: staff performance data was anonymized with the Andico-Ruby encryption
  (recursive dynamic shift + information-energy transformation) before modelling, which
  limits micro-level analysis but protects identities.
- **No dataset in repo**: `data/` contains 10–13 row synthetic fixtures, not the thesis
  dataset. Thesis accuracy figures are therefore cited, not reproduced.
- **Single split, not 5-fold CV**: the demo scripts use one 80/20 split; the thesis
  evaluation averaged 5 folds. Demo numbers are not comparable to thesis numbers.
- **Tiny test sets**: 2–3 test samples per domain; a single flipped label moves accuracy
  by 33–50 percentage points. The demo validates that the pipeline executes, nothing more.
- **Scope**: the study covers one campus (Abiansemal) and three domains (marketing, HR,
  operations); generalization to other campuses requires additional data.

---

## 📜 License

MIT — see [LICENSE](LICENSE). Documentation follows the same license unless stated
otherwise in the file.

---

## 👤 Author

**Afiq Andico Pangimpian** — Independent researcher — data science & cybersecurity.

<div align="center">
  <a href="https://github.com/afiqandico" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
  <a href="https://orcid.org/0009-0002-1750-9551" target="_blank">
    <img src="https://img.shields.io/badge/ORCID-0009--0002--1750--9551-A6CE39?style=for-the-badge&logo=orcid&logoColor=white"/>
  </a>
  <a href="mailto:afiqandico13@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
  </a>
</div>

> *Data is not just numbers. It is the blueprint of how systems operate, and the key to making them better.*
