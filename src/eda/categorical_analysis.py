# src/eda/categorical_analysis.py
"""
Categorical analysis — visualizes churn distribution across categorical features.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from src.eda.utils_eda import save_fig


def plot_categorical_features(df: pd.DataFrame, colors: list, save_path: str = "reports/eda_results/"):
    """
    Plot churn distributions across categorical features (e.g., gender, contract type).
    """
    categorical_features = [c for c in df.columns if df[c].dtype == "object" or df[c].nunique() <= 6]
    if "Churn" in categorical_features:
        categorical_features.remove("Churn")

    fig, axs = plt.subplots(2, 2, figsize=(16, 10))
    axs = axs.flatten()
    for i, feature in enumerate(categorical_features[:4]):
        sns.countplot(x=feature, data=df, hue="Churn", palette=colors, edgecolor="black", ax=axs[i])
        axs[i].set_title(f"{feature} vs Churn", fontsize=11)
        axs[i].tick_params(axis="x", rotation=30)
    plt.tight_layout()
    save_fig(fig, save_path, "categorical_overview.png")
    plt.close(fig)
