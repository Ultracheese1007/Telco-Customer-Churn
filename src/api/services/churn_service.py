# src/api/services/churn_service.py
"""
Churn Model Service
-------------------
Handles model loading and prediction.
"""

import joblib
import numpy as np
import pandas as pd
from src.api.schemas.churn_schema import CustomerFeatures, PredictionResult
from src.utils import ensure_dir

MODEL_PATH = "models/best_xgb.pkl"



class ChurnModelService:
    """Service class for model inference."""

    def __init__(self):
        self.model = self._load_model()

    def _load_model(self):
        """Load trained model from disk."""
        try:
            model = joblib.load(MODEL_PATH)
            print(f"✅ Model loaded successfully from {MODEL_PATH}")
            return model
        except Exception as e:
            raise RuntimeError(f"Failed to load model: {e}")

    def predict(self, features: CustomerFeatures) -> PredictionResult:
        """Perform churn prediction."""
        input_df = pd.DataFrame([features.dict()])
        prob = self.model.predict_proba(input_df)[0, 1]
        prediction = "Churn" if prob >= 0.5 else "No Churn"
        return PredictionResult(churn_probability=round(float(prob), 3), prediction=prediction)
