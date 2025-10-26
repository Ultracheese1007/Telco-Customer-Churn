"""
preprocess.py
-------------
Data preprocessing module for the Telco Customer Churn project.

This module handles:
1. Loading raw data
2. Cleaning and type conversion
3. Feature encoding
4. Processed data saving & reloading for modeling
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from typing import List, Tuple


# ============================================================
# 1. Load raw data
# ============================================================
def load_data(path: str) -> pd.DataFrame:
    """
    Load the raw Telco Customer Churn dataset from CSV.

    Args:
        path (str): Path to the raw CSV file.

    Returns:
        pd.DataFrame: Raw dataset.
    """
    data = pd.read_csv(path)
    print(f"✅ Data loaded successfully from {path}. Shape: {data.shape}")
    return data


# ============================================================
# 2. Data cleaning
# ============================================================
def clean_total_charges(data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and convert the 'TotalCharges' column:
    - Detect rows with blank or invalid values
    - Replace them with the previous valid record
    - Convert the column to float

    Args:
        data (pd.DataFrame): Input dataset.

    Returns:
        pd.DataFrame: Dataset with cleaned 'TotalCharges' column.
    """
    if "TotalCharges" not in data.columns:
        raise KeyError("❌ 'TotalCharges' column not found in dataset.")

    # Identify invalid entries (blank or whitespace)
    invalid_mask = data["TotalCharges"].str.strip() == ""
    invalid_count = invalid_mask.sum()

    if invalid_count > 0:
        print(f"⚠️ Found {invalid_count} invalid 'TotalCharges' rows. Replacing with previous valid values...")
        data.loc[invalid_mask, "TotalCharges"] = None
        data["TotalCharges"] = data["TotalCharges"].fillna(method="ffill")

    # Convert to numeric
    data["TotalCharges"] = data["TotalCharges"].astype(float)
    print("🧹 'TotalCharges' column cleaned and converted to float.")
    return data


# ============================================================
# 3. Drop unnecessary columns
# ============================================================
def drop_unnecessary_columns(data: pd.DataFrame, cols_to_drop: List[str] = None) -> pd.DataFrame:
    """
    Drop irrelevant or leakage-prone columns (e.g., 'customerID').

    Args:
        data (pd.DataFrame): Input dataset.
        cols_to_drop (List[str], optional): Columns to drop. Defaults to ['customerID'].

    Returns:
        pd.DataFrame: Dataset without the specified columns.
    """
    if cols_to_drop is None:
        cols_to_drop = ["customerID"]

    data = data.drop(columns=cols_to_drop, errors="ignore")
    print(f"🗑️ Dropped columns: {cols_to_drop}")
    return data


# ============================================================
# 4. Encode categorical features
# ============================================================
def encode_categorical_features(data: pd.DataFrame) -> pd.DataFrame:
    """
    Apply label encoding to categorical (non-numeric) columns.

    Args:
        data (pd.DataFrame): Cleaned dataset.

    Returns:
        pd.DataFrame: Encoded dataset with numeric values.
    """
    df = data.copy()
    le = LabelEncoder()

    numeric_cols = data.select_dtypes(include=["number"]).columns
    categorical_cols = [col for col in data.columns if col not in numeric_cols]

    print(f"🔤 Encoding {len(categorical_cols)} categorical features...")
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col].astype(str))
    print("✅ Categorical encoding completed.")
    return df


# ============================================================
# 5. Save processed data
# ============================================================
def save_processed_data(df: pd.DataFrame, path: str) -> None:
    """
    Save the processed dataset to a CSV file.

    Args:
        df (pd.DataFrame): Processed dataset.
        path (str): Output file path.
    """
    df.to_csv(path, index=False)
    print(f"💾 Processed data saved to: {path}")


# ============================================================
# 6. Reload processed data for modeling
# ============================================================
def load_processed_data(path: str) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Load processed dataset and split it into features (X) and target (y).

    Args:
        path (str): Path to the processed CSV file.

    Returns:
        Tuple[pd.DataFrame, pd.Series]: (X, y) feature matrix and target vector.
    """
    df = pd.read_csv(path)

    if "Churn" not in df.columns:
        raise ValueError("❌ 'Churn' column not found in processed dataset.")

    X = df.drop(columns=["Churn"])
    y = df["Churn"]

    print(f"📦 Processed data loaded. Samples: {X.shape[0]}, Features: {X.shape[1]}")
    return X, y
