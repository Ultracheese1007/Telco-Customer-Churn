"""
model_train.py
--------------
Model training module for the Telco Customer Churn project.

This module provides:
1. A lightweight `train_model()` for pytest validation
2. Baseline RandomForest training
3. Tuned RandomForest and XGBoost training with cross-validation
"""

import os
import joblib
import numpy as np
from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
    GridSearchCV,
    RandomizedSearchCV,
    RepeatedStratifiedKFold
)
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from src.utils import ensure_dir


# ============================================================
# 0. Minimal model for test (pytest will call this)
# ============================================================
def train_model(df, output_path=None):
    """
    Train a simple RandomForest model for testing.
    Used by pytest to verify the training pipeline.
    """
    X = df.drop(columns=["Churn"])
    y = df["Churn"].apply(lambda x: 1 if x == "Yes" else 0)

    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X.select_dtypes("number"), y)

    if output_path:
        joblib.dump(model, output_path)
        print(f"✅ Model saved to {output_path}")
    return model


# ============================================================
# 1. Baseline RandomForest
# ============================================================
def train_baseline_rf(x, y, save_path="models/baseline_rf.pkl"):
    """
    Train a baseline Random Forest model with cross-validation.
    Returns model and (x_train, x_test, y_train, y_test)
    """
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42, stratify=y
    )

    clf = RandomForestClassifier(
        n_estimators=300,
        random_state=42,
        n_jobs=-1,
        class_weight="balanced"
    )

    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    cv_auc = cross_val_score(clf, x_train, y_train, cv=cv, scoring="roc_auc").mean()
    print(f"[CV] ROC AUC: {cv_auc:.3f}")

    clf.fit(x_train, y_train)
    ensure_dir("models")
    joblib.dump(clf, save_path)
    print(f"✅ Baseline RandomForest saved to {save_path}")

    return clf, (x_train, x_test, y_train, y_test)


# ============================================================
# 2. Tuned XGBoost
# ============================================================
def train_xgboost_tuned(x, y, save_path="models/best_xgb.pkl"):
    """
    Perform grid search tuning for XGBoost.
    Returns best model and (x_train, x_test, y_train, y_test)
    """
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42, stratify=y
    )

    param_grid = {
        "learning_rate": [0.01, 0.1, 0.2],
        "max_depth": [3, 4, 5],
        "n_estimators": [100, 500, 1000],
        "subsample": [0.8, 1.0],
        "colsample_bytree": [0.8, 1.0],
    }

    model = XGBClassifier(
        use_label_encoder=False,
        eval_metric="logloss",
        random_state=42,
        n_jobs=-1
    )

    grid = GridSearchCV(
        model,
        param_grid=param_grid,
        scoring="roc_auc",
        cv=3,
        verbose=2,
        n_jobs=-1
    )
    grid.fit(x_train, y_train)

    print(f"🎯 Best XGB Params: {grid.best_params_}")
    best_model = grid.best_estimator_

    ensure_dir("models")
    joblib.dump(best_model, save_path)
    print(f"✅ Tuned XGBoost saved to {save_path}")

    return best_model, (x_train, x_test, y_train, y_test)


# ============================================================
# 3. Tuned RandomForest
# ============================================================
def train_rf_tuned(x_train, y_train):
    """
    Perform random search tuning for RandomForest.
    Returns best model
    """
    param_dist = {
        "max_depth": [3, 4, 5, 6, 7, 8, 9, 10],
        "n_estimators": [50, 100, 200, 300, 400, 500]
    }

    model = RandomForestClassifier(random_state=42)
    random_search = RandomizedSearchCV(
        model,
        param_distributions=param_dist,
        n_iter=20,
        scoring="roc_auc",
        cv=5,
        random_state=42,
        verbose=1,
        n_jobs=-1
    )
    random_search.fit(x_train, y_train)

    print(f"🎯 Best RF Params: {random_search.best_params_}")
    ensure_dir("models")
    joblib.dump(random_search.best_estimator_, "models/best_rf.pkl")
    print("✅ Tuned RandomForest saved to models/best_rf.pkl")

    return random_search.best_estimator_
