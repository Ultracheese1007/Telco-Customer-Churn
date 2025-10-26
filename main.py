"""
main.py
--------
Telco Customer Churn Analysis — Full Pipeline Orchestration.

This script controls the complete data science workflow:
1. Environment setup
2. Data loading and preprocessing
3. Exploratory Data Analysis (EDA)
4. Model training (Random Forest & XGBoost)
5. Model evaluation and saving artifacts

Author: Xinmei Ma (Leah)
"""

# === 1. Imports ===
import os
import joblib
from src.utils import setup_environment, configure_chinese_fonts, set_color_palette
from src.preprocess import (
    load_data,
    clean_total_charges,
    drop_unnecessary_columns,
    encode_categorical_features,
    save_processed_data,
    load_processed_data,
)
from src.eda import (
    plot_overview,
    plot_categorical_features,
    plot_numerical_features,
    plot_correlations,
)
from src.model_train import train_baseline_rf, train_xgboost_tuned
from src.model_eval import evaluate_model


# === 2. Global configuration ===
RAW_DATA_PATH = "data/raw/Telco-Customer-Churn.csv"
PROCESSED_DATA_PATH = "data/processed/telco_processed.csv"
RF_MODEL_PATH = "models/baseline_rf.pkl"
XGB_MODEL_PATH = "models/xgboost_tuned.pkl"


# === 3. Main workflow ===
def main():
    print("\n🚀 Starting Telco Customer Churn Full Pipeline...\n")

    # ---------- Step 1: Environment Setup ----------
    print("🧩 Step 1 — Setting up environment...")
    setup_environment()
    configure_chinese_fonts()
    colors = set_color_palette()
    print("✅ Environment configured.\n")

    # ---------- Step 2: Data Preprocessing ----------
    print("🧹 Step 2 — Loading and cleaning data...")
    data = load_data(RAW_DATA_PATH)
    data = clean_total_charges(data)
    data = drop_unnecessary_columns(data)
    df_encoded = encode_categorical_features(data)
    save_processed_data(df_encoded, PROCESSED_DATA_PATH)
    print(f"✅ Data preprocessing completed! Saved to {PROCESSED_DATA_PATH}\n")

    # ---------- Step 3: Exploratory Data Analysis ----------
    print("📊 Step 3 — Running Exploratory Data Analysis (EDA)...")
    plot_overview(df_encoded, colors)
    plot_categorical_features(df_encoded, colors)
    plot_numerical_features(df_encoded, colors)
    plot_correlations(df_encoded, colors)
    print("✅ EDA completed. Results available in reports/eda_results/\n")

    # ---------- Step 4a: Random Forest Model ----------
    print("🌲 Step 4a — Training baseline Random Forest model...")
    f1, t1 = load_processed_data(PROCESSED_DATA_PATH)
    rf_model, (x_train, x_test, y_train, y_test) = train_baseline_rf(f1, t1)
    joblib.dump(rf_model, RF_MODEL_PATH)
    print(f"✅ RandomForest saved to {RF_MODEL_PATH}\n")

    print("📈 Evaluating Random Forest...")
    rf_metrics = evaluate_model(rf_model, x_test, y_test, model_name="RandomForest")

    # ---------- Step 4b: XGBoost Model ----------
    print("\n⚡ Step 4b — Training tuned XGBoost model...")
    xgb_model, (x_train, x_test, y_train, y_test) = train_xgboost_tuned(f1, t1)
    joblib.dump(xgb_model, XGB_MODEL_PATH)
    print(f"✅ XGBoost model saved to {XGB_MODEL_PATH}\n")

    print("📈 Evaluating XGBoost...")
    xgb_metrics = evaluate_model(xgb_model, x_test, y_test, model_name="XGBoost")

    # ---------- Step 5: Model Comparison ----------
    print("\n📊 Step 5 — Comparing model performance...")
    print(f"RandomForest  | ROC AUC: {rf_metrics['roc_auc']:.3f} | PR AUC: {rf_metrics['pr_auc']:.3f} | Acc: {rf_metrics['accuracy']:.3f}")
    print(f"XGBoost       | ROC AUC: {xgb_metrics['roc_auc']:.3f} | PR AUC: {xgb_metrics['pr_auc']:.3f} | Acc: {xgb_metrics['accuracy']:.3f}")

    if xgb_metrics['roc_auc'] > rf_metrics['roc_auc']:
        print("\n🏆 XGBoost outperformed RandomForest — saving as final model.")
        joblib.dump(xgb_model, "models/final_model.pkl")
    else:
        print("\n🏆 RandomForest remains best — saving as final model.")
        joblib.dump(rf_model, "models/final_model.pkl")

    print("\n🎯 All pipeline stages executed successfully! Artifacts stored under /models and /reports.\n")


# === 4. Entry point ===
if __name__ == "__main__":
    main()
