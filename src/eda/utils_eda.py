# src/eda/utils_eda.py
"""
Utility functions for EDA visualizations.
"""

import os

def save_fig(fig, save_dir, filename):
    """
    Save a Matplotlib figure to the given directory.
    """
    os.makedirs(save_dir, exist_ok=True)
    path = os.path.join(save_dir, filename)
    fig.savefig(path, bbox_inches="tight")
    print(f"✅ Saved figure: {path}")
