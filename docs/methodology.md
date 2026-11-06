## Methodology

**Data Sources**
- Instagram campaign data (account @itbstikombaliabiansemal) for February–April 2025: number of likes, shares, comments, content type (Reels/Post).
- Staff performance data: absenteeism (%), productivity (%), performance label (Excellent/Good/Fair) based on the BKN 2023 standard.
- Operational goods purchase data: item name, quantity, unit price, average market price, efficiency label (efficient/inefficient) based on the 110% of market price threshold.

**Preprocessing**
1. Cleaning: removing duplicates, empty numeric values filled with the mean, categorical values with the mode.
2. Transformation: categorical variables (content type, performance label, efficiency label) converted to numeric (0/1 or label encoding).
3. Normalization: min-max scaling to the [0,1] range for all numeric features using the Orange *Data Table* → *Preprocess* widgets.
4. Dataset split: 80% training data, 20% test data (stratified by label).

**Modelling (Orange Data Mining)**
- **Marketing**: Random Forest (n_estimators=100) to predict high/low engagement based on content type and engagement metrics.
- **HR**: Decision Tree (max_depth=3) to classify staff performance based on absenteeism and productivity.
- **Operations**: SVM with linear kernel + k-NN (k=5) to detect inefficient purchases (price > 1.10 × market price).

**Evaluation**
- Accuracy, precision, and AUC (Area Under Curve) computed via 5-fold cross-validation.
- The final result is the average across folds.
- Visualization: confusion matrix, ROC curve, feature importance, scatter plot, heatmap.

> **Implementation note:** the scripts in `workflows/` re-implement the models but use a
> single seeded 80/20 split, not 5-fold cross-validation. They are a demonstration of the
> pipeline, and their output on the 10–13 row fixtures cannot reproduce the figures in the
> Results section below. See [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md).

**Integration & Recommendations**
The classification results are used as the basis for:
- *Content Calendar* (marketing): scheduling Reels content by effective days and hours.
- SWOT analysis and Gap analysis to determine improvement strategies.
- An interactive Orange dashboard displaying dominant factors and action recommendations (budget allocation, focused training, cost-efficient procurement).

**Ethics**
- Staff performance data is anonymized using the Andico-Ruby encryption algorithm (recursive dynamic shift + information-energy transformation) before being fed into the model.
- The research has obtained permission from the relevant institution (Appendix 11 Research Permit Letter).

## Results

> **Source note:** every figure in this section is the thesis result, computed on the full
> private dataset with 5-fold cross-validation. It is **not** produced by this repository
> and cannot be regenerated from `data/`. The repository's own measured output (fixture
> smoke test) is in [`results.md`](results.md) Part A and [`DEMO_OUTPUT.txt`](DEMO_OUTPUT.txt).

### 4.3 Classification Results per Domain

| Domain      | Algorithm           | Accuracy (± std) | Precision (± std) | AUC (± std) |
|-------------|---------------------|------------------|-------------------|-------------|
| Marketing   | Random Forest       | 94.0% ± 1.2%     | 92.5% ± 1.5%      | 0.96 ± 0.02 |
| HR          | Decision Tree       | 77.0% ± 2.0%     | 75.3% ± 2.3%      | 0.81 ± 0.03 |
| Operations  | SVM (linear) + k-NN | 82.0% ± 1.8%     | 80.1% ± 2.0%      | 0.88 ± 0.02 |

**Key Interpretations**
- Marketing: Reels content produces a 71% higher probability of high engagement than Post (evident from the label distribution and the feature importance of content type).
- HR: Absenteeism is the attribute with the highest information gain in the decision tree; productivity contributes as a secondary determinant.
- Operations: 13.6% of transactions (3 of 22) are predicted as *inefficient*; the average price violation is 23% above the market price, which could potentially strengthen monthly spending by IDR 2.3 million.

### 4.4 Managerial Strategy Implementation Based on Classification Models

- **Reels-Based Marketing Budget Allocation**: Shifting 20% of the daily Instagram budget from Post to Reels is estimated to increase the average monthly likes from 1,020 to ≈1,250 (up 22%).
- **Focused Staff Training**: Staff with absenteeism < 80% or productivity < 80% are identified for a monthly training program (soft skills, time-management). Simulation shows an increase in average productivity from 75% to 88% after 3 months of training.
- **Procurement Cost Savings**: Applying the efficiency rule (price ≤ 110% of market price) to electronics and CCTV purchases can reduce monthly spending by about IDR 2.3 million (13.6% of total goods procurement).

### 4.6 Staff Performance Data Encryption Implementation

Encryption uses the Andico-Ruby theorem:  
`E(x) = ( (x * a) + b ) mod m` with parameters a, b, m published in Appendix 4.6, allowing reconstruction only by authorized parties while protecting the original staff identities.

### 4.7 SWOT Analysis of Classification Model Implementation

| Strengths                                   | Weaknesses                               |
|---------------------------------------------|------------------------------------------|
| Integration of three domains in one workflow | Dependence on historical data quality    |
| Interpretability (Decision Tree, Linear Regression) | Requires initial training for non-technical users |
| Interactive visualization in Orange         | Commercial license for advanced plugins  |

| Opportunities                              | Threats                                  |
|--------------------------------------------|------------------------------------------|
| Scalability to other departments (finance, academic) | Campus data policy changes limiting collection |
| Advanced predictive model development (time series) | Dependence on a third-party platform (Orange) |

### 4.8 Gap Analysis

| Aspect               | Current Condition           | Target (after intervention) | Gap    |
|----------------------|-----------------------------|-----------------------------|--------|
| Reels Engagement     | 71% of Reels content is high | ≥ 85%                      | +14%   |
| HR Performance       | 77% classification accuracy | ≥ 85%                      | +8%    |
| Operational Efficiency | 13.6% inefficient transactions | ≤ 5%                  | −8.6%  |

### 4.9 Content Calendar for Marketing Strategy

- **Monday-Wednesday**: campus education Reels (daily 10:00-11:00 WITA)
- **Thursday-Friday**: student event promotion Reels (daily 15:00-16:00 WITA)
- **Saturday-Sunday**: alumni testimonial Reels (daily 09:00-10:00 WITA)

This schedule is derived from the analysis of peak engagement hours (10-11 and 15-16) and audience preference for dynamic visual content.

## Conclusion

This research proves that a data science approach with the Orange Data Mining platform can provide strategic, targeted, and evidence-based recommendations to improve marketing effectiveness, HR performance, and operational efficiency at the ITB STIKOM Bali Abiansemal Campus. The classification results show significant improvements if the recommendations are implemented, with potential operational savings of up to IDR 2.3 million per month and marketing engagement increases of up to 71% higher than baseline.

## Suggestions

1. **Periodic Dashboard Implementation** – Update data monthly and distribute it to leadership through automated PDF exports from Orange.
2. **User Training** – Hold half-day workshops for administrative staff on reading and using Orange visualization widgets.
3. **Expansion to the Academic Domain** – Use the same workflow to predict student graduation or dropout using GPA, attendance, and extracurricular activity data.
4. **Advanced Model Development** – Try gradient boosting algorithms (XGBoost, LightGBM) to improve accuracy, especially for HR and operations.
5. **Continuous Audit and Monitoring** – Create a monthly audit SOP to ensure the efficiency threshold (110% of market price) continues to be applied and that model drift does not occur.

---
*Note: the figures above are the thesis results computed on the full anonymized dataset with 5-fold cross-validation. They are not reproducible from this repository, which ships only 10–13 row synthetic fixtures and a single 80/20 split. See [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md).*