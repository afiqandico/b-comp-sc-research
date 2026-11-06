import pandas as pd
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import os
import numpy as np

def load_ops_data():
    base = os.path.dirname(__file__)
    path = os.path.join(base, '..', 'data', 'ops_sample.csv')
    df = pd.read_csv(path)
    # Feature engineering: price ratio
    df['price_ratio'] = df['unit_price'] / df['market_price']
    X = df[['price_ratio']]  # simple feature for demo
    y = df['efficiency_label'].map({'efficient':0, 'inefficient':1})
    return X, y

def train_and_evaluate():
    X, y = load_ops_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # SVM
    svm = SVC(kernel='linear', random_state=42)
    svm.fit(X_train, y_train)
    y_pred_svm = svm.predict(X_test)
    acc_svm = accuracy_score(y_test, y_pred_svm)
    print(f'Ops SVM Accuracy: {acc_svm:.2f}')
    print(classification_report(y_test, y_pred_svm, target_names=['efficient','inefficient']))
    # k-NN
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    y_pred_knn = knn.predict(X_test)
    acc_knn = accuracy_score(y_test, y_pred_knn)
    print(f'Ops k-NN Accuracy: {acc_knn:.2f}')
    print(classification_report(y_test, y_pred_knn, target_names=['efficient','inefficient']))
    return svm, knn

if __name__ == '__main__':
    train_and_evaluate()