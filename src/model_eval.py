# src/model_eval.py
"""
Model Evaluation Utilities
--------------------------
This module evaluates trained models using metrics and visualization.
"""

import os
import joblib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import (
    classification_report,
    roc_auc_score,
    roc_curve,
    precision_recall_curve,
    average_precision_score,
    accuracy_score
)
from src.utils import ensure_dir


def evaluate_model(model, X_test, y_test, model_name="model"):
    """
    Evaluate a trained model on test data and save metrics & plots.

    Args:
        model: Trained model object.
        X_test (pd.DataFrame): Test features.
        y_test (pd.Series): True labels.
        model_name (str): Name of the model for saving reports.

    Returns:
        dict: Evaluation metrics (accuracy, roc_auc, pr_auc)
    """

    ensure_dir("reports/model_eval")

    # --- Predict ---
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    # --- Compute Metrics ---
    roc_auc = roc_auc_score(y_test, y_prob)
    pr_auc = average_precision_score(y_test, y_prob)
    acc = accuracy_score(y_test, y_pred)

    print(f"\n=== {model_name} — Classification Report ===")
    print(classification_report(y_test, y_pred))

    # --- Save report ---
    report_path = f"reports/model_eval/{model_name}_report.txt"
    with open(report_path, "w") as f:
        f.write(f"=== {model_name} — Classification Report ===\n\n")
        f.write(classification_report(y_test, y_pred))
        f.write(f"\nROC AUC: {roc_auc:.3f}\nPR AUC: {pr_auc:.3f}\nAccuracy: {acc:.3f}\n")

    # --- ROC Curve ---
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    plt.figure(figsize=(6, 5))
    plt.plot(fpr, tpr, label=f"{model_name} (AUC={roc_auc:.3f})")
    plt.plot([0, 1], [0, 1], "--", color="gray")
    plt.title(f"ROC Curve — {model_name}")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend()
    plt.grid(alpha=0.3)
    roc_path = f"reports/model_eval/{model_name}_roc.png"
    plt.savefig(roc_path, dpi=120, bbox_inches="tight")
    plt.close()
    print(f"✅ Saved ROC Curve: {roc_path}")

    # --- Precision-Recall Curve ---
    prec, recall, _ = precision_recall_curve(y_test, y_prob)
    plt.figure(figsize=(6, 5))
    plt.plot(recall, prec, label=f"{model_name} (PR AUC={pr_auc:.3f})")
    plt.title(f"Precision-Recall Curve — {model_name}")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.legend()
    plt.grid(alpha=0.3)
    pr_path = f"reports/model_eval/{model_name}_pr.png"
    plt.savefig(pr_path, dpi=120, bbox_inches="tight")
    plt.close()
    print(f"✅ Saved PR Curve: {pr_path}")

    print(f"✅ {model_name} evaluation completed.\n")

    return {
        "accuracy": acc,
        "roc_auc": roc_auc,
        "pr_auc": pr_auc
    }
