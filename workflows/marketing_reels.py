import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import os

def load_marketing_data():
    base = os.path.dirname(__file__)
    path = os.path.join(base, '..', 'data', 'marketing_sample.csv')
    df = pd.read_csv(path)
    # Simple feature: content_type (Reels=1, Post=0)
    df['content_type_num'] = df['content_type'].map({'Reels':1, 'Post':0})
    X = df[['content_type_num']]
    y = df['engagement_label'].map({'High':1, 'Low':0})
    return X, y

def train_and_evaluate():
    X, y = load_marketing_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f'Marketing Random Forest Accuracy: {acc:.2f}')
    print(classification_report(y_test, y_pred, target_names=['Low','High']))
    return rf

if __name__ == '__main__':
    train_and_evaluate()