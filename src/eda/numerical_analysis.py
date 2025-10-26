# src/eda/numerical_analysis.py
"""
Numerical feature analysis module.
Includes distribution plots and boxplots for churn comparison.
Automatically splits results into multiple pages if too many features exist.
"""

import math
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from src.eda.utils_eda import save_fig


def plot_numerical_features(df: pd.DataFrame, colors: list, save_path: str = "reports/eda_results/"):
    """
    Visualize numerical feature distributions and their relationship with churn.
    Automatically paginates output if the number of features exceeds a given limit.

    Args:
        df (pd.DataFrame): The processed Telco dataset.
        colors (list): Color palette for plots.
        save_path (str): Directory path to save figures.

    Returns:
        None. Figures are saved to `reports/eda_results/`.
    """
    numerical_features = [c for c in df.columns if df[c].dtype != "object" and c != "Churn"]
    n_cols = 3           # number of plots per row
    n_per_page = 6       # number of features per page (2 rows × 3 columns)
    total_pages = math.ceil(len(numerical_features) / n_per_page)

    # === Page 1..N: Distribution plots ===
    for page in range(total_pages):
        subset = numerical_features[page * n_per_page : (page + 1) * n_per_page]
        n_rows = math.ceil(len(subset) / n_cols)
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(6 * n_cols, 4 * n_rows))
        axes = axes.flatten()

        for i, feature in enumerate(subset):
            sns.histplot(df[feature], color=colors[0], kde=True, ax=axes[i])
            axes[i].set_title(f"Distribution: {feature}", fontsize=11)
        for j in range(len(subset), len(axes)):
            axes[j].axis("off")

        plt.tight_layout()
        save_fig(fig, save_path, f"numerical_distributions_p{page + 1}.png")
        plt.close(fig)

    # === Page 1..N: Boxplots vs Churn ===
    for page in range(total_pages):
        subset = numerical_features[page * n_per_page : (page + 1) * n_per_page]
        n_rows = math.ceil(len(subset) / n_cols)
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(6 * n_cols, 4 * n_rows))
        axes = axes.flatten()

        for i, feature in enumerate(subset):
            sns.boxplot(x="Churn", y=feature, data=df, palette=colors, ax=axes[i])
            axes[i].set_title(f"{feature} vs Churn", fontsize=11)
        for j in range(len(subset), len(axes)):
            axes[j].axis("off")

        plt.tight_layout()
        save_fig(fig, save_path, f"numerical_boxplots_p{page + 1}.png")
        plt.close(fig)
