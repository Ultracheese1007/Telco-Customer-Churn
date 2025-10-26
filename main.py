# main.py
"""
main.py
--------
Entry point for the Telco Customer Churn Analysis pipeline.

This script orchestrates the full data processing workflow:
1. Environment setup
2. Data loading and preprocessing
3. Feature encoding and saving
4. Exploratory Data Analysis (EDA)
"""

# === 1. Import required project modules ===
from src.utils import setup_environment, configure_chinese_fonts, set_color_palette
from src.preprocess import (
    load_data,
    clean_total_charges,
    drop_unnecessary_columns,
    encode_categorical_features,
    save_processed_data,
)
from src.eda import (
    plot_overview,
    plot_categorical_features,
    plot_numerical_features,
    plot_correlations,
)

# === 2. Initialize environment ===
setup_environment()
configure_chinese_fonts()
colors = set_color_palette()

# === 3. Define file paths ===
RAW_DATA_PATH = "data/raw/Telco-Customer-Churn.csv"
PROCESSED_DATA_PATH = "data/processed/telco_processed.csv"

# === 4. Data Loading and Preprocessing ===
print("\n🚀 Starting data preprocessing pipeline...")

data = load_data(RAW_DATA_PATH)
data = clean_total_charges(data)
data = drop_unnecessary_columns(data)
df_encoded = encode_categorical_features(data)
save_processed_data(df_encoded, PROCESSED_DATA_PATH)

print("✅ Data preprocessing completed successfully!")

# === 5. Exploratory Data Analysis (EDA) ===
print("\n📊 Starting Exploratory Data Analysis...")

print("\n▶️ EDA Step 1: Overview")
plot_overview(df_encoded, colors)

print("\n▶️ EDA Step 2: Categorical Feature Analysis")
plot_categorical_features(df_encoded, colors)

print("\n▶️ EDA Step 3: Numerical Feature Analysis")
plot_numerical_features(df_encoded, colors)

print("\n▶️ EDA Step 4: Correlation Analysis")
plot_correlations(df_encoded, colors)

print("\n🎯 Pipeline execution completed successfully!")
