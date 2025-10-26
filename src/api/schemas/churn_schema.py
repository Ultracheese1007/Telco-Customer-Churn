# src/api/schemas/churn_schema.py
"""
Pydantic Schemas
----------------
Defines data validation and serialization models
for API request and response.
"""

from pydantic import BaseModel, Field

class CustomerFeatures(BaseModel):
    gender: int = Field(..., example=1)
    SeniorCitizen: int = Field(..., example=0)
    Partner: int = Field(..., example=1)
    Dependents: int = Field(..., example=0)
    tenure: float = Field(..., example=12)
    PhoneService: int = Field(..., example=1)
    MultipleLines: int = Field(..., example=0)
    InternetService: int = Field(..., example=2)
    OnlineSecurity: int = Field(..., example=1)
    OnlineBackup: int = Field(..., example=0)
    DeviceProtection: int = Field(..., example=1)
    TechSupport: int = Field(..., example=0)
    StreamingTV: int = Field(..., example=1)
    StreamingMovies: int = Field(..., example=0)
    Contract: int = Field(..., example=2)
    PaperlessBilling: int = Field(..., example=1)
    PaymentMethod: int = Field(..., example=3)
    MonthlyCharges: float = Field(..., example=70.35)
    TotalCharges: float = Field(..., example=840.5)

class PredictionResult(BaseModel):
    churn_probability: float
    prediction: str
