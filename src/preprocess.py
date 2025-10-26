# src/preprocess.py
"""
preprocess.py
-------------
This module handles data loading, cleaning, and feature encoding
for the Telco Customer Churn dataset.
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder


def load_data(path: str) -> pd.DataFrame:
    """
    Load raw dataset from a CSV file.

    Args:
        path (str): Path to the raw CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    data = pd.read_csv(path)
    print(f"✅ Data loaded successfully. Shape: {data.shape}")
    return data


def clean_total_charges(data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and convert the 'TotalCharges' column:
    - Detects rows containing blank or whitespace values.
    - Replaces them with the previous valid entry.
    - Converts the column to float type.

    Args:
        data (pd.DataFrame): Input raw dataset.

    Returns:
        pd.DataFrame: Dataset with cleaned 'TotalCharges' column.
    """
    l1 = [len(i.split()) for i in data['TotalCharges']]
    invalid_indices = [i for i in range(len(l1)) if l1[i] != 1]

    if invalid_indices:
        print(f"⚠️ Found {len(invalid_indices)} invalid TotalCharges rows. Fixing...")
        for i in invalid_indices:
            data.loc[i, 'TotalCharges'] = data.loc[i - 1, 'TotalCharges']

    data['TotalCharges'] = data['TotalCharges'].astype(float)
    print("🧹 'TotalCharges' column cleaned and converted to float.")
    return data


def drop_unnecessary_columns(data: pd.DataFrame, cols_to_drop: list = None) -> pd.DataFrame:
    """
    Drop irrelevant or leakage-prone columns such as 'customerID'.

    Args:
        data (pd.DataFrame): Input dataset.
        cols_to_drop (list, optional): List of column names to drop. Defaults to ['customerID'].

    Returns:
        pd.DataFrame: Dataset without the specified columns.
    """
    if cols_to_drop is None:
        cols_to_drop = ['customerID']
    data = data.drop(columns=cols_to_drop, errors='ignore')
    print(f"🗑️ Dropped columns: {cols_to_drop}")
    return data


def encode_categorical_features(data: pd.DataFrame) -> pd.DataFrame:
    """
    Apply Label Encoding to categorical (non-numeric) columns.

    Args:
        data (pd.DataFrame): Cleaned dataset.

    Returns:
        pd.DataFrame: Encoded dataset with numeric values.
    """
    df = data.copy(deep=True)
    le = LabelEncoder()
    numeric_cols = list(data.describe().columns)
    categorical_cols = [col for col in data.columns if col not in numeric_cols]

    print(f"🔤 Encoding {len(categorical_cols)} categorical features...")
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])
    print("✅ Categorical encoding completed.")
    return df


def save_processed_data(df: pd.DataFrame, path: str):
    """
    Save processed dataset to a CSV file.

    Args:
        df (pd.DataFrame): Processed dataset.
        path (str): Output file path.
    """
    df.to_csv(path, index=False)
    print(f"💾 Processed data saved to: {path}")
