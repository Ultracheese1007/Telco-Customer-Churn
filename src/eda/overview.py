# src/eda/overview.py
"""
Overview module for basic dataset insights and churn rate visualization.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.eda.utils_eda import save_fig


def plot_overview(df: pd.DataFrame, colors: list, save_path: str = "reports/eda_results/"):
    """
    Plot general churn distribution and print feature types.
    """
    # Identify categorical vs numerical
    cols = list(df.columns)
    categorical_features = [c for c in cols if len(df[c].unique()) <= 6]
    numerical_features = [c for c in cols if len(df[c].unique()) > 6]
    print("Categorical Features:", *categorical_features)
    print("Numerical Features:", *numerical_features)

    churn_rates = df["Churn"].value_counts(normalize=True) * 100
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))

    axs[0].pie(
        churn_rates,
        labels=["Not-Churn", "Churn"],
        autopct="%1.1f%%",
        startangle=90,
        explode=(0.1, 0),
        colors=colors,
        wedgeprops={"edgecolor": "black", "linewidth": 1},
    )
    axs[0].set_title("Churn Rate (%)")

    ax = sns.countplot(x="Churn", data=df, palette=colors, edgecolor="black", ax=axs[1])
    for rect in ax.patches:
        ax.text(rect.get_x() + rect.get_width() / 2, rect.get_height() + 2,
                f"{int(rect.get_height())}", ha="center", fontsize=10)
    ax.set_xticklabels(["Not-Churn", "Churn"])
    axs[1].set_title("Customer Counts")

    plt.tight_layout()
    save_fig(fig, save_path, "overview_churn_distribution.png")
    plt.close(fig)
    return categorical_features, numerical_features
