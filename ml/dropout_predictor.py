import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

def build_features(df):
    """df: user_id, course_id, done, total, days_inactive, avg_session"""
    df['progress_pct'] = df['done'] / df['total'].clip(lower=1)
    return df[['progress_pct', 'days_inactive', 'avg_session']]

def train(df, target):
    X = build_features(df)
    Xtr, Xte, ytr, yte = train_test_split(X, target, test_size=0.2, random_state=42)
    m = RandomForestClassifier(n_estimators=300, max_depth=8)
    m.fit(Xtr, ytr)
    print("AUC:", roc_auc_score(yte, m.predict_proba(Xte)[:,1]))
    return m

def predict_dropout(model, user_features):
    return model.predict_proba([user_features])[0][1]
