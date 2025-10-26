# src/api/routers/predict.py
"""
Predict Router
--------------
Defines the /api/predict endpoint for churn probability prediction.
"""

from fastapi import APIRouter, HTTPException
from src.api.schemas.churn_schema import CustomerFeatures, PredictionResult
from src.api.services.churn_service import ChurnModelService

router = APIRouter(tags=["Prediction"])
model_service = ChurnModelService()


@router.post("/predict", response_model=PredictionResult)
def predict_churn(data: CustomerFeatures):
    """
    Predict customer churn based on input features.
    """
    try:
        result = model_service.predict(data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
