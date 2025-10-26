# tests/test_preprocess.py
from src import preprocess

def test_clean_data(sample_data):
    """Check that preprocess.clean_data() outputs a non-empty DataFrame"""
    df_clean = preprocess.clean_data(sample_data)
    assert df_clean is not None
    assert not df_clean.empty
    assert "MonthlyCharges" in df_clean.columns
