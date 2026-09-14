# B.Comp.Sc. Research — Campus Management Optimization via Data Science Classification (ITB STIKOM Bali)

> B.Comp.Sc. (Bachelor of Computer Science) thesis research, Information Systems, ITB STIKOM
> Bali (2025). This README explains the research in detail: background and scope,
> method, results, and reproducibility.

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
| Key Results | Marketing 94% acc (Reels engagement uplift 71%) · HR 77% · Operations 82% (13.6% purchases inefficient, up to IDR 2.3M/month savings) |
| Documentation | `docs/abstract.md`, `docs/methodology.md`, `docs/results.md`, `docs/full_text.txt` (all in English) |

<div align="center">

[![Status](https://img.shields.io/badge/STATUS-RESEARCH-a6e3a1?style=for-the-badge&labelColor=1e1e2e)]()
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![Orange](https://img.shields.io/badge/Orange_Data_Mining-F78400?style=for-the-badge&logo=orange&logoColor=white)]()
[![License](https://img.shields.io/badge/License-MIT-89b4fa?style=for-the-badge&labelColor=1e1e2e)](LICENSE)

</div>

---

```text
[Pipeline] Data collection → Cleaning → Feature Engineering → Classification (Orange) → Insight Reporting
Marketing : 94% accuracy  | HR : 77% accuracy  | Operations : 82% accuracy | Status: VALIDATED
```

---

## 🎯 Research Summary

| Domain | Model | Accuracy | Key Finding |
|--------|-------|----------|-------------|
| **Marketing** | Random Forest (n=100) | 94.0% ± 1.2% | Reels content increases engagement by 71% vs Post |
| **HR** | Decision Tree (depth=3) | 77.0% ± 2.0% | Absenteeism is the dominant performance factor |
| **Operations** | SVM (linear) + k-NN (k=5) | 82.0% ± 1.8% | 13.6% of purchases detected as inefficient (savings up to IDR 2.3M/month) |

The three workflows follow one reproducible pipeline: preprocessing (cleaning,
label encoding, min-max normalization, 80/20 stratified split) → classification
in Orange Data Mining → 5-fold cross-validation → strategic recommendations
(Reels-based budget allocation, focused staff training, cost-efficient procurement).

---

## 📂 Project Structure

```text
b-comp-sc-research/
├── data/                     # Synthetic (anonymized) sample datasets
│   ├── marketing_sample.csv
│   ├── hr_sample.csv
│   └── ops_sample.csv
├── workflows/                # Algorithm implementations exported from Orange
│   ├── marketing_reels.py    # Random Forest — engagement prediction (Reels vs Post)
│   ├── hr_decision_tree.py   # Decision Tree — staff performance classification
│   └── ops_svm_knn.py        # SVM + k-NN — inefficient purchase detection
├── scripts/
│   ├── demo.py               # Run all workflows and print metrics
│   ├── generate_visuals.py   # Generate plots (confusion matrix, ROC)
│   └── plot_results.py       # Plot saved results
├── docs/
│   ├── abstract.md           # Abstract (English)
│   ├── methodology.md        # Data sources, preprocessing, modelling, evaluation
│   ├── results.md            # Numeric results and interpretations
│   └── full_text.txt         # Full thesis front matter + TOC (English)
├── results/                  # Numeric evaluation output (metrics.json, plots)
├── PROJECT_REPORT.md         # Full project report
├── verify.py                 # Reproducibility checks
└── README.md                 # This file
```

> **Note:** the `data/` directory contains only synthetic/anonymized samples for
> demonstration. The real institutional dataset is private and stays outside the
> repository (see `docs/methodology.md` and the thesis appendices).

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone git@github.com:afiqandico/b-comp-sc-research.git
cd b-comp-sc-research

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the demo
python scripts/demo.py

# 5. Reproduce results
python verify.py
```

---

## ⚠️ Research Limitations

- **Data Privacy**: staff performance data was anonymized with the Andico-Ruby
  encryption (recursive dynamic shift + information-energy transformation) before
  modelling, which limits micro-level analysis but protects identities.
- **Sample Data**: CSV files in `data/` are small synthetic samples for pipeline
  demonstration; real accuracy figures come from the original thesis dataset
  (see `docs/methodology.md`).
- **Scope**: the study covers one campus (Abiansemal) and three domains
  (marketing, HR, operations); generalization to other campuses requires
  additional data.

---

## 📜 License

MIT — see [LICENSE](LICENSE). Documentation follows the same license unless
stated otherwise in the file.

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