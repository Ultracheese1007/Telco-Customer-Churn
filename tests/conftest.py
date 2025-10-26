# tests/conftest.py
import pytest
import pandas as pd
from pathlib import Path

@pytest.fixture
def sample_data():
    """Fixture: load a small sample dataset for testing."""
    data_path = Path("data/raw/Telco-Customer-Churn.csv")
    if data_path.exists():
        df = pd.read_csv(data_path)
        return df.sample(10, random_state=42)
    else:
        # fallback for CI/CD environments without data
        return pd.DataFrame({
            "gender": ["Male", "Female"] * 5,
            "SeniorCitizen": [0, 1] * 5,
            "Partner": ["Yes", "No"] * 5,
            "Dependents": ["No", "Yes"] * 5,
            "tenure": range(10),
            "MonthlyCharges": [50.0 + i for i in range(10)],
            "TotalCharges": [500.0 + i * 10 for i in range(10)]
        })
