import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, roc_curve, auc
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import label_binarize

# Ensure docs directory exists
docs_dir = os.path.join(os.path.dirname(__file__), '..', 'docs')
os.makedirs(docs_dir, exist_ok=True)

# Generate synthetic binary classification data for demonstration
X, y = make_classification(n_samples=200, n_features=5, n_informative=3, n_redundant=0, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a simple Random Forest
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
y_proba = clf.predict_proba(X_test)[:, 1]

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots(figsize=(5,4))
im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
ax.figure.colorbar(im, ax=ax)
ax.set(xticks=np.arange(cm.shape[1]),
       yticks=np.arange(cm.shape[0]),
       xticklabels=['Kelas 0', 'Kelas 1'],
       yticklabels=['Kelas 0', 'Kelas 1'],
       ylabel='True label',
       xlabel='Predicted label',
       title='Confusion Matrix (Contoh)')

# Write values in cells
thresh = cm.max() / 2.
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        ax.text(j, i, format(cm[i, j], 'd'),
                ha="center", va="center",
                color="white" if cm[i, j] > thresh else "black")
plt.tight_layout()
conf_path = os.path.join(docs_dir, 'confusion_matrix.png')
plt.savefig(conf_path, dpi=150)
plt.close()

# ROC Curve
fpr, tpr, _ = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)
fig, ax = plt.subplots(figsize=(5,4))
ax.plot(fpr, tpr, color='darkorange',
         lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
ax.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
ax.set_xlim([0.0, 1.0])
ax.set_ylim([0.0, 1.05])
ax.set_xlabel('False Positive Rate')
ax.set_ylabel('True Positive Rate')
ax.set_title('Receiver Operating Characteristic (Contoh)')
ax.legend(loc="lower right")
plt.tight_layout()
roc_path = os.path.join(docs_dir, 'roc_curve.png')
plt.savefig(roc_path, dpi=150)
plt.close()

print(f'Saved confusion matrix to {conf_path}')
print(f'Saved ROC curve to {roc_path}')