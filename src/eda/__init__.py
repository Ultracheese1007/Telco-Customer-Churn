# src/eda/__init__.py
"""
EDA package initializer.
Defines public functions for importing across modules.
"""

from .overview import plot_overview
from .categorical_analysis import plot_categorical_features
from .numerical_analysis import plot_numerical_features
from .correlation_analysis import plot_correlations
from .report_generator import generate_eda_report

__all__ = [
    "plot_overview",
    "plot_categorical_features",
    "plot_numerical_features",
    "plot_correlations",
    "generate_eda_report"
]
