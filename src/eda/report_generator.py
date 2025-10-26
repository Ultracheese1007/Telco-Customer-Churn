# src/eda/report_generator.py
"""
EDA Report Generator — combines all EDA plots into one HTML summary.
"""

import os
from datetime import datetime

def generate_eda_report(output_dir="reports/eda_results/"):
    """
    Generate simple HTML report summarizing saved EDA figures.
    """
    images = [f for f in os.listdir(output_dir) if f.endswith(".png")]
    html_path = os.path.join(output_dir, "eda_summary.html")

    with open(html_path, "w", encoding="utf-8") as f:
        f.write("<html><head><title>EDA Summary</title></head><body>")
        f.write(f"<h1>EDA Summary Report</h1><p>Generated: {datetime.now()}</p>")
        for img in images:
            f.write(f"<h3>{img}</h3><img src='{img}' width='600'><hr>")
        f.write("</body></html>")

    print(f"✅ EDA summary saved to {html_path}")
