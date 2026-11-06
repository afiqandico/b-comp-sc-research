"""Plot the accuracies that scripts/demo.py actually measured.

Reads results/metrics.json (produced by scripts/demo.py from data/*.csv) and
writes results/accuracy_bar.png. Values are never hard-coded, and the chart is
labelled as the synthetic-fixture demo rather than the thesis result.

Usage:
    python scripts/demo.py        # refresh results/metrics.json
    python scripts/plot_results.py
"""

import json
import os

import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(BASE)
METRICS = os.path.join(REPO, "results", "metrics.json")
OUTPUT = os.path.join(REPO, "results", "accuracy_bar.png")

LABELS = [
    ("marketing", "marketing", "Marketing\n(Random Forest)"),
    ("hr", "hr", "HR\n(Decision Tree)"),
    ("ops_svm", "ops", "Ops\n(SVM)"),
    ("ops_knn", "ops", "Ops\n(k-NN)"),
]


def main():
    with open(METRICS, encoding="utf-8") as handle:
        metrics = json.load(handle)

    names, values, rows = [], [], []
    for key, dataset, label in LABELS:
        names.append(label)
        values.append(float(metrics[key]["accuracy"]))
        rows.append(int(metrics["datasets"][dataset]["rows"]))

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(names, values, color=["#4caf50", "#2196f3", "#ff9800", "#ff9800"])
    ax.set_ylim(0, 1.0)
    ax.set_ylabel("Accuracy on held-out test split")
    ax.set_title("Demo pipeline on synthetic fixtures (not thesis results)")
    for bar, value, n in zip(bars, values, rows):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2.0,
            height + 0.02,
            f"{value:.0%}\n(n={n})",
            ha="center",
            va="bottom",
        )

    fig.text(
        0.5,
        0.01,
        "Synthetic fixture rows: marketing 10, HR 13, operations 10. "
        "Test splits contain 2-3 samples, so these percentages are not meaningful estimates.",
        ha="center",
        fontsize=8,
        color="#444444",
    )

    plt.tight_layout(rect=(0, 0.04, 1, 1))
    plt.savefig(OUTPUT, dpi=150)
    print(f"Saved plot to {OUTPUT}")


if __name__ == "__main__":
    main()
