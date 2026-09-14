import matplotlib.pyplot as plt
import numpy as np
import os

# Accuracies from the demo (hardcoded for now; could be recomputed)
models = ['Marketing\n(Random Forest)', 'HR\n(Decision Tree)', 'Ops\n(SVM/k-NN)']
accuracies = [0.94, 0.77, 0.82]  # from thesis results

# Create bar chart
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(models, accuracies, color=['#4caf50', '#2196f3', '#ff9800'])
ax.set_ylim(0, 1.0)
ax.set_ylabel('Accuracy')
ax.set_title('Model Accuracies from Thesis Research')
# Add value labels on bars
for bar, acc in zip(bars, accuracies):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.02, f'{acc:.0%}', ha='center', va='bottom')

plt.tight_layout()

# Ensure results directory exists
os.makedirs('results', exist_ok=True)
output_path = os.path.join('results', 'accuracy_bar.png')
plt.savefig(output_path, dpi=150)
print(f'Saved plot to {output_path}')