# test_eda_run.py
"""
Quick test runner for the EDA module.
Runs all visualization steps and saves results under reports/eda_results/.
"""

import pandas as pd
from src.utils import setup_environment, set_color_palette, configure_chinese_fonts
from src.eda import (
    plot_overview,
    plot_categorical_features,
    plot_numerical_features,
    plot_correlations,
    generate_eda_report
)

# === 1. Environment setup ===
setup_environment()
configure_chinese_fonts()
colors = set_color_palette()

# === 2. Load processed data ===
df = pd.read_csv("data/processed/telco_processed.csv")

# === 3. Run EDA modules ===
print("🚀 Running EDA modules...\n")

cat_features, num_features = plot_overview(df, colors)
plot_categorical_features(df, colors)
plot_numerical_features(df, colors)
plot_correlations(df, colors)

# === 4. Generate HTML summary ===
generate_eda_report()

print("\n🎯 EDA completed successfully! Check results in reports/eda_results/")
