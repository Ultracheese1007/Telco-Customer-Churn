# src/api/routers/data_preview.py
"""
Data Preview Router
-------------------
Returns first few rows of processed dataset for verification.
"""

from fastapi import APIRouter, HTTPException
import pandas as pd
import os

router = APIRouter(tags=["Data Preview"])
DATA_PATH = "data/processed/telco_processed.csv"

@router.get("/data-preview")
def data_preview(n: int = 5):
    """Preview first n rows of the processed dataset."""
    if not os.path.exists(DATA_PATH):
        raise HTTPException(status_code=404, detail="Processed data not found.")
    df = pd.read_csv(DATA_PATH)
    return df.head(n).to_dict(orient="records")
