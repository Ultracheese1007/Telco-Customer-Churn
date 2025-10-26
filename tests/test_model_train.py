# tests/test_model_train.py
from src import model_train

def test_train_model(tmp_path, sample_data):
    """Test model training produces a model file"""
    model_path = tmp_path / "test_model.pkl"
    model = model_train.train_model(sample_data, output_path=model_path)
    assert model is not None
    assert model_path.exists()
