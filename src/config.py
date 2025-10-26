"""
config.py — Global configuration settings
-----------------------------------------
Centralized configuration for data paths, model parameters,
and API settings to avoid hard-coded values.
"""

import os
from pathlib import Path

# ====== Directory Structure ======
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
MODEL_DIR = BASE_DIR / "models"
REPORT_DIR = BASE_DIR / "reports"

# ====== File Paths ======
RAW_DATA = DATA_DIR / "raw" / "Telco-Customer-Churn.csv"
PROCESSED_DATA = DATA_DIR / "processed" / "cleaned_telco.csv"
MODEL_PATH = MODEL_DIR / "best_xgb.pkl"

# ====== Model Hyperparameters ======
MODEL_PARAMS = {
    "n_estimators": 300,
    "max_depth": 6,
    "learning_rate": 0.1,
    "random_state": 42
}

# ====== API Settings ======
FASTAPI_PORT = 8000
STREAMLIT_PORT = 8501

# ====== Logging ======
LOG_LEVEL = "INFO"
