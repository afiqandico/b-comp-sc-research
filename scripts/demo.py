# scripts/demo.py
# Runs the three workflow scripts and prints results.
# Also saves metrics to results/ folder.

import subprocess
import sys
import os
import json
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

def run_script_and_capture(script_path):
    print(f'Running {script_path}...')
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
    if result.returncode != 0:
        print(f'Error running {script_path}:')
        print(result.stderr)
        return None
    else:
        print(result.stdout)
        return result.stdout

def extract_accuracy_and_report(output, model_name):
    # Parse output to get accuracy and report
    lines = output.split('\n')
    acc_line = [l for l in lines if f'{model_name} Accuracy:' in l]
    if acc_line:
        acc = float(acc_line[0].split(':')[1].strip())
    else:
        acc = None
    # Find classification report lines (simplistic: look for 'precision' line)
    report_lines = []
    capture = False
    for l in lines:
        if 'precision' in l and 'recall' in l and 'f1-score' in l:
            capture = True
        if capture:
            report_lines.append(l)
            if len(report_lines) > 10:  # stop after a few lines
                break
    report = '\n'.join(report_lines) if report_lines else ''
    return acc, report

if __name__ == '__main__':
    base = os.path.dirname(os.path.abspath(__file__))
    workflows = [
        ('Marketing Random Forest', os.path.join(base, '../workflows/marketing_reels.py')),
        ('HR Decision Tree', os.path.join(base, '../workflows/hr_decision_tree.py')),
        ('Ops SVM', os.path.join(base, '../workflows/ops_svm_knn.py')),
        ('Ops k-NN', os.path.join(base, '../workflows/ops_svm_knn.py'))  # same file prints both
    ]
    results = {}
    for name, script in workflows:
        out = run_script_and_capture(script)
        if out is None:
            continue
        # Determine model name for extraction
        if 'Marketing' in name:
            acc, report = extract_accuracy_and_report(out, 'Marketing Random Forest')
            results['marketing'] = {'accuracy': acc, 'report': report}
        elif 'HR' in name:
            acc, report = extract_accuracy_and_report(out, 'HR Decision Tree')
            results['hr'] = {'accuracy': acc, 'report': report}
        elif 'SVM' in name:
            acc, report = extract_accuracy_and_report(out, 'Ops SVM')
            results['ops_svm'] = {'accuracy': acc, 'report': report}
        elif 'k-NN' in name:
            acc, report = extract_accuracy_and_report(out, 'Ops k-NN')
            results['ops_knn'] = {'accuracy': acc, 'report': report}
    # Save results
    os.makedirs(os.path.join(base, '../results'), exist_ok=True)
    with open(os.path.join(base, '../results/metrics.json'), 'w') as f:
        json.dump(results, f, indent=2)
    # Also create a simple summary text file
    summary_lines = []
    for key, val in results.items():
        summary_lines.append(f"{key}: accuracy = {val['accuracy']}")
        if val['report']:
            summary_lines.append(val['report'])
            summary_lines.append('')
    with open(os.path.join(base, '../results/summary.txt'), 'w') as f:
        f.write('\n'.join(summary_lines))
    print('Metrics saved to results/')