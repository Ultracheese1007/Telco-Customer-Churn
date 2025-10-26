# src/eda/correlation_analysis.py
"""
Correlation analysis — correlation heatmap and feature relationships.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from src.eda.utils_eda import save_fig


def plot_correlations(df: pd.DataFrame, colors: list, save_path: str = "reports/eda_results/"):
    """
    Plot correlation matrix for numerical features.
    """
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr, cmap="coolwarm", annot=False, linewidths=0.3, ax=ax)
    ax.set_title("Feature Correlation Matrix")
    plt.tight_layout()
    save_fig(fig, save_path, "correlation_heatmap.png")
    plt.close(fig)
