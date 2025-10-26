# src/app/components/charts.py
"""
📊 Charts Component for Telco Customer Churn Dashboard
-------------------------------------------------------
This module automatically loads and displays all EDA result images
from the reports/eda_results folder, ensuring compatibility both
locally and inside Docker containers.
"""

import streamlit as st
from pathlib import Path


def display_eda_charts():
    """
    Automatically load and display all EDA result images 
    from /app/reports/eda_results (in Docker) or reports/eda_results (locally).
    """

    # --- Determine base directory ---
    # When running in Docker, /app is the WORKDIR
    possible_paths = [
        Path("/app/reports/eda_results"),   # Docker path
        Path("reports/eda_results")         # Local dev path
    ]

    # Choose the first existing directory
    eda_dir = next((p for p in possible_paths if p.exists()), None)

    if not eda_dir:
        st.error("❌ EDA results folder not found. Expected at /app/reports/eda_results or reports/eda_results.")
        return

    # --- Find and display all .png images ---
    img_files = sorted(eda_dir.glob("*.png"))
    if not img_files:
        st.warning("⚠️ No EDA plots found in reports/eda_results.")
        return

    st.markdown("### 🔍 Exploratory Data Analysis Results")

    for img_path in img_files:
        # Generate readable caption from file name
        caption = img_path.stem.replace("_", " ").title()
        st.image(str(img_path), caption=caption, use_container_width=True)
