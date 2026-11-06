# Project Report: Data-Driven Management Optimization
## ITB STIKOM Bali, Abiansemal Campus
*S1 Information Systems Final Project Research*

---

## 📖 Abstract

> **Source note:** figures in this abstract are thesis results from the full private dataset
> and are not reproducible from this repository. Repo-measured fixture values are in
> "Key Results" below.

In order to remain competitive, universities in the higher education sector must optimize data-driven management. The ITB STIKOM Bali Abiansemal Campus is facing challenges in improving marketing effectiveness, HR performance, and operational efficiency. This study uses data science classification methods (K-Nearest Neighbors, Random Forest, Decision Tree, and Support Vector Machine (SVM)) on the Orange Data Mining Platform to identify the dominant factors in these three areas. Data was collected from Instagram marketing campaigns, staff performance (productivity), and the purchase of goods and the operational budget. The results showed that, in the marketing field: Reels content increased engagement by 71% (model accuracy: 94%). HR: Absenteeism was the dominant factor in performance classification (77% accuracy); and operations: 13.6% of purchases were identified as inefficient (with the potential to save IDR 2.3 million per month). Implementing the Orange Data Mining dashboard provided strategic recommendations for: Reels-based marketing budget allocation, Focused staff training, Procurement cost savings. This research proves the effectiveness of Orange Data Mining as an integrated, nontechnical analytics solution for universities.

---

## 🏗️ Project Structure

```
b-comp-sc-research/
│
├─ .gitignore               # Files and folders ignored by Git
├─ LICENSE                  # MIT License
├─ README.md                # Repository overview + research summary
├─ PROJECT_REPORT.md        # Full report (this file)
├─ CITATION.cff             # Citation metadata
├─ CONTRIBUTING.md          # Contribution guidelines
├─ SECURITY.md              # Security policy
│
├─ data/                    # ✅ Synthetic (anonymized) sample data
│   ├─ marketing_sample.csv # Instagram Reels vs Post engagement
│   ├─ hr_sample.csv        # Staff attendance/productivity performance
│   └─ ops_sample.csv       # Procurement unit vs market price efficiency
│
├─ workflows/               # ⚙️ Algorithm implementations (Python, scikit-learn)
│   ├─ marketing_reels.py   # Random Forest – engagement prediction (Reels vs Post)
│   ├─ hr_decision_tree.py  # Decision Tree – staff performance classification
│   └─ ops_svm_knn.py       # SVM + k-NN – inefficient purchase detection
│
├─ docs/                    # 📚 Narrative documentation (English)
│   ├─ abstract.md          # Thesis abstract (source-labelled)
│   ├─ methodology.md       # Methodology, preprocessing, modelling, evaluation
│   ├─ results.md           # Reproduced vs thesis results (labelled)
│   ├─ REPRODUCIBILITY.md   # What runs, what cannot be reproduced, and why
│   ├─ DEMO_OUTPUT.txt      # Raw captured output of scripts/demo.py
│   └─ full_text.txt        # Thesis front matter + TOC (English)
│
├─ scripts/                 # ▶️ Helper scripts
│   ├─ demo.py              # Runs the workflows; writes results/metrics.json + summary.txt
│   └─ plot_results.py      # Plots measured metrics → results/accuracy_bar.png (not committed)
│
├─ results/                 # 📊 Measured output from the demo fixtures
│   ├─ metrics.json
│   └─ summary.txt
│
└─ .github/                 # ⚙️ GitHub Actions CI (installs deps, runs demo + verify.py)
    └─ workflows/
        └─ ci.yml
```

---

## 🔧 How to Use

### 1. Clone the repository
```bash
git clone git@github.com:afiqandico/b-comp-sc-research.git
cd b-comp-sc-research
```

### 2. Set up a virtual environment (recommended)
```bash
# Python 3.11 or 3.12 recommended
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt   # core packages
pip install -r requirements-dev.txt   # development packages (jupyter, matplotlib, seaborn, etc.)
```

### 4. Run the quick demo
```bash
python scripts/demo.py
```
Output shows classification accuracy and reports for each workflow and saves `results/metrics.json` + `results/summary.txt`.

### 5. Verify reproducibility
```bash
python verify.py
```
Runs the demo again and asserts the measured accuracies as floats (±0.01) and the fixture
row counts — exits 0 only on success. It checks the fixture values, not the thesis values.

### 6. Regenerate the metric chart (optional)
```bash
python scripts/plot_results.py   # → results/accuracy_bar.png (from measured metrics.json)
```
The chart is labelled as demo-fixture output and is not committed.

### 7. View narrative documentation
- Summary: `README.md`
- Full: `PROJECT_REPORT.md` (this file)
- Specific topics: see the `docs/` folder

---

## 📊 Key Results

### Part A — reproduced by this repository (synthetic fixtures only)

Computed by `scripts/demo.py` from `data/*.csv` (10/13/10 rows, single 80/20 split,
`random_state=42`); raw log in `docs/DEMO_OUTPUT.txt`.

| Domain      | Algorithm            | Accuracy | Precision | Recall | F1-Score | Test samples |
|-------------|----------------------|----------|-----------|--------|----------|--------------|
| Marketing   | Random Forest        | 1.00     | 1.00      | 1.00   | 1.00     | 2            |
| HR          | Decision Tree        | 0.33     | 0.11      | 0.33   | 0.17     | 3            |
| Operations  | SVM (linear)         | 0.50     | 0.25      | 0.50   | 0.33     | 2            |
| Operations  | k-NN (k=5)           | 0.50     | 0.25      | 0.50   | 0.33     | 2            |

With two or three test samples these values are smoke tests, not estimates of model
quality, and they support no generalization.

### Part B — thesis results (cited, NOT reproducible here)

Computed on the full private dataset with 5-fold cross-validation (thesis abstract and
Chapter 4). The dataset is not in this repository, so these numbers cannot be regenerated:

- Marketing (Random Forest): **94%**
- HR (Decision Tree): **77%**
- Operations (SVM/k-NN): **82%**

See `docs/REPRODUCIBILITY.md` for what would be required to reproduce Part B.

---

## 📈 Figures

No figure is committed. The confusion-matrix and ROC images previously listed here were
generated from `make_classification()` random data unrelated to this study, and the
accuracy bar chart hard-coded 0.94/0.77/0.82; all three and their generators were removed.

`python scripts/plot_results.py` now renders `results/accuracy_bar.png` from the measured
`results/metrics.json` and labels it as fixture output. Thesis figures (confusion matrix,
ROC) can only be produced once the full dataset is available.

---

## 🛠️ Technologies Used

| Component         | Version / Notes |
|-------------------|-----------------|
| Python            | 3.11 – 3.12 |
| pandas            | ≥2.0 |
| scikit-learn      | ≥1.4 |
| matplotlib        | ≥3.7 |
| seaborn           | ≥0.13 |
| Jupyter Notebook  | ≥6.5 |
| Orange Data Mining | 3.36+ (optional, for original workflow export) |
| Git               | – |
| License           | MIT |

---

## 📖 Main Contributions

1. **Three-Domain Integration** – Combining marketing, HR, and operations in a single Orange-based classification workflow.
2. **Bridging the Gap** – Connecting data science analysis (classification) to strategic recommendations (SWOT, Gap Analysis, Content Calendar).
3. **No-Code/Low-Code Solution** – Using the Orange drag-and-drop interface so managers without a programming background can understand and use the results.
4. **Complete Documentation** – From abstract, methodology, results, to recommendations, all presented in easily accessible Markdown format.
5. **Reproducibility** – The demo pipeline and its fixture-level expected values are pinned by `verify.py` and run in CI. The thesis results are cited with their source but cannot be reproduced from this repository because the dataset is private.

---

## 🙋 Contact

- **Email**: afiqandico13@gmail.com
- **GitHub**: [github.com/afiqandico](https://github.com/afiqandico)
- **ORCID**: [orcid.org/0009-0002-1750-9551](https://orcid.org/0009-0002-1750-9551)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this code and documentation as long as you retain the copyright and license notice.

---

*© 2025 Afiq Andico Pangimpian. All rights reserved.*
*If you find this project useful, give it a ⭐ or fork it for further development!*