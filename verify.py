#!/usr/bin/env python3
"""Reproducibility check for the demo pipeline.

Runs scripts/demo.py, parses each accuracy value as a float, and compares it
against the value measured on the committed fixtures (tolerance 0.01). Exits
non-zero if any metric is missing or drifts.

These expectations are NOT the thesis accuracies (94/77/82 %). They are the
values this repository actually produces from data/*.csv, which are tiny
synthetic fixtures. See docs/REPRODUCIBILITY.md.
"""

import os
import re
import subprocess
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
TOLERANCE = 0.01

EXPECTED = [
    ("Marketing Random Forest", 1.00),
    ("HR Decision Tree", 0.33),
    ("Ops SVM", 0.50),
    ("Ops k-NN", 0.50),
]

EXPECTED_ROWS = {"marketing": 10, "hr": 13, "ops": 10}

ACCURACY_RE = re.compile(
    r"^(?P<label>[A-Za-z][A-Za-z0-9 /-]*?)\s+Accuracy:\s*(?P<value>[0-9]*\.?[0-9]+)\s*$",
    re.MULTILINE,
)


def run_demo():
    script = os.path.join(BASE, "scripts", "demo.py")
    result = subprocess.run(
        [sys.executable, script], capture_output=True, text=True, cwd=BASE
    )
    if result.returncode != 0:
        print("Demo failed with exit code", result.returncode)
        print(result.stderr)
        return None
    return result.stdout + result.stderr


def fixture_rows():
    import pandas as pd

    return {
        key: int(len(pd.read_csv(os.path.join(BASE, "data", f"{key}_sample.csv"))))
        for key in EXPECTED_ROWS
    }


def main():
    output = run_demo()
    if output is None:
        print("Verification FAILED")
        return 1

    measured = {
        match.group("label"): float(match.group("value"))
        for match in ACCURACY_RE.finditer(output)
    }

    failures = 0
    width = max(len(label) for label, _ in EXPECTED)

    print(f"Accuracy check (tolerance +/- {TOLERANCE:.2f})")
    print("-" * (width + 34))
    print(f"{'model':<{width}}  {'expected':>8}  {'actual':>6}  {'delta':>6}  result")
    print("-" * (width + 34))
    for label, expected in EXPECTED:
        actual = measured.get(label)
        if actual is None:
            print(f"{label:<{width}}  {expected:>8.2f}  {'MISSING':>6}  {'-':>6}  FAIL")
            failures += 1
            continue
        delta = abs(actual - expected)
        ok = delta <= TOLERANCE
        failures += 0 if ok else 1
        print(
            f"{label:<{width}}  {expected:>8.2f}  {actual:>6.2f}  {delta:>6.2f}  "
            f"{'PASS' if ok else 'FAIL'}"
        )

    print()
    print("Fixture size check (exact row counts)")
    print("-" * (width + 34))
    sizes = fixture_rows()
    for key, expected in EXPECTED_ROWS.items():
        actual = sizes[key]
        ok = actual == expected
        failures += 0 if ok else 1
        name = f"{key}_sample.csv"
        print(
            f"{name:<{width}}  {expected:>8}  {actual:>6}  {'-':>6}  "
            f"{'PASS' if ok else 'FAIL'}"
        )

    print()
    if failures:
        print(f"Verification FAILED ({failures} mismatch(es))")
        return 1
    print("Verification PASSED — demo values match the recorded measurements.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
