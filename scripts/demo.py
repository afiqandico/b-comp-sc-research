# scripts/demo.py
"""Run the three classification workflows and print their measured metrics.

Every number printed or written to results/ is computed at run time from the
CSV fixtures in data/. Nothing is hard-coded, and no accuracy figure from the
thesis is reproduced here: the fixtures are tiny synthetic samples.

Usage:
    python scripts/demo.py
"""

import json
import os
import re
import subprocess
import sys

import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(BASE)
RESULTS_DIR = os.path.join(REPO, "results")

ACCURACY_RE = re.compile(
    r"^(?P<label>[A-Za-z][A-Za-z0-9 /-]*?)\s+Accuracy:\s*(?P<value>[0-9]*\.?[0-9]+)\s*$",
    re.MULTILINE,
)

# script -> [(result key, "Label" prefix of the accuracy line)]
WORKFLOWS = [
    ("marketing_reels.py", [("marketing", "Marketing Random Forest")]),
    ("hr_decision_tree.py", [("hr", "HR Decision Tree")]),
    ("ops_svm_knn.py", [("ops_svm", "Ops SVM"), ("ops_knn", "Ops k-NN")]),
]

DATASETS = [
    ("marketing", "marketing_sample.csv"),
    ("hr", "hr_sample.csv"),
    ("ops", "ops_sample.csv"),
]


def run_script(filename):
    """Run one workflow, returning (stdout, stderr)."""
    path = os.path.join(REPO, "workflows", filename)
    result = subprocess.run(
        [sys.executable, path], capture_output=True, text=True, cwd=REPO
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"{filename} exited with code {result.returncode}\n{result.stderr}"
        )
    return result.stdout, result.stderr


def parse_accuracies(output):
    """Map every '<label> Accuracy: <float>' line in the output to a float."""
    return {
        match.group("label"): float(match.group("value"))
        for match in ACCURACY_RE.finditer(output)
    }


def extract_report(output, label):
    """Return the text block that follows a given accuracy line."""
    matches = list(ACCURACY_RE.finditer(output))
    for index, match in enumerate(matches):
        if match.group("label") != label:
            continue
        end = matches[index + 1].start() if index + 1 < len(matches) else len(output)
        return output[match.end():end].strip()
    return ""


def dataset_sizes():
    sizes = {}
    for key, filename in DATASETS:
        path = os.path.join(REPO, "data", filename)
        sizes[key] = int(len(pd.read_csv(path)))
    return sizes


def main():
    results = {}
    sizes = dataset_sizes()

    for filename, models in WORKFLOWS:
        print(f"Running workflows/{filename}...")
        output, warnings = run_script(filename)
        print(output)
        if warnings.strip():
            print("[stderr from workflow — not parsed]")
            print(warnings)
        accuracies = parse_accuracies(output)
        for key, label in models:
            if label not in accuracies:
                raise RuntimeError(f"Could not parse '{label} Accuracy' from {filename}")
            results[key] = {
                "accuracy": accuracies[label],
                "report": extract_report(output, label),
            }

    results["datasets"] = {key: {"rows": sizes[key]} for key in sizes}

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(os.path.join(RESULTS_DIR, "metrics.json"), "w", encoding="utf-8") as handle:
        json.dump(results, handle, indent=2)
        handle.write("\n")

    summary_lines = []
    for key, value in results.items():
        if key == "datasets":
            continue
        summary_lines.append(f"{key}: accuracy = {value['accuracy']:.2f}")
        if value["report"]:
            summary_lines.append(value["report"])
            summary_lines.append("")
    with open(os.path.join(RESULTS_DIR, "summary.txt"), "w", encoding="utf-8") as handle:
        handle.write("\n".join(summary_lines))

    print("Metrics saved to results/")


if __name__ == "__main__":
    main()
