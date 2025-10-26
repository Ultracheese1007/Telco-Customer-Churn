# src/app/components/charts.py
import streamlit as st
import os

def display_eda_charts():
    """Display key EDA images from the reports directory."""
    eda_dir = "reports/eda_results"

    charts = {
        "Customer Churn Overview": "overview_churn_pie.png",
        "Gender vs Churn": "categorical_gender_vs_churn.png",
        "Total Charges Distribution": "numerical_totalcharges_box.png",
        "Feature Correlation Heatmap": "correlation_heatmap.png"
    }

    for title, filename in charts.items():
        file_path = os.path.join(eda_dir, filename)
        if os.path.exists(file_path):
            st.image(file_path, caption=title, use_container_width=True)
        else:
            st.warning(f"⚠️ Missing: {filename}")
